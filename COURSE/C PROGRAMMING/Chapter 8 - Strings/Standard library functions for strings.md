# Standard library functions for strings
C provides a set of standard library functions for string manipulation.
These functions are declared under `<string.h>` header file.

### strlen()
This function is used to count the number of characters in the string excluding the null ('\0') characters.
```c
int length = strlen(st);
```

### strcpy()
This function is used to copy the content of second string into first string passed to it.
```c
char source[] = "harry";
char target[30];
strcpy(target, source); // target now contains "harry"
```

### strcat()
This function is used to concatenate two strings.
```c
char s1[12] = "hello";
char s2[] = "harry";
strcat(s1, s2); // s1 now contains "helloharry"
```

### strcmp()
This function is used to compare two strings. It returns 0 if the strings are equal, a negative value if the first string's mismatching character's ASCII value is less than the second string's corresponding mismatching character, and a positive value otherwise.
```c
strcmp("far", "joke"); // Negative value
strcmp("joke", "far"); // Positive value
```
