# 11 Advanced Data Types and Operators

THE C language includes a rich set of data type modifiers that allow you to better fit the type of a variable to the information it will be storing. Also, C includes a number of special operators that permit the creation of very efficient routines. Both of these items are the subject of this chapter.

---

### Review Skills Check

Before proceeding, you should be able to answer these questions and perform these exercises:

1. Write a program that uses an array of structures to hold the squares and cubes of the numbers 1 through 10. Display the contents of the array.
2. Write a program that uses a union to display as a character the individual bytes that make up a short integer entered by the user.
3. What does this fragment display? (Assume two-byte ints and eight-byte doubles.)
```c
union {
    int i;
    double d;
} uvar;

printf("%d", sizeof uvar);
```
4. What is wrong with this fragment?
```c
struct {
    int i;
    char str[80];
    double balance;
} svar;

svar->i = 100;
```
5. What is a bit-field?

---

## 11.1 USE THE STORAGE CLASS SPECIFIERS

C defines four type modifiers that affect how a variable is stored. They are

```c
auto
extern
register
static
```

These specifiers precede the type name. Let's look at each now.

The specifier `auto` is completely unnecessary. It is provided in C to allow compatibility with its predecessor, B. (Its use is to declare *automatic variables*. Automatic variables are simply local variables, which are `auto` by default. You will almost never see `auto` used in any C program.)

Although the programs we have been working with in this book are fairly short, programs in the real world tend to be quite long. As the size of a program grows, it takes longer to compile. For this reason, C allows you to break a program into two or more files. You can separately compile these files and then link them together. This saves compilation time and makes your projects easier to work with. (The actual method of separate compilation and linking will be explained in the instructions that accompany your compiler.) When working with multiple source files there is, however, one issue that needs to be addressed. As a general rule, global data can only be defined once. However, global data may need to be accessed by two or more files that form a program. In this case, each source file must inform the compiler about the global data it uses. To accomplish this you will need to use the keyword `extern`. To understand why, consider the following program, which is split between two files:

FILE #1:
```c
#include <stdio.h>

int count;

void f1(void);

int main(void)
{
    int i;

    f1(); /* set count's value */

    for(i=0; i<count; i++)
        printf("%d ", i);

    return 0;
}
```

FILE #2:
```c
#include <stdlib.h>

void f1(void)
{
    count = rand();
}
```

If you try to compile the second file, an error will be reported because `count` is not defined. However, you cannot change FILE #2 as follows:

```c
#include <stdlib.h>

int count;

void f1(void)
{
    count = rand();
}
```

If you declare `count` a second time, many linkers will report a duplicate-symbol error, which means that `count` is defined twice, and the linker doesn't know which to use.

The solution to this problem is C's `extern` specifier. By placing `extern` in front of `count`'s declaration in FILE #2, you are telling the compiler that `count` is an integer defined elsewhere. In other words, using `extern` informs the compiler about the existence and the type of the variable it precedes, but it does not cause storage for that variable to be allocated. The correct version of FILE #2 is

```c
#include <stdlib.h>

extern int count;

void f1(void)
{
    count = rand();
}
```

Although rarely done, it is not incorrect to use `extern` inside a function to declare a global variable defined elsewhere in the same file. For example, the following is valid:

```c
#include <stdio.h>

int count;

int main(void)
{
    extern int count; /* this refers to global count */

    count = 10;
    printf("%d", count);

    return 0;
}
```

The reason you will rarely see this use of `extern` is that it is redundant. Whenever the compiler encounters a variable name not defined by the function as a local variable, it assumes that it is global.

One very important storage-class specifier is `register`. When you specify a register variable you are telling the compiler that you want access to that variable to be as fast as possible. In early versions of C, `register` could only be applied to local variables (including formal parameters) of types **int** or **char**, or to a pointer type. It caused the variables to be held in a register of the CPU. (This is how the name register came about.) By using a register of the CPU, extremely fast access times are achieved. In modern versions of C, the definition of `register` has been broadened to include all types of variables and the requirement that register variables must be held in a CPU register was removed. Instead, the ANSI C standard stipulates that a `register` variable will be stored in such a way as to minimize access time. In practice, however, this means that `register` variables of type **int** and **char** continue to be held in a CPU register—this is still the fastest way to access them.

No matter what storage method is used, only so many variables can be granted the fastest possible access time. For example, the CPU has a limited number of registers. When fast-access locations are exhausted, the compiler is free to make `register` variables into regular variables. For this reason, you must choose carefully which variables you modify with `register`.

