# 5 Exploring Arrays and Strings

IN this chapter you will learn about arrays. An *array* is essentially a list of related variables and can be very useful in a variety of situations. Since in C strings are simply arrays of characters, you will also learn about strings and several of C's string functions.

---

### Review Skills Check

Before proceeding, you should be able to answer these questions and perform these exercises:

1. What is the difference between a local and a global variable?
2. What data type will a C compiler assign to these numbers? (Assume 16-bit integers.)
   a. `10`  
   b. `10000`  
   c. `123.45`  
   d. `123564`  
   e. `-45099`  
3. Write a program that inputs a **long**, a **short**, and a **double** and then writes these values to the screen.
4. What does a type cast do?
5. To which `if` is the `else` in this fragment associated? What is the general rule?
```c
if(i)
    if(j) printf("i and j are true");
else printf("i is false");
```
6. Using the following fragment, what is the value of `a` when `i` is 1? What is `a`'s value when `i` is 4?
```c
switch(i) {
    case 1: a = 1;
    case 2: a = 2;
        break;
    case 3: a = 3;
        break;
    case 4:
    case 5: a = 5;
}
```

---

## 5.1 DECLARE ONE-DIMENSIONAL ARRAYS

In C, a one-dimensional array is a list of variables that are all of the same type and are accessed through a common name. An individual variable in the array is called an *array element*. Arrays form a convenient way to handle groups of related data.

To declare a one-dimensional array, use the general form:

```c
type var_name[size];
```

where *type* is a valid C data type, *var_name* is the name of the array, and *size* specifies the number of elements in the array. For example, to declare an integer array with 20 elements called `myarray`, use this statement:

```c
int myarray[20];
```

An array element is accessed by indexing the array using the number of the element. In C, all arrays begin at zero. This means that if you want to access the first element in an array, use zero for the index. To index an array, specify the index of the element you want inside square brackets. For example, the following refers to the second element of `myarray`:

```c
myarray[1]
```

Remember, arrays start at zero, so an index of 1 references the second element.

To assign an array element a value, put the array on the left side of an assignment statement. For example, this gives the first element in `myarray` the value 100:

```c
myarray[0] = 100;
```

C stores one-dimensional arrays in one contiguous memory location with the first element at the lowest address. For example, after this fragment executes,

```c
int i[5];
int j;

for(j=0; j<5; j++) i[j] = j;
```

the array `i` will look like this in memory:

| `i[0]` | `i[1]` | `i[2]` | `i[3]` | `i[4]` |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 1 | 2 | 3 | 4 |

You can use an array element anywhere you can use a simple variable. For example, this statement adds the value of the first and second elements of `myarray` and assigns the result to `sum`:

```c
sum = myarray[0] + myarray[1];
```

### EXAMPLES

1. This program loads an array with the daily high temperature for a month and then finds the minimum, maximum, and average temperature:

```c
#include <stdio.h>

int main(void)
{
    int temp[31], min, max, avg;
    int days;

    printf("How many days in the month? ");
    scanf("%d", &days);

    for(int i=0; i<days; i++) {
        printf("Enter noontime temperature for day %d: ", i+1);
        scanf("%d", &temp[i]);
    }

    /* find average */
    avg = 0;
    for(int i=0; i<days; i++) avg = avg + temp[i];
    printf("Average temperature: %d\n", avg/days);

    /* find min and max */
    min = 200; /* initialize min and max */
    max = 0;
    for(int i=0; i<days; i++) {
        if(min>temp[i]) min = temp[i];
        if(max<temp[i]) max = temp[i];
    }

    printf("Minimum temperature: %d\n", min);
    printf("Maximum temperature: %d\n", max);

    return 0;
}
```

2. As stated earlier, to copy the contents of one array to another, you must explicitly copy each element separately. For example, this program loads `a1` with the numbers 1 through 10 and then copies them into `a2`.

