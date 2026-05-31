---
tags:
- css
- layout
- display
---
# Display Property

## What's the Actual Use?
The `display` property is the most important property for controlling layout. It determines if an element is treated as a block, inline, or a more complex layout container like Flex or Grid.

## Other Common Use Cases
- Hiding elements with `display: none;`.
- Converting inline links into block-level buttons.

## Documentation & Code
- `block`: Full width, starts on a new line.
- `inline`: Only as wide as content, no new line.
- `inline-block`: Inline flow but accepts width/height.
- `none`: Removes element from the document.

````css
.hidden { display: none; }

.inline-btn {
    display: inline-block;
    width: 100px;
    padding: 10px;
}
````
