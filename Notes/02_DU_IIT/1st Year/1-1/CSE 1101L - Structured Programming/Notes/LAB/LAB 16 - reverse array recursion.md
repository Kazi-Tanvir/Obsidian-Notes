---
title: "LAB 16 - reverse array recursion"
aliases:
  - reverse array recursion
  - 16_reverse_array_recursion
tags:
  - type/lab
  - c/recursion
  - c/arrays
  - c/functions
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/16_reverse_array_recursion.c"
number: 16
up: "[[LAB - Index]]"
prev: "[[LAB 15 - sum array recursion]]"
next: "[[LAB 17 - merge sort recursion]]"
related:
  - "[[LAB 23 - pointer array reverse]]"
  - "[[CLASS 17 - pointer string reverse]]"
created: 2026-10-29
status: draft
---
# LAB 16 - reverse array recursion

> [!abstract] Summary
> Reverses an integer array in place using a two-pointer recursive function swapping symmetric outer elements toward the center.

**Source:** `LAB/16_reverse_array_recursion.c`

## Problem
Invert the order of elements in an array without using iterative loops or auxiliary arrays, relying purely on recursive function calls.

## Concepts used
- **Two-Pointer Convergence:** Initializing `start = 0` and `end = size - 1`, moving inward (`start + 1`, `end - 1`) until `start >= end`.
- **In-Place Swap:** Swapping `arr[start]` and `arr[end]` via temporary variable `temp`.
- **Tail Recursion:** Making the recursive call as the final step of the function.

## Code
```c
#include<stdio.h>

int reverse(int arr[],int start,int end){
    if(start >= end) return 0;
    int temp = arr[end];
    arr[end] = arr[start];
    arr[start] = temp ;
    return reverse(arr , start + 1 , end - 1);
}

int main(){
    int arr[5] = { 2,5,6,7,4};
    int size = sizeof(arr)/sizeof(int);
    reverse(size - 1 , 0);
    for (int i = 0; i< size ; i++){
        printf("%d",arr[i]);
    }
    printf("\n")
}
```

## How it works
1. Defines `reverse(arr, start, end)`.
2. Base condition: if `start >= end`, pointers have met or crossed, so return 0.
3. Swaps `arr[start]` and `arr[end]` using temporary variable `temp`.
4. Recursively calls `reverse(arr, start + 1, end - 1)`.
5. Prints the inverted array.

## Sample run
> [!note] Traced from the source, not executed.
> In `main()`, the call `reverse(size - 1, 0);` omits the first argument `arr`, and line 18 is missing a terminating semicolon. When corrected to `reverse(arr, 0, size - 1);`, the output is:

```text
47652
```

## Gotchas
> [!bug] Missing Argument and Semicolon
> `reverse()` expects 3 arguments `(int arr[], int start, int end)`, but `main` calls it with only 2 arguments `reverse(size - 1, 0);`. In addition, line 18 (`printf("\n")`) omits the ending semicolon.

## My notes
> [!question]- My notes

## Related
- [[LAB 23 - pointer array reverse]]
- [[CLASS 17 - pointer string reverse]]
