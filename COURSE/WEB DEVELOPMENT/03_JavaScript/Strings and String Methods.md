---
tags:
- javascript
- strings
- methods
---
# Strings and String Methods

## What's the Actual Use?
Strings are used to handle text. String methods allow you to manipulate that text—searching for keywords, changing case, or splitting a sentence into words.

## Other Common Use Cases
- Formatting a user's name to be capitalized.
- Extracting the domain name from an email address.

## Documentation & Code
Common methods: `length`, `toUpperCase()`, `includes()`, `slice()`, `split()`.

````javascript
const text = "JavaScript is awesome";

console.log(text.length);           // 21
console.log(text.toUpperCase());    // "JAVASCRIPT IS AWESOME"
console.log(text.includes("awesome")); // true
console.log(text.slice(0, 10));     // "JavaScript"
console.log(text.split(" "));       // ["JavaScript", "is", "awesome"]
````
