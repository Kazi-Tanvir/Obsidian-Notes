# Appendix D: Answers

---

## Chapter 1

### 1.3 EXERCISES

2.
```c
#include <stdio.h>

int main(void)
{
    int num;

    num = 1000;
    printf("%d is the value of num", num);

    return 0;
}
```

---

### 1.4 EXERCISES

2.
```c
#include <stdio.h>

int main(void)
{
    float a, b;

    printf("Enter two numbers: ");
    scanf("%f", &a);
    scanf("%f", &b);
    printf("Their sum is %f.", a+b);

    return 0;
}
```

---

### 1.5 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int len, width, height;

    printf("Enter length: ");
    scanf("%d", &len);
    printf("Enter width: ");
    scanf("%d", &width);
    printf("Enter height: ");
    scanf("%d", &height);

    printf("Volume is %d.", len * width * height);

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    printf("Number of seconds in a year: ");
    printf("%f", 60.0 * 60.0 * 24.0 * 365.0);

    return 0;
}
```

---

### 1.6 EXERCISES

2. Yes, a comment can contain nothing.
3. Yes, you can temporarily remove a line of code from your program by making it into a comment. This is sometimes called "commenting out" a line of code.

---

### 1.7 EXERCISES

2.
```c
#include <stdio.h>

void one(void);
void two(void);

int main(void)
{
    one();
    two();

    return 0;
}

void one(void)
{
    printf("The summer soldier, ");
}

void two(void)
{
    printf("the sunshine patriot.");
}
```

3. The compiler will report an error. The prototype is needed in order for the compiler to properly call `func1()`.

---

### 1.8 EXERCISES

2.
```c
#include <stdio.h>

int convert(void);

int main(void)
{
    printf("%d", convert());

    return 0;
}

int convert(void)
{
    int dollars;

    printf("Enter number of dollars: ");
    scanf("%d", &dollars);
    return dollars / 2;
}
```

3. There is nothing technically wrong with the program. However, function `f1()` returns an integer value, but it is being assigned to a variable of type **double**. This would lead one to suspect that perhaps the programmer has misunderstood the purpose of the `f1()` function.
4. A function declared with a void return type cannot return a value.

---

### 1.9 EXERCISES

1.
```c
#include <stdio.h>

void outnum(int num);

int main(void)
{
    outnum(10);

    return 0;
}

void outnum(int num)
{
    printf("%d", num);
}
```

2. The `sqr_it()` function requires an integer argument, but it is called with a floating-point value.

---

### MASTERY SKILLS CHECK

1.
```c
#include <stdio.h>

int main(void)
{
    float weight;

    printf("Enter your weight: ");
    scanf("%f", &weight);
    printf("Effective moon weight: %f", weight * 0.17);

    return 0;
}
```

2. The comment is not terminated with a `*/`.
3.
```c
#include <stdio.h>

int o_to_c(int o);

int main(void)
{
    int ounces;
    int cups;

    printf("Enter ounces: ");
    scanf("%d", &ounces);

    cups = o_to_c(ounces);
    printf("%d cups", cups);

    return 0;
}

int o_to_c(int o)
{
    return o / 8;
}
```

4. **char**, **int**, **float**, **double**, and **void**.
5. The variable names are wrong because
   a. A dash may not be used in a variable name.
   b. A dollar sign may not be used in a variable name.
   c. A + sign may not be used in a variable name.
   d. A digit may not begin a variable name.

---

## Chapter 2

### REVIEW SKILLS CHECK

1. All programs must have a `main()` function. This is the first function called when your program begins executing.
2.
```c
#include <stdio.h>

int main(void)
{
    printf("This is the number %d", 100);

    return 0;
}
```
3. To include a header file, use the **#include** compiler directive. For example,
```c
#include <stdio.h>
```
includes the STDIO.H header.
4. The five basic data types are **char**, **int**, **float**, **double**, and **void**.
5. The invalid variable names are b, c, and e.
6. The `scanf()` function is used to input information from the keyboard.
7.
```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter a number: ");
    scanf("%d", &i);
    printf("%d", i*i);

    return 0;
}
```
8. Comments must be surrounded by the `/*` and `*/` comment symbols. For example, this is a valid C comment:
```c
/* This is a comment. */
```
9. A function returns a value to the calling routine using **return**.
10. `void Myfunc(int count, float balance, char ch);`

---

### 2.1 EXERCISES

1. b, d, and e are true.
2.
```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter a number: ");
    scanf("%d", &i);
    if((i%2)==0) printf("Even");
    if((i%2)==1) printf("Odd");

    return 0;
}
```

---

### 2.2 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int a, b, op;

    printf("Enter first number: ");
    scanf("%d", &a);

    printf("Enter second number: ");
    scanf("%d", &b);

    printf("Enter 0 to add, 1 to multiply: ");
    scanf("%d", &op);

    if(op==0) printf("%d", a+b);
    else printf("%d", a*b);

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter a number: ");
    scanf("%d", &i);
    if((i%2)==0) printf("Even");
    else printf("Odd");

    return 0;
}
```

---

### 2.3 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int a, b, op;

    printf("Enter 0 to add, 1 to subtract: ");
    scanf("%d", &op);

    if(op==0) { /* add */
        printf("Enter first number: ");
        scanf("%d", &a);
        printf("Enter second number: ");
        scanf("%d", &b);
        printf("%d", a+b);
    }
    else { /* subtract */
        printf("Enter first number: ");
        scanf("%d", &a);
        printf("Enter second number: ");
        scanf("%d", &b);
        printf("%d", a-b);
    }

    return 0;
}
```

2. No, the opening curly brace is missing.

---

### 2.4 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=1; i<101; i=i+1) printf("%d ", i);

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=17; i<101; i=i+1)
        if((i%17)==0) printf("%d ", i);

    return 0;
}
```

3.
```c
#include <stdio.h>

int main(void)
{
    int num, i;

    printf("Enter the number to test: ");
    scanf("%d", &num);

    for(i=2; i<(num/2)+1; i=i+1)
        if((num%i)==0) printf("%d ", i);

    return 0;
}
```

---

### 2.5 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=1; i<101; i++) printf("%d ", i);

    return 0;
}
```

```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=17; i<101; i++)
        if((i%17)==0) printf("%d ", i);

    return 0;
}
```

```c
#include <stdio.h>

int main(void)
{
    int num, i;

    printf("Enter the number to test: ");
    scanf("%d", &num);

    for(i=2; i<(num/2)+1; i++)
        if((num%i)==0) printf("%d ", i);

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int a, b;

    a = 1;
    a++;
    b = a;
    b--;
    printf("%d %d", a, b);

    return 0;
}
```

---

### 2.6 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=1; i<11; i++)
        printf("%d %d %d\n", i, i*i, i*i*i);

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int i, j;

    printf("Enter a number: ");
    scanf("%d", &i);

    for(j=i; j>0; j--) printf("%d\n", j);
    printf("\a");

    return 0;
}
```

---

### 2.7 EXERCISES

1. The loop prints the numbers 0 through 99.
2. Yes.
3. No, the first is true, the second is false.

---

### MASTERY SKILLS CHECK

1.
```c
#include <stdio.h>

int main(void)
{
    int magic; /* magic number */
    int guess; /* user's guess */
    int i;

    magic = 1325;
    guess = 0;

    for(i=0; i<10 && guess!=magic; i++) {
        printf("Enter your guess: ");
        scanf("%d", &guess);

        if(guess == magic) {
            printf("RIGHT!\n");
            printf("%d is the magic number.\n", magic);
        }
        else {
            printf("...Sorry, you're wrong...\n");
            if(guess > magic)
                printf(" Your guess is too high.\n");
            else printf(" Your guess is too low.\n");
        }
    }

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int rooms, len, width, total;
    int i;

    printf("Number of rooms? ");
    scanf("%d", &rooms);

    total = 0;
    for(i=rooms; i>0; i--) {
        printf("Enter length: ");
        scanf("%d", &len);

        printf("Enter width: ");
        scanf("%d", &width);

        total = total + len * width;
    }
    printf("Total square footage: %d", total);

    return 0;
}
```

3. The increment operator increases a variable by one and the decrement operator decreases a variable by one.
4.
```c
#include <stdio.h>

int main(void)
{
    int answer, count;
    int right, wrong;

    right = 0;
    wrong = 0;

    for(count=1; count < 11; count=count+1) {
        printf("What is %d + %d? ", count, count);
        scanf("%d", &answer);

        if(answer == count+count) {
            printf("Right! ");
            right++;
        }
        else {
            printf("Sorry, you're wrong. ");
            printf("The answer is %d. ", count+count);
            wrong++;
        }
    }
    printf("You got %d right and %d wrong.", right, wrong);

    return 0;
}
```

5.
```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=1; i<=100; i++) {
        printf("%d\t", i);
        if((i%5)==0) printf("\n");
    }

    return 0;
}
```

---

## Chapter 3

### REVIEW SKILLS CHECK

1. C's relational and logical operators are `<`, `>`, `<=`, `>=`, `!=`, `==`, `!`, `&&`, and `||`.
2. A block of code is a group of logically connected statements. To make a block, surround the statements with curly braces.
3. To output a newline, use the `\n` backslash character code.
4.
```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=-100; i<101; i++) printf("%d ", i);

    return 0;
}
```
5.
```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter proverb number: ");
    scanf("%d", &i);

    if(i==1) printf("A bird in the hand...");
    if(i==2) printf("A rolling stone...");
    if(i==3) printf("Once burned, twice shy.");
    if(i==4) printf("Early to bed, early to rise...");
    if(i==5) printf("A penny saved is a penny earned.");

    return 0;
}
```
6. `count++;` or `++count;`
7. In C, true is any nonzero value. False is zero.

---

### 3.1 EXERCISES

1.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    int i;
    char ch, smallest;

    printf("Enter 10 letters.\n");

    smallest = 'z'; /* make largest to begin with */

    for(i=0; i<10; i++) {
        ch = getche();
        if(ch < smallest) smallest = ch;
    }
    printf("\nThe smallest character is %c.", smallest);

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    char ch;

    for(ch='A'; ch<='Z'; ch++)
        printf("%d ", ch);

    printf("\n");

    for(ch='a'; ch<='z'; ch++)
        printf("%d ", ch);

    return 0;
}
```
The codes differ by 32.

---

### 3.2 EXERCISES

1. The `else` relates to the first `if`; it is not in the same block as the second.
2.
```c
#include <stdio.h>

int main(void)
{
    char ch;
    int s1, s2;
    float radius;

    printf("Compute area of Circle, Square, or Triangle? ");
    ch = getchar();
    printf("\n");

    if(ch=='C') {
        printf("Enter radius of circle: ");
        scanf("%f", &radius);
        printf("Area is: %f", 3.1416*radius*radius);
    }
    else if(ch=='S') {
        printf("Enter length of first side: ");
        scanf("%d", &s1);
        printf("Enter length of second side: ");
        scanf("%d", &s2);
        printf("Area is: %d", s1*s2);
    }
    else if(ch=='T') {
        printf("Enter length of base: ");
        scanf("%d", &s1);
        printf("Enter height: ");
        scanf("%d", &s2);
        printf("Area is: %d", (s1*s2)/2);
    }

    return 0;
}
```

---

### 3.3 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    float dist, speed;
    int num;

    printf("Enter number of drive time computations: ");
    scanf("%d", &num);

    for(; num; num--) {
        printf("\nEnter distance: ");
        scanf("%f", &dist);

        printf("Enter average speed: ");
        scanf("%f", &speed);

        printf("Drive time is %f\n", dist/speed);
    }

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter a number: ");
    scanf("%d", &i);

    for(; i; i--) ;

    printf("\a");

    return 0;
}
```

3.
```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=1; i<1001; i=i+i) printf("%d ", i);

    return 0;
}
```

---

