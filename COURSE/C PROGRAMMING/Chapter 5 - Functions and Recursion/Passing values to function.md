# Passing values to function
We can pass values to a function and can get a value in return from a function.

```c
int sum(int a, int b) {
    int c;
    c = a + b;
    return c;
}
```

**Note:**
1. Parameters are the values or variable placeholders in the function definition (e.g. `a` & `b`).
2. Arguments are the actual values passed to the function to make a call (e.g. `2` & `3`).
3. A function can return only one value at a time.
4. If the passed variable is changed inside the function, the function call doesn’t change the value in the calling function (Call by value).
