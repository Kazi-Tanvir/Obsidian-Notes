# 📚 Discrete Mathematics — Chapter 6: Counting
## Exam Suggestion & Predicted MCQ Set

> [!IMPORTANT]
> This chapter is from **Rosen's Discrete Mathematics** (Chapter 6). The chapter covers **6 sections**. Below is a complete priority-based study guide and a set of **50 predicted MCQs** with answers.

---

## 🎯 Topics You MUST Read (Priority Order)

### 🔴 Priority 1 — HIGHEST (These WILL be on the exam)

| # | Topic | Section | Why It's Critical |
|---|-------|---------|-------------------|
| 1 | **Product Rule & Sum Rule** | 6.1 | Foundation of every counting problem |
| 2 | **Permutations P(n,r)** | 6.3 | Direct formula questions are guaranteed |
| 3 | **Combinations C(n,r)** | 6.3 | Most tested topic in counting |
| 4 | **Pigeonhole Principle** | 6.2 | Classic MCQ favorite — "at least" questions |
| 5 | **Binomial Theorem** | 6.4 | Expanding $(x+y)^n$, finding specific terms |
| 6 | **Inclusion-Exclusion (2 sets)** | 6.1 | $|A \cup B| = |A| + |B| - |A \cap B|$ |

### 🟡 Priority 2 — HIGH (Very likely to appear)

| # | Topic | Section | Why It Matters |
|---|-------|---------|----------------|
| 7 | **Generalized Pigeonhole Principle** | 6.2 | $\lceil N/k \rceil$ problems |
| 8 | **Combinations with Repetition** | 6.5 | $C(n+r-1, r)$ — distributing identical objects |
| 9 | **Permutations with Repetition** | 6.5 | $n^r$ — passwords, strings, license plates |
| 10 | **Permutations of Indistinguishable Objects** | 6.5 | $\frac{n!}{n_1! n_2! \cdots n_k!}$ — rearranging words |
| 11 | **Pascal's Identity** | 6.4 | $C(n+1, k) = C(n, k-1) + C(n, k)$ |
| 12 | **Binomial Coefficient Identities** | 6.4 | Corollaries: $\sum C(n,k) = 2^n$, etc. |

### 🟢 Priority 3 — MEDIUM (May appear as 1-2 questions)

| # | Topic | Section | Notes |
|---|-------|---------|-------|
| 13 | **Distributing Objects to Boxes** | 6.5 | Labeled vs unlabeled objects/boxes |
| 14 | **Bit String Counting** | 6.1 | Strings with constraints (begin/end with specific bits) |
| 15 | **Circular Permutations** | 6.1/6.3 | $(n-1)!$ arrangements around a table |
| 16 | **Pascal's Triangle** | 6.4 | Properties and construction |
| 17 | **Ramsey Numbers** | 6.2 | $R(3,3) = 6$ — friends/enemies problem |

### ⚪ Priority 4 — LOW (Unlikely but possible)

| # | Topic | Section |
|---|-------|---------|
| 18 | Generating Permutations (lexicographic order) | 6.6 |
| 19 | Generating Combinations (bit string method) | 6.6 |
| 20 | Stirling Numbers | 6.5 |

---

## 📋 Key Formulas Cheat Sheet

> [!TIP]
> Memorize these formulas — almost every MCQ can be solved with one of these.

| Formula | Expression | When to Use |
|---------|-----------|-------------|
| **Product Rule** | $n_1 \times n_2 \times \cdots \times n_m$ | Sequential independent choices |
| **Sum Rule** | $n_1 + n_2 + \cdots + n_m$ | Mutually exclusive choices |
| **Permutations** | $P(n,r) = \frac{n!}{(n-r)!}$ | Ordered selection, no repetition |
| **Combinations** | $C(n,r) = \frac{n!}{r!(n-r)!}$ | Unordered selection, no repetition |
| **Permutations w/ repetition** | $n^r$ | Ordered selection, repetition allowed |
| **Combinations w/ repetition** | $C(n+r-1, r)$ | Unordered selection, repetition allowed |
| **Indistinguishable permutations** | $\frac{n!}{n_1! n_2! \cdots n_k!}$ | Arranging items with duplicates |
| **Binomial Theorem** | $(x+y)^n = \sum_{k=0}^{n} C(n,k) x^{n-k} y^k$ | Expanding binomial expressions |
| **Inclusion-Exclusion** | $|A \cup B| = |A| + |B| - |A \cap B|$ | "Either...or..." with overlap |
| **Pigeonhole** | If $N$ objects in $k$ boxes, some box has $\geq \lceil N/k \rceil$ | "Must have at least..." |
| **Circular permutations** | $(n-1)!$ | Seating around a round table |
| **Pascal's Identity** | $C(n+1,k) = C(n,k-1) + C(n,k)$ | Relating binomial coefficients |

