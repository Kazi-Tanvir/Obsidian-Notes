---
tags:
- nodejs
- backend
- npm
- javascript
---
# Introduction to Node.js and NPM

## What's the Actual Use?
Node.js is a runtime environment that allows you to run JavaScript code outside of a web browser, specifically on servers. NPM (Node Package Manager) is the world's largest software registry, used to install tools, libraries, and frameworks (like Express or React) into your project.

## Real-Life Analogy
JavaScript is like a master chef. Before Node.js, the chef was trapped in one specific restaurant (the browser). Node.js is like giving the chef their own food truck; now they can cook anywhere—on your computer, on a server, or in the cloud. NPM is the grocery store where the chef buys pre-made ingredients (packages) to make cooking faster.

## Other Common Use Cases
- Building web servers and APIs
- Creating command-line interface (CLI) tools
- Automating repetitive tasks (like image optimization or file renaming)

## Documentation & Code
Use the terminal to interact with Node and NPM.

```bash
# Check if Node is installed
node -v

# Initialize a new project (creates package.json)
npm init -y

# Install a package (e.g., lodash)
npm install lodash

# Run a JavaScript file with Node
node index.js
```

```javascript
// index.js
console.log("Hello from Node.js!");
console.log("Current Directory:", __dirname);
```