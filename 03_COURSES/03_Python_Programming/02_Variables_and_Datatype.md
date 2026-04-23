---
tags:
  - python-programming
  - variables
  - datatypes
  - operators
---

# Variables and Datatype

একটি ভেরিয়েবল হলো প্রোগ্রামের মেমরি লোকেশনের একটি নাম। উদাহরণস্বরূপ:

```python
a= 30       # variables = container to store a value.
b= "harry"  # keywords = reserved words in python
c= 71.22    # identifiers = class/function/variable name
```

## Data Types
পাইথনে মূলত নিচের ডেটা টাইপগুলো ব্যবহার করা হয়:
1. Integers
2. Floating point numbers
3. Strings
4. Booleans
5. None

পাইথন একটি চমৎকার ল্যাঙ্গুয়েজ যা নিজে থেকেই আমাদের জন্য ডেটা টাইপ আইডেন্টিফাই করে নেয়।

```python
a= 71       # identifies a as class <int>
b=88.44     # identifies b as class <float>
name= "harry" # identifies name as class <str>
```

## Rules for choosing an identifier
- একটি ভেরিয়েবলের নামে অ্যালফাবেট, ডিজিট এবং আন্ডারস্কোর থাকতে পারে।
- ভেরিয়েবলের নাম শুধুমাত্র অ্যালফাবেট এবং আন্ডারস্কোর দিয়ে শুরু হতে পারে।
- ভেরিয়েবলের নাম ডিজিট দিয়ে শুরু হতে পারবে না।
- ভেরিয়েবলের নামের ভেতরে কোনো হোয়াইট স্পেস (space) ব্যবহার করা যাবে না।

Examples of a few variable names are: `harry`, `one8`, `seven`, `_seven` etc.

## Operators in Python
পাইথনে ব্যবহৃত কিছু সাধারণ অপারেটর হলো:
1. **Arithmetic operators:** `+`, `-`, `*`, `/` etc.
2. **Assignment operators:** `=`, `+=`, `-=` etc.
3. **Comparison operators:** `==`, `>`, `>=`, `<`, `!=` etc.
4. **Logical operators:** `and`, `or`, `not`.

## type() function and Typecasting
`type()` ফাংশনটি পাইথনে কোনো একটি ভেরিয়েবলের ডেটা টাইপ বের করতে ব্যবহৃত হয়।

```python
a = 31
type(a) # class <int>

b = "31"
type(b) # class <str>
```

একটি ডেটা টাইপকে অন্য ডেটা টাইপে কনভার্ট করা যায় (যদি সম্ভব হয়)।
```python
str(31)   #=>"31"   integer to string conversion
int("32") #=> 32    string to integer conversion
float(32) #=> 32.0  integer to float conversion
```
Here `"31"` is a string literal and `31` a numeric literal.

## input() Function
এই ফাংশনটি ইউজারকে কীবোর্ড থেকে ইনপুট নিতে সাহায্য করে এবং ইনপুটটি সব সময় স্ট্রিং হিসেবে গ্রহণ করে।

```python
A = input("enter name") # if a is "harry", the user entered harry
```
এটি মনে রাখা গুরুত্বপূর্ণ যে, ইনপুটের আউটপুট সব সময় একটি স্ট্রিং হয় (এমনকি ইউজার যদি নাম্বারও ইনপুট দেয়)।

## Practice Set
- [ ] 1. Write a python program to add two numbers.
- [ ] 2. Write a python program to find remainder when a number is divided by z.
- [ ] 3. Check the type of variable assigned using input () function.
- [ ] 4. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80
- [ ] 5. Write a python program to find an average of two numbers entered by the user.
- [ ] 6. Write a python program to calculate the square of a number entered by the user.
