---
title: "LAB 24 - merge sort"
aliases:
  - merge sort
  - 24_merge_sort
tags:
  - type/lab
  - c/sorting
  - c/pointers
  - c/recursion
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "LAB/24_merge_sort.c"
number: 24
up: "[[LAB - Index]]"
prev: "[[LAB 23 - pointer array reverse]]"
next: "[[LAB 25 - titanic p1]]"
related:
  - "[[LAB 17 - merge sort recursion]]"
  - "[[LAB 18 - pointer sort]]"
created: 2026-10-29
status: draft
---
# LAB 24 - merge sort

> [!abstract] Summary
> Implements an $O(n \log n)$ divide-and-conquer Merge Sort combining recursive sub-array division, recursive merging, and direct pointer arithmetic manipulation.

**Source:** `LAB/24_merge_sort.c`

## Problem
Sort an array of user-specified integers using recursive Merge Sort, manipulating all internal elements, comparisons, and temporary buffer transfers via pointer arithmetic.

## Concepts used
- **Divide and Conquer:** Recursively partitioning the array into halves until single-element base cases are reached.
- **Pointer-Based Merging:** Writing values to temporary buffer using `*(temp + k) = *(arr + i)` or `*(temp + k) = *(arr + j)`.
- **Recursive Sub-Routines:** Structuring both element merging (`mergeElements`) and copying (`copyElements`) as recursive functions.
- **Heap Dynamic Allocation:** Allocating input array `arr` and auxiliary merge buffer `temp` via `malloc`.

## Code
```c
#include <stdio.h>

void copyElements(int* arr, int* temp, int right, int k){
    if (k > right) return;
    *(arr+k) = *(temp+k);
    copyElements(arr, temp, right, k + 1);
}

void mergeElements(int* arr, int* temp, int mid, int right, int i, int j, int k){
    if (i > mid && j > right) return;
    if (i > mid) {
        *(temp+k) = *(arr+j);
        mergeElements(arr, temp, mid, right, i, j + 1, k + 1);
    } else if (j > right) {
        *(temp+k) = *(arr+i);
        mergeElements(arr, temp, mid, right, i + 1, j, k + 1);
    } else if (*(arr+i) <= *(arr+j)) {
        *(temp+k) = *(arr+i);
        mergeElements(arr, temp, mid, right, i + 1, j, k + 1);
    } else {
        *(temp+k) = *(arr+j);
        mergeElements(arr, temp, mid, right, i, j + 1, k + 1);
    }
}

void mergeSort(int *arr, int *temp, int left, int right){
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSort(arr, temp, left, mid);
    mergeSort(arr, temp, mid + 1, right);
    mergeElements(arr, temp, mid, right, left, mid + 1, left);
    copyElements(arr, temp, right, left);
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

    int *temp = (int*) malloc(n * sizeof(int));
    
    mergeSort(arr, temp, 0, n - 1);
    
    printf("Sorted Array: \n");
    for(int i = 0; i < n; i++) printf("%d ", *(arr+i));
    printf("\n");

    free(temp);
    free(arr);
    
    return 0;
}
```

## How it works
1. Prompts user for array length `n`, allocates heap memory for `arr` and auxiliary buffer `temp`.
2. Reads integers using `scanf("%d", arr + i)`.
3. `mergeSort(arr, temp, left, right)`:
   - Base case: `if (left >= right) return;`
   - Computes midpoint `mid = left + (right - left) / 2`.
   - Recursively sorts left half (`left` to `mid`) and right half (`mid + 1` to `right`).
   - Recursively merges both halves into `temp` using `mergeElements`.
   - Recursively copies merged items back from `temp` into `arr` using `copyElements`.
4. Prints the sorted elements via pointer offsets `*(arr + i)`.
5. Frees `temp` and `arr`.

## Sample run
> [!note] Traced from the source, not executed.
> Compiling with strict flags requires `#include <stdlib.h>` for `malloc` and `free`. Running with 5 inputs `45 12 89 23 7` outputs:

```text
Enter the length of array :5
Enter you 5 integers :45 12 89 23 7
Sorted Array: 
7 12 23 45 89 
```

## Gotchas
> [!warning] Missing `<stdlib.h>` Header
> The source file omits `#include <stdlib.h>`, which provides the function prototypes for `malloc` and `free`. Strict C99/C11 compilers will issue warnings or errors.

## My notes
> [!question]- My notes

## Related
- [[LAB 17 - merge sort recursion]]
- [[LAB 18 - pointer sort]]
