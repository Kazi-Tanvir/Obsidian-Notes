# 7 A Closer Look at Functions

AT the very foundation of C is the function. All action statements must appear within one and an understanding of its operation is crucial to successful C programming. This chapter takes a close look at several important topics related to functions.

---

### Review Skills Check

Before proceeding you should be able to answer these questions and perform these exercises:

1. What does this fragment do?
```c
int i, *p;

p = &i;
*p = 19;
```
2. What is generated when you use an array name without an index?
3. Is this fragment correct? If it is correct, explain why it works.
```c
char *p = "this is a string";
```
4. Write a short program that assigns a floating-point value to a variable indirectly using a pointer to the variable.
5. Write your own version of `strlen()`, called `mystrlen()`, and demonstrate it in a program.
6. Is this fragment correct? If it is, what does the program display?
```c
char str[6];

strcpy(str, "ABCDEFG");
printf("%c", *(str+2));
```

---

## 7.1 UNDERSTAND FUNCTION PROTOTYPES

In Chapter 1 you were briefly introduced to the function prototype. Now it is time for you to understand precisely what a prototype does and why it is important to C programming. Function prototypes were not supported by the original version of C. They were added when C was standardized in 1989. Many consider prototypes to be the single most important addition made to the C language since its creation. Prototypes are not technically necessary. However, for reasons that will become self-evident, they should be used in all programs that you write.

The general form of a function prototype is shown here:

```c
type function-name(type parameter-name1,
                   type parameter-name2,
                   .
                   .
                   .
                   type parameter-nameN);
```

A prototype declares three attributes associated with a function:
1. Its return type.
2. The number of its parameters.
3. The type of its parameters.

Prototypes provide several benefits. They inform the compiler about the return type of a function. They allow the compiler to find and report illegal type conversions between the type of arguments used to call a function and the type definition of its parameters. Prototypes also enable the compiler to report when the number of arguments passed to a function is not the same as the number of parameters declared by the function. Let's look at each of these.

When you call a function, the compiler needs to know the type of data returned by that function so that it can generate the proper code to handle that data. The reason for this is easy to understand: different data types have different sizes. The code that handles an integer return type will be different from that which handles a **double**, for example. If you use a function that is not prototyped, then the compiler will simply assume that it is returning an integer. However, if it is actually returning some other type, an error will occur. If the function is in the same file as the rest of your program, then the compiler will catch this error. But if the function is in another file or a library, then the error will go uncaught—and this will lead to trouble when your program is executed.

In the absence of a function prototype, it is not syntactically wrong to call a function with incompatible arguments or with more or less arguments than the function has parameters. Of course, doing either of these is obviously incorrect even though the compiler may accept your program without complaint. The use of a function prototype prevents these errors by enabling the compiler to find them. It is important to understand, however, that not all kinds of type conversions are illegal in a function call. In fact, C automatically converts most types of arguments into the type of data specified by the parameter. But a few type conversions are inherently wrong. For example, you cannot convert an integer into a pointer. A function prototype allows the compiler to catch and return this type of error.

As mentioned, as important as prototypes are, they are not currently required. Because of the need to maintain compatibility with older code, all C compilers still support non-prototyped programs. Of course, at some point in the future, this situation may change.

In early versions of C, before prototypes were invented, it was still necessary to tell the compiler about the return type of a function (unless it returned type **int**) for the reasons explained earlier. This was done using a forerunner of the prototype, called a *forward declaration* or a *forward reference*. A forward declaration is essentially a truncated form of a prototype that declares only the return type of a function—not the type and number of its parameters. Although forward declarations are obsolete, they are still allowed for compatibility with older code.

The following program demonstrates an old-style forward declaration. It uses it to inform the compiler of `volume()`'s return type.

