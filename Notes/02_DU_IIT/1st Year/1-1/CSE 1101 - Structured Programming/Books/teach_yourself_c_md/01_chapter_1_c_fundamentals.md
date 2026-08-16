# 1 C Fundamentals

THE individual elements of a computer language such as C do not stand alone, but rather in conjunction with one another. Therefore, it is necessary to understand several key aspects of C before examining each element of the language in detail.

To this end, this chapter presents a quick overview of the C language. Its goal is to give you sufficient working knowledge of C so that you can understand the examples in later chapters.

As you work through this chapter, don't worry if a few points are not entirely clear. The main thing you need to understand is how and why the example programs execute as they do. Keep in mind that most of the topics introduced in this chapter will be discussed in greater detail later in this book. In this chapter, you will learn about the basic structure of a C program; what a C statement is; and what variables, constants, and functions are. You will learn how to display text on the screen and input information from the keyboard.

To use this book to the fullest, you must have a computer, a C compiler, and a text editor. (You may also use a C++ compiler. C++ compilers can also compile C programs.) Your compiler may include its own text editor, in which case you won't need a separate one. For the best results, you should work along with the examples and try the exercises.

---

## 1.1 UNDERSTAND THE COMPONENTS OF A C PROGRAM

All C programs share certain essential components and traits. All C programs consist of one or more *functions*, each of which contains one or more *statements*. In C, a function is a named subroutine that can be called by other parts of the program. Functions are the building blocks of C. A statement specifies an action to be performed by the program. In other words, statements are the parts of your program that actually perform operations.

All C statements end with a semicolon. C does not recognize the end of the line as a terminator. This means there are no constraints on the position of statements within a line. Also, you may place two or more statements on one line.

The general form of a C function is shown here:

```c
ret-type function-name(param-list)
{
    statement sequence
}
```

Here, *ret-type* specifies the type of data returned by the function. As you will see, it is possible for a function to return a value. The *function-name* is the name of the function. Information can be passed to a function through its parameters, which are specified in the function's parameter list, *param-list*. The *statement sequence* may be one or more statements. (Technically, a function can contain no statements, but since this means the function performs no action, it is a degenerative case.) If return types and parameters are new concepts, don't worry, they will be explained later in this chapter.

With few exceptions, you can call a function by any name you like. It must be composed of only the upper- and lowercase letters of the alphabet, the digits 0-9, and the underscore. A digit cannot start a function name, however. C is case-sensitive, which means that C recognizes the difference between upper- and lowercase letters. Thus, as far as C is concerned, `Myfunc` and `myfunc` are entirely different names.

Although a C program may contain several functions, the only function that it *must* have is `main()`. The `main()` function is where execution of your program begins. That is, when your program begins running, it starts executing the statements inside `main()`, beginning with the first statement after the opening curly brace. Your program ends when `main()`'s closing curly brace is reached. Of course, the curly brace does not actually exist in the compiled version of your program, but it is helpful to think of it in this way.

Throughout this book, when a function is referred to in text, it will be printed in bold and followed by parentheses. This way, you can see immediately that the name refers to a function, not some other part of the program.

Another important component of all C programs is *library functions*. The ANSI C standard specifies a set of library functions to be supplied by all C compilers, which your program may use. This collection of functions is usually referred to as the *C standard library*. The standard library contains functions to perform disk I/O (input/output), string manipulations, mathematical computations, and much more. When your program is compiled, the code for each library function used by your program is automatically included. This differs from the way some other computer languages work. For example, in BASIC or Pascal, operations such as writing to a file or computing a cosine are performed using keywords that are built into the language. The advantage C gains by having them as library functions is increased flexibility. Library functions can be enhanced and expanded as needed to accommodate changing circumstances. The C language itself does not need to change. As you will see, virtually all C programs you create will use functions from the C standard library.

One of the most common library functions is called `printf()`. This is C's general-purpose output function. The `printf()` function is quite versatile, allowing many variations. Its simplest form is shown here:

```c
printf("string-to-output");
```

The `printf()` function outputs the characters that are contained between the beginning and ending double quotes to the screen. (The double quotes are not displayed on the screen.) In C, one or more characters enclosed between double quotes is called a *string*. The quoted string between `printf()`'s parentheses is said to be an *argument* to `printf()`. In general, information passed to a function is called an argument. In C, calling a library function is a statement; therefore, it must end with a semicolon.

To call a function, you specify its name followed by a parenthesized list of arguments that you will be passing to it. If the function does not require any arguments, no arguments will be specified—and the parenthesized list will be empty. If there is more than one argument, the arguments must be separated by commas.

