---
title: "CLASS 18 - pointer books 2d arr"
aliases:
  - pointer books 2d arr
  - 18_pointer_books_2d_arr
tags:
  - type/lecture
  - c/pointers
  - c/arrays
  - c/strings
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "CLASS/18_pointer_books_2d_arr.c"
number: 18
up: "[[CLASS - Index]]"
prev: "[[CLASS 17 - pointer string reverse]]"
next: "[[CLASS 19 - pointer row sum]]"
related:
  - "[[CLASS 19 - pointer row sum]]"
  - "[[LAB 28 - matrix]]"
  - "[[ASG 07 - book reservation]]"
created: 2026-10-29
status: draft
---
# CLASS 18 - pointer books 2d arr

> [!abstract] Summary
> Explores ragged arrays of string pointers (`char *book[20]`) and illustrates the critical requirement for dynamic memory allocation.

**Source:** `CLASS/18_pointer_books_2d_arr.c`

## Problem
Maintain an indexed catalog of 20 book titles using an array of pointers (`char *book[20]`) and read multi-word titles containing spaces from user input.

## Concepts used
- **Array of Pointers (`char *book[20]`)**: An array where each element is not a character, but an address pointer capable of pointing to a character string in memory.
- **Ragged Array Principle**: Unlike a fixed 2D grid (`char book[20][100]`) where each row consumes 100 bytes regardless of title length, pointer arrays allow each title to consume only as much memory as its actual string length requires.
- **Scanset Specifier (`scanf(" %[^
]", ...)`)**: Reads characters including spaces until a newline is encountered.

## Code
```c
void book(){
    char *book[20];
    for(int i = 0; i < 20 ;i++){
        scanf(" %[\n]",book[i]);
    }
    for(int i = 0; i < 20 ;i++){
        printf("%s\n",book[i]);
    }
}

int main(){
    book();
    return 0;
}
```

## How it works
1. **Declaration**: `char *book[20];` allocates 20 pointer variables (each 8 bytes on 64-bit systems = 160 bytes total on the stack).
2. **Input Attempt**: Loops `i` from 0 to 19, attempting `scanf(" %[^
]", book[i])`.
3. **Display Attempt**: Loops through `book[i]` printing each string.

## Sample run
> [!note] Traced from the source, not executed.
> Executing this code triggers an immediate **Segmentation Fault (Crash)** due to dereferencing uninitialized wild pointers.

## Gotchas
> [!warning] Fatal Segmentation Fault: Unallocated Pointer Array
> `char *book[20];` creates 20 pointer variables, but **allocates zero bytes of storage for the actual strings**!
> The pointers contain indeterminate stack garbage addresses. When `scanf` attempts to write characters into the memory address held by `book[i]`, it writes into an illegal, unmapped, or protected memory page, causing the OS kernel to instantly terminate the process with a Segmentation Fault!
> **Correct Fix**: Allocate memory for each pointer before reading into it:
> ```c
> for (int i = 0; i < 20; i++) {
>     book[i] = malloc(100 * sizeof(char));
>     scanf(" %[^
]", book[i]);
> }
> ```

## My notes
> [!question]- My notes

## Related
- [[CLASS 19 - pointer row sum]] - 2D matrix memory layout
- [[LAB 28 - matrix]] - 2D matrix computation
- [[ASG 07 - book reservation]] - Complete book reservation system with structures