```c
#include <stdio.h>

double volume(); /* old-style forward declaration for volume() */

int main(void)
{
    double vol;

    vol = volume(12.2, 5.67, 9.03);
    printf("Volume: %f", vol);

    return 0;
}

/* Compute the volume of a cube. */
double volume(double s1, double s2, double s3)
{
    return s1 * s2 * s3;
}
```

Since the old-style declaration does not inform the compiler about any of `volume()`'s parameters it is not a function prototype. Instead, it simply states `volume()`'s return type. The trouble is that the lack of a full prototype will allow `volume()` to be called using an incorrect type and/or number of arguments. For example, given the preceding program, the following will not generate a compiler error message even though it is wrong.

```c
volume(120.2, 99.3); /* missing last arg */
```

Since the compiler has not been given information about `volume()`'s parameters it won't catch the fact that this call is wrong.

Although the old-style forward declaration is no longer used in new code, you will still find it quite frequently in older programs. If you will be updating older programs, you should consider adding prototypes to be your first job.

When function prototypes were added to C, two minor compatibility problems between the old version of C and the ANSI version of C had to be resolved. The first issue was how to handle the old-style forward declaration, which does not use a parameter list. To do so, the ANSI C standard specifies that when a function declaration occurs without a parameter list, nothing whatsoever is being said about the parameters to the function. It might have parameters, it might not. This allows old-style declarations to coexist with prototypes. But it also leads to a question: how do you prototype a function that takes no arguments? For example, this function simply outputs a line of periods:

```c
void line()
{
    int i;

    for(i=0; i<80; i++) printf(".");
}
```

If you try to use the following as a prototype, it won't work because the compiler will think that you are simply using the old-style declaration method:

```c
void line();
```

The solution to this problem is through the use of the **void** keyword. When a function has no parameters, its prototype uses **void** inside the parentheses. For example, here is `line()`'s proper prototype:

```c
void line(void);
```

This explicitly tells the compiler that the function has no parameters, and any call to that function that has parameters is an error. You must make sure to also use **void** when the function is defined. For example, `line()` must look like this:

```c
void line(void)
{
    int i;

    for(i=0; i<80; i++) printf(".");
}
```

Since we have been using **void** to specify empty parameter lists since Chapter 1, this mechanism is already familiar to you.

The second issue related to prototyping is the way it affects C's automatic type promotions. Because of some features of the environment in which C was developed, when a non-prototyped function is called, all integral promotions take place (for example, characters are converted to integers) and all floats are converted to **doubles**. However, these type promotions seem to violate the purpose of the prototype. The resolution to this problem is that when a prototype exists, the types specified in the prototype are maintained, and no type promotions will occur.

There is one other special case that relates to prototypes: variable length argument lists. We won't be creating any functions in this book that use a variable number of arguments because they require the use of some advanced techniques. But it is possible to do so, and it is sometimes quite useful. For example, both `printf()` and `scanf()` accept a variable number of arguments. To specify a variable number of arguments, use `...` in the prototype. For example,

```c
int myfunc(int a, ...);
```

specifies a function that has one integer parameter and a variable number of other parameters.

In C programming there has been a long-standing confusion about the usage of two terms: *declaration* and *definition*. A declaration specifies the type of an object. A definition causes storage for an object to be created. As these terms relate to functions, a prototype is a declaration. The function, itself, which contains the body of the function is a definition.

In C, it is also legal to fully define a function prior to its first use, thus eliminating the need for a separate prototype. However, this works only in very small programs. In real-world applications, this option is not feasible. For all practical purposes, function prototypes must exist for all functions that your program will use.

Remember that if a function does not return a value, then its return type should be specified as **void**—both in its definition and in its prototype.

Function prototypes enable you to write better, more reliable programs because they help ensure that the functions in your programs are being called with correct types and numbers of arguments. Fully prototyped programs are the norm and represent the current state of the art of C programming. Frankly, no professional C programmer today would write programs without them. Also, future versions of the ANSI C standard may mandate function prototypes and C++ requires them now. Although prototypes are still technically optional, their use is nearly universal. You should use them in all of the programs you write.

