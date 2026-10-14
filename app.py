import os
from collections import deque
from datetime import date, datetime
from functools import wraps

import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-development-secret")

DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "nestmatch"),
}

# Demonstration queue: requests are enqueued in arrival order and processed FIFO.
# MySQL remains the durable record; this queue is rebuilt from pending records at startup/use.
visit_queue = deque()

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "info")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

def query_all(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute(sql, params)
        return cur.fetchall()
    finally:
        conn.close()

def query_one(sql, params=()):
    rows = query_all(sql, params)
    return rows[0] if rows else None

def execute(sql, params=()):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()



def refresh_queue():
    """Rebuild the FIFO queue from all currently pending requests."""
    global visit_queue

    rows = query_all(
        """
        SELECT id
        FROM visit_requests
        WHERE status = 'Pending'
        ORDER BY created_at ASC, id ASC
        """
    )

    visit_queue = deque(row["id"] for row in rows)


@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("listings"))
    return render_template("login.html", page_title="Welcome home")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        if not name or not email or len(password) < 8:
            flash("Enter your name and email, and use a password of at least 8 characters.", "error")
            return render_template("register.html")
        try:
            execute(
                "INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)",
                (name, email, generate_password_hash(password))
            )
            user = query_one("SELECT id, name, email FROM users WHERE email = %s", (email,))
            session["user_id"], session["name"], session["email"] = user["id"], user["name"], user["email"]
            flash("Your account is ready. Welcome to NestMatch!", "success")
            return redirect(url_for("listings"))
        except Error as exc:
            if getattr(exc, "errno", None) == 1062:
                flash("An account with that email already exists. Please log in.", "error")
            else:
                app.logger.exception("Registration failed")
                flash("Could not create the account. Check your MySQL setup and try again.", "error")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        try:
            user = query_one("SELECT id, name, email, password_hash FROM users WHERE email = %s", (email,))
        except Error:
            flash("Database connection failed. Follow the setup steps in README.md.", "error")
            return render_template("login.html")
        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"], session["name"], session["email"] = user["id"], user["name"], user["email"]
            return redirect(url_for("listings"))
        flash("Email or password is incorrect.", "error")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

@app.route("/listings")
@login_required
def listings():
    q = request.args.get("q", "").strip()
    area = request.args.get("area", "").strip()
    pg_type = request.args.get("pg_type", "").strip()
    room_type = request.args.get("room_type", "").strip()
    facility = request.args.get("facility", "").strip()
    min_rent = request.args.get("min_rent", "").strip()
    max_rent = request.args.get("max_rent", "").strip()
    sort = request.args.get("sort", "recommended")
    sql = "SELECT * FROM pg_listings WHERE 1=1"
    params = []
    if q:
        sql += " AND (title LIKE %s OR area LIKE %s OR location LIKE %s)"
        params.extend([f"%{q}%"] * 3)
    if area:
        sql += " AND area = %s"; params.append(area)
    if pg_type:
        sql += " AND pg_type = %s"; params.append(pg_type)
    if room_type:
        sql += " AND room_type = %s"; params.append(room_type)
    if facility:
        sql += " AND facilities LIKE %s"; params.append(f"%{facility}%")
    if min_rent.isdigit():
        sql += " AND rent >= %s"; params.append(int(min_rent))
    if max_rent.isdigit():
        sql += " AND rent <= %s"; params.append(int(max_rent))
    order = {"rent_low": "rent ASC", "rent_high": "rent DESC", "rating": "rating DESC"}.get(sort, "featured DESC, rating DESC")
    sql += " ORDER BY " + order
    try:
        pgs = query_all(sql, tuple(params))
        areas = query_all("SELECT DISTINCT area FROM pg_listings ORDER BY area")
    except Error:
        pgs, areas = [], []
        flash("Cannot load PGs. Set up MySQL using database.sql.", "error")
    return render_template("listings.html", pgs=pgs, areas=areas, filters=request.args, now=date.today().isoformat())

@app.route("/visit/<int:pg_id>", methods=["POST"])
@login_required
def request_visit(pg_id):
    pg = query_one("SELECT id, title FROM pg_listings WHERE id = %s", (pg_id,))
    if not pg:
        flash("That PG could not be found.", "error")
        return redirect(url_for("listings"))
    preferred_date = request.form.get("preferred_date", "")
    try:
        visit_date = date.fromisoformat(preferred_date)
        if visit_date < date.today():
            raise ValueError
    except ValueError:
        flash("Choose today or a future date for your visit.", "error")
        return redirect(url_for("listings"))
    try:
        visit_id = execute(
            """INSERT INTO visit_requests (user_id, student_name, email, pg_id, preferred_date, status)
               VALUES (%s, %s, %s, %s, %s, 'Pending')""",
            (session["user_id"], session["name"], session["email"], pg_id, visit_date)
        )
        refresh_queue()
        flash(f"Visit request #{visit_id} for {pg['title']} is queued. Requests are handled FIFO (oldest first).", "success")
    except Error:
        app.logger.exception("Visit request failed")
        flash("Could not save your visit request. Please check the database setup.", "error")
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
@login_required
def dashboard():
    try:
        visits = query_all(
            """SELECT v.*, p.title AS pg_title, p.location AS pg_location
               FROM visit_requests v JOIN pg_listings p ON p.id = v.pg_id
               WHERE v.user_id = %s ORDER BY v.preferred_date ASC, v.created_at DESC""",
            (session["user_id"],)
        )
        # Reminder banner is shown when a visit is today or within the next 24 hours.
        now = datetime.now().date()
        reminders = [v for v in visits if v["status"] != "Cancelled" and v["preferred_date"] == now]
        refresh_queue()
        queue_count = len(visit_queue)
    except Error:
        visits, reminders, queue_count = [], [], 0
        flash("Could not load your dashboard. Check the MySQL connection.", "error")
    return render_template("dashboard.html", visits=visits, reminders=reminders, queue_count=queue_count, today=date.today())

@app.route("/cancel-visit/<int:visit_id>", methods=["POST"])
@login_required
def cancel_visit(visit_id):
    execute(
        "UPDATE visit_requests SET status = 'Cancelled' WHERE id = %s AND user_id = %s AND status = 'Pending'",
        (visit_id, session["user_id"])
    )
    refresh_queue()
    flash("Pending visit request cancelled.", "info")
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)
