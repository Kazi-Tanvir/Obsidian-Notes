---
tags:
- javascript
- async
- api
---
# Async, Await, and Fetch API

## What's the Actual Use?
`async/await` is a cleaner way to write asynchronous code, making it look and behave like synchronous code. The `fetch()` API is the modern way to make network requests.

## Real-Life Analogy
Imagine you are a chef. Instead of starting a roast and just standing there (synchronous), or leaving the kitchen and waiting for a bell to ring (promises), you simply "await" the roast to finish while you prep other ingredients. You are still working, but that specific line of logic is paused.

## Other Common Use Cases
- Getting the latest weather data for a user's location.
- Sending user registration data to a database.

## Documentation & Code
- `async`: Marks a function as asynchronous.
- `await`: Pauses execution until the promise is settled.
- `fetch()`: Returns a promise that resolves to the Response object.

````javascript
const fetchUser = async () => {
    try {
        const response = await fetch("https://api.github.com/users/octocat");
        const data = await response.json();
        console.log(data.name);
    } catch (error) {
        console.log("Fetch failed", error);
    }
};

fetchUser();
````
