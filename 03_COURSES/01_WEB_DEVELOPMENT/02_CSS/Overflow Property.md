---
tags:
- css
- layout
- overflow
---
# Overflow Property

## What's the Actual Use?
The `overflow` property specifies whether to clip content or add scrollbars when an element's content is too big to fit in its specified area.

## Other Common Use Cases
- Creating scrollable sidebar menus.
- Preventing text from leaking out of a fixed-size card.
- Clearing floats using `overflow: hidden;`.

## Documentation & Code
- `visible`: Default. Content is not clipped.
- `hidden`: Content is clipped, no scrollbars.
- `scroll`: Content is clipped, scrollbars are always added.
- `auto`: Scrollbars added only if content exceeds the box.

````css
.scroll-box {
    width: 200px;
    height: 100px;
    overflow: auto;
    border: 1px solid black;
}
````
