---
tags:
  - python-programming
  - strings
  - slicing
---

# Strings

স্ট্রিং হলো পাইথনে একটি ডেটা টাইপ। এটি হলো কোটেশনের (quotes) মধ্যে রাখা ক্যারেক্টারের একটি সিকোয়েন্স।

We can primarily write a string in these three ways:
```python
a = 'harry'     # Single quoted string
b = "harry"     # Double quoted string
c = '''harry''' # Triple quoted string
```

## String Slicing
স্ট্রিংয়ের একটি নির্দিষ্ট অংশ পাওয়ার জন্য পাইথনে স্ট্রিংকে স্লাইস (slice) করা যায়।
পাইথনে স্ট্রিংয়ের ইনডেক্স ০ থেকে (length -1) পর্যন্ত হয়। স্ট্রিং স্লাইস করার জন্য আমরা নিচের সিনট্যাক্স ব্যবহার করি:

```python
# sl = name[ind_start: ind_end]
# first index included, last index is not included
```
উদাহরণ: `sl[0:3]` দিলে এটি ০ থেকে ৩ এর পূর্ব পর্যন্ত (০, ১, ২) ক্যারেক্টার রিটার্ন করবে।

**Negative Indices:** নেগেটিভ ইনডেক্সও ব্যবহার করা যায়। `-1` বলতে (length - 1) ইনডেক্স বোঝায়, `-2` বলতে (length - 2) বোঝায়।

## Slicing with Skip Value
আমরা স্লাইসিংয়ের সময় স্কিপ ভ্যালুও দিতে পারি:
```python
word = "amazing"
word[1:6:2] # "mzn"
```

## String Functions
স্ট্রিং ম্যানিপুলেট বা বিভিন্ন অপারেশন করার জন্য কিছু সাধারণ ফাংশন নিচে দেওয়া হলো (ধরি স্ট্রিংটি হলো `str = 'harry'`):

1. **len() function:** এটি স্ট্রিংয়ের দৈর্ঘ্য (length) রিটার্ন করে।
```python
print(len(str)) # Output: 5
```
2. **endswith("rry"):** এটি চেক করে স্ট্রিংটি নির্দিষ্ট ক্যারেক্টার দিয়ে শেষ হয়েছে কি না এবং True বা False রিটার্ন করে।
```python
print(str.endswith("rry")) # Output: True
```
3. **count("c"):** এটি নির্দিষ্ট ক্যারেক্টার কতবার আছে তা গণনা করে।
```python
print(str.count("r")) # Output: 2
```
4. **capitalize():** এটি স্ট্রিংয়ের প্রথম ক্যারেক্টারকে বড় হাতের অক্ষরে (Capitalize) পরিণত করে।
```python
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Harry"
```
5. **find(word):** এটি স্ট্রিংয়ে নির্দিষ্ট শব্দের প্রথম উপস্থিতির ইনডেক্স রিটার্ন করে।
```python
index = str.find("rr")
print(index) # Output: 2
```
6. **replace(old, new):** এটি পুরো স্ট্রিংয়ে পুরনো শব্দকে নতুন শব্দ দিয়ে রিপ্লেস করে।
```python
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"
```

## Escape Sequence Characters
ব্যাকস্ল্যাশ `\` এর পরের ক্যারেক্টারগুলোকে এস্কেপ সিকোয়েন্স ক্যারেক্টার বলা হয়। এগুলো একের বেশি ক্যারেক্টার নিয়ে গঠিত হলেও স্ট্রিংয়ের ভেতরে এরা একটি ক্যারেক্টার হিসেবে কাজ করে।
Example: `\n` (newline), `\t` (Tab), `\'` (Single quote), `\\` (backslash) etc.

## Practice Set
- [ ] 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
- [ ] 2. Write a program to fill in a letter template given below with name and date.
```python
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
```
- [ ] 3. Write a program to detect double space in a string.
- [ ] 4. Replace the double space from problem 3 with single spaces.
- [ ] 5. Write a program to format the following letter using escape sequence characters.
```python
letter = "Dear Harry, this python course is nice. Thanks!"
```
