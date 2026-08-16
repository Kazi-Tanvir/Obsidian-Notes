# 8 Console I/O

IN this chapter you will learn about C's console I/O functions. These are the functions that read or write information to and from the console. You have already been using some of these functions. Here we will look at them in detail. This chapter begins with a short but necessary digression that introduces another of C's preprocessor directives: **#define**.

---

### Review Skills Check

Before proceeding, you should be able to answer these questions and perform these exercises:

1. What must you do to enable the compiler to check that a function is being called correctly?
2. What are the principal advantages of using function prototypes?
3. Write a program that uses a function called `hypot()` that returns the length of the hypotenuse of a right triangle when passed the length of the two opposing sides. Have the function return a **double** value. The type of the parameters must be **double** as well. Demonstrate the function in a program. (The Pythagorean theorem states that the sum of the squares of the two opposing sides equals the square of the hypotenuse.)
4. What return type should you use for a function that returns no value?
5. Write a recursive function called `rstrlen()` that uses recursion to compute the length of a string. Demonstrate it in a program.
6. Write a program that reports how many command line arguments it has been called with. Also, have it display the contents of the last one.
7. How is this declaration coded using the old-style function declaration form?
```c
void func(int a, char ch, double d)
{
```

---

## 8.1 LEARN ANOTHER PREPROCESSOR DIRECTIVE

As you recall, the C preprocessor performs various manipulations on the source code of your program before it is actually compiled. A preprocessor directive is simply an instruction to the preprocessor. Up to this point, you have learned about and have used one preprocessor directive, **#include**. Before proceeding, you need to learn about another: **#define**.

The **#define** directive tells the preprocessor to perform a text substitution throughout your entire program. That is, it causes one sequence of characters to be replaced by another. This process is generally referred to as *macro substitution*. The general form of the **#define** statement is shown here:

`#define macro-name character-sequence`

Notice that this line does not end in a semicolon. Each time the *macro-name* is encountered in the program, the associated *character-sequence* is substituted for it. For example, consider this program:

```c
#include <stdio.h>

#define MAX 100

int main(void)
{
    int i;

    for(i=0; i<MAX; i++) printf("%d ", i);

    return 0;
}
```

When the identifier MAX is encountered by the preprocessor, 100 is automatically substituted. Thus, the **for** loop will actually look like this to the compiler:

```c
for(i=0; i<100; i++) printf("%d ", i);
```

Keep one thing clearly in mind: At the time of the substitution, 100 is simply a string of characters composed of a 1 and two 0s. The preprocessor does not convert a numeric string into its internal binary format. This is left to the compiler.

The macro name can be any valid C identifier. Thus, macro names must follow the same naming rules as do variables. Although macro names can appear in either upper- or lowercase letters, most programmers have adopted the convention of using uppercase for macro names. This makes it easy for anyone reading your program to know when a macro name is being used.

There must be one or more spaces between the macro name and the character sequence. The character sequence can contain any type of character, including spaces. It is terminated by the end of the line.

Preprocessor directives in general and **#define** in particular are not affected by C's code blocks. That is, whether you define a macro name outside of all functions or within a function, once it is defined, all code after that point may have access to it. For example, this program prints 186000 on the screen.

```c
#include <stdio.h>

void f(void);

int main(void)
{
    #define LIGHTSPEED 186000

    f();

    return 0;
}

void f(void)
{
    printf("%ld", LIGHTSPEED);
}
```

There is one important point you must remember: Each preprocessor directive must appear on its own line.

Macro substitutions are useful for two main reasons. First, many C library functions use certain predefined values to indicate special conditions or results. Your programs will need access to these values when they use one of these functions. However, many times the actual value will vary between programming environments. For this reason, these values are usually specified using macro names. The macro names are defined inside the header file that relates to each specific function. You will see an example of this in the next section.

The second reason macro substitution is important is that it can help make it easier to maintain programs. For example, if you know that a value, such as an array size, is going to be used several places in your program, it is better to create a macro for this value. Then if you ever need to change this value, you simply change the macro definition. All references to it will be changed automatically when the program is recompiled.

### EXAMPLES

1. Since a macro substitution is simply a text replacement, you can use a macro name in place of a quoted string. For example, the following program prints **Macro Substitutions are Fun**.

