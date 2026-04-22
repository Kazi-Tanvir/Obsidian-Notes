---
tags:
- javascript
- dom
- mutation
---
# Inserting and Removing Elements

## What's the Actual Use?
You can dynamically add or remove HTML elements using JavaScript. This is how "infinite scroll" works or how new messages appear in a chat app without a page refresh.

## Other Common Use Cases
- Adding a new row to a table after a form is submitted.
- Removing a notification toast after a few seconds.

## Documentation & Code
- `createElement()`: Creates a new tag in memory.
- `appendChild()` / `prepend()`: Adds the element to the DOM.
- `remove()`: Deletes the element from the DOM.

````javascript
// 1. Create
const newDiv = document.createElement("div");
newDiv.innerText = "I am new here!";
newDiv.classList.add("box");

// 2. Insert
document.body.appendChild(newDiv);

// 3. Remove
const oldElement = document.getElementById("old");
oldElement.remove();
````
