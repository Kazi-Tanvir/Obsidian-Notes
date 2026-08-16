# 9 File I/O

ALTHOUGH C does not define any keywords that perform file I/O, the C standard library contains a very rich set of I/O functions. As you will see in this chapter, C's approach to I/O is efficient, powerful, and flexible.

> [!NOTE]
> Most C compilers supply two complete sets of file I/O functions. One is called the *ANSI file system* (sometimes called the *buffered file system*). This file system is defined by the ANSI C standard. The second file system is based on the original UNIX operating environment and is called the *UNIX-like file system* (sometimes called the *unbuffered file system*). This file system is not defined by the ANSI C standard. The ANSI standard only defines one file system because the two file systems are redundant. Further, not all environments may be able to adapt to the UNIX-like system. For these reasons, this book only discusses the ANSI file system. For a discussion of the UNIX-like file system, see my book *C: The Complete Reference* (Berkeley, CA, Osborne/McGraw-Hill).

---

### Review Skills Check

Before proceeding you should be able to perform these exercises and answer these questions:

1. What is the difference between `getchar()` and `getche()`?
2. Give one reason why you probably won't use `scanf()`'s `%s` option to read strings from the keyboard.
3. Write a program that prints a four-column table of the prime numbers between 2 and 1000. Make sure that the columns are aligned.
4. Write a program that inputs a double, a character, and a string not longer than 20 characters. Redisplay the values to confirm that they were input correctly.
5. Write a program that reads and discards leading digits and then reads a string. (Hint: Use a scanset to read past any leading digits.)

---

## 9.1 UNDERSTAND STREAMS

Before we can begin our discussion of file I/O, you must understand two very important concepts: the *stream* and the *file*. The C I/O system supplies a consistent interface to the programmer, independent of the actual I/O device being used. To accomplish this, C provides a level of abstraction between the programmer and the hardware. This abstraction is called a *stream*. The actual device providing I/O is called a *file*. Thus, a stream is a logical interface to a file. As C defines the term *file*, it can refer to a disk file, the screen, the keyboard, memory, a port, a file on tape, and various other types of I/O devices. The most common form of file is, of course, the disk file. Although files differ in form and capabilities, all streams are the same. The advantage to this approach is that to you, the programmer, one hardware device will look much like any other. The stream automatically handles the differences.

A stream is linked to a file using an *open* operation. A stream is disassociated from a file using a *close* operation.

There are two types of streams: *text* and *binary*. A *text stream* contains ASCII characters. When a text stream is being used, some character translations may take place. For example, when the newline character is output, it is usually converted into a carriage return, linefeed pair. For this reason, there may not be a one-to-one correspondence between what is sent to the stream and what is written to the file. A *binary stream* may be used with any type of data. No character translations will occur, and there is a one-to-one correspondence between what is sent to the stream and what is actually contained in the file.

One final concept you need to understand is that of the *current location*. The current location, also referred to as the *current position*, is the location in a file where the next file access will occur. For example, if a file is 100 bytes long and half the file has been read, the next read operation will occur at byte 50, which is the current location.

To summarize: In C, disk I/O (like certain other types of I/O) is performed through a logical interface called a stream. All streams have similar properties, and all are operated on by the same I/O functions, no matter what type of file the stream is associated with. A file is the actual physical entity that receives or supplies the data. Even though files differ, streams do not. (Of course, some devices may not support random-access operations, for example, so their associated streams will not support such operations either.)

Now that you are familiar with the theory behind C's file system, it is time to begin learning about it in practice.

---

## 9.2 MASTER FILE-SYSTEM BASICS

In this section you will learn how to open and close a file. You will also learn how to read characters from and write characters to a file.

To open a file and associate it with a stream, use `fopen()`. Its prototype is shown here:

```c
FILE *fopen(char *fname, char *mode);
```

The `fopen()` function, like all the file-system functions, uses the header STDIO.H. The name of the file to open is pointed to by *fname*. It must be a valid file name, as defined by the operating system. The string pointed to by *mode* determines how the file may be accessed. The legal values for *mode* as defined by the ANSI C standard are shown in Table 9-1. Your compiler may allow additional modes.

