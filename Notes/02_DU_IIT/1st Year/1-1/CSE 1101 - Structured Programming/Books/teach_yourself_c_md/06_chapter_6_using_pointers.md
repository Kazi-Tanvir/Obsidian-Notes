# 6 Using Pointers

THIS chapter covers one of C's most important and sometimes most troublesome features: the *pointer*. A pointer is basically the address of an object. One reason that pointers are so important is that much of the power of the C language is derived from the unique way in which they are implemented. You will learn about the special pointer operators, pointer arithmetic, and how arrays and pointers are related. Also, you will be introduced to using pointers as parameters to functions.

---

### Review Skills Check

Before proceeding, you should be able to answer these questions and perform these exercises:

1. Write a program that inputs 10 integers into an array. Then have the program display the sum of the even numbers and the sum of the odd numbers.
2. Write a program that simulates a log-on to a remote system. The system can be accessed only if the user knows the password, which in this case is "Tristan." Give the user three tries to enter the correct password. If the user succeeds, simply print **Log-on Successful** and exit. If the user fails after three attempts to enter the correct password, display **Access Denied** and exit.
3. What is wrong with this fragment?
```c
char name[10] = "Thomas Jefferson";
```
4. What is a null string?
5. What does `strcpy()` do? What does `strcmp()` do?
6. Write a program that creates a string table consisting of names and telephone numbers. Initialize the array with some names of people you know and their phone numbers. Next, have the program request a name and print the associated telephone number. In other words, create a computerized telephone book.

---

## 6.1 UNDERSTAND POINTER BASICS

A pointer is a variable that holds the memory address of another object. For example, if a variable called **p** contains the address of another variable called **q**, then **p** is said to *point to* **q**. Therefore if **q** is at location 100 in memory, then **p** would have the value 100.

To declare a pointer variable, use this general form:

```c
type *var-name;
```

Here, *type* is the *base type* of the pointer. The base type specifies the type of the object that the pointer can point to. Notice that the variable name is preceded by an asterisk. This tells the computer that a pointer variable is being created. For example, the following statement creates a pointer to an integer:

```c
int *p;
```

C contains two special pointer operators: `*` and `&`. The `&` operator returns the address of the variable it precedes. The `*` operator returns the value stored at the address that it precedes. (The `*` pointer operator has no relationship to the multiplication operator, which uses the same symbol.) For example, examine this short program:

```c
#include <stdio.h>

int main(void)
{
    int *p, q;

    q = 199; /* assign q 199 */

    p = &q; /* assign p the address of q */

    printf("%d", *p); /* display q's value using pointer */

    return 0;
}
```

This program prints **199** on the screen. Let's see why.

First, the line

```c
int *p, q;
```

defines two variables: `p`, which is declared as an integer pointer, and `q`, which is an integer. Next, `q` is assigned the value 199. In the next line, `p` is assigned the address of `q`. You can verbalize the `&` operator as "address of." Therefore, this line can be read as "assign `p` the address of `q`." Finally, the value is displayed using the `*` operator applied to `p`. The `*` operator can be verbalized as "at address." Therefore, the `printf()` statement can be read as "print the value at address `p`," which is 199.

When a variable's value is referenced through a pointer, the process is called *indirection*.

It is possible to use the `*` operator on the left side of an assignment statement in order to assign a variable a new value given a pointer to it. For example, this program assigns `q` a value indirectly using the pointer `p`:

```c
#include <stdio.h>

int main(void)
{
    int *p, q;

    p = &q; /* get q's address */

    *p = 199; /* assign q a value using a pointer */

    printf("q's value is %d", q);

    return 0;
}
```

In the two simple example programs just shown, there is no reason to use a pointer. However, as you learn more about C, you will understand why pointers are important. Pointers are used to support linked lists and binary trees, for example.

The base type of a pointer is very important. Although C allows any type of pointer to point anywhere in memory, it is the base type that determines how the object pointed to will be treated. To understand the importance of this, consider the following fragment:

```c
int q;
double *fp;

fp = &q;

/* what does this line do? */
*fp = 100.23;
```

