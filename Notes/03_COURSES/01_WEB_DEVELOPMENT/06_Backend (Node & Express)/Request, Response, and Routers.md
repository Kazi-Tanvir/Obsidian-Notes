---
tags:
- express
- routing
- backend
---
# Request, Response, and Routers

## What's the Actual Use?
- **Request (`req`):** An object containing all the data sent by the user (URL parameters, headers, body).
- **Response (`res`):** An object used to send data back to the user (HTML, JSON, status codes).
- **Routers:** A way to group related routes into separate files to keep your codebase clean and modular.

## Real-Life Analogy
Think of a large department store. The **Request** is the customer walking in and asking for a specific item. The **Response** is the store clerk giving the customer the item or an error message if it's out of stock. **Routers** are the different departments (Electronics, Clothing, Groceries)—they organize the store so customers don't have to ask every single employee for every item.

## Other Common Use Cases
- **Request:** Accessing `req.params.id` to fetch a specific user from a database.
- **Response:** Sending a `404 Not Found` status when a page doesn't exist.
- **Routers:** Separating user-related routes (`/users`) from product routes (`/products`).

## Documentation & Code
Use `express.Router()` to create modular route handlers.

```javascript
// --- routes/userRoutes.js ---
const express = require('express');
const router = express.Router();

router.get('/:id', (req, res) => {
  const userId = req.params.id; // Access dynamic URL segment
  res.send(`Fetching data for user: ${userId}`);
});

module.exports = router;

// --- server.js ---
const express = require('express');
const app = express();
const userRoutes = require('./routes/userRoutes');

// Mount the router at a specific path
app.use('/users', userRoutes); 

app.listen(3000);
```