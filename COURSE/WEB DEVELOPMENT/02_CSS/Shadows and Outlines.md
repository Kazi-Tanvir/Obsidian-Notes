---
tags:
- css
- design
- effects
---
# Shadows and Outlines

## What's the Actual Use?
Shadows add depth and "lift" to elements, while outlines provide a visible border that doesn't take up space in the box model, often used for accessibility.

## Other Common Use Cases
- Creating "Floating" cards with `box-shadow`.
- Highlighting focused elements for keyboard navigation with `outline`.

## Documentation & Code
- `box-shadow`: x-offset, y-offset, blur, spread, color.
- `outline`: width, style, color (drawn outside the border).

````css
.card {
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

button:focus {
    outline: 2px solid blue;
    outline-offset: 4px;
}
````
