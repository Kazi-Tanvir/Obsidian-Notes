---
tags:
- html
- css
- selectors
---
# IDs and Classes

## What's the Actual Use?
IDs and Classes are attributes used to identify elements so they can be styled with CSS or manipulated with JavaScript.

## Other Common Use Cases
- Using a unique `id` for an anchor link (jump to section).
- Using a `class` to apply the same styling (e.g., `.btn-primary`) to multiple buttons.

## Documentation & Code
- `id`: Unique per page. Use `#` in CSS.
- `class`: Reusable. Use `.` in CSS.

````html
<!-- ID is unique -->
<nav id="main-navigation"> ... </nav>

<!-- Classes are reusable -->
<button class="btn success">Submit</button>
<button class="btn danger">Cancel</button>

<style>
    #main-navigation { background: #333; }
    .btn { padding: 10px; border-radius: 5px; }
    .success { color: green; }
</style>
````
