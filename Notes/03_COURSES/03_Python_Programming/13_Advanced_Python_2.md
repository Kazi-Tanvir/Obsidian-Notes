---
tags:
  - python-programming
  - virtual-environment
  - lambda
  - map-filter-reduce
---

# Advanced Python 2

## Virtual Environment
An environment which is same as the system interpreter but is isolated from the other Python environments on the system.

**Installation:**
```bash
pip install virtualenv # Install the package
virtualenv myprojectenv # Creates a new venv
```

## pip freeze command
`pip freeze` returns all the package installed in a given python environment along with the versions.
```bash
pip freeze > requirements.txt
```
The above command creates a file named `requirements.txt` in the same directory containing the output of `pip freeze`. We can distribute this file to other users, and they can recreate the same environment using:
```bash
pip install -r requirements.txt
```

## Lambda functions
Function created using an expression using `lambda` keyword.

*Syntax:*
```python
# lambda arguments: expressions
square = lambda x: x*x
square(6) # returns 36
```

## join method (strings)
Creates a string from iterable objects.
```python
l = ["apple", "mango", "banana"]
result = ", and, ".join(l)
print(result) # "apple, and, mango, and, banana"
```

## format method (strings)
Formats the values inside the string into a desired output.
```python
"{} is a good {}".format("harry", "boy")
```

## Map, Filter & Reduce
- **Map:** Map applies a function to all the items in an input_list.
```python
map(function, input_list)
```
- **Filter:** Filter creates a list of items for which the function returns true.
```python
list(filter(function, input_list))
```
- **Reduce:** Reduce applies a rolling computation to sequential pair of elements.
```python
from functools import reduce
val = reduce(function, list1)
```

## Practice Set
- [ ] 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?
- [ ] 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
“The name of the student is Harry, his marks are 72 and phone number is 99999888”
- [ ] 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
- [ ] 4. Write a program to filter a list of numbers which are divisible by 5.
- [ ] 5. Write a program to find the maximum of the numbers in a list using the reduce function.
- [ ] 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.
- [ ] 7. Explore the ‘Flask’ module and create a web server using Flask & Python.