---

## 🧪 Predicted Exam MCQs (50 Questions)

### Section 1: Product Rule & Sum Rule (Q1–Q10)

---

**Q1.** A license plate consists of 3 letters followed by 4 digits. How many different license plates are possible?

- A) $26^3 \times 10^4$  
- B) $26^3 + 10^4$  
- C) $26 \times 25 \times 24 \times 10^4$  
- D) $36^7$  

> **Answer: A** — Product rule: 26 choices for each letter × 10 choices for each digit.

---

**Q2.** A student can choose a project from one of three lists containing 23, 15, and 19 projects respectively. No project is on more than one list. How many possible projects are there?

- A) $23 \times 15 \times 19$  
- B) $23 + 15 + 19 = 57$  
- C) $C(57, 1)$  
- D) Both B and C  

> **Answer: D** — Sum rule since choices are mutually exclusive. C(57,1) = 57 too.

---

**Q3.** Each user password is 6 to 8 characters long, where each character is an uppercase letter or digit. Each password must contain at least one digit. How many possible 6-character passwords are there?

- A) $36^6$  
- B) $36^6 - 26^6$  
- C) $10 \times 36^5$  
- D) $26 \times 36^5$  

> **Answer: B** — Total strings of length 6 minus strings with no digits (all letters).

---

**Q4.** How many bit strings of length 8 are there?

- A) 128  
- B) 256  
- C) 64  
- D) 512  

> **Answer: B** — $2^8 = 256$

---

**Q5.** How many functions are there from a set with 5 elements to a set with 3 elements?

- A) $5^3 = 125$  
- B) $3^5 = 243$  
- C) $P(5,3) = 60$  
- D) $C(5,3) = 10$  

> **Answer: B** — Each of the 5 elements can map to any of 3 elements: $3^5$.

---

**Q6.** How many one-to-one functions are there from a set with 5 elements to a set with 7 elements?

- A) $7^5$  
- B) $P(7,5) = 2520$  
- C) $C(7,5) = 21$  
- D) $5^7$  

> **Answer: B** — One-to-one: first element has 7 choices, second has 6, ..., fifth has 3. $P(7,5) = 7!/2! = 2520$.

---

**Q7.** How many strings of 4 lowercase English letters are there?

- A) $26 \times 25 \times 24 \times 23$  
- B) $26^4$  
- C) $4^{26}$  
- D) $C(26, 4)$  

> **Answer: B** — Each position has 26 choices (repetition allowed), product rule.

---

**Q8.** A new company has a telephone number of the form NXX-XXXX where N is a digit from 2-9 and X is any digit 0-9. How many phone numbers are possible?

- A) $10^7$  
- B) $8 \times 10^6$  
- C) $8 \times 10^4$  
- D) $10^{10}$  

> **Answer: B** — N has 8 choices, each X has 10 choices.

---

**Q9.** How many bit strings of length seven either begin with two 0s or end with three 1s?

- A) $2^5 + 2^4$  
- B) $2^5 + 2^4 - 2^2$  
- C) $2^7$  
- D) $2^5 \times 2^4$  

> **Answer: B** — |Begin with 00| = $2^5$. |End with 111| = $2^4$. |Both| = $2^2$. By inclusion-exclusion: $32 + 16 - 4 = 44$.

---

**Q10.** Every student in a class is either a CS or Math major or both. There are 38 CS majors, 23 Math majors, and 7 joint majors. How many students are in the class?

- A) 68  
- B) 54  
- C) 61  
- D) 58  

> **Answer: B** — $|CS \cup Math| = 38 + 23 - 7 = 54$.

---

