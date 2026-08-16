# CHAPTER 12: Boolean Algebra

- **12.1 Boolean Functions**
- **12.2 Representing Boolean Functions**
- **12.3 Logic Gates**
- **12.4 Minimization of Circuits**

The circuits in computers and other electronic devices have inputs, each of which is either a 0 or a 1, and produce outputs that are also 0s and 1s. Circuits can be constructed using any basic element that has two different states. Such elements include switches that can be in either the on or the off position and optical devices that can be either lit or unlit. In 1938 Claude Shannon showed how the basic rules of logic, first given by George Boole in 1854 in his *The Laws of Thought*, could be used to design circuits. These rules form the basis for Boolean algebra. In this chapter we develop the basic properties of Boolean algebra. The operation of a circuit is defined by a Boolean function that specifies the value of an output for each set of inputs. The first step in constructing a circuit is to represent its Boolean function by an expression built up using the basic operations of Boolean algebra. We will provide an algorithm for producing such expressions. The expression that we obtain may contain many more operations than are necessary to represent the function. Later in the chapter we will describe methods for finding an expression with the minimum number of sums and products that represents a Boolean function. The procedures that we will develop, Karnaugh maps and the Quine–McCluskey method, are important in the design of efficient circuits.

---

## 12.1 Boolean Functions

### 12.1.1 Basic Operations and Definitions

Boolean algebra operates on the set $B = \{0, 1\}$.
1. **Complementation:** $\overline{0} = 1, \overline{1} = 0$.
2. **Boolean Sum ($+$ or OR):** $1 + 1 = 1, 1 + 0 = 1, 0 + 1 = 1, 0 + 0 = 0$.
3. **Boolean Product ($\cdot$ or AND):** $1 \cdot 1 = 1, 1 \cdot 0 = 0, 0 \cdot 1 = 0, 0 \cdot 0 = 0$.

- **Precedence:** Complementation first, then Boolean products, then Boolean sums.

> **CLAUDE ELWOOD SHANNON (1916–2001)**  
> American mathematician and electrical engineer at MIT and Bell Labs, the "father of information theory," whose 1936 master's thesis founded digital circuit design using Boolean algebra.

---

### 12.1.2 Boolean Expressions and Functions

- $B^n = \{(x_1, \dots, x_n) \mid x_i \in \{0, 1\}\}$.
- A function from $B^n$ to $B$ is a **Boolean function of degree $n$**.
- **Number of Boolean functions of degree $n$:** $2^{2^n}$.
  - Degree 1: $4$
  - Degree 2: $16$ ($F_1, \dots, F_{16}$)
  - Degree 3: $256$
  - Degree 4: $65,536$
  - Degree 5: $4,294,967,296$
  - Degree 6: $18,446,744,073,709,551,616$

---

### 12.1.3 Identities of Boolean Algebra

#### TABLE 5: Boolean Identities
| Identity | Name |
| :--- | :--- |
| $\overline{\overline{x}} = x$ | Law of the double complement |
| $x + x = x$, $x \cdot x = x$ | Idempotent laws |
| $x + 0 = x$, $x \cdot 1 = x$ | Identity laws |
| $x + 1 = 1$, $x \cdot 0 = 0$ | Domination laws |
| $x + y = y + x$, $xy = yx$ | Commutative laws |
| $x + (y + z) = (x + y) + z$, $x(yz) = (xy)z$ | Associative laws |
| $x + yz = (x + y)(x + z)$, $x(y + z) = xy + xz$ | Distributive laws |
| $\overline{xy} = \overline{x} + \overline{y}$, $\overline{x + y} = \overline{x}\,\overline{y}$ | De Morgan’s laws |
| $x + xy = x$, $x(x + y) = x$ | Absorption laws |
| $x + \overline{x} = 1$ | Unit property |
| $x\overline{x} = 0$ | Zero property |

---

### 12.1.4 Duality Principle

The **dual** of a Boolean expression is obtained by interchanging $+$ and $\cdot$, and interchanging $0$ and $1$.
- **Duality Principle:** An identity between Boolean functions remains valid when duals of both sides are taken.

