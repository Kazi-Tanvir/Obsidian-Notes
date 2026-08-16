# CHAPTER 10: Graphs

- **10.1 Graphs and Graph Models**
- **10.2 Graph Terminology and Special Types of Graphs**
- **10.3 Representing Graphs and Graph Isomorphism**
- **10.4 Connectivity**
- **10.5 Euler and Hamilton Paths**
- **10.6 Shortest-Path Problems**
- **10.7 Planar Graphs**
- **10.8 Graph Coloring**

Graphs are discrete structures consisting of vertices and edges that connect these vertices. There are different kinds of graphs, depending on whether edges have directions, whether multiple edges can connect the same pair of vertices, and whether loops are allowed. Problems in almost every conceivable discipline can be solved using graph models. We will give examples to illustrate how graphs are used as models in a variety of areas. For instance, we will show how graphs are used to represent the competition of different species in an ecological niche, how graphs are used to represent who influences whom in an organization, and how graphs are used to represent the outcomes of round-robin tournaments. We will describe how graphs can be used to model acquaintanceships between people, collaboration between researchers, telephone calls between telephone numbers, and links between websites. We will show how graphs can be used to model roadmaps and the assignment of jobs to employees of an organization.

Using graph models, we can determine whether it is possible to walk down all the streets in a city without going down a street twice, and we can find the number of colors needed to color the regions of a map. Graphs can be used to determine whether a circuit can be implemented on a planar circuit board. We can distinguish between two chemical compounds with the same molecular formula but different structures using graphs. We can determine whether two computers are connected by a communications link using graph models of computer networks. Graphs with weights assigned to their edges can be used to solve problems such as finding the shortest path between two cities in a transportation network. We can also use graphs to schedule exams and assign channels to television stations. This chapter will introduce the basic concepts of graph theory and present many different graph models. To solve the wide variety of problems that can be studied using graphs, we will introduce many different graph algorithms. We will also study the complexity of these algorithms.

---

## 10.1 Graphs and Graph Models

### 10.1.1 Definitions and Graph Terminology

> **DEFINITION 1**  
> A **graph** $G = (V, E)$ consists of $V$, a nonempty set of **vertices** (or **nodes**) and $E$, a set of **edges**. Each edge has either one or two vertices associated with it, called its **endpoints**. An edge is said to **connect** its endpoints.

> **DEFINITION 2**  
> A **directed graph** (or **digraph**) $(V, E)$ consists of a nonempty set of vertices $V$ and a set of directed edges (or arcs) $E$. Each directed edge is associated with an ordered pair of vertices. The directed edge associated with the ordered pair $(u, v)$ is said to start at $u$ and end at $v$.

#### TABLE 1: Graph Terminology
| Type | Edges | Multiple Edges Allowed? | Loops Allowed? |
| :--- | :--- | :---: | :---: |
| **Simple graph** | Undirected | No | No |
| **Multigraph** | Undirected | Yes | No |
| **Pseudograph** | Undirected | Yes | Yes |
| **Simple directed graph** | Directed | No | No |
| **Directed multigraph** | Directed | Yes | Yes |
| **Mixed graph** | Directed and undirected | Yes | Yes |

---

### 10.1.2 Graph Models
- **Social Networks:** Acquaintanceship graphs, friendship graphs, influence graphs (directed), academic collaboration graphs (Erdős numbers), Hollywood graphs (Bacon numbers).
- **Communication Networks:** Call graphs (telephone networks), computer networks.
- **Information Networks:** The Web graph (directed), citation graphs.
- **Software Design:** Module dependency graphs, precedence graphs in concurrent processing.
- **Transportation Networks:** Airline route multigraphs, road networks (mixed graphs).
- **Biological Networks:** Niche overlap graphs in ecology, protein interaction graphs (PPI networks).
- **Semantic Networks:** Word similarity graphs in Natural Language Understanding (NLU).
- **Tournaments:** Round-robin tournaments (directed complete graphs), single-elimination tournament trees.

---

### Exercises 10.1

