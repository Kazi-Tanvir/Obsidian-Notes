# Switch case control instruction
switch-case is used when we have to make a choice between number of alternatives for a given variable.

```c
switch (integer expression)
{
case c1:
    // code;
case c2:
    // code;
case c3:
    // code;
default:
    // code;
}
```

The value of integer-expression is matched against c1, c2, c3... If it matches any of these cases, that case along with all subsequent “case” and “default” statements are executed.

**Some Important Notes:**
* We can use switch-case statements even by writing cases in any order of our choice.
* char values are allowed as they can be easily evaluated to an integer.
* A switch can occur within another but in practice this is rarely done.
