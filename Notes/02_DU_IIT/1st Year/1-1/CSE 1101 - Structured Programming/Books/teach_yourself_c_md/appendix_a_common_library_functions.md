# Appendix A: Some Common C Library Functions

THIS appendix discusses a number of the more frequently used ANSI C library functions. If you have looked through the library section in your C/C++ compiler's documentation, you are no doubt aware that there are a great many library functions. It is far beyond the scope of this book to cover each one. However, the ones you will most commonly need are discussed here. The library functions can be grouped into the following categories:

- I/O functions
- String and character functions
- Mathematics functions
- Time and date functions
- Dynamic allocation functions
- Miscellaneous functions

The I/O functions were thoroughly covered in Chapters 8 and 9 and will not be expanded upon here.

Each function's description begins with the header file required by the function followed by its prototype. The prototype provides you with a quick way of knowing what types of arguments and how many of them the function takes and what type of value it returns.

Keep in mind that ANSI C specifies many data types, which are defined in the header files used by the functions. New type names will be discussed as they are introduced.

---

## A.1 STRING AND CHARACTER FUNCTIONS

The C standard library has a rich and varied set of string- and character-handling functions. In C, a string is a null-terminated array of characters. The declarations for the string functions are found in the header file STRING.H. The character functions use CTYPE.H as their header file.

Because C has no bounds-checking on array operations, it is the programmer's responsibility to prevent an array overflow.

The character functions are declared with an integer parameter. While this is true, only the low-order byte is used by the function. Generally, you are free to use a character argument because it will automatically be elevated to **int** at the time of the call.

---

### isalnum

```c
#include <ctype.h>
int isalnum(int ch);
```

**Description**  
The `isalnum()` function returns nonzero if its argument is either a letter or a digit. If the character is not alphanumeric, then 0 is returned.

**Example**  
This program checks each character read from stdin and reports all alphanumeric ones:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch==' ') break;
        if(isalnum(ch)) printf("%c is alphanumeric\n", ch);
    }

    return 0;
}
```

---

### isalpha

```c
#include <ctype.h>
int isalpha(int ch);
```

**Description**  
The `isalpha()` function returns nonzero if `ch` is a letter of the alphabet; otherwise 0 is returned.

**Example**  
This program checks each character read from stdin and reports all those that are letters of the alphabet:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch==' ') break;
        if(isalpha(ch)) printf("%c is a letter\n", ch);
    }

    return 0;
}
```

---

### iscntrl

```c
#include <ctype.h>
int iscntrl(int ch);
```

**Description**  
The `iscntrl()` function returns nonzero if `ch` is between 0 and 0x1F or is equal to 0x7F (DEL); otherwise 0 is returned.

**Example**  
This program checks each character read from stdin and reports all control characters:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch==' ') break;
        if(iscntrl(ch))
            printf("%c is a control character\n", ch);
    }

    return 0;
}
```

---

### isdigit

```c
#include <ctype.h>
int isdigit(int ch);
```

**Description**  
The `isdigit()` function returns nonzero if `ch` is a digit (0 through 9); otherwise 0 is returned.

**Example**  
This program checks each character read from stdin and reports all those that are digits:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch==' ') break;
        if(isdigit(ch)) printf("%c is a digit\n", ch);
    }

    return 0;
}
```

---

### isgraph

```c
#include <ctype.h>
int isgraph(int ch);
```

**Description**  
The `isgraph()` function returns nonzero if `ch` is any printable character other than a space; otherwise 0 is returned. Printable characters are in the range 0x21 through 0x7E.

**Example**  
This program checks each character read from stdin and reports all printing characters:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch==' ') break;
        if(isgraph(ch))
            printf("%c is a printing character\n", ch);
    }

    return 0;
}
```

---

### islower

```c
#include <ctype.h>
int islower(int ch);
```

**Description**  
The `islower()` function returns nonzero if `ch` is a lowercase letter (a through z); otherwise 0 is returned.

**Example**  
This program checks each character read from stdin and reports all those that are lowercase letters:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch==' ') break;
        if(islower(ch)) printf("%c is lowercase\n", ch);
    }

    return 0;
}
```

---

### isprint

```c
#include <ctype.h>
int isprint(int ch);
```

**Description**  
The `isprint()` function returns nonzero if `ch` is a printable character, including a space; otherwise 0 is returned. Printable characters are often in the range 0x20 through 0x7E.

**Example**  
This program checks each character read from stdin and reports all those that are printable:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch=='Q') break;
        if(isprint(ch)) printf("%c is printable\n", ch);
    }

    return 0;
}
```

---

### ispunct

```c
#include <ctype.h>
int ispunct(int ch);
```

**Description**  
The `ispunct()` function returns nonzero if `ch` is a punctuation character, excluding the space; otherwise 0 is returned. The term "punctuation," as defined by this function, includes all printing characters that are neither alphanumeric nor a space.

**Example**  
This program checks each character read from stdin and reports all those that are punctuation:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch==' ') break;
        if(ispunct(ch)) printf("%c is punctuation\n", ch);
    }

    return 0;
}
```

---

### isspace

```c
#include <ctype.h>
int isspace(int ch);
```

**Description**  
The `isspace()` function returns nonzero if `ch` is either a space, tab, vertical tab, form feed, carriage return, or newline character; otherwise 0 is returned.