```c
#include <stdio.h>

#define FUN "Macro Substitutions are Fun"

int main(void)
{
    printf(FUN);

    return 0;
}
```

To the compiler, the `printf()` statement looks like this:

```c
printf("Macro Substitutions are Fun");
```

2. Once a macro name has been defined, it can be used to help define another macro name. For example, consider this program:

```c
#include <stdio.h>

#define SMALL 1
#define MEDIUM SMALL+1
#define LARGE MEDIUM+1

int main(void)
{
    printf("%d %d %d", SMALL, MEDIUM, LARGE);

    return 0;
}
```

As you might expect, it prints **1 2 3** on the screen.

3. If a macro name appears inside a quoted string, no substitution will take place. For example, given this definition

```c
#define ERROR "catastrophic error occurred"
```

the following statement will not be affected.

```c
printf("ERROR: Try again");
```

### EXERCISES

1. Create a program that defines two macro names, **MAX** and **COUNTBY**. Have the program count from zero to **MAX-1** by whatever value **COUNTBY** is defined as. (Give **COUNTBY** the value 3 for demonstration purposes.)
2. Is this fragment correct?
```c
#define MAX MIN+100
#define MIN 10
```
3. Is this fragment correct?
```c
#define STR this is a test

printf(STR);
```
4. Is this program correct?
```c
#define STDIO <stdio.h>
#include STDIO

int main(void)
{
    printf("This is a test.");

    return 0;
}
```

---

## 8.2 EXAMINE CHARACTER AND STRING INPUT AND OUTPUT

Although you have already learned how to input and output characters and strings, this section looks at these processes more formally.

The ANSI C standard defines these two functions that perform character input and output, respectively:

```c
int getchar(void);
int putchar(int ch);
```

They both use the header file STDIO.H. As mentioned earlier in this book, many compilers implement `getchar()` in a line-buffered manner, which makes its use limited in an interactive environment. Most compilers contain a non-standard function called `getche()`, which operates like `getchar()`, except that it is interactive. Discussion of `getche()` and other non-standard functions will occur in a later section.

The `getchar()` function returns the next character typed on the keyboard. This character is read as an **unsigned char** converted to an **int**. However, most commonly, your program will assign this value to a **char** variable, even though `getchar()` is declared as returning an **int**. If you do this, the high-order byte(s) of the integer is simply discarded.

The reason that `getchar()` returns an integer is that when an error occurs while reading input, `getchar()` returns the macro **EOF**, which is a negative integer (usually -1). The **EOF** macro, defined in STDIO.H, stands for end-of-file. Since **EOF** is an integer value, to allow it to be returned, `getchar()` must return an integer. In the vast majority of circumstances, if an error occurs when reading from the keyboard, it means that the computer has ceased to function. Therefore, most programmers don't usually bother checking for **EOF** when using `getchar()`. They just assume a valid character has been returned. Of course, there are circumstances in which this is not appropriate—for example, when I/O is redirected, as explained in Chapter 9. But most of the time you will not need to worry about `getchar()` encountering an error.

The `putchar()` function outputs a single character to the screen. Although its parameter is declared to be of type **int**, this value is converted into an **unsigned char** by the function. Thus, only the low-order byte of *ch* is actually displayed. If the output operation is successful, `putchar()` returns the character written. If an output error occurs, **EOF** is returned. For reasons similar to those given for `getchar()`, if output to the screen fails, the computer has probably crashed anyway, so most programmers don't bother checking the return value of `putchar()` for errors.

The reason you might want to use `putchar()` rather than `printf()` with the `%c` specifier to output a character is that `putchar()` is faster and more efficient. Because `printf()` is more powerful and flexible, a call to `printf()` generates greater overhead than a call to `putchar()`.

### EXAMPLES

1. As stated earlier, `getchar()` is generally implemented using line buffering. When input is line buffered, no characters are actually passed back to the calling program until the user presses ENTER. The following program demonstrates this:

```c
#include <stdio.h>

int main(void)
{
    char ch;

    do {
        ch = getchar();
        putchar('.');
    } while(ch != '\n');

    return 0;
}
```

