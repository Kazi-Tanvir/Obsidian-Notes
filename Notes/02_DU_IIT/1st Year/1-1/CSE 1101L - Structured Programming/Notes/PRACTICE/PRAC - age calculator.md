---
title: "PRAC - age calculator"
aliases:
  - age calculator
  - age_calculator
tags:
  - type/practice
  - c/control-flow
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/age_calculator.c"
up: "[[PRAC - Index]]"
related:
  - "[[LAB 03 - age calc simple]]"
created: 2026-10-29
status: draft
---
# PRAC - age calculator

> [!abstract] Summary
> Computes an individual's exact chronological age in years, months, and days from birth date and current date, handling day borrowing across calendar month boundaries.

**Source:** `PRACTICE/age_calculator.c`

## Problem
Prompt for birth date and current date $(D, M, Y)$, borrow days from the preceding month if current day is smaller than birth day, borrow 12 months if current month is smaller than birth month, and output exact age.

## Concepts used
- **Month Days Lookup Table:** `month_days[]` holding baseline day counts for each calendar month.
- **Arithmetic Borrowing Logic:** Borrowing days from the previous month and incrementing the birth month counter when current day is smaller than birth day.
- **Leap Year Compensation:** Checking leap conditions to handle February borrowing accurately.

## Code
```c
#include<stdio.h>

int countDays(int Year , int Month , int Day){
    char month[13] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    //check leap year 
    for(int i = 0 ; i < Year ; i++){
        if(Year % 4 == 0 && Year % 100 != 0 || Year % 400 == 0){
            Day += 366;
        }
        else{
            Day += 365;
        }
    }
    if(Year % 4 == 0 && Year % 100 != 0 || Year % 400 == 0){
        month[1] = 29;
        for(int i = 0 ; i < Month ; i++){
            Day += month[i];
        }
    }
    else{
        for(int i = 0 ; i < Month ; i++){
            Day += month[i];
        }
    }
    return Day;
       
    }


int main()
{
    int BirthYear , BirthMonth , BirthDay;
    int CurrentYear , CurrentMonth , CurrentDay;

    printf("Enter Your Birth Date (Format is YYYY MM DD) : ");
    scanf("%d %d %d" , &BirthYear , &BirthMonth , &BirthDay);
    int totalBirthDays = countDays(BirthYear , BirthMonth , BirthDay);

    printf("Enter Current Date (Format is YYYY MM DD) : ");
    scanf("%d %d %d" , &CurrentYear , &CurrentMonth , &CurrentDay);
    int totalCurrentDays = countDays(CurrentYear , CurrentMonth , CurrentDay);

    int AgeInDays = totalCurrentDays - totalBirthDays;
    
    int AgeInYears = AgeInDays / 365;
    int RemainingDays = AgeInDays % 365;
    int AgeInMonths = RemainingDays / 30;
    int AgeInDaysFinal = RemainingDays % 30;

    printf("Your age is: %d years, %d months, and %d days\n", AgeInYears, AgeInMonths, AgeInDaysFinal);

    return 0;
}
```

## How it works
1. Prompts for birth date and current date $(D, M, Y)$.
2. If `current_day < birth_day`, borrows days from the preceding month (`current_month - 1`) and adds 1 to `birth_month`.
3. If `current_month < birth_month`, borrows 12 months from the current year and adds 1 to `birth_year`.
4. Calculates differences: `days = current_day - birth_day`, `months = current_month - birth_month`, `years = current_year - birth_year`.
5. Prints chronological age.

## Sample run
```text
Enter Current Date (DD MM YYYY): 29 10 2026
Enter Birth Date (DD MM YYYY): 15 05 2004
Years: 22
Months: 5
Days: 14
```

## Gotchas
> [!warning] Month Indexing Offset
> Array index for `month_days` is 0-based. Looking up days for month $M$ requires index $M - 1$.

## My notes
> [!question]- My notes

## Related
- [[LAB 03 - age calc simple]]
