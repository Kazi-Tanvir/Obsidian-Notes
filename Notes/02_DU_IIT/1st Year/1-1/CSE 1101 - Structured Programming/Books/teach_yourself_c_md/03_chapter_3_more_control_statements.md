# 3 More C Program Control Statements

THIS chapter continues the discussion of C's program control statements. Before doing so, however, the chapter begins by explaining how to read characters from the keyboard. Although you know how to input numbers, it is now time for you to know how to input individual characters because several examples in this chapter will make use of them. Next, the chapter finishes the discussion of the **if** and **for** statements. Then it presents C's two other loop statements, the **while** and **do**. Next you will learn about nested loops and two more of C's control statements, the **break** and **continue**. This chapter also covers C's other selection statement, the **switch**. It ends with a short discussion of C's unconditional jump statement, **goto**.

---

### Review Skills Check

Before proceeding, you should be able to answer these questions and perform these exercises:

1. What are C's relational and logical operators?
2. What is a block of code? How do you make one?
3. How do you output a newline using `printf()`?
4. Write a program that prints the numbers -100 to 100.
5. Write a program that prints 5 different proverbs. The program prompts the user for the number of the proverb to print and then displays it. (Use any proverbs you like.)
6. How can this statement be rewritten?
```c
count = count + 1;
```
7. What values are true in C? What values are false?

---

## 3.1 INPUT CHARACTERS

Although numbers are important, your programs will also need to read characters from the keyboard. In C you can do this in a variety of ways. Unfortunately, this conceptually simple task is complicated by some baggage left over from the origins of C. However, let's begin with the traditional way characters are read from the keyboard. Later you will learn an alternative.

C defines a function called `getchar()`, which returns a single character typed on the keyboard. When called, the function waits for a key to be pressed. Then `getchar()` echoes the keystroke to the screen and returns the value of the key to the caller. The `getchar()` function is defined by the ANSI C standard and requires the header file STDIO.H. This program illustrates its use by reading a character and then telling you what it received. (Remember, to display a character, use the `%c` `printf()` format specifier.)

```c
#include <stdio.h>

int main(void)
{
    char ch;

    ch = getchar(); /* read a char */
    printf("you typed: %c", ch);

    return 0;
}
```

If you try this program, it may behave differently than you expected. The trouble is this: in many C compilers, `getchar()` is implemented in such a way that it *line buffers* input. That is, it does not immediately return as soon as you have pressed a key, but waits until you have entered an entire line, which may include several other characters. This means that even though it will read and return only one character, `getchar()` waits until you enter a carriage return (i.e., press ENTER) before doing so. When `getchar()` returns, it will return the first character you typed. However, any other characters that you entered, including the carriage return, will still be in the input buffer. These characters will be consumed by subsequent input requests, such as through calls to `scanf()`. In some circumstances, this can lead to trouble. This situation is examined more closely in Chapter 8. For now, just be aware that `getchar()` may behave differently than your intuition would suggest. Of course, the programs shown in this book behave properly.

The reason that `getchar()` works the way it does is that the version of UNIX for which C was developed was line-buffered input. When C compilers were created for other interactive environments, developers had to decide how to make `getchar()` behave. Many C compiler developers have decided, for the sake of compatibility, to keep `getchar()` line-buffered, even though there is no technical reason for it. (In fact, the ANSI C standard states that `getchar()` need not be line-buffered.) When `getchar()` is implemented in a line-buffered fashion in a modern interactive environment, its use is severely limited.

Because many compilers have implemented line-buffered versions of `getchar()`, most C compilers supply another function to perform interactive console input. Although it is not defined by the ANSI C standard, most compilers call this function `getche()`. You use it just like `getchar()`, except that it will return its value immediately after a key is pressed; it does not line-buffer input. For most compilers, this function requires a header file called CONIO.H, but it might be called something different in your compiler. Thus, if you want to achieve interactive character input, you will usually need to use the `getche()` function rather than `getchar()`.

Since all readers will have access to the `getchar()` function, it will be used by most of the examples in this book that require character input. However, some examples will use the `getche()` function. If your compiler does not include this function, substitute `getchar()`. You should feel free to experiment with `getche()` on your own.

