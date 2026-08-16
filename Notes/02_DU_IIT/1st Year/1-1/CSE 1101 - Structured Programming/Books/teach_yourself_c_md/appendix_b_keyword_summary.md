# Appendix B: C Keyword Summary

THERE are 32 keywords that, when combined with the formal C syntax, form the C language as defined by the ANSI C standard. These keywords are shown in Table B-1.

All C keywords use lowercase letters. In C, uppercase and lowercase are different; for instance, `else` is a keyword, `ELSE` is not.

An alphabetical summary of each of the keywords follows:

| | | | |
| :--- | :--- | :--- | :--- |
| auto | double | int | struct |
| break | else | long | switch |
| case | enum | register | typedef |
| char | extern | return | union |
| const | float | short | unsigned |
| continue | for | signed | void |
| default | goto | sizeof | volatile |
| do | if | static | while |

*Table B-1 Keyword List*

---

### auto

`auto` is used to create temporary variables that are created upon entry into a block and destroyed upon exit. For example:

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    for(;;) {
        if(getche()=='a') {
            auto int t;
            for(t=0; t<'a'; t++)
                printf("%d ", t);
            break;
        }
    }

    return 0;
}
```

In this example, the variable `t` is created only if the user strikes an **a**. Outside the `if` block, `t` is completely unknown; and any reference to it would generate a compile-time syntax error. The use of `auto` is completely optional since all local variables are `auto` by default.

---

### break

`break` is used to exit from a `do`, `for`, or `while` loop, bypassing the normal loop condition. It is also used to exit from a `switch` statement.

An example of `break` in a loop is shown here:

```c
while(x<100) {
    x = get_new_x();
    if(kbhit()) break; /* key hit on keyboard */
    process(x);
}
```

Here, if a key is pressed, the loop will terminate no matter what the value of `x` is.

In a switch statement, `break` effectively keeps program execution from "falling through" to the next case. (Refer to the `switch` section for details.)

---

### case

`case` is covered in conjunction with `switch`.

---

### char

`char` is a data type used to declare character variables. For example, to declare `ch` to be a character type, you would write:

```c
char ch;
```

In C, a character is one byte long.

---

### const

The `const` modifier tells the compiler that the contents of a variable cannot be changed. It is also used to prevent a function from modifying the object pointed to by one of its arguments.

---

### continue

`continue` is used to bypass portions of code in a loop and forces the conditional expression to be evaluated. For example, the following `while` loop will simply read characters from the keyboard until an **s** is typed:

```c
while(ch=getche()) {
    if(ch != 's') continue; /* read another char */
    process(ch);
}
```

The call to `process()` will not occur until `ch` contains the character **s**.

---

### default

`default` is used in the `switch` statement to signal a default block of code to be executed if no matches are found in the switch. See the `switch` section.

---

### do

The `do` loop is one of three loop constructs available in C. The general form of the `do` loop is

```c
do {
    statement block
} while(condition);
```

If only one statement is repeated, the braces are not necessary, but they add clarity to the statement. The `do` loop repeats as long as the *condition* is true.

The `do` loop is the only loop in C that will always have at least one iteration because the condition is tested at the bottom of the loop.

A common use of the `do` loop is to read disk files. This code will read a file until an `EOF` is encountered.

```c
do {
    ch = getc(fp);
    if(!feof(fp)) printf("%c", ch);
} while(!feof(fp));
```

---

### double

`double` is a data type specifier used to declare double-precision floating-point variables. To declare `d` to be of type `double` you would write the following statement:

```c
double d;
```

---

### else

See the `if` section.

---

### enum

The `enum` type specifier is used to create enumeration types. An enumeration is simply a list of named integer constants. For example, the following code declares an enumeration called `color` that consists of three constants: `red`, `green`, and `yellow`.

```c
#include <stdio.h>

enum color {red, green, yellow};
enum color c;

