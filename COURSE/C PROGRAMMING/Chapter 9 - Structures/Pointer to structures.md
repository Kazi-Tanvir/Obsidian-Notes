# Pointer to structures
A pointer to structures can be created as follows:

```c
struct employee *ptr;
ptr = &e1;
// now we can print structure elements using:
printf("%d", (*ptr).code);
```
