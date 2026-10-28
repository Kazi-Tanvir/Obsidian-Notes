# Elements of Probability
**Mahbub Latif, PhD**  
April 2026

---

## 2. Plan
* Sample space and events
* Venn diagrams and algebra of events
* Axioms of probability
* Counting principles, permutations, and combinations
* Conditional probability and Bayes' formula
* Independent events

---

## 3. Introduction
* The concept of the probability of a particular event of an experiment is subject to various meanings or interpretations
* There are three broad ways of interpreting probability:
  * **Frequentist or empirical**
  * **Subjective**
  * **Mathematical or axiomatic**

---

## 4. Introduction
* There could be one of the two meanings of a geologist's quote: *"There is a 60 percent chance of oil in a certain region"*
* **Frequency interpretation of probability**: The geologist feels that, over a long run, in 60 percent of the regions whose environmental conditions are very similar to the region under consideration, there will be oil
* **Subjective interpretation of probability**: The geologist believes that it is more likely that the region will contain oil than it will not

---

## 5. Introduction
* In **frequency interpretation**, the probability of a given outcome of an experiment is considered as being a "property" of that outcome
* In the **subjective interpretation**, the probability of an outcome is not thought of as being a property of the outcome but rather is considered a statement about the beliefs of the person who is quoting the probability, concerning the chance that the outcome will occur
* Mathematics of probability are the same for both interpretations

---

## 6. Sample Space and Events
* **Experiment**: A procedure whose outcome is not predictable with certainty in advance
* The set of all possible outcomes of an experiment is known as the **sample space** of the experiment and is denoted by $S$
* If the outcome of an experiment consists in the determination of the sex of a newborn child, then:
  $$S = \{\text{girl}, \text{boy}\} = \{g, b\}$$
* The outcome $g$ means that the child is a girl and $b$ that it is a boy

---

## 7. Sample Space and Events
* If the experiment consists of the running of a race among seven horses having post positions $\{1, 2, 3, 4, 5, 6, 7\}$:
  $$S = \{\text{all orderings of } (1, 2, 3, 4, 5, 6, 7)\}$$
* E.g., the outcome $(2, 3, 1, 6, 5, 4, 7) \to$ horse 2 is first, horse 3 is second, horse 1 is third, and so on.

---

## 8. Sample Space and Events
* Suppose we are interested in determining the amount of dosage that must be given to a patient until that patient reacts positively
* One possible sample space for this experiment is:
  $$S = \{x : 0 < x < \infty\}$$
* The outcome (dosage) $x$ can take any value between $0$ to $\infty$ (theoretically!)

---

## 9. Sample Space and Events
* Any subset $E$ of the sample space is known as an **event**, i.e., an event is a set consisting of possible outcomes of the experiment
* If the outcome of the experiment is contained in $E$, then we say that $E$ has occurred
* For $S = \{g, b\}$, the event that the child is a girl is $E = \{g\}$
* For $S = \{\text{all orderings of } (1, 2, 3, 4, 5, 6, 7)\}$, the event $E$ could be that horse 3 wins the race:
  $$E = \{\text{all outcomes in } S \text{ starting with } 3\}$$

---

## 10. Sample Space and Events
* For any two events $E$ and $F$ of a sample space $S$:
  * The new event $E \cup F$ is called the **union** of the events $E$ and $F$, which consists of all outcomes that are either in $E$ or in $F$ or in both $E$ and $F$
* Let us define with the horse racing example:
  * $E = \{\text{all outcomes starting with } 6\}$
  * $F = \{\text{all outcomes having } 6 \text{ in the second position}\}$
  * $E \cup F$ is the event that horse 6 comes in either first or second

---

## 11. Sample Space and Events
* For any two events $E$ and $F$, the new event $EF$ or $E \cap F$ is called the **intersection** of $E$ and $F$, which consists of all outcomes that are in both $E$ and $F$
* $EF$ will occur only if both $E$ and $F$ occur
* For the example with required dosage:
  * $E = \{x : 0 < x < 5\}$ and $F = \{x : 2 < x < 5\}$
  * $EF = \{x : 2 < x < 5\}$

---

## 12. Sample Space and Events
* Consider two events from the horse racing example:
  * $E = \{\text{all outcomes ending with } 5\}$
  * $F = \{\text{all outcomes starting with } 5\}$
* The event $EF$ does not have any outcomes and hence cannot occur, i.e.:
  $$EF = \emptyset$$
  where the null set $\emptyset$ does not contain any outcome
