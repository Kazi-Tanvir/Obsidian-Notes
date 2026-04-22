# Chapter 6 - Practice Set

## Problem 1
Write a program to print the address of a variable. Use this address to get the value of the variable.

**Solution:**
```c
#include <stdio.h>

int main() {
    int a = 4;
    int *ptr = &a;
    printf("The address of variable a is %u\n", ptr);
    printf("The value of variable a is %d\n", *ptr);
    return 0;
}
```

## Problem 2
Write a program having a variable ‘i’. Print the address of ‘i’. Pass this variable to a function and print its address. Are these addresses same? Why?

**Solution:**
```c
#include <stdio.h>

void printAddress(int a) {
    printf("The address of variable a is %u\n", &a);
}

int main() {
    int i = 4;
    printf("The value of variable i is %d\n", i);
    printAddress(i);
    printf("The address of variable i is %u\n", &i);
    return 0;
}
```
*They are not the same because call by value makes a copy of the variable.*

## Problem 3
Write a program to change the value of a variable to ten times of its current value. Write a function and pass the value by reference.

**Solution:**
```c
#include <stdio.h>

void tenTimes(int *x) {
    *x = *x * 10;
}

int main() {
    int a = 5;
    printf("Original value: %d\n", a);
    tenTimes(&a);
    printf("New value: %d\n", a);
    return 0;
}
```

## Problem 5
Write a program using a function which calculates the sum and average of two numbers. Use pointers and print the values of sum and average in main().

**Solution:**
```c
#include <stdio.h>

void sumAndAvg(int a, int b, int *sum, float *avg) {
    *sum = a + b;
    *avg = (float)(*sum) / 2;
}

int main() {
    int i, j, sum;
    float avg;
    i = 3;
    j = 6;
    sumAndAvg(i, j, &sum, &avg);
    printf("The value of sum is %d\n", sum);
    printf("The value of avg is %f\n", avg);
    return 0;
}
```

## Problem 6
Write a program to print the value of a variable i by using “pointer to pointer” type of variable.

**Solution:**
```c
#include <stdio.h>

int main() {
    int i = 345;
    int *ptr = &i;
    int **ptr_ptr = &ptr;
    
    printf("The value of i is %d\n", **ptr_ptr);
    return 0;
}
```