### 3.4 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    float dist, speed;
    int num;

    printf("Enter number of drive time computations: ");
    scanf("%d", &num);

    while(num) {
        printf("\nEnter distance: ");
        scanf("%f", &dist);

        printf("Enter average speed: ");
        scanf("%f", &speed);

        printf("Drive time is %f\n", dist/speed);

        num--;
    }

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    printf("Enter your encoded message.\n");

    ch = getche();
    while(ch!='\r') {
        printf("%c", ch-1);
        ch = getche();
    }

    return 0;
}
```

---

### 3.5 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    float gallons;

    printf("\nEnter gallons: ");
    scanf("%f", &gallons);

    do {
        printf("Liters: %f\n", gallons*3.7854);

        printf("Enter gallons or 0 to quit: ");
        scanf("%f", &gallons);

    } while(gallons!=0);

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int choice;

    printf("Mailing list menu:\n\n");
    printf(" 1. Enter addresses\n");
    printf(" 2. Delete addresses\n");
    printf(" 3. Search the list\n");
    printf(" 4. Print the list\n");
    printf(" 5. Quit\n");

    do {
        printf("Enter the number of the choice (1-5): ");
        scanf("%d", &choice);
    } while(choice<1 || choice>5);

    return 0;
}
```

---

### 3.6 EXERCISES

1.
```c
/* This program finds the prime numbers from 2 to 1000. */
#include <stdio.h>

int main(void)
{
    int i, j, prime;

    for(i=2; i<1000; i++) {
        prime = 1;
        for(j=2; j <= i/2; j++)
            if(!(i%j)) prime=0;
        if(prime) printf("%d is prime.\n", i);
    }

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    int i;
    char ch;

    for(i=0; i<10; i++) {
        printf("\nEnter a letter: ");
        ch = getche();
        printf("\n");
        for(; ch; ch--) printf("%c", '.');
    }

    return 0;
}
```

---

### 3.7 EXERCISES

2.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    float i;
    char ch;

    printf("Tip Computer\n");

    for(i=1.0; i<101.0; i=i+1.0) {
        printf("%f %f %f\n", i, i*0.1, i*0.15, i*0.2);
        printf("More? (Y/N) ");
        ch = getche();
        printf("\n");
        if(ch=='N') break;
    }

    return 0;
}
```

---

### 3.8 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=1; i<101; i++) {
        if(!(i%2)) continue;
        printf("%d ", i);
    }

    return 0;
}
```

---

### 3.9 EXERCISES

1. Floating point values may not be used to control `switch`.
2.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;
    int digit, punc, letter;

    printf("Enter characters, ENTER to stop.\n");

    digit = 0;
    punc = 0;
    letter = 0;

    do {
        ch = getche();
        switch(ch) {
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
            case '0':
                digit++;
                break;
            case '.':
            case ',':
            case '?':
            case '!':
            case ':':
            case ';':
                punc++;
                break;
            default:
                letter++;
        }
    } while(ch!='\r');
    printf("\nDigits: %d\n", digit);
    printf("Punctuation: %d\n", punc);
    printf("Letters: %d\n", letter);

    return 0;
}
```

---

### 3.10 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i;

    i = 1;

jump_label:
    if(i>=11) goto done_label;
    printf("%d ", i);
    i++;
    goto jump_label;
done_label: printf("Done");

    return 0;
}
```

---

### MASTERY SKILLS CHECK

1.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    printf("Enter lowercase letters. ");
    printf("(Press ENTER to Quit.)\n");
    do {
        ch = getche();
        if(ch!='\r') printf("%c", ch-32);
    } while(ch!='\r');

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter a number: ");
    scanf("%d", &i);

    if(!i) printf("zero");
    else if(i<0) printf("negative");
    else printf("positive");

    return 0;
}
```

3. The `for` loop is valid. C allows any of its expressions to be empty.
4. `for( ; ; ) ...`
5.
```c
/* for */
for(i=1; i<11; i++) printf("%d ", i);

/* do */
i = 1;
do {
    printf("%d ", i);
    i++;
} while(i<11);

/* while */
i=1;
while(i<11) {
    printf("%d ", i);
    i++;
}
```
6. The `break` statement causes immediate termination of the loop.
7. Yes.
8. No, the label is missing the colon.

---

### CUMULATIVE SKILLS CHECK

1.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    printf("Enter characters (q to quit): \n");
    do {
        ch = getche();
        switch(ch) {
            case '\t': printf("tab\n");
                break;
            case '\b': printf("backspace\n");
                break;
            case '\r': printf("Enter\n");
        }
    } while(ch!='q');

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int i, j, k;

    for(k=0; k<10; k++) { /* use increment operator */
        printf("Enter first number: ");
        scanf("%d", &i);

        printf("Enter second number: ");
        scanf("%d", &j);

        if(j != 0) printf("%d\n", i/j); /* simplify condition */
        else printf("Cannot divide by zero.\n"); /* use else */
    }

    return 0;
}
```

---

## Chapter 4

### REVIEW SKILLS CHECK

1.
```c
int i;
for(i=1; i<11; i++) printf("%d ", i);

i = 1;
do {
    printf("%d ", i);
    i++;
} while(i<11);

i = 1;
while(i<11) {
    printf("%d ", i);
    i++;
}
```

2.
```c
switch(ch) {
    case 'L': load();
        break;
    case 'S': save();
        break;
    case 'E': enter();
        break;
    case 'D': display();
        break;
    case 'Q': quit();
        break;
}
```

3.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch;

    do {
        ch = getche();
    } while(ch!='\r');

    return 0;
}
```

4. The `break` statement causes immediate termination of the loop that contains it. It also terminates a statement sequence in a switch.
5. The `continue` statement causes the next iteration of a loop to occur.
6.
```c
#include <stdio.h>

int main(void)
{
    int i;
    float feet, meters, ounces, pounds;

    do {
        printf("Convert\n\n");
        printf("1. feet to meters\n");
        printf("2. meters to feet\n");
        printf("3. ounces to pounds\n");
        printf("4. pounds to ounces\n");
        printf("5. Quit\n\n");
        do {
            printf("Enter the number of your choice: ");
            scanf("%d", &i);
        } while(i<0 || i>5);

        switch(i) {
            case 1:
                printf("Enter feet: ");
                scanf("%f", &feet);
                printf("Meters: %f\n", feet / 3.28);
                break;
            case 2:
                printf("Enter meters: ");
                scanf("%f", &meters);
                printf("Feet: %f\n", meters * 3.28);
                break;
            case 3:
                printf("Enter ounces: ");
                scanf("%f", &ounces);
                printf("Pounds: %f\n", ounces / 16);
                break;
            case 4:
                printf("Enter pounds: ");
                scanf("%f", &pounds);
                printf("Ounces: %f\n", pounds * 16);
                break;
        }
    } while(i!=5);

    return 0;
}
```

---

### 4.1 EXERCISES

1. `unsigned short int loc_counter;`
2.
```c
#include <stdio.h>

int main(void)
{
    unsigned long int distance;

    printf("Enter distance: ");
    scanf("%lu", &distance);

    printf("%ld seconds", distance / 186000);

    return 0;
}
```
3. The statement can be recoded using C's shorthand as follows:
`short i;`

---

### 4.2 EXERCISES

1. Local variables are known only to the function in which they are declared. Global variables are known to and accessible by all functions. Further, local variables are created when the function is entered and destroyed when the function is exited. Thus they cannot maintain their values between function calls. However, global variables stay in existence during the entire lifetime of the program and maintain their values.
2. Here is the non-generalized version:
```c
#include <stdio.h>

void soundspeed(void);

double distance;

int main(void)
{
    printf("Enter distance in feet: ");
    scanf("%lf", &distance);
    soundspeed();

    return 0;
}

void soundspeed(void)
{
    printf("Travel time: %f", distance / 1129);
}
```
Here is the parameterized version:
```c
#include <stdio.h>

void soundspeed(double distance);

int main(void)
{
    double distance;

    printf("Enter distance in feet: ");
    scanf("%lf", &distance);
    soundspeed(distance);

    return 0;
}

void soundspeed(double distance)
{
    printf("Travel time: %f", distance / 1129);
}
```

---

### 4.3 EXERCISES

1. To cause a constant to be recognized by the compiler explicitly as a **float**, follow the value with an **F**.
2.
```c
#include <stdio.h>

int main(void)
{
    long int i;

    printf("Enter a number: ");
    scanf("%ld", &i);
    printf("%ld", i);

    return 0;
}
```
3.
```c
#include <stdio.h>

int main(void)
{
    printf("%s %s %s", "I", "like", "C");

    return 0;
}
```

---

### 4.4 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i=100;

    for(; i>0; i--) printf("%d ", i);

    return 0;
}
```
2. No. You cannot initialize a global variable using another variable.
3. Yes. A local variable can be initialized using any expression valid at the time of the initialization.

---

### 4.5 EXERCISES

1. The entire expression is **float**.
2. The subexpression is **unsigned long**.

---

### 4.6 EXERCISES

1. The program displays **10**.
2. The program displays **3.0**.

---

### 4.7 EXERCISE

1.
```c
#include <stdio.h>

int main(void)
{
    float f;

    for(f=1.0; (int) f<=9; f=f + 0.1)
        printf("%f ", f);

    return 0;
}
```
2. Here is the corrected statement:
```c
x = (int) 123.23 % 3; /* now fixed */
```

---

### MASTERY SKILLS CHECK

1. The data-type modifiers are **unsigned**, **long**, **short**, **signed**. They are used to modify the base type so that you can obtain variables that best fit the needs of your program.
2. To define an **unsigned** constant, follow the value with a **U**. To define a **long** constant, follow the value with an **L**. To specify a **long double**, follow the value with an **L**.
3. `float balance = 0.0;`
4. When the C compiler evaluates an expression, it automatically converts all **char**s and **short**s to **int**.
5. A signed integer uses the high-order bit as a sign flag. When the bit is set, the number is negative; when it is cleared, the number is positive. An unsigned integer uses all bits as part of the number and can represent only positive values.
6. Global variables maintain their values throughout the lifetime of the program. They are also accessible by all functions in the program.
7.
```c
#include <stdio.h>

int series(void);

int num = 21;

int main(void)
{
    int i;

    for(i=0; i<10; i++)
        printf("%d ", series());

    return 0;
}

int series(void)
{
    num = (num*1468) % 467;
    return num;
}
```
8. A type cast temporarily changes the type of a variable. For example, here the **int** `i` is temporarily changed into a **double**:
```c
(double) i
```

---

### CUMULATIVE SKILLS CHECK

1. The fragment is not valid because to C, both 'A' and 65 are the same thing, and no two case constants can be the same.
2. The reason that the return value of `getchar()` or `getche()` can be assigned to a **char** is because C automatically removes the high-order byte.
3. No. Because `i` is a signed integer, its maximum value is 32,767. Therefore, it will never exceed 33,000.

---

## Chapter 5

### REVIEW SKILLS CHECK

1. A local variable is known only to the function in which it is declared. Further, it is created when the function is entered and destroyed when the function returns. A global variable is known throughout the entire program and remains in existence the entire time the program is executing.
2. C compiler will assign the following types:
   a. **int**
   b. **int**
   c. **double**
   d. **long**
   e. **long**
3.
```c
#include <stdio.h>

int main(void)
{
    long l;
    short s;
    double d;

    printf("Enter a long value: ");
    scanf("%ld", &l);

    printf("Enter a short value: ");
    scanf("%hd", &s);

    printf("Enter a double value: ");
    scanf("%lf", &d);

    printf("%ld\n", l);
    printf("%hd\n", s);
    printf("%f\n", d);

    return 0;
}
```
4. A type cast temporarily changes the type of a value.
5. The `else` is associated with the `if(j)` statement, contrary to what the (incorrect) indentation would have you believe.
6. When `i` is 1, `a` is 2. When `i` is 4, `a` is 5.

---

### 5.1 EXERCISES

1. The array `count` is being overrun. It is only 10 elements long, but the program requires one that is 100 elements long.
2.
```c
#include <stdio.h>

int main(void)
{
    int i[10], j, k, match;

    printf("Enter 10 numbers:\n");
    for(j=0; j<10; j++) scanf("%d", &i[j]);

    /* see if any match */
    for(j=0; j<10; j++) {
        match = i[j];
        for(k=j+1; k<10; k++)
            if(match==i[k])
                printf("%d is duplicated\n", match);
    }

    return 0;
}
```

3.
```c
#include <stdio.h>

int main(void)
{
    float item[100], t;
    int a, b;
    int count;

    /* read in numbers */
    printf("How many numbers? ");
    scanf("%d", &count);
    for(a=0; a<count; a++) scanf("%f", &item[a]);

    /* now sort them using a bubble sort */
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
    for(a=0; a<count; a++) printf("%f ", item[a]);

    return 0;
}
```

---

### 5.2 EXERCISES

