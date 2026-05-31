---
tags:
  - python-programming
  - dictionary
  - sets
---

# Dictionary & Sets

Dictionary is a collection of keys-value pairs.

*Syntax:*
```python
a = {
    "key": "value",
    "harry": "code",
    "marks": "100",
    "list": [1, 2, 9]
}
print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]
```

## Properties of Python Dictionaries
1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys.

## Dictionary Methods
Consider the following dictionary:
```python
a = {
    "name": "harry",
    "from": "india",
    "marks": [92, 98, 96]
}
```
- `a.items()`: Returns a list of (key,value)tuples.
- `a.keys()`: Returns a list containing dictionary's keys.
- `a.update({"friends": []})`: Updates the dictionary with supplied key-value pairs.
- `a.get("name")`: Returns the value of the specified keys (and value is returned eg."harry" is returned here).

## Sets in Python
Set is a collection of non-repetitive elements.

```python
s = set() # empty set
s.add(1)
s.add(2) # set becomes {1, 2}
```

## Properties of Sets
1. Sets are unordered => Element’s order doesn’t matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.

## Operations on Sets
Consider the following set `s = {1, 8, 2, 3}`:
- `len(s)`: Returns 4, the length of the set
- `s.remove(8)`: Updates the set s and removes 8 from s.
- `s.pop()`: Removes an arbitrary element from the set and return the element removed.
- `s.clear()`: empties the set s.
- `s.union({8, 11})`: Returns a new set with all items from both sets.
- `s.intersection({8, 11})`: Return a set which contains only item in both sets.

## Practice Set
- [ ] 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
- [ ] 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
- [ ] 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
- [ ] 4. What will be the length of following set s:
```python
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
```
- [ ] 5. `s = {}` What is the type of 's'?
- [ ] 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
- [ ] 7. If the names of 2 friends are same; what will happen to the program in problem 6?
- [ ] 8. If languages of two friends are same; what will happen to the program in problem 6?
- [ ] 9. Can you change the values inside a list which is contained in set S?
```python
s = {8, 7, 12, "Harry", [1,2]}
```