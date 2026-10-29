---
title: "LAB 23 - pointer array reverse"
aliases:
  - pointer array reverse
  - 23_pointer_array_reverse
tags:
  - type/lab
  - c/pointers
  - c/pointer-arithmetic
  - c/recursion
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "LAB/23_pointer_array_reverse.c"
number: 23
up: "[[LAB - Index]]"
prev: "[[LAB 22 - pointer recursion array sum]]"
next: "[[LAB 24 - merge sort]]"
related:
  - "[[LAB 16 - reverse array recursion]]"
  - "[[CLASS 17 - pointer string reverse]]"
created: 2026-10-29
status: draft
---
# LAB 23 - pointer array reverse

> [!abstract] Summary
> Attempts in-place recursive array reversal using pointer dereferencing with two converging boundary indices.

**Source:** `LAB/23_pointer_array_reverse.c`

## Problem
Invert an array of dynamically allocated integers recursively using two pointers (`start` and `end`) dereferenced via pointer arithmetic.

## Concepts used
- **Two-Pointer Recursive Inversion:** Exchanging symmetric boundary elements `*(arr + start)` and `*(arr + end)` and stepping inward.
- **Dynamic Allocation:** Allocating heap buffer for $n$ integers using `malloc`.
- **Pointer Swapping:** Using temporary storage `temp = *(arr + end)` to perform in-place swap.

## Code
```c
#include<stdio.h>

int reverse(int *arr,int start,int end){
    if(start >= end) return 0;
    int temp = *(arr+end);
    *(arr+end) = *(arr+start);
    *(arr+start) = temp ;
    return reverse(arr , start + 1 , end - 1);
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
    reverse(arr ,n - 1 , 0);
    for (int i = 0; i< n ; i++){
        printf("%d",*(arr+i));
    }
    printf("\n");
    free(arr);
}
```

## How it works
1. Reads array length `n` and allocates dynamic buffer `arr`.
2. Reads integers into `arr + i`.
3. In `reverse(int *arr, int start, int end)`:
   - Compares `start >= end`. If true, returns 0.
   - Swaps `*(arr + start)` and `*(arr + end)`.
   - Calls `reverse(arr, start + 1, end - 1)`.
4. Prints the array elements.
5. Frees heap memory.

## Sample run
> [!note] Traced from the source, not executed.
> In `main()`, the function is called as `reverse(arr, n - 1, 0)`. Because `start = n - 1` and `end = 0`, the base check `if (start >= end)` is immediately satisfied, so the function returns without swapping any elements!
> When corrected to `reverse(arr, 0, n - 1)`, input `1 2 3 4 5` outputs:

```text
54321
```

## Gotchas
> [!bug] Inverted Arguments Calling Bug
> Line 20 calls `reverse(arr, n - 1, 0)`. The function signature expects `(arr, start, end)`. Since `start = n - 1` is greater than or equal to `end = 0`, the function immediately exits at line 4 without performing any swaps. The correct invocation is `reverse(arr, 0, n - 1);`.

## My notes
> [!question]- My notes

## Related
- [[LAB 16 - reverse array recursion]]
- [[CLASS 17 - pointer string reverse]]