**Example**  
This program checks each character read from stdin and reports all those that are whitespace characters:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(isspace(ch)) printf("%c is whitespace\n", ch);
        if(ch==' ') break;
    }

    return 0;
}
```

---

### isupper

```c
#include <ctype.h>
int isupper(int ch);
```

**Description**  
The `isupper()` function returns nonzero if `ch` is an uppercase letter (A through Z); otherwise 0 is returned.

**Example**  
This program checks each character read from stdin and reports all those that are uppercase letters:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch==' ') break;
        if(isupper(ch)) printf("%c is uppercase\n", ch);
    }

    return 0;
}
```

---

### isxdigit

```c
#include <ctype.h>
int isxdigit(int ch);
```

**Description**  
The `isxdigit()` function returns nonzero if `ch` is a hexadecimal digit; otherwise 0 is returned. A hexadecimal digit will be in one of these ranges: A through F, a through f, or 0 through 9.

**Example**  
This program checks each character read from stdin and reports all those that are hexadecimal digits:

```c
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char ch;

    for(;;) {
        ch = getchar();
        if(ch==' ') break;
        if(isxdigit(ch)) printf("%c is hexadecimal \n", ch);
    }

    return 0;
}
```

---

### strcat

```c
#include <string.h>
char *strcat(char *str1, const char *str2);
```

**Description**  
The `strcat()` function concatenates a copy of `str2` to `str1` and terminates `str1` with a null. The null terminator originally ending `str1` is overwritten by the first character of `str2`. The string `str2` is untouched by the operation. The `strcat()` function returns `str1`.

> [!NOTE]
> *Remember*: No bounds-checking takes place, so it is the programmer's responsibility to ensure that `str1` is large enough to hold both its original contents and those of `str2`.

**Example**  
This program appends the first string read from stdin to the second. For example, assuming the user enters **hello** and **there**, the program will print **therehello**.

```c
#include <string.h>
#include <stdio.h>

int main(void)
{
    char s1[80], s2[80];

    printf("Enter two strings: ");
    gets(s1);
    gets(s2);

    strcat(s2, s1);
    printf(s2);

    return 0;
}
```

---

### strchr

```c
#include <string.h>
char *strchr(const char *str, int ch);
```

**Description**  
The `strchr()` function returns a pointer to the first occurrence of the low-order byte of `ch` in the string pointed to by `str`. If no match is found, a null pointer is returned.

**Example**  
This prints the string **is a test**:

```c
#include <string.h>
#include <stdio.h>

int main(void)
{
    char *p;

    p = strchr("this is a test", ' ');
    printf(p);

    return 0;
}
```

---

### strcmp

```c
#include <string.h>
int strcmp(const char *str1, const char *str2);
```

**Description**  
A `strcmp()` function lexicographically compares two null-terminated strings and returns an integer based on the outcome, as shown here:

| Result | Meaning |
| :--- | :--- |
| less than 0 | `str1` is less than `str2` |
| 0 | `str1` is equal to `str2` |
| greater than 0 | `str1` is greater than `str2` |

**Example**  
The following function can be used as a password verification routine. It will return 0 on failure and 1 on success.

```c
#include <string.h>
#include <stdio.h>

int password(void)
{
    char s[80];

    printf("Enter password: ");
    gets(s);

    if(strcmp(s, "pass")) {
        printf("Invalid Password\n");
        return 0;
    }
    return 1;
}
```

---

### strcpy

```c
#include <string.h>
char *strcpy(char *str1, const char *str2);
```

**Description**  
The `strcpy()` function is used to copy the contents of `str2` into `str1`; `str2` must be a pointer to a null-terminated string. The `strcpy()` function returns a pointer to `str1`.

If `str1` and `str2` overlap, the behavior of `strcpy()` is undefined.

**Example**  
The following code fragment will copy "hello" into string `str`:

```c
char str[80];
strcpy(str, "hello");
```

---

### strlen

```c
#include <string.h>
size_t strlen(const char *str);
```

**Description**  
The `strlen()` function returns the length of the null-terminated string pointed to by `str`. The null is not counted. The `size_t` type is defined in STRING.H.

**Example**  
The following code fragment will print 5 on the screen:

```c
strcpy(s, "hello");
printf("%d", strlen(s));
```

---

### strstr

```c
#include <string.h>
char *strstr(const char *str1, const char *str2);
```

