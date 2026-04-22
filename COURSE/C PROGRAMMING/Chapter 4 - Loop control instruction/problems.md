# Chapter 4 - Practice Set

## Problem 1
Write a program to print multiplication table of a given number n.

**Solution:**
```c
#include <stdio.h>

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    
    for (int i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", n, i, n * i);
    }
    return 0;
}
```

## Problem 2
Write a program to print multiplication table of 10 in reversed order.

**Solution:**
```c
#include <stdio.h>

int main() {
    for (int i = 10; i >= 1; i--) {
        printf("10 x %d = %d\n", i, 10 * i);
    }
    return 0;
}
```

## Problem 3
A do while loop is executed:
a. At least once.
b. At least twice.
c. At most once.

**Solution:**
`a. At least once.`

## Problem 5
Write a program to sum first ten natural numbers using while loop.

**Solution:**
```c
#include <stdio.h>

int main() {
    int i = 1, sum = 0;
    while (i <= 10) {
        sum += i;
        i++;
    }
    printf("Sum is %d\n", sum);
    return 0;
}
```

## Problem 8
Write a program to calculate the factorial of a given number using a for loop.

**Solution:**
```c
#include <stdio.h>

int main() {
    int n, factorial = 1;
    printf("Enter n: ");
    scanf("%d", &n);
    
    for (int i = 1; i <= n; i++) {
        factorial *= i;
    }
    printf("Factorial of %d is %d\n", n, factorial);
    return 0;
}
```

## Problem 10
Write a program to check whether a given number is prime or not using loops.

**Solution:**
```c
#include <stdio.h>

int main() {
    int n, isPrime = 1;
    printf("Enter n: ");
    scanf("%d", &n);
    
    if (n <= 1) isPrime = 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            isPrime = 0;
            break;
        }
    }
    
    if (isPrime) printf("%d is a prime number\n", n);
    else printf("%d is not a prime number\n", n);
    return 0;
}
```
