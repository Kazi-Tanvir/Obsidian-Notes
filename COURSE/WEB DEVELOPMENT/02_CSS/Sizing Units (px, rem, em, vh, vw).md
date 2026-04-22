---
tags:
- css
- sizing
- units
---
# Sizing Units (px, rem, em, vh, vw)

## What's the Actual Use?
Units define how the size of elements, fonts, and spacing are measured. Choosing between absolute and relative units is key to building responsive designs.

## Other Common Use Cases
- Using `rem` for accessible font sizes that scale with browser settings.
- Using `vh` and `vw` to create full-screen sections.

## Documentation & Code
- `px`: Absolute pixels.
- `rem`: Relative to the root (`<html>`) font size.
- `em`: Relative to the parent element's font size.
- `vh`/`vw`: Percentage of the viewport height/width.

````css
.container {
    width: 100vw; /* Full width */
    height: 50vh; /* Half screen height */
}

.text {
    font-size: 2rem; /* 2x root font size */
    padding: 1em;    /* Padding relative to current font size */
}
````
