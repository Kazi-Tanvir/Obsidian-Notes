---
tags:
  - python-programming
  - conditionals
  - if-else
---

# Conditional Expression

মাঝে মাঝে আমাদের প্রোগ্রামে কিছু সিদ্ধান্ত নেওয়ার প্রয়োজন হয় যা নির্দিষ্ট শর্ত পূরণ হওয়ার ওপর নির্ভর করে। পাইথন প্রোগ্রামিংয়েও শর্তের ওপর ভিত্তি করে ইনস্ট্রাকশন এক্সিকিউট করতে হয়। এর জন্যই কন্ডিশনালস ব্যবহৃত হয়!

## If Else and Elif in Python
`If else` এবং `elif` স্টেটমেন্টগুলো আমাদের কোডের নির্দিষ্ট শর্তের কারণে প্রোগ্রামে মাল্টিওয়ে ডিসিশন (বহুমুখী সিদ্ধান্ত) নিতে সাহায্য করে।

*Syntax:*
```python
if (condition1):    # if condition1 is True
    print("yes")
elif (condition2):  # if condition2 is True
    print("no")
else:               # otherwise
    print("maybe")
```

## Code Example
```python
a = 22
if (a > 9):
    print("greater")
else:
    print("lesser")
```

## Relational Operators
রিলেশনাল অপারেটরগুলো `if` স্টেটমেন্টের ভেতরে কন্ডিশন ইভালুয়েট করতে ব্যবহৃত হয়। যেমন:
- `==`: সমান কি না চেক করে।
- `>=`: বড় বা সমান কি না।
- `<=`: ছোট বা সমান কি না।

## Logical Operators
লজিক্যাল অপারেটরগুলো কন্ডিশনাল স্টেটমেন্টে কাজ করে। যেমন:
- `and`: দুটি কন্ডিশনই সত্য হলে True রিটার্ন করে।
- `or`: যেকোনো একটি কন্ডিশন সত্য হলে True রিটার্ন করে।
- `not`: True কে False এবং False কে True বানায়।

## Elif Clause
`elif` বলতে পাইথনে 'else if' বোঝায়। অনেকগুলো কন্ডিশন থাকলে আমরা একাধিক `elif` ব্যবহার করতে পারি। যখনই একটি কন্ডিশন মিলে যায় (True হয়), তখন প্রোগ্রাম সেই ব্লকটি এক্সিকিউট করে আর নিচের কন্ডিশনগুলো চেক করে না।

**Important notes:**
1. আপনি যত খুশি `elif` স্টেটমেন্ট ব্যবহার করতে পারেন।
2. সবশেষে থাকা `else` ব্লকটি তখনই এক্সিকিউট হয় যখন ওপরের সবগুলো `if` এবং `elif` কন্ডিশন ফেইল (False) করে।

## Practice Set
- [ ] 1. Write a program to find the greatest of four numbers entered by the user.
- [ ] 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
- [ ] 3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
- [ ] 4. Write a program to find whether a given username contains less than 10 characters or not.
- [ ] 5. Write a program which finds out whether a given name is present in a list or not.
- [ ] 6. Write a program to calculate the grade of a student from his marks from the following scheme:
  - 90 – 100 => Ex
  - 80 – 90 => A
  - 70 – 80 => B
  - 60 – 70 => C
  - 50 – 60 => D
  - <50 => F
- [ ] 7. Write a program to find out whether a given post is talking about “Harry” or not.
