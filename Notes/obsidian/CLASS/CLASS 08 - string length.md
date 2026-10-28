---
title: "CLASS 08 - string length"
aliases:
  - string length
  - 08_string_length
tags:
  - type/lecture
  - c/strings
  - c/loops
  - c/arrays
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/08_string_length.c"
number: 8
up: "[[CLASS - Index]]"
prev: "[[CLASS 07 - avg temperature array]]"
next: "[[CLASS 09 - string copy]]"
related:
  - "[[CLASS 12 - pointer strlen]]"
  - "[[PRAC CW 04 - pointer strlen]]"
created: 2026-10-29
status: draft
---
# CLASS 08 - string length

> [!abstract] Summary
> Computes the length of a string manually by iterating until the null terminator (`\0`) and compares the result against standard `strlen()`.

**Source:** `CLASS/08_string_length.c`

## Problem
In C, strings are not built-in high-level objects; they are raw character arrays terminated by a special zero byte (`'\0'`). We need to count how many printable characters precede this terminator.

## Concepts used
- **Null Terminator (`'\0'`)**: The sentinel character with byte value 0 marking the end of a string in C. Without it, string functions would not know where the string ends in memory.
- **Manual Traversal**: Iterating through array indices `str[i]` with a `while` loop until the null terminator is encountered.
- **Standard Library `strlen`**: Function from `<string.h>` that returns the number of characters excluding the null byte.

## Code
```c
#include<stdio.h>
#include <string.h>

int main(){
    char str[100];
    scanf("%s", str);
    // using for loop
    int count = 0;
    for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
    printf("%d\n", count);

    // directly using strlen from string library
    printf("%d\n", strlen(str));

    return 0;
}
```

## How it works
1. **Buffer Allocation**: `char str[100];` creates a 100-byte character buffer.
2. **String Input**: `scanf("%s", str)` reads a word from stdin, storing characters into `str` and appending a null byte `'\0'`.
3. **Linear Scanning**:
   - `int count = 0;`
   - `while (str[count] != '\0') count++;`
   - Increments `count` as long as the current character is not the null terminator.
4. **Verification**: Prints both the manual `count` and the result of `strlen(str)` to verify equivalence.

## Sample run
```text
HelloWorld
10
10
```

## Gotchas
> [!warning] Buffer Overflow & Whitespace Truncation
> 1. **Buffer Overflow**: `scanf("%s", str)` does not restrict the number of characters read. An input of 105 characters into a 100-byte buffer will write 5 bytes past the buffer end, corrupting stack memory. Safe alternative: `scanf("%99s", str)`.
> 2. **Whitespace Truncation**: `scanf("%s")` stops reading at the first whitespace. For input `"Hello World"`, only `"Hello"` (length 5) is read.

## My notes
> [!question]- My notes

## Related
- [[CLASS 12 - pointer strlen]] - Re-implementing string length using raw pointers
- [[PRAC CW 04 - pointer strlen]] - Pointer drill calculating string length
