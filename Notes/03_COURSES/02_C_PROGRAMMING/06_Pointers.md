---
tags: [c-programming, pointers, memory-management]
---

# 06 Pointers

A pointer is a variable that stores the memory address of another variable.

## Operators
- `&` (Address of): Returns the address of a variable.
- `*` (Value at address / Dereference): Returns the value stored at a specific address.

## Declaring a Pointer
```c
int i = 8;
int *j = &i; // 'j' stores the address of 'i'
```

## Pointer to a Pointer
A pointer can store the address of another pointer.
```c
int **k;
k = &j;
```

## Types of Function Calls
1. **Call by Value**: Passing a copy of the variable's value. Changes inside the function do not affect the original variable.
2. **Call by Reference**: Passing the address of the variable. Changes inside the function **do** affect the original variable.

### Example: Swapping using Call by Reference
```c
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}
```

## Practice Set
- [ ] Write a program to print the address of a variable. Use this address to get the value of the variable.
- [ ] Write a program having a variable `i`. Print the address of `i`. Pass this variable to a function and print its address. Are these addresses the same? Why?
- [ ] Write a program to change the value of a variable to ten times its current value.
- [ ] Write a function and pass the value by reference.
- [ ] Write a program using a function which calculates the sum and average of two numbers. Use pointers and print the values in `main()`.
- [ ] Write a program to print the value of a variable `i` by using a "pointer to pointer" type of variable.
- [ ] Try problem 3 using call by value and verify that it does not change the value.
