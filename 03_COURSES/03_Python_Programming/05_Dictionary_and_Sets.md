---
tags:
  - python-programming
  - dictionary
  - sets
---

# Dictionary & Sets

ডিকশনারি হলো 'কী-ভ্যালু' (keys-value) পেয়ারের একটি সংগ্রহ।

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
1. এটি অবিন্যস্ত (unordered)।
2. এটি পরিবর্তনযোগ্য (mutable)।
3. এটি ইনডেক্সড (indexed)।
4. এতে ডুপ্লিকেট কী (keys) থাকতে পারে না।

## Dictionary Methods
ধরি একটি ডিকশনারি হলো:
```python
a = {
    "name": "harry",
    "from": "india",
    "marks": [92, 98, 96]
}
```
- `a.items()`: ডিকশনারির (key, value) টাপলগুলোর একটি লিস্ট রিটার্ন করে।
- `a.keys()`: ডিকশনারির সবগুলো কী (keys) এর একটি লিস্ট রিটার্ন করে।
- `a.update({"friends": []})`: দেওয়া 'কী-ভ্যালু' পেয়ার দিয়ে ডিকশনারিটিকে আপডেট করে।
- `a.get("name")`: নির্দিষ্ট কী (যেমন "name") এর ভ্যালু রিটার্ন করে।

## Sets in Python
সেট হলো এমন উপাদানগুলোর সংগ্রহ যেখানে কোনো উপাদানের পুনরাবৃত্তি (repetition) থাকে না।

```python
s = set() # empty set
s.add(1)
s.add(2) # set becomes {1, 2}
```

## Properties of Sets
1. সেটের উপাদানগুলো অবিন্যস্ত থাকে, তাই উপাদানের ক্রম (order) কোনো বিষয় না।
2. সেট আনইনডেক্সড, অর্থাৎ ইনডেক্স দিয়ে উপাদান অ্যাক্সেস করা যায় না।
3. সেটের উপাদানগুলো পরিবর্তন করার কোনো উপায় নেই।
4. সেটে ডুপ্লিকেট ভ্যালু থাকতে পারে না।

## Operations on Sets
ধরি একটি সেট `s = {1, 8, 2, 3}`:
- `len(s)`: সেটের দৈর্ঘ্য অর্থাৎ উপাদানের সংখ্যা রিটার্ন করে।
- `s.remove(8)`: সেট থেকে 8 কে রিমুভ করে।
- `s.pop()`: সেট থেকে যেকোনো একটি উপাদান রিমুভ করে এবং সেটি রিটার্ন করে।
- `s.clear()`: সেটটিকে ফাঁকা করে দেয়।
- `s.union({8, 11})`: দুটি সেটের সমস্ত উপাদান নিয়ে একটি নতুন সেট রিটার্ন করে।
- `s.intersection({8, 11})`: দুটি সেটের মধ্যে যে উপাদানগুলো কমন (common) শুধু সেগুলো নিয়ে একটি নতুন সেট রিটার্ন করে।

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