1–2. Drawing and choosing graph models for airline routes and interstate highways.  
3–9. Identifying graph types (simple, multigraph, pseudograph, directed multigraph) from drawings.  
10–12. Converting graphs to simple graphs; reflexivity/symmetry of graph-induced relations.  
13. Intersection graphs of families of sets.  
14–15. Niche overlap graphs.  
16–17. Acquaintanceship and contemporaneous historical figures graphs.  
18–19. Influence graphs of organizations.  
20–21. Word association semantic networks.  
22–23. Round-robin tournament modeling.  
24–28. Telephone call graphs, email communication networks, and alias detection.  
29–33. Party acquaintance, subway network, academic prerequisite, movie critic, and marriage models.  
34–35. Precedence graphs for computer program instruction scheduling.  
36–38. Weighted and multi-relational graphs for communication.

---

## 10.2 Graph Terminology and Special Types of Graphs

### 10.2.1 Basic Terminology

> **DEFINITION 1 & 2**  
> - Two vertices $u$ and $v$ in an undirected graph $G$ are called **adjacent** (or **neighbors**) if $u$ and $v$ are endpoints of an edge $e$. Edge $e$ is **incident** with $u$ and $v$.  
> - The **neighborhood** of a vertex $v$, denoted $N(v)$, is the set of all neighbors of $v$. For $A \subseteq V$, $N(A) = \bigcup_{v \in A} N(v)$.

> **DEFINITION 3: Degree of a Vertex**  
> The **degree** of a vertex $v$ in an undirected graph, denoted $\deg(v)$, is the number of edges incident with it, except that a loop contributes 2 to the degree.  
> A vertex with degree 0 is **isolated**; a vertex with degree 1 is **pendant**.

> **THEOREM 1: THE HANDSHAKING THEOREM**  
> Let $G = (V, E)$ be an undirected graph with $m$ edges. Then
> $$2m = \sum_{v \in V} \deg(v).$$

> **THEOREM 2**  
> An undirected graph has an even number of vertices of odd degree.

#### Directed Graphs Terminology:
- **In-degree ($\deg^-(v)$):** Number of edges with $v$ as terminal vertex.
- **Out-degree ($\deg^+(v)$):** Number of edges with $v$ as initial vertex.
- **Theorem 3:** $\sum_{v \in V} \deg^-(v) = \sum_{v \in V} \deg^+(v) = |E|$.

---

### 10.2.2 Special Simple Graphs

1. **Complete Graphs ($K_n$):** Exactly one edge between every pair of vertices. $|V| = n, |E| = \binom{n}{2} = \frac{n(n-1)}{2}$.
2. **Cycles ($C_n, n \ge 3$):** Vertices $v_1, \dots, v_n$ connected in a circle. $|V| = n, |E| = n$.
3. **Wheels ($W_n, n \ge 3$):** Cycle $C_n$ with an additional hub vertex connected to all $n$ vertices. $|V| = n + 1, |E| = 2n$.
4. **$n$-Cubes ($Q_n$):** Vertices represent $2^n$ bit strings of length $n$; adjacent if strings differ in exactly 1 bit. $|V| = 2^n, |E| = n 2^{n-1}$.

---

### 10.2.3 Bipartite Graphs and Matchings

> **DEFINITION 6: Bipartite Graph**  
> A simple graph $G = (V, E)$ is **bipartite** if $V = V_1 \cup V_2$ where $V_1 \cap V_2 = \emptyset$, and every edge connects a vertex in $V_1$ to a vertex in $V_2$.

> **THEOREM 4: 2-Colorability Characterization**  
> A simple graph is bipartite if and only if its vertices can be colored using two colors such that no two adjacent vertices share the same color (i.e., $\chi(G) \le 2$).

- **Complete Bipartite Graph ($K_{m, n}$):** $V_1$ has $m$ vertices, $V_2$ has $n$ vertices; every vertex in $V_1$ is adjacent to every vertex in $V_2$. $|V| = m + n, |E| = mn$.

#### Matchings:
- A **matching** $M \subseteq E$ has no two edges sharing a vertex.
- A **complete matching** from $V_1$ to $V_2$ matches every vertex of $V_1$ ($|M| = |V_1|$).

> **THEOREM 5: HALL’S MARRIAGE THEOREM**  
> The bipartite graph $G = (V, E)$ with bipartition $(V_1, V_2)$ has a complete matching from $V_1$ to $V_2$ if and only if
> $$|N(A)| \ge |A| \quad\text{for all subsets } A \subseteq V_1.$$

> **PHILIP HALL (1904–1982)**  
> British mathematician at Cambridge who made seminal contributions to group theory and combinatorics, and worked as a cryptographer at Bletchley Park.

---

