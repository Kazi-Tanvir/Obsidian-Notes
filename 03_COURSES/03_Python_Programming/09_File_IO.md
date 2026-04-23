---
tags:
  - python-programming
  - file-io
---

# File I/O

The random-access memory is volatile, and all its contents are lost once a program terminates. In order to persist the data forever, we use files. A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.

## Type of Files
There are 2 types of files:
1. **Text files:** (.txt, .c, etc)
2. **Binary files:** (.jpg, .dat, etc)

Python has a lot of functions for reading, updating, and deleting files.

## Opening a File
Python has an `open()` function for opening files. It takes 2 parameters: filename and mode.

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
We can also use `f.readline()` function to read one full line at a time.
```python
f.readline() # Read one line from the file.
```

## Modes of opening a file
- `r` – open for reading
- `w` – open for writing
- `a` – open for appending
- `+` – open for updating
- `rb` will open for read in binary mode.
- `rt` will open for read in text mode.

## Write Files in Python
In order to write to a file, we first open it in write or append mode after which, we use the python’s `f.write()` method to write to the file!

```python
# Open the file in write mode
f = open("this.txt", "w")
# Write a string to the file
f.write("this is nice")
# Close the file
f.close()
```

## With Statement
The best way to open and close the file automatically is the `with` statement.

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