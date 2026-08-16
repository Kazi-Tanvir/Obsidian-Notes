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

**Solution.** If we can find the slope $m_{\tan}$ of the tangent line at $P$, then we can use the point $P$ and the point-slope formula for a line (Web Appendix G) to write the equation of the tangent line as
$$y - 1 = m_{\tan}(x - 1) \tag{1}$$
To find the slope $m_{\tan}$, consider the secant line through $P$ and a point $Q(x, x^2)$ on the parabola that is distinct from $P$. The slope $m_{\sec}$ of this secant line is
$$m_{\sec} = \frac{x^2 - 1}{x - 1} \tag{2}$$
*(Why are we requiring that $P$ and $Q$ be distinct?)*

Figure 1.1.4a suggests that if we now let $Q$ move along the parabola, getting closer and closer to $P$, then the limiting position of the secant line through $P$ and $Q$ will coincide with that of the tangent line at $P$. This in turn suggests that the value of $m_{\sec}$ will get closer and closer to the value of $m_{\tan}$ as $P$ moves toward $Q$ along the curve. However, to say that $Q(x, x^2)$ gets closer and closer to $P(1, 1)$ is algebraically equivalent to saying that $x$ gets closer and closer to 1. Thus, the problem of finding $m_{\tan}$ reduces to finding the "limiting value" of $m_{\sec}$ in Formula (2) as $x$ gets closer and closer to 1 (but with $x \neq 1$ to ensure that $P$ and $Q$ remain distinct).

We can rewrite (2) as
$$m_{\sec} = \frac{x^2 - 1}{x - 1} = \frac{(x - 1)(x + 1)}{x - 1} = x + 1$$
where the cancellation of the factor $(x - 1)$ is allowed because $x \neq 1$. It is now evident that $m_{\sec}$ gets closer and closer to 2 as $x$ gets closer and closer to 1. Thus, $m_{\tan} = 2$ and (1) implies that the equation of the tangent line is
$$y - 1 = 2(x - 1) \quad \text{or equivalently} \quad y = 2x - 1$$
Figure 1.1.5 shows the graph of $y = x^2$ and this tangent line.

---

### AREAS AND LIMITS

Just as the general notion of a tangent line leads to the concept of limit, so does the general notion of area. For plane regions with straight-line boundaries, areas can often be calculated by subdividing the region into rectangles or triangles and adding the areas of the constituent parts (Figure 1.1.6). However, for regions with curved boundaries, such as that in Figure 1.1.7a, a more general approach is needed. One such approach is to begin by approximating the area of the region by inscribing a number of rectangles of equal width under the curve and adding the areas of these rectangles (Figure 1.1.7b). Intuition suggests that if we repeat that approximation process using more and more rectangles, then the rectangles will tend to fill in the gaps under the curve, and the approximations will get closer and closer to the exact area under the curve (Figure 1.1.7c). This suggests that we can define the area under the curve to be the limiting value of these approximations. This idea will be considered in detail later, but the point to note here is that once again the concept of a limit comes into play.

---

### DECIMALS AND LIMITS

Limits also arise in the familiar context of decimals. For example, the decimal expansion of the fraction $\frac{1}{3}$ is
$$\frac{1}{3} = 0.33333\dots \tag{3}$$
in which the dots indicate that the digit 3 repeats indefinitely. Although you may not have thought about decimals in this way, we can write (3) as
$$\frac{1}{3} = 0.33333\dots = 0.3 + 0.03 + 0.003 + 0.0003 + 0.00003 + \dots \tag{4}$$
which is a sum with "infinitely many" terms. As we will discuss in more detail later, we interpret (4) to mean that the succession of finite sums
$$0.3, \; 0.3 + 0.03, \; 0.3 + 0.03 + 0.003, \; 0.3 + 0.03 + 0.003 + 0.0003, \dots$$
gets closer and closer to a limiting value of $\frac{1}{3}$ as more and more terms are included. Thus, limits even occur in the familiar context of decimal representations of real numbers.

---

### LIMITS

Now that we have seen how limits arise in various ways, let us focus on the limit concept itself.

The most basic use of limits is to describe how a function behaves as the independent variable approaches a given value. For example, let us examine the behavior of the function
$$f(x) = x^2 - x + 1$$
for $x$-values closer and closer to 2. It is evident from the graph and table in Figure 1.1.8 that the values of $f(x)$ get closer and closer to 3 as values of $x$ are selected closer and closer to 2 on either the left or the right side of 2. We describe this by saying that the "limit of $x^2 - x + 1$ is 3 as $x$ approaches 2 from either side," and we write
$$\lim_{x \to 2} (x^2 - x + 1) = 3 \tag{5}$$

#### Figure 1.1.8 Data Table
| $x$ (Left side) | $f(x)$ | $x$ (Right side) | $f(x)$ |
| :---: | :---: | :---: | :---: |
| 1.0 | 1.000000 | 3.0 | 7.000000 |
| 1.5 | 1.750000 | 2.5 | 4.750000 |
| 1.9 | 2.710000 | 2.1 | 3.310000 |
| 1.95 | 2.852500 | 2.05 | 3.152500 |
| 1.99 | 2.970100 | 2.01 | 3.030100 |
| 1.995 | 2.985025 | 2.005 | 3.015025 |
| 1.999 | 2.997001 | 2.001 | 3.003001 |

This leads us to the following general idea.

> **1.1.1 LIMITS (AN INFORMAL VIEW)**  
> If the values of $f(x)$ can be made as close as we like to $L$ by taking values of $x$ sufficiently close to $a$ (but not equal to $a$), then we write
> $$\lim_{x \to a} f(x) = L \tag{6}$$
> which is read "the limit of $f(x)$ as $x$ approaches $a$ is $L$" or "$f(x)$ approaches $L$ as $x$ approaches $a$." The expression in (6) can also be written as
> $$f(x) \to L \quad \text{as} \quad x \to a \tag{7}$$

> *Note:* Since $x$ is required to be different from $a$ in (6), the value of $f$ at $a$, or even whether $f$ is defined at $a$, has no bearing on the limit $L$. The limit describes the behavior of $f$ close to $a$ but not *at* $a$.

#### Example 2
Use numerical evidence to make a conjecture about the value of
$$\lim_{x \to 1} \frac{x - 1}{\sqrt{x} - 1} \tag{8}$$

**Solution.** Although the function
$$f(x) = \frac{x - 1}{\sqrt{x} - 1} \tag{9}$$
is undefined at $x = 1$, this has no bearing on the limit. Table 1.1.1 shows sample $x$-values approaching 1 from the left side and from the right side. In both cases the corresponding values of $f(x)$, calculated to six decimal places, appear to get closer and closer to 2, and hence we conjecture that
$$\lim_{x \to 1} \frac{x - 1}{\sqrt{x} - 1} = 2$$
This is consistent with the graph of $f$ shown in Figure 1.1.9. In the next section we will show how to obtain this result algebraically.

