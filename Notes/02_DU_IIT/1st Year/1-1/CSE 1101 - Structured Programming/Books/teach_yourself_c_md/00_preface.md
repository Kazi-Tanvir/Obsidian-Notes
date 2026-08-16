# Preface

This book teaches you how to program in what is usually regarded as the world's most important professional programming language: C.

One reason for C's success and staying power is that programmers *like* it. C combines subtlety and elegance with raw power and flexibility. It is a structured language that does not constrain. It is a high-performance language that does not restrain. C is also a language that puts you, the programmer, firmly in charge. C was created by a programmer for programmers. It is not the contrived product of a committee, but rather the outcome of programmers seeking a better programming language.

C is important for another reason. It is the gateway to the world's two other professional programming languages: C++ and Java. C++ is built upon C, and Java is built upon C++. Thus, C is at the foundation of all modern programming, and knowledge of C is fundamental to the successful creation of high-performance, high-quality software. Simply put, to be a professional programmer today means that you are competent in C.

---

### A Short History of C

C was invented and first implemented by Dennis Ritchie on a DEC PDP-11 using the UNIX operating system. C is the result of a development process that started with an older language called BCPL, developed by Martin Richards. BCPL influenced a language called B that was invented by Ken Thompson and that led to the development of C in the 1970s.

For many years, the de facto standard for C was the one described in *The C Programming Language* by Brian Kernighan and Dennis Ritchie (Prentice-Hall, 1978). However, as C grew in popularity, a committee was organized in 1983 to create an ANSI (American National Standards Institute) standard for C. The standardization process took six years (much longer than anyone reasonably expected). The ANSI C standard was finally adopted late in 1989 and the first copies became generally available in 1990. The standard was amended slightly in 1996. Today, virtually all C compilers comply with ANSI standard C and that is the version of C you will learn in this book. (That is, this book teaches ANSI standard C.)

C is often referred to as a *middle-level language*. Before C there were basically two types of languages used to program computers. One is called *assembly language*, which is the symbolic representation of the actual machine instructions executed by the computer. Assembly language is a *low-level language* because the programmer is working with (in symbolic form) the actual instructions that the computer will execute. Assembly language can be used to create very efficient programs, but it provides no built-in control structures or I/O functions. All such items must be manually constructed by the programmer. By contrast, a *high-level language* buffers the programmer from the computer. A high-level language typically supplies various control structures, input and output commands, and the like, which make programming easier and faster. However, the elements of a high-level language may not relate directly to the way that the computer ultimately carries out the program. This separation often causes programs written using a high-level language to be less efficient than those written in assembly language. Because many people find assembly language programming to be a tedious, difficult task, there was a need for a language that balanced ease-of-use with efficiency. Many programmers feel that C provides this balance. It successfully combines the structure of a high-level language with the power and efficiency of assembly language. Since it spans the gap between assembly language and high-level languages, it is called a middle-level language.

Initially, C was used primarily for creating *systems software*. Systems software consists of those programs that help run the computer. These include programs such as operating systems, compilers, and editors. However, as C gained in popularity, it began to be used for general purpose programming. Today, C is used by programmers for virtually any programming task. It is a language that has survived the test of time and proven itself to be as versatile as it is powerful.

---

### C vs. C++

Newcomers are sometimes confused about the differences between C and C++ and how they relate to each other. In short, C++ is an extended version of C that is designed to support object-oriented programming (OOP). C++ contains and supports the entire C language in addition to a set of object-oriented extensions. (That is, C++ is a superset of C.) Because C++ is built upon the foundation of C, you cannot learn C++ without learning the basics of C. Therefore, if you think that you will someday move on to C++, your knowledge of C will not only be useful, it will be necessary.

---

### About This Book

This book is unique because it teaches you the C language by applying mastery learning. It does so by presenting one idea at a time, followed by numerous examples and exercises to help you thoroughly understand each topic. This approach ensures that you master each topic before moving on.

The material is presented sequentially. Therefore, you should work carefully through each chapter because each chapter assumes that you know the material presented in all preceding chapters.

This book teaches ANSI standard C. This ensures that your knowledge will be applicable to the widest range of C environments. This book also uses contemporary syntax and structure, which means that you will be learning the right way to write C programs from the very beginning.

---

### How This Book is Organized

This book is composed of 12 chapters and 4 appendices. Each chapter (except Chapter 1) begins with a Review Skills Check, which consists of questions and exercises covering the previous chapter's material. The chapters are divided into sections. Each section covers one topic. At the end of each section are examples followed by exercises that test your understanding of the topic. At the end of each chapter, you will find a Mastery Skills Check, which checks your knowledge of the material in the chapter. Finally, a Cumulative Skills Check is provided (starting with Chapter 2) to test how well you have integrated material from earlier chapters.

---

### For Further Study

*Teach Yourself C, Third Edition* is your gateway into the "Herb Schildt" series of programming books. Here is a partial list of Schildt's other programming books published by Osborne/McGraw-Hill.

If you want to learn more about C, you will find these books especially helpful.

- *C: The Complete Reference*
- *The Annotated ANSI C Standard*

If you will be moving on to C++ (C's object-oriented extension), then you will find that Schildt's C++ books provide excellent coverage of this important language. We recommend:

- *Teach Yourself C++*
- *C++: The Complete Reference*
- *C++ from the Ground Up*

If you will be developing programs for the Web, you will want to read:

- *Java: The Complete Reference*, co-authored by Herbert Schildt and Patrick Naughton.

Finally, if you want to program for Windows, we recommend:

- *Schildt's Windows 95 Programming in C and C++*
- *Schildt's Advanced Windows 95 Programming in C and C++*
- *Windows NT 4 from the Ground Up*
- *MFC Programming from the Ground Up*

When you need solid answers, fast, turn to **Herbert Schildt**, the recognized authority on programming.
