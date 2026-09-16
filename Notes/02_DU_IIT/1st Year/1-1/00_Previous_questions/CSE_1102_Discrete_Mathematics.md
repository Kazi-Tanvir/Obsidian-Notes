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
<svg width="450" height="160" viewBox="0 0 680 240" xmlns="http://www.w3.org/2000/svg" style="font-family: serif; font-size: 15px; font-style: italic; background: white; border-radius: 8px;">
  <!-- Edges -->
  <g stroke="#000" stroke-width="1.8">
    <line x1="60" y1="120" x2="180" y2="40" />
    <line x1="60" y1="120" x2="180" y2="200" />
    <line x1="180" y1="40" x2="180" y2="200" />
    <line x1="180" y1="40" x2="310" y2="40" />
    <line x1="180" y1="200" x2="310" y2="40" />
    <line x1="180" y1="200" x2="310" y2="200" />
    <line x1="310" y1="40" x2="310" y2="200" />
    <line x1="310" y1="40" x2="440" y2="40" />
    <line x1="310" y1="200" x2="440" y2="200" />
    <line x1="440" y1="40" x2="440" y2="200" />
    <line x1="440" y1="40" x2="560" y2="120" />
    <line x1="440" y1="200" x2="560" y2="120" />
  </g>

  <!-- Edge Weights -->
  <g fill="#111" font-style="normal" font-size="14px" text-anchor="middle">
    <text x="110" y="70">4</text>
    <text x="110" y="180">3</text>
    <text x="170" y="125">2</text>
    <text x="245" y="30">5</text>
    <text x="235" y="115">3</text>
    <text x="245" y="218">6</text>
    <text x="320" y="125">1</text>
    <text x="375" y="30">5</text>
    <text x="375" y="218">5</text>
    <text x="430" y="125">2</text>
    <text x="510" y="70">7</text>
    <text x="510" y="180">4</text>
  </g>

  <!-- Nodes (Dots) -->
  <g fill="#000">
    <circle cx="60" cy="120" r="4.5" />
    <circle cx="180" cy="40" r="4.5" />
    <circle cx="180" cy="200" r="4.5" />
    <circle cx="310" cy="40" r="4.5" />
    <circle cx="310" cy="200" r="4.5" />
    <circle cx="440" cy="40" r="4.5" />
    <circle cx="440" cy="200" r="4.5" />
    <circle cx="560" cy="120" r="4.5" />
  </g>

  <!-- Vertex Labels -->
  <g fill="#000" font-size="16px">
    <text x="40" y="125">a</text>
    <text x="176" y="26">b</text>
    <text x="177" y="222">c</text>
    <text x="306" y="26">d</text>
    <text x="307" y="222">e</text>
    <text x="437" y="26">f</text>
    <text x="437" y="222">g</text>
    <text x="572" y="125">z</text>
  </g>
</svg>
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
MR1 = $$
\begin{bmatrix}
1 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}
$$