### EXAMPLES

1. To see how a function prototype can catch an error, try compiling this version of the volume program, which includes `volume()`'s full prototype:

```c
#include <stdio.h>

/* this is volume()'s full prototype */
double volume(double s1, double s2, double s3);

int main(void)
{
    double vol;

    vol = volume(12.2, 5.67, 9.03, 10.2); /* error */
    printf("Volume: %f", vol);

    return 0;
}

/* Compute the volume of a cube. */
double volume(double s1, double s2, double s3)
{
    return s1 * s2 * s3;
}
```

As you will see, this program will not compile because the compiler knows that `volume()` is declared as having only three parameters, but the program is attempting to call it with four parameters.

2. As explained, if a function is defined before it is called, it does not require a separate prototype. For example, the following program is perfectly valid:

```c
#include <stdio.h>

/* define getnum() prior to its first use */
float getnum(void)
{
    float x;

    printf("Enter a number: ");
    scanf("%f", &x);
    return x;
}

int main(void)
{
    float i;

    i = getnum();
    printf("%f", i);

    return 0;
}
```

Since `getnum()` is defined before it is used, the compiler knows what type of data it returns and that it has no parameters. A separate prototype is not needed. The reason that you will seldom use this method is that large programs are typically spread across several files. Since you can't define a function more than once, prototypes are the only way to inform all files about a function. (Multi-file programs are explained in Chapter 11.)

3. As you know, the standard library function `sqrt()` returns a **double** value. You might be wondering how the compiler knows this. The answer is that `sqrt()` is prototyped in its header file MATH.H. To see the importance of using the header file, try this program:

```c
#include <stdio.h>
/* math.h is intentionally not included */

int main(void)
{
    double answer;

    answer = sqrt(9.0);
    printf("%f", answer);

    return 0;
}
```

When you run this program, it displays something other than 3 because the compiler generates code that copies only two bytes (assuming two-byte integers) into `answer` and not the 8 bytes that typically comprise a **double**. If you include MATH.H, the program will work correctly.

In general, each of C's standard library functions has its prototype specified in a header file. For example, `printf()` and `scanf()` have their prototypes in STDIO.H. This is one of the reasons that it is important to include the appropriate header file for each library function you use.

4. There is one situation that you will encounter quite frequently that is, at first, unsettling. Some "character-based" functions have a return type of **int** rather than **char**. For example, the `getchar()` function's return type is **int**, not **char**. The reason for this is found in the fact that C very cleanly handles the conversion of characters to integers and integers back to characters. There is no loss of information. For example, the following program is perfectly valid:

```c
#include <stdio.h>

int get_a_char(void);

int main(void)
{
    char ch;

    ch = get_a_char();
    printf("%c", ch);

    return 0;
}

int get_a_char(void)
{
    return 'a';
}
```

When `get_a_char()` returns, it elevates the character 'a' to an integer by adding a high-order byte (or bytes) containing zeros. When this value is assigned to `ch` in `main()`, the high-order byte (or bytes) is removed. One reason to declare functions like `get_a_char()` as returning an integer instead of a character is to allow various error values to be returned that are intentionally outside the range of a `char`.

5. When a function returns a pointer, both the function and its prototype must declare the same pointer return type. For example, consider this short program:

```c
#include <stdio.h>

int *init(int x);
int count;

int main(void)
{
    int *p;

    p = init(110); /* return pointer */

    printf("count (through p) is %d", *p);

    return 0;
}

int *init(int x)
{
    count = x;

    return &count; /* return a pointer */
}
```

As you can see, the function `init()` returns a pointer to the global variable `count`. Notice the way that the return type for `init()` is specified. This same general form is used for any sort of pointer return type. Although this example is trivial, functions that return pointers are quite valuable in many programming situations. One other thing: if a function returns a pointer, then it must make sure that the object being pointed to does not go out-of-scope when the function returns. This means that you must not return pointers to local variables.