Instead of printing a period between each character, what you will see on the screen is all the letters you typed before pressing ENTER, followed by a string of periods.

One other point: When entering characters using `getchar()`, pressing ENTER will cause the newline character (`\n`) to be returned. However, when using one of the alternative non-standard functions, pressing ENTER will cause the carriage return character (`\r`) to be returned. Keep this difference in mind.

2. The following program illustrates the fact that you can use C's backslash character constants with `putchar()`.

```c
#include <stdio.h>

int main(void)
{
    putchar('A');
    putchar('\n');
    putchar('B');

    return 0;
}
```

This program displays

```
A
B
```

on the screen.

### EXERCISES

1. Rewrite the program shown in the first example so that it checks for errors on both input and output operations.
2. What is wrong with this fragment?
```c
char str[80] = "this is a test";

.
.
.
putchar(str);
```

---

## 8.3 EXAMINE SOME NON-STANDARD CONSOLE FUNCTIONS

Because character input using `getchar()` is usually line-buffered, many compilers supply additional input routines that provide interactive character input. You have already been introduced to one of these: `getche()`. Here is its prototype and that of its close relative `getch()`:

```c
int getche(void);
int getch(void);
```

Both functions use the header file CONIO.H. The `getche()` function waits until the next keystroke is entered at the keyboard. When a key is pressed, `getche()` echoes it to the screen and then immediately returns the character. The character is read as an **unsigned char** and elevated to **int**. However, your routines can simply assign this value to a **char** value. The `getch()` function is the same as `getche()`, except that the keystroke is not echoed to the screen.

Another very useful non-ANSI-standard function commonly supplied with a C compiler is `kbhit()`. It has this prototype:

```c
int kbhit(void);
```

The `kbhit()` function also requires the header file CONIO.H. This function is used to determine whether a key has been pressed or not. If the user has pressed a key, this function returns true (nonzero), but does not read the character. If a keystroke is waiting, you may read it with `getche()` or `getch()`. If no keystroke is pending, `kbhit()` returns false (zero).

For some compilers, the non-standard I/O functions such as `getche()` are not compatible with the standard I/O functions such as `printf()` or `scanf()`. When this is the case, mixing the two can cause unusual program behavior. Most troubles caused by this incompatibility occur when inputting information (although problems could occur on output). If the standard and non-standard I/O functions are not compatible in your compiler, you may need to use non-standard versions of `scanf()` and/or `printf()`, too. These are called `cprintf()` and `cscanf()`.

The `cprintf()` function works like `printf()` except that it does not translate the newline character (`\n`) into the carriage return, linefeed pair as does the `printf()` function. Therefore, it is necessary to explicitly output the carriage return (`\r`) where desired. The `cscanf()` function works like the `scanf()` function. Both `cprintf()` and `cscanf()` use the CONIO.H header file. The `cprintf()` and `cscanf()` functions are expressly designed to be compatible with `getch()` and `getche()`, as well as other non-standard I/O functions.

> [!NOTE]
> Microsoft C++ supports the functions just described. In addition, it provides alternative names for the functions that begin with an underscore. For example, when using Visual C++, you can specify `getche()` as `_getche()`, too.

One last point: Even for compilers that have incompatibilities between the standard and non-standard I/O functions, such incompatibilities sometimes only apply in one case and not another. If you encounter a problem, just try substituting a different function.

### EXAMPLES

1. The `getch()` function lets you take greater control of the screen because you can determine what is displayed each time a key is struck. For example, this program reads characters until a 'q' is typed. All characters are displayed in uppercase using the `cprintf()` function.

```c
#include <stdio.h>
#include <conio.h>
#include <ctype.h>

int main(void)
{
    char ch;

    do {
        ch = getch();
        cprintf("%c", toupper(ch));
    } while(ch != 'q');

    return 0;
}
```