### Section 2: Pigeonhole Principle (Q11–Q18)

---

**Q11.** A drawer has 12 brown socks and 12 black socks. How many socks must you take out (in the dark) to guarantee at least two of the same color?

- A) 2  
- B) 3  
- C) 12  
- D) 13  

> **Answer: B** — 2 colors (boxes), need 2 of same. Worst case: 1 of each color, then 3rd guarantees a pair.

---

**Q12.** How many students must be in a class to guarantee that at least two students have the same birthday? (Assume 366 possible birthdays.)

- A) 366  
- B) 367  
- C) 365  
- D) 732  

> **Answer: B** — Pigeonhole: 366 boxes + 1 = 367.

---

**Q13.** Among any group of 367 people, at least how many must have been born in the same month?

- A) 12  
- B) 30  
- C) 31  
- D) $\lceil 367/12 \rceil = 31$  

> **Answer: D** — Generalized pigeonhole: $\lceil 367/12 \rceil = 31$.

---

**Q14.** What is the minimum number of students in a class to guarantee at least 6 students receive the same grade (A, B, C, D, F)?

- A) 25  
- B) 26  
- C) 30  
- D) 21  

> **Answer: B** — 5 grades, need 6 of same: $5 \times 5 + 1 = 26$.

---

**Q15.** A bowl contains 10 red balls and 10 blue balls. How many balls must be selected (without looking) to be sure of having at least three blue balls?

- A) 3  
- B) 5  
- C) 12  
- D) 13  

> **Answer: D** — Worst case: all 10 red first, then need 3 blue → $10 + 3 = 13$.

---

**Q16.** Show that among any 5 integers, there exist 2 with the same remainder when divided by 4.

The minimum number of integers needed to guarantee this is:

- A) 4  
- B) 5  
- C) 8  
- D) 9  

> **Answer: B** — 4 possible remainders (0,1,2,3), so by pigeonhole, 5 integers guarantee a repeat.

---

**Q17.** In a group of 6 people, where each pair is either friends or enemies, what is guaranteed?

- A) There are 3 mutual friends  
- B) There are 3 mutual enemies  
- C) There are either 3 mutual friends or 3 mutual enemies  
- D) Nothing is guaranteed  

> **Answer: C** — This is the Ramsey number $R(3,3) = 6$.

---

**Q18.** Every sequence of $n^2 + 1$ distinct real numbers contains a subsequence of length _____ that is either strictly increasing or strictly decreasing.

- A) $n$  
- B) $n + 1$  
- C) $n^2$  
- D) $2n$  

> **Answer: B** — Theorem 3: subsequence of length $n+1$.

---

### Section 3: Permutations & Combinations (Q19–Q30)

---

**Q19.** How many ways can we select 3 students from a group of 5 students to receive different scholarships (order matters)?

- A) $C(5,3) = 10$  
- B) $P(5,3) = 60$  
- C) $5^3 = 125$  
- D) $3^5 = 243$  

> **Answer: B** — Different scholarships = order matters = permutation.

---

**Q20.** $P(8, 3) = ?$

- A) 56  
- B) 336  
- C) 512  
- D) 40320  

> **Answer: B** — $P(8,3) = 8 \times 7 \times 6 = 336$.

---

**Q21.** $C(10, 4) = ?$

- A) 210  
- B) 5040  
- C) 10000  
- D) 151200  

> **Answer: A** — $C(10,4) = \frac{10!}{4! \cdot 6!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 210$.

---

**Q22.** A committee of 5 is to be formed from a group of 9 women and 6 men. How many committees have exactly 3 women and 2 men?

- A) $C(9,3) \times C(6,2) = 84 \times 15 = 1260$  
- B) $C(15,5) = 3003$  
- C) $P(9,3) \times P(6,2)$  
- D) $9 \times 6$  

> **Answer: A** — Choose 3 women from 9 AND 2 men from 6.

---

**Q23.** How many ways can we arrange all the letters in "MISSISSIPPI"?

- A) $11!$  
- B) $\frac{11!}{4! \cdot 4! \cdot 2!}$  
- C) $\frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!}$  
- D) $C(11, 4)$  

> **Answer: C** — M=1, I=4, S=4, P=2. $\frac{11!}{1! \cdot 4! \cdot 4! \cdot 2!} = 34650$.