##### Table 1.1.1
| $x$ (Left) | $f(x)$ | $x$ (Right) | $f(x)$ |
| :---: | :---: | :---: | :---: |
| 0.99 | 1.994987 | 1.01 | 2.004988 |
| 0.999 | 1.999500 | 1.001 | 2.000500 |
| 0.9999 | 1.999950 | 1.0001 | 2.000050 |
| 0.99999 | 1.999995 | 1.00001 | 2.000005 |

#### Example 3
Use numerical evidence to make a conjecture about the value of
$$\lim_{x \to 0} \frac{\sin x}{x} \tag{10}$$

**Solution.** With the help of a calculating utility set in radian mode, we obtain Table 1.1.2. The data in the table suggest that
$$\lim_{x \to 0} \frac{\sin x}{x} = 1 \tag{11}$$
The result is consistent with the graph of $f(x) = (\sin x)/x$ shown in Figure 1.1.10. Later in this chapter we will give a geometric argument to prove that our conjecture is correct.

##### Table 1.1.2
| $x$ (radians) | $y = \frac{\sin x}{x}$ |
| :---: | :---: |
| $\pm 1.0$ | 0.84147 |
| $\pm 0.9$ | 0.87036 |
| $\pm 0.8$ | 0.89670 |
| $\pm 0.7$ | 0.92031 |
| $\pm 0.6$ | 0.94107 |
| $\pm 0.5$ | 0.95885 |
| $\pm 0.4$ | 0.97355 |
| $\pm 0.3$ | 0.98507 |
| $\pm 0.2$ | 0.99335 |
| $\pm 0.1$ | 0.99833 |
| $\pm 0.01$ | 0.99998 |

---

### SAMPLING PITFALLS

Numerical evidence can sometimes lead to incorrect conclusions about limits because of roundoff error or because the sample values chosen do not reveal the true limiting behavior. For example, one might incorrectly conclude from Table 1.1.3 that
$$\lim_{x \to 0} \sin\left(\frac{\pi}{x}\right) = 0$$

##### Table 1.1.3
| $x$ | $\pi/x$ | $f(x) = \sin(\pi/x)$ |
| :---: | :---: | :---: |
| $x = \pm 1$ | $\pm\pi$ | $\sin(\pm\pi) = 0$ |
| $x = \pm 0.1$ | $\pm 10\pi$ | $\sin(\pm 10\pi) = 0$ |
| $x = \pm 0.01$ | $\pm 100\pi$ | $\sin(\pm 100\pi) = 0$ |
| $x = \pm 0.001$ | $\pm 1000\pi$ | $\sin(\pm 1000\pi) = 0$ |
| $x = \pm 0.0001$ | $\pm 10{,}000\pi$ | $\sin(\pm 10{,}000\pi) = 0$ |

The fact that this is not correct is evidenced by the graph of $f$ in Figure 1.1.11. The graph reveals that the values of $f$ oscillate between $-1$ and 1 with increasing rapidity as $x \to 0$ and hence do not approach a limit. The data in the table deceived us because the $x$-values selected all happened to be $x$-intercepts for $f(x)$. This points out the need for having alternative methods for corroborating limits conjectured from numerical evidence.

---

### ONE-SIDED LIMITS

The limit in (6) is called a **two-sided limit** because it requires the values of $f(x)$ to get closer and closer to $L$ as values of $x$ are taken from either side of $x = a$. However, some functions exhibit different behaviors on the two sides of an $x$-value $a$, in which case it is necessary to distinguish whether values of $x$ near $a$ are on the left side or on the right side of $a$ for purposes of investigating limiting behavior. For example, consider the function
$$f(x) = \frac{|x|}{x} = \begin{cases} 1, & x > 0 \\ -1, & x < 0 \end{cases} \tag{12}$$
which is graphed in Figure 1.1.12. As $x$ approaches 0 from the right, the values of $f(x)$ approach a limit of 1 [in fact, the values of $f(x)$ are exactly 1 for all such $x$], and similarly, as $x$ approaches 0 from the left, the values of $f(x)$ approach a limit of $-1$. We denote these limits by writing
$$\lim_{x \to 0^+} \frac{|x|}{x} = 1 \quad \text{and} \quad \lim_{x \to 0^-} \frac{|x|}{x} = -1 \tag{13}$$
With this notation, the superscript "$+$" indicates a limit from the right and the superscript "$-$" indicates a limit from the left.

> **1.1.2 ONE-SIDED LIMITS (AN INFORMAL VIEW)**  
> If the values of $f(x)$ can be made as close as we like to $L$ by taking values of $x$ sufficiently close to $a$ (but greater than $a$), then we write
> $$\lim_{x \to a^+} f(x) = L \tag{14}$$
> and if the values of $f(x)$ can be made as close as we like to $L$ by taking values of $x$ sufficiently close to $a$ (but less than $a$), then we write
> $$\lim_{x \to a^-} f(x) = L \tag{15}$$

---

### THE RELATIONSHIP BETWEEN ONE-SIDED LIMITS AND TWO-SIDED LIMITS

In general, there is no guarantee that a function $f$ will have a two-sided limit at a given point $a$; that is, the values of $f(x)$ may not get closer and closer to any single real number $L$ as $x \to a$. In this case we say that $\lim_{x \to a} f(x)$ **does not exist**.

> **1.1.3 THE RELATIONSHIP BETWEEN ONE-SIDED AND TWO-SIDED LIMITS**  
> The two-sided limit of a function $f(x)$ exists at $a$ if and only if both of the one-sided limits exist at $a$ and have the same value; that is,
> $$\lim_{x \to a} f(x) = L \quad \text{if and only if} \quad \lim_{x \to a^-} f(x) = L = \lim_{x \to a^+} f(x)$$

#### Example 4
Explain why $\lim_{x \to 0} \frac{|x|}{x}$ does not exist.

**Solution.** As $x$ approaches 0, the values of $f(x) = |x|/x$ approach $-1$ from the left and approach 1 from the right [see (13)]. Thus, the one-sided limits at 0 are not the same.

#### Example 5
For the functions in Figure 1.1.13, find the one-sided and two-sided limits at $x = a$ if they exist.

**Solution.** The functions in all three figures have the same one-sided limits as $x \to a$, since the functions are identical, except at $x = a$. These limits are
$$\lim_{x \to a^+} f(x) = 3 \quad \text{and} \quad \lim_{x \to a^-} f(x) = 1$$
In all three cases the two-sided limit does not exist as $x \to a$ because the one-sided limits are not equal.

