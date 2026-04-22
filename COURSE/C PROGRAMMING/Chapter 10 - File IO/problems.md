# Chapter 10 - Practice Set

## Problem 1
Write a program to read three integers from a file.

**Solution:**
```c
#include <stdio.h>

int main() {
    int a, b, c;
    FILE *ptr;
    ptr = fopen("pr01.txt", "r");
    if (ptr != NULL) {
        fscanf(ptr, "%d %d %d", &a, &b, &c);
        printf("The values of a b and c is %d %d %d\n", a, b, c);
        fclose(ptr);
    } else {
        printf("File does not exist\n");
    }
    return 0;
}
```

## Problem 2
Write a program to generate multiplication table of a given number in text format. Make sure that the file is readable and well formatted.

**Solution:**
```c
#include <stdio.h>

int main() {
    FILE *ptr;
    int num;
    printf("Enter the integer you need the table of\n");
    scanf("%d", &num);
    ptr = fopen("table.txt", "w");
    for (int i = 0; i < 10; i++) {
        fprintf(ptr, "%d X %d = %d\n", num, i + 1, num * (i + 1));
    }
    fclose(ptr);
    printf("Successfully generated table of %d to table.txt\n", num);
    return 0;
}
```

## Problem 3
Write a program to read a text file character by character and write its content twice in separate file.

**Solution:**
```c
#include <stdio.h>

int main() {
    FILE *ptr1;
    FILE *ptr2;
    ptr1 = fopen("a.txt", "r");
    ptr2 = fopen("b.txt", "w");
    
    char c = fgetc(ptr1);
    while (c != EOF) {
        fputc(c, ptr2);
        fputc(c, ptr2);
        c = fgetc(ptr1);
    }
    fclose(ptr1);
    fclose(ptr2);
    return 0;
}
```

## Problem 4
Take name and salary of two employees as input from the user and write them to a text file in the following format:
i. Name1, 3300
ii. Name2, 7700

**Solution:**
```c
#include <stdio.h>

int main() {
    char name1[30], name2[30];
    int salary1, salary2;
    
    printf("Enter name 1: ");
    scanf("%s", name1);
    printf("Enter salary 1: ");
    scanf("%d", &salary1);
    
    printf("Enter name 2: ");
    scanf("%s", name2);
    printf("Enter salary 2: ");
    scanf("%d", &salary2);
    
    FILE *ptr = fopen("emp.txt", "w");
    fprintf(ptr, "%s, %d\n", name1, salary1);
    fprintf(ptr, "%s, %d\n", name2, salary2);
    fclose(ptr);
    return 0;
}
```

## Problem 5
Write a program to modify a file containing an integer to double its value.

**Solution:**
```c
#include <stdio.h>

int main() {
    FILE *ptr;
    int value;
    
    ptr = fopen("value.txt", "r");
    if (ptr != NULL) {
        fscanf(ptr, "%d", &value);
        fclose(ptr);
        
        ptr = fopen("value.txt", "w");
        fprintf(ptr, "%d", value * 2);
        fclose(ptr);
    }
    return 0;
}
```