```c
#include <stdio.h>

int main(void)
{
    int a1[10], a2[10];
    int i;

    for(i=1; i<11; i++) a1[i-1] = i;

    for(i=0; i<10; i++) a2[i] = a1[i];

    for(i=0; i<10; i++) printf("%d ", a2[i]);

    return 0;
}
```

3. The following program is an improved version of the code-machine program developed in Chapter 3. In this version, the user first enters the message, which is stored in a character array. When the user presses ENTER, the entire message is then encoded by adding 1 to each letter.

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char mess[80];
    int i;

    printf("Enter message (less than 80 characters)\n");
    for(i=0; i<80; i++) {
        mess[i] = getche();
        if(mess[i]=='\r') break;
    }
    printf("\n");

    for(i=0; mess[i]!='\r'; i++) printf("%c", mess[i]+1);

    return 0;
}
```

4. Arrays are especially useful when you want to sort information. For example, this program lets the user enter up to 100 numbers and then sorts them. The sorting algorithm is the *bubble sort*. The bubble sort algorithm is not very efficient, but it is simple to understand and easy to code. The general concept behind the bubble sort, indeed how it got its name, is the repeated comparisons and, if necessary, exchanges of adjacent elements. This is a little like bubbles in a tank of water with each bubble, in turn, seeking its own level.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int item[100];
    int a, b, t;
    int count;

    /* read in numbers */
    printf("How many numbers? ");
    scanf("%d", &count);
    for(a=0; a<count; a++) scanf("%d", &item[a]);

    /* now, sort them using a bubble sort */
    for(a=1; a<count; ++a)
        for(b=count-1; b>=a; --b) {
            /* compare adjacent elements */
            if(item[b-1] > item[b]) {
                /* exchange elements */
                t = item[b-1];
                item[b-1] = item[b];
                item[b] = t;
            }
        }

    /* display sorted list */
    for(t=0; t<count; t++) printf("%d ", item[t]);

    return 0;
}
```

### EXERCISES

1. What is wrong with this program fragment?

```c
#include <stdio.h>

int main(void)
{
    int i, count[10];

    for(i=0; i<100; i++) {
        printf("Enter a number: ");
        scanf("%d", &count[i]);
    }
    .
    .
    .
}
```

2. Write a program that reads ten numbers entered by the user and reports if any of them match.
3. Change the sorting program shown in the examples so that it sorts data of type **float**.

---

## 5.2 USE STRINGS

The most common use of the one-dimensional array in C is the string. Unlike most other computer languages, C has no built-in string data type. Instead, a string is defined as a *null-terminated character array*. In C, a null is zero. The fact that string must be terminated by a null means that you must define the array that is going to hold a string to be one byte larger than the largest string it will be required to hold, to make room for the null. A string constant is null-terminated by the compiler automatically.

There are several ways to read a string from the keyboard. The method we will use in this chapter employs another of C's standard library functions: `gets()`. Like the other standard I/O functions, `gets()` also uses the STDIO.H header file. To use `gets()`, call it using the name of a character array without any index. The `gets()` function reads characters until you press ENTER. The ENTER key (i.e., carriage return) is not stored, but is replaced by a null, which terminates the string. For example, this program reads a string entered at the keyboard. It then displays the contents of that string one character at a time.

```c
#include <stdio.h>

int main(void)
{
    char str[80];
    int i;

    printf("Enter a string (less than 80 chars): ");
    gets(str);
    for(i=0; str[i]; i++) printf("%c", str[i]);

    return 0;
}
```

Notice how the program uses the fact that a null is false to control the loop that outputs the string.

There is a potential problem with `gets()` that you need to be aware of. The `gets()` function performs no bounds checking, so it is possible for the user to enter more characters than the array receiving them can hold. For example, if you call `gets()` with an array that is 20 characters long, there is no mechanism to stop you from entering more than 20 characters. If you do enter more than 20 characters, the array will be overrun. This can obviously lead to trouble, including a program crash. Later in this book you will learn some alternative ways to read strings, although none are as convenient as using `gets()`. For now, just be sure to call `gets()` with an array that is more than large enough to hold the expected input.

