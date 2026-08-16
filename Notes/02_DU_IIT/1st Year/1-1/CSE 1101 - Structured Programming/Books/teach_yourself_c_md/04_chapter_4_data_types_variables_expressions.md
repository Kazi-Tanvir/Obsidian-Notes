# 4 A Closer Look at Data Types, Variables, and Expressions

THIS chapter more fully examines several concepts presented in Chapter 1. It covers C's data-type modifiers, global and local variables, and constants. It also discusses how C handles various type conversions.

---

### Review Skills Check

Before proceeding, you should be able to answer these questions and perform these exercises:

1. Using C's three loop statements, show three ways to write a loop that counts from 1 to 10.
2. Convert this series of `if`s into an equivalent `switch`:
```c
if(ch=='L') load();
else if(ch=='S') save();
else if(ch=='E') enter();
else if(ch=='D') display();
else if(ch=='Q') quit();
```
3. Write a program that inputs characters until the user strikes the ENTER key.
4. What does `break` do?
5. What does `continue` do?
6. Write a program that displays this menu, performs the selected operation, and then repeats until the user selects **Quit**.

```
Convert
1. feet to meters
2. meters to feet
3. ounces to pounds
4. pounds to ounces
5. Quit
Enter the number of your choice:
```

---

## 4.1 USE C'S DATA-TYPE MODIFIERS

In Chapter 1 you learned that C has five basic data types: `void`, `char`, `int`, `float`, and `double`. These basic types, except type `void`, can be modified using C's *type modifiers* to more precisely fit your specific need. The type modifiers are:

- `long`
- `short`
- `signed`
- `unsigned`

The type modifier precedes the type name. For example, this declares a long integer:

```c
long int i;
```

The effect of each modifier is examined next.

The `long` and `short` modifiers may be applied to `int`. As a general rule, `short int`s are often smaller than `int`s and `long int`s are often larger than `int`s. For example, in most 16-bit environments, an `int` is 16 bits long and a `long int` is 32 bits in length. However, the precise meaning of `long` and `short` is implementation dependent. When the ANSI C standard was created, it specified *minimum* ranges for integers, short integers, and long integers. It did not set fixed sizes for these items. (See Table 4-1.) For example, using the minimum ranges set forth in the ANSI C standard, the smallest acceptable size for an `int` is 16 bits and the smallest acceptable size for a `short int` is also 16 bits. Thus, it is permissible for integers and short integers to be the same size! In fact, in most 16-bit environments, there is no difference between an `int` and a `short int`. Further, in many 32-bit environments, you will find that integers and long integers are the same size. Since the exact effect of `long` and `short` on integers is determined by the environment in which you are working and by the compiler you are using, you will need to check your compiler's documentation for their precise effects.

The `long` modifier may also be applied to `double`. Doing so roughly doubles the precision of a floating point variable.

The `signed` modifier is used to specify a signed integer value. (A signed number means that it can be positive or negative.) However, the use of `signed` on integers is redundant because the default integer declaration automatically creates a signed variable. The main use of the `signed` modifier is with `char`. Whether `char` is signed or unsigned by itself is implementation dependent. In some implementations `char` is unsigned by default; in others, it is signed. To ensure a signed character variable in all environments, you must declare it as `signed char`. Since most compilers implement `char` as signed, this book simply assumes that characters are *signed* and will not use the `signed` modifier.

The `unsigned` modifier can be applied to `char` and `int`. It may also be used in combination with `long` or `short`. It is used to create an unsigned integer. The difference between signed and unsigned integers is in the way the high-order bit of the integer is interpreted. If a signed integer is specified, then the C compiler will generate code that assumes the high-order bit is used as a sign flag. If the sign flag is 0, the number is positive; if it is 1, the number is negative. Negative numbers are generally represented using the *two's complement* approach. In this method, all bits in the number (except the sign flag) are reversed, and 1 is added to this number. Finally, the sign flag is set to 1. (The reason for this method of representation is that it makes it easier for the CPU to perform arithmetic operations on negative values.)

Signed integers are important for a great many algorithms, but they only have half the absolute magnitude of their unsigned relatives. For example, here is 32,767 shown in binary:

```
01111111 11111111
```

