---
tags:
- express
- middleware
- backend
---
# Middlewares in Express.md

## What's the Actual Use?
Middleware functions are functions that have access to the request object (`req`), the response object (`res`), and the next middleware function in the application’s request-response cycle. They are used to execute code, make changes to the request/response, and end the request-response cycle.

## Real-Life Analogy
Middleware is like an airport security checkpoint. Before you can reach your gate (the route handler), you must pass through various "middle" steps: the document check (auth middleware), the X-ray machine (data validation), and the boarding pass scan (logging). If any step fails, you are stopped before reaching the gate.

## Other Common Use Cases
- **Logging:** Keeping track of every request made to the server (e.g., using `morgan`).
- **Parsing:** Converting incoming JSON data into a readable JavaScript object (`express.json()`).
- **Authentication:** Checking if a user is logged in before allowing access to a private route.

## Documentation & Code
Use `app.use()` for global middleware or pass it directly to specific routes.

```javascript
const express = require('express');
const app = express();

// 1. Built-in Middleware (Parses JSON bodies)
app.use(express.json());

// 2. Custom Middleware
const myLogger = (req, res, next) => {
  console.log(`${req.method} request made to: ${req.url}`);
  next(); // CRITICAL: Call next() to move to the next function
};

app.use(myLogger);

app.get('/profile', (req, res) => {
  res.send('User Profile');
});

app.listen(3000);
```