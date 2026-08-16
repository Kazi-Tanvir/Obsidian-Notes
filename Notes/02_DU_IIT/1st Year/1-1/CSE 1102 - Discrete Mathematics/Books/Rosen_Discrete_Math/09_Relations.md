# CHAPTER 9: Relations

- **9.1 Relations and Their Properties**
- **9.2 $n$-ary Relations and Their Applications**
- **9.3 Representing Relations**
- **9.4 Closures of Relations**
- **9.5 Equivalence Relations**
- **9.6 Partial Orderings**

Relationships between elements of sets occur in many contexts. Every day we deal with relationships such as those between a business and its telephone number, an employee and his or her salary, a person and a relative, and so on. In mathematics we study relationships such as those between a positive integer and one that it divides, an integer and one that it is congruent to modulo 5, a real number and one that is larger than it, a real number $x$ and the value $f(x)$ where $f$ is a function, and so on. Relationships such as that between a program and a variable it uses, and that between a computer language and a valid statement in this language, often arise in computer science. Relationships between elements of two sets are represented using the structure called a binary relation, which is just a subset of the Cartesian product of the sets. Relations can be used to solve problems such as determining which pairs of cities are linked by airline flights in a network, or finding a viable order for the different phases of a complicated project. We will introduce a number of different properties binary relations may enjoy.

Relationships between elements of more than two sets arise in many contexts. These relationships can be represented by $n$-ary relations, which are collections of $n$-tuples. Such relations are the basis of the relational data model, the most common way to store information in computer databases. We will introduce the terminology used to study relational databases, define some important operations on them, and introduce the database query language SQL. We will conclude our brief study of $n$-ary relations and databases with an important application from data mining. In particular, we will show how databases of transactions, represented by $n$-ary relations, are used to measure the likelihood that someone buys a particular product from a store when they buy one or more other products.

Two methods for representing relations, using square matrices and using directed graphs, consisting of vertices and directed edges, will be introduced and used in later sections of the chapter. We will also study relationships that have certain collections of properties that relations may enjoy. For example, in some computer languages, only the first 31 characters of the name of a variable matter. The relation consisting of ordered pairs of strings in which the first string has the same initial 31 characters as the second string is an example of a special type of relation, known as an equivalence relation. Equivalence relations arise throughout mathematics and computer science. Finally, we will study relations called partial orderings, which generalize the notion of the less than or equal to relation. For example, the set of all pairs of strings of English letters in which the second string is the same as the first string or comes after the first in dictionary order is a partial ordering.

---

## 9.1 Relations and Their Properties

### 9.1.1 Introduction & Definitions

> **DEFINITION 1**  
> Let $A$ and $B$ be sets. A **binary relation** from $A$ to $B$ is a subset of $A \times B$.

We use the notation $aRb$ to denote that $(a, b) \in R$ and $a \not{R} b$ to denote that $(a, b) \notin R$. When $(a, b)$ belongs to $R$, $a$ is said to be related to $b$ by $R$.

> **DEFINITION 2**  
> A relation on a set $A$ is a relation from $A$ to $A$ (that is, a subset of $A \times A$).

#### EXAMPLE 4
Let $A = \{1, 2, 3, 4\}$. The relation $R = \{(a, b) \mid a \text{ divides } b\}$ on $A$ is:
$$R = \{(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 3), (4, 4)\}.$$

#### NUMBER OF RELATIONS
On a set with $n$ elements, there are $|A \times A| = n^2$ pairs, so there are $2^{n^2}$ relations.

---

### 9.1.2 Properties of Relations

> **DEFINITION 3: Reflexive**  
> A relation $R$ on a set $A$ is called **reflexive** if $(a, a) \in R$ for every element $a \in A$.  
> Quantified: $\forall a ((a, a) \in R)$.

