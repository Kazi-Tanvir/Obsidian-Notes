---
title: "LAB 15 - sum array recursion"
aliases:
  - sum array recursion
  - 15_sum_array_recursion
tags:
  - type/lab
  - c/recursion
  - c/arrays
  - c/functions
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/15_sum_array_recursion.c"
number: 15
up: "[[LAB - Index]]"
prev: "[[LAB 14 - merge array]]"
next: "[[LAB 16 - reverse array recursion]]"
related:
  - "[[LAB 22 - pointer recursion array sum]]"
  - "[[ASG 08 - recursion practice]]"
created: 2026-10-29
status: draft
---
# LAB 15 - sum array recursion

> [!abstract] Summary
> Computes the cumulative sum of elements in an integer array using a recursive divide-and-conquer strategy backwards from the last element.

**Source:** `LAB/15_sum_array_recursion.c`

## Problem
Compute the sum of array elements recursively by adding the current element `arr[n]` to the sum of the preceding `n - 1` elements until the index drops below zero.

## Concepts used
- **Recursion Base Case:** Terminating the recursion when the index becomes negative ($n < 0$), returning $0$.
- **Recursive Step:** Breaking the total sum into `arr[n] + sum(arr, n - 1)`.
- **Call Stack Unwinding:** Each frame returns its element plus the child frame's return value back up the stack.

## Code
```c
#include<stdio.h>

int sum(int arr[], int n){
    int(n < 0) return 0;
    return arr[n] + sum(arr ,n-1);
}

int main(){
    int arr[5] = { 2,5,6,7,4};
    int size = sizeof(arr)/sizeof(int);
    printf("The Summ is %d \n" , sum(arr , size -1));
}
```

## How it works
1. Array `(2, 5, 6, 7, 4)` of 5 integers is initialized in `main`.
2. Calls `sum(arr, size - 1)` (index 4).
3. The function checks the base case: if $n < 0$, returns 0.
4. Otherwise, evaluates `arr[n] + sum(arr, n - 1)`.
5. The stack computes $4 + 7 + 6 + 5 + 2 + 0 = 24$.

## Sample run
> [!note] Traced from the source, not executed.
> Line 4 contains a syntax typo `int(n < 0)` preventing compilation with strict GCC flags. Once corrected to `if (n < 0)`, execution yields:

```text
The Summ is 24 
```

## Gotchas
> [!bug] Syntax Typo in Base Condition
> Line 4 contains `int(n < 0) return 0;` instead of `if (n < 0) return 0;`. Using `int` as a condition keyword causes a compiler syntax error.

## My notes
> [!question]- My notes

## Related
- [[LAB 22 - pointer recursion array sum]]
- [[ASG 08 - recursion practice]]