One good choice is to make a frequently used variable, such as the variable that controls a loop, into a register variable. The more times a variable is accessed, the greater the increase in performance when its access time is decreased. Generally, you can assume that at least two variables per function can be truly optimized for access speed.

> [!IMPORTANT]
> Because a register variable may be stored in a register of the CPU, it may not have a memory address. This means that you cannot use the `&` to find the address of a register variable.

When you use the `static` modifier, you cause the contents of a local variable to be preserved between function calls. Also, unlike normal local variables, which are initialized each time a function is entered, a `static` local variable is initialized only once. For example, take a look at this program:

```c
#include <stdio.h>

void f(void);

int main(void)
{
    int i;

    for(i=0; i<10; i++) f();

    return 0;
}

void f(void)
{
    static int count = 0;

    count++;
    printf("count is %d\n", count);
}
```

which displays the following output:

```
count is 1
count is 2
count is 3
count is 4
count is 5
count is 6
count is 7
count is 8
count is 9
count is 10
```

As you can see, `count` retains its value between function calls. The advantage to using a static local variable over a global one is that the static local variable is still known to and accessible by only the function in which it is declared.

The `static` modifier may also be used on global variables. When it is, it causes the global variable to be known to and accessible by only the functions in the same file in which it is declared. Not only is a function not declared in the same file as a `static` global variable unable to access that global variable, it does not even know its name. This means that there are no name conflicts if a static global variable in one file has the same name as another global variable in a different file of the same program. For example, consider these two fragments, which are parts of the same program:

FILE #1:
```c
int count;
.
.
.
count = 10;
printf("%d", count);
```

FILE #2:
```c
static int count;
.
.
.
count = 5;
printf("%d", count);
```

Because `count` is declared as static in FILE #2, no name conflicts arise. The `printf()` statement in FILE #1 displays 10 and the `printf()` statement in FILE #2 displays 5 because the two counts are different variables.

### EXAMPLES

1. To get an idea about how much faster access to a `register` variable is, try the following program. It makes use of another of C's standard library functions called `clock()`, which returns the number of system clock ticks since the program began execution. It has this prototype:

```c
clock_t clock(void);
```

It uses the TIME.H header. TIME.H also defines the `clock_t` type, which is more or less the same as **long**. To time an event using `clock()`, call it immediately before the event you wish to time and save its return value. Next, call it a second time after the event finishes and subtract the starting value from the ending value. This is the approach used by the program to time how long it takes two loops to execute. One set of loops is controlled by a `register` variable, the other is controlled by a non-register variable.

```c
#include <stdio.h>
#include <time.h>

int i; /* This will not be transformed into a
          register variable because it is global. */

int main(void)
{
    register int j;
    int k;
    clock_t start, finish;

    start = clock();
    for(k=0; k<100; k++)
        for(i=0; i<32000; i++) ;
    finish = clock();
    printf("Non-register loop: %ld ticks\n", finish - start);

    start = clock();
    for(k=0; k<100; k++)
        for(j=0; j<32000; j++) ;
    finish = clock();
    printf("Register loop: %ld ticks\n", finish - start);

    return 0;
}
```

For most compilers, the register-controlled loop will execute about twice as fast as the non-register controlled loop.

The non-register variable is global because, when feasible, virtually all compilers will automatically convert local variables not specified as register types into register types as an automatic optimization. If you do not see the predicted results, it may mean that the compiler has automatically optimized `i` into a register variable, too. Although you can't declare global variables as `register`, there is nothing that prevents a compiler from optimizing your program to this effect. If you don't see much difference between the two loops, try creating extra global variables prior to `i` so that it will not be automatically optimized.

2. As you know, the compiler can optimize access speed for only a limited number of register variables in any one function (perhaps as few as two). However, this does not mean that your program can only have a few register variables. Because of the way a C program executes, each function may utilize the maximum number of `register` variables. For example, for the average compiler, all the variables shown in the next program will be optimized for speed:

```c
#include <stdio.h>

void f2(void);
void f(void);

int main(void)
{
    register int a, b;
    .
    .
    .
}

void f(void)
{
    register int i, j;
    .
    .
    .
}

void f2(void)
{
    register int j, k;
    .
    .
    .
}
```

3. Local static variables have several uses. One is to allow a function to perform various initializations only once, when it is first called. For example, consider this function:

```c
void myfunc(void)
{
    static int first = 1;

    if(first) { /* initialize the system */
        rewind(fp);
        a = 0;
        loc = 0;
        fprintf("System Initialized");
        first = 0;
    }
    .
    .
    .
}
```

Because `first` is static, it will hold its value between calls. Thus, the initialization code will be executed only the first time the function is called.

