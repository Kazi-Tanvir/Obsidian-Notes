---
tags:
- javascript
- logic
- flow-control
---
# Conditionals (if, else if)

## What's the Actual Use?
Conditionals allow your code to make decisions. They execute different blocks of code based on whether a specified condition evaluates to true or false.

## Other Common Use Cases
- Checking if a user has entered a valid password.
- Showing a "Sale" banner only if a product is on discount.

## Documentation & Code
Basic structure using `if`, `else if`, and `else`.

````javascript
const temperature = 30;

if (temperature > 35) {
    console.log("It's very hot!");
} else if (temperature > 20) {
    console.log("It's a nice day.");
} else {
    console.log("It's cold.");
}
````
