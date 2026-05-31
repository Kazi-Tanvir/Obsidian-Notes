---
tags:
- css
- integration
- basics
---
# Inline, Internal, and External CSS

## What's the Actual Use?
There are three ways to apply CSS to an HTML document. Understanding them helps in choosing the best method for maintainability and performance.

## Other Common Use Cases
- **Inline:** Quick fixes or dynamic styling via JavaScript.
- **Internal:** Single-page projects or email templates.
- **External:** Standard for production apps (best for caching and maintenance).

## Documentation & Code
- **Inline:** Use the `style` attribute.
- **Internal:** Use `<style>` in `<head>`.
- **External:** Use `<link>` to a `.css` file.

````html
<!-- Inline -->
<h1 style="color: red;">Hello</h1>

<!-- Internal (in <head>) -->
<style>
    body { background-color: white; }
</style>

<!-- External (in <head>) -->
<link rel="stylesheet" href="style.css">
````
