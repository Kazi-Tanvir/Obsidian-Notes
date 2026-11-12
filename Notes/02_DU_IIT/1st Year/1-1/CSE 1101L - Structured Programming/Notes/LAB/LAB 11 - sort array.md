---
title: "LAB 11 - sort array"
aliases:
  - sort array
  - 11_sort_array
tags:
  - type/lab
  - c/sorting
  - c/arrays
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/11_sort_array.c"
number: 11
up: "[[LAB - Index]]"
prev: "[[LAB 10 - discount budget]]"
next: "[[LAB 12 - swap array]]"
related:
  - "[[LAB 18 - pointer sort]]"
  - "[[LAB 14 - merge array]]"
created: 2026-10-29
status: draft
---
# LAB 11 - sort array

> [!abstract] Summary
> Implements descending order array sorting via nested comparison loops (Selection/Bubble exchange pattern) and extracts the minimum and maximum elements.

**Source:** `LAB/11_sort_array.c`

## Problem
Prompt the user for the length of an integer array, read the elements, sort them in descending order, and report the sorted array along with the minimum and maximum values.

## Concepts used
- **Variable-Length Arrays (VLAs):** Sizing array `arr[n]` dynamically on the stack based on runtime user input.
- **Nested Comparison Loops:** Comparing every element at index $i$ with all subsequent elements at index $j > i$.
- **Descending Swap Logic:** Swapping `arr[i]` and `arr[j]` when `arr[j] > arr[i]` so that the largest values float toward index 0.
- **Extrema Retrieval:** In a descending sorted array of size $n$, maximum is at index $0$ and minimum is at index $n - 1$.

## Code
```c
#include<stdio.h>

int main(){
    int n;
    printf("Enter the length of array :");
    scanf("%d",&n);
    int arr[n];

    //input 
    printf("Enter you %d integers :", n);
    for(int i = 0; i < n;i++){
        scanf("%d",&arr[i]);
    }

    for(int i = 0;i<n;i++){
        for(int j = i + 1 ; j < n ;j++){
            if(arr[j]>arr[i]){
                int temp = arr[j];
                arr[j] = arr[i];
                arr[i] = temp;
            }
        }
    }

    printf("Sorted Array\n");
    for(int i = 0; i < n;i++){
        printf("%d ",arr[i]);
    }
    printf("The Minimum number is : %d\n" ,arr[n-1]);
    printf("The Maximum number is : %d\n" ,arr[0]);
    
    printf("\n");

}
```

## How it works
1. Prompts for length `n` and allocates stack array `arr[n]`.
2. Reads `n` integers into `arr` using a standard `for` loop.
3. The outer loop runs $i$ from $0$ to $n-1$. The inner loop runs $j$ from $i+1$ to $n-1$.
4. Whenever `arr[j] > arr[i]`, a temporary variable `temp` swaps the two values.
5. Prints the resulting array, followed by `arr[n-1]` (minimum) and `arr[0]` (maximum).

## Sample run
```text
Enter the length of array :5
Enter you 5 integers :12 45 7 23 89
Sorted Array
89 45 23 12 7 The Minimum number is : 7
The Maximum number is : 89
```

## Gotchas
> [!warning] Zero or Negative Array Sizes
> Entering $n \le 0$ produces undefined behavior when creating the variable-length array `arr[n]`, and reading `arr[n-1]` will access out-of-bounds memory.

## My notes
> [!question]- My notes

## Related
- [[LAB 18 - pointer sort]]
- [[LAB 14 - merge array]]
