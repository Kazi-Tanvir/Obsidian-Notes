---
tags:
- nodejs
- javascript
- modules
---
# CommonJS vs EcmaScript Modules

## What's the Actual Use?
These are two different systems for importing and exporting code between files in JavaScript. CommonJS (`require`) is the older, original Node.js standard. ES Modules (`import/export`) is the modern, official JavaScript standard used by browsers and modern Node.js versions.

## Real-Life Analogy
CommonJS is like a traditional wired telephone—it's reliable and has been used for decades. ES Modules is like a modern smartphone—it's more versatile, supports newer features (like asynchronous loading), and is the new global standard. Both can make a call, but the way you dial is different.

## Other Common Use Cases
- **CommonJS:** Still widely used in older Node.js projects and some backend libraries.
- **ES Modules:** Used in almost all modern frontend frameworks (React, Vue) and new backend projects.

## Documentation & Code
Node.js uses CommonJS by default. To use ES Modules, set `"type": "module"` in your `package.json`.

```javascript
// --- CommonJS (example.cjs) ---
const fs = require('fs'); // Import
module.exports = { name: "Alice" }; // Export

// --- ES Modules (example.js / "type": "module") ---
import fs from 'fs'; // Import
export const name = "Alice"; // Export
```

```javascript
// Default Export vs Named Export (ESM)
export default function main() {} // import main from './file'
export const data = 123;           // import { data } from './file'
```