Although not syntactically incorrect, this fragment is wrong. The pointer `fp` is assigned the address of an integer. This address is then used on the left side of an assignment statement to assign a floating-point value. However, ints are usually shorter than doubles, and this assignment statement causes memory adjacent to `q` to be overwritten. For example, in an environment in which integers are 2 bytes and doubles are 8 bytes, the assignment statement uses the 2 bytes allocated to `q` as well as 6 adjacent bytes, thus causing an error.

In general, the C compiler uses the base type to determine how many bytes are in the object pointed to by the pointer. This is how C knows how many bytes to copy when an indirect assignment is made, or how many bytes to compare if an indirect comparison is made. Therefore, it is very important that you always use the proper base type for a pointer. (Except in special cases, never use a pointer of one type to point to an object of a different type.)

If you attempt to use a pointer before it has been assigned the address of a variable, your program will probably crash. Remember, declaring a pointer variable simply creates a variable capable of holding a memory address. It does not give it any meaningful initial value. This is why the following fragment is incorrect:

```c
int main(void)
{
    int *p;

    *p = 10; /* incorrect - p is not pointing to anything */
}
```

As the comment notes, the pointer `p` is not pointing to any known object. Hence, trying to indirectly assign a value using `p` is meaningless and dangerous.

As pointers are defined in C, a pointer that contains a null value (zero) is assumed to be unused and pointing at nothing. In C, a null is, by convention, assumed to be an invalid memory address. However, the compiler will still let you use a null pointer, usually with disastrous results.

### EXAMPLES

1. To graphically illustrate how indirection works, assume these declarations:

```c
int *p, q;
```

Further assume that `q` is located at memory address 102 and that `p` is right before it, at location 100. After this statement

```c
p = &q;
```

the pointer `p` contains the value 102. Therefore, after this assignment, memory looks like this:

```
Location      Contents
 100           [ 102     ] ---> p points to q
 102           [ unknown ]
```

After the statement

```c
*p = 1000;
```

executes, memory looks like this:

```
Location      Contents
 100           [ 102     ] ---> p points to q
 102           [ 1000    ]
```

Remember, the value of `p` has nothing to do with the *value* of `q`. It simply holds `q`'s *address*, to which the indirection operator may be applied.

2. To illustrate why you must make sure that the base type of a pointer is the same as the object it points to, try this incorrect but benign program. (Some compilers may generate a warning message when you compile it, but none will issue an actual error message and stop compilation.)

```c
/* This program is wrong, but harmless. */

#include <stdio.h>

int main(void)
{
    int *p;
    double q, temp;

    temp = 1234.34;

    p = &temp; /* attempt to assign q a value using */
    q = *p;    /* indirection through an integer pointer */

    printf("%f", q); /* this will not print 1234.34 */

    return 0;
}
```

Even though `p` points to `temp`, which does, indeed, hold the value 1234.34, the assignment

```c
q = *p;
```

fails to copy the number because only 2 bytes (assuming 2-byte integers) will be transferred. Since `p` is an integer pointer, it cannot be used to transfer an 8-byte quantity (assuming 8-byte doubles).

### EXERCISES

1. What is a pointer?
2. What are the pointer operators and what are their effects?
3. Why is the base type of a pointer important?
4. Write a program with a `for` loop that counts from 0 to 9, displaying the numbers on the screen. Print the numbers using a pointer.

---

## 6.2 LEARN RESTRICTIONS TO POINTER EXPRESSIONS

In general, pointers may be used like other variables. However, you need to understand a few rules and restrictions.

In addition to the `*` and `&` operators, there are only four other operators that may be applied to pointer variables: the arithmetic operators `+`, `++`, `-`, and `--`. Further, you may add or subtract only *integer* quantities. You cannot, for example, add a floating-point number to a pointer.

Pointer arithmetic differs from "normal" arithmetic in one very important way: It is performed relative to the base type of the pointer. Each time a pointer is incremented, it will point to the next item, as defined by its base type, beyond the one currently pointed to. For example, assume that an integer pointer called `p` contains the address 200. After the statement

```c
p++;
```

executes, `p` will have the value 202, assuming integers are two bytes long. By the same token, if `p` had been a float pointer (assuming 4-byte floats), then the resultant value contained in `p` would have been 204.

The only pointer arithmetic that appears as "normal" occurs when `char` pointers are used. Because characters are one byte long, an increment increases the pointer's value by one, and a decrement decreases its value by one.

You may add or subtract any integer quantity to or from a pointer. For example, the following is a valid fragment:

