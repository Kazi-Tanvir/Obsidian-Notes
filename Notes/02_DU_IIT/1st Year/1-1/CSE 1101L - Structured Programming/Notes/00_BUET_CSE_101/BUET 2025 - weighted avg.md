---
title: "BUET 2025 - weighted avg"
aliases:
  - BUET weighted avg
  - weighted_avg
tags:
  - type/practice
  - c/math
  - c/bit-manipulation
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "00_BUET_CSE_101/2025/weighted_avg.c"
up: "[[BUET - Index]]"
related:
  - "[[CLASS 27 - binary encryption]]"
created: 2026-10-29
status: draft
---
# BUET 2025 - weighted avg

> [!abstract] Summary
> Investigates system architecture integer limits by computing $2^{8 \times \text{sizeof(long)}} - 1$ to calculate maximum integer magnitude boundaries.

**Source:** `00_BUET_CSE_101/2025/weighted_avg.c`

## Problem
Determine the bit width and maximum theoretical value of the `long` integer data type using the `sizeof` operator and powers of 2.

## Concepts used
- **Type Size Determination (`sizeof`):** Querying data type byte size in memory (`sizeof(long)`).
- **Bit-to-Byte Scaling:** Multiplying byte size by 8 to determine total bit capacity ($8 \times \text{bytes}$).
- **Maximum Representable Value:** Evaluating $2^{\text{bits}} - 1$.

## Code
```c
#include <stdio.h>
#include<math.h>

int main() {

    long x = sizeof(long);
    long y = pow(2,8*(x));
    printf("%ld",(y-1));

}
```

## How it works
1. Evaluates `sizeof(long)` (4 bytes on 32-bit Windows MinGW).
2. Computes `pow(2, 8 * 4)` = $2^{32}$.
3. Prints `y - 1`, outputting maximum unsigned 32-bit limit `2147483647` (or $4,294,967,295$).

## Sample run
```text
2147483647
```

## Gotchas
> [!warning] Mismatched Filename Intent
> Despite the file name `weighted_avg.c`, the source file contains bit-size limit exploration code rather than weighted average calculations.

## My notes
> [!question]- My notes

## Related
- [[CLASS 27 - binary encryption]]
