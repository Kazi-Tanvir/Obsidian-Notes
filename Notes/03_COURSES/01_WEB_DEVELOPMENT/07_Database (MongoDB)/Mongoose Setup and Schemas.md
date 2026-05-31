---
tags:
- database
- mongodb
- mongoose
---
# Mongoose Setup and Schemas

## What's the Actual Use?
Mongoose is an ODM (Object Data Modeling) library for MongoDB and Node.js. It provides a straight-forward, schema-based solution to model your application data, ensuring that the data being saved to your database follows a specific structure and validation rules.

## Real-Life Analogy
MongoDB by itself is like a blank notebook where you can write anything anywhere. Mongoose is like a printed form with specific boxes for "Name," "Date of Birth," and "Phone Number." It ensures that everyone fills out the information exactly the same way, so it's easy to read and manage later.

## Other Common Use Cases
- Enforcing that an "Email" field must be a valid email string.
- Automatically adding `createdAt` and `updatedAt` timestamps to documents.
- Defining relationships between different data (e.g., linking a Post to a User).

## Documentation & Code
Define a Schema, then create a Model to interact with the database.

```javascript
const mongoose = require('mongoose');

// 1. Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/myapp');

// 2. Define a Schema (The Blueprint)
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, unique: true },
  age: Number,
  createdAt: { type: Date, default: Date.now }
});

// 3. Create a Model (The Tool to interact with DB)
const User = mongoose.model('User', userSchema);

// Usage:
const newUser = new User({ name: 'Alice', email: 'alice@example.com' });
newUser.save();
```