1.
```c
/* Reverse a string. */
#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[80];
    int i;

    printf("Enter a string: ");
    gets(str);

    for(i=strlen(str)-1; i>=0; i--)
        printf("%c", str[i]);

    return 0;
}
```
2. The string `str` is not long enough to hold the string "this is a test".
3.
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char bigstr[1000] = "", str[80];

    for( ; ; ) {
        printf("Enter a string: ");
        gets(str);
        if(!strcmp(str, "quit")) break;
        strcat(str, "\n");
        /* prevent an array overrun */
        if(strlen(bigstr)+strlen(str) >= 1000) break;
        strcat(bigstr, str);
    }

    printf(bigstr);

    return 0;
}
```

---

### 5.3 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int three_d[3][3][3];
    int i, j, k, x;

    x = 1;
    for(i=0; i<3; i++)
        for(j=0; j<3; j++)
            for(k=0; k<3; k++) {
                three_d[i][j][k] = x;
                x++;
                printf("%d ", three_d[i][j][k]);
            }

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    int three_d[3][3][3];
    int i, j, k, sum;

    for(i=0; i<3; i++)
        for(j=0; j<3; j++)
            for(k=0; k<3; k++) {
                three_d[i][j][k] = (i+1) * (j+1) * (k+1);
                printf("%d ", three_d[i][j][k]);
            }

    /* sum all elements */
    sum = 0;
    for(i=0; i<3; i++)
        for(j=0; j<3; j++)
            for(k=0; k<3; k++)
                sum = sum + three_d[i][j][k];

    printf("\n%d", sum);

    return 0;
}
```

---

### 5.4 EXERCISES

1. No. The list must be enclosed between curly braces.
2. No. The array `name` is only 4 characters long. The attempted call to `strcpy()` will cause the array to be overrun.
3.
```c
#include <stdio.h>

int main(void)
{
    int cube[][3] = {
        1, 1, 1,
        2, 4, 8,
        3, 9, 27,
        4, 16, 64,
        5, 25, 125,
        6, 36, 216,
        7, 49, 343,
        8, 64, 512,
        9, 81, 729,
        10, 100, 1000
    };
    int num, i;

    printf("Enter cube: ");
    scanf("%d", &num);

    for(i=0; i<10; i++)
        if(cube[i][2]==num) {
            printf("Root: %d\n", cube[i][0]);
            printf("Square: %d", cube[i][1]);
            break;
        }

    if(i==10) printf("Cube not found.\n");

    return 0;
}
```

---

### 5.5 EXERCISES

1.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char digits[10][10] = {
        "zero", "one", "two", "three",
        "four", "five", "six", "seven",
        "eight", "nine"
    };
    char num;

    printf("Enter number: ");
    num = getche();
    printf("\n");

    num = num - '0';
    if(num>=0 && num<10) printf("%s", digits[num]);

    return 0;
}
```

---

### MASTERY SKILLS CHECK

1. An array is a list of like-type variables.
2. The statement will not generate an error message because C provides no bounds checking on array operations, but it is wrong because it causes `count` to be overrun.
3.
```c
#include <stdio.h>

int main(void)
{
    int stats[20], i, j;
    int mode, count, oldcount, oldmode;

    printf("Enter 20 numbers: \n");
    for(i=0; i<20; i++) scanf("%d", &stats[i]);

    oldcount = 0;
    /* find the mode */
    for(i=0; i<20; i++) {
        mode = stats[i];
        count = 1;

        /* count the occurrences of this value */
        for(j=i+1; j<20; j++)
            if(mode==stats[j]) count++;

        /* if count is greater than old count, use new mode */
        if(count>oldcount) {
            oldmode = mode;
            oldcount = count;
        }
    }
    printf("The mode is %d\n", oldmode);

    return 0;
}
```

4. `int items[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};`
5.
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[80];

    do {
        printf("Enter a string: ");
        gets(str);
    } while(strcmp("quit", str));

    return 0;
}
```

6.
```c
/* Computerized dictionary program. */
#include <stdio.h>
#include <string.h>

int main(void)
{
    char dict[][2][40] = {
        "house", "a place of dwelling",
        "car", "a vehicle",
        "computer", "a thinking machine",
        "program", "a sequence of instructions",
        "", ""
    };
    char word[80];
    int i;

    printf("Enter word: ");
    gets(word);

    /* look up the word */
    i = 0;
    /* search while null string not yet encountered */
    while(strcmp(dict[i][0], "")) {
        if(!strcmp(word, dict[i][0])) {
            printf("meaning: %s", dict[i][1]);
            break;
        }
        i++;
    }
    if(!strcmp(dict[i][0], ""))
        printf("Not in dictionary\n");

    return 0;
}
```

---

### CUMULATIVE SKILLS CHECK

1.
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[80];
    int i;

    printf("Enter a string: ");
    gets(str);

    /* pad the string if necessary */
    for(i=strlen(str); i<79; i++)
        strcat(str, ".");

    printf(str);

    return 0;
}
```

2.
```c
/* A simple coding program. */
#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[80];
    int i, j;

    printf("Enter message: ");
    gets(str);

    /* code it */
    i=0; j = strlen(str) - 1;
    while(i<=j) {
        if(i<j) printf("%c%c", str[i], str[j]);
        else printf("%c", str[i]);
        i++; j--;
    }

    return 0;
}
```

3.
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char str[80];
    int spaces, periods, commas;
    int i;

    printf("Enter a string: ");
    gets(str);

    spaces = 0;
    commas = 0;
    periods = 0;

    for(i=0; i<strlen(str); i++)
        switch(str[i]) {
            case '.': periods++;
                break;
            case ',': commas++;
                break;
            case ' ': spaces++;
        }

    printf("spaces: %d\n", spaces);
    printf("commas: %d\n", commas);
    printf("periods: %d", periods);

    return 0;
}
```

4. The `getchar()` function returns a character, not a string. Hence, it cannot be used as shown. You must use `gets()` to read a string from the keyboard.
5.
```c
/* A simple game of Hangman */
#include <stdio.h>
#include <string.h>

int main(void)
{
    char word[] = "concatenation";
    char temp[] = "-------------";
    char ch;
    int i, count;

    count = 0; /* count number of guesses */

    do {
        printf("%s\n", temp);
        printf("Enter your guess: ");
        ch = getchar();
        printf("\n");

        /* see if letter matches any in word */
        for(i=0; i<strlen(word); i++)
            if(ch==word[i]) temp[i] = ch;
        count++;
    } while(strcmp(temp, word));

    printf("%s\n", temp);
    printf("You guessed the word and used %d guesses", count);

    return 0;
}
```

---

## Chapter 6

### REVIEW SKILLS CHECK

1.
```c
#include <stdio.h>

int main(void)
{
    int num[10], i, even, odd;

    printf("Enter 10 integers: ");

    for(i=0; i<10; i++) scanf("%d", &num[i]);

    even = 0; odd = 0;
    for(i=0; i<10; i++) {
        if(num[i]%2) odd = odd + num[i];
        else even = even + num[i];
    }

    printf("Sum of even numbers: %d\n", even);
    printf("Sum of odd numbers: %d", odd);

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char pw[80];
    int i;

    for(i=0; i<3; i++) {
        printf("Password: ");
        gets(pw);
        if(!strcmp("Tristan", pw)) break;
    }

    if(i==3) printf("Access Denied");
    else printf("Log-on Successful");

    return 0;
}
```

3. The array, `name`, is not big enough to hold the string being assigned to it.
4. A null string is a string that contains only the null character.
5. The `strcpy()` function copies the contents of one string into another. The `strcmp()` function compares two strings and returns less than zero if the first string is less than the second, zero if the strings match, or greater than zero if the first string is greater than the second.
6.
```c
/* A Simple computerized telephone book. */
#include <stdio.h>
#include <string.h>

char phone[][2][40] = {
    "Fred", "555-1010",
    "Barney", "555-1234",
    "Ralph", "555-2347",
    "Tom", "555-8396",
    "", ""
};

int main(void)
{
    char name[80];
    int i;

    printf("Name? ");
    gets(name);

    for(i=0; phone[i][0][0]; i++)
        if(!strcmp(name, phone[i][0]))
            printf("number: %s", phone[i][1]);

    return 0;
}
```

---

### 6.1 EXERCISES

1. A pointer is a variable that contains the address of another variable.
2. The pointer operators are the `*` and the `&`. The `*` operator returns the value of the object pointed to by the pointer it precedes. The `&` operator returns the address of the variable it precedes.
3. The base type of a pointer is important because all pointer arithmetic is done relative to it.
4.
```c
#include <stdio.h>

int main(void)
{
    int i, *p;

    p = &i;

    for(i=0; i<10; i++) printf("%d ", *p);

    return 0;
}
```

---

### 6.2 EXERCISES

1. You cannot multiply a pointer.
2. No, you can only add or subtract integer values.
3. 108

---

### 6.3 EXERCISES

1. No, you cannot change the value of a pointer that is generated by using an array name without an index.
2. 8
3.
```c
#include <stdio.h>

int main(void)
{
    char str[80], *p;

    printf("Enter a string: ");
    gets(str);

    p = str;

    /* While not at the end of the string and no
       space has been encountered, increment p to
       point to next character.
    */
    while(*p && *p!=' ') p++;

    printf(p);

    return 0;
}
```

---

### 6.4 EXERCISE

1.
```c
#include <stdio.h>

int main(void)
{
    char *one = "one";
    char *two = "two";
    char *three = "three";

    printf("%s %s %s\n", one, two, three);
    printf("%s %s %s\n", one, three, two);
    printf("%s %s %s\n", two, one, three);
    printf("%s %s %s\n", two, three, one);
    printf("%s %s %s\n", three, one, two);
    printf("%s %s %s\n", three, two, one);

    return 0;
}
```

---

### 6.5 EXERCISE

1.
```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    char *p[3] = {
        "yes", "no",
        "maybe - rephrase the question"
    };
    char str[80];

    printf("Enter your question: \n");
    gets(str);

    printf(p[strlen(str) % 3]);

    return 0;
}
```

---

### 6.6 EXERCISE

1.
```c
#include <stdio.h>

int main(void)
{
    int i, *p, **mp;

    p = &i;
    mp = &p;

    **mp = 10;

    printf("%p %p %p", &i, p, mp);

    return 0;
}
```

---

### 6.7 EXERCISES

1.
```c
#include <stdio.h>
#include <string.h>

void mystrcat(char *to, char *from);

int main(void)
{
    char str[80];

    strcpy(str, "first part");
    mystrcat(str, " second part");
    printf(str);

    return 0;
}

void mystrcat(char *to, char *from)
{
    /* find the end of to */
    while(*to) to++;

    /* concatenate the string */
    while(*from) *to++ = *from++;

    /* add the null terminator */
    *to = '\0';
}
```

2.
```c
#include <stdio.h>

void f(int *p);

int main(void)
{
    int i;

    f(&i);

    printf("%d", i);

    return 0;
}

void f(int *p)
{
    *p = -1;
}
```

---

### MASTERY SKILLS CHECK

1. `double *p;`
2.
```c
#include <stdio.h>

int main(void)
{
    int i, *p;

    p = &i;

    *p = 100;

    printf("%d", i);

    return 0;
}
```
3. No. The pointer `p` has never been initialized to point to a valid piece of memory that can hold a string.
4. Pointers and arrays are basically two ways of looking at the same thing. They are virtually interchangeable.
5. `str[2]`, `*(str+2)`, `*(p+2)`
6. 108

---

### CUMULATIVE SKILLS CHECK

1. Pointers are often more convenient than array indexing and may be faster in some cases.
2.
```c
#include <stdio.h>

int main(void)
{
    char str[80], *p;
    int i, spaces;

    printf("Enter a string: ");
    gets(str);

    spaces = 0;
    p = str;
    while(*p) {
        if(*p==' ') spaces++;
        p++;
    }

    printf("Number of spaces: %d", spaces);

    return 0;
}
```
3. `*((int *)count + (44 * 10) + 8) = 99;`

---

## Chapter 7

### REVIEW SKILLS CHECK