Another component common to most C programs is the *header file*. In C, information about the standard library functions is found in various files supplied with your compiler. These files all end with a .H extension. The C compiler uses the information in these files to handle the library functions properly. You add these files to your program using the `#include` *preprocessor directive*. All C compilers use as their first phase of compilation a preprocessor, which performs various manipulations on your source file before it is compiled.

Preprocessor directives are not actually part of the C language, but rather instructions from you to the compiler. The `#include` directive tells the preprocessor to read in another file and include it with your program. You will learn more about the preprocessor later in this book.

The most commonly required header file is called STDIO.H. Here is the directive that includes this file:

```c
#include <stdio.h>
```

You can specify the file name in either upper- or lowercase, but lowercase is the traditional method. The STDIO.H header file contains, among other things, information related to the `printf()` library function. Notice that the `#include` directive does not end with a semicolon. The reason for this is that `#include` is not a C keyword that can define a statement. Instead, it is an instruction to the C compiler itself.

One last point: With few exceptions, C ignores spaces. That is, it doesn't care where on a line a statement, curly brace, or function name occurs. If you like, you can even put two or more of these items on the same line. The examples you will see in this book reflect the way C code is normally written; it is a form you should follow. The actual positioning of statements, functions, and braces is a stylistic, not a programming, decision.

### EXAMPLES

1. Since all C programs share certain common traits, understanding one program will help you understand many others. One of the simplest C programs is shown here:

```c
#include <stdio.h>

int main(void)
{
    printf("This is a short C program.");

    return 0;
}
```

When compiled and executed, this program displays the message **This is a short C program.** on the screen of your computer.

Even though this program is only six lines long, it illustrates those aspects common to all C programs. Let's examine it line by line.

The first line of the program is
```c
#include <stdio.h>
```
It causes the file STDIO.H to be read by the C compiler and to be included with the program. This file contains information related to `printf()`.

The second line,
```c
int main(void)
```
begins the `main()` function. As stated earlier, all C programs must have a `main()` function. This is where program execution begins. The `int` specifies that `main()` returns an integer value. The `void` tells the compiler that `main()` does not have any parameters.

After `main()` is an opening curly brace. This marks the beginning of statements that make up the function.

The next line in the program is
```c
printf("This is a short C program.");
```
This is a C statement. It calls the standard library function, `printf()`, which causes the string to be displayed.

The following line causes `main()` to return the value zero. In this case, the value is returned to the calling process, which is usually the operating system.
```c
return 0;
```
By convention, a return value of zero from `main()` indicates normal program termination. Any other value represents an error. The operating system can test this value to determine whether the program ran successfully or experienced an error. `return` is one of C's keywords and is examined more closely later in this chapter.

Finally, the program is formally concluded when `main()`'s closing curly brace is encountered.

2. Here is another simple C program:

```c
#include <stdio.h>

int main(void)
{
    printf("This is ");
    printf("another C ");
    printf("program.");

    return 0;
}
```

This program displays **This is another C program.** on the screen. The key point to this program is that statements are executed sequentially, beginning with the opening curly brace and ending with the closing curly brace.

---

## 1.2 CREATE AND COMPILE A PROGRAM

How you will create and compile a program is determined to a very large extent by the compiler you are using and the operating system under which it is running. If you are using a PC or compatible, you have your choice of a number of excellent compilers, such as those by Borland and Microsoft, that contain integrated program-development environments. If you are using such an environment, you can edit, compile, and run your programs directly inside this environment. This is an excellent option for beginners—just follow the instructions supplied with your compiler.

If you are using a traditional command-line compiler, then you need to follow these steps to create and compile a program:

1. Create your program using an editor.
2. Compile the program.
3. Execute your program.

The exact method to accomplish these steps will be explained in the user's manual for your compiler.

### EXERCISES

1. Enter into your computer the example programs from Section 1.1. Compile them and run them.

---

## 1.3 DECLARE VARIABLES AND ASSIGN VALUES

A *variable* is a named memory location that can hold various values. Only the most trivial C programs do not include variables. In C, unlike some computer languages, all variables must be declared before they can be used. A variable's declaration serves one important purpose: It tells the compiler *what type of variable* is being used. C supports five different basic data types, as shown in Table 1-1 along with the C keywords that represent them. Don't be confused by `void`. This is a special-purpose data type that we will later examine closely.

