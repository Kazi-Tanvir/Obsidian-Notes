# Chapter 5 - Practice Set

## Problem 1
Write a program using function to find average of three numbers.

**Solution:**
```c
#include <stdio.h>

float average(int a, int b, int c) {
    return (float)(a + b + c) / 3;
}

int main() {
    int x, y, z;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &x, &y, &z);
    printf("Average is %f\n", average(x, y, z));
    return 0;
}
```

## Problem 2
Write a function to convert Celsius temperature into Fahrenheit.

**Solution:**
```c
#include <stdio.h>

float celsiusToFahrenheit(float c) {
    return (c * 9.0 / 5.0) + 32.0;
}

int main() {
    float c;
    printf("Enter Celsius temperature: ");
    scanf("%f", &c);
    printf("Fahrenheit: %f\n", celsiusToFahrenheit(c));
    return 0;
}
```

## Problem 3
Write a function to calculate force of attraction on a body of mass ‘m’ exerted by earth. Consider g = 9.8m/s².

**Solution:**
```c
#include <stdio.h>

float force(float mass) {
    return mass * 9.8;
}

int main() {
    float m;
    printf("Enter mass in kg: ");
    scanf("%f", &m);
    printf("Force is %f N\n", force(m));
    return 0;
}
```

## Problem 4
Write a program using recursion to calculate nth element of Fibonacci series.

**Solution:**
```c
#include <stdio.h>

int fibonacci(int n) {
    if (n == 1) return 0;
    if (n == 2) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("The %dth element of Fibonacci series is %d\n", n, fibonacci(n));
    return 0;
}
```

## Problem 6
Write a recursive function to calculate the sum of first ‘n’ natural numbers.

**Solution:**
```c
#include <stdio.h>

int sumNatural(int n) {
    if (n == 1) return 1;
    return n + sumNatural(n - 1);
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    printf("Sum of first %d natural numbers is %d\n", n, sumNatural(n));
    return 0;
}
```