**Description**  
The `strstr()` function returns a pointer to the first occurrence of the string pointed to by `str2` in the string pointed to by `str1` (except `str2`'s null terminator). It returns a null pointer if no match is found.

**Example**  
This program displays the message **is a test**:

```c
#include <string.h>
#include <stdio.h>

int main(void)
{
    char *p;

    p = strstr("this is a test", "is");
    printf(p);

    return 0;
}
```

---

### strtok

```c
#include <string.h>
char *strtok(char *str1, const char *str2);
```

**Description**  
The `strtok()` function returns a pointer to the next token in the string pointed to by `str1`. The characters making up the string pointed to by `str2` are the delimiters that separate each token. A null pointer is returned when there are no more tokens.

The first time `strtok()` is called, `str1` is actually used in the call. Subsequent calls use a null pointer for the first argument. In this way the entire string can be reduced to its tokens.

It is possible to use a different set of delimiters for each call to `strtok()`.

**Example**  
This program tokenizes the string "The summer soldier, the sunshine patriot" with spaces and commas as the delimiters. The output will be **The | summer | soldier | the | sunshine | patriot**.

```c
#include <string.h>
#include <stdio.h>

int main(void)
{
    char *p;

    p = strtok("The summer soldier, the sunshine patriot", " ,");

    printf(p);
    do {
        p = strtok('\0', ", ");
        if(p) printf("|%s", p);
    } while(p);

    return 0;
}
```

---

### tolower

```c
#include <ctype.h>
int tolower(int ch);
```

**Description**  
The `tolower()` function returns the lowercase equivalent of `ch` if `ch` is a letter; otherwise `ch` is returned unchanged.

**Example**  
This fragment displays **q**:

```c
putchar(tolower('Q'));
```

---

### toupper

```c
#include <ctype.h>
int toupper(int ch);
```

**Description**  
The `toupper()` function returns the uppercase equivalent of `ch` if `ch` is a letter; otherwise `ch` is returned unchanged.

**Example**  
This displays **A**:

```c
putchar(toupper('a'));
```

---

## A.2 THE MATHEMATICS FUNCTIONS

ANSI C defines several mathematics functions that take **double** arguments and return **double** values. These functions fall into the following categories:

- Trigonometric functions
- Hyperbolic functions
- Exponential and logarithmic functions
- Miscellaneous functions

All the math functions require that the header MATH.H be included in any program that uses them. In addition to declaring the math functions, this header defines a macro called `HUGE_VAL`. If an operation produces a result that is too large to be represented by a **double**, an overflow occurs, which causes the routine to return `HUGE_VAL`. This is called a *range error*. For all the mathematics functions, if the input value is not in the domain for which the function is defined, a *domain error* occurs.

All angles are specified in radians.

---

### acos

```c
#include <math.h>
double acos(double arg);
```

**Description**  
The `acos()` function returns the arc cosine of `arg`. The argument to `acos()` must be in the range -1 through 1; otherwise a domain error will occur.

**Example**  
This program prints the arc cosines, in one-tenth increments, of the values -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = -1.0;

    do {
        printf("arc cosine of %f is %f\n", val, acos(val));
        val += 0.1;
    } while(val<=1.0);

    return 0;
}
```

---

### asin

```c
#include <math.h>
double asin(double arg);
```

**Description**  
The `asin()` function returns the arc sine of `arg`. The argument to `asin()` must be in the range -1 through 1; otherwise a domain error will occur.

**Example**  
This program prints the arc sines, in one-tenth increments, of the values -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = -1.0;

    do {
        printf("arc sine of %f is %f\n", val, asin(val));
        val += 0.1;
    } while(val<=1.0);

    return 0;
}
```

---

### atan

```c
#include <math.h>
double atan(double arg);
```

**Description**  
The `atan()` function returns the arc tangent of `arg`.

**Example**  
This program prints the arc tangents, in one-tenth increments, of the values -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = -1.0;

    do {
        printf("arc tangent of %f is %f\n", val, atan(val));
        val += 0.1;
    } while(val<=1.0);

    return 0;
}
```

---

### atan2

```c
#include <math.h>
double atan2(double y, double x);
```

**Description**  
The `atan2()` function returns the arc tangent of `y/x`. It uses the signs of its arguments to compute the quadrant of the return value.

**Example**  
This program prints the arc tangents, in one-tenth increments of `y`, from -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double y = -1.0;

    do {
        printf("atan2 of %f is %f\n", y, atan2(y, 1.0));
        y += 0.1;
    } while(y<=1.0);

    return 0;
}
```

---

### ceil

```c
#include <math.h>
double ceil(double num);
```

**Description**  
The `ceil()` function returns the smallest integer (represented as a **double**) that is not less than `num`. For example, given 1.02, `ceil()` would return 2.0; given -1.02, `ceil()` would return -1.

**Example**  
This fragment prints **10.0** on the screen:

```c
printf("%f", ceil(9.9));
```

---

### cos

```c
#include <math.h>
double cos(double arg);
```

**Description**  
The `cos()` function returns the cosine of `arg`. The value of `arg` must be in radians.

**Example**  
This program prints the cosines, in one-tenth increments, of the values -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = -1.0;

    do {
        printf("cosine of %f is %f\n", val, cos(val));
        val += 0.1;
    } while(val<=1.0);

    return 0;
}
```

---

### cosh

```c
#include <math.h>
double cosh(double arg);
```

**Description**  
The `cosh()` function returns the hyperbolic cosine of `arg`.

**Example**  
This program prints the hyperbolic cosines, in one-tenth increments, of the values -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = -1.0;

    do {
        printf("hyperbolic cosine of %f is %f\n", val, cosh(val));
        val += 0.1;
    } while(val<=1.0);

    return 0;
}
```

---

### exp

```c
#include <math.h>
double exp(double arg);
```

**Description**  
The `exp()` function returns the natural logarithm *e* raised to the `arg` power.

**Example**  
This fragment displays the value of *e* (rounded to 2.718282):

```c
printf("Value of e to the first: %f", exp(1.0));
```

---

### fabs

```c
#include <math.h>
double fabs(double num);
```

**Description**  
The `fabs()` function returns the absolute value of `num`.

