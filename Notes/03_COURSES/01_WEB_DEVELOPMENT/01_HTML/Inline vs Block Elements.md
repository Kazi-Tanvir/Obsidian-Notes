---
tags:
- html
- css
- layout
---
# Inline vs Block Elements

## What's the Actual Use?
This distinction determines how elements sit on the page. Block elements take up the full width, while inline elements only take up as much space as their content.

## Other Common Use Cases
- Using `<div>` (block) to create sections or containers.
- Using `<span>` (inline) to style a specific word inside a sentence.

## Documentation & Code
- **Block:** `<div>`, `<h1>`, `<p>`, `<section>`, `<ul>`.
- **Inline:** `<span>`, `<a>`, `<img>`, `<strong>`.

````html
<!-- Block elements stack on top of each other -->
<div>I am a block level element.</div>
<p>Me too, I take the whole width.</p>

<!-- Inline elements sit side-by-side -->
<span>I am inline.</span>
<a href="#">I am also inline.</a>
````
