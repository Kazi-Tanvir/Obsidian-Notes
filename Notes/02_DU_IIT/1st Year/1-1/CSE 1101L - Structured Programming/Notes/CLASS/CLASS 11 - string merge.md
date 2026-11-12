---
title: "CLASS 11 - string merge"
aliases:
  - string merge
  - 11_string_merge
tags:
  - type/lecture
  - c/strings
  - c/arrays
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/11_string_merge.c"
number: 11
up: "[[CLASS - Index]]"
prev: "[[CLASS 10 - string check equal]]"
next: "[[CLASS 12 - pointer strlen]]"
related:
  - "[[CLASS 15 - pointer strcat]]"
  - "[[LAB 14 - merge array]]"
created: 2026-10-29
status: draft
---
# CLASS 11 - string merge

> [!abstract] Summary
> Concatenates two strings manually by locating the destination string's null terminator, appending source characters, and re-terminating with `\0`.

**Source:** `CLASS/11_string_merge.c`

## Problem
Merge two distinct strings (e.g. `"Kazi "` and `"Tanvir"`) into a single concatenated string in memory without relying on standard library functions.

## Concepts used
- **String Concatenation Mechanics**: Locating the existing end of the primary string (index where `str1[len1] == '\0'`) and copying characters of the secondary string starting from that index.
- **Sentinel Preservation**: Ensuring that the final concatenated string concludes with a valid null terminator (`'\0'`).
- **Buffer Capacity**: The destination array must have adequate capacity to hold `strlen(str1) + strlen(str2) + 1` bytes.

## Code
```c
#include<stdio.h>
#include<string.h>

int main(){
    char str1[10] = "Kazi ";
    char str2[10] = "Tanvir";
    char str3[20];

    int len1 = strlen(str1);
    int len2 = strlen(str2);

    // manual process
    for(int i = 0; i < len1; i++){
        str3[i] = str1[i];
    }
    for(int i = 0; i < len2; i++){
        str3[len1 + i] = str2[i];
    }
    str3[len1 + len2] = '\0';
    printf(str3);
    printf("\n");


    // using built in function
    printf(strcat(str1, str2));
    printf("\n");
    

    return 0;
}
```

## How it works
1. **Initial State**: `str1` contains `"Kazi "` and `str2` contains `"Tanvir"`.
2. **Finding Destination End**:
   - `while (str1[len1] != '\0') len1++;`
   - Scans `str1` to find the index of its null terminator (index 5).
3. **Appending Characters**:
   - `for (int i = 0; str2[i] != '\0'; i++) str1[len1 + i] = str2[i];`
   - Copies characters from `str2` into `str1` starting immediately at index 5.
4. **Final Termination**: Explicitly places `str1[len1 + i] = '\0'`.
5. **Output**: Prints the concatenated string `str1`.

## Sample run
```text
Kazi Tanvir
Kazi Tanvir
```

## Gotchas
> [!warning] Stack Buffer Overflow
> Examine the array declaration:
> ```c
> char str1[10] = "Kazi ";
> char str2[10] = "Tanvir";
> ```
> `str1` is allocated exactly **10 bytes**. `"Kazi "` is 5 characters, and `"Tanvir"` is 6 characters. Merging them produces a string of length 5 + 6 = 11 characters, requiring **12 bytes** (including `'\0'`)! Writing 12 bytes into a 10-byte buffer overflows `str1` by 2 bytes, silently corrupting stack variables. In C, always ensure destination buffers are generously sized (e.g. `char str1[50]`).

## My notes
> [!question]- My notes

## Related
- [[CLASS 15 - pointer strcat]] - Concatenation using pointer arithmetic
- [[LAB 14 - merge array]] - Merging numerical arrays in memory
