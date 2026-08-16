# Chapter 3: Algorithms

Many problems can be solved by considering them as special cases of general problems. For instance, consider the problem of locating the largest integer in the sequence 101, 12, 144, 212, 98. This is a specific case of the problem of locating the largest integer in a sequence of integers. To solve this general problem we must give an algorithm, which specifies a sequence of steps used to solve this general problem. We will study algorithms for solving many different types of problems in this book. For example, in this chapter we will introduce algorithms for two of the most important problems in computer science, searching for an element in a list and sorting a list so its elements are in some prescribed order, such as increasing, decreasing, or alphabetic. Later in the book we will develop algorithms that find the greatest common divisor of two integers, that generate all the orderings of a finite set, that find the shortest path between nodes in a network, and for solving many other problems.

We will also introduce the notion of an algorithmic paradigm, which provides a general method for designing algorithms. In particular we will discuss brute-force algorithms, which find solutions using a straightforward approach without introducing any cleverness. We will also discuss greedy algorithms, a class of algorithms used to solve optimization problems. Proofs are important in the study of algorithms. In this chapter we illustrate this by proving that a particular greedy algorithm always finds an optimal solution.

One important consideration concerning an algorithm is its computational complexity, which measures the processing time and computer memory required by the algorithm to solve problems of a particular size. To measure the complexity of algorithms we use big-$O$ and big-Theta notation, which we develop in this chapter. We will illustrate the analysis of the complexity of algorithms in this chapter, focusing on the time an algorithm takes to solve a problem. Furthermore, we will discuss what the time complexity of an algorithm means in practical and theoretical terms.

---

## 3.1 Algorithms

### 3.1.1 Introduction

> **Definition 1**  
> An **algorithm** is a finite sequence of precise instructions for performing a computation or for solving a problem.

> **ABU JA‘FAR MOHAMMED IBN MUSA AL-KHOWARIZMI (c. 780–c. 850)**  
> Astronomer and mathematician at the House of Wisdom in Baghdad. His book on Hindu numerals introduced positional decimal notation to the West (*algorism* $\to$ *algorithm*), and his book *Kitab al-jabr w’al muquabala* gave us the word *algebra*.

#### Properties of Algorithms:
1. **Input:** Values from a specified set.
2. **Output:** Solution produced from the inputs.
3. **Definiteness:** Steps defined precisely.
4. **Correctness:** Correct output produced for every valid input.
5. **Finiteness:** Terminates after a finite number of steps.
6. **Effectiveness:** Each step can be performed exactly in finite time.
7. **Generality:** Applicable for all problems of the desired form.

```pascal
ALGORITHM 1 Finding the Maximum Element in a Finite Sequence.
procedure max(a1, a2, ..., an: integers)
  max := a1
  for i := 2 to n
    if max < ai then max := ai
  return max {max is the largest element}
```

### 3.1.2 Searching Algorithms

#### Linear Search (Sequential Search)
```pascal
ALGORITHM 2 The Linear Search Algorithm.
procedure linear search(x: integer, a1, a2, ..., an: distinct integers)
  i := 1
  while (i <= n and x != ai)
    i := i + 1
  if i <= n then location := i
  else location := 0
  return location {location is the subscript of the term that equals x, or 0 if not found}
```

#### Binary Search
```pascal
ALGORITHM 3 The Binary Search Algorithm.
procedure binary search(x: integer, a1, a2, ..., an: increasing integers)
  i := 1 {left endpoint}
  j := n {right endpoint}
  while i < j
    m := floor((i + j) / 2)
    if x > am then i := m + 1
    else j := m
  if x = ai then location := i
  else location := 0
  return location
```

### 3.1.3 Sorting Algorithms

#### Bubble Sort
```pascal
ALGORITHM 4 The Bubble Sort.
procedure bubblesort(a1, ..., an: real numbers with n >= 2)
  for i := 1 to n - 1
    for j := 1 to n - i
      if aj > aj+1 then interchange aj and aj+1
  {a1, ..., an is in increasing order}
```

#### Insertion Sort
```pascal
ALGORITHM 5 The Insertion Sort.
procedure insertion sort(a1, a2, ..., an: real numbers with n >= 2)
  for j := 2 to n
    i := 1
    while aj > ai
      i := i + 1
    m := aj
    for k := 0 to j - i - 1
      aj-k := aj-k-1
    ai := m
  {a1, ..., an is in increasing order}
```

### 3.1.4 String Matching

#### Naive String Matcher
```pascal
ALGORITHM 6 Naive String Matcher.
procedure string match(n, m: positive integers, m <= n, t1, t2, ..., tn, p1, p2, ..., pm: characters)
  for s := 0 to n - m
    j := 1
    while (j <= m and ts+j = pj)
      j := j + 1
    if j > m then print "s is a valid shift"
```

### 3.1.5 Greedy Algorithms

#### Cashier's Algorithm (Making Change)
```pascal
ALGORITHM 7 Cashier’s Algorithm.
procedure change(c1, c2, ..., cr: values of denominations of coins, where c1 > c2 > ... > cr; n: a positive integer)
  for i := 1 to r
    di := 0 {counts coins of denomination ci}
    while n >= ci
      di := di + 1
      n := n - ci
  {di is the number of coins of denomination ci in change}
```

> **THEOREM 1**  
> The cashier’s algorithm always makes change using the fewest coins possible when change is made from quarters ($25¢$), dimes ($10¢$), nickels ($5¢$), and pennies ($1¢$).

