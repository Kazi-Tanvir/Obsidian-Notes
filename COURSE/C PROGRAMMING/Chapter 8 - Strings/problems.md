# Chapter 8 - Practice Set

## Problem 2
Write a program to take string as an input from the user using %c and %s confirm that the strings are equal.

**Solution:**
```c
#include <stdio.h>
#include <string.h>

int main() {
    char st1[34];
    char st2[34];
    char c;
    int i = 0;
    
    printf("Enter the value of first string\n");
    scanf("%s", st1);
    
    printf("Enter the value of second string character by character\n");
    while (1) {
        fflush(stdin);
        scanf("%c", &c);
        if (c == '\n') break;
        st2[i] = c;
        i++;
    }
    st2[i] = '\0';
    
    printf("The value of st1 is %s\n", st1);
    printf("The value of st2 is %s\n", st2);
    printf("strcmp for these strings returns %d", strcmp(st1, st2));
    
    return 0;
}
```

## Problem 3
Write your own version of strlen function from `<string.h>`

**Solution:**
```c
#include <stdio.h>

int myStrlen(char *st) {
    char *ptr = st;
    int len = 0;
    while (*ptr != '\0') {
        len++;
        ptr++;
    }
    return len;
}

int main() {
    char st[] = "Harry";
    int l = myStrlen(st);
    printf("The length of this string is %d", l);
    return 0;
}
```

## Problem 4
Write a function slice() to slice a string. It should change the original string such that it is now the sliced string. Take ‘m’ and ‘n’ as the start and ending position for slice.

**Solution:**
```c
#include <stdio.h>

void slice(char *st, int m, int n) {
    int i = 0;
    while ((m + i) < n) {
        st[i] = st[i + m];
        i++;
    }
    st[i] = '\0';
}

int main() {
    char st[] = "HarryBhai";
    slice(st, 1, 6);
    printf("%s", st);
    return 0;
}
```

## Problem 6
Write a program to encrypt a string by adding 1 to the ascii value of its characters.

**Solution:**
```c
#include <stdio.h>

void encrypt(char *c) {
    char *ptr = c;
    while (*ptr != '\0') {
        *ptr = *ptr + 1;
        ptr++;
    }
}

int main() {
    char c[] = "come to this room";
    encrypt(c);
    printf("Encrypted string is: %s", c);
    return 0;
}
```

## Problem 7
Write a program to decrypt the string encrypted using encrypt function in problem 6.

**Solution:**
```c
#include <stdio.h>

void decrypt(char *c) {
    char *ptr = c;
    while (*ptr != '\0') {
        *ptr = *ptr - 1;
        ptr++;
    }
}

int main() {
    char c[] = "dpnf!up!uijt!sppn";
    decrypt(c);
    printf("Decrypted string is: %s", c);
    return 0;
}
```

## Problem 8
Write a program to count the occurrence of a given character in a string.

**Solution:**
```c
#include <stdio.h>

int occurrence(char st[], char c) {
    char *ptr = st;
    int count = 0;
    while (*ptr != '\0') {
        if (*ptr == c) {
            count++;
        }
        ptr++;
    }
    return count;
}

int main() {
    char st[] = "Harry";
    int count = occurrence(st, 'r');
    printf("Occurrences = %d", count);
    return 0;
}
```