> **Note:** At the time of this writing, when using Microsoft's Visual C++ compiler, `getche()` is not compatible with C's standard input functions, such as `scanf()`. Instead, you must use special console versions of these functions, such as `cscanf()`. This and other non-standard I/O functions are described in Chapter 8. The examples in this book that use `getche()` work correctly with Visual C++ because they avoid the use of the standard input functions.

Virtually all computers use the ASCII character codes when representing characters. Therefore, characters returned by either `getchar()` or `getche()` will be represented by their ASCII codes. This is useful because the ASCII character codes are an ordered sequence; each letter's code is one greater than the previous letter; each digit's code is one greater than the previous digit. This means that 'a' is less than 'b', '2' is less than '3', and so on. You may compare characters just like you compare numbers. For example,

```c
ch = getchar();
if(ch < 'f') printf("character is less than f");
```

is a perfectly valid fragment that will display its message if the user enters any character that comes before f.

### EXAMPLES

1. This program reads a character and displays its ASCII code. This illustrates an important feature of C: You can use a character as if it were a "little integer." The program also demonstrates the use of the `getche()` function.

```c
#include <conio.h>
#include <stdio.h>

int main(void)
{
    char ch;

    printf("Enter a character: ");
    ch = getche();
    printf("\nIts ASCII code is %d", ch);

    return 0;
}
```

Because this program uses `getche()`, it responds as soon as you press a key. Before continuing, try substituting `getchar()` for `getche()` in this program and observe the results. As you will see, `getchar()` does not return a character to your program until you press ENTER.

2. One of the most common uses of character input is to obtain a menu selection. For example, this program allows the user to add, subtract, multiply, or divide two numbers.

```c
#include <stdio.h>

int main(void)
{
    int a, b;
    char ch;

    printf("Do you want to:\n");
    printf("Add, Subtract, Multiply, or Divide?\n");
    printf("Enter first letter: ");
    ch = getchar();
    printf("\n");

    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);

    if(ch=='A') printf("%d", a+b);
    if(ch=='S') printf("%d", a-b);
    if(ch=='M') printf("%d", a*b);
    if(ch=='D' && b!=0) printf("%d", a/b);

    return 0;
}
```

One point to keep in mind is that C makes a distinction between upper- and lowercase letters. So, if the user enters an **s**, the program will not recognize it as a request to subtract. (Later, you will learn how to convert the case of a character.)

3. Another common reason that your program will need to read a character from the keyboard is to obtain a yes/no response from the user. For example, this fragment determines if the user wants to proceed.

```c
printf("Do you wish to continue? (Y/N : ");
ch = getche();
if(ch=='Y') {
    /* continue with something */
}
```

### EXERCISES

1. Write a program that reads ten letters. After the letters have been read, display the one that comes earliest in the alphabet. (Hint: The one with the smallest value comes first.)
2. Write a program that displays the ASCII codes for the characters A through Z and a through z. How do the codes differ between the upper- and lowercase characters?

---

## 3.2 NEST if STATEMENTS

When an `if` statement is the target of another `if` or `else`, it is said to be *nested* within the outer `if`. Here is a simple example of a nested `if`:

```c
if(count > max) /* outer if */
    if(error) printf("Error, try again."); /* nested if */
```

Here, the `printf()` statement will only execute if `count` is greater than `max` and if `error` is nonzero. Notice how the nested `if` is indented. This is common practice. It enables anyone reading your program to know quickly that the `if` is nested and what actions are nested. A nested `if` may also appear inside a block of statements that are the target of the outer `if`.

An ANSI-standard compiler will allow you to nest `if`s at least 15 levels deep. (However, it would be rare to find such a deep nesting.)

One confusing aspect of nested `if`s is illustrated by the following fragment:

```c
if(p)
    if(q) printf("a and b are true");
else printf("To which statement does this else apply?");
```

The question suggested by the second `printf()` is: which `if` is associated with the `else`? Fortunately, the answer is quite easy: An `else` always associates with the nearest `if` in the same block that does not already have an `else` associated with it. In this example, the `else` is associated with the second `if`.

### EXAMPLES

1. It is possible to string together several `if`s and `else`s into what is sometimes called an *if-else-if ladder* or *if-else-if staircase* because of its visual appearance. In this situation a nested `if` has as its target another `if`. The general form of the if-else-if ladder is shown here:

```c
if(expression) statement;
else
    if(expression) statement;
    else
        if(expression) statement;
        .
        .
        .
        else statement;
```

