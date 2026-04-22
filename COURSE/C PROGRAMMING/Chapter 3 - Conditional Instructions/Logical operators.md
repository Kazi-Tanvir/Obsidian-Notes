# Logical operators
`&&`, `||` and `!`, are three logical operators in C. These are read as “AND”, “OR” and “NOT”.
They are used to provide logic to our C programs.

### Usage of Logical Operators:
1. `&&` (AND) -> is true when both the conditions are true
   - “1 and 0” is evaluated as false.
   - “0 and 0” is evaluated as false.
   - “1 and 1” is evaluated as true.
2. `||` (OR) -> is true when at least one of the conditions is true. (1 or 0 -> 1) (1 or 1 -> 1)
3. `!` (NOT) -> returns true if given false and false if given true
   - `!(3==3)` -> evaluates to false
   - `!(3>30)` -> evaluates to true.

As the number of conditions increases, the level of indentation increases. This reduces readability. Logical operators come to rescue in such cases.