A variable of type `char` is 8 bits long and is most commonly used to hold a single character. Because C is very flexible, a variable of type `char` can also be used as a "little integer" if desired.

Integer variables (`int`) may hold signed whole numbers (numbers with no fractional part). For 16-bit environments, such as DOS or Windows 3.1, integers are usually 16 bits long and may hold values in the range -32,768 to 32,767. In 32-bit environments, such as Windows NT or Windows 95, integers are typically 32 bits in length. In this case, they may store values in the range -2,147,483,648 to 2,147,483,647.

#### TABLE 1-1: C's Five Basic Data Types

| Type | Keyword |
| :--- | :--- |
| character data | `char` |
| signed whole numbers | `int` |
| floating-point numbers | `float` |
| double-precision floating-point numbers | `double` |
| valueless | `void` |

Variables of types `float` and `double` hold signed floating-point values, which may have fractional components. One difference between `float` and `double` is that `double` provides about twice the precision (number of significant digits) as does `float`. Also, for most uses of C, a variable of type `double` is capable of storing values with absolute magnitudes larger than those stored by variables of type `float`. Of course, in all cases, variables of types `float` and `double` can hold very large values.

To declare a variable, use this general form:

```c
type var-name;
```

where *type* is a C data type and *var-name* is the name of the variable. For example, this declares `counter` to be of type `int`:

```c
int counter;
```

In C, a variable declaration is a statement and it must end in a semicolon.

There are two places where variables are declared: inside a function or outside all functions. Variables declared outside all functions are called *global variables* and they may be accessed by any function in your program. Global variables exist the entire time your program is executing.

Variables declared inside a function are called *local variables*. A local variable is known to—and may be accessed by—only the function in which it is declared. It is common practice to declare all local variables used by a function at the start of the function, after the opening curly brace. There are two important points you need to know about local variables at this time. First, the local variables in one function have no relationship to the local variables in another function. That is, if a variable called `count` is declared in one function, another variable called `count` may also be declared in a second function—the two variables are completely separate from and unrelated to each other. The second thing you need to know is that local variables are created when a function is called, and they are destroyed when the function is exited. Therefore, local variables do not maintain their values between function calls. The examples in this and the next few chapters will use only local variables. Chapter 4 discusses more thoroughly the issues and implications of global and local variables.

You can declare more than one variable of the same type by using a comma-separated list. For example, this declares three floating-point variables, `x`, `y`, and `z`:

```c
float x, y, z;
```

