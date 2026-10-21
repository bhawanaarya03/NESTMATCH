# File: `register.html`

**GitHub Link:** [register.html](https://github.com/bhawanaarya03/NESTMATCH/blob/main/register.html)
## Purpose
The `register.html` file defines the registration interface of the NestMatch web application. It allows new users to enter their personal details and create an account.

## Contents

- **Welcome Section:** Displays introductory text explaining how users can explore PG accommodations and plan visits.
- **Illustration Panel:** Presents the main heading, a short description, and three steps: setting preferences, finding suitable PGs, and planning visits.
- **Registration Form:** Contains fields for the user's full name, email address, and password.
- **Form Validation:** Uses HTML attributes such as `required`, `type="email"`, and `minlength="8"` to check that required fields are filled in, the email follows a basic valid format, and the password contains at least eight characters.
- **Create Account Button:** Submits the registration form to the Flask backend using the POST method.
- **Login Link:** Directs existing users to the login page through Flask's `login` route.
- **Styling and Layout:** Uses CSS classes to arrange the registration form, buttons, text, and decorative elements.
- **Base Template Integration:** Extends `base.html` to reuse the common website layout, navigation, and footer.

## Role in NestMatch
This page provides the interface for new users to register on NestMatch. It collects their name, email address, and password and submits the information to the Flask backend, where account creation and data processing are handled.
