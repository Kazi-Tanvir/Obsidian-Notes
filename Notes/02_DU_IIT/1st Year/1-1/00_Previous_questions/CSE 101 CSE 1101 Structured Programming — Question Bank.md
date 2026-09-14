# CSE 101 / CSE 1101: Structured Programming - Question Bank

---

## 1. CSE 101: Structured Programming - Final Examination 2022

**Institute of Information Technology, University of Dhaka**
**Program:** Bachelor of Science in Software Engineering
**Semester:** 1st Semester Final Examination, 2022
**Course Code:** CSE 101 (Structured Programming)
**Marks:** 30 | **Time:** 2 Hours
_Instruction: Answer any three of the following questions._

---

### Question 1

- **a)** What are the basic data types in C? What are C's data type modifiers and what function do they perform? `[2]`
- **b)** What does a type cast do? What is the difference between local and global variables? `[2]`
- **c)** Write a program to test whether an entered number is prime or not. In addition, it will also display all the factors of a number entered by the user. `[3]`
- **d)** Write a program in C to make such a pattern like a pyramid with numbers increased by 1: `[3]`

    ```plaintext
          1
         2 3
        4 5 6
       7 8 9 10
    ```

### Question 2

- **a)** What are the ways to initialize an array? Write a program that inputs a string from the command line and then displays it backward on the screen. `[3]`
- **b)** Write a program that acts like an electronic dictionary. If the user enters a word in the dictionary, the program displays its meaning. `[2]`
- **c)** What will be the output of the following program? Describe line by line. `[3]`

    ```c
    #include <stdio.h>

    int main(void) {
        int *p, q;
        q = 18;
        p = &q;
        printf("%d", *p);
        return 0;
    }
    ```

- **d)** Sort an array using pointers. `[2]`

### Question 3

- **a)** Write a program that takes a number $N$ as input and fills an array using factorials up to the given number $N$ using a recursive function.

    _Example:_ If the input is 4, the array will contain `1, 1, 2, 6, 24`. `[5]`

- **b)** Write a function called `avg()` that averages a list of floating-point values. The function will have three arguments: the first is a pointer to the array containing the numbers, the second is an integer value that specifies the size of the array, and the third is a float-type pointer to store the result. `[2]`
- **c)** Write a program that exchanges the contents of two files whose names are specified on the command line. `[3]`

### Question 4

- **a)** How can a file be accessed randomly? Write a program that reports the value of any byte within the file specified on the command line. `[3]`
- **b)** What is a structure and what is a union? What are the differences between a structure and an array? `[2]`
- **c)** Write a program that displays the ASCII code when a key is pressed. `[2]`
- **d)** Take a number file, from the command line, containing the marks of 52 students out of 100. Since you have to send it over an untrusted network, encode marks by swapping each of the mark's lower two bytes and store it in a separate file. Create another function that can decode those marks accordingly in another file. `[3]`

---

## 2. CSE 1101: Structured Programming - Final Examination 2023

**Institute of Information Technology, University of Dhaka**
**Program:** Bachelor of Science in Software Engineering (BSSE)
- [ ] **Semester:** 1st Semester Final Examination, 2023
**Course Code:** CSE 1101 (Structured Programming)
**Marks:** 60 | **Time:** 3 Hours
_Instruction: Answer any 5 (five) questions. When answering a question, please answer all the subsections of it at once._

---
### Question 1

- **a.** What are the essential components of a C program? Write an example code and show all the components. `[4]`
- **b.** What is a variable? What are C's data type modifiers and what function do they perform? What does a typecast do? `[3]`
- **c.** How do we put comments in C? Why are comments important? `[2]`
- **d.** What is a function? How many types of functions are there? How does a function return a value to the routine that called it? `[3]`

### Question 2

- **a.** What are C's relational and logical operators? Give one example code demonstrating all those operators. `[3]`
- **b.** What is a block of code? How do you make one? `[2]`
- **c.** Write short notes on C's increment and decrement operators. `[2]`
- **d.** Write a program that displays all the prime factors of a number entered by the user. Print the output as the prime factor tree as follows: `[5]`

    ```plaintext
    User input: 54
    Output:
    54
    2 27
      3 9
        3 3
          3 1
    ```

