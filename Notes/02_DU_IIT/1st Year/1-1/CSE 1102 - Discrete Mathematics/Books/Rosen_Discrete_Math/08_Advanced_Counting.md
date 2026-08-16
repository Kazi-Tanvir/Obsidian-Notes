# CHAPTER 8: Advanced Counting Techniques

- **8.1 Applications of Recurrence Relations**
- **8.2 Solving Linear Recurrence Relations**
- **8.3 Divide-and-Conquer Algorithms and Recurrence Relations**
- **8.4 Generating Functions**
- **8.5 Inclusion–Exclusion**
- **8.6 Applications of Inclusion–Exclusion**

Many counting problems cannot be solved easily using the methods discussed in Chapter 6. One such problem is: How many bit strings of length $n$ do not contain two consecutive zeros? To solve this problem, let $a_n$ be the number of such strings of length $n$. An argument can be given that shows that the sequence $\{a_n\}$ satisfies the recurrence relation $a_{n+1} = a_n + a_{n-1}$ and the initial conditions $a_1 = 2$ and $a_2 = 3$. This recurrence relation and the initial conditions determine the sequence $\{a_n\}$. Moreover, an explicit formula can be found for $a_n$ from the equation relating the terms of the sequence. As we will see, a similar technique can be used to solve many different types of counting problems.

We will discuss two ways that recurrence relations play important roles in the study of algorithms. First, we will introduce an important algorithmic paradigm known as dynamic programming. Algorithms that follow this paradigm break down a problem into overlapping subproblems. The solution to the problem is then found from the solutions to the subproblems through the use of a recurrence relation. Second, we will study another important algorithmic paradigm, divide-and-conquer. Algorithms that follow this paradigm can be used to solve a problem by recursively breaking it into a fixed number of nonoverlapping subproblems until these problems can be solved directly. The complexity of such algorithms can be analyzed using a special type of recurrence relation. In this chapter we will discuss a variety of divide-and-conquer algorithms and analyze their complexity using recurrence relations.

We will also see that many counting problems can be solved using formal power series, called generating functions, where the coefficients of powers of $x$ represent terms of the sequence we are interested in. Besides solving counting problems, we will also be able to use generating functions to solve recurrence relations and to prove combinatorial identities.

Many other kinds of counting problems cannot be solved using the techniques discussed in Chapter 6, such as: How many ways are there to assign seven jobs to three employees so that each employee is assigned at least one job? How many primes are there less than 1000? Both of these problems can be solved by counting the number of elements in the union of sets. We will develop a technique, called the principle of inclusion–exclusion, that counts the number of elements in a union of sets, and we will show how this principle can be used to solve counting problems.

The techniques studied in this chapter, together with the basic techniques of Chapter 6, can be used to solve many counting problems.

---

## 8.1 Applications of Recurrence Relations

### 8.1.1 Introduction

Recall from Chapter 2 that a recursive definition of a sequence specifies one or more initial terms and a rule for determining subsequent terms from those that precede them. Also, recall that a rule of the latter sort (whether or not it is part of a recursive definition) is called a recurrence relation and that a sequence is called a solution of a recurrence relation if its terms satisfy the recurrence relation.

In this section we will show that such relations can be used to study and to solve counting problems. For example, suppose that the number of bacteria in a colony doubles every hour. If a colony begins with five bacteria, how many will be present in $n$ hours? To solve this problem, let $a_n$ be the number of bacteria at the end of $n$ hours. Because the number of bacteria doubles every hour, the relationship $a_n = 2a_{n-1}$ holds whenever $n$ is a positive integer. This recurrence relation, together with the initial condition $a_0 = 5$, uniquely determines $a_n$ for all nonnegative integers $n$. We can find a formula for $a_n$ using the iterative approach followed in Chapter 2, namely that $a_n = 5 \cdot 2^n$ for all nonnegative integers $n$.

Some of the counting problems that cannot be solved using the techniques discussed in Chapter 6 can be solved by finding recurrence relations involving the terms of a sequence, as was done in the problem involving bacteria. In this section we will study a variety of counting problems that can be modeled using recurrence relations. In Chapter 2 we developed methods for solving certain recurrence relation. In Section 8.2 we will study methods for finding explicit formulae for the terms of sequences that satisfy certain types of recurrence relations.

We conclude this section by introducing the algorithmic paradigm of dynamic programming. After explaining how this paradigm works, we will illustrate its use with an example.

---

### 8.1.2 Modeling With Recurrence Relations

We can use recurrence relations to model a wide variety of problems, such as finding compound interest (see Example 11 in Section 2.4), counting rabbits on an island, determining the number of moves in the Tower of Hanoi puzzle, and counting bit strings with certain properties.

#### EXAMPLE 1: Rabbits and the Fibonacci Numbers
Consider this problem, which was originally posed by Leonardo Pisano, also known as Fibonacci, in the thirteenth century in his book *Liber Abaci*. A young pair of rabbits (one of each sex) is placed on an island. A pair of rabbits does not breed until they are 2 months old. After they are 2 months old, each pair of rabbits produces another pair each month, as shown in Figure 1. Find a recurrence relation for the number of pairs of rabbits on the island after $n$ months, assuming that no rabbits ever die.

| Month | Reproducing pairs (at least 2 months old) | Young pairs (less than 2 months old) | Total pairs |
| :---: | :---: | :---: | :---: |
| 1 | 0 | 1 | 1 |
| 2 | 0 | 1 | 1 |
| 3 | 1 | 1 | 2 |
| 4 | 1 | 2 | 3 |
| 5 | 2 | 3 | 5 |
| 6 | 3 | 5 | 8 |

