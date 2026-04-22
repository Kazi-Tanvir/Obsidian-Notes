# What is a function?
A function is a block of code which performs a particular task.
A function can be reused by the programmer in a given program any number of times.

**Syntax:**
```c
#include <stdio.h>

// Function prototype
void display();

int main() {
    int a; // Variable declaration
    display(); // Function call
    return 0; // Return statement
}

// Function definition
void display() {
    printf("hi i am display\n"); // Printing the message
}
```