### Question 3

- **a.** What are the ways we perform loops in C? How are they different from each other? `[3]`
- **b.** What are the ways we make decisions in C? How are they different from each other? `[3]`
- **c.** What does a `break` statement do? `[2]`
- **d.** Write a menu-driven program where the user will be asked to perform which operation she wants to perform from the following functions: Addition, Subtraction, Multiplication, and Division. The program will continuously run until the user selects the Exit function. If any error occurs, your program should also be able to inform that. `[4]`

### Question 4

- **a.** `int a[10]; int (*b)[10];` What do `a` and `b` represent? `[2]`
- **b.** Are the expressions `*ptr++` and `++*ptr` the same? Explain. `[2]`
- **c.** What will be the output of the following C code? `[2]`

    ```c
    int a = 0x11223344;
    unsigned char *c = (unsigned char *) &a;
    printf("%02X\n", *c);
    ```

- **d.** What would be the equivalent pointer expression for referring to the same element as `a[p][q][r][s]`? `[3]`
- **e.** Write a program in C to find the sum and mean of all elements in an array using pointers. `[3]`

### Question 5

- **a.** What are the advantages of using pointers as parameters in a function? Give one example code. `[3]`
- **b.** Write a program that takes an integer input and outputs the factorial of that number using recursion. `[3]`
- **c.** What are command-line arguments? `[2]`
- **d.** Write a program that accepts two strings as command-line arguments. Have the program compare them and report which is lexicographically greater than the other. `[4]`

### Question 6

- **a.** Find the errors in the following programs. Give a correct implementation of each of these functions: `[4]`

    - **i)** The `str_cpy` function is to copy a valid C string to another. An (erroneous) implementation is given below:

        ```c
        unsigned int str_cpy(char *d, char *s) {
            unsigned int i = 0;
            while (*s != '\0') {
                *d = *s;
                s++;
                d++;
                i++;
            }
            return i;
        }
        ```

    - **ii)** The `str_len` function takes a valid C string as an argument and returns the length of the string. An (erroneous) implementation is given below:

        ```c
        unsigned int str_len(const char *s) {
            unsigned int i;
            while (s[i] != '\0')
                i++;
            return i;
        }
        ```

- **b.** How do functions like `printf()` and `scanf()` relate to the C file system? `[2]`
- **c.** Write a program that takes a location value from the command line and shows the character at that location in the file. `[2]`

### Question 7

- **a.** What is a bit-field? Write a structure where you can put a student's roll, batch, and semester information in a single integer. `[2]`
- **b.** What are the differences between structure, union, and array? `[3]`
- **c.** Write a program that displays the ASCII code when a key is pressed. `[2]`
- **d.** Take a file, from the command line, containing the user ID and password (four bytes long). Since you have to store it securely, encode passwords by swapping each of the password's upper two bytes with the lower two bytes. When the user enters her user ID and password, you have to check the file and mention whether the user ID and password are right or wrong. `[5]`

---

## 3. CSE 1101: Structured Programming - Final Examination 2024

**Institute of Information Technology, University of Dhaka**
**Program:** Bachelor of Science in Software Engineering (BSSE)
**Semester:** 1st Year 1st Semester Final Examination, 2024
**Course Code:** CSE 1101 (Structured Programming)
**Marks:** 60 | **Duration:** 3 Hours
_Instruction: Answer any five questions. When answering a question, please answer all the subsections of it at once._

---

### Question 1

- **a.** Explain the advantages of using preprocessor directives such as `#define` and `#include`. How do these directives contribute to code organization and maintainability? `[4]`
- **b.** What are the data type modifiers? How are type conversions in expressions performed in C? Provide an example code. `[3]`
- **c.** Write a C program that reads an integer, then finds the prime numbers within that number, and after that checks if it can be represented as a sum of two prime numbers. `[5]`

### Question 2

- **a.** Explain how nested `if-else` statements work. Show where it is preferable over a `switch` statement. Write a code to identify whether a character is a vowel or not using `switch` and its corresponding code using `if-else`. `[4]`
- **b.** What are the significances of `break` and `continue`? `[2]`
- **c.** Write a C program that takes a year as input and determines if it is a leap year using a `switch` statement. Then determine if a given date (`dd/mm/yyyy`) is valid, considering leap years and varying days in months. `[6]`