```c
int *p;
.
.
.
p = p + 200;
```

This statement causes `p` to point to the 200th integer past the one to which `p` was previously pointing.

Aside from addition and subtraction of an integer, you may not perform any other type of arithmetic operations—you may not multiply, divide, or take the modulus of a pointer. However, you may subtract one pointer from another in order to find the number of elements separating them.

It is possible to apply the increment and decrement operators to either the pointer itself or the object to which it points. However, you must be careful when attempting to modify the object pointed to by a pointer. For example, assume that `p` points to an integer that contains the value 1. What do you think the following statement will do?

```c
*p++;
```

Contrary to what you might think, this statement first increments `p` and then obtains the value at the new location. To increment what is pointed to by a pointer, you must use a form like this:

```c
(*p)++;
```

The parentheses cause the value pointed to by `p` to be incremented.

You may compare two pointers using the relational operators. However, pointer comparisons make sense only if the pointers relate to each other—if they both point to the same object, for example. (Soon you will see an example of pointer comparisons.) You may also compare a pointer to zero to see if it is a null pointer.

At this point you might be wondering what use there is for pointer arithmetic. You will shortly see, however, that it is one of the most valuable components of the C language.

### EXAMPLES

1. You can use `printf()` to display the memory address contained in a pointer by using the `%p` format specifier. We can use this `printf()` capability to illustrate several aspects of pointer arithmetic. The following program, for example, shows how all pointer arithmetic is relative to the base type of the pointer.

```c
#include <stdio.h>

int main(void)
{
    char *cp, ch;
    int *ip, i;
    float *fp, f;
    double *dp, d;

    cp = &ch;
    ip = &i;
    fp = &f;
    dp = &d;

    /* print the current values */
    printf("%p %p %p %p\n", cp, ip, fp, dp);

    /* now increment them by one */
    cp++;
    ip++;
    fp++;
    dp++;

    /* print their new values */
    printf("%p %p %p %p\n", cp, ip, fp, dp);

    return 0;
}
```

Although the values contained in the pointer variables in this program will vary widely between compilers and even between versions of the same compiler, you will see that the address pointed to by `ch` will be incremented by one byte. The others will be incremented by the number of bytes in their base types. For example, in a 16-bit environment this will typically be 2 for ints, 4 for floats, and 8 for doubles.

2. The following program illustrates the need for parentheses when you want to increment the object pointed to by a pointer instead of the pointer itself.

```c
#include <stdio.h>

int main(void)
{
    int *p, q;

    p = &q;

    q = 1;
    printf("%p ", p);

    *p++; /* this will not increment q */
    printf("%d %p", q, p);

    return 0;
}
```

After this program has executed, `q` still has the value 1, but `p` has been incremented. However, if the program is written like this:

```c
#include <stdio.h>

int main(void)
{
    int *p, q;

    p = &q;

    q = 1;
    printf("%p ", p);

    (*p)++; /* now q is incremented and p is unchanged */
    printf("%d %p", q, p);

    return 0;
}
```

`q` is incremented to 2 and `p` is unchanged.

### EXERCISES

1. What is wrong with this fragment?
```c
int *p, i;

p = &i;

p = p * 8;
```
2. Can you add a floating-point number to a pointer?
3. Assume that `p` is a float pointer that currently points to location 100 and that floats are 4 bytes long. What is the value of `p` after this fragment has executed?
```c
p = p + 2;
```

---

## 6.3 USE POINTERS WITH ARRAYS

In C, pointers and arrays are closely related. In fact, they are often interchangeable. It is this relationship between the two that makes their implementation both unique and powerful.

When you use an array name without an index, you are generating a pointer to the start of the array. This is why no indexes are used when you read a string using `gets()`, for example. What is being passed to `gets()` is not an array, but a pointer. In fact, you cannot pass an array to a function in C; you may only pass a pointer to the array. This important point was not mentioned in the preceding chapter on arrays because you had not yet learned about pointers. However, this fact is crucial to understanding the C language. The `gets()` function uses the pointer to load the array it points to with the characters you enter at the keyboard. You will see how this is done later.

Since an array name without an index is a pointer to the start of the array, it stands to reason that you can assign that value to another pointer and access the array using pointer arithmetic. And, in fact, this is exactly what you can do. Consider this program:

```c
#include <stdio.h>

int main(void)
{
    int a[10] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
    int *p;

    p = a; /* assign p the address of start of a */

    /* this prints a's first, second and third elements */
    printf("%d %d %d\n", *p, *(p+1), *(p+2));

    /* this does the same thing using a */
    printf("%d %d %d", a[0], a[1], a[2]);

    return 0;
}
```

Here, both `printf()` statements display the same thing. The parentheses in expressions such as `*(p+2)` are necessary because the `*` has a higher precedence than the `+` operator.

Now you should be able to fully understand why pointer arithmetic is done relative to the base type—it allows arrays and pointers to relate to each other.

To use a pointer to access multidimensional arrays, you must manually do what the compiler does automatically. For example, in this array:

```c
float balance[10][5];
```

each row is five elements long. Therefore, to access `balance[3][1]` using a pointer you must use a fragment like this:

```c
float *p;

p = (float *) balance;
*(p + (3*5) + 1)
```

To reach the desired element, you must multiply the row number by the number of elements in the row and then add the number of the element within the row. Generally, with multidimensional arrays it is easier to use array indexing rather than pointer arithmetic.

In the preceding example, the cast of `balance` to `float *` was necessary. Since the array is being indexed manually, the pointer arithmetic must be relative to a float pointer. However, the type of pointer generated by `balance` is to a two-dimensional array of floats. Thus, there is need for the cast.

Pointers and arrays are linked by more than the fact that by using pointer arithmetic you can access array elements. You might be surprised to learn that you can index a pointer as if it were an array. The following program, for example, is perfectly valid:

```c
#include <stdio.h>

int main(void)
{
    char str[] = "Pointers are fun";
    char *p;
    int i;

    p = str;

    /* loop until null is found */
    for(i=0; p[i]; i++)
        printf("%c", p[i]);

    return 0;
}
```

Keep one point firmly in mind: you should index a pointer only when that pointer points to an array. While the following fragment is syntactically correct, it is wrong; if you tried to execute it, you would probably crash your computer.

```c
char *p, ch;
int i;

p = &ch;
for(i=0; i<10; i++) p[i] = 'A'+i; /* wrong */
```

Since `ch` is not an array, it cannot be meaningfully indexed.

Although you can index a pointer as if it were an array, you will seldom want to do this because pointer arithmetic is usually more convenient. Also, in some cases a C compiler can generate faster executable code for an expression involving pointers than for a comparable expression using arrays.

Because an array name without an index is a pointer to the start of the array, you can, if you choose, use pointer arithmetic rather than array indexing to access elements of the array. For example, this program is perfectly valid and prints **c** on the screen:

```c
#include <stdio.h>

int main(void)
{
    char str[80];

    *(str+3) = 'c';
    printf("%c", *(str+3));

    return 0;
}
```

You cannot, however, modify the value of the pointer generated by using an array name. For example, assuming the previous program, this is an invalid statement:

```c
str++;
```

The pointer that is generated by `str` must be thought of as a constant that always points to the start of the array. Therefore, it is invalid to modify it and the compiler will report an error.

### EXAMPLES

1. Two of C's library functions, `toupper()` and `tolower()`, are called using a character argument. In the case of `toupper()`, if the character is a lowercase letter, the uppercase equivalent is returned; otherwise the character is returned unchanged. For `tolower()`, if the character is an uppercase letter, the lowercase equivalent is returned; otherwise the character is returned unchanged. These functions use the header file CTYPE.H. The following program requests a string from the user and then prints the string, first in uppercase letters and then in lowercase. This version uses array indexing to access the characters in the string so they can be converted into the appropriate case.

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char str[80];
    int i;

    printf("Enter a string: ");
    gets(str);

    for(i=0; str[i]; i++)
        str[i] = toupper(str[i]);

    printf("%s\n", str); /* uppercase string */

    for(i=0; str[i]; i++)
        str[i] = tolower(str[i]);

    printf("%s\n", str); /* lowercase string */

    return 0;
}
```

The same program is shown below, only this time, a pointer is used to access the string. This second approach is the way you would see this program written by professional C programmers because incrementing a pointer is often faster than indexing an array.

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char str[80], *p;

    printf("Enter a string: ");
    gets(str);
    p = str;

    while(*p) {
        *p = toupper(*p);
        p++;
    }

    printf("%s\n", str); /* uppercase string */

    p = str; /* reset p */

    while(*p) {
        *p = tolower(*p);
        p++;
    }

    printf("%s\n", str); /* lowercase string */

    return 0;
}
```