**Example**  
This program prints the numbers **1.0 1.0** on the screen:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    printf("%.1f %.1f", fabs(1.0), fabs(-1.0));

    return 0;
}
```

---

### floor

```c
#include <math.h>
double floor(double num);
```

**Description**  
The `floor()` function returns the largest integer (represented as a **double**) not greater than `num`. For example, given 1.02, `floor()` would return 1.0; given -1.02, `floor()` would return -2.0.

**Example**  
This fragment prints **10.0** on the screen:

```c
printf("%f", floor(10.9));
```

---

### log

```c
#include <math.h>
double log(double num);
```

**Description**  
The `log()` function returns the natural logarithm for `num`. A domain error occurs if `num` is negative and a range error occurs if the argument is 0.

**Example**  
This program prints the natural logarithms for the numbers 1 through 10:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = 1.0;

    do {
        printf("%f %f\n", val, log(val));
        val++;
    } while(val<11.0);

    return 0;
}
```

---

### log10

```c
#include <math.h>
double log10(double num);
```

**Description**  
The `log10()` function returns the base 10 logarithm for the variable `num`. A domain error occurs if `num` is negative and a range error occurs if the argument is 0.

**Example**  
This program prints the base 10 logarithms for the numbers 1 through 10:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = 1.0;

    do {
        printf("%f %f\n", val, log10(val));
        val++;
    } while(val<11.0);

    return 0;
}
```

---

### pow

```c
#include <math.h>
double pow(double base, double exp);
```

**Description**  
The `pow()` function returns `base` raised to the `exp` power ($base^{exp}$). A domain error may occur if `base` is 0 and `exp` is less than or equal to 0. A domain error will occur if `base` is negative and `exp` is not an integer. An overflow produces a range error.

**Example**  
This program prints the first ten powers of 10:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double x=10.0, y=0.0;

    do {
        printf("%f ", pow(x, y));
        y++;
    } while(y<11);

    return 0;
}
```

---

### sin

```c
#include <math.h>
double sin(double arg);
```

**Description**  
The `sin()` function returns the sine of `arg`. The value of `arg` must be in radians.

**Example**  
This program prints the sines, in one-tenth increments, of the values -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = -1.0;

    do {
        printf("sine of %f is %f\n", val, sin(val));
        val += 0.1;
    } while(val<=1.0);

    return 0;
}
```

---

### sinh

```c
#include <math.h>
double sinh(double arg);
```

**Description**  
The `sinh()` function returns the hyperbolic sine of `arg`.

**Example**  
The following program prints the hyperbolic sines, in one-tenth increments, of the values -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = -1.0;

    do {
        printf("hyperbolic sine of %f is %f\n", val, sinh(val));
        val += 0.1;
    } while(val<=1.0);

    return 0;
}
```

---

### sqrt

```c
#include <math.h>
double sqrt(double num);
```

**Description**  
The `sqrt()` function returns the square root of `num`. If called with a negative argument, a domain error will occur.

**Example**  
This fragment prints **4.0** on the screen:

```c
printf("%f", sqrt(16.0));
```

---

### tan

```c
#include <math.h>
double tan(double arg);
```

**Description**  
The `tan()` function returns the tangent of `arg`. The value of `arg` must be in radians.

**Example**  
This program prints the tangents, in one-tenth increments, of the values -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = -1.0;

    do {
        printf("tangent of %f is %f\n", val, tan(val));
        val += 0.1;
    } while(val<=1.0);

    return 0;
}
```

---

### tanh

```c
#include <math.h>
double tanh(double arg);
```

**Description**  
The `tanh()` function returns the hyperbolic tangent of `arg`.

**Example**  
This program prints the hyperbolic tangents, in one-tenth increments, of the values -1 through 1:

```c
#include <math.h>
#include <stdio.h>

int main(void)
{
    double val = -1.0;

    do {
        printf("tanh of %f is %f\n", val, tanh(val));
        val += 0.1;
    } while(val<=1.0);

    return 0;
}
```

---

## A.3 TIME AND DATE FUNCTIONS

The time and date functions require the header TIME.H for their prototypes. This header file also defines four types and two macros. The type `time_t` is able to represent the system time and date as a long integer. This is called the *calendar time*. The structure type `tm` holds date and time broken down into its elements. The `tm` structure is defined as shown here:

```c
struct tm {
    int tm_sec;   /* seconds, 0-61 */
    int tm_min;   /* minutes, 0-59 */
    int tm_hour;  /* hours, 0-23 */
    int tm_mday;  /* day of the month, 1-31 */
    int tm_mon;   /* months since Jan, 0-11 */
    int tm_year;  /* years from 1900 */
    int tm_wday;  /* days since Sunday, 0-6 */
    int tm_yday;  /* days since Jan 1, 0-365 */
    int tm_isdst; /* Daylight Saving Time indicator */
};
```

The value of `tm_isdst` will be positive if Daylight Saving Time is in effect, 0 if it is not in effect, and negative if there is no information available. When the date and time are represented in this way, they are referred to as *broken-down time*.

The type `clock_t` is defined the same as `time_t`. The header file also defines `size_t`.

The macros defined are `NULL` and `CLOCKS_PER_SEC`.

---

### asctime

```c
#include <time.h>
char *asctime(const struct tm *ptr);
```

**Description**  
The `asctime()` function returns a pointer to a string that contains the time and date stored in the structure pointed to by *ptr* after it has been converted into the following form:

```
day month date hours:minutes:seconds year\n\0
```

For example:

```
Wed Jun 19 12:05:34 1999
```

The structure pointer passed to `asctime()` is generally obtained from either `localtime()` or `gmtime()`.

The buffer used by `asctime()` to hold the formatted output string is a statically allocated character array and is overwritten each time the function is called. If you want to save the contents of the string, you need to copy it elsewhere.

**Example**  
This program displays the local time defined by the system:

```c
#include <time.h>
#include <stdio.h>