#### Example 6
For the functions in Figure 1.1.14, find the one-sided and two-sided limits at $x = a$ if they exist.

**Solution.** As in the preceding example, the value of $f$ at $x = a$ has no bearing on the limits as $x \to a$, so in all three cases we have
$$\lim_{x \to a^+} f(x) = 2 \quad \text{and} \quad \lim_{x \to a^-} f(x) = 2$$
Since the one-sided limits are equal, the two-sided limit exists and
$$\lim_{x \to a} f(x) = 2$$

---

### INFINITE LIMITS

Sometimes one-sided or two-sided limits fail to exist because the values of the function increase or decrease without bound. For example, consider the behavior of $f(x) = 1/x$ for values of $x$ near 0. It is evident from Figure 1.1.15 that as $x$-values are taken closer and closer to 0 from the right, the values of $f(x) = 1/x$ are positive and increase without bound; and as $x$-values are taken closer and closer to 0 from the left, the values of $f(x) = 1/x$ are negative and decrease without bound. We write
$$\lim_{x \to 0^+} \frac{1}{x} = +\infty \quad \text{and} \quad \lim_{x \to 0^-} \frac{1}{x} = -\infty$$

> *Note:* The symbols $+\infty$ and $-\infty$ here are not real numbers; they simply describe particular ways in which the limits fail to exist. Do not make the mistake of manipulating these symbols using rules of algebra (e.g., $(+\infty) - (+\infty) \neq 0$).

> **1.1.4 INFINITE LIMITS (AN INFORMAL VIEW)**  
> The expressions
> $$\lim_{x \to a^-} f(x) = +\infty \quad \text{and} \quad \lim_{x \to a^+} f(x) = +\infty$$
> denote that $f(x)$ increases without bound as $x$ approaches $a$ from the left and from the right, respectively. If both are true, then we write
> $$\lim_{x \to a} f(x) = +\infty$$
> Similarly, the expressions
> $$\lim_{x \to a^-} f(x) = -\infty \quad \text{and} \quad \lim_{x \to a^+} f(x) = -\infty$$
> denote that $f(x)$ decreases without bound as $x$ approaches $a$ from the left and from the right, respectively. If both are true, then we write
> $$\lim_{x \to a} f(x) = -\infty$$

#### Example 7
For the functions in Figure 1.1.16, describe the limits at $x = a$ in appropriate limit notation.
* **(a)** $\lim_{x \to a^+} \frac{1}{x - a} = +\infty$ and $\lim_{x \to a^-} \frac{1}{x - a} = -\infty$
* **(b)** $\lim_{x \to a} \frac{1}{(x - a)^2} = +\infty$
* **(c)** $\lim_{x \to a^+} \frac{-1}{x - a} = -\infty$ and $\lim_{x \to a^-} \frac{-1}{x - a} = +\infty$
* **(d)** $\lim_{x \to a} \frac{-1}{(x - a)^2} = -\infty$

---

### VERTICAL ASYMPTOTES

Figure 1.1.17 illustrates geometrically what happens when any of the infinite limit situations occur. In each case the graph of $y = f(x)$ either rises or falls without bound, squeezing closer and closer to the vertical line $x = a$ as $x$ approaches $a$ from the side indicated in the limit. The line $x = a$ is called a **vertical asymptote** of the curve $y = f(x)$ (from the Greek word *asymptotos*, meaning "nonintersecting").

#### Example 8
For the function $f$ graphed in Figure 1.1.18, find:
(a) $\lim_{x \to -2^-} f(x) = 1 = f(-2)$  
(b) $\lim_{x \to -2^+} f(x) = -2$  
(c) $\lim_{x \to 0^-} f(x) = 0 = f(0)$  
(d) $\lim_{x \to 0^+} f(x) = -\infty$  
(e) $\lim_{x \to 4^-} f(x)$ does not exist due to oscillation  
(f) $\lim_{x \to 4^+} f(x) = +\infty$  
(g) The vertical asymptotes of the graph of $f$ are the $y$-axis ($x = 0$) and the line $x = 4$.

---

### QUICK CHECK EXERCISES 1.1
*(See page 61 for answers.)*

1. We write $\lim_{x \to a} f(x) = L$ provided the values of $\underline{\hspace{2cm}}$ can be made as close to $\underline{\hspace{2cm}}$ as desired, by taking values of $\underline{\hspace{2cm}}$ sufficiently close to $\underline{\hspace{2cm}}$ but not $\underline{\hspace{2cm}}$.  
2. We write $\lim_{x \to a^-} f(x) = +\infty$ provided $\underline{\hspace{2cm}}$ increases without bound, as $\underline{\hspace{2cm}}$ approaches $\underline{\hspace{2cm}}$ from the left.  
3. State what must be true about $\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$ in order for it to be the case that $\lim_{x \to a} f(x) = L$.  
4. Use the accompanying graph of $y = f(x)$ ($-\infty < x < 3$) to determine the limits:  
   (a) $\lim_{x \to 0} f(x) = \underline{\hspace{2cm}}$  
   (b) $\lim_{x \to 2^-} f(x) = \underline{\hspace{2cm}}$  
   (c) $\lim_{x \to 2^+} f(x) = \underline{\hspace{2cm}}$  
   (d) $\lim_{x \to 3^-} f(x) = \underline{\hspace{2cm}}$  
5. The slope of the secant line through $P(2, 4)$ and $Q(x, x^2)$ on the parabola $y = x^2$ is $m_{\sec} = x + 2$. It follows that the slope of the tangent line to this parabola at the point $P$ is $\underline{\hspace{2cm}}$.

---

### EXERCISE SET 1.1

