---
tags:
- css
- box-model
- layout
---
# Box Model (Margin, Padding, Borders)

## What's the Actual Use?
Every element in HTML is a rectangular box. The Box Model defines how the size of these boxes is calculated, including the content, padding, border, and margin.

## Real-Life Analogy
Think of a framed picture. The **Content** is the photo, the **Padding** is the white space between the photo and the frame, the **Border** is the physical frame, and the **Margin** is the space between this frame and other pictures on the wall.

## Other Common Use Cases
- Creating space between elements (Margin).
- Adding "breathing room" inside a container (Padding).

## Documentation & Code
The `box-sizing: border-box;` property is often used to include padding and border in the element's total width and height.

````css
.box {
    width: 300px;
    padding: 20px;
    border: 5px solid black;
    margin: 10px;
    box-sizing: border-box; /* Total width stays 300px */
}
````
