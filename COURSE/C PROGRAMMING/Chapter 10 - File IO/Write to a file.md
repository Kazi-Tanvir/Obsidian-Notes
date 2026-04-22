# Write to a file
We can write to a file in a very similar manner like we read the file

```c
FILE *fptr;
fptr = fopen("harry.txt", "w");
int num = 432;
fprintf(fptr, "%d", num);
fclose(fptr);
```