In the previous program, the string that was entered by the user was output to the screen a character at a time. There is, of course, a much easier way to display a string using `printf()`, as shown in this version of the program:

```c
#include <stdio.h>

int main(void)
{
    char str[80];

    printf("Enter a string (less than 80 chars): ");
    gets(str);
    printf(str); /* output the string */

    return 0;
}
```

Recall that the first argument to `printf()` is a string. Since `str` contains a string it can be used as the first argument to `printf()`. The contents of `str` will then be displayed.

If you wanted to output other items in addition to `str`, you could display `str` using the `%s` format code. For example, to output a newline after `str`, you could use this call to `printf()`:

```c
printf("%s\n", str);
```

This method uses the `%s` format specifier followed by the newline character and uses `str` as a second argument to be matched by the `%s` specifier.

The C standard library supplies many string-related functions. The four most important are `strcpy()`, `strcat()`, `strcmp()`, and `strlen()`. These functions require the header file STRING.H. Let's look at each now.

The `strcpy()` function has this general form:

```c
strcpy(to, from);
```

It copies the contents of `from` to `to`. The contents of `from` are unchanged. For example, this fragment copies the string "hello" into `str` and displays it on the screen:

```c
char str[80];

strcpy(str, "hello");
printf("%s", str);
```

The `strcpy()` function performs no bounds checking, so you must make sure that the array on the receiving end is large enough to hold what is being copied, including the null terminator.

The `strcat()` function adds the contents of one string to another. This is called *concatenation*. Its general form is

```c
strcat(to, from);
```

It adds the contents of `from` to the contents of `to`. It performs no bounds checking, so you must make sure that `to` is large enough to hold its current contents plus what it will be receiving. This fragment displays **hello there**:

```c
char str[80];

strcpy(str, "hello");
strcat(str, " there");
printf(str);
```

The `strcmp()` function compares two strings. It takes this general form:

```c
strcmp(s1, s2);
```

It returns zero if the strings are the same. It returns less than zero if `s1` is less than `s2` and greater than zero if `s1` is greater than `s2`. The strings are compared lexicographically; that is, in dictionary order. Therefore, a string is less than another when it would appear before the other in a dictionary. A string is greater than another when it would appear after the other. The comparison is not based upon the length of the string. Also, the comparison is case-sensitive, lowercase characters being greater than uppercase. This fragment prints 0, because the strings are the same:

```c
printf("%d", strcmp("one", "one"));
```

The `strlen()` function returns the length, in characters, of a string. Its general form is

```c
strlen(str);
```

The `strlen()` function does not count the null terminator. This means that if `strlen()` is called using the string "test", it will return 4.

### EXAMPLES

1. This program requests input of two strings, then demonstrates the four string functions with them.

```c
#include <string.h>
#include <stdio.h>

int main(void)
{
    char str1[80], str2[80];
    int i;

    printf("Enter the first string: ");
    gets(str1);
    printf("Enter the second string: ");
    gets(str2);

    /* see how long the strings are */
    printf("%s is %d chars long\n", str1, strlen(str1));
    printf("%s is %d chars long\n", str2, strlen(str2));

    /* compare the strings */
    i = strcmp(str1, str2);
    if(!i) printf("The strings are equal.\n");
    else if(i<0) printf("%s is less than %s\n", str1, str2);
    else printf("%s is greater than %s\n", str1, str2);

    /* concatenate str2 to end of str1 if
       there is enough room */
    if(strlen(str1) + strlen(str2) < 80) {
        strcat(str1, str2);
        printf("%s\n", str1);
    }

    /* copy str2 to str1 */
    strcpy(str1, str2);
    printf("%s %s\n", str1, str2);

    return 0;
}
```

