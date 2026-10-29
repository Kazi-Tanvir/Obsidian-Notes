---
title: "LAB 12 - swap array"
aliases:
  - swap array
  - 12_swap_array
tags:
  - type/lab
  - c/arrays
  - c/loops
  - c/searching
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/12_swap_array.c"
number: 12
up: "[[LAB - Index]]"
prev: "[[LAB 11 - sort array]]"
next: "[[LAB 13 - remove item]]"
related:
  - "[[LAB 19 - pointer swap]]"
  - "[[LAB 01 - change var temp]]"
created: 2026-10-29
status: draft
---
# LAB 12 - swap array

> [!abstract] Summary
> Searches an integer array for occurrences of a user-specified target value and substitutes them with a replacement value in place.

**Source:** `LAB/12_swap_array.c`

## Problem
Take an integer array of size $n$, prompt the user for target value $x$ and replacement value $y$, find all occurrences of $x$ in the array, replace them with $y$, and print the modified array.

## Concepts used
- **Linear Array Traversal:** Iterating through each index $0 \le i < n$ using a loop.
- **Conditional Value Replacement:** Comparing `arr[i] == a` and reassigning `arr[i] = b`.
- **Commented Dead Code:** Traces of two-array swapping experiments commented out in the source file.

## Code
```c
#include<stdio.h>

int main(){
    int n,a,b;
    printf("Enter the length of array :");
    scanf("%d",&n);
    int arr[n];


    //input 
    printf("Enter you %d integers for arr:", n);
    for(int i = 0; i < n;i++){
        scanf("%d",&arr[i]);
    }
    // printf("Enter you %d integers for y:", n);
    // for(int i = 0; i < n;i++){
    //         scanf("%d",&y[i]);
    // }
    printf("Enter x :");
    scanf("%d" ,&a);
    printf("Enter y :");
    scanf("%d",&b);
    //swap
    for(int i = 0; i<n ; i++){
        if(arr[i] == a){
            arr[i] = b;
        }
    }

    printf("Swapped Array X\n");
    for(int i = 0; i < n;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");

    // printf("Swapped Array Y\n");
    // for(int i = 0; i < n;i++){
    //     printf("%d ",y[i]);
    // }
    printf("\n");

}
```

## How it works
1. Reads array size `n` and populates `arr[n]` with user inputs.
2. Prompts for search value `a` (variable `x`) and replacement value `b` (variable `y`).
3. Iterates through indices $0$ to $n-1$; whenever `arr[i] == a`, it updates `arr[i] = b`.
4. Displays the updated array contents.

## Sample run
```text
Enter the length of array :5
Enter you 5 integers for arr:10 20 30 20 40
Enter x :20
Enter y :99
Swapped Array X
10 99 30 99 40 
```

## Gotchas
> [!warning] Value Substitution vs Element Exchange
> Despite the file name `12_swap_array.c`, this code performs value replacement rather than swapping two array positions or exchanging two separate arrays (which is commented out).

## My notes
> [!question]- My notes

## Related
- [[LAB 19 - pointer swap]]
- [[LAB 01 - change var temp]]
