# CHAPTER 11: Trees

- **11.1 Introduction to Trees**
- **11.2 Applications of Trees**
- **11.3 Tree Traversal**
- **11.4 Spanning Trees**
- **11.5 Minimum Spanning Trees**

A connected graph that contains no simple circuits is called a tree. Trees were used as long ago as 1857, when the English mathematician Arthur Cayley used them to count certain types of chemical compounds. Since that time, trees have been employed to solve problems in a wide variety of disciplines, as the examples in this chapter will show.

Trees are particularly useful in computer science, where they are employed in a wide range of algorithms. For instance, trees are used to construct efficient algorithms for locating items in a list. They can be used in algorithms, such as Huffman coding, that construct efficient codes saving costs in data transmission and storage. Trees can be used to study games such as checkers and chess and can help determine winning strategies for playing these games. Trees can be used to model procedures carried out using a sequence of decisions. Constructing these models can help determine the computational complexity of algorithms based on a sequence of decisions, such as sorting algorithms.

Procedures for building trees containing every vertex of a graph, including depth-first search and breadth-first search, can be used to systematically explore the vertices of a graph. Exploring the vertices of a graph via depth-first search, also known as backtracking, allows for the systematic search for solutions to a wide variety of problems, such as determining how eight queens can be placed on a chessboard so that no queen can attack another.

We can assign weights to the edges of a tree to model many problems. For example, using weighted trees we can develop algorithms to construct networks containing the least expensive set of telephone lines linking different network nodes.

---

## 11.1 Introduction to Trees

### 11.1.1 Definitions and Properties

> **DEFINITION 1**  
> A **tree** is a connected undirected graph with no simple circuits.  
> A **forest** is an undirected graph with no simple circuits (each connected component is a tree).

> **THEOREM 1**  
> An undirected graph is a tree if and only if there is a unique simple path between any two of its vertices.

---

### 11.1.2 Rooted Trees

> **DEFINITION 2**  
> A **rooted tree** is a tree in which one vertex has been designated as the root and every edge is directed away from the root.

#### Tree Terminology:
- **Parent ($u$):** The unique vertex such that there is a directed edge $u \to v$.
- **Child ($v$):** Any vertex with parent $u$.
- **Siblings:** Vertices with the same parent.
- **Ancestors:** Vertices on the path from the root to $v$, excluding $v$.
- **Descendants:** Vertices that have $v$ as an ancestor.
- **Leaf:** A vertex with no children.
- **Internal vertex:** A vertex that has children.
- **Subtree rooted at $a$:** The subgraph consisting of $a$, all its descendants, and their incident edges.

> **DEFINITION 3: $m$-ary Trees**  
> - An **$m$-ary tree** is a rooted tree where every internal vertex has at most $m$ children.  
> - A **full $m$-ary tree** is a rooted tree where every internal vertex has exactly $m$ children.  
> - A **binary tree** is an $m$-ary tree with $m = 2$ (each child is designated as a **left child** or a **right child**).

---

### 11.1.3 Trees as Models
- **Saturated Hydrocarbons ($C_n H_{2n+2}$):** Atoms = vertices (Carbon degree 4, Hydrogen degree 1). Vertices: $3n + 2$, Edges: $3n + 1 \implies$ Tree. Isomers correspond to nonisomorphic trees. (Arthur Cayley, 1857).
- **Organizational Trees:** Hierarchy charts.
- **Computer File Systems:** Directories = internal vertices, Files = leaves.
- **Tree-Connected Parallel Processors:** Complete binary tree of $n = 2^k - 1$ processors computing in $O(\log n)$ steps.

> **ARTHUR CAYLEY (1821–1895)**  
> English mathematician and lawyer who pioneered matrix algebra, group theory, higher-dimensional geometry, and the theory of trees in chemical graph enumeration.

---

### 11.1.4 Tree Counting Properties

> **THEOREM 2**  
> A tree with $n$ vertices has $n - 1$ edges.

