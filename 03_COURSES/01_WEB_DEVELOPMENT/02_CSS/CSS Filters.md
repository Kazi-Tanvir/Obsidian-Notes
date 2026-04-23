---
tags:
- css
- design
- filters
---
# CSS Filters

## What's the Actual Use?
Filters allow you to apply graphical effects like blur, brightness, contrast, and grayscale to elements (usually images) directly in the browser.

## Other Common Use Cases
- Blurring a background image to make text on top more readable.
- Creating a "dark" or "sepia" theme for images without using Photoshop.
- Adding a drop shadow to a transparent PNG.

## Documentation & Code
Common functions include `blur()`, `brightness()`, `contrast()`, `grayscale()`, `hue-rotate()`, `invert()`, `opacity()`, `saturate()`, and `sepia()`.

````css
.blurred-bg {
    filter: blur(5px);
}

.bw-image {
    filter: grayscale(100%);
}

.bright-hover:hover {
    filter: brightness(1.2);
}
````
