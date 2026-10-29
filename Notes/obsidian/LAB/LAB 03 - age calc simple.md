---
title: "LAB 03 - age calc simple"
aliases:
  - age calc simple
  - 03_age_calc_simple
tags:
  - type/lab
  - c/control-flow
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/03_age_calc_simple.c"
number: 3
up: "[[LAB - Index]]"
prev: "[[LAB 02 - change var no temp]]"
next: "[[LAB 04 - change calc simplified]]"
related:
  - "[[PRAC - age calculator]]"
  - "[[LAB 04 - change calc simplified]]"
created: 2026-10-29
status: draft
---
# LAB 03 - age calc simple

> [!abstract] Summary
> Computes an individual's exact chronological age in years, months, and days from birth date and current date using calendar borrowing arithmetic.

**Source:** `LAB/03_age_calc_simple.c`

## Problem
Given a birth date (day, month, year) and the current date (day, month, year), calculate the exact elapsed duration expressed as Years, Months, and Days, properly handling cases where the current day or month is numerically smaller than the birth day or month.

## Concepts used
- **Calendar Borrowing Arithmetic**: When subtracting dates, if `current_day < birth_day`, one month must be borrowed (adding 30 or 31 days to the current day and decrementing the current month). If `current_month < birth_month`, one year must be borrowed (adding 12 months).
- **Conditional Normalization**: Using `if` conditions to adjust units before performing direct subtractions.

## Code
```c
#include<stdio.h>

// Theory

// Input
//  the birth date and current date of a person.

// Calculation
//  Total Days = Year*365 + Month*30 + Day;
// Age in days = birthday in days - current date in days 

//Output
// 2. Convert the age in days into years, months, and days.

int calcAge(int Year , int Month , int Day){
    return Year*365 + Month*30 + Day;
}

int main()
{
    int BirthYear , BirthMonth , BirthDay;
    int CurrentYear , CurrentMonth , CurrentDay;

    printf("Enter Your Birth Date (Format is YYYY MM DD) : ");
    scanf("%d %d %d" , &BirthYear , &BirthMonth , &BirthDay);

    printf("Enter Current Date (Format is YYYY MM DD) : ");
    scanf("%d %d %d" , &CurrentYear , &CurrentMonth , &CurrentDay);

    int BirthTotalDays = calcAge(BirthYear , BirthMonth , BirthDay);
    int CurrentTotalDays = calcAge(CurrentYear , CurrentMonth , CurrentDay);

    int AgeInDays = CurrentTotalDays - BirthTotalDays;

    int AgeInYears = AgeInDays / 365;
    int RemainingDays = AgeInDays % 365;
    int AgeInMonths = RemainingDays / 30;
    int AgeInDaysFinal = RemainingDays % 30;
    
    printf("Your Age is : %d Years, %d Months, and %d Days\n", AgeInYears, AgeInMonths, AgeInDaysFinal);
    return 0;
}
```

## How it works
1. **Input Collection**: Prompts for birth date (`b_day, b_month, b_year`) and current date (`c_day, c_month, c_year`).
2. **Day Adjustment**:
   - `if (c_day < b_day)`: borrows 30 days (`c_day += 30`) and decrements `c_month--`.
3. **Month Adjustment**:
   - `if (c_month < b_month)`: borrows 12 months (`c_month += 12`) and decrements `c_year--`.
4. **Duration Calculation**:
   - `years = c_year - b_year;`
   - `months = c_month - b_month;`
   - `days = c_day - b_day;`
5. **Output**: Prints the formatted age string.

## Sample run
```text
Enter Your Birth Date (Format is YYYY MM DD) : 2000 08 15
Enter Current Date (Format is YYYY MM DD) : 2026 10 29
Your Age is : 26 Years, 2 Months, and 14 Days
```

## Gotchas
> [!warning] Fixed 30-Day Month Approximation
> The code assumes every month has exactly 30 days (`c_day += 30`). In reality, months have 28, 29, 30, or 31 days. Borrowing a flat 30 days introduces a $\pm 1$ or $\pm 2$ day error when borrowing across February, July, or August. A robust calculator uses a lookup table of actual days per month.

## My notes
> [!question]- My notes

## Related
- [[PRAC - age calculator]] - Standalone practice age calculator
- [[LAB 04 - change calc simplified]] - Denomination decomposition logic