The expressions are evaluated from the top downward. As soon as a true condition is found, the statement associated with it is executed, and the rest of the ladder is bypassed. If none of the expressions are true, the final `else` will be executed. That is, if all other conditional tests fail, the last `else` statement is performed. If the final `else` is not present, no action will take place if all expressions are false.

Although the indentation of the general form of the if-else-if ladder just shown is technically correct, it can lead to overly deep indentation. Because of this, the if-else-if ladder is generally written like this:

```c
if(expression)
    statement;
else if(expression)
    statement;
else if(expression)
    statement;
.
.
.
else
    statement;
```

We can improve the arithmetic program developed in Section 3.1 by using an if-else-if ladder, as shown here:

```c
#include <stdio.h>

int main(void)
{
    int a, b;
    char ch;

    printf("Do you want to:\n");
    printf("Add, Subtract, Multiply, or Divide?\n");
    printf("Enter first letter: ");
    ch = getchar();
    printf("\n");

    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);

    if(ch=='A') printf("%d", a+b);
    else if(ch=='S') printf("%d", a-b);
    else if(ch=='M') printf("%d", a*b);
    else if(ch=='D' && b!=0) printf("%d", a/b);

    return 0;
}
```

This is an improvement over the original version because once a match is found, any remaining `if` statements are skipped. This means that the program isn't wasting time on needless operations. While this is not too important in this example, you will encounter situations where it will be.

2. Nested `if` statements are very common in programming. For example, here is a further improvement to the addition drill program developed in the preceding chapter. It lets the user have a second try at getting the right answer.

```c
#include <stdio.h>

int main(void)
{
    int answer, count;
    int again;

    for(count=1; count<11; count++) {
        printf("What is %d + %d? ", count, count);
        scanf("%d", &answer);

        if(answer == count+count) printf("Right!\n");
        else {
            printf("Sorry, you're wrong\n");
            printf("Try again.\n");

            printf("\nWhat is %d + %d? ", count, count);
            scanf("%d", &answer);

            /* nested if */
            if(answer == count+count) printf("Right!\n");
            else
                printf("Wrong, the answer is %d\n", count+count);
        }
    }
    return 0;
}
```

Here, the second `if` is nested within the outer `if`'s `else` block.

### EXERCISES

1. To which `if` does the `else` relate to in this example?

```c
if(ch=='S') { /* first if */
    printf("Enter a number: ");
    scanf("%d", &y);

    /* second if */
    if(y) printf("Its square is %d.", y*y);
}
else printf("Make next selection.");
```

2. Write a program that computes the area of either a circle, rectangle, or triangle. Use an if-else-if ladder.

---

## 3.3 EXAMINE for LOOP VARIATIONS

The `for` loop in C is significantly more powerful and flexible than in most other computer languages. When you were introduced to the `for` loop in Chapter 2, you were only shown the form similar to that used by other languages. However, you will see that `for` is much more flexible.

The reason that `for` is so flexible is that the expressions we called the *initialization*, *conditional-test*, and *increment* portions of the loop are not limited to these narrow roles. The `for` loop places no limits on the types of expressions that occur inside it. For example, you do not have to use the initialization section to initialize a loop-control variable. Further, there does not need to be any loop-control variable because the conditional expression may use some other means of stopping the loop. Finally, the increment portion is technically just an expression that is evaluated each time the loop iterates. It does not have to increment or decrement a variable.

Another important reason that the `for` is so flexible is that one or more of the expressions inside it may be empty. For example, if the loop-control variable has already been initialized outside the `for`, there is no need for an initialization expression.

### EXAMPLES

1. This program continues to loop until a `q` is entered at the keyboard. Instead of testing a loop-control variable, the conditional test in this `for` checks the value of a character entered by the user.

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    int i;
    char ch;

    ch = 'a'; /* give ch an initial value */

    for(i=0; ch != 'q'; i++) {
        printf("pass: %d\n", i);
        ch = getche();
    }

    return 0;
}
```

Here, the condition that controls the loop has nothing to do with the loop-control variable. The reason `ch` is given an initial value is to prevent it from accidentally containing a `q` when the program begins.

2. As stated earlier, it is possible to leave an expression in a loop empty. For example, this program asks the user for a value and then counts down to zero from this number. Here, the loop-control variable is initialized by the user outside the loop, so the initialization portion of the loop is empty.

```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter an integer: ");
    scanf("%d", &i);

    for(; i; i--) printf("%d ", i);

    return 0;
}
```

3. Another variation to `for` is that its target may be empty. For example, this program simply keeps inputting characters until the user types `q`.

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    for(ch=getche(); ch!='q'; ch=getche());
    printf("Found the q.");

    return 0;
}
```