**Solution:** Denote by $f_n$ the number of pairs of rabbits after $n$ months. We will show that $f_n, n = 1, 2, 3, \dots$, are the terms of the Fibonacci sequence.  
The rabbit population can be modeled using a recurrence relation. At the end of the first month, the number of pairs of rabbits on the island is $f_1 = 1$. Because this pair does not breed during the second month, $f_2 = 1$ also. To find the number of pairs after $n$ months, add the number on the island the previous month, $f_{n-1}$, and the number of newborn pairs, which equals $f_{n-2}$, because each newborn pair comes from a pair at least 2 months old.  
Consequently, the sequence $\{f_n\}$ satisfies the recurrence relation
$$f_n = f_{n-1} + f_{n-2}$$
for $n \ge 3$ together with the initial conditions $f_1 = 1$ and $f_2 = 1$. Because this recurrence relation and the initial conditions uniquely determine this sequence, the number of pairs of rabbits on the island after $n$ months is given by the $n$th Fibonacci number. $\blacktriangleleft$

#### EXAMPLE 2: The Tower of Hanoi Puzzle
A popular puzzle of the late nineteenth century invented by the French mathematician Édouard Lucas, called the Tower of Hanoi, consists of three pegs mounted on a board together with disks of different sizes. Initially these disks are placed on the first peg in order of size, with the largest on the bottom. The rules of the puzzle allow disks to be moved one at a time from one peg to another as long as a disk is never placed on top of a smaller disk. The goal of the puzzle is to have all the disks on the second peg in order of size, with the largest on the bottom.  
Let $H_n$ denote the number of moves needed to solve the Tower of Hanoi puzzle with $n$ disks. Set up a recurrence relation for the sequence $\{H_n\}$.

**Solution:** Begin with $n$ disks on peg 1. We can transfer the top $n - 1$ disks, following the rules of the puzzle, to peg 3 using $H_{n-1}$ moves. We keep the largest disk fixed during these moves. Then, we use one move to transfer the largest disk to the second peg. Finally, we transfer the $n - 1$ disks on peg 3 to peg 2 using $H_{n-1}$ moves, placing them on top of the largest disk, which always stays fixed on the bottom of peg 2. This shows that we can solve the Tower of Hanoi puzzle for $n$ disks using $2H_{n-1} + 1$ moves.  
We now show that we cannot solve the puzzle for $n$ disks using fewer than $2H_{n-1} + 1$ moves. Note that when we move the largest disk, we must have already moved the $n - 1$ smaller disks onto a peg other than peg 1. Doing so requires at least $H_{n-1}$ moves. Another move is needed to transfer the largest disk. Finally, at least $H_{n-1}$ more moves are needed to put the $n - 1$ smallest disks back on top of the largest disk. Adding the number of moves required gives us the desired lower bound.  
We conclude that
$$H_n = 2H_{n-1} + 1.$$
The initial condition is $H_1 = 1$, because one disk can be transferred from peg 1 to peg 2 in one move.  
Using iteration:
$$\begin{aligned}
H_n &= 2H_{n-1} + 1 \\
&= 2(2H_{n-2} + 1) + 1 = 2^2 H_{n-2} + 2 + 1 \\
&= 2^2(2H_{n-3} + 1) + 2 + 1 = 2^3 H_{n-3} + 2^2 + 2 + 1 \\
&\;\;\vdots \\
&= 2^{n-1}H_1 + 2^{n-2} + \dots + 2 + 1 \\
&= 2^{n-1} + 2^{n-2} + \dots + 2 + 1 = 2^n - 1.
\end{aligned}$$
For 64 gold disks, the monks require $2^{64} - 1 = 18,446,744,073,709,551,615$ moves. At one move per second, it will take them more than 500 billion years. $\blacktriangleleft$

#### EXAMPLE 3
Find a recurrence relation and give initial conditions for the number of bit strings of length $n$ that do not have two consecutive 0s. How many such bit strings are there of length five?

**Solution:** Let $a_n$ denote the number of bit strings of length $n$ with no two consecutive 0s.  
Bit strings of length $n$ ending in 1 are obtained by appending 1 to a valid string of length $n - 1$ ($a_{n-1}$ ways).  
Bit strings of length $n$ ending in 0 must have 1 in the $(n - 1)$st position, so they are obtained by appending 10 to a valid string of length $n - 2$ ($a_{n-2}$ ways).  
Thus,
$$a_n = a_{n-1} + a_{n-2} \quad\text{for } n \ge 3.$$
Initial conditions: $a_1 = 2$ (strings: 0, 1) and $a_2 = 3$ (strings: 01, 10, 11).  
Using the recurrence relation:
$$\begin{aligned}
a_3 &= a_2 + a_1 = 3 + 2 = 5, \\
a_4 &= a_3 + a_2 = 5 + 3 = 8, \\
a_5 &= a_4 + a_3 = 8 + 5 = 13. \quad\blacktriangleleft
\end{aligned}$$

#### EXAMPLE 4: Codeword Enumeration
A computer system considers a string of decimal digits a valid codeword if it contains an even number of 0 digits. Let $a_n$ be the number of valid $n$-digit codewords. Find a recurrence relation for $a_n$.