**1–10** In these exercises, make reasonable assumptions about the graph of the indicated function outside of the region depicted.  
1. For the function $g$ graphed in Figure Ex-1, find: (a) $\lim_{x \to 0^-} g(x)$ (b) $\lim_{x \to 0^+} g(x)$ (c) $\lim_{x \to 0} g(x)$ (d) $g(0)$.  
2. For the function $G$ graphed in Figure Ex-2, find: (a) $\lim_{x \to 0^-} G(x)$ (b) $\lim_{x \to 0^+} G(x)$ (c) $\lim_{x \to 0} G(x)$ (d) $G(0)$.  
3. For the function $f$ graphed in Figure Ex-3, find: (a) $\lim_{x \to 3^-} f(x)$ (b) $\lim_{x \to 3^+} f(x)$ (c) $\lim_{x \to 3} f(x)$ (d) $f(3)$.  
4. For the function $f$ graphed in Figure Ex-4, find: (a) $\lim_{x \to 2^-} f(x)$ (b) $\lim_{x \to 2^+} f(x)$ (c) $\lim_{x \to 2} f(x)$ (d) $f(2)$.  
5. For the function $F$ graphed in Figure Ex-5, find: (a) $\lim_{x \to -2^-} F(x)$ (b) $\lim_{x \to -2^+} F(x)$ (c) $\lim_{x \to -2} F(x)$ (d) $F(-2)$.  
6. For the function $G$ graphed in Figure Ex-6, find: (a) $\lim_{x \to 0^-} G(x)$ (b) $\lim_{x \to 0^+} G(x)$ (c) $\lim_{x \to 0} G(x)$ (d) $G(0)$.  
7. For the function $f$ graphed in Figure Ex-7, find: (a) $\lim_{x \to 3^-} f(x)$ (b) $\lim_{x \to 3^+} f(x)$ (c) $\lim_{x \to 3} f(x)$ (d) $f(3)$.  
8. For the function $\phi$ graphed in Figure Ex-8, find: (a) $\lim_{x \to 4^-} \phi(x)$ (b) $\lim_{x \to 4^+} \phi(x)$ (c) $\lim_{x \to 4} \phi(x)$ (d) $\phi(4)$.  
9. For the function $f$ graphed in Figure Ex-9, find: (a) $\lim_{x \to -2} f(x)$ (b) $\lim_{x \to 0^-} f(x)$ (c) $\lim_{x \to 0^+} f(x)$ (d) $\lim_{x \to 2^-} f(x)$ (e) $\lim_{x \to 2^+} f(x)$ (f) the vertical asymptotes of the graph of $f$.  
10. For the function $f$ graphed in Figure Ex-10, find: (a) $\lim_{x \to -2^-} f(x)$ (b) $\lim_{x \to -2^+} f(x)$ (c) $\lim_{x \to 0^-} f(x)$ (d) $\lim_{x \to 0^+} f(x)$ (e) $\lim_{x \to 2^-} f(x)$ (f) $\lim_{x \to 2^+} f(x)$ (g) the vertical asymptotes of the graph of $f$.  

**11–12** (i) Complete the table and make a guess about the limit indicated. (ii) Confirm your conclusions about the limit by graphing a function over an appropriate interval.  
11. $f(x) = \frac{\sin 2x}{x}$; $\lim_{x \to 0} f(x)$  
12. $f(x) = \frac{\cos x - 1}{x^2}$; $\lim_{x \to 0} f(x)$  

**13–16** (i) Make a guess at the limit (if it exists) by evaluating the function at the specified $x$-values. (ii) Confirm your conclusions about the limit by graphing the function over an appropriate interval. (iii) If you have a CAS, then use it to find the limit.  
13. (a) $\lim_{x \to 1} \frac{x - 1}{x^3 - 1}$; $x = 2, 1.5, 1.1, 1.01, 1.001, 0, 0.5, 0.9, 0.99, 0.999$  
    (b) $\lim_{x \to 1^+} \frac{x + 1}{x^3 - 1}$; $x = 2, 1.5, 1.1, 1.01, 1.001, 1.0001$  
    (c) $\lim_{x \to 1^-} \frac{x + 1}{x^3 - 1}$; $x = 0, 0.5, 0.9, 0.99, 0.999, 0.9999$  
14. (a) $\lim_{x \to 0} \frac{\sqrt{x + 1} - 1}{x}$; $x = \pm 0.25, \pm 0.1, \pm 0.001, \pm 0.0001$  
    (b) $\lim_{x \to 0^+} \frac{\sqrt{x + 1} + 1}{x}$; $x = 0.25, 0.1, 0.001, 0.0001$  
    (c) $\lim_{x \to 0^-} \frac{\sqrt{x + 1} + 1}{x}$; $x = -0.25, -0.1, -0.001, -0.0001$  
15. (a) $\lim_{x \to 0} \frac{\sin 3x}{x}$; $x = \pm 0.25, \pm 0.1, \pm 0.001, \pm 0.0001$  
    (b) $\lim_{x \to -1} \frac{\cos x}{x + 1}$; $x = 0, -0.5, -0.9, -0.99, -0.999, -1.5, -1.1, -1.01, -1.001$  
16. (a) $\lim_{x \to -1} \frac{\tan(x + 1)}{x + 1}$; $x = 0, -0.5, -0.9, -0.99, -0.999, -1.5, -1.1, -1.01, -1.001$  
    (b) $\lim_{x \to 0} \frac{\sin(5x)}{\sin(2x)}$; $x = \pm 0.25, \pm 0.1, \pm 0.001, \pm 0.0001$  

**17–20 True–False** Determine whether the statement is true or false. Explain your answer.  
17. If $f(a) = L$, then $\lim_{x \to a} f(x) = L$.  
18. If $\lim_{x \to a} f(x)$ exists, then so do $\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$.  
19. If $\lim_{x \to a^-} f(x)$ and $\lim_{x \to a^+} f(x)$ exist, then so does $\lim_{x \to a} f(x)$.  
20. If $\lim_{x \to a^+} f(x) = +\infty$, then $f(a)$ is undefined.  

**21–26** Sketch a possible graph for a function $f$ with the specified properties.  
21. (i) the domain of $f$ is $[-1, 1]$ (ii) $f(-1) = f(0) = f(1) = 0$ (iii) $\lim_{x \to -1^+} f(x) = \lim_{x \to 0} f(x) = \lim_{x \to 1^-} f(x) = 1$  
22. (i) the domain of $f$ is $[-2, 1]$ (ii) $f(-2) = f(0) = f(1) = 0$ (iii) $\lim_{x \to -2^+} f(x) = 2$, $\lim_{x \to 0} f(x) = 0$, and $\lim_{x \to 1^-} f(x) = 1$  
23. (i) the domain of $f$ is $(-\infty, 0]$ (ii) $f(-2) = f(0) = 1$ (iii) $\lim_{x \to -2} f(x) = +\infty$  
24. (i) the domain of $f$ is $(0, +\infty)$ (ii) $f(1) = 0$ (iii) the $y$-axis is a vertical asymptote for the graph of $f$ (iv) $f(x) < 0$ if $0 < x < 1$  
25. (i) $f(-3) = f(0) = f(2) = 0$ (ii) $\lim_{x \to -2^-} f(x) = +\infty$ and $\lim_{x \to -2^+} f(x) = -\infty$ (iii) $\lim_{x \to 1} f(x) = +\infty$  
26. (i) $f(-1) = 0, f(0) = 1, f(1) = 0$ (ii) $\lim_{x \to -1^-} f(x) = 0$ and $\lim_{x \to -1^+} f(x) = +\infty$ (iii) $\lim_{x \to 1^-} f(x) = 1$ and $\lim_{x \to 1^+} f(x) = +\infty$  