2. One common use of strings is to support a *command-based interface*. Unlike a menu, which allows the user to make a selection, a command-based interface displays a prompting message, waits for the user to enter a command, and then does what the command requests. Many operating systems, such as Windows or DOS, support command-line interfaces, for example. The following program is similar to a program developed in Section 3.1. It allows the user to add, subtract, multiply, or divide, but does not use a menu. Instead, it uses a command-based interface.

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char command[80], temp[80];
    int i, j;

    for( ; ; ) {
        printf("Operation? ");
        gets(command);

        /* see if user wants to stop */
        if(!strcmp(command, "quit")) break;

        printf("Enter first number: ");
        gets(temp);
        i = atoi(temp);

        printf("Enter second number: ");
        gets(temp);
        j = atoi(temp);

        /* now, perform the operation */
        if(!strcmp(command, "add"))
            printf("%d\n", i+j);
        else if(!strcmp(command, "subtract"))
            printf("%d\n", i-j);
        else if(!strcmp(command, "divide")) {
            if(j) printf("%d\n", i/j);
        }
        else if(!strcmp(command, "multiply"))
            printf("%d\n", i*j);
        else printf("Unknown command.\n");
    }

    return 0;
}
```

Notice that this example also introduces another of C's standard library functions: `atoi()`. The `atoi()` function returns the integer equivalent of the number represented by its string argument. For example, `atoi("100")` returns the value 100. The reason that `scanf()` is not used to read the numbers is because, in this context, it is incompatible with `gets()`. (You will need to know more about C before you can understand the cause of this incompatibility.) The `atoi()` function uses the header file STDLIB.H.

3. You can create a zero-length string using a `strcpy()` statement like this:

```c
strcpy(str, "");
```

Such a string is called a *null string*. It contains only one element: the null terminator.

### EXERCISES

1. Write a program that inputs a string, then displays it backward on the screen.
2. What is wrong with this program?

```c
#include <string.h>
#include <stdio.h>

int main(void)
{
    char str[5];

    strcpy(str, "this is a test");
    printf(str);

    return 0;
}
```

3. Write a program that repeatedly inputs strings. Each time a string is input, concatenate it with a second string called `bigstr`. Add newlines to the end of each string. If the user types **quit**, stop inputting and display `bigstr` (which will contain a record of all strings input). Also stop if `bigstr` will be overrun by the next concatenation.

---

## 5.3 CREATE MULTIDIMENSIONAL ARRAYS

In addition to one-dimensional arrays, you can create arrays of two or more dimensions. For example, to create a 10x12 two-dimensional integer array called `count`, you would use this statement:

```c
int count[10][12];
```

As you can see, to add a dimension, you simply specify its size inside square brackets.

A two-dimensional array is essentially an array of one-dimensional arrays and is most easily thought of in a row, column format. For example, given a 4x5 integer array called `two_d`, you can think of it looking like that shown in Figure 5-1. Assuming this conceptual view, a two-dimensional array is accessed a row at a time, from left to right. This means that the rightmost index will change most quickly when the array is accessed sequentially from the lowest to highest memory address.

#### FIGURE 5-1: A conceptual view of a 4x5 two-dimensional array

| | 0 | 1 | 2 | 3 | 4 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | [0][0] | [0][1] | [0][2] | [0][3] | [0][4] |
| **1** | [1][0] | [1][1] | [1][2] | [1][3] | [1][4] |
| **2** | [2][0] | [2][1] | [2][2] | [2][3] | [2][4] |
| **3** | [3][0] | [3][1] | [3][2] | [3][3] | [3][4] |

Two-dimensional arrays are used like one-dimensional ones. For example, this program loads a 4x5 array with the products of the indices, then displays the array in row, column format:

```c
#include <stdio.h>

