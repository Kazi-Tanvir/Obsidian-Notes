# typedef keyword
We can use the ‘typedef’ keyword to create an alias name for data types in C.
‘typedef’ is more commonly used with structures.

```c
typedef struct Complex
{
    float real;
    float img;
} ComplexNo;
```

**Example Usage:**
Using the typedef alias, you can declare complex number variables more succinctly:
```c
ComplexNo c1, c2;
```