* Two events $E$ and $F$ are said to be **mutually exclusive** (disjoint) if $EF = \emptyset$

---

## 13. Sample Space and Events
* For any event $E$, the event $E^c$ is called the **complement** of $E$ if $E^c$ consists of all outcomes in the sample space $S$ that are not in $E$
* That is, $E^c$ will occur if and only if $E$ does not occur, e.g., $S^c = \emptyset$, $E E^c = \emptyset$
* For the example of determination of the sex of a child:
  * If $E = \{g\}$, then $E^c = \{b\}$

---

## 14. Sample Space and Events
* For any two events $E$ and $F$, if all of the outcomes in $E$ are also in $F$, then we say that $E$ is **contained in** $F$ and write $E \subset F$
* If $E \subset F$ and $F \subset E$, then we can write $E = F$
* For the required dosage example:
  * $F = \{x : 0 < x < 10\}$ and $E = \{x : 2 < x < 8\}$
  * $E \subset F$

---

## 15. Sample Space and Events
* **Union of more than two events**:
  $$\bigcup_{i=1}^n E_i = E_1 \cup E_2 \cup \dots \cup E_n$$
  * Union indicates at least one of the events $E_i$ occurs
* **Intersection of more than two events**:
  $$\bigcap_{i=1}^n E_i = E_1 \cap E_2 \cap \dots \cap E_n$$
  * Intersection indicates all of $E_i$ occur

---

## 16. Venn Diagrams
*(Diagram: Venn diagrams depicting the sample space $S$, subset events $E$ and $F$, their union $E \cup F$, and intersection $E \cap F$)*

---

## 17. Venn Diagrams
*(Diagram: Venn diagrams depicting the complement $E^c$, subset inclusion $E \subset F$, and mutually exclusive events $E \cap F = \emptyset$)*

---

## 18. The Algebra of Events
* **Commutative law:**
  $$E \cup F = F \cup E$$
  $$EF = FE$$
* **Associative law:**
  $$(E \cup F) \cup G = E \cup (F \cup G)$$
  $$(EF)G = E(FG)$$

---

## 19. The Algebra of Events
* **Distributive law:**
  $$(E \cup F)G = EG \cup FG$$
  $$EF \cup G = (E \cup G)(F \cup G)$$
* **DeMorgan's law:**
  $$(E \cup F)^c = E^c F^c$$
  $$(EF)^c = E^c \cup F^c$$

---

## 20. Axioms of Probability
* If an experiment is continually repeated under the exact same conditions, then for any event $E$, the proportion of time that the outcome is contained in $E$ approaches some constant value as the number of repetitions increases
* For instance, if a coin is continually flipped, then the proportion of flips resulting in heads will approach some value as the number of flips increases
* This constant limiting frequency is what we often have in mind when we speak of the **probability** of an event

---

## 21. Axioms of Probability
* For each event $E$ of an experiment having a sample space $S$, there is a number, denoted by $P(E)$, that is in accord with the following three axioms:
  * **(Axiom I)** $0 \le P(E) \le 1$
  * **(Axiom II)** $P(S) = 1$
  * **(Axiom III)** For any sequence of mutually exclusive events $E_1, E_2, \dots$:
    $$P\left(\bigcup_{i=1}^\infty E_i\right) = \sum_{i=1}^\infty P(E_i)$$
    and for finite $n$:
    $$P\left(\bigcup_{i=1}^n E_i\right) = \sum_{i=1}^n P(E_i)$$

---

## 22. Axioms of Probability
* From Axiom II and Axiom III:
  $$1 = P(S) = P(E \cup E^c) = P(E) + P(E^c) \implies P(E) = 1 - P(E^c)$$
* For any two events $E$ and $F$:
  $$P(E \cup F) = P(E) + P(F) - P(EF)$$

---

## 23. Example 3.4a
* A total of 28 percent of American males smoke cigarettes, 7 percent smoke cigars, and 5 percent smoke both cigars and cigarettes.
* What percentage of males smoke neither cigars nor cigarettes?

* **Solution:**
  * Let $C$ = smoker of cigarettes, $G$ = smoker of cigars
  * Given: $P(C) = 0.28$, $P(G) = 0.07$, $P(CG) = 0.05$
  * Probability of smoking cigarettes or cigars:
    $$P(C \cup G) = P(C) + P(G) - P(CG) = 0.28 + 0.07 - 0.05 = 0.30$$
  * Probability of smoking neither:
    $$P((C \cup G)^c) = 1 - P(C \cup G) = 1 - 0.30 = 0.70 \quad (70\%)$$