int main(void)
{
    int twod[4][5];
    int i, j;

    for(i=0; i<4; i++)
        for(j=0; j<5; j++)
            twod[i][j] = i*j;

    for(i=0; i<4; i++) {
        for(j=0; j<5; j++)
            printf("%d ", twod[i][j]);
        printf("\n");
    }

    return 0;
}
```

The program output looks like this:

```
0 0 0 0 0 
0 1 2 3 4 
0 2 4 6 8 
0 3 6 9 12 
```

To create arrays of three dimensions or greater, simply add the size of the additional dimension. For example, the following statement creates a 10x12x8 three-dimensional array:

```c
float values[10][12][8];
```

A three-dimensional array is essentially an array of two-dimensional arrays.

You may create arrays of more than three dimensions, but this is seldom done because the amount of memory they consume increases exponentially with each additional dimension. For example, a 100-character one-dimensional array requires 100 bytes of memory. A 100x100 character array requires 10,000 bytes, and a 100x100x100 array requires 1,000,000 bytes. A 100x100x100x100 four-dimensional array would require 100,000,000 bytes of storage—large even by today's standards.

### EXAMPLE

1. A good use of a two-dimensional array is to manage lists of numbers. For example, you could use this two-dimensional array to hold the noontime temperature for each day of the year, grouped by month:

```c
float yeartemp[12][31];
```

In the same vein, the following program can be used to keep track of the number of points scored per quarter by each member of a basketball team.

```c
#include <stdio.h>

int main(void)
{
    int bball[4][5];
    int i, j;

    for(i=0; i<4; i++)
        for(j=0; j<5; j++) {
            printf("Quarter %d, player %d, ", i+1, j+1);
            printf("Enter number of points: ");
            scanf("%d", &bball[i][j]);
        }

    /* display results */
    for(i=0; i<4; i++)
        for(j=0; j<5; j++) {
            printf("Quarter %d, player %d, ", i+1, j+1);
            printf("%d\n", bball[i][j]);
        }

    return 0;
}
```

### EXERCISES

1. Write a program that defines a 3x3x3 three-dimensional array, and load it with the numbers 1 to 27.
2. Have the program from the first exercise display the sum of its elements.

---

## 5.4 INITIALIZE ARRAYS

Like other types of variables, you can give the elements of arrays initial values. This is accomplished by specifying a list of values the array elements will have. The general form of array initialization for one-dimensional arrays is shown here:

```c
type array-name[size] = {value-list};
```

The *value-list* is a comma-separated list of constants that are type compatible with the base type of the array. Moving from left to right, the first constant will be placed in the first position of the array, the second constant in the second position, and so on. Note that a semicolon follows the `}`. In the following example, a five-element integer array is initialized with the squares of the numbers 1 through 5:

```c
int i[5] = {1, 4, 9, 16, 25};
```

This means that `i[0]` will have the value 1 and `i[4]` will have the value 25.

You can initialize character arrays two ways. First, if the array is not holding a null-terminated string, you simply specify each character using a comma-separated list. For example, this initializes `a` with the letters 'A', 'B', and 'C':

```c
char a[3] = {'A', 'B', 'C'};
```

If the character array is going to hold a string, you can initialize the array using a quoted string, as shown here:

```c
char name[5] = "Herb";
```

Notice that no curly braces surround the string. They are not used in this form of initialization. Because strings in C must end with a null, you must make sure that the array you declare is long enough to include the null. This is why `name` is 5 characters long, even though "Herb" is only 4. When a string constant is used, the compiler automatically supplies the null terminator.

Multidimensional arrays are initialized in the same way as one-dimensional arrays. For example, here the array `sqr` is initialized with the values 1 through 9, using row order:

```c
int sqr[3][3] = {
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
};
```

This initialization causes `sqr[0][0]` to have the value 1, `sqr[0][1]` to contain 2, `sqr[0][2]` to hold 3, and so forth.

If you are initializing a one-dimensional array, you need not specify the size of the array—simply put nothing inside the square brackets. If you don't specify the size, the compiler counts the number of initializers and uses that value as the size of the array. For example,

```c
int pwr[] = {1, 2, 4, 8, 16, 32, 64, 128};
```

causes the compiler to create an initialized array eight elements long. Arrays that don't have their dimensions explicitly specified are called *unsized arrays*. An unsized array is useful because the size of the array will be automatically adjusted when you change the number of its initializers. It also helps avoid counting errors on long lists, which is especially important when initializing strings. For example, here an unsized array is used to hold a prompting message:

```c
char prompt[] = "Enter your name: ";
```

If, at a later date, you wanted to change the prompt to "Enter your last name:", you would not have to count the characters and then change the array size. The size of `prompt` would automatically be adjusted.

Unsized array initializations are not restricted to one-dimensional arrays. However, for multidimensional arrays you must specify all but the leftmost dimension to allow C to index the array properly. In this way you may build tables of varying lengths with the compiler allocating enough storage for them automatically. For example, the declaration of `sqr` as an unsized array is shown here:

```c
int sqr[][3] = {
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
};
```

The advantage to this declaration over the sized version is that tables may be lengthened or shortened without changing the array dimensions.

### EXAMPLES

1. A common use of an initialized array is to create a lookup table. For example, in this program a 5x2 two-dimensional array is initialized so that the first element in each row is the number of a file server in a network and the second element contains the number of users connected to that server. The program allows a user to enter the number of a server. It then looks up the server in the table and reports the number of users.

```c
#include <stdio.h>