int main(void)
{
    struct tm *ptr;
    time_t lt;

    lt = time(NULL);
    ptr = localtime(&lt);
    printf(asctime(ptr));

    return 0;
}
```

---

### clock

```c
#include <time.h>
clock_t clock(void);
```

**Description**  
The `clock()` function returns the number of system clock cycles that have occurred since the program began execution. To compute the number of seconds, divide this value by the `CLOCKS_PER_SEC` macro.

**Example**  
The following program displays the number of system clock cycles occurring since it began:

```c
#include <stdio.h>
#include <time.h>

int main(void)
{
    int i;

    for(i=0; i<10000; i++) ;

    printf("%u", clock());

    return 0;
}
```

---

### ctime

```c
#include <time.h>
char *ctime(const time_t *time);
```

**Description**  
The `ctime()` function returns a pointer to a string of the form

```
day month date hours:minutes:seconds year\n\0
```

given a pointer to the calendar time. The calendar time is generally obtained through a call to `time()`. The `ctime()` function is equivalent to:

```c
asctime(localtime(time))
```

The buffer used by `ctime()` to hold the formatted output string is a statically allocated character array and is overwritten each time the function is called. If you wish to save the contents of the string, you need to copy it elsewhere.

**Example**  
This program displays the local time defined by the system:

```c
#include <time.h>
#include <stdio.h>

int main(void)
{
    time_t lt;

    lt = time(NULL);
    printf(ctime(&lt));

    return 0;
}
```

---

### difftime

```c
#include <time.h>
double difftime(time_t time2, time_t time1);
```

**Description**  
The `difftime()` function returns the difference, in seconds, between *time1* and *time2*. That is, *time2* - *time1*.

**Example**  
This program times the number of seconds that it takes for the empty `for` loop to go from 0 to 500000.

```c
#include <time.h>
#include <stdio.h>

int main(void)
{
    time_t start, end;
    long unsigned int t;

    start = time(NULL);
    for(t=0; t<500000L; t++) ;
    end = time(NULL);
    printf("Loop required %f seconds.\n", difftime(end, start));

    return 0;
}
```

---

### gmtime

```c
#include <time.h>
struct tm *gmtime(const time_t *time);
```

**Description**  
The `gmtime()` function returns a pointer to the broken-down form of *time* in the form of a `tm` structure. The time is represented in Coordinated Universal Time (i.e., Greenwich Mean Time). The *time* value is generally obtained through a call to `time()`.

The structure used by `gmtime()` to hold the broken-down time is statically allocated and is overwritten each time the function is called. If you wish to save the contents of the structure, you need to copy it elsewhere.

**Example**  
This program prints both the local time and the Coordinated Universal Time of the system:

```c
#include <time.h>
#include <stdio.h>

/* print local and Coordinated Universal time */
int main(void)
{
    struct tm *local, *coordinated;
    time_t t;

    t = time(NULL);
    local = localtime(&t);
    printf("Local time and date: %s", asctime(local));
    coordinated = gmtime(&t);
    printf("Coordinated Universal time and date: %s",
            asctime(coordinated));

    return 0;
}
```

---

### localtime

```c
#include <time.h>
struct tm *localtime(const time_t *time);
```

**Description**  
The `localtime()` function returns a pointer to the broken-down form of *time* in the form of a `tm` structure. The time is represented in local time. The *time* value is generally obtained through a call to the `time()` function.

The structure used by `localtime()` to hold the broken-down time is statically allocated and is overwritten each time the function is called. If you wish to save the contents of the structure, you need to copy it elsewhere.

**Example**  
This program prints both the local time and the Coordinated Universal time of the system:

```c
#include <time.h>
#include <stdio.h>

/* print local and Coordinated Universal time */
int main(void)
{
    struct tm *local;
    time_t t;

    t = time(NULL);
    local = localtime(&t);
    printf("Local time and date: %s", asctime(local));
    local = gmtime(&t);
    printf("Coordinated Universal time and date: %s",
            asctime(local));

    return 0;
}
```

---

### time

```c
#include <time.h>
time_t time(time_t *systime);
```

**Description**  
The `time()` function returns the current calendar time of the system. If the system has no time-keeping mechanism, then -1 is returned.

The `time()` function can be called either with a null pointer or with a pointer to a variable of type `time_t`. If the latter is used, then the argument will also be assigned the calendar time.

**Example**  
This program displays the local time defined by the system:

```c
#include <time.h>
#include <stdio.h>

