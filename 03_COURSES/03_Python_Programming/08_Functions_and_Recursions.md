---
tags:
  - python-programming
  - functions
  - recursion
---

# Functions & Recursions

ফাংশন হলো কিছু স্টেটমেন্টের একটি গ্রুপ, যা নির্দিষ্ট কোনো কাজ সম্পন্ন করে। যখন একটি প্রোগ্রাম আকারে বড় এবং জটিল হয়ে যায়, তখন ট্র্যাক রাখা কঠিন হয় যে কোন কোড কী কাজ করছে। ফাংশন ব্যবহার করে প্রোগ্রামাররা কোডের একটি অংশকে পুনরায় যেকোনো জায়গায় ব্যবহার করতে পারেন।

## Example and Syntax of a Function
একটি ফাংশনের সিনট্যাক্স নিচের মতো হয়:

```python
def func1():
    print('hello')
```
এই ফাংশনটিকে প্রোগ্রামের যেকোনো জায়গা থেকে যতবার খুশি কল (call) করা যায়।

## Function Call
যখনই আমরা কোনো ফাংশনকে কাজ করতে নির্দেশ দিতে চাই, তখন আমরা ফাংশনের নাম এবং তার সাথে প্যারেনথেসিস `()` ব্যবহার করি।

```python
func1() # This is called function call
```

## Function Definition
`def` কিওয়ার্ড দিয়ে শুরু হওয়া যে অংশটি ফাংশন কলের সময় এক্সিকিউট হবে ইনস্ট্রাকশনগুলো ধারণ করে, তাকে ফাংশন ডেফিনিশন বলা হয়।

## Types of Functions in Python
পাইথনে দুই ধরনের ফাংশন রয়েছে:
- **Built in functions:** এগুলো পাইথনে আগে থেকেই তৈরি থাকে (যেমন: `len()`, `print()`, `range()`)।
- **User defined functions:** যেগুলো ইউজার নিজে তৈরি করে (যেমন: আমাদের তৈরি করা `func1()`)।

## Functions with Arguments
একটি ফাংশন কিছু ভ্যালু ইনপুট হিসেবে গ্রহণ করতে পারে, যাকে আর্গুমেন্ট (argument) বলা হয়। আমরা এই ভ্যালুগুলোকে প্যারেনথেসিসের ভেতরে রাখি। একটি ফাংশন কোনো ভ্যালু রিটার্নও করতে পারে।

```python
def greet(name):
    gr = "hello" + name
    return gr

a = greet("harry")
# a will now contain "hello harry"
```

## Default Parameter Value
আমরা ফাংশনের আর্গুমেন্টে একটি ডিফল্ট ভ্যালু নির্ধারণ করে দিতে পারি। যদি ফাংশন কল করার সময় ওই আর্গুমেন্টের কোনো ভ্যালু দেওয়া না হয়, তবে এই ডিফল্ট ভ্যালুটি ব্যবহৃত হবে।

*Example:*
```python
def greet(name="stranger"):
    print("Hello", name)

greet() # name will be "stranger" (default)
greet("harry") # name will be "harry" (passed)
```

## Recursion
রিকারশন (Recursion) হলো এমন একটি ফাংশন যা নিজেকে নিজেই কল করে। এটি গাণিতিক ফর্মুলাকে সরাসরি ফাংশন হিসেবে রূপান্তর করতে খুব সহায়ক।

*Example:* `factorial(n) = n x factorial (n-1)`
এই ফাংশনটি এভাবে লেখা যায়:

```python
def factorial(n):
    if n == 0 or n == 1: # base condition
        return 1
    else:
        return n * factorial(n-1) # function calling itself
```

রিকারশন ব্যবহারের সময় প্রোগ্রামারকে অত্যন্ত সতর্ক থাকতে হয়, যাতে ফাংশনটি নিজেকে অসীম (infinitely) কল না করতে থাকে (Base condition নিশ্চিত করা খুব জরুরি)।

## Practice Set
- [ ] 1. Write a program using functions to find greatest of three numbers.
- [ ] 2. Write a python program using function to convert Celsius to Fahrenheit.
- [ ] 3. How do you prevent a python print() function to print a new line at the end.
- [ ] 4. Write a recursive function to calculate the sum of first n natural numbers.
- [ ] 5. Write a python function to print first n lines of the following pattern:
```text
***
**    - for n = 3
*
```
- [ ] 6. Write a python function which converts inches to cms.
- [ ] 7. Write a python function to remove a given word from a list and strip it at the same time.
- [ ] 8. Write a python function to print multiplication table of a given number.
