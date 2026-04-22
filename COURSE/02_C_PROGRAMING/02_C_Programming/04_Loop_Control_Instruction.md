---
tags: [c-programming, loops, while, for, do-while]
---

# 04 Loop Control Instruction

Loops are used to execute a set of instructions repeatedly.

## Types of Loops
1. **While Loop**
2. **Do-While Loop**
3. **For Loop**

### While Loop
Executes code as long as the condition remains true.
```c
while (condition) {
    // code
}
```

### Do-While Loop
Similar to `while`, but executes the block **at least once** before checking the condition.
```c
do {
    // code
} while (condition);
```

### For Loop
A more concise way to write loops.
```c
for (initialize; test; increment/decrement) {
    // code
}
```

## Increment and Decrement Operators
- `i++` (Post-increment): Increase `i` by 1.
- `++i` (Pre-increment): Increase `i` by 1.
- `i--` (Post-decrement): Decrease `i` by 1.
- `--i` (Pre-decrement): Decrease `i` by 1.

## Break and Continue
- `break`: Exits the loop immediately.
- `continue`: Skips the current iteration and moves to the next one.

## Practice Set
- [ ] Write a program to print the multiplication table of a given number `n`.
- [ ] Write a program to print the multiplication table of 10 in reverse order.
- [ ] Is a `do-while` loop executed at least once, twice, or at most once?
- [ ] Write a program to sum the first ten natural numbers using a `while` loop.
- [ ] Re-implement the sum program using `for` and `do-while` loops.
- [ ] Calculate the sum of numbers occurring in the multiplication table of 8.
- [ ] Write a program to calculate the factorial of a given number using a `for` loop.
- [ ] Check whether a given number is prime or not using loops.
