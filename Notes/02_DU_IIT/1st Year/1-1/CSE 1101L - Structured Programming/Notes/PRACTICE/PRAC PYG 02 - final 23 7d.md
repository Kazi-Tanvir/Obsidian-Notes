---
title: "PRAC PYG 02 - final 23 7d"
aliases:
  - final 23 7d
  - 02_Final_23_7d
tags:
  - type/practice
  - c/file-io
  - c/encryption
  - c/cli-args
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "PRACTICE/PYG/02_Final_23_7d.c"
up: "[[PRAC - Index]]"
related:
  - "[[CLASS 27 - binary encryption]]"
  - "[[CLASS 28 - shift encryption]]"
  - "[[CLASS 20 - cmd arg]]"
created: 2026-10-29
status: draft
---
# PRAC PYG 02 - final 23 7d

> [!abstract] Summary
> Solves University Final Exam 2023 Question 7(d): reads stored encrypted credentials from a file specified via command-line arguments and validates user login credentials using character permutation.

**Source:** `PRACTICE/PYG/02_Final_23_7d.c`

## Problem
Accept a credential filename as a command-line argument (`argv[1]`), read the stored user ID and encrypted password, prompt the user for interactive login credentials, encrypt the input password via index swapping ($0 \leftrightarrow 2$, $1 \leftrightarrow 3$), and verify credentials.

## Concepts used
- **Command-Line Arguments (`argc`, `argv`):** Accessing target credential files passed on the shell invocation line.
- **Symmetric Permutation Encryption:** Swapping characters: index 0 with 2, and index 1 with 3.
- **File Ingestion (`fscanf`):** Reading space-delimited text records from a file pointer.
- **String Authentication (`strcmp`):** Validating matching identity and encrypted password strings.

## Code
```c
#include<stdio.h>
#include<string.h>
struct{
    char id[5];
    char password[5];
}file,input;

void encryption(char pass[]){
    int temp = pass[0];
    pass[0]=pass[2];
    pass[2] = temp;

    temp = pass[1];
    pass[1] = pass[3];
    pass[3] = temp;
}

int main(int argc , char *argv[]){
    FILE *fp  =fopen(argv[1],"rb");
    if(!fp){
        printf("Error opening file!");
        return 1;
    }
    
    fscanf(fp, "%s %s", file.id, file.password);
    fclose(fp);

    printf("Enter your user name : ");
    scanf(" %[^\n]", input.id);
    printf("Enter your password : ");
    scanf(" %[^\n]", input.password);

    encryption(input.password);

    if(strcmp(file.id, input.id) == 0 && strcmp(file.password, input.password) == 0){
        printf("Login successful!");
    }else{
        printf("Login failed!");
    }
    
}
```

## How it works
1. Checks and opens `argv[1]` in read mode.
2. Reads stored ID and password into `file.id` and `file.password`.
3. Prompts user for username and plaintext password via `scanf`.
4. Calls `encryption()` on user's password, swapping letters: $0 \leftrightarrow 2$ and $1 \leftrightarrow 3$.
5. Compares ID and encrypted password: if both match, reports `Login successful!`; otherwise `Login failed!`.

## Sample run
```text
(When credentials file contains: "admin acbd")
Enter your user name : admin
Enter your password : abcd
Login successful!
```

## Gotchas
> [!warning] Fixed 5-Character Buffer Boundary
> `struct { char id[5]; char password[5]; }` allocates only 5 bytes per string (4 characters + `\0`). Input passwords longer than 4 characters cause buffer overflow.

## My notes
> [!question]- My notes

## Related
- [[CLASS 27 - binary encryption]]
- [[CLASS 28 - shift encryption]]
- [[CLASS 20 - cmd arg]]
