---
tags:
- css
- layout
- flexbox
---
# Flexbox

## What's the Actual Use?
Flexbox (Flexible Box Layout) is a one-dimensional layout method for arranging items in rows or columns. It excels at distributing space and aligning items even when their size is unknown or dynamic.

## Real-Life Analogy
Think of a tray of cupcakes. Flexbox is the logic that decides if the cupcakes sit in a single row, how much space is between them, and whether they stay centered or move to the edges of the tray.

## Other Common Use Cases
- Centering an element perfectly in the middle of a page.
- Creating a responsive navigation bar that switches from horizontal to vertical.

## Documentation & Code
Requires `display: flex;` on the parent (container).

````css
.container {
    display: flex;
    justify-content: center; /* Horizontal alignment */
    align-items: center;     /* Vertical alignment */
    flex-wrap: wrap;         /* Allows items to move to next line */
    gap: 20px;               /* Space between items */
}

.item {
    flex: 1; /* Grow to fill space */
}
````
