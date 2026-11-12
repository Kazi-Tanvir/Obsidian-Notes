---
title: "LAB 17 - merge sort recursion"
aliases:
  - merge sort recursion
  - 17_merge_sort_recursion
tags:
  - type/lab
  - c/recursion
  - c/sorting
  - c/arrays
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "LAB/17_merge_sort_recursion.c"
number: 17
up: "[[LAB - Index]]"
prev: "[[LAB 16 - reverse array recursion]]"
next: "[[LAB 18 - pointer sort]]"
related:
  - "[[LAB 24 - merge sort]]"
  - "[[LAB 11 - sort array]]"
created: 2026-10-29
status: draft
---
# LAB 17 - merge sort recursion

> [!abstract] Summary
> Implements the classic divide-and-conquer Merge Sort algorithm using purely recursive functions for both splitting and merging without iterative `while` loops.

**Source:** `LAB/17_merge_sort_recursion.c`

## Problem
Sort an array of integers with $O(n \log n)$ time complexity using recursive divide-and-conquer Merge Sort, structuring the merge step itself as a recursive traversal.

## Concepts used
- **Divide and Conquer:** Recursively halving the array into left and right sub-arrays around `mid = left + (right - left) / 2`.
- **Recursive Merging (`mergeElements`):** Comparing the heads of two sorted subarrays recursively and placing the smaller item into `temp[k]`.
- **Recursive Array Copying (`copyElements`):** Copying sorted elements from `temp` back into `arr` via recursive indexing instead of an iterative loop.

## Code
```c
#include <stdio.h>

void copyElements(int arr[], int temp[], int right, int k){
    if (k > right) return;
    arr[k] = temp[k];
    copyElements(arr, temp, right, k + 1);
}

void mergeElements(int arr[], int temp[], int mid, int right, int i, int j, int k){
    if (i > mid && j > right) return;
    if (i > mid) {
        temp[k] = arr[j];
        mergeElements(arr, temp, mid, right, i, j + 1, k + 1);
    } else if (j > right) {
        temp[k] = arr[i];
        mergeElements(arr, temp, mid, right, i + 1, j, k + 1);
    } else if (arr[i] <= arr[j]) {
        temp[k] = arr[i];
        mergeElements(arr, temp, mid, right, i + 1, j, k + 1);
    } else {
        temp[k] = arr[j];
        mergeElements(arr, temp, mid, right, i, j + 1, k + 1);
    }
}

void mergeSort(int arr[], int temp[], int left, int right){
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSort(arr, temp, left, mid);
    mergeSort(arr, temp, mid + 1, right);
    mergeElements(arr, temp, mid, right, left, mid + 1, left);
    copyElements(arr, temp, right, left);
}

int main(){
    int arr[] = {75, 90, 40, 85, 60, 55, 100, 35};
    int len = sizeof(arr) / sizeof(arr[0]);
    int temp[len]; 
    
    mergeSort(arr, temp, 0, len - 1);
    
    printf("Sorted Array: \n");
    for(int i = 0; i < len; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
```

## How it works
1. `mergeSort(arr, temp, left, right)` checks if `left >= right`; if so, a single element is already sorted.
2. Calculates `mid`, then recursively sorts the left half (`left` to `mid`) and right half (`mid + 1` to `right`).
3. Calls `mergeElements` with pointers $i = left$ and $j = mid + 1$:
   - If $i > mid$, picks remaining elements from right half.
   - If $j > right$, picks remaining elements from left half.
   - Otherwise picks whichever element `arr[i]` or `arr[j]` is smaller.
4. Recursively increments indices until both halves are exhausted.
5. `copyElements` transfers sorted elements from `temp` back into `arr`.

## Sample run
```text
Sorted Array: 
35 40 55 60 75 85 90 100 
```

## Gotchas
> [!warning] Stack Frame Depth in Recursive Merge
> While replacing `while` loops with recursive functions (`mergeElements` and `copyElements`) demonstrates pure recursion elegance, it adds $O(n)$ stack frames per merge step, increasing the risk of stack overflow on large inputs compared to standard iterative merging.

## My notes
> [!question]- My notes

## Related
- [[LAB 24 - merge sort]]
- [[LAB 11 - sort array]]