---

### 12.1.5 Abstract Definition of a Boolean Algebra

> **DEFINITION 1**  
> A **Boolean algebra** is a set $B$ with two binary operations $\lor$ and $\land$, elements $0$ and $1$, and a unary complement operation satisfying the identity, complement, associative, commutative, and distributive laws.

- Any **complemented, distributive lattice** is a Boolean algebra.

---

### Exercises 12.1

1–4. Evaluating Boolean arithmetic expressions and translating to propositional equivalences.  
5–8. Truth tables and $Q_3$ cube representations of Boolean functions.  
9–10. Solving Boolean equations and counting functions of degree 7 ($2^{2^7} = 2^{128}$).  
11–13. Algebraic proofs of absorption and consensus properties.  
14–23. Truth table verifications of all Boolean identities.  
24–27. XOR operator ($\oplus$) properties and distributivity tests.  
28–30. Finding dual expressions and proving the duality principle.  
31–32. Self-dual Boolean functions ($F^d = F$).  
33–34. Propositional translations of Boolean laws.  
35–43. Abstract Boolean algebra theorems (uniqueness of complement, modular laws, lattice isomorphisms).

---

## 12.2 Representing Boolean Functions

### 12.2.1 Sum-of-Products (DNF) and Product-of-Sums (CNF)

> **DEFINITION 1**  
> - A **literal** is a Boolean variable $x$ or its complement $\overline{x}$.  
> - A **minterm** of $x_1, \dots, x_n$ is a product $y_1 y_2 \dots y_n$ where $y_i = x_i$ or $y_i = \overline{x}_i$. (Equals 1 for exactly one input combination).  
> - A **maxterm** of $x_1, \dots, x_n$ is a sum $y_1 + y_2 + \dots + y_n$ where $y_i = x_i$ or $y_i = \overline{x}_i$. (Equals 0 for exactly one input combination).

- **Sum-of-Products Expansion (Disjunctive Normal Form - DNF):** Boolean sum of minterms corresponding to input combinations where $F = 1$.
- **Product-of-Sums Expansion (Conjunctive Normal Form - CNF):** Boolean product of maxterms corresponding to input combinations where $F = 0$.

---

### 12.2.2 Functional Completeness

A set of operators is **functionally complete** if every Boolean function can be expressed using only operators in the set.
- $\{\cdot, +, \overline{\phantom{x}}\}$ is functionally complete.
- $\{\cdot, \overline{\phantom{x}}\}$ is functionally complete ($x + y = \overline{\overline{x}\,\overline{y}}$).
- $\{+, \overline{\phantom{x}}\}$ is functionally complete ($xy = \overline{\overline{x} + \overline{y}}$).
- $\{+, \cdot\}$ is **not** functionally complete (cannot generate negation).

#### Single Universal Operators:
1. **NAND (Sheffer Stroke $|$):** $x | y = \overline{xy}$.  
   $\overline{x} = x | x$, $xy = (x | y) | (x | y)$, $x + y = (x | x) | (y | y)$.
2. **NOR (Peirce Arrow $\downarrow$):** $x \downarrow y = \overline{x + y}$.  
   $\overline{x} = x \downarrow x$, $xy = (x \downarrow x) \downarrow (y \downarrow y)$, $x + y = (x \downarrow y) \downarrow (x \downarrow y)$.

---

### Exercises 12.2

1–6. Constructing minterms and sum-of-products expansions for given functions and truth requirements.  
7–11. Maxterms and product-of-sums expansions.  
12–13. Converting expressions to use only $\{\cdot, \overline{\phantom{x}}\}$ or $\{+, \overline{\phantom{x}}\}$.  
14–18. Expressing operations and functions using exclusively NAND ($|$) or exclusively NOR ($\downarrow$).  
19–20. Functional completeness tests for operator subsets $(\{+, \oplus\}, \{\overline{\phantom{x}}, \oplus\}, \{\cdot, \oplus\})$.

---

## 12.3 Logic Gates

### 12.3.1 Gate Types and Combinational Circuits

