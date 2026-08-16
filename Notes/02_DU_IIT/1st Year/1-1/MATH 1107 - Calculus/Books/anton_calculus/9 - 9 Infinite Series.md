# CHAPTER 9: INFINITE SERIES

> Perspective creates the illusion that the sequence of railroad ties continues indefinitely but converges toward a single point infinitely far away.

In this chapter we will be concerned with infinite series, which are sums that involve infinitely many terms. Infinite series play a fundamental role in both mathematics and science—they are used, for example, to approximate trigonometric functions and logarithms, to solve differential equations, to evaluate difficult integrals, to create new functions, and to construct mathematical models of physical laws.

---

## 9.1 SEQUENCES

### DEFINITION OF A SEQUENCE
* **Informal Definition:** An unending succession of numbers (terms) written as $a_1, a_2, a_3, \dots, a_n, \dots$ or $\{a_n\}_{n=1}^{+\infty}$.
* **Formal Definition (9.1.1):** A sequence is a function whose domain is a set of integers (usually positive or nonnegative integers).

### LIMIT OF A SEQUENCE

> **9.1.2 DEFINITION**
> A sequence $\{a_n\}$ converges to the limit $L$ (written $\lim_{n \to +\infty} a_n = L$) if for every $\epsilon > 0$, there is a positive integer $N$ such that $|a_n - L| < \epsilon$ for all $n \ge N$.
> If no such finite limit exists, the sequence diverges.

#### Key Properties and Theorems
* **Theorem 9.1.3 (Limit Laws):** Standard algebraic limit laws (sum, difference, product, quotient, scalar multiple) apply to sequence limits.
* If $f(x) \to L$ as $x \to +\infty$, then $f(n) \to L$ as $n \to +\infty$.
* **Theorem 9.1.4:** A sequence converges to $L \iff$ both its even-numbered and odd-numbered subsequences converge to $L$.
* **Theorem 9.1.5 (Squeezing Theorem for Sequences):** If $a_n \le b_n \le c_n$ for all $n \ge N$, and $\lim a_n = \lim c_n = L$, then $\lim b_n = L$.
* **Theorem 9.1.6:** If $\lim_{n \to +\infty} |a_n| = 0$, then $\lim_{n \to +\infty} a_n = 0$.
* Important Limits:
  $$\lim_{n \to +\infty} \sqrt[n]{n} = 1, \quad \lim_{n \to +\infty} \frac{x^n}{n!} = 0 \quad (\text{for all } x)$$

---

### RECURSIVELY DEFINED SEQUENCES
* **Newton's / Mechanic's Rule for $\sqrt{a}$:** $x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right) \implies \lim_{n \to \infty} x_n = \sqrt{a}$.

---

### QUICK CHECK EXERCISES 9.1
*(See page 607 for answers.)*
1. Sequence $4, 6, 8, 10, 12, \dots$: (a) $a_1=4, a_4=10, a_7=16, a_n = 2n+2$; (b) $b_0=4, b_4=12, b_8=20, b_n = 2n+4$.
2. $\lim_{n \to +\infty} a_n$ exists.
3. If $a_n \to 2$ and $b_n = (-1)^n$: (a) $\{b_n\}$ diverges (b) $\{3a_n - 1\} \to 5$ (c) $\{b_n^2\} \to 1$ (d) $\{a_n + b_n\}$ diverges (e) $\left\{\frac{1}{a_n^2 + 3}\right\} \to \frac{1}{7}$ (f) $\left\{\frac{b_n}{1000}\right\}$ diverges.
4. Squeezing Theorem; 12.

---

## 9.2 MONOTONE SEQUENCES