### Question 3

- **a.** Explain the concept of pointer arithmetic with examples of increment and decrement operations on pointers. `[3]`
- **b.** Show that pointers and arrays are interchangeable with example codes. `[4]`
- **c.** Write a code which will take a string from the command line and use a recursive function to reverse the string using pointers. `[5]`

### Question 4

- **a.** Define what recursion is. Explain the two essential components of a recursive function. `[3]`
- **b.** Write a recursive function to calculate the factorial of a given non-negative integer. Explain how your function works and ensures where to return after each function call. `[5]`
- **c.** Discuss the importance of writing clean, maintainable code. What are some of the key principles of good code style? (e.g., naming conventions, comments, indentation, modularity). `[4]`

### Question 5

- **a.** Explain the difference between 'call by value' and 'call by reference' parameter passing methods in the context of functions. What are the implications of each method on the original variables passed to the function? Explain with appropriate examples. `[6]`
- **b.** Write a C function called `findMax` that takes an integer array and its size as input and returns the largest element in the array. `[6]`

### Question 6

- **a.** What do you understand by file and stream? List all the common file read and write functions. `[3]`
- **b.** How can we randomly access a file? Give an example code. `[3]`
- **c.** Write a C program to read an existing file and count the number of words and lines in it. Then copy the contents of one file into another while replacing all occurrences of a given word with another word. `[6]`

### Question 7

- **a.** Define and differentiate between Structure and Union. How are they different from arrays? `[4]`
- **b.** What is a bit-field? Write a structure where you can put a student's roll, batch, and semester information in a single integer. Then store the information of 56 students of BSSE16, where you can retrieve information by searching any of the fields. `[4]`
- **c.** Take an input text file and encrypt each two consecutive characters by swapping these two and write the encrypted text to a new file. `[4]`

---

## 4. CSE 1101: Structured Programming - Final Examination 2025

**Institute of Information Technology, University of Dhaka**
**Program:** Bachelor of Science in Software Engineering (BSSE)
**Semester:** 1st Year 1st Semester Final Examination, 2025
**Course Code:** CSE 1101 (Structured Programming)
**Marks:** 60 | **Duration:** 3 Hours
_Instruction: Answer any 5 (five) of the following questions. When answering a question, please answer all the subsections of it at once._

---

### Question 1

- **a.** Explain the structure of a simple C program with its essential components. `[4]`
- **b.** What is a type conversion? Explain implicit and explicit type conversions with examples. `[3]`
- **c.** Write a program that evaluates the expression:

    $$\text{result} = a + b \times c - d / e$$

    and displays step-by-step output to show the order of evaluation. `[5]`

### Question 2

- **a.** List the selection and iteration control structures in C with their general forms. Differentiate between selection and iteration control structures in C. `[4]`
- **b.** What is the difference between the `break` and `continue` statements in loops? Give appropriate example codes. `[3]`
- **c.** Write a C program that displays the following pattern using nested loops: `[5]`

    ```plaintext
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    ```

### Question 3

- **a.** Analyze the difference between declaring a function parameter as `int arr[]`, `int *arr`, and `int arr[10]`. Explain why, in the context of function arguments, these three forms are often considered identical by the compiler. `[5]`
- **b.** Describe the purpose of using a double pointer (`int **ptr`). Provide a detailed explanation and a scenario where a double pointer is necessary to correctly implement a function (e.g., modifying the address held by a pointer passed as an argument). `[4]`
- **c.** Explain the mechanism of pointer arithmetic. Given an array `int arr[10]` and a pointer `int *p = arr;`, analytically explain why `p + 1` increases the pointer's memory address by 4 bytes (assuming a 32-bit integer architecture), rather than just 1 byte. `[3]`

### Question 4

- **a.** Define a string in C. How are strings different from character arrays? What is the difference between `gets()` and `scanf()` for reading strings? `[3]`
- **b.** Write your own functions for `strlen`, `strcpy`, `strcmp`, and `strcat` using pointers. `[4]`
- **c.** Write a C program for finding fruit color. First, create a table that links fruits with their colors. The program will ask its user for a fruit name, and it displays the color of the fruit. `[5]`