**27–30** Modify the argument of Example 1 to find the equation of the tangent line to the specified graph at the point given.  
27. the graph of $y = x^2$ at $(-1, 1)$  
28. the graph of $y = x^2$ at $(0, 0)$  
29. the graph of $y = x^4$ at $(1, 1)$  
30. the graph of $y = x^4$ at $(-1, 1)$  

#### FOCUS ON CONCEPTS
31. In the special theory of relativity the length $l$ of a narrow rod moving longitudinally is a function $l = l(v)$ of the rod's speed $v$. Figure Ex-31 displays some of the qualitative features of this function.  
    (a) What is the physical interpretation of $l_0$?  
    (b) What is $\lim_{v \to c^-} l(v)$? What is the physical significance of this limit?  
32. In the special theory of relativity the mass $m$ of a moving object is a function $m = m(v)$ of the object's speed $v$. Figure Ex-32 displays some of the qualitative features of this function.  
    (a) What is the physical interpretation of $m_0$?  
    (b) What is $\lim_{v \to c^-} m(v)$? What is the physical significance of this limit?  
33. Let $f(x) = (1 + x^2)^{1.1/x^2}$.  
    (a) Graph $f$ in the window $[-1, 1] \times [2.5, 3.5]$ and use trace to conjecture $\lim_{x \to 0} f(x)$.  
    (b) Graph $f$ in the window $[-0.001, 0.001] \times [2.5, 3.5]$ and conjecture $\lim_{x \to 0} f(x)$.  
    (c) Graph $f$ in the window $[-0.000001, 0.000001] \times [2.5, 3.5]$ and conjecture $\lim_{x \to 0} f(x)$.  
    (d) Later we will be able to show that $\lim_{x \to 0} (1 + x^2)^{1.1/x^2} \approx 3.00416602$. What flaw do your graphs reveal about using numerical evidence to make conjectures about limits?  
34. **Writing** Two students are discussing the limit of $\sqrt{x}$ as $x$ approaches 0. One student maintains that the limit is 0, while the other claims that the limit does not exist. Write a short paragraph that discusses the pros and cons of each student's position.  
35. **Writing** Given a function $f$ and a real number $a$, explain informally why $\lim_{x \to 0} f(x + a) = \lim_{x \to a} f(x)$.  

#### QUICK CHECK ANSWERS 1.1
1. $f(x)$; $L$; $x$; $a$; $a$  
2. $f(x)$; $x$; $a$  
3. Both one-sided limits must exist and equal $L$.  
4. (a) 0 (b) 1 (c) $+\infty$ (d) $-\infty$  
5. 4  

---

## 1.2 COMPUTING LIMITS

### SOME BASIC LIMITS

> **1.2.1 THEOREM**  
> Let $a$ and $k$ be real numbers.  
> (a) $\lim_{x \to a} k = k$  
> (b) $\lim_{x \to a} x = a$  
> (c) $\lim_{x \to 0^-} \frac{1}{x} = -\infty$  
> (d) $\lim_{x \to 0^+} \frac{1}{x} = +\infty$

#### Example 1
$\lim_{x \to -25} 3 = 3, \quad \lim_{x \to 0} 3 = 3, \quad \lim_{x \to \pi} 3 = 3$

#### Example 2
$\lim_{x \to 0} x = 0, \quad \lim_{x \to -2} x = -2, \quad \lim_{x \to \pi} x = \pi$

#### Example 3
Table 1.2.1 illustrates why $1/x \to +\infty$ as $x \to 0^+$ and $1/x \to -\infty$ as $x \to 0^-$.

> **1.2.2 THEOREM**  
> Let $a$ be a real number, and suppose that $\lim_{x \to a} f(x) = L_1$ and $\lim_{x \to a} g(x) = L_2$. Then:  
> (a) $\lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x) = L_1 + L_2$  
> (b) $\lim_{x \to a} [f(x) - g(x)] = \lim_{x \to a} f(x) - \lim_{x \to a} g(x) = L_1 - L_2$  
> (c) $\lim_{x \to a} [f(x)g(x)] = (\lim_{x \to a} f(x))(\lim_{x \to a} g(x)) = L_1 L_2$  
> (d) $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)} = \frac{L_1}{L_2}$, provided $L_2 \neq 0$  
> (e) $\lim_{x \to a} \sqrt[n]{f(x)} = \sqrt[n]{\lim_{x \to a} f(x)} = \sqrt[n]{L_1}$, provided $L_1 > 0$ if $n$ is even.  
> Moreover, these statements are also true for one-sided limits as $x \to a^-$ or $x \to a^+$.

Constant multiple rule: $\lim_{x \to a} (kf(x)) = k \lim_{x \to a} f(x)$.

#### Example 4
* $\lim_{x \to a} [f(x) - g(x) + 2h(x)] = \lim_{x \to a} f(x) - \lim_{x \to a} g(x) + 2\lim_{x \to a} h(x)$
* $\lim_{x \to a} [f(x)]^n = [\lim_{x \to a} f(x)]^n$
* $\lim_{x \to a} x^n = a^n$

---

### LIMITS OF POLYNOMIALS AND RATIONAL FUNCTIONS AS $x \to a$

#### Example 5
$$\lim_{x \to 5} (x^2 - 4x + 3) = 5^2 - 4(5) + 3 = 8$$

> **1.2.3 THEOREM**  
> For any polynomial $p(x) = c_0 + c_1 x + \dots + c_n x^n$ and any real number $a$,
> $$\lim_{x \to a} p(x) = c_0 + c_1 a + \dots + c_n a^n = p(a)$$

#### Example 6
$$\lim_{x \to 1} (x^7 - 2x^5 + 1)^{35} = (1 - 2 + 1)^{35} = 0$$

#### Example 7
$$\lim_{x \to 2} \frac{5x^3 + 4}{x - 3} = \frac{5(2^3) + 4}{2 - 3} = \frac{44}{-1} = -44$$

#### Example 8
Find: (a) $\lim_{x \to 4^+} \frac{2 - x}{(x - 4)(x + 2)} = -\infty$  
(b) $\lim_{x \to 4^-} \frac{2 - x}{(x - 4)(x + 2)} = +\infty$  
(c) $\lim_{x \to 4} \frac{2 - x}{(x - 4)(x + 2)}$ does not exist.

#### Example 9
(a) $\lim_{x \to 3} \frac{x^2 - 6x + 9}{x - 3} = \lim_{x \to 3} (x - 3) = 0$  
(b) $\lim_{x \to -4} \frac{2x + 8}{x^2 + x - 12} = \lim_{x \to -4} \frac{2(x + 4)}{(x + 4)(x - 3)} = \lim_{x \to -4} \frac{2}{x - 3} = -\frac{2}{7}$  
(c) $\lim_{x \to 5} \frac{x^2 - 3x - 10}{x^2 - 10x + 25} = \lim_{x \to 5} \frac{x + 2}{x - 5}$ does not exist ($\to +\infty$ from right, $\to -\infty$ from left).