Like function names, variable names in C can consist of the letters of the alphabet, the digits 0 through 9, and the underscore. (But a digit may not start a variable's name.) Remember, C is case-sensitive; `count` and `COUNT` are two completely different variable names.

To assign a value to a variable, put its name to the left of an equal sign. Put the value you want to give the variable to the right of the equal sign. In C, an assignment operation is a statement; therefore, it must be terminated by a semicolon. The general form of an assignment statement is:

```c
variable-name = value;
```

For example, to assign an integer variable named `num` the value 100, you can use this statement:

```c
num = 100;
```

In the preceding assignment, 100 is a *constant*. Just as there are different types of variables, there are different types of constants. A constant is a fixed value used in your program. Constants are often used to initialize variables at the beginning of a program's execution.

A character constant is specified by placing the character between single quotes. For example, to specify the letter 'A', you would use `'A'`. Integers are specified as whole numbers. Floating-point values must include a decimal point. For example, to specify 100.1, you would use `100.1`. If the floating-point value you wish to specify does not have any digits to the right of the decimal point, then you must use 0. For example, to tell the compiler that 100 is a floating-point number, use `100.0`.

You can use `printf()` to display values of characters, integers, and floating-point values. To do so, however, requires that you know more about the `printf()` function. Let's look first at an example. This statement

```c
printf("This prints the number %d", 99);
```

displays **This prints the number 99** on the screen. As you can see, this call to `printf()` contains not one, but two arguments. The first is the quoted string and the other is the constant 99. Notice that the arguments are separated from each other by a comma. In general, when there is more than one argument to a function, the arguments are separated from each other by commas. The operation of the `printf()` function is as follows. The first argument is a quoted string that may contain either normal characters or *format specifiers* that begin with the percent sign. Normal characters are simply displayed as-is on the screen in the order in which they are encountered in the string (reading left to right). A format specifier, also called a *format code*, informs `printf()` that a different type item is to be displayed. In this case, the `%d` means that an integer is to be output in decimal format. The value to be displayed is found in the second argument. This value is then output to the screen at the point where the format specifier is found in the string. To understand the relationship between the normal characters and the format codes, examine this statement:

```c
printf("This displays %d, too", 99);
```

Now the call to `printf()` displays **This displays 99, too**. The key point is that the value associated with a format code is displayed at the point where that format code is encountered in the string.

If you want to specify a character value, the format specifier is `%c`. To specify a floating-point value, use `%f`. The `%f` works for both `float` and `double`. As you will see, `printf()` has many more capabilities.

Keep in mind that the values matched with the format specifier need not be constants; they may be variables, too.

### EXAMPLES

1. The program shown here illustrates the three new concepts introduced in this section. First, it declares a variable named `num`. Second, it assigns this variable the value 100. Finally, it uses `printf()` to display **The value is 100** on the screen. Examine this program closely:

```c
#include <stdio.h>

int main(void)
{
    int num;

    num = 100;
    printf("The value is %d", num);

    return 0;
}
```

The statement
```c
int num;
```
declares `num` to be an integer variable.
To display the value of `num`, the program uses this statement:
```c
printf("The value is %d", num);
```

2. This program creates variables of types `char`, `float`, and `double`; assigns each a value; and outputs these values to the screen.

```c
#include <stdio.h>

int main(void)
{
    char ch;
    float f;
    double d;

    ch = 'X';
    f = 100.123;
    d = 123.009;

    printf("ch is %c, ", ch);
    printf("f is %f, ", f);
    printf("d is %f", d);

    return 0;
}
```

### EXERCISES

1. Enter, compile, and run the example programs in this section.
2. Write a program that declares one integer variable called `num`. Give this variable the value 1000 and then, using one `printf()` statement, display the value on the screen like this:
```
1000 is the value of num
```

---

## 1.4 INPUT NUMBERS FROM THE KEYBOARD

Although there are actually several ways to input numeric values from the keyboard, one of the easiest is to use another of C's standard library functions called `scanf()`. Although it possesses considerable versatility, we will use it in this chapter to read only integers and floating-point numbers entered from the keyboard.

To use `scanf()` to read an integer value from the keyboard, call it using the general form
```c
scanf("%d", &int-var-name);
```
where *int-var-name* is the name of the integer variable you wish to receive the value. The first argument to `scanf()` is a string that determines how the second argument will be treated. In this case, the `%d` specifies that the second argument will be receiving an integer value entered in decimal format. This fragment, for example, reads an integer entered from the keyboard.

```c
int num;
scanf("%d", &num);
```

The `&` preceding the variable name is essential to the operation of `scanf()`. Although a detailed explanation will have to wait until later, loosely, the `&` allows a function to place a value into one of its arguments.

It is important to understand one key point: When you enter a number at the keyboard, you are simply typing a string of digits. The `scanf()` function waits until you have pressed ENTER before it converts the string into the internal binary format used by the computer.

To read a floating-point number from the keyboard, call `scanf()` using the general form
```c
scanf("%f", &float-var-name);
```
where *float-var-name* is the name of a variable that is declared as being of type `float`. If you want to input to a `double` variable, use the `%lf` specifier.

Notice that the format specifiers for `scanf()` are similar to those used for `printf()` for the corresponding data types except that `%lf` is used to read a double. This is no coincidence—`printf()` and `scanf()` are complementary functions.

### EXAMPLES

1. This program asks you to input an integer and a floating-point number. It then displays the values you enter.

```c
#include <stdio.h>

int main(void)
{
    int num;
    float f;

    printf("Enter an integer: ");
    scanf("%d", &num);

    printf("Enter a floating point number: ");
    scanf("%f", &f);

    printf("%d ", num);
    printf("%f", f);

    return 0;
}
```

### EXERCISES

1. Enter, compile, and run the example program.
2. Write a program that inputs two floating-point numbers (use type `float`) and then displays their sum.

---

## 1.5 PERFORM CALCULATIONS USING ARITHMETIC EXPRESSIONS

In C, the expression plays a much more important role than it does in most other programming languages. Part of the reason for this is that C defines many more operators than do most other languages. An *expression* is a combination of operators and operands. C expressions follow the rules of algebra, so, for the most part, they will be familiar. In this section we will look only at arithmetic expressions.

C defines these five arithmetic operators:

| Operator | Meaning |
| :--- | :--- |
| `+` | addition |
| `-` | subtraction |
| `*` | multiplication |
| `/` | division |
| `%` | modulus |

The `+`, `-`, `/`, and `*` operators may be used with any of the basic data types. However, the `%` may be used with integer types only. The modulus operator produces the remainder of an integer division. This has no meaning when applied to floating-point types.

The `-` has two meanings. First, it is the subtraction operator. Second, it can be used as a unary minus to reverse the sign of a number. A unary operator uses only one operand.

An expression may appear on the right side of an assignment statement. For example, this program fragment assigns the integer variable `answer` the value of 100*31.

```c
int answer;
answer = 100 * 31;
```

The `*`, `/`, and `%` are higher in precedence than the `+` and the `-`. However, you can use parentheses to alter the order of evaluation. For example, this expression produces the value zero,

```c
10 - 2 * 5
```

but this one produces the value 40.

```c
(10 - 2) * 5
```

A C expression may contain variables, constants, or both. For example, assuming that `answer` and `count` are variables, this expression is perfectly valid:

```c
answer = count - 100;
```

Finally, you may use spaces liberally within an expression.

### EXAMPLES

1. As stated earlier, the modulus operator returns the remainder of an integer division. The remainder of 10 % 3 equals 1, for example. This program shows the outcome of some integer divisions and their remainders:

```c
#include <stdio.h>

int main(void)
{
    printf("%d ", 5/2);
    printf("%d ", 5%2);
    printf("%d ", 4/2);
    printf("%d", 4%2);

    return 0;
}
```

This program displays **2 1 2 0** on the screen.

2. In long expressions, the use of parentheses and spaces can add clarity, even if they are not necessary. For example, examine this expression:

```c
count *num+88/val-19%count
```

This expression produces the same result, but is much easier to read:

```c
(count * num) + (88 / val) - (19 % count)
```

3. This program computes the area of a rectangle, given its dimensions. It first prompts the user for the length and width of the rectangle and then displays the area.

```c
#include <stdio.h>

int main(void)
{
    int len, width;

    printf("Enter length: ");
    scanf("%d", &len);
    printf("Enter width: ");
    scanf("%d", &width);

    printf("Area is %d", len * width);

    return 0;
}
```

4. As stated earlier, the `-` can be used as a unary operator to reverse the sign of its operand. To see how this works, try this program:

```c
#include <stdio.h>

int main(void)
{
    int i;

    i = 10;
    i = -i;
    printf("This is i: %d", i);

    return 0;
}
```

---

## 1.6 ADD COMMENTS TO A PROGRAM

A *comment* is a note to yourself (or others) that you put into your source code. All comments are ignored by the compiler. They exist solely for your benefit.

In C, a comment begins with `/*` and ends with `*/`. Anything between these two marking symbols is a comment. For example, this is a valid C comment:

```c
/* This is a C comment. */
```

Comments may span more than one line. For example, this is also valid:

```c
/*
   This is a multi-line
   C comment.
*/
```

Comments may be placed anywhere in a program, except within a keyword, function name, or variable name.

### EXAMPLES

1. Here is the Jovian-years calculation program with comments added:

```c
/* This program computes Jovian years. */
#include <stdio.h>

int main(void)
{
    float e_days; /* number of Earth days */
    float j_years; /* equivalent Jovian years */

    printf("Enter number of Earth days: ");
    scanf("%f", &e_days);

    /* now, compute Jovian years */
    j_years = e_days / (365.0 * 12.0);

    /* display the answer */
    printf("Equivalent Jovian years: %f", j_years);

    return 0;
}
```

Notice that comments can appear on the same line as other C program statements.

Comments are often used to help describe what the program is doing. Although this program is easy to understand even without the comments, many programs are very difficult to understand even with the liberal use of comments. For more complex programs, the general approach is the same as used here: simply describe the actions of the program. Also, notice the comment at the start of the program. In general, it is a good idea to identify the purpose of a program at the top of its source file.

2. You cannot place a comment inside the name of a function or variable name. For example, this is an incorrect statement:

```c
pri/* wrong */ntf("this won't work");
```

### EXERCISES

1. Go back and add comments to the programs developed in previous sections.
2. Is this comment correct?
```c
/***/
```
3. Is this comment correct?
```c
/* printf("this is a test"); */
```

---

## 1.7 WRITE YOUR OWN FUNCTIONS

Functions are the building blocks of C. So far, the programs you have seen included only one function: `main()`. Most real-world programs, however, will contain many functions. In this section you will begin to learn how to write programs that contain multiple functions.

The general form of a C program that has multiple functions is shown here:

```c
/* include header files here */

/* function prototypes here */

int main(void)
{
    /* ... */
}

ret-type f1(param-list)
{
    /* ... */
}

ret-type f2(param-list)
{
    /* ... */
}
.
.
.
ret-type fN(param-list)
{
    /* ... */
}
```

Of course, you can call your functions by different names. Here, *ret-type* specifies the type of data returned by the function. If a function does not return a value, then its return type should be `void`. If a function does not use parameters, then its *param-list* should contain the keyword `void`.

Notice the comment about prototypes. A *function prototype* declares a function before it is used and prior to its definition. A prototype consists of a function's name, its return type, and its parameter list. It is terminated by a semicolon. The compiler needs to know this information in order for it to properly execute a call to the function. For example, given this simple function:

```c
void myfunc(void)
{
    printf("This is a test.");
}
```

Its prototype is

```c
void myfunc(void);
```

The only function that does not need a prototype is `main()` since it is predefined by the C language.

Prototypes are an important part of C programming, but you will need to learn more about C before you can fully understand their purpose and value. For the next few chapters we will be using prototypes without any further explanation. They will be included as needed in all of the example programs shown in this book. You should also include them in programs that you write. A full explanation of prototypes is found in Chapter 7.

When a function is called, execution transfers to that function. When the end of that function is reached, execution returns to a point immediately after the place at which the function was called. Put differently, when a function ends, execution resumes at the point in your program immediately following the call to the function. Any function inside a program may call any other function within the same program. Traditionally, `main()` is not called by any other function, but there is no technical restriction to this effect.

In the examples that follow, you will learn to create the simplest type of C functions: those that do not return values and do not use parameters. The skeletal form of such a function is shown here:

```c
void FuncName(void)
{
    /* body of function here */
}
```

Of course, the name of the function will vary. Because the function does not return a value, its return type is `void`. Because the function does not have parameters, its parameter list is `void`.

### EXAMPLES

1. The following program contains two functions: `main()` and `func1()`. Try to determine what it displays on the screen before reading the description that follows it.

```c
/* A program with two functions */

#include <stdio.h>

void func1(void); /* prototype for func1() */

int main(void)
{
    printf("I ");
    func1();
    printf("C.");

    return 0;
}

void func1(void)
{
    printf("like ");
}
```

This program displays **I like C.** on the screen. Here is how it works. In `main()`, the first call to `printf()` executes, printing the **I**. Next, `func1()` is called. This causes the `printf()` inside `func1()` to execute, displaying **like**. Since this is the only statement inside `func1()`, the function returns. This causes execution to resume inside `main()` and the **C.** is printed. Notice that the statement that calls `func1()` ends with a semicolon. (Remember a function call is a statement.)

A key point to understand about writing your own functions is that when the closing curly brace is reached the function will return, and execution resumes one line after the point at which the function was called.

Notice the prototype for `func1()`. As you can see, it consists of its name, return type, and parameters list, but no body. It is terminated by a semicolon.

2. This program prints **1 2 3** on the screen:

```c
/* This program has three functions. */

#include <stdio.h>

void func1(void); /* prototypes */
void func2(void);

int main(void)
{
    func2();
    printf("3");

    return 0;
}

void func2(void)
{
    func1();
    printf("2 ");
}

void func1(void)
{
    printf("1 ");
}
```

In this program, `main()` first calls `func2()`, which then calls `func1()`. Next, `func1()` displays **1** and then returns to `func2()`, which prints **2** and then returns to `main()`, which prints **3**.

### EXERCISES

1. Enter, compile, and run the two example programs in this section.
2. Write a program that contains at least two functions and prints the message **The summer soldier, the sunshine patriot.**
3. Remove the prototype from the first example program and then compile it. What happens?

---

## 1.8 USE FUNCTIONS TO RETURN VALUES

In C, a function may return a value to the calling routine. For example, another of C's standard library functions is `sqrt()`, which returns the square root of its argument. For your program to obtain the return value, you must put the function on the right side of an assignment statement. For example, this program prints the square root of 10:

```c
#include <stdio.h>
#include <math.h> /* needed by sqrt() */

int main(void)
{
    double answer;

    answer = sqrt(10.0);
    printf("%f", answer);

    return 0;
}
```

This program calls `sqrt()` and assigns its return value to `answer`. Notice that `sqrt()` uses the MATH.H header file.

Actually, the assignment statement in the preceding program is not technically necessary because `sqrt()` could simply be used as an argument to `printf()`, as shown here:

```c
#include <stdio.h>
#include <math.h> /* needed by sqrt() */

int main(void)
{
    printf("%f", sqrt(10.0));

    return 0;
}
```

The reason this works is that C will automatically call `sqrt()` and obtain its return value before calling `printf()`. The return value then becomes the second argument to `printf()`. If this seems strange, don't worry; you will understand this sort of situation better as you learn more about C.

The `sqrt()` function requires a floating-point value for its argument, and the value it returns is of type `double`. You must match the type of value a function returns with the variable that the value will be assigned to. As you learn more about C, you will see why this is important. It is also important that you match the types of a function's arguments to the types it requires.

When writing your own functions, you can return a value to the calling routine using the `return` statement. The `return` statement takes the general form

```c
return value;
```

where *value* is the value to be returned. For example, this program prints **10** on the screen:

```c
#include <stdio.h>

int func(void); /* prototype */

int main(void)
{
    int num;

    num = func();
    printf("%d", num);

    return 0;
}

int func(void)
{
    return 10;
}
```

In this example, `func()` returns an integer value and its return type is specified as `int`. Although you can create functions that return any type of data, functions that return values of type `int` are quite common. Later in this book, you will see many examples of functions that return other types. Functions that are declared as `void` may not return values.

If a function does not explicitly specify a return type, it is assumed to return an integer by default. For example, `func()` could have been coded like this:

```c
func(void)
{
    return 10;
}
```

In this case, the `int` is implied. The use of the "default to int" rule is very common in older C code. However, recently there has been a move away from using the integer default. Whether this trend will continue is unknown. In any event, to avoid misunderstandings, this book will always explicitly specify `int`.

One important point: When the `return` statement is encountered, the function returns immediately. No statements after it will be executed. Thus, a `return` statement causes a function to return before its closing curly brace is reached.

The value associated with the `return` statement need not be a constant. It can be any valid C expression.

A `return` statement can also be used by itself, without a return value. This form of `return` looks like this:

```c
return ;
```

It is used mostly by `void` functions (i.e., functions that have a `void` return type) to cause the function to return immediately, before the function's closing curly brace is reached. While not recommended, you can also use this form of `return` in functions that are supposed to return values. However, doing so makes the returned value undefined.

There can be more than one `return` in a function. You will see examples of this later in this book.

Even though a function returns a value, you don't necessarily have to assign that value to anything. If the return value of a function is not used, it is lost, but no harm is done.

### EXAMPLES

1. This program displays the square of a number entered from the keyboard. The square is computed using the `get_sqr()` function. Its operation should be clear.

```c
#include <stdio.h>

int get_sqr(void);

int main(void)
{
    int sqr;

    sqr = get_sqr();
    printf("Square: %d", sqr);

    return 0;
}

int get_sqr(void)
{
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);
    return num*num; /* square the number */
}
```

2. As mentioned earlier, you can use `return` without specifying a value. This allows a function to return before its closing curly brace is reached. For example, in the following program, the line **This is never printed.** will not be displayed.

```c
#include <stdio.h>

void func1(void);

int main(void)
{
    func1();

    return 0;
}

void func1(void)
{
    printf("This is printed.");
    return; /* return with no value */
    printf("This is never printed.");
}
```

### EXERCISES

1. Enter, compile, and run the example programs in this section.
2. Write a program that uses a function called `convert()`, which prompts the user for an amount in dollars and returns this value converted into pounds. (Use an exchange rate of $2.00 per pound.) Display the conversion.
3. What is wrong with this program?

```c
#include <stdio.h>

int f1(void);

int main(void)
{
    double answer;

    answer = f1();
    printf("%f", answer);

    return 0;
}

int f1(void)
{
    return 100;
}
```

4. What is wrong with this function?

```c
void func(void)
{
    int i;

    printf("Enter a number: ");
    scanf("%d", &i);

    return i;
}
```

---

## 1.9 USE FUNCTION ARGUMENTS

As stated earlier, a function's *argument* is a value that is passed to the function when the function is called. A function in C can have from zero to several arguments. (The upper limit is determined by the compiler you are using, but the ANSI C standard specifies that a function must be able to take at least 31 arguments.) For a function to be able to take arguments, special variables to receive argument values must be declared. These are called the *formal parameters* of the function. The parameters are declared between the parentheses that follow the function's name. For example, the function listed below prints the sum of the two integer arguments used to call it.

```c
void sum(int x, int y)
{
    printf("%d ", x + y);
}
```

Each time `sum()` is called, it will sum the value passed to `x` with the value passed to `y`. Remember, however, that `x` and `y` are simply the function's operational variables, which receive the values you use when calling the function. Consider the following short program, which illustrates how to call `sum()`.

```c
/* A simple program that demonstrates sum(). */

#include <stdio.h>

void sum(int x, int y);

int main(void)
{
    sum(1, 20);
    sum(9, 6);
    sum(81, 9);

    return 0;
}

void sum(int x, int y)
{
    printf("%d ", x + y);
}
```

This program will print **21, 15, and 90** on the screen. When `sum()` is called, the value of each argument is copied into its matching parameter. That is, in the first call to `sum()`, 1 is copied into `x` and 20 is copied into `y`. In the second call, 9 is copied into `x` and 6 into `y`. In the third call, 81 is copied into `x` and 9 into `y`.

If you have never worked with a language that allows parameterized functions, the preceding process may seem strange. Don't worry—as you see more examples of C programs, the concept of arguments, parameters, and functions will become clear.

It is important to keep two terms straight. First, *argument* refers to the value that is passed to a function. The variable that receives the value of the argument inside the function is the *formal parameter* of the function. Functions that take arguments are called *parameterized functions*. Remember, if a variable is used as an argument to a function, it has nothing to do with the formal parameter that receives its value.

In C functions, arguments are always separated by commas. In this book, the term *argument list* will refer to comma-separated arguments.

All function parameters are declared in a fashion similar to that used by `sum()`. You must specify the type and name of each parameter and, if there is more than one parameter, you must use a comma to separate them. Functions that do not have parameters should use the keyword `void` in their parameter list.

### EXAMPLES

1. An argument to a function can consist of an expression. For example, it is perfectly valid to call `sum()` as shown here:

```c
sum(10-2, 9*7);
```

2. This program uses the `putchar()` function to output characters to the screen. The program prints **ABC**.

```c
#include <stdio.h>

void outchar(char ch);

int main(void)
{
    outchar('A');
    outchar('B');
    outchar('C');

    return 0;
}

void outchar(char ch)
{
    printf("%c", ch);
}
```

### EXERCISES

1. Write a program that uses a function called `outnum()` that takes one integer argument and displays it on the screen.
2. What is wrong with this program?

```c
#include <stdio.h>

void sqr_it(int num);

int main(void)
{
    sqr_it(10.0);

    return 0;
}

void sqr_it(int num)
{
    printf("%d", num * num);
}
```

---

## 1.10 REMEMBER THE C KEYWORDS

Before concluding this chapter, you should familiarize yourself with the keywords that make up the C language. ANSI C standard has 32 *keywords* that may not be used as variable or function names. These words, combined with the formal C syntax, form the C programming language. They are listed in Table 1-2.

Many C compilers have added several additional keywords that are used to take better advantage of the environment in which the compiler is used, and that give support for interlanguage programming, interrupts, and memory organization. Some commonly used extended keywords are shown in Table 1-3.

The lowercase lettering of the keywords is significant. C requires that all keywords be in lowercase form. For example, **RETURN** will *not* be recognized as the keyword `return`. Also, no keyword may be used as a variable or function name.

#### TABLE 1-2: The 32 Keywords as Defined by the ANSI C Standard

| | | | |
| :--- | :--- | :--- | :--- |
| `auto` | `double` | `int` | `struct` |
| `break` | `else` | `long` | `switch` |
| `case` | `enum` | `register` | `typedef` |
| `char` | `extern` | `return` | `union` |
| `const` | `float` | `short` | `unsigned` |
| `continue` | `for` | `signed` | `void` |
| `default` | `goto` | `sizeof` | `volatile` |
| `do` | `if` | `static` | `while` |

#### TABLE 1-3: Some Common C Extended Keywords

| | | | |
| :--- | :--- | :--- | :--- |
| `asm` | `_cs` | `_ds` | `_es` |
| `_ss` | `cdecl` | `far` | `huge` |
| `interrupt` | `near` | `pascal` | |

---

## Mastery Skills Check

At this point you should be able to answer these questions and perform these exercises:

1. The moon's gravity is about 17 percent of Earth's. Write a program that allows you to enter your weight and computes your effective weight on the moon.
2. What is wrong with this program fragment?
```c
/* this inputs a number
scanf("%d", &num);
```
3. There are 8 ounces in a cup. Write a program that converts ounces to cups. Use a function called `o_to_c()` to perform the conversion. Call it with the number of ounces and have it return the number of cups.
4. What are the five basic data types in C?
5. What is wrong with each of these variable names?
   a) `short-fall`  
   b) `$balance`  
   c) `last + name`  
   d) `9times`  