> **THEOREM 3**  
> A full $m$-ary tree with $i$ internal vertices contains $n = mi + 1$ vertices.

> **THEOREM 4: Full $m$-ary Tree Identities**  
> For a full $m$-ary tree with $n$ vertices, $i$ internal vertices, and $l$ leaves:
> 1. Given $n$: $i = \frac{n-1}{m}$ and $l = \frac{(m-1)n + 1}{m}$.
> 2. Given $i$: $n = mi + 1$ and $l = (m-1)i + 1$.
> 3. Given $l$: $n = \frac{ml - 1}{m-1}$ and $i = \frac{l - 1}{m-1}$.

#### Levels, Height, and Balanced Trees:
- **Level of $v$:** Length of path from root to $v$ ($\text{level}(\text{root}) = 0$).
- **Height ($h$):** Maximum level of any vertex.
- **Balanced Tree:** All leaves are at levels $h$ or $h - 1$.

> **THEOREM 5 & COROLLARY 1**  
> In an $m$-ary tree of height $h$:
> $$l \le m^h \quad\text{and}\quad h \ge \lceil \log_m l \rceil.$$
> If the tree is full and balanced, then $h = \lceil \log_m l \rceil$.

---

### Exercises 11.1

1–2. Identifying trees among given graphs.  
3–4. Rooted tree anatomy: identifying root, internal vertices, leaves, children, parent, siblings, ancestors, and descendants.  
5–8. Checking full $m$-ary properties, vertex levels, and heights.  
9–10. Drawing subtrees.  
11–13. Enumerating nonisomorphic unrooted and rooted trees on 3, 4, and 5 vertices.  
14–15. Equivalent tree characterizations (minimally connected / maximally acyclic graphs, $e = n - 1$).  
16. Trees among complete bipartite graphs ($K_{1, n}$ stars).  
17–20. Vertex, edge, leaf, and internal vertex counts using Theorems 2, 3, 4.  
21–23. Rooted tree tournament elimination models and chain letter propagation trees.  
24–26. Existence and bounds for full/balanced $m$-ary trees with given height and leaf counts.  
27–30. Complete $m$-ary trees and leaf bounds in balanced trees ($l > m^{h-1}$).  
31. Number of edges in a forest with $t$ trees and $n$ vertices: $e = n - t$.  
32–35. Models: book table of contents, hydrocarbon isomers, organizational structures, file systems.  
36–37. Tree-connected parallel addition networks.  
38. Labeled trees and Cayley’s formula ($n^{n-2}$).  
39–43. Eccentricity, tree centers (every tree has 1 or 2 adjacent centers).  
44. 2-colorability of trees (every tree is bipartite).  
45–46. Rooted Fibonacci trees $T_n$.  
47. Fallacy in inductive tree path proof.  
48. Average leaf depth lower bound $\Omega(\log n)$.

---

## 11.2 Applications of Trees

### 11.2.1 Binary Search Trees (BST)

A **binary search tree** has key values such that for every vertex $v$:
$$\text{keys in left subtree}(v) < \text{key}(v) < \text{keys in right subtree}(v).$$

#### ALGORITHM 1: Locating / Inserting in a BST
```pascal
procedure insertion (T: binary search tree, x: item)
v := root of T
while v != null and label(v) != x
    if x < label(v) then
        if left child of v != null then v := left child of v
        else add new vertex as a left child of v and set v := null
    else
        if right child of v != null then v := right child of v
        else add new vertex as a right child of v and set v := null
if root of T = null then add a vertex v to the tree and label it with x
else if v is null or label(v) != x then label new vertex with x and let v be this new vertex
return v {v = location of x}
```
**Complexity:** Adding an item to a balanced BST with $n$ keys requires at most $\lceil \log_2(n + 1) \rceil$ comparisons ($O(\log n)$).

---

### 11.2.2 Decision Trees and Lower Bounds on Sorting

A **decision tree** models algorithms based on comparisons (internal vertices = comparisons, leaves = outcomes).