**Solution:** $a_1 = 9$ (digits 1–9). A valid $n$-digit string can be obtained by:
1. Appending any digit from 1–9 to a valid $(n-1)$-digit string: $9a_{n-1}$ ways.
2. Appending 0 to an invalid $(n-1)$-digit string: $(10^{n-1} - a_{n-1})$ ways.  
Thus,
$$a_n = 9a_{n-1} + (10^{n-1} - a_{n-1}) = 8a_{n-1} + 10^{n-1}. \quad\blacktriangleleft$$

#### EXAMPLE 5
Find a recurrence relation for $C_n$, the number of ways to parenthesize the product of $n + 1$ numbers, $x_0 \cdot x_1 \cdot x_2 \cdots x_n$, to specify the order of multiplication.

**Solution:** The final multiplication operator appears between $x_k$ and $x_{k+1}$ for some $k \in \{0, 1, \dots, n-1\}$. There are $C_k$ ways to parenthesize the first $k + 1$ numbers and $C_{n-k-1}$ ways for the remaining $n - k$ numbers. Summing over all $k$:
$$C_n = \sum_{k=0}^{n-1} C_k C_{n-k-1} \quad\text{with } C_0 = 1, C_1 = 1.$$
$C_n$ are the **Catalan numbers**, with explicit formula $C_n = \frac{1}{n+1}\binom{2n}{n}$. $\blacktriangleleft$

> **EUGÈNE CHARLES CATALAN (1814–1894)**  
> Belgian-French mathematician who studied at École Polytechnique, worked in Paris and Liège, and contributed to number theory, continued fractions, and combinatorics.

---

### 8.1.3 Algorithms and Recurrence Relations

#### DYNAMIC PROGRAMMING
An algorithm follows the dynamic programming paradigm when it recursively breaks down a problem into simpler overlapping subproblems, and computes the solution using the solutions of the subproblems, storing results (memoization) to avoid redundant computation.

> **RICHARD BELLMAN (1920–1984)**  
> American mathematician at the RAND Corporation and USC who invented dynamic programming and the Bellman equation.

#### ALGORITHM 1: Dynamic Programming Algorithm for Scheduling Talks
```pascal
procedure Maximum Attendees (s1, s2, ..., sn: start times of talks;
                             e1, e2, ..., en: end times of talks;
                             w1, w2, ..., wn: number of attendees to talks)
sort talks by end time and relabel so that e1 <= e2 <= ... <= en
for j := 1 to n
    if no job i with i < j is compatible with job j
        p(j) := 0
    else
        p(j) := max{i | i < j and job i is compatible with job j}
T(0) := 0
for j := 1 to n
    T(j) := max(wj + T(p(j)), T(j - 1))
return T(n) {T(n) is the maximum number of attendees}
```

---

### Exercises 8.1

1. Use mathematical induction to verify the formula derived in Example 2 for the number of moves required to complete the Tower of Hanoi puzzle.
2. a) Find a recurrence relation for the number of permutations of a set with $n$ elements.  
   b) Use this recurrence relation to find the number of permutations of a set with $n$ elements using iteration.
3. A vending machine dispensing books of stamps accepts only one-dollar coins, $1 bills, and $5 bills.  
   a) Find a recurrence relation for the number of ways to deposit $n$ dollars in the vending machine, where the order matters.  
   b) What are the initial conditions?  
   c) How many ways are there to deposit $10 for a book of stamps?
4. A country uses coins of 1, 2, 5, and 10 pesos and bills of 5, 10, 20, 50, and 100 pesos. Find a recurrence relation for paying a bill of $n$ pesos when order matters.
5. How many ways are there to pay a bill of 17 pesos using the currency in Exercise 4?
6. $*\,$ a) Find a recurrence relation for the number of strictly increasing sequences of positive integers with $a_1 = 1$ and $a_k = n$.  
   b) What are the initial conditions?  
   c) How many sequences are there when $n \ge 2$?
7. a) Find a recurrence relation for the number of bit strings of length $n$ that contain a pair of consecutive 0s.  
   b) What are the initial conditions?  
   c) How many bit strings of length seven contain two consecutive 0s?
8. a) Find a recurrence relation for the number of bit strings of length $n$ containing three consecutive 0s.  
   b) What are the initial conditions?  
   c) How many bit strings of length seven contain three consecutive 0s?
9. a) Find a recurrence relation for the number of bit strings of length $n$ that do not contain three consecutive 0s.  
   b) What are the initial conditions?  
   c) How many bit strings of length seven do not contain three consecutive 0s?
10. $*\,$ a) Find a recurrence relation for the number of bit strings of length $n$ containing the string 01.  
    b) What are the initial conditions?  
    c) How many bit strings of length seven contain the string 01?
11. a) Find a recurrence relation for the number of ways to climb $n$ stairs taking 1 or 2 stairs at a time.  
    b) What are the initial conditions?  
    c) In how many ways can this person climb a flight of 8 stairs?
12. a) Find a recurrence relation for climbing $n$ stairs taking 1, 2, or 3 stairs at a time.  
    b) What are the initial conditions?  
    c) In how many ways can this person climb a flight of 8 stairs?
13. a) Find a recurrence relation for the number of ternary strings of length $n$ not containing two consecutive 0s.  
    b) What are the initial conditions?  
    c) How many ternary strings of length 6 do not contain two consecutive 0s?
14. a) Find a recurrence relation for the number of ternary strings of length $n$ containing two consecutive 0s.  
    b) What are the initial conditions?  
    c) How many ternary strings of length 6 contain two consecutive 0s?
15. $*\,$ a) Find a recurrence relation for ternary strings of length $n$ not containing two consecutive 0s or two consecutive 1s.  
    b) What are the initial conditions?  
    c) How many such ternary strings of length 6 are there?
