---
tags:
- javascript
- functional-programming
- currying
- composition
- immutability
- pure-functions
date: 2026-08-06
---

# Day 6 - Functional Programming: First-Class Functions, Currying, Composition & Immutability

## SECTION 1: IN-DEPTH THEORY & SYNTAX

### 1. Pure Functions & Side-Effect Management

Functional Programming (FP) in JavaScript centers on building software by combining **Pure Functions**. A function is pure if:

1.  **Determinism**: Given the same inputs, it always returns the exact same output.

2.  **No Side Effects**: It does not read or mutate external state (HTTP requests, global variables, DOM mutations, file I/O).

```javascript
// Impure Function (Mutates outer variable & non-deterministic)
let taxRate = 0.08;
function calculateTotalImpure(price) {
taxRate += 0.01; // Side Effect!
return price + price * taxRate;
}
// Pure Function (Referentially Transparent)
function calculateTotalPure(price, rate) {
return price + price * rate;
}
```

### 2. Currying & Partial Application

- **Currying**: A transformation process that converts a function with $N$ arguments into $N$ nested functions that each accept a single argument (f(a, b, c) $\rightarrow$ f(a)(b)(c)).

- **Partial Application**: Fixing a subset of arguments to produce a new function of lower arity.

```javascript
// Curried Logger Utility
const logger = (level) => (component) => (message) => {
console.log(`[${new Date().toISOString()}] [${level.toUpperCase()}] [${component}]: ${message}`);
};
const logError = logger("error");
const logAuthError = logError("AuthService");
logAuthError("Invalid JWT signature");
// Output: [2026-08-06...] [ERROR] [AuthService]: Invalid JWT signature
```

### 3. Function Composition (pipe vs compose)

**Function Composition** combines two or more functions to produce a new function.

- **compose(f, g, h)(x)**: Evaluates Right-To-Left $\rightarrow f(g(h(x)))$.

- **pipe(f, g, h)(x)**: Evaluates Left-To-Right $\rightarrow h(g(f(x)))$ (more readable dataflow).

```javascript
// Building 'pipe' and 'compose' from scratch using Array.prototype.reduce
const pipe = (...fns) => (initialValue) =>
fns.reduce((acc, fn) => fn(acc), initialValue);
const compose = (...fns) => (initialValue) =>
fns.reduceRight((acc, fn) => fn(acc), initialValue);
// Transformation Data Pipeline
const trim = (str) => str.trim();
const lowercase = (str) => str.toLowerCase();
const sanitizeSpaces = (str) => str.replace(/\s+/g, "_");
const formatSlug = pipe(trim, lowercase, sanitizeSpaces);
console.log(formatSlug(" JavaScript Clean Architecture "));
// "javascript_clean_architecture"
```

### 4. Immutability Patterns in Modern JS

Mutating state directly introduces unpredictable bug propagation. Modern JavaScript provides immutable methods and shallow/deep copy mechanisms:

- **Immutable Array Methods (ES2023)**: toSorted(), toReversed(), toSpliced(), with() return new arrays without mutating the original.

- **Deep Copy**: structuredClone(obj) native API for deep cloning without JSON limitations.

```javascript
// Immutable Data Mutation Pattern
const state = {
```

user: { name: "Alice", roles: ["admin"] },

settings: { theme: "light" }

```javascript
};
// Updating nested state immutably via spread operator
const updatedState = {
```

...state,

user: {

...state.user,

roles: [...state.user.roles, "editor"]

```javascript
}
};
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

| **Pattern / Method** | **Implementation / Syntax** | **Purpose** |
| --- | --- | --- |
| **pipe(...fns)** | ...args) => fns.reduce((v, f) => f(v), args)        Lef | -to-right function chaining |
| **compose(...fns)** | ...args) => fns.reduceRight((v, f) => f(v), args)   Rig | t-to-left function chaining |
| **Array.prototype.toSorted()** | arr.toSorted(compareFn) | Non-mutating version of sort() |
| **Array.prototype.toSpliced()** | arr.toSpliced(start, deleteCount, ...items) | on-mutating version of splice() |
| **structuredClone(val)** | const copy = structuredClone(original) | Native deep object cloning |
| **Object.freeze(obj)** | Object.freeze(obj) | Shallow-freezes object properties |

## SECTION 3: PRACTICAL PROBLEMS

### Challenge 1: Purity & Immutability Bug Identification

Analyze the function below. Identify 3 impurity/immutability bugs and rewrite it as a completely pure function.

```javascript
const globalCart = [{ id: 1, name: "Book", price: 20 }];
function applyDiscountAndTax(cart, discountPercent) {
for (let item of cart) {
item.price -= item.price * (discountPercent / 100);
item.tax = item.price * 0.1;
}
globalCart.push({ id: 2, name: "Freebie", price: 0 });
return cart.sort((a, b) => b.price - a.price);
}
```

*Hint*: Avoid in-place array mutation (sort), external state updates (globalCart.push), and item mutation (item.price -=).

### Challenge 2: Refactoring Imperative Data Flow to Composable Pipe

Refactor the following imperative data processing function into a point-free composable pipeline using pipe(...) and curried helper functions.

```javascript
// Imperative Data Processing
function getTopActiveUserEmails(users) {
const activeUsers = [];
for (let i = 0; i < users.length; i++) {
if (users[i].isActive) {
activeUsers.push(users[i]);
}
}
activeUsers.sort((a, b) => b.score - a.score);
const emails = [];
for (let j = 0; j < Math.min(3, activeUsers.length); j++) {
emails.push(activeUsers[j].email.toLowerCase());
}
return emails;
}
```

*Hint*: Create reusable curried helpers: filterBy(prop, val), sortByDesc(prop), take(limit), mapTo(prop).

### Challenge 3: Advanced Auto-Currying Engine with Placeholder Support

Implement an auto-currying wrapper function curry(fn) from scratch that supports argument placeholders (curry._).

**Requirements**:

1.  Allows partial application until fn.length arguments are supplied.

2.  Supports curry._ as a placeholder to skip argument slots.

3.  Example behavior:

> const fn = (a, b, c) => [a, b, c];
>
> const curried = curry(fn);
>
> curried(1)(2)(3); // [1, 2, 3]
>
> curried(curry._, 2)(1)(3); // [1, 2, 3]
>
> curried(curry._, curry._, 3)(1)(2); // [1, 2, 3]

*Hint*: Track supplied arguments array and fill placeholder indices (_) when subsequent arguments are passed.