MR2 = 
$$
\begin{bmatrix}
1 & 0 & 1 \\
0 & 1 & 1 \\
1 & 0 & 0
\end{bmatrix}
$$

   b. Identify following as one-to-one, onto, both, neither, or not a function. [5]
   <div style="max-width: 500px; margin: auto;">
   <svg xmlns="http://www.w3.org/2000/svg" viewBox="15 10 505 340" width="100%" height="100%">
  <defs>
    <marker id="arrow" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="5" markerHeight="5" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#fff" />
    </marker>
  </defs>

  <g stroke="#fff" stroke-width="1.3" fill="none" stroke-linecap="round" marker-end="url(#arrow)">
    <!-- Diagram i -->
    <path d="M 55,35 Q 90,45 129,91" />
    <path d="M 55,75 Q 85,85 129,127" />
    <path d="M 55,115 L 129,24" />

    <!-- Diagram ii -->
    <path d="M 235,22 Q 280,35 309,73" />
    <path d="M 235,58 Q 265,60 309,40" />
    <path d="M 235,94 Q 275,100 309,112" />
    <path d="M 235,130 Q 280,115 309,79" />

    <!-- Diagram iii -->
    <path d="M 415,22 Q 445,45 489,126" />
    <path d="M 415,58 L 489,24" />
    <path d="M 415,94 L 489,94" />
    <path d="M 415,130 Q 450,115 489,61" />

    <!-- Diagram iv -->
    <path d="M 55,202 L 129,236" />
    <path d="M 55,238 L 129,204" />
    <path d="M 55,274 L 129,240" />
    <path d="M 55,310 L 129,276" />

    <!-- Diagram v -->
    <path d="M 235,215 Q 270,215 309,236" />
    <path d="M 235,215 Q 265,245 309,306" />
    <path d="M 235,255 L 309,204" />
    <path d="M 235,295 Q 275,290 309,276" />
  </g>

  <!-- Nodes -->
  <g fill="#fff">
    <!-- i -->
    <circle cx="55" cy="35" r="2.5" />
    <circle cx="55" cy="75" r="2.5" />
    <circle cx="55" cy="115" r="2.5" />
    <circle cx="135" cy="22" r="2.5" />
    <circle cx="135" cy="58" r="2.5" />
    <circle cx="135" cy="94" r="2.5" />
    <circle cx="135" cy="130" r="2.5" />

    <!-- ii -->
    <circle cx="235" cy="22" r="2.5" />
    <circle cx="235" cy="58" r="2.5" />
    <circle cx="235" cy="94" r="2.5" />
    <circle cx="235" cy="130" r="2.5" />
    <circle cx="315" cy="38" r="2.5" />
    <circle cx="315" cy="76" r="2.5" />
    <circle cx="315" cy="114" r="2.5" />

    <!-- iii -->
    <circle cx="415" cy="22" r="2.5" />
    <circle cx="415" cy="58" r="2.5" />
    <circle cx="415" cy="94" r="2.5" />
    <circle cx="415" cy="130" r="2.5" />
    <circle cx="495" cy="22" r="2.5" />
    <circle cx="495" cy="58" r="2.5" />
    <circle cx="495" cy="94" r="2.5" />
    <circle cx="495" cy="130" r="2.5" />

    <!-- iv -->
    <circle cx="55" cy="202" r="2.5" />
    <circle cx="55" cy="238" r="2.5" />
    <circle cx="55" cy="274" r="2.5" />
    <circle cx="55" cy="310" r="2.5" />
    <circle cx="135" cy="202" r="2.5" />
    <circle cx="135" cy="238" r="2.5" />
    <circle cx="135" cy="274" r="2.5" />
    <circle cx="135" cy="310" r="2.5" />

    <!-- v -->
    <circle cx="235" cy="215" r="2.5" />
    <circle cx="235" cy="255" r="2.5" />
    <circle cx="235" cy="295" r="2.5" />
    <circle cx="315" cy="202" r="2.5" />
    <circle cx="315" cy="238" r="2.5" />
    <circle cx="315" cy="274" r="2.5" />
    <circle cx="315" cy="310" r="2.5" />
  </g>

  <!-- Labels -->
  <g fill="#fff" font-family="serif" font-size="13" dominant-baseline="central">
    <!-- Left Labels (Italic) -->
    <g font-style="italic" text-anchor="end">
      <!-- i -->
      <text x="45" y="35">a</text>
      <text x="45" y="75">b</text>
      <text x="45" y="115">c</text>

      <!-- ii -->
      <text x="225" y="22">a</text>
      <text x="225" y="58">b</text>
      <text x="225" y="94">c</text>
      <text x="225" y="130">d</text>

      <!-- iii -->
      <text x="405" y="22">a</text>
      <text x="405" y="58">b</text>
      <text x="405" y="94">c</text>
      <text x="405" y="130">d</text>

      <!-- iv -->
      <text x="45" y="202">a</text>
      <text x="45" y="238">b</text>
      <text x="45" y="274">c</text>
      <text x="45" y="310">d</text>

      <!-- v -->
      <text x="225" y="215">a</text>
      <text x="225" y="255">b</text>
      <text x="225" y="295">c</text>
    </g>

    <!-- Right Labels -->
    <g text-anchor="start">
      <!-- i -->
      <text x="145" y="22">1</text>
      <text x="145" y="58">2</text>
      <text x="145" y="94">3</text>
      <text x="145" y="130">4</text>

      <!-- ii -->
      <text x="325" y="38">1</text>
      <text x="325" y="76">2</text>
      <text x="325" y="114">3</text>

      <!-- iii -->
      <text x="505" y="22">1</text>
      <text x="505" y="58">2</text>
      <text x="505" y="94">3</text>
      <text x="505" y="130">4</text>

      <!-- iv -->
      <text x="145" y="202">1</text>
      <text x="145" y="238">2</text>
      <text x="145" y="274">3</text>
      <text x="145" y="310">4</text>

      <!-- v -->
      <text x="325" y="202">1</text>
      <text x="325" y="238">2</text>
      <text x="325" y="274">3</text>
      <text x="325" y="310">4</text>
    </g>

    <!-- Subfigure Roman Numerals -->
    <g font-size="14" font-weight="bold">
      <text x="25" y="150">i.</text>
      <text x="205" y="150">ii.</text>
      <text x="385" y="150">iii.</text>
      <text x="25" y="330">iv.</text>
      <text x="205" y="330">v.</text>
    </g>
  </g>
