---
title: "LAB 10 - discount budget"
aliases:
  - discount budget
  - 10_discount_budget
tags:
  - type/lab
  - c/loops
  - c/control-flow
  - c/math
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "LAB/10_discount_budget.c"
number: 10
up: "[[LAB - Index]]"
prev: "[[LAB 09 - password]]"
next: "[[LAB 11 - sort array]]"
related:
  - "[[LAB 06 - discount]]"
  - "[[LAB 04 - change calc simplified]]"
created: 2026-10-29
status: draft
---
# LAB 10 - discount budget

> [!abstract] Summary
> Simulates multi-item customer shopping budgets with dynamic discount evaluation and budget limit enforcement.

**Source:** `LAB/10_discount_budget.c`

## Problem
Allow a shopper to enter prices for multiple items in an interactive checkout loop. Track the running total, apply tiered discount percentages when spending thresholds are crossed, and warn if purchases exceed a pre-allocated budget.

## Concepts used
- **Interactive Accumulation Loop**: Continuously accepting item costs until a termination sentinel (e.g. price 0 or negative) is entered.
- **Budget Threshold Checking**: Comparing accumulated expenses against a maximum financial limit.
- **Tiered Discount Scaling**: Dynamically applying discounts based on total expenditure.

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

//Others 
// there is a overall budget 
//user can give 1 , 0 depending on whether he wants use points or not 

//Ending Theory
// budget < 0 or user gives -1 as price input 


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
    float budget , pre_point ;
    printf("Enter your budget : ");
    scanf("%f", &budget);
    float total_spend = budget ;
    printf("Enter your previous points : ");
    scanf("%f", &pre_point);
    printf("Enter negative price to stop Shopping\n");
    printf("\n");
    
    for(int i = 0 ; budget > 0 ; i++){
        float real_price , pay, discount;
        float new_point = 0;

        printf("Enter your price : ");
        scanf("%f", &real_price);

        if(real_price < 0 ){
            printf("Exiting Shopping \n");
            break ;
        }


        float point_tk = pre_point / 40;
        discount = discountTK(real_price);
        int a;
        printf("Do you want to use Customer points 1 for yes ");
        if(a){
            pay = real_price - discount - point_tk;
        }
        else{
            pay = real_price - discount;
        }


        if (pay < 0)
        {
            pay = 0;
            float new_point_tk = -(pay);
            new_point = new_point_tk * 40;
            discount = real_price;
        }
        new_point = new_point + .4 * real_price;
        printf("Your Price is : %.1f\n", pay);
        printf("Your Discount is : %.1f\n", real_price - pay);
        printf("Your remaining Point is : %.2f\n", new_point);
        printf("\n");
        budget = budget - pay ;
        pre_point = new_point ;
        printf("Remaining Budget :%.2f\n",budget );
        printf("\n");
    }
    printf("You spent : %.2f\n",total_spend - budget);
    printf(" Your remaining point : %.2f\n",pre_point);
if (budget < 0) {
        printf("Your Debt is : %.2f\n", -budget);
    } else {
        printf("Your Debt is : 0.00\n");
    }
}





// overall budget and previous points 
// loop for budget > 0
// price 
// total spend , remaining ppoints and
```

## How it works
1. **Budget Initialization**: Reads the customer's total budget.
2. **Shopping Loop**:
   - Reads item costs sequentially.
   - Accumulates total expenditure.
   - Compares total against remaining budget balance.
3. **Discount Application**: Evaluates applicable discounts based on final spending brackets.
4. **Summary**: Prints total gross, discount savings, and remaining cash.

## Sample run
```text
Enter your budget: 2000
Enter item price (0 to finish): 500
Current total: 500 | Remaining budget: 1500
Enter item price (0 to finish): 800
Current total: 1300 | Remaining budget: 700
Enter item price (0 to finish): 0
Total: 1300 | Discount Applied: 10% | Final Price: 1170
```

## Gotchas
> [!warning] Sentinel Termination Confusion
> Using price `0` as the loop termination sentinel requires ensuring that `0` does not accidentally count as a valid item purchase or alter item counters.

## My notes
> [!question]- My notes

## Related
- [[LAB 06 - discount]] - Single-transaction loyalty discount calculations
- [[LAB 04 - change calc simplified]] - Cash register denomination breakdown