> **THEOREM 1, COROLLARY 1, & THEOREM 2**  
> - Any sorting algorithm based on binary comparisons requires at least $\lceil \log_2 n! \rceil$ comparisons.  
> - Worst-case complexity of comparison sorting is $\Omega(n \log n)$.  
> - Average-case complexity of comparison sorting is $\Omega(n \log n)$.

---

### 11.2.3 Prefix Codes and Huffman Coding

A **prefix code** ensures that no codeword is a prefix of another codeword. It is represented as a binary tree with characters at the leaves (left edge = 0, right edge = 1).

#### ALGORITHM 2: Huffman Coding
```pascal
procedure Huffman (C: symbols ai with frequencies wi, i = 1, ..., n)
F := forest of n rooted trees, each consisting of the single vertex ai with weight wi
while F is not a tree
    Replace trees T, T' of least weights with a new tree having root with left subtree T (edge 0)
    and right subtree T' (edge 1) and weight w(T) + w(T')
return tree {gives optimal prefix code}
```

> **DAVID A. HUFFMAN (1925–1999)**  
> American computer scientist at MIT and UC Santa Cruz who invented Huffman coding in 1951 for a term paper.

---

### 11.2.4 Game Trees and the Minimax Strategy

A **game tree** models two-player zero-sum games with perfect information (e.g., Nim, Tic-Tac-Toe, Chess).
- **Even level vertices (Boxes):** First player's turn ($\max$).
- **Odd level vertices (Circles):** Second player's turn ($\min$).
- **Leaves:** Payoff values ($+1$ for player 1 win, $-1$ for player 2 win, $0$ for draw).

> **DEFINITION 1 & THEOREM 3: Minimax Value**  
> $$\text{value}(v) = \begin{cases} \text{payoff}(v) & \text{if } v \text{ is a leaf}, \\ \max_{c \in \text{children}(v)} \text{value}(c) & \text{if } v \text{ is at an even level}, \\ \min_{c \in \text{children}(v)} \text{value}(c) & \text{if } v \text{ is at an odd level}. \end{cases}$$
> The minimax value at the root gives the game outcome under optimal play.

- **Pruning & Heuristics:** $\alpha$-$\beta$ pruning, heuristic evaluation functions (e.g., Deep Blue).

---

### Exercises 11.2

1–5. Building binary search trees for given word lists and sentences.  
6–10. Decision trees for counterfeit coin weighing puzzles on balance scales.  
11–12. Optimal sorting of 4 and 5 elements.  
13–18. Tournament sort algorithm, execution traces, and $\Theta(n \log n)$ proof.  
19–22. Validating prefix codes, tree constructions, and decoding bit strings.  
23–27. Constructing Huffman codes, computing expected code lengths, English letter frequency codes.  
28–31. $m$-ary Huffman coding, block Huffman coding, Fibonacci string codes.  
32. Proof of optimality of Huffman codes.  
33–36. Nim game trees and optimal winning strategies.  
37–38. Tic-tac-toe game trees and winning strategies.  
39–42. Piles analysis in Nim and checkers branch factors.  
43–44. Minimax algorithm pseudocode and evaluation functions.

---

## 11.3 Tree Traversal

### 11.3.1 Universal Address System
- Root is labeled $0$.
- Children of $r$ are labeled $1, 2, \dots, k$ from left to right.
- For vertex with label $A$, its $k_v$ children are labeled $A.1, A.2, \dots, A.k_v$.
- Lexicographic ordering of addresses orders all vertices.

---

### 11.3.2 Traversal Algorithms

1. **Preorder Traversal (Root $\to$ Subtrees):**
   ```pascal
   procedure preorder (T: ordered rooted tree)
   r := root of T; list r
   for each child c of r from left to right: preorder(T(c))
   ```
2. **Inorder Traversal (Leftmost Subtree $\to$ Root $\to$ Remaining Subtrees):**
   ```pascal
   procedure inorder (T: ordered rooted tree)
   r := root of T
   if r is a leaf then list r
   else
       l := first child of r; inorder(T(l))
       list r
       for each other child c of r: inorder(T(c))
   ```