### Question 5

- **a.** Explain the concept of file and stream. List all the common file read and write built-in functions with an example code. `[3]`
- **b.** How can we randomly access a file? Give an example code where a program reports the value of any byte within the file specified on the command line. `[5]`
- **c.** Write a program that copies a file. Have the user specify both the source and destination files on the command line. Have the program count all the white spaces (space and tab) in the source file and print it. `[4]`

### Question 6

- **a.** Differentiate between a structure, a union, and an array in terms of memory storage and access. `[3]`
- **b.** How can arrays of structures be declared and used? Write a program to input details of 5 students (name and marks) and sort them in descending order of marks. `[4]`
- **c.** Take an input text file and encrypt each two consecutive characters by swapping these two and write the encrypted text to a new file. `[5]`

### Question 7

- **a.** Define what recursion is. Explain the two essential components of a recursive function. `[3]`
- **b.** Write a recursive function to calculate the $n^{\text{th}}$ number in the Fibonacci series. Explain how your function works and ensures where to return after each function call, assuming the function is called to calculate the $5^{\text{th}}$ number in the series. `[5]`
- **c.** Write a C function `swap_pointers(int **p1, int **p2)` that swaps the values pointed to by two integer pointers, by passing the pointers by reference (using double pointers). `[4]`

---

## 5. CSE 1101: Structured Programming - Midterm Examination 2024

### Section A: Multiple Choice Questions `[35 Ã— 1 = 35 Marks]`

1. **Which is not true about a Statement?**
    - a. Essential parts of the program
    - b. Perform operations
    - c. Specifies an action
    - d. Executed by the program
    - e. None of the above

2. **What is not true about a C function?**
    - a. Function name convention is similar to variable name convention
    - b. A Function prototype declares a function before it is used
    - c. A function should return a value
    - d. A function must have statements inside
    - e. Parameters are used to send input to the function

3. **Which is not true about C preprocessor?**
    - a. Header files are included with your program by the preprocessor
    - b. All C compilers use as their first phase of compilation a preprocessor.
    - c. Preprocessor is a part of the C language
    - d. `#include` is a preprocessor
    - e. Using preprocessor, a programmer gives instructions to the compiler

4. **Which is not true about C?**
    - a. Statements ends with a semi-colon
    - b. Functions are blocked by curly braces but statements are not
    - c. C ignores spaces
    - d. You can put two or more statements on the same line
    - e. The actual positioning of statements, functions and braces is a programming decision

5. **What is not true about variable?**
    - a. All Variables must be declared before they can be used
    - b. A Variable is a named memory location
    - c. Variable is the future memory reference
    - d. A Variable is the memory that can hold values
    - e. None of the above

6. **What is not true about variable (again)?**
    - a. A Local variable can be accessed by the function where it has been declared
    - b. A global variable can be accessed by any of the functions
    - c. Variable declaration is not a statement
    - d. Variable can be declared inside a function
    - e. Variable can be declared outside all the functions

7. **Which keyword is used to prevent any changes in the variable within a C program?**
    - a. `immutable`
    - b. `mutable`
    - c. `const`
    - d. `volatile`
    - e. None of the above

8. **In C, comments written as `/* text */` are:**
    - a. Single-line comments only
    - b. Multi-line comments
    - c. Errors in syntax
    - d. Executed by the compiler
    - e. None of the above

9. **Associativity of C Operators `*`, `/`, `%`, `+`, `-` and `=` is:**
    - a. Operators `*`, `/` and `%` have Left to Right Associativity. Operators `+` and `-` have Left to Right Associativity. Operator `=` has Right to Left Associativity.
    - b. Operators `*`, `/` and `%` have Right to Left Associativity. Operators `+` and `-` have Left to Right Associativity. Operator `=` has Right to Left Associativity.
    - c. Operators `*`, `/` and `%` have Right to Left Associativity. Operators `+` and `-` have Right to Left Associativity. Operator `=` has Right to Left Associativity.
    - d. Operators `*`, `/` and `%` have Right to Left Associativity. Operators `+` and `-` have Right to Left Associativity. Operator `=` has Left to Right Associativity.
    - e. None of the above