16. $*\,$ a) Find a recurrence relation for ternary strings of length $n$ containing either two consecutive 0s or two consecutive 1s.  
    b) What are the initial conditions?  
    c) How many such ternary strings of length 6 are there?
17. $*\,$ a) Find a recurrence relation for ternary strings of length $n$ not containing consecutive symbols that are the same.  
    b) What are the initial conditions?  
    c) How many such strings of length 6 are there?
18. $**\,$ a) Find a recurrence relation for ternary strings of length $n$ containing two consecutive symbols that are the same.  
    b) What are the initial conditions?  
    c) How many such strings of length 6 are there?
19. Messages using two signals of duration 1 microsecond and 2 microseconds:  
    a) Find a recurrence relation for messages of length $n$ microseconds.  
    b) What are the initial conditions?  
    c) How many messages can be sent in 10 microseconds?
20. Paying bus toll in nickels and dimes:  
    a) Find a recurrence relation for toll of $n$ cents.  
    b) How many ways to pay 45 cents?
21. a) Recurrence relation for regions $R_n$ dividing a plane by $n$ lines (no two parallel, no three concurrent).  
    b) Find $R_n$ using iteration.
22. $*\,$ Surface of sphere divided by $n$ great circles: find recurrence and solve by iteration.
23. $*\,$ 3D space divided by $n$ planes: find recurrence and solve by iteration.
24. Find a recurrence relation for bit strings of length $n$ with an even number of 0s.
25. How many bit sequences of length 7 contain an even number of 0s?
26. Covering a $2 \times n$ checkerboard with $1 \times 2$ dominoes:  
    a) Find recurrence relation.  
    b) Find initial conditions.  
    c) Ways to cover a $2 \times 17$ board.
27. Laying out a walkway with red, green, or gray tiles where no two red tiles are adjacent:  
    a) Find recurrence relation.  
    b) Find initial conditions.  
    c) Ways to lay out path of 7 tiles.
28. Show $f_n = 5f_{n-4} + 3f_{n-5}$ for Fibonacci numbers and prove $f_{5n}$ is divisible by 5.
29. $*\,$ Recurrence relation for onto functions $S(m, n) = n^m - \sum_{k=1}^{n-1} \binom{n}{k}S(m, k)$.
30. Parenthesizing $x_0 \cdot x_1 \cdot x_2 \cdot x_3 \cdot x_4$: list all ways, calculate $C_4$, and verify formula.
31. Calculate $C_5$ using recurrence and closed formula.
32. $*\,$ Tower of Hanoi with no direct moves between peg 1 and 3 (all moves via peg 2).
33–37. Josephus problem variations: finding $J(n)$, proving recurrence $J(2n) = 2J(n) - 1$, $J(2n+1) = 2J(n) + 1$, and computing $J(100), J(1000), J(10,000)$.
38–45. Reve’s puzzle (4 pegs, $n$ disks) and Frame–Stewart algorithm analysis.
46–52. Backward differences $\nabla a_n = a_n - a_{n-1}$, difference equations.
53–55. Talk scheduling dynamic programming implementation.
56. Maximum subarray sum dynamic programming algorithm.
57. $*\,$ Matrix-chain multiplication dynamic programming algorithm.

---

## 8.2 Solving Linear Recurrence Relations

### 8.2.1 Definitions and Properties

> **DEFINITION 1**  
> A **linear homogeneous recurrence relation of degree $k$ with constant coefficients** is a recurrence relation of the form
> $$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k},$$
> where $c_1, c_2, \dots, c_k$ are real numbers, and $c_k \neq 0$.

The **characteristic equation** of this recurrence relation is
$$r^k - c_1 r^{k-1} - c_2 r^{k-2} - \dots - c_k = 0.$$
Its roots are called the **characteristic roots**.

---

### 8.2.2 Solving Linear Homogeneous Recurrence Relations

> **THEOREM 1: Degree Two with Distinct Roots**  
> Let $c_1$ and $c_2$ be real numbers. Suppose that $r^2 - c_1 r - c_2 = 0$ has two distinct roots $r_1$ and $r_2$. Then $\{a_n\}$ is a solution of $a_n = c_1 a_{n-1} + c_2 a_{n-2}$ if and only if
> $$a_n = \alpha_1 r_1^n + \alpha_2 r_2^n \quad\text{for } n = 0, 1, 2, \dots,$$
> where $\alpha_1$ and $\alpha_2$ are constants.

> **THEOREM 2: Degree Two with One Root of Multiplicity Two**  
> Let $c_1, c_2 \in \mathbf{R}$ with $c_2 \neq 0$. Suppose $r^2 - c_1 r - c_2 = 0$ has only one root $r_0$. Then $\{a_n\}$ is a solution of $a_n = c_1 a_{n-1} + c_2 a_{n-2}$ if and only if
> $$a_n = \alpha_1 r_0^n + \alpha_2 n r_0^n \quad\text{for } n = 0, 1, 2, \dots,$$
> where $\alpha_1$ and $\alpha_2$ are constants.

> **THEOREM 3: Degree $k$ with Distinct Roots**  
> If $r^k - c_1 r^{k-1} - \dots - c_k = 0$ has $k$ distinct roots $r_1, r_2, \dots, r_k$, then
> $$a_n = \alpha_1 r_1^n + \alpha_2 r_2^n + \dots + \alpha_k r_k^n.$$

