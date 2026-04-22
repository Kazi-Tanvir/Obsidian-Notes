# Pointer to a pointer
Just like `j` is pointing to `i` or storing the address of `i`, we can have another variable `k` which can further store the address of `j`.

```c
int **k;
k = &j;
```
We can even go further one level and create a variable `l` of type `int***` to store the address of `k`.