Before leaving this example, a small digression is in order. The routine

```c
while(*p) {
    *p = toupper(*p);
    p++;
}
```

will generally be written by experienced programmers like this:

```c
while(*p)
    *p++ = toupper(*p);
```

Because the `++` follows the `p`, the value pointed to by `p` is first modified and then `p` is incremented to point to the next element. Since this is the way C code is often written, this book will use the more compact form from time to time when it seems appropriate.

2. Remember that although most of the examples have been incrementing pointers, you can decrement a pointer as well. For example, the following program uses a pointer to copy the contents of one string into another in reversed order.

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char str1[] = "Pointers are fun to use";
    char str2[80], *p1, *p2;

    /* make p point to end of str1 */
    p1 = str1 + strlen(str1) - 1;

    p2 = str2;

    while(p1 >= str1)
        *p2++ = *p1--;

    /* null terminate str2 */
    *p2 = '\0';

    printf("%s %s", str1, str2);

    return 0;
}
```

This program works by setting `p1` to point to the end of `str1`, and `p2` to the start of `str2`. It then copies the contents of `str1` into `str2` in reverse order. Notice the pointer comparison in the `while` loop. It is used to stop the copying process when the start of `str1` is reached.

Also, notice the use of the compacted forms `*p2++` and `*p1--`. The loop is the equivalent of this one:

```c
while(p1 >= str1) {
    *p2 = *p1;
    p1--;
    p2++;
}
```

Again, it is important for you to become familiar with the compact form of these types of pointer operations.

### EXERCISES

1. Is this fragment correct?
```c
int count[10];
.
.
.
count = count + 2;
```
2. What value does this fragment display?
```c
int temp[5] = {10, 19, 23, 8, 9};
int *p;

p = temp;

printf("%d", *(p+3));
```
3. Write a program that inputs a string. Have the program look for the first space. If it finds one, print the remainder of the string.

---

## 6.4 USE POINTERS TO STRING CONSTANTS

As you know, C allows string constants enclosed between double quotes to be used in a program. When the compiler encounters such a string, it stores it in the program's string table and generates a pointer to the string. For this reason, the following program is correct and prints **one two three** on the screen.

```c
#include <stdio.h>

int main(void)
{
    char *p;

    p = "one two three";

    printf(p);

    return 0;
}
```

Let's see how this program works. First, `p` is declared as a character pointer. This means that it may point to an array of characters. When the compiler compiles the line

```c
p = "one two three";
```

it stores the string in the program's string table and assigns to `p` the address of the string in the table. Therefore, when `p` is used in the `printf()` statement, **one two three** is displayed on the screen.

This program can be written more efficiently, as shown here:

```c
#include <stdio.h>

int main(void)
{
    char *p = "one two three";

    printf(p);

    return 0;
}
```

Here, `p` is initialized to point to the string.

### EXAMPLES

1. This program continues to read strings until you enter **stop**:

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *p = "stop";
    char str[80];

    do {
        printf("Enter a string: ");
        gets(str);
    } while(strcmp(p, str));

    return 0;
}
```

2. Using pointers to string constants can be very helpful when those constants are quite long. For example, suppose that you had a program that at various times would prompt the user to insert a diskette into drive A. To save yourself some typing, you might elect to initialize a pointer to the string and then simply use the pointer when the message needed to be displayed; for example:

```c
char *InsDisk = "Insert disk into drive A, then press ENTER";
.
.
.
printf(InsDisk);
.
.
.
printf(InsDisk);
```

Another advantage to this approach is that to change the prompt, you only need to change it once, and all references to it will reflect the change.

### EXERCISE

1. Write a program that creates three character pointers and initialize them so that one points to the string "one", the second to the string "two", and the third to the string "three". Next, have the program print all six permutations of these three strings. (For example, one permutation is "one two three", another is "two one three".)

---

## 6.5 CREATE ARRAYS OF POINTERS

Pointers may be arrayed like any other data type. For example, the following statement declares an integer pointer array that has 20 elements:

```c
int *pa[20];
```