4. Another interesting use for a local static variable is to control a recursive function. For example, this program prints the numbers 1 through 9 on the screen:

```c
#include <stdio.h>

void f(void);

int main(void)
{
    f();

    return 0;
}

void f(void)
{
    static int stop=0;

    stop++;

    if(stop==10) return;
    printf("%d ", stop);
    f(); /* recursive call */
}
```

Notice how `stop` is used to prevent a recursive call to `f()` when it equals 10.

5. Here is another example of using `extern` to allow global data to be accessed by two files:

FILE #1:
```c
#include <stdio.h>

char str[80];

void getname(void);

int main(void)
{
    getname();
    printf("Hello %s", str);

    return 0;
}
```

FILE #2:
```c
#include <stdio.h>

extern char str[80];

void getname(void)
{
    printf("Enter your first name: ");
    gets(str);
}
```

### EXERCISES

1. Assume that your compiler will actually optimize access time of only two `register` variables per function. In this program, which two variables are the best ones to be made into `register` variables?

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    int i, j, k, m;

    do {
        printf("Enter a value: ");
        scanf("%d", &i);

        m = 0;
        for(j=0; j<i; j++)
            for(k=0; k<100; k++)
                m = k + m;
    } while(i>0);

    return 0;
}
```

2. Write a program that contains a function called `sum_it()` that has this prototype:

```c
void sum_it(int value);
```

Have this function use a local static integer variable to maintain and display a running total of the values of the parameters it is called with. For example, if `sum_it()` is called three times with the values 3, 6, 4, then `sum_it()` will display 3, 9, and 13.
3. Try the program described in Example 5. Be sure to actually use two files. If you are unsure how to compile and link a program consisting of two files, check your compiler's user manual.
4. What is wrong with this fragment?

```c
register int i;
int *p;

p = &i;
```

---

## 11.2 USE THE ACCESS MODIFIERS

C includes two type modifiers that affect the way variables are accessed by both your program and the compiler. These modifiers are `const` and `volatile`. This section examines these type modifiers.

If you precede a variable's type with `const`, you prevent that variable from being modified by your program. The variable may be given an initial value, however, through the use of an initialization when it is declared. The compiler is free to locate `const` variables in ROM (read-only memory) in environments that support it. A `const` variable may also have its value changed by hardware-dependent means.

The `const` modifier has a second use. It can prevent a function from modifying the object that a parameter points to. That is, when a pointer parameter is preceded by `const`, no statement in the function can modify the variable pointed to by that parameter.

When you precede a variable's type with `volatile`, you are telling the compiler that the value of the variable may be changed in ways not explicitly defined in the program. For example, a variable's address might be given to an interrupt service routine, and its value changed each time an interrupt occurs. The reason that `volatile` is important is that most C compilers apply complex and sophisticated optimizations to your program to create faster and more efficient executable programs. If the compiler does not know that the contents of a variable may change in ways not explicitly specified by the program, it may not actually examine the contents of the variable each time it is referenced. (Unless it occurs on the left side of an assignment statement, of course.)

### EXAMPLES

1. The following short program shows how a `const` variable can be given an initial value and be used in the program, as long as it is not on the left side of an assignment statement.

```c
#include <stdio.h>

int main(void)
{
    const int i = 10;

    printf("%d", i); /* this is OK */

    return 0;
}
```

The following program tries to assign `i` another value. This program will not compile because `i` cannot be modified by the program.

```c
#include <stdio.h>

int main(void)
{
    const int i = 10;

    i = 20; /* this is wrong */

    printf("%d", i);

    return 0;
}
```

2. The next program shows how a pointer parameter can be declared as `const` to prevent the object it points to from being modified.

```c
#include <stdio.h>

void pr_str(const char *p);

int main(void)
{
    char str[80];

    printf("Enter a string: ");
    gets(str);

    pr_str(str);

    return 0;
}

void pr_str(const char *p)
{
    while(*p) putchar(*p++); /* this is ok */
}
```

If you change the program as shown below, it will not compile because this version attempts to alter the string pointed to by `p`.

```c
#include <stdio.h>
#include <ctype.h>

void pr_str(const char *p);

int main(void)
{
    char str[80];

    printf("Enter a string: ");
    gets(str);

    pr_str(str);

    return 0;
}

void pr_str(const char *p)
{
    while(*p) {
        *p = toupper(*p); /* this will not compile */
        putchar(*p++);
    }
}
```

3. Perhaps the most important feature of `const` pointer parameters is that they guarantee that many standard library functions will not modify the variables pointed to by their parameters. For example, here is the actual prototype to `strlen()` specified by the ANSI standard:

```c
size_t strlen(const char *str);
```

Since *str* is specified as `const`, the string it points to cannot be changed.

4. While short examples of `volatile` are hard to find, the following fragment gives you the flavor of its use:

```c
volatile unsigned u;