10. **Which is not true about `scanf()` function?**
    - a. The `scanf()` function waits until you have pressed ENTER before considering the input value
    - b. It requires at least three arguments
    - c. It is used to input from the keyboard
    - d. Identifiers are used to understand what type of input is expecting
    - e. Memory reference is used to assign the input values

11. **Which is not true about C comments?**
    - a. Multiline comment starts with `/*`
    - b. You can use nested comments
    - c. A comment is a note to yourself or others
    - d. All comments are ignored by the compiler
    - e. Single line comments start with `//`, is not standardized currently

12. **Which is not true about parameter and argument?**
    - a. Function that takes arguments are called parameterized function
    - b. You can send an expression as an argument
    - c. Argument is a value that is passed to the function
    - d. Parameters are variables that receive the arguments
    - e. None of the above

13. **Which set contains invalid C keyword?**
    - a. `auto`, `double`, `int`, `struct`
    - b. `break`, `else`, `long`, `switch`
    - c. `case`, `enum`, `register`, `typedef`
    - d. `char`, `extern`, `intern`, `return`
    - e. None of the above

14. **What is the result of logical or relational expression in C?**
    - a. True or False
    - b. 0 or 1
    - c. 0 or any integer number
    - d. 0 if an expression is false and any positive number if an expression is true
    - e. None of the above

15. **Which is not true about `if` statement?**
    - a. It can take any valid expression as condition
    - b. If the condition is true the followed statements are executed
    - c. One of the selection statements
    - d. Also called unconditional statements
    - e. None of the above

16. **Which is not a valid relational operator?**
    - a. `==`
    - b. `>`
    - c. `<`
    - d. `<=`
    - e. `!`

17. **Which of the following comments about the `++` operator is correct?**
    - a. It is a unary operator
    - b. The operand can come before or after the operator
    - c. It cannot be applied to an expression
    - d. It associates from the right
    - e. All of the above

18. **Which is not true (according to our textbook)?**
    - a. `double` is 64 bit
    - b. `long double` is 80 bit
    - c. `char` is 8 bit
    - d. `unsigned short int` is 32 bit
    - e. `float` is 32 bit

19. **Which is not true about `switch` statement?**
    - a. A value is tested here against a list of constants
    - b. It is C's multiple selection statement
    - c. It is interchangeable with `if-else` statement
    - d. It is used to select one of several alternative paths
    - e. None of the above

20. **In the context of "break" and "continue" statements in C, pick the best statement.**
    - a. "break" and "continue" can be used in "for", "while", "do-while" loop body and "switch" body
    - b. "break" and "continue" can be used in "for", "while" and "do-while" loop body. But only "break" can be used in "switch" body
    - c. "break" and "continue" can be used in "for", "while" and "do-while" loop body. Besides, "continue" and "break" can be used in "switch" and "if-else" body
    - d. "break" can be used in "for", "while" and "do-while" loop body
    - e. None of the above

21. **Which is not true about nested loops?**
    - a. For each of the nested loop you have to use different loop variables
    - b. When the body of one loop contains another, the second is said to be nested
    - c. Any of the C's loops can be nested within any other loop.
    - d. Most compilers allow a fixed level of nesting
    - e. None of the above

22. **Which is not true about `do-while` loop?**
    - a. Since the loop condition is tested at the bottom, it is not necessary to initialize the loop variable prior entering into the do-while loop.
    - b. The do loop repeats the statements while the expression inside the while is true
    - c. If only one statement is repeated inside the loop, still curly braces are necessary.
    - d. It will always execute the code within the loop at least once.
    - e. None of the above

23. **`for` loop is powerful and flexible - not because of:**
    - a. `for` loop places no limits on the type of expressions that occur inside it
    - b. You do not have to initialize the loop variable at the initialization section
    - c. There does not need to be any loop variable
    - d. Other variables can be initialized at the loop initialization section
    - e. None of the above

24. **`for` loop is powerful and flexible - not because of (again):**
    - a. `for` does not have to increment or decrement any loop variable
    - b. the initialization, condition and modification parts can be empty
    - c. you may use other mechanisms to stop loop inside the loop body
    - d. you can use any statements as the initialization, condition or modification parts
    - e. None of the above