> **THEOREM 4: General Case with Multiple Roots**  
> If $r^k - c_1 r^{k-1} - \dots - c_k = 0$ has $t$ distinct roots $r_1, \dots, r_t$ with multiplicities $m_1, \dots, m_t$, then
> $$a_n = \sum_{i=1}^t \left( \sum_{j=0}^{m_i - 1} \alpha_{i,j} n^j \right) r_i^n.$$

#### EXAMPLES 1–8 HIGHLIGHTS:
- **Example 3:** $a_n = a_{n-1} + 2a_{n-2}$, $a_0 = 2, a_1 = 7 \implies r^2 - r - 2 = (r - 2)(r + 1) = 0 \implies a_n = 3 \cdot 2^n - (-1)^n$.
- **Example 4:** Fibonacci numbers $f_n = f_{n-1} + f_{n-2}$, $f_0 = 0, f_1 = 1 \implies r = \frac{1 \pm \sqrt{5}}{2} \implies f_n = \frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^n - \frac{1}{\sqrt{5}}\left(\frac{1-\sqrt{5}}{2}\right)^n$.
- **Example 5:** $a_n = 6a_{n-1} - 9a_{n-2}$, $a_0 = 1, a_1 = 6 \implies (r - 3)^2 = 0 \implies a_n = 3^n + n 3^n$.
- **Example 6:** $a_n = 6a_{n-1} - 11a_{n-2} + 6a_{n-3} \implies r = 1, 2, 3 \implies a_n = 1 - 2^n + 2 \cdot 3^n$.
- **Example 8:** $a_n = -3a_{n-1} - 3a_{n-2} - a_{n-3} \implies (r + 1)^3 = 0 \implies a_n = (1 + 3n - 2n^2)(-1)^n$.

---

### 8.2.3 Linear Nonhomogeneous Recurrence Relations

A nonhomogeneous linear recurrence relation with constant coefficients has the form:
$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k} + F(n).$$

> **THEOREM 5**  
> If $\{a_n^{(p)}\}$ is a particular solution and $\{a_n^{(h)}\}$ is the general solution of the associated homogeneous relation, then every solution is of the form
> $$a_n = a_n^{(p)} + a_n^{(h)}.$$

> **THEOREM 6: Particular Solutions for $F(n) = P(n)s^n$**  
> If $F(n) = (b_t n^t + \dots + b_1 n + b_0)s^n$:
> - If $s$ is not a root of the characteristic equation, $a_n^{(p)} = (p_t n^t + \dots + p_1 n + p_0)s^n$.
> - If $s$ is a root of multiplicity $m$, $a_n^{(p)} = n^m (p_t n^t + \dots + p_1 n + p_0)s^n$.

#### EXAMPLES 9–13 HIGHLIGHTS:
- **Example 10:** $a_n = 3a_{n-1} + 2n, a_1 = 3 \implies a_n = -n - \frac{3}{2} + \frac{11}{6}3^n$.
- **Example 11:** $a_n = 5a_{n-1} - 6a_{n-2} + 7^n \implies a_n = \alpha_1 3^n + \alpha_2 2^n + \frac{49}{20}7^n$.
- **Example 13:** $a_n = a_{n-1} + n, a_1 = 1 \implies a_n = \frac{n(n+1)}{2}$.

---

### Exercises 8.2

1–2. Determine linear homogeneous recurrence relations and their degrees.  
3–4. Solve second-degree homogeneous relations with initial conditions.  
5–9. Applications to signal messaging, checkerboard tiling, lobster harvesting, and compound interest.  
10. Proof of Theorem 2.  
11. Lucas numbers $L_n = L_{n-1} + L_{n-2}, L_0 = 2, L_1 = 1$.  
12–15. Higher-order homogeneous recurrence relations.  
16. Proof of Theorem 3.  
17. Binomial identity for Fibonacci numbers $f_{n+1} = \sum_{k=0}^{\lfloor n/2 \rfloor} \binom{n-k}{k}$.  
18–22. Repeated roots and characteristic forms.  
23–25. Nonhomogeneous recurrence relations with linear/exponential particular solutions.  
26–27. Forms of particular solutions using Theorem 6.  
28–35. Solving nonhomogeneous recurrence relations.  
36–37. Sum of squares $\sum k^2$ and triangular numbers via recurrence relations.  
38–39. Complex characteristic roots.  
40. Simultaneous recurrence relations.  
41–43. Fibonacci approximations and transformations.  
44. Tridiagonal matrix determinants $d_n = 2d_{n-1} - d_{n-2}$.  
45–47. Population models and salary scales.  
48–50. Recurrence relations with variable coefficients: $f(n)a_n = g(n)a_{n-1} + h(n)$ reduction and quick sort average comparisons.  
51–52. Proofs of Theorems 4 and 6.  
53. Non-linear transformation $T(n) = n T^2(n/2)$.

---

## 8.3 Divide-and-Conquer Algorithms and Recurrence Relations

### 8.3.1 Introduction & Recurrence Form

Divide-and-conquer algorithms divide a problem of size $n$ into $a$ subproblems of size $n/b$, with $g(n)$ operations to combine results:
$$f(n) = a f(n/b) + g(n).$$

#### Classical Examples:
1. **Binary Search:** $f(n) = f(n/2) + 2 \implies O(\log n)$.
2. **Finding Min and Max:** $f(n) = 2f(n/2) + 2 \implies O(n)$.
3. **Merge Sort:** $M(n) = 2M(n/2) + n \implies O(n \log n)$.
4. **Fast Multiplication of Integers (Karatsuba):** $f(2n) = 3f(n) + Cn \implies O(n^{\log_2 3}) \approx O(n^{1.585})$.
5. **Fast Matrix Multiplication (Strassen):** $f(n) = 7f(n/2) + \frac{15}{4}n^2 \implies O(n^{\log_2 7}) \approx O(n^{2.807})$.