int main(void)
{
    int ServerUsers[5][2] = {
        1, 14,
        2, 28,
        3, 19,
        4, 8,
        5, 15
    };

    int server;
    int i;

    printf("Enter the server number: ");
    scanf("%d", &server);

    /* look it up in the table */
    for(i=0; i<5; i++) {
        if(server == ServerUsers[i][0]) {
            printf("There are %d users on server %d.\n",
                   ServerUsers[i][1], server);
            break;
        }
    }

    /* report error if not found */
    if(i==5) printf("Server not listed.\n");

    return 0;
}
```

2. Even though an array has been given an initial value, its contents may be changed. For example, this program prints **hello** on the screen:

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[80] = "I like C";

    strcpy(str, "hello");
    printf(str);

    return 0;
}
```

As this program illustrates, in no way does an initialization fix the contents of an array.

### EXERCISES

1. Is this fragment correct?
```c
int balance[] = 10.0, 122.23, 100.0;
```
2. Is this fragment correct?
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[] = "Tom";

    strcpy(name, "Tom Brazwell");
}
```
3. Write a program that initializes a 10x3 array so that the first element of each row contains a number, the second element contains its square, and the third element contains its cube. Start with 1 and stop at 10. For example, the first few rows will look like this:
```
1, 1, 1,
2, 4, 8,
3, 9, 27,
4, 16, 64,
.
.
```
Next, prompt the user for a cube, look up this value in the table, and report the cube's root and the root's square. Use an unsized array so that the table size may be easily changed.

---

## 5.5 BUILD ARRAYS OF STRINGS

Arrays of strings, often called *string tables*, are very common in C programming. A string table is created like any other two-dimensional array. However, the way you think about it will be slightly different. For example, here is a small string table. What do you think it defines?

```c
char names[10][40];
```

This statement specifies a table that can contain 10 strings, each up to 40 characters long (including the null terminator). To access a string within this table, specify only the left-most index. For example, to read a string from the keyboard into the third string in `names`, use this statement:

```c
gets(names[2]);
```

By the same token, to output the first string, use this `printf()` statement:

```c
printf(names[0]);
```

The declaration that follows creates a three-dimensional table with three lists of strings. Each list is five strings long, and each string can hold 80 characters.

```c
char animals[3][5][80];
```

To access a specific string in this situation, you must specify the two left-most indexes. For example, to access the second string in the third list, specify `animals[2][1]`.

### EXAMPLES

1. This program lets you enter ten strings, then lets you display them, one at a time, in any order you choose. To stop the program, enter a negative number.

```c
#include <stdio.h>