6. The `main()` function does not have (nor does it require) a prototype. This allows you to define `main()` any way that is supported by your compiler. This book uses

```c
int main(void) { ...
```

because it is one of the most common forms. Another frequently used form of `main()` is shown here:

```c
void main(void) { ...
```

This form is used when no value is returned by `main()`. Later in this chapter, you will see another form of `main()` that has parameters.

The reason `main()` does not have a prototype is to allow C to be used in the widest variety of environments. Since the precise conditions present at program start-up and what actions must occur at program termination may differ widely from one operating system to the next, C allows the acceptable forms of `main()` to be determined by the compiler. However, nearly all compilers will accept `int main(void)` and `void main(void)`.

### EXERCISES

1. Write a program that creates a function, called `avg()`, that reads ten floating-point numbers entered by the user and returns their average. Use an old-style forward reference and not a function prototype.
2. Rewrite the program from Exercise 1 so that it uses a function prototype.
3. Is the following program correct? If not, why not? If it is, can it be made better?

```c
#include <stdio.h>

double myfunc();

int main(void)
{
    printf("%f", myfunc(10.2));

    return 0;
}

double myfunc(double num)
{
    return num / 2.0;
}
```

4. Show the prototype for a function called `Purge()` that has no parameters and returns a pointer to a **double**.
5. On your own, experiment with the concepts presented in this section.

---

## 7.2 UNDERSTAND RECURSION

Recursion is the process by which something is defined in terms of itself. When applied to computer languages, recursion means that a function can call itself. Not all computer languages support recursive functions, but C does. A very simple example of recursion is shown in this program:

```c
#include <stdio.h>

void recurse(int i);

int main(void)
{
    recurse(0);

    return 0;
}

void recurse(int i)
{
    if(i<10) {
        recurse(i+1); /* recursive call */
        printf("%d ", i);
    }
}
```

This program prints

```
9 8 7 6 5 4 3 2 1 0
```

on the screen. Let's see why.

The `recurse()` function is first called with 0. This is `recurse()`'s first activation. Since 0 is less than 10, `recurse()` then calls itself with the value of `i` (in this case 0) plus 1. This is the second activation of `recurse()`, and `i` equals 1. This causes `recurse()` to be called again using the value 2. This process repeats until `recurse()` is called with the value 10. This causes `recurse()` to return. Since it returns to the point of its call, it will execute the `printf()` statement in its previous activation, print 9, and return. This, then, returns to the point of its call in the previous activation, which causes 8 to be displayed. The process continues until all the calls return, and the program terminates.

It is important to understand that there are not multiple copies of a recursive function. Instead, only one copy exists. When a function is called, storage for its parameters and local data are allocated on the stack. Thus, when a function is called recursively, the function begins executing with a new set of parameters and local variables, but the code that constitutes the function remains the same.

If you think about the preceding program, you will see that recursion is essentially a new type of program control mechanism. This is why every recursive function you write will have a conditional statement that controls whether the function will call itself again or return. Without such a statement, a recursive function will simply run wild, using up all the memory allocated to the stack and then crashing the program.

Recursion is generally employed sparingly. However, it can be quite useful in simplifying certain algorithms. For example, the Quicksort sorting algorithm is difficult to implement without the use of recursion. If you are new to programming in general, you might find yourself uncomfortable with recursion. Don't worry; as you become more experienced, the use of recursive functions will become more natural.

### EXAMPLES

1. The recursive program described above can be altered to print the numbers 0 through 9 on the screen. To accomplish this, only the position of the `printf()` statement needs to be changed, as shown here:

```c
#include <stdio.h>

void recurse(int i);

int main(void)
{
    recurse(0);

    return 0;
}

void recurse(int i)
{
    if(i<10) {
        printf("%d ", i);
        recurse(i+1);
    }
}
```

