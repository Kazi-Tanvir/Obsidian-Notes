---
tags:
- html
- entities
- code
---
# Entities and Code Tags

## What's the Actual Use?
Entities are used to display reserved characters (like `<` and `>`) that would otherwise be interpreted as HTML. Code tags are used to display snippets of programming code with proper monospaced formatting.

## Other Common Use Cases
- Displaying mathematical symbols or currency signs (e.g., `&euro;`).
- Sharing technical documentation or tutorials with code snippets.

## Documentation & Code
- **Entities:** Start with `&` and end with `;`.
- **Code Tags:** Use `<code>` for inline code and `<pre>` for preformatted blocks.

````html
<!-- Entities -->
<p>To write a tag, use &lt;h1&gt; &amp; &lt;/h1&gt;</p>

<!-- Code Display -->
<p>Use the <code>console.log()</code> method to debug.</p>

<pre>
<code>
function hello() {
    console.log("Hello World");
}
</code>
</pre>
````
