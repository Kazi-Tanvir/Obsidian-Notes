# CHAPTER 1: LIMITS AND CONTINUITY

> Air resistance prevents the velocity of a skydiver from increasing indefinitely. The velocity approaches a limit, called the "terminal velocity."

The development of calculus in the seventeenth century by Newton and Leibniz provided scientists with their first real understanding of what is meant by an "instantaneous rate of change" such as velocity and acceleration. Once the idea was understood conceptually, efficient computational methods followed, and science took a quantum leap forward. The fundamental building block on which rates of change rest is the concept of a "limit," an idea that is so important that all other calculus concepts are now based on it.

In this chapter we will develop the concept of a limit in stages, proceeding from an informal, intuitive notion to a precise mathematical definition. We will also develop theorems and procedures for calculating limits, and we will conclude the chapter by using the limits to study "continuous" curves.

---

## 1.1 LIMITS (AN INTUITIVE APPROACH)

The concept of a "limit" is the fundamental building block on which all calculus concepts are based. In this section we will study limits informally, with the goal of developing an intuitive feel for the basic ideas. In the next three sections we will focus on computational methods and precise definitions.

Many of the ideas of calculus originated with the following two geometric problems:

> **THE TANGENT LINE PROBLEM**  
> Given a function $f$ and a point $P(x_0, y_0)$ on its graph, find an equation of the line that is tangent to the graph at $P$ (Figure 1.1.1).

> **THE AREA PROBLEM**  
> Given a function $f$, find the area between the graph of $f$ and an interval $[a, b]$ on the $x$-axis (Figure 1.1.2).

Traditionally, that portion of calculus arising from the tangent line problem is called **differential calculus** and that arising from the area problem is called **integral calculus**. However, we will see later that the tangent line and area problems are so closely related that the distinction between differential and integral calculus is somewhat artificial.

---

### TANGENT LINES AND LIMITS

In plane geometry, a line is called tangent to a circle if it meets the circle at precisely one point (Figure 1.1.3a). Although this definition is adequate for circles, it is not appropriate for more general curves. For example, in Figure 1.1.3b, the line meets the curve exactly once but is obviously not what we would regard to be a tangent line; and in Figure 1.1.3c, the line appears to be tangent to the curve, yet it intersects the curve more than once.

To obtain a definition of a tangent line that applies to curves other than circles, we must view tangent lines another way. For this purpose, suppose that we are interested in the tangent line at a point $P$ on a curve in the $xy$-plane and that $Q$ is any point that lies on the curve and is different from $P$. The line through $P$ and $Q$ is called a **secant line** for the curve at $P$. Intuition suggests that if we move the point $Q$ along the curve toward $P$, then the secant line will rotate toward a limiting position. The line in this limiting position is what we will consider to be the **tangent line** at $P$ (Figure 1.1.4a). As suggested by Figure 1.1.4b, this new concept of a tangent line coincides with the traditional concept when applied to circles.

#### Example 1
Find an equation for the tangent line to the parabola $y = x^2$ at the point $P(1, 1)$.

**Solution.** If we can find the slope $m_{\text{tan}}$ of the tangent line at $P$, then we can use the point $P$ and the point-slope formula for a line to write the equation of the tangent line as
$$y - 1 = m_{\text{tan}}(x - 1) \tag{1}$$
To find the slope $m_{\text{tan}}$, consider the secant line through $P$ and a point $Q(x, x^2)$ on the parabola that is distinct from $P$. The slope $m_{\text{sec}}$ of this secant line is
$$m_{\text{sec}} = \frac{x^2 - 1}{x - 1} \tag{2}$$
Figure 1.1.4a suggests that if we now let $Q$ move along the parabola, getting closer and closer to $P$, then the limiting position of the secant line through $P$ and $Q$ will coincide with that of the tangent line at $P$. This in turn suggests that the value of $m_{\text{sec}}$ will get closer and closer to the value of $m_{\text{tan}}$ as $P$ moves toward $Q$ along the curve. However, to say that $Q(x, x^2)$ gets closer and closer to $P(1, 1)$ is algebraically equivalent to saying that $x$ gets closer and closer to 1. Thus, the problem of finding $m_{\text{tan}}$ reduces to finding the "limiting value" of $m_{\text{sec}}$ in Formula (2) as $x$ gets closer and closer to 1 (but with $x \neq 1$ to ensure that $P$ and $Q$ remain distinct).

We can rewrite (2) as
$$m_{\text{sec}} = \frac{x^2 - 1}{x - 1} = \frac{(x - 1)(x + 1)}{x - 1} = x + 1$$
where the cancellation of the factor $(x - 1)$ is allowed because $x \neq 1$. It is now evident that $m_{\text{sec}}$ gets closer and closer to 2 as $x$ gets closer and closer to 1. Thus, $m_{\text{tan}} = 2$ and (1) implies that the equation of the tangent line is
$$y - 1 = 2(x - 1) \quad \text{or equivalently} \quad y = 2x - 1$$
Figure 1.1.5 shows the graph of $y = x^2$ and this tangent line.

---

### AREAS AND LIMITS

Just as the general notion of a tangent line leads to the concept of limit, so does the general notion of area. For plane regions with straight-line boundaries, areas can often be calculated by subdividing the region into rectangles or triangles and adding the areas of the constituent parts (Figure 1.1.6). However, for regions with curved boundaries, such as that in Figure 1.1.7a, a more general approach is needed. One such approach is to begin by approximating the area of the region by inscribing a number of rectangles of equal width under the curve and adding the areas of these rectangles (Figure 1.1.7b). Intuition suggests that if we repeat that approximation process using more and more rectangles, then the rectangles will tend to fill in the gaps under the curve, and the approximations will get closer and closer to the exact area under the curve (Figure 1.1.7c). This suggests that we can define the area under the curve to be the limiting value of these approximations.

---

### DECIMALS AND LIMITS

Limits also arise in the familiar context of decimals. For example, the decimal expansion of the fraction $\frac{1}{3}$ is
$$\frac{1}{3} = 0.33333\dots \tag{3}$$
in which the dots indicate that the digit 3 repeats indefinitely. Although you may not have thought about decimals in this way, we can write (3) as
$$\frac{1}{3} = 0.33333\dots = 0.3 + 0.03 + 0.003 + 0.0003 + 0.00003 + \dots \tag{4}$$
which is a sum with "infinitely many" terms. We interpret this to mean that the succession of finite sums
$$0.3, \; 0.3 + 0.03, \; 0.3 + 0.03 + 0.003, \; 0.3 + 0.03 + 0.003 + 0.0003, \dots$$
gets closer and closer to a limiting value of $\frac{1}{3}$ as more and more terms are included.

---

### LIMITS

The most basic use of limits is to describe how a function behaves as the independent variable approaches a given value. For example, for $f(x) = x^2 - x + 1$ near $x = 2$, as $x$ approaches 2 from either side, $f(x)$ approaches 3:
$$\lim_{x \to 2} (x^2 - x + 1) = 3 \tag{5}$$

> **1.1.1 LIMITS (AN INFORMAL VIEW)**  
> If the values of $f(x)$ can be made as close as we like to $L$ by taking values of $x$ sufficiently close to $a$ (but not equal to $a$), then we write
> $$\lim_{x \to a} f(x) = L \tag{6}$$
> which is read "the limit of $f(x)$ as $x$ approaches $a$ is $L$." The expression in (6) can also be written as $f(x) \to L$ as $x \to a$.

#### Example 2
Use numerical evidence to make a conjecture about the value of $\lim_{x \to 1} \frac{x - 1}{\sqrt{x} - 1}$.

**Solution.** Table 1.1.1 shows sample $x$-values approaching 1:
* From left: $x = 0.99 \implies f(x) = 1.994987; \; x = 0.999 \implies f(x) = 1.999500; \; x = 0.9999 \implies f(x) = 1.999950; \; x = 0.99999 \implies f(x) = 1.999995$.
* From right: $x = 1.01 \implies f(x) = 2.004988; \; x = 1.001 \implies f(x) = 2.000500; \; x = 1.0001 \implies f(x) = 2.000050; \; x = 1.00001 \implies f(x) = 2.000005$.  
We conjecture that $\lim_{x \to 1} \frac{x - 1}{\sqrt{x} - 1} = 2$.

#### Example 3
Use numerical evidence to make a conjecture about the value of $\lim_{x \to 0} \frac{\sin x}{x}$ ($x$ in radians).

**Solution.** Table 1.1.2 shows that for $x = \pm 1.0, \pm 0.9, \pm 0.8, \pm 0.7, \pm 0.6, \pm 0.5, \pm 0.4, \pm 0.3, \pm 0.2, \pm 0.1, \pm 0.01$, $\frac{\sin x}{x}$ evaluates to $0.84147, 0.87036, 0.89670, 0.92031, 0.94107, 0.95885, 0.97355, 0.98507, 0.99335, 0.99833, 0.99998$. We conjecture that $\lim_{x \to 0} \frac{\sin x}{x} = 1$.

#### SAMPLING PITFALLS
Evaluating $\sin(\pi/x)$ at $x = \pm 1, \pm 0.1, \pm 0.01, \dots$ gives $\sin(\pm n\pi) = 0$, falsely suggesting a limit of 0. In reality, the function oscillates infinitely between $-1$ and $1$ as $x \to 0$, so no limit exists.

---

### ONE-SIDED LIMITS

> **1.1.2 ONE-SIDED LIMITS (AN INFORMAL VIEW)**  
> If the values of $f(x)$ can be made as close as we like to $L$ by taking values of $x$ sufficiently close to $a$ (but greater than $a$), then we write
> $$\lim_{x \to a^+} f(x) = L \tag{14}$$
> and if the values of $f(x)$ can be made as close as we like to $L$ by taking values of $x$ sufficiently close to $a$ (but less than $a$), then we write
> $$\lim_{x \to a^-} f(x) = L \tag{15}$$

> **1.1.3 THE RELATIONSHIP BETWEEN ONE-SIDED AND TWO-SIDED LIMITS**  
> The two-sided limit of a function $f(x)$ exists at $a$ if and only if both of the one-sided limits exist at $a$ and have the same value; that is,
> $$\lim_{x \to a} f(x) = L \iff \lim_{x \to a^-} f(x) = L = \lim_{x \to a^+} f(x)$$

#### Example 4
$\lim_{x \to 0} \frac{|x|}{x}$ does not exist because $\lim_{x \to 0^+} \frac{|x|}{x} = 1$ and $\lim_{x \to 0^-} \frac{|x|}{x} = -1$.

#### Example 5 & 6
For piecewise/jump graphs in Figure 1.1.13 and Figure 1.1.14:
* If $\lim_{x \to a^+} f(x) = 3$ and $\lim_{x \to a^-} f(x) = 1$, then $\lim_{x \to a} f(x)$ does not exist.
* If $\lim_{x \to a^+} f(x) = 2$ and $\lim_{x \to a^-} f(x) = 2$, then $\lim_{x \to a} f(x) = 2$, regardless of the value of $f(a)$.