2. The `kbhit()` function is very useful when you want to let a user interrupt a routine without actually forcing the user to continually respond to a prompt like "Continue?". For example, this program prints a 5-percent sales-tax table in increments of 20 cents. The program continues to print the table until either the user strikes a key or the maximum value is printed.

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    double amount;

    amount = 0.20;

    cprintf("Printing 5-percent tax table\n\r");
    cprintf("Press a key to stop.\n\n\r");
    do {
        cprintf("amount: %f, tax: %f\n\r", amount,
                amount*0.05);
        if(kbhit()) break;
        amount = amount + 0.20;
    } while(amount < 100.0);

    return 0;
}
```

In the calls to `cprintf()`, notice how both the carriage return (`\r`) and the newline (`\n`) must be output. As explained, `cprintf()` does not automatically convert newlines into carriage return, linefeed pairs.

### EXERCISES

1. Write a program that displays the ASCII code of each character typed. Do not display the actual character, however.
2. Write a program that prints periods on the screen until you press a key.

---

## 8.4 TAKE A CLOSER LOOK AT gets( ) AND puts( )

Although both `gets()` and `puts()` were introduced earlier, let's take a closer look at them now. Their function prototypes are

```c
char *gets(char *str);
int puts(char *str);
```

These functions use the header file STDIO.H. The `gets()` function reads characters entered at the keyboard until a carriage return is read (i.e., until the user presses ENTER). It stores the characters in the array pointed to by *str*. The carriage return is not added to the string. Instead, it is converted into the null terminator. If successful, `gets()` returns a pointer to the start of *str*. If an error occurs, a null pointer is returned.

The `puts()` function outputs the string pointed to by *str* to the screen. It automatically appends a carriage return, line-feed sequence. If successful, `puts()` returns a non-negative value. If an error occurs, **EOF** is returned.

The main reason you may want to use `puts()` instead of `printf()` to output a string is that `puts()` is much smaller and faster. While this is not important in the example programs shown in this book, it may be in some applications.

### EXAMPLES

1. This program shows how you can use the return value of `gets()` to access the string holding the input information. Notice that this program also confirms that no error has occurred before attempting to use the string.

```c
#include <stdio.h>

int main(void)
{
    char *p, str[80];

    printf("Enter a string: ");
    p = gets(str);
    if(p) /* if not null */
        printf("%s %s", p, str);

    return 0;
}
```

2. If you simply want to make sure that `gets()` did not encounter an error before proceeding, you can place `gets()` directly inside an **if** statement, as illustrated by the following program:

```c
#include <stdio.h>

int main(void)
{
    char str[80];

    printf("Enter a string: ");
    if(gets(str)) /* if not null */
        printf("Here is your string: %s", str);

    return 0;
}
```

Because a null pointer is false, there is no need for the intermediary variable **p**, and the `gets()` statement can be put directly inside the **if**.

3. It is important to understand that even though `gets()` returns a pointer to the start of the string, it still must be called with a pointer to an actual array. For example, the following is wrong:

```c
char *p;

p = gets(p); /* wrong!!! */
```

Here, there is no array defined into which `gets()` can put the string. This will result in a program failure.

4. This program outputs the words **one**, **two**, and **three** on three separate lines, using `puts()`.

```c
#include <stdio.h>

int main(void)
{
    puts("one");
    puts("two");
    puts("three");

    return 0;
}
```

### EXERCISES

1. Compile the program shown in Example 2, above. Note the size of the compiled code. Next, convert it so that it uses `printf()` statements, instead of `puts()`. You will find that the `printf()` version is several bytes larger.
2. Is this program correct? If not, why not?
```c
#include <stdio.h>

