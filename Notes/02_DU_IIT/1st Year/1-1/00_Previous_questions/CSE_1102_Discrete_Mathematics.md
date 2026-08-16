# CSE 1102 — Discrete Mathematics

> **Program:** BSSE 17, 16, 15, 14 | **Semester:** 1-1 | **Institute of Information Technology, University of Dhaka**
> **Complete Question Bank — Sorted by Exam**

---

## 📝 Mid Term Exam

### 17th Batch

**Marks: 15 | Duration: 1 hour**

*Instructions: Answer all of the following questions. When answering a question, please answer all the subsections together.*

**1.** Let p, q, and r be the propositions:
- p : You get an A on the final exam.
- q : You do every exercise from the reference book.
- r : You get an A in this class.

Write these propositions using p, q, and r and logical connectives (including negations): `(10)`

- **(a)** You get an A in this class, but you do not do every exercise in the book.
- **(b)** You get an A on the final, you do every exercise in the book, and you get an A in this class.
- **(c)** To get an A in this class, it is necessary for you to get an A on the final.
- **(d)** You get an A on the final, but you don't do every exercise in the book; nevertheless, you get an A in this class.
- **(e)** Getting an A on the final and doing every exercise in the book is sufficient for getting an A in this class.
- **(f)** You will get an A in this class if and only if you either do every exercise in the book or you get an A on the final.

**2.** For each of these sentences, determine whether an inclusive or, an exclusive or, is intended. Explain your answer. `(5)`

- **(a)** Experience with C++ or Java is required.
- **(b)** Lunch includes soup or salad.
- **(c)** To enter the country you need a passport or a voter registration card.
- **(d)** Publish or perish.
- **(e)** A password must have at least three digits or be at least eight characters long.

### 16th Batch

**Marks: 20 | Duration: 1 hour**

1. Define a proposition. What are the contrapositive, the converse, and the inverse of the conditional statement "If Muhammad learns discrete mathematics, then he will find a good job" [4]
2. Show that ¬(p ∨ (¬p ∧ q)) and ¬p ∧ ¬q are logically equivalent by developing a series of logical equivalences. [4]
3. Show that the premises "A student in this class has not read the Discrete ebook," and "Everyone in this class passed the Midterm exam" imply the conclusion "Someone who passed the Midterm exam has not read the Discrete ebook" [4]
4. Prove that √2 is irrational by giving a proof by contradiction. [4]
5. Find all minterms and the CNF expression from the following truth table. [4]

---

## 📝 Final Term Exam

### 17th Batch

**Marks: 60 | Duration: 3 hours**

*Instructions: Answer any 5 (five) of the following questions. When answering a question, please answer all the subsections of it at once.*

**1.**
- **(a)** Let p be "It is raining" and q be "The streets are wet." `(3)`
  - (i) Translate the following into English: ¬p → ¬q
  - (ii) Translate the following into logical notation: "The streets being wet implies that it is raining."
  - (iii) State the converse and contrapositive of the statement in part (ii).
- **(b)** Using the laws of propositional logic, prove that the following is a tautology: `(3)`
  $(p \wedge q) \to (p \vee q)$
  Show the steps and name the law used in each step.
- **(c)** Let p and q be the propositions "The election is decided" and "The votes have been counted," respectively. Express each of these compound propositions as an English sentence. `(3)`
  - (i) $p \vee q$
  - (ii) $\neg p \wedge q$
  - (iii) $q \to p$
- **(d)** Show that the following conditional statement is a tautology by using truth tables: `(3)`
  $p \to (p \vee q)$

**2.**
- **(a)** Let the domain be all integers. Define P(x): x > 0 and Q(x): x is even. `(2)`
  - (i) Translate the following into English: ∀x(Q(x) → P(x)). Is this statement true? Justify your answer.
  - (ii) Translate the following into logical notation using quantifiers: "There is an integer that is positive and even."
- **(b)** Let $f: \mathbb{Z} \to \mathbb{Z}$ be defined by $f(n) = 2n - 3$. `(6)`
  - (i) Is $f$ injective (one-to-one)? Justify.
  - (ii) Is $f$ surjective (onto)? Justify.
  - (iii) Let $g(n) = n^2$. What is $(f \circ g)(n)$?
- **(c)** What rule of inference is used in each of these arguments? `(2)`
  - (i) Kangaroos live in Australia and are marsupials. Therefore, kangaroos are marsupials.
  - (ii) It is either hotter than 100 degrees today or the pollution is dangerous. It is less than 100 degrees outside today. Therefore, the pollution is dangerous.
