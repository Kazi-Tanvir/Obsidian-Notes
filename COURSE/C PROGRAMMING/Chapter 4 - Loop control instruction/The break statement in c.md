# The break statement in c
The ‘break’ statement is used to exit the loop irrespective of whether the condition is true or false.
Whenever a “break” is encountered inside the loop, the control is sent outside the loop

```c
for (i=0; i<1000; i++){
    printf("%d\n",i);
    if (i==5){
        break;
    }
}
```
