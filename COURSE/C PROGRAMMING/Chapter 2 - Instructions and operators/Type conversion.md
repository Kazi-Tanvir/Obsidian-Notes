# Type conversion
An Arithmetic operation between
* `int` and `int` -> `int`
* `int` and `float` -> `float`
* `float` and `float` -> `float`

**Example:**
* `5/2` becomes 2 as both the operands are int
* `5.0/2` becomes 2.5 as one of the operands is float
* `2/5` becomes 0 as both the operands are int

**Note:**
In programming, type compatibility is crucial. For `int a = 3.5;`, the float 3.5 is demoted to 3, losing the fractional part. Conversely, for `float a = 8;`, the integer 8 is promoted to 8.0.

```c
int a = 3.5; // 3.5 (float) will be demoted to 3 (int)
float a = 8; // a will store 8.0 (promotion to float)
```
