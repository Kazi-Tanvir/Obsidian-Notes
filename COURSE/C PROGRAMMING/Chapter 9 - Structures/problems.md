# Chapter 9 - Practice Set

## Problem 1
Create a two-dimensional vector using structures in C.

**Solution:**
```c
#include <stdio.h>

struct vector {
    int x;
    int y;
};

int main() {
    struct vector v1, v2;
    v1.x = 34;
    v1.y = 54;
    printf("X dim is %d and Y dim is %d\n", v1.x, v1.y);
    return 0;
}
```

## Problem 2
Write a function ‘sumVector’ which returns the sum of two vectors passed to it. The vectors must be two–dimensional.

**Solution:**
```c
#include <stdio.h>

struct vector {
    int x;
    int y;
};

struct vector sumVector(struct vector v1, struct vector v2) {
    struct vector result;
    result.x = v1.x + v2.x;
    result.y = v1.y + v2.y;
    return result;
}

int main() {
    struct vector v1, v2, sum;
    v1.x = 4; v1.y = 9;
    v2.x = 5; v2.y = 4;
    sum = sumVector(v1, v2);
    printf("X dim of result is %d and Y dim is %d\n", sum.x, sum.y);
    return 0;
}
```

## Problem 4
Write a program to illustrate the use of arrow operator `->` in C.

**Solution:**
```c
#include <stdio.h>

struct employee {
    int code;
    float salary;
};

int main() {
    struct employee e1;
    struct employee *ptr;
    ptr = &e1;
    ptr->code = 101;
    ptr->salary = 11.01;
    printf("Code is %d\n", e1.code);
    return 0;
}
```

## Problem 5
Write a program with a structure representing a complex number.

**Solution:**
```c
#include <stdio.h>

typedef struct complex {
    int real;
    int complex;
} comp;

int main() {
    comp cnums[5];
    for (int i = 0; i < 5; i++) {
        printf("Enter the real value for %d num\n", i + 1);
        scanf("%d", &cnums[i].real);
        printf("Enter the complex value for %d num\n", i + 1);
        scanf("%d", &cnums[i].complex);
    }
    for (int i = 0; i < 5; i++) {
        printf("Real value for %d num is: %d\n", i + 1, cnums[i].real);
        printf("Complex value for %d num is: %d\n", i + 1, cnums[i].complex);
    }
    return 0;
}
```

## Problem 9
Write a structure capable of storing date. Write a function to compare those dates.

**Solution:**
```c
#include <stdio.h>

typedef struct date {
    int date;
    int month;
    int year;
} date;

void display(date d) {
    printf("The date is: %d/%d/%d\n", d.date, d.month, d.year);
}

int dateCmp(date d1, date d2) {
    if (d1.year > d2.year) return 1;
    if (d1.year < d2.year) return -1;
    if (d1.month > d2.month) return 1;
    if (d1.month < d2.month) return -1;
    if (d1.date > d2.date) return 1;
    if (d1.date < d2.date) return -1;
    return 0;
}

int main() {
    date d1 = {2, 11, 21};
    date d2 = {5, 4, 22};
    display(d1);
    display(d2);
    int a = dateCmp(d1, d2);
    printf("Date comparison function returns: %d", a);
    return 0;
}
```
