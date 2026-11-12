---
title: "CLASS 09 - string copy"
aliases:
  - string copy
  - 09_string_copy
tags:
  - type/lecture
  - c/strings
  - c/arrays
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/09_string_copy.c"
number: 9
up: "[[CLASS - Index]]"
prev: "[[CLASS 08 - string length]]"
next: "[[CLASS 10 - string check equal]]"
related:
  - "[[CLASS 13 - pointer strcpy]]"
  - "[[LAB 12 - swap array]]"
created: 2026-10-29
status: draft
---
# CLASS 09 - string copy

> [!abstract] Summary
> Demonstrates manual byte-by-byte string copying into a destination buffer with explicit null-termination versus standard `strcpy()`.

**Source:** `CLASS/09_string_copy.c`

## Problem
In C, arrays cannot be copied using the assignment operator (`str2 = str1;` will result in a compiler error because array names are non-modifiable lvalues). We must copy strings character by character from the source buffer into the destination buffer.

## Concepts used
- **Character Transfer**: Reading `str1[i]` and writing it to `str2[i]` within a loop.
- **Explicit Termination**: A manual copy loop must explicitly write `str2[i] = '\0'` after the characters have been copied; otherwise, reading `str2` will print trailing garbage memory.
- **Standard `strcpy`**: The standard `<string.h>` library function that copies bytes until `'\0'` is transferred.

## Code
```c
#include<stdio.h>
#include <string.h>

int main(){
    char str1[] = "Kazi";
    char str2[10];
    char str3[10];

    // using for loop
    int i;
    for(i = 0; str1[i] != '\0'; i++){
        str2[i] = str1[i];
    }
    str2[i] = '\0';


    // directly using strcpy from string library
    strcpy(str3, str1);
    printf(str2);
    printf("\n");
    printf(str3);
    return 0;
}
```

## How it works
1. **Buffer Allocation**: Source `str1[] = "Kazi"` is initialized with 5 bytes (`'K', 'a', 'z', 'i', '\0'`). Destination `str2[10]` is an uninitialized 10-byte buffer.
2. **Manual Copy Loop**:
   - `for (i = 0; str1[i] != '\0'; i++) str2[i] = str1[i];`
   - Copies each character index by index.
3. **Null Termination**: When the loop encounters `str1[4] == '\0'`, the loop terminates. The critical statement `str2[i] = '\0';` places the null terminator at index 4 of `str2`.
4. **Verification**: Outputs `str2` (copied manually) and copies again using `strcpy(str2, str1)`.

## Sample run
```text
Kazi
Kazi
```

## Gotchas
> [!warning] Destination Buffer Overflow
> The destination buffer `str2` must have capacity strictly greater than the source string length (>= length + 1). If `str1` contains 15 characters, copying it into `str2[10]` overflows `str2`, overwriting neighboring stack variables and causing undefined behavior.

## My notes
> [!question]- My notes

## Related
- [[CLASS 13 - pointer strcpy]] - Implementing string copy using pointer dereference idioms
- [[LAB 12 - swap array]] - Copying and swapping arrays in memory
