---
tags: [c-programming, arrays, pointer-arithmetic]
---

# 07 Arrays

An array is a collection of similar elements stored in contiguous memory locations.

## Syntax
```c
int marks[90]; // Array of 90 integers
char name[20]; // Array of 20 characters
```

### Note:
Array indexing starts at **0**.

## Accessing Elements
```c
marks[0] = 33;
printf("%d", marks[0]);
```

## Initialization
```c
int cgpa[3] = {9, 8, 8};
float marks[] = {33, 40}; // Size inferred
```

## Pointer Arithmetic
A pointer can be incremented to point to the next memory location of that type.
```c
int *ptr = &marks[0];
ptr++; // Points to marks[1]
```

## Multidimensional Arrays
An array can have 2, 3, or more dimensions.
```c
int arr[3][2] = {{1, 4}, {7, 9}, {11, 22}};
```

## Practice Set
- [ ] Create an array of 10 numbers. Verify using pointer arithmetic that `(ptr+2)` points to the third element.
- [ ] If `S[3]` is a 1-D array, does `*(S+3)` refer to the third element? (True/False/Depends).
- [ ] Write a program to create an array of 10 integers and store the multiplication table of 5 in it.
- [ ] Repeat the above for a general input provided by the user.
- [ ] Write a program containing a function which reverses the array passed to it.
- [ ] Write a program containing functions which count the number of positive integers in an array.
- [ ] Create an array of size 3x10 containing multiplication tables of 2, 7, and 9.
- [ ] Create a 3D array and print the address of its elements in increasing order.