---

### INFINITE LIMITS & VERTICAL ASYMPTOTES

> **1.1.4 INFINITE LIMITS (AN INFORMAL VIEW)**  
> * $\lim_{x \to a} f(x) = +\infty$ means $f(x)$ increases without bound as $x \to a$.
> * $\lim_{x \to a} f(x) = -\infty$ means $f(x)$ decreases without bound as $x \to a$.

The line $x = a$ is called a **vertical asymptote** of the curve $y = f(x)$ if at least one of the one-sided limits as $x \to a^-$ or $x \to a^+$ is $+\infty$ or $-\infty$.

#### Example 7
* $f(x) = \frac{1}{x - a} \implies \lim_{x \to a^+} f(x) = +\infty, \ \lim_{x \to a^-} f(x) = -\infty$.
* $f(x) = \frac{1}{(x - a)^2} \implies \lim_{x \to a} f(x) = +\infty$.
* $f(x) = -\frac{1}{x - a} \implies \lim_{x \to a^+} f(x) = -\infty, \ \lim_{x \to a^-} f(x) = +\infty$.
* $f(x) = -\frac{1}{(x - a)^2} \implies \lim_{x \to a} f(x) = -\infty$.

#### Example 8
For the function $f$ graphed in Figure 1.1.18:
(a) $\lim_{x \to -2^-} f(x) = 1$  
(b) $\lim_{x \to -2^+} f(x) = -2$  
(c) $\lim_{x \to 0^-} f(x) = 0$  
(d) $\lim_{x \to 0^+} f(x) = -\infty$  
(e) $\lim_{x \to 4^-} f(x)$ does not exist (oscillates)  
(f) $\lim_{x \to 4^+} f(x) = +\infty$  
(g) Vertical asymptotes: $x = 0$ ($y$-axis) and $x = 4$.

---

### QUICK CHECK EXERCISES 1.1
*(See page 61 for answers.)*

1. We write $\lim_{x \to a} f(x) = L$ provided the values of $\underline{\hspace{1cm}}$ can be made as close to $\underline{\hspace{1cm}}$ as desired, by taking values of $\underline{\hspace{1cm}}$ sufficiently close to $\underline{\hspace{1cm}}$ but not $\underline{\hspace{1cm}}$.
2. We write $\lim_{x \to a^-} f(x) = +\infty$ provided $\underline{\hspace{1cm}}$ increases without bound, as $\underline{\hspace{1cm}}$ approaches $\underline{\hspace{1cm}}$ from the left.
3. State what must be true about $\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$ in order for it to be the case that $\lim_{x \to a} f(x) = L$.
4. Use the accompanying graph of $y = f(x) \ (-\infty < x < 3)$ to determine the limits:  
   (a) $\lim_{x \to 0} f(x) = \underline{\hspace{1cm}}$  
   (b) $\lim_{x \to 2^-} f(x) = \underline{\hspace{1cm}}$  
   (c) $\lim_{x \to 2^+} f(x) = \underline{\hspace{1cm}}$  
   (d) $\lim_{x \to 3^-} f(x) = \underline{\hspace{1cm}}$
5. The slope of the secant line through $P(2, 4)$ and $Q(x, x^2)$ on the parabola $y = x^2$ is $m_{\text{sec}} = x + 2$. It follows that the slope of the tangent line to this parabola at the point $P$ is $\underline{\hspace{1cm}}$.

#### QUICK CHECK ANSWERS 1.1
1. $f(x); \ L; \ x; \ a; \ a$  
2. $f(x); \ x; \ a$  
3. Both one-sided limits must exist and equal $L$.  
4. (a) $0$ (b) $1$ (c) $+\infty$ (d) $-\infty$  
5. $4$

---

### EXERCISE SET 1.1

**1–10 In these exercises, make reasonable assumptions about the graph of the indicated function outside of the region depicted.**

1. For the function $g$ in Figure Ex-1, find: (a) $\lim_{x \to 0^-} g(x)$ (b) $\lim_{x \to 0^+} g(x)$ (c) $\lim_{x \to 0} g(x)$ (d) $g(0)$.
2. For the function $G$ in Figure Ex-2, find: (a) $\lim_{x \to 0^-} G(x)$ (b) $\lim_{x \to 0^+} G(x)$ (c) $\lim_{x \to 0} G(x)$ (d) $G(0)$.
3. For the function $f$ in Figure Ex-3, find: (a) $\lim_{x \to 3^-} f(x)$ (b) $\lim_{x \to 3^+} f(x)$ (c) $\lim_{x \to 3} f(x)$ (d) $f(3)$.
4. For the function $f$ in Figure Ex-4, find: (a) $\lim_{x \to 2^-} f(x)$ (b) $\lim_{x \to 2^+} f(x)$ (c) $\lim_{x \to 2} f(x)$ (d) $f(2)$.
5. For the function $F$ in Figure Ex-5, find: (a) $\lim_{x \to -2^-} F(x)$ (b) $\lim_{x \to -2^+} F(x)$ (c) $\lim_{x \to -2} F(x)$ (d) $F(-2)$.
6. For the function $G$ in Figure Ex-6, find: (a) $\lim_{x \to 0^-} G(x)$ (b) $\lim_{x \to 0^+} G(x)$ (c) $\lim_{x \to 0} G(x)$ (d) $G(0)$.
7. For the function $f$ in Figure Ex-7, find: (a) $\lim_{x \to 3^-} f(x)$ (b) $\lim_{x \to 3^+} f(x)$ (c) $\lim_{x \to 3} f(x)$ (d) $f(3)$.
8. For the function $\phi$ in Figure Ex-8, find: (a) $\lim_{x \to 4^-} \phi(x)$ (b) $\lim_{x \to 4^+} \phi(x)$ (c) $\lim_{x \to 4} \phi(x)$ (d) $\phi(4)$.
9. For the function $f$ in Figure Ex-9, find:  
   (a) $\lim_{x \to -2} f(x)$  
   (b) $\lim_{x \to 0^-} f(x)$  
   (c) $\lim_{x \to 0^+} f(x)$  
   (d) $\lim_{x \to 2^-} f(x)$  
   (e) $\lim_{x \to 2^+} f(x)$  
   (f) the vertical asymptotes of the graph of $f$.
10. For the function $f$ in Figure Ex-10, find:  
    (a) $\lim_{x \to -2^-} f(x)$  
    (b) $\lim_{x \to -2^+} f(x)$  
    (c) $\lim_{x \to 0^-} f(x)$  
    (d) $\lim_{x \to 0^+} f(x)$  
    (e) $\lim_{x \to 2^-} f(x)$  
    (f) $\lim_{x \to 2^+} f(x)$  
    (g) the vertical asymptotes of the graph of $f$.

**11–12 (i) Complete the table and make a guess about the limit. (ii) Confirm by graphing.**

11. $f(x) = \frac{\sin 2x}{x}; \quad \lim_{x \to 0} f(x)$  
    $x: -0.1, -0.01, -0.001, 0.001, 0.01, 0.1$
12. $f(x) = \frac{\cos x - 1}{x^2}; \quad \lim_{x \to 0} f(x)$  
    $x: -0.5, -0.05, -0.005, 0.005, 0.05, 0.5$

**13–16 [CAS] (i) Make a guess at the limit by evaluating at specified $x$-values. (ii) Confirm graphically. (iii) Find with CAS.**

13. (a) $\lim_{x \to 1} \frac{x - 1}{x^3 - 1}; \quad x = 2, 1.5, 1.1, 1.01, 1.001, 0, 0.5, 0.9, 0.99, 0.999$  
    (b) $\lim_{x \to 1^+} \frac{x + 1}{x^3 - 1}; \quad x = 2, 1.5, 1.1, 1.01, 1.001, 1.0001$  
    (c) $\lim_{x \to 1^-} \frac{x + 1}{x^3 - 1}; \quad x = 0, 0.5, 0.9, 0.99, 0.999, 0.9999$
14. (a) $\lim_{x \to 0} \frac{\sqrt{x + 1} - 1}{x}; \quad x = \pm 0.25, \pm 0.1, \pm 0.001, \pm 0.0001$  
    (b) $\lim_{x \to 0^+} \frac{\sqrt{x + 1} + 1}{x}; \quad x = 0.25, 0.1, 0.001, 0.0001$  
    (c) $\lim_{x \to 0^-} \frac{\sqrt{x + 1} + 1}{x}; \quad x = -0.25, -0.1, -0.001, -0.0001$
15. (a) $\lim_{x \to 0} \frac{\sin 3x}{x}; \quad x = \pm 0.25, \pm 0.1, \pm 0.001, \pm 0.0001$  
    (b) $\lim_{x \to -1} \frac{\cos x}{x + 1}; \quad x = 0, -0.5, -0.9, -0.99, -0.999, -1.5, -1.1, -1.01, -1.001$
16. (a) $\lim_{x \to -1} \frac{\tan(x + 1)}{x + 1}; \quad x = 0, -0.5, -0.9, -0.99, -0.999, -1.5, -1.1, -1.01, -1.001$  
    (b) $\lim_{x \to 0} \frac{\sin(5x)}{\sin(2x)}; \quad x = \pm 0.25, \pm 0.1, \pm 0.001, \pm 0.0001$

**17–20 True–False Determine whether the statement is true or false. Explain your answer.**

17. If $f(a) = L$, then $\lim_{x \to a} f(x) = L$.
18. If $\lim_{x \to a} f(x)$ exists, then so do $\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$.
19. If $\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$ exist, then so does $\lim_{x \to a} f(x)$.
20. If $\lim_{x \to a^+} f(x) = +\infty$, then $f(a)$ is undefined.

**21–26 Sketch a possible graph for a function $f$ with the specified properties.**

21. (i) Domain of $f$ is $[-1, 1]$; (ii) $f(-1) = f(0) = f(1) = 0$; (iii) $\lim_{x \to -1^+} f(x) = \lim_{x \to 0} f(x) = \lim_{x \to 1^-} f(x) = 1$.
22. (i) Domain of $f$ is $[-2, 1]$; (ii) $f(-2) = f(0) = f(1) = 0$; (iii) $\lim_{x \to -2^+} f(x) = 2, \lim_{x \to 0} f(x) = 0,$ and $\lim_{x \to 1^-} f(x) = 1$.
23. (i) Domain of $f$ is $(-\infty, 0]$; (ii) $f(-2) = f(0) = 1$; (iii) $\lim_{x \to -2} f(x) = +\infty$.
24. (i) Domain of $f$ is $(0, +\infty)$; (ii) $f(1) = 0$; (iii) $y$-axis is vertical asymptote; (iv) $f(x) < 0$ if $0 < x < 1$.
25. (i) $f(-3) = f(0) = f(2) = 0$; (ii) $\lim_{x \to -2^-} f(x) = +\infty, \lim_{x \to -2^+} f(x) = -\infty$; (iii) $\lim_{x \to 1} f(x) = +\infty$.
26. (i) $f(-1) = 0, f(0) = 1, f(1) = 0$; (ii) $\lim_{x \to -1^-} f(x) = 0, \lim_{x \to -1^+} f(x) = +\infty$; (iii) $\lim_{x \to 1^-} f(x) = 1, \lim_{x \to 1^+} f(x) = +\infty$.

