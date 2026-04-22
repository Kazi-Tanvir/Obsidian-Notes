---
tags:
- css
- specificity
- cascade
---
# Specificity and Cascade

## What's the Actual Use?
The Cascade and Specificity determine which CSS rule "wins" when multiple rules apply to the same element. It's the core logic behind how CSS resolves styling conflicts.

## Real-Life Analogy
Think of a military hierarchy. A General's (ID) order overrides a Captain's (Class) order, which overrides a Private's (Element) order. If two officers of the same rank give different orders, the one who spoke last (Source Order) is followed.

## Other Common Use Cases
- Overriding third-party library styles without using `!important`.
- Organizing CSS so that global styles are easily specialized.

## Documentation & Code
Hierarchy of specificity (lowest to highest):
1. Element selectors (`h1`)
2. Class selectors (`.main`)
3. ID selectors (`#header`)
4. Inline styles (`style="..."`)

````css
/* Specificity: 0,0,1 */
p { color: red; }

/* Specificity: 0,1,0 (Wins over element) */
.text { color: blue; }

/* Specificity: 1,0,0 (Wins over class) */
#main-text { color: green; }
````