---

### 8.3.2 Master Theorem & Complexity

> **THEOREM 1**  
> Let $f$ be an increasing function satisfying $f(n) = a f(n/b) + c$ when $n$ is divisible by $b$, with $a \ge 1, b > 1, c > 0$. Then
> $$f(n) \text{ is } \begin{cases} O(n^{\log_b a}) & \text{if } a > 1, \\ O(\log n) & \text{if } a = 1. \end{cases}$$
> For $n = b^k$ and $a \neq 1$, $f(n) = C_1 n^{\log_b a} + C_2$, where $C_1 = f(1) + c/(a-1)$ and $C_2 = -c/(a-1)$.

> **THEOREM 2: MASTER THEOREM**  
> Let $f$ be an increasing function satisfying $f(n) = a f(n/b) + c n^d$ for $n = b^k$, with $a \ge 1, b > 1, c > 0, d \ge 0$. Then
> $$f(n) \text{ is } \begin{cases} O(n^d) & \text{if } a < b^d, \\ O(n^d \log n) & \text{if } a = b^d, \\ O(n^{\log_b a}) & \text{if } a > b^d. \end{cases}$$

#### EXAMPLE 12: The Closest-Pair Problem
Finding the closest pair among $n$ points in the plane:
- Presort by $x$ and $y$ coordinates in $O(n \log n)$.
- Divide into left and right halves by vertical line $\ell$. Recursively find minimum distances $d_L, d_R$, let $d = \min(d_L, d_R)$.
- Inspect vertical strip of width $2d$ centered at $\ell$. Sort points in strip by $y$-coordinate. Each point needs comparison with at most 7 following points (since each $(d/2) \times (d/2)$ square contains at most 1 point).
- Recurrence: $f(n) = 2f(n/2) + 7n \implies O(n \log n)$.

---

### Exercises 8.3

1–2. Binary search and min/max operations counts.  
3–5. Karatsuba multiplication implementations and operations estimates.  
6. Strassen matrix multiplication operations for $32 \times 32$.  
7–13. Divide-and-conquer recurrences and big-$O$ estimates.  
14–16. Elimination tournament round recurrence.  
17–18. Majority vote finding via divide-and-conquer.  
19–20. Modular exponentiation and power algorithms.  
21–22. Variable substitutions $m = \log n$ for $f(n) = 2f(\sqrt{n}) + g(n)$.  
23. Maximum contiguous subarray sum via divide-and-conquer.  
24–27. Closest-pair algorithm traces and $L_\infty$ metric variation.  
28. Ulam’s searching problem with one lie.  
29–33. Proof of the Master Theorem.  
34–37. Applications of Master Theorem to recurrences.

---

## 8.4 Generating Functions

### 8.4.1 Definitions and Useful Series

> **DEFINITION 1**  
> The **generating function** for the sequence $a_0, a_1, \dots, a_k, \dots$ of real numbers is the infinite series
> $$G(x) = \sum_{k=0}^\infty a_k x^k.$$

#### TABLE 1: Useful Generating Functions
| $G(x)$ | $a_k$ |
| :--- | :--- |
| $(1 + x)^n = \sum_{k=0}^n \binom{n}{k} x^k$ | $\binom{n}{k}$ |
| $(1 + ax)^n = \sum_{k=0}^n \binom{n}{k} a^k x^k$ | $\binom{n}{k} a^k$ |
| $(1 + x^r)^n = \sum_{k=0}^n \binom{n}{k} x^{rk}$ | $\binom{n}{k/r}$ if $r \mid k$; 0 otherwise |
| $\frac{1 - x^{n+1}}{1 - x} = \sum_{k=0}^n x^k$ | $1$ if $k \le n$; 0 otherwise |
| $\frac{1}{1 - x} = \sum_{k=0}^\infty x^k$ | $1$ |
| $\frac{1}{1 - ax} = \sum_{k=0}^\infty a^k x^k$ | $a^k$ |
| $\frac{1}{1 - x^r} = \sum_{k=0}^\infty x^{rk}$ | $1$ if $r \mid k$; 0 otherwise |
| $\frac{1}{(1 - x)^2} = \sum_{k=0}^\infty (k + 1)x^k$ | $k + 1$ |
| $\frac{1}{(1 - x)^n} = \sum_{k=0}^\infty \binom{n + k - 1}{k} x^k$ | $\binom{n + k - 1}{k} = \binom{n + k - 1}{n - 1}$ |
| $\frac{1}{(1 + x)^n} = \sum_{k=0}^\infty (-1)^k \binom{n + k - 1}{k} x^k$ | $(-1)^k \binom{n + k - 1}{k}$ |
| $\frac{1}{(1 - ax)^n} = \sum_{k=0}^\infty \binom{n + k - 1}{k} a^k x^k$ | $\binom{n + k - 1}{k} a^k$ |
| $e^x = \sum_{k=0}^\infty \frac{x^k}{k!}$ | $1/k!$ |
| $\ln(1 + x) = \sum_{k=1}^\infty \frac{(-1)^{k+1}}{k} x^k$ | $(-1)^{k+1}/k$ |

---

### 8.4.2 Extended Binomial Theorem