**27–30 Modify the argument of Example 1 to find tangent line equation:**

27. The graph of $y = x^2$ at $(-1, 1)$
28. The graph of $y = x^2$ at $(0, 0)$
29. The graph of $y = x^4$ at $(1, 1)$
30. The graph of $y = x^4$ at $(-1, 1)$

**FOCUS ON CONCEPTS**

31. In the special theory of relativity the length $l$ of a narrow rod moving longitudinally is a function $l = l(v)$ of speed $v$.  
    (a) What is the physical interpretation of $l_0$?  
    (b) What is $\lim_{v \to c^-} l(v)$? What is the physical significance of this limit?
32. In the special theory of relativity the mass $m$ of a moving object is a function $m = m(v)$ of speed $v$.  
    (a) What is the physical interpretation of $m_0$?  
    (b) What is $\lim_{v \to c^-} m(v)$? What is the physical significance of this limit?
33. Let $f(x) = (1 + x^2)^{1.1/x^2}$.  
    (a) Graph $f$ in $[-1, 1] \times [2.5, 3.5]$ and conjecture $\lim_{x \to 0} f(x)$.  
    (b) Graph $f$ in $[-0.001, 0.001] \times [2.5, 3.5]$ and conjecture.  
    (c) Graph $f$ in $[-0.000001, 0.000001] \times [2.5, 3.5]$ and conjecture.  
    (d) Given exact limit $\approx 3.00416602$, what flaw do the graphs reveal about numerical evidence?
34. **Writing.** Discuss whether $\lim_{x \to 0} \sqrt{x}$ equals 0 or does not exist.
35. **Writing.** Explain informally why $\lim_{x \to 0} f(x + a) = \lim_{x \to a} f(x)$.

---

## 1.2 COMPUTING LIMITS

### BASIC LIMITS AND LIMIT LAWS

> **1.2.1 THEOREM**  
> Let $a$ and $k$ be real numbers.  
> (a) $\lim_{x \to a} k = k$  
> (b) $\lim_{x \to a} x = a$  
> (c) $\lim_{x \to 0^-} \frac{1}{x} = -\infty$  
> (d) $\lim_{x \to 0^+} \frac{1}{x} = +\infty$

> **1.2.2 THEOREM (Limit Laws)**  
> Let $a$ be a real number, and suppose $\lim_{x \to a} f(x) = L_1$ and $\lim_{x \to a} g(x) = L_2$. Then:  
> (a) $\lim_{x \to a} [f(x) + g(x)] = L_1 + L_2$  
> (b) $\lim_{x \to a} [f(x) - g(x)] = L_1 - L_2$  
> (c) $\lim_{x \to a} [f(x)g(x)] = L_1 L_2$  
> (d) $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L_1}{L_2}$, provided $L_2 \neq 0$  
> (e) $\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{L_1}$, provided $L_1 > 0$ if $n$ is even.

> **1.2.3 THEOREM**  
> For any polynomial $p(x) = c_0 + c_1x + \dots + c_n x^n$ and any real number $a$,
> $$\lim_{x \to a} p(x) = c_0 + c_1a + \dots + c_n a^n = p(a)$$

#### Example 1 to 11
* $\lim_{x \to -25} 3 = 3, \ \lim_{x \to 0} 3 = 3, \ \lim_{x \to \pi} 3 = 3$
* $\lim_{x \to 0} x = 0, \ \lim_{x \to -2} x = -2, \ \lim_{x \to \pi} x = \pi$
* $\lim_{x \to 0^+} \frac{1}{x} = +\infty, \ \lim_{x \to 0^-} \frac{1}{x} = -\infty$
* $\lim_{x \to a} [f(x) - g(x) + 2h(x)] = \lim f - \lim g + 2\lim h$
* $\lim_{x \to 5} (x^2 - 4x + 3) = 5^2 - 4(5) + 3 = 8$
* $\lim_{x \to 1} (x^7 - 2x^5 + 1)^{35} = 0$
* $\lim_{x \to 2} \frac{5x^3 + 4}{x - 3} = \frac{44}{-1} = -44$
* For $f(x) = \frac{2 - x}{(x - 4)(x + 2)}$: $\lim_{x \to 4^+} f(x) = -\infty, \ \lim_{x \to 4^-} f(x) = +\infty \implies \lim_{x \to 4} f(x)$ does not exist.
* (a) $\lim_{x \to 3} \frac{x^2 - 6x + 9}{x - 3} = \lim_{x \to 3} (x - 3) = 0$  
  (b) $\lim_{x \to -4} \frac{2x + 8}{x^2 + x - 12} = \lim_{x \to -4} \frac{2}{x - 3} = -\frac{2}{7}$  
  (c) $\lim_{x \to 5} \frac{x^2 - 3x - 10}{x^2 - 10x + 25} = \lim_{x \to 5} \frac{x + 2}{x - 5}$ does not exist ($+\infty$ from right, $-\infty$ from left).
* $\lim_{x \to 1} \frac{x - 1}{\sqrt{x} - 1} = \lim_{x \to 1} (\sqrt{x} + 1) = 2$
* Piecewise function $f(x) = \begin{cases} 1/(x + 2), & x < -2 \\ x^2 - 5, & -2 < x \le 3 \\ \sqrt{x + 13}, & x > 3 \end{cases}$:  
  (a) $\lim_{x \to -2} f(x)$ does not exist ($\lim_{x \to -2^-} = -\infty, \lim_{x \to -2^+} = -1$)  
  (b) $\lim_{x \to 0} f(x) = -5$  
  (c) $\lim_{x \to 3} f(x) = 4$ ($\lim_{x \to 3^-} = 4, \lim_{x \to 3^+} = 4$).

---

### QUICK CHECK EXERCISES 1.2
*(See page 70 for answers.)*

1. In each part, find the limit by inspection:  
   (a) $\lim_{x \to 8} 7 = \underline{\hspace{1cm}}$  
   (b) $\lim_{y \to 3^+} 12y = \underline{\hspace{1cm}}$  
   (c) $\lim_{x \to 0^-} \frac{x}{|x|} = \underline{\hspace{1cm}}$  
   (d) $\lim_{w \to 5} \frac{w}{|w|} = \underline{\hspace{1cm}}$  
   (e) $\lim_{z \to 1^-} \frac{1}{1 - z} = \underline{\hspace{1cm}}$
2. Given that $\lim_{x \to a} f(x) = 1$ and $\lim_{x \to a} g(x) = 2$, find the limits:  
   (a) $\lim_{x \to a} [3f(x) + 2g(x)] = \underline{\hspace{1cm}}$  
   (b) $\lim_{x \to a} \frac{2f(x) + 1}{1 - f(x)g(x)} = \underline{\hspace{1cm}}$  
   (c) $\lim_{x \to a} \frac{\sqrt{f(x) + 3}}{g(x)} = \underline{\hspace{1cm}}$
3. Find the limits:  
   (a) $\lim_{x \to -1} (x^3 + x^2 + x)^{101} = \underline{\hspace{1cm}}$  
   (b) $\lim_{x \to 2^-} \frac{(x - 1)(x - 2)}{x + 1} = \underline{\hspace{1cm}}$  
   (c) $\lim_{x \to -1^+} \frac{(x - 1)(x - 2)}{x + 1} = \underline{\hspace{1cm}}$  
   (d) $\lim_{x \to 4} \frac{x^2 - 16}{x - 4} = \underline{\hspace{1cm}}$
4. Let
   $$f(x) = \begin{cases} x + 1, & x \le 1 \\ x - 1, & x > 1 \end{cases}$$
   Find the limits that exist: (a) $\lim_{x \to 1^-} f(x)$ (b) $\lim_{x \to 1^+} f(x)$ (c) $\lim_{x \to 1} f(x)$.

#### QUICK CHECK ANSWERS 1.2
1. (a) $7$ (b) $36$ (c) $-1$ (d) $1$ (e) $+\infty$  
2. (a) $7$ (b) $-3$ (c) $1$  
3. (a) $-1$ (b) $0$ (c) $+\infty$ (d) $8$  
4. (a) $2$ (b) $0$ (c) does not exist

---

### EXERCISE SET 1.2

1. Given that $\lim_{x \to a} f(x) = 2, \lim_{x \to a} g(x) = -4, \lim_{x \to a} h(x) = 0$, find:  
   (a) $\lim_{x \to a} [f(x) + 2g(x)]$  
   (b) $\lim_{x \to a} [h(x) - 3g(x) + 1]$  
   (c) $\lim_{x \to a} [f(x)g(x)]$  
   (d) $\lim_{x \to a} [g(x)]^2$  
   (e) $\lim_{x \to a} \sqrt[3]{6 + f(x)}$  
   (f) $\lim_{x \to a} \frac{2}{g(x)}$
2. Use the graphs of $f$ and $g$ in Figure Ex-2 to find the limits that exist:  
   (a) $\lim_{x \to 2} [f(x) + g(x)]$  
   (b) $\lim_{x \to 0} [f(x) + g(x)]$  
   (c) $\lim_{x \to 0^+} [f(x) + g(x)]$  
   (d) $\lim_{x \to 0^-} [f(x) + g(x)]$  
   (e) $\lim_{x \to 2} \frac{f(x)}{1 + g(x)}$  
   (f) $\lim_{x \to 2} \frac{1 + g(x)}{f(x)}$  
   (g) $\lim_{x \to 0^+} \sqrt{f(x)}$  
   (h) $\lim_{x \to 0^-} \sqrt{f(x)}$

**3–30 Find the limits.**