> **DEFINITION 4: Symmetric and Antisymmetric**  
> - A relation $R$ on a set $A$ is called **symmetric** if $(b, a) \in R$ whenever $(a, b) \in R$, for all $a, b \in A$.  
>   Quantified: $\forall a \forall b ((a, b) \in R \to (b, a) \in R)$.  
> - A relation $R$ on a set $A$ such that for all $a, b \in A$, if $(a, b) \in R$ and $(b, a) \in R$, then $a = b$ is called **antisymmetric**.  
>   Quantified: $\forall a \forall b (((a, b) \in R \land (b, a) \in R) \to (a = b))$.

> **DEFINITION 5: Transitive**  
> A relation $R$ on a set $A$ is called **transitive** if whenever $(a, b) \in R$ and $(b, c) \in R$, then $(a, c) \in R$, for all $a, b, c \in A$.  
> Quantified: $\forall a \forall b \forall c (((a, b) \in R \land (b, c) \in R) \to (a, c) \in R)$.

#### Number of Reflexive, Symmetric, and Antisymmetric Relations on an $n$-element set:
- **Reflexive relations:** $2^{n(n-1)}$
- **Symmetric relations:** $2^{n(n+1)/2}$
- **Antisymmetric relations:** $2^n 3^{n(n-1)/2}$
- **Irreflexive relations:** $2^{n(n-1)}$

---

### 9.1.3 Combining Relations and Composition

> **DEFINITION 6: Composite Relation**  
> Let $R$ be a relation from $A$ to $B$ and $S$ a relation from $B$ to $C$. The **composite** of $R$ and $S$, denoted by $S \circ R$, is the relation consisting of ordered pairs $(a, c)$, where $a \in A, c \in C$, and for which there exists an element $b \in B$ such that $(a, b) \in R$ and $(b, c) \in S$.

> **DEFINITION 7: Powers of a Relation**  
> Let $R$ be a relation on the set $A$. The powers $R^n, n = 1, 2, 3, \dots$, are defined recursively by
> $$R^1 = R \quad\text{and}\quad R^{n+1} = R^n \circ R.$$

> **THEOREM 1**  
> The relation $R$ on a set $A$ is transitive if and only if $R^n \subseteq R$ for $n = 1, 2, 3, \dots$.

---

### Exercises 9.1

1–2. Listing ordered pairs of relations based on arithmetic and divisibility conditions.  
3–7. Checking reflexivity, symmetry, antisymmetry, and transitivity for relations on finite sets, people, web pages, $\mathbf{R}$, and $\mathbf{Z}$.  
8–10. Empty relations and relations that are both symmetric/antisymmetric.  
11–17. Irreflexive relations ($\forall a ((a, a) \notin R)$).  
18–24. Asymmetric relations ($(a, b) \in R \implies (b, a) \notin R$).  
25. Number of relations from set of size $m$ to set of size $n$: $2^{mn}$.  
26–29. Inverse relation $R^{-1} = \{(b, a) \mid (a, b) \in R\}$ and complementary relation $\overline{R}$.  
30–31. Set operations on relations: $R_1 \cup R_2, R_1 \cap R_2, R_1 \oplus R_2, R_1 - R_2$.  
32–33. Compositions $S \circ R$ and parent/sibling relations.  
34–39. Operations and compositions of standard inequality relations on $\mathbf{R}$ and $\mathbf{Z}$.  
40–41. Powers $R^n$ for parent and advisor relations.  
42–43. Operations on divides/multiple relations and modulo congruence relations.  
44–46. The 16 relations on $\{0, 1\}$.  
47–50. Counting relations with specific properties on sets with $n$ elements.  
51. Identifying the fallacy in proving "symmetric + transitive $\implies$ reflexive".  
52–57. Properties of reflexive, symmetric, and transitive closures and powers ($R^n = R$ for reflexive & transitive $R$).  
58–62. Computing powers $R^n$ and computational complexity of transitivity verification.

---

## 9.2 $n$-ary Relations and Their Applications

### 9.2.1 Definitions & Databases

> **DEFINITION 1**  
> Let $A_1, A_2, \dots, A_n$ be sets. An **$n$-ary relation** on these sets is a subset of $A_1 \times A_2 \times \dots \times A_n$. The sets $A_1, A_2, \dots, A_n$ are called the **domains** of the relation, and $n$ is called its **degree**.

