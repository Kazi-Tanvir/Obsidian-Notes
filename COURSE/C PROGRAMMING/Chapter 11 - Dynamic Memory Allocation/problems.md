# Chapter 11 - Practice Set

## Problem 1
Write a program to dynamically create an array of size 6 capable of storing 6 integers.

**Solution:**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    ptr = (int *)malloc(6 * sizeof(int));
    for (int i = 0; i < 6; i++) {
        printf("Enter the value of %d element: \n", i);
        scanf("%d", &ptr[i]);
    }
    for (int i = 0; i < 6; i++) {
        printf("The value of %d element is: %d\n", i, ptr[i]);
    }
    free(ptr);
    return 0;
}
```

## Problem 2
Use the array in problem 1 to store 6 integers entered by the user.

**Solution:** *(Included in Problem 1)*

## Problem 3
Solve problem 1 using calloc().

**Solution:**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    ptr = (int *)calloc(6, sizeof(int));
    for (int i = 0; i < 6; i++) {
        printf("Enter the value of %d element: \n", i);
        scanf("%d", &ptr[i]);
    }
    for (int i = 0; i < 6; i++) {
        printf("The value of %d element is: %d\n", i, ptr[i]);
    }
    free(ptr);
    return 0;
}
```

## Problem 4
Create an array dynamically capable of storing 5 integers. Now use realloc so that it can now store 10 integers.

**Solution:**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    ptr = (int *)malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) {
        printf("Enter the value of %d element: \n", i);
        scanf("%d", &ptr[i]);
    }
    for (int i = 0; i < 5; i++) {
        printf("The value of %d element is: %d\n", i, ptr[i]);
    }
    
    // Reallocate
    ptr = realloc(ptr, 10 * sizeof(int));
    for (int i = 0; i < 10; i++) {
        printf("Enter the value of %d element: \n", i);
        scanf("%d", &ptr[i]);
    }
    for (int i = 0; i < 10; i++) {
        printf("The value of %d element is: %d\n", i, ptr[i]);
    }
    free(ptr);
    return 0;
}
```

## Problem 5
Create an array of multiplication table of 7 upto 10 (7 x 10 = 70). Use realloc to make it store 15 number (from 7 x 1 to 7 x 15).

**Solution:**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;
    ptr = (int *)malloc(10 * sizeof(int));
    for (int i = 0; i < 10; i++) {
        ptr[i] = 7 * (i + 1);
        printf("The value of 7 X %d = %d\n", i + 1, ptr[i]);
    }
    
    ptr = realloc(ptr, 15 * sizeof(int));
    printf("\nAfter reallocating\n\n");
    for (int i = 0; i < 15; i++) {
        ptr[i] = 7 * (i + 1);
        printf("The value of 7 X %d = %d\n", i + 1, ptr[i]);
    }
    free(ptr);
    return 0;
}
```
