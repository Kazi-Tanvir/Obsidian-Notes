# realloc() function
Sometimes the dynamically allocated memory is insufficient or more than required.
realloc is used to allocate memory of new size using the previous pointer and size.

**Syntax:**
```c
ptr = realloc(ptr, newsize);
ptr = realloc(ptr, 3 * sizeof(int));
```