#### Talk Scheduling (Interval Scheduling)
```pascal
ALGORITHM 8 Greedy Algorithm for Scheduling Talks.
procedure schedule(s1 <= s2 <= ... <= sn: start times, e1 <= e2 <= ... <= en: ending times)
  sort talks by finish time and reorder so that e1 <= e2 <= ... <= en
  S := empty set
  for j := 1 to n
    if talk j is compatible with S then
      S := S union {talk j}
  return S
```

### 3.1.6 The Halting Problem

> **THEOREM (Alan Turing, 1936)**  
> The Halting Problem is unsolvable: There is no procedure that takes an arbitrary computer program $P$ and input $I$ and decides whether $P$ halts on $I$.

---

## 3.2 The Growth of Functions

### 3.2.1 Big-$O$ Notation

> **Definition 1**  
> Let $f$ and $g$ be functions from the set of integers or real numbers to the set of real numbers. We say that $f(x)$ is $O(g(x))$ if there are constants $C$ and $k$ (called **witnesses**) such that  
> $|f(x)| \le C|g(x)| \quad \text{whenever } x > k$.

> **PAUL BACHMANN (1837–1920) & EDMUND LANDAU (1877–1938)**  
> Bachmann introduced big-$O$ notation in *Analytische Zahlentheorie* (1892). Landau popularized the notation throughout number theory.

> **DONALD E. KNUTH (BORN 1938)**  
> Professor Emeritus at Stanford, author of the multivolume masterpiece *The Art of Computer Programming*, creator of $\TeX$ and METAFONT, recipient of the 1974 Turing Award. Popularized $O$, $\Omega$, and $\Theta$ notations in computer science.

#### Growth hierarchy of common reference functions:
$$1 < \log n < n < n \log n < n^2 < 2^n < n!$$

### 3.2.2 Important Big-$O$ Properties

- **Polynomials:** If $f(x) = a_n x^n + \dots + a_1 x + a_0$, then $f(x)$ is $O(x^n)$.
- **Sum Rule:** If $f_1(x)$ is $O(g_1(x))$ and $f_2(x)$ is $O(g_2(x))$, then $(f_1 + f_2)(x)$ is $O(\max(|g_1(x)|, |g_2(x)|))$.
- **Product Rule:** $(f_1 f_2)(x)$ is $O(g_1(x)g_2(x))$.
- **Factorial & Logarithm:** $n!$ is $O(n^n)$ and $\log(n!)$ is $O(n \log n)$.

### 3.2.3 Big-$\Omega$ and Big-$\Theta$ Notation

> **Definition 2 (Big-$\Omega$)**  
> $f(x)$ is $\Omega(g(x))$ if there exist positive constants $C$ and $k$ such that $|f(x)| \ge C|g(x)|$ whenever $x > k$. ($f(x)$ is $\Omega(g(x)) \iff g(x)$ is $O(f(x))$).

> **Definition 3 (Big-$\Theta$)**  
> $f(x)$ is $\Theta(g(x))$ if $f(x)$ is $O(g(x))$ and $f(x)$ is $\Omega(g(x))$ (i.e., $C_1 |g(x)| \le |f(x)| \le C_2 |g(x)|$ for $x > k$).

---

## 3.3 Complexity of Algorithms

### 3.3.1 Time Complexity

##### TABLE 1: Common Time Complexity Classes
| Complexity | Terminology |
| :--- | :--- |
| $\Theta(1)$ | Constant complexity |
| $\Theta(\log n)$ | Logarithmic complexity |
| $\Theta(n)$ | Linear complexity |
| $\Theta(n \log n)$ | Linearithmic complexity |
| $\Theta(n^b)$ ($b \ge 1$) | Polynomial complexity |
| $\Theta(b^n)$ ($b > 1$) | Exponential complexity |
| $\Theta(n!)$ | Factorial complexity |

##### Summary of Key Complexities:
- **Maximum element search:** $\Theta(n)$ comparisons.
- **Linear search:** Worst-case $\Theta(n)$, average-case $\Theta(n)$.
- **Binary search:** Worst-case $\Theta(\log n)$.
- **Bubble sort:** Worst-case $\Theta(n^2)$ comparisons.
- **Insertion sort:** Worst-case $\Theta(n^2)$ comparisons.
- **Standard Matrix Multiplication ($n \times n$):** $n^3$ multiplications, $n^2(n - 1)$ additions $\implies \Theta(n^3)$.
- **Boolean Product of $n \times n$ 0-1 Matrices:** $2n^3$ bit operations $\implies \Theta(n^3)$.

### 3.3.2 Algorithmic Paradigms
- **Brute Force:** Testing all possibilities systematically (e.g., closest pair of $n$ points in $O(n^2)$).
- **Greedy Algorithms:** Making locally optimal choices at each stage.
- **Divide and Conquer:** Breaking into smaller independent subproblems.
- **Dynamic Programming & Backtracking:** Explored in later chapters.

### 3.3.3 Tractability and P versus NP
- **Class P (Tractable):** Problems solvable by worst-case polynomial-time algorithms ($O(n^k)$).
- **Intractable:** Solvable, but no polynomial-time algorithm exists (e.g., exponential $\Omega(2^n)$).
- **Class NP:** Problems whose solutions can be *checked* in polynomial time.
- **NP-Complete:** The hardest problems in NP; if any NP-complete problem has a polynomial-time algorithm, then P = NP (Cook-Levin Theorem).

> **STEPHEN COOK (BORN 1939)**  
> University Professor at University of Toronto; 1982 Turing Award winner. Formalized NP-completeness and polynomial-time reductions in 1971.