3. $\lim_{x \to 2} x(x - 1)(x + 1)$
4. $\lim_{x \to 3} (x^3 - 3x^2 + 9x)$
5. $\lim_{x \to 3} \frac{x^2 - 2x}{x + 1}$
6. $\lim_{x \to 0} \frac{6x - 9}{x^3 - 12x + 3}$
7. $\lim_{x \to 1^+} \frac{x^4 - 1}{x - 1}$
8. $\lim_{t \to -2} \frac{t^3 + 8}{t + 2}$
9. $\lim_{x \to -1} \frac{x^2 + 6x + 5}{x^2 - 3x - 4}$
10. $\lim_{x \to 2} \frac{x^2 - 4x + 4}{x^2 + x - 6}$
11. $\lim_{x \to -1} \frac{2x^2 + x - 1}{x + 1}$
12. $\lim_{x \to 1} \frac{3x^2 - x - 2}{2x^2 + x - 3}$
13. $\lim_{t \to 2} \frac{t^3 + 3t^2 - 12t + 4}{t^3 - 4t}$
14. $\lim_{t \to 1} \frac{t^3 + t^2 - 5t + 3}{t^3 - 3t + 2}$
15. $\lim_{x \to 3^+} \frac{x}{x - 3}$
16. $\lim_{x \to 3^-} \frac{x}{x - 3}$
17. $\lim_{x \to 3} \frac{x}{x - 3}$
18. $\lim_{x \to 2^+} \frac{x}{x^2 - 4}$
19. $\lim_{x \to 2^-} \frac{x}{x^2 - 4}$
20. $\lim_{x \to 2} \frac{x}{x^2 - 4}$
21. $\lim_{y \to 6^+} \frac{y + 6}{y^2 - 36}$
22. $\lim_{y \to 6^-} \frac{y + 6}{y^2 - 36}$
23. $\lim_{y \to 6} \frac{y + 6}{y^2 - 36}$
24. $\lim_{x \to 4^+} \frac{3 - x}{x^2 - 2x - 8}$
25. $\lim_{x \to 4^-} \frac{3 - x}{x^2 - 2x - 8}$
26. $\lim_{x \to 4} \frac{3 - x}{x^2 - 2x - 8}$
27. $\lim_{x \to 2^+} \frac{1}{|2 - x|}$
28. $\lim_{x \to 3^-} \frac{1}{|x - 3|}$
29. $\lim_{x \to 9} \frac{x - 9}{\sqrt{x} - 3}$
30. $\lim_{y \to 4} \frac{4 - y}{2 - \sqrt{y}}$

31. Let $f(x) = \begin{cases} x - 1, & x \le 3 \\ 3x - 7, & x > 3 \end{cases}$. Find: (a) $\lim_{x \to 3^-} f(x)$ (b) $\lim_{x \to 3^+} f(x)$ (c) $\lim_{x \to 3} f(x)$.
32. Let $g(t) = \begin{cases} t - 2, & t < 0 \\ t^2, & 0 \le t \le 2 \\ 2t, & t > 2 \end{cases}$. Find: (a) $\lim_{t \to 0} g(t)$ (b) $\lim_{t \to 1} g(t)$ (c) $\lim_{t \to 2} g(t)$.

**33–36 True–False Determine whether the statement is true or false. Explain your answer.**

33. If $\lim_{x \to a} f(x)$ and $\lim_{x \to a} g(x)$ exist, then so does $\lim_{x \to a} [f(x) + g(x)]$.
34. If $\lim_{x \to a} g(x) = 0$ and $\lim_{x \to a} f(x)$ exists, then $\lim_{x \to a} [f(x)/g(x)]$ does not exist.
35. If $\lim_{x \to a} f(x)$ and $\lim_{x \to a} g(x)$ both exist and are equal, then $\lim_{x \to a} [f(x)/g(x)] = 1$.
36. If $f(x)$ is a rational function and $x = a$ is in the domain of $f$, then $\lim_{x \to a} f(x) = f(a)$.

**37–38 First rationalize the numerator and then find the limit.**

37. $\lim_{x \to 0} \frac{\sqrt{x + 4} - 2}{x}$
38. $\lim_{x \to 0} \frac{\sqrt{x^2 + 4} - 2}{x}$

39. Let $f(x) = \frac{x^3 - 1}{x - 1}$.  
    (a) Find $\lim_{x \to 1} f(x)$.  
    (b) Sketch the graph of $y = f(x)$.
40. Let $f(x) = \begin{cases} \frac{x^2 - 9}{x + 3}, & x \neq -3 \\ k, & x = -3 \end{cases}$.  
    (a) Find $k$ so that $f(-3) = \lim_{x \to -3} f(x)$.  
    (b) With $k$ assigned this value, show that $f(x)$ can be expressed as a polynomial.

**FOCUS ON CONCEPTS**

41. (a) Explain why $\lim_{x \to 0^+} (1/x - 1/x^2) = +\infty - (+\infty) = 0$ is incorrect.  
    (b) Show that $\lim_{x \to 0^+} (1/x - 1/x^2) = -\infty$.
42. (a) Explain why $\lim_{x \to 0} \left(\frac{1}{x} - \frac{2}{x^2 + 2x}\right) = \lim_{x \to 0} \frac{1}{x}\left(1 - \frac{2}{x+2}\right) = \infty \cdot 0 = 0$ is incorrect.  
    (b) Show that $\lim_{x \to 0} \left(\frac{1}{x} - \frac{2}{x^2 + 2x}\right) = \frac{1}{2}$.
43. Find all values of $a$ such that $\lim_{x \to 1} \left(\frac{1}{x - 1} - \frac{a}{x^2 - 1}\right)$ exists and is finite.
44. (a) Explain informally why $\lim_{x \to 0^-} (1/x + 1/x^2) = +\infty$.  
    (b) Verify algebraically.
45. Let $p(x)$ and $q(x)$ be polynomials, with $q(x_0) = 0$. Discuss the behavior of $y = p(x)/q(x)$ near $x_0$.
46. If $\lim f(x)$ exists but $\lim [f(x) + g(x)]$ does not, prove $\lim g(x)$ does not exist.
47. If both $\lim f(x)$ and $\lim [f(x) + g(x)]$ exist, prove $\lim g(x)$ exists.
48. If $\lim g(x) = 0$ and $\lim [f(x)/g(x)]$ exists, prove $\lim f(x) = 0$.
49. **Writing.** Gravitational attraction as distance approaches zero.
50. **Writing.** Limits of functions equal except at finitely many points and algebraic simplification.

---

## 1.3 LIMITS AT INFINITY; END BEHAVIOR OF A FUNCTION

### LIMITS AT INFINITY AND HORIZONTAL ASYMPTOTES

* $\lim_{x \to +\infty} \frac{1}{x} = 0, \quad \lim_{x \to -\infty} \frac{1}{x} = 0$.
* If $\lim_{x \to +\infty} f(x) = L$ or $\lim_{x \to -\infty} f(x) = L$, the line $y = L$ is a **horizontal asymptote** for the graph of $f$.

> **Limit Laws for Limits at Infinity**  
> * $\lim_{x \to \pm\infty} [f(x)]^n = [\lim_{x \to \pm\infty} f(x)]^n$  
> * $\lim_{x \to \pm\infty} kf(x) = k\lim_{x \to \pm\infty} f(x)$  
> * $\lim_{x \to \pm\infty} k = k$  
> * $\lim_{x \to \pm\infty} \frac{1}{x^n} = 0$ for positive integer $n$.

### END BEHAVIOR OF POLYNOMIALS AND RATIONAL FUNCTIONS

* **Polynomials:**
  $$\lim_{x \to \pm\infty} (c_0 + c_1x + \dots + c_n x^n) = \lim_{x \to \pm\infty} c_n x^n$$
* **Rational Functions:**
  $$\lim_{x \to \pm\infty} \frac{c_0 + c_1x + \dots + c_n x^n}{d_0 + d_1x + \dots + d_m x^m} = \lim_{x \to \pm\infty} \frac{c_n x^n}{d_m x^m}$$

#### Examples
* $\lim_{x \to +\infty} \frac{3x + 5}{6x - 8} = \lim_{x \to +\infty} \frac{3 + 5/x}{6 - 8/x} = \frac{1}{2}$
* $\lim_{x \to -\infty} \frac{4x^2 - x}{2x^3 - 5} = \lim_{x \to -\infty} \frac{4/x - 1/x^2}{2 - 5/x^3} = 0$
* $\lim_{x \to +\infty} \frac{5x^3 - 2x^2 + 1}{1 - 3x} = -\infty$
* $\lim_{x \to +\infty} \frac{\sqrt{x^2 + 2}}{3x - 6} = \frac{1}{3}, \quad \lim_{x \to -\infty} \frac{\sqrt{x^2 + 2}}{3x - 6} = -\frac{1}{3}$
* $\lim_{x \to +\infty} (\sqrt{x^6 + 5} - x^3) = 0, \quad \lim_{x \to +\infty} (\sqrt{x^6 + 5x^3} - x^3) = \frac{5}{2}$
* Trigonometric functions $\sin x, \cos x$ oscillate and have no limit at $\pm\infty$.

---

### QUICK CHECK EXERCISES 1.3
*(See page 80 for answers.)*

1. Find the limits:  
   (a) $\lim_{x \to +\infty} (-2x) = \underline{\hspace{1cm}}$  
   (b) $\lim_{x \to -\infty} \frac{x}{|x|} = \underline{\hspace{1cm}}$  
   (c) $\lim_{x \to -\infty} (3 - x) = \underline{\hspace{1cm}}$  
   (d) $\lim_{x \to +\infty} (5 - 1/x) = \underline{\hspace{1cm}}$
2. Find the limits that exist:  
   (a) $\lim_{x \to -\infty} \frac{2x^2 + x}{4x^2 - 3} = \underline{\hspace{1cm}}$  
   (b) $\lim_{x \to +\infty} \frac{1}{2 + \sin x} = \underline{\hspace{1cm}}$
3. Given that $\lim_{x \to +\infty} f(x) = 2$ and $\lim_{x \to +\infty} g(x) = -3$, find:  
   (a) $\lim_{x \to +\infty} [3f(x) - g(x)] = \underline{\hspace{1cm}}$  
   (b) $\lim_{x \to +\infty} \frac{f(x)}{g(x)} = \underline{\hspace{1cm}}$  
   (c) $\lim_{x \to +\infty} \frac{2f(x) + 3g(x)}{3f(x) + 2g(x)} = \underline{\hspace{1cm}}$  
   (d) $\lim_{x \to +\infty} \sqrt{10 - f(x)g(x)} = \underline{\hspace{1cm}}$
4. Consider the graphs of $y = 1/(x + 1), y = x/(x + 1),$ and $y = x^2/(x + 1)$. Which of these graphs has a horizontal asymptote?

#### QUICK CHECK ANSWERS 1.3
1. (a) $-\infty$ (b) $-1$ (c) $+\infty$ (d) $5$  
2. (a) $\frac{1}{2}$ (b) does not exist  
3. (a) $9$ (b) $-\frac{2}{3}$ (c) does not exist (d) $4$  
4. The graphs of $y = 1/(x + 1)$ and $y = x/(x + 1)$ have horizontal asymptotes.

---

### EXERCISE SET 1.3

**1–4 In these exercises, make reasonable assumptions about the end behavior of the indicated function.**