> **1.2.4 THEOREM**  
> Let $f(x) = p(x)/q(x)$ be a rational function, and let $a$ be any real number.  
> (a) If $q(a) \neq 0$, then $\lim_{x \to a} f(x) = f(a)$.  
> (b) If $q(a) = 0$ but $p(a) \neq 0$, then $\lim_{x \to a} f(x)$ does not exist.

---

### LIMITS INVOLVING RADICALS

#### Example 10
$$\lim_{x \to 1} \frac{x - 1}{\sqrt{x} - 1} = \lim_{x \to 1} \frac{(x - 1)(\sqrt{x} + 1)}{x - 1} = \lim_{x \to 1} (\sqrt{x} + 1) = 2$$

---

### LIMITS OF PIECEWISE-DEFINED FUNCTIONS

#### Example 11
Let
$$f(x) = \begin{cases} 1/(x + 2), & x < -2 \\ x^2 - 5, & -2 < x \le 3 \\ \sqrt{x + 13}, & x > 3 \end{cases}$$
(a) $\lim_{x \to -2} f(x)$ does not exist ($\lim_{x \to -2^-} = -\infty, \; \lim_{x \to -2^+} = -1$)  
(b) $\lim_{x \to 0} f(x) = 0^2 - 5 = -5$  
(c) $\lim_{x \to 3} f(x) = 4$ ($\lim_{x \to 3^-} = 3^2 - 5 = 4, \; \lim_{x \to 3^+} = \sqrt{3 + 13} = 4$)

---

### QUICK CHECK EXERCISES 1.2
*(See page 70 for answers.)*

1. Find the limit by inspection: (a) $\lim_{x \to 8} 7$ (b) $\lim_{y \to 3^+} 12y$ (c) $\lim_{x \to 0^-} \frac{x}{|x|}$ (d) $\lim_{w \to 5} \frac{w}{|w|}$ (e) $\lim_{z \to 1^-} \frac{1}{1 - z}$  
2. Given $\lim_{x \to a} f(x) = 1$ and $\lim_{x \to a} g(x) = 2$, find: (a) $\lim_{x \to a} [3f(x) + 2g(x)]$ (b) $\lim_{x \to a} \frac{2f(x) + 1}{1 - f(x)g(x)}$ (c) $\lim_{x \to a} \frac{\sqrt{f(x) + 3}}{g(x)}$  
3. Find the limits: (a) $\lim_{x \to -1} (x^3 + x^2 + x)^{101}$ (b) $\lim_{x \to 2^-} \frac{(x - 1)(x - 2)}{x + 1}$ (c) $\lim_{x \to -1^+} \frac{(x - 1)(x - 2)}{x + 1}$ (d) $\lim_{x \to 4} \frac{x^2 - 16}{x - 4}$  
4. Let $f(x) = \begin{cases} x + 1, & x \le 1 \\ x - 1, & x > 1 \end{cases}$. Find: (a) $\lim_{x \to 1^-} f(x)$ (b) $\lim_{x \to 1^+} f(x)$ (c) $\lim_{x \to 1} f(x)$  

---

### EXERCISE SET 1.2

1. Given $\lim_{x \to a} f(x) = 2, \lim_{x \to a} g(x) = -4, \lim_{x \to a} h(x) = 0$, find:  
   (a) $\lim [f(x) + 2g(x)]$ (b) $\lim [h(x) - 3g(x) + 1]$ (c) $\lim [f(x)g(x)]$ (d) $\lim [g(x)]^2$ (e) $\lim \sqrt[3]{6 + f(x)}$ (f) $\lim \frac{2}{g(x)}$  
2. Graph-based limit evaluations using Figure Ex-2.  
**3–30** Find the limits (rational expressions, indeterminate forms, one-sided infinite limits, radicals).  
31–32 Piecewise function limits.  
**33–36 True–False** statements.  
**37–38** Rationalize numerators.  
39–40 Piecewise definitions and continuity parameters.  
**41–50 Focus on Concepts & Writing.**

#### QUICK CHECK ANSWERS 1.2
1. (a) 7 (b) 36 (c) $-1$ (d) 1 (e) $+\infty$  
2. (a) 7 (b) $-3$ (c) 1  
3. (a) $-1$ (b) 0 (c) $+\infty$ (d) 8  
4. (a) 2 (b) 0 (c) does not exist  

---

## 1.3 LIMITS AT INFINITY; END BEHAVIOR OF A FUNCTION

### LIMITS AT INFINITY AND HORIZONTAL ASYMPTOTES

> **1.3.1 LIMITS AT INFINITY (AN INFORMAL VIEW)**  
> If the values of $f(x)$ eventually get as close as we like to a number $L$ as $x$ increases without bound, then we write
> $$\lim_{x \to +\infty} f(x) = L \quad \text{or} \quad f(x) \to L \text{ as } x \to +\infty \tag{3}$$
> Similarly, if the values of $f(x)$ eventually get as close as we like to a number $L$ as $x$ decreases without bound, then we write
> $$\lim_{x \to -\infty} f(x) = L \quad \text{or} \quad f(x) \to L \text{ as } x \to -\infty \tag{4}$$

If either limit holds, the line $y = L$ is called a **horizontal asymptote** for the graph of $f$.

#### Basic Results:
$$\lim_{x \to +\infty} \frac{1}{x^n} = 0 \quad \text{and} \quad \lim_{x \to -\infty} \frac{1}{x^n} = 0 \quad (n > 0 \text{ integer})$$

---

### INFINITE LIMITS AT INFINITY

> **1.3.2 INFINITE LIMITS AT INFINITY (AN INFORMAL VIEW)**  
> If $f(x)$ increases/decreases without bound as $x \to \pm\infty$, we write $\lim_{x \to \pm\infty} f(x) = \pm\infty$ as appropriate.

#### Limits of $x^n$:
$$\lim_{x \to +\infty} x^n = +\infty \quad (n = 1, 2, 3, \dots)$$
$$\lim_{x \to -\infty} x^n = \begin{cases} -\infty, & n = 1, 3, 5, \dots \\ +\infty, & n = 2, 4, 6, \dots \end{cases}$$

#### Limits of Polynomials:
*The end behavior of a polynomial matches the end behavior of its highest degree term:*
$$\lim_{x \to \pm\infty} (c_0 + c_1 x + \dots + c_n x^n) = \lim_{x \to \pm\infty} c_n x^n$$

