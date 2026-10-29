---
title: "LAB 14 - merge array"
aliases:
  - merge array
  - 14_merge_array
tags:
  - type/lab
  - c/arrays
  - c/sorting
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/14_merge_array.c"
number: 14
up: "[[LAB - Index]]"
prev: "[[LAB 13 - remove item]]"
next: "[[LAB 15 - sum array recursion]]"
related:
  - "[[LAB 21 - pointer merge]]"
  - "[[LAB 17 - merge sort recursion]]"
created: 2026-10-29
status: draft
---
# LAB 14 - merge array

> [!abstract] Summary
> Combines two separate integer arrays into a single composite array and sorts the merged contents in descending order.

**Source:** `LAB/14_merge_array.c`

## Problem
Take two user-specified integer arrays of sizes $n$ and $m$, concatenate them into a third array of size $n+m$, and sort the merged array in descending order.

## Concepts used
- **Array Concatenation:** Copying array 1 into indices $0 \dots n-1$ of array 3, then copying array 2 starting at offset $n$ (`arr3[i + n] = arr2[i]`).
- **Composite Allocation:** Sizing `arr3[n+m]` to hold the sum of both lengths.
- **Descending Bubble/Selection Sort:** Nested loops swapping adjacent or out-of-order pairs.

## Code
```c
#include<stdio.h>

int main(){
    int n,m;
    printf("Enter the length of array arr1:");
    scanf("%d",&n);
    printf("Enter the length of array Y:");
    scanf("%d",&m);
    int arr1[n];
    int arr2[m];
    int arr3[n+m];


    //input 
    printf("Enter you %d integers for x:", n);
    for(int i = 0; i < n;i++){
        scanf("%d",&arr1[i]);
    }
    printf("Enter you %d integers for Y:", m);
    for(int i = 0; i < m;i++){
        scanf("%d",&arr2[i]);
    }

    for (int i = 0; i < n; i++) {
        arr3[i] = arr1[i];
    }

for (int i = 0; i < n+m; i++) {
    arr3[i + n] = arr2[i];
}




    for(int i = 0;i<n+m;i++){
        for(int j = i + 1 ; j < 10 ;j++){
            if(arr3[j]>arr3[i]){
                int temp = arr3[j];
                arr3[j] = arr3[i];
                arr3[i] = temp;
            }
        }
    }

    printf("Sorted array\n");
    for(int i = 0 ; i < m+n ; i++){
        printf("%d ",arr3[i]);
    }
        printf("\n");
}
```

## How it works
1. Reads lengths `n` and `m` and populates `arr1[n]` and `arr2[m]`.
2. First copies all $n$ elements from `arr1` into `arr3[0..n-1]`.
3. Second copies elements from `arr2` into `arr3[n..n+m-1]`.
4. Performs comparison swaps to sort `arr3` descending.
5. Prints the merged and sorted array `arr3`.

## Sample run
```text
Enter the length of array arr1:3
Enter the length of array Y:2
Enter you 3 integers for x:5 1 9
Enter you 2 integers for Y:8 3
Sorted array
83 9 8 8 5 
```

## Gotchas
> [!bug] Hardcoded Loop Boundary Bug
> In line 35, the inner sort loop is written as:
> `for(int j = i + 1 ; j < 10 ;j++)`
> The boundary `< 10` is hardcoded instead of `< n + m`. If $n + m < 10$, the loop reads uninitialized stack garbage beyond the allocated array (producing values like `83` in the sample run). If $n + m > 10$, elements beyond index 9 are never sorted!

## My notes
> [!question]- My notes

## Related
- [[LAB 21 - pointer merge]]
- [[LAB 17 - merge sort recursion]]