give_address_to_some_interrupt(&u);

for(;;) { /* watch value of u */
    printf("%d", u);
    .
    .
    .
}
```

In this example, if `u` had not been declared as `volatile`, the compiler could have optimized the repeated calls to `printf()` in such a way that `u` was not reexamined each time. The use of `volatile` forces the compiler to actually obtain the value of `u` whenever it is used.

### EXERCISES

1. One good time to use `const` is when you want to embed a version control number into a program. By using a `const` variable to hold the version, you prevent it from accidentally being changed. Write a short program that illustrates how this can be done. Use 6.01 as the version number.
2. Write your own version of `strcpy()` called `mystrcpy()`, which has the prototype

```c
char *mystrcpy(char *to, const char *from);
```

The function returns a pointer to *to*. Demonstrate your version of `mystrcpy()` in a program.
3. On your own, see if you can think of any ways to use `volatile`.

---

## 11.3 DEFINE ENUMERATIONS

In C you can define a list of named integer constants called an *enumeration*. These constants can then be used any place an integer can. To define an enumeration, use this general form:

```c
enum tag-name { enumeration list } variable-list;
```

Either the *tag-name* or the *variable-list* is optional. The *tag-name* is essentially the type name of the enumeration. For example,

```c
enum color_type {red, green, yellow} color;
```

Here, an enumeration consisting of the constants `red`, `green`, and `yellow` is created. The enumeration tag is `color_type` and one variable, called `color`, has been created.

By default, the compiler assigns integer values to enumeration constants, beginning with 0 at the far left side of the list. Each constant to the right is one greater than the constant that precedes it. Therefore, in the color enumeration, `red` is 0, `green` is 1, and `yellow` is 2. However, you can override the compiler's default values by explicitly giving a constant a value. For example, in this statement

```c
enum color_type {red, green=9, yellow} color;
```

`red` is still 0, but `green` is 9, and `yellow` is 10.

Once you have defined an enumeration, you can use its tag name to declare enumeration variables at other points in the program. For example, assuming the `color_type` enumeration, this statement is perfectly valid and declares `mycolor` as a `color_type` variable:

```c
enum color_type mycolor;
```

An enumeration is essentially an integer type and an enumeration variable can hold any integer value—not just those defined by the enumeration. But for clarity and structure, you should use enumeration variables to hold only values that are defined by their enumeration type.

Two of the main uses of an enumeration are to help provide self-documenting code and to clarify the structure of your program.

### EXAMPLES

1. This short program creates an enumeration consisting of the parts of a computer. It assigns `comp` the value `CPU` and then displays its value (which is 1). Notice how the enumeration tag name is used to declare `comp` as an enumeration variable separately from the actual declaration of `computer`.

```c
#include <stdio.h>

enum computer {keyboard, CPU, screen, printer};

int main(void)
{
    enum computer comp;

    comp = CPU;

    printf("%d", comp);

    return 0;
}
```

2. It takes a little work to display the string equivalent of an enumerated constant. Remember, enumerated constants are not strings; they are named integer constants. The following program uses a `switch` statement to output the string equivalent of an enumerated value. The program uses C's random-number generator to choose a means of transportation. It then displays the means on the screen. (This program is for people who can't make up their minds!)

```c
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

enum transport {car, train, airplane, bus} tp;

int main(void)
{
    printf("Press a key to select transport: ");

    /* generate a new random number each time
       the program is run */
    while(!kbhit()) rand();
    getch(); /* read and discard character */

    tp = rand() % 4;
    switch(tp) {
        case car: printf("car");
            break;
        case train: printf("train");
            break;
        case airplane: printf("airplane");
            break;
        case bus: printf("bus");
    }

    return 0;
}
```

In some cases, there is an easier way to obtain a string equivalent of an enumerated value. As long as you do not initialize any of the constants, you can create a two-dimensional string array that contains the string equivalents of the enumerated values in the same order that the constants appear in the enumeration. You can then index the array using an enumeration value to obtain its corresponding string. The following version of the transportation-choosing program, for example, uses this approach:

```c
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

enum transport {car, train, airplane, bus} tp;

char trans[][20] = {
    "car", "train", "airplane", "bus"
};

int main(void)
{
    printf("Press a key to select transport: ");

    /* Generate a new random number each time
       the program is run */
    while(!kbhit()) rand();
    getch(); /* read and discard character */

    tp = rand() % 4;
    printf("%s", trans[tp]);

    return 0;
}
```

3. Remember, the names of enumerated constants are known only to the program, not to any library functions. For example, given the fragment

```c
enum numbers {zero, one, two, three} num;

