# Chapter 6: Counting

Combinatorics, the study of arrangements of objects, is an important part of discrete mathematics. This subject was studied as long ago as the seventeenth century, when combinatorial questions arose in the study of gambling games. Enumeration, the counting of objects with certain properties, is an important part of combinatorics. We must count objects to solve many different types of problems. For instance, counting is used to determine the complexity of algorithms. Counting is also required to determine whether there are enough telephone numbers or Internet protocol addresses to meet demand. Recently, it has played a key role in mathematical biology, especially in sequencing DNA. Furthermore, counting techniques are used extensively when probabilities of events are computed.

The basic rules of counting, which we will study in Section 6.1, can solve a tremendous variety of problems. For instance, we can use these rules to enumerate the different telephone numbers possible in the United States, the allowable passwords on a computer system, and the different orders in which the runners in a race can finish. Another important combinatorial tool is the pigeonhole principle, which we will study in Section 6.2. This states that when objects are placed in boxes and there are more objects than boxes, then there is a box containing at least two objects. For instance, we can use this principle to show that among a set of 15 or more students, at least 3 were born on the same day of the week.

We can phrase many counting problems in terms of ordered or unordered arrangements of the objects of a set with or without repetitions. These arrangements, called permutations and combinations, are used in many counting problems. For instance, suppose the 100 top finishers on a competitive exam taken by 2000 students are invited to a banquet. We can count the possible sets of 100 students that will be invited, as well as the ways in which the top 10 prizes can be awarded.

Another problem in combinatorics involves generating all the arrangements of a specified kind. This is often important in computer simulations. We will devise algorithms to generate arrangements of various types.

---

## 6.1 The Basics of Counting

### 6.1.1 Basic Principles
- **The Product Rule:** If a procedure can be broken down into a sequence of two tasks with $n_1$ ways for the first and $n_2$ ways for the second, there are $n_1 n_2$ ways for the procedure.
  - In terms of Cartesian product: $|A_1 \times A_2 \times \dots \times A_m| = |A_1| \cdot |A_2| \cdots |A_m|$.
- **The Sum Rule:** If a task can be done in $n_1$ ways or $n_2$ ways (mutually exclusive), there are $n_1 + n_2$ ways.
  - In terms of sets: $|A_1 \cup A_2 \cup \dots \cup A_m| = \sum_{i=1}^m |A_i|$ for pairwise disjoint sets $A_i$.
- **The Subtraction Rule (Principle of Inclusion–Exclusion):**
  $$|A_1 \cup A_2| = |A_1| + |A_2| - |A_1 \cap A_2|$$
- **The Division Rule:** There are $n/d$ ways to do a task if it can be done in $n$ ways and for every way $w$, exactly $d$ of the $n$ ways correspond to $w$. ($|B| = |A|/d$ for $d$-to-1 functions).

---

## 6.2 The Pigeonhole Principle

### 6.2.1 Introduction

> **THEOREM 1 (The Pigeonhole Principle / Dirichlet Drawer Principle)**  
> If $k$ is a positive integer and $k + 1$ or more objects are placed into $k$ boxes, then there is at least one box containing two or more of the objects.

> **G. LEJEUNE DIRICHLET (1805–1859)**  
> Succeeded Gauss at Göttingen. Proved that there are infinitely many primes in arithmetic progressions $an + b$ ($\gcd(a, b) = 1$) and proved Fermat’s Last Theorem for $n = 5$.

### 6.2.2 The Generalized Pigeonhole Principle

> **THEOREM 2 (Generalized Pigeonhole Principle)**  
> If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least $\lceil N/k \rceil$ objects.

### 6.2.3 Applications & Ramsey Theory
- **Theorem 3:** Every sequence of $n^2 + 1$ distinct real numbers contains a strictly increasing or strictly decreasing subsequence of length $n + 1$.
- **Ramsey Theory:** In every group of 6 people, there are either 3 mutual friends or 3 mutual enemies ($R(3, 3) = 6$).

> **FRANK PLUMPTON RAMSEY (1903–1930)**  
> Fellow at King's College, Cambridge. Formulated foundational theorems in mathematical logic and combinatorics (*Ramsey numbers* $R(m, n)$).

---

## 6.3 Permutations and Combinations

### 6.3.1 Permutations

> **THEOREM 1 & COROLLARY 1**  
> An **$r$-permutation** of $n$ elements is an ordered selection:
> $$P(n, r) = n(n-1)\dots(n-r+1) = \frac{n!}{(n-r)!}$$

### 6.3.2 Combinations