int main(void)
{
    struct tm *ptr;
    time_t lt;

    lt = time(NULL);
    ptr = localtime(&lt);
    printf(asctime(ptr));

    return 0;
}
```

---

## A.4 DYNAMIC ALLOCATION

There are two primary ways a C program can store information in the main memory of the computer. The first uses global and local variables—including arrays and structures. In the case of global and static local variables, the storage is fixed throughout the runtime of your program. For dynamic local variables, storage is allocated on the stack. Although these variables are efficiently implemented in C, they require the programmer to know in advance the amount of storage needed for every situation. The second way information can be stored is with C's dynamic allocation system. In this method, storage for information is allocated from the free memory area (called the *heap*) as it is needed.

The ANSI C standard specifies that the header information necessary to the dynamic allocation system is in STDLIB.H. In this file, the type `size_t` is defined. This type is used extensively by the allocation functions and is essentially the equivalent of **unsigned**.

---

### calloc

```c
#include <stdlib.h>
void *calloc(size_t num, size_t size);
```

**Description**  
The `calloc()` function returns a pointer to the allocated memory. The amount of memory allocated is equal to `num * size`. That is, `calloc()` allocates sufficient memory for an array of *num* objects of size *size*.

The `calloc()` function returns a pointer to the first byte of the allocated region. If there is not enough memory to satisfy the request, a null pointer is returned.

It is always important to verify that the return value is not a null pointer before attempting to use it.

**Example**  
This function returns a pointer to a dynamically allocated array of 100 floats:

```c
#include <stdlib.h>
#include <stdio.h>

float *get_mem(void)
{
    float *p;

    p = calloc(100, sizeof(float));
    if(!p) {
        printf("Allocation error - aborting.\n");
        exit(1);
    }
    return p;
}
```

---

### free

```c
#include <stdlib.h>
void free(void *ptr);
```

**Description**  
The `free()` function deallocates the memory pointed to by *ptr*. This makes the memory available for future allocation.

It is imperative that the `free()` function be called only with a pointer that was previously allocated using one of the dynamic allocation system's functions, such as `malloc()` or `calloc()`. Using an invalid pointer in the call will probably destroy the memory management mechanism and cause a system crash.

**Example**  
This program first allocates room for 100 user-entered strings and then frees them:

```c
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    char *str[100];
    int i;

    for(i=0; i<100; i++) {
        if((str[i] = malloc(128))==NULL) {
            printf("Allocation error - aborting.\n");
            exit(0);
        }
        gets(str[i]);
    }

    /* now free the memory */
    for(i=0; i<100; i++) free(str[i]);

    return 0;
}
```

---

### malloc

```c
#include <stdlib.h>
void *malloc(size_t size);
```

**Description**  
The `malloc()` function returns a pointer to the first byte of a region of memory of size *size* that has been allocated from the heap. (Remember, the heap is a region of free memory managed by C's dynamic allocation subsystem.) If there is insufficient memory in the heap to satisfy the request, `malloc()` returns a null pointer. It is always important to verify that the return value is not a null pointer before attempting to use it. Attempting to use a null pointer will usually result in a system crash.

**Example**  
This function allocates sufficient memory to hold structures of type `addr`:

```c
#include <stdlib.h>
#include <stdio.h>

struct addr {
    char name[40];
    char street[40];
    char city[40];
    char state[3];
    char zip[10];
};

struct addr *get_struct(void)
{
    struct addr *p;

    if((p = malloc(sizeof(struct addr)))==NULL) {
        printf("Allocation error - aborting.\n");
        exit(0);
    }
    return p;
}
```

---

### realloc

```c
#include <stdlib.h>
void *realloc(void *ptr, size_t size);
```

**Description**  
The `realloc()` function changes the size of the allocated memory pointed to by *ptr* to that specified by *size*. The value of *size* may be greater or less than the original. A pointer to the memory block is returned since it may be necessary for `realloc()` to move the block to increase its size. If this occurs, the contents of the old block are copied into the new block—no information is lost.

If there is not enough free memory in the heap to allocate *size* bytes, a null pointer is returned. This means it is important to verify the success of a call to `realloc()`.

**Example**  
This program first allocates 17 characters, copies the string "this is 16 chars" into the space, and then uses `realloc()` to increase the size to 18 in order to place a period at the end.

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *p;

    p = malloc(17);
    if(!p) {
        printf("Allocation error - aborting.\n");
        exit(1);
    }

    strcpy(p, "this is 16 chars");

    p = realloc(p, 18);
    if(!p) {
        printf("Allocation error - aborting.\n");
        exit(1);
    }

    strcat(p, ".");

    printf(p);

    free(p);

    return 0;
}
```

---

## A.5 MISCELLANEOUS FUNCTIONS

The functions discussed in this section are all standard functions that don't easily fit in any other category.

---

### abort

```c
#include <stdlib.h>
void abort(void);
```

**Description**  
The `abort()` function causes immediate termination of a program. Whether it closes any open files is defined by the implementation, but generally it won't.

**Example**  
In this program, if the user enters A, the program will terminate:

```c
#include <stdlib.h>
#include <conio.h>

int main(void)
{
    for(;;)
        if(getche()=='A') abort();

    return 0;
}
```

---

### abs

```c
#include <stdlib.h>
int abs(int num);
```

**Description**  
The `abs()` function returns the absolute value of the integer *num*.

**Example**  
This function converts the user-entered numbers into their absolute values:

```c
#include <stdlib.h>
#include <stdio.h>

int get_abs(void)
{
    char num[80];

    gets(num);

    return abs(atoi(num));
}
```

---

### atof

```c
#include <stdlib.h>
double atof(const char *str);
```

**Description**  
The `atof()` function converts the string pointed to by *str* into a double value. The string must contain a valid floating-point number. If this is not the case, the returned value is 0.