1. For the function $g$ in Figure Ex-1, find: (a) $\lim_{x \to -\infty} g(x)$ (b) $\lim_{x \to +\infty} g(x)$.
2. For the function $\phi$ in Figure Ex-2, find: (a) $\lim_{x \to -\infty} \phi(x)$ (b) $\lim_{x \to +\infty} \phi(x)$.
3. For the function $\phi$ in Figure Ex-3, find: (a) $\lim_{x \to -\infty} \phi(x)$ (b) $\lim_{x \to +\infty} \phi(x)$.
4. For the function $G$ in Figure Ex-4, find: (a) $\lim_{x \to -\infty} G(x)$ (b) $\lim_{x \to +\infty} G(x)$.

5. Given $\lim_{x \to +\infty} f(x) = 3, \lim_{x \to +\infty} g(x) = -5, \lim_{x \to +\infty} h(x) = 0$, find:  
   (a) $\lim_{x \to +\infty} [f(x) + 3g(x)]$  
   (b) $\lim_{x \to +\infty} [h(x) - 4g(x) + 1]$  
   (c) $\lim_{x \to +\infty} [f(x)g(x)]$  
   (d) $\lim_{x \to +\infty} [g(x)]^2$  
   (e) $\lim_{x \to +\infty} \sqrt[3]{5 + f(x)}$  
   (f) $\lim_{x \to +\infty} \frac{3}{g(x)}$  
   (g) $\lim_{x \to +\infty} \frac{3h(x) + 4}{x^2}$  
   (h) $\lim_{x \to +\infty} \frac{6f(x)}{5f(x) + 3g(x)}$
6. Given $\lim_{x \to -\infty} f(x) = 7, \lim_{x \to -\infty} g(x) = -6$, find:  
   (a) $\lim_{x \to -\infty} [2f(x) - g(x)]$  
   (b) $\lim_{x \to -\infty} [6f(x) + 7g(x)]$  
   (c) $\lim_{x \to -\infty} [x^2 + g(x)]$  
   (d) $\lim_{x \to -\infty} [x^2 g(x)]$  
   (e) $\lim_{x \to -\infty} \sqrt[3]{f(x)g(x)}$  
   (f) $\lim_{x \to -\infty} \frac{g(x)}{f(x)}$  
   (g) $\lim_{x \to -\infty} [f(x) + \frac{g(x)}{x}]$  
   (h) $\lim_{x \to -\infty} \frac{xf(x)}{(2x + 3)g(x)}$

7. Complete the table and guess $\lim_{x \to +\infty} \frac{\sqrt{x^2 + x}}{x + 1}$ for $x = 10, 100, 1000, 10000, 100000, 1000000$.
8. Complete the table and guess $\lim_{x \to -\infty} \frac{\sqrt{x^2 + x}}{x + 1}$ for $x = -10, -100, -1000, -10000, -100000, -1000000$.

**9–32 Find the limits.**

9. $\lim_{x \to +\infty} (1 + 2x - 3x^5)$
10. $\lim_{x \to +\infty} (2x^3 - 100x + 5)$
11. $\lim_{x \to +\infty} \sqrt{x}$
12. $\lim_{x \to -\infty} \sqrt{5 - x}$
13. $\lim_{x \to +\infty} \frac{3x + 1}{2x - 5}$
14. $\lim_{x \to +\infty} \frac{5x^2 - 4x}{2x^2 + 3}$
15. $\lim_{y \to -\infty} \frac{3}{y + 4}$
16. $\lim_{x \to +\infty} \frac{1}{x - 12}$
17. $\lim_{x \to -\infty} \frac{x - 2}{x^2 + 2x + 1}$
18. $\lim_{x \to +\infty} \frac{5x^2 + 7}{3x^2 - x}$
19. $\lim_{x \to +\infty} \frac{7 - 6x^5}{x + 3}$
20. $\lim_{t \to -\infty} \frac{5 - 2t^3}{t^2 + 1}$
21. $\lim_{t \to +\infty} \frac{6 - t^3}{7t^3 + 3}$
22. $\lim_{x \to -\infty} \frac{x + 4x^3}{1 - x^2 + 7x^3}$
23. $\lim_{x \to +\infty} \sqrt[3]{\frac{2 + 3x - 5x^2}{1 + 8x^2}}$
24. $\lim_{s \to +\infty} \sqrt[3]{\frac{3s^7 - 4s^5}{2s^7 + 1}}$
25. $\lim_{x \to -\infty} \frac{\sqrt{5x^2 - 2}}{x + 3}$
26. $\lim_{x \to +\infty} \frac{\sqrt{5x^2 - 2}}{x + 3}$
27. $\lim_{y \to -\infty} \frac{2 - y}{\sqrt{7 + 6y^2}}$
28. $\lim_{y \to +\infty} \frac{2 - y}{\sqrt{7 + 6y^2}}$
29. $\lim_{x \to -\infty} \frac{\sqrt{3x^4 + x}}{x^2 - 8}$
30. $\lim_{x \to +\infty} \frac{\sqrt{3x^4 + x}}{x^2 - 8}$
31. $\lim_{x \to +\infty} (\sqrt{x^2 + 3} - x)$
32. $\lim_{x \to +\infty} (\sqrt{x^2 - 3x} - x)$

**33–36 True–False Determine whether the statement is true or false. Explain your answer.**

33. By subtraction, $\lim_{x \to +\infty} (x^2 - 1000x) = \infty - \infty = 0$.
34. If $y = L$ is a horizontal asymptote for $y = f(x)$, then $\lim_{x \to -\infty} f(x) = L$ and $\lim_{x \to +\infty} f(x) = L$.
35. If $y = L$ is a horizontal asymptote for $y = f(x)$, then it is possible for the graph of $f$ to intersect the line $y = L$ infinitely many times.
36. If a rational function $p(x)/q(x)$ has a horizontal asymptote, then the degree of $p(x)$ must equal the degree of $q(x)$.

**FOCUS ON CONCEPTS**

37. Relativistic vs classical velocity under constant acceleration: $v = n(t)$ vs $v = e(t)$.
38. Baked potato cooling curve: physical meaning of $\lim_{t \to 0^+} f(t)$ and $\lim_{t \to +\infty} f(t)$.
39. Piecewise limits at infinity: $f(x) = \begin{cases} 2x^2 + 5, & x < 0 \\ \frac{3 - 5x^3}{1 + 4x + x^3}, & x \ge 0 \end{cases}$.
40. Piecewise limits at infinity: $g(t) = \begin{cases} \frac{2 + 3t}{5t^2 + 6}, & t < 1,000,000 \\ \frac{\sqrt{36t^2 - 100}}{5 - t}, & t > 1,000,000 \end{cases}$.
41. Limits of $p(x) = (1 - x)^n$ as $x \to \pm\infty$ for positive integer $n$.
42. Polynomials with specific limit ratios at infinity.
43. Asymptotes of the six trigonometric functions.
44. Degree analysis of general rational functions at infinity.
45–46. Substitution principle for limits at infinity: $\lim_{x \to +\infty} f(g(x)) = \lim_{t \to +\infty} f(t)$ if $g(x) \to +\infty$.
47–50. Evaluating limits with given $\lim_{x \to -\infty} f(x) = 0$ and $\lim_{x \to +\infty} f(x) = +\infty$.
51–55. Curvilinear and oblique asymptotes: $f(x) = \frac{x^2 - 2}{x - 2}, \frac{x^3 - x + 3}{x}, \frac{-x^3 + 3x^2 + x - 1}{x - 3}, \frac{x^5 - x^3 + 3}{x^2 - 1}, \sin x + \frac{1}{x - 1}$.
56. **Writing.** Skill learning curves and maximum limits.
57. **Writing.** Carrying capacity $L$ ecological population models.

---

## 1.4 LIMITS (DISCUSSED MORE RIGOROUSLY)

### MOTIVATION & PRECISE DEFINITIONS

> **1.4.1 LIMIT DEFINITION ($\epsilon$-$\delta$)**  
> Let $f(x)$ be defined for all $x$ in some open interval containing $a$, except possibly at $a$. We write
> $$\lim_{x \to a} f(x) = L$$
> if given any number $\epsilon > 0$, we can find a number $\delta > 0$ such that
> $$|f(x) - L| < \epsilon \quad \text{if} \quad 0 < |x - a| < \delta$$

> **Karl Weierstrass (1815–1897)**  
> German mathematician who developed the rigorous epsilon-delta foundation of mathematical analysis.

> **1.4.2 & 1.4.3 LIMITS AT INFINITY**  
> * $\lim_{x \to +\infty} f(x) = L \iff \forall \epsilon > 0, \exists N > 0 \text{ s.t. } |f(x) - L| < \epsilon \text{ if } x > N$.  
> * $\lim_{x \to -\infty} f(x) = L \iff \forall \epsilon > 0, \exists N < 0 \text{ s.t. } |f(x) - L| < \epsilon \text{ if } x < N$.

> **1.4.4 & 1.4.5 INFINITE LIMITS**  
> * $\lim_{x \to a} f(x) = +\infty \iff \forall M > 0, \exists \delta > 0 \text{ s.t. } f(x) > M \text{ if } 0 < |x - a| < \delta$.  
> * $\lim_{x \to a} f(x) = -\infty \iff \forall M < 0, \exists \delta > 0 \text{ s.t. } f(x) < M \text{ if } 0 < |x - a| < \delta$.

#### Example 1
Use Definition 1.4.1 to prove $\lim_{x \to 2} (3x - 5) = 1$.  
**Solution.** $|(3x - 5) - 1| = 3|x - 2| < \epsilon \iff |x - 2| < \epsilon/3$. Choose $\delta = \epsilon/3$.

#### Example 2
Prove $\lim_{x \to 0^+} \sqrt{x} = 0$.  
**Solution.** $|\sqrt{x} - 0| < \epsilon \iff 0 < x < \epsilon^2$. Choose $\delta = \epsilon^2$.

#### Example 3
Prove $\lim_{x \to 3} x^2 = 9$.  
**Solution.** $|x^2 - 9| = |x + 3||x - 3|$. Assuming $\delta \le 1$, $|x - 3| < 1 \implies 5 < x + 3 < 7 \implies |x + 3| < 7$. Thus $|x^2 - 9| < 7|x - 3| < \epsilon$. Choose $\delta = \min(1, \epsilon/7)$.

#### Example 4
Prove $\lim_{x \to +\infty} \frac{1}{x} = 0$. Choose $N = 1/\epsilon$.

#### Example 5
Prove $\lim_{x \to 0} \frac{1}{x^2} = +\infty$. Choose $\delta = 1/\sqrt{M}$.

---

### QUICK CHECK EXERCISES 1.4
*(See page 90 for answers.)*