- **(d)** Let $A = \{1,2,3\}$, $B = \{2,3,4\}$, and $C = \{3,4,5\}$. The universal set is $U = \{1,2,3,4,5,6\}$. Find: `(2)`
  - (i) $A \cap (B \cup C)$
  - (ii) $(A \times B) \cap (B \times A)$

**3.**
- **(a)** Find tight asymptotic bound for $T(n) = 4T(n/2) + n^3$ `(4)`
- **(b)** Show that the solution of $T(n) = T(\lceil n/2 \rceil) + 1$ is $O(\lg n)$ `(4)`
- **(c)** Find the solution to recurrence: $a_n = -4a_{n-1} + 2a_{n-2} + 2^{n-3}$ `(4)`

**4.**
- **(a)** The relation R on the set $A = \{1,2,3,4\}$ is defined by: $R = \{(a, b) \mid a + b \text{ is even}\}$ `(3)`
  - (i) List all the elements of R.
  - (ii) Is R an equivalence relation?
- **(b)** Determine whether the relation on the set of all webpages is reflexive, symmetric, anti-symmetric and/or transitive, where $(a, b) \in R$ iff: `(6)`
  - (i) Everyone who visited webpage a has also visited webpage b
  - (ii) There are no common links found on both webpages a and b
  - (iii) There is at least one common link on webpages a and b
  - (iv) There is a webpage that includes links to both webpages a and b
  
  Justify your answer.
- **(c)** Consider the following two graphs, Graph A and Graph B. `(3)`
  - Graph A: A cycle (loop) with 5 vertices: a - b - c - d - e - a
  - Graph B: A star graph with 5 vertices: One central vertex connected to 4 other vertices (no other edges)
  
  Determine if the above graphs are bipartite. If one or both of them are, show a possible division of the vertices into two sets. If they are not, explain why. Based on your answers, state the key property that makes a graph bipartite.

**5.**
- **(a)** Show that the binary expansion of a positive integer can be obtained from its hexadecimal expansion by translating each hexadecimal digit into a block of four binary digits. `(4)`
- **(b)** Suppose that $a$ and $b$ are integers, $a \equiv 4 \pmod{11}$, and $b \equiv 9 \pmod{11}$. Find the integer $c$ with $0 \leq c \leq 10$ such that: `(4)`
  - (i) $c \equiv 2a + 3b \pmod{11}$
  - (ii) $c \equiv a^3 - b^3 \pmod{11}$
- **(c)** Can you find a formula or rule for the nth term of a sequence related to the prime numbers or prime factorizations so that the initial terms of the sequence have these values? `(4)`
  - (i) 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, ...
  - (ii) 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6, 2, 4, ...

**6.**
- **(a)** Define Hamilton Circuit? Show that neither graph displayed below has a Hamilton circuit. `(4)`
- **(b)** Find a shortest path between a and z in the following graph. `(4)`
- **(c)** Suppose that a connected planar simple graph has 20 vertices, each of degree 3. Into how many regions does a representation of this planar graph split the plane? `(4)`

**7.**
- **(a)** A bank is setting up a new secure vault. The access code is a 7-digit sequence using the digits 1 through 7, with the following security rules: `(3)`
  1. The code must start with an odd digit (1, 3, 5, or 7).
  2. The even digits (2, 4, 6) must appear together as a block, side-by-side, in any order amongst themselves.
  3. The digits 3 and 5 cannot be adjacent to each other anywhere in the code.
  
  How many different 7-digit access codes are possible that satisfy all these rules?

- **(b)** The National Cybersecurity Agency is forming an elite 8-person team from a pool of 15 top specialists. The pool consists of: `(4)`
  - 5 Cryptography experts (C)
  - 4 Network Security experts (N)
  - 3 Malware Analysis experts (M)
  - 3 Social Engineering experts (S)
  
  The team must be selected under the following strict conditions:
  1. The team must have at least one expert from each of the four fields.
  2. There cannot be more Cryptography experts than Network Security experts on the team.
  3. If any Malware Analysis experts are selected, then at least one Social Engineering expert must also be selected, and vice versa.
  4. The team must have either exactly 2 Cryptography experts OR exactly 3 Network Security experts (or both).
  
  How many different ways can this elite 8-person team be formed?