printf("Enter a number: ");
scanf("%d", &num);
```

you cannot respond to `scanf()` by entering `one`.

### EXERCISES

1. Compile and run the example programs.
2. Create an enumeration of the coins of the U.S. from penny to dollar.
3. Is this fragment correct? If not, why not?
```c
enum cars {Ford, Chrysler, GM} make;

make = GM;
printf("car is %s", make);
```

---

## 11.4 UNDERSTAND typedef

In C you can create a new name for an existing type using `typedef`. The general form of `typedef` is

```c
typedef old-name new-name;
```

This new name can be used to declare variables. For example, in the following program, `smallint` is a new name for a `signed char` and is used to declare `i`.

```c
#include <stdio.h>

typedef signed char smallint;

int main(void)
{
    smallint i;

    for(i=0; i<10; i++)
        printf("%d ", i);

    return 0;
}
```

Keep two points firmly in mind: First, a `typedef` does not cause the original name to be deactivated. For example, in the program, `signed char` is still a valid type. Second, you can use several `typedef` statements to create many different, new names for the same type.

There are basically two reasons to use `typedef`. The first is to create portable programs. For example, if you know that you will be writing a program that will be executed on computers using 16-bit integers as well as on computers using 32-bit integers, and you want to ensure that certain variables are 16 bits long in both environments, you might want to use a `typedef` when compiling the program for the 16-bit machines as follows:

```c
typedef int myint;
```

Then, before compiling the code for a 32-bit computer, you can change the `typedef` statement like this:

```c
typedef short int myint;
```

This works because on computers using 32-bit integers, a **short int** will be 16 bits long. Assuming that you used `myint` to declare all integer values that you wanted to be 16 bits long, you need change only one statement to change the type of all variables declared using `myint`.

The second reason you might want to use `typedef` is to help provide self-documenting code. For example, if you are writing an inventory program, you might use this `typedef` statement.

```c
typedef double subtotal;
```

Now, when anyone reading your program sees a variable declared as `subtotal`, he or she will know that it is used to hold a subtotal.

### EXAMPLES

1. The new name created by one `typedef` can be used in a subsequent `typedef` to create another name. For example, consider this fragment:

```c
typedef int height;
typedef height length;
typedef length depth;

depth d;
```

Here, `d` is still an integer.

2. In addition to the basic types, you can use `typedef` on more complicated types. For example, the following is perfectly valid:

```c
enum e_type {one, two, three};

typedef enum e_type mynums;

mynums num; /* declare a variable */
```

Here, `num` is a variable of type `e_type`.

### EXERCISES

1. Show how to make `UL` a new name for `unsigned long`. Show that it works by writing a short program that declares a variable using `UL`, assigns it a value, and displays the value on the screen.
2. What is wrong with this fragment?
```c
typedef balance float;
```

---

## 11.5 USE C'S BITWISE OPERATORS

C contains four special operators that perform their operations on a bit-by-bit level. These operators are

| Operator | Meaning |
| :--- | :--- |
| `&` | bitwise AND |
| `\|` | bitwise OR |
| `^` | bitwise XOR (eXclusive OR) |
| `~` | 1's complement |

These operators work with character and integer types; they cannot be used with floating-point types.

The AND, OR, and XOR operators produce a result based on a comparison of corresponding bits in each operand. The AND operator sets a bit if both bits being compared are set. The OR sets a bit if either of the bits being compared is set. The XOR operation sets a bit when either of the two bits involved is 1, but not when both are 1 or both are 0. Here is an example of a bitwise AND:

```
  1010 0110
& 0011 1011
------------
  0010 0010
```

Notice how the resulting bit is set, based on the outcome of the operation being applied to the corresponding bits in each operand.

The 1's complement operator is a unary operator that reverses the state of each bit within an integer or character.

### EXAMPLES

1. The XOR operation has one interesting property. Given two values A and B, when the outcome of A XOR B is XORed with B a second time, A is produced. For example, this output

```
initial value of i: 100
i after first XOR: 21895
i after second XOR: 100
```

is produced by the following program:

```c
#include <stdio.h>

int main(void)
{
    int i;

    i = 100;
    printf("initial value of i: %d\n", i);

    i = i ^ 21987;
    printf("i after first XOR: %d\n", i);

    i = i ^ 21987;
    printf("i after second XOR: %d\n", i);

    return 0;
}
```

2. The following program uses a bitwise AND to display, in binary, the ASCII value of a character typed at the keyboard:

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;
    int i;

    printf("Enter a character: ");
    ch = getche();
    printf("\n");

    /* display binary representation */
    for(i=128; i>0; i=i/2)
        if(i & ch) printf("1 ");
        else printf("0 ");

    return 0;
}
```

