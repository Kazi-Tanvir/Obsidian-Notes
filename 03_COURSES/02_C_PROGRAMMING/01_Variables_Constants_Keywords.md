---
tags: [c-programming, variables, constants, keywords]
---

# 01 Variables, Constants & Keywords

## Variables
A variable is a container which stores a 'value'. Similar to containers in a kitchen storing Rice or Sugar, variables in C store the value of a constant.

### Example:
```c
int a = 3;      // 'a' is assigned 3
float b = 4.7;  // 'b' is assigned 4.7
char c = 'A';   // 'c' is assigned 'A'
```

### Rules for Naming Variables
1. The first character must be an alphabet or underscore `_`.
2. No commas or blanks are allowed.
3. No special symbols other than underscore `_` are allowed.
4. Variable names are case-sensitive.

## Constants
An entity whose value does not change is called a constant. A variable is an entity whose value can be changed.

### Types of Constants
1. **Integer Constant**: e.g., 1, 6, 7, 9
2. **Real Constant**: e.g., 322.1, 2.5, 7.0
3. **Character Constant**: e.g., 'a', '$', '@' (must be enclosed in single quotes)

## Keywords
Keywords are reserved words whose meaning is already known to the compiler. There are 32 keywords available in C (e.g., `int`, `float`, `char`, `if`, `else`, `while`, `return`, etc.).

## Comments
Comments clarify the program in plain language and are ignored by the compiler.
1. **Single-line Comment**: Starts with `//`.
2. **Multi-line Comment**: Starts with `/*` and ends with `*/`.

## Library Functions & Input
- `printf()`: Used to print values on the screen.
- `scanf()`: Used to take input from the user.
  - Syntax: `scanf("%d", &i);`
  - `&` is the "address of" operator.

## Practice Set
- [ ] Write a C program to calculate the area of a rectangle using hard-coded inputs.
- [ ] Write a C program to calculate the area of a rectangle using inputs supplied by the user.
- [ ] Calculate the area of a circle and modify the same program to calculate the volume of a cylinder given its radius and height.
- [ ] Write a program to convert Celsius to Fahrenheit.
- [ ] Write a program to calculate simple interest for a set of values representing principal, number of years, and rate of interest.