Because the call to `printf()` now precedes the recursive call to `recurse()`, the numbers are printed in ascending order.

2. The following program demonstrates how recursion can be used to copy one string to another.

```c
#include <stdio.h>

void rcopy(char *s1, char *s2);

int main(void)
{
    char str[80];

    rcopy(str, "this is a test");
    printf(str);

    return 0;
}

/* Copy s2 to s1 using recursion. */
void rcopy(char *s1, char *s2)
{
    if(*s2) { /* if not at end of s2 */
        *s1++ = *s2++;
        rcopy(s1, s2);
    }
    else *s1 = '\0'; /* null terminates the string */
}
```

The program works by assigning the character currently pointed to by `s2` to the one pointed to by `s1`, and then incrementing both pointers. These pointers are then used in a recursive call to `rcopy()`, until `s2` points to the null that terminates the string.

Although this program makes an interesting example of recursion, no professional C programmer would actually code a function like this for one simple reason: efficiency. It takes more time to execute a function call than it does to execute a loop. Therefore, tasks like this will almost always be coded using an iterative approach.

3. It is possible to have a program in which two or more functions are mutually recursive. Mutual recursion occurs when one function calls another, which in turn calls the first. For example, study this short program:

```c
#include <stdio.h>

void f2(int b);
void f1(int a);

int main(void)
{
    f1(30);

    return 0;
}

void f1(int a)
{
    if(a) f2(a-1);
    printf("%d ", a);
}

void f2(int b)
{
    printf(".");
    if(b) f1(b-1);
}
```

This program displays

```
...............0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
```

on the screen. Its output is caused by the way the two functions `f1()` and `f2()` call each other. Each time `f1()` is called, it checks to see if `a` is zero. If not, it calls `f2()` with `a-1`. The `f2()` function first prints a period and then checks to see if `b` is zero. If not, it calls `f1()` with `b-1`, and the process repeats. Eventually, `b` is zero and the function calls start unraveling, causing `f1()` to display the numbers 0 to 30 counting by twos.

### EXERCISES

1. One of the best known examples of recursion is the recursive version of a function that computes the factorial of a number. The factorial of a number is obtained by multiplying the original number by all integers less than it and greater than 1. Therefore, 4 factorial is 4x3x2, or 24. Write a function, called `fact()`, that uses recursion to compute the factorial of its integer argument. Have it return the result. Also, demonstrate its use in a program.
2. What is wrong with this recursive function?

```c
void f(void)
{
    int i;

    printf("in f()\n");

    /* call f() 10 times */
    for(i=0; i<10; i++) f();
}
```

3. Write a program that displays a string on the screen, one character at a time, using a recursive function.

---

## 7.3 TAKE A CLOSER LOOK AT PARAMETERS

For computer languages in general, a subroutine can be passed arguments in one of two ways. The first is called *call by value*. This method copies the value of an argument into the formal parameter of the subroutine. Therefore, changes made to a parameter of the subroutine have *no effect* on the argument used to call it. The second way a subroutine can have arguments passed to it is through *call by reference*. In this method, the address of an argument is copied into the parameter. Inside the subroutine, the address is used to access the actual argument. This means that changes made to the parameter *will affect the argument*.

By default, C uses call by value to pass arguments. This means that you cannot alter the arguments used in a call to a function. What occurs to a parameter inside the function will have no effect on the argument outside the function. However, as you saw in Chapter 6, it is possible to manually construct a call by reference by passing a pointer to an argument. Since this causes the address of the argument to be passed, it then is possible to change the value of the argument outside the function.

The classic example of a call-by-reference function is `swap()`, shown here. It exchanges the value of its two integer arguments.