3. **Postorder Traversal (Subtrees $\to$ Root):**
   ```pascal
   procedure postorder (T: ordered rooted tree)
   r := root of T
   for each child c of r from left to right: postorder(T(c))
   list r
   ```

---

### 11.3.3 Infix, Prefix, and Postfix Notations
- **Infix form:** Inorder traversal of expression tree (requires parentheses).
- **Prefix form (Polish Notation):** Preorder traversal (evaluated right to left, no parentheses needed).
- **Postfix form (Reverse Polish Notation):** Postorder traversal (evaluated left to right, stack-based).

> **JAN ŁUKASIEWICZ (1878–1956)**  
> Polish logician of the Warsaw School of Logic who invented parenthesis-free Polish prefix notation.

---

### Exercises 11.3

1–6. Universal address systems and lexicographical vertex orderings.  
7–15. Preorder, inorder, and postorder traversal listings of given trees.  
16–19. Constructing expression trees for arithmetic expressions, logic propositions, and set expressions; extracting prefix, postfix, and infix forms.  
20–21. Counting parenthesizations of infix expressions.  
22–24. Evaluating arithmetic expressions in prefix and postfix notations.  
25–29. Reconstructing ordered rooted trees from traversal sequences and child degree sequences.  
30–34. Well-formed formulas (WFF) in prefix and postfix notation, syntax rules, and operators.

---

## 11.4 Spanning Trees

### 11.4.1 Spanning Trees and IP Multicasting

> **DEFINITION 1 & THEOREM 1**  
> A **spanning tree** of a simple graph $G$ is a subgraph of $G$ that is a tree containing every vertex of $G$.  
> A simple graph is **connected if and only if it has a spanning tree**.

- **IP Multicasting:** Uses spanning trees without cycles to route datagrams from a source to multiple subnetwork recipients efficiently.

---

### 11.4.2 Depth-First Search (DFS) / Backtracking

Builds a path by successively visiting unvisited adjacent vertices; when stuck, backtracks to the most recent vertex with unvisited neighbors.

#### ALGORITHM 1: Depth-First Search (DFS)
```pascal
procedure DFS (G: connected graph with vertices v1, ..., vn)
T := tree consisting only of vertex v1
visit(v1)

procedure visit (v: vertex of G)
for each vertex w adjacent to v and not yet in T
    add vertex w and edge {v, w} to T
    visit(w)
```
- **Tree Edges:** Edges included in the DFS spanning tree.
- **Back Edges:** Edges of $G$ not in $T$ connecting a vertex to an ancestor/descendant in $T$.
- **Complexity:** $O(|E|)$ steps (or $O(n^2)$ using adjacency matrices).

---

### 11.4.3 Breadth-First Search (BFS)

Builds a spanning tree level by level by adding all unvisited neighbors of the current vertex to a FIFO queue.

#### ALGORITHM 2: Breadth-First Search (BFS)
```pascal
procedure BFS (G: connected graph with vertices v1, ..., vn)
T := tree consisting only of vertex v1
L := empty list
put v1 in the list L of unprocessed vertices
while L is not empty
    remove the first vertex, v, from L
    for each neighbor w of v
        if w is not in L and not in T then
            add w to the end of list L
            add w and edge {v, w} to T
```
- **Cross Edges:** Edges in $G \setminus T$ connect vertices at the same level or adjacent levels ($\Delta \text{level} \le 1$).
- **Shortest Paths:** The level of vertex $u$ in a BFS tree rooted at $v$ is the shortest path distance $d(u, v)$.
- **Complexity:** $O(|E|)$ steps.

---

### 11.4.4 Backtracking Applications
1. **Graph Coloring:** Backtracks when a vertex cannot be assigned any of the $n$ available colors.
2. **$n$-Queens Problem:** Placing $n$ non-attacking queens on an $n \times n$ chessboard.
3. **Subset Sum:** Finding a subset summing to target $M$.
4. **Maze Solving:** Exploring paths and backtracking at dead ends.
5. **Web Crawlers:** Googlebot uses BFS on seed URLs with DFS extensions for deep exploration.

