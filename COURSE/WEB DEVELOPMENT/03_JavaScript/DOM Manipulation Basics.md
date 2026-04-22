---
tags:
- javascript
- dom
- basics
---
# DOM Manipulation Basics

## What's the Actual Use?
The DOM (Document Object Model) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content.

## Other Common Use Cases
- Changing the text of a heading when a button is clicked.
- Adding a "dark-mode" class to the body element.

## Documentation & Code
The browser creates a DOM when a page is loaded. JavaScript uses the `document` object to interact with it.

````javascript
// Changing content
document.title = "New Page Title";

// Changing styles
document.body.style.backgroundColor = "#f0f0f0";

// Accessing an element
const heading = document.getElementById("main-title");
heading.innerText = "Updated Heading";
````
