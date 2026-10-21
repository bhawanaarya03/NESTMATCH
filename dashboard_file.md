# File: `dashboard.html`

**GitHub Link:** [dashboard.html](https://github.com/bhawanaarya03/NESTMATCH/blob/main/dashboard.html)
## Purpose
The `dashboard.html` file displays the user's visit dashboard, where they can view their PG visit requests, check their status, and manage pending requests.

## Contents

- **Page Header:** Displays the title “Your visit diary” and a button to explore more PGs.
- **Visit Reminders:** Shows an in-app reminder when the user has a PG visit scheduled for the current day.
- **Summary Cards:** Displays the total number of visit requests, pending visits, and requests in the FIFO queue.
- **Visit Request List:** Shows details of each request, including PG name, location, preferred visit date, request time, status, and request ID.
- **Cancel Request:** Allows users to cancel pending visit requests after confirming the action.
- **Empty State:** Displays a message and a link to explore PGs when the user has no visit requests.
- **Reminder Information:** Explains how visit reminders work and clarifies that the demo does not send email or SMS notifications.

## Role in NestMatch
This page helps users monitor their visit requests, track their status, view upcoming visits, and cancel pending requests. It uses Flask's Jinja2 template syntax to display dynamic information supplied by the application.

