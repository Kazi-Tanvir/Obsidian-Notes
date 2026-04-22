# Chapter 7 - Practice Set

## Problem 1
Create an array of 10 numbers. Verify using pointer arithmetic that (ptr+2) points to the third element where ptr is a pointer pointing to the first element of the array.

**Solution:**
```c
#include <stdio.h>

int main() {
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int *ptr = arr; // points to arr[0]
    
    printf("The third element is %d\n", *(ptr + 2));
    return 0;
}
```

## Problem 3
Write a program to create an array of 10 integers and store multiplication table of 5 in it.

**Solution:**
```c
#include <stdio.h>

int main() {
    int mul[10];
    for (int i = 0; i < 10; i++) {
        mul[i] = 5 * (i + 1);
    }
    
    for (int i = 0; i < 10; i++) {
        printf("5 x %d = %d\n", i + 1, mul[i]);
    }
    return 0;
}
```

## Problem 5
Write a program containing a function which reverses the array passed to it.

**Solution:**
```c
#include <stdio.h>

void reverse(int *arr, int n) {
    int temp;
    for (int i = 0; i < (n / 2); i++) {
        temp = arr[i];
        arr[i] = arr[n - i - 1];
        arr[n - i - 1] = temp;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    reverse(arr, 7);
    for (int i = 0; i < 7; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

## Problem 6
Write a program containing functions which counts the number of positive integers in an array.

**Solution:**
```c
#include <stdio.h>

int countPositive(int *arr, int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > 0) {
            count++;
        }
    }
    return count;
}

int main() {
    int arr[] = {1, -2, 3, -4, 5, 6, -7};
    printf("Number of positive integers is %d\n", countPositive(arr, 7));
    return 0;
}
```

## Problem 7
Create an array of size 3 x 10 containing multiplication tables of the numbers 2, 7 and 9 respectively.

**Solution:**
```c
#include <stdio.h>

int main() {
    int mulTable[3][10];
    int numbers[] = {2, 7, 9};
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 10; j++) {
            mulTable[i][j] = numbers[i] * (j + 1);
        }
    }
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 10; j++) {
            printf("%d x %d = %d\n", numbers[i], j + 1, mulTable[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}
```
