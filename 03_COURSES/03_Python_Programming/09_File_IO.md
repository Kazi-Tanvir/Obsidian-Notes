---
tags:
  - python-programming
  - file-io
---

# File I/O

র‌্যান্ডম-অ্যাক্সেস মেমরি (RAM) হলো ভোলাটাইল (volatile), অর্থাৎ প্রোগ্রাম বন্ধ হয়ে গেলে এর ভেতরের ডেটা হারিয়ে যায়। ডেটা চিরস্থায়ীভাবে সংরক্ষণ করার জন্য আমরা ফাইল ব্যবহার করি। ফাইল হলো স্টোরেজ ডিভাইসে সংরক্ষিত ডেটা। পাইথন প্রোগ্রামের মাধ্যমে ফাইলে ডেটা লেখা এবং ফাইল থেকে ডেটা পড়া যায়।

## Type of Files
প্রধানত দুই ধরনের ফাইল আছে:
1. **Text files:** যেমন `.txt`, `.c` ইত্যাদি।
2. **Binary files:** যেমন `.jpg`, `.dat` ইত্যাদি।

## Opening a File
ফাইল ওপেন করার জন্য পাইথনে `open()` ফাংশন রয়েছে। এটি দুটি প্যারামিটার নেয়: ফাইলের নাম এবং মোড (mode)।

```python
# open("filename", "mode of opening(read mode by default)")
f = open("this.txt", "r")
```

## Reading a File in Python
```python
# Open the file in read mode
f = open("this.txt", "r")
# Read its contents
text = f.read()
# Print its contents
print(text)
# Close the file
f.close()
```

## Other methods to read the file
আমরা `f.readline()` ফাংশন ব্যবহার করে ফাইল থেকে এক লাইন করে পড়তে পারি।
```python
f.readline() # Read one line from the file.
```

## Modes of opening a file
- `r` – open for reading
- `w` – open for writing
- `a` – open for appending
- `+` – open for updating
- `rb` – open for read in binary mode
- `rt` – open for read in text mode

## Write Files in Python
কোনো ফাইলে লেখার জন্য প্রথমে সেটিকে রাইট (`w`) বা অ্যাপেন্ড (`a`) মোডে ওপেন করতে হয়, এরপর `f.write()` মেথড ব্যবহার করে ফাইলে ডেটা লেখা যায়।

```python
# Open the file in write mode
f = open("this.txt", "w")
# Write a string to the file
f.write("this is nice")
# Close the file
f.close()
```

## With Statement
ফাইল ওপেন এবং ক্লোজ করার সবচেয়ে ভালো উপায় হলো `with` স্টেটমেন্ট ব্যবহার করা। এটি ব্যবহার করলে ফাইলটি স্বয়ংক্রিয়ভাবে ক্লোজ হয়ে যায়।

```python
with open("this.txt", "r") as f:
    text = f.read()
print(text)
```

## Practice Set
- [ ] 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
- [ ] 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
- [ ] 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.
- [ ] 4. A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.
- [ ] 5. Repeat program 4 for a list of such words to be censored.
- [ ] 6. Write a program to mine a log file and find out whether it contains ‘python’.
- [ ] 7. Write a program to find out the line number where python is present from ques 6.
- [ ] 8. Write a program to make a copy of a text file “this. txt”
- [ ] 9. Write a program to find out whether a file is identical & matches the content of another file.
- [ ] 10. Write a program to wipe out the content of a file using python.
- [ ] 11. Write a python program to rename a file to “renamed_by_ python.txt.
