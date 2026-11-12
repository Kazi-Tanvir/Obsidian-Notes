---
title: "LAB 18 - pointer sort"
aliases:
  - pointer sort
  - 18_pointer_sort
tags:
  - type/lab
  - c/pointers
  - c/pointer-arithmetic
  - c/sorting
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "LAB/18_pointer_sort.c"
number: 18
up: "[[LAB - Index]]"
prev: "[[LAB 17 - merge sort recursion]]"
next: "[[LAB 19 - pointer swap]]"
related:
  - "[[LAB 11 - sort array]]"
  - "[[CLASS 18 - pointer books 2d arr]]"
created: 2026-10-29
status: draft
---
# LAB 18 - pointer sort

> [!abstract] Summary
> Re-implements descending array sorting and min/max detection using pointer arithmetic dereferencing (`*(arr + i)`) rather than bracketed indexing (`arr[i]`).

**Source:** `LAB/18_pointer_sort.c`

## Problem
Sort an array of $n$ user-provided integers in descending order, find the minimum and maximum elements, and access all elements strictly through pointer arithmetic.

## Concepts used
- **Pointer Arithmetic Equivalence:** Recognizing that `arr[i]` is identical to `*(arr + i)`. The base address `arr` is offset by $i \times \text{sizeof(int)}$ bytes.
- **Descending Selection Sort:** Swapping `*(arr + i)` and `*(arr + j)` whenever `*(arr + j) > *(arr + i)`.
- **Extrema Retrieval:** In a descending sequence, the minimum is `*(arr + n - 1)` and the maximum is `*arr` (or `*(arr + 0)`).

## Code
```c
#include<stdio.h>
#include <stdlib.h>

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

    for(int i = 0;i<n;i++){
        for(int j = i + 1 ; j < n ;j++){
            if(*(arr+ j)>*(arr+i)){
                int temp = *(arr+j);
                *(arr+j) = *(arr+i);
                *(arr+i) = temp;
            }
        }
    }

    printf("Sorted Array\n");
    for(int i = 0; i < n;i++){
        printf("%d ",*(arr+i));
    }
    printf("\n");
    printf("The Minimum number is : %d\n" ,*(arr + n-1));
    printf("The Maximum number is : %d\n" ,*(arr));
    printf("\n");
    free(arr);

    return 0;

}
```

## How it works
1. Prompts for array length `n` and allocates stack array `arr[n]`.
2. Reads inputs directly into addresses using `scanf("%d", arr + i)`.
3. Compares elements at addresses `arr + i` and `arr + j` using `*(arr + j) > *(arr + i)`.
4. Performs an in-place swap using a temporary integer variable `temp`.
5. Prints the sorted array, minimum value `*(arr + n - 1)`, and maximum value `*(arr + 0)`.

## Sample run
```text
Enter the length of array :5
Enter you 5 integers :50 20 40 10 30
Sorted Array
50 40 30 20 10 
The Minimum number is : 10
The Maximum number is : 50
```

## Gotchas
> [!warning] Precedence of Dereference vs Addition
> Dereferencing `*arr + i` adds $i$ to the first element's value, whereas `*(arr + i)` adds $i$ to the pointer before dereferencing. Parentheses are strictly necessary.

## My notes
> [!question]- My notes

## Related
- [[LAB 11 - sort array]]
- [[CLASS 18 - pointer books 2d arr]]