Notice that the statements assigning `ch` a value have been moved into the loop. This means that when the loop starts, `getche()` is called. Then, the value of `ch` is tested against `q`. Next, conceptually, the nonexistent target of the `for` is executed, and the call to `getche()` in the increment portion of the loop is executed. This process repeats until the user enters a `q`.

The reason the target of the `for` can be empty is because C allows null statements.

4. Using the `for`, it is possible to create a loop that never stops. This type of loop is usually called an *infinite loop*. Although accidentally creating an infinite loop is a bug, you will sometimes want to create one on purpose. (Later in this chapter, you will see that there are ways to exit even an infinite loop!) To create an infinite loop, use a `for` construct like this:

```c
for( ; ; ) {
    .
    .
    .
}
```

As you can see, there are no expressions in the `for`. When there is no expression in the conditional portion, the compiler assumes that it is true. Therefore, the loop continues to run.

5. In C, unlike most other computer languages, it is perfectly valid for the loop-control variable to be altered outside the increment section. For example, the following program manually increments `i` at the bottom of the loop:

```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=0; i<10; ) {
        printf("%d ", i);
        i++;
    }

    return 0;
}
```

### EXERCISES

1. Write a program that computes driving time when given the distance and the average speed. Let the user specify the number of drive time computations he or she wants to perform.
2. To create time-delay loops, `for` loops with empty targets are often used. Create a program that asks the user for a number and then iterates until zero is reached. Once the countdown is done, sound the bell, but don't display anything on the screen.
3. Even if a `for` loop uses a loop-control variable, it need not be incremented or decremented by a fixed amount. Instead, the amount added or subtracted may vary. Write a program that begins at 1 and runs to 1000. Have the program add the loop-control variable to itself inside the increment expression. This is an easy way to produce the arithmetic progression 1 2 4 8 16, and so on.

---

## 3.4 UNDERSTAND C'S while LOOP

Another of C's loops is `while`. It has this general form:

```c
while(expression) statement;
```

Of course, the target of `while` may also be a block of code. The `while` loop works by repeating its target as long as the expression is true. When it becomes false, the loop stops. The value of the expression is checked at the top of the loop. This means that if the expression is false to begin with, the loop will not execute even once.

### EXAMPLES

1. Even though the `for` is flexible enough to allow itself to be controlled by factors not related to its traditional use, you should generally select the loop that best fits the needs of the situation. For example, a better way to wait for the letter `q` to be typed is shown here using `while`. If you compare it to Example 3 in Section 3.3, you will see how much clearer this version is. (However, you will soon see that a better loop for this job exists.)

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    ch = getche();

    while(ch!='q') ch = getche();
    printf("Found the q.");

    return 0;
}
```

2. The following program is a simple code machine. It translates the characters you type into a coded form by adding 1 to each letter. That is, 'A' becomes 'B', and so forth. The program stops when you press ENTER. (The `getche()` function returns `\r` when ENTER is pressed.)

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    printf("Enter your message.\n");

    ch = getche();
    while(ch != '\r') {
        printf("%c", ch+1);
        ch = getche();
    }

    return 0;
}
```

### EXERCISES

1. In Exercise 1 of Section 3.3, you created a program that computed driving time, given distance and average speed. You used a `for` loop to let the user compute several drive times. Rework that program so that it uses a `while` loop.
2. Write a program that will decode messages that have been encoded using the code machine program in the second example in this section.

---

## 3.5 USE THE do LOOP

C's final loop is `do`, which has this general form:

```c
do {
    statements
} while(expression);
```

If only one statement is being repeated, the curly braces are not necessary. Most programmers include them, however, so that they can easily recognize that the `while` that ends the `do` is part of a `do` loop, not the beginning of a `while` loop.

The `do` loop repeats the statement or statements while the expression is true. It stops when the expression becomes false. The `do` loop is unique because it will always execute the code within the loop at least once, since the expression controlling the loop is tested at the bottom of the loop.

### EXAMPLES