- **(c)** Construct a precedence graph for the following program: `(3)`
  ```
  S1: a := 5
  S2: b := 10
  S3: c := a + b
  S4: d := c * 2
  S5: e := d - 3
  S6: e := a + c
  S7: f := b / 2
  S8: g := e + f
  S9: h := g * a
  ```

- **(d)** Prove that in any group of 13 people, at least two were born in the same month. Use the pigeonhole principle to answer it. `(2)`

### 16th Batch

**Marks: 60 | Duration: 3 hours**

*Answer any five questions.*

1. a. Express the following statements using predicates and quantifiers. [3]
      "Every student in this class has studied calculus"
      "Some student in this class has visited Mexico"
      "Every student in this class has visited either Canada or Mexico"
   b. Use a truth table to verify the first De Morgan law ¬(p ∧ q) ≡ ¬p ∨ ¬q. [3]
   c. Show that the premises "If you send me an e-mail message, then I will finish writing the program," "If you do not send me an e-mail message, then I will go to sleep early," and "If I go to sleep early, then I will wake up feeling refreshed" lead to the conclusion "If I do not finish writing the program, then I will wake up feeling refreshed." [4]
   d. What are Universal modus ponens and tollens rules? [2]

2. a. Prove that if n is an integer and 3n + 2 is odd, then n is odd. [3]
   b. Let A, B, and C be sets. Show that A ∪ (B ∩ C) = (C ∪ B) ∩ A. [3]
   c. Define fallacy of affirming the conclusion. Give an example. [2]
   d. Define proper subset using implication and quantifiers. What is the Cartesian product A × B × C, where A = {1, 2}, B = {2, 3}, and C = {1, 2, 3}? [4]

3. a. Consider the following relations on {1, 2, 3, 4}: [6]
      R1 = {(1,1),(1,2),(2,1),(2,2),(3,4),(4,1),(4,4)}
      R2 = {(1,1),(1,2),(2,1)}
      R3 = {(1,1),(1,2),(1,4),(2,1),(2,2),(3,3),(4,1),(4,4)}
      R4 = {(2,1),(3,1),(3,2),(4,1),(4,2),(4,3)}
      R5 = {(1,1),(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)}
      R6 = {(3,4)}
      Which of these are reflexive, symmetric, anti-symmetric, and transitive?
   b. What is recurrence relation? Express Fibonacci sequence using recurrence relation. [2]
   c. Use mathematical Induction to prove that 2n < n! for every integer n with n ≥ 4. [3]
   d. What is a well-ordered set? Give example. [1]

4. a. Suppose that the relations R1 and R2 on a set A are represented by the matrices M_R1 and M_R2. What are the matrices representing R1 ∪ R2 and R1 ∩ R2? [4]
   b. Identify following as one-to-one, onto, both, neither, or not a function. [5]
   c. Find the adjacency matrix of the given directed multigraph. [3]

5. a. How many bit strings are there of length six or less, not counting the empty string? [2]
   b. How many bit strings of length ten both begin and end with a 1? [2]
   c. How many license plates consisting of three letters followed by three digits contain no letter or digit twice? [3]
   d. Use binomial theorem to determine the coefficient of x^7 in (1+x)^11 [2]
   e. A coin is flipped eight times: i. total outcomes? ii. exactly three heads? iii. at least three heads? [3]

6. a. Construct a precedence graph for the following program. [4]
   b. Bipartite matching problem with employees and responsibilities. [8]
   c. i. How many edges does a full binary tree with 1000 internal vertices have? ii. How many leaves does a full 3-ary tree with 100 vertices have? [6]
   d. Perform Preorder traversal of the following tree. [6]

### 15th Batch

**Marks: 60 | Duration: 3 hours**

*Answer any 5 out of 7 questions.*

1. a) Use rules of inference to show that "If it does not rain or if it is not foggy, then the cricket final will be held," "If the cricket final is held, then the trophy will be awarded," and "The trophy was not awarded" imply "It rained."
   b) Write first-order logic: i. "For every food, there is a person who likes that food." ii. "There is a food that every person likes." iii. "For every person, there is a food that the person likes." [3]
   c) Prove that m² = n² iff m = n or m = -n. [3]
   d) Give an explicit formula for a function from Z to Z+ that is: i. one-to-one but not onto, ii. onto but not one-to-one, iii. one-to-one and onto, iv. neither. [2]

