---
tags:
  - python-programming
  - lists
  - tuples
---

# Lists and Tuples

পাইথনের লিস্ট হলো এক ধরনের কন্টেইনার যেখানে যেকোনো ডেটা টাইপের ভ্যালু স্টোর করা যায়।
```python
friends = ["apple", "akash", "rohan", 7, False]
```

## List Indexing
একটি লিস্টকে স্ট্রিংয়ের মতোই ইনডেক্স করা যায়।
```python
l1 = [7, 9, "harry"]
l1[0] # 7
l1[1] # 9
l1[70] # error
l1[0:2] # [7, 9] (list slicing)
```

## List Methods
নিচের লিস্টটি বিবেচনা করুন: `l1 = [1, 8, 7, 2, 21, 15]`
- `l1.sort()`: এটি লিস্টটিকে সর্ট বা ক্রমানুসারে সাজিয়ে দেয় `[1, 2, 7, 8, 15, 21]`।
- `l1.reverse()`: এটি লিস্টটিকে উল্টে দেয় `[15, 21, 2, 7, 8, 1]`।
- `l1.append(8)`: এটি লিস্টের শেষে 8 যুক্ত করে।
- `l1.insert(3, 8)`: এটি 3 নম্বর ইনডেক্সে 8 যুক্ত করবে।
- `l1.pop(2)`: এটি 2 নম্বর ইনডেক্সের উপাদানটি ডিলিট করবে এবং এর ভ্যালু রিটার্ন করবে।
- `l1.remove(21)`: এটি লিস্ট থেকে 21 কে রিমুভ করবে।

## Tuples in Python
টাপল হলো পাইথনের একটি অপরিবর্তনযোগ্য (immutable) ডেটা টাইপ। অর্থাৎ একবার তৈরি করলে একে আর পরিবর্তন করা যায় না।
```python
a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1, 7, 2) # tuple with more than one element
```

## Tuple Methods
ধরি একটি টাপল `a = (1, 7, 2)`:
- `a.count(1)`: এটি টাপলে 1 কতবার আছে তা রিটার্ন করবে।
- `a.index(1)`: এটি টাপলে 1 এর প্রথম উপস্থিতির ইনডেক্স রিটার্ন করবে।

## Practice Set
- [ ] 1. Write a program to store seven fruits in a list entered by the user.
- [ ] 2. Write a program to accept marks of 6 students and display them in a sorted manner.
- [ ] 3. Check that a tuple type cannot be changed in python.
- [ ] 4. Write a program to sum a list with 4 numbers.
- [ ] 5. Write a program to count the number of zeros in the following tuple:
```python
a = (7, 0, 8, 0, 0, 9)
```