int main(void)
{
    char *p, *q;

    printf("Enter a string: ");
    p = gets(q);
    printf(p);

    return 0;
}
```

---

## 8.5 MASTER printf( )

Although you already know many things about `printf()`, you will be surprised by how many more features it has. In this section you will learn about some more of them. To begin, let's review what you know so far.

The `printf()` function has this prototype:

```c
int printf(char *control-string, ...);
```

The periods indicate a variable-length argument list. The `printf()` function returns the number of characters output. If an error occurs, it returns a negative number. Frankly, few programmers bother with the return value of `printf()` because, as mentioned earlier, if the console is not working, the computer is probably not functional anyway.

The control string may contain two types of items: characters to be output and format specifiers. All format specifiers begin with `%`. A format specifier, also referred to as a *format code*, determines how its matching argument will be displayed. Format specifiers and their arguments are matched from left to right, and there must be as many arguments as there are specifiers.

The format specifiers accepted by `printf()` are shown in Table 8-1. You have already learned about the `%c`, `%d`, `%s`, `%u`, `%p`, and `%f` specifiers. The others will be examined now.

| Code | Format |
| :--- | :--- |
| `%c` | Character |
| `%d` | Signed decimal integers |
| `%i` | Signed decimal integers |
| `%e` | Scientific notation (lowercase 'e') |
| `%E` | Scientific notation (uppercase 'E') |
| `%f` | Decimal floating point |
| `%g` | Uses `%e` or `%f`, whichever is shorter |
| `%G` | Uses `%E` or `%f`, whichever is shorter |
| `%o` | Unsigned octal |
| `%s` | String of characters |
| `%u` | Unsigned decimal integers |
| `%x` | Unsigned hexadecimal (lowercase letters) |
| `%X` | Unsigned hexadecimal (uppercase letters) |
| `%p` | Displays a pointer |
| `%n` | The associated argument is a pointer to an integer into which the number of characters written so far is placed. |
| `%%` | Prints a `%` sign |

*Table 8-1 The printf( ) Format Specifiers*

The `%i` command is the same as `%d` and is redundant.

You can display numbers of type **float** or **double** using scientific notation by using either `%e` or `%E`. The only difference between the two is that `%e` uses a lowercase 'e' and `%E` uses an uppercase 'E'. These specifiers may have the **L** modifier applied to them to allow them to display values of type **long double**.

The `%g` and `%G` specifiers cause output to be in either normal or scientific notation, depending upon which is shorter. The difference between the `%g` and the `%G` is whether a lower- or uppercase 'e' is used in cases where scientific notation is shorter. These specifiers may have the **L** modifier applied to them to allow them to display values of type **long double**.

You can display an integer in octal format using `%o` or in hexadecimal using `%x` or `%X`. Using `%x` causes the letters 'a' through 'f' to be displayed in lowercase. Using `%X` causes them to be displayed in uppercase. These specifiers may have the **h** and **l** modifiers applied to allow them to display short and long data types, respectively.

The argument that matches the `%n` specifier must be a pointer to an integer. When the `%n` is encountered, `printf()` assigns the integer pointed to by the associated argument the number of characters output so far.

Since all format commands begin with a percent sign, you must use `%%` to output a percent sign.

All but the `%%`, `%p`, and `%c` specifiers may have a minimum-field-width specifier and/or a precision specifier associated with them. Both of these are integer quantities. If the item to output is shorter than the specified minimum field width, the output is padded with spaces, so that it equals the minimum width. However, if the output is longer than the minimum, output is *not* truncated. The minimum-field-width specifier is placed after the `%` sign and before the format specifier.

The precision specifier follows the minimum-field-width specifier. The two are separated by a period. The precision specifier affects different types of format specifiers differently. If it is applied to the `%d`, `%i`, `%o`, `%u` or `%x` specifiers, it determines how many digits are to be shown. Leading zeros are added if needed. When applied to `%f`, `%e`, or `%E`, it determines how many digits will be displayed after the decimal point. For `%g` or `%G`, it determines the number of significant digits. When applied to the `%s`, it specifies a maximum field width. If a string is longer than the maximum-field-width specifier, it will be truncated.

By default, all numeric output is right justified. To left justify output, put a minus sign directly after the `%` sign.

The general form of a format specifier is shown here. Optional items are shown between brackets.

`%[-][minimum-field-width][.][precision]format-specifier`

For example, this format specifier tells `printf()` to output a **double** value using a field width of 15, with 2 digits after the decimal point.

`%15.2f`

### EXAMPLES

1. If you don't want to specify a minimum field width, you can still specify the precision. Simply put a period in front of the precision value, as illustrated by the following program:

```c
#include <stdio.h>

int main(void)
{
    printf("%.5d\n", 10);
    printf("$%.2f\n", 99.95);
    printf("%.10s", "Not all of this will be printed\n");

    return 0;
}
```

The output from this program looks like this:

```
00010
$99.95
Not all of
```

Notice the effect of the precision specifier as applied to each data type.

2. The minimum-field-width specifier is especially useful for creating tables that contain columns of numbers that must line up. For example, this program prints 1000 random numbers in three columns. It uses another of C's standard library functions, `rand()`, to generate the random numbers. The `rand()` function returns a random integer value each time it is called. It uses the header STDLIB.H.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int i;

    for(i=0; i<1000; i++)
        printf("%10d %10d %10d\n", rand(), rand(), rand());

    return 0;
}
```

