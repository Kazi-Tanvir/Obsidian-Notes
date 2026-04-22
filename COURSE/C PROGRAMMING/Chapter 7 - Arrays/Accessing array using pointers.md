# Accessing array using pointers
This way we can have an integer pointer pointing to first element of the array like this:

```c
int *ptr = &arr[0]; // or simple arr
ptr++;
*ptr // will have next value
```
