---
tags:
- nodejs
- backend
- files
---
# Working with Files (fs and path)

## What's the Actual Use?
The `fs` (File System) module allows Node.js to read, write, delete, and manage files on your computer. The `path` module provides utilities for handling and transforming file paths safely across different operating systems (Windows vs. Mac/Linux).

## Real-Life Analogy
If Node.js is an office worker, the `fs` module is their hands, allowing them to open folders, read documents, and write new reports. The `path` module is like a GPS; it ensures the worker finds the right office even if the building's address is written in a slightly different format.

## Other Common Use Cases
- Creating logs for a web server
- Uploading and saving user profile pictures
- Reading configuration files (like `.json` or `.txt`) to start an application

## Documentation & Code
Always prefer the `promises` version of `fs` or the `Sync` methods to avoid "callback hell."

```javascript
const fs = require('fs').promises;
const path = require('path');

async function manageFiles() {
  try {
    // 1. Create a safe path (works on Windows & Linux)
    const filePath = path.join(__dirname, 'data', 'hello.txt');

    // 2. Write to a file
    await fs.writeFile(filePath, 'Hello, Node.js!');

    // 3. Read from a file
    const content = await fs.readFile(filePath, 'utf-8');
    console.log("File content:", content);
  } catch (err) {
    console.error("Error managing files:", err);
  }
}

manageFiles();
```