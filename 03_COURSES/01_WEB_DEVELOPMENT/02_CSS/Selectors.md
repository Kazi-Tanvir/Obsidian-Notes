---
tags:
- css
- selectors
- syntax
---
# Selectors

## What's the Actual Use?
Selectors are used to "find" or select the HTML elements you want to style. They range from simple element names to complex patterns.

## Other Common Use Cases
- Styling all buttons of a certain type (`input[type="submit"]`).
- Selecting an element only when it's a direct child of another (`div > p`).

## Documentation & Code
Common selectors include Universal (`*`), Element, ID (`#`), Class (`.`), and Attribute selectors.

````css
/* Universal selector */
* { margin: 0; }

/* Element selector */
h1 { font-family: sans-serif; }

/* ID selector */
#header { height: 100px; }

/* Class selector */
.card { border: 1px solid black; }

/* Attribute selector */
a[target="_blank"] { color: green; }
````
