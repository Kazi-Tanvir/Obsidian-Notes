---
tags:
- css
- layout
- positioning
---
# Position Property

## What's the Actual Use?
The `position` property specifies the type of positioning method used for an element (static, relative, absolute, fixed, or sticky).

## Real-Life Analogy
- **Static:** A book on a shelf in its natural spot.
- **Relative:** Moving the book slightly from its original spot without affecting other books.
- **Absolute:** Taking the book and placing it exactly 2 inches from the top of the entire bookshelf.
- **Fixed:** Taping the book to your glasses so it's always in front of your eyes no matter where you move.
- **Sticky:** A book that stays on the shelf until you scroll past it, then it slides down with you.

## Other Common Use Cases
- Creating "sticky" navigation bars.
- Positioning icons inside search bars or input fields.

## Documentation & Code
- `static`: Default; follows normal flow.
- `relative`: Positioned relative to its normal position.
- `absolute`: Positioned relative to the nearest positioned ancestor.
- `fixed`: Positioned relative to the viewport.
- `sticky`: Toggles between relative and fixed based on scroll position.

````css
.parent { position: relative; }

.child {
    position: absolute;
    top: 10px;
    right: 10px;
}

.navbar {
    position: sticky;
    top: 0;
}
````
