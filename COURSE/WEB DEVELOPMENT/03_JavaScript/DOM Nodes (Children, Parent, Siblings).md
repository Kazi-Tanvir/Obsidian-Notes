---
tags:
- javascript
- dom
- traversal
---
# DOM Nodes (Children, Parent, Siblings)

## What's the Actual Use?
DOM traversal allows you to navigate the "family tree" of HTML elements. If you have one element, you can find its parent, its children, or its neighbors (siblings) without needing new selectors.

## Other Common Use Cases
- Finding the parent "card" of a clicked "delete" button.
- Iterating through all child items in a navigation menu.

## Documentation & Code
- `parentNode` / `parentElement`: Up the tree.
- `childNodes` / `children`: Down the tree.
- `nextSibling` / `previousSibling`: Sideways.

````javascript
const item = document.querySelector(".active");

// Get Parent
const list = item.parentElement;

// Get Next Neighbor
const nextItem = item.nextElementSibling;

// Get All Children
const allChildren = list.children;
````