If this is a signed value and the high-order bit is set to 1, the number would then be interpreted as -1 (assuming two's complement format). However, if this is an unsigned value, then when the high-order bit is set to 1, the number becomes 65,535.

Table 4-1 shows all allowed combinations of the basic types and the type modifiers. The table also shows the most common size and minimum range for each type as specified by the ANSI C standard.

It is important to understand that the ranges shown in Table 4-1 are just the minimums that all compilers must provide. The compiler is free to exceed them, and most compilers do for at least some data types. As mentioned, an `int` in a 32-bit environment will usually have a range larger than the minimum. Also, in environments that use two's complement arithmetic (which is the case for the vast majority of computers), the lower bound for signed characters and integers is one greater than the minimums shown. For instance, in most environments, a `signed char` has a range of -128 to 127 and a `short int` is typically -32,768 to 32,767. You will need to check your compiler's documentation for the specific ranges of the data types as they apply to your compiler.

#### TABLE 4-1: All Data Types Defined by the ANSI C Standard

| Type | Typical Size in Bits | Minimal Range |
| :--- | :--- | :--- |
| `char` | 8 | -127 to 127 |
| `unsigned char` | 8 | 0 to 255 |
| `signed char` | 8 | -127 to 127 |
| `int` | 16 or 32 | -32,767 to 32,767 |
| `unsigned int` | 16 or 32 | 0 to 65,535 |
| `signed int` | 16 or 32 | same as int |
| `short int` | 16 | same as int |
| `unsigned short int` | 16 | 0 to 65,535 |
| `signed short int` | 16 | same as short int |
| `long int` | 32 | -2,147,483,647 to 2,147,483,647 |
| `signed long int` | 32 | same as long int |
| `unsigned long int` | 32 | 0 to 4,294,967,295 |
| `float` | 32 | Six digits of precision |
| `double` | 64 | Ten digits of precision |
| `long double` | 80 | Ten digits of precision |

C allows a shorthand notation for declaring `unsigned`, `short`, or `long` integers. You may simply use the word **unsigned**, **short**, or **long** without the `int`. The `int` is implied. For example,

```c
unsigned count;
unsigned int num;
```

both declare unsigned `int` variables.

It is important to remember that variables of type `char` may be used to hold values other than just the ASCII character set. C makes little distinction between a character and an integer, except for the magnitudes of the values each may hold. Therefore, as mentioned earlier, a signed `char` variable can also be used as a "small" integer when the situation does not require larger numbers.

When outputting integers modified by `short`, `long`, or `unsigned` using `printf()`, you cannot simply use the `%d` specifier. The reason is that `printf()` needs to know precisely what type of data it is receiving. To use `printf()` to output a `short`, use `%hd`. To output a `long`, use `%ld`. When outputting an `unsigned` value, use `%u`. To output an `unsigned long int`, use `%lu`. Also, to output a `long double` use `%Lf`.

The `scanf()` function operates in a fashion similar to `printf()`. When reading a `short int` using `scanf()`, use `%hd`. When reading a `long int`, use `%ld`. To read an `unsigned long int`, use `%lu`. To read a `double`, use `%lf`. To read a `long double`, use `%Lf`.

### EXAMPLES

1. This program shows how to input and output short, long, and unsigned values.

```c
#include <stdio.h>

int main(void)
{
    unsigned u;
    long l;
    short s;

    printf("Enter an unsigned: ");
    scanf("%u", &u);
    printf("Enter a long: ");
    scanf("%ld", &l);
    printf("Enter a short: ");
    scanf("%hd", &s);

    printf("%u %ld %hd\n", u, l, s);

    return 0;
}
```

2. To understand the difference between the way that signed and unsigned integers are interpreted by C, run the following short program. (This program assumes that short integers are 16 bits wide.)

```c
#include <stdio.h>

int main(void)
{
    short int i; /* a signed short integer */
    unsigned short int u; /* an unsigned short integer */

    u = 33000;
    i = u;
    printf("%hd %hu", i, u);

    return 0;
}
```

When this program is run, the output is `-32536 33000`. The reason for this is that the bit pattern that 33000 represents as an unsigned short int is interpreted as -32536 as a signed short int.

3. In C, you may use a `char` variable any place you would use an `int` variable (assuming the differences in their ranges is not a factor). For example, the following program uses a `char` variable to control the loop that is summing the numbers between 1 and 100. In some cases it takes the computer less time to access a single byte (one character) than it does to access two bytes. Therefore, many professional programmers use a character variable rather than an integer one when the range permits.

```c
#include <stdio.h>

int main(void)
{
    int i;
    char j;

    i = 0;
    for(j=1; j<101; j++) i = j + i;

    printf("Total is: %d", i);

    return 0;
}
```

### EXERCISES

1. Show how to declare an unsigned short int called `loc_counter`.
2. Write a program that prompts the user for a distance and computes how long it takes light to travel that distance. Use an unsigned long int to hold the distance. (Light travels at approximately 186,000 miles per second.)
3. Write this statement another way:
```c
short int i;
```

---

## 4.2 LEARN WHERE VARIABLES ARE DECLARED

As you learned in Chapter 1, there are two basic places where a variable will be declared: inside a function and outside all functions. These variables are called *local variables* and *global variables*, respectively. It is now time to take a closer look at these two types of variables and the *scope* rules that govern them.

Local variables (declared inside a function) may be referenced only by statements that are inside that function. They are not known outside their own function. One of the most important things to understand about local variables is that they exist only while the function in which they are declared is executing. That is, a local variable is created upon entry into its function and destroyed upon exit.

Since local variables are not known outside their own function, it is perfectly acceptable for local variables in different functions to have the same name. Consider the following program:

```c
#include <stdio.h>

void f1(void), f2(void);

int main(void)
{
    f1();

    return 0;
}

void f1(void)
{
    int count;

    for(count=0; count<10; count++) f2();
}

void f2(void)
{
    int count;

    for(count=0; count<10; count++) printf("%d ", count);
}
```

This program prints the numbers 0 through 9 on the screen ten times. The fact that both functions use a variable called `count` has no effect upon the operation of the code. Therefore, what happens to `count` inside `f2()` has no effect on `count` in `f1()`.

The C language contains the keyword `auto`, which can be used to declare local variables. However, since all local variables are, by default, assumed to be `auto`, it is virtually never used. Hence, you will not see it in any of the examples in this book.

Within a function, local variables can be declared at the start of any block. They do not need to be declared only at the start of the block that defines the function. For example, the following program is perfectly valid:

```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=0; i<10; i++) {
        if(i==5) {
            int j; /* declare j within the if block */

            j = i * 10;
            printf("%d", j);
        }
    }

    return 0;
}
```

A variable declared within a block is known only to other code within that block. Thus, `j` may not be used outside of its block. Frankly, most C programmers declare all variables used by a function at the start of the function's block because it is simply more convenient to do so. This is the approach that will be used in this book.

Remember one important point: You must declare all local variables at the start of the block in which they are defined, prior to any program statements. For example, the following is incorrect:

```c
#include <stdio.h>

int main(void)
{
    printf("This program won't compile.");
    int i; /* this should come first */
    i = 10;
    printf("%d", i);

    return 0;
}
```

When a function is called, its local variables are created, and upon its return, they are destroyed. This means that local variables cannot retain their values between calls.

The formal parameters to a function are also local variables. Even though these variables perform the special task of receiving the value of the arguments passed to the function, they can be used like any other local variable within that function.

Unlike local variables, global variables are known throughout the entire program and may be used by any piece of code in the program. Also, they will hold their value during the entire execution of the program. Global variables are created by declaring them outside any function. For example, consider this program:

```c
#include <stdio.h>

void f1(void);

int max; /* this is a global variable */

int main(void)
{
    max = 10;
    f1();

    return 0;
}

void f1(void)
{
    int i;

    for(i=0; i<max; i++) printf("%d ", i);
}
```

Here, both `main()` and `f1()` use the global variable `max`. The `main()` function sets the value of `max` to 10, and `f1()` uses this value to control its `for` loop.

### EXAMPLES

1. In C, a local variable and a global variable may have the same name. For example, this is a valid program:

```c
#include <stdio.h>

void f1(void);

int count; /* global count */

int main(void)
{
    count = 10;
    f1();
    printf("count in main(): %d\n", count);

    return 0;
}

void f1(void)
{
    int count; /* local count */

    count = 100;
    printf("count in f1() : %d\n", count);
}
```

The program displays this output:

```
count in f1() : 100
count in main(): 10
```

In `main()`, the reference to `count` is to the global variable. Inside `f1()`, a local variable called `count` is also defined. When the assignment statement inside `f1()` is encountered, the compiler first looks to see if there is a local variable called `count`. Since there is, the local variable is used, not the global one with the same name. That is, when local and global variables share the same name, the compiler will always use the local variable.

2. Global variables are very helpful when the same data is used by many functions in your program. However, you should always use local variables where you can because the excessive use of global variables has some negative consequences. First, global variables use memory the entire time your program is executing, not just when they are needed. In situations where memory is in short supply, this could be a problem. Second, using a global where a local variable will do makes a function less general, because it relies on something that must be defined outside itself. For example, here is a case where global variables are being used for no reason:

```c
#include <stdio.h>

int power(void);

int m, e;

int main(void)
{
    m = 2;
    e = 3;

    printf("%d raised to the %d power is %d", m, e, power());

    return 0;
}

/* Non-general version of power. */
int power(void)
{
    int temp, temp2;

    temp = 1;
    temp2 = e;
    for( ; temp2 > 0; temp2--) temp = temp * m;

    return temp;
}
```

Here, the function `power()` is created to compute the value of **m** raised to the **e**th power. Since `m` and `e` are global, the function cannot be used to compute the power of other values. It can only operate on those contained within `m` and `e`. However, if the program is rewritten as follows, `power()` can be used with any two values.

```c
#include <stdio.h>

int power(int m, int e);

int main(void)
{
    int m, e;
    m = 2;
    e = 3;

    printf("%d to the %d is %d\n", m, e, power(m, e));
    printf("4 to the 5th is %d\n", power(4, 5));
    printf("3 to the 3rd is %d\n", power(3, 3));

    return 0;
}

/* Parameterized version of power. */
int power(int m, int e)
{
    int temp;

    temp = 1;
    for( ; e> 0; e--) temp = temp * m;

    return temp;
}
```

By parameterizing `power()`, you can use it to return the result of any value raised to some power, as the program now shows.

The important point is that in the non-generalized version, any program that uses `power()` must always declare `m` and `e` as global variables and then load them with the desired values each time `power()` is used. In the parameterized form, the function is complete within itself—no extra baggage need be carried about when it is used.

Finally, using a large number of global variables can lead to program errors because of unknown and unwanted side effects. A major problem in developing large programs is the accidental modification of a variable's value because it was used elsewhere in the program. This can happen in C if you use too many global variables in your programs.

3. Remember, local variables do not maintain their values between functions calls. For example, the following program will not work correctly:

```c
#include <stdio.h>

int series(void);

int main(void)
{
    int i;

    for(i=0; i<10; i++) printf("%d ", series());

    return 0;
}

/* This is incorrect. */
int series(void)
{
    int total;

    total = (total + 1423) % 1422;
    return total;
}
```

This program attempts to use `series()` to generate a number series in which each number is based upon the value of the preceding one. However, the value `total` will not be maintained between function calls, and the function fails to carry out its intended task.

### EXERCISES

1. What are key differences between local and global variables?
2. Write a program that contains a function called `soundspeed()`, which computes the number of seconds it will take sound to travel a specified distance. Write the program two ways: first, with `soundspeed()` as a non-general function and second, with `soundspeed()` parameterized. (For the speed of sound, use 1129 feet per second).

---

## 4.3 TAKE A CLOSER LOOK AT CONSTANTS

Constants refer to fixed values that may not be altered by the program. For example, the number 100 is a constant. We have been using constants in the preceding sample programs without much fanfare because, in most cases, their use is intuitive. However, the time has come to cover them formally.

Integer constants are specified as numbers without fractional components. For example, 10 and -100 are integer constants. Floating-point constants require the use of the decimal point followed by the number's fractional component. For example, 11.123 is a floating-point constant. C also allows you to use scientific notation for floating-point numbers. Constants using scientific notation must follow this general form:

```
number E sign exponent
```

The sign is optional. Although the general form is shown with spaces between the component parts for clarity, there may be no spaces between the parts in an actual number. For example, the following defines the value 1234.56 using scientific notation:

```
123.456E1
```

Character constants are enclosed between single quotes. For example `'a'` and `'%'` are both character constants. As some of the examples have shown, this means that if you wish to assign a character to a variable of type `char`, you will use a statement similar to

```c
ch = 'Z';
```

However, there is nothing in C that prevents you from assigning a character variable a value using a numeric constant. For example, the ASCII code for 'A' is 65. Therefore, these two assignment statements are equivalent.

```c
char ch;

ch = 'A';
ch = 65;
```

When you enter numeric constants into your program, the compiler must decide what type of constant they are. For example, is 1000 an `int`, an `unsigned`, or a `short`? The reason we haven't worried about this earlier is that C automatically converts the type of the right side of an assignment statement to that of the variable on the left. (We will examine this process more fully later in this chapter.) So, for many situations it doesn't matter what the compiler thinks 1000 is. However, this can be important when you use a constant as an argument to a function, such as in a call to `printf()`.

By default, the C compiler fits a numeric constant into the smallest compatible data type that will hold it. Assuming 16-bit integers, 10 is an `int` by default and 100003 is a `long`. Even though the value 10 could be fit into a `char`, the compiler will not do this because it means crossing type boundaries. The only exceptions to the smallest-type rule are floating-point constants, which are assumed to be `doubles`. For virtually all programs you will write as a beginner, the compiler defaults are perfectly adequate. However, as you will see later in this book, there will come a point when you will need to specify precisely the type of constant you want.

In cases where the assumption that C makes about a numeric constant is not what you want, C allows you to specify the exact type by using a suffix. For floating-point types, if you follow the number with an 'F', the number is treated as a `float`. If you follow it with an 'L', the number becomes a `long double`. For integer types, the 'U' suffix stands for `unsigned` and the 'L' stands for `long`.

As you may know, in programming it is sometimes easier to use a number system based on 8 or 16 instead of 10. As you learned in Chapter 2, the number system based on 8 is called *octal* and it uses the digits 0 through 7. The base-16 number system is called *hexadecimal* and uses the digits 0 through 9 plus the letters 'A' through 'F', which stand for 10 through 15. C allows you to specify integer constants as hexadecimal or octal instead of decimal if you prefer. A hexadecimal constant must begin with '0x' (a zero followed by an x) then the constant in hexadecimal form. An octal constant begins with a zero. For example, `0xAB` is a hexadecimal constant, and `024` is an octal constant. You may use either upper- or lowercase letters when entering hexadecimal constants.

C supports one other type of constant in addition to those of the predefined data types: the string. A *string* is a set of characters enclosed by double quotes. You have been working with strings since Chapter 1 because both the `printf()` and `scanf()` functions use them. Keep in mind one important fact: although C allows you to define string constants, it does not formally have a string data type. Instead, as you will see a little later in this book, strings are supported in C as character arrays. (Arrays are discussed in Chapter 5.)

To display a string using `printf()` you can either make it part of the control string or pass it as a separate argument and display it using the `%s` format code. For example, this program prints **Once upon a time** on the screen:

```c
#include <stdio.h>

int main(void)
{
    printf("%s %s %s", "Once", "upon", "a time");

    return 0;
}
```

Here, each string is passed to `printf()` as an argument and displayed using the `%s` specifier.

### EXAMPLES

1. To see why it is important to use the correct type specifier with `printf()`, try this program. (It assumes that short integers are 16 bits.) Instead of printing the number 42340, it displays **-23196**, because it thinks that it is receiving a signed short integer. The problem is that 42,340 is outside the range of a short int. To make it work properly, you must use the `%hu` specifier.

```c
#include <stdio.h>

int main(void)
{
    printf("%hd", 42340); /* this won't work right */

    return 0;
}
```

2. To see why you may need to explicitly tell the compiler what type of constant you are using, try this program. For most compilers, it will not produce the desired output. (If it does work, it is only by chance.)

```c
#include <stdio.h>

int main(void)
{
    printf("%f", 2309);

    return 0;
}
```

This program is telling `printf()` to expect a floating point value, but the compiler assumes that 2309 is simply an `int`. Hence, it does not output the correct value. To fix it, you must specify 2309 as `2309.0`. Adding the decimal point forces the compiler to treat the value as a `double`.

### EXERCISES

1. How do you tell the C compiler that a floating-point constant should be represented as a `float` instead of a `double`?
2. Write a program that reads and writes a `long int` value.
3. Write a program that outputs **I like C** using three separate strings.

---

## 4.4 INITIALIZE VARIABLES

A variable may be given an initial value when it is declared. This is called *variable initialization*. The general form of variable initialization is shown here:

```c
type var-name = constant;
```

For example, this statement declares `count` as an `int` and gives it an initial value of 100.

```c
int count = 100;
```

The main advantage of using an initialization rather than a separate assignment statement is that the compiler may be able to produce faster code. Also, this saves some typing effort on your part.

Global variables may be initialized using only constants. Local variables can be initialized using constants, variables, or function calls as long as each is valid at the time of the initialization. However, most often both global and local variables are initialized using constants.

Global variables are initialized only once, at the start of program execution. Local variables are initialized each time a function is entered.

Global variables that are not explicitly initialized are automatically set to zero. Local variables that are not initialized should be assumed to contain unknown values. Although some C compilers automatically initialize un-initialized local variables to 0, you should not count on this.

### EXAMPLES

1. This program gives `i` the initial value of -1 and then displays its value.

```c
#include <stdio.h>

int main(void)
{
    int i = -1;

    printf("i is initialized to %d", i);

    return 0;
}
```

2. When you declare a list of variables, you may initialize one or more of them. For example, this fragment initializes `min` to 0 and `max` to 100. It does not initialize `count`.

```c
int min=0, count, max=100;
```

3. As stated earlier, local variables are initialized each time the function is entered. For this reason, this program prints **10** three times.

```c
#include <stdio.h>

void f(void);

int main(void)
{
    f();
    f();
    f();

    return 0;
}

void f(void)
{
    int i = 10;

    printf("%d ", i);
}
```

4. A local variable can be initialized by any expression valid at the time the variable is declared. For example, consider this program:

```c
#include <stdio.h>

int x = 10; /* initialize global variable */

int myfunc(int i);

int main(void)
{
    /* initialize a local variable using
       a global variable */
    int y = x;

    /* initialize a local variable using another
       local variable and a function call */
    int z = myfunc(y);

    printf("%d %d", y, z);

    return 0;
}

int myfunc(int i)
{
    return i/2;
}
```

The local variable `y` is initialized using the value of the global variable `x`. Since `x` is initialized before `main()` is called, it is valid to use its value to initialize a local variable. The value of `z` is initialized by calling `myfunc()` using `y` as an argument. Since `y` has already been initialized, it is entirely proper to use it as an argument to `myfunc()` at this point.

### EXERCISES

1. Write a program that gives an integer variable called `i` an initial value of 100 and then uses `i` to control a `for` loop that displays the numbers 100 down to 1.
2. Assume that this line of code declares global variables. Is it correct?
```c
int a=1, b=2, c=a;
```
3. If the preceding declaration was for local variables, would it be correct?

---

## 4.5 UNDERSTAND TYPE CONVERSIONS IN EXPRESSIONS

Unlike many other computer languages, C lets you mix different types of data together in one expression. For example, this is perfectly valid C code:

```c
char ch;
int i;
float f;
double outcome;

ch = '0';
i = 10;
f = 10.2;

outcome = ch * i / f;
```

C allows the mixing of types within an expression because it has a strict set of conversion rules that dictate how type differences are resolved. Let's look closely at them in this section.

One portion of C's conversion rules is called *integral promotion*. In C, whenever a `char` or a `short int` is used in an expression, its value is automatically elevated to `int` during the evaluation of that expression. This is why you can use `char` variables as "little integers" anywhere an `int` variable can be used. Keep in mind that the integral promotion does not become physically larger. (In essence, the compiler just uses a temporary copy of its value.)

After the automatic integral promotions have been applied, the C compiler will convert all operands "up" to the type of the largest operand. This is called *type promotion* and is done on an operation-by-operation basis, as described in the following type-conversion algorithm:

```
IF an operand is a long double
    THEN the second is converted to long double
ELSE IF an operand is a double
    THEN the second is converted to double
ELSE IF an operand is a float
    THEN the second is converted to float
ELSE IF an operand is an unsigned long
    THEN the second is converted to unsigned long
ELSE IF an operand is long
    THEN the second is converted to long
ELSE IF an operand is unsigned
    THEN the second is converted to unsigned
```

There is one additional special case: If one operand is `long` and the other is `unsigned int`, and if the value of the `unsigned int` cannot be represented by a `long`, both operands are converted to `unsigned long`.

Once these conversion rules have been applied, each pair of operands will be of the same type and the result of each operation will be the same as the type of both operands.

### EXAMPLES

1. In this program, `i` is elevated to a `float` during the evaluation of the expression `i * f`. Thus, the program prints **232.5**.

```c
#include <stdio.h>

int main(void)
{
    int i;
    float f;

    i = 10;
    f = 23.25;

    printf("%f", i * f);

    return 0;
}
```

2. This program illustrates how short ints are automatically promoted to ints. The `printf()` statement works correctly even though the `%d` modifier is used because `i` is automatically elevated to `int` when `printf()` is called.

```c
#include <stdio.h>

int main(void)
{
    short int i;

    i = -10;
    printf("%d", i);

    return 0;
}
```

3. Even though the final outcome of an expression will be of the largest type, the type conversion rules are applied on an operation-by-operation basis. For example, in this expression

```c
100.0 / (10 / 3)
```

the division of 10 by 3 produces an integer result, since both are integers. Then this value is elevated to 3.0 to divide 100.0.

### EXERCISES

1. Given these variables,
```c
char ch;
short i;
unsigned long ul;
float f;
```
what is the overall type of this expression:
```c
f/ch - (i*ul)
```
2. What is the type of the subexpression `i*ul`, above?

---

## 4.6 UNDERSTAND TYPE CONVERSIONS IN ASSIGNMENTS

In an assignment statement in which the type of the right side differs from that of the left, the type of the right side is converted into that of the left. When the type of the left side is larger than the type of the right side, this process causes no problems. However, when the type of the left side is smaller than the type of the right, data loss may occur. For example, this program displays **-24**:

```c
#include <stdio.h>

int main(void)
{
    char ch;
    int i;

    i = 1000;
    ch = i;

    printf("%d", ch);

    return 0;
}
```

The reason for this is that only the low-order eight bits of `i` are copied into `ch`. Since this sort of assignment type conversion is not an error in C, you will receive no error message. Remember, one reason C was created was to replace assembly language, so it must allow all sorts of type conversions. For example, in some instances you may only want the low-order eight bits of `i`, and this sort of assignment is an easy way to obtain them.

When there is an integer-to-character or a longer-integer to shorter-integer type conversion across an assignment, the basic rule is that the appropriate number of high-order bits will be removed. For example, in many environments, this means 8 bits will be lost when going from an `int` to a `char`, and 16 bits will be lost when going from a `long` to an `int`.

When converting from a `long double` to a `double` or from a `double` to a `float`, precision is lost. When converting from a floating-point value to an integer value, the fractional part is lost, and if the number is too large to fit in the target type, a garbage value will result.

Remember two important points: First, the conversion of an `int` to a `float` or a `float` to `double`, and so on, will not add any precision or accuracy. These kinds of conversions will only change the form in which the value is represented. Second, some C compilers will always treat a `char` variable as an `unsigned` value. Others will treat it as a `signed` value. Thus, what will happen when a character variable holds a value greater than 127 is implementation-dependent. If this is important in a program that you write, it is best to declare the variable explicitly as either `signed` or `unsigned`.

### EXAMPLES

1. As stated, when converting from a floating-point value to an integer value, the fractional portion of the number is lost. The following program illustrates this fact. It prints **1234.0098 1234**.

```c
#include <stdio.h>

int main(void)
{
    int i;
    float f;

    f = 1234.0098;
    i = f; /* convert to int */
    printf("%f %d", f, i);

    return 0;
}
```

2. When converting from a larger integer type to a smaller one, it is possible to generate a garbage value, as this program illustrates. (This program assumes that short integers are 16 bits long and that long integers are 32 bits long.)

```c
#include <stdio.h>

int main(void)
{
    short int si;
    long int li;

    li = 100000;
    si = li; /* convert to short int */

    printf("%hd", si);

    return 0;
}
```

Since the largest value that a short integer can hold is 32,767, it cannot hold 100,000. What the compiler does, however, is copy the lower-order 16 bits of `li` into `si`. This produces the meaningless value of **-31072** on the screen.

### EXERCISES

1. What will this program display?
```c
#include <stdio.h>

int main(void)
{
    int i;
    long double ld;

    ld = 10.0;
    i = ld;

    printf("%d", i);
}
```
2. What does this program display?
```c
#include <stdio.h>

int main(void)
{
    float f;

    f = 10 / 3;
    printf("%f", f);

    return 0;
}
```

---

## 4.7 PROGRAM WITH TYPE CASTS

Sometimes you may want to transform the type of a variable temporarily. For example, you may want to use a floating-point value for one computation, but wish to apply the modulus operator to it elsewhere. Since the modulus operator can only be used on integer values, you have a problem. One solution is to create an integer variable for use in the modulus operation and assign the value of the floating-point variable to it when the time comes. This is a somewhat inelegant solution, however. The other way around this problem is to use a *type cast*, which causes a temporary type change.

A type cast takes this general form:

```c
(type) value
```

where *type* is the name of a valid C data type. For example,

```c
float f;

f = 100.2;

/* print f as an integer */
printf("%d", (int) f);
```

Here, the type cast causes the value of `f` to be converted to an `int`.

### EXAMPLES

1. As you learned in Chapter 1, `sqrt()`, one of C's library functions, returns the square root of its argument. It uses the MATH.H header file. Its single argument must be of type `double`. It also returns a `double` value. The following program prints the square roots of the numbers between 1 and 100 using a `for` loop. It also prints the whole number portion and the fractional part of each result separately. To do so, it uses a type cast to convert `sqrt()`'s return value into an `int`.

```c
#include <stdio.h>
#include <math.h>

int main(void)
{
    double i;

    for(i=1.0; i<101.0; i++) {
        printf("The square root of %lf is %lf\n", i, sqrt(i));
        printf("Whole number part: %d ", (int)sqrt(i));
        printf("Fractional part: %lf\n", sqrt(i)-(int)sqrt(i));
        printf("\n");
    }

    return 0;
}
```

2. You cannot cast a variable that is on the left side of an assignment statement. For example, this is an invalid statement in C:

```c
int num;

(float) num = 123.23; /* this is incorrect */
```

### EXERCISES

1. Write a program that uses `for` to print the numbers 1 to 10 by tenths. Use a floating-point variable to control the loop. However, use a type cast so that the conditional expression is evaluated as an integer expression in the interest of speed.
2. Since a floating point value cannot be used with the `%` operator, how can you fix this statement?
```c
x = 123.23 % 3; /* fix this statement */
```

---

## Mastery Skills Check

At this point you should be able to answer these questions and perform these exercises:

1. What are C's data-type modifiers and what function do they perform?
2. How do you explicitly define an unsigned constant, a long constant, and a long double constant?
3. Show how to give a float variable called `balance` an initial value of 0.0.
4. What are C's automatic integral promotions?
5. What is the difference between a signed and an unsigned integer?
6. Give one reason why you might want to use a global variable in your program.
7. Write a program that contains a function called `series()`. Have this function generate a series of numbers, based upon this formula:
```
next-number = (previous-number * 1468) % 467
```
Give the number an initial value of 21. Use a global variable to hold the last value between function calls. In `main()` demonstrate that the function works by calling it ten times and displaying the result.
8. What is a type cast? Give an example.

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. As you know from Chapter 3, no two cases with the same switch may use the same value. Therefore, is this switch valid or invalid? Why? (Hint: the ASCII code for 'A' is 65.)

```c
switch(x) {
    case 'A': printf("is an A");
        break;
    case 65 : printf("is the number 65");
        break;
}
```

2. Technically, for traditional reasons the `getchar()` and `getche()` functions are declared as returning integers, not character values. However, the character read from the keyboard is contained in the low-order byte. Can you explain why this value can be assigned to `char` variables?
3. In this fragment, will the loop ever terminate? Why? (Assume integers are 16 bits long.)

```c
int i;
for(i=0; i<33000; i++);
```
