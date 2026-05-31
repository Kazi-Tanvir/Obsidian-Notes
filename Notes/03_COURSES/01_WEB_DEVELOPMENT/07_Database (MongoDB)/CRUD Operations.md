---
tags:
- database
- mongodb
- crud
---
# CRUD Operations

## What's the Actual Use?
CRUD stands for **C**reate, **R**ead, **U**pdate, and **D**elete. These are the four basic functions that every persistent storage system must perform. Mastering CRUD in MongoDB allows you to manage the entire lifecycle of your application's data.

## Real-Life Analogy
Think of a filing cabinet in a doctor's office. 
- **Create:** Filling out a new patient's folder. 
- **Read:** Looking up a patient's history to see their last visit. 
- **Update:** Changing a patient's address because they moved. 
- **Delete:** Shredding a folder for a patient who hasn't visited in 50 years.

## Other Common Use Cases
- **Create:** A user signing up for a new account.
- **Read:** A user viewing their "Order History."
- **Update:** A user changing their profile picture.
- **Delete:** A user deleting a comment on a blog post.

## Documentation & Code
In the MongoDB Shell or a driver, use these methods:

```javascript
// 1. CREATE
db.users.insertOne({ name: "Bob", age: 25 });

// 2. READ
db.users.find({ age: { $gte: 18 } }); // Find all users 18 or older

// 3. UPDATE
db.users.updateOne(
  { name: "Bob" }, 
  { $set: { age: 26 } }
);

// 4. DELETE
db.users.deleteOne({ name: "Bob" });
```