- **Relational Data Model:** Represents databases as tables where rows are $n$-tuples (records) and columns are attributes (fields).
- **Primary Key:** A domain (field) whose value uniquely identifies an $n$-tuple in the relation.
- **Composite Key:** A Cartesian product of domains that uniquely identifies each $n$-tuple.

---

### 9.2.2 Operations on $n$-ary Relations

1. **Selection Operator ($s_C$):** Selects all $n$-tuples from relation $R$ satisfying condition $C$.
2. **Projection Operator ($P_{i_1, i_2, \dots, i_m}$):** Maps each $n$-tuple $(a_1, \dots, a_n)$ to the $m$-tuple $(a_{i_1}, \dots, a_{i_m})$ where $i_1 < \dots < i_m$, deleting $n - m$ components.
3. **Join Operator ($J_p(R, S)$):** Combines an $m$-ary relation $R$ and an $n$-ary relation $S$ matching on the last $p$ components of $R$ and the first $p$ components of $S$, producing an $(m + n - p)$-ary relation.

#### SQL Syntax Connection:
```sql
SELECT Projection_Attributes
FROM Tables_Joined
WHERE Selection_Condition
```

---

### 9.2.3 Association Rules from Data Mining

- **Transaction:** An itemset $t_i \subseteq S$.
- **Count ($\sigma(I)$):** $\sigma(I) = |\{t_i \in T \mid I \subseteq t_i\}|$.
- **Support:** $\text{support}(I) = \frac{\sigma(I)}{|T|}$.
- **Association Rule ($I \to J$):**
  $$\text{support}(I \to J) = \frac{\sigma(I \cup J)}{|T|}, \quad \text{confidence}(I \to J) = \frac{\sigma(I \cup J)}{\sigma(I)}.$$
- **Lift:** $\text{lift}(I \to J) = \frac{\text{support}(I \cup J)}{\text{support}(I)\text{support}(J)}$. (Lift = 1 indicates independence).

---

### Exercises 9.2

1–3. Listing tuples of $n$-ary relations.  
4–9. Primary and composite keys for student, airline, and inventory databases.  
10–17. Applying selection $s_C$, projection $P$, and join $J_p$ operators.  
18–27. Properties of selection, projection, and join operators under set operations.  
28–29. Expressing relational algebra via SQL SELECT/FROM/WHERE queries.  
30–32. Primary keys as function graphs.  
33–36. Market basket analysis: finding counts, support, confidence, and frequent itemsets.  
37–41. Theoretical properties of association rules, lift, Apriori property (downward closure), and counting possible rules ($3^n$).

---

## 9.3 Representing Relations

### 9.3.1 Representing Relations Using Matrices

Let $R$ be a relation from $A = \{a_1, \dots, a_m\}$ to $B = \{b_1, \dots, b_n\}$. The zero–one matrix $M_R = [m_{ij}]$ is defined by:
$$m_{ij} = \begin{cases} 1 & \text{if } (a_i, b_j) \in R, \\ 0 & \text{if } (a_i, b_j) \notin R. \end{cases}$$

#### Matrix Characterizations of Properties:
- **Reflexive:** $m_{ii} = 1$ for all $i$ (all 1s on main diagonal).
- **Symmetric:** $m_{ij} = m_{ji}$ for all $i, j$ ($M_R = M_R^t$, matrix is symmetric).
- **Antisymmetric:** $m_{ij} = 1 \implies m_{ji} = 0$ for all $i \neq j$ ($m_{ij} \land m_{ji} = 0$ for $i \neq j$).
- **Irreflexive:** $m_{ii} = 0$ for all $i$ (all 0s on main diagonal).

