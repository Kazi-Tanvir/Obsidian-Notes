---
title: "PRAC CW 03 - pointer reverse"
aliases:
  - pointer reverse
  - 03_pointer_reverse
tags:
  - type/practice
  - c/pointers
  - c/arrays
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/CONCEPT_WISE/03_pointer_reverse.c"
up: "[[PRAC - Index]]"
related:
  - "[[LAB 23 - pointer array reverse]]"
created: 2026-10-29
status: draft
---
# PRAC CW 03 - pointer reverse

> [!abstract] Summary
> Reverses an integer array in place using two converging pointer indices.

**Source:** `PRACTICE/CONCEPT_WISE/03_pointer_reverse.c`

## Problem
Demonstrate pointer arithmetic and memory addressing fundamentals by implementing `pointer reverse` directly in C.

## Concepts used
- **Pointer Addressing & Dereferencing:** Accessing and mutating memory locations directly via pointer variables.
- **Pointer Offset Arithmetic:** Moving through memory sequentially using `*(p + i)`.

## Code
```c
#include<stdio.h>

void reverse(int *start, int *end){
    if(start >= end) return ;
    int temp = *end;
    *end = *start;
    *start = temp ;
    reverse(start + 1, end - 1);
}
int main(){
    int N;
    scanf("%d",&N);
    int arr[N];

    for( int i = 0; i < N;i++){
        scanf("%d",arr + i);
    }
    reverse(arr, arr + N - 1);

    for(int i = 0; i < N; i++){
        printf("%d ",*(arr+i));
    }
    
}
```

## How it works
1. Initializes inputs or reads from standard input.
2. Manipulates data memory addresses directly using pointer references.
3. Produces output verifying in-place memory mutation.

## My notes
> [!question]- My notes

## Related
- [[LAB 23 - pointer array reverse]]
