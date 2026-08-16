# 2 Introducing C's Program Control Statements

IN this chapter you will learn about two of C's most important program control statements: **if** and **for**. In general, program control statements determine your program's flow of execution. As such, they form the backbone of your programs. In addition to these, you will also learn about blocks of code, the relational and logical operators, and more about the `printf()` function.

---

### Review Skills Check

Before proceeding, you should be able to correctly answer these questions and do these exercises:

1. All C programs are composed of one or more functions. What is the name of the function that all programs must have? Further, what special purpose does it perform?
2. The `printf()` function is used to output information to the screen. Write a program that displays **This is the number 100.** (Output the 100 as a number, not as a string.)
3. Header files contain information used by the standard library functions. How do you tell the compiler to include one in your program? Give an example.
4. C supports five basic types of data. Name them.
5. Which of these variable names are invalid in C?
   a. `_count`  
   b. `123count`  
   c. `$test`  
   d. `This_is_a_long_name`  
   e. `new-word`  
6. What is `scanf()` used for?
7. Write a program that inputs an integer from the keyboard and displays its square.
8. How are comments entered into a C program? Give an example.
9. How does a function return a value to the routine that called it?
10. A function called `Myfunc()` has these three parameters: an `int` called **count**, a `float` called **balance**, and a `char` called **ch**. The function does not return a value. Show how this function is prototyped.

---

## 2.1 BECOME FAMILIAR WITH THE if

The `if` statement is one of C's selection statements (sometimes called *conditional statements*). Its operation is governed by the outcome of a conditional test that evaluates to either true or false. Simply put, selection statements make decisions based upon the outcome of some condition.

In its simplest form, the `if` statement allows your program to conditionally execute a statement. This form of the `if` is shown here:

```c
if(expression) statement;
```

The *expression* may be any valid C expression. If the expression evaluates as true, the statement will be executed. If it does not, the statement is bypassed, and the line of code following the `if` is executed. In C, an expression is true if it evaluates to any nonzero value. If it evaluates to zero, it is false. The statement that follows an `if` is usually referred to as the *target* of the `if` statement.

Commonly, the expression inside the `if` compares one value with another using a *relational operator*. Although you will learn about all the relational operators later in this chapter, three are introduced here so that we can create some example programs. A relational operator tests how one value relates to another. For example, to see if one value is greater than another, C uses the `>` relational operator. The outcome of this comparison is either true or false. For example, `10 > 9` is true, but `9 > 10` is false. Therefore, the following `if` will cause the message **true** to be displayed:

```c
if(10 > 9) printf("true");
```

However, because the expression in the following statement is false, the `if` does not execute its target statement:

```c
if(5 > 9) printf("this will not print");
```

C uses `<` as its *less than* operator. For example, `10 < 11` is true. To test for equality, C provides the `==` operator. (There can be no space between the two equal signs.) Therefore, `10 == 10` is true, but `10 == 11` is not.

Of course, the expression inside the `if` may involve variables. For example, the following program tells whether an integer entered from the keyboard is negative or non-negative:

```c
#include <stdio.h>

int main(void)
{
    int num;

    printf("Enter an integer: ");
    scanf("%d", &num);

    if(num < 0) printf("Number is negative.");
    if(num > -1) printf("Number is non-negative.");

    return 0;
}
```

Remember, in C, true is any nonzero value and false is zero. Therefore, it is perfectly valid to have an `if` statement such as the one shown here:

```c
if(count+1) printf("Not Zero");
```

### EXAMPLES

1. This program forms the basis for an addition drill. It displays two numbers and asks the user what the answer is. The program then tells the user if the answer is right or wrong.

```c
#include <stdio.h>

int main(void)
{
    int answer;

    printf("What is 10 + 14? ");
    scanf("%d", &answer);
    if(answer == 10+14) printf("Right!");

    return 0;
}
```

2. This program converts either feet to meters or meters to feet, depending upon what the user requests.

```c
#include <stdio.h>

int main(void)
{
    float num;
    int choice;

    printf("Enter value: ");
    scanf("%f", &num);

    printf("1: Feet to Meters, 2: Meters to Feet. ");
    printf("Enter choice: ");
    scanf("%d", &choice);

    if(choice == 1) printf("%f", num / 3.28);
    if(choice == 2) printf("%f", num * 3.28);

    return 0;
}
```

### EXERCISES

1. Which of these expressions are true?
   a. `0`  
   b. `1`  
   c. `10 * 9 < 90`  
   d. `1 == 1`  
   e. `-1`  