---

**Q24.** How many bit strings of length 10 contain exactly four 1s?

- A) $C(10, 4) = 210$  
- B) $2^{10} = 1024$  
- C) $P(10, 4)$  
- D) $10^4$  

> **Answer: A** — Choose 4 positions out of 10 for the 1s.

---

**Q25.** How many ways are there to choose 5 cards from a standard 52-card deck?

- A) $P(52, 5)$  
- B) $C(52, 5) = 2,598,960$  
- C) $52^5$  
- D) $5^{52}$  

> **Answer: B** — Order doesn't matter in a hand.

---

**Q26.** $C(n, 0) + C(n, 1) + C(n, 2) + \cdots + C(n, n) = ?$

- A) $n!$  
- B) $n^2$  
- C) $2^n$  
- D) $3^n$  

> **Answer: C** — Set $x = y = 1$ in the binomial theorem.

---

**Q27.** Which identity is Pascal's Identity?

- A) $C(n,r) = C(n, n-r)$  
- B) $C(n+1, k) = C(n, k-1) + C(n, k)$  
- C) $C(n, r) = \frac{n!}{r!(n-r)!}$  
- D) $\sum C(n,k) = 2^n$  

> **Answer: B** — Pascal's Identity.

---

**Q28.** How many ways are there to seat 6 people around a circular table?

- A) $6! = 720$  
- B) $(6-1)! = 120$  
- C) $6^6$  
- D) $C(6, 6)$  

> **Answer: B** — Circular permutation: $(n-1)!$.

---

**Q29.** In how many ways can a photographer arrange 6 people in a row from a group of 10?

- A) $C(10, 6) = 210$  
- B) $P(10, 6) = 151200$  
- C) $10^6$  
- D) $6^{10}$  

> **Answer: B** — Arranging in a row = order matters = permutation.

---

**Q30.** $C(n, r) = C(n, n-r)$ is known as:

- A) Pascal's Identity  
- B) The Symmetry Identity  
- C) Vandermonde's Identity  
- D) The Binomial Theorem  

> **Answer: B** — Choosing $r$ items is equivalent to choosing which $n-r$ to leave out.

---

### Section 4: Binomial Theorem (Q31–Q38)

---

**Q31.** What is the expansion of $(x + y)^4$?

- A) $x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4$  
- B) $x^4 + y^4$  
- C) $4x^4 + 4y^4$  
- D) $x^4 + 4x^3y + 4xy^3 + y^4$  

> **Answer: A** — Coefficients from Pascal's triangle row 4: 1, 4, 6, 4, 1.

---

**Q32.** What is the coefficient of $x^3 y^{17}$ in the expansion of $(x + y)^{20}$?

- A) $C(20, 3) = 1140$  
- B) $C(20, 17) = 1140$  
- C) Both A and B  
- D) $20^3$  

> **Answer: C** — $C(20,3) = C(20,17) = 1140$.

---

**Q33.** What is the coefficient of $x^{12} y^{13}$ in $(2x - 3y)^{25}$?

- A) $C(25, 12) \cdot 2^{12} \cdot 3^{13}$  
- B) $C(25, 12) \cdot 2^{12} \cdot (-3)^{13}$  
- C) $C(25, 13) \cdot 2^{12} \cdot (-3)^{13}$  
- D) Both B and C  

> **Answer: D** — Binomial theorem: $C(25,12) \cdot (2x)^{12} \cdot (-3y)^{13}$, and $C(25,12) = C(25,13)$.

---

**Q34.** $\sum_{k=0}^{n} (-1)^k C(n,k) = ?$

- A) $2^n$  
- B) $0$  
- C) $1$  
- D) $-1$  

> **Answer: B** — Set $x = 1, y = -1$ in $(x+y)^n = 0^n = 0$ (for $n \geq 1$).

---

**Q35.** $\sum_{k=0}^{n} 2^k \cdot C(n, k) = ?$

- A) $2^n$  
- B) $3^n$  
- C) $n \cdot 2^n$  
- D) $2^{2n}$  

> **Answer: B** — Set $x = 1, y = 2$ in $(1+2)^n = 3^n$.

---

