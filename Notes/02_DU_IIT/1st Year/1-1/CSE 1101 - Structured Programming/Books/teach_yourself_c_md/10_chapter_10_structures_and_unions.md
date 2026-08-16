# 10 Structures and Unions

IN this chapter you will learn about two of C's most important user-defined types: the *structure* and the *union*.

---

### Review Skills Check

Before proceeding you should be able to answer these questions and perform these exercises:

1. Write a program that copies a file. Have the user specify both the source and destination file names on the command line. Include full error checking.
2. Write a program using `fprintf()` to create a file that contains this information:
`this is a string 1230.23 1FFF A`
Use a string, a double, a hexadecimal integer, and character format specifiers and values.
3. Write a program that contains a 20-element integer array. Initialize the array so that it contains the numbers 1 through 20. Using only one `fwrite()` statement, save this array to a file called TEMP.
4. Write a program that reads the TEMP file created in Exercise 3 into an integer array using only one `fread()` statement. Display the contents of the array.
5. What are **stdin**, **stdout**, and **stderr**?
6. How do functions like `printf()` and `scanf()` relate to the C file system?

---

## 10.1 MASTER STRUCTURE BASICS

A *structure* is an aggregate (or conglomerate) data type that is composed of two or more related variables called *members*. Unlike an array in which each element is of the same type, each member of a structure can have its own type, which may differ from the types of the other members. Structures are defined in C using this general form:

```c
struct tag-name {
    type member1;
    type member2;
    type member3;
    .
    .
    .
    type memberN;
} variable-list;
```

The keyword `struct` tells the compiler that a structure type is being defined. Each *type* is a valid C type. The *tag-name* is essentially the type name of the structure, and the *variable-list* is where actual instances of the structure are declared. Either the *tag-name* or the *variable-list* is optional, but one must be present (you will see why shortly). The members of a structure are also commonly referred to as *fields* or *elements*. This book will use these terms interchangeably.

Generally, the information contained in a structure is logically related. For example, you might use a structure to hold a person's address. Another structure might be used to support an inventory program in which each item's name, retail and wholesale cost, and the quantity on hand are stored. The structure shown here defines fields that can hold card-catalog information:

```c
struct catalog {
    char name[40];    /* author name */
    char title[40];   /* title */
    char pub[40];     /* publisher */
    unsigned date;    /* copyright date */
    unsigned char ed; /* edition */
} card;
```

Here, `catalog` is the type name of the structure. It is not the name of a variable. The only variable defined by this fragment is `card`. It is important to understand that a structure declaration defines only a logical entity, which is a new data type. It is not until variables of that type are declared than an object of that type actually exists. Thus, `catalog` is a logical template; `card` has physical reality. Figure 10-1 shows how this structure will appear in memory (using 2-byte integers).

```
FIGURE 10-1
How the card structure variable appears in memory (assuming 2-byte integers)

+----------+----------+
| name     | 40 bytes |
+----------+----------+
| title    | 40 bytes |
+----------+----------+
| pub      | 40 bytes |
+----------+----------+
| date     |  2 bytes |
+----------+----------+
| ed       |  1 byte  |
+----------+----------+
```

To access a member of a structure, you must specify both the structure variable name and the member name, separated by a period. For example, using `card`, the following statement assigns the `date` field the value 1776:

```c
card.date = 1776;
```

C programmers often refer to the period as the *dot operator*. To print the copyright date, you can use a statement such as:

```c
printf("Copyright date: %u", card.date);
```

To input the date, use a `scanf()` statement such as:

```c
scanf("%u", &card.date);
```