Part of the output from this program is shown here. Notice how the columns are aligned. (Remember, if you try the program, you will probably see different numbers.)

```
10982        130        346
 7117      11656       1090
22948       6415      17595
14558       9004      31126
18492      22879       3571
26721       5412       1360
27119      25047      22463
13985       7190      31441
30252      27509      31214
19816      14779      26571
17995      19651      21681
13310       3734      23593
15561      21995       3979
11288      18489      16092
 5892       8664      28466
 5364      22766      13863
20427      21151      17639
 8812      25795        100
12347      12666      15108
```

3. This program prints the value 90 four different ways: decimal, octal, lowercase hexadecimal, and uppercase hexadecimal. It also prints a floating-point number using scientific notation with a lowercase 'e' and an uppercase 'E'.

```c
#include <stdio.h>

int main(void)
{
    printf("%d %o %x %X\n", 90, 90, 90, 90);
    printf("%e %E\n", 99.231, 99.231);

    return 0;
}
```

The output from this program is shown here:

```
90 132 5a 5A
9.92310e+01 9.92310E+01
```

4. The following program demonstrates the `%n` specifier:

```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("%d %f\n%n", 100, 123.23, &i);
    printf("%d characters output so far", i);

    return 0;
}
```

Its output looks like this:

```
100 123.230000
15 characters output so far
```

The fifteenth character is the newline.

### EXERCISES

1. Write a program that prints a table of numbers, each line consisting of a number, its square, and its cube. Have the table begin at 2 and end at 100. Make the columns line up, and left justify each column.
2. How would you output this line using `printf()`?
`Clearance price: 40% off as marked`
3. Show how to display **1023.03** so that only two decimal places are printed.

---

## 8.6 MASTER scanf( )

Like `printf()`, `scanf()` has many more features than we have used so far. In this section, several of these additional features are explored. Let's begin by reviewing what you have already learned.

The prototype for `scanf()` is shown here:

```c
int scanf(char *control-string, ...);
```

The *control-string* consists mostly of format specifiers. However, it can contain other characters. (You will learn about the effect of other characters in the control string soon.) The format specifiers determine how `scanf()` reads information into the variables pointed to by the arguments that follow the control string. The specifiers are matched in order, from left to right, with the arguments. There must be as many arguments as there are specifiers. The format specifiers are shown in Table 8-2. As you can see, the `scanf()` specifiers are very much like the `printf()` specifiers.

The `scanf()` function returns the number of fields assigned values. If an error occurs before any assignments are made, **EOF** is returned.

The specifiers `%x` and `%o` are used to read an unsigned integer using hexadecimal and octal number bases, respectively.

The specifiers `%d`, `%i`, `%u`, `%x`, and `%o` may be modified by the **h** when inputting into a **short** variable and by **l** when inputting into a **long** variable.

The specifiers `%e`, `%f`, and `%g` are equivalent. They all read floating-point numbers represented in either scientific notation or standard decimal notation. Unmodified, they input information into a **float** variable. You can modify them using an **l** when inputting into a **double**. To read a **long double**, modify them with an **L**.

You can use `scanf()` to read a string using the `%s` specifier, but you probably won't want to. Here's why: When `scanf()` inputs a string, it stops reading that string when the first whitespace character is encountered. A whitespace character is either a space, a tab, or a newline. This means that you cannot easily use `scanf()` to read input like this into a string:

`this is one string`

Because there is a space after "this," `scanf()` will stop inputting the string at that point. This is why `gets()` is generally used to input strings.

| Code | Meaning |
| :--- | :--- |
| `%c` | Read a single character |
| `%d` | Read a decimal integer |
| `%i` | Read a decimal integer |
| `%e` | Read a floating-point number |
| `%f` | Read a floating-point number |
| `%g` | Read a floating-point number |
| `%o` | Read an octal number |
| `%s` | Read a string |
| `%x` | Read a hexadecimal number |
| `%p` | Read a pointer |
| `%n` | Receives an integer value equal to the number of characters read so far |
| `%u` | Read an unsigned integer |
| `%[ ]` | Scan for a set of characters |

