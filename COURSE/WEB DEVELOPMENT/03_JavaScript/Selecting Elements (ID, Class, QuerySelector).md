---
tags:
- javascript
- dom
- selectors
---
# Selecting Elements (ID, Class, QuerySelector)

## What's the Actual Use?
To manipulate an element, you first have to find it. Selectors allow you to target specific elements based on their ID, class, tag name, or CSS selectors.

## Other Common Use Cases
- Targeting all images to add a lazy-loading attribute.
- Selecting a specific form to handle its submission.

## Documentation & Code
- `getElementById`: Fastest, targets a single unique ID.
- `getElementsByClassName`: Targets multiple elements by class.
- `querySelector`: Most flexible, uses CSS syntax (targets first match).
- `querySelectorAll`: Uses CSS syntax (targets all matches).

````javascript
// By ID
const header = document.getElementById("header");

// By Class
const buttons = document.getElementsByClassName("btn");

// By QuerySelector
const firstLink = document.querySelector("nav a.active");

// By QuerySelectorAll
const allItems = document.querySelectorAll(".list-item");
````
