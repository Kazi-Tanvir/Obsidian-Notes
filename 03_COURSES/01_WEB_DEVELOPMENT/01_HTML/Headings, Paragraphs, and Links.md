---
tags:
- html
- typography
- links
---
# Headings, Paragraphs, and Links

## What's the Actual Use?
These tags are the building blocks of text content. Headings provide hierarchy, paragraphs group text, and links (anchors) connect different pages or sections together.

## Other Common Use Cases
- Creating a Table of Contents using internal IDs (`#section-id`).
- Improving SEO by using `<h1>` through `<h6>` in a logical order.

## Documentation & Code
- `<h1>` to `<h6>`: Used for titles (h1 is the most important).
- `<p>`: Used for blocks of text.
- `<a>`: Used for hyperlinks; requires the `href` attribute.

````html
<h1>Main Topic</h1>
<h2>Sub-topic</h2>
<p>This is a paragraph explaining the concept of web development.</p>

<!-- External Link -->
<a href="https://www.google.com" target="_blank">Visit Google</a>

<!-- Internal Link to an ID -->
<a href="#footer">Jump to Footer</a>
````