### 10.2.4 Parallel Computer Interconnection Networks
- **Linear array:** Processors $P_1, \dots, P_n$ chained linearly.
- **Mesh network ($m \times m$):** $n = m^2$ processors on a 2D grid; each interior node connects to 4 neighbors. Communication takes $O(\sqrt{n})$ hops.
- **Hypercube network ($Q_m$):** $n = 2^m$ processors; degree $m = \log_2 n$, max communication distance $m = \log_2 n$ hops.

---

### 10.2.5 Subgraphs, Operations, and Graph Unions
- **Subgraph:** $H = (W, F)$ where $W \subseteq V, F \subseteq E$.
- **Induced Subgraph:** Subgraph induced by $W \subseteq V$ containing all edges of $G$ with both endpoints in $W$.
- **Vertex / Edge Removal:** $G - v$, $G - e$.
- **Edge Contraction:** Merges endpoints $u, v$ of edge $e$ into a single vertex.
- **Graph Union:** $G_1 \cup G_2 = (V_1 \cup V_2, E_1 \cup E_2)$.

---

### Exercises 10.2

1–4. Vertex degrees, edge counts, and verification of Handshaking Theorem.  
5–6. Parity of odd-degree vertices and party handshake problem.  
7–10. In-degrees and out-degrees in directed multigraphs.  
11–17. Interpretations of vertex degrees in social, web, and tournament graphs.  
18–19. Proving that every simple graph with $\ge 2$ vertices has two vertices of equal degree.  
20. Drawing standard graphs ($K_7, K_{1,8}, K_{4,4}, C_7, W_7, Q_4$).  
21–26. Bipartite graph verification and characterization for $K_n, C_n, W_n, Q_n$.  
27–30. Job assignment and marriage models via bipartite graphs.  
31–33. Applications of Hall's Marriage Theorem ($k$-regular bipartite graphs, tournament schedules).  
34. Ore's deficiency theorem for bipartite matchings.  
35–37. Subgraphs, vertex/edge counts of standard graph families.  
38–43. Degree sequences of graphs.  
44–48. Havel–Hakimi theorem and graphic sequences.  
49–54. Degree bounds and regular graphs.  
55–57. $n$-regular graphs and completeness.  
58–60. Computing graph unions.  
61–67. Complementary graphs $\overline{G}$, self-complementary graphs, and edge bounds ($e \le v^2/4$ for bipartite graphs).  
68–72. 2-coloring bipartite testing algorithm and converse digraphs.  
73–75. Mesh network processor architectures and routing hops.

---

## 10.3 Representing Graphs and Graph Isomorphism

### 10.3.1 Adjacency Lists, Adjacency Matrices, and Incidence Matrices

1. **Adjacency List:** Specifies for each vertex the list of its adjacent vertices.
2. **Adjacency Matrix ($A = [a_{ij}]$):**
   $$a_{ij} = \begin{cases} 1 & \text{if } \{v_i, v_j\} \in E, \\ 0 & \text{otherwise.} \end{cases}$$
   (For multigraphs/pseudographs, $a_{ij}$ is the number of edges connecting $v_i, v_j$; diagonal $a_{ii}$ counts loops).
3. **Incidence Matrix ($M = [m_{ij}]$):** Size $n \times m$, where $m_{ij} = 1$ if edge $e_j$ is incident with vertex $v_i$, and $0$ otherwise.

---

### 10.3.2 Graph Isomorphism

> **DEFINITION 1**  
> Simple graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are **isomorphic** if there exists a bijection $f: V_1 \to V_2$ such that
> $$\{a, b\} \in E_1 \iff \{f(a), f(b)\} \in E_2 \quad\text{for all } a, b \in V_1.$$

#### Graph Invariants under Isomorphism:
- Number of vertices $|V|$
- Number of edges $|E|$
- Degree sequence (number of vertices of each degree)
- Subgraph structures and lengths of simple circuits

> **LÁSZLÓ BABAI (2015/2017)**  
> Developed a landmark algorithm determining graph isomorphism in quasi-polynomial time $2^{O((\log n)^c)}$.

---

### Exercises 10.3