**Q36.** In Pascal's triangle, each entry is the sum of:

- A) The two entries directly above it  
- B) All entries in the row above  
- C) The entry directly above and to the left  
- D) The product of the two entries above  

> **Answer: A** — Pascal's Identity: each entry = sum of two entries above.

---

**Q37.** What is $C(2n, n)$ called?

- A) The central binomial coefficient  
- B) Pascal's number  
- C) The Catalan number  
- D) Vandermonde's coefficient  

> **Answer: A** — It's the middle/central entry in row $2n$ of Pascal's triangle.

---

**Q38.** Vandermonde's Identity states: $C(m+n, r) = ?$

- A) $C(m,r) + C(n,r)$  
- B) $C(m,r) \cdot C(n,r)$  
- C) $\sum_{k=0}^{r} C(m, r-k) \cdot C(n, k)$  
- D) $C(m,n) \cdot C(n,r)$  

> **Answer: C** — Vandermonde's Identity: $C(m+n, r) = \sum_{k=0}^{r} C(m, r-k) \cdot C(n, k)$.

---

### Section 5: Generalized Permutations & Combinations (Q39–Q50)

---

**Q39.** How many ways are there to select 5 items from 3 types of items (with unlimited supply)?

- A) $3^5 = 243$  
- B) $C(3, 5)$  
- C) $C(3+5-1, 5) = C(7, 5) = 21$  
- D) $P(3, 5)$  

> **Answer: C** — Combinations with repetition: $C(n+r-1, r) = C(7, 5)$.

---

**Q40.** How many solutions are there to $x_1 + x_2 + x_3 = 11$ where $x_1, x_2, x_3$ are non-negative integers?

- A) $C(11, 3)$  
- B) $C(13, 2) = 78$  
- C) $3^{11}$  
- D) $11^3$  

> **Answer: B** — Stars and bars: $C(11 + 3 - 1, 3 - 1) = C(13, 2) = 78$.

---

**Q41.** How many solutions are there to $x_1 + x_2 + x_3 + x_4 = 17$ where each $x_i \geq 1$?

- A) $C(20, 3) = 1140$  
- B) $C(16, 3) = 560$  
- C) $C(17, 4)$  
- D) $4^{17}$  

> **Answer: B** — Substituting $y_i = x_i - 1$: $y_1 + y_2 + y_3 + y_4 = 13$, then $C(13+3, 3) = C(16, 3) = 560$.

---

**Q42.** How many ways are there to arrange the letters in "SUCCESS"?

- A) $7!$  
- B) $\frac{7!}{3! \cdot 2!}$  
- C) $\frac{7!}{3! \cdot 2! \cdot 1! \cdot 1!}$  
- D) $C(7, 3)$  

> **Answer: C** — S=3, C=2, U=1, E=1. $\frac{7!}{3! \cdot 2! \cdot 1! \cdot 1!} = 420$.

---

**Q43.** How many strings can be made by reordering the letters of "ABRACADABRA"?

- A) $11!$  
- B) $\frac{11!}{5! \cdot 2! \cdot 2!}$  
- C) $\frac{11!}{5! \cdot 2! \cdot 2! \cdot 1! \cdot 1!}$  
- D) $C(11, 5)$  

> **Answer: C** — A=5, B=2, R=2, C=1, D=1.

---

**Q44.** How many ways can 8 identical cookies be distributed among 3 children?

- A) $3^8$  
- B) $C(10, 2) = 45$  
- C) $8^3$  
- D) $C(8, 3)$  

> **Answer: B** — Identical objects to distinct boxes: $C(8+3-1, 3-1) = C(10, 2) = 45$.

---

**Q45.** How many ways are there to distribute 5 distinguishable balls into 3 distinguishable boxes?

- A) $C(5, 3)$  
- B) $3^5 = 243$  
- C) $5^3 = 125$  
- D) $P(5, 3) = 60$  

> **Answer: B** — Each ball has 3 choices → $3^5$.

---

**Q46.** A coin is flipped 10 times. How many different outcomes are possible?

- A) 20  
- B) 100  
- C) $2^{10} = 1024$  
- D) $10^2 = 100$  

> **Answer: C** — Each flip has 2 outcomes, 10 flips → $2^{10}$.

---

