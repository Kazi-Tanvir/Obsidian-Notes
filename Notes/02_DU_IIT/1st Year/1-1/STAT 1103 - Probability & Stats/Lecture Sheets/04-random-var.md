# Random Variables and Expectation
**Mahbub Latif, PhD**  
May 2026

---

## 2. Plan
* Random variables (discrete and continuous)
* Cumulative distribution function (CDF)
* Probability mass function (PMF) and probability density function (PDF)
* Jointly distributed random variables
* Independent random variables and conditional distributions
* Expectation and variance
* Covariance and variance of sums
* Moment generating functions
* Markov's and Chebyshev's inequalities, and Weak Law of Large Numbers

---

## 3. Random variables
* Random variables are one of the fundamental building blocks of probability theory and statistical inference
* A random variable is formed by assigning a numerical value to each outcome in the sample space of a particular experiment
* A random variable can be thought of as being generated from a function that maps each outcome in a particular sample space onto the real number line $\mathbb{R}$

---

## 4. Random variables
* A random variable is obtained by assigning a numerical value to each outcome of a particular experiment.

---

## 5. Random variables
* Consider an experiment with two fair dice and corresponding sample space having 36 elements:
  $$S = \{(1, 1), (1, 2), \dots, (6, 5), (6, 6)\}$$
* A random variable can be defined as:
  $$X = \text{sum of faces of two fair dice}$$
* $X$ is a function of elements of the sample space, e.g.:
  $$X((1, 1)) = 2, \quad X((1, 3)) = 4, \quad \dots$$
* Possible values of $X$ are:
  $$X \in \{2, 3, \dots, 12\}$$

---

## 6. Probability distribution of $X$
*(Probability distribution of $X$, the sum of faces of two fair dice)*

| $x$ | $P(X = x)$ | Elements of $S$ | Probability |
|:---:|:---:|:---|:---:|
| 2 | $P(X = 2)$ | $\{(1, 1)\}$ | $1/36$ |
| 3 | $P(X = 3)$ | $\{(1, 2), (2, 1)\}$ | $2/36$ |
| 4 | $P(X = 4)$ | $\{(1, 3), (2, 2), (3, 1)\}$ | $3/36$ |
| 5 | $P(X = 5)$ | $\{(1, 4), (2, 3), (3, 2), (4, 1)\}$ | $4/36$ |
| 6 | $P(X = 6)$ | $\{(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)\}$ | $5/36$ |
| 7 | $P(X = 7)$ | $\{(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)\}$ | $6/36$ |
| 8 | $P(X = 8)$ | $\{(2, 6), (3, 5), (4, 4), (5, 3), (6, 2)\}$ | $5/36$ |
| 9 | $P(X = 9)$ | $\{(3, 6), (4, 5), (5, 4), (6, 3)\}$ | $4/36$ |
| 10 | $P(X = 10)$ | $\{(4, 6), (5, 5), (6, 4)\}$ | $3/36$ |
| 11 | $P(X = 11)$ | $\{(5, 6), (6, 5)\}$ | $2/36$ |
| 12 | $P(X = 12)$ | $\{(6, 6)\}$ | $1/36$ |

$$1 = P(S) = P\left(\bigcup_{i=2}^{12} \{X = i\}\right) = \sum_{i=2}^{12} P(X = i)$$

---

## 7. Example 4.1b
* An individual purchases two electronic components, each of which may be either defective ($d$) or acceptable ($a$).
* The four possible outcomes and their probabilities:

| Outcome | Probability |
|:---:|:---:|
| $(d, d)$ | 0.09 |
| $(d, a)$ | 0.21 |
| $(a, d)$ | 0.21 |
| $(a, a)$ | 0.49 |

* We can define random variables:
  * $X \to$ the number of acceptable components obtained in the purchase:
    * $P(X = 0) = 0.09$
    * $P(X = 1) = 0.21 + 0.21 = 0.42$
    * $P(X = 2) = 0.49$
  * $Y \to$ indicator of at least one acceptable component:
    * $P(Y = 0) = 0.09$
    * $P(Y = 1) = 0.42 + 0.49 = 0.91$

