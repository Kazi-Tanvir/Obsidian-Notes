---
tags:
  - python-programming
  - lists
  - tuples
---

# Lists and Tuples

Python lists are containers to store a set of values of any data type.
```python
friends = ["apple", "akash", "rohan", 7, False]
```

## List Indexing
A list can be indexed just like a string.
```python
l1 = [7, 9, "harry"]
l1[0] # 7
l1[1] # 9
l1[70] # error
l1[0:2] # [7, 9] (list slicing)
```

## List Methods
Consider the following list: `l1 = [1, 8, 7, 2, 21, 15]`
- `l1.sort()`: updates the list to `[1, 2, 7, 8, 15, 21]`.
- `l1.reverse()`: updates the list to `[15, 21, 2, 7, 8, 1]`.
- `l1.append(8)`: adds 8 at the end of the list.
- `l1.insert(3, 8)`: This will add 8 at 3 index.
- `l1.pop(2)`: Will delete element at index 2 and return its value.
- `l1.remove(21)`: Will remove 21 from the list.

## Tuples in Python
A tuple is an immutable data type in python.
```python
a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1, 7, 2) # tuple with more than one element
```

## Tuple Methods
Consider the following tuple `a = (1, 7, 2)`:
- `a.count(1)`: a.count (1) will return number of times 1 occurs in a.
- `a.index(1)`: a.index (1) will return the index of first occurrence of 1 in a.

## Practice Set
- [ ] 1. Write a program to store seven fruits in a list entered by the user.
- [ ] 2. Write a program to accept marks of 6 students and display them in a sorted manner.
- [ ] 3. Check that a tuple type cannot be changed in python.
- [ ] 4. Write a program to sum a list with 4 numbers.
- [ ] 5. Write a program to count the number of zeros in the following tuple:
```python
a = (7, 0, 8, 0, 0, 9)
```