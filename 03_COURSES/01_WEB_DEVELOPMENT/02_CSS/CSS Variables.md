---
tags:
- css
- variables
- maintenance
---
# CSS Variables

## What's the Actual Use?
CSS Variables (Custom Properties) allow you to store specific values (like colors or sizes) in one place and reuse them throughout your stylesheet. This makes updating themes much easier.

## Other Common Use Cases
- Managing "Dark Mode" vs "Light Mode" by swapping variable values.
- Creating a consistent spacing system (e.g., `--main-padding: 20px`).

## Documentation & Code
Variables are defined using `--` and accessed using the `var()` function. Usually defined in the `:root` selector for global access.

````css
:root {
    --primary-color: #3498db;
    --main-font: 'Roboto', sans-serif;
}

.button {
    background-color: var(--primary-color);
    font-family: var(--main-font);
}
````
