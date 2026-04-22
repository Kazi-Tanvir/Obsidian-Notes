---
tags:
- javascript
- async
- timers
---
# setInterval and setTimeout

## What's the Actual Use?
Timers allow you to execute code after a certain delay or repeatedly at a fixed interval. This is essential for animations, periodic data fetching, or delayed user feedback.

## Other Common Use Cases
- Creating a countdown timer or a clock.
- Displaying a popup after a user has been on the page for 10 seconds.
- Automatically scrolling a carousel every 5 seconds.

## Documentation & Code
- `setTimeout`: Executes a function once after a delay.
- `setInterval`: Repeatedly executes a function with a fixed delay between calls.
- `clearTimeout` / `clearInterval`: Stops the timer.

````javascript
// Run once after 2 seconds
const timerId = setTimeout(() => {
    console.log("Time is up!");
}, 2000);

// Run every 1 second
const intervalId = setInterval(() => {
    console.log("Ticking...");
}, 1000);

// Stop the interval after 5 seconds
setTimeout(() => clearInterval(intervalId), 5000);
````
