# Closing the file
It is very important to close the file after read or write. This is achieved using fclose as follows:

```c
fclose(ptr);
```
This will tell the compiler that we are done working with this file and the associated resources could be freed.