1–4. Adjacency list representations.  
5–9. Adjacency matrices of standard graph families.  
10–12. Reconstructing graphs from adjacency matrices.  
13–18. Adjacency matrices for multigraphs and pseudographs.  
19–24. Directed graph adjacency matrices.  
25–28. Graph density $D = \frac{2|E|}{|V|(|V|-1)}$ and sparse vs. dense classification.  
29–35. Properties of adjacency and incidence matrix row/column sums.  
36–37. Matrix forms for $K_n, C_n, W_n, K_{m,n}, Q_n$.  
38–48. Proving graph isomorphism or exhibiting invariants to prove nonisomorphism.  
49–53. Equivalence relation of isomorphism, bipartite block form $\begin{bmatrix} 0 & A \\ B & 0 \end{bmatrix}$.  
54–57. Self-complementary graphs ($G \cong \overline{G} \implies v \equiv 0, 1 \pmod 4$).  
58–62. Enumerating nonisomorphic graphs on small vertex sets.  
63–70. Isomorphism of matrix representations and directed graphs.  
71–78. Storage complexity of graph representations (adjacency list $O(|V| + |E|)$ vs. matrix $O(|V|^2)$) and polynomial verification of isomorphism witnesses.

---

## 10.4 Connectivity

### 10.4.1 Paths, Circuits, and Connectedness

> **DEFINITION 1 & 2**  
> In an undirected graph $G$, a **path of length $n$** from $u$ to $v$ is a sequence of edges $e_1, e_2, \dots, e_n$ visiting vertices $x_0 = u, x_1, \dots, x_n = v$.  
> A **circuit** is a path of length $\ge 1$ with $x_0 = x_n$.  
> A path/circuit is **simple** if it contains no repeated edge.

> **THEOREM 1**  
> There is a simple path between every pair of distinct vertices of a connected undirected graph.

- **Connected Component:** A maximal connected subgraph of $G$.

---

### 10.4.2 Vertex and Edge Connectivity

- **Cut vertex (articulation point):** Vertex $v$ whose removal increases the number of connected components ($G - v$).
- **Cut edge (bridge):** Edge $e$ whose removal increases the number of connected components ($G - e$).
- **Vertex cut (separating set):** Subset $V' \subset V$ such that $G - V'$ is disconnected.
- **Vertex connectivity ($\kappa(G)$):** Minimum size of a vertex cut. ($\kappa(K_n) = n - 1$).
- **Edge connectivity ($\lambda(G)$):** Minimum size of an edge cut.

> **FUNDAMENTAL CONNECTIVITY INEQUALITY**  
> For any graph $G$:
> $$\kappa(G) \le \lambda(G) \le \min_{v \in V} \deg(v).$$

---

### 10.4.3 Connectedness in Directed Graphs

> **DEFINITION 4 & 5**  
> - A directed graph is **strongly connected** if there is a directed path from $a$ to $b$ and from $b$ to $a$ for all pairs of vertices $a, b$.  
> - A directed graph is **weakly connected** if its underlying undirected graph is connected.

- **Strongly Connected Components:** Maximal strongly connected subgraphs (partitions the vertex set).
- **The Web Graph:** Giant Strongly Connected Component (GSCC) containing over 53 million pages.

---

### 10.4.4 Counting Paths via Matrix Powers

> **THEOREM 2**  
> Let $A$ be the adjacency matrix of a graph $G$. The number of different paths of length $r$ from $v_i$ to $v_j$ equals the $(i, j)$th entry of $A^r$.

---

### Exercises 10.4

1–2. Path identification and simple circuit detection.  
3–6. Graph connectedness and component enumeration.  
7–10. Social/academic component structures (Erdős and Bacon components).  
11–15. Strong and weak connectivity in digraphs; identifying strong components.  
16–18. Mutual reachability equivalence relation.  
19–27. Counting paths of length $n$ using adjacency matrix powers $A^n$.  
28–30. Minimum edge counts in connected graphs ($|E| \ge n - 1$) and odd-degree paths.  
31–37. Cut vertices, cut edges, and nonseparable graphs.  
38–39. Characterization of bridges (not on any simple circuit) and network reliability backup design.  
40–41. Vertex basis in directed graphs.  
42–45. Component bounds and maximum edges in disconnected graphs $\le \frac{(n-k)(n-k+1)}{2}$.  
46–47. Block diagonal matrices of disconnected graphs and nonisomorphic connected graphs.  
48–55. Verifying $\kappa(G) \le \lambda(G) \le \min \deg(v)$ on standard and custom graphs.  
56–60. Shortest path finding via $A^r$ and simple circuit length as an isomorphism invariant.  
61–63. Connectivity and odd-cycle bipartite characterization ($G$ bipartite $\iff$ no odd cycles).  
64–66. State-space river crossing puzzles: Wolf-Goat-Cabbage, Jealous Husbands, and Water Jugs.

