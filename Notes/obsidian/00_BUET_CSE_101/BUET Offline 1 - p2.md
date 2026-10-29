---
title: "BUET Offline 1 - p2"
aliases:
  - BUET Offline 1 p2
  - offline1_A1_p2
tags:
  - type/practice
  - c/control-flow
  - c/math
  - c/arrays
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "00_BUET_CSE_101/offline/offline1_A1_p2.c"
up: "[[BUET - Index]]"
prev: "[[BUET Offline 1 - p1]]"
next: "[[BUET Offline 4 - p1]]"
related:
  - "[[PROJ Midterm Exam - q1]]"
  - "[[LAB 03 - age calc simple]]"
created: 2026-10-29
status: draft
---
# BUET Offline 1 - p2

> [!abstract] Summary
> Validates calendar dates against Gregorian calendar limits, handling year boundaries, month ranges, and February leap year day limits.

**Source:** `00_BUET_CSE_101/offline/offline1_A1_p2.c`

## Problem
Accept a day, month, and year $(D, M, Y)$. Verify that the date represents a valid Gregorian calendar date, accounting for century leap years, month length limits, and negative values.

## Concepts used
- **Month Days Lookup Table:** Initializing `mday[12]` with standard month lengths.
- **Leap Year Conditional Update:** Updating `mday[1] = 29` if `year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)`.
- **Compound Flag Validation:** Accumulating validation errors into flag `invalid`.

## Code
```c
#include<stdio.h>

int main(){
    int mday[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int day , month , year, invalid = 0;

    printf("Input:\n");
    scanf("%d %d %d", &day, &month, &year);

    if(year < 0) invalid = 1;
    if(month > 12 || month < 1) invalid = 1;
    if(month == 2 && year%100 != 0 && (year%4 == 0 || year%400 == 0)) mday[1] = 29;
    if(day > mday[month - 1] || day < 1) invalid = 1;

    if(invalid) printf("INVALID");
    else printf("VALID");
    
    return 0;
}
```

## How it works
1. Reads `day`, `month`, and `year`.
2. Validates ranges: `year >= 0`, `1 <= month <= 12`.
3. Checks leap year condition; if met, sets February to 29 days.
4. Checks `day < 1 || day > mday[month - 1]`.
5. Prints `VALID` if all constraints pass, or `INVALID` otherwise.

## Sample run
```text
Input:
29 2 2024
VALID
```

## Gotchas
> [!warning] Month Index Offset
> When querying `mday[month - 1]`, array indexing requires subtracting 1 from human 1-based month numbers.

## My notes
> [!question]- My notes

## Related
- [[PROJ Midterm Exam - q1]]
- [[LAB 03 - age calc simple]]
