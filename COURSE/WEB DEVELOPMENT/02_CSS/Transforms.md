---
tags:
- css
- design
- transforms
---
# Transforms

## What's the Actual Use?
Transforms allow you to rotate, scale, skew, or move (translate) elements in 2D or 3D space without affecting the normal document flow.

## Other Common Use Cases
- Rotating an icon when a menu opens.
- Zooming in on an image when hovered.
- Centering an absolute element with `translate(-50%, -50%)`.

## Documentation & Code
Common functions: `translate()`, `rotate()`, `scale()`, and `skew()`.

````css
.box:hover {
    transform: scale(1.1) rotate(5deg);
}

.centered {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
````
