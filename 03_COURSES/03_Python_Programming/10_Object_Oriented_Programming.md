---
tags:
  - python-programming
  - oop
  - class
  - object
---

# Object Oriented Programming

প্রোগ্রামিংয়ে কোনো সমস্যার সমাধান অবজেক্ট (object) তৈরি করে করার পদ্ধতি বেশ জনপ্রিয়। একে অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং বা OOP বলা হয়। এর মূল উদ্দেশ্য হলো রিইউজেবল কোড (DRY Principle - Don't Repeat Yourself) ব্যবহার করা।

## Class
ক্লাস (Class) হলো অবজেক্ট তৈরি করার জন্য একটি ব্লুপ্রিন্ট বা টেমপ্লেট।

*Syntax:*
```python
class Employee: # Class name is written in pascal case
    # Methods & Variables
    pass
```

## Object
অবজেক্ট হলো একটি ক্লাসের ইন্সট্যান্স (instantiation)। ক্লাস ডিফাইন করার পর মেমরি অ্যালোকেশন হয় না, মেমরি অ্যালোকেশন হয় অবজেক্ট তৈরি হওয়ার পর।

একটি নির্দিষ্ট ক্লাসের অবজেক্ট ব্যবহার করে ইউজারের কাছে ভেতরের ইমপ্লিমেন্টেশন ডিটেইলস গোপন রেখেই মেথডগুলো কল করা যায়। একে অ্যাবস্ট্রাকশন এবং এনক্যাপসুলেশন (Abstractions & Encapsulation) বলে।

## Modelling a problem in OOPs
আমরা কোনো সমস্যাকে এভাবে ভাগ করতে পারি:
- **Noun** -> Class -> Employee
- **Adjective** -> Attributes -> name, age, salary
- **Verbs** -> Methods -> getSalary(), increment()

## Class Attributes
যে অ্যাট্রিবিউটটি কোনো নির্দিষ্ট অবজেক্টের না হয়ে পুরো ক্লাসের হয়, তাকে ক্লাস অ্যাট্রিবিউট বলে।

*Example:*
```python
class Employee:
    company = "Google" # Specific to Each Class

harry = Employee() # Object Instantiation
print(harry.company)
Employee.company = "YouTube" # Changing Class Attribute
```

## Instance attributes
যে অ্যাট্রিবিউটটি অবজেক্ট বা ইন্সট্যান্সের সাথে সম্পর্কিত, তাকে ইন্সট্যান্স অ্যাট্রিবিউট বলে।

```python
harry.name = "harry"
harry.salary = "30k" # Adding instance attribute
```
*Note:* যখন অ্যাসাইনমেন্ট বা ডেটা রিট্রিভ করা হয়, তখন ক্লাস অ্যাট্রিবিউটের চেয়ে ইন্সট্যান্স অ্যাট্রিবিউট বেশি প্রাধান্য পায়।

## self parameter
`self` বলতে ক্লাসের নির্দিষ্ট ইন্সট্যান্সকে (অবজেক্ট) বোঝায়। যখন অবজেক্ট থেকে কোনো ফাংশন কল করা হয়, তখন এটি স্বয়ংক্রিয়ভাবে পাস হয়ে যায়।

```python
harry.getSalary() # here self is harry
# is equivalent to Employee.getSalary(harry)
```

## static method
মাঝে মাঝে এমন ফাংশন দরকার হতে পারে যার জন্য `self` প্যারামিটারের প্রয়োজন নেই। তখন আমরা স্ট্যাটিক মেথড ব্যবহার করতে পারি।

```python
@staticmethod # decorator to mark greet as a static method
def greet():
    print("Hello user")
```

## `__init__()` constructor
`__init__()` হলো একটি স্পেশাল মেথড, যা অবজেক্ট তৈরি হওয়ার সাথে সাথেই স্বয়ংক্রিয়ভাবে রান হয়। একে কনস্ট্রাক্টর (constructor) বলা হয়। এটি `self` আর্গুমেন্ট গ্রহণ করে এবং আরও অন্যান্য আর্গুমেন্টও নিতে পারে।

*For Example:*
```python
class Employee:
    def __init__(self, name):
        self.name = name
    def getSalary(self):
        pass

harry = Employee("Harry")
```

## Practice Set
- [ ] 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
- [ ] 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
- [ ] 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
- [ ] 4. Add a static method in problem 2, to greet the user with hello.
- [ ] 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
- [ ] 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
