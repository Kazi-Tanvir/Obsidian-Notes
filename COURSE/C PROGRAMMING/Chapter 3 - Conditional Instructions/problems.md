# Chapter 3 - Practice Set

## Problem 1
What will be the output of this program
```c
int a = 10;
if (a = 11)
    printf("I am 11");
else
    printf("I am not 11");
```

**Solution:**
The output will be `I am 11` because `a = 11` is an assignment, which evaluates to 11 (non-zero), making the condition true.

## Problem 2
Write a program to determine whether a student has passed or failed. To pass, a student requires a total of 40% and at least 33% in each subject. Assume there are three subjects and take the marks as input from the user.

**Solution:**
```c
#include <stdio.h>

int main() {
    int marks1, marks2, marks3;
    printf("Enter marks for 3 subjects: ");
    scanf("%d %d %d", &marks1, &marks2, &marks3);
    
    float total = (marks1 + marks2 + marks3) / 3.0;
    if (total >= 40 && marks1 >= 33 && marks2 >= 33 && marks3 >= 33) {
        printf("Student Passed\n");
    } else {
        printf("Student Failed\n");
    }
    return 0;
}
```

## Problem 3
Calculate income tax paid by an employee to the government as per the slabs mentioned below:
- 2.5L - 5.0L: 5%
- 5.0L - 10.0L: 20%
- Above 10.0L: 30%
Note that there is no tax below 2.5L. Take income amount as an input from the user.

**Solution:**
```c
#include <stdio.h>

int main() {
    float income, tax = 0;
    printf("Enter income in Lakhs: ");
    scanf("%f", &income);
    
    if (income >= 2.5 && income <= 5.0) {
        tax = 0.05 * (income - 2.5);
    } else if (income > 5.0 && income <= 10.0) {
        tax = 0.05 * 2.5 + 0.20 * (income - 5.0);
    } else if (income > 10.0) {
        tax = 0.05 * 2.5 + 0.20 * 5.0 + 0.30 * (income - 10.0);
    }
    
    printf("Tax to be paid is %f Lakhs\n", tax);
    return 0;
}
```

## Problem 4
Write a program to find whether a year entered by the user is a leap year or not. Take year as an input from the user.

**Solution:**
```c
#include <stdio.h>

int main() {
    int year;
    printf("Enter a year: ");
    scanf("%d", &year);
    
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        printf("%d is a leap year.\n", year);
    } else {
        printf("%d is not a leap year.\n", year);
    }
    return 0;
}
```

## Problem 5
Write a program to determine whether a character entered by the user is lowercase or not.

**Solution:**
```c
#include <stdio.h>

int main() {
    char ch;
    printf("Enter a character: ");
    scanf("%c", &ch);
    
    if (ch >= 'a' && ch <= 'z') {
        printf("Lowercase\n");
    } else {
        printf("Not Lowercase\n");
    }
    return 0;
}
```

## Problem 6
Write a program to find greatest of four numbers entered by the user.

**Solution:**
```c
#include <stdio.h>

int main() {
    int a, b, c, d, max;
    printf("Enter 4 numbers: ");
    scanf("%d %d %d %d", &a, &b, &c, &d);
    
    max = a;
    if (b > max) max = b;
    if (c > max) max = c;
    if (d > max) max = d;
    
    printf("Greatest number is %d\n", max);
    return 0;
}
```