- **Inverter (NOT):** Input $x \to$ Output $\overline{x}$.
- **OR Gate:** Inputs $x_1, \dots, x_n \to$ Output $x_1 + \dots + x_n$.
- **AND Gate:** Inputs $x_1, \dots, x_n \to$ Output $x_1 x_2 \dots x_n$.
- **NAND / NOR Gates:** Inverted output gates.
- **XOR Gate ($\oplus$):** Inputs $x, y \to$ Output $x \oplus y = xy + \overline{x}y$.

---

### 12.3.2 Examples of Circuits
1. **Majority Voting Circuit:** $F(x, y, z) = xy + xz + yz$.
2. **Light Control Switches:**
   - 2 switches: $F(x, y) = xy + \overline{x}\,\overline{y}$.
   - 3 switches: $F(x, y, z) = xyz + x\overline{y}\,\overline{z} + \overline{x}y\overline{z} + \overline{x}\,\overline{y}z$.

---

### 12.3.3 Adders
1. **Half Adder:** Adds two bits $x, y$.  
   $$\text{Sum } s = (x + y)\overline{xy} = x \oplus y, \quad \text{Carry } c = xy.$$
2. **Full Adder:** Adds two bits $x_i, y_i$ and carry-in $c_i$.  
   $$s = x_i \oplus y_i \oplus c_i, \quad c_{i+1} = x_i y_i + (x_i \oplus y_i)c_i.$$
3. **Ripple Carry Adder:** Chaining $n$ full adders to add two $n$-bit integers.

---

### Exercises 12.3

1–5. Determining output Boolean functions of given logic circuits.  
6–8. Designing circuits using inverters, AND, and OR gates for specified functions and 4-way light switches.  
9. 5-bit ripple carry adder construction.  
10–12. Half subtractors, full subtractors, and 4-bit subtractor circuits.  
13–14. 2-bit integer comparator and 2-bit binary multiplier circuits.  
15–18. Constructing circuits and half adders using purely NAND or purely NOR gates.  
19. 4-to-1 Multiplexer design with control bits $c_0, c_1$.  
20. Circuit depth analysis.

---

## 12.4 Minimization of Circuits

### 12.4.1 Karnaugh Maps (K-Maps)

A **K-map** is a visual representation organizing minterms using Gray codes so that geometrically adjacent cells differ in exactly one literal.

- **Implicant:** Product of literals corresponding to a rectangular block of $2^k$ 1s.
- **Prime Implicant:** A block of $2^k$ 1s not contained in any larger block of $2^{k+1}$ 1s.
- **Essential Prime Implicant:** A prime implicant covering a 1 that is covered by no other prime implicant.

#### K-Map Dimensions:
- 2 variables: $2 \times 2$ grid (4 cells).
- 3 variables: $2 \times 4$ grid (8 cells, toroidally adjacent columns).
- 4 variables: $4 \times 4$ grid (16 cells, torus adjacency on rows and columns).
- 5/6 variables: $4 \times 8$ and $8 \times 8$ grids with Gray code indexing.

> **MAURICE KARNAUGH (BORN 1924)**  
> American physicist and engineer at Bell Labs and IBM who introduced Karnaugh maps in 1953.

---

