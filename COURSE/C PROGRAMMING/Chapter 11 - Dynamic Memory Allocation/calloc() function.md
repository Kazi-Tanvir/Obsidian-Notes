# calloc() function
calloc stands for continuous allocation. It initializes each memory block with a default value of 0.

**Syntax:**
```c
ptr = (float*)calloc(30, sizeof(float));
//allocates contiguous space in memory for 30 blocks (floats)
```
If the space is not sufficient, memory allocation fails, and a NULL pointer is returned.
