---
tags: [c-programming, structures, data-types]
---

# 09 Structures

While arrays hold similar data, structures can hold dissimilar data types under a single name.

## Syntax
```c
struct employee {
    int code;
    float salary;
    char name[10];
}; // Semicolon is important
```

## Creating & Accessing
```c
struct employee e1;
e1.code = 100;
e1.salary = 71.22;
strcpy(e1.name, "harry");
```

## Array of Structures
```c
struct employee facebook[100];
facebook[0].code = 100;
```

## Initializing Structures
```c
struct employee harry = {100, 71.22, "harry"};
struct employee shubh = {0}; // All elements set to 0
```

## Pointer to Structures & Arrow Operator
A pointer can store the address of a structure.
```c
struct employee *ptr = &e1;
printf("%d", (*ptr).code);
printf("%d", ptr->code); // Arrow operator (Shorthand)
```

## Typedef Keyword
Used to create an alias for a data type.
```c
typedef struct Complex {
    float real;
    float img;
} ComplexNo;

ComplexNo c1, c2; // Using the alias
```

## Practice Set
- [ ] Create a two-dimensional vector using structures in C.
- [ ] Write a function `sumVector` which returns the sum of two vectors passed to it.
- [ ] You need to store twenty integers. Would you prefer an array or a structure?
- [ ] Write a program to illustrate the use of the arrow operator.
- [ ] Create a structure representing a complex number.
- [ ] Create an array of 5 complex numbers and display them using a `display()` function.
- [ ] Rewrite the previous complex number structure using `typedef`.
- [ ] Create a structure for a bank account of a customer. Which fields would you use and why?
- [ ] Create a structure for storing a date and a function to compare two dates.
- [ ] Rewrite the date comparison using `typedef`.
