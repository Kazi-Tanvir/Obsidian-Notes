# CHAPTER 3: THE DERIVATIVE IN GRAPHING AND APPLICATIONS

> Derivatives can help to find the most cost-effective location for an offshore oil-drilling rig.

In this chapter we will study various applications of the derivative. For example, we will use methods of calculus to analyze functions and their graphs. In the process, we will show how calculus and graphing utilities, working together, can provide most of the important information about the behavior of functions. Another important application of the derivative will be in the solution of optimization problems. For example, if time is the main consideration in a problem, we might be interested in finding the quickest way to perform a task, and if cost is the main consideration, we might be interested in finding the least expensive way to perform a task. Mathematically, optimization problems can be reduced to finding the largest or smallest value of a function on some interval, and determining where the largest or smallest value occurs. Using the derivative, we will develop the mathematical tools necessary for solving such problems. We will also use the derivative to study the motion of a particle moving along a line, and we will show how the derivative can help us to approximate solutions of equations.

---

## 3.1 ANALYSIS OF FUNCTIONS I: INCREASE, DECREASE, AND CONCAVITY

### INCREASING AND DECREASING FUNCTIONS

> **3.1.1 DEFINITION**  
> Let $f$ be defined on an interval, and let $x_1$ and $x_2$ denote points in that interval.  
> (a) $f$ is **increasing** on the interval if $f(x_1) < f(x_2)$ whenever $x_1 < x_2$.  
> (b) $f$ is **decreasing** on the interval if $f(x_1) > f(x_2)$ whenever $x_1 < x_2$.  
> (c) $f$ is **constant** on the interval if $f(x_1) = f(x_2)$ for all points $x_1$ and $x_2$.

> **3.1.2 THEOREM**  
> Let $f$ be a function that is continuous on a closed interval $[a, b]$ and differentiable on the open interval $(a, b)$.  
> (a) If $f'(x) > 0$ for every value of $x$ in $(a, b)$, then $f$ is **increasing** on $[a, b]$.  
> (b) If $f'(x) < 0$ for every value of $x$ in $(a, b)$, then $f$ is **decreasing** on $[a, b]$.  
> (c) If $f'(x) = 0$ for every value of $x$ in $(a, b)$, then $f$ is **constant** on $[a, b]$.

#### Examples:
* **Example 1:** $f(x) = x^2 - 4x + 3 \implies f'(x) = 2(x - 2)$. Decreasing on $(-\infty, 2]$, increasing on $[2, +\infty)$.
* **Example 2:** $f(x) = x^3 \implies f'(x) = 3x^2 > 0$ for $x \neq 0$. Increasing on $(-\infty, +\infty)$.
* **Example 3:** $f(x) = 3x^4 + 4x^3 - 12x^2 + 2 \implies f'(x) = 12x(x + 2)(x - 1)$. Decreasing on $(-\infty, -2]$ and $[0, 1]$, increasing on $[-2, 0]$ and $[1, +\infty)$.

---

### CONCAVITY

> **3.1.3 DEFINITION**  
> If $f$ is differentiable on an open interval, then $f$ is said to be **concave up** on the open interval if $f'$ is increasing on that interval, and $f$ is said to be **concave down** on the open interval if $f'$ is decreasing on that interval.

> **3.1.4 THEOREM**  
> Let $f$ be twice differentiable on an open interval.  
> (a) If $f''(x) > 0$ for every value of $x$ in the open interval, then $f$ is **concave up** on that interval.  
> (b) If $f''(x) < 0$ for every value of $x$ in the open interval, then $f$ is **concave down** on that interval.

---

### INFLECTION POINTS

> **3.1.5 DEFINITION**  
> If $f$ is continuous on an open interval containing a value $x_0$, and if $f$ changes the direction of its concavity at the point $(x_0, f(x_0))$, then we say that $f$ has an **inflection point** at $x_0$, and we call the point $(x_0, f(x_0))$ on the graph of $f$ an inflection point of $f$.

* If $(x_0, f(x_0))$ is an inflection point and $f''(x_0)$ exists, then $f''(x_0) = 0$.
* *Note:* $f''(x_0) = 0$ does not guarantee an inflection point (e.g., $f(x) = x^4$ at $x = 0$).

---

### QUICK CHECK EXERCISES 3.1
*(See page 196 for answers.)*
1. (a) $f(x_1) < f(x_2)$ (b) $f(x_1) > f(x_2)$ (c) increasing (d) $= 0$.  
2. $f(x) = 0.1(x^3 - 3x^2 - 9x) \implies f'(x) = 0.3(x + 1)(x - 3), f''(x) = 0.6(x - 1)$: (a) $x = -1, 3$ (b) $(-\infty, -1]$ and $[3, +\infty)$ (c) $(-\infty, 1)$ (d) $(1, -1.1)$.  
3. $f'(x) = x(x - 4)^2, f''(x) = (x - 4)(3x - 4)$: (a) $[0, +\infty)$ (b) $(-\infty, 4/3)$ and $(4, +\infty)$ (c) $(4/3, 4)$.  
4. The graph is increasing and concave down.

