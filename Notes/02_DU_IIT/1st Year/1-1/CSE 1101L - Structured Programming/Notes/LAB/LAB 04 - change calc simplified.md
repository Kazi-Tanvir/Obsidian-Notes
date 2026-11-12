---
title: "LAB 04 - change calc simplified"
aliases:
  - change calc simplified
  - 04_change_calc_simplified
tags:
  - type/lab
  - c/math
  - c/control-flow
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/04_change_calc_simplified.c"
number: 4
up: "[[LAB - Index]]"
prev: "[[LAB 03 - age calc simple]]"
next: "[[LAB 05 - cgpa]]"
related:
  - "[[LAB 06 - discount]]"
  - "[[LAB 10 - discount budget]]"
created: 2026-10-29
status: draft
---
# LAB 04 - change calc simplified

> [!abstract] Summary
> Computes optimal change returned to a customer by breaking down total currency into the minimum count of banknotes and coins using greedy integer division.

**Source:** `LAB/04_change_calc_simplified.c`

## Problem
In a point-of-sale cash register, a customer tenders cash to pay for an item. The cashier must return the exact change using the fewest possible currency notes across standard denominations: 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1.

## Concepts used
- **Greedy Coin Change Strategy**: Selecting the largest denomination available that is less than or equal to the remaining change, maximizing its count, and repeating for the remainder.
- **Integer Division & Modulo Pairing**:
  - `count = change / denomination;` (computes how many notes of this denomination fit)
  - `change = change % denomination;` (computes remaining balance to be broken down by smaller denominations)

## Code
```c
#include<stdio.h>

int main()
{
    int amount , change ;
    printf("Enter the Amount : ");
    scanf("%d" , &amount);

    change = amount;
    
    int notes_1000 = change / 1000;
    change = change % 1000;

    int notes_500 = change / 500;
    change = change % 500;

    int notes_200 = change / 200;
    change = change % 200;

    int notes_100 = change / 100;
    change = change % 100;

    int notes_50 = change / 50;
    change = change % 50;

    int notes_20 = change / 20;
    change = change % 20;

    int notes_10 = change / 10;
    change = change % 10;

    int notes_5 = change / 5;
    change = change % 5;

    int notes_2 = change / 2;
    change = change % 2;

    int notes_1 = change / 1;
    
    printf("Change to be returned : \n");
    printf("1000 : %d\n", notes_1000);
    printf("500 : %d\n", notes_500);
    printf("200 : %d\n", notes_200);
    printf("100 : %d\n", notes_100);
    printf("50 : %d\n", notes_50);
    printf("20 : %d\n", notes_20);
    printf("10 : %d\n", notes_10);
    printf("5 : %d\n", notes_5);
    printf("2 : %d\n", notes_2);
    printf("1 : %d\n", notes_1);
}
```

## How it works
1. **Inputs**: Reads `taka` (tendered cash) and `price` (purchase cost).
2. **Change Balance**: Computes `change = taka - price;`.
3. **Sequential Denomination Breakdown**:
   - For 1000: `note1000 = change / 1000; change %= 1000;`
   - For 500: `note500 = change / 500; change %= 500;`
   - Continues through 200, 100, 50, 20, 10, 5, 2, down to 1.
4. **Display**: Prints the count of each note required.

## Sample run
```text
Enter the Amount : 1000
Change to be returned : 
1000 : 0
500 : 1
200 : 0
100 : 1
50 : 1
20 : 0
10 : 0
5 : 0
2 : 1
1 : 0
```

## Gotchas
> [!warning] Tender Underpayment
> If `taka < price`, `change` becomes negative! Because the program does not check `if (taka < price)`, integer division on negative values will produce negative note counts. An initial validation guard is essential.

## My notes
> [!question]- My notes

## Related
- [[LAB 06 - discount]] - Calculating transaction costs and discounts
- [[LAB 10 - discount budget]] - Multi-tiered shopping budget calculations