The program works by adjusting the value of `i` so that only one bit is set each time a comparison is made. Since the high-order bit in a byte represents 128, this value is used as a starting point. Each time through the loop, `i` is halved. This causes the next bit position to be set and all others cleared. Thus, each time through the loop, a bit in `ch` is tested. If it is 1, the comparison produces a true result and a **1** is output. Otherwise a **0** is displayed. This process continues until all bits have been tested.

3. By modifying the program from Example 2, it can be used to show the effect of the 1's complement operator.

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;
    int i;

    ch = 'a';

    /* display binary representation */
    for(i=128; i>0; i=i/2)
        if(i & ch) printf("1 ");
        else printf("0 ");

    /* reverse bit pattern */
    ch = ~ch;
    printf("\n");

    /* display binary representation */
    for(i=128; i>0; i=i/2)
        if(i & ch) printf("1 ");
        else printf("0 ");

    return 0;
}
```

When you run this program, you will see that the state of bits in `ch` are reversed after the `~` operation has occurred.

4. The following program shows how to use the `&` operator to determine if a signed integer is positive or negative. (The program assumes short integers are 16 bits long.) Since negative numbers are represented with their high-order bit set, the comparison will be true only if `i` is negative. (The value 32768 is the value of an unsigned short integer when only its high-order bit is set. This value is 1000 0000 in binary.)

```c
#include <stdio.h>

int main(void)
{
    short i;

    printf("Enter a number: ");
    scanf("%hd", &i);

    if(i & 32768) printf("Number is negative.\n");

    return 0;
}
```

5. The following program makes `i` into a negative number by setting its high-order bit. (Again, 16-bit short integers are assumed.)

```c
#include <stdio.h>

int main(void)
{
    short i;

    i = 1;
    i = i | 32768;
    printf("%hd", i);

    return 0;
}
```

It displays **-32,767**.

### EXERCISES

1. One very easy way to encode a file is to reverse the state of each bit using the `~` operator. Write a program that encodes a file using this method. (To decode the file, simply run the program a second time.) Have the user specify the name of the file on the command line.
2. A better method of coding a file uses the XOR operation combined with a user-defined key. Write a program that encodes a file using this method. Have the user specify the file to code as well as a single character key on the command line. (To decode the file, run the program a second time using the same key.)
3. What is the outcome of these operations?
   A. 1010 0011 & 0101 1101
   B. 0101 1101 | 1111 1011
   C. 0101 0110 ^ 1010 1011
4. Sometimes, the high-order bit of a byte is used as a *parity bit* by modem programs. It is used to verify the integrity of each byte transferred. There are two types of parity: even and odd. If even parity is used, the parity bit is used to ensure that each byte has an even number of 1 bits. If odd parity is used, the parity bit is used to ensure that each byte has an odd number of 1 bits. Since the parity bit is not part of the information being transferred, show how you can clear the high-order bit of a character value.

---

## 11.6 MASTER THE SHIFT OPERATORS

C includes two operators not commonly found in other computer languages: the left and right bit-shift operators. The left shift operator is `<<`, and the right shift operator is `>>`. These operators may be applied only to character or integer operands. They take these general forms:

```c
value << number-of-bits;
value >> number-of-bits;
```

The integer expression specified by *number-of-bits* determines how many places to the left or right the bits within *value* are shifted. Each left-shift causes all bits within the specified value to be shifted left one position and a zero is brought in on the right. A right-shift shifts all bits to the right one position and brings a zero in on the left. (Unless the number is negative, in which case a one is brought in.) When bits are shifted off an end, they are lost.

A right shift is equivalent to dividing a number by 2, and a left shift is the same as multiplying the number by 2. Because of the internal operation of virtually all CPUs, shift operations are usually faster than their equivalent arithmetic operations.

### EXAMPLES

1. This program demonstrates the right and left shift operators:

```c
#include <stdio.h>

void show_binary(unsigned u);

int main(void)
{
    unsigned short u;

    u = 45678;

    show_binary(u);
    u = u << 1;
    show_binary(u);
    u = u >> 1;
    show_binary(u);

    return 0;
}

