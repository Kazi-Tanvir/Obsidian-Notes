---
title: "ASG 03 - hollow box and butterfly"
aliases:
  - hollow box and butterfly
  - hollow_box and butterfly
tags:
  - type/assignment
  - c/loops
  - c/control-flow
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "ASSIGNMENT/ASSIGNMENT_03/"
number: 3
up: "[[ASG - Index]]"
prev: "[[ASG 02 - pyramid patterns]]"
next: "[[ASG 04 - sort student by cgpa]]"
related:
  - "[[ASG 02 - pyramid patterns]]"
  - "[[LAB 07 - hollow triangle]]"
created: 2026-10-29
status: draft
---
# ASG 03 - hollow box and butterfly

> [!abstract] Summary
> Explores 2D coordinate boundary conditions to generate a customized hollow square box and a multi-character symmetric butterfly wing pattern.

**Source:** `ASSIGNMENT/ASSIGNMENT_03/hollow_box.c` and `butterfly.c`

## Problem
Create two distinct geometric coordinate patterns:
1. A customizable hollow box of size $n$ printing boundary characters on edges and spaces inside.
2. A symmetric butterfly pattern rendering alternating character textures (`*`, `=`, `\`, `/`, `@`) across upper and lower wings.

## Concepts used
- **Boundary Condition Masks:** Identifying boundary edges via boolean logical OR:
  $$i == 0 \lor i == n - 1 \lor j == 0 \lor j == n - 1$$
- **Multi-Zone Coordinate Mapping:** Splitting rows into upper wings, middle body (`@`), and lower wings.
- **Dynamic Character Customization:** Reading both dimension $n$ and custom boundary glyph $c$ using formatted `scanf`.

---

## Pattern Implementations & Code

### 1. Hollow Box (`hollow_box.c`)
```c
#include <stdio.h>

int main()

{

    int n;
    char c;

    printf("Enter Your number and char : ");
    scanf("%d %c", &n, &c);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 || i == n - 1 || j == 0 || j == n - 1)
                printf("%c", c);
            else
                printf(" ");
        }
        printf("\n");
    }
    return 0;
}
```
**Sample Run ($n = 4, c = '*'$):**
```text
Enter Your number and char : 4 *
****
*  *
*  *
****
```

### 2. Symmetrical Butterfly (`butterfly.c`)
```c
#include <stdio.h>

void print(int n, char c){
    for (int i = 0; i <= 2 * (n - 2) ; i++)
    {
        i == n - 2 ? printf("\\ /") : printf("%c", c);
    }
}

int main()  
{
    int n;

    printf("Enter Your number: ");
    scanf("%d", &n);
    
    int height = 2 * (n - 2) + 1;

    for (int i = 0; i < height; i++)
    {
        if (i == (height - 1) / 2)
        {
            for (int j = 0; j < n - 1; j++)
            {
                printf(" ");
            }
            printf("@");
        }
        else
        {
            print(n, (i % 2 == 0) ? '*' : '=');
        }
        printf("\n");
    }

    return 0;
}
```
**Sample Run ($n = 4$):**
```text
Enter Your number: 4
**\ /**
==\ /==
   @
==\ /==
**\ /**
```

## How it works
1. **Hollow Box:** Evaluates cell $(i, j)$ on an $n 	imes n$ grid. If the cell lies on the top row ($i = 0$), bottom row ($i = n - 1$), left column ($j = 0$), or right column ($j = n - 1$), it prints character $c$; otherwise, it prints a blank space.
2. **Butterfly:** Divides an $n$-row canvas into symmetric top and bottom wing segments centered around a single core `@` node, alternating textures (`*` and `=`) by parity with diagonal dividers `\` and `/`.

## Gotchas
> [!warning] Skipping Whitespace in `scanf("%d %c")`
> When reading a number followed by a character, the space between `%d` and `%c` is required. Without it, `%c` will consume the newline character pressed after entering the number.

## My notes
> [!question]- My notes

## Related
- [[ASG 02 - pyramid patterns]]
- [[LAB 07 - hollow triangle]]
