---
title: "LAB 19 - pointer swap"
aliases:
  - pointer swap
  - 19_pointer_swap
tags:
  - type/lab
  - c/pointers
  - c/pointer-arithmetic
  - c/dynamic-memory
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/19_pointer_swap.c"
number: 19
up: "[[LAB - Index]]"
prev: "[[LAB 18 - pointer sort]]"
next: "[[LAB 20 - pointer remove]]"
related:
  - "[[LAB 12 - swap array]]"
  - "[[LAB 01 - change var temp]]"
created: 2026-10-29
status: draft
---
# LAB 19 - pointer swap

> [!abstract] Summary
> Allocates a dynamic heap array, searches for a target value using pointer traversal, and replaces matched elements with a new value.

**Source:** `LAB/19_pointer_swap.c`

## Problem
Allocate an integer array of size $n$ on the heap, populate it using pointer arithmetic, find all instances of value $a$, replace them with $b$, and display the updated array.

## Concepts used
- **Dynamic Memory Allocation (`malloc`):** Requesting heap memory via `(int*)malloc(n * sizeof(int))`.
- **Pointer Dereferencing for Read/Write:** Checking condition `*(arr + i) == a` and updating `*(arr + i) = b`.
- **Address-Based Input:** Passing `arr + i` directly to `scanf` without an address-of operator `&`.

## Code
```c
#include<stdio.h>

int main(){
    int n,a,b;
    printf("Enter the length of array :");
    scanf("%d",&n);
    int *arr = malloc(n * sizeof(int));

    printf("Enter you %d integers for arr:", n);
    for(int i = 0; i < n;i++){
        scanf("%d",arr + i);
    }
    printf("Enter x :");
    scanf("%d" ,&a);
    printf("Enter y :");
    scanf("%d",&b);
    for(int i = 0; i<n ; i++){
        if(*(arr + i) == a){
            *(arr + i) = b;
        }
    }

    printf("Swapped Array X\n");
    for(int i = 0; i < n;i++){
        printf("%d ",*(arr + i));
    }
    printf("\n");


}
```

## How it works
1. Reads length `n` and allocates heap buffer `int *arr = (int*)malloc(n * sizeof(int))`.
2. Reads integers into each slot via `scanf("%d", arr + i)`.
3. Reads search target `a` and replacement `b`.
4. Loops through indices $0 \le i < n$; when `*(arr + i) == a`, overwrites it with `b`.
5. Prints the modified elements using pointer offsets `*(arr + i)`.

## Sample run
> [!note] Traced from the source, not executed.
> Compiling with strict flags requires `#include <stdlib.h>`. When linked and run with inputs `5`, array `10 20 30 20 40`, and target `20 -> 99`, the output is:

```text
Enter the length of array :5
Enter you 5 integers for arr:10 20 30 20 40
Enter x :20
Enter y :99
Swapped Array X
10 99 30 99 40 
```

## Gotchas
> [!warning] Missing Header and Memory Leak
> The file uses `malloc` without including `<stdlib.h>`. In addition, dynamically allocated memory `arr` is never released with `free(arr)`, causing a heap memory leak.

## My notes
> [!question]- My notes

## Related
- [[LAB 12 - swap array]]
- [[LAB 01 - change var temp]]
