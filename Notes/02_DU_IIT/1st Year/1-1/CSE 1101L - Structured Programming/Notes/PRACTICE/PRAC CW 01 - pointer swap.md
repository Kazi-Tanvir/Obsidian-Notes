---
title: "PRAC CW 01 - pointer swap"
aliases:
  - pointer swap
  - 01_pointer_swap
tags:
  - type/practice
  - c/pointers
  - c/functions
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/CONCEPT_WISE/01_pointer_swap.c"
up: "[[PRAC - Index]]"
related:
  - "[[LAB 01 - change var temp]]"
created: 2026-10-29
status: draft
---
# PRAC CW 01 - pointer swap

> [!abstract] Summary
> Swaps two integers using pass-by-reference pointer parameters.

**Source:** `PRACTICE/CONCEPT_WISE/01_pointer_swap.c`

## Problem
Demonstrate pointer arithmetic and memory addressing fundamentals by implementing `pointer swap` directly in C.

## Concepts used
- **Pointer Addressing & Dereferencing:** Accessing and mutating memory locations directly via pointer variables.
- **Pointer Offset Arithmetic:** Moving through memory sequentially using `*(p + i)`.

## Code
```c
#include<stdio.h>

void swap(int* a , int* b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(){
    int x = 5 , y = 10;
    printf("x:%d\ny:%d\n",x,y);
    swap(&x,&y);
    printf("x:%d\ny:%d\n",x,y);
    return 0;
}
```

## How it works
1. Initializes inputs or reads from standard input.
2. Manipulates data memory addresses directly using pointer references.
3. Produces output verifying in-place memory mutation.

## My notes
> [!question]- My notes

## Related
- [[LAB 01 - change var temp]]