1. The definition of a two-sided limit states: $\lim_{x \to a} f(x) = L$ if given any number $\underline{\hspace{1cm}}$ there is a number $\underline{\hspace{1cm}}$ such that $|f(x) - L| < \epsilon$ if $\underline{\hspace{1.5cm}}$.
2. Suppose that $f(x)$ is a function such that for any given $\epsilon > 0$, the condition $0 < |x - 1| < \epsilon/2$ guarantees that $|f(x) - 5| < \epsilon$. What limit results from this property?
3. Suppose that $\epsilon$ is any positive number. Find the largest value of $\delta$ such that $|5x - 10| < \epsilon$ if $0 < |x - 2| < \delta$.
4. The definition of limit at $+\infty$ states: $\lim_{x \to +\infty} f(x) = L$ if given any number $\underline{\hspace{1cm}}$ there is a positive number $\underline{\hspace{1cm}}$ such that $|f(x) - L| < \epsilon$ if $\underline{\hspace{1cm}}$.
5. Find the smallest positive number $N$ such that for each $x > N$, the value of $f(x) = 1/\sqrt{x}$ is within 0.01 of 0.

#### QUICK CHECK ANSWERS 1.4
1. $\epsilon > 0; \ \delta > 0; \ 0 < |x - a| < \delta$  
2. $\lim_{x \to 1} f(x) = 5$  
3. $\delta = \epsilon/5$  
4. $\epsilon > 0; \ N; \ x > N$  
5. $N = 10,000$

---

### EXERCISE SET 1.4

1. (a) Open interval around 0 for $f(x) = x + 2$ within $0.1$ of 2.  
   (b) Open interval around 3 for $f(x) = 4x - 5$ within $0.01$ of 7.  
   (c) Open interval around 4 for $f(x) = x^2$ within $0.001$ of 16.
2. Open interval around 0 for $f(x) = 2x + 3$ within $\epsilon$ of 3: (a) $\epsilon = 0.1$ (b) $\epsilon = 0.01$ (c) $\epsilon = 0.0012$.
3. Values of $x_0, x_1$ and $\delta$ for $|\sqrt{x} - 2| < 0.05$ on $0 < |x - 4| < \delta$.
4. Values of $x_0, x_1$ and $\delta$ for $|1/x - 1| < 0.1$ on $0 < |x - 1| < \delta$.
5. Finding $\delta$ for $|(x^3 - 4x + 5) - 2| < 0.05$ when $0 < |x - 1| < \delta$.
6. Finding $\delta$ for $|\sqrt{5x + 1} - 4| < 0.5$ when $0 < |x - 3| < \delta$.
7. Graphing utility trace to find $\delta$ for $f(x) = x + \sqrt{x}$ at $x = 1, \epsilon = 0.2$.
8. Graphing utility trace to find $\delta$ for $f(x) = (\sin 2x)/x$ at $x = 0, \epsilon = 0.1$.

**9–16 Find $\delta$ such that $|f(x) - L| < \epsilon$ if $0 < |x - a| < \delta$:**

9. $\lim_{x \to 4} 2x = 8; \ \epsilon = 0.1$
10. $\lim_{x \to 3} (5x - 2) = 13; \ \epsilon = 0.01$
11. $\lim_{x \to 3} \frac{x^2 - 9}{x - 3} = 6; \ \epsilon = 0.05$
12. $\lim_{x \to -1/2} \frac{4x^2 - 1}{2x + 1} = -2; \ \epsilon = 0.05$
13. $\lim_{x \to 2} x^3 = 8; \ \epsilon = 0.001$
14. $\lim_{x \to 4} \sqrt{x} = 2; \ \epsilon = 0.001$
15. $\lim_{x \to 5} \frac{1}{x} = \frac{1}{5}; \ \epsilon = 0.05$
16. $\lim_{x \to 0} |x| = 0; \ \epsilon = 0.05$

**17–26 Use Definition 1.4.1 to prove that the limit is correct:**

17. $\lim_{x \to 2} 3 = 3$
18. $\lim_{x \to 4} (x + 2) = 6$
19. $\lim_{x \to 5} 3x = 15$
20. $\lim_{x \to -1} (7x + 5) = -2$
21. $\lim_{x \to 0} \frac{2x^2 + x}{x} = 1$
22. $\lim_{x \to -3} \frac{x^2 - 9}{x + 3} = -6$
23. $\lim_{x \to 1} f(x) = 3$, where $f(x) = \begin{cases} x + 2, & x \neq 1 \\ 10, & x = 1 \end{cases}$
24. $\lim_{x \to 2} f(x) = 5$, where $f(x) = \begin{cases} 9 - 2x, & x \neq 2 \\ 49, & x = 2 \end{cases}$
25. $\lim_{x \to 0} |x| = 0$
26. $\lim_{x \to 2} f(x) = 5$, where $f(x) = \begin{cases} 9 - 2x, & x < 2 \\ 3x - 1, & x > 2 \end{cases}$

**FOCUS ON CONCEPTS**

27. Definitions of $\lim_{x \to a^+} f(x) = L$ and $\lim_{x \to a^-} f(x) = L$.
28. Equivalence of $\lim_{x \to a} |f(x) - L| = 0$ and $\lim_{x \to a} f(x) = L$.
29. Proof that $\lim_{x \to 10} (3x^2 + 2x - 20) = 300$.
30. Proof that $\lim_{x \to 2} \frac{28}{3x + 1} = 4$.

**31–36 Use Definition 1.4.1 with bounded factors:**

31. $\lim_{x \to 1} 2x^2 = 2$
32. $\lim_{x \to 3} (x^2 + x) = 12$
33. $\lim_{x \to -2} \frac{1}{x + 1} = -1$
34. $\lim_{x \to 1/2} \frac{2x + 3}{x} = 8$
35. $\lim_{x \to 4} \sqrt{x} = 2$
36. $\lim_{x \to 2} x^3 = 8$

37. Prove $\lim_{x \to 0} f(x) = 0$ for $f(x) = \begin{cases} 0, & x \text{ rational} \\ x, & x \text{ irrational} \end{cases}$.
38. Prove $\lim_{x \to 0} f(x)$ does not exist for $f(x) = \begin{cases} 0, & x \text{ rational} \\ 1, & x \text{ irrational} \end{cases}$.
39. Finding $N$ for limits at infinity ($1/x^2, x/(x + 1), 1/x^3$).
40. Finding $N$ for $f(x) = 1/x^3$ within $\epsilon$ of 0.
41–42. $N$-$\epsilon$ proofs for $y = \frac{x^2}{1 + x^2}$ and $y = 1/\sqrt[3]{x}$.
43–50. Finding $N$ for given $\epsilon$ as $x \to \pm\infty$.
51–56. Proving limits at $\pm\infty$ using Definitions 1.4.2/1.4.3 ($1/x^2, 1/(x + 2), \frac{4x - 1}{2x + 5}, \frac{x}{x + 1}, \frac{2\sqrt{x}}{\sqrt{x} - 1}, \frac{\sqrt[3]{x}}{\sqrt[3]{x} + 2}$).
57–58. Intervals where $f(x) > M$ or $f(x) < -M$.
59–64. Rigorous proofs of infinite limits using Definitions 1.4.4/1.4.5.
65–70. Rigorous proofs of one-sided limits.
71–74. Rigorous proofs of infinite limits from the left/right and at infinity.
75. Ohm's law and current variations: $I = V/R$ with $V = 3.0\text{ V}, R = 7.5\,\Omega$.
76–77. **Writing.** Comparison between informal and rigorous epsilon-delta limit definitions.

---

## 1.5 CONTINUITY

### DEFINITION & PROPERTIES OF CONTINUITY

> **1.5.1 DEFINITION**  
> A function $f$ is **continuous at $x = c$** provided:  
> 1. $f(c)$ is defined.  
> 2. $\lim_{x \to c} f(x)$ exists.  
> 3. $\lim_{x \to c} f(x) = f(c)$.

> **1.5.2 DEFINITION (Continuity on Closed Interval $[a, b]$)**  
> 1. $f$ is continuous on $(a, b)$.  
> 2. $\lim_{x \to a^+} f(x) = f(a)$.  
> 3. $\lim_{x \to b^-} f(x) = f(b)$.

> **1.5.3 THEOREM**  
> If $f$ and $g$ are continuous at $c$, then $f + g, f - g, fg$ are continuous at $c$, and $f/g$ is continuous at $c$ if $g(c) \neq 0$.

> **1.5.4 THEOREM**  
> (a) Polynomials are continuous everywhere.  
> (b) Rational functions are continuous everywhere except at zeros of the denominator.

> **1.5.5 THEOREM**  
> If $\lim_{x \to c} g(x) = L$ and $f$ is continuous at $L$, then $\lim_{x \to c} f(g(x)) = f(\lim_{x \to c} g(x)) = f(L)$.

> **1.5.6 THEOREM (Continuity of Compositions)**  
> If $g$ is continuous at $c$ and $f$ is continuous at $g(c)$, then $f \circ g$ is continuous at $c$. If both are continuous everywhere, $f \circ g$ is continuous everywhere.

> **1.5.7 THEOREM (Continuity of Inverse Functions)**  
> The inverse of a continuous one-to-one function is continuous.

> **1.5.8 THEOREM (Intermediate-Value Theorem)**  
> If $f$ is continuous on $[a, b]$ and $k$ is between $f(a)$ and $f(b)$, then there is at least one $x \in [a, b]$ such that $f(x) = k$.

> **1.5.9 THEOREM (Intermediate-Value Theorem for Zeroes)**  
> If $f$ is continuous on $[a, b]$ and $f(a)$ and $f(b)$ have opposite signs, then $f(x) = 0$ has at least one solution in $(a, b)$.

#### Examples 1 to 6
* $f(x) = \frac{x^2 - 4}{x - 2}$ (discontinuous at $x = 2$), $g(x) = \begin{cases} \frac{x^2 - 4}{x - 2}, & x \neq 2 \\ 3, & x = 2 \end{cases}$ (discontinuous), $h(x) = \begin{cases} \frac{x^2 - 4}{x - 2}, & x \neq 2 \\ 4, & x = 2 \end{cases}$ (continuous at $x = 2$).
* $f(x) = \sqrt{9 - x^2}$ is continuous on $[-3, 3]$.
* $y = \frac{x^2 - 9}{x^2 - 5x + 6}$ has discontinuities at $x = 2$ and $x = 3$.
* $f(x) = |x|$ is continuous everywhere.
* $f(x) = x^3 + x$ is one-to-one and continuous $\implies f^{-1}$ is continuous on $(-\infty, +\infty)$.
* Root approximation of $x^3 - x - 1 = 0$ on $[1, 2]$ to two decimal places: $x_0 \approx 1.325$.

---

### QUICK CHECK EXERCISES 1.5
*(See page 101 for answers.)*