---

## 10.5 Euler and Hamilton Paths

### 10.5.1 Euler Paths and Circuits

> **DEFINITION 1**  
> - An **Euler circuit** in a graph $G$ is a simple circuit containing every edge of $G$.  
> - An **Euler path** in $G$ is a simple path containing every edge of $G$.

> **THEOREM 1 (Euler Circuit Theorem)**  
> A connected multigraph with at least two vertices has an Euler circuit if and only if **every vertex has even degree**.

> **THEOREM 2 (Euler Path Theorem)**  
> A connected multigraph has an Euler path (and not an Euler circuit) if and only if it has **exactly two vertices of odd degree** (which serve as the start and end of the path).

#### Constructive Algorithms:
- **Hierholzer's / Euler's Algorithm (Algorithm 1):** Splicing subcircuits in $O(|E|)$ time.
- **Fleury’s Algorithm:** Bridge avoidance edge traversal.
- **Directed Graph Euler Criteria:** Weakly connected and $\deg^-(v) = \deg^+(v)$ for all $v$ (circuit) or for all but two vertices (path).

> **LEONHARD EULER (1707–1783)**  
> Swiss mathematician who solved the Königsberg bridge problem in 1736, founding graph theory.

---

### 10.5.2 Hamilton Paths and Circuits

> **DEFINITION 2**  
> - A **Hamilton path** is a simple path that visits every vertex of $G$ exactly once.  
> - A **Hamilton circuit** is a simple circuit that visits every vertex of $G$ exactly once.

> **THEOREM 3 (Dirac’s Theorem)**  
> If $G$ is a simple graph with $n \ge 3$ vertices such that $\deg(v) \ge n/2$ for every vertex $v$, then $G$ has a Hamilton circuit.

> **THEOREM 4 (Ore’s Theorem)**  
> If $G$ is a simple graph with $n \ge 3$ vertices such that $\deg(u) + \deg(v) \ge n$ for every pair of nonadjacent vertices $u$ and $v$, then $G$ has a Hamilton circuit.

#### Applications:
- **Traveling Salesperson Problem (TSP):** Minimum weight Hamilton circuit in a complete weighted graph.
- **Gray Codes:** Hamilton circuits on the $n$-cube $Q_n$.
- **Knight’s Tours:** Hamilton paths/circuits on the chessboard knight move graph.

> **SIR WILLIAM ROWAN HAMILTON (1805–1865)**  
> Irish mathematician and astronomer who invented quaternions and the Icosian Game.

---

### Exercises 10.5