---

## 8. Discrete and continuous random variables
* A **discrete random variable** can take a value from a set of possible finite (e.g. $x_1, \dots, x_n$) or countably infinite ($x_1, x_2, \dots$) values:
  * Number of females in a group of five
  * Number of Toyota cars in a parking lot
  * Number of HIV incidences in 2020 in a district
* A **continuous random variable** can take any value in an interval:
  * Lifetime of a mobile phone
  * Milk contents of a container

---

## 9. Cumulative distribution function
* The **cumulative distribution function** (CDF, or distribution function) of the random variable $X$ is defined for any real number $x$ as:
  $$F(x) = P(X \le x)$$
* $X \sim F \to F$ is the distribution function of $X$
* All probability questions about $X$ can be answered in terms of its distribution function

---

## 10. Probability mass function
* Probabilities for all possible values of a discrete random variable are defined by the **probability mass function** (PMF):
  $$p(a) = P(X = a)$$
  $$0 \le p(x) \le 1, \quad \forall x$$
  $$\sum_x p(x) = 1$$
* **(Example 4.2a)** Suppose a random variable $X$ takes values 1, 2, or 3, with $p(1) = 1/2$ and $p(2) = 1/3$. What is $p(3)$?
  $$p(3) = 1 - \left(\frac{1}{2} + \frac{1}{3}\right) = 1 - \frac{5}{6} = \frac{1}{6}$$

---

## 11. Cumulative distribution function (Discrete)
* Cumulative distribution function of a discrete random variable $X$:
  $$F(a) = P(X \le a) = \sum_{x \le a} p(x)$$
* For a discrete random variable, $F(x)$ is a step function and there is a jump of size $p(x_i)$ at $x_i$
* Probability mass function of $X$ can be obtained from its cumulative distribution function:
  $$p(a) = F(a) - F(a^-)$$

---

## 12. PMF and CDF of Example 4.2a

| $x$ | $p(x) = P(X = x)$ | $F(x) = P(X \le x)$ |
|:---:|:---:|:---:|
| 1 | $1/2$ | $1/2$ |
| 2 | $1/3$ | $5/6$ |
| 3 | $1/6$ | $1.0$ |

---

## 13. Probability density function
* **Probability density function** (PDF) is used to obtain probability of an event related to a continuous random variable
* A non-negative function $f(x)$ is said to be the probability density function if:
  $$1 = P(X \in (-\infty, \infty)) = \int_{-\infty}^\infty f(x)\,dx$$
* The probability that $X$ lies in $[a, b]$ is given by the area under $f(x)$:
  $$P(a \le X \le b) = \int_a^b f(x)\,dx \implies P(X = a) = 0$$

---

## 14. Probability density function and CDF
* For a continuous variable $X$, the cumulative distribution function is defined as:
  $$F(a) = P(X \le a) = \int_{-\infty}^a f(x)\,dx$$
* Probability of an event can be expressed in terms of the cumulative distribution function:
  $$P(a \le X \le b) = F(b) - F(a)$$

---

## 15. Probability density function
* Probability density function can be obtained from the cumulative distribution function:
  $$f(x) = \frac{dF(x)}{dx}$$

---

## 16. Continuous Example
* Let $X$ be a random variable with probability density function:
  $$f(x) = \begin{cases} e^{-x} & x \ge 0 \\ 0 & x < 0 \end{cases}$$
* Probability:
  $$P(1 < X < 2) = \int_1^2 e^{-x}\,dx = \left[ -e^{-x} \right]_1^2 = e^{-1} - e^{-2} \approx 0.233$$

---

## 17. Cumulative distribution function Example
* Cumulative distribution function:
  $$F(x) = \int_0^x e^{-y}\,dy = 1 - e^{-x}, \quad x \ge 0$$
* Density from CDF:
  $$f(x) = \frac{dF(x)}{dx} = e^{-x}$$
* Probability using CDF:
  $$P(1 < X < 2) = F(2) - F(1) = (1 - e^{-2}) - (1 - e^{-1}) = e^{-1} - e^{-2} \approx 0.233$$

---