```c
#include <stdio.h>

void swap(int *i, int *j);

int main(void)
{
    int num1, num2;

    num1 = 100;
    num2 = 800;

    printf("num1: %d num2: %d\n", num1, num2);
    swap(&num1, &num2);
    printf("num1: %d num2: %d\n", num1, num2);

    return 0;
}

/* Exchange the values pointed to by two integer pointers. */
void swap(int *i, int *j)
{
    int temp;

    temp = *i;
    *i = *j;
    *j = temp;
}
```

Since pointers to the two integers are passed to the function, the actual values pointed to by the arguments are exchanged.

As you know, when an array is used as an argument to a function, only the address of the array is passed, not a copy of the entire array, which implies call-by-reference. This means that the parameter declaration must be of a compatible pointer type. There are three ways to declare a parameter that is to receive a pointer to an array. First, the parameter may be declared as an array of the same type and size as that used to call the function. Second, it may be specified as an unsized array. Finally, and most commonly, it may be specified as a pointer to the base type of the array. The following program demonstrates all three methods:

```c
#include <stdio.h>

void f1(int num[5]), f2(int num[]), f3(int *num);

int main(void)
{
    int count[5] = {1, 2, 3, 4, 5};

    f1(count);
    f2(count);
    f3(count);

    return 0;
}

/* parameter specified as array */
void f1(int num[5])
{
    int i;

    for(i=0; i<5; i++) printf("%d ", num[i]);
}

/* parameter specified as unsized array */
void f2(int num[])
{
    int i;

    for(i=0; i<5; i++) printf("%d ", num[i]);
}

/* parameter specified as pointer */
void f3(int *num)
{
    int i;

    for(i=0; i<5; i++) printf("%d ", num[i]);
}
```

Even though the three methods of declaring a parameter that will receive a pointer to an array look different, they all result in a pointer parameter being created.

### EXAMPLE

1. Some computer languages, such as BASIC, provide an input function that allows you to specify a prompting message. C has no counterpart for this type of function. However, you can easily create one. The program shown here uses the function `prompt()` to display a prompting message and then to read a number entered by the user.

```c
#include <stdio.h>

void prompt(char *msg, int *num);

int main(void)
{
    int i;

    prompt("Enter a num: ", &i);
    printf("Your number is: %d", i);

    return 0;
}

void prompt(char *msg, int *num)
{
    printf(msg);
    scanf("%d", num);
}
```

Because the parameter `num` is already a pointer, you do not need to precede it with an `&` in the call to `scanf()`. (In fact, it would be an error to do so.)

### EXERCISES

1. Is this program correct? If not, why not?

```c
#include <stdio.h>

void myfunc(int num, int min, int max);

int main(void)
{
    int i;

    printf("Enter a number between 1 and 10: ");
    myfunc(&i, 1, 10);

    return 0;
}

void myfunc(int num, int min, int max)
{
    do {
        scanf("%d", num);
    } while(*num<min || *num>max);
}
```

2. Write a program that creates an input function similar to `prompt()` described earlier in this section. Have it input a string rather than an integer.
3. Explain the difference between call by value and call by reference.

---

## 7.4 PASS ARGUMENTS TO main( )

Many programs allow command-line arguments to be specified when they are run. A *command-line argument* is the information that follows the program's name on the command line of the operating system. Command-line arguments are used to pass information into a program. For example, when you use a text editor, you probably specify the name of the file you want to edit after the name of the text editor. Assuming you use a text editor called EDTEXT, then this line causes the file TEST to be edited:

```
EDTEXT TEST
```

Here, TEST is a command-line argument.

Your C programs may also utilize command-line arguments. These are passed to a C program through two arguments to the `main()` function. The parameters are called `argc` and `argv`. As you probably guessed, these parameters are optional and are not present when no command-line arguments are being used. Let's look at `argc` and `argv` more closely.

The `argc` parameter holds the number of arguments on the command-line and is an integer. It will always be at least 1 because the name of the program qualifies as the first argument.

The `argv` parameter is an array of string pointers. The most common method for declaring `argv` is shown here:

```c
char *argv[];
```