---

## 3.2 ANALYSIS OF FUNCTIONS II: RELATIVE EXTREMA; GRAPHING POLYNOMIALS

### RELATIVE MAXIMA AND MINIMA

> **3.2.1 DEFINITION**  
> * $f$ has a **relative maximum** at $x_0$ if $f(x_0) \ge f(x)$ for all $x$ in an open interval containing $x_0$.  
> * $f$ has a **relative minimum** at $x_0$ if $f(x_0) \le f(x)$ for all $x$ in an open interval containing $x_0$.  
> * An extremum is either a relative maximum or relative minimum.

> **3.2.2 THEOREM (Critical Point Theorem)**  
> If $f$ has a relative extremum at $x = x_0$, then $x = x_0$ is a **critical point** of $f$; that is, either $f'(x_0) = 0$ (a **stationary point**) or $f$ is not differentiable at $x_0$.

---

### TESTS FOR RELATIVE EXTREMA

> **3.2.3 THEOREM (First Derivative Test)**  
> Suppose $f$ is continuous at a critical point $x_0$:  
> (a) If $f'(x)$ changes from $+$ to $-$ across $x_0$, then $f$ has a **relative maximum** at $x_0$.  
> (b) If $f'(x)$ changes from $-$ to $+$ across $x_0$, then $f$ has a **relative minimum** at $x_0$.  
> (c) If $f'(x)$ does not change sign across $x_0$, then $f$ has **no relative extremum** at $x_0$.

> **3.2.4 THEOREM (Second Derivative Test)**  
> Suppose $f$ is twice differentiable at $x_0$ and $f'(x_0) = 0$:  
> (a) If $f''(x_0) > 0$, then $f$ has a **relative minimum** at $x_0$.  
> (b) If $f''(x_0) < 0$, then $f$ has a **relative maximum** at $x_0$.  
> (c) If $f''(x_0) = 0$, the test is **inconclusive**.

---

### MULTIPLICITY AND POLYNOMIAL GRAPHS

> **3.2.5 THEOREM (Geometric Implications of Multiplicity)**  
> For a polynomial $p(x)$ with root $r$ of multiplicity $m$:  
> (a) If $m$ is **even**, the graph is tangent to the $x$-axis at $r$ and does **not** cross it (no inflection point).  
> (b) If $m$ is **odd and $> 1$**, the graph is tangent to the $x$-axis at $r$, **crosses** it, and has an **inflection point** there.  
> (c) If $m = 1$ (**simple root**), the graph is **not** tangent to the $x$-axis and **crosses** it.

A polynomial of degree $n$ has at most $n$ roots ($x$-intercepts), at most $n - 1$ relative extrema, and at most $n - 2$ inflection points.

---

### QUICK CHECK EXERCISES 3.2
*(See page 207 for answers.)*
1. $\le$ (or $\ge$ for relative max/min definition).  
2. $f'(x) > 0$ on $(-\infty, 2), (5, 7)$ and $f'(x) < 0$ on $(2, 3), (3, 5), (7, +\infty) \implies$ relative maxima at $x = 2, 7$; relative minimum at $x = 5$.  
3. $f''(x) = 2x + 1 \implies f''(-2) = -3 < 0$ (relative maximum), $f''(1) = 3 > 0$ (relative minimum).  
4. $f(x) = (x^2 - 4)^2$: (a) relative maximum at $(0, 16)$ (b) relative minima at $(-2, 0)$ and $(2, 0)$ (c) inflection points at $(\pm 2/\sqrt{3}, 64/9)$.

---

## 3.3 ANALYSIS OF FUNCTIONS III: RATIONAL FUNCTIONS, CUSPS, AND VERTICAL TANGENTS

### PROCEDURE FOR GRAPHING RATIONAL FUNCTIONS
1. **Symmetries:** Check for $y$-axis symmetry ($f(-x) = f(x)$) or origin symmetry ($f(-x) = -f(x)$).
2. **Intercepts:** $x$-intercepts ($P(x) = 0$) and $y$-intercept ($f(0)$).
3. **Vertical Asymptotes:** $Q(x) = 0$ (where denominator is zero and not cancelled).
4. **Sign Analysis:** Intervals determined by $x$-intercepts and vertical asymptotes.
5. **End Behavior & Horizontal/Oblique Asymptotes:** Limits as $x \to \pm\infty$.
   * If $\deg(P) = \deg(Q) + 1$, division yields an **oblique (slant) asymptote** $y = mx + b$.
   * If $\deg(P) \ge \deg(Q) + 2$, division yields a **curvilinear asymptote**.
