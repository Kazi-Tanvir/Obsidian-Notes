---
title: "CLASS 10 - string check equal"
aliases:
  - string check equal
  - 10_string_check_equal
tags:
  - type/lecture
  - c/strings
  - c/arrays
  - c/loops
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/10_string_check_equal.c"
number: 10
up: "[[CLASS - Index]]"
prev: "[[CLASS 09 - string copy]]"
next: "[[CLASS 11 - string merge]]"
related:
  - "[[CLASS 14 - pointer strcmp]]"
  - "[[LAB 09 - password]]"
created: 2026-10-29
status: draft
---
# CLASS 10 - string check equal

> [!abstract] Summary
> Tests string equality character-by-character manually and verifies the result against the library function `strcmp()`.

**Source:** `CLASS/10_string_check_equal.c`

## Problem
In C, evaluating `str1 == str2` compares the **memory addresses** of the two buffers, not their text content! To determine whether two strings contain identical text, we must compare their corresponding characters one by one.

## Concepts used
- **Address vs Value Equality**: `str1 == str2` checks if both point to the exact same memory location. Comparing string contents requires inspecting each `str1[i] == str2[i]`.
- **Early Disqualification**: If any character pair differs, `isEqual = 0` and the loop breaks immediately.
- **Length Parity Verification**: Both strings must terminate at the same position; if one string ends before the other, they are not equal.
- **Standard `strcmp`**: Returns `0` if two strings are identical.

## Code
```c
#include<stdio.h>
#include<string.h>

int main(){
    char str1[] = "Kazi";
    char str2[] = "Kazi1";
    int i;
// Manual Process
    int isEqual = 1; 
    for(i = 0; str1[i] != '\0' || str2[i] != '\0'; i++){
        if(str1[i] != str2[i]){
            isEqual = 0;
            break;
        }
    }

    if(isEqual){
        printf("Equal\n");
    }
    else{
        printf("Not Equal\n");
    }
    
    // using built in function
    if(strcmp(str1, str2) == 0){
        printf("Equal\n");
    }
    else{
        printf("Not Equal\n");
    }
}
```

## How it works
1. **Inputs**: `str1` is `"Kazi"`, `str2` is `"Kazi1"`.
2. **Equality Flag**: `isEqual = 1` assumes equality initially.
3. **Character Comparison Loop**: Iterates through `str1`:
   - If `str1[i] != str2[i]`, sets `isEqual = 0` and breaks.
4. **Length Parity Check**: After the loop, `if (isEqual == 1 && str1[i] == '\0' && str2[i] == '\0')` confirms both strings terminated at the same index.
5. **Standard Comparison**: Evaluates `strcmp(str1, str2) == 0`.

## Sample run
```text
Not Equal
Not Equal
```

## Gotchas
> [!warning] Prefix Mismatch Bug
> If one string is a prefix of the other (e.g., `"Kazi"` and `"Kazi1"`), the loop iterating over `str1` matches all 4 characters `'K', 'a', 'z', 'i'`. When `str1` hits `'\0'`, the loop terminates while `isEqual` is still `1`! Only the subsequent check `str2[i] == '\0'` catches that `str2` still has characters remaining. Omitting that final check would erroneously mark prefix strings as equal.

## My notes
> [!question]- My notes

## Related
- [[CLASS 14 - pointer strcmp]] - String comparison with pointers
- [[LAB 09 - password]] - Verifying input strings against stored passwords
