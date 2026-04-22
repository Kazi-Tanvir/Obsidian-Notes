# The continue statement in c
The ‘continue’ statement is used to immediately move to the next iteration of the loop.
The control is taken to the next iteration thus skipping everything below “continue” inside the loop for that iteration.

```c
int i = 0;
while (i < 10) {
    if (i == 5) {
        i++;
        continue; // skips the rest of the loop body for i == 5
    }
    printf("%d\n", i);
    i++;
}
```

**Notes:**
1. ‘break’ statement completely exits the loop.
2. ‘continue’ statement skips the particular iteration of the loop.
