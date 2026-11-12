---
title: "CLASS 14 - pointer strcmp"
aliases:
  - pointer strcmp
  - 14_pointer_strcmp
tags:
  - type/lecture
  - c/pointers
  - c/strings
  - c/pointer-arithmetic
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "CLASS/14_pointer_strcmp.c"
number: 14
up: "[[CLASS - Index]]"
prev: "[[CLASS 13 - pointer strcpy]]"
next: "[[CLASS 15 - pointer strcat]]"
related:
  - "[[CLASS 10 - string check equal]]"
  - "[[ASG 05 - dictionary sort lexicographic]]"
created: 2026-10-29
status: draft
---
# CLASS 14 - pointer strcmp

> [!abstract] Summary
> Explores string comparison using dual pointer traversal and exposes subtle type-dereference pitfalls.

**Source:** `CLASS/14_pointer_strcmp.c`

## Problem
Compare two strings lexicographically using pointers to determine whether they contain the exact same sequence of characters.

## Concepts used
- **Dual Pointer Lockstep Traversal**: Incrementing two pointers (`x++`, `y++`) simultaneously to compare corresponding characters.
- **Pointer Dereferencing**: `*x == *y` evaluates character equality at the current memory locations.
- **Type Signatures in Standard Library Functions**: Understanding that standard functions like `strlen` require pointer addresses (`const char *`), not dereferenced characters (`char`).

## Code
```c
#include<stdio.h>

int my_strcmp(char *x, char *y){
    int i;
    if(strlen(*x)!= strlen(*y)) return 0;
    for(i = 0; *x++ == *y++ ; i++){
    }
    if(i == strlen(*x)) return 1;
    return 0;
}

int main(){
    char x[] = "Tanvir";
    char y[] = "Tanvir";
    printf("%d",my_strcmp(x, y));
    return 0;
}
```

## How it works
1. **Intended Logic**:
   - First compare string lengths; if lengths differ, return `0` (not equal).
   - Iterate while `*x++ == *y++`, tracking count `i`.
   - If `i` reaches the string length, return `1` (equal).
2. **Main Routine**: Declares `x[] = "Tanvir"` and `y[] = "Tanvir"`, passes them to `my_strcmp(x, y)`, and prints the result.

## Sample run
> [!note] Traced from the source, not executed.
> This program does not compile as written due to type mismatch errors. The intended output for identical strings is `1`.

## Gotchas
> [!warning] Dereferencing Pointers into `strlen`
> The program contains critical syntax/type bugs:
> 1. **Dereferencing into `strlen`**: Line 5 writes `if (strlen(*x) != strlen(*y))`. But `*x` is a `char` (a single character byte), whereas `strlen` expects a pointer `const char *`! Passing a `char` to `strlen` forces the compiler to interpret an ASCII integer (e.g. `'T'` = 84) as a memory address, triggering compiler errors or segmentation faults. It should be `strlen(x) != strlen(y)`.
> 2. **Missing Header**: The file uses `strlen` without `#include <string.h>`.

## My notes
> [!question]- My notes

## Related
- [[CLASS 10 - string check equal]] - Array-based string comparison
- [[ASG 05 - dictionary sort lexicographic]] - Alphabetical string comparison and sorting