> **DEFINITION 2**  
> For $u \in \mathbf{R}$ and integer $k \ge 0$, the **extended binomial coefficient** is:
> $$\binom{u}{k} = \begin{cases} \frac{u(u-1)\cdots(u-k+1)}{k!} & \text{if } k > 0, \\ 1 & \text{if } k = 0. \end{cases}$$

Key identity for negative integers:
$$\binom{-n}{r} = (-1)^r \binom{n + r - 1}{r}.$$

> **THEOREM 2: EXTENDED BINOMIAL THEOREM**  
> For $|x| < 1$ and $u \in \mathbf{R}$:
> $$(1 + x)^u = \sum_{k=0}^\infty \binom{u}{k} x^k.$$

---

### 8.4.3 Applications to Counting and Recurrences
- **Combinations with Repetition:** Coefficient of $x^r$ in $(1 - x)^{-n}$ is $\binom{n + r - 1}{r}$.
- **Constrained integer equations:** $e_1 + e_2 + \dots + e_n = C$ with bounds represented by polynomial factors.
- **Solving Recurrences:** Transforming relations into algebraic equations for $G(x)$, using partial fractions, and expanding back to sequence coefficients.

---

### Exercises 8.4

1–8. Generating functions for finite and infinite sequences, closed forms, and coefficient extraction.  
9–12. Finding specific coefficients in polynomial/series products.  
13–18. Combinatorial distribution problems with lower and upper bounds.  
19–20. Change-making generating functions.  
21–24. Integer partitions and linear constraints.  
25–27. Postage and purchase combinations.  
28. Die roll sums generating function $\frac{1}{1 - x - x^2 - x^3 - x^4 - x^5 - x^6}$.  
29–31. Coin and bill change problems.  
32–33. Sequence transformations and generating function operations.  
34–40. Solving recurrence relations via generating functions.  
41. Fibonacci sequence generating function derivation.  
42–43. Catalan numbers generating function $G(x) = \frac{1 - \sqrt{1 - 4x}}{2x}$ and explicit form $C_n = \frac{1}{n+1}\binom{2n}{n}$.  
44–45. Generating function proofs of Pascal’s and Vandermonde’s identities.  
46. Sum of squares $\sum k^2$ via generating function $\frac{x^2 + x}{(1-x)^4}$.  
47–50. Exponential generating functions $E(x) = \sum \frac{a_n}{n!} x^n$.  
51–52. Codeword problems with parity constraints.  
53–58. Integer partitions $p(n), p_o(n), p_d(n)$ and Euler’s partition theorem $p_o(n) = p_d(n)$.  
59–62. Probability generating functions $G_X(x) = \sum p(X = k)x^k$, mean $E(X) = G'_X(1)$, variance $V(X) = G''_X(1) + G'_X(1) - [G'_X(1)]^2$.

---

## 8.5 Inclusion–Exclusion

### 8.5.1 Principle of Inclusion–Exclusion

For two sets:
$$|A \cup B| = |A| + |B| - |A \cap B|.$$

For three sets:
$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|.$$

> **THEOREM 1: THE PRINCIPLE OF INCLUSION–EXCLUSION**  
> Let $A_1, A_2, \dots, A_n$ be finite sets. Then
> $$\left|\bigcup_{i=1}^n A_i\right| = \sum_{1 \le i \le n} |A_i| - \sum_{1 \le i < j \le n} |A_i \cap A_j| + \sum_{1 \le i < j < k \le n} |A_i \cap A_j \cap A_k| - \dots + (-1)^{n+1} \left|\bigcap_{i=1}^n A_i\right|.$$

*Proof:* An element in exactly $r$ sets is counted:
$$\binom{r}{1} - \binom{r}{2} + \binom{r}{3} - \dots + (-1)^{r+1}\binom{r}{r} = 1 - (1 - 1)^r = 1 \quad\text{time}. \quad\blacksquare$$

---

### Exercises 8.5

1–9. Inclusion–exclusion for 2, 3, and 4 sets (student enrollments, language courses, surveys).  
10–14. Divisibility counts of integers in ranges not divisible by given sets of primes/integers.  
15–17. Permutations avoiding specific substrings or character patterns.  
18–23. Multi-set union formulas and general $n$-set expansions.  
24. Induction proof of inclusion–exclusion.  
25–31. Probability formulas for unions of events.

---

## 8.6 Applications of Inclusion–Exclusion

### 8.6.1 Alternative Form of Inclusion–Exclusion

Let $N(P_1' P_2' \dots P_n')$ denote the number of elements having none of properties $P_1, P_2, \dots, P_n$:
$$N(P_1' P_2' \dots P_n') = N - \sum_{1 \le i \le n} N(P_i) + \sum_{1 \le i < j \le n} N(P_i P_j) - \dots + (-1)^n N(P_1 P_2 \dots P_n).$$

---

### 8.6.2 Number of Primes (Sieve of Eratosthenes)
To find primes not exceeding 100, eliminate multiples of primes $\le \sqrt{100} = 10$, namely $2, 3, 5, 7$:
$$\text{Primes } \le 100 = 4 + N(P_1' P_2' P_3' P_4') = 4 + 21 = 25.$$

---

### 8.6.3 Number of Onto Functions

> **THEOREM 1**  
> The number of onto functions from a set of $m$ elements to a set of $n$ elements ($m \ge n$) is:
> $$n^m - \binom{n}{1}(n - 1)^m + \binom{n}{2}(n - 2)^m - \dots + (-1)^{n-1}\binom{n}{n-1} 1^m = \sum_{k=0}^{n-1} (-1)^k \binom{n}{k}(n - k)^m = n! S(m, n),$$
> where $S(m, n)$ is the Stirling number of the second kind.

---

### 8.6.4 Derangements and the Hatcheck Problem

A **derangement** is a permutation leaving no element in its original position.

> **THEOREM 2**  
> The number of derangements of an $n$-element set is:
> $$D_n = n!\left[ 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \dots + (-1)^n \frac{1}{n!} \right] = n! \sum_{k=0}^n \frac{(-1)^k}{k!}.$$

The probability that a random permutation is a derangement is:
$$\frac{D_n}{n!} = \sum_{k=0}^n \frac{(-1)^k}{k!} \xrightarrow{n \to \infty} e^{-1} \approx 0.368.$$

| $n$ | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $D_n/n!$ | 0.50000 | 0.33333 | 0.37500 | 0.36667 | 0.36806 | 0.36786 |

---

### Exercises 8.6

1–2. Universal set subtraction and Venn diagram counts.  
3–4. Solutions to integer equations with upper bounds.  
5–7. Sieve of Eratosthenes, squarefree integers, and powers.  
8–11. Onto functions and job/toy assignment problems.  
12–15. Derangements and hatcheck problem probabilities.  
16–17. Constrained permutations and derangements of subsets.  
18–20. Recurrence relation for derangements $D_n = (n - 1)(D_{n-1} + D_{n-2}) = n D_{n-1} + (-1)^n$.  
21. Parity of $D_n$.  
22–23. Euler’s totient function $\phi(n) = n \prod_{p \mid n} (1 - 1/p)$ via inclusion–exclusion.  
24. Identity $n! = \sum_{k=0}^n \binom{n}{k} D_{n-k}$.  
25–27. Derangements with fixed sub-blocks and proof of Theorem 1.

---

## Key Terms and Results

### TERMS
- **recurrence relation:** a formula expressing terms of a sequence as a function of previous terms.
- **initial conditions:** specified base values that uniquely determine the sequence.
- **dynamic programming:** algorithmic paradigm solving optimization problems by combining overlapping subproblems with memoization.
- **linear homogeneous recurrence relation with constant coefficients:** $a_n = c_1 a_{n-1} + \dots + c_k a_{n-k}$.
- **characteristic equation / roots:** algebraic equation $r^k - c_1 r^{k-1} - \dots - c_k = 0$ and its solutions.
- **linear nonhomogeneous recurrence relation:** $a_n = c_1 a_{n-1} + \dots + c_k a_{n-k} + F(n)$.
- **divide-and-conquer algorithm:** solving a problem by recursively splitting it into $a$ subproblems of size $n/b$.
- **generating function:** formal power series $G(x) = \sum a_k x^k$.
- **extended binomial coefficient:** $\binom{u}{k} = u(u-1)\cdots(u-k+1)/k!$.
- **principle of inclusion–exclusion:** formula for counting elements in the union of finite sets.
- **derangement:** a permutation with no fixed points ($D_n$).

### RESULTS
- Homogeneous solution: $a_n = \sum \alpha_i r_i^n$ (distinct roots) or $a_n = \sum P_i(n) r_i^n$ (repeated roots).
- Nonhomogeneous solution: $a_n = a_n^{(p)} + a_n^{(h)}$.
- Master Theorem: complexity bounds for $f(n) = a f(n/b) + c n^d$.
- Extended Binomial Theorem: $(1 + x)^u = \sum_{k=0}^\infty \binom{u}{k} x^k$.
- Number of onto functions: $\sum_{k=0}^{n-1} (-1)^k \binom{n}{k}(n - k)^m = n! S(m, n)$.
- Number of derangements: $D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$.

---

## Review Questions

1–16. Comprehensive review covering recurrence relations, Fibonacci rabbits, Tower of Hanoi, dynamic programming, linear homogeneous/nonhomogeneous solution methods, divide-and-conquer, Master Theorem, generating functions, inclusion–exclusion principle, onto functions, and derangements.

---

## Supplementary Exercises

1–43. Extensive problem set covering chain letters, isotope decay, currency print runs, bacteria growth models, signal transmissions, postage stamp combinations, coupled recurrence relations, logarithmic transformations, rabbit models, knapsack dynamic programming, longest common subsequence (LCS) algorithm, divide-and-conquer recurrences, unimodal sequence search, forward differences $\Delta a_n$, calculus-based generating functions, student surveys, farm animal combinations, Euler's totient, derangements, and constrained bit strings.

---

## Computer Projects, Computations and Explorations, Writing Projects

- **Computer Projects (1–13):** Hanoi moves generator, Frame–Stewart 4-peg Hanoi simulator, bit string generators, parenthesization algorithms, dynamic programming talk scheduler, matrix-chain multiplication, recurrence solvers, inclusion–exclusion formulas, onto function enumerators, derangement generators.
- **Computations and Explorations (1–8):** High-precision Fibonacci numbers ($f_{1000}$), prime Fibonacci searches, Karatsuba vs. standard multiplication performance, Strassen matrix multiplication comparisons, birthday problem thresholds, large prime searches.
- **Writing Projects (1–17):** History of Fibonacci and Liber Abaci, phyllotaxis, Hanoi variations and Reve’s puzzle, Catalan number manifestations, Bellman’s dynamic programming foundations, bioinformatics applications, Ulam’s searching problem, convex hull algorithms, sieve methods in number theory, Montmort’s rencontres problem, Polya theory of counting, and ménage problem.