---

## 24. Odds of an event
* **Odds of an event $A$** is defined as:
  $$O(A) = \frac{P(A)}{P(A^c)} = \frac{P(A)}{1 - P(A)} \implies P(A) = \frac{O(A)}{1 + O(A)}$$
* Thus the odds of an event $A$ tells how much more likely it is that $A$ occurs than that it does not occur
* For $P(A) = 2/3$, the odds of $A$ is 2 (i.e. $P(A)$ is two times that of $P(A^c)$)

---

## 25. Equally likely outcomes
* Suppose all the outcomes of an experiment with sample space $S = \{1, \dots, N\}$ are equally likely, i.e.:
  $$P(1) = P(2) = \dots = P(N) = p$$
  $$\sum_{i=1}^N P(i) = 1 \implies p = \frac{1}{N} = P(i), \quad \forall i$$
* For any event $E$:
  $$P(E) = \frac{\text{number of outcomes in } E}{N}$$

---

## 26. Basic principle of counting
* Suppose that two experiments are to be performed
* If experiment 1 can result in any one of $m$ possible outcomes and if, for each outcome of experiment 1, there are $n$ possible outcomes of experiment 2, then together there are $mn$ possible outcomes of the two experiments
* For example, there will be $6 \times 6 = 36$ possible outcomes for an experiment with tossing 2 dice

---

## 27. Example 3.5a
* Two balls are "randomly drawn" from a bowl containing 6 white and 5 black balls.
* What is the probability that one of the drawn balls is white and the other black?

* **Solution:**
  * Total number of ways to draw 2 balls from 11:
    $$\binom{11}{2} = \frac{11 \times 10}{2} = 55$$
  * Number of ways to choose 1 white and 1 black:
    $$\binom{6}{1}\binom{5}{1} = 6 \times 5 = 30$$
  * Probability:
    $$P = \frac{30}{55} = \frac{6}{11} \approx 0.5455$$

---

## 28. Generalized basic principle of counting
* If $r$ experiments that are to be performed are such that:
  * the first one may result in any of $n_1$ possible outcomes,
  * and if for each of these $n_1$ possible outcomes there are $n_2$ possible outcomes of the second experiment,
  * and if for each of the possible outcomes of the first two experiments there are $n_3$ possible outcomes of the third experiment, and so on...
* then there are a total of $n_1 \times n_2 \times \dots \times n_r$ possible outcomes of the $r$ experiments

---

## 29. Permutations
* The number of ways $n$ distinct objects can be arranged in a linear order is:
  $$n! = n(n-1)(n-2)\dots 3 \cdot 2 \cdot 1$$
* Each of these ordered arrangements is known as a **permutation**
* E.g., how many different ordered arrangements of the letters $a, b, c$ are possible?

---

## 30. Permutations
* How many different ordered arrangements of the letters $a, b, c$ are possible?
  $$abc, \; acb, \; bac, \; bca, \; cab, \; cba$$
* There are $3! = 3 \times 2 \times 1 = 6$ possible permutations of three distinct objects

---

## 31. Example 3.5b
* Mr. Jones has 10 books that he is going to put on his bookshelf.
* Of these, 4 are mathematics books, 3 are chemistry books, 2 are history books, and 1 is a language book.
* Jones wants to arrange his books so that all the books dealing with the same subject are together on the shelf.
* How many different arrangements are possible?

* **Solution:**
  * Number of subject categories = 4 (which can be ordered in $4!$ ways)
  * Within math: $4!$, within chemistry: $3!$, within history: $2!$, within language: $1!$
  * Total arrangements:
    $$4! \times (4! \times 3! \times 2! \times 1!) = 24 \times (24 \times 6 \times 2 \times 1) = 6{,}912$$

---

## 32. Combinations
* Determine the number of different groups of $r$ objects that could be formed from a total of $n$ objects
* E.g., how many different groups of three can be selected from five letters $A, B, C, D, E$?
  * There are $5 \cdot 4 \cdot 3 = 60$ ordered groups of three
  * Every group of three is counted $3! = 6$ times (e.g. $ABC, ACB, BAC, BCA, CAB, CBA$)
  * Total number of different groups that can be formed is:
    $$\frac{60}{6} = 10$$