---

### Exercises 11.4

1. Edges removed to form a spanning tree: $m - (n - 1) = m - n + 1$.  
2–7. Constructing spanning trees by circuit breaking.  
8–12. Enumerating all spanning trees and nonisomorphic spanning trees ($K_3, K_4, K_5, C_5, K_{2,2}$).  
13–16. Generating spanning trees using DFS and BFS starting at root $a$.  
17–22. DFS and BFS spanning trees on $W_n, K_n, K_{m,n}, Q_n$.  
23. Airline route reductions.  
24–25. Shortest path distance via BFS level numbers.  
26–30. Backtracking applications: 3-coloring, $n$-queens ($n=3,5,6$), subset sum, and maze routing.  
31–33. Spanning forests for disconnected graphs ($m - n + c$ edges removed).  
34–38. Properties of BFS levels, cycle detection, component labeling, and bipartiteness testing.  
39–46. Unique spanning tree criteria, back edge theorem for DFS, and max edges without $P_k$ paths.  
47–52. BFS level order induction, preorder DFS vertex numberings, forward/back/cross edge classification in directed graphs.  
53–56. Spanning tree distance metric $d(T_1, T_2) = |E(T_1) \setminus E(T_2)|$ and edge-swap connectivity of spanning tree spaces.  
57–61. Arborescences (directed rooted spanning trees) and cycle detection via back edges.

---

## 11.5 Minimum Spanning Trees

### 11.5.1 Definitions

> **DEFINITION 1**  
> A **minimum spanning tree (MST)** in a connected weighted graph is a spanning tree with the smallest possible total edge weight.

---

### 11.5.2 MST Algorithms

#### 1. Prim’s Algorithm (Prim–Jarník)
Starts with a minimum weight edge, then iteratively adds the edge of minimum weight that connects a vertex in the current tree to a vertex outside the tree without forming a circuit.

```pascal
procedure Prim (G: weighted connected undirected graph with n vertices)
T := a minimum-weight edge
for i := 1 to n - 2
    e := an edge of minimum weight incident to a vertex in T and not forming a simple circuit in T
    T := T with e added
return T
```

#### 2. Kruskal’s Algorithm
Sorts all edges by weight, then successively adds the edge of smallest weight that does not form a simple circuit with previously chosen edges (maintaining a forest until $n - 1$ edges are added).

```pascal
procedure Kruskal (G: weighted connected undirected graph with n vertices)
T := empty graph
for i := 1 to n - 1
    e := any edge in G with smallest weight that does not form a simple circuit when added to T
    T := T with e added
return T
```

#### 3. Sollin’s Algorithm (Borůvka’s Algorithm)
Each component in the current forest simultaneously selects its cheapest outgoing edge. Terminates in at most $\lceil \log_2 n \rceil$ phases.

#### 4. Reverse-Delete Algorithm
Iteratively removes the edge of maximum weight from $G$ as long as its removal does not disconnect the graph.

#### Complexity Comparison:
- **Kruskal:** $O(m \log m) = O(m \log n)$ (better for sparse graphs).
- **Prim:** $O(m + n \log n)$ with Fibonacci heaps ($O(m \log n)$ with binary heaps).

> **ROBERT CLAY PRIM (BORN 1921)** & **JOSEPH BERNARD KRUSKAL (1928–2010)**  
> American mathematicians who developed the two standard MST algorithms at Bell Labs in the 1950s (building on earlier 1926/1930 work by Borůvka and Jarník).

---

### Exercises 11.5