void show_binary(unsigned u)
{
    unsigned n;

    for(n=32768; n>0; n=n/2)
        if(u & n) printf("1 ");
        else printf("0 ");

    printf("\n");
}
```

The output from this program is

```
1 0 1 1 0 0 1 0 0 1 1 0 1 1 1 0
0 1 1 0 0 1 0 0 1 1 0 1 1 1 0 0
0 0 1 1 0 0 1 0 0 1 1 0 1 1 1 0
```

Notice that after the left shift, a bit of information has been lost. When the right shift occurs, a zero is brought in. As stated earlier, bits that are shifted off one end are lost.

2. Since a right shift is the same as a division by two, but faster, the `show_binary()` function can be made more efficient as shown here:

```c
void show_binary(unsigned u)
{
    unsigned n;

    for(n=32768; n; n=n>>1)
        if(u & n) printf("1 ");
        else printf("0 ");

    printf("\n");
}
```

### EXERCISES

1. Write a program that uses the shift operators to multiply and divide an integer. Have the user enter the initial value. Display the result of each operation.
2. C does not have a rotate operator. A *rotate* is similar to a shift, except that the bit shifted off one end is inserted onto the other. For example, 1010 0000 rotated left one place is 0100 0001. Write a function called `rotate()` that rotates a byte left one position each time it is called. (Hint, you will need to use a union so that you can have access to the bit shifted off the end of the byte.) Demonstrate the function in a program.

---

## 11.7 UNDERSTAND THE ? OPERATOR

C contains one ternary operator: the `?`. A ternary operator requires three operands. The `?` operator is used to replace statements such as:

```c
if(condition) var = exp1;
else var = exp2;
```

The general form of the `?` operator is

```c
var = condition ? exp1 : exp2;
```

Here, *condition* is an expression that evaluates to true or false. If it is true, *var* is assigned the value of *exp1*. If it is false, *var* is assigned the value of *exp2*. The reason for the `?` operator is that a C compiler can produce more efficient code using it instead of the equivalent `if`/`else` statement.

### EXAMPLES

1. The following program illustrates the `?` operator. It inputs a number and then converts the number into 1 if the number is positive and -1 if it is negative.

```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter a number: ");
    scanf("%d", &i);

    i = i>0 ? 1 : -1;

    printf("Outcome: %d", i);

    return 0;
}
```

2. The next program is a computerized coin toss. It waits for you to press a key and then prints either **Heads** or **Tails**.

```c
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main(void)
{
    int i;

    while(!kbhit()) rand();

    i = rand() % 2 ? 1 : 0;

    if(i) printf("Heads");
    else printf("Tails");

    return 0;
}
```

The coin-toss program can be written in a more efficient way. There is no technical reason that the `?` operator need assign its value to any variable. Therefore, the coin toss program can be written as:

```c
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main(void)
{
    while(!kbhit()) rand();

    rand()%2 ? printf("Heads") : printf("Tails");

    return 0;
}
```

Remember, since a call to a function is a valid C expression, it is perfectly valid to call `printf()` in the `?` statement.

### EXERCISES

1. One particularly good use for the `?` operator is to provide a means of preventing a division-by-zero error. Write a program that inputs two integers from the user and displays the result of dividing the first by the second. Use `?` to avoid division by zero.
2. Convert the following statement into its equivalent `?` statement.
```c
if(a>b) count = 100;
else count = 0;
```

---

## 11.8 DO MORE WITH THE ASSIGNMENT OPERATOR

The assignment operator is more powerful in C than in most other computer languages. In this section, you will learn some new things about it.

You can assign several variables the same value using the general form

```c
var1 = var2 = var3 = ... = varN = value;
```

For example, this statement

```c
i = j = k = 100;
```

assigns `i`, `j`, and `k` the value 100. In professionally written C code, it is common to see such multiple-variable assignments.

Another variation on the assignment statement is sometimes called *C shorthand*. In C, you can transform a statement like

```c
a = a + 3;
```

into a statement like

```c
a += 3;
```

In general, any time you have a statement of the form

```c
var = var op expression;
```

you can write it in shorthand form as

```c
var op= expression;
```

Here, *op* is one of the following operators.

```
+ - * / % << >> & | ^
```

There must be no space between the operator and the equal sign. The reason you will want to use the shorthand form is not that it saves you a little typing effort, but because the C compiler can create more efficient executable code.

### EXAMPLES

1. The following program illustrates the multiple-assignment statement:

```c
#include <stdio.h>

int main(void)
{
    int i, j, k;

    i = j = k = 99;

    printf("%d %d %d", i, j, k);

    return 0;
}
```

2. The next program counts to 98 by twos. Notice that it uses C shorthand to increment the loop-control variable by two each iteration.

```c
#include <stdio.h>

