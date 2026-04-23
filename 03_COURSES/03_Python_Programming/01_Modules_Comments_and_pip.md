---
tags:
  - python-programming
  - modules
  - comments
  - pip
---

# Modules, Comments & pip

Let's write our very first python program. Create a file called `hello.py` and paste the below code in it.

```python
print("hello world") # print is a function (more later)
```

এই ফাইলটি (.py এক্সটেনশন) রান করতে টার্মিনালে `python hello.py` টাইপ করুন, তাহলে স্ক্রিনে 'Hello World' প্রিন্ট হবে।

## Modules
মডিউল হলো অন্য কারও লেখা কোড (সাধারণত) সম্বলিত একটি ফাইল, যা আমরা আমাদের প্রোগ্রামে ইম্পোর্ট করে ব্যবহার করতে পারি।

### Types of Modules
পাইথনে দুই ধরনের মডিউল রয়েছে:
1. **Built in Modules:** এগুলো পাইথনে আগে থেকেই ইনস্টল করা থাকে (যেমন: `os`, `random`)।
2. **External Modules:** এগুলোকে `pip` ব্যবহার করে ইনস্টল করতে হয় (যেমন: `tensorflow`, `flask`)।

## pip
pip হলো পাইথনের প্যাকেজ ম্যানেজার। আপনার সিস্টেমে কোনো মডিউল ইনস্টল করতে আপনি pip ব্যবহার করতে পারেন।

```bash
pip install flask # Installs Flask Module
```

## Using python as a calculator
আমরা টার্মিনালে `python` টাইপ করে এন্টার চাপলে পাইথনকে একটি ক্যালকুলেটর হিসেবে ব্যবহার করতে পারি। এটি REPL (Read Evaluate Print Loop) চালু করে।

## Comments
কমেন্ট হলো এমন কিছু লেখা যা প্রোগ্রামার এক্সিকিউট করতে চান না। এটি সাধারণত অথরের নাম, তারিখ ইত্যাদি মার্ক করতে ব্যবহার করা হয়।

### Types of Comments
পাইথনে দুই ধরনের কমেন্ট আছে:
1. **Single Line Comments:** এক লাইনের কমেন্ট লিখতে লাইনের শুরুতে `#` ব্যবহার করা হয়।
```python
# This is a Single-Line Comment
```
2. **Multiline Comments:** একাধিক লাইনের কমেন্ট লিখতে প্রতিটি লাইনে `#` ব্যবহার করা যায়, অথবা মাল্টিলাইন স্ট্রিং (`""" """`) ব্যবহার করা যায়।
```python
"""This is an amazing
example of a Multiline
comment!"""
```

## Practice Set
- [ ] 1. Write a program to print Twinkle twinkle little star poem in python.
- [ ] 2. Use REPL and print the table of 5 using it.
- [ ] 3. Install an external module and use it to perform an operation of your interest.
- [ ] 4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
- [ ] 5. Label the program written in problem 4 with comments.
