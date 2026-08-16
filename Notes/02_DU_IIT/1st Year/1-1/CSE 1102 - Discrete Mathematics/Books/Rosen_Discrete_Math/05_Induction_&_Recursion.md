# Chapter 5: Induction and Recursion

Many mathematical statements assert that a property is true for all positive integers. Examples of such statements are that for every positive integer $n$: $n! \le n^n$, $n^3 - n$ is divisible by 3; a set with $n$ elements has $2^n$ subsets; and the sum of the first $n$ positive integers is $n(n + 1)/2$. A major goal of this chapter, and the book, is to provide a thorough understanding of mathematical induction, which is used to prove results of this kind.

Proofs using mathematical induction have two parts. First, they show that the statement holds for the positive integer 1. Second, they show that if the statement holds for a positive integer then it must also hold for the next larger integer. Mathematical induction is based on the rule of inference that tells us that if $P(1)$ and $\forall k(P(k) \to P(k + 1))$ are true for the domain of positive integers, then $\forall n P(n)$ is true. Mathematical induction can be used to prove a tremendous variety of results. Understanding how to read and construct proofs by mathematical induction is a key goal of learning discrete mathematics.

In Chapter 2 we explicitly defined sets and functions. That is, we described sets by listing their elements or by giving some property that characterizes these elements. We gave formulae for the values of functions. There is another important way to define such objects, based on mathematical induction. To define functions, some initial terms are specified, and a rule is given for finding subsequent values from values already known. (We briefly touched on this sort of definition in Chapter 2 when we showed how sequences can be defined using recurrence relations.) Sets can be defined by listing some of their elements and giving rules for constructing elements from those already known to be in the set. Such definitions, called **recursive definitions**, are used throughout discrete mathematics and computer science. Once we have defined a set recursively, we can use a proof method called **structural induction** to prove results about this set.

When a procedure is specified for solving a problem, this procedure must always solve the problem correctly. Just testing to see that the correct result is obtained for a set of input values does not show that the procedure always works correctly. The correctness of a procedure can be guaranteed only by proving that it always yields the correct result. The final section of this chapter contains an introduction to the techniques of program verification. This is a formal technique to verify that procedures are correct. Program verification serves as the basis for attempts under way to prove in a mechanical fashion that programs are correct.

---

## 5.1 Mathematical Induction

### 5.1.1 Principle of Mathematical Induction

> **PRINCIPLE OF MATHEMATICAL INDUCTION**  
> To prove that $P(n)$ is true for all positive integers $n$, where $P(n)$ is a propositional function, complete two steps:  
> 1. **BASIS STEP:** Verify that $P(1)$ is true.  
> 2. **INDUCTIVE STEP:** Show that the conditional statement $P(k) \to P(k + 1)$ is true for all positive integers $k$.

Rule of Inference form:
$$[P(1) \land \forall k(P(k) \to P(k + 1))] \to \forall n P(n)$$

- **Inductive Hypothesis:** The assumption that $P(k)$ is true.
- **Validity:** Follows from the **Well-Ordering Property** for the set of positive integers (every nonempty subset of $\mathbf{Z}^+$ has a least element).

> **FRANCESCO MAUROLICO (1494–1575)**  
> 16th-century mathematician from Messina who devised the method of mathematical induction in *Arithmeticorum Libri Duo*. Augustus De Morgan formalized the proofs in 1838.

### 5.1.2 Examples of Mathematical Induction
1. **Sum of first $n$ integers:** $\sum_{i=1}^n i = \frac{n(n+1)}{2}$.
2. **Sum of first $n$ odd positive integers:** $\sum_{i=1}^n (2i-1) = n^2$.
3. **Geometric series sum:** $\sum_{j=0}^n ar^j = \frac{ar^{n+1}-a}{r-1}$ for $r \neq 1$.
4. **Inequalities:** $n < 2^n$ for all $n \ge 1$; $2^n < n!$ for all $n \ge 4$.
5. **Harmonic Numbers:** $H_{2^n} \ge 1 + \frac{n}{2}$.
6. **Divisibility:** $3 \mid (n^3 - n)$ for all $n \ge 1$; $57 \mid (7^{n+2} + 8^{2n+1})$ for all $n \ge 0$.
7. **Sets:** A set with $n$ elements has $2^n$ subsets.
8. **Generalized De Morgan's Law:** $\overline{\bigcap_{j=1}^n A_j} = \bigcup_{j=1}^n \overline{A_j}$.
9. **Tiling:** Every $2^n \times 2^n$ checkerboard with one square removed can be tiled using right triominoes.

---

## 5.2 Strong Induction and Well-Ordering

### 5.2.1 Strong Induction (Complete Induction)

> **STRONG INDUCTION**  
> To prove that $P(n)$ is true for all positive integers $n$:  
> 1. **BASIS STEP:** Verify that $P(1)$ is true.  
> 2. **INDUCTIVE STEP:** Show that $[P(1) \land P(2) \land \dots \land P(k)] \to P(k + 1)$ is true for all positive integers $k$.