## 18. Exercise
* If the density function of $X$ is:
  $$f(x) = \begin{cases} c e^{-2x} & 0 < x < \infty \\ 0 & x < 0 \end{cases}$$
* Find the value of $c$.
  $$\int_0^\infty c e^{-2x}\,dx = 1 \implies c \left[ -\frac{1}{2} e^{-2x} \right]_0^\infty = \frac{c}{2} = 1 \implies c = 2$$
* What is $P(X > 2)$?
  $$P(X > 2) = \int_2^\infty 2 e^{-2x}\,dx = \left[ -e^{-2x} \right]_2^\infty = e^{-4} \approx 0.0183$$

---

## 19. Jointly Distributed Random Variables

---

## 20. Jointly distributed random variables
* Studying relationships between two or more variables can lead to interesting conclusions, e.g.:
  * In an experiment into the possible causes of cancer, we might be interested in the relationship between the average number of cigarettes smoked daily and the age at which an individual contracts cancer.
* **Cumulative joint probability distribution** of two random variables $X$ and $Y$:
  $$F(x, y) = P(X \le x, Y \le y)$$
* Marginal distribution functions $F_X(x)$ and $F_Y(y)$ can be derived from the joint distribution:
  $$F_X(x) = F(x, \infty), \quad F_Y(y) = F(\infty, y)$$

---

## 21. Joint probability mass function
* Let $X$ and $Y$ be discrete random variables taking values $x_1, x_2, \dots$ for $X$ and $y_1, y_2, \dots$ for $Y$
* The **joint probability mass function** of $X$ and $Y$:
  $$p(x_i, y_j) = P(X = x_i, Y = y_j)$$
* The **joint cumulative distribution function**:
  $$F(x_k, y_m) = P(X \le x_k, Y \le y_m) = \sum_{i=1}^k \sum_{j=1}^m P(X = x_i, Y = y_j)$$

---

## 22. Marginal PMF
* Individual (marginal) probability mass functions of $X$ and $Y$ can be obtained from the joint probability mass function:
  $$P(X = x_i) = \sum_j P(X = x_i, Y = y_j) = \sum_j p(x_i, y_j)$$
  $$P(Y = y_j) = \sum_i P(X = x_i, Y = y_j) = \sum_i p(x_i, y_j)$$
* Note:
  $$\{X = x_i\} = \bigcup_j \{X = x_i, Y = y_j\}$$

---

## 23. Example 4.3a
* Suppose that 3 batteries are randomly chosen from a group of 3 new, 4 used but still working, and 5 defective batteries.
* Let $X$ denote the number of new batteries chosen
* Let $Y$ denote the number of used but still working batteries chosen
* The joint probabilities:
  $$P(X = 0, Y = 0) = p(0, 0) = \frac{\binom{5}{3}}{\binom{12}{3}} = \frac{10}{220}$$

---

## 24. Example 4.3a (Joint PMF Table)

| $X \backslash Y$ | 0 | 1 | 2 | 3 | $P(X = x)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | $10/220$ | $40/220$ | $30/220$ | $4/220$ | $84/220$ |
| **1** | $30/220$ | $60/220$ | $18/220$ | 0 | $108/220$ |
| **2** | $15/220$ | $12/220$ | 0 | 0 | $27/220$ |
| **3** | $1/220$ | 0 | 0 | 0 | $1/220$ |
| **$P(Y = y)$** | $56/220$ | $112/220$ | $48/220$ | $4/220$ | 1.0 |

---

## 25. Joint probability density function
* Let $X$ and $Y$ be two continuous random variables; a function $f(x, y)$ is said to be a **joint probability density function** if:
  $$f(x, y) \ge 0, \quad \forall x, y$$
  $$\int_{-\infty}^\infty \int_{-\infty}^\infty f(x, y)\,dx\,dy = 1$$
* Probability of an event:
  $$P(a \le X \le b, c \le Y \le d) = \int_a^b \int_c^d f(x, y)\,dy\,dx$$

---

## 26. Joint probability density function
* The joint cumulative distribution function:
  $$F(a, b) = P(X \le a, Y \le b) = \int_{-\infty}^a \int_{-\infty}^b f(x, y)\,dy\,dx$$
