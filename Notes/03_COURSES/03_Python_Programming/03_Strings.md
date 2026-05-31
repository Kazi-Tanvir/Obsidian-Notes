---
tags:
  - python-programming
  - strings
  - slicing
---

# Strings

String is a data type in python.
String is a sequence of characters enclosed in quotes.

We can primarily write a string in these three ways:
```python
a = 'harry'     # Single quoted string
b = "harry"     # Double quoted string
c = '''harry''' # Triple quoted string
```

## String Slicing
A string in python can be sliced for getting a part of the strings.
The index in a string starts from 0 to (length -1) in Python. In order to slice a string, we use the following syntax:

```python
# sl = name[ind_start: ind_end]
# first index included, last index is not included
```
Example: `sl[0:3]` returns "har" characters from 0 to 3.

**Negative Indices:** Negative indices can also be used. -1 corresponds to the (length - 1) index, -2 to (length - 2).

## Slicing with Skip Value
We can provide a skip value as a part of our slice like this:
```python
word = "amazing"
word[1:6:2] # "mzn"
```

## String Functions
Some of the commonly used functions to perform operations on or manipulate strings are as follows. Let us assume there is a string `str = 'harry'`:

1. **len() function:** This function returns the length of the strings.
```python
print(len(str)) # Output: 5
```
2. **endswith("rry"):** This function tells whether the variable string ends with the string "rry" or not. If string is "harry", it returns true.
```python
print(str.endswith("rry")) # Output: True
```
3. **count("c"):** counts the total number of occurrences of any character.
```python
print(str.count("r")) # Output: 2
```
4. **capitalize():** Capitalizes the first character of a given string.
```python
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Harry"
```
5. **find(word):** This function finds a word and returns the index of first occurrence of that word in the string.
```python
index = str.find("rr")
print(index) # Output: 2
```
6. **replace(old, new):** This function replaces the old word with new word in the entire string.
```python
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"
```

## Escape Sequence Characters
Sequence of characters after backslash `\` -> Escape Sequence characters
Escape Sequence characters comprise of more than one character but represent one character when used within the strings.
Example: `\n` (newline), `\t` (Tab), `\'` (Single quote), `\\` (backslash) etc.

## Practice Set
- [ ] 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
- [ ] 2. Write a program to fill in a letter template given below with name and date.
```python
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
```
- [ ] 3. Write a program to detect double space in a string.
- [ ] 4. Replace the double space from problem 3 with single spaces.
- [ ] 5. Write a program to format the following letter using escape sequence characters.
```python
letter = "Dear Harry, this python course is nice. Thanks!"
```