# File: `base.html`

**GitHub Link:** [base.html]([https://github.com/bhawanaarya03/NESTMATCH](https://github.com/bhawanaarya03/NESTMATCH/blob/19cdec96fba5fb0cbb888e7db4d3be5fd6d842c5/base.html))

## Purpose
The `base.html` file defines the common HTML structure and layout of the NestMatch web application. Other HTML templates extend this file to maintain a consistent design across the website.

## Contents

- **HTML Document Structure:** Defines the page's language, character encoding, viewport settings, and browser title.
- **Font Integration:** Imports DM Sans and Playfair Display fonts from Google Fonts.
- **CSS Integration:** Connects the website to `style.css` using Flask's `url_for()` function.
- **Navigation Bar:** Displays the NestMatch logo and navigation links for Explore PGs, My Visits, and Log Out when a user is logged in.
- **User Greeting:** Displays the first name of the logged-in user.
- **Flash Messages:** Displays notifications, such as success or error messages, using Flask's flash-message system.
- **Content Block:** The `{% block content %}` section allows individual page templates to insert their specific content.
- **Footer:** Displays the copyright notice and the tagline, “A little closer to feeling at home.”

## Role in NestMatch
This file acts as the parent template for pages such as `login.html`, `register.html`, `listings.html`, and `dashboard.html`. It reduces repeated code and ensures that the website maintains a consistent layout across different pages.

