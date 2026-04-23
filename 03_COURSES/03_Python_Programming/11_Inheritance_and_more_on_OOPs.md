---
tags:
  - python-programming
  - inheritance
  - dunder-methods
---

# Inheritance & more on OOPs

ইনহেরিট্যান্স (Inheritance) হলো একটি বিদ্যমান ক্লাস থেকে নতুন একটি ক্লাস তৈরি করার পদ্ধতি।

*Syntax:*
```python
class Employee: # Base class
    # Code
    pass

class Programmer(Employee): # Derived or child class
    # Code
    pass
```
আমরা 'Programmer' অবজেক্টে 'Employee' ক্লাসের মেথড এবং অ্যাট্রিবিউটগুলো ব্যবহার করতে পারি। পাশাপাশি 'Programmer' ক্লাসে নতুন অ্যাট্রিবিউট বা মেথড যোগ করতে পারি অথবা আগেরগুলো ওভাররাইট করতে পারি।

## Types of Inheritance
- Single inheritance
- Multiple inheritance
- Multilevel inheritance

### Single Inheritance
যখন কোনো চাইল্ড ক্লাস শুধুমাত্র একটি প্যারেন্ট ক্লাস থেকে ইনহেরিট করে, তখন তাকে সিঙ্গেল ইনহেরিট্যান্স বলে।

### Multiple Inheritance
যখন কোনো চাইল্ড ক্লাস একাধিক প্যারেন্ট ক্লাস থেকে ইনহেরিট করে, তখন তাকে মাল্টিপল ইনহেরিট্যান্স বলে।

### Multilevel Inheritance
যখন কোনো চাইল্ড ক্লাস অন্য আরেকটি চাইল্ড ক্লাসের প্যারেন্ট হয়ে যায়, তখন তাকে মাল্টিলেভেল ইনহেরিট্যান্স বলে।

## super() method
`super()` মেথড ব্যবহার করে ডিরাইভড (চাইল্ড) ক্লাসের ভেতর থেকে সুপার (প্যারেন্ট) ক্লাসের মেথড অ্যাক্সেস করা যায়।
```python
super().__init__() # Calls constructor of the base class
```

## class method
ক্লাস মেথড হলো এমন একটি মেথড যা সরাসরি ক্লাসের সাথে যুক্ত থাকে, অবজেক্টের সাথে নয়। `@classmethod` ডেকোরেটর ব্যবহার করে ক্লাস মেথড তৈরি করা হয়।

*Syntax:*
```python
@classmethod
def (cls, p1, p2):
    pass
```

## @property Decorators
আমরা `@property` ডেকোরেটর ব্যবহার করে ক্লাসের মেথডকে প্রপার্টি হিসেবে অ্যাক্সেস করতে পারি। যে মেথডে `@property` ডেকোরেটর থাকে, তাকে গেটার (getter) মেথড বলা হয়।
```python
class Employee:
    @property
    def name(self):
        return self.ename
```

## @.getters and @.setters
আমরা ফাংশন এবং `@name.setter` ডেকোরেটর ব্যবহার করে সেটার (setter) ডিফাইন করতে পারি:
```python
@name.setter
def name(self, value):
    self.ename = value
```

## Operator Overloading in Python
ডান্ডার (dunder) বা ম্যাজিক মেথড ব্যবহার করে পাইথনে অপারেটর ওভারলোড করা যায়। অবজেক্টের সাথে অপারেটর ব্যবহার করলে এই মেথডগুলো স্বয়ংক্রিয়ভাবে কল হয়।
- `p1+p2` -> `p1.__add__(p2)`
- `p1-p2` -> `p1.__sub__(p2)`
- `p1*p2` -> `p1.__mul__(p2)`
- `__str__()` -> অবজেক্ট প্রিন্ট করার সময় কী আউটপুট দেখাবে তা নির্ধারণ করতে।
- `__len__()` -> `len(obj)` কল করলে কী রেজাল্ট আসবে তা নির্ধারণ করতে।

## Practice Set
- [ ] 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.
- [ ] 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
- [ ] 3. Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.
- [ ] 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
- [ ] 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
- [ ] 6. Write `__str__()` method to print the vector as follows:
`7i + 8j +10k`
Assume vector of dimension 3 for this problem.
- [ ] 7. Override the `__len__()` method on vector of problem 5 to display the dimension of the vector.
