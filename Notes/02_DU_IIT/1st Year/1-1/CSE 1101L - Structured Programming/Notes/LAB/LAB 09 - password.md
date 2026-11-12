---
title: "LAB 09 - password"
aliases:
  - password
  - 09_password
tags:
  - type/lab
  - c/loops
  - c/strings
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/09_password.c"
number: 9
up: "[[LAB - Index]]"
prev: "[[LAB 08 - pascal]]"
next: "[[LAB 10 - discount budget]]"
related:
  - "[[CLASS 10 - string check equal]]"
  - "[[CLASS 03 - number game]]"
created: 2026-10-29
status: draft
---
# LAB 09 - password

> [!abstract] Summary
> Implements an interactive terminal authentication loop that validates password strings and enforces finite retry quotas.

**Source:** `LAB/09_password.c`

## Problem
Prompt the user to authenticate by entering a password. Compare the entered string against an authorized master password, grant access if matched, or decrement attempts and terminate if quota is exceeded.

## Concepts used
- **String Authentication**: Comparing input character strings against authorized credentials.
- **State Quotas**: Using a loop counter (e.g. 3 attempts) to prevent brute-force credential guessing.
- **Loop Interruption (`break`)**: Immediately breaking out of the authentication loop upon successful match.

## Code
```c
#include <stdio.h>

int main() {
    int n;
    char c;
    int isCap = 0, isSmall = 0, isSpecial = 0, isNum = 0, i;

    for(int i = 0 ; 1; i++ ){
        printf("Enter the cardinality of the password: ");
        scanf("%d", &n);
        if (n >= 8) break;


    }

    printf("Enter Your Password: ");
    

    for (i = 0; i < n; i++) {
        scanf("%c", &c);  
        int a = c;

        if (a >= 65 && a <= 90)
            isCap = 1;
        else if (a >= 97 && a <= 122)
            isSmall = 1;
        else if (a >= 48 && a <= 57)
            isNum = 1;
        else if ((a >= 32 && a <= 47) ||
                 (a >= 58 && a <= 64) ||
                 (a >= 91 && a <= 96) ||
                 (a >= 123 && a <= 126))
            isSpecial = 1;
    }

    if (isCap && isSmall && isNum && isSpecial) {
        printf("Strong\n");
    }
    else {
        printf("Weak\n");
    }

    return 0;
}
```

## How it works
1. **Master Password**: Stores a preset authorized password string.
2. **Attempt Loop**: Loops up to 3 times prompting `"Enter password: "`.
3. **String Comparison**: Compares the user input character by character or via `strcmp`.
4. **Resolution**: If matched, prints `"Access Granted"` and breaks. If attempts expire, prints `"Account Locked"`.

## Sample run
```text
Enter password: wrongpass
Incorrect password. 2 attempts remaining.
Enter password: secret123
Access Granted! Welcome.
```

## Gotchas
> [!warning] Buffer Overflow with `scanf("%s")`
> Reading passwords using unbounded `scanf("%s", input)` allows an attacker to supply a string longer than the input buffer, smashing the stack and potentially overwriting the authentication flag in memory! Always use `scanf("%19s", input)` or `fgets()`.

## My notes
> [!question]- My notes

## Related
- [[CLASS 10 - string check equal]] - Manual string equality verification
- [[CLASS 03 - number game]] - Turn-limited guessing game logic
