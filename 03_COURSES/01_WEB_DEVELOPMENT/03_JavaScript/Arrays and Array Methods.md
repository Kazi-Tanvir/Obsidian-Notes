---
tags:
- javascript
- arrays
- methods
---
# Arrays and Array Methods

## What's the Actual Use?
Arrays are used to store multiple values in a single variable. Array methods allow you to transform, filter, and iterate through these lists efficiently.

## Other Common Use Cases
- Storing a list of items in a user's wishlist.
- Filtering a list of products by category or price.

## Documentation & Code
Common methods: `push()`, `pop()`, `map()`, `filter()`, `forEach()`, `reduce()`.

````javascript
const numbers = [1, 2, 3, 4, 5];

// map: transform each element
const doubled = numbers.map(n => n * 2);

// filter: remove elements that don't match
const even = numbers.filter(n => n % 2 === 0);

// forEach: iterate through elements
numbers.forEach(n => console.log("Number: " + n));

console.log(doubled); // [2, 4, 6, 8, 10]
console.log(even);    // [2, 4]
````
