# Types of function call
Based on the way we pass arguments to the function, function calls are of two types.

1. **Call by value** -> Sending the values of arguments.
2. **Call by reference** -> Sending the address of arguments.

### Call by reference
Here the address of the variables is passed to the function as arguments.
Now since the addresses are passed to the function, the function can now modify the value of a variable in calling function using `*` and `&` operators.

**Example:**
```c
void swap(int *x, int *y) {
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
```
