---
tags:
- javascript
- advanced
- syntax
---
# Advanced JS (Destructuring, Spread, IIFE)

## What's the Actual Use?
These modern JavaScript features allow for cleaner, more readable, and more efficient code. They simplify how we extract data from objects/arrays and how we combine them.

## Other Common Use Cases
- Extracting only the needed props from a React component.
- Merging two configuration objects together.
- Protecting variables from the global scope (IIFE).

## Documentation & Code
- **Destructuring:** Unpacking values from arrays or properties from objects.
- **Spread (`...`):** Expanding an array or object into its elements.
- **IIFE:** Immediately Invoked Function Expression.

````javascript
// Destructuring
const user = { id: 1, username: "dev_user" };
const { username } = user;

// Spread
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4]; // [1, 2, 3, 4]

// IIFE
(function() {
    console.log("I run immediately and keep variables private!");
})();
````
