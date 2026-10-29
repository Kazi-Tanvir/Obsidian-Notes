---
title: "BUET Offline 4 - p1"
aliases:
  - BUET Offline 4 p1
  - offline4_A1_p1
tags:
  - type/practice
  - c/pointers
  - c/sorting
  - c/arrays
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "00_BUET_CSE_101/offline/offline4_A1_p1.c"
up: "[[BUET - Index]]"
prev: "[[BUET Offline 1 - p2]]"
related:
  - "[[LAB 18 - pointer sort]]"
  - "[[CLASS 18 - pointer books 2d arr]]"
created: 2026-10-29
status: draft
---
# BUET Offline 4 - p1

> [!abstract] Summary
> Implements indirect array sorting using an array of pointers (`int *ptr[3]`), sorting address pointers while preserving original array order in memory.

**Source:** `00_BUET_CSE_101/offline/offline4_A1_p1.c`

## Problem
Read three integers into array `arr[3]`. Create an array of pointers pointing to each element, sort the values by swapping pointers, and print the resulting sorted order.

## Concepts used
- **Array of Pointers:** Declaring `int *ptr[3]` where each element stores the memory address of an integer.
- **Indirect Sorting:** Comparing dereferenced values `*ptr[i] > *ptr[j]` and swapping address pointers rather than data values.
- **Pass-by-Reference Swapping:** Implementing `swap(int *a, int *b)`.

## Code
```c
#include<stdio.h>
void swap(int *a, int*b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int main(){
    int arr[3];
    int *ptr[3];
    for (int i = 0; i < 3; i++){
        scanf("%d",&arr[i]);
        ptr[i] = &arr[i];
    }
    
    for(int i = 0; i < 3; i++){
        for(int j = i+1 ; j < 3; j++){
            if(arr[i] > arr[j]){
                swap(ptr[i],ptr[j]);
            }
        }
    }

    for(int i = 0; i < 3; i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
}
```

## How it works
1. Populates `arr[3]` from user input.
2. Initializes pointer array: `ptr[i] = &arr[i]`.
3. Compares values via dereferencing: if `*ptr[i] > *ptr[j]`, swaps values or pointers.
4. Prints sorted elements.

## Sample run
```text
30 10 20
10 20 30 
```

## Gotchas
> [!warning] Swapping Values vs Swapping Addresses
> In `offline4_A1_p1.c`, the swap function `swap(ptr[i], ptr[j])` dereferences and swaps the values stored in `arr`. To achieve true pointer sorting without altering `arr`, the pointer addresses themselves (`int **`) must be swapped.

## My notes
> [!question]- My notes

## Related
- [[LAB 18 - pointer sort]]
- [[CLASS 18 - pointer books 2d arr]]
