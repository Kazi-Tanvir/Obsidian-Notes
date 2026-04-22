---
tags: [c-programming, memory-allocation, dynamic-memory]
---

# 11 Dynamic Memory Allocation

Allows allocating memory during runtime.

## Key Functions (`<stdlib.h>`)

### 1. `malloc()`
Allocates a block of memory and returns a void pointer. Initial memory contains garbage values.
```c
ptr = (int*) malloc(30 * sizeof(int));
```

### 2. `calloc()`
Allocates contiguous memory and initializes each block with **0**.
```c
ptr = (float*) calloc(30, sizeof(float));
```

### 3. `free()`
Deallocates the memory previously allocated by `malloc` or `calloc`.
```c
free(ptr);
```

### 4. `realloc()`
Used to change the size of the previously allocated memory.
```c
ptr = realloc(ptr, new_size);
```

## Practice Set
- [ ] Write a program to dynamically create an array of size 6 capable of storing 6 integers.
- [ ] Use the array in the previous problem to store 6 integers entered by the user.
- [ ] Solve problem 1 using `calloc()`.
- [ ] Create an array dynamically capable of storing 5 integers, then use `realloc` so that it can store 10 integers.
- [ ] Create an array of the multiplication table of 7 up to 10 (7x10=70). Use `realloc` to make it store 15 numbers (up to 7x15).
- [ ] Attempt problem 4 using `calloc()`.