* The joint PDF can be obtained by differentiating the joint CDF:
  $$f(a, b) = \frac{\partial^2 F(a, b)}{\partial a \partial b}$$

---

## 27. Marginal probability density function
* Probability density function of $X$ and $Y$ can be obtained from the joint probability density function:
  $$f_X(x) = \int_{-\infty}^\infty f(x, y)\,dy$$
  $$f_Y(y) = \int_{-\infty}^\infty f(x, y)\,dx$$

---

## 28. Example 4.3c
* The joint density function of $X$ and $Y$ is given by:
  $$f(x, y) = \begin{cases} 2e^{-x} e^{-2y} & 0 < x < \infty, \; 0 < y < \infty \\ 0 & \text{otherwise} \end{cases}$$
* Compute:
  * $P(X > 1, Y < 1) = \int_1^\infty e^{-x}\,dx \int_0^1 2e^{-2y}\,dy = e^{-1}(1 - e^{-2})$
  * $P(X < Y) = \int_0^\infty \int_0^y 2e^{-x} e^{-2y}\,dx\,dy = \frac{1}{3}$
  * $P(X < a) = \int_0^a e^{-x}\,dx = 1 - e^{-a}$

---

## 29. Independent random variables
* Two random variables $X$ and $Y$ are said to be **independent** if:
  $$P(X = x, Y = y) = P(X = x)P(Y = y)$$
  $$P(X \le x, Y \le y) = P(X \le x)P(Y \le y)$$
  $$F(x, y) = F_X(x)F_Y(y)$$
  $$p(x, y) = p_X(x)p_Y(y) \quad (\text{discrete})$$
  $$f(x, y) = f_X(x)f_Y(y) \quad (\text{continuous})$$

---

## 30. Conditional distributions (Discrete)
* If $X$ and $Y$ are two discrete random variables, the conditional probability mass function of $X$ given $Y = y$ is:
  $$p_{X|Y}(x|y) = P(X = x \mid Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)} = \frac{p(x, y)}{p_Y(y)}$$
* **(Example 4.3g)** Suppose the joint probability distribution of $X$ and $Y$ is given by:
  $$p(0, 0) = 0.4, \quad p(0, 1) = 0.2, \quad p(1, 0) = 0.1, \quad p(1, 1) = 0.3$$
* Calculate the conditional probability mass function of $X$ given that $Y = 1$:
  $$P(Y = 1) = 0.2 + 0.3 = 0.5$$
  $$P(X = 0 \mid Y = 1) = \frac{0.2}{0.5} = 0.4$$
  $$P(X = 1 \mid Y = 1) = \frac{0.3}{0.5} = 0.6$$

---

## 31. Conditional distributions (Continuous)
* Let $X$ and $Y$ be two continuous random variables; the conditional density of $X$ given $Y = y$ is:
  $$f_{X|Y}(x|y) = \frac{f(x, y)}{f_Y(y)}$$
* **(Example 4.3h)** The joint density of $X$ and $Y$ is given by:
  $$f(x, y) = \frac{12}{5}(2 - x - y), \quad 0 < x < 1, \; 0 < y < 1$$
* Calculate the conditional probability density function of $X$ given that $Y = y$:
  $$f_Y(y) = \int_0^1 \frac{12}{5}(2 - x - y)\,dx = \frac{12}{5}\left( \frac{3}{2} - y \right)$$
  $$f_{X|Y}(x|y) = \frac{2 - x - y}{\frac{3}{2} - y}, \quad 0 < x < 1$$

---

## 32. Expectation

---

## 33. Expectation
* Expectation of a random variable is one of the most important concepts in probability theory
* If $X$ is a discrete random variable taking on possible values $x_1, x_2, \dots$, then the **expected value** of $X$ is defined as:
  $$E(X) = \sum_i x_i P(X = x_i)$$