6. **Derivatives:** Find $f'(x)$ and $f''(x)$.
7. **Conclusions & Graph:** Determine increase/decrease, extrema, concavity, and inflection points.

### CUSPS AND VERTICAL TANGENTS
* **Vertical Tangent with Inflection Point:** $f'(x) \to +\infty$ (or $-\infty$) from both sides.
* **Cusp:** $f'(x) \to +\infty$ from one side and $f'(x) \to -\infty$ from the other side.

---

### QUICK CHECK EXERCISES 3.3
*(See page 216 for answers.)*
Properties of $f(x) = \frac{3(x + 1)(x - 3)}{(x + 2)(x - 4)}$ and $f(x) = \frac{x^2 - 4}{x^{8/3}}$.

---

## 3.4 ABSOLUTE MAXIMA AND MINIMA

### ABSOLUTE EXTREMA

> **3.4.1 DEFINITION**  
> * $f$ has an **absolute maximum** at $x_0$ on interval $I$ if $f(x) \le f(x_0)$ for all $x \in I$.  
> * $f$ has an **absolute minimum** at $x_0$ on interval $I$ if $f(x) \ge f(x_0)$ for all $x \in I$.

> **3.4.2 THEOREM (Extreme-Value Theorem)**  
> If $f$ is continuous on a finite closed interval $[a, b]$, then $f$ attains both an absolute maximum and an absolute minimum on $[a, b]$.

> **3.4.3 THEOREM**  
> If $f$ has an absolute extremum on an open interval $(a, b)$, it must occur at a critical point of $f$.

#### Finding Absolute Extrema on Finite Closed Interval $[a, b]$:
1. Find all critical points in $(a, b)$.
2. Evaluate $f$ at all critical points and at endpoints $a$ and $b$.
3. The largest value is the absolute maximum; the smallest is the absolute minimum.

> **3.4.4 THEOREM (Single Relative Extremum Rule)**  
> If $f$ is continuous on an interval and has **only one relative extremum** at $x_0$:  
> (a) If it is a relative minimum, then $f(x_0)$ is the **absolute minimum**.  
> (b) If it is a relative maximum, then $f(x_0)$ is the **absolute maximum**.

---

### QUICK CHECK EXERCISES 3.4
*(See page 224 for answers.)*
Absolute and relative extrema evaluations from graphs and tables.

---

## 3.5 APPLIED MAXIMUM AND MINIMUM PROBLEMS

### 5-STEP PROCEDURE FOR OPTIMIZATION PROBLEMS
1. **Draw a figure** and label relevant quantities.
2. **Write a formula** for the quantity $Q$ to be maximized or minimized.
3. **Eliminate extra variables** using given geometric/physical constraints so that $Q = f(x)$ is a function of a single variable.
4. **Determine the allowable interval** for $x$ based on physical restrictions.
5. **Apply optimization techniques** (EVT on closed interval, or First/Second Derivative Tests on open/infinite intervals).

#### Classic Applied Examples:
* **Fencing Garden:** Max area of rectangle with perimeter 100 ft is a $25\text{ ft} \times 25\text{ ft}$ square ($A = 625\text{ ft}^2$).
* **Open Box:** From 16 in by 30 in cardboard, cut squares of side $x = 10/3\text{ in} \implies V \approx 726\text{ in}^3$.
* **Pipeline Cost:** Minimum cost occurs at $x = 5/\sqrt{3}\text{ km} \approx 2.89\text{ km}$.
* **Can of Least Surface Area:** For fixed volume $V$, minimum surface area occurs when $h = 2r$ (height = diameter).

> **Pierre de Fermat (1601–1665)**  
> Pioneer in optimization and differential methods (*Fermat's Principle of Least Time*, *Fermat's Last Theorem*).

### ECONOMICS APPLICATIONS
* Profit: $P(x) = R(x) - C(x)$
* **Marginal Analysis:** Marginal cost $C'(x)$, Marginal revenue $R'(x)$, Marginal profit $P'(x) = R'(x) - C'(x)$.
* Maximum profit occurs where $P'(x) = 0 \iff R'(x) = C'(x)$ (Marginal Revenue = Marginal Cost).

---

### QUICK CHECK EXERCISES 3.5
*(See page 238 for answers.)*
Formulating objective functions and intervals for number sums, products, and dimensions.

---

## 3.6 RECTILINEAR MOTION

