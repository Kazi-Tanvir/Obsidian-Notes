---
title: "PRAC CW 04 - pointer strlen"
aliases:
  - pointer strlen
  - 04_pointer_strlen
tags:
  - type/practice
  - c/pointers
  - c/strings
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/CONCEPT_WISE/04_pointer_strlen.c"
up: "[[PRAC - Index]]"
related:
  - "[[CLASS 12 - pointer strlen]]"
created: 2026-10-29
status: draft
---
# PRAC CW 04 - pointer strlen

> [!abstract] Summary
> Calculates string length by incrementing a pointer until reaching the null byte.

**Source:** `PRACTICE/CONCEPT_WISE/04_pointer_strlen.c`

## Problem
Demonstrate pointer arithmetic and memory addressing fundamentals by implementing `pointer strlen` directly in C.

## Concepts used
- **Pointer Addressing & Dereferencing:** Accessing and mutating memory locations directly via pointer variables.
- **Pointer Offset Arithmetic:** Moving through memory sequentially using `*(p + i)`.

## Code
```c
#include<stdio.h>

void my_strlen(const char *str){
    int i;
    for(i = 0 ; *(str++);i++);
    printf("%d",i);
}

int main(){
    char str[] = "KaziTanvir";
    my_strlen(str);
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
- [[CLASS 12 - pointer strlen]]
