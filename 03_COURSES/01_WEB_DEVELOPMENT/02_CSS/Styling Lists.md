---
tags:
- css
- lists
- styling
---
# Styling Lists

## What's the Actual Use?
CSS allows you to customize the appearance of HTML lists, including changing the bullet type, position, or removing them entirely for navigation bars.

## Other Common Use Cases
- Using custom images as list markers.
- Creating horizontal navigation menus.

## Documentation & Code
Key properties: `list-style-type`, `list-style-position`, and `list-style-image`.

````css
/* Remove bullets for navigation */
nav ul {
    list-style: none;
    padding: 0;
}

/* Custom bullet type */
ul.custom {
    list-style-type: square;
    list-style-position: inside;
}
````