The empty brackets indicate that it is an array of undetermined length. All command-line arguments are passed to `main()` as strings. To access an individual string, index `argv`. For example, `argv[0]` points to the program's name and `argv[1]` points to the first argument. This program displays all the command-line arguments that are present when it is executed.

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    int i;

    for(i=1; i<argc; i++) printf("%s ", argv[i]);

    return 0;
}
```

C does not specify what constitutes a command-line argument, because operating systems vary considerably on this point. However, the most common convention is as follows: Each command-line argument must be separated by a space or a tab character. Commas, semicolons, and the like are not considered separators. For example,

```
This is a test
```

is made up of four strings, but

```
this, that, and, another
```

is one string.

If you need to pass a command-line argument that does, in fact, contain spaces, you must place it between quotes, as shown in this example:

```
"this is a test"
```

The names of `argv` and `argc` are arbitrary—you can use any names you like. However, `argc` and `argv` are traditional and have been used since C's origin. It is a good idea to use these names so that anyone reading your program can quickly identify them as the command-line parameters.

One last point: the ANSI C standard only defines the `argc` and `argv` parameters. However, your compiler may allow additional parameters to `main()`. For example, some DOS or Windows compatible compilers allow access to environmental information through a command-line argument. Check your compiler's user manual.

### EXAMPLES

1. When you pass numeric data to a program, that data will be received in its string form. Your program will need to convert it into the proper internal format using one or another of C's standard library functions. The most common conversion functions are shown here, using their prototypes:

```c
int atoi(char *str);
double atof(char *str);
long atol(char *str);
```

These functions use the STDLIB.H header file. The `atoi()` function returns the `int` equivalent of its string argument. The `atof()` returns the **double** equivalent of its string argument, and the `atol()` returns the **long** equivalent of its string argument. If you call one of these functions with a string that is not a valid number, zero will be returned. The following program demonstrates these functions. To use it, enter an integer, a long integer, and a floating-point number on the command line. It will then redisplay them on the screen.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int i;
    double d;
    long l;

    i = atoi(argv[1]);
    l = atol(argv[2]);
    d = atof(argv[3]);

    printf("%d %ld %f", i, l, d);

    return 0;
}
```

2. This program converts ounces to pounds. To use it, specify the number of ounces on the command line.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    double pounds;

    pounds = atof(argv[1]) / 16.0;
    printf("%f pounds", pounds);

    return 0;
}
```

3. Although the examples up to this point haven't done so, you should verify in real programs, that the right number of command-line arguments have been supplied by the user. The way to do this is to test the value of `argc`. For example, the ounces-to-pounds program can be improved as shown here:

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    double pounds;

    if(argc!=2) {
        printf("Usage: CONVERT <ounces>\n");
        printf("Try Again");
    }
    else {
        pounds = atof(argv[1]) / 16.0;
        printf("%f pounds", pounds);
    }

    return 0;
}
```

This way the program will perform a conversion only if a command-line argument is present. (Of course, you may prompt the user for any missing information, if you choose.)

