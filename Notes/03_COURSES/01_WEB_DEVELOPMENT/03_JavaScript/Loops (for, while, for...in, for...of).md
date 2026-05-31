---
tags:
- javascript
- loops
- iteration
---
# Loops (for, while, for...in, for...of)

## What's the Actual Use?
Loops automate repetitive tasks. Instead of writing the same code ten times, you write it once inside a loop and tell JavaScript how many times to run it.

## Other Common Use Cases
- Displaying a list of 100 products from a database.
- Summing up all the numbers in an array.

## Documentation & Code
- `for`: Classic loop for a specific count.
- `while`: Runs as long as a condition is true.
- `for...of`: Best for iterating over arrays.
- `for...in`: Best for iterating over object keys.

````javascript
// for loop
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// for...of (Arrays)
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log(color);
}

// for...in (Objects)
const car = { brand: "Tesla", model: "S" };
for (const key in car) {
    console.log(key + ": " + car[key]);
}
````