#### Operations on Relation Matrices:
- **Union:** $M_{R_1 \cup R_2} = M_{R_1} \lor M_{R_2}$ (join of matrices)
- **Intersection:** $M_{R_1 \cap R_2} = M_{R_1} \land M_{R_2}$ (meet of matrices)
- **Composition:** $M_{S \circ R} = M_R \odot M_S$ (Boolean product)
- **Powers:** $M_{R^n} = M_R^{[n]}$ ($n$th Boolean power)

---

### 9.3.2 Representing Relations Using Digraphs

A **directed graph (digraph)** $G = (V, E)$ consists of vertices $V$ (elements of $A$) and directed edges $E \subseteq V \times V$ (pairs in $R$).
- **Loop:** An edge $(a, a)$ from a vertex to itself.
- **Reflexive:** A loop at every vertex.
- **Symmetric:** Every directed edge between distinct vertices is paired with an antiparallel edge in the opposite direction.
- **Antisymmetric:** No two distinct vertices have edges in both directions.
- **Transitive:** Whenever there are edges $x \to y$ and $y \to z$, there is also a direct edge $x \to z$.

---

### Exercises 9.3

1–4. Constructing matrices from relations and listing relations from matrices.  
5–8. Determining relation properties (reflexive, symmetric, antisymmetric, transitive) from zero–one matrices.  
9–10. Counting nonzero matrix entries.  
11–17. Matrix operations for inverse $M_{R^{-1}} = M_R^t$, complement $M_{\overline{R}} = J - M_R$, join $\lor$, meet $\land$, and Boolean powers.  
18–28. Constructing and interpreting digraphs and listing ordered pairs.  
29–32. Determining relation properties from digraph representations.  
33–36. Graphical operations for inverse, complement, union, intersection, and composition.

---

## 9.4 Closures of Relations

### 9.4.1 Closures

> **DEFINITION 1**  
> The **closure** of a relation $R$ with respect to property $P$ is the smallest relation $S$ with property $P$ containing $R$ (if it exists).

1. **Reflexive Closure:** $R \cup \Delta$, where $\Delta = \{(a, a) \mid a \in A\}$. Matrix: $M_R \lor I_n$.
2. **Symmetric Closure:** $R \cup R^{-1}$. Matrix: $M_R \lor M_R^t$.

---

### 9.4.2 Transitive Closure & Paths

> **DEFINITION 2 & THEOREM 1**  
> A **path** of length $n$ from $a$ to $b$ is a sequence $x_0, x_1, \dots, x_n$ where $x_0 = a, x_n = b$, and $(x_{i-1}, x_i) \in R$.  
> There is a path of length $n$ from $a$ to $b$ if and only if $(a, b) \in R^n$.

> **DEFINITION 3 & THEOREM 2**  
> The **connectivity relation** is $R^* = \bigcup_{n=1}^\infty R^n$.  
> The transitive closure of a relation $R$ equals the connectivity relation $R^*$.

> **LEMMA 1 & THEOREM 3**  
> For a set with $n$ elements, if a path exists between two vertices, there is a path of length $\le n$ (and $\le n - 1$ if $a \neq b$).  
> Thus, $R^* = R \cup R^2 \cup \dots \cup R^n$, and:
> $$M_{R^*} = M_R \lor M_R^{[2]} \lor M_R^{[3]} \lor \dots \lor M_R^{[n]}.$$

---

### 9.4.3 Warshall’s Algorithm

Warshall’s algorithm computes $W_0, W_1, \dots, W_n = M_{R^*}$, where $W_k = [w_{ij}^{(k)}]$ indicates the existence of a path from $v_i$ to $v_j$ whose interior vertices belong to $\{v_1, \dots, v_k\}$.