1. The fragment assigns to `i` the value 19 indirectly using a pointer.
2. An array name with no index generates a pointer to the start of the array.
3. Yes, the fragment is correct. It works because the compiler creates a string table entry for the string "this is a string" and assigns `p` a pointer to the start of it.
4.
```c
#include <stdio.h>

int main(void)
{
    double d, *p;

    p = &d;

    *p = 100.99;

    printf("%f", d);

    return 0;
}
```
5.
```c
#include <stdio.h>

int mystrlen(char *p);

int main(void)
{
    char str[80];

    printf("Enter a string: ");
    gets(str);

    printf("Length is %d", mystrlen(str));

    return 0;
}

int mystrlen(char *p)
{
    int i;

    i = 0;
    while(*p) {
        i++;
        p++;
    }
    return i;
}
```
6. The fragment is correct. It displays **C**.

---

### 7.1 EXERCISES

1.
```c
#include <stdio.h>

double avg();

int main(void)
{
    printf("%f", avg());

    return 0;
}

double avg()
{
    int i;
    double sum, num;

    sum = 0.0;
    for(i=0; i<10; i++) {
        printf("Enter next number: ");
        scanf("%lf", &num);
        sum = sum + num;
    }
    return sum / 10.0;
}
```

2.
```c
#include <stdio.h>

double avg(void);

int main(void)
{
    printf("%f", avg());

    return 0;
}

double avg(void)
{
    int i;
    double sum, num;

    sum = 0.0;
    for(i=0; i<10; i++) {
        printf("Enter next number: ");
        scanf("%lf", &num);
        sum = sum + num;
    }
    return sum / 10.0;
}
```

3. The program is correct. However, the program would be better if a full function prototype were used when declaring `myfunc()`.
4. `double *Purge(void);`

---

### 7.2 EXERCISES

1.
```c
#include <stdio.h>

int fact(int i);

int main(void)
{
    printf("5 factorial is %d", fact(5));

    return 0;
}

int fact(int i)
{
    if(i==1) return 1;
    else return i * fact(i-1);
}
```

2. The function will call itself repeatedly, until it crashes the program, because there is no condition that prevents a recursive call from occurring.
3.
```c
#include <stdio.h>

void display(char *p);

int main(void)
{
    display("this is a test");

    return 0;
}

void display(char *p)
{
    if(*p) {
        printf("%c", *p);
        display(p+1);
    }
}
```

---

### 7.3 EXERCISES

1. No. The function `myfunc()` is being called with a pointer to the first parameter instead of the parameter itself.
2.
```c
#include <stdio.h>

void prompt(char *msg, char *str);

int main(void)
{
    char str[80];

    prompt("Enter a string: ", str);
    printf("Your string is: %s", str);

    return 0;
}

void prompt(char *msg, char *p)
{
    printf(msg);
    gets(p);
}
```
3. In call by value, the value of an argument is passed to a function. In call by reference, the address of an argument is passed to a function.

---

### 7.4 EXERCISES

1.
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int i;

    if(argc!=3) {
        printf("You must specify two arguments.");
        exit(1);
    }

    i = strcmp(argv[1], argv[2]);
    if(i < 0) printf("%s > %s", argv[2], argv[1]);
    else if(i > 0) printf("%s > %s", argv[1], argv[2]);
    else printf("They are the same");

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if(argc!=3) {
        printf("You must specify two numbers.");
        exit(1);
    }

    printf("%f", atof(argv[1]) + atof(argv[2]));

    return 0;
}
```

3.
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if(argc!=4) {
        printf("You must specify the operation ");
        printf("followed by two numbers.");
        exit(1);
    }

    if(!strcmp("add", argv[1]))
        printf("%f", atof(argv[2]) + atof(argv[3]));
    else if(!strcmp("subtract", argv[1]))
        printf("%f", atof(argv[2]) - atof(argv[3]));
    else if(!strcmp("multiply", argv[1]))
        printf("%f", atof(argv[2]) * atof(argv[3]));
    else if(!strcmp("divide", argv[1]))
        printf("%f", atof(argv[2]) / atof(argv[3]));

    return 0;
}
```

---

### 7.5 EXERCISE

1.
```c
#include <stdio.h>

double f_to_m(double f);

int main(void)
{
    double feet;

    printf("Enter feet: ");
    scanf("%lf", &feet);
    printf("Meters: %f", f_to_m(feet));

    return 0;
}

/* use old-style declaration. */
double f_to_m(f)
double f;
{
    return f / 3.28;
}
```

---

### MASTERY SKILLS CHECK

1. A function that does not have parameters specifies **void** in the parameter list of its prototype.
2. A function prototype tells the compiler these three things: the return type of the function, the type of its parameters, and the number of its parameters. It is useful because it allows the compiler to find errors if the function is called incorrectly.
3. Command-line arguments are passed to a C program through the `argc` and `argv` parameters to `main()`.
4.
```c
#include <stdio.h>

void alpha(char ch);

int main(void)
{
    alpha('A');

    return 0;
}

void alpha(char ch)
{
    printf("%c", ch);
    if(ch < 'Z') alpha(ch+1);
}
```

5.
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char *p;

    if(argc!=2) {
        printf("You need to specify a string");
        exit(1);
    }

    p = argv[1];

    while(*p) {
        printf("%c", (*p)+1);
        p++;
    }

    return 0;
}
```

6. The prototype is shown here:
`double myfunc(int x, int y, char ch);`
7. Using the old-style function declaration, the function from Exercise 6 looks like this:
```c
double myfunc(x, y, ch)
int x, y;
char ch;
{
    .
    .
    .
}
```
8. The `exit()` function causes immediate program termination. It also returns a value to the operating system.
9. The `atoi()` function converts its string argument into its equivalent integer form. The string must represent (in string form) a valid integer.

---

### CUMULATIVE SKILLS CHECK

1.
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if(argc!=2) {
        printf("Specify a password");
        exit(1);
    }

    if(!strcmp(argv[1], "password"))
        printf("Access Permitted");
    else printf("Access Denied");

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <ctype.h>

void string_up(char *p);

int main(void)
{
    char str[] = "this is a test";

    string_up(str);
    printf(str);

    return 0;
}

void string_up(char *p)
{
    while(*p) {
        *p = toupper(*p);
        p++;
    }
}
```

3.
```c
#include <stdio.h>

void avg(double *d, int num);

int main(void)
{
    double nums[] = {1.0, 2.0, 3.0, 4.0, 5.0,
                     6.0, 7.0, 8.0, 9.0, 10.0};

    avg(nums, 10);

    return 0;
}

void avg(double *d, int num)
{
    double sum;
    int temp;

    temp = num-1;

    for(sum=0; temp>=0; temp--)
        sum = sum + d[temp];

    printf("Average is %f", sum / (double) num);
}
```
4. A pointer contains the address of another variable. When a pointer is passed to a function, the function may alter the contents of the object pointed to by the pointer. This is the equivalent of call by reference.

---

## Chapter 8

### REVIEW SKILLS CHECK

1. To allow the compiler to verify that a function is being called correctly, you must include its prototype.
2. Function prototypes enable the compiler to provide stronger type checking between the arguments used to call a function and the parameters of the function. Also, it lets the compiler confirm that the function is called with the proper number of arguments.
3.
```c
#include <stdio.h>
#include <math.h>

double hypot(double s1, double s2);

int main(void)
{
    printf("%f", hypot(12.2, 19.2));

    return 0;
}

double hypot(double s1, double s2)
{
    double h;

    h = s1*s1 + s2*s2;
    return sqrt(h);
}
```
4. When a function does not return a value, its return type should be specified as **void**.
5.
```c
#include <stdio.h>

int rstrlen(char *p);

int main(void)
{
    printf("%d", rstrlen("hello there"));

    return 0;
}

int rstrlen(char *p)
{
    if(*p) {
        p++;
        return 1+rstrlen(p);
    }
    else return 0;
}
```
6.
```c
#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("There were %d arguments.\n", argc);
    printf("The last one is %s.", argv[argc-1]);

    return 0;
}
```
7.
```c
func(a, ch, d)
int a;
char ch;
double d;
{
```

---

### 8.1 EXERCISES

1.
```c
#include <stdio.h>

#define MAX 100
#define COUNTBY 3

int main(void)
{
    int i;

    for(i=0; i<MAX; i++)
        if(!(i%COUNTBY)) printf("%d ", i);

    return 0;
}
```
2. No, the fragment is wrong because a macro cannot be defined in terms of another before the second macro is defined. Stated differently, `MIN` is not defined when `MAX` is being defined.
3. As the macro is used, the fragment is wrong. The string needs to be within double quotes.
4. Yes.

---

### 8.2 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i;

    do {
        i = getchar();
        if(i==EOF) {
            printf("Error on input.");
            break;
        }
        if(putchar('.')==EOF) {
            printf("Error on output.");
            break;
        }
    } while((char) i != '\n');

    return 0;
}
```
2. The `putchar()` function outputs a character. It cannot output a string.

---

### 8.3 EXERCISES

1.
```c
#include <conio.h>
#include <stdio.h>

int main(void)
{
    char ch;

    ch = getch();
    printf("%d", ch);

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    do {
        printf("%c", '.');
    } while(!kbhit());

    return 0;
}
```

---

### 8.4 EXERCISES

2. No. The program is incorrect because `gets()` must be called with a pointer to an actual array.

---

### 8.5 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    unsigned long i;

    for(i=2; i<=100; i++)
        printf("%-10lu %-10lu %-10lu\n", i, i*i, i*i*i);

    return 0;
}
```
2. `printf("Clearance price: 40%% off as marked");`
3. `printf("%.2f", 1023.03);`

---

### 8.6 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    char first[21], middle[21], last[21];

    printf("Enter your entire name: ");
    scanf("%20s%20s%20s", first, middle, last);
    printf("%s %s %s", first, middle, last);

    return 0;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    char num[80];

    printf("Enter a floating point number: ");
    scanf("%[0-9.]", num);
    printf(num);

    return 0;
}
```
3. No, a character can only have a maximum field length of 1.
4.
```c
#include <stdio.h>

int main(void)
{
    char str[80];
    double d;
    int i, num;

    printf("Enter a string, a double, and an integer: ");
    scanf("%s%lf%d%n", str, &d, &i, &num);
    printf("Number of characters read: %d", num);

    return 0;
}
```

5.
```c
#include <stdio.h>

int main(void)
{
    unsigned u;

    printf("Enter hexadecimal number: ");
    scanf("%x", &u);
    printf("Decimal equivalent: %u", u);

    return 0;
}
```

---

### MASTERY SKILLS CHECK

1. All these functions input a character from the keyboard. The `getchar()` function is often implemented using line-buffered I/O which makes its use in interactive environments undesirable. The `getche()` is an interactive equivalent to `getchar()`. The `getch()` function is the same as `getche()` except that it does not echo the character typed.
2. The `%e` specifier outputs a number in scientific notation using a lowercase 'e'. The `%E` specifier outputs a number in scientific notation using an 'E'.
3. A scanset is a set of characters that `scanf()` matches with input. As long as the characters being read are part of the scanset, `scanf()` continues to input them into the array pointed to by the scanset's corresponding argument.
4.
```c
#include <stdio.h>

int main(void)
{
    char name[80], date[80], phone[80];

    printf("Enter first name, birthdate ");
    printf("and phone number:\n");
    scanf("%s%8s%8s", name, date, phone);
    printf("%s %s %s", name, date, phone);

    return 0;
}
```
5. The `puts()` function is much smaller and faster than `printf()`. But, it can only output strings.
6.
```c
#include <stdio.h>

#define COUNT 100

int main(void)
{
    int i;

    for(i=0; i<COUNT; i++)
        printf("%d ", i);

    return 0;
}
```
7. `EOF` is a macro that stands for end-of-file. It is defined in STDIO.H.

---

### CUMULATIVE SKILLS CHECK

1.
```c
#include <stdio.h>

int main(void)
{
    char name[9][80];
    double b_avg[9];
    int i, h, l;
    double high, low, team_avg;

    for(i=0; i<9; i++) {
        printf("Enter name %d: ", i+1);
        scanf("%s", name[i]);
        printf("Enter batting average: ");
        scanf("%lf", &b_avg[i]);
        printf("\n");
    }

    high = 0.0;
    low = 1000.0;
    team_avg = 0.0;
    for(i=0; i<9; i++) {
        if(b_avg[i]>high) {
            h = i;
            high = b_avg[i];
        }
        if(b_avg[i]<low) {
            l = i;
            low = b_avg[i];
        }
        team_avg = team_avg+b_avg[i];
    }
    printf("The high is %s %f\n", name[h], b_avg[h]);
    printf("The low is %s %f\n", name[l], b_avg[l]);
    printf("The team average is %f", team_avg/9.0);

    return 0;
}
```

2. Note: There are many ways you could have written this program. This one is simply representative.
```c
/* An electronic card catalog. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

int menu(void);
void display(int i);
void author_search(void);
void title_search(void);
void enter(void);

char names[MAX][80];   /* author names */
char titles[MAX][80];  /* titles */
char pubs[MAX][80];    /* publisher */

