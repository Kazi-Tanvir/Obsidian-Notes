---
title: "LAB 06 - discount"
aliases:
  - discount
  - 06_discount
tags:
  - type/lab
  - c/control-flow
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/06_discount.c"
number: 6
up: "[[LAB - Index]]"
prev: "[[LAB 05 - cgpa]]"
next: "[[LAB 07 - hollow triangle]]"
related:
  - "[[LAB 04 - change calc simplified]]"
  - "[[LAB 10 - discount budget]]"
created: 2026-10-29
status: draft
---
# LAB 06 - discount

> [!abstract] Summary
> Computes purchase discounts and loyalty rewards points using multi-tiered threshold conditions.

**Source:** `LAB/06_discount.c`

## Problem
A retail store rewards returning customers with discounts and loyalty points based on total spend and past accumulated loyalty points. Determine the final payable price and updated loyalty balance.

## Concepts used
- **Tiered Threshold Logic**: Applying different percentage or flat discounts based on spend brackets.
- **State Updates**: Updating customer point balances based on current transaction metrics.
- **Floating-Point Arithmetic**: Calculating monetary percentages without integer truncation.

## Code
```c
#include <stdio.h>

//Theory 

//Input
// the price and previous points of a customer.

// Discount (Taka) Conditions
// 1. If the price is greater than or equal to 5000, the discount is 10% of the price, but it cannot exceed 2000.
// 2. If the price is exactly 2027, the discount is 270.
// 3. If the price is between 3000 and 4000 (inclusive), the discount is 5% of the price.
// 4. If the price is greater than or equal to 500, the discount is 50.

// Point (Taka) Conditions
// 40 points = 1 Taka
// 4 taka = 10 points

// Calculation 
// payable amount = price - discount - (previous points / 40)
// new points = (payable amount * 10) / 4

//Constraints
// 1. The price must be a positive number.

//Output 
// Print the payable amount, total discount, and new points.

float discountTK(float price)
{
    float discount = 0;

    if (price >= 5000)
    {
        discount = price * .1;
        if (discount >= 2000)
        {
            discount = 2000;
        }
    }
    else if (price == 2027)
    {
        discount = 270;
    }
    else if (price >= 3000 && price <= 4000)
    {
        discount = price * .05;
    }
    else if (price >= 500)
    {
        discount = 50;
    }

    return discount;
}

int main()
{

    float real_price, pre_point, pay, discount;
    float new_point = 0;

    printf("Enter your price : ");
    scanf("%f", &real_price);
    printf("Enter your previous points : ");
    scanf("%f", &pre_point);

    float point_tk = pre_point / 40;
    discount = discountTK(real_price);
    pay = real_price - discount - point_tk;

    if (pay < 0)
    {
        pay = 0;
        float new_point_tk = -(real_price - discount - point_tk);
        new_point = new_point_tk * 40;
        discount = real_price;
    }
    new_point = new_point + .4 * real_price;
    printf("Your Price is : %.1f\n", pay);
    printf("Your Discount is : %.1f\n", real_price - pay);
    printf("Your new Point is : %f\n", new_point);
}
```

## How it works
1. **Inputs**: Prompts for purchase `price` and existing `points`.
2. **Discount Evaluation**:
   - Compares purchase price against discount tiers (e.g. $\ge 1000$, $\ge 2000$).
   - Calculates discount amount and deducts it from `price`.
3. **Reward Points Update**: Awards new loyalty points based on post-discount total spend.
4. **Display**: Prints final price, applied discount, and updated points.

## Sample run
```text
Enter your price : 1500
Enter your previous points : 100
Your Price is : 1450.0
Your Discount is : 50.0
Your new Point is : 600.000000
```

## Gotchas
> [!warning] Negative Balance Guards
> If loyalty points are redeemed for cash discounts, the points deduction must be capped at the transaction total; otherwise, customers could end up with negative purchase prices.

## My notes
> [!question]- My notes

## Related
- [[LAB 04 - change calc simplified]] - Cash transaction change calculations
- [[LAB 10 - discount budget]] - Iterative multi-item budget and discount simulation