Generally, the preceding program will be written by a professional C programmer like this:

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    double pounds;

    if(argc!=2) {
        printf("Usage: CONVERT <ounces>\n");
        printf("Try Again");
        exit(1); /* stop the program */
    }

    pounds = atof(argv[1]) / 16.0;
    printf("%f pounds", pounds);

    return 0;
}
```

When some condition necessary for a program's execution has not been met, most C programmers call the standard library function `exit()` to terminate the program. The `exit()` function has this prototype:

```c
void exit(int return-code);
```

and uses the STDLIB.H header file. When `exit()` terminates the program, it returns the value of `return-code` to the operating system. By convention, most operating systems use a return code of zero to mean that a program has terminated normally. Nonzero values indicate abnormal termination.

### EXERCISES

1. Write a program that accepts two command-line arguments. Have the program compare them and report which is lexicographically greater than the other.
2. Write a program that takes two numeric arguments and displays their sum.
3. Expand the program in Exercise 2 so that it takes three arguments. The first argument must be one of these words: add, subtract, multiply, or divide. Based on the value of the first argument, perform the requested operation on the remaining two numeric arguments.

---

## 7.5 COMPARE OLD-STYLE TO MODERN FUNCTION PARAMETER DECLARATIONS

Early versions of C used a different parameter declaration method than has been shown in this book. This original declaration method is now called the *old-style* or *classic* form. The form used in this book is the *modern form*. It was introduced when the ANSI C standard was created. While the modern form should be used for all new programs, you will still find examples of old-style parameter declarations in older programs and you need to be familiar with it.

The general form of the old-style parameter declaration is shown here:

```c
type function-name(parameter1, parameter2, ... parameterN)
type parameter1;
type parameter2;
.
.
.
type parameterN;
{
    function-code
}
```

Notice that the declaration is divided into two parts. Within the parentheses, only the names of the parameters are specified. Outside the parentheses, the types and names are specified. For example, given the following modern declaration:

```c
float f(char ch, long size, double max)
{
    .
    .
    .
}
```

the equivalent old-style declaration is

```c
float f(ch, size, max)
char ch;
long size;
double max;
{
    .
    .
    .
}
```

One other aspect of the old-style declaration is that you can specify more than one parameter after the type name. For example, this is perfectly valid:

```c
myfunc(i, j, k)
int i, j, k;
{
    .
    .
    .
}
```

The ANSI C standard specifies that either the old-style or the modern declaration form may be used. The reason for this is to maintain compatibility with older C programs. (There are literally millions of lines of C code still in existence that use the old-style form.) So, if you see programs in books or magazines that use the classic form, don't worry; your compiler will be able to compile them. However for all new programs, you should definitely use the modern form.

### EXAMPLE

1. This program uses the old declaration form:

```c
#include <stdio.h>

int area(int l, int w);

int main(void)
{
    printf("area is %d", area(10, 13));
    return 0;
}

int area(l, w)
int l, w;
{
    return l * w;
}
```

Notice that even though the old form of parameter declaration is used to define the function, it is still possible to prototype the function.

### EXERCISE

1. Convert this program so that `f_to_m()` uses the old-style declaration form.

```c
#include <stdio.h>

double f_to_m(double f);

int main(void)
{
    double feet;

    printf("Enter feet: ");
    scanf("%lf", &feet);
    printf("Meters: %f", f_to_m(feet));

    return 0;
}

double f_to_m(double f)
{
    return f / 3.28;
}
```

---

## Mastery Skills Check

At this point you should be able to answer these questions and perform these exercises:

1. How do you prototype a function that does not have parameters?
2. What is a function prototype, and what are the benefits of it?
3. How do command-line arguments get passed to a C program?
4. Write a program that uses a recursive function to display the letters of the alphabet.
5. Write a program that takes a string as a command-line argument. Have it output the string in coded form. To code the string, add 1 to each character.
6. What is the prototype for this function?
```c
double myfunc(int x, int y, char ch)
{
    .
    .
    .
}
```
7. Show how the function in Exercise 6 would be coded using the old-style function declaration.
8. What does the `exit()` function do?
9. What does the `atoi()` function do?

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. Write a program that allows access only if the user enters the correct password as a command-line parameter. If the user enters the right word, print **Access Permitted**; otherwise print **Access Denied**.
2. Create a function called `string_up()` that transforms the string it is called with into uppercase characters. Demonstrate its use in a program. (Hint, use the `toupper()` function to convert lowercase characters into uppercase.)
3. Write a function called `avg()` that averages a list of floating-point values. The function will have two arguments. The first is a pointer to the array containing the numbers; the second is an integer value, which specifies the size of the array. Demonstrate its use in a program.
4. Explain how pointers allow C to construct a call-by-reference parameter.