> **THEOREM 2 & COROLLARY 2**  
> An **$r$-combination** is an unordered subset of $r$ elements:
> $$C(n, r) = \binom{n}{r} = \frac{n!}{r!(n-r)!} = C(n, n-r)$$

- **Combinatorial Proofs:** Double counting proofs and bijective proofs.

---

## 6.4 Binomial Coefficients and Identities

### 6.4.1 The Binomial Theorem

> **THEOREM 1 (The Binomial Theorem)**  
> $$(x + y)^n = \sum_{j=0}^n \binom{n}{j} x^{n-j} y^j$$

#### Corollaries:
1. $\sum_{k=0}^n \binom{n}{k} = 2^n$
2. $\sum_{k=0}^n (-1)^k \binom{n}{k} = 0 \implies \binom{n}{0} + \binom{n}{2} + \dots = \binom{n}{1} + \binom{n}{3} + \dots$
3. $\sum_{k=0}^n 2^k \binom{n}{k} = 3^n$

### 6.4.2 Pascal's Identity & Triangle

> **THEOREM 2 (Pascal’s Identity)**  
> $$\binom{n+1}{k} = \binom{n}{k-1} + \binom{n}{k}$$

> **BLAISE PASCAL (1623–1662)**  
> French polymath who developed Pascal's triangle properties and probability foundations with Fermat.

### 6.4.3 Additional Identities

> **THEOREM 3 (Vandermonde’s Identity)**  
> $$\binom{m+n}{r} = \sum_{k=0}^r \binom{m}{r-k} \binom{n}{k}$$

- **Corollary 4:** $\binom{2n}{n} = \sum_{k=0}^n \binom{n}{k}^2$.
- **Theorem 4 (Hockey Stick Identity):** $\binom{n+1}{r+1} = \sum_{j=r}^n \binom{j}{r}$.

> **ALEXANDRE-THÉOPHILE VANDERMONDE (1735–1796)**  
> French mathematician and chemist who published on determinants and combinatorics.

---

## 6.5 Generalized Permutations and Combinations

##### TABLE 1: Summary of Permutations & Combinations
| Type | Repetition Allowed? | Formula |
| :--- | :---: | :--- |
| $r$-permutations | No | $\frac{n!}{(n-r)!}$ |
| $r$-combinations | No | $\frac{n!}{r!(n-r)!}$ |
| $r$-permutations | Yes | $n^r$ |
| $r$-combinations | Yes | $\binom{n+r-1}{r} = \frac{(n+r-1)!}{r!(n-1)!}$ |

### 6.5.1 Indistinguishable Objects & Boxes
- **Permutations with indistinguishable objects:** $\frac{n!}{n_1! n_2! \dots n_k!}$
- **Distinguishable objects into Distinguishable boxes:** $\frac{n!}{n_1! n_2! \dots n_k!}$
- **Indistinguishable objects into Distinguishable boxes (Stars & Bars):** $\binom{n+r-1}{r}$
- **Distinguishable objects into Indistinguishable boxes:** $\sum_{j=1}^k S(n, j)$, where $S(n, j)$ are Stirling numbers of the second kind:
  $$S(n, j) = \frac{1}{j!} \sum_{i=0}^{j-1} (-1)^i \binom{j}{i} (j-i)^n$$
- **Indistinguishable objects into Indistinguishable boxes:** Partitions $p_k(n)$ of $n$ into at most $k$ parts.

---

## 6.6 Generating Permutations and Combinations

### 6.6.1 Generating Next Permutation in Lexicographic Order
```pascal
ALGORITHM 1 Generating the Next Permutation in Lexicographic Order.
procedure next permutation(a1 a2 ... an: permutation of {1, 2, ..., n} != n n-1 ... 1)
  j := n - 1
  while aj > aj+1
    j := j - 1
  k := n
  while aj > ak
    k := k - 1
  interchange aj and ak
  r := n
  s := j + 1
  while r > s
    interchange ar and as
    r := r - 1
    s := s + 1
  {a1 a2 ... an is now the next permutation}
```

### 6.6.2 Generating Next $r$-Combination
```pascal
ALGORITHM 3 Generating the Next r-Combination in Lexicographic Order.
procedure next r-combination({a1, a2, ..., ar} != {n-r+1, ..., n} with a1 < a2 < ... < ar)
  i := r
  while ai = n - r + i
    i := i - 1
  ai := ai + 1
  for j := i + 1 to r
    aj := ai + j - i
  {{a1, a2, ..., ar} is now the next combination}
```