*Table 8-2 The scanf( ) Format Specifiers*

The `%p` specifier inputs a memory address using the format determined by the host environment. The `%n` specifier assigns the number of characters input up to the point the `%n` is encountered to the integer variable pointed to by its matching argument. The `%n` may be modified by either **l** or **h** so that it may assign its value to either a **long** or **short** variable.

A very interesting feature of `scanf()` is called a *scanset*. A scanset specifier is created by putting a list of characters inside square brackets. For example, here is a scanset specifier containing the letters 'ABC.'

`%[ABC]`

When `scanf()` encounters a scanset, it begins reading input into the character array pointed to by the scanset's matching argument. It will only continue reading characters as long as the next character is part of the scanset. As soon as a character that is not part of the scanset is found, `scanf()` stops reading input for this specifier and moves on to any others in the control string.

You can specify a range in a scanset using the `-` (hyphen). For example, this scanset specifies the characters 'A' through 'Z'.

`%[A-Z]`

Technically, the use of the hyphen to specify a range is not specified by the ANSI C standard, but it is nearly universally accepted.

When the scanset is very large, sometimes it is easier to specify what is *not* part of a scanset. To do this, precede the set with a `^`. For example,

`%[^0123456789]`

When `scanf()` encounters this scanset, it will read any characters *except* the digits 0 through 9.

You can suppress the assignment of a field by putting an asterisk immediately after the `%` sign. This can be very useful when inputting information that contains needless characters. For example, given this `scanf()` statement

```c
int first, second;
scanf("%d%*c%d", &first, &second);
```

this input

`555-2345`

will cause `scanf()` to assign 555 to **first**, discard the -, and assign 2345 to **second**. Since the hyphen is not needed, there is no reason to assign it to anything. Hence, no associated argument is supplied.

You can specify a maximum field width for all specifiers except `%c`, for which a field is always one character, and `%n`, to which the concept does not apply. The maximum field width is specified as an unsigned integer, and it immediately precedes the format specifier character. For example, this limits the maximum length of a string assigned to **str** to 20 characters:

```c
scanf("%20s", str);
```

If a space appears in the control string, then `scanf()` will begin reading and discarding whitespace characters until the first non-whitespace character is encountered. If any other character appears in the control string, `scanf()` reads and discards all matching characters until it reads the first character that does not match that character.

One other point: As `scanf()` is generally implemented, it line-buffers input in the same way that `getchar()` often does. While this makes little difference when inputting numbers, its lack of interactivity tends to make `scanf()` of limited value for other types of input.

### EXAMPLES

1. To see the effect of the `%s` specifier, try this program. When prompted, type **this is a test** and press ENTER. You will see only **this** redisplayed on the screen. This is because, when reading strings, `scanf()` stops when it encounters the first whitespace character.

```c
#include <stdio.h>

int main(void)
{
    char str[80];

    /* Enter "this is a test" */
    printf("Enter a string: ");
    scanf("%s", str);
    printf(str);

    return 0;
}
```

2. Here's an example of a scanset that accepts both the upper- and lowercase characters. Try entering some letters, then any other character, and then some more letters. After you press ENTER, only the letters that you entered before pressing the non-letter key will be contained in **str**.

```c
#include <stdio.h>

int main(void)
{
    char str[80];

    printf("Enter letters, anything else to stop\n");
    scanf("%[a-zA-Z]", str);

    printf(str);

    return 0;
}
```

3. If you want to read a string containing spaces using `scanf()`, you can do so using the scanset shown in this slight variation of the previous program.

```c
#include <stdio.h>

int main(void)
{
    char str[80];

    printf("Enter letters and spaces\n");
    scanf("%[a-zA-Z ]", str);
    printf(str);

    return 0;
}
```

You could also specify punctuation symbols and digits, so that you can read virtually any type of string. However, this is a fairly cumbersome way of doing things.

4. This program lets the user enter a number followed by an operator followed by a second number, such as 12+4. It then performs the specified operation on the two numbers and displays the results.