The number may be terminated by any character that cannot be part of a valid floating-point number. This includes whitespace characters, punctuation (other than periods), and characters other than 'E' or 'e'. Thus, if `atof()` is called with "100.00HELLO", the value 100.00 will be returned.

**Example**  
This program reads two floating-point numbers and displays their sum:

```c
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    char num1[80], num2[80];

    printf("Enter first: ");
    gets(num1);
    printf("Enter second: ");
    gets(num2);
    printf("The sum is: %f", atof(num1) + atof(num2));

    return 0;
}
```

---

### atoi

```c
#include <stdlib.h>
int atoi(const char *str);
```

**Description**  
The `atoi()` function converts the string pointed to by *str* into an **int** value. The string must contain a valid integer number. If this is not the case, the returned value is 0.

The number may be terminated by any character that cannot be part of a integer number. This includes whitespace characters, punctuation, and other characters. Thus, if `atoi()` is called with 123.23, the integer value 123 will be returned, and the 0.23 ignored.

**Example**  
This program reads two integer numbers and displays their sum:

```c
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    char num1[80], num2[80];

    printf("Enter first: ");
    gets(num1);
    printf("Enter second: ");
    gets(num2);
    printf("The sum is: %d", atoi(num1) + atoi(num2));

    return 0;
}
```

---

### atol

```c
#include <stdlib.h>
long atol(const char *str);
```

**Description**  
The `atol()` function converts the string pointed to by *str* into a **long int** value. The string must contain a valid long integer number. If this is not the case, the returned value is 0.

The number may be terminated by any character that cannot be part of an integer number. This includes whitespace characters, punctuation, and other characters. Thus, if `atol()` is called with 123.23, the integer value 123 will be returned, and the 0.23 ignored.

**Example**  
This program reads two long integer numbers and displays their sum:

```c
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    char num1[80], num2[80];

    printf("Enter first: ");
    gets(num1);
    printf("Enter second: ");
    gets(num2);
    printf("The sum is: %ld", atol(num1) + atol(num2));

    return 0;
}
```

---

### bsearch

```c
#include <stdlib.h>
void *bsearch(const void *key, const void *base, size_t num, size_t size, int (*compare)(const void *, const void *));
```

**Description**  
The `bsearch()` function performs a binary search on the sorted array pointed to by *base* and returns a pointer to the first member that matches the key pointed to by *key*. The number of elements in the array is specified by *num* and the size (in bytes) of each element is described by *size*. (The `size_t` type is defined in STDLIB.H and is essentially the equivalent of **unsigned**.)

The function pointed to by *compare* is used to compare an element of the array with the key. The form of *compare* must be

```c
int function_name(const void *arg1, const void *arg2)
```

It must return the following values:

| Value | Meaning |
| :--- | :--- |
| Less than 0 | If *arg1* is less than *arg2* |
| 0 | If *arg1* is equal to *arg2* |
| Greater than 0 | If *arg1* is greater than *arg2* |

The array must be sorted in ascending order, with the lowest address containing the lowest element.

If the array does not contain the key, then a null pointer is returned.

**Example**  
This program reads characters entered at the keyboard and determines whether they belong to the alphabet.

```c
#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>

char *alpha = "abcdefghijklmnopqrstuvwxyz";

int comp(const void *ch, const void *s);

int main(void)
{
    char ch;
    char *p;

    do {
        printf("Enter a character: ");
        scanf("%c%*c", &ch);
        ch = tolower(ch);
        p = bsearch(&ch, alpha, 26, 1, comp);
        if(p) printf("is in alphabet.\n");
        else printf("is not in alphabet.\n");
    } while(p);

    return 0;
}

/* compare two characters */
int comp(const void *ch, const void *s)
{
    return *(char *)ch - *(char *)s;
}
```

---

### exit

```c
#include <stdlib.h>
void exit(int status);
```

**Description**  
The `exit()` function causes immediate normal termination of a program.

The value of *status* is passed to the calling process, usually the operating system, if the environment supports it. By convention, if the value of *status* is 0, normal program termination is assumed. A nonzero value may be used to indicate an error.

You may also use the predefined macros `EXIT_SUCCESS` and `EXIT_FAILURE` as arguments to `exit()`.

**Example**  
This function performs menu selection for a mailing list program. If Q is selected, the program is terminated.

```c
char menu(void)
{
    char ch;

    do {
        printf("Enter names (E)\n");
        printf("Delete name (D)\n");
        printf("Print (P)\n");
        printf("Quit (Q)\n");
    } while(!strchr("EDPQ", toupper(ch)));
    if(ch=='Q') exit(0);
    return ch;
}
```

---

### labs

```c
#include <stdlib.h>
long labs(long num);
```

**Description**  
The `labs()` function returns the absolute value of the long int *num*.

**Example**  
This function converts the user-entered numbers into their absolute values:

```c
#include <stdlib.h>
#include <stdio.h>

long int get_labs(void)
{
    char num[80];

    gets(num);

    return labs(atol(num));
}
```

---

### longjmp

```c
#include <setjmp.h>
void longjmp(jmp_buf envbuf, int val);
```

**Description**  
The `longjmp()` function causes program execution to resume at the point of the last call to `setjmp()`. These two functions are the way ANSI C provides for a jump between functions. Notice that the header SETJMP.H is required.

