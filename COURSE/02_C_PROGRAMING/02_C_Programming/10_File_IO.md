---
tags: [c-programming, file-io, persistence]
---

# 10 File I/O

Files are used to persist data even after the program terminates.

## File Pointer
A "FILE" structure is needed to open a file.
```c
FILE *ptr;
ptr = fopen("filename.txt", "mode");
```

## File Opening Modes
- `"r"`: Open for reading.
- `"rb"`: Open for reading in binary.
- `"w"`: Open for writing (overwrites if file exists).
- `"wb"`: Open for writing in binary.
- `"a"`: Open for append (creates if it doesn't exist).

## Reading & Writing
- `fscanf(ptr, "%d", &num);`: Read from file.
- `fprintf(ptr, "%d", num);`: Write to file.
- `fgetc(ptr)`: Read a single character.
- `fputc('c', ptr)`: Write a single character.

### Closing a File
It is crucial to close the file to free associated resources.
```c
fclose(ptr);
```

## EOF (End of File)
`fgetc` returns `EOF` when all characters from a file have been read.

## Practice Set
- [ ] Write a program to read three integers from a file.
- [ ] Write a program to generate a multiplication table of a given number in text format.
- [ ] Write a program to read a text file character by character and write its content twice into a separate file.
- [ ] Take name and salary of two employees as input from the user and write them to a text file.
- [ ] Write a program to modify a file containing an integer to double its value.
