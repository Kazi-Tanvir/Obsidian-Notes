---
tags:
  - python-programming
  - virtual-environment
  - lambda
  - map-filter-reduce
---

# Advanced Python 2

## Virtual Environment
ভার্চুয়াল এনভায়রনমেন্ট (Virtual environment) হলো সিস্টেমের মেইন পাইথন ইন্টারপ্রেটারের মতোই একটি এনভায়রনমেন্ট, তবে এটি সিস্টেমের অন্যান্য পাইথন এনভায়রনমেন্ট থেকে সম্পূর্ণ আলাদা এবং আইসোলেটেড থাকে।

**Installation:**
```bash
pip install virtualenv # Install the package
virtualenv myprojectenv # Creates a new venv
```

## pip freeze command
`pip freeze` কমান্ড একটি নির্দিষ্ট পাইথন এনভায়রনমেন্টে ইনস্টল করা সমস্ত প্যাকেজ এবং তাদের ভার্সনগুলোর তালিকা রিটার্ন করে।
```bash
pip freeze > requirements.txt
```
এই কমান্ডটি `requirements.txt` নামের একটি ফাইলে প্যাকেজগুলোর লিস্ট সেভ করে। অন্য ইউজাররা এই ফাইলটি ব্যবহার করে একই এনভায়রনমেন্ট তৈরি করতে পারেন:
```bash
pip install -r requirements.txt
```

## Lambda functions
`lambda` কিওয়ার্ড ব্যবহার করে একটি এক্সপ্রেশনের মাধ্যমে যে ফাংশন তৈরি করা হয়, তাকে ল্যাম্বডা ফাংশন বা অ্যানোনিমাস (anonymous) ফাংশন বলে।

*Syntax:*
```python
# lambda arguments: expressions
square = lambda x: x*x
square(6) # returns 36
```

## join method (strings)
এই মেথডটি ইটারেবল অবজেক্টের (যেমন লিস্ট) উপাদানগুলো নিয়ে একটি স্ট্রিং তৈরি করে।
```python
l = ["apple", "mango", "banana"]
result = ", and, ".join(l)
print(result) # "apple, and, mango, and, banana"
```

## format method (strings)
এই মেথডটি স্ট্রিংয়ের ভেতরে ভ্যালু ফরম্যাট করে একটি নির্দিষ্ট আউটপুট তৈরি করে।
```python
"{} is a good {}".format("harry", "boy")
```

## Map, Filter & Reduce
- **Map:** এটি একটি ফাংশনকে ইনপুট লিস্টের সমস্ত উপাদানের ওপর অ্যাপ্লাই করে।
```python
map(function, input_list)
```
- **Filter:** এটি একটি লিস্ট তৈরি করে যেখানকার উপাদানগুলোর জন্য দেওয়া ফাংশনটি True রিটার্ন করে।
```python
list(filter(function, input_list))
```
- **Reduce:** এটি সিকোয়েনশিয়াল উপাদানগুলোর ওপর কম্পিউটেশন চালিয়ে একটি সিঙ্গেল ভ্যালু রিটার্ন করে।
```python
from functools import reduce
val = reduce(function, list1)
```

## Practice Set
- [ ] 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?
- [ ] 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:
“The name of the student is Harry, his marks are 72 and phone number is 99999888”
- [ ] 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
- [ ] 4. Write a program to filter a list of numbers which are divisible by 5.
- [ ] 5. Write a program to find the maximum of the numbers in a list using the reduce function.
- [ ] 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.
- [ ] 7. Explore the ‘Flask’ module and create a web server using Flask & Python.