Notice that the `&` goes before the structure name, not before the member name. (In a similar fashion, these statements input the author's name and output the title:

```c
gets(card.name);
printf("%s", card.title);
```

To access an individual character in the title field, simply index `title`. For example, the following statement prints the third letter:

```c
printf("%c", card.title[2]);
```

Once you have defined a structure type, you can create additional variables of that type using this general form:

```c
struct tag_name var_list;
```

Assuming, for example, that `catalog` has been defined as shown earlier in this section, this statement declares three variables of type **struct catalog**:

```c
struct catalog var1, var2, var3;
```

This is why it is not necessary to declare any variables when the structure type is defined. You can declare them separately, as needed.

A key concept to understand is that each instance of a structure contains its own copy of the members of the structure. For example, given the preceding declaration, the `title` field of `var1` is completely separate from the `title` field of `var2`. (In fact, the only relationship that `var1`, `var2`, and `var3` have with one another is that they are all variables of the same type of structure. There is no other linkage among the three.)

If you know you only need a fixed number of structure variables, you do not need to specify the tag name. For example, this code creates two structure variables, but the structure itself is unnamed:

```c
struct {
    int a;
    char ch;
} var1, var2;
```

In actual practice, however, you will usually want to specify the tag name.

Structures can be arrayed in the same fashion as other data types. For example, the following structure definition creates a 100-element array of structures of type `catalog`:

```c
struct catalog cat[100];
```

To access an individual structure of the array, you must index the array name. For example, the following accesses the first structure:

```c
cat[0]
```

To access a member within a specified structure, follow the index with a period and the name of the member you want. For example, the following statement loads the `ed` field of structure 33 with the value of 2:

```c
cat[33].ed = 2;
```

Structures may be passed as parameters to functions just like any other type of value. A function may also return a structure.

You may assign the contents of one instance of a structure to another as long as they are both of the same type. For example, this fragment is perfectly valid:

```c
struct s_type {
    int a;
    float f;
} var1, var2;

var1.a = 10;
var1.f = 100.23;

var2 = var1;
```

After this fragment executes, `var2` will contain exactly the same thing as `var1`.

### EXAMPLES

1. This program demonstrates some ways to access structure members:

```c
#include <stdio.h>

struct s_type {
    int i;
    char ch;
    double d;
    char str[80];
} s;

int main(void)
{
    printf("Enter an integer: ");
    scanf("%d", &s.i);
    printf("Enter a character: ");
    scanf(" %c", &s.ch);
    printf("Enter a floating point number: ");
    scanf("%lf", &s.d);
    printf("Enter a string: ");
    scanf("%s", s.str);

    printf("%d %c %f %s", s.i, s.ch, s.d, s.str);

    return 0;
}
```

2. When you need to know the size of a structure, you should use the `sizeof` compile-time operator. Do not try to manually add up the number of bytes in each field. There are three good reasons for this. First, as you learned in the preceding chapter, using `sizeof` ensures that your code is portable to different environments. Second, in some situations, the compiler may need to align certain types of data on even word boundaries. In this case, the size of the structure will be larger than the sum of its individual elements. Finally, for computers based on the 8086 family of CPUs (such as the 80486 or the Pentium), there are several different ways the compiler can organize memory. Some of these ways cause pointers to take up twice the space they do when memory is arranged differently.

When using `sizeof` with a structure type, you must precede the tag name with the keyword `struct`, as shown in this program:

```c
#include <stdio.h>

struct s_type {
    int i;
    char ch;
    int *p;
    double d;
} s;

int main(void)
{
    printf("s_type is %d bytes long", sizeof(struct s_type));

    return 0;
}
```

3. To see how useful arrays of structures are, examine an improved version of the card-catalog program developed in the preceding two chapters. Notice how using a structure makes it easier to organize the information about each book. Also notice how the entire structure array is written and read from disk in a single operation.

```c
/* An electronic card catalog. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

int menu(void);
void display(int i);
void author_search(void);
void title_search(void);
void enter(void);
void save(void);
void load(void);

struct catalog {
    char name[80];       /* author name */
    char title[80];      /* title */
    char pub[80];        /* publisher */
    unsigned date;       /* copyright date */
    unsigned char ed;    /* edition */
} cat[MAX];

int top = 0; /* last location used */

int main(void)
{
    int choice;

    load(); /* read in catalog */

    do {
        choice = menu();
        switch(choice) {
            case 1: enter(); /* enter books */
                break;
            case 2: author_search(); /* search by author */
                break;
            case 3: title_search(); /* search by title */
                break;
            case 4: save();
        }
    } while(choice!=5);

    return 0;
}

/* Return a menu selection. */
int menu(void)
{
    int i;
    char str[80];

    printf("Card catalog:\n");
    printf(" 1. Enter\n");
    printf(" 2. Search by Author\n");
    printf(" 3. Search by Title\n");
    printf(" 4. Save catalog\n");
    printf(" 5. Quit\n");

    do {
        printf("Choose your selection: ");
        gets(str);
        i = atoi(str);
        printf("\n");
    } while(i<1 || i>5);

    return i;
}

/* Enter books into database. */
void enter(void)
{
    int i;
    char temp[80];

    for(i=top; i<MAX; i++) {
        printf("Enter author name (ENTER to quit): ");
        gets(cat[i].name);
        if(!*cat[i].name) break;
        printf("Enter title: ");
        gets(cat[i].title);
        printf("Enter publisher: ");
        gets(cat[i].pub);
        printf("Enter copyright date: ");
        gets(temp);
        cat[i].date = (unsigned) atoi(temp);
        printf("Enter edition: ");
        gets(temp);
        cat[i].ed = (unsigned char) atoi(temp);
    }
    top = i;
}

/* Search by author. */
void author_search(void)
{
    char name[80];
    int i, found;

    printf("Name: ");
    gets(name);

    found = 0;
    for(i=0; i<top; i++)
        if(!strcmp(name, cat[i].name)) {
            display(i);
            found = 1;
            printf("\n");
        }

    if(!found) printf("Not Found\n");
}

/* Search by title. */
void title_search(void)
{
    char title[80];
    int i, found;

    printf("Title: ");
    gets(title);

    found = 0;
    for(i=0; i<top; i++)
        if(!strcmp(title, cat[i].title)) {
            display(i);
            found = 1;
            printf("\n");
        }

    if(!found) printf("Not Found\n");
}

/* Display catalog entry. */
void display(int i)
{
    printf("%s\n", cat[i].title);
    printf("by %s\n", cat[i].name);
    printf("Published by %s\n", cat[i].pub);
    printf("Copyright: %u, %u edition\n", cat[i].date,
            cat[i].ed);
}

/* Load the catalog file. */
void load(void)
{
    FILE *fp;

    if((fp = fopen("catalog", "rb"))==NULL) {
        printf("Catalog file not on disk.\n");
        return;
    }

    if(fread(&top, sizeof top, 1, fp) != 1) { /* read count */
        printf("Error reading count.\n");
        exit(1);
    }
    if(fread(cat, sizeof cat, 1, fp) != 1) { /* read data */
        printf("Error reading catalog data.\n");
        exit(1);
    }

    fclose(fp);
}

/* Save the catalog file. */
void save(void)
{
    FILE *fp;

    if((fp = fopen("catalog", "wb"))==NULL) {
        printf("Cannot open catalog file.\n");
        exit(1);
    }

    if(fwrite(&top, sizeof top, 1, fp) != 1) { /* write count */
        printf("Error writing count.\n");
        exit(1);
    }
    if(fwrite(cat, sizeof cat, 1, fp) != 1) { /* write data */
        printf("Error writing catalog data.\n");
        exit(1);
    }

    fclose(fp);
}
```

4. In the preceding example, the entire catalog array is stored on disk, even if the array is not full. If you like, you can change the `load()` and `save()` routines as follows, so that only structures actually holding data are stored on disk:

```c
/* Load the catalog file. */
void load(void)
{
    FILE *fp;
    int i;

    if((fp = fopen("catalog", "rb"))==NULL) {
        printf("Catalog file not on disk.\n");
        return;
    }

    if(fread(&top, sizeof top, 1, fp) != 1) { /* read count */
        printf("Error reading count.\n");
        exit(1);
    }
    for(i=0; i<=top; i++) /* read data */
        if(fread(&cat[i], sizeof(struct catalog), 1, fp) != 1) {
            printf("Error reading catalog data.\n");
            exit(1);
        }

    fclose(fp);
}

/* Save the catalog file. */
void save(void)
{
    FILE *fp;
    int i;

    if((fp = fopen("catalog", "wb"))==NULL) {
        printf("Cannot open catalog file.\n");
        exit(1);
    }

    if(fwrite(&top, sizeof top, 1, fp) != 1) { /* write count */
        printf("Error writing count.\n");
        exit(1);
    }
    for(i=0; i<=top; i++) /* write data */
        if(fwrite(&cat[i], sizeof(struct catalog), 1, fp) != 1) {
            printf("Error writing catalog data.\n");
            exit(1);
        }

    fclose(fp);
}
```

5. The names of structure members will not conflict with other variables using the same names. Because the member name is linked with the structure name, it is separate from other variables of the same name. For example, this program prints **10 100 101** on the screen.

```c
#include <stdio.h>

int main(void)
{
    struct s_type {
        int i;
        int j;
    } s;

    int i;

    i = 10;
    s.i = 100;
    s.j = 101;

    printf("%d %d %d", i, s.i, s.j);

    return 0;
}
```

The variable `i` and the structure member `i` have no relationship to each other.

6. As stated earlier, a function may return a structure to the calling procedure. The following program, for example, loads the members of `var1` with the values 100 and 123.23 and then displays them on the screen:

```c
#include <stdio.h>

struct s_type {
    int i;
    double d;
};

struct s_type f(void);

int main(void)
{
    struct s_type var1;

    var1 = f();
    printf("%d %f", var1.i, var1.d);

    return 0;
}

struct s_type f(void)
{
    struct s_type temp;

    temp.i = 100;
    temp.d = 123.23;

    return temp;
}
```

7. This program passes a structure to a function:

```c
#include <stdio.h>

struct s_type {
    int i;
    double d;
};

void f(struct s_type temp);

int main(void)
{
    struct s_type var1;

    var1.i = 99;
    var1.d = 98.6;
    f(var1);

    return 0;
}

void f(struct s_type temp)
{
    printf("%d %f", temp.i, temp.d);
}
```

### EXERCISES

1. In Chapter 9, you wrote a program that created a telephone directory that was stored on disk. Improve the program so that it uses an array of structures, each containing a person's name, area code, and telephone number. Store the area code as an integer. Store the name and telephone number as strings. Make the array MAX elements long, where MAX is any convenient value that you choose.
2. What is wrong with this fragment?
```c
struct s_type {
    int i;
    long l;
    char str[80];
} s;

.
.
.
i = 10;
```
3. On your own, examine the header file STDIO.H and look at how the `FILE` structure is defined.

---

## 10.2 DECLARE POINTERS TO STRUCTURES

It is very common to access a structure through a pointer. You declare a pointer to a structure in the same way that you declare a pointer to any other type of variable. For example, the following fragment defines a structure called `s_type` and declares two variables. The first, `s`, is an actual structure variable. The second, `p`, is a pointer to structures of type `s_type`.

```c
struct s_type {
    int i;
    char str[80];
} s, *p;
```

Given this definition, the following statement assigns to `p` the address of `s`:

```c
p = &s;
```

Now that `p` points to `s` you can access `s` through `p`. However, to access an individual element of `s` using `p` you cannot use the dot operator. Instead, you must use the *arrow operator*, as shown in the following example:

```c
p->i = 1;
```

This statement assigns the value 1 to element `i` of `s` through `p`. The arrow operator is formed using a minus sign followed by a greater-than sign. There must be no spaces between the two.

C passes structures to functions in their entirety. However, if the structure is very large, the passing of a structure can cause a considerable reduction in a program's execution speed. For this reason, when working with large structures, you might want to pass a pointer to a structure in situations that allow it instead of passing the structure itself.

> [!TIP]
> When accessing a member using a structure variable, use the dot operator. When accessing a member using a pointer, use the arrow operator.

### EXAMPLES

1. The following program illustrates how to use a pointer to a structure:

```c
#include <stdio.h>
#include <string.h>

struct s_type {
    int i;
    char str[80];
} s, *p;

int main(void)
{
    p = &s;

    s.i = 10; /* this is functionally the same */
    p->i = 10; /* as this */
    strcpy(p->str, "I like structures.");

    printf("%d %d %s", s.i, p->i, p->str);

    return 0;
}
```

2. One very useful application of structure pointers is found in C's time and date functions. Several of these functions use a pointer to the current time and date of the system. Several of these functions require the header file TIME.H, in which a structure called `tm` is defined. This structure can hold the date and time broken down into its elements. This is called the *broken-down time*. The `tm` structure is defined as follows:

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

The value of `tm_isdst` will be positive if Daylight Saving Time is in effect, zero if it is not in effect, and negative if there is no information available. Also defined in TIME.H is the type `time_t`. It is essentially a **long integer** capable of representing the time and date of the system in an encoded implementation-specific internal format. This is referred to as the *calendar time*. To obtain the calendar time of the system, you must use the `time()` function, whose prototype is:

```c
time_t time(time_t *systime);
```

The `time()` function returns the encoded calendar time of the system or -1 if no system time is available. It also places this encoded form of the time into the variable pointed to by *systime*. However, if *systime* is null, the argument is ignored.

Since the calendar time is represented using an implementation-specified internal format, you must use another of C's time and date functions to convert it into a form that is easier to use. One of these functions is called `localtime()`. Its prototype is

```c
struct tm *localtime(time_t *systime);
```

The `localtime()` function returns a pointer to the broken-down form of *systime*. The structure that holds the broken-down time is internally allocated by the compiler and will be overwritten by each subsequent call.

This program demonstrates `time()` and `localtime()` by displaying the current time of the system:

```c
#include <stdio.h>
#include <time.h>

int main(void)
{
    struct tm *systime;
    time_t t;

    t = time(NULL);
    systime = localtime(&t);

    printf("Time is %.2d:%.2d:%.2d\n", systime->tm_hour,
            systime->tm_min, systime->tm_sec);
    printf("Date: %.2d/%.2d/%.2d", systime->tm_mon+1,
            systime->tm_mday, systime->tm_year);

    return 0;
}
```

Here is sample output produced by this program:

```
Time is 10:32:49
Date: 03/15/97
```

### EXERCISES

1. Is this program fragment correct?
```c
struct s_type {
    int a;
    int b;
} s, *p;

int main(void)
{
    p = &s;

    p.a = 100;
```
2. Another of C's time and date functions is called `gmtime()`. Its prototype is
```c
struct tm *gmtime(time_t *time);
```
The `gmtime()` function works exactly like `localtime()`, except that it returns the Coordinated Universal Time (which is, essentially, Greenwich Mean Time) of the system. Change the program in Example 2 so that it displays both local time and Coordinated Universal Time. (Note: Coordinated Universal Time may not be available on your system.)

---

## 10.3 WORK WITH NESTED STRUCTURES

So far, we have only been working with structures whose members consist solely of C's basic types. However, members can also be other structures. These are referred to as *nested structures*. Here is an example that uses nested structures to hold information on the performance of two assembly lines, each with ten workers:

```c
#define NUM_ON_LINE 10

struct worker {
    char name[80];
    int avg_units_per_hour;
    int avg_errs_per_hour;
};

struct asm_line {
    int product_code;
    double material_cost;
    struct worker wkers[NUM_ON_LINE];
} line1, line2;
```

To assign the value 12 to the `avg_units_per_hour` of the second `wkers` structure of `line1`, use this statement:

```c
line1.wkers[1].avg_units_per_hour = 12;
```

As you see, the structures are accessed from the outer to the inner. This is also the general case. Whenever you have nested structures, you begin with the outermost and end with the innermost.

### EXAMPLE

1. A nested structure can be used to improve the card catalog program. Here, the mechanical information about each book is stored in its own structure, which, in turn, is part of the catalog structure. The entire catalog program using this approach is shown here. Notice how the program now stores the length of the book in pages.

```c
/* An electronic card catalog--3rd Improvement. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

int menu(void);
void display(int i);
void author_search(void);
void title_search(void);
void enter(void);
void save(void);
void load(void);

struct book_type {
    unsigned date;       /* copyright date */
    unsigned char ed;    /* edition */
    unsigned pages;      /* length of book */
};

struct catalog {
    char name[80];       /* author name */
    char title[80];      /* title */
    char pub[80];        /* publisher */
    struct book_type book; /* mechanical info */
} cat[MAX];

int top = 0; /* last location used */

int main(void)
{
    int choice;

    load(); /* read in catalog */

    do {
        choice = menu();
        switch(choice) {
            case 1: enter(); /* enter books */
                break;
            case 2: author_search(); /* search by author */
                break;
            case 3: title_search(); /* search by title */
                break;
            case 4: save();
        }
    } while(choice!=5);

    return 0;
}

/* Return a menu selection. */
int menu(void)
{
    int i;
    char str[80];

    printf("Card catalog:\n");
    printf(" 1. Enter\n");
    printf(" 2. Search by Author\n");
    printf(" 3. Search by Title\n");
    printf(" 4. Save catalog\n");
    printf(" 5. Quit\n");

    do {
        printf("Choose your selection: ");
        gets(str);
        i = atoi(str);
        printf("\n");
    } while(i<1 || i>5);

    return i;
}

/* Enter books into database. */
void enter(void)
{
    int i;
    char temp[80];

    for(i=top; i<MAX; i++) {
        printf("Enter author name (ENTER to quit): ");
        gets(cat[i].name);
        if(!*cat[i].name) break;
        printf("Enter title: ");
        gets(cat[i].title);
        printf("Enter publisher: ");
        gets(cat[i].pub);
        printf("Enter copyright date: ");
        gets(temp);
        cat[i].book.date = (unsigned) atoi(temp);
        printf("Enter edition: ");
        gets(temp);
        cat[i].book.ed = (unsigned char) atoi(temp);
        printf("Enter number of pages: ");
        gets(temp);
        cat[i].book.pages = (unsigned) atoi(temp);
    }
    top = i;
}

/* Search by author. */
void author_search(void)
{
    char name[80];
    int i, found;

    printf("Name: ");
    gets(name);

    found = 0;
    for(i=0; i<top; i++)
        if(!strcmp(name, cat[i].name)) {
            display(i);
            found = 1;
            printf("\n");
        }

    if(!found) printf("Not Found\n");
}

/* Search by title. */
void title_search(void)
{
    char title[80];
    int i, found;

    printf("Title: ");
    gets(title);

    found = 0;
    for(i=0; i<top; i++)
        if(!strcmp(title, cat[i].title)) {
            display(i);
            found = 1;
            printf("\n");
        }

    if(!found) printf("Not Found\n");
}

/* Display catalog entry. */
void display(int i)
{
    printf("%s\n", cat[i].title);
    printf("by %s\n", cat[i].name);
    printf("Published by %s\n", cat[i].pub);
    printf("Copyright: %u, edition: %u\n",
            cat[i].book.date, cat[i].book.ed);
    printf("Pages: %u\n", cat[i].book.pages);
}

/* Load the catalog file. */
void load(void)
{
    FILE *fp;

    if((fp = fopen("catalog", "rb"))==NULL) {
        printf("Catalog file not on disk.\n");
        return;
    }

    if(fread(&top, sizeof top, 1, fp) != 1) { /* read count */
        printf("Error reading count.\n");
        exit(1);
    }
    if(fread(cat, sizeof cat, 1, fp) != 1) { /* read data */
        printf("Error reading catalog data.\n");
        exit(1);
    }

    fclose(fp);
}

/* Save the catalog file. */
void save(void)
{
    FILE *fp;

    if((fp = fopen("catalog", "wb"))==NULL) {
        printf("Cannot open catalog file.\n");
        exit(1);
    }

    if(fwrite(&top, sizeof top, 1, fp) != 1) { /* write count */
        printf("Error writing count.\n");
        exit(1);
    }
    if(fwrite(cat, sizeof cat, 1, fp) != 1) { /* write data */
        printf("Error writing catalog data.\n");
        exit(1);
    }

    fclose(fp);
}
```

### EXERCISE

1. Improve the telephone-directory program you wrote earlier in this chapter so that it includes each person's mailing address. Store the address in its own structure, called **address**, which is nested inside the directory structure.

---

## 10.4 UNDERSTAND BIT-FIELDS

C allows a variation on a structure member called a *bit-field*. A bit-field is composed of one or more bits. Using a bit-field, you can access by name one or more bits within a byte or word. To define a bit-field, use this general form:

```c
type name : size;
```

Here, *type* is either **int** or **unsigned**. If you specify a signed bit-field, then the high-order bit is treated as a sign bit, if possible. The number of bits in the field is specified by *size*. Notice that a colon separates the name of the bit-field from its size in bits.

Bit-fields are useful when you want to pack information into the smallest possible space. For example, here is a structure that uses bit-fields to hold inventory information.

```c
struct b_type {
    unsigned department: 3; /* up to 7 departments */
    unsigned instock: 1;    /* 1 if in stock, 0 if out */
    unsigned backordered: 1;/* 1 if backordered, 0 if not */
    unsigned lead_time: 3;  /* order lead time in months */
} inv[MAX_ITEM];
```

In this case one byte can be used to store information on an inventory item that would normally have taken four bytes without the use of bit-fields. You refer to a bit-field just like any other member of a structure. The following statement, for example, assigns the value 3 to the `department` field of item 10:

```c
inv[9].department = 3;
```

The following statement determines whether item 5 is out of stock:

```c
if(!inv[4].instock) printf("Out of Stock");
else printf("In Stock");
```

It is not necessary to completely define all bits within a byte or word. For example, this is perfectly valid:

```c
struct b_type {
    int a: 2;
    int b: 3;
};
```

The C compiler is free to store bit-fields as it sees fit. However, usually the compiler will automatically store bit-fields in the smallest unit of memory that will hold them. Whether the bit-fields are stored high-order to low-order or the other way around is implementation-dependent. However, many compilers use high-order to low-order.

You can mix bit-fields with other types of members in a structure's definition. For example, this version of the inventory structure also includes room for the name of each item:

```c
struct b_type {
    char name[40];          /* name of item */
    unsigned department: 3; /* up to 7 departments */
    unsigned instock: 1;    /* 1 if in stock, 0 if not */
    unsigned backordered: 1;/* 1 if backordered, 0 if not */
    unsigned lead_time: 3;  /* order lead time in months */
} inv[MAX_ITEM];
```

Because the smallest addressable unit of memory is a byte, you cannot obtain the address of a bit-field variable.

Bit-fields are often used to store Boolean (true/false) data because they allow the efficient use of memory—remember, you can pack eight Boolean values into a single byte.

### EXAMPLES

1. It is not necessary to name every bit when using bit-fields. Here, for example, is a structure that uses bit-fields to access the first and last bit in a byte.

```c
struct b_type {
    unsigned first: 1;
    int : 6;
    unsigned last: 1;
};
```

The use of unnamed bit-fields makes it easy to reach the bits you are interested in.

2. To see how useful bit-fields can be when working with Boolean data, here is a crude simulation of a spaceship flight recorder. By packing all the relevant information into one byte, comparatively little disk space is used to record a flight.

```c
/* Simulation of a 100 minute spaceship flight recorder. */
#include <stdlib.h>
#include <stdio.h>

/* all fields indicate OK if 1, malfunctioning or low if 0 */
struct telemetry {
    unsigned fuel: 1;
    unsigned radio: 1;
    unsigned tv: 1;
    unsigned water: 1;
    unsigned food: 1;
    unsigned waste: 1;
} flt_recd;

void display(struct telemetry i);

int main(void)
{
    FILE *fp;
    int i;

    if((fp = fopen("flight", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* Imagine that each minute a status report of
       the spaceship is recorded on disk. */
    for(i=0; i<100; i++) {
        flt_recd.fuel = rand()%2;
        flt_recd.radio = rand()%2;
        flt_recd.tv = rand()%2;
        flt_recd.water = rand()%2;
        flt_recd.food = rand()%2;
        flt_recd.waste = rand()%2;

        display(flt_recd);
        fwrite(&flt_recd, sizeof flt_recd, 1, fp);
    }

    fclose(fp);

    return 0;
}

void display(struct telemetry i)
{
    if(i.fuel) printf("Fuel OK\n");
    else printf("Fuel low\n");
    if(i.radio) printf("Radio OK\n");
    else printf("Radio failure\n");
    if(i.tv) printf("TV system OK\n");
    else printf("TV malfunction\n");
    if(i.water) printf("Water supply OK\n");
    else printf("Water supply low\n");
    if(i.food) printf("Food supply OK\n");
    else printf("Food supply low\n");
    if(i.waste) printf("Waste containment OK\n");
    else printf("Waste containment failure\n");
    printf("\n");
}
```

Depending on how your compiler packs the bit-fields, after you run this program, the file on disk may be as short as 100 bytes long. Now try the program after modifying the telemetry structure as shown here:

```c
struct telemetry {
    char fuel;
    char radio;
    char tv;
    char water;
    char food;
    char waste;
} flt_recd;
```

In this version, no bit-fields are used and the resulting file is at least 600 bytes long. As you can see, using bit-fields can provide substantial space savings.

### EXERCISES

1. Write a program that creates a structure that contains three bit-fields called **a**, **b**, and **c**. Make **a** and **b** three bits long and make **c** two bits long. Next, assign each a value and display the values.
2. Many compilers supply library functions that return the status of various hardware devices, such as a serial port or the keyboard, by encoding information in a bit-by-bit fashion. On your own, consult the user's manual for your compiler to see if it supports such functions. If it does, write some programs that read and decode the status of one or more devices.

---

## 10.5 CREATE UNIONS

In C, a union is a single piece of memory that is shared by two or more variables. The variables that share the memory may be of different types. However, only one variable may be in use at any one time. A union is defined much like a structure. Its general form is

```c
union tag-name {
    type member1;
    type member2;
    type member3;
    .
    .
    .
    type memberN;
} variable-names;
```

Like a structure, either the *tag-name* or the *variable-names* may be missing. Members may be of any valid C data type. For example, here is a union that contains three elements: an integer, a character array, and a double:

```c
union u_type {
    int i;
    char c[2];
    double d;
} sample;
```

This union will appear in memory as shown in Figure 10-2.

```
FIGURE 10-2
How an instance of the union u_type appears in memory (assuming 2-byte ints and 8-byte doubles)

  |<- c[0] + c[1] ->|
  +--------+--------+--------+--------+--------+--------+--------+--------+
  |        |        |        |        |        |        |        |        |
  +--------+--------+--------+--------+--------+--------+--------+--------+
  |<-      i      ->|
  |<-                             d                                    ->|
```

To access a member of a union, use the dot and arrow operators just as you do for structures. For example, this statement assigns 123.098 to **d** of **sample**:

```c
sample.d = 123.098;
```

If you are accessing a union through a pointer, you must use the arrow operator. For example, assume that **p** points to **sample**. The following statement assigns **i** the value 101:

```c
p->i = 101;
```

It is important to understand that the size of a union is fixed at compile time and is large enough to accommodate the largest member of the union. Assuming 8-byte doubles, this means that **sample** will be 8 bytes long. Even if **sample** is currently used to hold an **int** value, it will still occupy 8 bytes of memory. As is the case with structures, you should use the `sizeof` compile-time operator to determine the size of a union. You should not simply assume that it will be the size of the largest element, because in some environments, the compiler may pad the union so that it aligns on a word boundary.

### EXAMPLES

1. Unions are very useful when you need to interpret data in two or more different ways. For example, the `encode()` function shown below uses a union to encode an integer by swapping its two low-order bytes. The same function can also be used to decode an encoded integer by swapping the already exchanged bytes back to their original positions.

```c
#include <stdio.h>

int encode(int i);

int main(void)
{
    int i;

    i = encode(10); /* encode it */
    printf("10 encoded is %d\n", i);
    i = encode(i); /* decode it */
    printf("i decoded is %d", i);

    return 0;
}

/* Encode an integer, decode an encoded integer. */
int encode(int i)
{
    union crypt_type {
        int num;
        char c[2];
    } crypt;
    unsigned char ch;

    crypt.num = i;

    /* swap bytes */
    ch = crypt.c[0];
    crypt.c[0] = crypt.c[1];
    crypt.c[1] = ch;

    /* return encoded integer */
    return crypt.num;
}
```

The program displays the following:

```
10 encoded is 2560
i decoded is 10
```

2. The following program uses the union of a structure containing bit-fields and a character to display the binary representation of a character typed at the keyboard:

```c
/* This program displays the binary code for a
   character entered at the keyboard. */
#include <stdio.h>
#include <conio.h>

struct sample {
    unsigned a: 1;
    unsigned b: 1;
    unsigned c: 1;
    unsigned d: 1;
    unsigned e: 1;
    unsigned f: 1;
    unsigned g: 1;
    unsigned h: 1;
};

union key_type {
    char ch;
    struct sample bits;
} key;

int main(void)
{
    printf("Strike a key: ");

    key.ch = getche();
    printf("\nBinary code is: ");

    if(key.bits.h) printf("1 ");
    else printf("0 ");
    if(key.bits.g) printf("1 ");
    else printf("0 ");
    if(key.bits.f) printf("1 ");
    else printf("0 ");
    if(key.bits.e) printf("1 ");
    else printf("0 ");
    if(key.bits.d) printf("1 ");
    else printf("0 ");
    if(key.bits.c) printf("1 ");
    else printf("0 ");
    if(key.bits.b) printf("1 ");
    else printf("0 ");
    if(key.bits.a) printf("1 ");
    else printf("0 ");

    return 0;
}
```

When a key is pressed, its ASCII code is assigned to `key.ch`, which is a **char**. This data is reinterpreted as a series of bit-fields, which allow the binary representation of the key to be displayed. Sample output is shown here:

```
Strike a key: X
Binary code is: 0 1 0 1 1 0 0 0
```

### EXERCISES

1. Using a union composed of a **double** and an 8-byte character array, write a function that writes a **double** to a disk file, a character at a time. Write another function that reads this value from the file and reconstructs the value using the same union. (Note: If the length of a **double** for your compiler is not 8 bytes, use an appropriately sized character array.)
2. Write a program that uses a union to convert an **int** into a **long**. Demonstrate that it works.

---

## Mastery Skills Check

At this point you should be able to answer these questions and perform these exercises:

1. In general terms what is a structure, and what is a union?
2. Show how to create a structure type called `s_type` that contains these five members:
```c
char ch;
float d;
int i;
char str[80];
double balance;
```
Also, define one variable called `s_var` using this structure.
3. What is wrong with this fragment?
```c
struct s_type {
    int a;
    char b;
    float bal;
} myvar, *p;

p = &myvar;

p.a = 10;
```
4. Write a program that uses an array of structures to store employee names, telephone numbers, hours worked, and hourly wages. Allow for 10 employees. Have the program input the information and save it to a disk file. Call the file EMP.
5. Write a program that reads the EMP file created in Exercise 4 and displays the information on the screen.
6. What is a bit-field?
7. Write a program that displays individually the values of the high- and low-order bytes of a short integer. (Hint: Use a union that contains as its two elements a short integer and a two-byte character array.)

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. Write a program that contains two structure variables defined as:
```c
struct s_type {
    int i;
    char ch;
    double d;
} var1, var2;
```
Have the program give each member of both structures initial values, but make sure that the values differ between the two structures. Using a function called `struct_swap()`, have the program swap the contents of `var1` and `var2`.
2. As you know from Chapter 9, `fgetc()` returns an integer value, even though it only reads a character from a file. Write a program that copies one file to another. Assign the return value of `fgetc()` to a union that contains an integer and character member. Use the integer element to check for `EOF`. Write the character element to the destination file. Have the user specify both the source and destination file names on the command line.
3. What is wrong with this fragment?
```c
struct s_type {
    int a;
    int b: 2;
    int c: 6;
} var;

.
.
.
scanf("%d", &var);
```
4. In C, as you know, you cannot pass an array to a function as a parameter. (Only a pointer to an array can be passed.) However, there is one way around this restriction. If you enclose the array within a structure, the array is passed using the standard call-by-value convention. Write a program that demonstrates this by passing a string inside a structure to a function, altering its contents inside the function and demonstrating that the original string is not altered after the function returns.
