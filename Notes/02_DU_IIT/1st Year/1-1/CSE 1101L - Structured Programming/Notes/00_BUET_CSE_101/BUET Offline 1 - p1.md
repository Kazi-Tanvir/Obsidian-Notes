---
title: "BUET Offline 1 - p1"
aliases:
  - BUET Offline 1 p1
  - offline1_A1_p1
tags:
  - type/practice
  - c/control-flow
  - c/math
  - c/arrays
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "00_BUET_CSE_101/offline/offline1_A1_p1.c"
up: "[[BUET - Index]]"
next: "[[BUET Offline 1 - p2]]"
related:
  - "[[LAB 04 - change calc simplified]]"
  - "[[BUET Offline 1 - p2]]"
created: 2026-10-29
status: draft
---
# BUET Offline 1 - p1

> [!abstract] Summary
> Implements an automated ATM cash dispensation algorithm that satisfies customer preferences for specific note denominations (200, 100, 50, 20, 10) while validating divisibility.

**Source:** `00_BUET_CSE_101/offline/offline1_A1_p1.c`

## Problem
Simulate an ATM cash dispenser: accept a total withdrawal amount (must be divisible by 500), prompt for the desired number of 200, 100, and 50 notes, deduct their value, and greedily allocate remaining balances using 20 and 10 notes.

## Concepts used
- **Input Validation Rules:** Checking `amount % 500 != 0` to enforce ATM hardware transaction rules.
- **Customer Denomination Allocation:** Allocating user-requested counts of 200, 100, and 50 notes, checking that their sum does not exceed total withdrawal.
- **Greedy Currency Breakdown:** Decomposing remaining balance into largest available notes (`amount / 20`, `amount / 10`).

## Code
```c
#include<stdio.h>

int main(){
    int amount = -1;
    int notes[] = {200 ,100, 50, 20, 10};
    int wanted[5]={0};
    scanf("%d", &amount);
    if(amount%500 != 0) {
        printf("Invalid Input");
        return 0;
    }
    for(int i = 0; i < 3; i++) {
        scanf(" %d", &wanted[i]);
        if(wanted <= 0){
            printf("Invalid Input");
            return 0;
        }
        if(notes[i]*wanted[i] > amount){
            printf("Exchange Not Possible!");
            return 0;
        }
    }
    for(int i = 0; i < 5; i++){
        if(i > 2)  wanted[i] = amount/(notes[i]);
        amount -= notes[i]*wanted[i];
        printf("Tk %d notes: %d\n",notes[i],wanted[i]);
    }
    return 0;
}


// left amount = amount - notes[i]*wanted[i];
// if notes*wanted greater than amount then amount calculated amount/notes i = available *
```

## How it works
1. Reads `amount`. If not divisible by 500, prints `Invalid Input` and terminates.
2. Reads desired quantities for 200, 100, and 50 notes.
3. Verifies requested note value does not exceed total amount.
4. Deducts preferred note totals from `amount`.
5. Fills remaining amount using 20 notes, then 10 notes.
6. Prints final itemized note counts.

## Sample run
```text
1000
1 2 3
Tk 200 notes: 1
Tk 100 notes: 2
Tk 50 notes: 3
Tk 20 notes: 22
Tk 10 notes: 1
```

## Gotchas
> [!warning] Negative Balance Deductions
> If a user requests more notes than the total withdrawal amount permits, `amount` turns negative, producing invalid negative counts for 20 and 10 notes.

## My notes
> [!question]- My notes

## Related
- [[LAB 04 - change calc simplified]]
- [[BUET Offline 1 - p2]]