#### Limits of Rational Functions:
*The end behavior of a rational function matches the end behavior of the quotient of the highest degree term in the numerator divided by the highest degree term in the denominator:*
$$\lim_{x \to \pm\infty} \frac{a_n x^n + \dots + a_0}{b_m x^m + \dots + b_0} = \lim_{x \to \pm\infty} \frac{a_n x^n}{b_m x^m}$$

#### Example 8 (Radicals at Infinity)
(a) $\lim_{x \to +\infty} \frac{\sqrt{x^2 + 2}}{3x - 6} = \frac{1}{3}$  
(b) $\lim_{x \to -\infty} \frac{\sqrt{x^2 + 2}}{3x - 6} = -\frac{1}{3}$ (since $\sqrt{x^2} = |x| = -x$ for $x < 0$).

#### Example 9 (Rationalizing Differences)
(a) $\lim_{x \to +\infty} (\sqrt{x^6 + 5} - x^3) = 0$  
(b) $\lim_{x \to +\infty} (\sqrt{x^6 + 5x^3} - x^3) = \frac{5}{2}$

---

### QUICK CHECK EXERCISES 1.3
*(See page 80 for answers.)*

1. (a) $\lim_{x \to +\infty} (-2x)$ (b) $\lim_{x \to -\infty} \frac{x}{|x|}$ (c) $\lim_{x \to -\infty} (3 - x)$ (d) $\lim_{x \to +\infty} (5 - 1/x)$  
2. (a) $\lim_{x \to -\infty} \frac{2x^2 + x}{4x^2 - 3}$ (b) $\lim_{x \to +\infty} \frac{1}{2 + \sin x}$  
3. Given $\lim_{x \to +\infty} f(x) = 2$ and $\lim_{x \to +\infty} g(x) = -3$, evaluate combinations.  
4. Horizontal asymptote identification.

---

