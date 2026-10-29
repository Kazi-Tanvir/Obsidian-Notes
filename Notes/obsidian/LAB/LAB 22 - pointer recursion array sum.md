---
title: "LAB 22 - pointer recursion array sum"
aliases:
  - pointer recursion array sum
  - 22_pointer_recursion_array_sum
tags:
  - type/lab
  - c/pointers
  - c/pointer-arithmetic
  - c/recursion
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "LAB/22_pointer_recursion_array_sum.c"
number: 22
up: "[[LAB - Index]]"
prev: "[[LAB 21 - pointer merge]]"
next: "[[LAB 23 - pointer array reverse]]"
related:
  - "[[LAB 15 - sum array recursion]]"
  - "[[CLASS 19 - pointer row sum]]"
created: 2026-10-29
status: draft
---
# LAB 22 - pointer recursion array sum

> [!abstract] Summary
> Computes the cumulative sum of a dynamic integer array by combining recursive call stacks with pointer arithmetic offset dereferencing.

**Source:** `LAB/22_pointer_recursion_array_sum.c`

## Problem
Prompt the user for the number of elements, allocate an array dynamically on the heap, and calculate its sum using a recursive function that accesses elements via pointer arithmetic.

## Concepts used
- **Recursive Array Summation:** Calculating total sum as `*(arr + n) + sum(arr, n - 1)`.
- **Pointer Offset Dereferencing:** Accessing the $n$-th element as `*(arr + n)` rather than `arr[n]`.
- **Base Condition:** Stopping recursion when $n < 0$, returning $0$.
- **Heap Lifetime:** Allocating array with `malloc(n * sizeof(int))` and freeing it with `free(arr)`.

## Code
```c
#include<stdio.h>
#include<stdlib.h>

int sum(int* arr, int n){
    if(n < 0) return 0;
    return *(arr + n) + sum(arr ,n-1);
}

int main(){
    int n;
    printf("Enter the length of array :");
    scanf("%d",&n);
    int *arr = (int*) malloc(n * sizeof(int));

    printf("Enter you %d integers :", n);
    for(int i = 0; i < n;i++){
        scanf("%d",arr + i);
    }

    if(arr == NULL) return 0;

    printf("The Summ is %d \n" , sum(arr , n -1));   
    free(arr);
}
```

## How it works
1. Reads array length `n` and allocates dynamic buffer `arr`.
2. Reads integers into addresses `arr + i`.
3. Calls `sum(arr, n - 1)`:
   - When $n < 0$, returns 0 (base case).
   - Otherwise computes `*(arr + n) + sum(arr, n - 1)`.
4. Returns cumulative sum to `main`.
5. Prints total and frees allocated memory.

## Sample run
```text
Enter the length of array :4
Enter you 4 integers :10 20 30 40
The Summ is 100 
```

## Gotchas
> [!warning] Late NULL Check
> As with other lab exercises, `if (arr == NULL) return 0;` appears after `scanf` has already attempted to populate `arr + i`. A failed allocation would segfault before reaching this check.

## My notes
> [!question]- My notes

## Related
- [[LAB 15 - sum array recursion]]
- [[CLASS 19 - pointer row sum]]
