---
title: "CLASS 12 - pointer strlen"
aliases:
  - pointer strlen
  - 12_pointer_strlen
tags:
  - type/lecture
  - c/pointers
  - c/strings
  - c/pointer-arithmetic
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "CLASS/12_pointer_strlen.c"
number: 12
up: "[[CLASS - Index]]"
prev: "[[CLASS 11 - string merge]]"
next: "[[CLASS 13 - pointer strcpy]]"
related:
  - "[[CLASS 08 - string length]]"
  - "[[PRAC CW 04 - pointer strlen]]"
created: 2026-10-29
status: draft
---
# CLASS 12 - pointer strlen

> [!abstract] Summary
> Computes string length using raw pointer dereferencing and post-increment traversal idioms.

**Source:** `CLASS/12_pointer_strlen.c`

## Problem
Calculate the length of a null-terminated string by traversing memory directly via pointer arithmetic rather than using array bracket indexing (`str[i]`).

## Concepts used
- **Pointer as Memory Iterator (`char *str`)**: In C, an array name decays to a pointer to its first element. Pointers can directly traverse contiguous memory.
- **Dereference Operator (`*`)**: Accesses the byte value stored at the memory address currently held by the pointer.
- **Post-Increment (`str++`)**: Advances the pointer to the next memory address (by `sizeof(char)` = 1 byte) *after* yielding its current address for evaluation.
- **Truthiness in Loop Conditions**: In C, non-zero integer values evaluate to true, while zero (`'\0'`) evaluates to false. Thus, `*(str++)` automatically terminates when pointing to the null byte.

## Code
```c
#include<stdio.h>

int my_strlen(char *str){
    int i;
    for(i = 0; *(str++);i++);
    return i;
}

int main(){
    char str[10] = "Kazi";
    printf("%d",my_strlen(str));
    return 0;
}
```

## How it works
1. **Passing the Pointer**: In `main()`, `char x[] = "Kazi";` allocates 5 bytes on the stack. Calling `my_strlen(x)` passes the address of `x[0]` into pointer parameter `char *str`.
2. **Loop Condition `for(i = 0; *(str++); i++);`**:
   - On each step, `*(str++)` dereferences the current character to test if it is non-zero (not `'\0'`).
   - Simultaneously, `str` is incremented to the next memory address.
   - If the character was non-zero, the loop body increments counter `i`.
3. **Termination**: When `str` points to `'\0'`, `*(str++)` evaluates to 0 (false), the loop terminates, and `i` (which equals 4) is returned.

## Sample run
```text
4
```

## Gotchas
> [!warning] Side-Effects in Loop Conditions
> The idiom `*(str++)` inside a `for` condition has an important side effect: even on the iteration where `*str` is `'\0'` (causing the loop to terminate), the post-increment `str++` **still executes**, advancing `str` one byte past the null terminator! While safe here because `i` tracks the count independently, relying on `str`'s final address after the loop requires accounting for this extra advance.

## My notes
> [!question]- My notes

## Related
- [[CLASS 08 - string length]] - Array indexing version of string length
- [[PRAC CW 04 - pointer strlen]] - Concept-wise drill on pointer string metrics