int main(void)
{
    int i;

    /* count by 2s */
    for(i=0; i<100; i+=2)
        printf("%d ", i);

    return 0;
}
```

3. The following program uses the left-shift operator in shorthand form to multiply the value of `i` by 2, three times. (The resulting value is 8.)

```c
#include <stdio.h>

int main(void)
{
    int i = 1;

    i <<= 3; /* multiply by 2, 3 times */

    printf("%d", i);

    return 0;
}
```

### EXERCISES

1. Compile and run the program in Example 1 to prove to yourself that the multiple-assignment statement works.
2. How is the following statement written using C shorthand?
```c
x = x & y;
```
3. Write a program that displays all the even multiples of 17 from 17 to 1000. Use C shorthand.

---

## 11.9 UNDERSTAND THE COMMA OPERATOR

The last operator we will examine is the comma. It has a very unique function: it tells the compiler to "do this and this and this." That is, the comma is used to string together several operations. The most common use of the comma is in the `for` loop. In the following loop, the comma is used in the initialization portion to initialize two loop-control variables, and in the increment portion to increment `i` and `j`.

```c
for(i=0, j=0; i+j<count; i++, j++) . . .
```

The value of a comma-separated list of expressions is the rightmost expression. For example, the following statement assigns 100 to `value`:

```c
value = (count, 99, 33, 100);
```

The parentheses are necessary because the comma operator is lower in precedence than the assignment operator.

### EXAMPLES

1. This program displays the numbers 0 through 49. It uses the comma operator to maintain two loop-control variables.

```c
#include <stdio.h>

int main(void)
{
    int i, j;

    /* count to 49 */
    for(i=0, j=100; i<j; i++, j--)
        printf("%d ", i);

    return 0;
}
```

2. In many places in C, it is actually syntactically correct to use the comma in place of the semicolon. For example, examine the following short program:

```c
#include <stdio.h>

int main(void)
{
    char ch;

    ch = getchar(), /* notice the comma here */
    putchar(ch+1);

    return 0;
}
```

Because the comma tells the compiler to "do this and this," the program runs the same with the comma after `getchar()` as it would had a semicolon been used. Using a comma in this way is considered extremely bad form, however. It is possible that an unwanted side effect could occur. (This use of the comma operator *does* make interesting coffee-break conversation, however! Many C programmers are not aware of this interesting twist in the C syntax.)

### EXERCISES

1. Write a program that uses the comma operator to maintain three for loop-control variables. Have one variable run from 0 to 99, the second run from -50 to 49, and have the third set to the sum of the first two, both initially and each time the loop iterates. Have the loop stop when the first variable reaches 100. Have the program display the value of the third variable each time the loop repeats.
2. What is the value of `i` after the following statement executes?
```c
i = (1, 2, 3);
```

---

## 11.10 KNOW THE PRECEDENCE SUMMARY

The following table shows the precedence of all the C operators.

```
Highest   ( )  [ ]  ->  .
          !  ~  +  -  ++  --  (type cast)  *  &  sizeof
          *  /  %
          +  -
          <<  >>
          <  <=  >  >=
          ==  !=
          &
          ^
          |
          &&
          ||
          ?:
          =  +=  -=  *=  /=  etc.
Lowest    ,
```

---

## Mastery Skills Check

At this point you should be able to answer these questions and perform these exercises:

1. What does the `register` specifier do?
2. What do the `const` and `volatile` modifiers do?
3. Write a program that sums the numbers 1 to 100. Make the program execute as fast as possible.
4. Is this statement valid? If so, what does it do?
```c
typedef long double bigfloat;
```
5. Write a program that inputs two characters and compares corresponding bits. Have the program display the number of each bit in which a match occurs. For example, if the two integers are
```
1001 0110
1110 1010
```
the program will report that bits 7, 1, and 0 match. (Use the bitwise operators to solve this problem.)
6. What do the `<<` and `>>` operators do?
7. Show how this statement can be rewritten:
```c
c = c + 10;
```
8. Rewrite this statement using the `?` operator:
```c
if(!done) count = 100;
else count = 0;
```
9. What is an enumeration? Show an example that enumerates the planets.

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. Write a program that swaps the low-order four bits of a byte with the high-order four bits. Demonstrate that your routine works by displaying the contents of the byte before and after, using the `show_binary()` function developed earlier. (Change `show_binary()` so that it works on an eight-bit quantity, however.)
2. Earlier you wrote a program that encoded files using the 1's complement operator. Write a program that reads a text file encoded using this method and displays its decoded contents. Leave the actual file encoded, however.
3. Is this fragment correct?
```c
register FILE *fp;
```
4. Using the program you developed for Chapter 10, Section 10.3, Exercise 1, optimize the program by selecting appropriate local variables to become register types.