1. What three conditions are satisfied if $f$ is continuous at $x = c$?
2. Suppose that $f$ and $g$ are continuous functions such that $f(2) = 1$ and $\lim_{x \to 2} [f(x) + 4g(x)] = 13$. Find (a) $g(2)$ (b) $\lim_{x \to 2} g(x)$.
3. Suppose that $f$ and $g$ are continuous functions such that $\lim_{x \to 3} g(x) = 5$ and $f(3) = -2$. Find $\lim_{x \to 3} [f(x)/g(x)]$.
4. For what values of $x$, if any, is the function $f(x) = \frac{x^2 - 16}{x^2 - 5x + 4}$ discontinuous?
5. Suppose that $f$ is continuous everywhere with $f(-2) = 3, f(-1) = -1, f(0) = -4, f(1) = 1, f(2) = 5$. Does the Intermediate-Value Theorem guarantee a root on:  
   (a) $[-2, -1]$ (b) $[-1, 0]$ (c) $[-1, 1]$ (d) $[0, 2]$?

#### QUICK CHECK ANSWERS 1.5
1. $f(c)$ is defined; $\lim_{x \to c} f(x)$ exists; $\lim_{x \to c} f(x) = f(c)$  
2. (a) $3$ (b) $3$  
3. $-2/5$  
4. $x = 1, 4$  
5. (a) yes (b) no (c) yes (d) yes

---

### EXERCISE SET 1.5

1–4. Intervals of continuity from graphs.
5. Functions $f(x) = \begin{cases} 1, & x \neq 4 \\ -1, & x = 4 \end{cases}$ and $g(x) = \begin{cases} 4x - 10, & x \neq 4 \\ -6, & x = 4 \end{cases}$: continuity at $x = 4$ of $f, g, -g, |f|, fg, g \circ f, g - 6f$.
6. Functions $f(x) = \begin{cases} 1, & 0 \le x \\ 0, & x < 0 \end{cases}$ and $g(x) = \begin{cases} 0, & 0 \le x \\ 1, & x < 0 \end{cases}$: continuity at $x = 0$ of $f, g, f(-x), |g|, fg, g \circ f, f + g$.
7. Graphs satisfying specified continuity/one-sided continuity conditions.
8. Bloodstream medication concentration discontinuities.
9. Parking lot fee step function.
10. Continuous vs discontinuous real-world quantities (population, height, taxi fare, melting ice).

**11–22 Find values of $x$, if any, at which $f$ is not continuous.**

11. $f(x) = 5x^4 - 3x + 7$
12. $f(x) = \sqrt[3]{x - 8}$
13. $f(x) = \frac{x + 2}{x^2 + 4}$
14. $f(x) = \frac{x + 2}{x^2 - 4}$
15. $f(x) = \frac{x}{2x^2 + x}$
16. $f(x) = \frac{2x + 1}{4x^2 + 4x + 5}$
17. $f(x) = \frac{3}{x} + \frac{x - 1}{x^2 - 1}$
18. $f(x) = \frac{5}{x} + \frac{2x}{x + 4}$
19. $f(x) = \frac{x^2 + 6x + 9}{|x| + 3}$
20. $f(x) = |4 - \frac{8}{x^4 + x}|$
21. $f(x) = \begin{cases} 2x + 3, & x \le 4 \\ 7 + 16/x, & x > 4 \end{cases}$
22. $f(x) = \begin{cases} \frac{3}{x - 1}, & x \neq 1 \\ 3, & x = 1 \end{cases}$

**23–28 True–False Determine whether the statement is true or false. Explain your answer.**

23. If $f(x)$ is continuous at $x = c$, then so is $|f(x)|$.
24. If $|f(x)|$ is continuous at $x = c$, then so is $f(x)$.
25. If $f$ and $g$ are discontinuous at $x = c$, then so is $f + g$.
26. If $f$ and $g$ are discontinuous at $x = c$, then so is $fg$.
27. If $\sqrt{f(x)}$ is continuous at $x = c$, then so is $f(x)$.
28. If $f(x)$ is continuous at $x = c$, then so is $\sqrt{f(x)}$.

**29–30 Find constant $k$ to make $f$ continuous everywhere:**

29. (a) $f(x) = \begin{cases} 7x - 2, & x \le 1 \\ kx^2, & x > 1 \end{cases}$  
    (b) $f(x) = \begin{cases} kx^2, & x \le 2 \\ 2x + k, & x > 2 \end{cases}$
30. (a) $f(x) = \begin{cases} 9 - x^2, & x \ge -3 \\ k/x^2, & x < -3 \end{cases}$  
    (b) $f(x) = \begin{cases} 9 - x^2, & x \ge 0 \\ k/x^2, & x < 0 \end{cases}$

31. Find $k, m$ to make $f$ continuous everywhere:
    $$f(x) = \begin{cases} x^2 + 5, & x > 2 \\ m(x + 1) + k, & -1 < x \le 2 \\ 2x^3 + x + 7, & x \le -1 \end{cases}$$
32. Continuity intervals for $f(x) = \frac{1}{\sqrt{x - 2}}$.
33–34. Removable discontinuities and redefining values at points.
35–36. Identifying removable vs nonremovable discontinuities.
37–38. Graphing utility and IVT approximations for rational discontinuities.
39. Proof that $x^{3/5}$ is continuous everywhere.
40. Proof that $1/\sqrt{x^4 + 7x^2 + 1}$ is continuous everywhere.
41. Proof of Theorem 1.5.3 (a), (b), (c).
42. Proof of Theorem 1.5.4(b).
43. Continuity characterization: $f$ continuous at $c \iff \lim_{h \to 0} f(c + h) = f(c)$.
44. If $f, g$ continuous on $[a, b]$ with $f(a) > g(a), f(b) < g(b)$, then $f(x) = g(x)$ has a solution in $(a, b)$.

**FOCUS ON CONCEPTS**

45. Counterexample to IVT if $f$ is not continuous.
46. Checking IVT hypotheses and conclusions.
47. Solution existence for $x^3 + x^2 - 2x = 1$ on $[-1, 1]$.
48. Odd-degree polynomials have at least one real root.
49–50. Approximating roots of $x^4 + x - 1 = 0$ and $5 - x - x^4 = 0$ via IVT.
51. Approximating $\sqrt{5}$ via $x^2 - 5 = 0$.
52. Sprinter stopwatch problem.
53. Antipodal equatorial temperature theorem.
54–55. Elliptical region area bisection theorem.
56. Fixed-point theorem: continuous $f: [0, 1] \to [0, 1]$ has $f(c) = c$.
57. Invertibility of $f(x) = x^6 + 3x + 5, x \ge 0$.
58. Limit of inverse function $\lim_{x \to 0} \frac{x}{f^{-1}(x)} = L$.
59–60. **Writing.** Physical continuity assumptions and existence theorems.

---

## 1.6 CONTINUITY OF TRIGONOMETRIC FUNCTIONS

### CONTINUITY AND SQUEEZING THEOREM

> **1.6.1 THEOREM**  
> The six basic trigonometric functions are continuous on their natural domains:
> $$\lim_{x \to c} \sin x = \sin c, \quad \lim_{x \to c} \cos x = \cos c, \quad \lim_{x \to c} \tan x = \tan c$$
> $$\lim_{x \to c} \csc x = \csc c, \quad \lim_{x \to c} \sec x = \sec c, \quad \lim_{x \to c} \cot x = \cot c$$

> **1.6.2 THEOREM (The Squeezing Theorem)**  
> Let $f, g, h$ satisfy $g(x) \le f(x) \le h(x)$ on an open interval containing $c$ (except possibly at $c$). If $\lim_{x \to c} g(x) = \lim_{x \to c} h(x) = L$, then
> $$\lim_{x \to c} f(x) = L$$

> **1.6.3 THEOREM**  
> (a) $\lim_{x \to 0} \frac{\sin x}{x} = 1$  
> (b) $\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$

**Proof of (a).** For $0 < x < \pi/2$, area of sector $\frac{1}{2}x$ is between area of inner triangle $\frac{1}{2}\sin x$ and outer triangle $\frac{1}{2}\tan x$:
$$\cos x \le \frac{\sin x}{x} \le 1$$
Since $\lim_{x \to 0} \cos x = 1$ and $\lim_{x \to 0} 1 = 1$, by Squeezing Theorem $\lim_{x \to 0} \frac{\sin x}{x} = 1$. $\blacksquare$

#### Example 1 to 3
* $\lim_{x \to 1} \cos\left(\frac{x^2 - 1}{x - 1}\right) = \cos 2$
* $\lim_{x \to 0} \frac{\tan x}{x} = 1, \quad \lim_{\theta \to 0} \frac{\sin 2\theta}{\theta} = 2, \quad \lim_{x \to 0} \frac{\sin 3x}{\sin 5x} = \frac{3}{5}$
* $\lim_{x \to 0} \sin(1/x)$ does not exist; $\lim_{x \to 0} x\sin(1/x) = 0$ via Squeezing Theorem.

---

### QUICK CHECK EXERCISES 1.6
*(See page 107 for answers.)*

1. Is $f$ continuous on $[0, \pi/2)$: (a) $\sin x$ (yes) (b) $\cos x$ (yes) (c) $\tan x$ (yes) (d) $\csc x$ (no).
2. (a) $\lim_{x \to 0} \frac{\sin x}{x} = 1$ (b) $\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$.
3. If $3 - |x| \le f(x) \le 3 + |x|$, then $f(x) \to 3$ as $x \to 0$.

#### QUICK CHECK ANSWERS 1.6
1. (a) yes (b) yes (c) yes (d) no  
2. (a) $1$ (b) $0$  
3. $3; \ 0$

---

### EXERCISE SET 1.6

**1–8 Find the discontinuities, if any.**

1. $f(x) = \sin(x^2 - 2)$
2. $f(x) = \cos\left(\frac{x}{x - \pi}\right)$
3. $f(x) = |\cot x|$
4. $f(x) = \sec x$
5. $f(x) = \csc x$
6. $f(x) = \frac{1}{1 + \sin^2 x}$
7. $f(x) = \frac{1}{1 - 2\sin x}$
8. $f(x) = \sqrt{2 + \tan^2 x}$

**9–10 Show that the function is continuous everywhere.**

9. (a) $\sin(x^3 + 7x + 1)$ (b) $|\sin x|$ (c) $\cos^3(x + 1)$
10. (a) $|3 + \sin 2x|$ (b) $\sin(\sin x)$ (c) $\cos^5 x - 2\cos^3 x + 1$

**11–32 Find the limits.**

