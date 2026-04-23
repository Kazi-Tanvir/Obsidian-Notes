---
tags: 
- html
- basics
- webdev
---
# Basic Structure

## What's the Actual Use?
Every HTML document requires a boilerplate structure to be recognized by browsers. It defines the document type, language, and essential metadata like the title and character encoding.

## Other Common Use Cases
- Setting the favicon and external CSS/JS links in the `<head>`.
- Defining the language of the page for accessibility and SEO.

## Documentation & Code
The basic skeleton consists of the `<!DOCTYPE html>` declaration followed by the `<html>`, `<head>`, and `<body>` tags.

````html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Webpage</title>
</head>
<body>
    <!-- Content goes here -->
    <h1>Hello World</h1>
</body>
</html>
````