25. **What will be printed?**

    ```c
    int n = 2;
    switch(n) {
        case 1: printf("A");
        case 2: printf("B");
        case 3: printf("C"); break;
        default: printf("D");
    }
    ```

    - a. ABC
    - b. BC
    - c. B
    - d. C
    - e. ABCD

26. **If `int a = 5; printf("%d", a++);` is executed, what will be the output?**
    - a. 4
    - b. 5
    - c. 6
    - d. 56
    - e. Compiler dependent

27. **Which of the following correctly describes the value of `char c = 255;` in a system where char is signed and 8 bits?**
    - a. 255
    - b. -1
    - c. Undefined behavior
    - d. 127
    - e. 0

28. **Which statement about type casting in C is correct?**
    - a. `(float) (5/2)` results in 2.5.
    - b. `(float) 5/2` results in 2.5.
    - c. Casting always changes the stored variable permanently.
    - d. Implicit type promotion never occurs in C.
    - e. Casting a `const` removes its constness.

29. **Which of the following is true for `#define PI 3.14159` compared to `const double PI = 3.14159;`?**
    - a. `#define` creates a typed constant, `const` does not.
    - b. `const` respects scope, `#define` does not.
    - c. `#define` is safer than `const`.
    - d. Both are identical in every way.
    - e. `const` cannot be used for floating-point values.

30. **Which of the following statements about global variables in C is true?**
    - a. They are stored in the stack segment.
    - b. They are automatically initialized to 0 if not explicitly initialized.
    - c. They cannot be declared as `const`.
    - d. They can only be used in the file where they are declared.
    - e. They must always be declared as `extern`.

31. **What is not true about Arrays?**
    - a. All the array elements are of same type
    - b. Array is a datatype
    - c. Array is a list of variables, but accessed through a common name
    - d. An individual variable in the array is called an array element
    - e. None of the above

32. **Which of the following is true about string constants in C?**
    - a. They are enclosed in single quotes `''`
    - b. They automatically include a null character `\0` at the end
    - c. They are stored in integer arrays
    - d. They cannot contain spaces
    - e. They must always be initialized

33. **Which of the following is NOT a valid way to initialize a character array?**
    - a. `char str[] = "C";`
    - b. `char str[5] = "C";`
    - c. `char str[] = {'C', '\0'};`
    - d. `char str[2] = "C";`
    - e. `char str[] = 'C';`

34. **Which of the following statements about strings in C is FALSE?**
    - a. Strings are stored as arrays of characters.
    - b. A string must end with `'\0'`.
    - c. `strlen()` counts the `'\0'` character.
    - d. `strcpy()` copies characters until `'\0'`.
    - e. `"Hello"` is stored as 6 characters including `'\0'`.

35. **Which is not true about Array (again)?**
    - a. Each of the array elements can be used as exactly as a simple variable or constant
    - b. C does not perform any bounds checking on array index
    - c. An array element is accessed by indexing the number of elements
    - d. Element indexes are specified inside a square bracket
    - e. C stores the arrays in one contiguous memory location with the first element at the highest address

---

### Section B: Programming `[4 Ã— 5 = 20 Marks]`

**1.** Write a program where you store all the answers (a, b, c, d or e) given by you from the above Section A. In a separate array, the correct answer keys are given. Then:

- **a.** Write a function to find the correct number of answers.
- **b.** Write a function to sort the answer keys.
- **c.** Write a function to find the statistical frequency of each letter.
- **d.** Create a menu for the above operations to perform any of the functions whenever needed, and the menu will exit if `'x'` or `'X'` is pressed.

---

### Section B: Programming (Written) `[4 Ã— 5 = 20 Marks]`

**1.** Write a program showing a menu of following things:

- **a.** Enter your Roll number
- **b.** Start Exam
- **c.** Show the results of all the students
- **d.** Exit from the menu

**2.** When `'a'` is pressed: A function should ask for entering a roll number from the keyboard. Then store the roll number in an array such a way that the array is sorted ascendingly.

**3.** When `'b'` is pressed: The user has to enter his/her answers of above 35 questions. These will also be stored in a separate array. The given values will be matched with a given correct answer keys. And result will be stored in a separate array.

**4.** When `'c'` is pressed: The marks will be printed along with the roll in the monitor. however, marks will be sorted from highest to lowest.
