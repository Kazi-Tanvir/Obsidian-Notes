# Reading a file
A file can be opened for reading as follows:

```c
FILE *ptr;
ptr = fopen("harry.txt", "r");
int num;
```
Let us assume that "harry.txt" contains an integer we can read that integer using:
```c
fscanf(ptr, "%d", &num); // fscanf is file counterpart of scanf
```
This will read an integer from file in num variables.
