---
tags:
- css
- media
- images
---
# Object-fit and Object-cover

## What's the Actual Use?
The `object-fit` property specifies how an `<img>` or `<video>` should be resized to fit its container. It prevents images from looking "stretched" or "squashed".

## Other Common Use Cases
- Creating uniform profile picture circles where the image fills the area.
- Full-screen background videos that don't lose their aspect ratio.

## Documentation & Code
- `fill`: Stretches to fill (distorts).
- `contain`: Shows whole image (leaves gaps).
- `cover`: Fills area, crops edges (maintains ratio).

````css
.profile-img {
    width: 150px;
    height: 150px;
    object-fit: cover;
    border-radius: 50%;
}
````