1. The fact that `do` will always execute the body of its loop at least once makes it perfect for checking menu input. For example, this version of the arithmetic program reprompts the user until a valid response is entered.

```c
#include <stdio.h>

int main(void)
{
    int a, b;
    char ch;

    printf("Do you want to:\n");
    printf("Add, Subtract, Multiply, or Divide?\n");

    /* force user to enter a valid response */
    do {
        printf("Enter first letter: ");
        ch = getchar();
    } while(ch!='A' && ch!='S' && ch!='M' && ch!='D');
    printf("\n");

    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);

    if(ch=='A') printf("%d", a+b);
    else if(ch=='S') printf("%d", a-b);
    else if(ch=='M') printf("%d", a*b);
    else if(ch=='D' && b!=0) printf("%d", a/b);

    return 0;
}
```

2. The `do` loop is especially useful when your program is waiting for some event to occur. For example, this program waits for the user to type a `q`. Notice that it contains one less call to `getche()` than the equivalent program described in the section on the `while` loop.

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    do {
        ch = getche();
    } while(ch!='q');

    printf("Found the q.");

    return 0;
}
```

Since the loop condition is tested at the bottom, it is not necessary to initialize `ch` prior to entering the loop.

### EXERCISES

1. Write a program that converts gallons to liters. Using a `do` loop, allow the user to repeat the conversion. (One gallon is approximately 3.7854 liters.)
2. Write a program that displays the menu below and uses a `do` loop to check for valid responses. (Your program does not need to implement the actual functions shown in the menu.)

```
Mailing list menu:

1. Enter addresses
2. Delete address
3. Search the list
4. Print the list
5. Quit

Enter the number of your choice (1-5).
```

---

## 3.6 CREATE NESTED LOOPS

When the body of one loop contains another, the second is said to be nested inside the first. Any of C's loops may be nested within any other loop. The ANSI C standard specifies that loops may be nested at least 15 levels deep. However, most compilers allow nesting to virtually any level. As a simple example of nested `for`s, this fragment prints the numbers 1 to 10 on the screen ten times.

```c
for(i=0; i<10; i++) {
    for(j=1; j<11; j++) printf("%d ", j); /* nested loop */
    printf("\n");
}
```

### EXAMPLES

1. You can use a nested `for` to make another improvement to the arithmetic drill. In the version shown below, the program will give the user three chances to get the right answer. Notice the use of the variable `right` to stop the loop early if the correct answer is given.

```c
#include <stdio.h>

int main(void)
{
    int answer, count, chances, right;

    for(count=1; count<11; count++) {
        printf("What is %d + %d? ", count, count);
        scanf("%d", &answer);

        if(answer == count+count) printf("Right!\n");
        else {
            printf("Sorry, you're wrong.\n");
            printf("Try again.\n");

            right = 0;

            /* nested for */
            for(chances=0; chances<3 && !right; chances++) {
                printf("What is %d + %d? ", count, count);
                scanf("%d", &answer);

                if(answer == count+count) {
                    printf("Right!\n");
                    right = 1;
                }
            }

            /* if answer still wrong, tell user */
            if(!right)
                printf("The answer is %d.\n", count+count);
        }
    }

    return 0;
}
```

2. This program uses three `for` loops to print the alphabet three times, each time printing each letter twice:

```c
#include <stdio.h>

int main(void)
{
    int i, j, k;
    for(i=0; i<3; i++)
        for(j=0; j<26; j++)
            for(k=0; k<2; k++) printf("%c", 'A'+j);

    return 0;
}
```

The statement

```c
printf("%c", 'A'+j);
```

works because ASCII codes for the letters of the alphabet are strictly ascending—each one is greater than the letter that precedes it.

### EXERCISES

1. Write a program that finds all the prime numbers between 2 and 1000.
2. Write a program that reads ten characters from the keyboard. Each time a character is read, use its ASCII code value to output a string of periods equal in number to this code. For example, given the letter 'A', whose code is 65, your program would output 65 periods.

---

## 3.7 USE break TO EXIT A LOOP

The `break` statement allows you to exit a loop from any point within its body, bypassing its normal termination expression. When the `break` statement is encountered inside a loop, the loop is immediately stopped, and program control resumes at the next statement following the loop. For example, this loop prints only the numbers 1 to 10:

```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=1; i<100; i++) {
        printf("%d ", i);
        if(i==10) break; /* exit the loop */
    }

    return 0;
}
```

The `break` statement can be used with all three of C's loops. You can have as many `break` statements within a loop as you desire. However, since too many exit points from a loop tend to destructure your code, it is generally best to use the `break` for special purposes, not as your normal loop exit.

### EXAMPLES

1. The `break` statement is commonly used in loops in which a special condition can cause immediate termination. Here is an example of such a situation. In this case, a keypress can stop the execution of the program.

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    int i;
    char ch;

    /* display all numbers that are multiples of 6 */
    for(i=1; i<10000; i++) {
        if(!(i%6)) {
            printf("%d, more? (Y/N) ", i);
            ch = getche();
            if(ch=='N') break; /* stop the loop */
            printf("\n");
        }
    }

    return 0;
}
```

