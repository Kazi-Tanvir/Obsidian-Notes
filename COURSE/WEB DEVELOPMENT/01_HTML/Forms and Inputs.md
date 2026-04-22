---
tags:
- html
- forms
- inputs
---
# Forms and Inputs

## What's the Actual Use?
Forms allow users to send data to a server. They are essential for logins, registrations, searches, and data entry.

## Other Common Use Cases
- Search bars in the navigation header.
- Contact forms with validation for email and phone numbers.

## Documentation & Code
Forms use the `<form>` tag with `action` and `method`. Common inputs include `text`, `password`, `email`, and `submit`.

````html
<form action="/submit-data" method="POST">
    <label for="username">Username:</label>
    <input type="text" id="username" name="user_name" required>

    <label for="pass">Password:</label>
    <input type="password" id="pass" name="user_password">

    <button type="submit">Login</button>
</form>
````
