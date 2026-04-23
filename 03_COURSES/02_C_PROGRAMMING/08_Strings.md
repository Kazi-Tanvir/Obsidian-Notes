---
tags: [c-programming, strings, character-arrays]
---

# 08 Strings

A string is a 1-D character array terminated by a null character `\0`.

## Initialization
```c
char s[] = {'H', 'A', 'R', 'R', 'Y', '\0'};
char s[] = "HARRY"; // C adds \0 automatically
```

## Printing & Input
- `printf("%s", st);` prints the entire string.
- `scanf("%s", st);` takes input but cannot read multi-word strings (stops at space).
- `gets(st);` used to receive multi-word strings.
- `puts(st);` outputs a string and moves the cursor to the next line.

## Declaring Strings using Pointers
```c
char *ptr = "harry";
```
**Note**: Strings defined using pointers can be reinitialized, while those defined as arrays cannot.

## Standard Library Functions (`<string.h>`)
- `strlen(st)`: Counts the number of characters (excluding `\0`).
- `strcpy(target, source)`: Copies content of source to target.
- `strcat(s1, s2)`: Concatenates `s2` to the end of `s1`.
- `strcmp(s1, s2)`: Compares two strings. Returns `0` if equal.

## Practice Set
- [ ] Which of the following is used to read a multi-word string? (`gets`, `puts`, `printf`, `scanf`).
- [ ] Write a program to take string input using `%c` and `%s` and confirm they are equal.
- [ ] Write your own version of the `strlen` function.
- [ ] Write a function `slice()` to slice a string between index `m` and `n`.
- [ ] Write your own version of the `strcpy` function.
- [ ] Write a program to encrypt a string by adding 1 to the ASCII value of its characters.
- [ ] Write a program to decrypt the string encrypted in the previous problem.
- [ ] Write a program to count the occurrence of a given character in a string.
- [ ] Write a program to check whether a given character is present in a string or not.
