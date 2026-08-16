# Chapter 2: Basic Structures: Sets, Functions, Sequences, Sums, and Matrices

Much of discrete mathematics is devoted to the study of discrete structures, used to represent discrete objects. Many important discrete structures are built using sets, which are collections of objects. Among the discrete structures built from sets are combinations, unordered collections of objects used extensively in counting; relations, sets of ordered pairs that represent relationships between objects; graphs, sets of vertices and edges that connect vertices; and finite state machines, used to model computing machines. These are some of the topics we will study in later chapters.

The concept of a function is extremely important in discrete mathematics. A function assigns to each element of a first set exactly one element of a second set, where the two sets are not necessarily distinct. Functions play important roles throughout discrete mathematics. They are used to represent the computational complexity of algorithms, to study the size of sets, to count objects, and in a myriad of other ways. Useful structures such as sequences and strings are special types of functions. In this chapter, we will introduce the notion of sequences, which represent ordered lists of elements. Furthermore, we will introduce some important types of sequences and we will show how to define the terms of a sequence using earlier terms. We will also address the problem of identifying a sequence from its first few terms.

In our study of discrete mathematics, we will often add consecutive terms of a sequence of numbers. Because adding terms from a sequence, as well as other indexed sets of numbers, is such a common occurrence, a special notation has been developed for adding such terms. In this chapter, we will introduce the notation used to express summations. We will develop formulae for certain types of summations that appear throughout the study of discrete mathematics. For instance, we will encounter such summations in the analysis of the number of steps used by an algorithm to sort a list of numbers so that its terms are in increasing order.

The relative sizes of infinite sets can be studied by introducing the notion of the size, or cardinality, of a set. We say that a set is countable when it is finite or has the same size as the set of positive integers. In this chapter we will establish the surprising result that the set of rational numbers is countable, while the set of real numbers is not. We will also show how the concepts we discuss can be used to show that there are functions that cannot be computed using a computer program in any programming language.

Matrices are used in discrete mathematics to represent a variety of discrete structures. We will review the basic material about matrices and matrix arithmetic needed to represent relations and graphs. The matrix arithmetic we study will be used to solve a variety of problems involving these structures.

---

## 2.1 Sets

### 2.1.1 Introduction

> **Definition 1**  
> A **set** is an unordered collection of distinct objects, called **elements** or **members** of the set. A set is said to contain its elements. We write $a \in A$ to denote that $a$ is an element of the set $A$. The notation $a \notin A$ denotes that $a$ is not an element of the set $A$.

#### Methods of Describing Sets:
1. **Roster method:** Listing members between braces, e.g., $V = \{a, e, i, o, u\}$, $O = \{1, 3, 5, 7, 9\}$, $\{1, 2, 3, \dots, 99\}$.
2. **Set builder notation:** Characterizing members by property: $\{x \mid x \text{ has property } P\}$, e.g., $O = \{x \in \mathbf{Z}^+ \mid x \text{ is odd and } x < 10\}$.