**Q47.** How many 4-digit PINs are there where digits can repeat?

- A) $P(10, 4) = 5040$  
- B) $10^4 = 10000$  
- C) $C(10, 4) = 210$  
- D) $4^{10}$  

> **Answer: B** — Each digit has 10 choices, repetition allowed: $10^4$.

---

**Q48.** How many subsets of a set with 10 elements have exactly 4 elements?

- A) $2^{10}$  
- B) $C(10, 4) = 210$  
- C) $P(10, 4)$  
- D) $10^4$  

> **Answer: B** — Choosing a 4-element subset = $C(10, 4)$.

---

**Q49.** How many bit strings of length 10 have exactly 4 ones?

- A) $C(10, 4) = 210$  
- B) $2^{10}$  
- C) $10^4$  
- D) $4^{10}$  

> **Answer: A** — Choose 4 positions for 1s: $C(10, 4)$.

---

**Q50.** How many ways can 12 people be divided into 3 groups of 4 for a project?

- A) $C(12,4) \times C(8,4) \times C(4,4)$  
- B) $\frac{C(12,4) \times C(8,4) \times C(4,4)}{3!}$  
- C) $12!/(4!)^3$  
- D) Both B and C  

> **Answer: D** — If groups are unlabeled (interchangeable), divide by $3!$. Both B and C give $\frac{12!}{(4!)^3 \cdot 3!}$ if groups are unlabeled. If groups are labeled (Group A, B, C), the answer is A or equivalently $\frac{12!}{(4!)^3}$. Since the question says "3 groups" without labels, **B = C** = $\frac{12!}{(4!)^3 \cdot 3!} = 5775$.

---

## 🧠 Quick Tips for the Exam

> [!TIP]
> **How to identify which formula to use:**

| Clue in the Question | Formula to Use |
|----------------------|---------------|
| "How many ways to **arrange/order**..." | Permutation $P(n,r)$ |
| "How many ways to **choose/select**..." | Combination $C(n,r)$ |
| "Letters/digits **can repeat**" | $n^r$ (permutation with repetition) |
| "**At least** one/two..." | Total − complementary count |
| "**Must** have at least..." | Pigeonhole Principle $\lceil N/k \rceil$ |
| "$x_1 + x_2 + \cdots = n$" (non-negative) | Stars and bars: $C(n+k-1, k-1)$ |
| "Rearrange letters of a word" | $\frac{n!}{n_1! \cdot n_2! \cdots}$ |
| "Expand $(x+y)^n$" | Binomial Theorem |
| "Either A or B" | Inclusion-Exclusion |
| "Around a **circular table**" | $(n-1)!$ |
| "**Identical** objects to **distinct** boxes" | $C(n+r-1, r)$ |
| "**Distinct** objects to **distinct** boxes" | $k^n$ |

> [!CAUTION]
> **Common traps in MCQs:**
> - Confusing permutations (order matters) with combinations (order doesn't matter)
> - Forgetting to subtract the overlap in inclusion-exclusion problems
> - Using $n!$ instead of $(n-1)!$ for circular arrangements
> - Forgetting the constraint "at least one digit/letter" — use complementary counting
> - In stars-and-bars: using $C(n+r-1, r)$ vs $C(n+r-1, n-1)$ — they're the same thing!

---

## 📌 Summary: What to Study Tonight

If you have **limited time**, focus in this order:

1. ✅ **Permutations & Combinations formulas** — P(n,r), C(n,r), and when to use each
2. ✅ **Product Rule & Sum Rule** — the foundation
3. ✅ **Pigeonhole Principle** — easy marks if you understand the concept
4. ✅ **Binomial Theorem** — know how to expand and find specific coefficients
5. ✅ **Inclusion-Exclusion** for 2 sets
6. ✅ **Stars and Bars** ($C(n+r-1, r)$) for distribution problems
7. ✅ **Permutations with indistinguishable objects** (MISSISSIPPI-type problems)

> [!NOTE]
> All 50 questions above are based on the patterns found in [06_Counting.pdf](file:///d:/BSSE 17 1-1 Questions_/06_Counting.pdf). The questions mirror the style and difficulty level of the textbook exercises, which are the most likely source of exam questions.

Good luck on your exam! 🍀