2. A `break` will cause an exit from only the innermost loop. For example, this program prints the numbers 0 to 5 five times:

```c
#include <stdio.h>

int main(void)
{
    int i, j;

    for(i=0; i<5; i++) {
        for(j=0; j<100; j++) {
            printf("%d ", j);
            if(j==5) break;
        }
        printf("\n");
    }

    return 0;
}
```

3. The reason C includes the `break` statement is to allow your programs to be more efficient. For example, examine this fragment:

```c
do {
    printf("Load, Save, Edit, Quit?\n");
    do {
        printf("Enter your selection: ");
        ch = getchar();
    } while(ch!='L' && ch!='S' && ch!='E' && ch!='Q');

    if(ch != 'Q') {
        /* do something */
    }

    if(ch != 'Q') {
        /* do something else */
    }
    /* etc. */
} while(ch != 'Q');
```

In this situation, several additional tests are performed on `ch` to see if it is equal to 'Q' to avoid executing certain sections of code when the Quit option is selected. Most C programmers would write the preceding loop as shown here:

```c
for( ; ; ) { /* infinite for loop */
    printf("Load, Save, Edit, Quit?\n");
    do {
        printf("Enter your selection: ");
        ch = getchar();
    } while(ch!='L' && ch!='S' && ch!='E' && ch!='Q');

    if(ch == 'Q') break;

    /* do something */
    /* do something else */
    /* etc. */
}
```

In this version, `ch` need only be tested once to see if it contains a 'Q'. As you can see, this implementation is more efficient because only one `if` statement is required.

### EXERCISES

1. On your own, write several short programs that use `break` to exit a loop. Be sure to try all three loop statements.
2. Write a program that prints a table showing the proper amount of tip to leave. Start the table at $1 and stop at $100, using increments of $1. Compute three tip percentages: 10%, 15%, and 20%. After each line, ask the user if he or she wants to continue. If not, use `break` to stop the loop and end the program.

---

## 3.8 KNOW WHEN TO USE THE continue STATEMENT

The `continue` statement is somewhat the opposite of the `break` statement. It forces the next iteration of the loop to take place, skipping any code in between itself and the test condition of the loop. For example, this program never displays any output:

```c
#include <stdio.h>

int main(void)
{
    int x;

    for(x=0; x<100; x++) {
        continue;
        printf("%d ", x); /* this is never executed */
    }

    return 0;
}
```

Each time the `continue` statement is reached, it causes the loop to repeat, skipping the `printf()` statement.

In `while` and `do-while` loops, a `continue` statement will cause control to go directly to the test condition and then continue the looping process. In the case of `for`, the increment part of the loop is performed, the conditional test is executed, and the loop continues.

Frankly, `continue` is seldom used, not because it is poor practice to use it, but simply because good applications for it are not common.

### EXAMPLE

1. One good use for `continue` is to restart a statement sequence when an error occurs. For example, this program computes a running total of numbers entered by the user. Before adding a value to the running total, it verifies that the number was correctly entered by having the user enter it a second time. If the two numbers don't match, the program uses `continue` to restart the loop.

```c
#include <stdio.h>

int main(void)
{
    int total, i, j;

    total = 0;
    do {
        printf("Enter next number (0 to stop): ");
        scanf("%d", &i);
        printf("Enter number again: ");
        scanf("%d", &j);
        if(i != j) {
            printf("Mismatch\n");
            continue;
        }
        total = total + i;
    } while(i);

    printf("Total is %d\n", total);

    return 0;
}
```