</svg>
   </div>

   c. Find the adjacency matrix of the given directed multigraph. [3]
<div style="max-width: 400px; margin: auto;">
   <svg xmlns="http://www.w3.org/2000/svg" viewBox="30 25 285 270" width="100%" height="100%">
  <!-- Edges -->
  <g stroke="#fff" stroke-width="1.5" fill="none" stroke-linecap="round">
    <!-- Loops -->
    <path d="M 98,77 C 88,38 48,40 46,62 C 44,82 72,96 95,84" />
    <path d="M 95,236 C 72,224 44,238 46,258 C 48,280 88,282 98,243" />

    <!-- Between a and b -->
    <path d="M 100,80 Q 180,52 260,80" />
    <path d="M 260,80 Q 180,108 100,80" />

    <!-- Between a and c -->
    <path d="M 100,80 Q 72,160 100,240" />
    <line x1="100" y1="240" x2="100" y2="80" />
    <path d="M 100,80 Q 128,160 100,240" />

    <!-- Diagonal a to d -->
    <line x1="100" y1="80" x2="260" y2="240" />

    <!-- Between b and d -->
    <path d="M 260,240 Q 212,160 260,80" />
    <path d="M 260,80 Q 242,160 260,240" />
    <path d="M 260,80 Q 278,160 260,240" />
    <path d="M 260,240 Q 308,160 260,80" />

    <!-- Between c and d -->
    <path d="M 260,240 Q 180,212 100,240" />
    <path d="M 260,240 Q 180,268 100,240" />
  </g>

  <!-- Arrowheads -->
  <g fill="#fff">
    <!-- Loop a -->
    <polygon points="94,84 85,83 89,90" />
    <!-- Loop c -->
    <polygon points="97,244 92,253 87,248" />

    <!-- a -> b and b -> a -->
    <polygon points="184,66 176,62 176,70" />
    <polygon points="176,94 184,90 184,98" />

    <!-- a -> c (left, right) and c -> a (middle) -->
    <polygon points="86,164 82,156 90,156" />
    <polygon points="100,156 96,164 104,164" />
    <polygon points="114,164 110,156 118,156" />

    <!-- Diagonal a -> d -->
    <polygon points="183.5,163.5 175,159.5 179.5,155" />

    <!-- b <-> d (outer up, inner down) -->
    <polygon points="239,131.5 234,138 242,137" />
    <polygon points="252,180 248,172 256,173" />
    <polygon points="268,180 264,173 272,172" />
    <polygon points="281,131.5 278,137 286,138" />

    <!-- d -> c (both upper and lower) -->
    <polygon points="176,226 184,222 184,230" />
    <polygon points="176,254 184,250 184,258" />
  </g>

  <!-- Nodes -->
  <g fill="#fff">
    <circle cx="100" cy="80" r="3.5" />
    <circle cx="260" cy="80" r="3.5" />
    <circle cx="100" cy="240" r="3.5" />
    <circle cx="260" cy="240" r="3.5" />
  </g>

  <!-- Labels -->
  <g fill="#fff" font-family="serif" font-style="italic" font-size="15">
    <text x="108" y="74">a</text>
    <text x="246" y="74">b</text>
    <text x="108" y="254">c</text>
    <text x="260" y="258" text-anchor="middle">d</text>
  </g>
