# Structures
Array and strings -> Similar data (int, float, char).
Structures can hold -> Dissimilar data.

A C structure can be created as follows:
```c
struct employee
{
    int code; // This declares a new user defined data type!
    float salary;
    char name[10];
}; // semicolon is important
```

We can use this user defined data type as follows:
```c
struct employee e1; // creating a structure variable
strcpy(e1.name, "harry");
e1.code = 100;
e1.salary = 71.22;
```
So, a structure in C is a collection of variables of different types under a single name.