> **LEMMA 2 (Warshall's Update Formula)**  
> $$w_{ij}^{(k)} = w_{ij}^{(k-1)} \lor (w_{ik}^{(k-1)} \land w_{kj}^{(k-1)}).$$

#### ALGORITHM 2: Warshall’s Algorithm
```pascal
procedure Warshall (MR: n x n zero-one matrix)
W := MR
for k := 1 to n
    for i := 1 to n
        for j := 1 to n
            wij := wij or (wik and wkj)
return W {W = [wij] is MR*}
```
**Complexity:** Algorithm 1 uses $O(n^4)$ bit operations, while Warshall's algorithm uses only $2n^3 = O(n^3)$ bit operations.

> **STEPHEN WARSHALL (1935–2006)**  
> American computer scientist who developed Warshall's algorithm at Technical Operations in 1960.

---

### Exercises 9.4

1–3. Finding reflexive and symmetric closures of numerical relations.  
4–11. Graphical and matrix methods for reflexive and symmetric closures.  
12–14. Matrix representations: $M_R \lor I_n$ and $M_R \lor M_R^t$.  
15. Nonexistence of irreflexive closure.  
16–18. Path tracing and circuits in digraphs.  
19–24. Computing relation powers and connectivity relations $R^*$.  
25–28. Transitive closure computation via Boolean matrix powers (Algorithm 1) vs. Warshall's algorithm (Algorithm 2).  
29–30. Finding minimal relations with multiple closure properties and completing Lemma 1 proof.  
31–36. Fast matrix multiplication complexity bounds, shortest path extensions, and counterexamples for commutativity of closures.

---

## 9.5 Equivalence Relations

### 9.5.1 Definitions and Properties

> **DEFINITION 1 & 2**  
> A relation on a set $A$ is an **equivalence relation** if it is reflexive, symmetric, and transitive. Elements $a, b$ with $aRb$ are called **equivalent** ($a \sim b$).

- **Fundamental Examples:**
  1. Equality ($a = b$)
  2. Congruence modulo $m$: $a \equiv b \pmod m \iff m \mid (a - b)$
  3. String length equality ($l(s) = l(t)$)
  4. Strings agreeing on first $n$ characters ($s R_n t$)

---

### 9.5.2 Equivalence Classes and Partitions

> **DEFINITION 3**  
> The **equivalence class** of $a$ with respect to $R$, denoted $[a]_R$ (or $[a]$), is:
> $$[a]_R = \{s \in A \mid (a, s) \in R\}.$$
> Any element $b \in [a]_R$ is called a **representative** of the class.

> **THEOREM 1**  
> Let $R$ be an equivalence relation on $A$. The following are equivalent:
> 1. $aRb$
> 2. $[a] = [b]$
> 3. $[a] \cap [b] \neq \emptyset$

> **THEOREM 2: Equivalence Relations and Partitions**  
> 1. The equivalence classes of an equivalence relation $R$ on $S$ form a **partition** of $S$.  
> 2. Conversely, given any partition $\{A_i \mid i \in I\}$ of $S$, the relation $R = \{(x, y) \mid x, y \in A_i \text{ for some } i\}$ is an equivalence relation whose equivalence classes are the sets $A_i$.

#### Bell Numbers:
The number of equivalence relations (partitions) on an $n$-element set is given by the **Bell number** $p(n)$, satisfying:
$$p(n) = \sum_{j=0}^{n-1} \binom{n-1}{j} p(n - 1 - j), \quad p(0) = 1.$$
$p(1)=1, p(2)=2, p(3)=5, p(4)=15, p(5)=52, p(6)=203$.

---

### Exercises 9.5

1–6. Identifying equivalence relations on numbers, strings, and campus entities.  
7–10. Logical equivalence and function-induced equivalence relations ($f(x) = f(y)$).  
11–16. String prefix equivalence and rational coordinate relations $((a, b) \sim (c, d) \iff ad = bc)$.  
17–18. Calculus-based equivalence relations ($f'(x) = g'(x)$).  
19–24. URL, web browsing, and matrix/digraph equivalence relation verification.  
25–34. Equivalence classes for bit strings, C identifiers, and partition descriptions.  
35–37. Congruence classes modulo $m$.  
38–40. Equivalence class interpretations for rational pairs and differences.  
41–48. Validating partitions of sets and constructing induced relations.  
49–54. Partition refinements ($P_1$ refines $P_2 \iff R_1 \subseteq R_2$).  
55–57. Smallest equivalence relations containing given subsets.  
58–59. Geometric bead bracelet colorings and $2 \times 2$ checkerboard symmetries.  
60. $\Theta$-complexity classes as equivalence relations on function spaces.  
61–62. Listing all equivalence relations on sets of size 3 and 4.  
63–67. Order of closure operations and Bell numbers recursion.

---

## 9.6 Partial Orderings

### 9.6.1 Definitions and Posets

> **DEFINITION 1**  
> A relation $R$ on a set $S$ is called a **partial ordering** (or **partial order**) if it is **reflexive, antisymmetric, and transitive**.  
> The pair $(S, R)$ is called a **partially ordered set**, or **poset**. Customary notation: $(S, \preceq)$.

- **Standard Examples:** $(\mathbf{Z}, \le)$, $(\mathbf{Z}^+, \mid)$, $(\mathcal{P}(S), \subseteq)$.

> **DEFINITION 2 & 3: Comparable vs Incomparable, Total Orders**  
> - Elements $a, b \in S$ are **comparable** if $a \preceq b$ or $b \preceq a$; otherwise **incomparable**.  
> - If every pair of elements in $(S, \preceq)$ is comparable, $(S, \preceq)$ is a **totally ordered set** (or **chain**), and $\preceq$ is a **total order** (linear order).

> **DEFINITION 4: Well-Ordered Sets**  
> $(S, \preceq)$ is a **well-ordered set** if it is a poset such that $\preceq$ is a total ordering and every nonempty subset of $S$ has a least element.

> **THEOREM 1: Principle of Well-Ordered Induction**  
> If $S$ is a well-ordered set, then $P(x)$ is true for all $x \in S$ if:  
> **Inductive Step:** For every $y \in S$, $[\forall x \in S (x \prec y \to P(x))] \implies P(y)$.

---

### 9.6.2 Lexicographic Order & Hasse Diagrams

- **Lexicographic Order on $A_1 \times A_2$:** $(a_1, a_2) \prec (b_1, b_2)$ if $a_1 \prec_1 b_1$ or ($a_1 = b_1$ and $a_2 \prec_2 b_2$).
- **Covering Relation:** $y$ covers $x$ ($x \prec y$ with no $z$ such that $x \prec z \prec y$).
- **Hasse Diagram:** A simplified graph representation of a finite poset where loops are omitted, transitive edges are removed, and all edges point upward (no arrows).

> **HELMUT HASSE (1898–1979)**  
> German mathematician at Göttingen and Hamburg who made foundational contributions to algebraic number theory and class field theory.

---

### 9.6.3 Extremal Elements, Bounds, and Lattices

- **Maximal element:** No $b \in S$ has $a \prec b$ (top of diagram).
- **Minimal element:** No $b \in S$ has $b \prec a$ (bottom of diagram).
- **Greatest element:** Unique element $a$ such that $b \preceq a$ for all $b \in S$.
- **Least element:** Unique element $a$ such that $a \preceq b$ for all $b \in S$.
- **Upper / Lower Bounds:** For $A \subseteq S$, $u$ is an upper bound if $a \preceq u, \forall a \in A$; $l$ is a lower bound if $l \preceq a, \forall a \in A$.
- **Least Upper Bound ($\text{lub}(A)$):** Smallest upper bound (also called supremum / join $\lor$).
- **Greatest Lower Bound ($\text{glb}(A)$):** Largest lower bound (also called infimum / meet $\land$).

> **DEFINITION: Lattice**  
> A poset in which every pair of elements has both a least upper bound and a greatest lower bound is called a **lattice**.

---

### 9.6.4 Topological Sorting

> **LEMMA 1**  
> Every finite nonempty poset $(S, \preceq)$ has at least one minimal element.

#### ALGORITHM 1: Topological Sorting
```pascal
procedure topological sort ((S, <=): finite poset)
k := 1
while S != empty_set
    ak := a minimal element of S {exists by Lemma 1}
    S := S - {ak}
    k := k + 1
return a1, a2, ..., an {a1 <t a2 <t ... <t an is a compatible total ordering}
```

---

### Exercises 9.6

1–6. Poset validation on numbers, people, power sets, and matrices.  
7–11. Matrix and digraph criteria for partial orderings.  
12–13. Dual posets $(S, R^{-1})$.  
14–15. Comparability in $(\mathbf{Z}^+, \mid)$ and power sets.  
16–19. Lexicographic orderings on $n$-tuples, strings, and bit strings.  
20–27. Drawing Hasse diagrams and extracting relations.  
28–31. Covering relations and reconstruction of posets.  
32–35. Extremal elements, bounds, lub, and glb.  
36–42. Uniqueness of least/greatest elements and bounds.  
43–46. Lattice verification and dual lattices.  
47–48. Multilevel security clearance information flow lattice.  
49–52. Partition lattices and bounded lattices.  
53–59. Well-ordered, well-founded, and dense posets.  
60–65. Topological sort traces for numerical posets and project task schedules.  
66–67. Practical scheduling: House construction and software engineering workflow Hasse diagrams.

---

## Key Terms and Results

### TERMS
- **binary relation:** a subset $R \subseteq A \times B$.
- **reflexive / symmetric / antisymmetric / transitive:** foundational relational properties.
- **$n$-ary relation:** a subset of $A_1 \times \dots \times A_n$.
- **selection / projection / join:** primary relational database operators.
- **support / confidence / lift:** key metrics for association rules in data mining.
- **digraph / loop / path / circuit:** graph structures representing relations.
- **transitive closure / connectivity relation ($R^*$):** $\bigcup_{n=1}^\infty R^n$.
- **Warshall's algorithm:** $O(n^3)$ algorithm for computing transitive closures.
- **equivalence relation / equivalence classes / partition:** reflexive, symmetric, transitive relation that partitions the underlying set into disjoint classes.
- **poset / partial order:** reflexive, antisymmetric, transitive relation $(S, \preceq)$.
- **Hasse diagram:** transitively reduced upward-directed visualization of a finite poset.
- **lattice:** a poset where every pair has a unique $\text{lub}$ (join) and $\text{glb}$ (meet).
- **topological sorting:** linearizing a partial order into a compatible total order.

### RESULTS
- Reflexive closure: $R \cup \Delta$; Symmetric closure: $R \cup R^{-1}$.
- Transitive closure $R^* = \bigcup_{k=1}^n R^k$ (for $|A| = n$).
- Equivalence Theorem: $aRb \iff [a] = [b] \iff [a] \cap [b] \neq \emptyset$.
- Every equivalence relation defines a unique partition, and vice versa.
- Every finite nonempty poset has at least one minimal element (and can be topologically sorted).

---

## Review Questions

1–20. In-depth review covering definitions of relations, matrix/digraph representations, closures, Warshall’s algorithm, relational databases, equivalence relations, partitions, posets, Hasse diagrams, lattices, and topological sorting.

---

## Supplementary Exercises

1–50. Comprehensive problem sets covering string relations, non-standard relations, circular relations ($aRb \land bRc \implies cRa$), Erdős numbers, matrix powers, subroutines, quotient posets, Dilworth's theorem (chains/antichains), well-founded induction, distributive/modular lattices, and the game of Chomp on general posets.

---

## Computer Projects, Computations and Explorations, Writing Projects

- **Computer Projects (1–15):** Relational property checkers, matrix join/meet/product implementations, Warshall's algorithm, database projection and join operators, equivalence class extractors, and topological sort engines.
- **Computations and Explorations (1–9):** Exhaustive relation generation on small sets, large graph transitive closures, equivalence relations counting, and lattice visualizations.
- **Writing Projects (1–12):** Fuzzy relations, advanced relational algebra, Apriori algorithm, Roy-Warshall algorithm history, construction of $\mathbf{Q}$ via equivalence classes of $\mathbf{Z} \times (\mathbf{Z} \setminus \{0\})$, PERT/CPM project management methods, and modular/projective geometric lattices.