* The expected value of $X$ is a weighted average of the possible values that $X$ can take on, each value being weighted by the corresponding probability value
* **What is the expected value of a roll of a fair die?**
  $$E(X) = 1\left(\frac{1}{6}\right) + 2\left(\frac{1}{6}\right) + 3\left(\frac{1}{6}\right) + 4\left(\frac{1}{6}\right) + 5\left(\frac{1}{6}\right) + 6\left(\frac{1}{6}\right) = \frac{21}{6} = 3.5$$

---

## 34. Some observations on expectation
* The expected value of $X$ is not necessarily a value that $X$ could possibly assume (e.g. 3.5 for a die roll)
* Even though we call $E[X]$ the expectation of $X$, it should not be interpreted as the value that we expect $X$ to have, but rather as the average value of $X$ in a large number of repetitions of the experiment
* That is, if we continually roll a fair die, then after a large number of rolls the average of all the outcomes will be approximately $7/2 = 3.5$

---

## 35. Some observations on expectation
* $E[X]$ has the same units of measurement as does $X$
* **What is the expectation of an indicator random variable $I_A$**, which takes either 1 or 0 if $A$ occurs or not, respectively?
  $$E[I_A] = 1 \cdot P(A) + 0 \cdot P(A^c) = P(A)$$

---

## 36. Expectation (Continuous)
* Expectation of a continuous random variable $X$ is defined as:
  $$E(X) = \int_{-\infty}^\infty x f(x)\,dx$$
* **(Example 4.4d)** Suppose that you are expecting a message at some time past 5 P.M. From experience you know that $X$, the number of hours after 5 P.M. until the message arrives, has the PDF:
  $$f(x) = \begin{cases} \frac{1}{1.5} & 0 < x < 1.5 \\ 0 & \text{otherwise} \end{cases}$$
* $E(X)$:
  $$E(X) = \int_0^{1.5} x \left( \frac{1}{1.5} \right)\,dx = \frac{1}{1.5} \left[ \frac{x^2}{2} \right]_0^{1.5} = \frac{1.5}{2} = 0.75 \text{ hours (45 mins)}$$

---

## 37. Expectation of a function of a random variable
* If $X$ is a discrete random variable with PMF $p(x)$, then for any real-valued function $g$:
  $$E[g(X)] = \sum_x g(x) P(X = x) = \sum_x g(x) p(x)$$
* If $X$ is a continuous random variable with PDF $f(x)$, then for any real-valued function $g$:
  $$E[g(X)] = \int_{-\infty}^\infty g(x) f(x)\,dx$$

---

## 38. Example 4.5a
* Suppose $X$ has the following probability mass function:
  $$p(0) = 0.2, \quad p(1) = 0.5, \quad p(2) = 0.3$$
* Obtain $E(X^2)$:
  $$\begin{aligned}
  E(X^2) &= 0^2 P(X = 0) + 1^2 P(X = 1) + 2^2 P(X = 2) \\
  &= 0(0.2) + 1(0.5) + 4(0.3) \\
  &= 0 + 0.5 + 1.2 = 1.7
  \end{aligned}$$

---

## 39. Example 4.5d
* A continuous random variable $X$ has the following density function:
  $$f(x) = \begin{cases} 1 & 0 < x < 1 \\ 0 & \text{otherwise} \end{cases}$$
* Obtain $E(X^3)$:
  $$E(X^3) = \int_0^1 x^3 (1)\,dx = \left[ \frac{x^4}{4} \right]_0^1 = \frac{1}{4} = 0.25$$

---

## 40. Linearity of Expectation
* For two constants $a$ and $b$:
  $$E(aX + b) = aE(X) + b$$
* **Expected value of sums of random variables**:
  * For any two random variables $X$ and $Y$:
    $$E(X + Y) = E(X) + E(Y)$$
  * In general:
    $$E\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n E(X_i)$$

---

## 41. Example 4.5f
* A secretary has typed $N$ letters along with their respective envelopes.
* The envelopes get mixed up when they fall on the floor.
* If the letters are placed in the mixed-up envelopes in a completely random manner (that is, each letter is equally likely to end up in any of the envelopes), what is the expected number of letters that are placed in the correct envelopes?

---