---

## 33. Combinations
* In general, $n(n-1)(n-2)\dots(n-r+1)$ represents the number of different ways that a group of $r$ items could be selected from $n$ items when the order of selection is relevant
* Each group of $r$ items will be counted $r!$ times in this count
* The number of different groups of $r$ items that could be formed from a set of $n$ items is:
  $$\binom{n}{r} = \frac{n(n-1)(n-2)\dots(n-r+1)}{r!} = \frac{n!}{r!(n-r)!}$$
* $\binom{n}{r} \to$ the number of combinations of $n$ objects taken $r$ at a time

---

## 34. Example 3.5d
* A committee of size 5 is to be selected from a group of 6 men and 9 women.
* If the selection is made randomly, what is the probability that the committee consists of 3 men and 2 women?

* **Solution:**
  $$P(\text{3 men and 2 women}) = \frac{\binom{6}{3} \binom{9}{2}}{\binom{15}{5}} = \frac{20 \times 36}{3003} = \frac{720}{3003} \approx 0.2398$$

---

## 35. Example 3.5f
* A basketball team consists of 6 black and 6 white players.
* The players are to be paired in groups of two for the purpose of determining roommates.
* If the pairings are done at random, what is the probability that none of the black players will have a white roommate?

---

## 36. Example 3.5f
* The first pair can be selected from the 12 players in $\binom{12}{2}$ ways
* The second pair can be selected from the remaining 10 players in $\binom{10}{2}$ ways
* The third pair in $\binom{8}{2}$ ways, and so on, until the sixth pair in $\binom{2}{2}$ ways

---

## 37. Example 3.5f
* The number of ways 12 players can be divided into 6 ordered pairs:
  $$\binom{12}{2}\binom{10}{2}\binom{8}{2}\binom{6}{2}\binom{4}{2}\binom{2}{2} = \frac{12!}{(2!)^6}$$
* The number of ways 12 players can be divided into 6 unordered pairs:
  $$\frac{12!}{(2!)^6 6!} = \frac{12!}{2^6 6!}$$

---

## 38. Example 3.5f
* Number of ways to pair only the 6 white players among themselves: $\frac{6!}{2^3 3!}$
* Same for the 6 black players among themselves: $\frac{6!}{2^3 3!}$
* The desired probability:
  $$\frac{\left[ \frac{6!}{2^3 3!} \right] \left[ \frac{6!}{2^3 3!} \right]}{\frac{12!}{2^6 6!}} = \frac{\left[ \frac{6!}{2^3 3!} \right]^2}{\frac{12!}{2^6 6!}} = \frac{5}{231} \approx 0.0216$$

---

## 39. Conditional probability
* Conditional probability is an important concept of probability theory
* It is useful to calculate probability when some partial information about the result of the experiment is available
* It is useful to recalculate the probability when some additional information is available
* Sometimes it is easier to calculate conditional probability

---

## 40. Conditional probability
* Consider an experiment with rolling two fair dice; the sample space has 36 elements:
  $$S = \{(i, j) : i = 1, \dots, 6, \; j = 1, \dots, 6\}$$
* Since outcomes are equally likely, each outcome has the probability of $1/36$ to occur
* The probability that the sum of two dice equals 8 is $5/36$
* What is the probability that the sum of two dice equals 8 provided the first die lands on 3?

---

## 41. Conditional probability
* Let $E$ be the event that the sum of two dice is 8, and $F$ denote the event that the first die lands on 3
* We want to calculate the probability of $E$ given $F$, which is notationally denoted as $P(E|F)$, known as **conditional probability**
* The conditional probability of $E$ given $F$ is defined as:
  $$P(E|F) = \frac{P(EF)}{P(F)}, \quad \text{provided } P(F) > 0$$
* The probabilities $P(EF)$ and $P(F)$ are unconditional probabilities and can be calculated using the sample space

---

## 42. Conditional probability
* What is the probability that the sum of two dice equals 8 provided the first die lands on 3?
* Let $E = \{\text{sum is 8}\} = \{(2,6), (3,5), (4,4), (5,3), (6,2)\}$
* Let $F = \{\text{first die is 3}\} = \{(3,1), (3,2), (3,3), (3,4), (3,5), (3,6)\}$
* $EF = \{(3,5)\}$
* Using the definition:
  $$P(E|F) = \frac{P(EF)}{P(F)} = \frac{1/36}{6/36} = \frac{1}{6}$$
