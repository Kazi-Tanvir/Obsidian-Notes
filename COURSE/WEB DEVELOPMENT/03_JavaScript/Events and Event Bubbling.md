---
tags:
- javascript
- events
- interactivity
---
# Events and Event Bubbling

## What's the Actual Use?
Events are actions that happen in the browser (clicks, keypresses, scrolls). Event Bubbling is the process where an event triggered on a child element "bubbles up" to its parents.

## Real-Life Analogy
Think of a fire alarm in a specific room (the child). Even though the fire is only in that room, the alarm signal travels up through the building's wiring (the parents) so the main security desk knows something happened.

## Other Common Use Cases
- Handling clicks on a single `<ul>` to detect which `<li>` was clicked (Event Delegation).
- Preventing a form from submitting while you validate inputs.

## Documentation & Code
- `addEventListener()`: The standard way to listen for events.
- `stopPropagation()`: Stops the event from bubbling up.
- `preventDefault()`: Stops the default browser behavior.

````javascript
const btn = document.querySelector("#myBtn");

btn.addEventListener("click", (event) => {
    console.log("Button Clicked!");
    event.stopPropagation(); // Stop bubbling
});

const form = document.querySelector("form");
form.addEventListener("submit", (e) => {
    e.preventDefault(); // Don't refresh page
    console.log("Form data processed manually.");
});
````