## 42. Example 4.5f
* Let $X$ denote the number of letters that are placed in the correct envelope:
  $$X = X_1 + \dots + X_N$$
  where
  $$X_i = \begin{cases} 1 & \text{if the } i\text{-th letter is placed in its proper envelope} \\ 0 & \text{otherwise} \end{cases}$$
* Since the $i$-th letter is equally likely to be put in any of the $N$ envelopes:
  $$P(X_i = 1) = \frac{1}{N} \implies E(X_i) = \frac{1}{N}$$
* Therefore:
  $$E(X) = \sum_{i=1}^N E(X_i) = N \times \left(\frac{1}{N}\right) = 1$$

---

## 43. Variance
* If $X$ is a random variable with mean $\mu$ (i.e. $E(X) = \mu$), then the **variance** of $X$ is defined by:
  $$\mathrm{Var}(X) = E[(X - \mu)^2]$$
* It can be shown that:
  $$\mathrm{Var}(X) = E[X^2] - \mu^2$$
* For constants $a$ and $b$:
  $$\mathrm{Var}(aX + b) = a^2 \mathrm{Var}(X)$$

---

## 44. Example 4.6a & 4.6b
* **Example 4.6a**: Compute $\mathrm{Var}(X)$ when $X$ represents the outcome when we roll a fair die:
  $$\mu = E[X] = \frac{7}{2}$$
  $$E[X^2] = \frac{1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2}{6} = \frac{91}{6}$$
  $$\mathrm{Var}(X) = \frac{91}{6} - \left(\frac{7}{2}\right)^2 = \frac{91}{6} - \frac{49}{4} = \frac{35}{12} \approx 2.917$$
* **Example 4.6b (Variance of an Indicator RV)**:
  $$I = \begin{cases} 1 & \text{if } A \text{ occurs} \\ 0 & \text{if } A \text{ does not occur} \end{cases}$$
  $$E[I] = P(A) = p, \quad E[I^2] = 1^2(p) = p$$
  $$\mathrm{Var}(I) = E[I^2] - (E[I])^2 = p - p^2 = p(1 - p)$$

---

## 45. Covariance and Variance of Sums of Random Variables

---

## 46. Covariance
* The **covariance** of two random variables $X$ and $Y$ is defined by:
  $$\begin{aligned}
  \mathrm{Cov}(X, Y) &= E[(X - \mu_X)(Y - \mu_Y)] \\
  &= E[XY] - \mu_X \mu_Y \\
  &= E[XY] - E[X]E[Y]
  \end{aligned}$$
* Properties:
  $$\mathrm{Cov}(X, X) = \mathrm{Var}(X)$$
  $$\mathrm{Cov}(aX, Y) = a\mathrm{Cov}(X, Y)$$
  $$\mathrm{Cov}(X + Z, Y) = \mathrm{Cov}(X, Y) + \mathrm{Cov}(Z, Y)$$

---

## 47. Covariance and variance of sums
* If $X$ and $Y$ are independent, then:
  $$E[XY] = E[X]E[Y] \implies \mathrm{Cov}(X, Y) = 0$$
* Variance of sum of two random variables:
  $$\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2\mathrm{Cov}(X, Y)$$
* If $X$ and $Y$ are independent:
  $$\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y)$$

---

## 48. Moment generating function
* The **moment generating function** (MGF) $M(t)$ of the random variable $X$ is defined for all values $t$ by:
  $$M(t) = E[e^{tX}] = \begin{cases} \sum_x e^{tx} P(X = x) & \text{if } X \text{ is discrete} \\ \int_{-\infty}^\infty e^{tx} f(x)\,dx & \text{if } X \text{ is continuous} \end{cases}$$
* The MGF can be used to obtain moments: $E(X), E(X^2), \dots$

---

## 49. Moment generating function properties
* It can be shown that:
  $$M'(t) = \frac{d}{dt} M(t) = E[X e^{tX}]$$
* Setting $t = 0$:
  $$M'(0) = E[X e^0] = E(X)$$
* Similarly, for the second derivative:
  $$M''(0) = E(X^2)$$
* In general:
  $$M^{(n)}(0) = E(X^n)$$

---

