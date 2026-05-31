---
tags:
- javascript
- basics
- data-types
---
# Variables, Data Types, and Objects

## What's the Actual Use?
Variables store data that your program needs to operate. Data types define what kind of data is being stored, and objects allow you to group related data and functions together into a single entity.

## Other Common Use Cases
- Storing user profile information in an object.
- Managing "state" in an application (e.g., is the user logged in?).

## Documentation & Code
- `let` & `const`: Modern ways to declare variables (prefer `const`).
- `var`: Legacy variable declaration (avoid).
- **Primitives:** String, Number, Boolean, Null, Undefined, Symbol, BigInt.
- **Objects:** Key-value pairs.

````javascript
const name = "John"; // String
const age = 25;      // Number
const isStudent = true; // Boolean

// Object
const user = {
    firstName: "Jane",
    lastName: "Doe",
    hobbies: ["coding", "reading"]
};

console.log(user.firstName);
````
