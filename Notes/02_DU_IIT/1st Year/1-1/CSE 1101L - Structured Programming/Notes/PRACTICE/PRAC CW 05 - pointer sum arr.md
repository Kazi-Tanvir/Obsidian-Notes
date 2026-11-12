---
title: "PRAC CW 05 - pointer sum arr"
aliases:
  - pointer sum arr
  - 05_pointer_sum_arr
tags:
  - type/practice
  - c/pointers
  - c/arrays
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/CONCEPT_WISE/05_pointer_sum_arr.c"
up: "[[PRAC - Index]]"
related:
  - "[[LAB 22 - pointer recursion array sum]]"
created: 2026-10-29
status: draft
---
# PRAC CW 05 - pointer sum arr

> [!abstract] Summary
> Calculates the sum of all elements in an integer array using pointer dereferencing.

**Source:** `PRACTICE/CONCEPT_WISE/05_pointer_sum_arr.c`

## Problem
Demonstrate pointer arithmetic and memory addressing fundamentals by implementing `pointer sum arr` directly in C.

## Concepts used
- **Pointer Addressing & Dereferencing:** Accessing and mutating memory locations directly via pointer variables.
- **Pointer Offset Arithmetic:** Moving through memory sequentially using `*(p + i)`.

## Code
```c
#include<stdio.h>

int array_sum(const int *start , const int *end){
    int sum = 0;
    for(int i = 0; start != end; i++){
        sum += *start ;
        start++;
    }
    return sum;
}

int main(){
    int arr[10] = { 1,2,3,4,5,6,7,8,9,10};
    int sum = array_sum(arr , arr + 9);

    printf("%d",sum);
}
```

## How it works
1. Initializes inputs or reads from standard input.
2. Manipulates data memory addresses directly using pointer references.
3. Produces output verifying in-place memory mutation.

## My notes
> [!question]- My notes

## Related
- [[LAB 22 - pointer recursion array sum]]
