---
tags:
- javascript
- async
- promises
---
# Callbacks and Promises

## What's the Actual Use?
Callbacks and Promises handle asynchronous operations. They ensure that your code waits for a task to finish (like loading an image or fetching data) before proceeding to the next step, without freezing the browser.

## Real-Life Analogy
**Callbacks:** Ordering pizza and giving the shop your phone number. They call you back when it's ready.
**Promises:** Ordering pizza and receiving a buzzer. The buzzer is a "promise" that you will have pizza. It's currently "pending", it will eventually be "resolved" (buzzes when ready) or "rejected" (they ran out of dough).

## Other Common Use Cases
- Fetching data from an API.
- Reading a file from the disk in Node.js.

## Documentation & Code
- **Callback:** A function passed as an argument.
- **Promise:** An object representing the eventual completion of an async task.

````javascript
// Promise Example
const getData = new Promise((resolve, reject) => {
    const success = true;
    if (success) resolve("Data received!");
    else reject("Error occurred.");
});

getData
    .then(data => console.log(data))
    .catch(err => console.error(err));
````
