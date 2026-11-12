---
title: "PRAC CW 09 - file char space newline counter"
aliases:
  - file char space newline counter
  - 09_file_char_space_newline_counter
tags:
  - type/practice
  - c/file-io
  - c/strings
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/CONCEPT_WISE/09_file_char_space_newline_counter.c"
up: "[[PRAC - Index]]"
related:
  - "[[CLASS 22 - space finder]]"
created: 2026-10-29
status: draft
---
# PRAC CW 09 - file char space newline counter

> [!abstract] Summary
> Reads an external text file character by character, tallying total characters, spaces, and newlines.

**Source:** `PRACTICE/CONCEPT_WISE/09_file_char_space_newline_counter.c`

## Problem
Demonstrate pointer arithmetic and memory addressing fundamentals by implementing `file char space newline counter` directly in C.

## Concepts used
- **Pointer Addressing & Dereferencing:** Accessing and mutating memory locations directly via pointer variables.
- **Pointer Offset Arithmetic:** Moving through memory sequentially using `*(p + i)`.

## Code
```c
#include<stdio.h>
#include<stdlib.h>

int main(){
    FILE *fp = fopen("text.txt", "r");
    if(fp == NULL) exit(1);
    int char_counter = 0;
    int space_counter = 0;
    int newline_counter = 0;
    char ch;
    
    for(int i = 0;(ch = fgetc(fp))!= EOF;i++){
        int ascii = ch;
        if(ascii >= 0 && ascii <= 255) char_counter++;
        if(ch == ' ') space_counter++;
        if(ch == '\n') newline_counter++;
        printf("%d",i);

    }
    printf("%d %d %d",char_counter,space_counter,newline_counter );
}
```

## How it works
1. Initializes inputs or reads from standard input.
2. Manipulates data memory addresses directly using pointer references.
3. Produces output verifying in-place memory mutation.

## My notes
> [!question]- My notes

## Related
- [[CLASS 22 - space finder]]