The address of an integer variable called `myvar` is assigned to the ninth element of the array as follows:

```c
pa[8] = &myvar;
```

Because `pa` is an array of pointers, the only values that the array elements may hold are the addresses of integer variables. To assign the integer pointed to by the third element of `pa` the value 100, use the statement:

```c
*pa[2] = 100;
```

### EXAMPLES

1. Probably the single most common use of arrays of pointers is to create string tables in much the same way that unsized arrays were used in the previous chapter. For example, this function displays an error message based on the value of its parameter `err_num`.

```c
char *p[] = {
    "Input exceeds field width",
    "Out of range",
    "Printer not turned on",
    "Paper out",
    "Disk full",
    "Disk write error"
};

void error(int err_num)
{
    printf(p[err_num]);
}
```

2. The following program uses a two-dimensional array of pointers to create a string table that links apple varieties with their colors. To use the program, enter the name of the apple, and the program will tell you its color.

```c
#include <stdio.h>
#include <string.h>

char *p[][2] = {
    "Red Delicious", "red",
    "Golden Delicious", "yellow",
    "Winesap", "red",
    "Gala", "reddish orange",
    "Lodi", "green",
    "Mutsu", "yellow",
    "Cortland", "red",
    "Jonathan", "red",
    "", "" /* terminate the table with null strings */
};

int main(void)
{
    int i;
    char apple[80];

    printf("Enter name of apple: ");
    gets(apple);

    for(i=0; *p[i][0]; i++) {
        if(!strcmp(apple, p[i][0]))
            printf("%s is %s\n", apple, p[i][1]);
    }

    return 0;
}
```

Look carefully at the condition controlling the `for` loop. The expression `*p[i][0]` gets the value of the first byte of the *i*th string. Since the list is terminated by null strings, this value will be zero (false) when the end of the table is reached. In all other cases it will be nonzero, and the loop will repeat.

### EXERCISE

1. In this exercise, you will create an "executive decision aid." This is a program that answers yes, no, or maybe to a question entered at the keyboard. To create this program use an array of character pointers and initialize them to point to these three strings: "Yes", "No", and "Maybe. Rephrase the question". Next, input the user's question and find the length of the string. Next, use this formula to compute an index into the pointer array:

```c
index = length % 3
```

---

## 6.6 BECOME ACQUAINTED WITH MULTIPLE INDIRECTION

It is possible in C to have a pointer point to another pointer. This is called *multiple indirection* (see Figure 6-1). When a pointer points to another pointer, the first pointer contains the address of the second pointer, which points to the location containing the object.

To declare a pointer to a pointer, an additional asterisk is placed in front of the pointer's name. For example, this declaration tells the compiler that `mp` is a pointer to a character pointer:

```c
char **mp;
```

It is important to understand that `mp` is not a pointer to a character, but rather a pointer to a character pointer.

#### Multiple Indirection Diagram

```
Pointer to pointer ( **mp )  --->  Pointer ( *p )  --->  Variable ( ch )
```

Accessing the target value indirectly pointed to by a pointer to a pointer requires that the asterisk operator be applied twice. For example,

```c
char **mp, *p, ch;

p = &ch; /* get address of ch */
mp = &p; /* get address of p */
**mp = 'A'; /* assign ch the value A using multiple indirection */
```

As the comments suggest, `ch` is assigned a value indirectly using two pointers.

Multiple indirection is not limited to merely "a pointer to a pointer." You can apply the `*` as often as needed. However, multiple indirection beyond a pointer to a pointer is very difficult to follow and is not recommended.

You may not see the need for multiple indirection at this time, but as you learn more about C, you will see some examples in which it is very valuable.

### EXAMPLES

1. The following program assigns `val` a value using multiple indirection. It displays the value first directly, then through the use of multiple indirection.

```c
#include <stdio.h>

int main(void)
{
    float *fp, **mfp, val;

    fp = &val;
    mfp = &fp;

    **mfp = 123.903;
    printf("%f %f", val, **mfp);

    return 0;
}
```

2. This program shows how you can input a string using `gets()` by using a pointer to a pointer to the string.

```c
#include <stdio.h>

int main(void)
{
    char *p, **mp, str[80];

    p = str;
    mp = &p;

    printf("Enter your name: ");
    gets(*mp);
    printf("Hi %s", *mp);

    return 0;
}
```

