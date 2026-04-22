# Taking string input from the user
We can use %s with scanf to take string input from the user:

```c
char st[50];
scanf ("%s", st);
```
scanf automatically adds a null character when the enter key is pressed.

**Note:**
1. The string should be short enough to fit into the array.
2. scanf cannot be used to input multi-word strings with spaces.
