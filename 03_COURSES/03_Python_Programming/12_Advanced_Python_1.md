---
tags:
  - python-programming
  - advanced
  - exception-handling
---

# Advanced Python 1

## Newly added features in python
পাইথন প্রোগ্রামিং ল্যাঙ্গুয়েজে নতুন বেশ কিছু ফিচার যুক্ত হয়েছে।

### Walrus Operator
ওয়ালরাস অপারেটর (`:=`) পাইথন ৩.৮ এ যুক্ত করা হয়েছে। এটি একটি এক্সপ্রেশনের ভেতরে ভেরিয়েবলে ভ্যালু অ্যাসাইন করতে ব্যবহৃত হয়। একে অফিশিয়ালি "assignment expression" বলা হয়।

```python
# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
```

### Types Definitions in Python
টাইপ হিন্ট (Type hints) অ্যাড করতে ফাংশনের রিটার্ন টাইপের জন্য `->` সিনট্যাক্স এবং ভেরিয়েবলের জন্য কোলন `:` ব্যবহার করা হয়।
```python
# Variable type hint
age: int = 25

# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"
```

### Advanced Type Hints
পাইথনের `typing` মডিউল আরও অ্যাডভান্সড টাইপ হিন্ট যেমন List, Tuple, Dict এবং Union প্রদান করে।
```python
from typing import List, Tuple, Dict, Union

numbers: List[int] = [1, 2, 3, 4, 5]
identifier: Union[int, str] = "ID123"
```

### Match Case
পাইথন ৩.১০ এ `match` স্টেটমেন্ট যুক্ত করা হয়, যা অন্যান্য প্রোগ্রামিং ভাষার `switch` স্টেটমেন্টের মতোই কাজ করে।
```python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown status"
```

### Dictionary Merge & Update Operators
নতুন অপারেটর `|` এবং `|=` ডিকশনারি মার্জ (merge) ও আপডেট করার সুযোগ দেয়।
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
```

## Exception handling in Python
যখন কোনো প্রোগ্রামে ভুল (error) ঘটে, তখন পাইথন ডিফল্টভাবে কিছু এরর থ্রো (throw) করে।
ট্রাই-অ্যাক্সেপ্ট (`try-except`) স্টেটমেন্ট ব্যবহার করে এক্সসেপশন হ্যান্ডেল করা যায়। এতে প্রোগ্রাম ক্র্যাশ না হয়ে স্বাভাবিকভাবে চলতে পারে।

```python
try:
    # Code which might throw exception
except Exception as e:
    print(e)
```
আমরা সুনির্দিষ্ট এক্সসেপশনও ক্যাচ করতে পারি, যেমন `ZeroDivisionError` বা `TypeError`।

### Raising Exceptions
আমরা চাইলে `raise` কিওয়ার্ড ব্যবহার করে কাস্টম এক্সসেপশন তৈরি করতে পারি।

### try with else clause
`try` ব্লকটি সফলভাবে এক্সিকিউট হলে (কোনো এরর ছাড়া), তবেই `else` ব্লকের কোড এক্সিকিউট হবে।

### try with finally
`finally` ব্লকের কোড সব সময় এক্সিকিউট হবে, এরর আসুক বা না আসুক।

## `__name__ == '__main__'` in python
`__name__` ইভালুয়েট করে মডিউলের নাম নির্ধারণ করে। যদি প্রোগ্রামটি সরাসরি ওই ফাইল থেকে রান করা হয়, তবে `__name__` এর ভ্যালু `__main__` হয়। এটি চেক করতে ব্যবহৃত হয় যে মডিউলটি সরাসরি রান হচ্ছে নাকি অন্য ফাইলে ইম্পোর্ট করা হয়েছে।

## The global keyword
বর্তমান স্কোপের বাইরের গ্লোবাল ভেরিয়েবল মডিফাই করতে `global` কিওয়ার্ড ব্যবহৃত হয়।

## enumerate function in python
`enumerate` ফাংশন যেকোনো ইটারেবলের (যেমন লিস্ট) উপাদানগুলোর সাথে একটি কাউন্টার (ইনডেক্স) যুক্ত করে রিটার্ন করে।
```python
for i, item in enumerate(list1):
    print(i, item)
```

## List comprehensions
বিদ্যমান লিস্টের ওপর ভিত্তি করে সুন্দর উপায়ে নতুন লিস্ট তৈরি করার পদ্ধতি হলো লিস্ট কম্প্রিহেনশন।
```python
list1 = [1, 7, 12, 11, 22]
list2 = [item for item in list1 if item > 8]
```

## Practice Set
- [ ] 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.
- [ ] 2. Write a program to print third, fifth and seventh element from a list using enumerate function.
- [ ] 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.
- [ ] 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
- [ ] 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
