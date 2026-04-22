# Chapter 1 - Practice Set

## Problem 1
Write a C program to calculate area of a rectangle:
a. Using hard coded inputs.
b. Using inputs supplied by the user.

**Solution:**
```c
#include <stdio.h>

int main() {
    // a. Hard coded inputs
    int length = 10, breadth = 5;
    int area = length * breadth;
    printf("Area of rectangle (hardcoded) is %d\n", area);

    // b. Inputs supplied by the user
    int l, b;
    printf("Enter length: ");
    scanf("%d", &l);
    printf("Enter breadth: ");
    scanf("%d", &b);
    printf("Area of rectangle (user input) is %d\n", l * b);

    return 0;
}
```

## Problem 2
Calculate the area of a circle and modify the same program to calculate the volume of a cylinder given its radius and height.

**Solution:**
```c
#include <stdio.h>

int main() {
    float radius = 3;
    float pi = 3.14159;
    float height = 5;
    
    printf("Area of circle is %f\n", pi * radius * radius);
    printf("Volume of cylinder is %f\n", pi * radius * radius * height);
    
    return 0;
}
```

## Problem 3
Write a program to convert Celsius (Centigrade degrees temperature to Fahrenheit).

**Solution:**
```c
#include <stdio.h>

int main() {
    float celsius = 37.0, fahrenheit;
    fahrenheit = (celsius * 9 / 5) + 32;
    printf("%f Celsius is %f Fahrenheit\n", celsius, fahrenheit);
    
    return 0;
}
```

## Problem 4
Write a program to calculate simple interest for a set of values representing principal, number of years and rate of interest.

**Solution:**
```c
#include <stdio.h>

int main() {
    float principal = 10000.0, rate = 8.5, years = 5.0;
    float simpleInterest = (principal * rate * years) / 100;
    
    printf("Simple interest is %f\n", simpleInterest);
    
    return 0;
}
```