```c
#include <stdio.h>

int main(void)
{
    int i, j;
    char op;

    printf("Enter operation: ");
    scanf("%d%c%d", &i, &op, &j);

    switch(op) {
        case '+': printf("%d", i+j);
            break;
        case '-': printf("%d", i-j);
            break;
        case '/': if(j) printf("%d", i/j);
            break;
        case '*': printf("%d", i*j);
    }

    return 0;
}
```

Notice that the format for entering the information is somewhat restricted because no spaces are allowed between the first number and the operator. It is possible to remove this restriction. As you know, `scanf()` automatically discards leading whitespace characters except when you use the `%c` specifier. However, since you know that the operator will not be a whitespace character, you can modify the `scanf()` command to look like this:

```c
scanf("%d %c%d", &i, &op, &j);
```

Whenever there is a space in the control string, `scanf()` will match and discard whitespace characters until the first non-whitespace character is found. This includes matching zero whitespace characters. With this change in place, you can enter the information into the program using one or more spaces between the first number and the operator.

5. This program illustrates the maximum-field-width specifier:

```c
#include <stdio.h>

int main(void)
{
    int i, j;

    printf("Enter an integer: ");
    scanf("%3d%d", &i, &j);
    printf("%d %d", i, j);

    return 0;
}
```

If you run this program and enter the number 12345, **i** will be assigned 123, and **j** will have the value 45. The reason for this is that `scanf()` is told that **i**'s field is only three characters long. The remainder of the input is then sent to **j**.

6. This program illustrates the effect of having non-whitespace characters in the control string. It allows you to enter a decimal value, but it assigns the digits to the left of the decimal point to one integer and those to the right of the decimal to another. The decimal point between the two `%d` specifiers causes the decimal point in the number to be matched and discarded.

```c
#include <stdio.h>

int main(void)
{
    int i, j;

    printf("Enter a decimal number: ");
    scanf("%d.%d", &i, &j);
    printf("left part: %d, right part: %d", i, j);

    return 0;
}
```

### EXERCISES

1. Write a program that prompts for your name and then inputs your first, middle, and last names. Have the program read no more than 20 characters for each part of your name. Finally, have the program redisplay your name.
2. Write a program that reads a floating-point number as a string using a scanset.
3. Is this fragment correct? If not why not?
```c
char ch;

scanf("%2c", &ch);
```
4. Write a program that inputs a string, a double, and an integer. After these items have been read, have the program display how many characters were input. (Hint: use the `%n` specifier.)
5. Write a program that converts a hexadecimal number entered by the user into its corresponding decimal and octal equivalents.

---

## Mastery Skills Check

Before proceeding you should be able to answer these questions and perform these exercises:

1. What is the difference between `getchar()`, `getche()`, and `getch()`?
2. What is the difference between the `%e` and the `%E` `printf()` format specifiers?
3. What is a scanset?
4. Write a program, using `scanf()`, that inputs your first name, birth date (using the format mm/dd/yy), and telephone number. Redisplay the information on the screen to verify that it was input correctly.
5. What is one advantage to using `puts()` over `printf()` when you only need to output a string? What is one disadvantage to `puts()`?
6. Write a program that defines a macro called **COUNT** as the value 100. Have the program then use this macro to control a `for` loop that displays the numbers 0 through 99.
7. What is **EOF**, and where is it defined?

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. Write a program that allows you to enter the batting averages for the players on a little league team. (Assume there are exactly 9 players.) Have the user enter the first name and batting average of each player. Use a two-dimensional character array to hold the names and a one-dimensional double array to hold the batting averages. Once all the names are entered, have the program report the name and average of the players with the highest and lowest averages. Also, have the program display the team average.
2. Write a program that is a simple electronic library card catalog. Have the program display this menu:

```
Card Catalog:
1. Enter
2. Search by Author
3. Search by Title
4. Quit
Choose your selection:
```

If you choose Enter, have the program repeatedly input the name, author, and publisher of a book. Have this process continue until the user enters a blank line for the name of the book.
For searches, prompt the user for the specified author or title and then, if a match is found, display the rest of the information. After you finish this program, keep your file, because in the next chapter you will learn how to save the catalog to a disk file.
