---
title: "PRAC CW 06 - pointer reverse string"
aliases:
  - pointer reverse string
  - 06_pointer_reverse_string
tags:
  - type/practice
  - c/pointers
  - c/strings
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/CONCEPT_WISE/06_pointer_reverse_string.c"
up: "[[PRAC - Index]]"
related:
  - "[[CLASS 17 - pointer string reverse]]"
created: 2026-10-29
status: draft
---
# PRAC CW 06 - pointer reverse string

> [!abstract] Summary
> Inverts a character string in place by swapping symmetric characters via pointers.

**Source:** `PRACTICE/CONCEPT_WISE/06_pointer_reverse_string.c`

## Problem
Demonstrate pointer arithmetic and memory addressing fundamentals by implementing `pointer reverse string` directly in C.

## Concepts used
- **Pointer Addressing & Dereferencing:** Accessing and mutating memory locations directly via pointer variables.
- **Pointer Offset Arithmetic:** Moving through memory sequentially using `*(p + i)`.

## Code
```c
// 6. Reverse String
// Reference: LeetCode #344 — Reverse String (Easy)
// Task: Write a function that reverses a string in-place. The input is given as an array of characters char* s.
// C Signature: void reverseString(char* s, int sSize)
// Pointer Concept: Two pointers (left and right) moving toward each other.
#include<stdio.h>
#include<string.h>

void reverseString(char* s, int sSize) {
    if(sSize <= 1 && sSize>= 100000) return;
    for(int i = 0 ; i < sSize ; i++){
        int ascii = s[i];
        if(ascii > 255 && ascii < 0) return;
    }

    for(int i = 0;i < sSize/2 ; i++){
        char temp = *(s + i);
        *(s + i) = *(s + sSize -1- i); 
        *(s + sSize - i-1) = temp;
    }
}

int main(){
    char str[100];
    fgets(str, sizeof(str), stdin);
    int sSize = strlen(str);

    reverseString(str , sSize);
    printf("%s\n",str);

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
- [[CLASS 17 - pointer string reverse]]