1–8. Determining and constructing Euler circuits/paths on undirected graphs.  
9–10. Königsberg bridge variations and river island bridge maps.  
11–12. Street sweeping / centerline painting models and path construction algorithms.  
13–15. Continuous one-line drawing puzzles (Mohammed's scimitars).  
16–17. Necessary and sufficient conditions for Euler circuits/paths in directed multigraphs.  
18–25. Finding Euler circuits/paths in directed graphs and algorithm designs.  
26–28. Euler circuit/path conditions for $K_n, C_n, W_n, Q_n, K_{m,n}$.  
29. Minimum pencil lifts when drawing graphs without retracing.  
30–36. Identifying and constructing Hamilton circuits/paths.  
37–43. Testing for Hamilton paths on given graphs.  
44–45. Hamilton circuit criteria for $K_n, C_n, W_n, Q_n, K_{m,n}$.  
46. The Petersen graph has no Hamilton circuit (but $G - v$ has one).  
47–48. Applying Dirac's and Ore's theorems to determine Hamilton circuits.  
49. Induction proof of Gray codes of order $n$ (Hamilton circuit on $Q_n$).  
50–53. Fleury’s algorithm implementation and correctness proofs.  
54. Network link testing vs. device testing paths.  
55. Bipartite graphs with an odd number of vertices have no Hamilton circuit.  
56–64. Knight’s Tour problems on $m \times n$ chessboards, bipartite property of knight moves, and Warnsdorff’s heuristic.  
65–66. Proof outline of Ore’s Theorem and edge-closure property.  
67–68. Non-Hamiltonian graph counterexample and $O(m)$ complexity proof of Euler circuit algorithm.

---

## 10.6 Shortest-Path Problems

### 10.6.1 Dijkstra’s Algorithm

Dijkstra’s algorithm finds the shortest path from a source vertex $a$ to a destination vertex $z$ (or all vertices) in a weighted graph with positive weights.

#### ALGORITHM 1: Dijkstra’s Algorithm
```pascal
procedure Dijkstra (G: weighted connected simple graph, with all weights positive)
{G has vertices a = v0, v1, ..., vn = z and lengths w(vi, vj)}
for i := 1 to n
    L(vi) := infinity
L(a) := 0
S := empty_set
while z not in S
    u := a vertex not in S with L(u) minimal
    S := S union {u}
    for all vertices v not in S
        if L(u) + w(u, v) < L(v) then
            L(v) := L(u) + w(u, v)
return L(z) {L(z) is the length of a shortest path from a to z}
```
**Complexity:** $O(n^2)$ additions and comparisons for an $n$-vertex graph.

> **EDSGER WYBE DIJKSTRA (1930–2002)**  
> Dutch computer scientist and Turing Award laureate who pioneered structured programming, semaphore concurrency, and the shortest-path algorithm.

---

### 10.6.2 All-Pairs Shortest Paths: Floyd’s Algorithm

#### ALGORITHM 2: Floyd’s Algorithm
```pascal
procedure Floyd (G: weighted simple graph)
for i := 1 to n
    for j := 1 to n
        d(vi, vj) := w(vi, vj)
for i := 1 to n
    for j := 1 to n
        for k := 1 to n
            if d(vj, vi) + d(vi, vk) < d(vj, vk) then
                d(vj, vk) := d(vj, vi) + d(vi, vk)
return [d(vi, vj)]
```
**Complexity:** $O(n^3)$ operations for all-pairs shortest paths.

---

### 10.6.3 The Traveling Salesperson Problem (TSP)
- Complete weighted graph with $n$ vertices.
- Exhaustive search evaluates $\frac{(n-1)!}{2}$ Hamilton circuits ($O(n!)$ time).
- TSP is NP-hard. Approximation algorithms achieve a factor $c = 3/2$ (Christofides' algorithm) under the triangle inequality.

---

### Exercises 10.6

1. Modeling subway time, distance, and fare minimization.  
2–7. Running Dijkstra’s algorithm to find shortest paths and path lengths.  
8–13. Airline distance, flight time, and fare route optimization; computer network response time and lease cost routing.  
14. Unweighted shortest path as a weighted shortest path with unit weights.  
15–16. Extending Dijkstra’s algorithm to record full paths and shortest paths to all vertices.  
17. New Jersey road distance vs. toll route optimization.  
18–20. Uniqueness of shortest paths, longest simple paths in weighted graphs.  
21–24. Floyd’s all-pairs algorithm execution, correctness proof ($O(n^3)$), and Dijkstra failure on negative weights.  
25–28. TSP instances on small complete graphs (cities and airfares).  
29–31. TSP variations with revisited vertices and DAG longest path via topological sorting.

---

## 10.7 Planar Graphs

### 10.7.1 Planar Graphs and Euler’s Formula

> **DEFINITION 1**  
> A graph is called **planar** if it can be drawn in the plane without any edges crossing.

> **THEOREM 1: EULER’S FORMULA**  
> Let $G$ be a connected planar simple graph with $e$ edges, $v$ vertices, and $r$ regions. Then
> $$r = e - v + 2.$$

#### Key Corollaries:
> **COROLLARY 1:** If $G$ is a connected planar simple graph with $v \ge 3$, then $e \le 3v - 6$.  
> **COROLLARY 2:** Every connected planar simple graph has a vertex of degree $\le 5$.  
> **COROLLARY 3:** If $G$ is a connected planar simple graph with $v \ge 3$ and no circuits of length 3, then $e \le 2v - 4$.

#### Nonplanarity of $K_5$ and $K_{3,3}$:
- $K_5$: $v = 5, e = 10 \implies 3v - 6 = 9 < 10$, violating Corollary 1 $\implies K_5$ is nonplanar.
- $K_{3,3}$: $v = 6, e = 9$, no triangles $\implies 2v - 4 = 8 < 9$, violating Corollary 3 $\implies K_{3,3}$ is nonplanar.

---

### 10.7.2 Kuratowski’s Theorem

- **Elementary Subdivision:** Replacing an edge $\{u, v\}$ by a vertex $w$ and edges $\{u, w\}, \{w, v\}$.
- **Homeomorphic Graphs:** Graphs obtainable from the same graph by a sequence of elementary subdivisions.

> **THEOREM 2: KURATOWSKI’S THEOREM**  
> A graph is nonplanar if and only if it contains a subgraph homeomorphic to $K_{3,3}$ or $K_5$.

> **KAZIMIERZ KURATOWSKI (1896–1980)**  
> Polish mathematician of the Warsaw School who made foundational contributions to topology and set theory, and proved the planarity criterion in 1930.

---

### Exercises 10.7

1. Three houses and two utilities ($K_{3,2}$ is planar).  
2–4. Redrawing planar graphs without crossings.  
5–9. Determining graph planarity and drawing planar embeddings.  
10–11. Geometric proofs that $K_{3,3}$ and $K_5$ are nonplanar.  
12–14. Region counts via Euler’s formula $r = e - v + 2$.  
15–17. Proving Corollaries 1, 2, 3 and girth-based inequalities ($e \le \frac{g}{g-2}(v - 2)$).  
18. Euler's formula for graphs with $k$ connected components: $r = e - v + k + 1$.  
19. Minimally nonplanar graphs ($K_5 - v, K_{3,3} - v$).  
20–22. Homeomorphism to $K_{3,3}$.  
23–25. Kuratowski's theorem reductions for complex graphs.  
26–29. Crossing numbers $\text{cr}(G)$ of $K_5, K_6, K_7, K_{m,n}$, Petersen graph ($\text{cr} = 2$).  
30–35. Graph thickness $\theta(G)$ bounds ($\theta(G) \ge \lceil \frac{e}{3v-6} \rceil$).  
36–37. Toroidal embeddings of $K_5$ and $K_{3,3}$ (genus 1).

---

## 10.8 Graph Coloring

### 10.8.1 Vertex Colorings and Chromatic Number

> **DEFINITION 1 & 2**  
> - A **coloring** of a simple graph assigns colors to vertices such that no two adjacent vertices share the same color.  
> - The **chromatic number** $\chi(G)$ is the least number of colors needed to color $G$.

#### Chromatic Numbers of Standard Families:
- Complete Graph: $\chi(K_n) = n$
- Bipartite Graph: $\chi(K_{m,n}) = 2$ (for $m, n \ge 1$)
- Cycle Graph: $\chi(C_n) = \begin{cases} 2 & \text{if } n \text{ is even}, \\ 3 & \text{if } n \text{ is odd.} \end{cases}$
- Wheel Graph: $\chi(W_n) = \begin{cases} 3 & \text{if } n \text{ is even}, \\ 4 & \text{if } n \text{ is odd.} \end{cases}$

> **THEOREM 1: THE FOUR COLOR THEOREM**  
> The chromatic number of every planar graph is no greater than four:
> $$\chi(G) \le 4 \quad\text{for all planar } G.$$
> *(Proved by Appel and Haken in 1976 using computer verification).*

> **ALFRED BRAY KEMPE (1849–1922)**  
> English barrister whose 1879 Kempe chain argument paved the way for the eventual four color proof.

---

### 10.8.2 Applications of Graph Colorings
- **Exam Scheduling:** Vertices = courses, edges = conflicting students, colors = exam time slots.
- **Frequency Assignment:** Vertices = radio/TV transmitters, edges = distance $< 150$ miles, colors = broadcast channels.
- **Register Allocation in Compilers:** Vertices = variables, edges = overlapping live ranges, colors = CPU index registers.

---

### 10.8.3 Edge Coloring and the Art Gallery Problem
- **Edge Chromatic Number ($\chi'(G)$):** Smallest number of colors to color edges so no two incident edges share a color. Vizing's theorem: $\Delta(G) \le \chi'(G) \le \Delta(G) + 1$.
- **The Art Gallery Theorem (Chvátal):** Every simple polygon with $n$ vertices can be guarded by at most $\lfloor n/3 \rfloor$ guards (proved via 3-coloring of triangulations).

---

### Exercises 10.8

1–4. Dual graph construction and region coloring.  
5–11. Calculating chromatic numbers of given graphs.  
12–15. Chromatic numbers of subgraphs, $W_n$, and odd-circuit chromatic obstruction.  
16–20. Applications: Exam timetabling, frequency assignments, committee meeting scheduling, zoo animal habitats.  
21–26. Edge colorings, $\chi'(G)$, and Vizing bounds.  
27–28. Compiler register allocation.  
29–31. Welsh–Powell greedy coloring heuristic algorithm and non-optimality counterexamples.  
32–35. Chromatically $k$-critical graphs ($\deg(v) \ge k - 1$).  
36–39. $k$-tuple graph coloring $\chi_k(G)$ and cellular frequency reuse zones.  
40–41. Proof of the Six Color and Five Color Theorems for planar graphs.  
42–46. The Art Gallery Problem: proving $g(n) = \lfloor n/3 \rfloor$ via triangulation and 3-coloring.

---

## Key Terms and Results

### TERMS
- **simple graph / multigraph / pseudograph:** classification of undirected graphs by edges/loops.
- **degree / neighborhood / handshaking theorem:** fundamental vertex edge counts.
- **complete / cycle / wheel / hypercube:** standard graph families ($K_n, C_n, W_n, Q_n$).
- **bipartite / complete bipartite ($K_{m,n}$):** 2-colorable graphs.
- **matching / maximum matching / complete matching:** disjoint edge selections.
- **isomorphism / graph invariant:** structural equivalence between graphs.
- **path / circuit / simple path / connected component:** connectivity concepts.
- **cut vertex / cut edge / vertex connectivity $\kappa(G)$ / edge connectivity $\lambda(G)$:** network robustness metrics.
- **Euler circuit / Euler path:** traversing every edge once.
- **Hamilton circuit / Hamilton path:** visiting every vertex once.
- **Dijkstra's / Floyd's algorithms:** shortest path search methods.
- **planar graph / Euler's formula ($r = e - v + 2$):** crossing-free planar embeddings.
- **Kuratowski's theorem:** nonplanarity characterization via $K_5$ and $K_{3,3}$ minors.
- **chromatic number $\chi(G)$ / Four Color Theorem:** vertex coloring bounds.

### RESULTS
- Handshaking Theorem: $\sum \deg(v) = 2m$.
- Hall's Marriage Theorem: Complete matching exists $\iff |N(A)| \ge |A|, \forall A \subseteq V_1$.
- Connectivity: $\kappa(G) \le \lambda(G) \le \min \deg(v)$.
- Euler Theorem: Euler circuit $\iff$ all degrees even; Euler path $\iff$ exactly 2 odd degrees.
- Dirac ($\deg(v) \ge n/2$) and Ore ($\deg(u) + \deg(v) \ge n$) sufficient conditions for Hamilton circuits.
- Planar graphs: $e \le 3v - 6$ (no $K_5$), $e \le 2v - 4$ if triangle-free (no $K_{3,3}$).

---

## Review Questions

1–22. Comprehensive review covering simple/directed graphs, Handshaking Theorem, standard graph families, bipartite graphs, matrix/list representations, isomorphisms, connectivity, Euler/Hamilton circuits, Dijkstra's algorithm, planarity and Euler's formula, Kuratowski's theorem, and graph coloring.

---

## Supplementary Exercises

1–66. Comprehensive problem set covering $k$-regular graphs, complete multipartite graphs $K_{n_1, \dots, n_m}$, systems of distinct representatives (SDRs), clustering coefficients, cliques, minimum dominating sets, $n$-queens control graphs, self-converse graphs, graph orientations (Robbins' theorem), tournament Hamilton paths, bandwidth $B(G)$, radius and diameter, random graphs $G(n, p)$, and monotone graph properties.

---

## Computer Projects, Computations and Explorations, Writing Projects

- **Computer Projects (1–20):** Degree sequence computers, bipartite testers, adjacency/incidence matrix converters, graph isomorphism testers, path counters ($A^n$), connected component extractors, Euler/Hamilton solvers, Dijkstra/Floyd implementations, greedy colorers, exam schedulers.
- **Computations and Explorations (1–14):** Exhaustive generation of nonisomorphic graphs on $\le 6$ vertices, Gray code generation, Knight’s tour solvers, random graph connectivity percolation thresholds, TSP exact/approximation on US state capitals.
- **Writing Projects (1–25):** History of graph theory (Euler, Hamilton, Kempe), biological/ecological niche overlap, web graph GSCC structure, community detection, automated graph drawing, DNA sequence assembly via de Bruijn graphs and Euler paths, Chinese postman problem, VLSI book embeddings, Four Color Theorem computer verification, and random graph theory.