11. $\lim_{x \to +\infty} \cos(1/x)$
12. $\lim_{x \to +\infty} \sin\left(\frac{\pi x}{2 - 3x}\right)$
13. $\lim_{\theta \to 0} \frac{\sin 3\theta}{\theta}$
14. $\lim_{h \to 0} \frac{\sin h}{2h}$
15. $\lim_{x \to 0} \frac{x^2 - 3\sin x}{x}$
16. $\lim_{x \to 0} \frac{2 - \cos 3x - \cos 4x}{x}$
17. $\lim_{\theta \to 0^+} \frac{\sin\theta}{\theta^2}$
18. $\lim_{\theta \to 0} \frac{\sin^2\theta}{\theta}$
19. $\lim_{x \to 0} \frac{\tan 7x}{\sin 3x}$
20. $\lim_{x \to 0} \frac{\sin 6x}{\sin 8x}$
21. $\lim_{x \to 0^+} \frac{\sin x}{5\sqrt{x}}$
22. $\lim_{x \to 0} \frac{\sin^2 x}{3x^2}$
23. $\lim_{x \to 0} \frac{\sin x^2}{x}$
24. $\lim_{h \to 0} \frac{\sin h}{1 - \cos h}$
25. $\lim_{t \to 0} \frac{t^2}{1 - \cos^2 t}$
26. $\lim_{x \to 0} \frac{x}{\cos(\frac{1}{2}\pi - x)}$
27. $\lim_{\theta \to 0} \frac{\theta^2}{1 - \cos\theta}$
28. $\lim_{h \to 0} \frac{1 - \cos 3h}{\cos^2 5h - 1}$
29. $\lim_{x \to 0^+} \sin(1/x)$
30. $\lim_{x \to 0} \frac{\tan 3x^2 + \sin^2 5x}{x^2}$
31. $\lim_{x \to 0} \frac{\tan ax}{\sin bx} \ (a \neq 0, b \neq 0)$
32. $\lim_{x \to 0} \frac{\sin^2(kx)}{x} \ (k \neq 0)$

**33–34 Complete the table and find the exact value of the limit.**

33. $f(x) = \frac{\sin(x - 5)}{x^2 - 25}; \quad \lim_{x \to 5} f(x)$  
    $x: 4, 4.5, 4.9, 5.1, 5.5, 6$
34. $f(x) = \frac{\sin(x^2 + 3x + 2)}{x + 2}; \quad \lim_{x \to -2} f(x)$  
    $x: -2.1, -2.01, -2.001, -1.999, -1.99, -1.9$

**35–38 True–False Determine whether the statement is true or false. Explain your answer.**

35. If $|f(x) + 5| \le |x + 1|$, then $\lim_{x \to -1} f(x) = -5$.
36. For $0 < x < \pi/2$, the graph of $y = \sin x$ lies below $y = x$ and above $y = x\cos x$.
37. $f(x) = \begin{cases} x\sin(1/x), & x \neq 0 \\ 0, & x = 0 \end{cases}$ is continuous everywhere.
38. If $-M \le f(x) \le M$, then $\lim_{x \to 0} xf(x) = 0$ and $\lim_{x \to +\infty} \frac{f(x)}{x} = 0$.

**FOCUS ON CONCEPTS**

39. Student table error in degrees mode for $(\sin x)/x$.
40. Limit of ratio of chord length to arc length $\lim_{\theta \to 0^+} c(\theta)/s(\theta) = 1$.
41. Find $k \neq 0$ so that $f(x) = \begin{cases} \frac{\tan kx}{x}, & x < 0 \\ 3x + 2k^2, & x \ge 0 \end{cases}$ is continuous at $x = 0$.
42. Continuity of $f(x) = \begin{cases} \frac{\sin x}{|x|}, & x \neq 0 \\ 1, & x = 0 \end{cases}$ at $x = 0$.
43. Limits by substitution:  
    (a) $\lim_{x \to +\infty} x\sin(1/x); \ t = 1/x$  
    (b) $\lim_{x \to -\infty} x(1 - \cos(1/x)); \ t = 1/x$  
    (c) $\lim_{x \to \pi} \frac{\pi - x}{\sin x}; \ t = \pi - x$
44. $\lim_{x \to 2} \frac{\cos(\pi/x)}{x - 2}$.
45. $\lim_{x \to 1} \frac{\sin(\pi x)}{x - 1}$.
46. $\lim_{x \to \pi/4} \frac{\tan x - 1}{x - \pi/4}$.
47–48. Squeezing Theorem proofs for $x\cos(50\pi/x)$ and $x^2\sin(50\pi/\sqrt[3]{x})$.
49. Why $\lim_{x \to 0} [x\sin(1/x)] = \lim x \cdot \lim \sin(1/x) = 0 \cdot \text{DNE} = 0$ is invalid.
50. Sandwiching between $1 - x^2 \le f(x) \le \cos x$ on $(-\pi/2, \pi/2)$.
51. Sandwiching between $-1/x \le f(x) \le 1/x$ on $[1, +\infty)$.
52. Geometric diagrams for Squeezing Theorem at $\pm\infty$.
53. IVT proof of solution to $x = \cos x$ on $[0, \pi/2]$.
54. IVT proof of solution to $x + \sin x = 1$ on $[0, \pi/6]$.
55. WGS 84 Ellipsoidal Gravity formula: $g = 9.7803253359\frac{1 + 0.0019318526461\sin^2\phi}{\sqrt{1 - 0.0066943799901\sin^2\phi}}\text{ m/s}^2$.
56. **Writing.** Practical value of Squeezing Theorem.
57. **Writing.** Report on Fred Richman's article "A Circular Argument".

---

## CHAPTER 1 REVIEW EXERCISES

1. Limits from graph in Figure Ex-1: $\lim_{x \to 1}, \lim_{x \to 2}, \lim_{x \to 3}, \lim_{x \to 4}, \lim_{x \to +\infty}, \lim_{x \to -\infty}, \lim_{x \to 3^+}, \lim_{x \to 3^-}, \lim_{x \to 0}$.
2. Tables and analytical confirmation for: (a) $\lim_{x \to 2^+} \frac{x - 2}{x^2 - 4}$ (b) $\lim_{x \to 0} \frac{\tan 4x}{x}$.

**3–8 Find the limits.**

3. $\lim_{x \to -1} \frac{x^3 - x^2}{x - 1}$
4. $\lim_{x \to 1} \frac{x^3 - x^2}{x - 1}$
5. $\lim_{x \to -3} \frac{3x + 9}{x^2 + 4x + 3}$
6. $\lim_{x \to 2^-} \frac{x + 2}{x - 2}$
7. $\lim_{x \to +\infty} \frac{(2x - 1)^5}{(3x^2 + 2x - 7)(x^3 - 9x)}$
8. $\lim_{x \to 0} \frac{\sqrt{x^2 + 4} - 2}{x^2}$

9. Find horizontal asymptotes:  
   (a) $y = \frac{2x - 7}{x^2 - 4x}$  
   (b) $y = \frac{x^3 - x^2 + 10}{3x^2 - 4x}$  
   (c) $y = \frac{2x^2 - 6}{x^2 + 5x}$
10. Find $\lim_{x \to a} f(x)$ for $a = 0, 5^+, -5^-, -5, 5, -\infty, +\infty$:  
    (a) $f(x) = \sqrt{5 - x}$  
    (b) $f(x) = \begin{cases} \frac{x - 5}{|x - 5|}, & x \neq 5 \\ 0, & x = 5 \end{cases}$

**11–15 Find the limits.**

11. $\lim_{x \to 0} \frac{\sin 3x}{\tan 3x}$
12. $\lim_{x \to 0} \frac{x\sin x}{1 - \cos x}$
13. $\lim_{x \to 0} \frac{3x - \sin(kx)}{x} \ (k \neq 0)$
14. $\lim_{\theta \to 0} \tan\left(\frac{1 - \cos\theta}{\theta}\right)$
15. $\lim_{x \to -1} \frac{\sin(x + 1)}{x^2 - 1}$

16. **Writing.** Descriptions of limit failure, infinite limits, and discontinuities.
17. Rational function with vertical asymptote $x = 1$ and horizontal asymptote $y = 2$.
18. Viewing window paraphrase of $\epsilon$-$\delta$ limit definition.
19. If $0 < |x - 2| < \frac{3}{4}\epsilon \implies |f(x) - 5| < \epsilon$: (a) identify limit (b) find $\delta$ for $|8f(x) - 40| < 0.048$.
20. Largest $\delta$ for $|(\sin x)/x - 1| < 0.001$.
21. Find $\delta$ for given $\epsilon$: (a) $\lim_{x \to 2} (4x - 7) = 1, \epsilon = 0.01$ (b) $\lim_{x \to 3/2} \frac{4x^2 - 9}{2x - 3} = 6, \epsilon = 0.05$ (c) $\lim_{x \to 4} x^2 = 16, \epsilon = 0.001$.
22. $\epsilon$-$\delta$ proofs for $\lim_{x \to 2} (4x - 7) = 1$ and $\lim_{x \to 3/2} \frac{4x^2 - 9}{2x - 3} = 6$.
23. Positivity interval proof for continuous function with $f(x_0) > 0$.
24. (a) Approximate $\lim_{x \to 1} \frac{\sin x - \sin 1}{x - 1}$.  
    (b) Use identity $\sin\alpha - \sin\beta = 2\sin(\frac{\alpha-\beta}{2})\cos(\frac{\alpha+\beta}{2})$ to evaluate exact limit.
25. Discontinuities of: (a) $\frac{x}{x^2 - 1}$ (b) $|x^3 - 2x^2|$ (c) $\frac{x + 3}{|x^2 + 3x|}$.
26. Continuity domain of: (a) $\frac{x}{|x| - 3}$ (b) $\cos^{-1}(1/x)$ (c) $\frac{2x - 1}{2x^2 + 3x - 2}$.
27. Continuity of $f(x) = \begin{cases} -x^4 + 3, & x \le 2 \\ x^2 + 9, & x > 2 \end{cases}$.
28. Dictionary definition of continuous function.
29. Counterexample to IVT if $f$ is discontinuous.
30. Prove $f(x) > 0$ on $[0, 1]$ if $f$ is continuous, $f(0) = 2$, and has no zeros.
31. Show $x^4 + 5x^3 + 5x - 1 = 0$ has at least two real roots in $[-6, 2]$.

---

## CHAPTER 1 MAKING CONNECTIONS

1. Unique secant circle through $O(0, 0), Q(-x, x^2),$ and $P(x, x^2)$ on $y = x^2$. The center lies on the intersection of the $y$-axis and the perpendicular bisector of segment $OP$.
2. (a) Center of secant circle is $(0, C(x))$ where $C(x) = \frac{1}{2}x^2 + \frac{1}{2}$.  
   (b) As $x \to 0^+$, secant circles approach the **osculating circle** centered at $(0, 1/2)$ with radius $1/2$.
3. Osculating circle center formula for even functions $y = f(x)$ at $(0, f(0))$:
   $$C(x) = \frac{1}{2}\left[f(0) + f(x) + \frac{x^2}{f(x) - f(0)}\right]$$
4. Osculating circles at $(0, f(0))$ for:  
   (a) $f(x) = 4x^2$  
   (b) $f(x) = x^2\cos x$  
   (c) $f(x) = |x|$  
   (d) $f(x) = x\sin x$  
   (e) $f(x) = \cos x$  
   (f) $f(x) = x^2 g(x)$ ($g$ even, continuous, $g(0) \neq 0$)  
   (g) $f(x) = x^4$.
