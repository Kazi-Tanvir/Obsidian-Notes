---
tags:
- javascript
- functions
- logic
---
# Functions and Arrow Functions

## What's the Actual Use?
Functions are reusable blocks of code. They allow you to write logic once and "call" it multiple times throughout your application, keeping your code DRY (Don't Repeat Yourself).

## Other Common Use Cases
- Calculating the total price of items in a shopping cart.
- Handling a button click event.

## Documentation & Code
- **Function Declaration:** Can be called before it's defined (hoisting).
- **Arrow Function:** Modern, concise syntax; does not have its own `this` context.

````javascript
// Function Declaration
function greet(name) {
    return "Hello " + name;
}

// Arrow Function
const add = (a, b) => a + b;

console.log(greet("Alice"));
console.log(add(5, 10));
````
