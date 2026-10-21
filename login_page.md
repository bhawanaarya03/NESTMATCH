# File: `login.html`

**GitHub Link:** [login.html](https://github.com/bhawanaarya03/NESTMATCH/blob/main/login.html)
## Purpose
The `login.html` file defines the login interface of the NestMatch web application. It allows registered users to enter their email address and password to log in to their accounts.

## Contents

- **Welcome Section:** Displays introductory text explaining the purpose of NestMatch and its PG discovery features.
- **Illustration Panel:** Shows the main heading, a short description, and three steps highlighting the process of searching, comparing, and planning a PG visit.
- **Login Form:** Contains email and password fields for user authentication.
- **Form Validation:** Uses HTML attributes such as `required` and `type="email"` to ensure that the required fields are filled in and the email follows a basic valid format.
- **Login Button:** Submits the entered credentials to Flask's `login` route using the POST method.
- **Registration Link:** Directs new users to the account creation page through the `register` route.
- **Styling and Layout:** Uses CSS classes to arrange the login panel, buttons, text, and decorative elements.
- **Base Template Integration:** Extends `base.html` to reuse the website's common navigation, footer, and overall layout.

## Role in NestMatch
This page provides the user interface for existing users to log in. It collects their credentials and sends them to the Flask backend, where the authentication process is handled.

