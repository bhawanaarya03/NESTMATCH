🏡 NestMatch
Smart PG Recommendation System for Students

NestMatch is a web-based application designed to help students find suitable Paying Guest (PG) accommodations based on their location, budget, distance, room type, and required facilities.

📌 Project Overview

Finding a suitable PG accommodation near college can be difficult for students. NestMatch simplifies this process by allowing users to explore and filter PG listings according to their preferences.

✨ Features

- 🔍 Search PG accommodations by location.
- 💰 Filter PGs according to budget.
- 📍 Consider distance from the preferred location.
- 🛏️ Choose PG type and room type.
- 🏠 Explore available facilities.
- 📋 View PG details.
- 📝 Submit visit requests.
- ⏳ Manage visit requests using a FIFO queue.

🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web application framework |
| HTML | Webpage structure |
| CSS | Website styling |
| MySQL | Database management |
| Data Structures | FIFO queue for visit requests |

🗄️ Database Structure

NestMatch uses a MySQL database named `nestmatch`.

1. PG Listings

Stores accommodation information, including title, location, rent, distance, PG type, room type, facilities, rating, and description.

![PG Listings Table](pg_listings.png)

2. Visit Requests

Stores student visit requests, including student details, selected PG, preferred visit date, and request status.

![Visit Requests Table](visit_requests.png)

For more details, see [TABLE_STRUCTURE.md](TABLE_STRUCTURE.md).

⚙️ Installation and Setup

Prerequisites

- Python installed
- MySQL Server installed
- MySQL Workbench (optional)

Steps

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install the required Python packages:

   pip install flask mysql-connector-python


4. Open MySQL Workbench or the MySQL command line.
5. Execute the SQL script in `database.sql` to create the database and tables.
6. Configure the database connection in `app.py` according to your local MySQL username and password.
7. Run the application:

   python app.py
   

8. Open the local URL displayed in the terminal in your browser.

## 📂 Project Files

- `app.py` — Main Flask application.
- `database.sql` — Database and table creation script with sample data.
- `TABLE_STRUCTURE.md` — Database table structure documentation.
- `pg_listings.png` — Screenshot of the PG listings table.
- `visit_requests.png` — Screenshot of the visit requests table.

🎯 Project Objective

The objective of NestMatch is to make PG accommodation searching easier for students by combining preference-based filtering, database management, and queue-based visit request processing.


**Project:** NestMatch  
**Category:** Web Development and Database Management
