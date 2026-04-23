---
tags:
  - python-programming
  - loops
  - while-loop
  - for-loop
---

# Loops in Python

কখনো কখনো আমরা আমাদের প্রোগ্রামে কিছু নির্দিষ্ট স্টেটমেন্ট বারবার এক্সিকিউট করতে চাই (যেমন: ১ থেকে ১০০০ প্রিন্ট করা)। লুপ ব্যবহার করে একজন প্রোগ্রামার খুব সহজেই কম্পিউটারকে বোঝাতে পারেন কোন ইনস্ট্রাকশনগুলো বারবার চালাতে হবে।

## Types of Loops in Python
পাইথনে মূলত দুই ধরনের লুপ থাকে:
- `while` loops
- `for` loops

## While Loop
`while` লুপে প্রথমে কন্ডিশন চেক করা হয়। যদি কন্ডিশন True হয়, তাহলে লুপের ভেতরের কোড এক্সিকিউট হয়; অন্যথায় লুপ থেকে বের হয়ে আসে। লুপের বডি এক্সিকিউট হওয়ার পর আবার কন্ডিশন চেক হয়, এবং এই প্রক্রিয়া চলতে থাকে যতক্ষণ না কন্ডিশন False হয়।

*Syntax:*
```python
while (condition): # The block keeps executing until the condition is true
    # Body of the loop
```

*Example:*
```python
i = 0
while i < 5: # print "Harry" - 5 times!
    print("Harry")
    i = i + 1
```

## For Loop
একটি `for` লুপ কোনো একটি সিকোয়েন্স (যেমন: লিস্ট, টাপল, স্ট্রিং) এর উপাদানগুলোর ওপর ইটারেট (iterate) করতে ব্যবহৃত হয়।

*Syntax:*
```python
l = [1, 7, 8]
for item in l:
    print(item) # prints 1, 7 and 8
```

## range() Function in Python
`range()` ফাংশনটি নাম্বারের একটি সিকোয়েন্স জেনারেট করতে ব্যবহৃত হয়। আমরা শুরু (start), শেষ (stop) এবং স্টেপ-সাইজ (step-size) উল্লেখ করতে পারি:
```python
range(start, stop, step_size)
```

*Example:*
```python
for i in range(0, 7): # range(7) can also be used.
    print(i) # prints 0 to 6
```

## For Loop with Else
`for` লুপের সাথে একটি ঐচ্ছিক (optional) `else` ব্লক ব্যবহার করা যায়। লুপটি যখন সফলভাবে শেষ হয়ে যায় (অর্থাৎ সব ইটারেশন শেষ হয়), তখন `else` ব্লকের কোড এক্সিকিউট হয়।

*Example:*
```python
l = [1, 7, 8]
for item in l:
    print(item)
else:
    print("done") # this is printed when the loop exhausts!
```

## The Break Statement
লুপ চলতে থাকা অবস্থায় যদি `break` স্টেটমেন্ট পাওয়া যায়, তবে এটি লুপ থেকে তাৎক্ষণিকভাবে বের হয়ে আসতে ইনস্ট্রাকশন দেয়।

*Example:*
```python
for i in range(0, 80):
    print(i) # this will print 0, 1, 2 and 3
    if i == 3:
        break
```

## The Continue Statement
`continue` স্টেটমেন্ট বর্তমান ইটারেশনটি থামিয়ে দিয়ে লুপের পরবর্তী ইটারেশনে চলে যেতে ব্যবহৃত হয়। এটি মূলত "এই ইটারেশনটি স্কিপ করো" নির্দেশ দেয়।

*Example:*
```python
for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
    print(i)
```

## Pass Statement
`pass` হলো পাইথনের একটি নাল (null) স্টেটমেন্ট। এটি মূলত নির্দেশ দেয় "কিছুই করো না" (do nothing)।

*Example:*
```python
l = [1, 7, 8]
for item in l:
    pass # without pass, the program will throw an error
```

## Practice Set
- [ ] 1. Write a program to print multiplication table of a given number using for loop.
- [ ] 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
`l = ["Harry", "Soham", "Sachin", "Rahul"]`
- [ ] 3. Attempt problem 1 using while loop.
- [ ] 4. Write a program to find whether a given number is prime or not.
- [ ] 5. Write a program to find the sum of first n natural numbers using while loop.
- [ ] 6. Write a program to calculate the factorial of a given number using for loop.
- [ ] 7. Write a program to print the following star pattern.
```text
  *
 ***
***** for n = 3
```
- [ ] 8. Write a program to print the following star pattern:
```text
*
**
***   for n = 3
```
- [ ] 9. Write a program to print the following star pattern.
```text
* * *
*   * for n = 3
* * *
```
- [ ] 10. Write a program to print multiplication table of n using for loops in reversed order.