#### Important Sets:
- $\mathbf{N} = \{0, 1, 2, 3, \dots\}$, natural numbers
- $\mathbf{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$, integers
- $\mathbf{Z}^+ = \{1, 2, 3, \dots\}$, positive integers
- $\mathbf{Q} = \{p/q \mid p \in \mathbf{Z}, q \in \mathbf{Z}, \text{ and } q \neq 0\}$, rational numbers
- $\mathbf{R}$, real numbers; $\mathbf{R}^+$, positive real numbers
- $\mathbf{C}$, complex numbers

#### Intervals:
- $[a, b] = \{x \mid a \le x \le b\}$ (closed interval)
- $[a, b) = \{x \mid a \le x < b\}$
- $(a, b] = \{x \mid a < x \le b\}$
- $(a, b) = \{x \mid a < x < b\}$ (open interval)

> **Definition 2**  
> Two sets are **equal** if and only if they have the same elements: $\forall x(x \in A \leftrightarrow x \in B)$. We write $A = B$.

> **GEORG CANTOR (1845–1918)**  
> Born in St. Petersburg, Russia; studied at Zurich and University of Berlin under Weierstrass, Kummer, and Kronecker. Assumed position at University of Halle. Founder of set theory, discovering the uncountability of $\mathbf{R}$ and founding transfinite arithmetic.

#### The Empty Set
The set with no elements is called the **empty set** or **null set**, denoted $\emptyset$ or $\{\}$. Note that $\{\emptyset\}$ is a singleton set containing one element (the empty set), so $|\{\emptyset\}| = 1 \neq |\emptyset| = 0$.

### 2.1.2 Venn Diagrams
The universal set $U$ is represented by a rectangle, and sets within $U$ are represented by circles or geometric shapes.

### 2.1.3 Subsets

> **Definition 3**  
> $A$ is a **subset** of $B$ ($A \subseteq B$, or $B \supseteq A$) if and only if every element of $A$ is also an element of $B$: $\forall x(x \in A \to x \in B)$.

> **THEOREM 1**  
> For every set $S$:  
> (i) $\emptyset \subseteq S$  
> (ii) $S \subseteq S$

- **Proper Subset:** $A \subset B$ if $A \subseteq B$ and $A \neq B$.
- **Showing Two Sets Equal:** Show $A \subseteq B$ and $B \subseteq A$.

> **BERTRAND RUSSELL (1872–1970)**  
> English philosopher, mathematician, and logician at Trinity College, Cambridge. Co-author with Alfred North Whitehead of *Principia Mathematica*. Famous for Russell’s paradox and awarded Nobel Prize in Literature in 1950.

> **JOHN VENN (1834–1923)**  
> English mathematician and fellow of Caius College, Cambridge. Clarified Boolean logic and developed Venn diagrams in his 1881 work *Symbolic Logic*.

### 2.1.4 The Size of a Set

> **Definition 4**  
> If there are exactly $n$ distinct elements in $S$ where $n$ is a nonnegative integer, $S$ is a **finite set** and $n$ is the **cardinality** of $S$, denoted $|S|$. Otherwise, $S$ is **infinite**.

### 2.1.5 Power Sets

> **Definition 6**  
> Given a set $S$, the **power set** $\mathcal{P}(S)$ is the set of all subsets of $S$. If $|S| = n$, then $|\mathcal{P}(S)| = 2^n$.

### 2.1.6 Cartesian Products

> **Definition 7**  
> The **ordered $n$-tuple** $(a_1, a_2, \dots, a_n)$ is the ordered collection with $a_1$ as first element, etc. When $n=2$, it is an **ordered pair**.

> **Definition 8**  
> The **Cartesian product** $A \times B = \{(a, b) \mid a \in A \land b \in B\}$.  
> Generalized: $A_1 \times A_2 \times \dots \times A_n = \{(a_1, a_2, \dots, a_n) \mid a_i \in A_i \text{ for } i = 1, 2, \dots, n\}$.

> **RENÉ DESCARTES (1596–1650)**  
> French mathematician and philosopher. Developed analytic geometry linking algebra and geometry (*Cartesian coordinates*).

A subset $R \subseteq A \times B$ is called a **relation** from $A$ to $B$.

---

## 2.2 Set Operations

### 2.2.1 Basic Operations
- **Union:** $A \cup B = \{x \mid x \in A \lor x \in B\}$
- **Intersection:** $A \cap B = \{x \mid x \in A \land x \in B\}$
- **Disjoint Sets:** $A \cap B = \emptyset$
- **Principle of Inclusion–Exclusion (for 2 sets):** $|A \cup B| = |A| + |B| - |A \cap B|$
- **Difference:** $A - B = \{x \mid x \in A \land x \notin B\} = A \cap \overline{B}$
- **Complement:** $\overline{A} = U - A = \{x \in U \mid x \notin A\}$

##### TABLE 1: Set Identities
| Identity | Name |
| :--- | :--- |
| $A \cap U = A$, $A \cup \emptyset = A$ | Identity laws |
| $A \cup U = U$, $A \cap \emptyset = \emptyset$ | Domination laws |
| $A \cup A = A$, $A \cap A = A$ | Idempotent laws |
| $\overline{(\overline{A})} = A$ | Complementation law |
| $A \cup B = B \cup A$, $A \cap B = B \cap A$ | Commutative laws |
| $A \cup (B \cup C) = (A \cup B) \cup C$<br>$A \cap (B \cap C) = (A \cap B) \cap C$ | Associative laws |
| $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$<br>$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ | Distributive laws |
| $\overline{A \cap B} = \overline{A} \cup \overline{B}$, $\overline{A \cup B} = \overline{A} \cap \overline{B}$ | De Morgan’s laws |
| $A \cup (A \cap B) = A$, $A \cap (A \cup B) = A$ | Absorption laws |
| $A \cup \overline{A} = U$, $A \cap \overline{A} = \emptyset$ | Complement laws |

### 2.2.2 Multisets
A **multiset** is an unordered collection allowing repeated elements: $\{m_1 \cdot a_1, m_2 \cdot a_2, \dots, m_r \cdot a_r\}$.
- **Union $P \cup Q$:** Multiplicity is $\max(m_P(a), m_Q(a))$
- **Intersection $P \cap Q$:** Multiplicity is $\min(m_P(a), m_Q(a))$
- **Difference $P - Q$:** Multiplicity is $\max(m_P(a) - m_Q(a), 0)$
- **Sum $P + Q$:** Multiplicity is $m_P(a) + m_Q(a)$

> **BHASKARACHARYA (1114–1185)**  
> Medieval Indian mathematician and astronomer who headed the observatory at Ujjain. Author of *Siddhanta Shiromani*, anticipating calculus concepts and introducing multisets.

---

## 2.3 Functions

### 2.3.1 Definitions
Let $A$ and $B$ be nonempty sets. A **function** $f: A \to B$ assigns exactly one element $b = f(a) \in B$ to each $a \in A$.
- **Domain:** $A$
- **Codomain:** $B$
- **Range:** $f(A) = \{f(a) \mid a \in A\} \subseteq B$

### 2.3.2 Properties of Functions
- **One-to-One (Injective):** $f(a) = f(b) \implies a = b$.
- **Onto (Surjective):** For every $b \in B$, there exists $a \in A$ such that $f(a) = b$.
- **Bijection (One-to-One Correspondence):** Both injective and surjective.
- **Inverse Function $f^{-1}$:** Defined if and only if $f$ is a bijection ($f^{-1}(b) = a \iff f(a) = b$).
- **Composition:** $(f \circ g)(a) = f(g(a))$.

### 2.3.3 Floor and Ceiling Functions
- **Floor function $\lfloor x \rfloor$:** Largest integer $\le x$.
- **Ceiling function $\lceil x \rceil$:** Smallest integer $\ge x$.

##### TABLE 1: Useful Properties of Floor and Ceiling Functions
- $\lfloor x \rfloor = n \iff n \le x < n + 1$
- $\lceil x \rceil = n \iff n - 1 < x \le n$
- $x - 1 < \lfloor x \rfloor \le x \le \lceil x \rceil < x + 1$
- $\lfloor -x \rfloor = -\lceil x \rceil$, $\lceil -x \rceil = -\lfloor x \rfloor$
- $\lfloor x + n \rfloor = \lfloor x \rfloor + n$, $\lceil x + n \rceil = \lceil x \rceil + n$

> **JAMES STIRLING (1692–1770)**  
> Scottish mathematician who authored *Methodus Differentialis* (1730), giving the famous Stirling’s approximation formula $n! \sim \sqrt{2\pi n}(n/e)^n$.

---

## 2.4 Sequences and Summations

### 2.4.1 Sequences
- **Geometric Progression:** $a, ar, ar^2, \dots, ar^n, \dots$
- **Arithmetic Progression:** $a, a+d, a+2d, \dots, a+nd, \dots$
- **Recurrence Relations:** E.g., Fibonacci sequence: $f_0 = 0, f_1 = 1, f_n = f_{n-1} + f_{n-2}$.

> **NEIL SLOANE (BORN 1939)**  
> Australian-American mathematician and Bell Labs researcher; founder of the *On-Line Encyclopedia of Integer Sequences (OEIS)*.

### 2.4.2 Summations

##### TABLE 2: Useful Summation Formulae
| Sum | Closed Form |
| :--- | :--- |
| $\sum_{k=0}^n ar^k$ ($r \neq 0$) | $\frac{ar^{n+1}-a}{r-1}, r \neq 1$ |
| $\sum_{k=1}^n k$ | $\frac{n(n+1)}{2}$ |
| $\sum_{k=1}^n k^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $\sum_{k=1}^n k^3$ | $\frac{n^2(n+1)^2}{4}$ |
| $\sum_{k=0}^\infty x^k$ ($|x| < 1$) | $\frac{1}{1-x}$ |
| $\sum_{k=1}^\infty kx^{k-1}$ ($|x| < 1$) | $\frac{1}{(1-x)^2}$ |

---

## 2.5 Cardinality of Sets

### 2.5.1 Countability
- $|A| = |B|$ if there is a bijection between $A$ and $B$.
- $|A| \le |B|$ if there is an injection from $A$ to $B$.
- **Countable:** Finite or countably infinite ($|S| = \aleph_0$, same cardinality as $\mathbf{Z}^+$).
- **$\mathbf{Q}$ is countable**, but **$\mathbf{R}$ is uncountable** (Cantor's diagonalization argument).

> **DAVID HILBERT (1862–1943)**  
> German mathematician at Göttingen; posed Hilbert's 23 problems in 1900 and created Hilbert's Grand Hotel paradox.

> **SCHRÖDER-BERNSTEIN THEOREM**  
> If $|A| \le |B|$ and $|B| \le |A|$, then $|A| = |B|$.

- **Continuum Hypothesis:** There is no cardinal $\mathfrak{c}$ between $\aleph_0$ and $2^{\aleph_0}$.

---

## 2.6 Matrices

### 2.6.1 Matrix Arithmetic
- **Addition:** $[a_{ij}] + [b_{ij}] = [a_{ij} + b_{ij}]$
- **Product:** $C = AB$ where $c_{ij} = \sum_{k=1}^m a_{ik} b_{kj}$
- **Identity Matrix $I_n$:** $[ \delta_{ij} ]$ where $\delta_{ij} = 1$ if $i=j$, 0 otherwise.
- **Transpose $A^t$:** $b_{ij} = a_{ji}$.
- **Symmetric Matrix:** $A = A^t$.

### 2.6.2 Zero–One Matrices
- **Join ($A \lor B$):** $(a_{ij} \lor b_{ij})$
- **Meet ($A \land B$):** $(a_{ij} \land b_{ij})$
- **Boolean Product ($A \odot B$):** $c_{ij} = \bigvee_{k=1}^m (a_{ik} \land b_{kj})$
- **Boolean Power $A^{[r]}$:** $A \odot A \odot \dots \odot A$ ($r$ times).