Notice that when `mp` is used as an argument to both `gets()` and `printf()`, only one `*` is used. This is because both of these functions require a pointer to a string for their operation. Remember, `**mp` is a pointer to `p`. However, `p` is a pointer to `str`. If you are a little confused, don't worry. Over time, you will develop a clearer concept of pointers to pointers.

### EXERCISE

1. To help you understand multiple indirection better, write a program that assigns an integer a value using a pointer to a pointer. Before the program ends, display the addresses of the integer variable, the pointer, and the pointer to the pointer. (Remember, use `%p` to display a pointer value.)

---

## 6.7 USE POINTERS AS PARAMETERS

Pointers may be passed to functions. For example, when you call a function like `strlen()` with the name of a string, you are actually passing a pointer to a function. When you pass a pointer to a function, the function must be declared as receiving a pointer of the same type. In the case of `strlen()`, this is a character pointer. A complete discussion of using pointers as parameters is presented in the next chapter. However, some basic concepts are discussed here.

When you pass a pointer to a function, the code inside that function has access to the variable pointed to by the parameter. This means that the function can change the variable used to call the function. This is why functions like `strcpy()`, for example, can work. Because it is passed a pointer, the function is able to modify the array that receives the string.

Now you can understand why you need to precede a variable's name with `&` when using `scanf()`. In order for `scanf()` to modify the value of one of its arguments, it must be passed a pointer to that argument.

### EXAMPLES

1. Another of C's standard library functions is called `puts()`; it writes its string argument to the screen followed by a newline. The program that follows creates its own version of `puts()` called `myputs()`.

```c
#include <stdio.h>

void myputs(char *p);

int main(void)
{
    myputs("this is a test");

    return 0;
}

void myputs(char *p)
{
    while(*p) { /* loop as long as p does not point to the
                   null that terminates the string */
        printf("%c", *p);
        p++; /* go to next character */
    }
    printf("\n");
}
```

This program illustrates a very important point that was mentioned earlier in this chapter. When the compiler encounters a string constant, it places it into the program's string table and generates a pointer to it. Therefore, the `myputs()` function is actually called with a character pointer, and the parameter `p` must be declared as a character pointer in order to receive it.

2. The following program shows one way to implement the `strcpy()` function, called `mystrcpy()`.

```c
#include <stdio.h>

void mystrcpy(char *to, char *from);

int main(void)
{
    char str[80];

    mystrcpy(str, "this is a test");
    printf(str);

    return 0;
}

void mystrcpy(char *to, char *from)
{
    while(*from) *to++ = *from++;
    *to = '\0'; /* null terminates the string */
}
```

### EXERCISES

1. Write your own version of `strcat()` called `mystrcat()`, and write a short program that demonstrates it.
2. Write a program that passes a pointer to an integer variable to a function. Inside that function, assign the variable the value -1. After the function has returned, demonstrate that the variable does, indeed, contain -1 by printing its value.

---

## Mastery Skills Check

At this point you should be able to perform these exercises and answer these questions:

1. Show how to declare a pointer to a **double**.
2. Write a program that assigns a value to a variable indirectly by using a pointer to that variable.
3. Is this fragment correct? If not, why not?
```c
int main(void)
{
    char *p;

    printf("Enter a string: ");
    gets(p);

    return 0;
}
```
4. How do pointers and arrays relate to each other?
5. Given this fragment:
```c
char *p, str[80] = "this is a test";

p = str;
```
show two ways to access the 'i' in "this."
6. Assume that `p` is declared as a pointer to a **double** and contains the address 100. Further, assume that **doubles** are 8 bytes long. After `p` is incremented, what will its value be?

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. What is the advantage of using pointers over array indexing?
2. Below is a program that counts the number of spaces in a string entered by the user. Rewrite the program so that it uses pointer arithmetic rather than array indexing.

```c
#include <stdio.h>

int main(void)
{
    char str[80];
    int i, spaces;

    printf("Enter a string: ");
    gets(str);

    spaces = 0;
    for(i=0; str[i]; i++)
        if(str[i]==' ') spaces++;

    printf("Number of spaces: %d", spaces);

    return 0;
}
```

3. Rewrite the following array reference using pointer arithmetic:
```c
int count[100][10];

count[44][8] = 99;
```