### DEFINITIONS & RELATIONSHIPS
* **Position:** $s = s(t)$
* **Velocity:** $v(t) = s'(t) = \frac{ds}{dt}$
* **Speed:** $|v(t)| = |s'(t)| = \left|\frac{ds}{dt}\right|$
* **Acceleration:** $a(t) = v'(t) = s''(t) = \frac{d^2s}{dt^2}$

### SPEEDING UP AND SLOWING DOWN
* **Speeding Up:** $v(t)$ and $a(t)$ have the **same sign** ($v(t)a(t) > 0$).
* **Slowing Down:** $v(t)$ and $a(t)$ have **opposite signs** ($v(t)a(t) < 0$).
* **Momentarily Stopped:** $v(t) = 0$.

> **Willebrord Snell (1591–1626)**  
> Formulated Snell's law of refraction: $\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$.

---

### QUICK CHECK EXERCISES 3.6
*(See page 246 for answers.)*
1. $v(t) = s'(t)$; $a(t) = v'(t)$.  
2. $s(t) = 7t - 2t^2 \implies s(3) = 3, v(3) = -5, \text{speed} = 5, a(3) = -4$.  
3. the same; opposite.  
4. $s(t) = t^4 - 24t^2 \implies$ slowing down for $2 < t < 2\sqrt{3}$.

---

## 3.7 NEWTON'S METHOD

### ROOT-FINDING ALGORITHM

For an initial approximation $x_1$ to a root of $f(x) = 0$:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}, \quad n = 1, 2, 3, \dots \tag{4}$$

> **Niels Henrik Abel (1802–1829)**  
> Proved impossibility of solving general quintic equations by radicals.

#### Examples:
* $x^3 - x - 1 = 0 \implies x_{n+1} = x_n - \frac{x_n^3 - x_n - 1}{3x_n^2 - 1} \implies x \approx 1.32471796$.
* $\cos x = x \implies x_{n+1} = x_n - \frac{x_n - \cos x_n}{1 + \sin x_n} \implies x \approx 0.739085133$.

#### Failure Cases:
* $f'(x_n) = 0$ (division by zero; horizontal tangent).
* Oscillation or divergence (e.g., $f(x) = x^{1/3}$ yields $x_{n+1} = -2x_n$).

---

### QUICK CHECK EXERCISES 3.7
*(See page 252 for answers.)*
1. $x_2 \approx 4, x_3 \approx 2$.  
2. $f(1) = 2, f'(1) = 4 \implies x_2 = 1 - 2/4 = 1/2$.  
3. $x_2 = 0 - 3/f'(0) = 3 \implies f'(0) = -1$.  
4. $f(x) = x^5 - 2, x_1 = 1 \implies x_2 = 1 - (-1)/5 = 1.2$.

---

## 3.8 ROLLE'S THEOREM; MEAN-VALUE THEOREM

### ROLLE'S THEOREM

> **3.8.1 THEOREM (Rolle's Theorem)**  
> Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$. If
> $$f(a) = 0 \quad \text{and} \quad f(b) = 0$$
> then there is at least one point $c \in (a, b)$ such that
> $$f'(c) = 0$$

> **Michel Rolle (1652–1719)**  
> French algebraist who proved the polynomial case of the theorem and established standard root notation $\sqrt[n]{a}$.

---

### THE MEAN-VALUE THEOREM

> **3.8.2 THEOREM (Mean-Value Theorem)**  
> Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$. Then there is at least one point $c \in (a, b)$ such that
> $$f'(c) = \frac{f(b) - f(a)}{b - a} \tag{1}$$

* **Physical / Velocity Meaning:** Instantaneous velocity equals average velocity at least once during a trip.

> **3.8.3 THEOREM (Constant Difference Theorem)**  
> If $f'(x) = g'(x)$ for all $x$ on an interval, then there exists a constant $k$ such that
> $$f(x) = g(x) + k$$
> for all $x$ in that interval (their graphs are vertical shifts of each other).

---

### QUICK CHECK EXERCISES 3.8
*(See page 259 for answers.)*
1. (a) $[0, 1]$ (b) $c = 1/2$.  
2. $[a, b] = [-3, 3] \implies c = -2, 0, 2$.  
3. (a) $b = 2$ (b) $c = 1$.  
4. (a) 1.5 (b) 0.8.  
5. $f(x) = x^2 + 4$.

---

## CHAPTER 3 REVIEW EXERCISES
Exercises 1–72 covering all concepts of increase/decrease, concavity, inflection points, rational curve sketching, absolute extrema on closed/open/infinite intervals, applied optimization problems, rectilinear motion, Newton's method, and the Mean-Value Theorem.

---

## CHAPTER 3 MAKING CONNECTIONS
Explores functions with given derivative and concavity properties, critical point analysis from derivative graphs, Newton's method error convergence analysis, and optimal path problems for obstacles.