*Equivalence:* Mathematical Induction, Strong Induction, and the Well-Ordering Property are all logically equivalent.

### 5.2.2 Examples
1. **Fundamental Theorem of Arithmetic (Existence):** Every integer $n > 1$ can be written as a product of primes.
2. **Postage Problem:** Every postage of $n \ge 12$ cents can be formed using 4-cent and 5-cent stamps.
3. **Polygon Triangulation:**
   > **THEOREM 1**  
   > A simple polygon with $n$ sides ($n \ge 3$) can be triangulated into $n - 2$ triangles.

### 5.2.3 Proofs Using Well-Ordering
- Proof of the Division Algorithm ($a = dq + r$, $0 \le r < d$).
- Round-robin tournament cycle theorem.

---

## 5.3 Recursive Definitions and Structural Induction

### 5.3.1 Recursively Defined Functions
1. **Basis Step:** Specify $f(0)$.
2. **Recursive Step:** Rule for finding $f(n + 1)$ from $f(0), \dots, f(n)$.

> **GABRIEL LAMÉ (1795–1870)**  
> Proved **Lamé's Theorem**: The number of divisions used by the Euclidean algorithm to find $\gcd(a, b)$ with $a \ge b$ is $\le 5 \times (\text{number of decimal digits in } b)$, which is $O(\log b)$.

### 5.3.2 Recursively Defined Sets and Structures
- **Strings $\Sigma^*$:** $\lambda \in \Sigma^*$; if $w \in \Sigma^*$ and $x \in \Sigma$, then $wx \in \Sigma^*$.
- **Length:** $l(\lambda) = 0$, $l(wx) = l(w) + 1$.
- **Rooted Trees:** Single vertex $r$ is a rooted tree; connecting new root $r$ to roots of disjoint trees $T_1, \dots, T_n$ forms a rooted tree.
- **Full Binary Trees:** Root vertex $r$; combination $T_1 \cdot T_2$ where $T_1, T_2$ are full binary trees.
  - Height: $h(T) = 1 + \max(h(T_1), h(T_2))$.
  - Vertices: $n(T) = 1 + n(T_1) + n(T_2)$.
  - Bound: $n(T) \le 2^{h(T)+1} - 1$.

### 5.3.3 Structural Induction
To prove property $P$ for recursively defined set $S$:
1. **Basis Step:** Show $P(x)$ holds for all elements $x$ in the basis step.
2. **Recursive Step:** Show that if $P$ holds for elements used to construct new elements, $P$ holds for the newly constructed elements.

---

## 5.4 Recursive Algorithms

An algorithm is **recursive** if it solves a problem by reducing it to an instance of the same problem with smaller input.

```pascal
ALGORITHM 1 Factorial.
procedure factorial(n: nonnegative integer)
  if n = 0 then return 1
  else return n * factorial(n - 1)
```

```pascal
ALGORITHM 3 Recursive GCD.
procedure gcd(a, b: nonnegative integers with a < b)
  if a = 0 then return b
  else return gcd(b mod a, a)
```

```pascal
ALGORITHM 4 Recursive Modular Exponentiation.
procedure mpower(b, n, m: integers with b > 0, m >= 2, n >= 0)
  if n = 0 then return 1
  else if n is even then return mpower(b, n/2, m)^2 mod m
  else return (mpower(b, floor(n/2), m)^2 mod m * b mod m) mod m
```

### Merge Sort
```pascal
ALGORITHM 9 Recursive Merge Sort.
procedure mergesort(L = a1, ..., an)
  if n > 1 then
    m := floor(n / 2)
    L1 := a1, ..., am
    L2 := am+1, ..., an
    L := merge(mergesort(L1), mergesort(L2))
  {L is sorted in nondecreasing order}
```
*Complexity:* $\Theta(n \log n)$ comparisons.

---

## 5.5 Program Correctness

### 5.5.1 Hoare Triples & Partial Correctness

> **Definition 1**  
> $p\{S\}q$ (**Hoare Triple**): If initial assertion $p$ is true for input values and $S$ terminates, then final assertion $q$ is true for output values.

> **SIR C. ANTHONY R. HOARE (BORN 1934)**  
> 1980 ACM Turing Award winner, invented quicksort and axiomatic semantics (Hoare logic).

### 5.5.2 Rules of Inference for Program Verification
- **Composition Rule:**
  $$\frac{p\{S_1\}q, \quad q\{S_2\}r}{p\{S_1; S_2\}r}$$
- **Conditional Statement (`if condition then S`):**
  $$\frac{(p \land \text{condition})\{S\}q, \quad (p \land \neg\text{condition}) \to q}{p\{\text{if condition then } S\}q}$$
- **Loop Invariant (`while condition S`):**
  $$\frac{(p \land \text{condition})\{S\}p}{p\{\text{while condition } S\}(\neg\text{condition} \land p)}$$