int main(void)
{
    c = red;
    if(c==red) printf("is red\n");

    return 0;
}
```

---

### extern

The `extern` data type modifier tells the compiler that a variable is defined elsewhere in the program. This is often used in conjunction with separately compiled files that share the same global data and are linked together. In essence, it notifies the compiler of a variable without redefining it.

As an example, if `first` were declared in another file as an integer, the following declaration would be used in subsequent files:

```c
extern int first;
```

---

### float

`float` is a data type specifier used to declare floating-point variables. To declare `f` to be of type `float` you would write:

```c
float f;
```

---

### for

The `for` loop allows automatic initialization and incrementation of a counter variable. The general form is

```c
for(initialization; condition; increment) {
    statement block
}
```

If the statement block is only one statement, the braces are not necessary.

Although the `for` allows a number of variations, generally the *initialization* is used to set a counter variable to its starting value. The *condition* is generally a relational statement that checks the counter variable against a termination value, and the *increment* increments (or decrements) the counter value. The loop repeats until the condition becomes false.

The following code will print **hello** ten times.

```c
for(t=0; t<10; t++) printf("Hello\n");
```

---

### goto

The `goto` causes program execution to jump to the label specified in the `goto` statement. The general form of the `goto` is

```c
goto label;
.
.
.
label:
```

All labels must end in a colon and must not conflict with keywords or function names. Furthermore, a `goto` can branch only within the current function, and not from one function to another.

The following example will print the message **right** but not the message **wrong**:

```c
goto lab1;
printf("wrong");
lab1:
printf("right");
```

---

### if

The general form of the `if` statement is

```c
if(condition) {
    statement block 1
}
else {
    statement block 2
}
```

If single statements are used, the braces are not needed. The `else` is optional.

The condition may be any expression. If that expression evaluates to any value other than 0, then statement block 1 will be executed; otherwise, if it exists, statement block 2 will be executed.

The following code fragment can be used for keyboard input and to look for a 'q' which signifies "quit."

```c
ch = getche();
if(ch=='q') {
    printf("Program Terminated");
    exit(0);
}
else proceed();
```

---

### int

`int` is the type specifier used to declare integer variables. For example, to declare `count` as an integer you would write

```c
int count;
```

---

### long

`long` is a data type modifier used to declare long integer and long double variables. For example, to declare `count` as a long integer you would write

```c
long int count;
```

---

### register

The `register` modifier requests that a variable be stored in the way that allows the fastest possible access. In the case of characters or integers, this usually means a register of the CPU. To declare `i` to be a register integer, you would write

```c
register int i;
```

---

### return

The `return` statement forces a return from a function and can be used to transfer a value back to the calling routine. For example, the following function returns the product of its two integer arguments.

```c
int mul(int a, int b)
{
    return a*b;
}
```

Keep in mind that as soon as a return is encountered, the function will return, skipping any other code in the function.

---

### short

`short` is a data type modifier used to declare small integers. For example, to declare `sh` to be a short integer you would write

```c
short int sh;
```

---

### signed

The `signed` type modifier is most commonly used to specify a signed char data type.

---

### sizeof

The `sizeof` keyword is a compile-time operator that returns the length of the variable or type it precedes. If it precedes a type, the type must be enclosed in parentheses. For example,

```c
printf("%d", sizeof(short int));
```

will print 2 for most C implementations.

The `sizeof` statement's principal use is in helping to generate portable code when that code depends on the size of the C built-in data types.

---

### static

The `static` keyword is a data type modifier that causes the compiler to create permanent storage for the local variable that it precedes. This enables the specified variable to maintain its value between function calls. For example, to declare `last_time` as a `static` integer, you would write

```c
static int last_time;
```

`static` can also be used on global variables to limit their scope to the file in which they are declared.

---

### struct

The `struct` statement is used to create aggregate data types, called structures, that are made up of one or more members. The general form of a structure is

```c
struct struct-name {
    type member1;
    type member2;
    .
    .
    .
    type memberN;
} variable-list;
```

The individual members are referenced using the dot or arrow operators.

---

### switch

The `switch` statement is C's multi-path branch statement. It is used to route execution in one of several ways. The general form of the statement is

```c
switch(int-expression) {
    case constant1: statement-set 1;
        break;
    case constant2: statement-set 2;
        break;
    .
    .
    .
    case constantN: statement-set N;
        break;
    default: default-statements;
}
```

Each *statement-set* may be one or many statements long. The `default` portion is optional. The expression controlling the `switch` and all case constants must be of integral or character types.

The switch works by checking the value of *int-expression* against the constants. As soon as a match is found, that set of statements is executed. If the `break` statement is omitted, execution will continue into the next case. You can think of the cases as labels. Execution will continue until a break statement is found or the switch ends.

The following example can be used to process a menu selection:

```c
ch = getche();

switch(ch) {
    case 'e': enter();
        break;
    case 'l': list();
        break;
    case 's': sort();
        break;
    case 'q': exit(0);
        break;
    default: printf("Unknown Command\n");
             printf("Try Again\n");
}
```

---

### typedef

The `typedef` statement allows you to create a new name for an existing data type. The general form of `typedef` is

```c
typedef type-specifier new-name;
```

For example, to use the word `balance` in place of `float`, you would write

```c
typedef float balance;
```

---

### union

The `union` keyword creates an aggregate type in which two or more variables share the same memory location. The form of the declaration and the way a member is accessed are the same as for `struct`. The general form is

```c
union union-name {
    type member1;
    type member2;
    .
    .
    .
    type memberN;
} variable-list;
```

---

### unsigned

The `unsigned` type modifier tells the compiler to create a variable that holds only unsigned (i.e., positive) values. For example, to declare `big` to be an unsigned integer you would write

```c
unsigned int big;
```

---

### void

The `void` type specifier is primarily used to declare void functions (functions that do not return values). It is also used to create void pointers (pointers to void) that are generic pointers capable of pointing to any type of object and to specify an empty parameter list.

---

### volatile

The `volatile` modifier tells the compiler that a variable may have its contents altered in ways not explicitly defined by the program. Variables that are changed by the hardware, such as real-time clocks, interrupts, or other inputs are examples.

---

### while

The `while` loop has the general form:

```c
while(condition) {
    statement block
}
```

If a single statement is the object of the `while`, the braces may be omitted. The loop will repeat as long as the *condition* is true.

The `while` tests its condition at the top of the loop. Therefore, if the condition is false to begin with, the loop will not execute at all. The condition may be any expression.

An example of a `while` follows. It reads characters until end-of-file is encountered.

```c
t = 0;

while(!feof(fp)) {
    s[t] = getc(fp);
    t++;
}
```
