# Operator precedence in c
Have a look at the below statement:
`3*x - 8*y` is `(3x)-(8y)` or `3(x-8y)`?

In C language simple mathematical rules like BODMAS, no longer apply. The answer is provided by operator precedence & associativity.

### Operator Precedence
1st: `* / %`
2nd: `+ -`
3rd: `=`
Operators of higher priority are evaluated first in the absence of parenthesis.

### Operator Associativity
When operators of equal priority are present in an expression, the tie is taken care of by associativity.
`x * y / z` -> `(x * y) / z`
`x / y * z` -> `(x / y) * z`
`* , /` follows left to right associativity.

*Pro Tip: Always use parenthesis in case of confusion*