2. Write a program that asks the user for an integer and then tells the user if that number is even or odd. (Hint, use C's modulus operator `%`.)

---

## 2.2 ADD THE else

You can add an `else` statement to the `if`. When this is done, the `if` statement looks like this:

```c
if(expression) statement1;
else statement2;
```

If the expression is true, then the target of the `if` will execute, and the `else` portion will be skipped. However, if the expression is false, then the target of the `if` is bypassed, and the target of the `else` will execute. Under no circumstances will both statements execute. Thus, the addition of the `else` provides a two-way decision path.

### EXAMPLES

1. You can use the `else` to create more efficient code in some cases. For example, here the `else` is used in place of a second `if` in the program from the preceding section, which determines whether a number is negative or non-negative:

```c
#include <stdio.h>

int main(void)
{
    int num;

    printf("Enter an integer: ");
    scanf("%d", &num);

    if(num < 0) printf("Number is negative.");
    else printf("Number is non-negative.");

    return 0;
}
```

Recall that the original version of this program explicitly tested for non-negative numbers by comparing `num` to -1 using a second `if` statement. But since there are only two possibilities—`num` is either negative or non-negative—there is no reason for this second test. Because of the way a C compiler generates code, the `else` requires far fewer machine instructions than an additional `if` and is, therefore, more efficient.

2. This program prompts the user for two numbers, divides the first by the second, and displays the result. However, division by zero is undefined, so the program uses an `if` and an `else` statement to prevent division by zero from occurring.

```c
#include <stdio.h>

int main(void)
{
    int num1, num2;

    printf("Enter first number: ");
    scanf("%d", &num1);

    printf("Enter second number: ");
    scanf("%d", &num2);

    if(num2 == 0) printf("Cannot divide by zero.");
    else printf("Answer is: %d.", num1 / num2);

    return 0;
}
```

### EXERCISES

1. Write a program that requests two numbers and then displays either their sum or product, depending on what the user selects.
2. Rewrite Exercise 2 from Section 2.1 so that it uses an `else` statement.

---

## 2.3 CREATE BLOCKS OF CODE

In C, you can link two or more statements together. This is called a *block of code* or a *code block*. To create a block of code, you surround the statements in the block with opening and closing curly braces. Once this is done, the statements form one logical unit, which may be used anywhere that a single statement may.

For example, the general form of the `if` using blocks of code is:

```c
if(expression) {
    statement1;
    statement2;
    .
    .
    statement N;
}
else {
    statement1;
    statement2;
    .
    .
    statement N;
}
```

If the expression evaluates to true, then all the statements in the block of code associated with the `if` will be executed. If the expression is false, then all the statements in the `else` block will be executed. (Remember, the `else` is optional and need not be present.) For example, this fragment prints the message **This is an example of a code block.** if the user enters any positive number:

```c
scanf("%d", &num);

if(num > 0) {
    printf("This is ");
    printf("an example of ");
    printf("a code block.");
}
```

Keep in mind that a block of code represents one indivisible logical unit. This means that under no circumstances could one of the `printf()` statements in this fragment execute without the others also executing.

In the example shown, the statements that appear within the block of code are indented. Although C does not care where a statement appears on a line, it is common practice to indent one level at the start of a block. Indenting makes the structure of a program easier to understand. Also, the placement of the curly braces is arbitrary. However, the way they are shown in the example is a common method and will be used by the examples in this book.

In C, as you will see, you can use a block of code anywhere you can use a single statement.

### EXAMPLES

1. This program is an improved version of the feet-to-meters, meters-to-feet conversion program. Notice how the use of code blocks allows the program to prompt specifically for each unit.

```c
#include <stdio.h>

int main(void)
{
    float num;
    int choice;

    printf("1: Feet to Meters, 2: Meters to Feet. ");
    printf("Enter choice: ");
    scanf("%d", &choice);

    if(choice == 1) {
        printf("Enter number of feet: ");
        scanf("%f", &num);
        printf("Meters: %f", num / 3.28);
    }
    else {
        printf("Enter number of meters: ");
        scanf("%f", &num);
        printf("Feet: %f", num * 3.28);
    }

    return 0;
}
```

2. Using code blocks, we can improve the addition drill program so that it also prints the correct answer when the user makes a mistake.

```c
#include <stdio.h>

int main(void)
{
    int answer;

    printf("What is 10 + 14? ");
    scanf("%d", &answer);

    if(answer == 10+14) printf("Right!");
    else {
        printf("Sorry, you're wrong. ");
        printf("The answer is 24.");
    }

    return 0;
}
```

This example illustrates an important point: it is not necessary for targets of both the `if` and the `else` statements to be blocks of code. In this case, the target of `if` is a single statement, while the target of `else` is a block. Remember, you are free to use either a single statement or a code block at either place.

### EXERCISES

1. Write a program that either adds or subtracts two integers. First, prompt the user to choose an operation; then prompt for the two numbers and display the result.
2. Is this fragment correct?

```c
if(count < 100)
    printf("Number is less than 100.");
    printf("Its square is %d.", count * count);
```

---

## 2.4 USE THE for LOOP

The `for` loop is one of C's three loop statements. It allows one or more statements to be repeated. If you have programmed in any other computer language, such as BASIC or Pascal, you will be pleased to learn that the `for` behaves much like its equivalent in other languages.

The `for` loop is considered by many C programmers to be its most flexible loop. Although the `for` loop allows a large number of variations, we will examine only its most common form in this section.

The `for` loop is used to repeat a statement or block of statements a specified number of times. Its general form for repeating a single statement is shown here:

```c
for(initialization; conditional-test; increment) statement;
```

The *initialization* section is used to give an initial value to the variable that controls the loop. This variable is usually referred to as the *loop-control variable*. The initialization section is executed only once, before the loop begins. The *conditional-test* portion of the loop tests the loop-control variable against a target value. If the conditional test evaluates true, the loop repeats. If it is false, the loop stops, and program execution picks up with the next line of code that follows the loop. The conditional test is performed at the start or *top* of the loop each time the loop is repeated. The *increment* portion of the `for` is executed at the bottom of the loop. That is, the increment portion is executed after the statement or block that forms its body has been executed. The purpose of the increment portion is to increase (or decrease) the loop-control value by a certain amount.

As a simple first example, this program uses a `for` loop to print the numbers 1 through 10 on the screen:

```c
#include <stdio.h>

int main(void)
{
    int num;

    for(num=1; num<11; num=num+1) printf("%d ", num);
    printf("terminating");

    return 0;
}
```

This program produces the following output:

```
1 2 3 4 5 6 7 8 9 10 terminating
```

The program works like this: First, the loop control variable `num` is initialized to 1. Next, the expression `num < 11` is evaluated. Since it is true, the `for` loop begins running. After the number is printed, `num` is incremented by one and the conditional test is evaluated again. This process continues until `num` equals 11. When this happens, the `for` loop stops, and `terminating` is displayed. Keep in mind that the initialization portion of the `for` loop is only executed once, when the loop is first entered.

As stated earlier, the conditional test is performed at the start of each iteration. This means that if the test is false to begin with, the loop will not execute even once. For example, this program only displays `terminating` because `num` is initialized to 11, causing the conditional test to fail:

```c
#include <stdio.h>

int main(void)
{
    int num;

    /* this loop will not execute */
    for(num=11; num<11; num=num+1) printf("%d ", num);

    printf("terminating");

    return 0;
}
```

To repeat several statements, use a block of code as the target of the `for` loop. For example, this program computes the product and sum of the numbers from 1 to 5:

```c
#include <stdio.h>

int main(void)
{
    int num, sum, prod;

    sum = 0;
    prod = 1;

    for(num=1; num<6; num=num+1) {
        sum = sum + num;
        prod = prod * num;
    }
    printf("product and sum: %d %d", prod, sum);

    return 0;
}
```

A `for` loop can run negatively. For example, this fragment decrements the loop-control variable:

```c
for(num=20; num>0; num=num-1)...
```

Further, the loop-control variable may be incremented or decremented by more than one. For example, this program counts to 100 by fives:

```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=0; i<101; i=i+5) printf("%d ", i);

    return 0;
}
```

### EXAMPLES

1. The addition-drill program created earlier can be enhanced using a `for` loop. The version shown here asks for the sums of the numbers between 1 and 10. That is, it asks for 1 + 1, then 2 + 2, and so on. This program would be useful to a first grader who is learning to add.

```c
#include <stdio.h>

int main(void)
{
    int answer, count;

    for(count=1; count<11; count=count+1) {
        printf("What is %d + %d? ", count, count);
        scanf("%d", &answer);

        if(answer == count+count) printf("Right! ");
        else {
            printf("Sorry, you're wrong. ");
            printf("The answer is %d. ", count+count);
        }
    }

    return 0;
}
```

Notice that this program has an `if` statement as part of the `for` block. Notice further that the target of `else` is a block of code. This is perfectly valid. In C, a code block may contain statements that create other code blocks. Notice how the indentation adds clarity to the structure of the program.

2. We can use a `for` loop to create a program that determines if a number is prime. The following program asks the user to enter a number and then checks to see if it has any factors.

```c
/* Prime number tester. */
#include <stdio.h>

int main(void)
{
    int num, i, is_prime;

    printf("Enter the number to test: ");
    scanf("%d", &num);

    /* now test for factors */
    is_prime = 1;
    for(i=2; i<=num/2; i=i+1)
        if((num%i)==0) is_prime = 0;

    if(is_prime==1) printf("The number is prime.");
    else printf("The number is not prime.");

    return 0;
}
```

### EXERCISES

1. Create a program that prints the numbers from 1 to 100.
2. Write a program that prints the numbers between 17 and 100 that can be evenly divided by 17.
3. Write a program similar to the prime-number tester, except that it displays all the factors of a number entered by the user. For example, if the user entered 8, it would respond with 2 and 4.

---

## 2.5 SUBSTITUTE C'S INCREMENT AND DECREMENT OPERATORS

When you learned about the `for` in the preceding section, the increment portion of the loop looked more or less like the one shown here:

```c
for(num=0; num<some_value; num=num+1)...
```

Although not incorrect, you will almost never see a statement like `num = num + 1` in professionally written C programs because C provides a special operator that increments a variable by one. The *increment operator* is `++` (two pluses with no intervening space). Using the increment operator, you can change this line of code:

```c
i = i + 1;
```

into this:

```c
i++;
```

Therefore, the `for` shown earlier will normally be written like this:

```c
for(num=0; num<some_value; num++)...
```

In a similar fashion, to decrease a variable by one, you can use C's *decrement operator*, `--`. (There must be no space between the two minus signs.) Therefore,

```c
count = count - 1;
```

can be rewritten as

```c
count--;
```

Aside from saving you a little typing effort, the reason you will want to use the increment and decrement operators is that, for most C compilers, they will be faster than the equivalent assignment statements. The reason for this difference is that the C compiler can often avoid separate load-and-store machine-language instructions and substitute a single increment or decrement instruction in the executable version of a program.

The increment and decrement operators do not need to follow the variable; they can precede it. Although the effect on the variable is the same, the position of the operator does affect *when* the operation is performed. To see how, examine this program:

```c
#include <stdio.h>

int main(void)
{
    int i, j;

    i = 10;
    j = i++;

    /* this will print 11 10 */
    printf("i and j: %d %d", i, j);

    return 0;
}
```

Don't let the `j = i++;` statement trouble you. The increment operator may be used as part of any valid C expression. This statement works like this: First, the current value of `i` is assigned to `j`. Then `i` is incremented. This is why `j` has the value 10, not 11. When the increment or decrement operator *follows* the variable, the operation is performed *after* its value has been obtained for use in the expression. Therefore, assuming that `max` has the value 1, an expression such as this:

```c
count = 10 * max++;
```

assigns the value 10 to `count` and increases `max` by one.

If the variable is *preceded* by the increment or decrement operator, the operation is performed *first*, and then the value of the variable is obtained for use in the expression. For example, rewriting the previous program as follows causes `j` to be 11.

```c
#include <stdio.h>

int main(void)
{
    int i, j;

    i = 10;
    j = ++i;

    /* this will print 11 11 */
    printf("i and j: %d %d", i, j);

    return 0;
}
```

If you are simply using the increment or decrement operators to replace equivalent assignment statements, it doesn't matter if the operator precedes or follows the variable. This is a matter of your own personal style.

### EXAMPLES

1. Here is the addition drill program developed in Section 2. It has been rewritten using the increment operator.

```c
#include <stdio.h>

int main(void)
{
    int answer, count;

    for(count=1; count<11; count++) {
        printf("What is %d + %d? ", count, count);
        scanf("%d", &answer);

        if(answer == count+count) printf("Right! ");
        else {
            printf("Sorry, you're wrong. ");
            printf("The answer is %d. ", count+count);
        }
    }

    return 0;
}
```

2. This program illustrates the use of the increment and decrement operators:

```c
#include <stdio.h>

int main(void)
{
    int i;

    i = 0;

    i++;
    printf("%d ", i); /* prints 1 */
    i--;
    printf("%d ", i); /* prints 0 */

    return 0;
}
```

### EXERCISES

1. Rewrite the answer to the `for` loop exercises in the previous section so that they use the increment or decrement operators.
2. Change all appropriate assignment statements in this program to increment or decrement statements.

```c
#include <stdio.h>

int main(void)
{
    int a, b;

    a = 1;
    a = a + 1;
    b = a;
    b = b - 1;
    printf("%d %d", a, b);

    return 0;
}
```

---

## 2.6 EXPAND printf( )'S CAPABILITIES

So far, we have only used `printf()` to output text, integers, and floating-point values. However, `printf()` has several other capabilities. One important feature is the use of *backslash-character constants* (also called *escape sequences*).

In C, the backslash character `\` is an escape character. When used inside a string, it signals the compiler that a special character code follows.

#### TABLE 2-1: Backslash Character Codes

| Code | Meaning |
| :--- | :--- |
| `\b` | Backspace |
| `\f` | Form feed |
| `\n` | Newline |
| `\r` | Carriage return |
| `\t` | Horizontal tab |
| `\"` | Double quote |
| `\'` | Single quote |
| `\0` | Null |
| `\\` | Backslash |
| `\v` | Vertical tab |
| `\a` | Alert (bell) |
| `\N` | Octal constant (where N is an octal constant) |
| `\xN` | Hexadecimal constant (where N is a hex constant) |

You can enter any special character by specifying it as an octal or hexadecimal value following the backslash. The octal number system is based on 8 and uses the digits 0 through 7. In octal, the number 10 is the same as 8 in decimal. The hexadecimal number system is based on 16 and uses the digits 0 through 9 plus the letters 'A' through 'F', which stand for 10, 11, 12, 13, 14, and 15. For example, the hexadecimal number 10 is 16 in decimal. When specifying a character in hexadecimal, you must follow the backslash with an 'x', followed by the number.

The ASCII character set is defined from 0 to 127. However, many computers, including most PCs, use the values 128 to 255 for special and graphics characters. If your computer supports these extra characters, the following program will display a few of them on the screen.

```c
#include <stdio.h>

int main(void)
{
    printf("\xA0 \xA1 \xA2 \xA3");

    return 0;
}
```

The `\n` newline character does not have to go at the end of the string that is being output by `printf()`; it can go anywhere in the string. Further, there can be as many newline characters in a string as you desire. The point is that there is no connection between a newline and the end of a string. For example, this program:

```c
#include <stdio.h>

int main(void)
{
    printf("one\ntwo\nthree\nfour");

    return 0;
}
```

displays

```
one
two
three
four
```

on the screen.

### EXERCISES

1. Write a program that outputs a table of numbers. Each line in the table contains three entries: the number, its square, and its cube. Begin with **1** and end with **10**. Also, use a `for` loop to generate the numbers.
2. Write a program that prompts the user for an integer value. Next, using a `for` loop, make it count down from this value to 0, displaying each number on its own line. When it reaches 0, have it sound the bell.
3. Experiment on your own with the backslash codes.

---

## 2.7 PROGRAM WITH C'S RELATIONAL AND LOGICAL OPERATORS

The C language contains a rich set of operators. In this section you will learn about C's relational and logical operators. As you saw earlier, the relational operators compare two values and return a true or false result based upon that comparison. The logical operators connect together true/false results. These operators are shown in Table 2-2 and Table 2-3.

#### TABLE 2-2: Relational Operators

| Operator | Action |
| :--- | :--- |
| `>` | Greater than |
| `>=` | Greater than or equal |
| `<` | Less than |
| `<=` | Less than or equal |
| `==` | Equal |
| `!=` | Not equal |

The logical operators are used to support the basic logical operations of AND, OR, and NOT according to this truth table. The table uses 1 for true and 0 for false.

#### Logical Truth Table

| p | q | p && q | p \|\| q | !p |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |

The relational and logical operators are both lower in precedence than the arithmetic operators. This means that an expression like

```c
10 + count > a + 12
```

is evaluated as if it were written

```c
(10 + count) > (a + 12)
```

#### TABLE 2-3: Logical Operators

| Operator | Action |
| :--- | :--- |
| `&&` | AND |
| `\|\|` | OR |
| `!` | NOT |

You may link any number of relational operations together using logical operators. For example, this expression joins three relational operations:

```c
var > max || !(max==100) && 0 <= item
```

The table below shows the relative precedence of the relational and logical operators:

```
Highest    !
           > >= < <=
           == !=
           &&
Lowest     ||
```

There is one important fact to remember about the values produced by the relational and logical operators: the result is either 0 or 1. Even though C defines true as any nonzero value, the relational and logical operators always produce the value 1 for true. Your programs may make use of this fact.

You can use the relational and logical operators in both the `if` and `for` statements. For example, the following statement reports when both `a` and `b` are positive:

```c
if(a>0 && b>0) printf("Both are positive.");
```

### EXAMPLES

1. In professionally written C code, it is uncommon to find a statement like this:

```c
if(count != 0)...
```

The reason is that in C, true is any nonzero value and false is zero. Therefore, the preceding statement is generally written as this:

```c
if(count)...
```

Further, statements like this:

```c
if(count == 0)...
```

are generally written as:

```c
if(!count)...
```

The expression `!count` is true only if `count` is zero.

2. It is important to remember that the outcome of a relational or logical operation is 0 when false and 1 when true. For example, the following program requests two integers, then displays the outcome of each relational and logical operation when applied to them. In all cases, the result will be a 0 or a 1.

```c
#include <stdio.h>

int main(void)
{
    int i, j;

    printf("Enter first number: ");
    scanf("%d", &i);
    printf("Enter second number: ");
    scanf("%d", &j);

    /* relational operations */
    printf("i < j %d\n", i < j);
    printf("i <= j %d\n", i <= j);
    printf("i == j %d\n", i == j);
    printf("i > j %d\n", i > j);
    printf("i >= j %d\n", i >= j);

    /* logical operations */
    printf("i && j %d\n", i && j);
    printf("i || j %d\n", i || j);
    printf("!i !j %d %d\n", !i, !j);

    return 0;
}
```

3. C does not define an exclusive-OR (XOR) logical operator. However, it is easy to create a function that performs the operation. The XOR operation uses this truth table:

| p | q | XOR |
| :---: | :---: | :---: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

That is, the XOR operation produces a true result when one and only one operand is true. The following function uses the `&&` and `||` operators to construct an XOR operation. It compares the values of its two arguments and returns the outcome of an XOR operation.

```c
int xor(int a, int b)
{
    return (a || b) && !(a && b);
}
```

The following program uses this function. It displays the result of an AND, OR, and XOR on the values you enter.

```c
/* This program demonstrates the xor() function. */
#include <stdio.h>

int xor(int a, int b);

int main(void)
{
    int p, q;

    printf("enter P (0 or 1): ");
    scanf("%d", &p);
    printf("enter Q (0 or 1): ");
    scanf("%d", &q);
    printf("P AND Q: %d\n", p && q);
    printf("P OR Q: %d\n", p || q);
    printf("P XOR Q: %d\n", xor(p, q));

    return 0;
}

int xor(int a, int b)
{
    return (a || b) && !(a && b);
}
```

### EXERCISES

1. What does this loop do?
```c
for(x=0; x<100; x++) printf("%d ", x);
```
2. Is this expression true?
```c
!(10==9)
```
3. Do these two expressions evaluate to the same outcome?
   a. `0 && 1 || 1`  
   b. `0 && (1 || 1)`  
4. On your own, experiment with the relational and logical operators.

---

## Mastery Skills Check

1. Write a program that plays a computerized form of the "guess the magic number" game. It works like this: The player has ten tries to guess the magic number. If the number entered is the value you have selected for your magic number, have the program print the message **RIGHT!** and then terminate. Otherwise, have the program report whether the guess was high or low and then let the player enter another number. This process goes on until the player guesses the number or the ten tries have been used up. For fun, you might want to report the number of tries it takes to guess the number.
2. Write a program that computes the square footage of a house given the dimensions of each room. Have the program ask the user how many rooms are in the house and then request the dimensions of each room. Display the resulting total square footage.
3. What are the increment and decrement operators and what do they do?
4. Create an improved addition-drill program that keeps track of the number of right and wrong answers and displays them when the program ends.
5. Write a program that prints the numbers 1 to 100 using 5 columns. Have each number separated from the next by a tab.

---

## Cumulative Skills Check

This section checks how well you have integrated the material in this chapter with that from earlier chapters.

1. Using a switch statement, write a program that reads characters from the keyboard and watches for tabs, newlines, and backspaces. When one is received, display what it is in words. For example, when the user presses the TAB key, print **tab**. Have the user enter a **q** to stop the program.
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