* Conditional probability can also be calculated using the "reduced sample space" $F$ (which contains 6 equally likely outcomes, exactly 1 of which is in $E$)

---

## 43. Example 3.6a
* A bin contains 5 defective (that immediately fail when put in use), 10 partially defective (that fail after a couple of hours of use), and 25 acceptable transistors.
* A transistor is chosen at random from the bin and put into use.
* If it does not immediately fail, what is the probability it is acceptable?

* **Solution:**
  * Total transistors = $5 + 10 + 25 = 40$
  * Non-immediately failing transistors = $10 + 25 = 35$
  * Probability:
    $$P(\text{acceptable} \mid \text{not immediately failing}) = \frac{25}{35} = \frac{5}{7} \approx 0.7143$$

---

## 44. Example 3.6c
* Ms. Perez figures that there is a 30 percent chance that her company will set up a branch office in Phoenix.
* If it does, she is 60 percent certain that she will be made manager of this new operation.
* What is the probability that Perez will be a Phoenix branch office manager?

* **Solution:**
  * Let $O$ = branch office set up in Phoenix ($P(O) = 0.30$)
  * Let $M$ = Perez becomes manager ($P(M|O) = 0.60$)
  * Desired probability:
    $$P(OM) = P(O)P(M|O) = (0.30)(0.60) = 0.18$$

---

## 45. Bayes' formula
* For two events $E$ and $F$, we can write:
  $$P(E|F) = \frac{P(EF)}{P(F)} \implies P(EF) = P(F)P(E|F)$$
* We can also write:
  $$E = EF \cup EF^c$$
* Since $EF$ and $EF^c$ are mutually exclusive:
  $$P(E) = P(EF) + P(EF^c)$$

---

## 46. Bayes' formula
* $P(E)$ can be expressed in terms of a weighted sum of conditional probabilities:
  $$\begin{aligned}
  P(E) &= P(EF) + P(EF^c) \\
  &= P(E|F)P(F) + P(E|F^c)P(F^c) \\
  &= P(E|F)P(F) + P(E|F^c)[1 - P(F)]
  \end{aligned}$$

---

## 47. Example 3.7a
* An insurance company believes that people can be divided into two classes:
  * Those that are accident prone
  * Those that are not
* Their statistics show that an accident-prone person will have an accident at some time within a fixed 1-year period with probability 0.4, whereas this probability decreases to 0.2 for a non-accident-prone person.
* If we assume that 30 percent of the population is accident prone, what is the probability that a new policy holder will have an accident within a year of purchasing a policy?

---

## 48. Example 3.7a
* Let $A_1 \to$ the policy holder will have an accident within a year of purchase
* Let $A \to$ the policy holder is accident prone
* Given: $P(A) = 0.3$, $P(A^c) = 0.7$, $P(A_1|A) = 0.4$, $P(A_1|A^c) = 0.2$
* By the law of total probability:
  $$\begin{aligned}
  P(A_1) &= P(A_1|A)P(A) + P(A_1|A^c)P(A^c) \\
  &= (0.4)(0.3) + (0.2)(0.7) = 0.12 + 0.14 = 0.26
  \end{aligned}$$

---

## 49. Example 3.7a
* Suppose that a new policy holder has an accident within a year of purchasing his policy.
* What is the probability that he is accident prone?
  $$P(A|A_1) = {?}$$

---

## 50. Bayes' formula
* What is the probability that he is accident prone?
  $$\begin{aligned}
  P(A|A_1) &= \frac{P(A A_1)}{P(A_1)} \\
  &= \frac{P(A_1|A)P(A)}{P(A_1)} \\
  &= \frac{(0.4)(0.3)}{0.26} = \frac{0.12}{0.26} \approx 0.4615
  \end{aligned}$$

---

## 51. Bayes' formula
* Let $F_1, F_2, \dots, F_n$ be mutually exclusive events such that $\bigcup_{i=1}^n F_i = S$ (a partition of $S$)
* Define an event $E$ in terms of $F_i$'s as $E = \bigcup_{i=1}^n EF_i$
* We can write:
  $$P(E) = \sum_{i=1}^n P(EF_i) = \sum_{i=1}^n P(E|F_i)P(F_i)$$

---

## 52. Bayes' formula
* Given $E$, what is the probability that one of $F_i$ will occur?
* This formula is known as **Bayes' formula**:
  $$P(F_i|E) = \frac{P(F_i E)}{P(E)} = \frac{P(E|F_i)P(F_i)}{P(E)} = \frac{P(E|F_i)P(F_i)}{\sum_{j=1}^n P(E|F_j)P(F_j)}$$

