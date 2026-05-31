---
tags:
- css
- animation
- transitions
---
# Transitions

## What's the Actual Use?
Transitions allow you to change property values smoothly (from one state to another) over a given duration, rather than the change happening instantly.

## Other Common Use Cases
- Making button color changes smooth on hover.
- Animating the width of a search bar when it gains focus.

## Documentation & Code
Requires four values: `property`, `duration`, `timing-function`, and `delay`.

````css
.button {
    background-color: blue;
    transition: background-color 0.3s ease-in-out;
}

.button:hover {
    background-color: darkblue;
}
````