### EXERCISE

1. Write a program that prints only the odd numbers between 1 and 100. Use a `for` loop that looks like this:

```c
for(i=1; i<101; i++) . . .
```

Use a `continue` statement to avoid printing even numbers.

---

## 3.9 SELECT AMONG ALTERNATIVES WITH THE switch STATEMENT

While `if` is good for choosing between two alternatives, it quickly becomes cumbersome when several alternatives are needed. C's solution to this problem is the `switch` statement. The `switch` statement is C's multiple selection statement. It is used to select one of several alternative paths in program execution and works as follows: A value is successively tested against a list of integer or character constants. When a match is found, the statement sequence associated with that match is executed. The general form of the `switch` statement is this:

```c
switch(value) {
    case constant1:
        statement sequence
        break;
    case constant2:
        statement sequence
        break;
    case constant3:
        statement sequence
        break;
    .
    .
    .
    default:
        statement sequence
        break;
}
```

The `default` statement sequence is performed if no matches are found. The `default` is optional. If all matches fail and `default` is absent, no action takes place. When a match is found, the statements associated with that `case` are executed until `break` is encountered or, in the case of `default` or the last `case`, the end of the `switch` is reached.

As a very simple example, this program recognizes the numbers 1, 2, 3, and 4 and prints the name of the one you enter. That is, if you enter 2, the program displays **two**.

```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter a number between 1 and 4: ");
    scanf("%d", &i);

    switch(i) {
        case 1:
            printf("one");
            break;
        case 2:
            printf("two");
            break;
        case 3:
            printf("three");
            break;
        case 4:
            printf("four");
            break;
        default:
            printf("Unrecognized Number");
    }

    return 0;
}
```

The `switch` statement differs from `if` in that `switch` can only test for equality, whereas the `if` conditional expression can be of any type. Also, `switch` will work with only `int` or `char` types. You cannot, for example, use floating-point numbers.

The statement sequences associated with each case are *not* blocks; they are not enclosed by curly braces.

The ANSI C standard states that at least 257 `case` statements will be allowed. In practice, you should usually limit the amount of case statements to a much smaller number for efficiency reasons. Also, no two `case` constants in the same `switch` can have identical values.

It is possible to have a `switch` as part of the statement sequence of an outer `switch`. This is called a *nested switch*. If the case constants of the inner and outer switch contain common values, no conflicts will arise. For example, the following code fragment is perfectly acceptable:

```c
switch(a) {
    case 1:
        switch(b) {
            case 0: printf("b is false");
                break;
            case 1: printf("b is true");
                break;
        }
        break;
    case 2:
        .
        .
        .
}
```

An ANSI-standard compiler will allow at least 15 levels of nesting for `switch` statements.

### EXAMPLES

1. The `switch` statement is often used to process menu commands. For example, the arithmetic program can be recoded as shown here. This version reflects the way professional C code is written.

```c
#include <stdio.h>

int main(void)
{
    int a, b;
    char ch;

    printf("Do you want to:\n");
    printf("Add, Subtract, Multiply, or Divide?\n");
    /* force user to enter a valid response */
    do {
        printf("Enter first letter: ");
        ch = getchar();
    } while(ch!='A' && ch!='S' && ch!='M' && ch!='D');
    printf("\n");

    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);

    switch(ch) {
        case 'A': printf("%d", a+b);
            break;
        case 'S': printf("%d", a-b);
            break;
        case 'M': printf("%d", a*b);
            break;
        case 'D': if(b!=0) printf("%d", a/b);
    }

    return 0;
}
```

2. Technically, the `break` statement is optional. The `break` statement, when encountered within a `switch`, causes the program flow to exit from the entire `switch` statement and continue on to the next statement outside the switch. This is much the way it works when breaking out of a loop. However, if a `break` statement is omitted, execution continues into the following `case` or `default` statement (if either exists). That is, when a `break` statement is missing, execution "falls through" into the next case and stops only when a `break` statement or the end of the switch is encountered. For example, study this program carefully:

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    do {
        printf("\nEnter a character, q to quit: ");
        ch = getche();
        printf("\n");

        switch(ch) {
            case 'a':
                printf("Now is ");
            case 'b':
                printf("the time ");
            case 'c':
                printf("for all good men");
                break;
            case 'd':
                printf("The summer ");
            case 'e':
                printf("soldier ");
        }
    } while(ch != 'q');

    return 0;
}
```

If the user types **a**, the entire phrase **Now is the time for all good men** is displayed. Typing **b** displays **the time for all good men**. As you can see, once execution begins inside a case, it continues until a `break` statement or the end of the switch is encountered.

3. The statement sequence associated with a case may be empty. This allows two or more cases to share a common statement sequence without duplication of code. For example, here is a program that categorizes letters into vowels and consonants:

```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    printf("Enter the letter: ");
    ch = getche();

    switch(ch) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'y':
            printf(" is a vowel\n");
            break;
        default:
            printf(" is a consonant");
    }

    return 0;
}
```

### EXERCISES

1. What is wrong with this fragment?

```c
float f;