### DEFINITIONS & TESTS (9.2.1)
* **Strictly Increasing:** $a_1 < a_2 < a_3 < \dots$ ($a_{n+1} - a_n > 0$ or $a_{n+1}/a_n > 1$ or $f'(x) > 0$)
* **Increasing:** $a_1 \le a_2 \le a_3 \le \dots$ ($a_{n+1} - a_n \ge 0$ or $a_{n+1}/a_n \ge 1$ or $f'(x) \ge 0$)
* **Strictly Decreasing:** $a_1 > a_2 > a_3 > \dots$ ($a_{n+1} - a_n < 0$ or $a_{n+1}/a_n < 1$ or $f'(x) < 0$)
* **Decreasing:** $a_1 \ge a_2 \ge a_3 \ge \dots$ ($a_{n+1} - a_n \le 0$ or $a_{n+1}/a_n \le 1$ or $f'(x) \le 0$)
* **Monotone:** Either increasing or decreasing.

### CONVERGENCE OF MONOTONE SEQUENCES

> **9.2.3 THEOREM (Increasing Sequences)**
> If $\{a_n\}$ is eventually increasing:
> (a) If bounded above by $M$, it converges to $L \le M$.
> (b) If unbounded above, $\lim_{n \to +\infty} a_n = +\infty$.

> **9.2.4 THEOREM (Decreasing Sequences)**
> If $\{a_n\}$ is eventually decreasing:
> (a) If bounded below by $M$, it converges to $L \ge M$.
> (b) If unbounded below, $\lim_{n \to +\infty} a_n = -\infty$.

> **9.2.5 AXIOM (The Completeness Axiom)**
> Every nonempty set of real numbers bounded above has a least upper bound (supremum), and every nonempty set bounded below has a greatest lower bound (infimum).

---

### QUICK CHECK EXERCISES 9.2
*(See page 614 for answers.)*
1. $\{2^n\}$: I; $\{2^{-n}\}$: D; $\left\{\frac{5-n}{n^2}\right\}$: N; $\left\{\frac{-1}{n^2}\right\}$: I; $\left\{\frac{(-1)^n}{n^2}\right\}$: N.
2. $\{n+(-1)^n\}$: N; $\{2n+(-1)^n\}$: M; $\{3n+(-1)^n\}$: S.
3. $1$; increasing.
4. $8$; eventually; increasing.

---

## 9.3 INFINITE SERIES

### SUM OF AN INFINITE SERIES
* **Infinite Series:** $\sum_{k=1}^\infty u_k = u_1 + u_2 + u_3 + \dots$
* **$n$th Partial Sum:** $s_n = \sum_{k=1}^n u_k = u_1 + u_2 + \dots + u_n$
* **Sum of the Series:** If $\lim_{n \to \infty} s_n = S$, the series converges and $\sum_{k=1}^\infty u_k = S$. If the limit does not exist, the series diverges.

---

### GEOMETRIC SERIES

> **9.3.3 THEOREM (Geometric Series)**
> $$\sum_{k=0}^\infty a r^k = a + ar + ar^2 + \dots + ar^k + \dots \quad (a \neq 0)$$
> * Converges if $|r| < 1$, with sum $S = \frac{a}{1 - r}$.
> * Diverges if $|r| \ge 1$.

---

### TELESCOPING & HARMONIC SERIES
* **Telescoping Series Example:**
  $$\sum_{k=1}^\infty \frac{1}{k(k+1)} = \lim_{n \to \infty} \left(1 - \frac{1}{n+1}\right) = 1$$
* **Harmonic Series:**
  $$\sum_{k=1}^\infty \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \dots \quad \text{Diverges (Proof by Nicole Oresme: } s_{2^n} > \frac{n+1}{2})$$

---

### QUICK CHECK EXERCISES 9.3
*(See page 623 for answers.)*
1. sequence; series.
2. For $\sum_{k=1}^\infty \frac{1}{2^k}$: $s_1 = 1/2, s_2 = 3/4, s_3 = 7/8, s_4 = 15/16, s_n = 1 - 1/2^n$.
3. Sequence of partial sums converges.
4. $ar^k (a \neq 0)$; $\frac{a}{1-r}$; $|r| < 1$; $|r| \ge 1$.
5. $\frac{1}{k}$; diverge.

---

## 9.4 CONVERGENCE TESTS

### THE DIVERGENCE TEST ($n$th-Term Test)

> **9.4.1 THEOREM (The Divergence Test)**
> * If $\lim_{k \to +\infty} u_k \neq 0$, then $\sum u_k$ diverges.
> * If $\lim_{k \to +\infty} u_k = 0$, the test is inconclusive (the series may converge or diverge).
>
> *(Note: Converse of $\sum u_k \text{ converges} \implies \lim u_k = 0$ is false!)*

### THE INTEGRAL TEST

> **9.4.4 THEOREM (The Integral Test)**
> Let $\sum u_k$ be a series with positive terms. If $f$ is positive, continuous, and decreasing on $[a, +\infty)$ with $u_k = f(k)$ for $k \ge a$, then:
> $$\sum_{k=1}^\infty u_k \text{ and } \int_a^{+\infty} f(x)\,dx \quad \text{both converge or both diverge.}$$

### $p$-SERIES TEST

> **9.4.5 THEOREM ($p$-Series)**
> $$\sum_{k=1}^\infty \frac{1}{k^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \dots$$
> * Converges if $p > 1$
> * Diverges if $0 < p \le 1$

---

### QUICK CHECK EXERCISES 9.4
*(See page 631 for answers.)*
1. $\lim_{k \to +\infty} u_k \neq 0$.
2. $\sum_{k=2}^\infty a_k = -2$; $\sum_{k=1}^\infty (2a_k + b_k) = 7$.
3. integral; $\frac{1}{\sqrt{k}}$; diverges.
4. $\frac{1}{k^p}$; $p > 1$; $0 < p \le 1$.

---

## 9.5 THE COMPARISON, RATIO, AND ROOT TESTS

### COMPARISON TEST (9.5.1)
For series with nonnegative terms $a_k \le b_k$:
* If $\sum b_k$ converges, then $\sum a_k$ converges.
* If $\sum a_k$ diverges, then $\sum b_k$ diverges.

### LIMIT COMPARISON TEST (9.5.4)
For positive series $a_k, b_k$, let $\rho = \lim_{k \to +\infty} \frac{a_k}{b_k}$:
* If $0 < \rho < +\infty$, both converge or both diverge.
* If $\rho = 0$ and $\sum b_k$ converges, then $\sum a_k$ converges.
* If $\rho = +\infty$ and $\sum b_k$ diverges, then $\sum a_k$ diverges.

### RATIO TEST (9.5.5)
Let $\rho = \lim_{k \to +\infty} \frac{u_{k+1}}{u_k}$:
* If $\rho < 1$, the series converges.
* If $\rho > 1$ or $\rho = +\infty$, the series diverges.
* If $\rho = 1$, the test is inconclusive.

### ROOT TEST (9.5.6)
Let $\rho = \lim_{k \to +\infty} \sqrt[k]{u_k} = \lim_{k \to +\infty} (u_k)^{1/k}$:
* If $\rho < 1$, the series converges.
* If $\rho > 1$ or $\rho = +\infty$, the series diverges.
* If $\rho = 1$, the test is inconclusive.

---

### QUICK CHECK EXERCISES 9.5
*(See page 637 for answers.)*
1. diverges; $1/k^{2/3}$.
2. converges; ratio test.
3. diverges; ratio test.
4. converges; root test.

---

## 9.6 ALTERNATING SERIES; ABSOLUTE AND CONDITIONAL CONVERGENCE

### ALTERNATING SERIES TEST (Leibniz's Test - 9.6.1)
An alternating series $\sum (-1)^{k+1} a_k$ or $\sum (-1)^k a_k$ ($a_k > 0$) converges if:
1. $a_1 \ge a_2 \ge a_3 \ge \dots$ ($a_{k+1} \le a_k$ eventually)
2. $\lim_{k \to +\infty} a_k = 0$

### ALTERNATING SERIES ESTIMATION THEOREM (9.6.2)
If an alternating series satisfies the AST, then:
$$|S - s_n| \le a_{n+1}$$
The error has the same sign as the first omitted term.

### ABSOLUTE VS. CONDITIONAL CONVERGENCE
* **Absolute Convergence:** $\sum |u_k|$ converges $\implies \sum u_k$ converges (Theorem 9.6.4).
* **Conditional Convergence:** $\sum u_k$ converges, but $\sum |u_k|$ diverges (e.g., alternating harmonic series).
* **Ratio Test for Absolute Convergence (9.6.5):** Let $\rho = \lim_{k \to \infty} \left|\frac{u_{k+1}}{u_k}\right|$. If $\rho < 1$, converges absolutely; if $\rho > 1$ or $\infty$, diverges; if $\rho = 1$, inconclusive.

---

### SUMMARY OF CONVERGENCE TESTS (Table 9.6.1)

| Name | Statement | Primary Use Case |
| :--- | :--- | :--- |
| **Divergence Test** | If $\lim u_k \neq 0 \implies$ diverges. | Quick initial check for divergence. |
| **Integral Test** | $\sum u_k$ and $\int_a^\infty f(x)dx$ share convergence. | $f(x)$ readily integrable. |
| **Comparison Test** | $a_k \le b_k$: $\sum b_k$ conv $\implies \sum a_k$ conv; $\sum a_k$ div $\implies \sum b_k$ div. | Clear termwise inequality. |
| **Limit Comparison** | $\rho = \lim \frac{a_k}{b_k} \in (0, \infty) \implies$ same behavior. | Rational/algebraic expressions in $k$. |
| **Ratio Test** | $\rho = \lim \frac{u_{k+1}}{u_k}$: $\rho < 1$ conv, $\rho > 1$ div, $\rho = 1$ inc. | Factorials $k!$ and powers $c^k$. |
| **Root Test** | $\rho = \lim \sqrt[k]{u_k}$: $\rho < 1$ conv, $\rho > 1$ div, $\rho = 1$ inc. | $k$th powers $(u_k)^k$. |
| **Alternating Series** | $a_{k+1} \le a_k$ and $a_k \to 0 \implies \sum (-1)^k a_k$ conv. | Alternating sign series. |
| **Ratio Test (Abs)** | $\rho = \lim |\frac{u_{k+1}}{u_k}|$: $\rho < 1$ abs conv, $\rho > 1$ div. | Mixed signs, power series. |

---

### QUICK CHECK EXERCISES 9.6
*(See page 648 for answers.)*
1. Terms alternate between positive and negative.
2. (a) $1 \ge 1/4 \ge 1/9 \ge \dots \ge 1/k^2 \dots$ and $\lim 1/k^2 = 0$; (b) $|S - s_9| < 1/100$.
3. (a) Conditionally convergent (b) Divergent (c) Absolutely convergent (d) Conditionally convergent.
4. Absolutely convergent.

---

## 9.7 MACLAURIN AND TAYLOR POLYNOMIALS

### TAYLOR AND MACLAURIN POLYNOMIALS
* **$n$th Taylor Polynomial about $x = x_0$ (Definition 9.7.3):**
  $$p_n(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \dots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n$$
* **$n$th Maclaurin Polynomial ($x_0 = 0$):**
  $$p_n(x) = \sum_{k=0}^n \frac{f^{(k)}(0)}{k!}x^k = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \dots + \frac{f^{(n)}(0)}{n!}x^n$$

### REMAINDER & LAGRANGE ERROR BOUND

> **9.7.4 THEOREM (Remainder Estimation Theorem)**
> If $|f^{(n+1)}(t)| \le M$ for all $t$ between $x_0$ and $x$, the remainder $R_n(x) = f(x) - p_n(x)$ satisfies:
> $$|R_n(x)| \le \frac{M}{(n+1)!}|x - x_0|^{n+1} \tag{14}$$

---

### QUICK CHECK EXERCISES 9.7
*(See page 659 for answers.)*
1. $p_3(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3$.
2. For $e^{2x}$: $p_3(x) = 1 + 2x + 2x^2 + \frac{4}{3}x^3$.
3. $p_2(x) = 3 - 4(x-2) + 5(x-2)^2$.
4. For $x^5$ at $x_0 = -1$: $p_3(x) = -1 + 5(x+1) - 10(x+1)^2 + 10(x+1)^3$.
5. (a) $R_n(x) = f(x) - p_n(x)$; (b) $|R_4(x)| \le \frac{20}{5!}|x-2|^5 = \frac{1}{6}|x-2|^5$.

---

## 9.8 MACLAURIN AND TAYLOR SERIES; POWER SERIES

### TAYLOR AND MACLAURIN SERIES

> **9.8.1 DEFINITION**
> * **Taylor Series about $x = x_0$:**
>   $$\sum_{k=0}^\infty \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k$$
> * **Maclaurin Series ($x_0 = 0$):**
>   $$\sum_{k=0}^\infty \frac{f^{(k)}(0)}{k!}x^k$$

### RADIUS AND INTERVAL OF CONVERGENCE (9.8.2 & 9.8.3)
For every power series $\sum c_k(x - x_0)^k$, exactly one of the following holds:
1. Converges only at $x = x_0$ ($R = 0$).
2. Converges absolutely for all $x \in (-\infty, +\infty)$ ($R = +\infty$).
3. Converges absolutely for $|x - x_0| < R$, diverges for $|x - x_0| > R$ ($R = \text{radius of convergence}$). Endpoints $x = x_0 \pm R$ must be tested individually.

### BESSEL FUNCTIONS
* $J_0(x) = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{2^{2k}(k!)^2}, \quad R = +\infty$
* $J_1(x) = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{2^{2k+1} k!(k+1)!}, \quad R = +\infty$

---

### QUICK CHECK EXERCISES 9.8
*(See page 668 for answers.)*
1. $\sum_{k=0}^\infty \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$.
2. $R = 1/2$.
3. $(-\infty, +\infty)$.
4. For $\sum_{k=1}^\infty \frac{(x-4)^k}{\sqrt{k}}$: (a) $R = 1$; (b) At $x=3$, converges (AST); (c) At $x=5$, diverges ($p$-series); (d) Interval is $[3, 5)$.

---

## 9.9 CONVERGENCE OF TAYLOR SERIES

### CONVERGENCE THEOREM (9.9.2)
$$f(x) = \sum_{k=0}^\infty \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k \iff \lim_{n \to \infty} R_n(x) = 0$$

---

### IMPORTANT MACLAURIN SERIES (Table 9.9.1)

| Function | Maclaurin Series | Interval of Convergence |
| :--- | :--- | :--- |
| $\frac{1}{1-x}$ | $\sum_{k=0}^\infty x^k = 1 + x + x^2 + x^3 + \dots$ | $-1 < x < 1$ |
| $\frac{1}{1+x^2}$ | $\sum_{k=0}^\infty (-1)^k x^{2k} = 1 - x^2 + x^4 - x^6 + \dots$ | $-1 < x < 1$ |
| $e^x$ | $\sum_{k=0}^\infty \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$ | $-\infty < x < +\infty$ |
| $\sin x$ | $\sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$ | $-\infty < x < +\infty$ |
| $\cos x$ | $\sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$ | $-\infty < x < +\infty$ |
| $\ln(1+x)$ | $\sum_{k=1}^\infty \frac{(-1)^{k+1} x^k}{k} = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$ | $-1 < x \le 1$ |
| $\tan^{-1} x$ | $\sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{2k+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \dots$ | $-1 \le x \le 1$ |
| $\sinh x$ | $\sum_{k=0}^\infty \frac{x^{2k+1}}{(2k+1)!} = x + \frac{x^3}{3!} + \frac{x^5}{5!} + \dots$ | $-\infty < x < +\infty$ |
| $\cosh x$ | $\sum_{k=0}^\infty \frac{x^{2k}}{(2k)!} = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \dots$ | $-\infty < x < +\infty$ |
| $(1+x)^m$ | $1 + \sum_{k=1}^\infty \frac{m(m-1)\dots(m-k+1)}{k!}x^k$ | $-1 < x < 1$ |

---

### QUICK CHECK EXERCISES 9.9
*(See page 677 for answers.)*
1. $\sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!}$.
2. $\sum_{k=0}^\infty \frac{x^k}{k!}$.
3. $\sum_{k=1}^\infty \frac{(-1)^{k+1}x^k}{k}$ on $(-1, 1]$.
4. $1 + \sum_{k=1}^\infty \frac{m(m-1)\dots(m-k+1)}{k!}x^k$ for $|x| < 1$.

---

## 9.10 DIFFERENTIATING AND INTEGRATING POWER SERIES; MODELING WITH TAYLOR SERIES

### TERM-BY-TERM DIFFERENTIATION & INTEGRATION (9.10.2 & 9.10.4)
If $f(x) = \sum_{k=0}^\infty c_k(x - x_0)^k$ with radius $R > 0$:
* $f'(x) = \sum_{k=1}^\infty k c_k(x - x_0)^{k-1}$ with radius $R$.
* $\int f(x)\,dx = \sum_{k=0}^\infty \frac{c_k}{k+1}(x - x_0)^{k+1} + C$ with radius $R$.

> **Theorem 9.10.6:** Any power series representing $f$ on an open interval containing $x_0$ is the unique Taylor series for $f$ about $x_0$.

---

### APPLICATIONS & PHYSICAL MODELS
* **Definite Integrals:** $\int_0^1 e^{-x^2}dx = \sum_{k=0}^\infty \frac{(-1)^k}{(2k+1)k!} \approx 0.747$.
* **Simple Pendulum Period:**
  $$T = 4\sqrt{\frac{L}{g}}\int_0^{\pi/2} \frac{d\phi}{\sqrt{1 - k^2\sin^2\phi}} = 2\pi\sqrt{\frac{L}{g}}\left[1 + \frac{1}{4}k^2 + \frac{9}{64}k^4 + \dots\right]$$
  * First-order (small vibration) model: $T \approx 2\pi\sqrt{\frac{L}{g}}$.
  * Second-order model: $T \approx 2\pi\sqrt{\frac{L}{g}}\left(1 + \frac{k^2}{4}\right)$.

---

### QUICK CHECK EXERCISES 9.10
*(See page 689 for answers.)*
1. $\sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{k!}$.
2. $1 - x + x^2 - x^3 + \dots = \sum_{k=0}^\infty (-1)^k x^k$.
3. $1 + \frac{3}{2}x + \frac{4}{3}x^2 + \dots$
4. (a) $f''(1) = -1/2$; (b) $f(x) = 4 + (x-1) - \frac{1}{4}(x-1)^2 + \frac{1}{18}(x-1)^3 + \dots = 4 + \sum_{k=1}^\infty \frac{(-1)^{k+1}(x-1)^k}{k \cdot (k!)}$.
