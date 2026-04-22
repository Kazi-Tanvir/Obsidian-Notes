# File pointer
A “FILE” is a structure which needs to be created for opening the file.
A file pointer is a pointer to this structure of the file.
(FILE pointer is needed for communication between the file and the program).

A FILE pointer can be created as follows:
```c
FILE *ptr;
ptr = fopen("filename.ext", "mode");
```