The `longjmp()` function operates by resetting the stack as described in *envbuf*, which must have been set by a prior call to `setjmp()`. This causes program execution to resume at the statement following the `setjmp()` invocation—the computer is "tricked" into thinking that it never left the function that called `setjmp()`. (As a somewhat graphic explanation, the `longjmp()` function "warps" across time and (memory) space to a previous point in your program, without having to perform the normal function-return process.)

The buffer *envbuf* is of type `jmp_buf`, which is defined in the header SETJMP.H. The buffer must have been set through a call to `setjmp()` prior to calling `longjmp()`.

The value of *val* becomes the return value of `setjmp()` and may be interrogated to determine where the long jump came from. The only value not allowed is 0.

It is important to understand that the `longjmp()` function must be called before the function that called `setjmp()` returns. If not, the result is technically undefined. In actuality, a crash will almost certainly occur.

By far the most common use of `longjmp()` is to return from a deeply nested set of routines when a catastrophic error occurs.

**Example**  
This program prints **1 2 3**:

```c
#include <setjmp.h>
#include <stdio.h>

void f2(void);

jmp_buf ebuf;

int main(void)
{
    char first=1;
    int i;

    printf("1 ");
    i = setjmp(ebuf);
    if(first) {
        first = !first;
        f2();
        printf("this will not be printed");
    }
    printf("%d", i);

    return 0;
}

void f2(void)
{
    printf("2 ");
    longjmp(ebuf, 3);
}
```

---

### qsort

```c
#include <stdlib.h>
void qsort(void *base, size_t num, size_t size, int (*compare)(const void *, const void *));
```

**Description**  
The `qsort()` function sorts the array pointed to by *base* using a Quicksort (which was developed by C.A.R. Hoare). The Quicksort is generally considered the best general-purpose sorting algorithm. Upon termination, the array will be sorted. The number of elements in the array is specified by *num* and the size (in bytes) of each element is described by *size*. (The `size_t` type is defined in STDLIB.H and is essentially the equivalent of **unsigned**.)

The function pointed to by *compare* is used to compare two elements in the array. The form of *compare* must be

```c
int function_name(const void *arg1, const void *arg2)
```

It must return the following values:

| Value | Meaning |
| :--- | :--- |
| Less than 0 | If *arg1* is less than *arg2* |
| 0 | If *arg1* is equal to *arg2* |
| Greater than 0 | If *arg1* is greater than *arg2* |

The array is sorted in ascending order, with the lowest address containing the lowest element.

**Example**  
This program sorts a list of integers and displays the results:

```c
#include <stdlib.h>
#include <stdio.h>

int comp(const void *i, const void *j);

int num[10] = {
    1, 3, 6, 5, 8, 7, 9, 6, 2, 0
};

int main(void)
{
    int i;

    printf("Original array: ");
    for(i=0; i<10; i++) printf("%d ", num[i]);
    printf("\n");

    qsort(num, 10, sizeof(int), comp);

    printf("Sorted array: ");
    for(i=0; i<10; i++) printf("%d ", num[i]);

    return 0;
}

/* compare the integers */
int comp(const void *i, const void *j)
{
    return *(int *)i - *(int *)j;
}
```

---

### rand

```c
#include <stdlib.h>
int rand(void);
```

**Description**  
The `rand()` function generates a sequence of pseudo-random numbers. Each time it is called, an integer between 0 and `RAND_MAX` is returned. `RAND_MAX` is defined in STDLIB.H. The ANSI standard stipulates that the macro `RAND_MAX` will have a value of at least 32,767.

**Example**  
This program displays ten pseudo-random numbers:

```c
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    int i;

    for(i=0; i<10; i++)
        printf("%d ", rand());

    return 0;
}
```

---

### setjmp

```c
#include <setjmp.h>
int setjmp(jmp_buf envbuf);
```

**Description**  
The `setjmp()` function saves the contents of the system stack in the buffer *envbuf* for later use by `longjmp()`.

The `setjmp()` function returns 0 upon invocation. However, `longjmp()` passes an argument to `setjmp()` when it executes, and it is this value (always nonzero) that will appear to be the value of `setjmp()` after a call to `longjmp()`.

See the `longjmp()` section for more information.

**Example**  
This program prints **1 2 3**:

```c
#include <setjmp.h>
#include <stdio.h>

void f2(void);

jmp_buf ebuf;

int main(void)
{
    char first=1;
    int i;

    printf("1 ");
    i = setjmp(ebuf);
    if(first) {
        first = !first;
        f2();
        printf("this will not be printed");
    }
    printf("%d", i);

    return 0;
}

void f2(void)
{
    printf("2 ");
    longjmp(ebuf, 3);
}
```

---

### srand

```c
#include <stdlib.h>
void srand(unsigned seed);
```

**Description**  
The `srand()` function is used to set a starting point for the sequence generated by `rand()`, which returns pseudo-random numbers.

Generally `srand()` is used to allow multiple program runs to use different sequences of pseudo-random numbers.

**Example**  
This program uses the system time to randomly initialize the `rand()` function using `srand()`:

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Seed rand with the system time
   and display the first 100 numbers.
*/
int main(void)
{
    int i, utime;
    long ltime;

    /* get the current calendar time */
    ltime = time(NULL);
    utime = (unsigned int) ltime/2;
    srand(utime);

    for(i=0; i<10; i++) printf("%d ", rand());

    return 0;
}
```