1. Road paving cost minimization in Nevada towns network.  
2–4. Step-by-step traces of Prim’s algorithm on weighted graphs.  
5–8. Step-by-step traces of Kruskal’s algorithm on weighted graphs.  
9. Smallest graph with multiple MSTs.  
10. Minimum spanning forests.  
11–15. Maximum spanning tree algorithms.  
16–17. Finding the second least expensive spanning tree.  
18–19. Uniqueness of MST when all edge weights are distinct.  
20–23. Constrained MST containing prescribed edges.  
24–31. Sollin’s (Borůvka’s) algorithm: traces, pseudocode, correctness proof, and $O(\log n)$ phase bound.  
32–33. Proof of correctness of Kruskal’s algorithm and cycle cut property.  
34–35. Reverse-delete algorithm pseudocode and correctness proof.

---

## Key Terms and Results

### TERMS
- **tree / forest:** connected acyclic graph / acyclic graph.
- **rooted tree / parent / child / sibling / ancestor / descendant / leaf / internal vertex:** rooted hierarchy terms.
- **$m$-ary tree / full $m$-ary tree / binary tree / balanced tree:** structural tree classifications.
- **binary search tree (BST):** search structure with ordered subtrees.
- **decision tree / game tree / minimax strategy:** decision and game theory structures.
- **prefix code / Huffman code:** data compression codes.
- **preorder / inorder / postorder traversal:** systematic vertex visitation orderings.
- **prefix / infix / postfix notation:** expression representations.
- **spanning tree / minimum spanning tree (MST):** skeleton trees spanning all vertices.
- **DFS / BFS / backtracking:** graph exploration paradigms.
- **tree edge / back edge / forward edge / cross edge:** edge classifications in DFS/BFS trees.
- **Prim’s / Kruskal’s / Borůvka’s / Reverse-Delete algorithms:** MST construction methods.

### RESULTS
- Tree Characterization: $G$ is a tree $\iff$ unique simple path between every pair of vertices $\iff$ connected and $e = n - 1$.
- Full $m$-ary Tree: $n = mi + 1$, $l = (m-1)i + 1$.
- Height Bound: $l \le m^h \implies h \ge \lceil \log_m l \rceil$.
- Comparison Sorting Lower Bound: $\Omega(n \log n)$ comparisons.
- Huffman codes produce optimal prefix codes.
- Minimax values at game tree roots determine game outcomes.
- A connected simple graph has a spanning tree.
- Prim's and Kruskal's greedy algorithms always produce an optimal MST.

---

## Review Questions

1–19. Comprehensive review covering definitions of trees/forests, rooted trees, counting properties, binary search trees, prefix codes, Huffman coding, game trees and minimax strategy, tree traversals, infix/prefix/postfix notation, sorting lower bounds, spanning trees, DFS and BFS, backtracking, and Prim's/Kruskal's MST algorithms.

---

## Supplementary Exercises

1–47. Advanced problem sets covering edge addition circuit properties, nonisomorphic rooted trees of size 6, degree sequences of trees, planarity and bipartiteness of trees, B-trees, binomial trees $B_k$, $S_k$-trees, level-order traversals, universal addresses, cut sets, cacti graphs, degree-constrained spanning trees, graceful trees, caterpillars, Huffman codes for independent bit blocks, arborescences, and directed strong component algorithms.

---

## Computer Projects, Computations and Explorations, Writing Projects

- **Computer Projects (1–18):** Tree recognition, tree navigation, BST construction and search, universal address labeling, tree traversal implementations, expression evaluators, Huffman coding, Nim solver, DFS and BFS spanning trees, $n$-queens and subset-sum solvers, Prim's and Kruskal's MST builders.
- **Computations and Explorations (1–8):** Tree enumeration, ASCII Huffman coding, Cayley's tree formula ($n^{n-2}$), sorting comparisons benchmark, 50-state capital MST.
- **Writing Projects (1–18):** Cayley's chemical trees, evolutionary ancestral trees, AVL-trees, quad trees in image processing, heaps and heapsort, adaptive Huffman coding, alpha-beta pruning, chess engines (Deep Blue), IP multicast routing, and MST history (Borůvka, Jarník, Kruskal, Prim).