## 50. Moment generating function of sums
* If $X$ and $Y$ are independent variables, then the moment generating function of $X + Y$ can be expressed as the product of the moment generating functions of $X$ and $Y$:
  $$M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX} e^{tY}] = E[e^{tX}] E[e^{tY}] = M_X(t) M_Y(t)$$

---

## 51. Chebyshev's Inequality and the Weak Law of Large Numbers

---

## 52. Markov's Inequality
* If $X$ is a random variable that takes only nonnegative values, then for any value $a > 0$:
  $$P(X \ge a) \le \frac{E(X)}{a}$$
* **Proof:**
  $$E(X) = \int_0^\infty x f(x)\,dx \ge \int_a^\infty x f(x)\,dx \ge \int_a^\infty a f(x)\,dx = a P(X \ge a)$$
  $$\implies P(X \ge a) \le \frac{E(X)}{a}$$

---

## 53. Chebyshev's Inequality
* If $X$ is a random variable with mean $\mu$ and variance $\sigma^2$, then for any $k > 0$:
  $$P(|X - \mu| \ge k) \le \frac{\sigma^2}{k^2}$$
* Setting $k = k\sigma$:
  $$P(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}$$
* **Significance**: Enables deriving bounds on probabilities when only the mean and variance are known

---

## 54. Example 4.9a
* Suppose that it is known that the number of items produced in a factory during a week is a random variable with mean 50.
* **(a)** What can be said about the probability that this week's production will exceed 75?
  * Using Markov's inequality:
    $$P(X > 75) \le P(X \ge 75) \le \frac{E(X)}{75} = \frac{50}{75} = \frac{2}{3}$$
* **(b)** If the variance of a week's production is known to equal 25, what can be said about the probability that this week's production will be between 40 and 60?
  * Using Chebyshev's inequality:
    $$P(40 < X < 60) = P(|X - 50| < 10) = 1 - P(|X - 50| \ge 10) \ge 1 - \frac{25}{10^2} = 1 - \frac{25}{100} = 0.75$$

---

## 55. The weak law of large numbers
* Let $X_1, X_2, \dots, X_n$ be a sequence of independent and identically distributed (i.i.d.) random variables, each having mean $\mu$ and variance $\sigma^2$.
* Then, for any $\epsilon > 0$:
  $$P\left(\left| \frac{X_1 + X_2 + \dots + X_n}{n} - \mu \right| > \epsilon\right) = P(|\bar{X} - \mu| > \epsilon) \to 0 \quad \text{as } n \to \infty$$
* **Proof (using Chebyshev's inequality)**:
  $$E[\bar{X}] = \mu, \quad \mathrm{Var}(\bar{X}) = \frac{\sigma^2}{n}$$
  $$P(|\bar{X} - \mu| > \epsilon) \le \frac{\sigma^2}{n\epsilon^2} \to 0 \quad \text{as } n \to \infty$$

---

## 56. Problems

---

## 57. Problem 2 & 3
* **(Problem 2)** Let $X$ represent the difference between the number of heads and the number of tails obtained when a coin is tossed $n$ times. What are the possible values of $X$?
  * If $k$ heads are obtained, then $(n - k)$ tails are obtained:
    $$X = k - (n - k) = 2k - n, \quad k \in \{0, 1, \dots, n\}$$
  * Possible values: $\{-n, -n+2, -n+4, \dots, n\}$
* **(Problem 3)** In Problem 2, if the coin is assumed fair and $n = 3$, what are the probabilities associated with the values that $X$ can take on?
  * For $n=3$, possible values of $X$ are $-3, -1, 1, 3$:
    * $P(X = -3) = \binom{3}{0}(1/2)^3 = 1/8$
    * $P(X = -1) = \binom{3}{1}(1/2)^3 = 3/8$
    * $P(X = 1) = \binom{3}{2}(1/2)^3 = 3/8$
    * $P(X = 3) = \binom{3}{3}(1/2)^3 = 1/8$

---

## 58. Recommended Problems
* Chapter 4 Problems:
  **4, 6, 7, 8, 10, 11, 12, 13, 25, 27, 28, 29, 31, 32, 33, 34, 36, 39, 40, 45, 54, 58**
