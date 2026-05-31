---
tags: [c-programming, operators, instructions]
---

# 02 Instructions and Operators

A C program is a set of instructions, similar to a recipe.

## Types of Instructions
1. **Type Declaration Instructions**: Declaring variables before use.
2. **Arithmetic Instructions**: Performing mathematical operations.
3. **Control Instructions**: Determining the flow of control (Sequence, Decision, Loop, Case).

## Type Declaration Instructions
Variables must be declared before they are used.

```c
int a;
float b;
char c;

// Valid variations
int i = 10;
int j = i;
int a = 2, b = 3, c = 4;
int j1 = a + j - i;
```

## Arithmetic Instructions
Operators used for mathematical calculations:
- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `%` (Modulus/Remainder)

### Note:
- `%` returns the remainder and cannot be applied to `float` values.
- No operator is assumed (e.g., `ab` is invalid; use `a * b`).
- Exponentiation requires `pow(x, y)` from `<math.h>`.

## Type Conversion
- `int` and `int` → `int`
- `int` and `float` → `float`
- `float` and `float` → `float`

*Example:* `5/2` becomes `2`, while `5.0/2` becomes `2.5`.

## Operator Precedence & Associativity
C does not follow simple BODMAS rules.

| Priority | Operators |
| :--- | :--- |
| 1st | `*`, `/`, `%` |
| 2nd | `+`, `-` |
| 3rd | `=` |

**Associativity**: When operators have equal priority, they are evaluated based on associativity (usually left-to-right for arithmetic operators).

## Practice Set
- [ ] Which of the following is invalid in C?
    - a. `int a=1; int b = a;`
    - b. `int v = 3*3;`
    - c. `char dt = '21 dec 2020';`
- [ ] What data type will `3.0/8 – 2` return?
- [ ] Write a program to check whether a number is divisible by 97 or not.
- [ ] Explain step-by-step evaluation of `3*x/y – z+k`, where x=2, y=3, z=3, k=1.
- [ ] What will `3.0 + 1` result in? (Integer, Floating point, or Character).