int top = 0; /* last location used */

int main(void)
{
    int choice;

    do {
        choice = menu();
        switch(choice) {
            case 1: enter(); /* enter books */
                break;
            case 2: author_search(); /* search by author */
                break;
            case 3: title_search(); /* search by title */
                break;
        }
    } while(choice!=4);

    return 0;
}

/* Return a menu selection. */
int menu(void)
{
    char str[80];
    int i;

    printf("Card Catalog:\n");
    printf(" 1. Enter\n");
    printf(" 2. Search by Author\n");
    printf(" 3. Search by Title\n");
    printf(" 4. Quit\n");

    do {
        printf("Choose your selection: ");
        gets(str);
        i = atoi(str);
        printf("\n");
    } while(i<1 || i>4);

    return i;
}

/* Enter books into database. */
void enter(void)
{
    int i;

    for(i=top; i<MAX; i++) {
        printf("Enter author name (ENTER to quit): ");
        gets(names[i]);
        if(!*names[i]) break;
        printf("Enter title: ");
        gets(titles[i]);
        printf("Enter publisher: ");
        gets(pubs[i]);
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
        if(!strcmp(name, names[i])) {
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
        if(!strcmp(title, titles[i])) {
            display(i);
            found = 1;
            printf("\n");
        }

    if(!found) printf("Not Found\n");
}

/* Display catalog entry. */
void display(int i)
{
    printf("%s\n", titles[i]);
    printf("by %s\n", names[i]);
    printf("Published by %s\n", pubs[i]);
}
```

---

## Chapter 9

### REVIEW SKILLS CHECK

1. The `getchar()` function is defined by the ANSI standard and is used to input characters from the keyboard. However, in most implementations, it uses line-buffered I/O, which makes it impractical for interactive use. The `getche()` function is not defined by the ANSI standard, but it is quite common and is essentially an interactive version of `getchar()`.
2. When `scanf()` is reading a string, it stops when it encounters the first whitespace character.
3.
```c
#include <stdio.h>

int isprime(int i);

int main(void)
{
    int i, count;

    count = 0;
    for(i=2; i<1001; i++)
        if(isprime(i)) {
            printf("%10d", i);
            count++;
            if(count==4) {
                printf("\n");
                count = 0;
            }
        }

    return 0;
}

int isprime(int i)
{
    int j;

    for(j=2; j<=(i/2); j++)
        if(!(i%j)) return 0;
    return 1;
}
```

4.
```c
#include <stdio.h>

int main(void)
{
    double d;
    char ch;
    char str[80];

    printf("Enter a double, a character, and a string\n");
    scanf("%lf%c%20s", &d, &ch, str);
    printf("%f %c %s", d, ch, str);

    return 0;
}
```

5.
```c
#include <stdio.h>

int main(void)
{
    char str[80];

    printf("Enter leading digits followed by a string\n");
    scanf("%*[0-9]%s", str);
    printf("%s", str);

    return 0;
}
```

---

### 9.2 EXERCISES

1.
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    char ch;

    /* see if filename is specified */
    if(argc!=2) {
        printf("File name missing.\n");
        exit(1);
    }

    if((fp = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    while((ch=fgetc(fp)) != EOF) putchar(ch);

    fclose(fp);

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int count[26];

int main(int argc, char *argv[])
{
    FILE *fp;
    char ch;
    int i;

    /* see if file name is specified */
    if(argc!=2) {
        printf("File name missing.\n");
        exit(1);
    }

    if((fp = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    while((ch=fgetc(fp))!=EOF) {
        ch = toupper(ch);
        if(ch>='A' && ch<='Z') count[ch-'A']++;
    }

    for(i=0; i<26; i++)
        printf("%c occurred %d times\n", i+'A', count[i]);

    fclose(fp);

    return 0;
}
```

3.
```c
/* Copy a file. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *from, *to;
    char ch, watch;

    /* see if correct number of command line arguments */
    if(argc<3) {
        printf("Usage: copy <source> <destination>\n");
        exit(1);
    }

    /* open source file */
    if((from = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open source file.\n");
        exit(1);
    }

    /* open destination file */
    if((to = fopen(argv[2], "w"))==NULL) {
        printf("Cannot open destination file.\n");
        exit(1);
    }

    if(argc==4 && !strcmp(argv[3], "watch")) watch = 1;
    else watch = 0;

    /* copy the file */
    while((ch=fgetc(from)) !=EOF) {
        fputc(ch, to);
        if(watch) putchar(ch);
    }
    fclose(from);
    fclose(to);

    return 0;
}
```

---

### 9.3 EXERCISES

1.
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    unsigned count;

    /* see if file name is specified */
    if(argc!=2) {
        printf("File name missing.\n");
        exit(1);
    }

    if((fp = fopen(argv[1], "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    count = 0;
    while(!feof(fp)) {
        fgetc(fp);
        if(ferror(fp)) {
            printf("File error.\n");
            exit(1);
        }
        count++;
    }

    printf("File has %u bytes", count-1);
    fclose(fp);

    return 0;
}
```

2.
```c
/* Exchange two files. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *f1, *f2, *temp;
    char ch;

    /* see if correct number of command line arguments */
    if(argc!=3) {
        printf("Usage: exchange <f1> <f2>\n");
        exit(1);
    }

    /* open first file */
    if((f1 = fopen(argv[1], "rb"))==NULL) {
        printf("Cannot open first file.\n");
        exit(1);
    }

    /* open second file */
    if((f2 = fopen(argv[2], "rb"))==NULL) {
        printf("Cannot open second file.\n");
        exit(1);
    }

    /* open temporary file */
    if((temp = fopen("temp.tmp", "wb"))==NULL) {
        printf("Cannot open temporary file.\n");
        exit(1);
    }

    /* copy f1 to temp */
    while(!feof(f1)) {
        ch = fgetc(f1);
        if(!feof(f1)) fputc(ch, temp);
    }

    fclose(f1);

    /* open first file for output */
    if((f1 = fopen(argv[1], "wb"))==NULL) {
        printf("Cannot open first file.\n");
        exit(1);
    }

    /* copy f2 to f1 */
    while(!feof(f2)) {
        ch = fgetc(f2);
        if(!feof(f2)) fputc(ch, f1);
    }
    fclose(f2);
    fclose(temp);

    /* open second file for output */
    if((f2 = fopen(argv[2], "wb"))==NULL) {
        printf("Cannot open second file.\n");
        exit(1);
    }

    /* open temp file for input */
    if((temp = fopen("temp.tmp", "rb"))==NULL) {
        printf("Cannot open temporary file.\n");
        exit(1);
    }

    /* copy temp to f2 */
    while(!feof(temp)) {
        ch = fgetc(temp);
        if(!feof(temp)) fputc(ch, f2);
    }

    fclose(f1);
    fclose(f2);
    fclose(temp);

    return 0;
}
```

---

### 9.4 EXERCISES

1.
```c
/* A simple computerized telephone book. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char names[100][40];
char numbers[100][40];

int loc=0;

int menu(void);
void enter(void);
void load(void);
void save(void);
void find(void);

int main(void)
{
    int choice;

    do {
        choice = menu();
        switch(choice) {
            case 1: enter();
                break;
            case 2: find();
                break;
            case 3: save();
                break;
            case 4: load();
                break;
        }
    } while(choice!=5);

    return 0;
}

/* Get menu choice. */
int menu(void)
{
    int i;
    char str[80];

    printf("1. Enter names and numbers\n");
    printf("2. Find numbers\n");
    printf("3. Save directory to disk\n");
    printf("4. Load directory from disk\n");
    printf("5. Quit\n");

    do {
        printf("Enter your choice: ");
        gets(str);
        i = atoi(str);
        printf("\n");
    } while(i<1 || i>5);
    return i;
}

void enter(void)
{
    for(;loc<100; loc++) {
        if(loc<100) {
            printf("Enter name and phone number:\n");
            gets(names[loc]);
            if(!*names[loc]) break;
            gets(numbers[loc]);
        }
    }
}

void find(void)
{
    char name[80];
    int i;

    printf("Enter name: ");
    gets(name);

    for(i=0; i<100; i++)
        if(!strcmp(name, names[i]))
            printf("%s %s\n", names[i], numbers[i]);
}

void load(void)
{
    FILE *fp;

    if((fp = fopen("phone", "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    loc = 0;
    while(!feof(fp)) {
        fscanf(fp, "%s%s", names[loc], numbers[loc]);
        loc++;
    }
    fclose(fp);
}

void save(void)
{
    FILE *fp;
    int i;

    if((fp = fopen("phone", "w"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    for(i=0; i<loc; i++) {
        fprintf(fp, "%s %s ", names[i], numbers[i]);
    }
    fclose(fp);
}
```

2.
```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    char str[80];
    int count;

    /* see if correct number of command line arguments */
    if(argc!=2) {
        printf("Usage: display <file>\n");
        exit(1);
    }

    /* open the file */
    if((fp = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open the file.\n");
        exit(1);
    }

    count = 0;
    while(!feof(fp)) {
        fgets(str, 79, fp);
        printf("%s", str);
        count++;

        if(count==23) {
            printf("More? (y/n) ");
            gets(str);
            if(toupper(*str)=='N') break;
            count = 0;
        }
    }

    fclose(fp);

    return 0;
}
```

3.
```c
/* Copy a file. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *from, *to;
    char str[128];

    /* see if correct number of command line arguments */
    if(argc<3) {
        printf("Usage: copy <source> <destination>\n");
        exit(1);
    }

    /* open source file */
    if((from = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open source file.\n");
        exit(1);
    }

    /* open destination file */
    if((to = fopen(argv[2], "w"))==NULL) {
        printf("Cannot open destination file.\n");
        exit(1);
    }

    /* copy the file */
    while(!feof(from)) {
        fgets(str, 127, from);
        if(ferror(from)) {
            printf("Error on input.\n");
            break;
        }
        if(!feof(from)) fputs(str, to);
        if(ferror(to)) {
            printf("Error on output.\n");
            break;
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

---

### 9.5 EXERCISES

1.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp1, *fp2;
    double d;
    int i;

    if((fp1 = fopen("values", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    if((fp2 = fopen("count", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    d = 1.0;
    for(i=0; d!=0.0 && i<32766; i++) {
        printf("Enter a number (0 to quit): ");
        scanf("%lf", &d);
        fwrite(&d, sizeof d, 1, fp1);
    }

    fwrite(&i, sizeof i, 1, fp2);

    fclose(fp1);
    fclose(fp2);

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp1, *fp2;
    double d;
    int i;

    if((fp1 = fopen("values", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    if((fp2 = fopen("count", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    fread(&i, sizeof i, 1, fp2); /* get count */

    for(; i>0; i--) {
        fread(&d, sizeof d, 1, fp1);
        printf("%f\n", d);
    }

    fclose(fp1);
    fclose(fp2);

    return 0;
}
```

---

### 9.6 EXERCISES

1.
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    char ch;
    long l;

    if(argc!=2) {
        printf("You must specify the file.\n");
        exit(1);
    }

    if((fp = fopen(argv[1], "rb"))== NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    fseek(fp, 0, SEEK_END); /* find end of file */
    l = ftell(fp);

    /* go back to the start of the file */
    fseek(fp, 0, SEEK_SET);
    for(; l>=0; l = l - 2L) {
        ch = fgetc(fp);
        putchar(ch);
        fseek(fp, 1L, SEEK_CUR);
    }

    fclose(fp);

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    unsigned char ch, val;

    if(argc!=3) {
        printf("Usage: find <filename> <value>");
        exit(1);
    }

    if((fp = fopen(argv[1], "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    val = atoi(argv[2]);

    while(!feof(fp)) {
        ch = fgetc(fp);
        if(ch == val)
            printf("Found value at %ld\n", ftell(fp));
    }

    fclose(fp);

    return 0;
}
```

---

### 9.7 EXERCISES

1.
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
    if(toupper(getchar())=='Y')
        if(remove(fname))
            printf("\nFile not found or write protected.\n");

    return 0;
}
```

---

### 9.8 EXERCISE

1.
```c
/* Copy using redirection.
   Execute like this:
   C>NAME < in > out
*/
#include <stdio.h>

int main(void)
{
    char ch;

    while(!feof(stdin)) {
        scanf("%c", &ch);
        if(!feof(stdin)) printf("%c", ch);
    }

    return 0;
}
```

---

### MASTERY SKILLS CHECK

1.
```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    char str[80];

    /* see if file name is specified */
    if(argc!=2) {
        printf("File name missing.\n");
        exit(1);
    }

    if((fp = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    while(!feof(fp)) {
        fgets(str, 79, fp);
        if(!feof(fp)) printf("%s", str);
        printf("...More? (y/n) ");
        if(toupper(getchar())=='N') break;
        printf("\n");
    }

    fclose(fp);

    return 0;
}
```

2.
```c
/* Copy a file and convert to uppercase. */
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

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
    if((from = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open source file.\n");
        exit(1);
    }

    /* open destination file */
    if((to = fopen(argv[2], "w"))==NULL) {
        printf("Cannot open destination file.\n");
        exit(1);
    }

    /* copy the file */
    while(!feof(from)) {
        ch = fgetc(from);
        if(!feof(from)) fputc(toupper(ch), to);
    }

    fclose(from);
    fclose(to);

    return 0;
}
```

3. The `fprintf()` and `fscanf()` functions operate exactly like `printf()` and `scanf()`, except that they work with files.
4.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;
    int i, num;

    if((fp = fopen("rand", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    for(i=0; i<100; i++) {
        num = rand();
        fwrite(&num, sizeof num, 1, fp);
    }

    fclose(fp);

    return 0;
}
```

5.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;
    int i, num;

    if((fp = fopen("rand", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    for(i=0; i<100; i++) {
        fread(&num, sizeof num, 1, fp);
        printf("%d\n", num);
    }

    fclose(fp);

    return 0;
}
```

6.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;
    long i;
    int num;

    if((fp = fopen("rand", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    printf("Which number (0-99)? ");
    scanf("%ld", &i);
    fseek(fp, i * sizeof(int), SEEK_SET);
    fread(&num, sizeof num, 1, fp);
    printf("%d\n", num);

    fclose(fp);

    return 0;
}
```

7. The "console" I/O functions are simply special cases of the general file system.

---

### CUMULATIVE SKILLS CHECK

1.
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

char names[MAX][80];   /* author names */
char titles[MAX][80];  /* titles */
char pubs[MAX][80];    /* publisher */

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
                break;
        }
    } while(choice!=5);

    return 0;
}

/* Return a menu selection. */
int menu(void)
{
    int i;
    char str[80];

    printf("Card Catalog:\n");
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

    for(i=top; i<MAX; i++) {
        if(loc<100) {
            printf("Enter name: ");
            gets(phone[loc].name);
            if(!*phone[loc].name) break;
            printf("Enter area code: ");
            gets(temp);
            phone[loc].areacode = atoi(temp);
            printf("Enter number: ");
            gets(phone[loc].number);
        }
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
        if(!strcmp(name, names[i])) {
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
        if(!strcmp(title, titles[i])) {
            display(i);
            found = 1;
            printf("\n");
        }

    if(!found) printf("Not Found\n");
}

/* Display catalog entry. */
void display(int i)
{
    printf("%s\n", titles[i]);
    printf("by %s\n", names[i]);
    printf("Published by %s\n", pubs[i]);
}

/* Load the catalog file. */
void load(void)
{
    FILE *fp;

    if((fp = fopen("catalog", "rb"))==NULL) {
        printf("Catalog file not on disk.\n");
        return;
    }

    fread(&top, sizeof top, 1, fp); /* read count */
    fread(names, sizeof names, 1, fp);
    fread(titles, sizeof titles, 1, fp);
    fread(pubs, sizeof pubs, 1, fp);

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

    fwrite(&top, sizeof top, 1, fp); /* write count */
    fwrite(names, sizeof names, 1, fp);
    fwrite(titles, sizeof titles, 1, fp);
    fwrite(pubs, sizeof pubs, 1, fp);

    fclose(fp);
}
```

2.
```c
/* Copy a file and remove tabs. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *from, *to;
    char ch;
    int tab, count;

    /* see if correct number of command line arguments */
    if(argc!=3) {
        printf("Usage: copy <source> <destination>\n");
        exit(1);
    }

    /* open source file */
    if((from = fopen(argv[1], "r"))==NULL) {
        printf("Cannot open source file.\n");
        exit(1);
    }

    /* open destination file */
    if((to = fopen(argv[2], "w"))==NULL) {
        printf("Cannot open destination file.\n");
        exit(1);
    }

    /* copy the file */
    count = 0;
    while(!feof(from)) {
        ch = fgetc(from);
        if(ch=='\t') {
            for(tab = count; tab<8; tab++)
                fputc(' ', to);
            count = 0;
        }
        else {
            if(!feof(from)) fputc(ch, to);
            count++;
            if(count==8 || ch=='\n') count = 0;
        }
    }
    fclose(from);
    fclose(to);

    return 0;
}
```

---

## Chapter 10

### REVIEW SKILLS CHECK

1.
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
            printf("Error on input.\n");
            break;
        }
        if(!feof(from)) fputc(ch, to);
        if(ferror(to)) {
            printf("Error on output.\n");
            break;
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

2.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;

    /* open file */
    if((fp = fopen("myfile", "w"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    fprintf(fp, "%s %f %X %c", "this is a string",
            1230.23, 0x1FFF, 'A');

    fclose(fp);

    return 0;
}
```

3.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;
    int count[20], i;

    /* open file */
    if((fp = fopen("TEMP", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    for(i=0; i<20; i++) count[i] = i+1;

    fwrite(count, sizeof count, 1, fp);

    fclose(fp);

    return 0;
}
```

4.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE *fp;
    int count[20], i;

    /* open file */
    if((fp = fopen("TEMP", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    fread(count, sizeof count, 1, fp);

    for(i=0; i<20; i++) printf("%d ", count[i]);

    fclose(fp);

    return 0;
}
```
5. `stdin`, `stdout`, and `stderr` are three streams that are opened automatically when your C program begins executing. By default they refer to the console, but in operating systems that support I/O redirection, they can be redirected to other devices.
6. The `printf()` and `scanf()` functions are part of the C file system. They are simply special case functions that automatically use `stdin` and `stdout`.

---

### 10.1 EXERCISES

1.
```c
/* A simple computerized telephone book. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

struct phone_type {
    char name[40];
    int areacode;
    char number[9];
} phone[MAX];

int loc=0;

int menu(void);
void enter(void);
void load(void);
void save(void);
void find(void);

int main(void)
{
    int choice;

    do {
        choice = menu();
        switch(choice) {
            case 1: enter();
                break;
            case 2: find();
                break;
            case 3: save();
                break;
            case 4: load();
                break;
        }
    } while(choice!=5);

    return 0;
}

/* Get menu choice. */
int menu(void)
{
    int i;
    char str[80];

    printf("1. Enter names and numbers\n");
    printf("2. Find numbers\n");
    printf("3. Save directory to disk\n");
    printf("4. Load directory from disk\n");
    printf("5. Quit\n");

    do {
        printf("Enter your choice: ");
        gets(str);
        i = atoi(str);
        printf("\n");
    } while(i<1 || i>5);
    return i;
}

void enter(void)
{
    char temp[80];

    for(;loc<100; loc++) {
        if(loc<100) {
            printf("Enter name: ");
            gets(phone[loc].name);
            if(!*phone[loc].name) break;
            printf("Enter area code: ");
            gets(temp);
            phone[loc].areacode = atoi(temp);
            printf("Enter number: ");
            gets(phone[loc].number);
        }
    }
}

void find(void)
{
    char name[80];
    int i;

    printf("Enter name: ");
    gets(name);
    if(!*name) return;

    for(i=0; i<100; i++)
        if(!strcmp(name, phone[i].name))
            printf("%s (%d) %s\n", phone[i].name,
                   phone[i].areacode, phone[i].number);
}

void load(void)
{
    FILE *fp;

    if((fp = fopen("phone", "r"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    loc = 0;
    while(!feof(fp)) {
        fscanf(fp, "%s%d%s", phone[loc].name,
               &phone[loc].areacode, phone[loc].number);
        loc++;
    }
    fclose(fp);
}

void save(void)
{
    FILE *fp;
    int i;

    if((fp = fopen("phone", "w"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    for(i=0; i<loc; i++) {
        fprintf(fp, "%s %d %s ", phone[i].name,
                phone[i].areacode, phone[i].number);
    }
    fclose(fp);
}
```
2. The variable `i` is a member of structure `s_type`. Therefore, it cannot be used by itself. Instead, it must be accessed using `s` and the dot operator, as shown here:
`s.i = 10;`

---

### 10.2 EXERCISES

1. No. Since `p` is a pointer to a structure, you must use the arrow operator, not the dot operator, to access a member.
2.
```c
#include <stdio.h>
#include <time.h>

int main(void)
{
    struct tm *systime, *gmt;
    time_t t;

    t = time(NULL);
    systime = localtime(&t);

    printf("Time is %.2d:%.2d:%.2d\n", systime->tm_hour,
            systime->tm_min, systime->tm_sec);
    gmt = gmtime(&t);
    printf("Coordinated Universal Time is %.2d:%.2d:%.2d\n",
            gmt->tm_hour,
            gmt->tm_min, gmt->tm_sec);
    printf("Date: %.2d/%.2d/%.2d", systime->tm_mon+1,
            systime->tm_mday, systime->tm_year);

    return 0;
}
```

---

### 10.3 EXERCISES

1.
```c
/* A simple computerized telephone book. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

struct address {
    char street[40];
    char city[40];
    char state[3];
    char zip[12];
};

struct phone_type {
    char name[40];
    int areacode;
    char number[9];
    struct address addr;
} phone[MAX];

int loc=0;

int menu(void);
void enter(void);
void load(void);
void save(void);
void find(void);

int main(void)
{
    int choice;

    do {
        choice = menu();
        switch(choice) {
            case 1: enter();
                break;
            case 2: find();
                break;
            case 3: save();
                break;
            case 4: load();
                break;
        }
    } while(choice!=5);

    return 0;
}

/* Get menu choice. */
int menu(void)
{
    int i;
    char str[80];

    printf("1. Enter names and numbers\n");
    printf("2. Find numbers\n");
    printf("3. Save directory to disk\n");
    printf("4. Load directory from disk\n");
    printf("5. Quit\n");

    do {
        printf("Enter your choice: ");
        gets(str);
        i = atoi(str);
        printf("\n");
    } while(i<1 || i>5);
    return i;
}

void enter(void)
{
    char temp[80];

    for(;loc<100; loc++) {
        if(loc<100) {
            printf("Enter name: ");
            gets(phone[loc].name);
            if(!*phone[loc].name) break;
            printf("Enter area code: ");
            gets(temp);
            phone[loc].areacode = atoi(temp);
            printf("Enter number: ");
            gets(phone[loc].number);

            /* input address info */
            printf("Enter street address: ");
            gets(phone[loc].addr.street);
            printf("Enter city: ");
            gets(phone[loc].addr.city);
            printf("Enter State: ");
            gets(phone[loc].addr.state);
            printf("Enter zip code: ");
            gets(phone[loc].addr.zip);
        }
    }
}

void find(void)
{
    char name[80];
    int i;

    printf("Enter name: ");
    gets(name);
    if(!*name) return;

    for(i=0; i<100; i++)
        if(!strcmp(name, phone[i].name)) {
            printf("%s (%d) %s\n", phone[i].name,
                   phone[i].areacode, phone[i].number);
            printf("%s\n%s %s %s\n", phone[i].addr.street,
                   phone[i].addr.city, phone[i].addr.state,
                   phone[i].addr.zip);
        }
}

void load(void)
{
    FILE *fp;

    if((fp = fopen("phone", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    loc = 0;
    while(!feof(fp)) {
        fread(&phone[loc], sizeof phone[loc], 1, fp);
        loc++;
    }
    fclose(fp);
}

void save(void)
{
    FILE *fp;
    int i;

    if((fp = fopen("phone", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    for(i=0; i<loc; i++) {
        fwrite(&phone[i], sizeof phone[i], 1, fp);
    }
    fclose(fp);
}
```

---

### 10.4 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    struct b_type {
        int a: 3;
        int b: 3;
        int c: 2;
    } bvar;

    bvar.a = -1;
    bvar.b = 3;
    bvar.c = 1;
    printf("%d %d %d", bvar.a, bvar.b, bvar.c);

    return 0;
}
```

---

### 10.5 EXERCISES

1.
```c
#include <stdio.h>
#include <stdlib.h>

union u_type {
    double d;
    unsigned char c[8];
};

double uread(FILE *fp);
void uwrite(double num, FILE *fp);

int main(void)
{
    FILE *fp;
    double d;

    if((fp = fopen("myfile", "wb+"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    uwrite(100.23, fp);
    d = uread(fp);
    printf("%lf", d);

    return 0;
}

void uwrite(double num, FILE *fp)
{
    int i;
    union u_type var;

    var.d = num;
    for(i=0; i<8; i++) fputc(var.c[i], fp);
}

double uread(FILE *fp)
{
    int i;
    union u_type var;

    rewind(fp);
    for(i=0; i<8; i++) var.c[i] = fgetc(fp);

    return var.d;
}
```

2.
```c
#include <stdio.h>

int main(void)
{
    union t_type {
        long l;
        int i;
    } uvar;

    uvar.l = 0L; /* clear l */
    uvar.i = 100;

    printf("%ld", uvar.l);

    return 0;
}
```

---

### MASTERY SKILLS CHECK

1. A structure is a named group of related variables. A union defines a memory location shared by two or more variables of different types.
2.
```c
struct s_type {
    char ch;
    float d;
    int i;
    char str[80];
    double balance;
} s_var;
```
3. Because `p` is a pointer to a structure, you must use the arrow operator to reference an element, not the dot operator.
4.
```c
#include <stdio.h>
#include <stdlib.h>

struct s_type {
    char name[40];
    char phone[14];
    int hours;
    double wage;
} emp[10];

int main(void)
{
    FILE *fp;
    int i;
    char temp[80];

    if((fp = fopen("emp", "wb"))==NULL) {
        printf("Cannot open EMP file.\n");
        exit(1);
    }

    for(i=0; i<10; i++) {
        printf("Enter name: ");
        gets(emp[i].name);
        printf("Enter telephone number: ");
        gets(emp[i].phone);
        printf("Enter hours worked: ");
        gets(temp);
        emp[i].hours = atoi(temp);
        printf("Enter hourly wage: ");
        gets(temp);
        emp[i].wage = atof(temp);
    }

    fwrite(emp, sizeof emp, 1, fp);
    fclose(fp);

    return 0;
}
```

5.
```c
#include <stdio.h>
#include <stdlib.h>

struct s_type {
    char name[40];
    char phone[14];
    int hours;
    double wage;
} emp[10];

int main(void)
{
    FILE *fp;
    int i;

    if((fp = fopen("emp", "rb"))==NULL) {
        printf("Cannot open EMP file.\n");
        exit(1);
    }

    fread(emp, sizeof emp, 1, fp);
    for(i=0; i<10; i++) {
        printf("%s %s\n", emp[i].name, emp[i].phone);
        printf("%d %f\n\n", emp[i].hours, emp[i].wage);
    }

    fclose(fp);

    return 0;
}
```
6. A bit-field is a structure member that specifies its length in bits.
7.
```c
#include <stdio.h>

int main(void)
{
    union u_type {
        short int i;
        unsigned char c[2];
    } uvar;

    uvar.i = 99;

    printf("High order byte: %u\n", uvar.c[1]);
    printf("Low order byte: %u\n", uvar.c[0]);

    return 0;
}
```

---

### CUMULATIVE SKILLS CHECK

1.
```c
#include <stdio.h>

struct s_type {
    int i;
    char ch;
    double d;
} var1, var2;

void struct_swap(struct s_type *i, struct s_type *j);

int main(void)
{
    var1.i = 100;
    var2.i = 99;
    var1.ch = 'a';
    var2.ch = 'b';
    var1.d = 1.0;
    var2.d = 2.0;

    printf("var1: %d %c %f\n", var1.i, var1.ch, var1.d);
    printf("var2: %d %c %f\n", var2.i, var2.ch, var2.d);

    struct_swap(&var1, &var2);

    printf("After swap:\n");
    printf("var1: %d %c %f\n", var1.i, var1.ch, var1.d);
    printf("var2: %d %c %f", var2.i, var2.ch, var2.d);

    return 0;
}

void struct_swap(struct s_type *i, struct s_type *j)
{
    struct s_type temp;

    temp = *i;
    *i = *j;
    *j = temp;
}
```

2.
```c
/* Copy a file. */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *from, *to;
    union u_type {
        int i;
        char ch;
    } uvar;

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
    for(;;) {
        uvar.i = fgetc(from);
        if(uvar.i==EOF) break;
        fputc(uvar.ch, to);
    }
    fclose(from);
    fclose(to);

    return 0;
}
```
3. You cannot use a structure as an argument to `scanf()`. However, you can use a structure element as an argument, as shown here:
`scanf("%d", &var.a);`
4.
```c
#include <string.h>
#include <stdio.h>

struct s_type {
    char str[80];
} var;

void f(struct s_type i);

int main(void)
{
    strcpy(var.str, "this is original string");
    f(var);
    printf("%s", var.str);

    return 0;
}

void f(struct s_type i)
{
    strcpy(i.str, "new string");
    printf("%s\n", i.str);
}
```

---

## Chapter 11

### REVIEW SKILLS CHECK

1.
```c
#include <stdio.h>

struct num_type {
    int i;
    int sqr;
    int cube;
} nums[10];

int main(void)
{
    int i;

    for(i=1; i<11; i++) {
        nums[i-1].i = i;
        nums[i-1].sqr = i*i;
        nums[i-1].cube = i*i*i;
    }

    for(i=0; i<10; i++) {
        printf("%d ", nums[i].i);
        printf("%d ", nums[i].sqr);
        printf("%d\n", nums[i].cube);
    }

    return 0;
}
```

2.
```c
#include <stdio.h>

union i_to_c {
    char c[2];
    short int i;
} ic;

int main(void)
{
    printf("Enter an integer ");
    scanf("%hd", &ic.i);
    printf("Character representation of each byte: %c %c",
           ic.c[0], ic.c[1]);

    return 0;
}
```
3. The fragment displays 8, the size of the largest element of the union.
4. To access a structure member when actually using a structure variable, you must use the dot operator. The arrow operator is used when accessing a member using a pointer to a structure.
5. A bit-field is a structure element whose size is specified in bits.

---

### 11.1 EXERCISES

1. The best variables to make into register types are `k` and `m`, because they are accessed most frequently.
2.
```c
#include <stdio.h>

void sum_it(int value);

int main(void)
{
    sum_it(10);
    sum_it(20);
    sum_it(30);
    sum_it(40);

    return 0;
}

void sum_it(int value)
{
    static int sum=0;

    sum = sum + value;
    printf("Current value: %d\n", sum);
}
```
4. You cannot obtain the address of a register variable.

---

### 11.2 EXERCISES

1.
```c
#include <stdio.h>

const double version = 6.01;

int main(void)
{
    printf("Version %.2f", version);

    return 0;
}
```

2.
```c
#include <stdio.h>

char *mystrcpy(char *to, const char *from);

int main(void)
{
    char *p, str[80];

    p = mystrcpy(str, "testing");

    printf("%s %s", p, str);

    return 0;
}

char *mystrcpy(char *to, const char *from)
{
    char *temp;

    temp = to;

    while(*from) *to++ = *from++;
    *to = '\0'; /* null terminator */

    return temp;
}
```

---

### 11.3 EXERCISES

2. `enum money {penny, nickel, quarter, half_dollar, dollar};`
3. No, you cannot output an enumeration constant as a string as is attempted in the `printf()` statement.

---

### 11.4 EXERCISES

1.
```c
#include <stdio.h>

typedef unsigned long UL;

int main(void)
{
    UL count;

    count = 312323;

    printf("%lu", count);

    return 0;
}
```
2. The typedef statement is out of order. The correct form of typedef is
`typedef oldname newname;`

---

### 11.5 EXERCISES

1.
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *in, *out;
    unsigned char ch;

    if(argc!=3) {
        printf("Usage: code <in> <out>\n");
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

    while(!feof(in)) {
        ch = fgetc(in);
        if(!feof(in)) fputc(~ch, out);
    }

    fclose(in);
    fclose(out);

    return 0;
}
```

2.
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *in, *out;
    unsigned char ch;

    if(argc!=4) {
        printf("Usage: code <in> <out> <key>\n");
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

    while(!feof(in)) {
        ch = fgetc(in);
        ch = *argv[3] ^ ch;
        if(!feof(in)) fputc(ch, out);
    }

    fclose(in);
    fclose(out);

    return 0;
}
```

3.
   a. 0000 0001
   b. 1111 1111
   c. 1111 1101
4.
```c
char ch;
.
.
.
/* To zero high order bit, AND with 127, which
   in binary is 0111 1111. This causes the high-
   order bit to be zeroed and all other bits left
   untouched.
*/
ch = ch & 127;
```

---

### 11.6 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i, j, k;

    printf("Enter a number: ");
    scanf("%d", &i);

    j = i << 1;
    k = i >> 1;
    printf("%d doubled: %d\n", i, j);
    printf("%d halved: %d", i, k);

    return 0;
}
```

2.
```c
#include <stdio.h>

void rotate(unsigned char *c);

int main(void)
{
    unsigned char ch;
    int i;

    ch = 1;

    for(i=0; i<16; i++) {
        rotate(&ch);
        printf("%u\n", ch);
    }

    return 0;
}

void rotate(unsigned char *c)
{
    union {
        unsigned char ch[2];
        unsigned u;
    } rot;

    rot.u = 0; /* clear 16 bits */

    rot.ch[0] = *c;

    /* shift integer left */
    rot.u = rot.u << 1;

    /* See if a bit got shifted into c[1].
       If so, OR it back onto the other end. */
    if(rot.ch[1]) rot.ch[0] = rot.ch[0] | 1;

    *c = rot.ch[0];
}
```

---

### 11.7 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i, j, answer;

    printf("Enter two integers: ");
    scanf("%d%d", &i, &j);

    answer = j ? i/j: 0;
    printf("%d", answer);

    return 0;
}
```
2. `count = a>b ? 100 : 0;`

---

### 11.8 EXERCISES

2. `x &= y;`
3.
```c
#include <stdio.h>

int main(void)
{
    int i;

    for(i=17; i<=1000; i+=17)
        printf("%d\n", i);

    return 0;
}
```

---

### 11.9 EXERCISES

1.
```c
#include <stdio.h>

int main(void)
{
    int i, j, k;

    for(i=0, j=-50, k=i+j; i<100; i++, j++, k=i+j)
        printf("k = %d\n", k);

    return 0;
}
```
2. 3

---

### MASTERY SKILLS CHECK

1. The `register` specifier causes the C compiler to provide the fastest access possible for the variable it precedes.
2. The `const` specifier tells the C compiler that no statement in the program may modify a variable declared as `const`. Also, a const pointer parameter may not be used to modify the object pointed to by the pointer. The `volatile` specifier tells the compiler that any variable it precedes may have its value changed in ways not explicitly specified by the program.
3.
```c
#include <stdio.h>

int main(void)
{
    register int i, sum;

    sum = 0;
    for(i=1; i<101; i++)
        sum = sum + i;

    printf("%d", sum);

    return 0;
}
```
4. Yes, the statement is valid. It creates another name for the type **long double**.
5.
```c
#include <stdio.h>
#include <conio.h>

int main(void)
{
    char ch1, ch2;
    char mask, i;

    printf("Enter two characters: ");
    ch1 = getche();
    ch2 = getche();
    printf("\n");

    mask = 1;
    for(i=0; i<8; i++) {
        if((mask & ch1) && (mask & ch2))
            printf("bits %d the same\n", i);
        mask <<= 1;
    }

    return 0;
}
```
6. The `<<` and `>>` are the left and right shift operators, respectively.
7. `c += 10;`
8. `count = done ? 0 : 100;`
9. An enumeration is a list of named integer constants. Here is one that enumerates the planets:
```c
enum planets {Mercury, Venus, Earth, Mars, Jupiter,
              Saturn, Neptune, Uranus, Pluto} ;
```

---

### CUMULATIVE SKILLS CHECK

1.
```c
#include <stdio.h>

void show_binary(unsigned u);

int main(void)
{
    unsigned char ch, t1, t2;

    ch = 100;
    show_binary(ch);

    t1 = ch;
    t2 = ch;

    t1 <<= 4;
    t2 >>= 4;

    ch = t1 | t2;

    show_binary(ch);

    return 0;
}

void show_binary(unsigned u)
{
    unsigned n;

    for(n=128; n>0; n=n/2)
        if(u & n) printf("1 ");
        else printf("0 ");
    printf("\n");
}
```

2.
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *in;
    unsigned char ch;

    if(argc!=2) {
        printf("Usage: code <in>\n");
        exit(1);
    }

    if((in = fopen(argv[1], "rb"))==NULL) {
        printf("Cannot open input file.\n");
        exit(1);
    }

    while(!feof(in)) {
        ch = fgetc(in);
        if(!feof(in)) putchar(~ch);
    }

    fclose(in);

    return 0;
}
```
3. Yes, any type of variable can be specified using `register`. However, on some types, it may have no effect.
4.
```c
/* A simple computerized telephone book. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100

struct address {
    char street[40];
    char city[40];
    char state[3];
    char zip[12];
};

struct phone_type {
    char name[40];
    int areacode;
    char number[9];
    struct address addr;
} phone[MAX];

int loc = 0;

int menu(void);
void enter(void);
void load(void);
void save(void);
void find(void);

int main(void)
{
    register int choice;

    do {
        choice = menu();
        switch(choice) {
            case 1: enter();
                break;
            case 2: find();
                break;
            case 3: save();
                break;
            case 4: load();
                break;
        }
    } while(choice!=5);

    return 0;
}

/* Get menu choice. */
int menu(void)
{
    register int i;
    char str[80];

    printf("1. Enter names and numbers\n");
    printf("2. Find numbers\n");
    printf("3. Save directory to disk\n");
    printf("4. Load directory from disk\n");
    printf("5. Quit\n");

    do {
        printf("Enter your choice: ");
        gets(str);
        i = atoi(str);
        printf("\n");
    } while(i<1 || i>5);
    return i;
}

void enter(void)
{
    char temp[80];

    for(; loc<100; loc++) {
        if(loc<100) {
            printf("Enter name: ");
            gets(phone[loc].name);
            if(!*phone[loc].name) break;
            printf("Enter area code: ");
            gets(temp);
            phone[loc].areacode = atoi(temp);
            printf("Enter number: ");
            gets(phone[loc].number);

            /* input address info */
            printf("Enter street address: ");
            gets(phone[loc].addr.street);
            printf("Enter city: ");
            gets(phone[loc].addr.city);
            printf("Enter State: ");
            gets(phone[loc].addr.state);
            printf("Enter zip code: ");
            gets(phone[loc].addr.zip);
        }
    }
}

void find(void)
{
    char name[80];
    register int i;

    printf("Enter name: ");
    gets(name);
    if(!*name) return;

    for(i=0; i<100; i++)
        if(!strcmp(name, phone[i].name)) {
            printf("%s (%d) %s\n", phone[i].name,
                   phone[i].areacode, phone[i].number);
            printf("%s\n%s %s %s\n", phone[i].addr.street,
                   phone[i].addr.city, phone[i].addr.state,
                   phone[i].addr.zip);
        }
}

void load(void)
{
    FILE *fp;

    if((fp = fopen("phone", "rb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    loc = 0;
    while(!feof(fp)) {
        fread(&phone[loc], sizeof phone[loc], 1, fp);
        loc++;
    }
    fclose(fp);
}

void save(void)
{
    FILE *fp;
    register int i;

    if((fp = fopen("phone", "wb"))==NULL) {
        printf("Cannot open file.\n");
        exit(1);
    }

    for(i=0; i<loc; i++) {
        fwrite(&phone[i], sizeof phone[i], 1, fp);
    }
    fclose(fp);
}
```

---

## Chapter 12

### REVIEW SKILLS CHECK

1. Modifying a variable with `register` causes the compiler to store the variable in such a way that it is as fast as possible. For integer and character types, this typically means storing it in a register of the CPU.
2. Because `i` is declared as const the function cannot modify any object pointed to by it.
3.
   a. 1100 0100
   b. 1111 1111
   c. 0011 1011
4.
```c
#include <stdio.h>

int main(void)
{
    int i;

    printf("Enter a number: ");
    scanf("%d", &i);

    printf("Doubled: %d\n", i << 1);
    printf("Halved: %d\n", i >> 1);

    return 0;
}
```
5.
```c
a = b = c = 1;

max = a<b ? 100 : 0;

i *= 2;
```
6. The `extern` modifier is principally used to inform the compiler about global variables defined in a different file. Placing `extern` in front of a variable's declaration tells the compiler that the variable is defined elsewhere, but allows the current file to refer to it.

---

### 12.1 EXERCISES

1. `#define RANGE(i, min, max) ((i)<(min)) || ((i)>(max)) ? 1 : 0`
2.
```c
#include <stdio.h>

#define ABS(i) (i)<0 ? -(i) : i

int main(void)
{
    printf("%d %d", ABS(-1), ABS(1));

    return 0;
}
```

---

### 12.2 EXERCISES

1.
```c
#include <stdio.h>

#define INT 0
#define FLOAT 1
#define PWR_TYPE INT

int main(void)
{
    int e;
#if PWR_TYPE==FLOAT
    double base, result;
#elif PWR_TYPE==INT
    int base, result;
#endif

#if PWR_TYPE==FLOAT
    printf("Enter floating point base: ");
    scanf("%lf", &base);
#elif PWR_TYPE==INT
    printf("Enter integer base: ");
    scanf("%d", &base);
#endif
    printf("Enter integer exponent (greater than 0): ");
    scanf("%d", &e);

    result = 1;
    for(; e; e--)
        result = result * base;

#if PWR_TYPE==FLOAT
    printf("Result: %f", result);
#elif PWR_TYPE==INT
    printf("Result: %d", result);
#endif

    return 0;
}
```

2. No. You cannot use an expression like !MIKE with `#ifdef`. Here are two possible solutions:
```c
#ifndef MIKE
.
.
.
#endif

/* or */

#if !defined MIKE
.
.
.
#endif
```

---

### 12.5 EXERCISES

2. The program displays **one two**.

---

### 12.6 EXERCISES

2.
```c
#include <stdio.h>
#include <stdlib.h>

int comp(const void *i, const void *j);

int main(void)
{
    int sort[100], i, key;
    int *p;

    for(i=0; i<100; i++)
        sort[i] = rand();

    qsort(sort, 100, sizeof(int), comp);

    for(i=0; i<100; i++)
        printf("%d\n", sort[i]);

    printf("Enter number to find: ");
    scanf("%d", &key);
    p = bsearch(&key, sort, 100, sizeof(int), comp);
    if(p) printf("Number is in array.\n");
    else printf("Number not found.\n");

    return 0;
}

int comp(const void *i, const void *j)
{
    return *(int*)i - *(int*)j;
}
```

3.
```c
#include <stdio.h>

int sum(int a, int b);
int subtract(int a, int b);
int mul(int a, int b);
int div(int a, int b);
int modulus(int a, int b);

/* initialize the pointer array */
int (*p[5]) (int x, int y) = {
    sum, subtract, mul, div, modulus
};

int main(void)
{
    int result;
    int i, j, op;

    printf("Enter two numbers: ");
    scanf("%d%d", &i, &j);
    printf("0: add, 1: subtract, 2: multiply, 3: divide, 4: modulus\n");
    do {
        printf("Enter number of operation: ");
        scanf("%d", &op);
    } while(op<0 || op>4);

    result = (*p[op]) (i, j);
    printf("%d", result);

    return 0;
}

int sum(int a, int b)
{
    return a+b;
}

int subtract(int a, int b)
{
    return a-b;
}

int mul(int a, int b)
{
    return a*b;
}

int div(int a, int b)
{
    if(b) return a/b;
    else return 0;
}

int modulus(int a, int b)
{
    if(b) return a%b;
    else return 0;
}
```

---

### 12.7 EXERCISES

2.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *p, i;

    p = malloc(10*sizeof(int));
    if(!p) {
        printf("Allocation Error");
        exit(1);
    }

    for(i=0; i<10; i++) p[i] = i+1;

    for(i=0; i<10; i++) printf("%d ", *(p+i));

    free(p);

    return 0;
}
```

3. The statement
`*p = malloc(10);`
should be
`p = malloc(10);`
Also, the value returned by `malloc()` is not verified as a valid pointer.

---

### MASTERY SKILLS CHECK

1. When you specify the file name within angle brackets, the compiler searches for the file in an implementation-defined manner. When you enclose the file name within double quotes, the compiler first tries some other implementation-defined manner to find the file. If that fails, it restarts the search as if you had enclosed the file name within angle brackets.
2.
```c
#ifdef DEBUG
if(!(j%2)) {
    printf("j = %d\n", j);
    j = 0;
}
#endif
```

3.
```c
#if DEBUG==1
if(!(j%2)) {
    printf("j = %d\n", j);
    j = 0;
}
#endif
```

4. To undefine a macro name use `#undef`.
5. `__FILE__` is a predefined macro that contains the name of the source file currently being compiled.
6. The `#` operator makes the argument it precedes into a quoted string. The `##` operator concatenates two arguments.
7.
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp(const void *i, const void *j);

int main(void)
{
    char str[] = "this is a test of qsort";

    qsort(str, strlen(str), 1, comp);

    printf(str);

    return 0;
}

int comp(const void *i, const void *j)
{
    return *(char*)i - *(char*)j;
}
```

8.
```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    double *p;

    p = malloc(sizeof(double));
    if(!p) {
        printf("Allocation Error");
        exit(1);
    }

    *p = 99.01;
    printf("%f", *p);
    free(p);

    return 0;
}
```

---

### CUMULATIVE SKILLS CHECK

1.
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
    unsigned date;       /* date of publication */
    unsigned char ed;    /* edition */
} *cat[MAX]; /* notice that this declares a pointer array. */

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

    printf("Card Catalog:\n");
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
        /* allocate memory for book info */
        cat[i] = malloc(sizeof(struct catalog));
        if(!cat[i]) {
            printf("Out of memory.\n");
            return;
        }

        printf("Enter author name (ENTER to quit): ");
        gets(cat[i]->name);
        if(!*cat[i]->name) break;
        printf("Enter title: ");
        gets(cat[i]->title);
        printf("Enter publisher: ");
        gets(cat[i]->pub);
        printf("Enter copyright date: ");
        gets(temp);
        cat[i]->date = (unsigned) atoi(temp);
        printf("Enter edition: ");
        gets(temp);
        cat[i]->ed = (unsigned char) atoi(temp);
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
        if(!strcmp(name, cat[i]->name)) {
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
        if(!strcmp(title, cat[i]->title)) {
            display(i);
            found = 1;
            printf("\n");
        }

    if(!found) printf("Not Found\n");
}

/* Display catalog entry. */
void display(int i)
{
    printf("%s\n", cat[i]->title);
    printf("by %s\n", cat[i]->name);
    printf("Published by %s\n", cat[i]->pub);
    printf("Copyright: %u, %u edition\n", cat[i]->date,
            cat[i]->ed);
}

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

    for(i=0; i<top; i++) {
        cat[i] = malloc(sizeof(struct catalog));
        if(!cat[i]) {
            printf("Out of memory.\n");
            top = i-1;
            break;
        }
        if(fread(cat[i], sizeof(struct catalog), 1, fp) != 1) {
            printf("Error reading catalog data.\n");
            exit(1);
        }
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

    for(i=0; i<top; i++)
        if(fwrite(cat[i], sizeof(struct catalog), 1, fp) != 1) {
            printf("Error writing catalog data.\n");
            exit(1);
        }

    fclose(fp);
}
```

2.
```c
#include <stdio.h>

#define CODE_IT(ch) ~ch

int main(void)
{
    int ch;

    printf("Enter a character: ");
    ch = getchar();
    printf("%c coded is %c", ch, CODE_IT(ch));

    return 0;
}
```
