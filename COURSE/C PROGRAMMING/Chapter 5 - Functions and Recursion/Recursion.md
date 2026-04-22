# Recursion
A function defined in C can call itself. This is called recursion. A function calling itself is also called ‘recursive’ function.

**Example:** Factorial
```c
int factorial(int x) {
    int f;
    if (x == 0 || x == 1) {
        return 1; // base case
    } else {
        f = x * factorial(x - 1);
        return f;
    }
}
```

**Important Notes:**
1. Recursion is often a direct way to implement certain algorithms, but not always the most direct for every algorithm.
2. The condition in a recursive function that stops further recursion is called the **base case**.
3. Without a base case, a recursive function can continue indefinitely, causing a stack overflow.
