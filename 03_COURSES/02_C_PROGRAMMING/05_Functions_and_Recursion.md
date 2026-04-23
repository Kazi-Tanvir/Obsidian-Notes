---
tags: [c-programming, functions, recursion]
---

# 05 Functions and Recursion

Functions are used to break a program into smaller, manageable, and reusable chunks.

## Function Components
1. **Function Prototype**: Declaration informing the compiler about the function.
2. **Function Call**: Instructs the compiler to execute the function body.
3. **Function Definition**: The actual code inside the function.

### Syntax:
```c
void display(); // Prototype

int main() {
    display(); // Call
    return 0;
}

void display() { // Definition
    printf("hi i am display\n");
}
```

## Passing Values to Functions
Functions can take **parameters** and **return** a value.

```c
int sum(int a, int b) {
    return a + b;
}
```

## Recursion
A function that calls itself is called a recursive function.

### Example: Factorial using Recursion
```c
int factorial(int x) {
    if (x == 0 || x == 1) return 1;
    return x * factorial(x - 1);
}
```

## Practice Set
- [ ] Write a program using a function to find the average of three numbers.
- [ ] Write a function to convert Celsius to Fahrenheit.
- [ ] Write a function to calculate the force of attraction on a body of mass `m` exerted by Earth (`g = 9.8m/s²`).
- [ ] Write a program using recursion to calculate the nth element of the Fibonacci series.
- [ ] What will `printf("%d %d %d \n", a, ++a, a++);` produce (where `a = 4`)?
- [ ] Write a recursive function to calculate the sum of the first `n` natural numbers.
- [ ] Write a program using functions to print a star pattern (1, 3, 5, ... stars).