If the open operation is successful, `fopen()` returns a valid file pointer. The type `FILE` is defined in STDIO.H. It is a structure that holds various kinds of information about the file, such as its size, the current location of the file, and its access modes. It essentially identifies the file. (A structure is a group of variables accessed under one name. You will learn about structures in the next chapter, but you do not need to know anything about them to learn and fully use C's file system.) The `fopen()` function returns a pointer to the structure associated with the file by the open process. You will use this pointer with all other functions that operate on the file. However, you must never alter it or the object it points to.

If the `fopen()` function fails, it returns a null pointer. The header STDIO.H defines the macro `NULL`, which is defined to be a null pointer. It is very important to ensure that a valid file pointer has been returned. To do so, check the value returned by `fopen()` to make sure that it is not `NULL`. For example, the proper way to open a file called **myfile** for text input is shown in this fragment:

```c
FILE *fp;

if((fp = fopen("myfile", "r")) == NULL) {
    printf("Error opening file.\n");
    exit(1); /* or substitute your own error handler */
}
```

Although most of the file modes are self-explanatory, a few comments are in order. If, when opening a file for read-only operations, the file does not exist, `fopen()` will fail. When opening a file using append mode, if the file does not exist, it will be created. Further, when a file is opened for append all new data written to the file will be written to the end of the file. The original contents will remain unchanged. If, when a file is opened for writing, the file does not exist, it will be created. If it does exist, the contents of the original file will be destroyed and a new file created. The difference between modes **r+** and **w+** is that **r+** will not create a file if it does not exist; however, **w+** will. Further, if the file already exists, opening it with **w+** destroys its contents; opening it with **r+** does not.

| Mode | Meaning |
| :--- | :--- |
| "r" | Open a text file for reading. |
| "w" | Create a text file for writing. |
| "a" | Append to a text file. |
| "rb" | Open a binary file for reading. |
| "wb" | Create a binary file for writing. |
| "ab" | Append to a binary file. |
| "r+" | Open a text file for read/write. |
| "w+" | Create a text file for read/write. |
| "a+" | Append or create a text file for read/write. |
| "r+b" | Open a binary file for read/write. You may also use "rb+". |
| "w+b" | Create a binary file for read/write. You may also use "wb+". |
| "a+b" | Append or create a binary file for read/write. You may also use "ab+". |

*Table 9-1 The Legal Values for Mode*

To close a file, use `fclose()`, whose prototype is

```c
int fclose(FILE *fp);
```

The `fclose()` function closes the file associated with *fp*, which must be a valid file pointer previously obtained using `fopen()`, and disassociates the stream from the file. In order to improve efficiency, most file system implementations write data to disk one sector at a time. Therefore, data is buffered until a sector's worth of information has been output before the buffer is physically written to disk. When you call `fclose()`, it automatically writes any information remaining in a partially full buffer to disk. This is often referred to as *flushing the buffer*.

You must never call `fclose()` with an invalid argument. Doing so will damage the file system and possibly cause irretrievable data loss.

The `fclose()` function returns zero if successful. If an error occurs, `EOF` is returned.

Once a file has been opened, depending upon its mode, you may read and/or write bytes (i.e., characters) using these two functions:

```c
int fgetc(FILE *fp);
int fputc(int ch, FILE *fp);
```

The `fgetc()` function reads the next byte from the file described by *fp* as an **unsigned char** and returns it as an integer. (The character is returned in the low-order byte.) If an error occurs, `fgetc()` returns `EOF`. As you should recall from Chapter 8, `EOF` is a negative integer (usually -1). The `fgetc()` function also returns `EOF` when the end of the file is reached. Although `fgetc()` returns an integer value, your program can assign it to a **char** variable since the low-order byte contains the character read from the file.

The `fputc()` function writes the byte contained in the low-order byte of *ch* to the file associated with *fp* as an **unsigned char**. Although *ch* is defined as an **int**, you may call it using a **char**, which is the common procedure. The `fputc()` function returns the character written if successful or `EOF` if an error occurs.

Historical note: The traditional names for `fgetc()` and `fputc()` are `getc()` and `putc()`. The ANSI C standard still defines these names, and they are essentially interchangeable with `fgetc()` and `fputc()`. One reason the new names were added was for consistency. All other ANSI file system function names begin with 'f,' so 'f' was added to `getc()` and `putc()`. The ANSI standard still supports the traditional names, however, because there are so many existing programs that use them. If you see programs that use `getc()` and `putc()`, don't worry. They are essentially different names for `fgetc()` and `fputc()`.

### EXAMPLES

1. This program demonstrates the four file-system functions you have learned about so far. First, it opens a file called MYFILE for output. Next, it writes the string "This is a file system test." to the file. Then, it closes the file and reopens it for read operations. Finally, it displays the contents of the file on the screen and closes the file.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char str[80] = "This is a file system test.\n";
    FILE *fp;
    char *p;
    int i;

    /* open myfile for output */
    if((fp = fopen("myfile", "w"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* write str to disk */
    p = str;
    while(*p) {
        if(fputc(*p, fp)==EOF) {
            printf("Error writing file.\n");
            exit(1);
        }
        p++;
    }
    fclose(fp);

    /* open myfile for input */
    if((fp = fopen("myfile", "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* read back the file */
    for(;;) {
        i = fgetc(fp);
        if(i == EOF) break;
        putchar(i);
    }
    fclose(fp);

    return 0;
}
```

In this version, when reading from the file, the return value of `fgetc()` is assigned to an integer variable called **i**. The value of this integer is then checked to see if the end of the file has been reached. For most compilers, however, you can simply assign the value returned by `fgetc()` to a **char** and still check for `EOF`, as is shown in the following version:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char str[80] = "This is a file system test.\n";
    FILE *fp;
    char ch, *p;

    /* open myfile for output */
    if((fp = fopen("myfile", "w"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* write str to disk */
    p = str;
    while(*p) {
        if(fputc(*p, fp)==EOF) {
            printf("Error writing file.\n");
            exit(1);
        }
        p++;
    }
    fclose(fp);

    /* open myfile for input */
    if((fp = fopen("myfile", "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* read back the file */
    for(;;) {
        ch = fgetc(fp);
        if(ch == EOF) break;
        putchar(ch);
    }
    fclose(fp);

    return 0;
}
```

The reason this approach works is that when a **char** is being compared to an **int**, the **char** value is automatically elevated to an equivalent **int** value.

There is, however, an even better way to code this program. For example, there is no need for a separate comparison step because the assignment and the comparison can be performed at the same time, within the **if**, as shown here:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char str[80] = "This is a file system test.\n";
    FILE *fp;
    char ch, *p;

    /* open myfile for output */
    if((fp = fopen("myfile", "w"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* write str to disk */
    p = str;
    while(*p) {
        if(fputc(*p, fp)==EOF) {
            printf("Error writing file.\n");
            exit(1);
        }
        p++;
    }
    fclose(fp);

    /* open myfile for input */
    if((fp = fopen("myfile", "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* read back the file */
    for(;;) {
        if((ch = fgetc(fp)) == EOF) break;
        putchar(ch);
    }
    fclose(fp);

    return 0;
}
```

Don't let the statement

```c
if((ch = fgetc(fp)) == EOF) break;
```

fool you. Here's what is happening. First, inside the **if**, the return value of `fgetc()` is assigned to **ch**. As you may recall, the assignment operation in C is an expression. The entire value of `(ch = fgetc(fp))` is equal to the return value of `fgetc()`. Therefore, it is this integer value that is tested against `EOF`.

Expanding upon this approach, you will normally see this program written by a professional C programmer as follows:

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char str[80] = "This is a file system test.\n";
    FILE *fp;
    char *p;
    char ch;

    /* open myfile for output */
    if((fp = fopen("myfile", "w"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* write str to disk */
    p = str;
    while(*p)
        if(fputc(*p++, fp)==EOF) {
            printf("Error writing file.\n");
            exit(1);
        }

    fclose(fp);

    /* open myfile for input */
    if((fp = fopen("myfile", "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* read back the file */
    while((ch = fgetc(fp)) != EOF) putchar(ch);
    fclose(fp);

    return 0;
}
```

Notice that now, each character is read, assigned to **ch**, and tested against `EOF`, all within the expression of the **while** loop that controls the input process. If you compare this with the original version, you can see how much more efficient this one is. In fact, the ability to integrate such operations is one reason C is so powerful. It is important that you get used to the kind of approach just shown. Later on in this book we will explore such assignment statements more fully.

2. The following program takes two command-line arguments. The first is the name of a file, the second is a character. The program searches the specified file, looking for the character. If the file contains at least one of these characters, it reports this fact. Notice how it uses `argv` to access the file name and the character for which to search.

```c
/* Search specified file for specified character. */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    char ch;

    /* see if correct number of command line arguments */
    if(argc!=3) {
        printf("Usage: find <file name> <ch>\n");
        exit(1);
    }

    /* open file for input */
    if((fp = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* look for character */
    while((ch = fgetc(fp)) != EOF)
        if(ch==*argv[2]) {
            printf("%c found", ch);
            break;
        }
    fclose(fp);

    return 0;
}
```

### EXERCISES

1. Write a program that displays the contents of the text file specified on the command line.
2. Write a program that reads a text file and counts how many times each letter from 'A' to 'Z' occurs. Have it display the results. (Do not differentiate between upper- and lowercase letters.)
3. Write a program that copies the contents of one text file to another. Have the program accept three command-line arguments. The first is the name of the source file, the second is the name of the destination file, the third is optional. If present and if it equals "watch," have the program display each character as it copies the files; otherwise, do not have the program display any screen output. If the destination file does not exist, create it.

---

## 9.3 UNDERSTAND feof( ) AND ferror( )

As you know, when `fgetc()` returns `EOF`, either an error has occurred or the end of the file has been reached, but how do you know which event has taken place? Further if you are operating on a binary file, all values are valid. This means it is possible that a byte will have the same value (when elevated to an **int**) as `EOF`, so how do you know if valid data has been returned or if the end of the file has been reached? The solution to these problems are the functions `feof()` and `ferror()`, whose prototypes are shown here:

```c
int feof(FILE *fp);
int ferror(FILE *fp);
```

The `feof()` function returns nonzero if the file associated with *fp* has reached the end of the file. Otherwise it returns zero. This function works for both binary files and text files. The `ferror()` function returns nonzero if the file associated with *fp* has experienced an error; otherwise, it returns zero.

Using the `feof()` function, this code fragment shows how to read to the end of a file:

```c
FILE *fp;

.
.
.
while(!feof(fp)) ch = fgetc(fp);
```

This code works for any type of file and is better in general than checking for `EOF`. However, it still does not provide any error checking. Error checking is added here:

```c
FILE *fp;

.
.
.
while(!feof(fp)) {
    ch = fgetc(fp);
    if(ferror(fp)) {
        printf("File Error\n");
        break;
    }
}
```

Keep in mind that `ferror()` only reports the status of the file system relative to the last file access. Therefore, to provide the fullest error checking, you must call it after each file operation.

The most damaging file errors occur at the operating-system level. Frequently, it is the operating system that intercepts these errors and displays its own error messages. For example, if a bad sector is found on the disk, most operating systems will, themselves, stop the execution of the program and report the error. Often the only types of errors that actually get passed back to your program are those caused by mistakes on your part, such as accessing a file in a way inconsistent with the mode used to open it or when you cause an out-of-range condition. Usually these types of errors can be trapped by checking the return type of the other file system functions rather than by calling `ferror()`. For this reason, you will frequently see examples of C code in which there are relatively few (if any) calls to `ferror()`. One last point: Not all of the file system examples in this book will provide full error checking, mostly in the interest of keeping the programs short and easy to understand. However, if you are writing programs for actual use, you should pay special attention to error checking.

### EXAMPLES

1. This program copies any type of file, binary or text. It takes two command-line arguments. The first is the name of the source file, the second is the name of the destination file. If the destination file does not exist, it is created. It includes full error checking. (You might want to compare this version with the copy program you wrote for text files in the preceding section.)

```c
/* Copy a file. */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *from, *to;
    char ch;

    /* see if correct number of command line arguments */
    if(argc!=3) {
        printf("Usage: copy <source> <destination>\n");
        exit(1);
    }

    /* open source file */
    if((from = fopen(argv[1], "rb"))==NULL) {
        printf("Cannot open source file.\n");
        exit(1);
    }

    /* open destination file */
    if((to = fopen(argv[2], "wb"))==NULL) {
        printf("Cannot open destination file.\n");
        exit(1);
    }

    /* copy the file */
    while(!feof(from)) {
        ch = fgetc(from);
        if(ferror(from)) {
            printf("Error reading source file.\n");
            exit(1);
        }
        if(!feof(from)) fputc(ch, to);
        if(ferror(to)) {
            printf("Error writing destination file.\n");
            exit(1);
        }
    }

    if(fclose(from)==EOF) {
        printf("Error closing source file.\n");
        exit(1);
    }

    if(fclose(to)==EOF) {
        printf("Error closing destination file.\n");
        exit(1);
    }

    return 0;
}
```

2. This program compares the two files whose names are specified on the command line. It either prints **Files are the same**, or it displays the byte of the first mismatch. It also uses full error checking.

```c
/* Compare files. */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *fp1, *fp2;
    char ch1, ch2, same;
    unsigned long l;

    /* see if correct number of command line arguments */
    if(argc!=3) {
        printf("Usage: compare <file 1> <file 2>\n");
        exit(1);
    }

    /* open first file */
    if((fp1 = fopen(argv[1], "rb"))==NULL) {
        printf("Cannot open first file.\n");
        exit(1);
    }

    /* open second file */
    if((fp2 = fopen(argv[2], "rb"))==NULL) {
        printf("Cannot open second file.\n");
        exit(1);
    }

    l = 0;
    same = 1;
    /* compare the files */
    while(!feof(fp1)) {
        ch1 = fgetc(fp1);
        if(ferror(fp1)) {
            printf("Error reading first file.\n");
            exit(1);
        }
        ch2 = fgetc(fp2);
        if(ferror(fp2)) {
            printf("Error reading second file.\n");
            exit(1);
        }
        if(ch1!=ch2) {
            printf("Files differ at byte number %lu", l);
            same = 0;
            break;
        }
        l++;
    }
    if(same) printf("Files are the same.\n");

    if(fclose(fp1)==EOF) {
        printf("Error closing first file.\n");
        exit(1);
    }

    if(fclose(fp2)==EOF) {
        printf("Error closing second file.\n");
        exit(1);
    }

    return 0;
}
```

### EXERCISES

1. Write a program that counts the number of bytes in a file (text or binary) and displays the result. Have the user specify the file to count on the command line.
2. Write a program that exchanges the contents of the two files whose names are specified on the command line. That is, given two files called FILE1 and FILE2, after the program has run, FILE1 will contain FILE2's original contents, and FILE2 will contain FILE1's original contents. (Hint: Use a temporary file to aid in the exchange process.)

---

## 9.4 LEARN SOME HIGHER-LEVEL TEXT FUNCTIONS

When working with text files, C provides four functions that make file operations easier. The first two are called `fputs()` and `fgets()`, which write a string to and read a string from a file, respectively. Their prototypes are

```c
int fputs(char *str, FILE *fp);
char *fgets(char *str, int num, FILE *fp);
```

The `fputs()` function writes the string pointed to by *str* to the file associated with *fp*. It returns `EOF` if an error occurs and a non-negative value if successful. The null that terminates *str* is not written. Also, unlike its related function `puts()`, it does not automatically append a carriage return, linefeed pair.

The `fgets()` function reads characters from the file associated with *fp* into the string pointed to by *str* until *num*-1 characters have been read, a newline character is encountered, or the end of the file is reached. In any case, the string is null-terminated. Unlike its related function `gets()`, the newline character is retained. The function returns *str* if successful and a null pointer if an error occurs.

The C file system contains two very powerful functions similar to two you already know. They are `fprintf()` and `fscanf()`. These functions operate exactly like `printf()` and `scanf()` except that they work with files. Their prototypes are:

```c
int fprintf(FILE *fp, char *control-string, ...);
int fscanf(FILE *fp, char *control-string, ...);
```

Instead of directing their I/O operations to the console, these functions operate on the file specified by *fp*. Otherwise their operations are the same as their console-based relatives. The advantage to `fprintf()` and `fscanf()` is that they make it very easy to write a wide variety of data to a file using a text format.

### EXAMPLES

1. This program demonstrates `fputs()` and `fgets()`. It reads lines entered by the user and writes them to the file specified on the command line. When the user enters a blank line, the input phase terminates, and the file is closed. Next, the file is reopened for input, and the program uses `fgets()` to display the contents of the file.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    char str[80];

    /* check for command line arg */
    if(argc!=2) {
        printf("Specify file name.\n");
        exit(1);
    }

    /* open file for output */
    if((fp = fopen(argv[1], "w"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    printf("Enter a blank line to stop.\n");
    do {
        printf(": ");
        gets(str);
        strcat(str, "\n"); /* add newline */
        if(*str != '\n') fputs(str, fp);
    } while(*str != '\n');
    fclose(fp);

    /* open file for input */
    if((fp = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* read back the file */
    do {
        fgets(str, 79, fp);
        if(!feof(fp)) printf(str);
    } while(!feof(fp));
    fclose(fp);

    return 0;
}
```

2. This program demonstrates `fprintf()` and `fscanf()`. It first writes a double, an int, and a string to the file specified on the command line. Next, it reads them back and displays their values as verification. If you examine the file created by this program, you will see that it contains human-readable text. This is because `fprintf()` writes to a disk file what `printf()` would write to the screen. No internal data formats are used.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    double ld;
    int d;
    char str[80];

    /* check for command line arg */
    if(argc!=2) {
        printf("Specify file name.\n");
        exit(1);
    }

    /* open file for output */
    if((fp = fopen(argv[1], "w"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    fprintf(fp, "%f %d %s", 12345.342, 1908, "hello");
    fclose(fp);

    /* open file for input */
    if((fp = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    fscanf(fp, "%lf%d%s", &ld, &d, str);
    printf("%f %d %s", ld, d, str);
    fclose(fp);

    return 0;
}
```

### EXERCISES

1. In Chapter 6 you wrote a very simple telephone-directory program. Write a program that expands on this concept by allowing the directory to be saved to a disk file. Have the program present a menu that looks like this:

```
1. Enter the names and numbers
2. Find numbers
3. Save directory to disk
4. Load directory from disk
5. Quit
```

The program should be capable of storing 100 names and numbers. (Use only first names if you like.) Use `fprintf()` to save the directory to disk and `fscanf()` to read it back into memory.
2. Write a program that uses `fgets()` to display the contents of a text file, one screenful at a time. After each screen is displayed, have the program prompt the user for more.
3. Write a program that copies a text file. Specify both the source and destination file names on the command line. Use `fgets()` and `fputs()` to copy the file. Include full error checking.

---

## 9.5 LEARN TO READ AND WRITE BINARY DATA

As useful and convenient as `fprintf()` and `fscanf()` are, they are not necessarily the most efficient way to read and write numeric data. The reason for this is that both functions perform conversions on the data. For example, when you output a number using `fprintf()`, the number is converted from its binary format into ASCII text. Conversely, when you read a number using `fscanf()`, it must be converted back into its binary representation. For many applications, this conversion time will not be meaningful; for others, it will be a severe limitation. Further, for some types of data, a file created by `fprintf()` will also be larger than one that contains a mirror image of the data using its binary format. For these reasons, the C file system includes two important functions: `fread()` and `fwrite()`. These functions can read and write any type of data, using its binary representation. Their prototypes are

```c
size_t fread(void *buffer, size_t size, size_t num, FILE *fp);
size_t fwrite(void *buffer, size_t size, size_t num, FILE *fp);
```

As you can see, these prototypes introduce some unfamiliar elements. However, before discussing them, a brief description of each function is necessary.

The `fread()` function reads from the file associated with *fp*, *num* number of objects, each object *size* bytes long, into the buffer pointed to by *buffer*. It returns the number of objects actually read. If this value is less than *num*, either the end of the file has been encountered or an error has occurred. You can use `feof()` or `ferror()` to find out which.

The `fwrite()` function is the opposite of `fread()`. It writes to the file associated with *fp*, *num* number of objects, each object *size* bytes long, from the buffer pointed to by *buffer*. It returns the number of objects written. This value will be less than *num* only if an output error has occurred.

Before looking at any examples, let's examine the new concepts introduced by the functions' prototypes.

The first concept is that of the *void pointer*. A void pointer is a pointer that can point to any type of data without the use of a type cast. This is generally referred to as a *generic pointer*. In C, void pointers are used for two primary purposes. First, as illustrated by `fread()` and `fwrite()`, they are a way for a function to receive a pointer to any type of data without causing a type mismatch error. As stated earlier, `fread()` and `fwrite()` can be used to read or write any type of data. Therefore, the functions must be capable of receiving any sort of data pointed to by *buffer*. Void pointers make this possible. A second purpose they serve is to allow a function to return a generic pointer. You will see an example of this later in this book.

The second new item is the type `size_t`. This type is defined in the STDIO.H header file. (You will learn how to define types later in this book.) A variable of this type is defined by the ANSI C standard as being able to hold a value equal to the size of the largest object supported by the compiler. For our purposes, you can think of `size_t` as being the same as **unsigned** or **unsigned long**. The reason that `size_t` is used instead of its equivalent built-in type is to allow C compilers running in different environments to accommodate the needs and confines of those environments.

When using `fread()` or `fwrite()` to input or output binary data, the file must be opened for binary operations. Forgetting this can cause hard-to-find problems.

To understand the operation of `fread()` and `fwrite()`, let's begin with a simple example. The following program writes an integer to a file called MYFILE using its internal, binary representation and then reads it back. (The program assumes that integers are 2 bytes long.)

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;
    int i;

    /* open file for output */
    if((fp = fopen("myfile", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    i = 100;

    if(fwrite(&i, 2, 1, fp) != 1) {
        printf("Write error occurred.\n");
        exit(1);
    }
    fclose(fp);

    /* open file for input */
    if((fp = fopen("myfile", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    if(fread(&i, 2, 1, fp) != 1) {
        printf("Read error occurred.\n");
        exit(1);
    }
    printf("i is %d", i);
    fclose(fp);

    return 0;
}
```

Notice how error checking is easily performed in this program by simply comparing the number of items written or read with that requested. In some situations, however, you will still need to use `feof()` or `ferror()` to determine if the end of the file has been reached or if an error has occurred.

One thing wrong with the preceding example is that an assumption about the size of an integer has been made and this size is hardcoded into the program. Therefore, the program will not work properly with compilers that use 4-byte integers, for example. More generally, the size of many types of data changes between systems or is difficult to determine manually. For this reason, C includes the keyword `sizeof`, which is a compile-time operator that returns the size, in bytes, of a data type or variable. It takes the general forms

`sizeof(type)`

or

`sizeof var_name;`

For example, if floats are four bytes long and **f** is a **float** variable, both of the following expressions evaluate to 4:

```c
sizeof f
sizeof(float)
```

When using `sizeof` with a type, the type must be enclosed between parentheses. No parentheses are needed when using a variable name, although the use of parentheses in this context is not an error.

By using `sizeof`, not only do you save yourself the drudgery of computing the size of some object by hand, but you also ensure the portability of your code to new environments. An improved version of the preceding program is shown here, using `sizeof`.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;
    int i;

    /* open file for output */
    if((fp = fopen("myfile", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    i = 100;

    if(fwrite(&i, sizeof(int), 1, fp) != 1) {
        printf("Write error occurred.\n");
        exit(1);
    }
    fclose(fp);

    /* open file for input */
    if((fp = fopen("myfile", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    if(fread(&i, sizeof i, 1, fp) != 1) {
        printf("Read error occurred.\n");
        exit(1);
    }
    printf("i is %d", i);
    fclose(fp);

    return 0;
}
```

### EXAMPLES

1. This program fills a ten-element array with floating-point numbers, writes them to a file, and then reads them back. This program writes each element of the array separately. Because binary data is being written using its internal format, the file must be opened for binary I/O operations.

```c
#include <stdio.h>
#include <stdlib.h>

double d[10] = {
    10.23, 19.87, 1002.23, 12.9, 0.897,
    11.45, 75.34, 0.0, 1.01, 875.875
};

int main(void)
{
    int i;
    FILE *fp;

    if((fp = fopen("myfile", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    for(i=0; i<10; i++)
        if(fwrite(&d[i], sizeof(double), 1, fp) != 1) {
            printf("Write error.\n");
            exit(1);
        }

    fclose(fp);

    if((fp = fopen("myfile", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* clear the array */
    for(i=0; i<10; i++) d[i] = -1.0;

    for(i=0; i<10; i++)
        if(fread(&d[i], sizeof(double), 1, fp) != 1) {
            printf("Read error.\n");
            exit(1);
        }
    fclose(fp);

    /* display the array */
    for(i=0; i<10; i++) printf("%f ", d[i]);

    return 0;
}
```

The array is cleared between the write and read operations only to "prove" that it is being filled by the `fread()` statement.

2. The following program does the same thing as the first, but here only one call to `fwrite()` and `fread()` is used because the entire array is written in one step, which is much more efficient. This example helps illustrate how powerful these functions are.

```c
#include <stdio.h>
#include <stdlib.h>

double d[10] = {
    10.23, 19.87, 1002.23, 12.9, 0.897,
    11.45, 75.34, 0.0, 1.01, 875.875
};

int main(void)
{
    int i;
    FILE *fp;

    if((fp = fopen("myfile", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* write the entire array in one step */
    if(fwrite(d, sizeof d, 1, fp) != 1) {
        printf("Write error.\n");
        exit(1);
    }
    fclose(fp);

    if((fp = fopen("myfile", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* clear the array */
    for(i=0; i<10; i++) d[i] = -1.0;

    /* read the entire array in one step */
    if(fread(d, sizeof d, 1, fp) != 1) {
        printf("Read error.\n");
        exit(1);
    }
    fclose(fp);

    /* display the array */
    for(i=0; i<10; i++) printf("%f ", d[i]);

    return 0;
}
```

### EXERCISES

1. Write a program that allows a user to input as many **double** values as desired (up to 32,767) and writes them to a disk file as they are entered. Call this file VALUES. Keep a count of the number of values entered, and write this number to a file called COUNT.
2. Using the file you created in Exercise 1, write a program that first reads the number of items in VALUES from COUNT. Next, read the values in VALUES and display them.

---

## 9.6 UNDERSTAND RANDOM ACCESS

So far, the examples have either written or read a file sequentially from its beginning to its end. However, using another of C's file system functions, you can access any point in a file at any time. The function that lets you do this is called `fseek()`, and its prototype is

```c
int fseek(FILE *fp, long offset, int origin);
```

Here, *fp* is associated with the file being accessed. The value of *offset* determines the number of bytes from *origin* to make the new current position. *origin* must be one of these macros, shown here with their meanings:

| Origin | Meaning |
| :--- | :--- |
| `SEEK_SET` | Seek from start of file |
| `SEEK_CUR` | Seek from current location |
| `SEEK_END` | Seek from end of file |

These macros are defined in STDIO.H. For example, if you wanted to set the current location 100 bytes from the start of the file, then *origin* will be `SEEK_SET` and *offset* will be 100.

The `fseek()` function returns zero when successful and nonzero if a failure occurs. In most implementations, you may seek past the end of the file, but you may never seek to a point before the start of the file.

You can determine the current location of a file using `ftell()`, another of C's file system functions. Its prototype is

```c
long ftell(FILE *fp);
```

It returns the location of the current position of the file associated with *fp*. If a failure occurs, it returns -1.

In general, you will want to use random access only on binary files. The reason for this is simple. Because text files may have character translations performed on them, there may not be a direct correspondence between what is in the file and the byte to which it would appear that you want to seek. The only time you should use `fseek()` with a text file is when seeking to a position previously determined by `ftell()`, using `SEEK_SET` as the origin.

Remember one important point: Even a file that contains only text can be opened as a binary file, if you like. There is no inherent restriction about random access on files containing text. The restriction applies only to files opened as text files.

### EXAMPLES

1. The following program uses `fseek()` to report the value of any byte within the file specified on the command line.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    long loc;
    FILE *fp;

    /* see if file name is specified */
    if(argc!=2) {
        printf("File name missing.\n");
        exit(1);
    }

    if((fp = fopen(argv[1], "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    printf("Enter byte to seek to: ");
    scanf("%ld", &loc);
    if(fseek(fp, loc, SEEK_SET)) {
        printf("Seek error.\n");
        exit(1);
    }

    printf("Value at loc %ld is %d", loc, getc(fp));
    fclose(fp);

    return 0;
}
```

2. The following program uses `ftell()` and `fseek()` to copy the contents of one file into another in reverse order. Pay special attention to how the end of the file is found. Since the program has sought to the end of the file, the program backs up one byte so that the current location of the file associated with **in** is at the last actual character in the file.

```c
/* Copy a file in reverse order */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    long loc;
    FILE *in, *out;
    char ch;

    /* see if correct number of command line arguments */
    if(argc!=3) {
        printf("Usage: revcopy <source> <destination>.\n");
        exit(1);
    }

    if((in = fopen(argv[1], "rb"))==NULL) {
        printf("Cannot open input file.\n");
        exit(1);
    }
    if((out = fopen(argv[2], "wb"))==NULL) {
        printf("Cannot open output file.\n");
        exit(1);
    }

    /* find end of source file */
    fseek(in, 0L, SEEK_END);
    loc = ftell(in);

    /* copy file in reverse order */
    loc = loc-1; /* back up past end-of-file mark */
    while(loc >= 0L) {
        fseek(in, loc, SEEK_SET);
        ch = fgetc(in);
        fputc(ch, out);
        loc--;
    }
    fclose(in);
    fclose(out);

    return 0;
}
```

3. This program writes ten **double** values to disk. It then asks you which one you want to see. This example shows how you can randomly access data of any type. You simply need to multiply the size of the base data type by its index in the file.

```c
#include <stdio.h>
#include <stdlib.h>

double d[10] = {
    10.23, 19.87, 1002.23, 12.9, 0.897,
    11.45, 75.34, 0.0, 1.01, 875.875
};

int main(void)
{
    long loc;
    double value;
    FILE *fp;

    if((fp = fopen("myfile", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* write the entire array in one step */
    if(fwrite(d, sizeof d, 1, fp) != 1) {
        printf("Write error.\n");
        exit(1);
    }
    fclose(fp);

    if((fp = fopen("myfile", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    printf("Which element? ");
    scanf("%ld", &loc);
    if(fseek(fp, loc*sizeof(double), SEEK_SET)) {
        printf("Seek error.\n");
        exit(1);
    }

    fread(&value, sizeof(double), 1, fp);
    printf("Element %ld is %f", loc, value);

    fclose(fp);

    return 0;
}
```

### EXERCISES

1. Write a program that uses `fseek()` to display every other byte in a text file. (Remember, you must open the text file as a binary file in order for `fseek()` to work properly.) Have the user specify the file on the command line.
2. Write a program that searches a file, specified on the command line, for a specific integer value (also specified on the command line). If this value is found, have the program display its location, in bytes, relative to the start of the file.

---

## 9.7 LEARN ABOUT VARIOUS FILE-SYSTEM FUNCTIONS

You can rename a file using `rename()`, shown here:

```c
int rename(char *oldname, char *newname);
```

Here, *oldname* points to the original name of the file and *newname* points to its new name. The function returns zero if successful and nonzero if an error occurs.

You can erase a file using `remove()`. Its prototype is

```c
int remove(char *file-name);
```

This function will erase the file whose name matches that pointed to by *file-name*. It returns zero if successful and nonzero if an error occurs.

You can position a file's current location to the start of the file using `rewind()`. Its prototype is

```c
void rewind(FILE *fp);
```

It rewinds the file associated with *fp*. The `rewind()` function has no return value, because any file that has been successfully opened can be rewound.

Although seldom necessary because of the way C's file system works, you can cause a file's disk buffer to be flushed using `fflush()`. Its prototype is

```c
int fflush(FILE *fp);
```

It flushes the buffer of the file associated with *fp*. The function returns zero if successful, `EOF` if a failure occurs. If you call `fflush()` using a `NULL` for *fp*, all existing disk buffers are flushed.

### EXAMPLES

1. This program demonstrates `remove()`. It prompts the user for the file to erase and also provides a safety check in case the user entered the wrong name.

```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void)
{
    char fname[80];

    printf("Enter name of file to erase: ");
    gets(fname);
    printf("Are you sure? (Y/N) ");
    if(toupper(getchar())=='Y') remove(fname);

    return 0;
}
```

2. The following program demonstrates `rewind()` by displaying the contents of the file specified on the command line twice.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *fp;

    /* see if file name is specified */
    if(argc!=2) {
        printf("File name missing.\n");
        exit(1);
    }

    if((fp = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    /* show it once */
    while(!feof(fp))
        putchar(getc(fp));

    rewind(fp);

    /* show it twice */
    while(!feof(fp))
        putchar(getc(fp));

    fclose(fp);

    return 0;
}
```

3. This fragment causes the buffer associated with **fp** to be flushed to disk.

```c
FILE *fp;

.
.
.
fflush(fp);
```

4. This program renames a file called MYFILE.TXT to YOURFILE.TXT.

```c
#include <stdio.h>

int main(void)
{
    if(rename("myfile.txt", "yourfile.txt"))
        printf("Rename failed.\n");
    else
        printf("Rename successful.\n");

    return 0;
}
```

### EXERCISES

1. Improve the erase program so that it notifies the user if he or she tries to remove a nonexistent file.
2. On your own, think of ways that `rewind()` and `fflush()` could be useful in real applications.

---

## 9.8 LEARN ABOUT THE STANDARD STREAMS

When a C program begins execution, three streams are automatically opened and available for use. These streams are called *standard input* (**stdin**), *standard output* (**stdout**), and *standard error* (**stderr**). By default, they refer to the console, but in environments that support redirectable I/O, they can be redirected by the operating system to some other device.

Normally, **stdin** inputs from the keyboard; **stdout** and **stderr** write to the screen. These standard streams are `FILE` pointers and may be used with any function that requires a variable of type `FILE *`. For example, you can use `fprintf()` to print formatted output to the screen by specifying **stdout** as its output stream. The following two statements are functionally the same:

```c
fprintf(stdout, "%d %c %s", 100, 'c', "this is a string");
printf("%d %c %s", 100, 'c', "this is a string");
```

In actuality, C makes little distinction between console I/O and file I/O. As just shown, it is possible to perform console I/O using several of the file-system functions. Although it may come as a bit of a surprise, it is also possible to perform disk file I/O using console I/O functions, such as `printf()`. Here's why.

All of the functions described in Chapter 8 and referred to as "console I/O functions" are actually special-case file-system functions that automatically operate on **stdin** and **stdout**. Thus, the console I/O functions are just conveniences for you, the programmer. As far as C is concerned, the console is simply another hardware device. You don't actually need the console functions to access the console. Any file-system function can access it. (Of course, non-standard I/O functions like `getche()` are differentiated from the standard file-system functions and do, in fact, operate only on the console.) In environments that allow redirection of I/O, **stdin** and **stdout** could refer to devices other than the keyboard and screen. Since the console functions operate on **stdin** and **stdout**, if these streams are redirected, the "console" functions can be made to operate on other devices. For example, by redirecting the **stdout** to a disk file, you can use a "console" I/O function to write to a disk file.

One important point: **stdin**, **stdout**, and **stderr** are not variables. They may not be assigned a value using `fopen()`, nor should you attempt to close them using `fclose()`. These streams are maintained internally by the compiler. You are free to use them, but not to change them.

### EXAMPLES

1. Consider this program:

```c
#include <stdio.h>

int main(void)
{
    printf("This is an example of redirection.\n");

    return 0;
}
```

Assume that this program is called TEST. If you execute TEST normally, it displays the string on the screen. However, if an environment supports redirection of I/O, **stdout** can be redirected to a file. For example, in a DOS, OS/2, Windows, or UNIX environment, executing TEST like this

`TEST > OUTPUT`

causes the output of TEST to be written to a file called OUTPUT. You might want to try this now for yourself.

2. Input can also be redirected. For example, consider the following program:

```c
#include <stdio.h>

int main(void)
{
    int i;

    scanf("%d", &i);
    printf("%d", i);

    return 0;
}
```

Assuming it is called TEST, executing it as

`TEST < INPUT`

causes **stdin** to be directed to the file called INPUT. Assuming that INPUT contained the ASCII representation for an integer, the value of this integer will be read from the file and printed on the screen.

3. As mentioned earlier in this book, when using `gets()` it is possible to overrun the array that is being used to receive the characters entered by the user because `gets()` provides no bounds checking. One way around this problem is to use `fgets()`, specifying **stdin** for the input stream. Since `fgets()` requires you to specify a maximum length, it is possible to prevent an array overrun. The only trouble is that `fgets()` does not remove the newline character and `gets()` does. This means that you will have to manually remove it, as shown in the following program:

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[10];
    int i;

    printf("Enter a string: ");
    fgets(str, 10, stdin);

    /* remove newline, if present */
    i = strlen(str)-1;
    if(str[i]=='\n') str[i] = '\0';

    printf("This is your string: %s", str);

    return 0;
}
```

### EXERCISES

1. Write a program that copies the contents of one text file to another. However, use only "console" I/O functions and redirection to accomplish the file copy.
2. On your own, experiment using `fgets()` to read strings entered from the keyboard.

---

## Mastery Skills Check

Before continuing, you should be able to answer these questions and complete these exercises:

1. Write a program that displays the contents of a text file (specified on the command line), one line at a time. After each line is displayed, ask the user if he or she wants to see another line.
2. Write a program that copies a text file. Have the user specify both file names on the command line. Have the copy program convert all lowercase letters into uppercase ones.
3. What do `fprintf()` and `fscanf()` do?
4. Write a program that uses `fwrite()` to write 100 randomly generated integers to a file called RAND.
5. Write a program that uses `fread()` to display the integers stored in the file called RAND, created in Exercise 4.
6. Using the file called RAND, write a program that uses `fseek()` to allow the user to access and display the value of any integer in the file.
7. How do the "console" I/O functions relate to the file system?

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. Enhance the card-catalog program you wrote in Chapter 8 so that it stores its information in a disk file called CATALOG. When the program begins, have it read the catalog into memory. Also, add an option to save the information to disk.
2. Write a program that copies a file. Have the user specify both the source and destination files on the command line. Have the program remove tab characters, substituting the appropriate number of spaces.
3. On your own, create a small database to keep track of anything you desire—your CD collection, for example.
