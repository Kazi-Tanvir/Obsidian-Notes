---
tags: [c-programming, conditionals, if-else, switch]
---

# 03 Conditional Instructions

In C, we execute instructions based on whether certain conditions are met.

## If-Else Statement
Used to execute code only if a condition is true.

```c
if (condition) {
    // Code if true
} else {
    // Code if false
}
```

### Relational Operators
- `==` (Equality)
- `!=` (Not equal)
- `>`, `<` (Greater than, Less than)
- `>=`, `<=` (Greater than or equal to, Less than or equal to)

## Logical Operators
- `&&` (AND): True if both conditions are true.
- `||` (OR): True if at least one condition is true.
- `!` (NOT): Inverts the result.

## Else-If Clause
Used for multiple conditions (if-else ladder).

```c
if (condition1) {
    // ...
} else if (condition2) {
    // ...
} else {
    // ...
}
```

## Ternary Operator
Short-hand for if-else.
```c
condition ? expression_if_true : expression_if_false;
```

## Switch Case
Used when choosing between multiple alternatives for a variable.

```c
switch (variable) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code
}
```

## Practice Set
- [ ] What will be the output of `int a=10; if(a=11) printf("I am 11"); else printf("I am not 11");`?
- [ ] Write a program to determine if a student has passed (requires total 40% and at least 33% in each of 3 subjects).
- [ ] Calculate income tax as per government slabs (2.5-5L: 5%, 5-10L: 20%, Above 10L: 30%).
- [ ] Write a program to check if a year is a leap year.
- [ ] Determine if a character entered is lowercase.
- [ ] Find the greatest of four numbers entered by the user.