### 12.4.2 Don't Care Conditions
Combinations of input variables that never occur in practice are marked with $d$ (don't care) and can be set to 1 or 0 to form the largest possible rectangular blocks.

---

### 12.4.3 The Quine–McCluskey Method

An algorithmic, tabular reduction method suitable for computer automation:
1. Group minterms by the number of 1s in their binary representations.
2. Successively combine terms differing by 1 bit (replacing the difference with a dash `–`).
3. Identify all **prime implicants** (terms that cannot be combined further).
4. Construct a **prime implicant coverage table** to select the minimal set of essential and secondary prime implicants covering all original minterms.

> **WILLARD VAN ORMAN QUINE (1908–2000)** & **EDWARD J. MCCLUSKEY (1929–2016)**  
> Quine (Harvard philosopher/logician) and McCluskey (Stanford computer scientist) developed the exact minimization algorithm in 1952–1956.

---

### Exercises 12.4

1–4. 2-variable K-maps.  
5–9. 3-variable K-maps, implicants, prime implicants, and essential prime implicants.  
10–11. Hypercubes $Q_3, Q_4$ subcube representations of literal products.  
12–14. Minimizing 3-variable and 4-variable functions with K-maps.  
15–19. 5-variable and 6-variable K-map structures and Gray code adjacencies.  
20–21. BCD digit checkers (odd, divisibility by 3) and voting circuits with biased members.  
22–25. Quine–McCluskey method step-by-step reductions.  
26–27. Product-of-sums minimization using K-maps.  
28. Torus drawing of 4-variable K-maps.  
29–32. Minimizing circuits with don't care conditions ($d$).  
33. Proving $k$-literal products correspond to $2^{n-k}$-dimensional subcubes of $Q_n$.

---

## Key Terms and Results

### TERMS
- **Boolean variable / complement / Boolean sum / Boolean product:** basic primitives on $B = \{0, 1\}$.
- **dual of Boolean expression:** expression obtained by swapping $+ \leftrightarrow \cdot$ and $0 \leftrightarrow 1$.
- **Boolean function of degree $n$:** mapping $F: B^n \to B$ ($2^{2^n}$ total functions).
- **literal / minterm / maxterm:** building blocks of canonical forms.
- **sum-of-products (DNF) / product-of-sums (CNF):** canonical representations.
- **functionally complete:** operator set able to generate all Boolean functions ($\{\cdot, \overline{\phantom{x}}\}, \{+, \overline{\phantom{x}}\}, \{|\}, \{\downarrow\}$).
- **logic gates (Inverter, OR, AND, NAND, NOR, XOR):** physical gate primitives.
- **half adder / full adder:** binary addition circuits.
- **K-map (Karnaugh map):** visual grid minimization method using Gray codes.
- **implicant / prime implicant / essential prime implicant:** term coverings on K-maps.
- **don’t care condition ($d$):** unconstrained input combinations.
- **Quine–McCluskey method:** tabular algorithm for exact Boolean minimization.

### RESULTS
- Shannon (1938): Digital circuit design is isomorphic to Boolean algebra.
- Every Boolean function has a unique sum-of-products expansion.
- NAND ($|$) and NOR ($\downarrow$) are individually functionally complete.
- Duality Principle: Any Boolean identity implies its dual identity.
- Full adder adds two bits and carry-in with $O(1)$ delay per stage.
- Quine-McCluskey method finds minimal SOP representations for any degree $n$.

---

## Review Questions

1–13. Comprehensive review covering degree $n$ Boolean functions, recursive syntax, duality principle, sum-of-products expansions, functional completeness, circuit implementations (switches, adders, universal gates), 3- and 4-variable K-maps, don't care conditions, and the Quine-McCluskey method.

---

## Supplementary Exercises

1–24. Advanced problems covering self-dual Boolean functions ($F^d = F$, $2^{2^{n-1}}$ self-dual functions), poset ordering on Boolean functions ($F \le G$), Hasse diagrams of degree-2 functions, non-associativity of NAND/NOR, functional completeness of equivalence/implication operators, threshold gates and threshold functions (linear separability $w \cdot x \ge T$), and non-threshold functions ($x \oplus y, wx + yz$).

---

## Computer Projects, Computations and Explorations, Writing Projects

- **Computer Projects (1–12):** Boolean calculator, truth table enumerator, DNF generator, universal NAND/NOR converter, automated K-map generator, full Quine-McCluskey minimization engine, threshold gate evaluator.
- **Computations and Explorations (1–7):** Enumerating high-degree functions ($n \le 10$), benchmark minimization comparisons, randomized Quine-McCluskey step profiling.
- **Writing Projects (1–12):** Early logic machines (Stanhope, Jevons, Marquand), sequential circuits and flip-flops, shift registers, hardware multipliers, multiplexers, threshold neural logic, hazard-free switching circuits, 6-variable K-maps, Espresso heuristic minimization, and functional decomposition.
