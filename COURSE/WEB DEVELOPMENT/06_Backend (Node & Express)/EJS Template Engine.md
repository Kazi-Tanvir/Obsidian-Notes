---
tags:
- express
- ejs
- templating
---
# EJS Template Engine

## What's the Actual Use?
EJS (Embedded JavaScript) is a simple templating language that lets you generate HTML markup with plain JavaScript. It allows you to build dynamic websites on the server by injecting data (like user names or product lists) directly into your HTML files before sending them to the browser.

## Real-Life Analogy
EJS is like a "Fill-in-the-blanks" form. You have a standard letter (the HTML structure) with blank spaces like `Dear [Name]`. When a customer requests the letter, the server quickly fills in the blank with their actual name and hands them the finished, personalized paper.

## Other Common Use Cases
- Rendering a dynamic blog post page where the title and content come from a database.
- Displaying user-specific dashboards without using a frontend framework like React.
- Creating reusable UI parts like headers and footers using `includes`.

## Documentation & Code
Set EJS as the view engine in Express and use `<%= %>` for output.

```javascript
// --- server.js ---
const express = require('express');
const app = express();

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  const data = { user: 'Alice', items: ['Apple', 'Banana'] };
  // Render 'index.ejs' from the /views folder and pass data
  res.render('index', data);
});

// --- views/index.ejs ---
/*
<html>
  <body>
    <h1>Welcome, <%= user %>!</h1>
    <ul>
      <% items.forEach(function(item) { %>
        <li><%= item %></li>
      <% }); %>
    </ul>
  </body>
</html>
*/
```