---

## 53. Example 3.7f
* A plane is missing and it is presumed that it was equally likely to have gone down in any of three possible regions.
* Let $(1 - \alpha_i)$ denote the probability the plane will be found upon a search of the $i$-th region when the plane is, in fact, in that region ($i = 1, 2, 3$). ($\alpha_i$ is the overlook probability)
* What is the conditional probability that the plane is in the $i$-th region, given that a search of region 1 is unsuccessful?

---

## 54. Example 3.7f
* Let $R_i \to$ the event that the plane is in region $i$ ($P(R_i) = 1/3, \; i = 1, 2, 3$)
* Let $E \to$ the event that the search in region 1 is unsuccessful
* $P(E|R_1) = \alpha_1$, $P(E|R_2) = 1$, $P(E|R_3) = 1$
* Total probability of $E$:
  $$P(E) = \sum_{i=1}^3 P(E|R_i)P(R_i) = \frac{\alpha_1(1/3) + 1(1/3) + 1(1/3)}{1} = \frac{\alpha_1 + 2}{3}$$
* Posterior probabilities:
  $$P(R_1|E) = \frac{P(E|R_1)P(R_1)}{P(E)} = \frac{\alpha_1/3}{(\alpha_1 + 2)/3} = \frac{\alpha_1}{\alpha_1 + 2}$$
  $$P(R_2|E) = P(R_3|E) = \frac{1/3}{(\alpha_1 + 2)/3} = \frac{1}{\alpha_1 + 2}$$

---

## 55. Independent events
* Two events $E$ and $F$ are said to be **independent** if one of the following three equivalent conditions is true (otherwise they are dependent):
  $$P(EF) = P(E)P(F)$$
  $$P(E|F) = P(E)$$
  $$P(F|E) = P(F)$$

---

## 56. Example 3.8a
* A card is selected at random from an ordinary deck of 52 playing cards.
* If $A$ is the event that the selected card is an ace and $H$ is the event that it is a heart, then show $A$ and $H$ are independent.

* **Proof:**
  * $P(A) = \frac{4}{52} = \frac{1}{13}$
  * $P(H) = \frac{13}{52} = \frac{1}{4}$
  * $AH$ is the event that the card is the ace of hearts:
    $$P(AH) = \frac{1}{52}$$
  * Since $P(AH) = \frac{1}{52} = \left(\frac{1}{13}\right)\left(\frac{1}{4}\right) = P(A)P(H)$, $A$ and $H$ are independent.

---

## 57. Problems
* **(Problem 1)** A box contains three marbles — one red, one green, and one blue. Consider an experiment that consists of taking one marble from the box, then replacing it in the box and drawing a second marble from the box. Describe the sample space.
  * Repeat for the case in which the second marble is drawn without first replacing the first marble.

---

## 58. Problems
* **(Problem 5)** A system is composed of four components, each of which is either working or failed. Consider an experiment that consists of observing the status of each component, and let the outcome of the experiment be given by the vector $(x_1, x_2, x_3, x_4)$, where $x_i = 1$ if component $i$ is working and $x_i = 0$ if component $i$ is failed.
  * How many outcomes are in the sample space of this experiment?
  * Let $E$ be the event that components 1 and 3 are both failed. How many outcomes are contained in event $E$?

---

## 59. Problems
* **(Problem 29)** You ask your neighbor to water a sickly plant while you were on a vacation. Without water it will die with probability 0.8 and with water it will die with probability 0.15. You are 90 percent certain that your neighbor will remember to water the plant.
  * What is the probability that the plant will be alive when you return?
  * If it is dead, what is the probability your neighbor forgot to water it?

---

## 60. Law of Total Probability Summary
$$E = (EF) \cup (EF^c) \implies P(E) = P(EF) + P(EF^c) = P(E|F)P(F) + P(E|F^c)P(F^c)$$

---

## 61. Monty Hall Problem
* Suppose you're on a game show, and you're given the choice of three doors:
  * Behind one door is a car; behind the others, goats.
* You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
* He then says to you, "Do you want to pick door No. 2?"
* **Question**: Is it to your advantage to switch your choice?
  * **Answer**: Yes! Switching gives a $2/3$ probability of winning the car, while staying gives only $1/3$.