2. a) Let C(x, y) mean "student x is enrolled in course y". Express each in English: i. ∃x(C(x, Math 222) ∧ C(x, CS 252)) ii. ∃x∃y∀z((x ≠ y) ∧ (C(x,z) → C(y,z))) iii. ∀x∀z∃y((x ≠ z) → ¬(C(x,y) ∧ C(z,y))) [3]
   b) Use induction to prove 3 + 3·5 + 3·5² + ... + 3·5ⁿ = 3(5^(n+1) - 1)/4. [3]
   c) Use strong induction to show that if you can run one mile or two miles, and can always run two more miles, then you can run any number of miles. [3]
   d) Determine truth value with domain = all reals: i. ∃x(x²=2) ii. ∃x(x²=-1) iii. ∀x(x²+2≥1) iv. ∃x(x⁴<x²) v. ∀x((-x)²=x²) vi. ∀x(2x>x) [3]

3. a) Use Huffman coding to encode symbols: a:0.20, b:0.10, c:0.15, d:0.25, e:0.30. Average bits? [6]
   b) Devise a recursive algorithm for computing b^n mod m. [6]

4. a) Determine whether relation R on set of all people is reflexive, symmetric, antisymmetric, transitive, where (x,y)∈R iff: i. x is parent of y, ii. x is sibling of y. [varies]
   b) Determine whether given pair of graphs is isomorphic. [varies]
   c) Find vertex connectivity and edge connectivity of given graphs. [varies]

5. a) Find smallest relation containing {(1,2),(1,4),(3,3),(4,1)} that is: i. reflexive and transitive, ii. symmetric and transitive, iii. reflexive, symmetric, and transitive. [3]
   b) Build BST for words: oenology, phrenology, campanology, ornithology, ichthyology, limnology, alchemy, astrology. [3]
   c) Determine preorder and inorder traversal of given tree. [4]
   d) Give example of relation that is: i. both symmetric and antisymmetric, ii. neither symmetric nor antisymmetric. [2]

6. a) Pigeonhole: cricket team plays at least 1 game/day, no more than 45 in 30 days. Show consecutive days with exactly 14 games. [3]
   b) License plate: 6 alphanumeric, first 2 or 3 uppercase, rest digits. Total possible? [3]
   c) BFS from node i to produce spanning tree. [varies]
   d) Draw all spanning trees of given simple graph. [2]

7. a) Solutions to x1+x2+x3+x4=17, nonneg integers? [3]
   b) 14 children with identical triplets/twins, seating arrangements? [3]
   c) Euler circuit/path in given graph? [3]
   d) Define bipartite graph, example, two real-life applications. [3]

### 14th Batch

**Marks: 60 | Duration: 3 hours**

*Answer any FIVE questions*

1. (a) Let A={1,2,3,4} and B={a,b,c}. Determine which are functions, one-to-one or onto. (4)
   (b) Find inverse of f(x)=(2x+1)/(x-3) and verify. (4)
   (c) f: Z→Z, f(x)=3x-2. Is f injective/surjective/bijective? (4)

2. (a) Define equivalence relation. Prove aRb if a≡b(mod 3) is equivalence on Z. (5)
   (b) Draw Hasse diagram for ({1,2,3,4,5,6,10,12,15,30,60}, |). (4)
   (c) Number of relations from 3-element to 4-element set? (3)

3. (a) Prove by induction: 1²+2²+...+n²=n(n+1)(2n+1)/6. (6)
   (b) Define recurrence relation. Solve aₙ=3aₙ₋₁, a₀=2. (6)

4. (a) Define planar graph. Prove K₃,₃ is non-planar using Euler's formula. (5)
   (b) MST using Kruskal's algorithm. (4)
   (c) Define Hamiltonian graph. Example with Hamilton cycle but no Euler circuit. (3)

5. (a) State and prove Pigeonhole Principle. (4)
   (b) Bit strings of length 8 starting with "1" or ending with "00"? (4)
   (c) Committee of 5 from 6 men, 4 women, at least 3 men? (4)

6. (a) Truth table for (p→q)∧(q→r)→(p→r). Tautology? (5)
   (b) Show ¬(p→q) ≡ p∧¬q. (4)
   (c) Translate to predicate logic: i. "Every student passed" ii. "Some study both Math and CS". (3)

7. (a) What is a tree? Prove n vertices → n-1 edges. (5)
   (b) Define graph isomorphism. Determine if two graphs are isomorphic. (4)
   (c) Chromatic number of Petersen graph. (3)