int main(void)
{
    char text[10][80];
    int i;

    for(i=0; i<10; i++) {
        printf("%d: ", i+1);
        gets(text[i]);
    }

    do {
        printf("Enter number of string (1-10) : ");
        scanf("%d", &i);
        i--; /* adjust value to match array index */
        if(i>=0 && i<10) printf("%s\n", text[i]);
    } while(i>=0);

    return 0;
}
```

2. You can initialize a string table as you would any other type of array. For example, the following program uses an initialized string table to translate between German and English. Notice that curly braces are needed to surround the list. The only time they are not needed is when a single string is being initialized.

```c
/* English-to-German Translator. */

#include <stdio.h>
#include <string.h>

char words[][2][40] = {
    "dog", "Hund",
    "no", "nein",
    "year", "Jahr",
    "child", "Kind",
    "I", "Ich",
    "drive", "fahren",
    "house", "Haus",
    "to", "zu",
    "", ""
};

int main(void)
{
    char english[80];
    int i;

    printf("Enter English word: ");
    gets(english);

    /* look up the word */
    i = 0;
    /* search while null string not yet encountered */
    while(strcmp(words[i][0], "")) {
        if(!strcmp(english, words[i][0])) {
            printf("German translation: %s", words[i][1]);
            break;
        }
        i++;
    }
    if(!strcmp(words[i][0], ""))
        printf("Not in dictionary\n");

    return 0;
}
```

3. You can access the individual characters that comprise a string within a string table by using the rightmost index. For example, the following program prints the strings in the table one character at a time.

```c
#include <stdio.h>

int main(void)
{
    char text[][80] = {
        "When", "in", "the",
        "course", "of", "human",
        "events", ""
    };

    int i, j;

    /* now, display them */
    for(i=0; text[i][0]; i++) {
        for(j=0; text[i][j]; j++)
            printf("%c", text[i][j]);
        printf(" ");
    }

    return 0;
}
```

### EXERCISE

1. Write a program that creates a string table containing the English words for the numbers 0 through 9. Using this table, allow the user to enter a digit (as a character) and then have your program display the word equivalent. (Hint: to obtain an index into the table, subtract '0' from the character entered.)

---

## Mastery Skills Check

At this point you should be able to perform these exercises and answer these questions:

1. What is an array?
2. Given the array
```c
int count[10];
```
will this statement generate an error message?
```c
for(i=0; i<20; i++) count[i] = i;
```
3. In statistics, the *mode* of a group of numbers is the one that occurs the most often. For example, given the list 1, 2, 3, 6, 4, 7, 5, 4, 6, 9, 4, the mode is 4, because it occurs three times. Write a program that allows the user to enter a list of 20 numbers and then finds and displays the mode.
4. Show how to initialize an integer array called `items` with the values 1 through 10.
5. Write a program that repeatedly reads strings from the keyboard until the user enters **quit**.
6. Write a program that acts like an electronic dictionary. If the user enters a word in the dictionary, the program displays its meaning. Use a three-dimensional character array to hold the words and their meanings.

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. Write a program that inputs strings from the user. If the string is less than 80 characters long, pad it with periods. Print out the string to verify that you have correctly lengthened the string.
2. Write a program that inputs a string and then encodes it by taking the characters from each end, starting with the left side and alternating, stopping when the middle of the string has been reached. For example, the string "Hi there" would be "Heir eth".
3. Write a program that counts the number of spaces, commas, and periods in a string. Use a `switch` to categorize the characters.
4. What is wrong with this fragment?
```c
char str[80];
str = getchar();
```
5. Write a program that plays a computerized version of Hangman. In the game of Hangman, you are shown the length of a magic word (using hyphens) and you try to guess what the word is by entering letters. Each time you enter a letter, the magic word is checked to see if it contains that letter. If it does, that letter is shown. Keep a count on the number of letters entered to complete the word. For the sake of simplicity, a player wins when the magic word is entirely filled by characters using 15 or fewer guesses. For this exercise make the magic word "concatenation."
