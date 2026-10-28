---
title: "CLASS 05 - vowel switch"
aliases:
  - vowel switch
  - 05_vowel_switch
tags:
  - type/lecture
  - c/control-flow
  - c/strings
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/05_vowel_switch.c"
number: 5
up: "[[CLASS - Index]]"
prev: "[[CLASS 04 - prime number]]"
next: "[[CLASS 06 - calc menu switch]]"
related:
  - "[[CLASS 06 - calc menu switch]]"
  - "[[LAB 09 - password]]"
created: 2026-10-29
status: draft
---
# CLASS 05 - vowel switch

> [!abstract] Summary
> Classifies an input character as a vowel or consonant utilizing `switch-case` multi-case fallthrough.

**Source:** `CLASS/05_vowel_switch.c`

## Problem
Read a single character from the console and determine whether it is an English vowel (`a, e, i, o, u` in either lowercase or uppercase) or a consonant.

## Concepts used
- **`switch-case` Jump Tables**: A control structure where the compiler can generate an efficient jump table or binary search branch based on an integral/character expression.
- **Case Fallthrough**: Omitting a `break` statement causes execution to continue falling through into subsequent `case` blocks until a `break` is encountered.
- **Character Literals as Integers**: In C, `char` constants such as `'a'` are integer values corresponding to their ASCII codes.

## Code
```c
#include<stdio.h> 

int main(){
    char c;
    printf("Enter a character : ");
    scanf("%c", &c);
    switch(c){
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
            printf("Vowel");
            break;
        default:
            printf("Consonant");
    }
    return 0;
}
```

## How it works
1. **Character Input**: `scanf("%c", &c)` reads a single character code from standard input into `c`.
2. **Switch Dispatch**: `switch (c)` inspects the byte value of `c`.
3. **Fallthrough Matching**:
   - `case 'a': case 'e': case 'i': case 'o': case 'u':`
   - `case 'A': case 'E': case 'I': case 'O': case 'U':`
   All ten cases stack together without `break` statements. If `c` matches any of them, control falls into the shared statement `printf("Vowel\n"); break;`.
4. **Default Handler**: If no case matches, the `default:` branch executes `printf("Consonant\n");`.

## Sample run
```text
Enter a character : e
Vowel

Enter a character : Z
Consonant

Enter a character : 7
Consonant
```

## Gotchas
> [!warning] Non-Alphabetical Input Fallthrough
> The `default` branch labels *everything* that is not a vowel as a `"Consonant"`. If a user enters a digit (`'7'`), punctuation (`'!'`), or whitespace (`' '`), the program will report it as a consonant! Robust validation requires checking `isalpha(c)` first.

## My notes
> [!question]- My notes

## Related
- [[CLASS 06 - calc menu switch]] - Menu command routing using `switch`
- [[LAB 09 - password]] - Character inspection and classification in strings
