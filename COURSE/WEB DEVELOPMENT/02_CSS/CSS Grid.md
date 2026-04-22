---
tags:
- css
- layout
- grid
---
# CSS Grid

## What's the Actual Use?
CSS Grid Layout is a two-dimensional layout system for the web. It lets you arrange content in rows and columns, making it ideal for building complex page structures.

## Real-Life Analogy
Think of a graph paper. Grid allows you to define exactly which squares (cells) an element should occupy, allowing for precise control over both horizontal and vertical positioning simultaneously.

## Other Common Use Cases
- Creating a full-page "Holy Grail" layout (header, sidebar, main, footer).
- Designing a masonry-style image gallery.

## Documentation & Code
Requires `display: grid;` on the parent.

````css
.grid-container {
    display: grid;
    grid-template-columns: 200px 1fr 1fr; /* 3 columns */
    grid-template-rows: auto 1fr auto;   /* 3 rows */
    gap: 10px;
}

.header { grid-column: 1 / 4; } /* Spans all 3 columns */
````