</svg>
</div>
5. a. How many bit strings are there of length six or less, not counting the empty string? [2]
   b. How many bit strings of length ten both begin and end with a 1? [2]
   c. How many license plates consisting of three letters followed by three digits contain no letter or digit twice? [3]
   d. Use binomial theorem to determine the coefficient of x^7 in (1+x)^11 [2]
   e. A coin is flipped eight times: i. total outcomes? ii. exactly three heads? iii. at least three heads? [3]

6. a. Construct a precedence graph for the following program. [4]
		S1: x:=0
		S2: x:x+1
		S3: y:=2
		S4: z:=y
		S5: x:=x+2
		S6: y:=x+z
		S7: z:=4
	b. Suppose that a new company has five employees: Zaman, Ahmed, Siddique, Chowdhury, and Mahmud. Each employee will assume one of six responsibilities: planning, publicity, sales, marketing, development, and industry relations. Each employee is capable of doing one or more of these jobs: Zaman could do planning, sales, marketing, or industry relations; Ahmed could do planning or development; Siddique could do publicity, sales, or industry relations; Chowdhury could do planning, sales, or industry relations; and Mahmud could do planning, publicity, sales, or industry relations. **[8]**
		i. Model the capabilities of these employees using a partite graph.
		ii. Find an assignment of responsibilities such that each employee is assigned one responsibility.
		iii. Is the matching of responsibilities you found in part (b) a complete matching?
		iv. Is it a maximum matching?
7. a. i. How many edges does a full binary tree with 1000 internal vertices have? 
        ii. How many leaves does a full 3-ary tree with 100 vertices have? [6]
   b. Perform Preorder traversal of the following tree. [6]
 <svg xmlns="http://www.w3.org/2000/svg" viewBox="10 0 425 265" width="70%" height="70%">
  <!-- Edges -->
  <path d="
    M240,20 L120,75 M240,20 V75 M240,20 L360,75
    M120,75 L60,130 M120,75 V130 M120,75 L180,130
    M60,130 L25,185 M60,130 V185 M60,130 L95,185
    M180,130 V185 L155,240 M180,185 L205,240
    M360,75 L305,130 V185
    M360,75 V185
    M360,75 L415,130 V185" 
    stroke="#fff" stroke-width="1.5" stroke-linecap="round" fill="none" />

  <!-- Nodes -->
  <g fill="#fff">
    <circle cx="240" cy="20" r="2.5" />
    <circle cx="120" cy="75" r="2.5" />
    <circle cx="240" cy="75" r="2.5" />
    <circle cx="360" cy="75" r="2.5" />
    <circle cx="60" cy="130" r="2.5" />
    <circle cx="120" cy="130" r="2.5" />
    <circle cx="180" cy="130" r="2.5" />
    <circle cx="305" cy="130" r="2.5" />
    <circle cx="360" cy="130" r="2.5" />
    <circle cx="415" cy="130" r="2.5" />
    <circle cx="25" cy="185" r="2.5" />
    <circle cx="60" cy="185" r="2.5" />
    <circle cx="95" cy="185" r="2.5" />
    <circle cx="180" cy="185" r="2.5" />
    <circle cx="305" cy="185" r="2.5" />
    <circle cx="360" cy="185" r="2.5" />
    <circle cx="415" cy="185" r="2.5" />
    <circle cx="155" cy="240" r="2.5" />
    <circle cx="205" cy="240" r="2.5" />
  </g>

  <!-- Labels -->
  <g fill="#fff" font-family="serif" font-style="italic" font-size="13" text-anchor="middle">
    <text x="240" y="11">a</text>
    <text x="108" y="72">b</text>
    <text x="240" y="92">c</text>
    <text x="372" y="72">d</text>
    <text x="49" y="127">e</text>
    <text x="120" y="147">f</text>
    <text x="191" y="127">g</text>
    <text x="294" y="127">h</text>
    <text x="372" y="127">i</text>
    <text x="426" y="127">j</text>
    <text x="25" y="201">k</text>
    <text x="60" y="201">l</text>
    <text x="95" y="201">m</text>
    <text x="192" y="188" text-anchor="start">n</text>
    <text x="305" y="201">o</text>
    <text x="360" y="201">p</text>
    <text x="415" y="201">q</text>
    <text x="155" y="256">r</text>
    <text x="205" y="256">s</text>
  </g>
</svg>


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