scanf("%f", &f);

switch(f) {
    case 10.05:
        .
        .
        .
}
```

2. Write a program that counts the numbers of letters, digits, and common punctuation symbols entered by the user. Stop inputting when the user presses ENTER. Use a `switch` statement to categorize the characters into punctuation, digits, and letters. When the program ends, report the number of characters in each category. (If you like, simply assume that, if a character is not a digit or punctuation, it is a letter. Also, just use the most common punctuation symbols.)

---

## 3.10 UNDERSTAND THE goto STATEMENT

C supports a non-conditional jump statement, called the `goto`. Because C is a replacement for assembly code, the inclusion of `goto` is necessary because it can be used to create very fast routines. However, most programmers do not use `goto` because it destructures a program and, if frequently used, can render the program virtually impossible to understand later. Also, there is no routine that requires a `goto`. For these reasons, it is not used in this book outside of this section.

The `goto` statement can perform a jump within a function. It cannot jump between functions. It works with a *label*. In C, a label is a valid identifier name followed by a colon. For example, the following `goto` jumps around the `printf()` statement:

```c
goto mylabel;
printf("This will not print.");
mylabel: printf("This will print.");
```

About the only good use for `goto` is to jump out of a deeply nested routine when a catastrophic error occurs.

### EXAMPLE

1. This program uses `goto` to create the equivalent of a `for` loop running from 1 to 10. (This is just an example of `goto`. In actual practice, you should use a real `for` loop when one is needed.)

```c
#include <stdio.h>

int main(void)
{
    int i;

    i = 1;
again:
    printf("%d ", i);
    i++;
    if(i<10) goto again;

    return 0;
}
```

### EXERCISE

1. Write a program that uses `goto` to emulate a `while` loop that counts from 1 to 10.

---

## Mastery Skills Check

At this point, you should be able to answer these questions and perform these exercises:

1. As illustrated by Exercise 2 in Section 3.1, the ASCII codes for the lowercase letters are separated from the uppercase letters by a difference of 32. Therefore, to convert a lowercase letter to an uppercase one, simply subtract 32 from it. Write a program that reads characters from the keyboard and displays lowercase letters as uppercase ones. Stop when ENTER is pressed.
2. Using a nested `if` statement, write a program that prompts the user for a number and then reports if the number is positive, zero, or negative.
3. Is this a valid `for` loop?
```c
char ch;

ch = 'x';
for( ; ch != ' ' ; ) ch = getche();
```
4. Show the traditional way to create an infinite loop in C.
5. Using the three loop statements, show three different ways to count from 1 to 10.
6. What does the `break` statement do when used in a loop?
7. Is this `switch` statement correct?
```c
switch(i) {
    case 1: printf("nickel");
        break;
    case 2: printf("dime");
        break;
    case 3: printf("quarter");
}
```
8. Is this `goto` fragment correct?
```c
goto alldone;
.
.
.
alldone
```

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. Using a `switch` statement, write a program that reads characters from the keyboard and watches for tabs, newlines, and backspaces. When one is received, display what it is in words. For example, when the user presses the TAB key, print **tab**. Have the user enter a **q** to stop the program.
2. While this program is not incorrect, show how it would look if written by an experienced C programmer:

```c
#include <stdio.h>

int main(void)
{
    int i, j, k;

    for(k=0; k<10; k=k+1) {
        printf("Enter first number: ");
        scanf("%d", &i);

        printf("Enter second number: ");
        scanf("%d", &j);

        if(j != 0) printf("%d\n", i/j);
        if(j == 0) printf("cannot divide by zero\n");
    }

    return 0;
}
```
