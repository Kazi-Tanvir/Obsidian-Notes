# Arithmetic instructions
Arithmetic instructions perform mathematical operations.

Here are some of the commonly used operators in C language:
* `+` (Addition)
* `-` (Subtraction)
* `*` (Multiplication)
* `/` (Division)
* `%` (Modulus)

**Note:**
1. Operands can be int/float etc. `+ - * /` are arithmetic operators.
```c
int b = 2, c = 3;
int z; z = b*c; // legal
// int z; b*c = z; // illegal (not allowed)
```
2. `%` is the modular division operator
   - `%` -> returns the remainder
   - `%` -> cannot be applied on float
   - `%` -> sign is same as of numerator (-5%2=-1)
3. No operator is assumed to be present.
```c
// int i = ab // invalid
int i = a * b; // valid
```
4. There is no operator to perform exponentiation in C however we can use `pow(x,y)` from `<math.h>`.