### EXERCISE SET 1.3
Exercises 1–57 covering limits at infinity, rational functions, radical limits, applications (relativity, Newton's law of cooling, logistic/carrying capacity), and asymptote curves.

#### QUICK CHECK ANSWERS 1.3
1. (a) $-\infty$ (b) $-1$ (c) $+\infty$ (d) 5  
2. (a) $1/2$ (b) does not exist  
3. (a) 9 (b) $-2/3$ (c) does not exist (d) 4  
4. The graphs of $y = 1/(x + 1)$ and $y = x/(x + 1)$ have horizontal asymptotes.

---

## 1.4 LIMITS (DISCUSSED MORE RIGOROUSLY)

### PRECISE EPSILON-DELTA DEFINITION

> **1.4.1 LIMIT DEFINITION (Epsilon-Delta)**  
> Let $f(x)$ be defined for all $x$ in some open interval containing the number $a$, with the possible exception that $f(x)$ need not be defined at $a$. We will write
> $$\lim_{x \to a} f(x) = L$$
> if given any number $\epsilon > 0$ we can find a number $\delta > 0$ such that
> $$|f(x) - L| < \epsilon \quad \text{if} \quad 0 < |x - a| < \delta$$

> **Karl Weierstrass (1815–1897)**  
> Weierstrass formalized the modern $\epsilon$-$\delta$ foundation of mathematical analysis.

#### Example 1
Prove that $\lim_{x \to 2} (3x - 5) = 1$.  
Given $\epsilon > 0$, choose $\delta = \epsilon/3$. If $0 < |x - 2| < \delta$, then $|(3x - 5) - 1| = 3|x - 2| < 3(\epsilon/3) = \epsilon$.

#### Example 3
Prove that $\lim_{x \to 3} x^2 = 9$.  
$|x^2 - 9| = |x + 3||x - 3|$. Assuming $\delta \le 1$, $|x - 3| < 1 \implies 5 < x + 3 < 7 \implies |x + 3| < 7$.  
Set $\delta = \min(1, \epsilon/7)$. Then $|x^2 - 9| < 7\delta \le \epsilon$.

> **1.4.2 & 1.4.3 DEFINITIONS (Limits at $\pm\infty$)**  
> * $\lim_{x \to +\infty} f(x) = L$: For every $\epsilon > 0$, there exists $N > 0$ such that $|f(x) - L| < \epsilon$ whenever $x > N$.  
> * $\lim_{x \to -\infty} f(x) = L$: For every $\epsilon > 0$, there exists $N < 0$ such that $|f(x) - L| < \epsilon$ whenever $x < N$.

> **1.4.4 & 1.4.5 DEFINITIONS (Infinite Limits)**  
> * $\lim_{x \to a} f(x) = +\infty$: For every $M > 0$, there exists $\delta > 0$ such that $f(x) > M$ whenever $0 < |x - a| < \delta$.  
> * $\lim_{x \to a} f(x) = -\infty$: For every $M < 0$, there exists $\delta > 0$ such that $f(x) < M$ whenever $0 < |x - a| < \delta$.

---

### QUICK CHECK EXERCISES 1.4
*(See page 90 for answers.)*
1. Fill in the blanks for definition of limit.  
2. If $0 < |x - 1| < \epsilon/2 \implies |f(x) - 5| < \epsilon$, limit statement is $\lim_{x \to 1} f(x) = 5$.  
3. Largest $\delta$ for $|5x - 10| < \epsilon \implies \delta = \epsilon/5$.  
4. Definition of limit at $+\infty$.  
5. $f(x) = 1/\sqrt{x}$ within 0.01 of 0 for $x > N \implies N = 10{,}000$.

---

### EXERCISE SET 1.4
Exercises 1–77 on $\epsilon$-$\delta$ proofs, finding $\delta$ for given $\epsilon$, $N$-proofs for limits at infinity, $M$-proofs for infinite limits, and physics applications.

#### QUICK CHECK ANSWERS 1.4
1. $\epsilon > 0$; $\delta > 0$; $0 < |x - a| < \delta$  
2. $\lim_{x \to 1} f(x) = 5$  
3. $\delta = \epsilon/5$  
4. $\epsilon > 0$; $N$; $x > N$  
5. $N = 10{,}000$  

---

## 1.5 CONTINUITY

### DEFINITION OF CONTINUITY

> **1.5.1 DEFINITION**  
> A function $f$ is said to be **continuous at $x = c$** provided the following conditions are satisfied:  
> 1. $f(c)$ is defined.  
> 2. $\lim_{x \to c} f(x)$ exists.  
> 3. $\lim_{x \to c} f(x) = f(c)$.

#### Types of Discontinuities:
* **Removable Discontinuity:** $\lim_{x \to c} f(x)$ exists, but either $f(c)$ is undefined or $f(c) \neq \lim_{x \to c} f(x)$.
* **Jump Discontinuity:** One-sided limits exist but are unequal ($\lim_{x \to c^-} f(x) \neq \lim_{x \to c^+} f(x)$).
* **Infinite Discontinuity:** One or both one-sided limits are $\pm\infty$.

> **1.5.2 DEFINITION (Continuity on a Closed Interval)**  
> A function $f$ is continuous on $[a, b]$ if:  
> 1. $f$ is continuous on $(a, b)$.  
> 2. $\lim_{x \to a^+} f(x) = f(a)$ (continuous from the right at $a$).  
> 3. $\lim_{x \to b^-} f(x) = f(b)$ (continuous from the left at $b$).

> **1.5.3 & 1.5.4 THEOREMS (Properties & Continuity of Polynomials/Rationals)**  
> * Sums, differences, products, and quotients (where denominator $\neq 0$) of continuous functions are continuous.  
> * Polynomials are continuous everywhere.  
> * Rational functions are continuous everywhere except where their denominators equal zero.

> **1.5.5 & 1.5.6 THEOREMS (Continuity of Compositions)**  
> If $\lim_{x \to c} g(x) = L$ and $f$ is continuous at $L$, then $\lim_{x \to c} f(g(x)) = f(L)$.  
> If $g$ is continuous at $c$ and $f$ is continuous at $g(c)$, then $f \circ g$ is continuous at $c$.

> **1.5.7 THEOREM (Continuity of Inverses)**  
> If $f$ is a one-to-one continuous function on its domain, then $f^{-1}$ is continuous on its domain (the range of $f$).

> **1.5.8 THEOREM (Intermediate-Value Theorem)**  
> If $f$ is continuous on a closed interval $[a, b]$ and $k$ is any number between $f(a)$ and $f(b)$, inclusive, then there is at least one number $x$ in $[a, b]$ such that $f(x) = k$.

> **1.5.9 THEOREM (Root Location)**  
> If $f$ is continuous on $[a, b]$, and if $f(a)$ and $f(b)$ are nonzero and have opposite signs, then there is at least one solution of the equation $f(x) = 0$ in the open interval $(a, b)$.

---

### QUICK CHECK EXERCISES 1.5
*(See page 101 for answers.)*
1. Three conditions for continuity at $x = c$.  
2. Given $f, g$ continuous, $f(2) = 1$, $\lim_{x \to 2} [f(x) + 4g(x)] = 13 \implies g(2) = 3, \lim_{x \to 2} g(x) = 3$.  
3. $\lim_{x \to 3} [f(x)/g(x)] = -2/5$.  
4. Discontinuities of $f(x) = \frac{x^2 - 16}{x^2 - 5x + 4} \implies x = 1, 4$.  
5. Intermediate-Value Theorem root guarantees.

---

### EXERCISE SET 1.5
Exercises 1–60 covering continuity intervals, piecewise continuity, classification of discontinuities, finding constants $k, m$ for continuity, IVT proofs, root approximation (bisection method), and application problems.

#### QUICK CHECK ANSWERS 1.5
1. $f(c)$ is defined; $\lim_{x \to c} f(x)$ exists; $\lim_{x \to c} f(x) = f(c)$  
2. (a) 3 (b) 3  
3. $-2/5$  
4. $x = 1, 4$  
5. (a) yes (b) no (c) yes (d) yes  

---

## 1.6 CONTINUITY OF TRIGONOMETRIC FUNCTIONS

### CONTINUITY THEOREMS

> **1.6.1 THEOREM**  
> If $c$ is any number in the natural domain of the stated trigonometric function, then:  
> $$\begin{aligned}
> \lim_{x \to c} \sin x &= \sin c, & \lim_{x \to c} \cos x &= \cos c, & \lim_{x \to c} \tan x &= \tan c \\
> \lim_{x \to c} \csc x &= \csc c, & \lim_{x \to c} \sec x &= \sec c, & \lim_{x \to c} \cot x &= \cot c
> \end{aligned}$$
> In particular, $\sin x$ and $\cos x$ are continuous everywhere.

---

### THE SQUEEZING THEOREM

> **1.6.2 THEOREM (The Squeezing Theorem / Sandwich Theorem)**  
> Let $f, g,$ and $h$ be functions satisfying
> $$g(x) \le f(x) \le h(x)$$
> for all $x$ in some open interval containing $c$, except possibly at $c$ itself. If
> $$\lim_{x \to c} g(x) = \lim_{x \to c} h(x) = L$$
> then
> $$\lim_{x \to c} f(x) = L$$

> **1.6.3 THEOREM (Fundamental Trigonometric Limits)**  
> (a) $$\lim_{x \to 0} \frac{\sin x}{x} = 1$$  
> (b) $$\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$$

#### Proof of (a):
Using the unit circle and sector areas for $0 < x < \pi/2$:
$$\text{Area}(\triangle OAP) \le \text{Area}(\text{sector } OAP) \le \text{Area}(\triangle OA T)$$
$$\frac{1}{2}\sin x \le \frac{1}{2}x \le \frac{1}{2}\tan x$$
Dividing by $\frac{1}{2}\sin x$ and taking reciprocals yields:
$$\cos x \le \frac{\sin x}{x} \le 1$$
Since $\lim_{x \to 0} \cos x = 1$ and $\lim_{x \to 0} 1 = 1$, by the Squeezing Theorem, $\lim_{x \to 0} \frac{\sin x}{x} = 1$.

---

### QUICK CHECK EXERCISES 1.6
*(See page 107 for answers.)*
1. Continuity on $[0, \pi/2)$ for $\sin x, \cos x, \tan x, \csc x$.  
2. Fundamental limits evaluation.  
3. Squeeze application: $3 - |x| \le f(x) \le 3 + |x| \implies f(x) \to 3$ as $x \to 0$.

---

### EXERCISE SET 1.6
Exercises 1–57 covering trigonometric limits, squeeze theorem applications, continuity of trigonometric compositions, and physics modeling.

#### QUICK CHECK ANSWERS 1.6
1. (a) yes (b) yes (c) yes (d) no  
2. (a) 1 (b) 0  
3. 3; 0  

---

## CHAPTER 1 REVIEW EXERCISES
Exercises 1–31 summarizing all limit techniques, piecewise functions, graphical limits, asymptotes, $\epsilon$-$\delta$ definitions, and Intermediate-Value Theorem applications.

---

## CHAPTER 1 MAKING CONNECTIONS (OSCULATING CIRCLES)
Explores the concept of secant circles and the osculating circle (tangent circle) to a curve at a point, analogous to tangent lines as limits of secant lines.
* Osculating circle to $y = x^2$ at $(0, 0)$ is centered at $(0, 1/2)$ with radius $1/2$.
* Formula for general even function $f(x)$:
  $$C(x) = \frac{1}{2}\left[f(0) + f(x) + \frac{x^2}{f(x) - f(0)}\right]$$
