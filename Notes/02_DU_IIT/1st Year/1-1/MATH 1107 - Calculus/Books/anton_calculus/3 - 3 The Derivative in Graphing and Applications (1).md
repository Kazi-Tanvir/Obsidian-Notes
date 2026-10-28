# CHAPTER 3: THE DERIVATIVE IN GRAPHING AND APPLICATIONS

> Derivatives can help to find the most cost-effective location for an offshore oil-drilling rig.

In this chapter we will study various applications of the derivative. For example, we will use methods of calculus to analyze functions and their graphs. In the process, we will show how calculus and graphing utilities, working together, can provide most of the important information about the behavior of functions. Another important application of the derivative will be in the solution of optimization problems. For example, if time is the main consideration in a problem, we might be interested in finding the quickest way to perform a task, and if cost is the main consideration, we might be interested in finding the least expensive way to perform a task. Mathematically, optimization problems can be reduced to finding the largest or smallest value of a function on some interval, and determining where the largest or smallest value occurs. Using the derivative, we will develop the mathematical tools necessary for solving such problems. We will also use the derivative to study the motion of a particle moving along a line, and we will show how the derivative can help us to approximate solutions of equations.

---

## 3.1 ANALYSIS OF FUNCTIONS I: INCREASE, DECREASE, AND CONCAVITY

Although graphing utilities are useful for determining the general shape of a graph, many problems require more precision than graphing utilities are capable of producing. The purpose of this section is to develop mathematical tools that can be used to determine the exact shape of a graph and the precise locations of its key features.

### INCREASING AND DECREASING FUNCTIONS

The terms *increasing*, *decreasing*, and *constant* are used to describe the behavior of a function as we travel left to right along its graph. For example, the function graphed in Figure 3.1.1 can be described as increasing to the left of $x = 0$, decreasing from $x = 0$ to $x = 2$, increasing from $x = 2$ to $x = 4$, and constant to the right of $x = 4$.

The following definition, which is illustrated in Figure 3.1.2, expresses these intuitive ideas precisely.

> **3.1.1 DEFINITION**  
> Let $f$ be defined on an interval, and let $x_1$ and $x_2$ denote points in that interval.  
> (a) $f$ is **increasing** on the interval if $f(x_1) < f(x_2)$ whenever $x_1 < x_2$.  
> (b) $f$ is **decreasing** on the interval if $f(x_1) > f(x_2)$ whenever $x_1 < x_2$.  
> (c) $f$ is **constant** on the interval if $f(x_1) = f(x_2)$ for all points $x_1$ and $x_2$.

*Note:* The definitions of "increasing," "decreasing," and "constant" describe the behavior of a function on an interval and not at a point. In particular, it is not inconsistent to say that the function in Figure 3.1.1 is decreasing on the interval $[0, 2]$ and increasing on the interval $[2, 4]$.

Figure 3.1.3 suggests that a differentiable function $f$ is increasing on any interval where each tangent line to its graph has positive slope, is decreasing on any interval where each tangent line to its graph has negative slope, and is constant on any interval where each tangent line to its graph has zero slope. This intuitive observation suggests the following important theorem that will be proved in Section 3.8.

> **3.1.2 THEOREM**  
> Let $f$ be a function that is continuous on a closed interval $[a, b]$ and differentiable on the open interval $(a, b)$.  
> (a) If $f'(x) > 0$ for every value of $x$ in $(a, b)$, then $f$ is increasing on $[a, b]$.  
> (b) If $f'(x) < 0$ for every value of $x$ in $(a, b)$, then $f$ is decreasing on $[a, b]$.  
> (c) If $f'(x) = 0$ for every value of $x$ in $(a, b)$, then $f$ is constant on $[a, b]$.

*Note:* Observe that the derivative conditions in Theorem 3.1.2 are only required to hold inside the interval $[a, b]$, even though the conclusions apply to the entire interval.

Although stated for closed intervals, Theorem 3.1.2 is applicable on any interval on which $f$ is continuous. For example, if $f$ is continuous on $[a, +\infty)$ and $f'(x) > 0$ on $(a, +\infty)$, then $f$ is increasing on $[a, +\infty)$; and if $f$ is continuous on $(-\infty, +\infty)$ and $f'(x) < 0$ on $(-\infty, +\infty)$, then $f$ is decreasing on $(-\infty, +\infty)$.

#### Example 1
Find the intervals on which $f(x) = x^2 - 4x + 3$ is increasing and the intervals on which it is decreasing.

**Solution.** The graph of $f$ in Figure 3.1.4 suggests that $f$ is decreasing for $x \le 2$ and increasing for $x \ge 2$. To confirm this, we analyze the sign of $f'$. The derivative of $f$ is
$$f'(x) = 2x - 4 = 2(x - 2)$$
It follows that
$$f'(x) < 0 \quad \text{if } x < 2$$
$$f'(x) > 0 \quad \text{if } 2 < x$$
Since $f$ is continuous everywhere, it follows from the comment after Theorem 3.1.2 that
$$f \text{ is decreasing on } (-\infty, 2]$$
$$f \text{ is increasing on } [2, +\infty)$$
These conclusions are consistent with the graph of $f$ in Figure 3.1.4.

#### Example 2
Find the intervals on which $f(x) = x^3$ is increasing and the intervals on which it is decreasing.

**Solution.** The graph of $f$ in Figure 3.1.5 suggests that $f$ is increasing over the entire $x$-axis. To confirm this, we differentiate $f$ to obtain $f'(x) = 3x^2$. Thus,
$$f'(x) > 0 \quad \text{if } x < 0$$
$$f'(x) > 0 \quad \text{if } 0 < x$$
Since $f$ is continuous everywhere,
$$f \text{ is increasing on } (-\infty, 0]$$
$$f \text{ is increasing on } [0, +\infty)$$
Since $f$ is increasing on the adjacent intervals $(-\infty, 0]$ and $[0, +\infty)$, it follows that $f$ is increasing on their union $(-\infty, +\infty)$ (see Exercise 51).

#### Example 3
(a) Use the graph of $f(x) = 3x^4 + 4x^3 - 12x^2 + 2$ in Figure 3.1.6 to make a conjecture about the intervals on which $f$ is increasing or decreasing.  
(b) Use Theorem 3.1.2 to determine whether your conjecture is correct.

**Solution (a).** The graph suggests that the function $f$ is decreasing if $x \le -2$, increasing if $-2 \le x \le 0$, decreasing if $0 \le x \le 1$, and increasing if $x \ge 1$.

**Solution (b).** Differentiating $f$ we obtain
$$f'(x) = 12x^3 + 12x^2 - 24x = 12x(x^2 + x - 2) = 12x(x + 2)(x - 1)$$
The sign analysis of $f'$ in Table 3.1.1 can be obtained using the method of test points. The conclusions in Table 3.1.1 confirm the conjecture in part (a).

#### Table 3.1.1
| Interval | $(12x)(x + 2)(x - 1)$ | $f'(x)$ | Conclusion |
| :--- | :--- | :---: | :--- |
| $x < -2$ | $(-)(-)(-)$ | $-$ | $f$ is decreasing on $(-\infty, -2]$ |
| $-2 < x < 0$ | $(-)(+)(-)$ | $+$ | $f$ is increasing on $[-2, 0]$ |
| $0 < x < 1$ | $(+)(+)(-)$ | $-$ | $f$ is decreasing on $[0, 1]$ |
| $1 < x$ | $(+)(+)(+)$ | $+$ | $f$ is increasing on $[1, +\infty)$ |

---

### CONCAVITY

Although the sign of the derivative of $f$ reveals where the graph of $f$ is increasing or decreasing, it does not reveal the direction of *curvature*. For example, the graph is increasing on both sides of the point in Figure 3.1.7, but on the left side it has an upward curvature ("holds water") and on the right side it has a downward curvature ("spills water"). On intervals where the graph of $f$ has upward curvature we say that $f$ is **concave up**, and on intervals where the graph has downward curvature we say that $f$ is **concave down**.

Figure 3.1.8 suggests two ways to characterize the concavity of a differentiable function $f$ on an open interval:
* $f$ is concave up on an open interval if its tangent lines have increasing slopes on that interval and is concave down if they have decreasing slopes.
* $f$ is concave up on an open interval if its graph lies above its tangent lines on that interval and is concave down if it lies below its tangent lines.

Our formal definition for "concave up" and "concave down" corresponds to the first of these characterizations.

> **3.1.3 DEFINITION**  
> If $f$ is differentiable on an open interval, then $f$ is said to be **concave up** on the open interval if $f'$ is increasing on that interval, and $f$ is said to be **concave down** on the open interval if $f'$ is decreasing on that interval.

Since the slopes of the tangent lines to the graph of a differentiable function $f$ are the values of its derivative $f'$, it follows from Theorem 3.1.2 (applied to $f'$ rather than $f$) that $f'$ will be increasing on intervals where $f''$ is positive and that $f'$ will be decreasing on intervals where $f''$ is negative. Thus, we have the following theorem.

> **3.1.4 THEOREM**  
> Let $f$ be twice differentiable on an open interval.  
> (a) If $f''(x) > 0$ for every value of $x$ in the open interval, then $f$ is concave up on that interval.  
> (b) If $f''(x) < 0$ for every value of $x$ in the open interval, then $f$ is concave down on that interval.

#### Example 4
Figure 3.1.4 suggests that the function $f(x) = x^2 - 4x + 3$ is concave up on the interval $(-\infty, +\infty)$. This is consistent with Theorem 3.1.4, since $f'(x) = 2x - 4$ and $f''(x) = 2$, so
$$f''(x) > 0 \quad \text{on the interval } (-\infty, +\infty)$$
Also, Figure 3.1.5 suggests that $f(x) = x^3$ is concave down on the interval $(-\infty, 0)$ and concave up on the interval $(0, +\infty)$. This agrees with Theorem 3.1.4, since $f'(x) = 3x^2$ and $f''(x) = 6x$, so
$$f''(x) < 0 \quad \text{if } x < 0 \quad \text{and} \quad f''(x) > 0 \quad \text{if } x > 0$$

---

### INFLECTION POINTS

We see from Example 4 and Figure 3.1.5 that the graph of $f(x) = x^3$ changes from concave down to concave up at $x = 0$. Points where a curve changes from concave up to concave down or vice versa are of special interest, so there is some terminology associated with them.

> **3.1.5 DEFINITION**  
> If $f$ is continuous on an open interval containing a value $x_0$, and if $f$ changes the direction of its concavity at the point $(x_0, f(x_0))$, then we say that $f$ has an **inflection point** at $x_0$, and we call the point $(x_0, f(x_0))$ on the graph of $f$ an **inflection point of $f$** (Figure 3.1.9).

#### Example 5
Figure 3.1.10 shows the graph of the function $f(x) = x^3 - 3x^2 + 1$. Use the first and second derivatives of $f$ to determine the intervals on which $f$ is increasing, decreasing, concave up, and concave down. Locate all inflection points and confirm that your conclusions are consistent with the graph.

**Solution.** Calculating the first two derivatives of $f$ we obtain
$$f'(x) = 3x^2 - 6x = 3x(x - 2)$$
$$f''(x) = 6x - 6 = 6(x - 1)$$
The sign analysis of these derivatives is shown in the following tables:

| Interval | $(3x)(x - 2)$ | $f'(x)$ | Conclusion |
| :--- | :--- | :---: | :--- |
| $x < 0$ | $(-)(-)$ | $+$ | $f$ is increasing on $(-\infty, 0]$ |
| $0 < x < 2$ | $(+)(-)$ | $-$ | $f$ is decreasing on $[0, 2]$ |
| $x > 2$ | $(+)(+)$ | $+$ | $f$ is increasing on $[2, +\infty)$ |

| Interval | $6(x - 1)$ | $f''(x)$ | Conclusion |
| :--- | :--- | :---: | :--- |
| $x < 1$ | $(-)$ | $-$ | $f$ is concave down on $(-\infty, 1)$ |
| $x > 1$ | $(+)$ | $+$ | $f$ is concave up on $(1, +\infty)$ |

The second table shows that there is an inflection point at $x = 1$, since $f$ changes from concave down to concave up at that point. The inflection point is $(1, f(1)) = (1, -1)$. All of these conclusions are consistent with the graph of $f$.

One can correctly guess from Figure 3.1.10 that the function $f(x) = x^3 - 3x^2 + 1$ has an inflection point at $x = 1$ without actually computing derivatives. However, sometimes changes in concavity are so subtle that calculus is essential to confirm their existence and identify their location.

#### Example 6
Figure 3.1.11 shows the graph of the function $f(x) = x + 2\sin x$ over the interval $[0, 2\pi]$. Use the first and second derivatives of $f$ to determine where $f$ is increasing, decreasing, concave up, and concave down. Locate all inflection points and confirm that your conclusions are consistent with the graph.

**Solution.** Calculating the first two derivatives of $f$ we obtain
$$f'(x) = 1 + 2\cos x$$
$$f''(x) = -2\sin x$$
Since $f'$ is a continuous function, it changes sign on the interval $(0, 2\pi)$ only at points where $f'(x) = 0$. These values are solutions of the equation
$$1 + 2\cos x = 0 \quad \text{or equivalently} \quad \cos x = -\frac{1}{2}$$
There are two solutions of this equation in the interval $(0, 2\pi)$, namely, $x = 2\pi/3$ and $x = 4\pi/3$. Similarly, $f''$ is a continuous function, so its sign changes in the interval $(0, 2\pi)$ will occur only at values of $x$ for which $f''(x) = 0$. These values are solutions of the equation $-2\sin x = 0$.
There is one solution of this equation in the interval $(0, 2\pi)$, namely, $x = \pi$. With the help of these "sign transition points" we obtain the sign analysis shown in the following tables:

| Interval | $f'(x) = 1 + 2\cos x$ | Conclusion |
| :--- | :---: | :--- |
| $0 < x < 2\pi/3$ | $+$ | $f$ is increasing on $[0, 2\pi/3]$ |
| $2\pi/3 < x < 4\pi/3$ | $-$ | $f$ is decreasing on $[2\pi/3, 4\pi/3]$ |
| $4\pi/3 < x < 2\pi$ | $+$ | $f$ is increasing on $[4\pi/3, 2\pi]$ |

| Interval | $f''(x) = -2\sin x$ | Conclusion |
| :--- | :---: | :--- |
| $0 < x < \pi$ | $-$ | $f$ is concave down on $(0, \pi)$ |
| $\pi < x < 2\pi$ | $+$ | $f$ is concave up on $(\pi, 2\pi)$ |

The second table shows that there is an inflection point at $x = \pi$, since $f$ changes from concave down to concave up at that point. All of these conclusions are consistent with the graph of $f$.

In the preceding examples the inflection points of $f$ occurred wherever $f''(x) = 0$. However, this is not always the case. Here is a specific example.

#### Example 7
Find the inflection points, if any, of $f(x) = x^4$.

**Solution.** Calculating the first two derivatives of $f$ we obtain
$$f'(x) = 4x^3$$
$$f''(x) = 12x^2$$
Since $f''(x)$ is positive for $x < 0$ and for $x > 0$, the function $f$ is concave up on the interval $(-\infty, 0)$ and on the interval $(0, +\infty)$. Thus, there is no change in concavity and hence no inflection point at $x = 0$, even though $f''(0) = 0$ (Figure 3.1.12).

We will see later that if a function $f$ has an inflection point at $x = x_0$ and $f''(x_0)$ exists, then $f''(x_0) = 0$. Further, we will see in Section 3.3 that an inflection point may also occur where $f''(x)$ is not defined.

---

### INFLECTION POINTS IN APPLICATIONS

Inflection points of a function $f$ are those points on the graph of $y = f(x)$ where the slopes of the tangent lines change from increasing to decreasing or vice versa (Figure 3.1.13). Since the slope of the tangent line at a point on the graph of $y = f(x)$ can be interpreted as the rate of change of $y$ with respect to $x$ at that point, we can interpret inflection points in the following way:

> *Inflection points mark the places on the curve $y = f(x)$ where the rate of change of $y$ with respect to $x$ changes from increasing to decreasing, or vice versa.*

This is a subtle idea, since we are dealing with a change in a rate of change. It can help with your understanding of this idea to realize that inflection points may have interpretations in more familiar contexts. For example, consider the statement "Oil prices rose sharply during the first half of the year but have since begun to level off." If the price of oil is plotted as a function of time of year, this statement suggests the existence of an inflection point on the graph near the end of June. (Why?) To give a more visual example, consider the flask shown in Figure 3.1.14. Suppose that water is added to the flask so that the volume increases at a constant rate with respect to the time $t$, and let us examine the rate at which the water level $y$ rises with respect to $t$. Initially, the level $y$ will rise at a slow rate because of the wide base. However, as the diameter of the flask narrows, the rate at which the level $y$ rises will increase until the level is at the narrow point in the neck. From that point on the rate at which the level rises will decrease as the diameter gets wider and wider. Thus, the narrow point in the neck is the point at which the rate of change of $y$ with respect to $t$ changes from increasing to decreasing.

---

### QUICK CHECK EXERCISES 3.1
*(See page 196 for answers.)*

1. (a) A function $f$ is increasing on $(a, b)$ if $\underline{\hspace{1.5cm}}$ whenever $a < x_1 < x_2 < b$.  
   (b) A function $f$ is decreasing on $(a, b)$ if $\underline{\hspace{1.5cm}}$ whenever $a < x_1 < x_2 < b$.  
   (c) A function $f$ is concave up on $(a, b)$ if $f'$ is $\underline{\hspace{1.5cm}}$ on $(a, b)$.  
   (d) If $f''(a)$ exists and $f$ has an inflection point at $x = a$, then $f''(a) \ \underline{\hspace{1.5cm}}$.
2. Let $f(x) = 0.1(x^3 - 3x^2 - 9x)$. Then
   $$f'(x) = 0.1(3x^2 - 6x - 9) = 0.3(x + 1)(x - 3)$$
   $$f''(x) = 0.6(x - 1)$$
   (a) Solutions to $f'(x) = 0$ are $x = \underline{\hspace{1.5cm}}$.  
   (b) The function $f$ is increasing on the interval(s) $\underline{\hspace{1.5cm}}$.  
   (c) The function $f$ is concave down on the interval(s) $\underline{\hspace{1.5cm}}$.  
   (d) $\underline{\hspace{1.5cm}}$ is an inflection point on the graph of $f$.
3. Suppose that $f(x)$ has derivative $f'(x) = x(x - 4)^2$. Then $f''(x) = (x - 4)(3x - 4)$.  
   (a) The function $f$ is increasing on the interval(s) $\underline{\hspace{1.5cm}}$.  
   (b) The function $f$ is concave up on the interval(s) $\underline{\hspace{1.5cm}}$.  
   (c) The function $f$ is concave down on the interval(s) $\underline{\hspace{1.5cm}}$.
4. Consider the statement "The rise in the cost of living slowed during the first half of the year." If we graph the cost of living versus time for the first half of the year, how does the graph reflect this statement?

#### QUICK CHECK ANSWERS 3.1
1. (a) $f(x_1) < f(x_2)$ (b) $f(x_1) > f(x_2)$ (c) increasing (d) $= 0$  
2. (a) $-1, 3$ (b) $(-\infty, -1]$ and $[3, +\infty)$ (c) $(-\infty, 1)$ (d) $(1, -1.1)$  
3. (a) $[0, +\infty)$ (b) $(-\infty, 4/3), (4, +\infty)$ (c) $(4/3, 4)$  
4. The graph is increasing and concave down.

---

### EXERCISE SET 3.1

**FOCUS ON CONCEPTS**

1. In each part, sketch the graph of a function $f$ with the stated properties, and discuss the signs of $f'$ and $f''$.  
   (a) The function $f$ is concave up and increasing on the interval $(-\infty, +\infty)$.  
   (b) The function $f$ is concave down and increasing on the interval $(-\infty, +\infty)$.  
   (c) The function $f$ is concave up and decreasing on the interval $(-\infty, +\infty)$.  
   (d) The function $f$ is concave down and decreasing on the interval $(-\infty, +\infty)$.
2. In each part, sketch the graph of a function $f$ with the stated properties.  
   (a) $f$ is increasing on $(-\infty, +\infty)$, has an inflection point at the origin, and is concave up on $(0, +\infty)$.  
   (b) $f$ is increasing on $(-\infty, +\infty)$, has an inflection point at the origin, and is concave down on $(0, +\infty)$.  
   (c) $f$ is decreasing on $(-\infty, +\infty)$, has an inflection point at the origin, and is concave up on $(0, +\infty)$.  
   (d) $f$ is decreasing on $(-\infty, +\infty)$, has an inflection point at the origin, and is concave down on $(0, +\infty)$.
3. Use the graph of the equation $y = f(x)$ in Figure Ex-3 to find the signs of $dy/dx$ and $d^2y/dx^2$ at the points $A, B,$ and $C$.
4. Use the graph of the equation $y = f'(x)$ in Figure Ex-4 to find the signs of $dy/dx$ and $d^2y/dx^2$ at the points $A, B,$ and $C$.
5. Use the graph of $y = f''(x)$ in Figure Ex-5 to determine the $x$-coordinates of all inflection points of $f$. Explain your reasoning.
6. Use the graph of $y = f'(x)$ in Figure Ex-6 to replace the question mark with $<, =,$ or $>$, as appropriate. Explain your reasoning.  
   (a) $f(0) \ ? \ f(1)$  
   (b) $f(1) \ ? \ f(2)$  
   (c) $f'(0) \ ? \ 0$  
   (d) $f'(1) \ ? \ 0$  
   (e) $f''(0) \ ? \ 0$  
   (f) $f''(2) \ ? \ 0$
7. In each part, use the graph of $y = f(x)$ in Figure Ex-7 to find the requested information.  
   (a) Find the intervals on which $f$ is increasing.  
   (b) Find the intervals on which $f$ is decreasing.  
   (c) Find the open intervals on which $f$ is concave up.  
   (d) Find the open intervals on which $f$ is concave down.  
   (e) Find all values of $x$ at which $f$ has an inflection point.
8. Use the graph in Exercise 7 to make a table that shows the signs of $f'$ and $f''$ over the intervals $(1, 2), (2, 3), (3, 4), (4, 5), (5, 6),$ and $(6, 7)$.

**9–10 A sign chart is presented for the first and second derivatives of a function $f$. Assuming that $f$ is continuous everywhere, find: (a) the intervals on which $f$ is increasing, (b) the intervals on which $f$ is decreasing, (c) the open intervals on which $f$ is concave up, (d) the open intervals on which $f$ is concave down, and (e) the $x$-coordinates of all inflection points.**

9. 
   | Interval | Sign of $f'(x)$ | Sign of $f''(x)$ |
   | :--- | :---: | :---: |
   | $x < 1$ | $-$ | $+$ |
   | $1 < x < 2$ | $+$ | $+$ |
   | $2 < x < 3$ | $+$ | $-$ |
   | $3 < x < 4$ | $-$ | $-$ |
   | $4 < x$ | $-$ | $+$ |

10. 
    | Interval | Sign of $f'(x)$ | Sign of $f''(x)$ |
    | :--- | :---: | :---: |
    | $x < 1$ | $+$ | $+$ |
    | $1 < x < 3$ | $+$ | $-$ |
    | $3 < x$ | $+$ | $+$ |

**11–14 True–False Assume that $f$ is differentiable everywhere. Determine whether the statement is true or false. Explain your answer.**

11. If $f$ is decreasing on $[0, 2]$, then $f(0) > f(1) > f(2)$.
12. If $f'(1) > 0$, then $f$ is increasing on $[0, 2]$.
13. If $f$ is increasing on $[0, 2]$, then $f'(1) > 0$.
14. If $f'$ is increasing on $[0, 1]$ and $f'$ is decreasing on $[1, 2]$, then $f$ has an inflection point at $x = 1$.

**15–26 Find: (a) the intervals on which $f$ is increasing, (b) the intervals on which $f$ is decreasing, (c) the open intervals on which $f$ is concave up, (d) the open intervals on which $f$ is concave down, and (e) the $x$-coordinates of all inflection points.**

15. $f(x) = x^2 - 3x + 8$
16. $f(x) = 5 - 4x - x^2$
17. $f(x) = (2x + 1)^3$
18. $f(x) = 5 + 12x - x^3$
19. $f(x) = 3x^4 - 4x^3$
20. $f(x) = x^4 - 5x^3 + 9x^2$
21. $f(x) = \frac{x - 2}{(x^2 - x + 1)^2}$
22. $f(x) = \frac{x}{x^2 + 2}$
23. $f(x) = \sqrt[3]{x^2 + x + 1}$
24. $f(x) = x^{4/3} - x^{1/3}$
25. $f(x) = (x^{2/3} - 1)^2$
26. $f(x) = x^{2/3} - x$

**27–32 Analyze the trigonometric function $f$ over the specified interval, stating where $f$ is increasing, decreasing, concave up, and concave down, and stating the $x$-coordinates of all inflection points. Confirm that your results are consistent with the graph of $f$ generated with a graphing utility.**

27. $f(x) = \sin x - \cos x; \quad [-\pi, \pi]$
28. $f(x) = \sec x \tan x; \quad (-\pi/2, \pi/2)$
29. $f(x) = 1 - \tan(x/2); \quad (-\pi, \pi)$
30. $f(x) = 2x + \cot x; \quad (0, \pi)$
31. $f(x) = (\sin x + \cos x)^2; \quad [-\pi, \pi]$
32. $f(x) = \sin^2 2x; \quad [0, \pi]$

**FOCUS ON CONCEPTS**

33. In parts (a)–(c), sketch a continuous curve $y = f(x)$ with the stated properties.  
    (a) $f(2) = 4, \ f'(2) = 0, \ f''(x) > 0 \text{ for all } x$  
    (b) $f(2) = 4, \ f'(2) = 0, \ f''(x) < 0 \text{ for } x < 2, \ f''(x) > 0 \text{ for } x > 2$  
    (c) $f(2) = 4, \ f''(x) < 0 \text{ for } x \neq 2 \text{ and } \lim_{x \to 2^+} f'(x) = +\infty, \ \lim_{x \to 2^-} f'(x) = -\infty$
34. In each part sketch a continuous curve $y = f(x)$ with the stated properties.  
    (a) $f(2) = 4, \ f'(2) = 0, \ f''(x) < 0 \text{ for all } x$  
    (b) $f(2) = 4, \ f'(2) = 0, \ f''(x) > 0 \text{ for } x < 2, \ f''(x) < 0 \text{ for } x > 2$  
    (c) $f(2) = 4, \ f''(x) > 0 \text{ for } x \neq 2 \text{ and } \lim_{x \to 2^+} f'(x) = -\infty, \ \lim_{x \to 2^-} f'(x) = +\infty$

**35–38 If $f$ is increasing on an interval $[0, b)$, then it follows from Definition 3.1.1 that $f(0) < f(x)$ for each $x$ in the interval $(0, b)$. Use this result in these exercises.**

35. Show that $\sqrt[3]{1 + x} < 1 + \frac{1}{3}x$ if $x > 0$, and confirm the inequality with a graphing utility. [Hint: Show that the function $f(x) = 1 + \frac{1}{3}x - \sqrt[3]{1 + x}$ is increasing on $[0, +\infty)$.]
36. Show that $x < \tan x$ if $0 < x < \pi/2$, and confirm the inequality with a graphing utility. [Hint: Show that the function $f(x) = \tan x - x$ is increasing on $[0, \pi/2)$.]
37. Use a graphing utility to make a conjecture about the relative sizes of $x$ and $\sin x$ for $x \ge 0$, and prove your conjecture.
38. Use a graphing utility to make a conjecture about the relative sizes of $1 - x^2/2$ and $\cos x$ for $x \ge 0$, and prove your conjecture. [Hint: Use the result of Exercise 37.]

**39–40 Use a graphing utility to generate the graphs of $f'$ and $f''$ over the stated interval; then use those graphs to estimate the $x$-coordinates of the inflection points of $f$, the intervals on which $f$ is concave up or down, and the intervals on which $f$ is increasing or decreasing. Check your estimates by graphing $f$.**

39. $f(x) = x^4 - 24x^2 + 12x, \quad -5 \le x \le 5$
40. $f(x) = \frac{1}{1 + x^2}, \quad -5 \le x \le 5$

**41–42 [CAS] Use a CAS to find $f''$ and to approximate the $x$-coordinates of the inflection points to six decimal places. Confirm that your answer is consistent with the graph of $f$.**

41. $f(x) = \frac{10x - 3}{3x^2 - 5x + 8}$
42. $f(x) = \frac{x^3 - 8x + 7}{\sqrt{x^2 + 1}}$

43. Use Definition 3.1.1 to prove that $f(x) = x^2$ is increasing on $[0, +\infty)$.
44. Use Definition 3.1.1 to prove that $f(x) = 1/x$ is decreasing on $(0, +\infty)$.

**FOCUS ON CONCEPTS**

**45–48 Determine whether the statements are true or false. If a statement is false, find functions for which the statement fails to hold.**

45. (a) If $f$ and $g$ are increasing on an interval, then so is $f + g$.  
    (b) If $f$ and $g$ are increasing on an interval, then so is $f \cdot g$.
46. (a) If $f$ and $g$ are concave up on an interval, then so is $f + g$.  
    (b) If $f$ and $g$ are concave up on an interval, then so is $f \cdot g$.
47. In each part, find functions $f$ and $g$ that are increasing on $(-\infty, +\infty)$ and for which $f - g$ has the stated property.  
    (a) $f - g$ is decreasing on $(-\infty, +\infty)$.  
    (b) $f - g$ is constant on $(-\infty, +\infty)$.  
    (c) $f - g$ is increasing on $(-\infty, +\infty)$.
48. In each part, find functions $f$ and $g$ that are positive and increasing on $(-\infty, +\infty)$ and for which $f/g$ has the stated property.  
    (a) $f/g$ is decreasing on $(-\infty, +\infty)$.  
    (b) $f/g$ is constant on $(-\infty, +\infty)$.  
    (c) $f/g$ is increasing on $(-\infty, +\infty)$.

49. (a) Prove that a general cubic polynomial
    $$f(x) = ax^3 + bx^2 + cx + d \quad (a \neq 0)$$
    has exactly one inflection point.  
    (b) Prove that if a cubic polynomial has three $x$-intercepts, then the inflection point occurs at the average value of the intercepts.  
    (c) Use the result in part (b) to find the inflection point of the cubic polynomial $f(x) = x^3 - 3x^2 + 2x$, and check your result by using $f''$ to determine where $f$ is concave up and concave down.
50. From Exercise 49, the polynomial $f(x) = x^3 + bx^2 + 1$ has one inflection point. Use a graphing utility to reach a conclusion about the effect of the constant $b$ on the location of the inflection point. Use $f''$ to explain what you have observed graphically.
51. Use Definition 3.1.1 to prove:  
    (a) If $f$ is increasing on the intervals $(a, c]$ and $[c, b)$, then $f$ is increasing on $(a, b)$.  
    (b) If $f$ is decreasing on the intervals $(a, c]$ and $[c, b)$, then $f$ is decreasing on $(a, b)$.
52. Use part (a) of Exercise 51 to show that $f(x) = x + \sin x$ is increasing on the interval $(-\infty, +\infty)$.
53. Use part (b) of Exercise 51 to show that $f(x) = \cos x - x$ is decreasing on the interval $(-\infty, +\infty)$.
54. Let $y = 1/(1 + x^2)$. Find the values of $x$ for which $y$ is increasing most rapidly or decreasing most rapidly.

**55–58 Suppose that water is flowing at a constant rate into the container shown. Make a rough sketch of the graph of the water level $y$ versus the time $t$. Make sure that your sketch conveys where the graph is concave up and concave down, and label the $y$-coordinates of the inflection points.**

55. Container with narrow cylinder bottom (height $y = 1$) and wide cylinder top (height $y = 2$).
56. Container shaped like a vase, wider at base and top, narrowest at $y = 1$.
57. Container conical/tapered, widest at base ($y=0$), narrowing to neck at $y=4$.
58. Flask with multiple spherical bulbs / hourglass necks at $y=1, 2, 3, 4$.

59. **Writing.** An approaching storm causes the air temperature to fall. Make a statement that indicates there is an inflection point in the graph of temperature versus time. Explain how the existence of an inflection point follows from your statement.
60. **Writing.** Explain what the sign analyses of $f'(x)$ and $f''(x)$ tell us about the graph of $y = f(x)$.

---

## 3.2 ANALYSIS OF FUNCTIONS II: RELATIVE EXTREMA; GRAPHING POLYNOMIALS

In this section we will develop methods for finding the high and low points on the graph of a function and we will discuss procedures for analyzing the graphs of polynomials.

### RELATIVE MAXIMA AND MINIMA

If we imagine the graph of a function $f$ to be a two-dimensional mountain range with hills and valleys, then the tops of the hills are called "relative maxima," and the bottoms of the valleys are called "relative minima" (Figure 3.2.1). The relative maxima are the high points in their immediate vicinity, and the relative minima are the low points. A relative maximum need not be the highest point in the entire mountain range, and a relative minimum need not be the lowest point—they are just high and low points relative to the nearby terrain. These ideas are captured in the following definition.

> **3.2.1 DEFINITION**  
> A function $f$ is said to have a **relative maximum** at $x_0$ if there is an open interval containing $x_0$ on which $f(x_0)$ is the largest value, that is, $f(x_0) \ge f(x)$ for all $x$ in the interval. Similarly, $f$ is said to have a **relative minimum** at $x_0$ if there is an open interval containing $x_0$ on which $f(x_0)$ is the smallest value, that is, $f(x_0) \le f(x)$ for all $x$ in the interval. If $f$ has either a relative maximum or a relative minimum at $x_0$, then $f$ is said to have a **relative extremum** at $x_0$.

#### Example 1
We can see from Figure 3.2.2 that:
* $f(x) = x^2$ has a relative minimum at $x = 0$ but no relative maxima.
* $f(x) = x^3$ has no relative extrema.
* $f(x) = x^3 - 3x + 3$ has a relative maximum at $x = -1$ and a relative minimum at $x = 1$.
* $f(x) = \frac{1}{2}x^4 - \frac{4}{3}x^3 - x^2 + 4x + 1$ has relative minima at $x = -1$ and $x = 2$ and a relative maximum at $x = 1$.
* $f(x) = \cos x$ has relative maxima at all even multiples of $\pi$ and relative minima at all odd multiples of $\pi$.

The relative extrema for the five functions in Example 1 occur at points where the graphs of the functions have horizontal tangent lines. Figure 3.2.3 illustrates that a relative extremum can also occur at a point where a function is not differentiable. In general, we define a **critical point** for a function $f$ to be a point in the domain of $f$ at which either the graph of $f$ has a horizontal tangent line or $f$ is not differentiable. To distinguish between the two types of critical points we call $x$ a **stationary point** of $f$ if $f'(x) = 0$. The following theorem states that the critical points for a function form a complete set of candidates for relative extrema on the interior of the domain of the function.

> **3.2.2 THEOREM**  
> Suppose that $f$ is a function defined on an open interval containing the point $x_0$. If $f$ has a relative extremum at $x = x_0$, then $x = x_0$ is a critical point of $f$; that is, either $f'(x_0) = 0$ or $f$ is not differentiable at $x_0$.

#### Example 2
Find all critical points of $f(x) = x^3 - 3x + 1$.

**Solution.** The function $f$, being a polynomial, is differentiable everywhere, so its critical points are all stationary points. To find these points we must solve the equation $f'(x) = 0$. Since
$$f'(x) = 3x^2 - 3 = 3(x + 1)(x - 1)$$
we conclude that the critical points occur at $x = -1$ and $x = 1$. This is consistent with the graph of $f$ in Figure 3.2.4.

#### Example 3
Find all critical points of $f(x) = 3x^{5/3} - 15x^{2/3}$.

**Solution.** The function $f$ is continuous everywhere and its derivative is
$$f'(x) = 5x^{2/3} - 10x^{-1/3} = 5x^{-1/3}(x - 2) = \frac{5(x - 2)}{x^{1/3}}$$
We see from this that $f'(x) = 0$ if $x = 2$ and $f'(x)$ is undefined if $x = 0$. Thus $x = 0$ and $x = 2$ are critical points and $x = 2$ is a stationary point. This is consistent with the graph of $f$ shown in Figure 3.2.5.

---

### FIRST DERIVATIVE TEST

Theorem 3.2.2 asserts that the relative extrema must occur at critical points, but it does not say that a relative extremum occurs at every critical point. For example, for the eight critical points in Figure 3.2.6, relative extrema occur at each $x_0$ in the top row but not at any $x_0$ in the bottom row. Moreover, at the critical points in the first row the derivatives have opposite signs on the two sides of $x_0$, whereas at the critical points in the second row the signs of the derivatives are the same on both sides. This suggests:
*A function $f$ has a relative extremum at those critical points where $f'$ changes sign.*

> **3.2.3 THEOREM (First Derivative Test)**  
> Suppose that $f$ is continuous at a critical point $x_0$.  
> (a) If $f'(x) > 0$ on an open interval extending left from $x_0$ and $f'(x) < 0$ on an open interval extending right from $x_0$, then $f$ has a relative maximum at $x_0$.  
> (b) If $f'(x) < 0$ on an open interval extending left from $x_0$ and $f'(x) > 0$ on an open interval extending right from $x_0$, then $f$ has a relative minimum at $x_0$.  
> (c) If $f'(x)$ has the same sign on an open interval extending left from $x_0$ as it does on an open interval extending right from $x_0$, then $f$ does not have a relative extremum at $x_0$.

**Proof of (a).** We are assuming that $f'(x) > 0$ on the interval $(a, x_0)$ and that $f'(x) < 0$ on the interval $(x_0, b)$, and we want to show that
$$f(x_0) \ge f(x)$$
for all $x$ in the interval $(a, b)$. However, the two hypotheses, together with Theorem 3.1.2 and its associated marginal note imply that $f$ is increasing on the interval $(a, x_0]$ and decreasing on the interval $[x_0, b)$. Thus, $f(x_0) \ge f(x)$ for all $x$ in $(a, b)$ with equality only at $x_0$. $\blacksquare$

#### Example 4
We showed in Example 3 that the function $f(x) = 3x^{5/3} - 15x^{2/3}$ has critical points at $x = 0$ and $x = 2$. Figure 3.2.5 suggests that $f$ has a relative maximum at $x = 0$ and a relative minimum at $x = 2$. Confirm this using the first derivative test.

**Solution.** We showed in Example 3 that
$$f'(x) = \frac{5(x - 2)}{x^{1/3}}$$
A sign analysis of this derivative is shown in Table 3.2.1. The sign of $f'$ changes from $+$ to $-$ at $x = 0$, so there is a relative maximum at that point. The sign changes from $-$ to $+$ at $x = 2$, so there is a relative minimum at that point.

#### Table 3.2.1
| Interval | $5(x - 2)/x^{1/3}$ | $f'(x)$ |
| :--- | :--- | :---: |
| $x < 0$ | $(-)/(-)$ | $+$ |
| $0 < x < 2$ | $(-)/(+)$ | $-$ |
| $x > 2$ | $(+)/(+)$ | $+$ |

---

### SECOND DERIVATIVE TEST

There is another test for relative extrema that is based on the following geometric observation: A function $f$ has a relative maximum at a stationary point if the graph of $f$ is concave down on an open interval containing that point, and it has a relative minimum if it is concave up (Figure 3.2.7).

> **3.2.4 THEOREM (Second Derivative Test)**  
> Suppose that $f$ is twice differentiable at the point $x_0$.  
> (a) If $f'(x_0) = 0$ and $f''(x_0) > 0$, then $f$ has a relative minimum at $x_0$.  
> (b) If $f'(x_0) = 0$ and $f''(x_0) < 0$, then $f$ has a relative maximum at $x_0$.  
> (c) If $f'(x_0) = 0$ and $f''(x_0) = 0$, then the test is inconclusive; that is, $f$ may have a relative maximum, a relative minimum, or neither at $x_0$.

**Proof of (a).** We are given that $f'(x_0) = 0$ and $f''(x_0) > 0$, and we want to show that $f$ has a relative minimum at $x_0$. Expressing $f''(x_0)$ as a limit and using the two given conditions we obtain
$$f''(x_0) = \lim_{x \to x_0} \frac{f'(x) - f'(x_0)}{x - x_0} = \lim_{x \to x_0} \frac{f'(x)}{x - x_0} > 0$$
This implies that for $x$ sufficiently close to but different from $x_0$ we have
$$\frac{f'(x)}{x - x_0} > 0 \tag{1}$$
Thus, there is an open interval extending left from $x_0$ and an open interval extending right from $x_0$ on which (1) holds. On the open interval extending left the denominator in (1) is negative, so $f'(x) < 0$, and on the open interval extending right the denominator is positive, so $f'(x) > 0$. It now follows from part (b) of the first derivative test (Theorem 3.2.3) that $f$ has a relative minimum at $x_0$. $\blacksquare$

**Proof of (c).** To prove this part of the theorem we need only provide functions for which $f'(x_0) = 0$ and $f''(x_0) = 0$ at some point $x_0$, but with one having a relative minimum at $x_0$, one having a relative maximum at $x_0$, and one having neither at $x_0$. Three such functions are $f(x) = x^4$ (relative minimum at $x = 0$), $f(x) = -x^4$ (relative maximum at $x = 0$), and $f(x) = x^3$ (neither a relative maximum nor a relative minimum at $x = 0$). $\blacksquare$

#### Example 5
Find the relative extrema of $f(x) = 3x^5 - 5x^3$.

**Solution.** We have
$$f'(x) = 15x^4 - 15x^2 = 15x^2(x^2 - 1) = 15x^2(x + 1)(x - 1)$$
$$f''(x) = 60x^3 - 30x = 30x(2x^2 - 1)$$
Solving $f'(x) = 0$ yields the stationary points $x = 0, x = -1,$ and $x = 1$. As shown in the following table, we can conclude from the second derivative test that $f$ has a relative maximum at $x = -1$ and a relative minimum at $x = 1$.

| Stationary Point | $30x(2x^2 - 1)$ | $f''(x)$ | Second Derivative Test |
| :---: | :---: | :---: | :--- |
| $x = -1$ | $-30$ | $-$ | $f$ has a relative maximum |
| $x = 0$ | $0$ | $0$ | Inconclusive |
| $x = 1$ | $30$ | $+$ | $f$ has a relative minimum |

The test is inconclusive at $x = 0$, so we will try the first derivative test at that point. A sign analysis of $f'$ is given in the following table:

| Interval | $15x^2(x + 1)(x - 1)$ | $f'(x)$ |
| :--- | :--- | :---: |
| $-1 < x < 0$ | $(+)(+)(-)$ | $-$ |
| $0 < x < 1$ | $(+)(+)(-)$ | $-$ |

Since there is no sign change in $f'$ at $x = 0$, there is neither a relative maximum nor a relative minimum at that point. All of this is consistent with the graph of $f$ shown in Figure 3.2.8.

---

### GEOMETRIC IMPLICATIONS OF MULTIPLICITY

Our final goal in this section is to outline a general procedure that can be used to analyze and graph polynomials. To do so, it will be helpful to understand how the graph of a polynomial behaves in the vicinity of its roots.

Recall that a root $x = r$ of a polynomial $p(x)$ has **multiplicity $m$** if $(x - r)^m$ divides $p(x)$ but $(x - r)^{m+1}$ does not. A root of multiplicity 1 is called a **simple root**. Figure 3.2.9 and the following theorem show that the behavior of a polynomial in the vicinity of a real root is determined by the multiplicity of that root.

> **3.2.5 THEOREM (The Geometric Implications of Multiplicity)**  
> Suppose that $p(x)$ is a polynomial with a root of multiplicity $m$ at $x = r$.  
> (a) If $m$ is even, then the graph of $y = p(x)$ is tangent to the $x$-axis at $x = r$, does not cross the $x$-axis there, and does not have an inflection point there.  
> (b) If $m$ is odd and greater than 1, then the graph is tangent to the $x$-axis at $x = r$, crosses the $x$-axis there, and also has an inflection point there.  
> (c) If $m = 1$ (so that the root is simple), then the graph is not tangent to the $x$-axis at $x = r$, crosses the $x$-axis there, and may or may not have an inflection point there.

#### Example 6
Make a conjecture about the behavior of the graph of
$$y = x^3(3x - 4)(x + 2)^2$$
in the vicinity of its $x$-intercepts, and test your conjecture by generating the graph.

**Solution.** The $x$-intercepts occur at $x = 0, x = 4/3,$ and $x = -2$. The root $x = 0$ has multiplicity 3, which is odd, so at that point the graph should be tangent to the $x$-axis, cross the $x$-axis, and have an inflection point there. The root $x = -2$ has multiplicity 2, which is even, so the graph should be tangent to but not cross the $x$-axis there. The root $x = 4/3$ is simple, so at that point the curve should cross the $x$-axis without being tangent to it. All of this is consistent with the graph in Figure 3.2.10.

---

### ANALYSIS OF POLYNOMIALS

Polynomials are among the simplest functions to graph and analyze. Their significant features are symmetry, intercepts, relative extrema, inflection points, and the behavior as $x \to +\infty$ and as $x \to -\infty$. Figure 3.2.11 shows the graphs of four polynomials in $x$. The graphs have properties that are common to all polynomials:
* The natural domain of a polynomial is $(-\infty, +\infty)$.
* Polynomials are continuous everywhere.
* Polynomials are differentiable everywhere, so their graphs have no corners or vertical tangent lines.
* The graph of a nonconstant polynomial eventually increases or decreases without bound as $x \to +\infty$ and as $x \to -\infty$.
* The graph of a polynomial of degree $n \ (> 2)$ has at most $n$ $x$-intercepts, at most $n - 1$ relative extrema, and at most $n - 2$ inflection points.

#### Example 7
Figure 3.2.12 shows the graph of $y = 3x^4 - 6x^3 + 2x$ produced on a graphing calculator. Confirm that the graph is not missing any significant features.

**Solution.** We can be confident that the graph shows all significant features of the polynomial because the polynomial has degree 4 and we can account for four roots, three relative extrema, and two inflection points. Moreover, the graph suggests the correct behavior as $x \to +\infty$ and as $x \to -\infty$, since
$$\lim_{x \to +\infty} (3x^4 - 6x^3 + 2x) = \lim_{x \to +\infty} 3x^4 = +\infty$$
$$\lim_{x \to -\infty} (3x^4 - 6x^3 + 2x) = \lim_{x \to -\infty} 3x^4 = +\infty$$

#### Example 8
Sketch the graph of the equation $y = x^3 - 3x + 2$ and identify the locations of the intercepts, relative extrema, and inflection points.

**Solution.**
* $x$-intercepts: Factoring yields $x^3 - 3x + 2 = (x + 2)(x - 1)^2$, which tells us that the $x$-intercepts are $x = -2$ and $x = 1$.
* $y$-intercept: Setting $x = 0$ yields $y = 2$.
* End behavior: $\lim_{x \to +\infty} (x^3 - 3x + 2) = +\infty$ and $\lim_{x \to -\infty} (x^3 - 3x + 2) = -\infty$.
* Derivatives:
  $$\frac{dy}{dx} = 3x^2 - 3 = 3(x - 1)(x + 1), \quad \frac{d^2y}{dx^2} = 6x$$
* Increase, decrease, relative extrema, inflection points: Stationary points at $x = -1$ and $x = 1$. $dy/dx$ changes from $+$ to $-$ at $x = -1$ (relative maximum at $(-1, 4)$), and changes from $-$ to $+$ at $x = 1$ (relative minimum at $(1, 0)$). $d^2y/dx^2$ changes sign from $-$ to $+$ at $x = 0$, so there is an inflection point at $(0, 2)$.
* Final sketch: Shown in Figure 3.2.14.

---

### QUICK CHECK EXERCISES 3.2
*(See page 207 for answers.)*

1. A function $f$ has a relative maximum at $x_0$ if there is an open interval containing $x_0$ on which $f(x)$ is $\underline{\hspace{1.5cm}}$ $f(x_0)$ for every $x$ in the interval.
2. Suppose that $f$ is defined everywhere and $x = 2, 3, 5, 7$ are critical points for $f$. If $f'(x)$ is positive on the intervals $(-\infty, 2)$ and $(5, 7)$, and if $f'(x)$ is negative on the intervals $(2, 3), (3, 5),$ and $(7, +\infty)$, then $f$ has relative maxima at $x = \underline{\hspace{1.5cm}}$ and $f$ has relative minima at $x = \underline{\hspace{1.5cm}}$.
3. Suppose that $f$ is defined everywhere and $x = -2$ and $x = 1$ are critical points for $f$. If $f''(x) = 2x + 1$, then $f$ has a relative $\underline{\hspace{1.5cm}}$ at $x = -2$ and $f$ has a relative $\underline{\hspace{1.5cm}}$ at $x = 1$.
4. Let $f(x) = (x^2 - 4)^2$. Then $f'(x) = 4x(x^2 - 4)$ and $f''(x) = 4(3x^2 - 4)$. Identify the locations of the (a) relative maxima, (b) relative minima, and (c) inflection points on the graph of $f$.

#### QUICK CHECK ANSWERS 3.2
1. less than or equal to  
2. $2, 7; \quad 5$  
3. maximum; minimum  
4. (a) $(0, 16)$ (b) $(-2, 0)$ and $(2, 0)$ (c) $(-2/\sqrt{3}, 64/9)$ and $(2/\sqrt{3}, 64/9)$

---

### EXERCISE SET 3.2

**FOCUS ON CONCEPTS**

1. In each part, sketch the graph of a continuous function $f$ with the stated properties.  
   (a) $f$ is concave up on the interval $(-\infty, +\infty)$ and has exactly one relative extremum.  
   (b) $f$ is concave up on the interval $(-\infty, +\infty)$ and has no relative extrema.  
   (c) The function $f$ has exactly two relative extrema on the interval $(-\infty, +\infty)$, and $f(x) \to +\infty$ as $x \to +\infty$.  
   (d) The function $f$ has exactly two relative extrema on the interval $(-\infty, +\infty)$, and $f(x) \to -\infty$ as $x \to +\infty$.
2. In each part, sketch the graph of a continuous function $f$ with the stated properties.  
   (a) $f$ has exactly one relative extremum on $(-\infty, +\infty)$, and $f(x) \to 0$ as $x \to +\infty$ and as $x \to -\infty$.  
   (b) $f$ has exactly two relative extrema on $(-\infty, +\infty)$, and $f(x) \to 0$ as $x \to +\infty$ and as $x \to -\infty$.  
   (c) $f$ has exactly one inflection point and one relative extremum on $(-\infty, +\infty)$.  
   (d) $f$ has infinitely many relative extrema, and $f(x) \to 0$ as $x \to +\infty$ and as $x \to -\infty$.
3. (a) Use both the first and second derivative tests to show that $f(x) = 3x^2 - 6x + 1$ has a relative minimum at $x = 1$.  
   (b) Use both the first and second derivative tests to show that $f(x) = x^3 - 3x + 3$ has a relative minimum at $x = 1$ and a relative maximum at $x = -1$.
4. (a) Use both the first and second derivative tests to show that $f(x) = \sin^2 x$ has a relative minimum at $x = 0$.  
   (b) Use both the first and second derivative tests to show that $g(x) = \tan^2 x$ has a relative minimum at $x = 0$.  
   (c) Give an informal verbal argument to explain without calculus why the functions in parts (a) and (b) have relative minima at $x = 0$.
5. (a) Show that both of the functions $f(x) = (x - 1)^4$ and $g(x) = x^3 - 3x^2 + 3x - 2$ have stationary points at $x = 1$.  
   (b) What does the second derivative test tell you about the nature of these stationary points?  
   (c) What does the first derivative test tell you about the nature of these stationary points?
6. (a) Show that $f(x) = 1 - x^5$ and $g(x) = 3x^4 - 8x^3$ both have stationary points at $x = 0$.  
   (b) What does the second derivative test tell you about the nature of these stationary points?  
   (c) What does the first derivative test tell you about the nature of these stationary points?

**7–14 Locate the critical points and identify which critical points are stationary points.**

7. $f(x) = 4x^4 - 16x^2 + 17$
8. $f(x) = 3x^4 + 12x$
9. $f(x) = \frac{x + 1}{x^2 + 3}$
10. $f(x) = \frac{x^2}{x^3 + 8}$
11. $f(x) = \sqrt[3]{x^2 - 25}$
12. $f(x) = x^2(x - 1)^{2/3}$
13. $f(x) = |\sin x|$
14. $f(x) = \sin |x|$

**15–18 True–False Assume that $f$ is continuous everywhere. Determine whether the statement is true or false. Explain your answer.**

15. If $f$ has a relative maximum at $x = 1$, then $f(1) \ge f(2)$.
16. If $f$ has a relative maximum at $x = 1$, then $x = 1$ is a critical point for $f$.
17. If $f''(x) > 0$, then $f$ has a relative minimum at $x = 1$.
18. If $p(x)$ is a polynomial such that $p'(x)$ has a simple root at $x = 1$, then $p$ has a relative extremum at $x = 1$.

**FOCUS ON CONCEPTS**

**19–20 The graph of a function $f(x)$ is given. Sketch graphs of $y = f'(x)$ and $y = f''(x)$.**

19. Graph of cubic-like curve with local max at $x = -1$ and local min at $x = 3$.
20. Graph of curve with local min at $x = 1$ and local max at $x = 5$.

**21–24 Use the graph of $f'$ shown in the figure to estimate all values of $x$ at which $f$ has (a) relative minima, (b) relative maxima, and (c) inflection points. (d) Draw a rough sketch of the graph of a function $f$ with the given derivative.**

21. Graph of $f'(x)$ linear decreasing crossing $x$-axis at $x = 1$.
22. Graph of $f'(x)$ inverted parabola crossing $x$-axis at $x = 1, 3$.
23. Graph of $f'(x)$ cubic crossing $x$-axis at $x = -1, 1, 3$.
24. Graph of $f'(x)$ quartic crossing $x$-axis at $x = -1, 1, 3, 5$.

**25–28 Use the given derivative to find all critical points of $f$, and at each critical point determine whether a relative maximum, relative minimum, or neither occurs. Assume in each case that $f$ is continuous everywhere.**

25. $f'(x) = x^2(x^3 - 5)$
26. $f'(x) = 4x^3 - 9x$
27. $f'(x) = \frac{2 - 3x}{\sqrt[3]{x + 2}}$
28. $f'(x) = \frac{x^2 - 7}{\sqrt[3]{x^2 + 4}}$

**29–32 Find the relative extrema using both first and second derivative tests.**

29. $f(x) = 1 + 8x - 3x^2$
30. $f(x) = x^4 - 12x^3$
31. $f(x) = \sin 2x, \quad 0 < x < \pi$
32. $f(x) = x + \sin 2x, \quad 0 < x < \pi$

**33–42 Use any method to find the relative extrema of the function $f$.**

33. $f(x) = x^4 - 4x^3 + 4x^2$
34. $f(x) = x(x - 4)^3$
35. $f(x) = x^3(x + 1)^2$
36. $f(x) = x^2(x + 1)^3$
37. $f(x) = 2x + 3x^{2/3}$
38. $f(x) = 2x + 3x^{1/3}$
39. $f(x) = \frac{x + 3}{x - 2}$
40. $f(x) = \frac{x^2}{x^4 + 16}$
41. $f(x) = |3x - x^2|$
42. $f(x) = |1 + \sqrt[3]{x}|$

**43–52 Give a graph of the polynomial and label the coordinates of the intercepts, stationary points, and inflection points. Check your work with a graphing utility.**

43. $p(x) = x^2 - 3x - 4$
44. $p(x) = 1 + 8x - x^2$
45. $p(x) = 2x^3 - 3x^2 - 36x + 5$
46. $p(x) = 2 - x + 2x^2 - x^3$
47. $p(x) = (x + 1)^2(2x - x^2)$
48. $p(x) = x^4 - 6x^2 + 5$
49. $p(x) = x^4 - 2x^3 + 2x - 1$
50. $p(x) = 4x^3 - 9x^4$
51. $p(x) = x(x^2 - 1)^2$
52. $p(x) = x(x^2 - 1)^3$

53. In each part: (i) Make a conjecture about the behavior of the graph in the vicinity of its $x$-intercepts. (ii) Make a rough sketch of the graph based on your conjecture and the limits of the polynomial as $x \to +\infty$ and as $x \to -\infty$. (iii) Compare your sketch to the graph generated with a graphing utility.  
    (a) $y = x(x - 1)(x + 1)$  
    (b) $y = x^2(x - 1)^2(x + 1)^2$  
    (c) $y = x^2(x - 1)^2(x + 1)^3$  
    (d) $y = x(x - 1)^5(x + 1)^4$
54. Sketch the graph of $y = (x - a)^m(x - b)^n$ for the stated values of $m$ and $n$, assuming that $a < b$ (six graphs in total).  
    (a) $m = 1, \ n = 1, 2, 3$  
    (b) $m = 2, \ n = 2, 3$  
    (c) $m = 3, \ n = 3$

**55–58 Find the relative extrema in the interval $0 < x < 2\pi$, and confirm that your results are consistent with the graph of $f$ generated with a graphing utility.**

55. $f(x) = |\sin 2x|$
56. $f(x) = \sqrt{3}x + 2\sin x$
57. $f(x) = \cos^2 x$
58. $f(x) = \frac{\sin x}{2 - \cos x}$

**59–60 Use a graphing utility to generate the graphs of $f'$ and $f''$ over the stated interval, and then use those graphs to estimate the $x$-coordinates of the relative extrema of $f$. Check that your estimates are consistent with the graph of $f$.**

59. $f(x) = x^4 - 24x^2 + 12x, \quad -5 \le x \le 5$
60. $f(x) = \sin\left(\frac{1}{2}x\right)\cos x, \quad -\pi/2 \le x \le \pi/2$

**61–64 [CAS] Use a CAS to graph $f'$ and $f''$, and then use those graphs to estimate the $x$-coordinates of the relative extrema of $f$. Check that your estimates are consistent with the graph of $f$.**

61. $f(x) = \frac{10x^3 - 3}{3x^2 - 5x + 8}$
62. $f(x) = \frac{x^3 - x^2}{x^2 + 1}$
63. $f(x) = \sqrt{x^4 + \cos^2 x}$
64. $f(x) = \frac{x^3 - 8x + 7}{\sqrt{x^2 + 1}}$

65. In each part, find $k$ so that $f$ has a relative extremum at the point where $x = 3$.  
    (a) $f(x) = x^2 + \frac{k}{x}$  
    (b) $f(x) = \frac{x}{x^2 + k}$
66. [CAS] (a) Use a CAS to graph the function
    $$f(x) = \frac{x^4 + 1}{x^2 + 1}$$
    and use the graph to estimate the $x$-coordinates of the relative extrema.  
    (b) Find the exact $x$-coordinates by using the CAS to solve the equation $f'(x) = 0$.
67. Let $h$ and $g$ have relative maxima at $x_0$. Prove or disprove:  
    (a) $h + g$ has a relative maximum at $x_0$  
    (b) $h - g$ has a relative maximum at $x_0$.
68. Sketch some curves that show that the three parts of the first derivative test (Theorem 3.2.3) can be false without the assumption that $f$ is continuous at $x_0$.
69. **Writing.** Discuss the relative advantages or disadvantages of using the first derivative test versus using the second derivative test to classify candidates for relative extrema on the interior of the domain of a function. Include specific examples to illustrate your points.
70. **Writing.** If $p(x)$ is a polynomial, discuss the usefulness of knowing zeros for $p, p',$ and $p''$ when determining information about the graph of $p$.

---

## 3.3 ANALYSIS OF FUNCTIONS III: RATIONAL FUNCTIONS, CUSPS, AND VERTICAL TANGENTS

In this section we will discuss procedures for graphing rational functions and other kinds of curves. We will also discuss the interplay between calculus and technology in curve sketching.

### PROPERTIES OF GRAPHS

In many problems, the properties of interest in the graph of a function are:
* symmetries
* $x$-intercepts
* relative extrema
* intervals of increase and decrease
* asymptotes
* periodicity
* $y$-intercepts
* concavity
* inflection points
* behavior as $x \to +\infty$ or as $x \to -\infty$

---

### GRAPHING RATIONAL FUNCTIONS

Recall that a rational function is a function of the form $f(x) = P(x)/Q(x)$ in which $P(x)$ and $Q(x)$ are polynomials. Graphs of rational functions are more complicated than those of polynomials because of the possibility of asymptotes and discontinuities. If $P(x)$ and $Q(x)$ have no common factors, then the information obtained in the following steps will usually be sufficient to obtain an accurate sketch of the graph of a rational function.

**Graphing a Rational Function $f(x) = P(x)/Q(x)$ if $P(x)$ and $Q(x)$ have no Common Factors**
* **Step 1. (symmetries).** Determine whether there is symmetry about the $y$-axis or the origin.
* **Step 2. ($x$- and $y$-intercepts).** Find the $x$- and $y$-intercepts.
* **Step 3. (vertical asymptotes).** Find the values of $x$ for which $Q(x) = 0$. The graph has a vertical asymptote at each such value.
* **Step 4. (sign of $f(x)$).** The only places where $f(x)$ can change sign are at the $x$-intercepts or vertical asymptotes. Mark the points on the $x$-axis at which these occur and calculate a sample value of $f(x)$ in each of the open intervals determined by these points. This will tell you whether $f(x)$ is positive or negative over that interval.
* **Step 5. (end behavior).** Determine the end behavior of the graph by computing the limits of $f(x)$ as $x \to +\infty$ and as $x \to -\infty$. If either limit has a finite value $L$, then the line $y = L$ is a horizontal asymptote.
* **Step 6. (derivatives).** Find $f'(x)$ and $f''(x)$.
* **Step 7. (conclusions and graph).** Analyze the sign changes of $f'(x)$ and $f''(x)$ to determine the intervals where $f(x)$ is increasing, decreasing, concave up, and concave down. Determine the locations of all stationary points, relative extrema, and inflection points. Use the sign analysis of $f(x)$ to determine the behavior of the graph in the vicinity of the vertical asymptotes. Sketch a graph of $f$ that exhibits these conclusions.

#### Example 1
Sketch a graph of the equation
$$y = \frac{2x^2 - 8}{x^2 - 16}$$
and identify the locations of the intercepts, relative extrema, inflection points, and asymptotes.

**Solution.**
* Symmetries: Replacing $x$ by $-x$ does not change the equation, so the graph is symmetric about the $y$-axis.
* $x$- and $y$-intercepts: Setting $y = 0$ yields $x = -2$ and $x = 2$. Setting $x = 0$ yields $y = 1/2$.
* Vertical asymptotes: $x = -4$ and $x = 4$.
* Sign of $y$: Test points $\{-5, -3, 0, 3, 5\}$ in $(-\infty, -4), (-4, -2), (-2, 2), (2, 4), (4, +\infty)$ show signs $+ , -, +, -, +$.
* End behavior: $\lim_{x \to \pm\infty} \frac{2x^2 - 8}{x^2 - 16} = 2$, so $y = 2$ is a horizontal asymptote.
* Derivatives:
  $$\frac{dy}{dx} = -\frac{48x}{(x^2 - 16)^2}, \quad \frac{d^2y}{dx^2} = \frac{48(16 + 3x^2)}{(x^2 - 16)^3}$$
* Conclusions: Increasing on $(-\infty, -4)$ and $(-4, 0]$; decreasing on $[0, 4)$ and $(4, +\infty)$. Relative maximum at $(0, 1/2)$. Concave up on $(-\infty, -4)$ and $(4, +\infty)$; concave down on $(-4, 4)$. No inflection points.

#### Example 2
Sketch a graph of $y = \frac{x^2 - 1}{x^3}$ and identify the locations of all asymptotes, intercepts, relative extrema, and inflection points.

**Solution.**
* Symmetries: Replacing $x$ by $-x$ and $y$ by $-y$ leaves the equation unchanged; symmetric about the origin.
* Intercepts: $x = -1, 1$; no $y$-intercept.
* Vertical asymptote: $x = 0$.
* Horizontal asymptote: $y = 0$ as $x \to \pm\infty$.
* Derivatives:
  $$\frac{dy}{dx} = \frac{3 - x^2}{x^4} = \frac{(\sqrt{3} + x)(\sqrt{3} - x)}{x^4}$$
  $$\frac{d^2y}{dx^2} = \frac{2(x^2 - 6)}{x^5} = \frac{2(x - \sqrt{6})(x + \sqrt{6})}{x^5}$$
* Conclusions: Relative minimum at $x = -\sqrt{3}$ (point $(-\sqrt{3}, -\frac{2}{3\sqrt{3}}) \approx (-1.73, -0.38)$), relative maximum at $x = \sqrt{3}$ (point $(\sqrt{3}, \frac{2}{3\sqrt{3}}) \approx (1.73, 0.38)$). Inflection points at $x = -\sqrt{6}$ and $x = \sqrt{6}$ (points $(\mp\sqrt{6}, \mp\frac{5}{6\sqrt{6}}) \approx (\mp 2.45, \mp 0.34)$).

---

### RATIONAL FUNCTIONS WITH OBLIQUE OR CURVILINEAR ASYMPTOTES

If the numerator of a rational function $f(x) = P(x)/Q(x)$ has greater degree than the denominator:
$$f(x) = q(x) + \frac{r(x)}{Q(x)}$$
where degree of $r(x) <$ degree of $Q(x)$. As $x \to \pm\infty$, $r(x)/Q(x) \to 0$, so $y = q(x)$ is an asymptote.
* If degree of $P(x)$ is one greater than $Q(x)$, $q(x) = mx + b$ is an **oblique (slant) asymptote**. (e.g., $f(x) = \frac{x^2 + 1}{x} = x + \frac{1}{x} \implies y = x$).
* If degree of $P(x)$ exceeds $Q(x)$ by two or more, $y = q(x)$ is a **curvilinear asymptote**. (e.g., $g(x) = \frac{x^3 - x^2 - 8}{x - 1} = x^2 - \frac{8}{x-1} \implies y = x^2$).

---

### GRAPHS WITH VERTICAL TANGENTS AND CUSPS

Figure 3.3.5 shows four curve elements where a function is continuous at $x_0$ but the secant line approaches a vertical line:
* **Vertical Tangent (Inflection Point type):** $\lim_{x \to x_0^+} f'(x) = +\infty$ and $\lim_{x \to x_0^-} f'(x) = +\infty$ (or both $-\infty$).
* **Cusp:** $f'(x) \to +\infty$ from one side and $f'(x) \to -\infty$ from the other side.

#### Example 3
Sketch the graph of $y = (x - 4)^{2/3}$.

**Solution.** $f$ is continuous everywhere, $x$-intercept $x = 4$, $y$-intercept $y = \sqrt[3]{16} \approx 2.5$.
$$\frac{dy}{dx} = \frac{2}{3(x - 4)^{1/3}}, \quad \frac{d^2y}{dx^2} = -\frac{2}{9(x - 4)^{4/3}}$$
Since $\lim_{x \to 4^+} f'(x) = +\infty$ and $\lim_{x \to 4^-} f'(x) = -\infty$, there is a vertical tangent and a cusp at $x = 4$. $f'(x) < 0$ for $x < 4$ and $f'(x) > 0$ for $x > 4$, so there is a relative minimum at $(4, 0)$. $f''(x) < 0$ for all $x \neq 4$, so the graph is concave down on $(-\infty, 4)$ and $(4, +\infty)$.

#### Example 4
Use a graphing utility to generate the graph of $f(x) = 6x^{1/3} + 3x^{4/3} = 3x^{1/3}(2 + x)$, and discuss what it tells you about relative extrema, inflection points, asymptotes, and end behavior. Use calculus to find the exact locations of all key features of the graph.

**Solution.**
* Intercepts: $x = 0, -2$; $y = 0$.
* Derivatives:
  $$f'(x) = \frac{2(2x + 1)}{x^{2/3}}, \quad f''(x) = \frac{4(x - 1)}{3x^{5/3}}$$
* Stationary point at $x = -1/2$ (relative minimum); non-differentiable critical point at $x = 0$.
* At $x = 0$, $\lim_{x \to 0^+} f'(x) = +\infty$ and $\lim_{x \to 0^-} f'(x) = +\infty$, so there is a vertical tangent and an inflection point at $(0, 0)$.
* At $x = 1$, $f''(x)$ changes sign from $-$ to $+$, so $(1, 9)$ is another inflection point.

---

### QUICK CHECK EXERCISES 3.3
*(See page 216 for answers.)*

1. Let $f(x) = \frac{3(x + 1)(x - 3)}{(x + 2)(x - 4)}$. Given that
   $$f'(x) = \frac{-30(x - 1)}{(x + 2)^2(x - 4)^2}, \quad f''(x) = \frac{90(x^2 - 2x + 4)}{(x + 2)^3(x - 4)^3}$$
   determine the following properties of the graph of $f$:  
   (a) The $x$- and $y$-intercepts are $\underline{\hspace{1.5cm}}$.  
   (b) The vertical asymptotes are $\underline{\hspace{1.5cm}}$.  
   (c) The horizontal asymptote is $\underline{\hspace{1.5cm}}$.  
   (d) The graph is above the $x$-axis on the intervals $\underline{\hspace{1.5cm}}$.  
   (e) The graph is increasing on the intervals $\underline{\hspace{1.5cm}}$.  
   (f) The graph is concave up on the intervals $\underline{\hspace{1.5cm}}$.  
   (g) The relative maximum point on the graph is $\underline{\hspace{1.5cm}}$.
2. Let $f(x) = \frac{x^2 - 4}{x^{8/3}}$. Given that
   $$f'(x) = \frac{-2(x^2 - 16)}{3x^{11/3}}, \quad f''(x) = \frac{2(5x^2 - 176)}{9x^{14/3}}$$
   determine the following properties of the graph of $f$:  
   (a) The $x$-intercepts are $\underline{\hspace{1.5cm}}$.  
   (b) The vertical asymptote is $\underline{\hspace{1.5cm}}$.  
   (c) The horizontal asymptote is $\underline{\hspace{1.5cm}}$.  
   (d) The graph is above the $x$-axis on the intervals $\underline{\hspace{1.5cm}}$.  
   (e) The graph is increasing on the intervals $\underline{\hspace{1.5cm}}$.  
   (f) The graph is concave up on the intervals $\underline{\hspace{1.5cm}}$.  
   (g) Inflection points occur at $x = \underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 3.3
1. (a) $(-1, 0), (3, 0), (0, 9/8)$ (b) $x = -2$ and $x = 4$ (c) $y = 3$ (d) $(-\infty, -2), (-1, 3),$ and $(4, +\infty)$ (e) $(-\infty, -2)$ and $(-2, 1]$ (f) $(-\infty, -2)$ and $(4, +\infty)$ (g) $(1, 4/3)$  
2. (a) $(-2, 0), (2, 0)$ (b) $x = 0$ (c) $y = 0$ (d) $(-\infty, -2)$ and $(2, +\infty)$ (e) $(-\infty, -4]$ and $(0, 4]$ (f) $(-\infty, -4\sqrt{11}/5)$ and $(4\sqrt{11}/5, +\infty)$ (g) $\pm 4\sqrt{11}/5 \approx \pm 5.93$

---

### EXERCISE SET 3.3

**1–14 Give a graph of the rational function and label the coordinates of the stationary points and inflection points. Show the horizontal and vertical asymptotes and label them with their equations. Label point(s), if any, where the graph crosses a horizontal asymptote. Check your work with a graphing utility.**

1. $y = \frac{2x - 6}{4 - x}$
2. $y = \frac{8}{x^2 - 4}$
3. $y = \frac{x}{x^2 - 4}$
4. $y = \frac{x^2}{x^2 - 4}$
5. $y = \frac{x^2}{x^2 + 4}$
6. $y = \frac{(x^2 - 1)^2}{x^4 + 1}$
7. $y = \frac{x^3 + 1}{x^3 - 1}$
8. $y = 2 - \frac{1}{3x^2 + x^3}$
9. $y = \frac{4}{x^2} - \frac{2}{x} + 3$
10. $y = \frac{3(x + 1)^2}{(x - 1)^2}$
11. $y = \frac{(3x + 1)^2}{(x - 1)^2}$
12. $y = 3 + \frac{x + 1}{(x - 1)^4}$
13. $y = \frac{x^2 + x}{1 - x^2}$
14. $y = \frac{x^2}{1 - x^3}$

**15–16 In each part, make a rough sketch of the graph using asymptotes and appropriate limits but no derivatives. Compare your graph to that generated with a graphing utility.**

15. (a) $y = \frac{3x^2 - 8}{x^2 - 4}$  
    (b) $y = \frac{x^2 + 2x}{x^2 - 1}$
16. (a) $y = \frac{2x - x^2}{x^2 + x - 2}$  
    (b) $y = \frac{x^2}{x^2 - x - 2}$

17. Show that $y = x + 3$ is an oblique asymptote of the graph of $f(x) = x^2/(x - 3)$. Sketch the graph of $y = f(x)$ showing this asymptotic behavior.
18. Show that $y = 3 - x^2$ is a curvilinear asymptote of the graph of $f(x) = (2 + 3x - x^3)/x$. Sketch the graph of $y = f(x)$ showing this asymptotic behavior.

**19–24 Sketch a graph of the rational function and label the coordinates of the stationary points and inflection points. Show the horizontal, vertical, oblique, and curvilinear asymptotes and label them with their equations. Label point(s), if any, where the graph crosses an asymptote. Check your work with a graphing utility.**

19. $y = x^2 - \frac{1}{x}$
20. $y = \frac{x^2 - 2}{x}$
21. $y = \frac{(x - 2)^3}{x^2}$
22. $y = x - \frac{1}{x} - \frac{1}{x^2}$
23. $y = \frac{x^3 - 4x - 8}{x + 2}$
24. $y = \frac{x^5}{x^2 + 1}$

**FOCUS ON CONCEPTS**

25. In each part, match the function with graphs I–VI:  
    (a) $x^{1/3}$  
    (b) $x^{1/4}$  
    (c) $x^{1/5}$  
    (d) $x^{2/5}$  
    (e) $x^{4/3}$  
    (f) $x^{-1/3}$
26. Sketch the general shape of the graph of $y = x^{1/n}$, and then explain in words what happens to the shape of the graph as $n$ increases if  
    (a) $n$ is a positive even integer  
    (b) $n$ is a positive odd integer.

**27–30 True–False Determine whether the statement is true or false. Explain your answer.**

27. Suppose that $f(x) = P(x)/Q(x)$, where $P$ and $Q$ are polynomials with no common factors. If $y = 5$ is a horizontal asymptote for the graph of $f$, then $P$ and $Q$ have the same degree.
28. If the graph of $f$ has a vertical asymptote at $x = 1$, then $f$ cannot be continuous at $x = 1$.
29. If the graph of $f'$ has a vertical asymptote at $x = 1$, then $f$ cannot be continuous at $x = 1$.
30. If the graph of $f$ has a cusp at $x = 1$, then $f$ cannot have an inflection point at $x = 1$.

**31–38 Give a graph of the function and identify the locations of all critical points and inflection points. Check your work with a graphing utility.**

31. $y = \sqrt{4x^2 - 1}$
32. $y = \sqrt[3]{x^2 - 4}$
33. $y = 2x + 3x^{2/3}$
34. $y = 2x^2 - 3x^{4/3}$
35. $y = 4x^{1/3} - x^{4/3}$
36. $y = 5x^{2/3} + x^{5/3}$
37. $y = \frac{8 + x}{2 + \sqrt[3]{x}}$
38. $y = \frac{8(\sqrt{x} - 1)}{x}$

**39–44 Give a graph of the function and identify the locations of all relative extrema and inflection points. Check your work with a graphing utility.**

39. $y = x + \sin x$
40. $y = x - \tan x$
41. $y = \sqrt{3}\cos x + \sin x$
42. $y = \sin x + \cos x$
43. $y = \sin^2 x - \cos x, \quad -\pi \le x \le 3\pi$
44. $y = \sqrt{\tan x}, \quad 0 \le x < \pi/2$

**FOCUS ON CONCEPTS**

45. The accompanying figure shows the graph of the derivative of a function $h$ that is defined and continuous on the interval $(-\infty, +\infty)$. Assume that the graph of $h'$ has a vertical asymptote at $x = 3$ and that
    $$h'(x) \to 0^+ \text{ as } x \to -\infty, \quad h'(x) \to -\infty \text{ as } x \to +\infty$$
    (a) What are the critical points for $h(x)$?  
    (b) Identify the intervals on which $h(x)$ is increasing.  
    (c) Identify the $x$-coordinates of relative extrema for $h(x)$ and classify each as a relative maximum or relative minimum.  
    (d) Estimate the $x$-coordinates of inflection points for $h(x)$.
46. Let $f(x) = (1 - 2x)h(x)$, where $h(x)$ is as given in Exercise 45. Suppose that $x = 5$ is a critical point for $f(x)$.  
    (a) Estimate $h(5)$.  
    (b) Use the second derivative test to determine whether $f(x)$ has a relative maximum or a relative minimum at $x = 5$.
47. A rectangular plot of land is to be fenced off so that the area enclosed will be $400\text{ ft}^2$. Let $L$ be the length of fencing needed and $x$ the length of one side of the rectangle. Show that $L = 2x + 800/x$ for $x > 0$, and sketch the graph of $L$ versus $x$ for $x > 0$.
48. A box with a square base and open top is to be made from sheet metal so that its volume is $500\text{ in}^3$. Let $S$ be the area of the surface of the box and $x$ the length of a side of the square base. Show that $S = x^2 + 2000/x$ for $x > 0$, and sketch the graph of $S$ versus $x$ for $x > 0$.
49. The accompanying figure shows a computer-generated graph of the polynomial $y = 0.1x^5(x - 1)$ using a viewing window of $[-2, 2.5] \times [-1, 5]$. Show that the choice of the vertical scale caused the computer to miss important features of the graph. Find the features that were missed and make your own sketch of the graph that shows the missing features.
50. The accompanying figure shows a computer-generated graph of the polynomial $y = 0.1x^5(x + 1)^2$ using a viewing window of $[-2, 1.5] \times [-0.2, 0.2]$. Show that the choice of the vertical scale caused the computer to miss important features of the graph. Find the features that were missed and make your own sketch of the graph that shows the missing features.
51. **Writing.** Suppose that $x = x_0$ is a point at which a function $f$ is continuous but not differentiable and that $f'(x)$ approaches different finite limits as $x$ approaches $x_0$ from either side. Invent your own term to describe the graph of $f$ at such a point and discuss the appropriateness of your term.
52. **Writing.** Suppose that the graph of a function $f$ is obtained using a graphing utility. Discuss the information that calculus techniques can provide about $f$ to add to what can already be inferred about $f$ from the graph as shown on your utility's display.

---

## 3.4 ABSOLUTE MAXIMA AND MINIMA

At the beginning of Section 3.2 we observed that if the graph of a function $f$ is viewed as a two-dimensional mountain range (Figure 3.2.1), then the relative maxima and minima correspond to the tops of the hills and the bottoms of the valleys; that is, they are the high and low points in their immediate vicinity. In this section we will be concerned with the more encompassing problem of finding the highest and lowest points over the entire mountain range, that is, we will be looking for the top of the highest hill and the bottom of the deepest valley. In mathematical terms, we will be looking for the largest and smallest values of a function over an interval.

### ABSOLUTE EXTREMA

> **3.4.1 DEFINITION**  
> Consider an interval in the domain of a function $f$ and a point $x_0$ in that interval. We say that $f$ has an **absolute maximum** at $x_0$ if $f(x) \le f(x_0)$ for all $x$ in the interval, and we say that $f$ has an **absolute minimum** at $x_0$ if $f(x_0) \le f(x)$ for all $x$ in the interval. We say that $f$ has an **absolute extremum** at $x_0$ if it has either an absolute maximum or an absolute minimum at that point.

---

### THE EXTREME VALUE THEOREM

> **3.4.2 THEOREM (Extreme-Value Theorem)**  
> If a function $f$ is continuous on a finite closed interval $[a, b]$, then $f$ has both an **absolute maximum** and an **absolute minimum** on $[a, b]$.

*Remark:* The Extreme-Value Theorem is an example of an *existence theorem*. Such theorems state conditions under which certain objects exist, in this case absolute extrema.

> **3.4.3 THEOREM**  
> If $f$ has an absolute extremum on an open interval $(a, b)$, then it must occur at a critical point of $f$.

**Proof.** If $f$ has an absolute maximum on $(a, b)$ at $x_0$, then $f(x_0)$ is also a relative maximum for $f$; for if $f(x_0)$ is the largest value of $f$ on all $(a, b)$, then $f(x_0)$ is certainly the largest value for $f$ in the immediate vicinity of $x_0$. Thus, $x_0$ is a critical point of $f$ by Theorem 3.2.2. The proof for absolute minima is similar. $\blacksquare$

**A Procedure for Finding the Absolute Extrema of a Continuous Function $f$ on a Finite Closed Interval $[a, b]$**
* **Step 1.** Find the critical points of $f$ in $(a, b)$.
* **Step 2.** Evaluate $f$ at all the critical points and at the endpoints $a$ and $b$.
* **Step 3.** The largest of the values in Step 2 is the absolute maximum value of $f$ on $[a, b]$ and the smallest value is the absolute minimum.

#### Example 1
Find the absolute maximum and minimum values of the function $f(x) = 2x^3 - 15x^2 + 36x$ on the interval $[1, 5]$, and determine where these values occur.

**Solution.** $f'(x) = 6x^2 - 30x + 36 = 6(x - 2)(x - 3) = 0 \implies x = 2, 3$.  
Evaluating $f$ at the endpoints and critical points:
$$f(1) = 23, \quad f(2) = 28, \quad f(3) = 27, \quad f(5) = 55$$
Absolute minimum is $23$ at $x = 1$; absolute maximum is $55$ at $x = 5$.

#### Example 2
Find the absolute extrema of $f(x) = 6x^{4/3} - 3x^{1/3}$ on the interval $[-1, 1]$, and determine where these values occur.

**Solution.** $f'(x) = 8x^{1/3} - x^{-2/3} = \frac{8x - 1}{x^{2/3}}$. Critical points in $(-1, 1)$ are $x = 1/8$ (stationary point) and $x = 0$ (non-differentiable).
$$f(-1) = 9, \quad f(0) = 0, \quad f(1/8) = -9/8, \quad f(1) = 3$$
Absolute minimum is $-9/8$ at $x = 1/8$; absolute maximum is $9$ at $x = -1$.

---

### ABSOLUTE EXTREMA ON INFINITE INTERVALS

#### Table 3.4.2: Absolute Extrema on Infinite Intervals
| Limits | Conclusion if $f$ is continuous everywhere |
| :--- | :--- |
| $\lim_{x \to -\infty} f(x) = +\infty$ and $\lim_{x \to +\infty} f(x) = +\infty$ | $f$ has an absolute minimum but no absolute maximum on $(-\infty, +\infty)$. |
| $\lim_{x \to -\infty} f(x) = -\infty$ and $\lim_{x \to +\infty} f(x) = -\infty$ | $f$ has an absolute maximum but no absolute minimum on $(-\infty, +\infty)$. |
| $\lim_{x \to -\infty} f(x) = -\infty$ and $\lim_{x \to +\infty} f(x) = +\infty$ | $f$ has neither an absolute maximum nor an absolute minimum on $(-\infty, +\infty)$. |
| $\lim_{x \to -\infty} f(x) = +\infty$ and $\lim_{x \to +\infty} f(x) = -\infty$ | $f$ has neither an absolute maximum nor an absolute minimum on $(-\infty, +\infty)$. |

#### Example 3
What can you say about the existence of absolute extrema on $(-\infty, +\infty)$ for polynomials?

**Solution.** If $p(x)$ is of odd degree, the limits at $\pm\infty$ have opposite signs, so there are no absolute extrema. If $p(x)$ is of even degree with positive leading coefficient, both limits are $+\infty$ (absolute minimum exists, no absolute maximum). If leading coefficient is negative, both limits are $-\infty$ (absolute maximum exists, no absolute minimum).

#### Example 4
Determine by inspection whether $p(x) = 3x^4 + 4x^3$ has any absolute extrema. If so, find them and state where they occur.

**Solution.** Even degree, positive leading coefficient $\implies$ absolute minimum exists.
$$p'(x) = 12x^3 + 12x^2 = 12x^2(x + 1) = 0 \implies x = 0, -1$$
$$p(0) = 0, \quad p(-1) = -1$$
Absolute minimum is $-1$ at $x = -1$.

---

### ABSOLUTE EXTREMA ON OPEN INTERVALS

#### Table 3.4.3: Absolute Extrema on Open Intervals $(a, b)$
| Limits | Conclusion if $f$ is continuous on $(a, b)$ |
| :--- | :--- |
| $\lim_{x \to a^+} f(x) = +\infty$ and $\lim_{x \to b^-} f(x) = +\infty$ | $f$ has an absolute minimum but no absolute maximum on $(a, b)$. |
| $\lim_{x \to a^+} f(x) = -\infty$ and $\lim_{x \to b^-} f(x) = -\infty$ | $f$ has an absolute maximum but no absolute minimum on $(a, b)$. |
| $\lim_{x \to a^+} f(x) = -\infty$ and $\lim_{x \to b^-} f(x) = +\infty$ | $f$ has neither an absolute maximum nor an absolute minimum on $(a, b)$. |
| $\lim_{x \to a^+} f(x) = +\infty$ and $\lim_{x \to b^-} f(x) = -\infty$ | $f$ has neither an absolute maximum nor an absolute minimum on $(a, b)$. |

#### Example 5
Determine whether the function $f(x) = \frac{1}{x^2 - x}$ has any absolute extrema on the interval $(0, 1)$. If so, find them and state where they occur.

**Solution.** As $x \to 0^+$, $f(x) \to -\infty$; as $x \to 1^-$, $f(x) \to -\infty$. Thus $f$ has an absolute maximum on $(0, 1)$.
$$f'(x) = -\frac{2x - 1}{(x^2 - x)^2} = 0 \implies x = 1/2$$
Absolute maximum is $f(1/2) = \frac{1}{1/4 - 1/2} = -4$ at $x = 1/2$.

---

### ABSOLUTE EXTREMA OF FUNCTIONS WITH ONE RELATIVE EXTREMUM

> **3.4.4 THEOREM**  
> Suppose that $f$ is continuous and has exactly one relative extremum on an interval, say at $x_0$.  
> (a) If $f$ has a relative minimum at $x_0$, then $f(x_0)$ is the absolute minimum of $f$ on the interval.  
> (b) If $f$ has a relative maximum at $x_0$, then $f(x_0)$ is the absolute maximum of $f$ on the interval.

#### Example 6
Find the absolute extrema, if any, of the function $f(x) = x^3 - 3x^2 + 4$ on the interval $(0, +\infty)$.

**Solution.** $\lim_{x \to +\infty} f(x) = +\infty$ (no absolute max). $f'(x) = 3x(x - 2) = 0 \implies x = 0, 2$. Only $x = 2$ lies in $(0, +\infty)$. $f''(2) = 6 > 0$, so $x = 2$ is a relative minimum. By Theorem 3.4.4, $f(2) = 0$ is the absolute minimum on $(0, +\infty)$.

---

### QUICK CHECK EXERCISES 3.4
*(See page 224 for answers.)*

1. Use the accompanying graph to find the $x$-coordinates of the relative extrema and absolute extrema of $f$ on $[0, 6]$.
2. Suppose that a function $f$ is continuous on $[-4, 4]$ and has critical points at $x = -3, 0, 2$. Use the accompanying table to determine the absolute maximum and absolute minimum values, if any, for $f$ on the indicated intervals:  
   (a) $[1, 4]$ (b) $[-2, 2]$ (c) $[-4, 4]$ (d) $(-4, 4)$  
   *Table values:* $f(-4)=2224, f(-3)=-1333, f(-2)=0, f(-1)=1603, f(0)=2096, f(1)=2293, f(2)=2400, f(3)=2717, f(4)=6064$.
3. Let $f(x) = x^3 - 3x^2 - 9x + 25$. Use the derivative $f'(x) = 3(x + 1)(x - 3)$ to determine the absolute maximum and absolute minimum values, if any, for $f$ on each of the given intervals:  
   (a) $[0, 4]$ (b) $[-2, 4]$ (c) $[-4, 2]$ (d) $[-5, 10]$ (e) $(-5, 4)$

#### QUICK CHECK ANSWERS 3.4
1. There is a relative minimum at $x = 3$, a relative maximum at $x = 1$, an absolute minimum at $x = 3$, and an absolute maximum at $x = 6$.  
2. (a) max, 6064; min, 2293 (b) max, 2400; min, 0 (c) max, 6064; min, $-1333$ (d) no max; min, $-1333$  
3. (a) max, $f(0) = 25$; min, $f(3) = -2$ (b) max, $f(-1) = 30$; min, $f(3) = -2$ (c) max, $f(-1) = 30$; min, $f(-4) = -51$ (d) max, $f(10) = 635$; min, $f(-5) = -130$ (e) max, $f(-1) = 30$; no min

---

### EXERCISE SET 3.4

**FOCUS ON CONCEPTS**

**1–2 Use the graph to find $x$-coordinates of the relative extrema and absolute extrema of $f$ on $[0, 7]$.**

1. Graph of continuous function on $[0, 7]$ with peaks and valleys.
2. Graph of continuous function on $[0, 7]$ with peaks and valleys.

3. In each part, sketch the graph of a continuous function $f$ with the stated properties on the interval $[0, 10]$.  
   (a) $f$ has an absolute minimum at $x = 0$ and an absolute maximum at $x = 10$.  
   (b) $f$ has an absolute minimum at $x = 2$ and an absolute maximum at $x = 7$.  
   (c) $f$ has relative minima at $x = 1$ and $x = 8$, has relative maxima at $x = 3$ and $x = 7$, has an absolute minimum at $x = 5$, and has an absolute maximum at $x = 10$.
4. In each part, sketch the graph of a continuous function $f$ with the stated properties on the interval $(-\infty, +\infty)$.  
   (a) $f$ has no relative extrema or absolute extrema.  
   (b) $f$ has an absolute minimum at $x = 0$ but no absolute maximum.  
   (c) $f$ has an absolute maximum at $x = -5$ and an absolute minimum at $x = 5$.
5. Let
   $$f(x) = \begin{cases} \frac{1}{1 - x}, & 0 \le x < 1 \\ 0, & x = 1 \end{cases}$$
   Explain why $f$ has a minimum value but no maximum value on the closed interval $[0, 1]$.
6. Let
   $$f(x) = \begin{cases} x, & 0 < x < 1 \\ \frac{1}{2}, & x = 0, 1 \end{cases}$$
   Explain why $f$ has neither a minimum value nor a maximum value on the closed interval $[0, 1]$.

**7–16 Find the absolute maximum and minimum values of $f$ on the given closed interval, and state where those values occur.**

7. $f(x) = 4x^2 - 12x + 10; \quad [1, 2]$
8. $f(x) = 8x - x^2; \quad [0, 6]$
9. $f(x) = (x - 2)^3; \quad [1, 4]$
10. $f(x) = 2x^3 + 3x^2 - 12x; \quad [-3, 2]$
11. $f(x) = \frac{3x}{\sqrt{4x^2 + 1}}; \quad [-1, 1]$
12. $f(x) = (x^2 + x)^{2/3}; \quad [-2, 3]$
13. $f(x) = x - 2\sin x; \quad [-\pi/4, \pi/2]$
14. $f(x) = \sin x - \cos x; \quad [0, \pi]$
15. $f(x) = 1 + |9 - x^2|; \quad [-5, 1]$
16. $f(x) = |6 - 4x|; \quad [-3, 3]$

**17–20 True–False Determine whether the statement is true or false. Explain your answer.**

17. If a function $f$ is continuous on $[a, b]$, then $f$ has an absolute maximum on $[a, b]$.
18. If a function $f$ is continuous on $(a, b)$, then $f$ has an absolute minimum on $(a, b)$.
19. If a function $f$ has an absolute minimum on $(a, b)$, then there is a critical point of $f$ in $(a, b)$.
20. If a function $f$ is continuous on $[a, b]$ and $f$ has no relative extreme values in $(a, b)$, then the absolute maximum value of $f$ exists and occurs either at $x = a$ or at $x = b$.

**21–28 Find the absolute maximum and minimum values of $f$, if any, on the given interval, and state where those values occur.**

21. $f(x) = x^2 - x - 2; \quad (-\infty, +\infty)$
22. $f(x) = 3 - 4x - 2x^2; \quad (-\infty, +\infty)$
23. $f(x) = 4x^3 - 3x^4; \quad (-\infty, +\infty)$
24. $f(x) = x^4 + 4x; \quad (-\infty, +\infty)$
25. $f(x) = 2x^3 - 6x + 2; \quad (-\infty, +\infty)$
26. $f(x) = x^3 - 9x + 1; \quad (-\infty, +\infty)$
27. $f(x) = \frac{x^2 + 1}{x + 1}; \quad (-5, -1)$
28. $f(x) = \frac{x - 2}{x + 1}; \quad (-1, 5]$

**29–38 Use a graphing utility to estimate the absolute maximum and minimum values of $f$, if any, on the stated interval, and then use calculus methods to find the exact values.**

29. $f(x) = (x^2 - 2x)^2; \quad (-\infty, +\infty)$
30. $f(x) = (x - 1)^2(x + 2)^2; \quad (-\infty, +\infty)$
31. $f(x) = x^{2/3}(20 - x); \quad [-1, 20]$
32. $f(x) = \frac{x}{x^2 + 2}; \quad [-1, 4]$
33. $f(x) = 1 + \frac{1}{x}; \quad (0, +\infty)$
34. $f(x) = \frac{2x^2 - 3x + 3}{x^2 - 2x + 2}; \quad [1, +\infty)$
35. $f(x) = \frac{2 - \cos x}{\sin x}; \quad [\pi/4, 3\pi/4]$
36. $f(x) = \sin^2 x + \cos x; \quad [-\pi, \pi]$
37. $f(x) = \sin(\cos x); \quad [0, 2\pi]$
38. $f(x) = \cos(\sin x); \quad [0, \pi]$

39. Find the absolute maximum and minimum values of
    $$f(x) = \begin{cases} 4x - 2, & x < 1 \\ (x - 2)(x - 3), & x \ge 1 \end{cases}$$
    on $[1/2, 7/2]$.
40. Let $f(x) = x^2 + px + q$. Find the values of $p$ and $q$ such that $f(1) = 3$ is an extreme value of $f$ on $[0, 2]$. Is this value a maximum or minimum?

**41–42 If $f$ is a periodic function, then the locations of all absolute extrema on the interval $(-\infty, +\infty)$ can be obtained by finding the locations of the absolute extrema for one period and using the periodicity to locate the rest. Use this idea in these exercises to find the absolute maximum and minimum values of the function, and state the $x$-values at which they occur.**

41. $f(x) = 2\cos x + \cos 2x$
42. $f(x) = 3\cos(x/3) + 2\cos(x/2)$

**43–44 One way of proving that $f(x) \le g(x)$ for all $x$ in a given interval is to show that $0 \le g(x) - f(x)$ for all $x$ in the interval; and one way of proving the latter inequality is to show that the absolute minimum value of $g(x) - f(x)$ on the interval is nonnegative. Use this idea to prove the inequalities in these exercises.**

43. Prove that $\sin x \le x$ for all $x$ in the interval $[0, 2\pi]$.
44. Prove that $\cos x \ge 1 - (x^2/2)$ for all $x$ in the interval $[0, 2\pi]$.

45. What is the smallest possible slope for a tangent to the graph of the equation $y = x^3 - 3x^2 + 5x$?
46. (a) Show that $f(x) = \sec x + \csc x$ has a minimum value but no maximum value on the interval $(0, \pi/2)$.  
    (b) Find the minimum value in part (a).
47. [CAS] Show that the absolute minimum value of
    $$f(x) = x^2 + \frac{x^2}{(8 - x)^2}, \quad x > 8$$
    occurs at $x = 10$ by using a CAS to find $f'(x)$ and to solve the equation $f'(x) = 0$.
48. [CAS] The vertical displacement $f(t)$ of a cork bobbing up and down on the ocean's surface may be modeled by the function
    $$f(t) = A\cos t + B\sin t$$
    where $A > 0$ and $B > 0$. Use a CAS to find the maximum and minimum values of $f(t)$ in terms of $A$ and $B$.
49. Suppose that the equations of motion of a paper airplane during the first 12 seconds of flight are
    $$x = t - 2\sin t, \quad y = 2 - 2\cos t \quad (0 \le t \le 12)$$
    What are the highest and lowest points in the trajectory, and when is the airplane at those points?
50. The accompanying figure shows the path of a fly whose equations of motion are
    $$x = \frac{\cos t}{2 + \sin t}, \quad y = 3 + \sin(2t) - 2\sin^2 t \quad (0 \le t \le 2\pi)$$
    (a) How high and low does it fly?  
    (b) How far left and right of the origin does it fly?
51. Let $f(x) = ax^2 + bx + c$, where $a > 0$. Prove that $f(x) \ge 0$ for all $x$ if and only if $b^2 - 4ac \le 0$. [Hint: Find the minimum of $f(x)$.]
52. Prove Theorem 3.4.3 in the case where the extreme value is a minimum.
53. **Writing.** Suppose that $f$ is continuous and positive-valued everywhere and that the $x$-axis is an asymptote for the graph of $f$, both as $x \to -\infty$ and as $x \to +\infty$. Explain why $f$ cannot have an absolute minimum but may have a relative minimum.
54. **Writing.** Explain the difference between a relative maximum and an absolute maximum. Sketch a graph that illustrates a function with a relative maximum that is not an absolute maximum, and sketch another graph illustrating an absolute maximum that is not a relative maximum. Explain how these graphs satisfy the given conditions.

---

## 3.5 APPLIED MAXIMUM AND MINIMUM PROBLEMS

In this section we will show how the methods discussed in the last section can be used to solve various applied optimization problems.

### CLASSIFICATION OF OPTIMIZATION PROBLEMS

The applied optimization problems that we will consider in this section fall into the following two categories:
* Problems that reduce to maximizing or minimizing a continuous function over a finite closed interval.
* Problems that reduce to maximizing or minimizing a continuous function over an infinite interval or a finite interval that is not closed.

### PROBLEMS INVOLVING FINITE CLOSED INTERVALS

> **Pierre de Fermat (1601–1665)**  
> Fermat, the son of a successful French leather merchant, was a lawyer who practiced mathematics as a hobby. He received a Bachelor of Civil Laws degree from the University of Orleans in 1631 and subsequently held various government positions, including a post as councillor to the Toulouse parliament. Throughout his life, Fermat fought all efforts to have his mathematical results published. He had the unfortunate habit of scribbling his work in the margins of books and often sent his results to friends without keeping copies for himself. It is now known that Fermat, simultaneously and independently of Descartes, developed analytic geometry. Fermat solved many fundamental calculus problems, obtained the first procedure for differentiating polynomials, and solved many important maximization, minimization, area, and tangent problems. His work served to inspire Isaac Newton. Fermat is best known for his work in number theory and Fermat's Last Theorem, which was finally proved by Andrew Wiles and Richard Taylor in 1995.

#### Example 1
A garden is to be laid out in a rectangular area and protected by a chicken wire fence. What is the largest possible area of the garden if only 100 running feet of chicken wire is available for the fence?

**Solution.** Let $x = \text{length (ft)}$, $y = \text{width (ft)}$, $A = xy$.  
Perimeter: $2x + 2y = 100 \implies y = 50 - x$.  
$$A = x(50 - x) = 50x - x^2, \quad 0 \le x \le 50$$
$$\frac{dA}{dx} = 50 - 2x = 0 \implies x = 25$$
$A(0) = 0, A(25) = 625, A(50) = 0$. Maximum area is $625\text{ ft}^2$ when $x = 25\text{ ft}$ and $y = 25\text{ ft}$ (a square).

---

### A PROCEDURE FOR SOLVING APPLIED MAXIMUM AND MINIMUM PROBLEMS

* **Step 1.** Draw an appropriate figure and label the quantities relevant to the problem.
* **Step 2.** Find a formula for the quantity to be maximized or minimized.
* **Step 3.** Using the conditions stated in the problem to eliminate variables, express the quantity to be maximized or minimized as a function of one variable.
* **Step 4.** Find the interval of possible values for this variable from the physical restrictions in the problem.
* **Step 5.** If applicable, use the techniques of the preceding section to obtain the maximum or minimum.

#### Example 2
An open box is to be made from a 16-inch by 30-inch piece of cardboard by cutting out squares of equal size from the four corners and bending up the sides (Figure 3.5.3). What size should the squares be to obtain a box with the largest volume?

**Solution.** Let $x$ be the length of the side of each removed square. The box has dimensions $16 - 2x$ by $30 - 2x$ by $x$.
$$V(x) = (16 - 2x)(30 - 2x)x = 480x - 92x^2 + 4x^3, \quad 0 \le x \le 8$$
$$\frac{dV}{dx} = 480 - 184x + 12x^2 = 4(x - 12)(3x - 10) = 0 \implies x = 10/3 \text{ (since } x = 12 \notin [0, 8]\text{)}$$
$V(0) = 0, V(8) = 0, V(10/3) = \frac{19,600}{27}\text{ in}^3 \approx 726\text{ in}^3$.  
The greatest volume occurs when $x = 10/3\text{ inches}$.

#### Example 3
Figure 3.5.5 shows an offshore oil well located at a point $W$ that is $5\text{ km}$ from the closest point $A$ on a straight shoreline. Oil is to be piped from $W$ to a shore point $B$ that is $8\text{ km}$ from $A$ by piping it on a straight line under water from $W$ to some shore point $P$ between $A$ and $B$ and then on to $B$ via pipe along the shoreline. If the cost of laying pipe is $\$1,000,000/\text{km}$ under water and $\$500,000/\text{km}$ over land, where should the point $P$ be located to minimize the cost of laying the pipe?

**Solution.** Distance $AP = x \in [0, 8]$. Underwater length $= \sqrt{x^2 + 25}$, land length $= 8 - x$.
$$c(x) = \sqrt{x^2 + 25} + \frac{1}{2}(8 - x)$$
$$\frac{dc}{dx} = \frac{x}{\sqrt{x^2 + 25}} - \frac{1}{2} = 0 \implies 2x = \sqrt{x^2 + 25} \implies 4x^2 = x^2 + 25 \implies x = \frac{5}{\sqrt{3}} \approx 2.89\text{ km}$$
$c(0) = 9, c(8) = \sqrt{89} \approx 9.43, c(5/\sqrt{3}) \approx 8.330127$ million dollars ($\$8,330,127$).  
$P$ should be $5/\sqrt{3}\text{ km} \approx 2.89\text{ km}$ from $A$.

#### Example 4
Find the radius and height of the right circular cylinder of largest volume that can be inscribed in a right circular cone with radius 6 inches and height 10 inches.

**Solution.** Volume $V = \pi r^2 h$. By similar triangles, $\frac{10 - h}{r} = \frac{10}{6} \implies h = 10 - \frac{5}{3}r$.
$$V(r) = \pi r^2\left(10 - \frac{5}{3}r\right) = 10\pi r^2 - \frac{5}{3}\pi r^3, \quad 0 \le r \le 6$$
$$\frac{dV}{dr} = 20\pi r - 5\pi r^2 = 5\pi r(4 - r) = 0 \implies r = 4$$
$V(0) = 0, V(6) = 0, V(4) = \frac{160}{3}\pi \approx 168\text{ in}^3$. Height $h = 10 - \frac{5}{3}(4) = \frac{10}{3}\text{ in}$.

---

### PROBLEMS INVOLVING INTERVALS THAT ARE NOT BOTH FINITE AND CLOSED

#### Example 5
A closed cylindrical can is to hold 1 liter ($1000\text{ cm}^3$) of liquid. How should we choose the height and radius to minimize the amount of material needed to manufacture the can?

**Solution.** Surface area $S = 2\pi r^2 + 2\pi rh$. Volume $\pi r^2 h = 1000 \implies h = \frac{1000}{\pi r^2}$.
$$S(r) = 2\pi r^2 + \frac{2000}{r}, \quad r \in (0, +\infty)$$
$$\lim_{r \to 0^+} S(r) = +\infty, \quad \lim_{r \to +\infty} S(r) = +\infty$$
$$\frac{dS}{dr} = 4\pi r - \frac{2000}{r^2} = 0 \implies r^3 = \frac{2000}{4\pi} = \frac{500}{\pi} \implies r = \frac{10}{\sqrt[3]{2\pi}} \approx 5.4\text{ cm}$$
$$h = \frac{1000}{\pi(10/\sqrt[3]{2\pi})^2} = \frac{20}{\sqrt[3]{2\pi}} = 2r$$
Minimum material occurs when height equals base diameter.

#### Example 6
Find a point on the curve $y = x^2$ that is closest to the point $(18, 0)$.

**Solution.** Square of distance $S = (x - 18)^2 + y^2 = (x - 18)^2 + x^4$.
$$\frac{dS}{dx} = 2(x - 18) + 4x^3 = 4x^3 + 2x - 36 = 2(x - 2)(2x^2 + 4x + 9) = 0 \implies x = 2$$
$\frac{d^2S}{dx^2} = 12x^2 + 2 > 0 \implies$ absolute minimum at $(2, 4)$.

---

### AN APPLICATION TO ECONOMICS & MARGINAL ANALYSIS

* $C(x) = \text{total cost} = a + M(x) = a + bx + cx^2$
* $R(x) = \text{total revenue} = px$
* $P(x) = R(x) - C(x) = \text{total profit}$
* Marginal profit $P'(x)$, marginal revenue $R'(x)$, marginal cost $C'(x)$.
* Maximum profit condition: $P'(x) = 0 \implies R'(x) = C'(x)$ (Marginal Revenue $=$ Marginal Cost).

> **Willebrord van Roijen Snell (1591–1626)**  
> Dutch mathematician and Professor at the University of Leiden. Discovered the law of refraction (Snell's Law) and founded modern mapmaking by triangulation.

#### Example 7
A liquid form of antibiotic manufactured by a pharmaceutical firm is sold in bulk at a price of $\$200$ per unit. If the total production cost (in dollars) for $x$ units is
$$C(x) = 500,000 + 80x + 0.003x^2$$
and if the production capacity of the firm is at most $30,000$ units in a specified time, how many units of antibiotic must be manufactured and sold in that time to maximize the profit?

**Solution.** Profit $P(x) = 200x - (500,000 + 80x + 0.003x^2)$ on $[0, 30,000]$.
$$\frac{dP}{dx} = 120 - 0.006x = 0 \implies x = 20,000$$
$P(0) = -500,000$, $P(20,000) = 700,000$, $P(30,000) = 400,000$. Maximum profit is $\$700,000$ at $x = 20,000\text{ units}$.

---

### QUICK CHECK EXERCISES 3.5
*(See page 238 for answers.)*

1. A positive number $x$ and its reciprocal are added together. The smallest possible value of this sum is obtained by minimizing $f(x) = \underline{\hspace{1.5cm}}$ for $x$ in the interval $\underline{\hspace{1.5cm}}$.
2. Two nonnegative numbers, $x$ and $y$, have a sum equal to 10. The largest possible product of the two numbers is obtained by maximizing $f(x) = \underline{\hspace{1.5cm}}$ for $x$ in the interval $\underline{\hspace{1.5cm}}$.
3. A rectangle in the $xy$-plane has one corner at the origin, an adjacent corner at the point $(x, 0)$, and a third corner at a point on the line segment from $(0, 4)$ to $(3, 0)$. The largest possible area of the rectangle is obtained by maximizing $A(x) = \underline{\hspace{1.5cm}}$ for $x$ in the interval $\underline{\hspace{1.5cm}}$.
4. An open box is to be made from a 20-inch by 32-inch piece of cardboard by cutting out $x$-inch by $x$-inch squares from the four corners and bending up the sides. The largest possible volume of the box is obtained by maximizing $V(x) = \underline{\hspace{1.5cm}}$ for $x$ in the interval $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 3.5
1. $x + \frac{1}{x}; \quad (0, +\infty)$  
2. $x(10 - x); \quad [0, 10]$  
3. $x\left(-\frac{4}{3}x + 4\right) = -\frac{4}{3}x^2 + 4x; \quad [0, 3]$  
4. $x(20 - 2x)(32 - 2x) = 4x^3 - 104x^2 + 640x; \quad [0, 10]$

---

### EXERCISE SET 3.5

1. Find a number in the closed interval $[1/2, 3/2]$ such that the sum of the number and its reciprocal is  
   (a) as small as possible  
   (b) as large as possible.
2. How should two nonnegative numbers be chosen so that their sum is 1 and the sum of their squares is  
   (a) as large as possible  
   (b) as small as possible?
3. A rectangular field is to be bounded by a fence on three sides and by a straight stream on the fourth side. Find the dimensions of the field with maximum area that can be enclosed using $1000\text{ ft}$ of fence.
4. The boundary of a field is a right triangle with a straight stream along its hypotenuse and with fences along its other two sides. Find the dimensions of the field with maximum area that can be enclosed using $1000\text{ ft}$ of fence.
5. A rectangular plot of land is to be fenced in using two kinds of fencing. Two opposite sides will use heavy-duty fencing selling for $\$3$ a foot, while the remaining two sides will use standard fencing selling for $\$2$ a foot. What are the dimensions of the rectangular plot of greatest area that can be fenced in at a cost of $\$6000$?
6. A rectangle is to be inscribed in a right triangle having sides of length $6\text{ in}, 8\text{ in},$ and $10\text{ in}$. Find the dimensions of the rectangle with greatest area assuming the rectangle is positioned as in Figure Ex-6.
7. Solve the problem in Exercise 6 assuming the rectangle is positioned as in Figure Ex-7.
8. A rectangle has its two lower corners on the $x$-axis and its two upper corners on the curve $y = 16 - x^2$. For all such rectangles, what are the dimensions of the one with largest area?
9. Find the dimensions of the rectangle with maximum area that can be inscribed in a circle of radius 10.
10. Find the point $P$ in the first quadrant on the curve $y = x^{-2}$ such that a rectangle with sides on the coordinate axes and a vertex at $P$ has the smallest possible perimeter.
11. A rectangular area of $3200\text{ ft}^2$ is to be fenced off. Two opposite sides will use fencing costing $\$1$ per foot and the remaining sides will use fencing costing $\$2$ per foot. Find the dimensions of the rectangle of least cost.
12. Show that among all rectangles with perimeter $p$, the square has the maximum area.
13. Show that among all rectangles with area $A$, the square has the minimum perimeter.
14. A wire of length $12\text{ in}$ can be bent into a circle, bent into a square, or cut into two pieces to make both a circle and a square. How much wire should be used for the circle if the total area enclosed by the figure(s) is to be  
    (a) a maximum  
    (b) a minimum?
15. A rectangle $R$ in the plane has corners at $(\pm 8, \pm 12)$, and a 100 by 100 square $S$ is positioned in the plane so that its sides are parallel to the coordinate axes and the lower left corner of $S$ is on the line $y = -3x$. What is the largest possible area of a region in the plane that is contained in both $R$ and $S$?
16. Solve the problem in Exercise 15 if $S$ is a 16 by 16 square.
17. Solve the problem in Exercise 15 if $S$ is positioned with its lower left corner on the line $y = -6x$.
18. A rectangular page is to contain 42 square inches of printable area. The margins at the top and bottom of the page are each 1 inch, one side margin is 1 inch, and the other side margin is 2 inches. What should the dimensions of the page be so that the least amount of paper is used?
19. A box with a square base is taller than it is wide. In order to send the box through the U.S. mail, the height of the box and the perimeter of the base can sum to no more than $108\text{ in}$. What is the maximum volume for such a box?
20. A box with a square base is wider than it is tall. In order to send the box through the U.S. mail, the width of the box and the perimeter of one of the (nonsquare) sides of the box can sum to no more than $108\text{ in}$. What is the maximum volume for such a box?
21. An open box is to be made from a $3\text{ ft}$ by $8\text{ ft}$ rectangular piece of sheet metal by cutting out squares of equal size from the four corners and bending up the sides. Find the maximum volume that the box can have.
22. A closed rectangular container with a square base is to have a volume of $2250\text{ in}^3$. The material for the top and bottom of the container will cost $\$2\text{ per in}^2$, and the material for the sides will cost $\$3\text{ per in}^2$. Find the dimensions of the container of least cost.
23. A closed rectangular container with a square base is to have a volume of $2000\text{ cm}^3$. It costs twice as much per square centimeter for the top and bottom as it does for the sides. Find the dimensions of the container of least cost.
24. A container with square base, vertical sides, and open top is to be made from $1000\text{ ft}^2$ of material. Find the dimensions of the container with greatest volume.
25. A rectangular container with two square sides and an open top is to have a volume of $V$ cubic units. Find the dimensions of the container with minimum surface area.
26. A church window consisting of a rectangle topped by a semicircle is to have a perimeter $p$. Find the radius of the semicircle if the area of the window is to be maximum.
27. Find the dimensions of the right circular cylinder of largest volume that can be inscribed in a sphere of radius $R$.
28. Find the dimensions of the right circular cylinder of greatest surface area that can be inscribed in a sphere of radius $R$.
29. A closed, cylindrical can is to have a volume of $V$ cubic units. Show that the can of minimum surface area is achieved when the height is equal to the diameter of the base.
30. A closed cylindrical can is to have a surface area of $S$ square units. Show that the can of maximum volume is achieved when the height is equal to the diameter of the base.
31. A cylindrical can, open at the top, is to hold $500\text{ cm}^3$ of liquid. Find the height and radius that minimize the amount of material needed to manufacture the can.
32. A soup can in the shape of a right circular cylinder of radius $r$ and height $h$ is to have a prescribed volume $V$. The top and bottom are cut from squares as shown in Figure Ex-32. If the shaded corners are wasted, but there is no other waste, find the ratio $r/h$ for the can requiring the least material (including waste).
33. A box-shaped wire frame consists of two identical wire squares whose vertices are connected by four straight wires of equal length (Figure Ex-33). If the frame is to be made from a wire of length $L$, what should the dimensions be to obtain a box of greatest volume?
34. Suppose that the sum of the surface areas of a sphere and a cube is a constant.  
    (a) Show that the sum of their volumes is smallest when the diameter of the sphere is equal to the length of an edge of the cube.  
    (b) When will the sum of their volumes be greatest?
35. Find the height and radius of the cone of slant height $L$ whose volume is as large as possible.
36. A cone is made from a circular sheet of radius $R$ by cutting out a sector and gluing the cut edges of the remaining piece together (Figure Ex-36). What is the maximum volume attainable for the cone?
37. A cone-shaped paper drinking cup is to hold $100\text{ cm}^3$ of water. Find the height and radius of the cup that will require the least amount of paper.
38. Find the dimensions of the isosceles triangle of least area that can be circumscribed about a circle of radius $R$.
39. Find the height and radius of the right circular cone with least volume that can be circumscribed about a sphere of radius $R$.
40. A commercial cattle ranch currently allows 20 steers per acre of grazing land; on the average its steers weigh $2000\text{ lb}$ at market. Estimates by the Agriculture Department indicate that the average market weight per steer will be reduced by $50\text{ lb}$ for each additional steer added per acre of grazing land. How many steers per acre should be allowed in order for the ranch to get the largest possible total market weight for its cattle?
41. A company mines low-grade nickel ore. If the company mines $x$ tons of ore, it can sell the ore for $p = 225 - 0.25x$ dollars per ton. Find the revenue and marginal revenue functions. At what level of production would the company obtain the maximum revenue?
42. A fertilizer producer finds that it can sell its product at a price of $p = 300 - 0.1x$ dollars per unit when it produces $x$ units of fertilizer. The total production cost (in dollars) for $x$ units is
    $$C(x) = 15,000 + 125x + 0.025x^2$$
    If the production capacity of the firm is at most 1000 units of fertilizer in a specified time, how many units must be manufactured and sold in that time to maximize the profit?
43. (a) A chemical manufacturer sells sulfuric acid in bulk at a price of $\$100$ per unit. If the daily total production cost in dollars for $x$ units is
    $$C(x) = 100,000 + 50x + 0.0025x^2$$
    and if the daily production capacity is at most 7000 units, how many units of sulfuric acid must be manufactured and sold daily to maximize the profit?  
    (b) Would it benefit the manufacturer to expand the daily production capacity?  
    (c) Use marginal analysis to approximate the effect on profit if daily production could be increased from 7000 to 7001 units.
44. A firm determines that $x$ units of its product can be sold daily at $p$ dollars per unit, where $x = 1000 - p$. The cost of producing $x$ units per day is $C(x) = 3000 + 20x$.  
    (a) Find the revenue function $R(x)$.  
    (b) Find the profit function $P(x)$.  
    (c) Assuming that the production capacity is at most 500 units per day, determine how many units the company must produce and sell each day to maximize the profit.  
    (d) Find the maximum profit.  
    (e) What price per unit must be charged to obtain the maximum profit?
45. In a certain chemical manufacturing process, the daily weight $y$ of defective chemical output depends on the total weight $x$ of all output according to the empirical formula
    $$y = 0.01x + 0.00003x^2$$
    where $x$ and $y$ are in pounds. If the profit is $\$100$ per pound of nondefective chemical produced and the loss is $\$20$ per pound of defective chemical produced, how many pounds of chemical should be produced daily to maximize the total daily profit?
46. An independent truck driver charges a client $\$15$ for each hour of driving, plus the cost of fuel. At highway speeds of $v$ miles per hour, the trucker's rig gets $10 - 0.07v$ miles per gallon of diesel fuel. If diesel fuel costs $\$2.50$ per gallon, what speed $v$ will minimize the cost to the client?
47. A trapezoid is inscribed in a semicircle of radius 2 so that one side is along the diameter (Figure Ex-47). Find the maximum possible area for the trapezoid. [Hint: Express the area of the trapezoid in terms of $\theta$.]
48. A drainage channel is to be made so that its cross section is a trapezoid with equally sloping sides (Figure Ex-48). If the sides and bottom all have a length of $5\text{ ft}$, how should the angle $\theta \ (0 \le \theta \le \pi/2)$ be chosen to yield the greatest cross-sectional area of the channel?
49. A lamp is suspended above the center of a round table of radius $r$. How high above the table should the lamp be placed to achieve maximum illumination at the edge of the table? [Assume that the illumination $I$ is directly proportional to the cosine of the angle of incidence $\phi$ of the light rays and inversely proportional to the square of the distance $l$ from the light source (Figure Ex-49).]
50. A plank is used to reach over a fence $8\text{ ft}$ high to support a wall that is $1\text{ ft}$ behind the fence (Figure Ex-50). What is the length of the shortest plank that can be used? [Hint: Express the length of the plank in terms of the angle $\theta$ shown in the figure.]
51. Two particles, $A$ and $B$, are in motion in the $xy$-plane. Their coordinates at each instant of time $t \ (t \ge 0)$ are given by $x_A = t, y_A = 2t, x_B = 1 - t,$ and $y_B = t$. Find the minimum distance between $A$ and $B$.
52. Follow the directions of Exercise 51, with $x_A = t, y_A = t^2, x_B = 2t,$ and $y_B = 2$.
53. Find the coordinates of the point $P$ on the curve $y = 1/x^2 \ (x > 0)$ where the segment of the tangent line at $P$ that is cut off by the coordinate axes has its shortest length.
54. Find the $x$-coordinate of the point $P$ on the parabola $y = 1 - x^2 \ (0 < x \le 1)$ where the triangle that is enclosed by the tangent line at $P$ and the coordinate axes has the smallest area.
55. Where on the curve $y = (1 + x^2)^{-1}$ does the tangent line have the greatest slope?
56. A rectangular water tank has a base of area four square meters. Water flows into the tank until the amount of water in the tank is $20\text{ m}^3$, at which point any additional flow into the tank is diverted by an overflow valve. Suppose that the tank is initially empty, and water is pumped into the tank so that after $t$ minutes, $(2t^3 + 7t)/(t^2 + 12)$ cubic meters of water has been pumped into the tank. At what time is the height of the water in the tank increasing most rapidly?
57. The shoreline of Circle Lake is a circle with diameter $2\text{ mi}$. Nancy's training routine begins at point $E$ on the eastern shore of the lake. She jogs along the north shore to a point $P$ and then swims the straight line distance, if any, from $P$ to point $W$ diametrically opposite $E$ (Figure Ex-57). Nancy swims at a rate of $2\text{ mi/h}$ and jogs at $8\text{ mi/h}$. How far should Nancy jog in order to complete her training routine in  
    (a) the least amount of time  
    (b) the greatest amount of time?
58. A man is floating in a rowboat 1 mile from the (straight) shoreline of a large lake. A town is located on the shoreline 1 mile from the point on the shoreline closest to the man. As suggested in Figure Ex-58, he intends to row in a straight line to some point $P$ on the shoreline and then walk the remaining distance to the town. To what point should he row in order to reach his destination in the least time if  
    (a) he can walk $5\text{ mi/h}$ and row $3\text{ mi/h}$  
    (b) he can walk $5\text{ mi/h}$ and row $4\text{ mi/h}$?
59. A pipe of negligible diameter is to be carried horizontally around a corner from a hallway $8\text{ ft}$ wide into a hallway $4\text{ ft}$ wide (Figure Ex-59). What is the maximum length that the pipe can have?
60. A concrete barrier whose cross section is an isosceles triangle runs parallel to a wall. The height of the barrier is $3\text{ ft}$, the width of the base of a cross section is $8\text{ ft}$, and the barrier is positioned on level ground with its base $1\text{ ft}$ from the wall. A straight, stiff metal rod of negligible diameter has one end on the ground, the other end against the wall, and touches the top of the barrier (Figure Ex-60). What is the minimum length the rod can have?
61. Suppose that the intensity of a point light source is directly proportional to the strength of the source and inversely proportional to the square of the distance from the source. Two point light sources with strengths of $S$ and $8S$ are separated by a distance of $90\text{ cm}$. Where on the line segment between the two sources is the total intensity a minimum?
62. Given points $A(2, 1)$ and $B(5, 4)$, find the point $P$ in the interval $[2, 5]$ on the $x$-axis that maximizes angle $APB$.
63. The lower edge of a painting, $10\text{ ft}$ in height, is $2\text{ ft}$ above an observer's eye level. Assuming that the best view is obtained when the angle subtended at the observer's eye by the painting is maximum, how far from the wall should the observer stand?

**FOCUS ON CONCEPTS**

64. **Fermat's principle in optics** states that light traveling from one point to another follows that path for which the total travel time is minimum. In a uniform medium, the paths of "minimum time" and "shortest distance" turn out to be the same, so that light, if unobstructed, travels along a straight line. Assume that we have a light source, a flat mirror, and an observer in a uniform medium. If a light ray leaves the source, bounces off the mirror, and travels on to the observer, then its path will consist of two line segments, as shown in Figure Ex-64. According to Fermat's principle, the path will be such that the total travel time $t$ is minimum or, since the medium is uniform, the path will be such that the total distance traveled from $A$ to $P$ to $B$ is as small as possible. Assuming the minimum occurs when $dt/dx = 0$, show that the light ray will strike the mirror at the point $P$ where the "angle of incidence" $\theta_1$ equals the "angle of reflection" $\theta_2$.
65. Fermat's principle (Exercise 64) also explains why light rays traveling between air and water undergo bending (refraction). Imagine that we have two uniform media (such as air and water) and a light ray traveling from a source $A$ in one medium to an observer $B$ in the other medium (Figure Ex-65). It is known that light travels at a constant speed in a uniform medium, but more slowly in a dense medium (such as water) than in a thin medium (such as air). Consequently, the path of shortest time from $A$ to $B$ is not necessarily a straight line, but rather some broken line path $A$ to $P$ to $B$ allowing the light to take greatest advantage of its higher speed through the thin medium. **Snell's law of refraction** states that the path of the light ray will be such that
    $$\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$$
    where $v_1$ is the speed of light in the first medium, $v_2$ is the speed of light in the second medium, and $\theta_1$ and $\theta_2$ are the angles shown in Figure Ex-65. Show that this follows from the assumption that the path of minimum time occurs when $dt/dx = 0$.
66. A farmer wants to walk at a constant rate from her barn to a straight river, fill her pail, and carry it to her house in the least time.  
    (a) Explain how this problem relates to Fermat's principle and the light-reflection problem in Exercise 64.  
    (b) Use the result of Exercise 64 to describe geometrically the best path for the farmer to take.  
    (c) Use part (b) to determine where the farmer should fill her pail if her house and barn are located as in Figure Ex-66.
67. If an unknown physical quantity $x$ is measured $n$ times, the measurements $x_1, x_2, \dots, x_n$ often vary because of uncontrollable factors such as temperature, atmospheric pressure, and so forth. Thus, a scientist is often faced with the problem of using $n$ different observed measurements to obtain an estimate $\bar{x}$ of an unknown quantity $x$. One method for making such an estimate is based on the **least squares principle**, which states that the estimate $\bar{x}$ should be chosen to minimize
    $$s = (x_1 - \bar{x})^2 + (x_2 - \bar{x})^2 + \dots + (x_n - \bar{x})^2$$
    which is the sum of the squares of the deviations between the estimate $\bar{x}$ and the measured values. Show that the estimate resulting from the least squares principle is
    $$\bar{x} = \frac{1}{n}(x_1 + x_2 + \dots + x_n)$$
    that is, $\bar{x}$ is the arithmetic average of the observed values.
68. Prove: If $f(x) \ge 0$ on an interval and if $f(x)$ has a maximum value on that interval at $x_0$, then $\sqrt{f(x)}$ also has a maximum value at $x_0$. Similarly for minimum values. [Hint: Use the fact that $\sqrt{x}$ is an increasing function on the interval $[0, +\infty)$.]
69. **Writing.** Discuss the importance of finding intervals of possible values imposed by physical restrictions on variables in an applied maximum or minimum problem.

---

## 3.6 RECTILINEAR MOTION

In this section we will continue the study of rectilinear motion that we began in Section 2.1. We will define the notion of "acceleration" mathematically, and we will show how the tools of calculus developed earlier in this chapter can be used to analyze rectilinear motion in more depth.

### REVIEW OF TERMINOLOGY

Recall from Section 2.1 that a particle that can move in either direction along a coordinate line is said to be in **rectilinear motion**. In general discussions we will designate the coordinate line as the $s$-axis. As the particle moves along the $s$-axis, its coordinate $s$ will be some function of time, say $s = s(t)$. We call $s(t)$ the **position function** of the particle, and we call the graph of $s$ versus $t$ the **position versus time curve**. If the coordinate of a particle at time $t_1$ is $s(t_1)$ and the coordinate at a later time $t_2$ is $s(t_2)$, then $s(t_2) - s(t_1)$ is called the **displacement** of the particle over the time interval $[t_1, t_2]$.

#### Example 1
Figure 3.6.2a shows the position versus time curve for a particle moving along an $s$-axis. In words, describe how the position of the particle changes with time.

**Solution.** The particle is at $s = -3$ at time $t = 0$. It moves in the positive direction until time $t = 4$, since $s$ is increasing. At time $t = 4$ the particle is at position $s = 3$. At that time it turns around and travels in the negative direction until time $t = 7$, since $s$ is decreasing. At time $t = 7$ the particle is at position $s = -1$, and it remains stationary thereafter, since $s$ is constant for $t > 7$.

---

### VELOCITY AND SPEED

If a particle in rectilinear motion has position function $s(t)$, then we define its **velocity function** $v(t)$ to be
$$v(t) = s'(t) = \frac{ds}{dt} \tag{1}$$
The sign of the velocity tells which way the particle is moving—a positive value for $v(t)$ means that $s$ is increasing with time (moving in positive direction), and a negative value means $s$ is decreasing with time (moving in negative direction). If $v(t) = 0$, the particle has momentarily stopped.

We define the **speed function** to be the absolute value of instantaneous velocity:
$$|v(t)| = |s'(t)| = \left|\frac{ds}{dt}\right| \tag{2}$$

#### Example 2
Let $s(t) = t^3 - 6t^2$ be the position function of a particle moving along an $s$-axis, where $s$ is in meters and $t$ is in seconds. Find the velocity and speed functions, and show the graphs of position, velocity, and speed versus time.

**Solution.**
$$v(t) = \frac{ds}{dt} = 3t^2 - 12t \quad \text{and} \quad |v(t)| = |3t^2 - 12t|$$
The particle is on the negative side of the origin for $0 < t < 6$, on the positive side for $t > 6$, and at the origin at $t = 0$ and $t = 6$. It moves in the negative direction for $0 < t < 4$, positive direction for $t > 4$, and momentarily stops at $t = 0$ and $t = 4$. Speed increases for $0 < t < 2$, decreases for $2 < t < 4$, and increases for $t > 4$.

---

### ACCELERATION

In rectilinear motion, the rate at which the instantaneous velocity of a particle changes with time is called its **instantaneous acceleration**:
$$a(t) = v'(t) = \frac{dv}{dt} = s''(t) = \frac{d^2s}{dt^2} \tag{3-4}$$

#### Example 3
Let $s(t) = t^3 - 6t^2$ be the position function of a particle moving along an $s$-axis ($s$ in meters, $t$ in seconds). Find the acceleration function $a(t)$, and show the graph of acceleration versus time.

**Solution.** From Example 2, $v(t) = 3t^2 - 12t$, so
$$a(t) = \frac{dv}{dt} = 6t - 12 \quad (\text{units of m/s}^2)$$

---

### SPEEDING UP AND SLOWING DOWN

> **INTERPRETING THE SIGN OF ACCELERATION**  
> A particle in rectilinear motion is **speeding up** when its velocity and acceleration have the **same sign** ($v(t)a(t) > 0$) and **slowing down** when they have **opposite signs** ($v(t)a(t) < 0$).

#### Example 4
In Examples 2 and 3 we found $v(t) = 3t^2 - 12t$ and $a(t) = 6t - 12$ for $s(t) = t^3 - 6t^2$. Determine when the particle is speeding up and slowing down.

**Solution.**
* $0 < t < 2$: $v(t) < 0$ and $a(t) < 0 \implies$ speeding up.
* $2 < t < 4$: $v(t) < 0$ and $a(t) > 0 \implies$ slowing down.
* $t > 4$: $v(t) > 0$ and $a(t) > 0 \implies$ speeding up.

---

### ANALYZING THE POSITION VERSUS TIME CURVE

#### Table 3.6.1: Analysis of Particle Motion from Position vs. Time Curve
| Position vs. Time Curve | Characteristics of the Curve at $t = t_0$ | Behavior of the Particle at Time $t = t_0$ |
| :--- | :--- | :--- |
| Increasing, concave down, $s(t_0) > 0$ | $s(t_0) > 0$, positive slope, concave down | Particle on positive side of origin, moving in positive direction, velocity decreasing, slowing down. |
| Decreasing, concave down, $s(t_0) > 0$ | $s(t_0) > 0$, negative slope, concave down | Particle on positive side of origin, moving in negative direction, velocity decreasing, speeding up. |
| Decreasing, concave up, $s(t_0) < 0$ | $s(t_0) < 0$, negative slope, concave up | Particle on negative side of origin, moving in negative direction, velocity increasing, slowing down. |
| Peak (horizontal tangent), concave down, $s(t_0) > 0$ | $s(t_0) > 0$, zero slope, concave down | Particle on positive side of origin, momentarily stopped, velocity decreasing. |

#### Example 5
Use the position versus time curve in Figure 3.6.5 to determine when the particle in Example 1 is speeding up and slowing down.

**Solution.**
* $t = 0$ to $t = 2$: $a > 0$ and $v > 0 \implies$ speeding up.
* $t = 2$ to $t = 4$: $a < 0$ and $v > 0 \implies$ slowing down.
* At $t = 4$: $v = 0 \implies$ momentarily stopped.
* $t = 4$ to $t = 6$: $a < 0$ and $v < 0 \implies$ speeding up.
* $t = 6$ to $t = 7$: $a > 0$ and $v < 0 \implies$ slowing down.
* $t > 7$: $v = 0 \implies$ stopped.

#### Example 6
Suppose that the position function of a particle moving on a coordinate line is given by $s(t) = 2t^3 - 21t^2 + 60t + 3$. Analyze the motion of the particle for $t \ge 0$.

**Solution.**
$$v(t) = s'(t) = 6t^2 - 42t + 60 = 6(t - 2)(t - 5)$$
$$a(t) = v'(t) = 12t - 42 = 12(t - 7/2)$$
* Direction of motion: Moves in positive direction for $0 \le t < 2$, stops momentarily at $t = 2$, moves in negative direction for $2 < t < 5$, stops momentarily at $t = 5$, moves in positive direction for $t > 5$.
* Change in speed:
  * $0 \le t < 2$: $v > 0, a < 0 \implies$ slowing down.
  * $2 < t < 7/2$: $v < 0, a < 0 \implies$ speeding up.
  * At $t = 7/2$: $a = 0$ (inflection point).
  * $7/2 < t < 5$: $v < 0, a > 0 \implies$ slowing down.
  * $t > 5$: $v > 0, a > 0 \implies$ speeding up.
* Positions: $s(0) = 3$, $s(2) = 55$, $s(7/2) = 41.5$, $s(5) = 28$.

---

### QUICK CHECK EXERCISES 3.6
*(See page 246 for answers.)*

1. For a particle in rectilinear motion, the velocity and position functions $v(t)$ and $s(t)$ are related by the equation $\underline{\hspace{1.5cm}}$, and the acceleration and velocity functions $a(t)$ and $v(t)$ are related by the equation $\underline{\hspace{1.5cm}}$.
2. Suppose that a particle moving along the $s$-axis has position function $s(t) = 7t - 2t^2$. At time $t = 3$, the particle's position is $\underline{\hspace{1.5cm}}$, its velocity is $\underline{\hspace{1.5cm}}$, its speed is $\underline{\hspace{1.5cm}}$, and its acceleration is $\underline{\hspace{1.5cm}}$.
3. A particle in rectilinear motion is speeding up if the signs of its velocity and acceleration are $\underline{\hspace{1.5cm}}$, and it is slowing down if these signs are $\underline{\hspace{1.5cm}}$.
4. Suppose that a particle moving along the $s$-axis has position function $s(t) = t^4 - 24t^2$ over the time interval $t \ge 0$. The particle slows down over the time interval(s) $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 3.6
1. $v(t) = s'(t); \quad a(t) = v'(t)$  
2. $3; \ -5; \ 5; \ -4$  
3. the same; opposite  
4. $2 < t < 2\sqrt{3}$

---

### EXERCISE SET 3.6

**FOCUS ON CONCEPTS**

1. The graphs of three position functions are shown in Figure Ex-1. In each case determine the signs of the velocity and acceleration, and then determine whether the particle is speeding up or slowing down.  
   (a) $s$ increasing, concave down  
   (b) $s$ increasing, concave up  
   (c) $s$ decreasing, concave up
2. The graphs of three velocity functions are shown in Figure Ex-2. In each case determine the sign of the acceleration, and then determine whether the particle is speeding up or slowing down.  
   (a) $v > 0$, slope $< 0$  
   (b) $v < 0$, slope $< 0$  
   (c) $v > 0$, slope $> 0$
3. The graph of the position function of a particle moving on a horizontal line is shown in Figure Ex-3.  
   (a) Is the particle moving left or right at time $t_0$?  
   (b) Is the acceleration positive or negative at time $t_0$?  
   (c) Is the particle speeding up or slowing down at time $t_0$?  
   (d) Is the particle speeding up or slowing down at time $t_1$?
4. For the graphs in Figure Ex-4, match the position functions (a)–(c) with their corresponding velocity functions (I)–(III).
5. Sketch a reasonable graph of $s$ versus $t$ for a mouse that is trapped in a narrow corridor (an $s$-axis with the positive direction to the right) and scurries back and forth as follows. It runs right with a constant speed of $1.2\text{ m/s}$ for a while, then gradually slows down to $0.6\text{ m/s}$, then quickly speeds up to $2.0\text{ m/s}$, then gradually slows to a stop but immediately reverses direction and quickly speeds up to $1.2\text{ m/s}$.
6. The accompanying figure shows the position versus time curve for an ant that moves along a narrow vertical pipe, where $t$ is measured in seconds and the $s$-axis is along the pipe with the positive direction up.  
   (a) When, if ever, is the ant above the origin?  
   (b) When, if ever, does the ant have velocity zero?  
   (c) When, if ever, is the ant moving down the pipe?
7. The accompanying figure shows the graph of velocity versus time for a particle moving along a coordinate line. Make a rough sketch of the graphs of speed versus time and acceleration versus time.
8. The accompanying figure shows the position versus time graph for an elevator that ascends $40\text{ m}$ from one stop to the next.  
   (a) Estimate the velocity when the elevator is halfway up to the top.  
   (b) Sketch rough graphs of the velocity versus time curve and the acceleration versus time curve.

**9–12 True–False Determine whether the statement is true or false. Explain your answer.**

9. A particle is speeding up when its position versus time graph is increasing.
10. Velocity is the derivative of position with respect to time.
11. Acceleration is the absolute value of velocity.
12. If the position versus time curve is increasing and concave down, then the particle is slowing down.

13. The accompanying figure shows the velocity versus time graph for a test run on a Chevrolet Volt. Using this graph, estimate  
    (a) the acceleration at $60\text{ mi/h}$ (in $\text{ft/s}^2$)  
    (b) the time at which the maximum acceleration occurs.
14. The accompanying figure shows the velocity versus time graph for a test run on a Dodge Challenger. Using this graph, estimate  
    (a) the acceleration at $60\text{ mi/h}$ (in $\text{ft/s}^2$)  
    (b) the time at which the maximum acceleration occurs.

**15–16 The function $s(t)$ describes the position of a particle moving along a coordinate line, where $s$ is in meters and $t$ is in seconds.**  
**(a) Make a table showing the position, velocity, and acceleration to two decimal places at times $t = 1, 2, 3, 4, 5$.**  
**(b) At each of the times in part (a), determine whether the particle is stopped; if it is not, state its direction of motion.**  
**(c) At each of the times in part (a), determine whether the particle is speeding up, slowing down, or neither.**

15. $s(t) = \sin\left(\frac{\pi t}{4}\right)$
16. $s(t) = 2\cos\left(\frac{\pi}{3}t - \frac{2\pi}{3}\right)$

**17–20 The function $s(t)$ describes the position of a particle moving along a coordinate line, where $s$ is in feet and $t$ is in seconds.**  
**(a) Find the velocity and acceleration functions.**  
**(b) Find the position, velocity, speed, and acceleration at time $t = 1$.**  
**(c) At what times is the particle stopped?**  
**(d) When is the particle speeding up? Slowing down?**  
**(e) Find the total distance traveled by the particle from time $t = 0$ to time $t = 5$.**

17. $s(t) = t^3 - 3t^2, \quad t \ge 0$
18. $s(t) = t^4 - 4t^2 + 4, \quad t \ge 0$
19. $s(t) = 9 - 9\cos(\pi t/3), \quad 0 \le t \le 5$
20. $s(t) = \frac{t}{t^2 + 4}, \quad t \ge 0$

21. Let $s(t) = t/(t^2 + 5)$ be the position function of a particle moving along a coordinate line, where $s$ is in meters and $t$ is in seconds. Use a graphing utility to generate the graphs of $s(t), v(t),$ and $a(t)$ for $t \ge 0$, and use those graphs where needed.  
    (a) Use the appropriate graph to make a rough estimate of the time at which the particle first reverses the direction of its motion; and then find the time exactly.  
    (b) Find the exact position of the particle when it first reverses the direction of its motion.  
    (c) Use the appropriate graphs to make a rough estimate of the time intervals on which the particle is speeding up and on which it is slowing down; and then find those time intervals exactly.
22. Let $s(t) = 4t^2/(2t^4 + 3)$ be the position function of a particle moving along a coordinate line, where $s$ is in meters and $t$ is in seconds. Use a graphing utility to generate the graphs of $s(t), v(t),$ and $a(t)$ for $t \ge 0$, and use those graphs where needed.  
    (a) Use the appropriate graph to make a rough estimate of the time at which the particle first reverses the direction of its motion; and then find the time exactly.  
    (b) Find the exact position of the particle when it first reverses the direction of its motion.  
    (c) Use the appropriate graphs to make a rough estimate of the time intervals on which the particle is speeding up and on which it is slowing down; and then find those time intervals exactly.

**23–28 A position function of a particle moving along a coordinate line is given. Use the method of Example 6 to analyze the motion of the particle for $t \ge 0$, and give a schematic picture of the motion (as in Figure 3.6.8).**

23. $s = -4t + 3$
24. $s = 5t^2 - 20t$
25. $s = t^3 - 9t^2 + 24t$
26. $s = t + \frac{25}{t + 2}$
27. $s = \begin{cases} \cos t, & 0 \le t < 2\pi \\ 1, & t \ge 2\pi \end{cases}$
28. $s = \begin{cases} 2t(t - 2)^2, & 0 \le t < 3 \\ 13 - 7(t - 4)^2, & t \ge 3 \end{cases}$

29. Let $s(t) = 5t^2 - 22t$ be the position function of a particle moving along a coordinate line, where $s$ is in feet and $t$ is in seconds.  
    (a) Find the maximum speed of the particle during the time interval $1 \le t \le 3$.  
    (b) When, during the time interval $1 \le t \le 3$, is the particle farthest from the origin? What is its position at that instant?
30. Let $s = 100/(t^2 + 12)$ be the position function of a particle moving along a coordinate line, where $s$ is in feet and $t$ is in seconds. Find the maximum speed of the particle for $t \ge 0$, and find the direction of motion of the particle when it has its maximum speed.

**31–32 A position function of a particle moving along a coordinate line is provided. (a) Evaluate $s$ and $v$ when $a = 0$. (b) Evaluate $s$ and $a$ when $v = 0$.**

31. $s = \sin 2t, \quad 0 \le t \le \pi/2$
32. $s = t^3 - 6t^2 + 1$

33. Let $s = \sqrt{2t^2 + 1}$ be the position function of a particle moving along a coordinate line.  
    (a) Use a graphing utility to generate the graph of $v$ versus $t$, and make a conjecture about the velocity of the particle as $t \to +\infty$.  
    (b) Check your conjecture by finding $\lim_{t \to +\infty} v$.
34. (a) Use the chain rule to show that for a particle in rectilinear motion $a = v(dv/ds)$.  
    (b) Let $s = \sqrt{3t + 7}, \ t \ge 0$. Find a formula for $v$ in terms of $s$ and use the equation in part (a) to find the acceleration when $s = 5$.
35. Suppose that the position functions of two particles, $P_1$ and $P_2$, in motion along the same line are
    $$s_1 = \frac{1}{2}t^2 - t + 3 \quad \text{and} \quad s_2 = -\frac{1}{4}t^2 + t + 1$$
    respectively, for $t \ge 0$.  
    (a) Prove that $P_1$ and $P_2$ do not collide.  
    (b) How close do $P_1$ and $P_2$ get to each other?  
    (c) During what intervals of time are they moving in opposite directions?
36. Let $s_A = 15t^2 + 10t + 20$ and $s_B = 5t^2 + 40t, \ t \ge 0$, be the position functions of cars $A$ and $B$ that are moving along parallel straight lanes of a highway.  
    (a) How far is car $A$ ahead of car $B$ when $t = 0$?  
    (b) At what instants of time are the cars next to each other?  
    (c) At what instant of time do they have the same velocity? Which car is ahead at this instant?
37. Prove that a particle is speeding up if the velocity and acceleration have the same sign, and slowing down if they have opposite signs. [Hint: Let $r(t) = |v(t)|$ and find $r'(t)$ using the chain rule.]
38. **Writing.** A speedometer on a bicycle calculates the bicycle's speed by measuring the time per rotation for one of the bicycle's wheels. Explain how this measurement can be used to calculate an average velocity for the bicycle, and discuss how well it approximates the instantaneous velocity for the bicycle.
39. **Writing.** A toy rocket is launched into the air and falls to the ground after its fuel runs out. Describe the rocket's acceleration and when the rocket is speeding up or slowing down during its flight. Accompany your description with a sketch of a graph of the rocket's acceleration versus time.

---

## 3.7 NEWTON'S METHOD

In Section 1.5 we showed how to approximate the roots of an equation $f(x) = 0$ using the Intermediate-Value Theorem. In this section we will study a technique, called "Newton's Method," that is usually more efficient than that method. Newton's Method is the technique used by many commercial and scientific computer programs for finding roots.

> **Niels Henrik Abel (1802–1829)**  
> Norwegian mathematician. In his brief life of 26 years Abel lived in virtual poverty, yet he managed to prove major results that altered the mathematical landscape forever. In 1824 he published at his own expense the proof that it is impossible to solve the general fifth-degree polynomial equation algebraically. In the summer of 1826 he completed a landmark work on transcendental functions, which was submitted to the French Academy of Sciences. He died of tuberculosis in 1829, just two days before a letter arrived informing him that a professorship had been secured for him in Berlin.

### NEWTON'S METHOD FORMULA

Suppose that we are trying to find a root $r$ of the equation $f(x) = 0$. Given an initial approximation $x_1$, the tangent line to $y = f(x)$ at $x_1$ has equation
$$y - f(x_1) = f'(x_1)(x - x_1) \tag{1}$$
If $f'(x_1) \neq 0$, the $x$-intercept $x_2$ satisfies $-f(x_1) = f'(x_1)(x_2 - x_1)$, so
$$x_2 = x_1 - \frac{f(x_1)}{f'(x_1)} \tag{2}$$
In general, if $x_n$ is the $n$th approximation, the improved approximation $x_{n+1}$ is given by:

> **Newton's Method Formula**  
> $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}, \quad n = 1, 2, 3, \dots \tag{4}$$

#### Example 1
Use Newton's Method to approximate the real solutions of $x^3 - x - 1 = 0$.

**Solution.** Let $f(x) = x^3 - x - 1$, so $f'(x) = 3x^2 - 1$.
$$x_{n+1} = x_n - \frac{x_n^3 - x_n - 1}{3x_n^2 - 1}$$
Choosing $x_1 = 1.5$:
$$x_2 \approx 1.34782609$$
$$x_3 \approx 1.32520040$$
$$x_4 \approx 1.32471817$$
$$x_5 \approx 1.32471796$$
$$x_6 \approx 1.32471796$$
Thus, $x \approx 1.32471796$.

#### Example 2
Use Newton's Method to approximate the solution of $\cos x = x$.

**Solution.** Rewrite as $x - \cos x = 0$. $f(x) = x - \cos x, \ f'(x) = 1 + \sin x$.
$$x_{n+1} = x_n - \frac{x_n - \cos x_n}{1 + \sin x_n}$$
With $x_1 = 1$:
$$x_2 \approx 0.750363868$$
$$x_3 \approx 0.739112891$$
$$x_4 \approx 0.739085133$$
$$x_5 \approx 0.739085133$$
Thus, $x \approx 0.739085133$.

---

### SOME DIFFICULTIES WITH NEWTON'S METHOD

* If $f'(x_n) = 0$, the formula involves division by zero (the tangent line is horizontal and does not cross the $x$-axis).
* Newton's Method may fail to converge altogether, or may cycle endlessly, or converge to a different root than intended. For example, applying Newton's method to $x^{1/3} = 0$ with $x_1 = 1$ yields $x_{n+1} = -2x_n$, so the iterates $1, -2, 4, -8, \dots$ diverge.

---

### QUICK CHECK EXERCISES 3.7
*(See page 252 for answers.)*

1. Use the accompanying graph to estimate $x_2$ and $x_3$ if Newton's Method is applied to the equation $y = f(x)$ with $x_1 = 8$.
2. Suppose that $f(1) = 2$ and $f'(1) = 4$. If Newton's Method is applied to $y = f(x)$ with $x_1 = 1$, then $x_2 = \underline{\hspace{1.5cm}}$.
3. Suppose we are given that $f(0) = 3$ and that $x_2 = 3$ when Newton's Method is applied to $y = f(x)$ with $x_1 = 0$. Then $f'(0) = \underline{\hspace{1.5cm}}$.
4. If Newton's Method is applied to $y = x^5 - 2$ with $x_1 = 1$, then $x_2 = \underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 3.7
1. $x_2 \approx 4, \ x_3 \approx 2$  
2. $\frac{1}{2}$  
3. $-1$  
4. $1.2$

---

### EXERCISE SET 3.7

**1–4 Radical Approximations**

1. Approximate $\sqrt{2}$ by applying Newton's Method to the equation $x^2 - 2 = 0$.
2. Approximate $\sqrt{5}$ by applying Newton's Method to the equation $x^2 - 5 = 0$.
3. Approximate $\sqrt[3]{6}$ by applying Newton's Method to the equation $x^3 - 6 = 0$.
4. To what equation would you apply Newton's Method to approximate the $n$th root of $a$?

**5–8 The given equation has one real solution. Approximate it by Newton's Method.**

5. $x^3 - 2x - 2 = 0$
6. $x^3 + x - 1 = 0$
7. $x^5 + x^4 - 5 = 0$
8. $x^5 - 3x + 3 = 0$

**9–14 Use a graphing utility to determine how many solutions the equation has, and then use Newton's Method to approximate the solution that satisfies the stated condition.**

9. $x^4 + x^2 - 4 = 0; \quad x < 0$
10. $x^5 - 5x^3 - 2 = 0; \quad x > 0$
11. $2\cos x = x; \quad x > 0$
12. $\sin x = x^2; \quad x > 0$
13. $x - \tan x = 0; \quad \pi/2 < x < 3\pi/2$
14. $1 + x^2\sin x = 0; \quad \pi/2 < x < 3\pi/2$

**15–20 Use a graphing utility to determine the number of times the curves intersect; and then apply Newton's Method, where needed, to approximate the $x$-coordinates of all intersections.**

15. $y = x^3$ and $y = 1 - x$
16. $y = \sin x$ and $y = x^3 - 2x^2 + 1$
17. $y = x^2$ and $y = \sqrt{2x + 1}$
18. $y = \frac{1}{8}x^3 - 1$ and $y = \cos x - 2$

**19–22 True–False Determine whether the statement is true or false. Explain your answer.**

19. Newton's Method uses the tangent line to $y = f(x)$ at $x = x_n$ to compute $x_{n+1}$.
20. Newton's Method is a process to find exact solutions to $f(x) = 0$.
21. If $f(x) = 0$ has a root, then Newton's Method starting at $x = x_1$ will approximate the root nearest $x_1$.
22. Newton's Method can be used to approximate a point of intersection of two curves.

23. The mechanic's rule for approximating square roots states that $\sqrt{a} \approx x_{n+1}$, where
    $$x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right), \quad n = 1, 2, 3, \dots$$
    and $x_1$ is any positive approximation to $\sqrt{a}$.  
    (a) Apply Newton's Method to $f(x) = x^2 - a$ to derive the mechanic's rule.  
    (b) Use the mechanic's rule to approximate $\sqrt{10}$.
24. Many calculators compute reciprocals using the approximation $1/a \approx x_{n+1}$, where
    $$x_{n+1} = x_n(2 - ax_n), \quad n = 1, 2, 3, \dots$$
    and $x_1$ is an initial approximation to $1/a$.  
    (a) Apply Newton's Method to $f(x) = \frac{1}{x} - a$ to derive this approximation.  
    (b) Use the formula to approximate $\frac{1}{17}$.
25. Use Newton's Method to approximate the absolute minimum of $f(x) = \frac{1}{4}x^4 + x^2 - 5x$.
26. Use Newton's Method to approximate the absolute maximum of $f(x) = x\sin x$ on the interval $[0, \pi]$.
27. Use Newton's Method to approximate the coordinates of the point on the parabola $y = x^2$ that is closest to the point $(1, 0)$.
28. Use Newton's Method to approximate the dimensions of the rectangle of largest area that can be inscribed under the curve $y = \cos x$ for $0 \le x \le \pi/2$ (Figure Ex-28).
29. (a) Show that on a circle of radius $r$, the central angle $\theta$ that subtends an arc whose length is 1.5 times the length $L$ of its chord satisfies the equation $\theta = 3\sin(\theta/2)$ (Figure Ex-29).  
    (b) Use Newton's Method to approximate $\theta$.
30. A segment of a circle is the region enclosed by an arc and its chord. If $r$ is the radius of the circle and $\theta$ the angle subtended at the center of the circle, then the area $A$ of the segment is $A = \frac{1}{2}r^2(\theta - \sin\theta)$, where $\theta$ is in radians. Find the value of $\theta$ for which the area of the segment is one-fourth the area of the circle. Give $\theta$ to the nearest degree.

**31–32 Use Newton's Method to approximate all real values of $y$ satisfying the given equation for the indicated value of $x$.**

31. $xy^4 + x^3y = 1; \quad x = 1$
32. $xy - \cos\left(\frac{1}{2}xy\right) = 0; \quad x = 2$

33. An annuity is a sequence of equal payments that are paid or received at regular time intervals. When payments of $Q$ dollars are deposited at the end of each year into an account paying $i \times 100\%$ compounded annually, the amount $S(n)$ after the $n$th payment is
    $$S(n) = \frac{Q}{i}[(1 + i)^n - 1]$$
    Suppose that you can invest $\$5000$ at the end of each year, and your objective is to have $\$250,000$ on the 25th payment. Approximately what annual compound interest rate must the account pay? [Hint: Show that $50i = (1 + i)^{25} - 1$, and solve it using Newton's Method.]

**FOCUS ON CONCEPTS**

34. (a) Use a graphing utility to generate the graph of $f(x) = \frac{x}{x^2 + 1}$ and use it to explain what happens if you apply Newton's Method with a starting value of $x_1 = 2$. Check your conclusion by computing $x_2, x_3, x_4,$ and $x_5$.  
    (b) Use the graph generated in part (a) to explain what happens if you apply Newton's Method with a starting value of $x_1 = 0.5$. Check your conclusion by computing $x_2, x_3, x_4,$ and $x_5$.
35. (a) Apply Newton's Method to $f(x) = x^2 + 1$ with a starting value of $x_1 = 0.5$, and determine if the values of $x_2, \dots, x_{10}$ appear to converge.  
    (b) Explain what is happening.
36. In each part, explain what happens if you apply Newton's Method to a function $f$ when the given condition is satisfied for some value of $n$:  
    (a) $f(x_n) = 0$  
    (b) $x_{n+1} = x_n$  
    (c) $x_{n+2} = x_n \neq x_{n+1}$
37. **Writing.** Compare Newton's Method and the Intermediate-Value Theorem (1.5.8; see Example 6 in Section 1.5) as methods to locate solutions to $f(x) = 0$.
38. **Writing.** Newton's Method uses a local linear approximation to $y = f(x)$ at $x = x_n$ to find an "improved" approximation $x_{n+1}$ to a zero of $f$. Your friend proposes a process that uses a local quadratic approximation to $y = f(x)$ at $x = x_n$ (that is, matching values for the function and its first two derivatives) to obtain $x_{n+1}$. Discuss the pros and cons of this proposal. Support your statements with some examples.

---

## 3.8 ROLLE'S THEOREM; MEAN-VALUE THEOREM

In this section we will discuss a result called the Mean-Value Theorem. This theorem has so many important consequences that it is regarded as one of the major principles in calculus.

### ROLLE'S THEOREM

> **3.8.1 THEOREM (Rolle's Theorem)**  
> Let $f$ be continuous on the closed interval $[a, b]$ and differentiable on the open interval $(a, b)$. If
> $$f(a) = 0 \quad \text{and} \quad f(b) = 0$$
> then there is at least one point $c$ in the interval $(a, b)$ such that $f'(c) = 0$.

> **Michel Rolle (1652–1719)**  
> French mathematician known for Diophantine analysis and the algebra of equations (*Traité d'algèbre*, 1690). Rolle established the notation $\sqrt[n]{a}$ for the $n$th root of $a$, and proved a polynomial version of the theorem that today bears his name.

**Proof.** We divide the proof into three cases:
* **Case 1.** If $f(x) = 0$ for all $x$ in $(a, b)$, then $f'(c) = 0$ at every point $c$ in $(a, b)$ because $f$ is constant.
* **Case 2.** Assume that $f(x) > 0$ at some point in $(a, b)$. Since $f$ is continuous on $[a, b]$, by the Extreme-Value Theorem $f$ has an absolute maximum on $[a, b]$. The absolute maximum cannot occur at $a$ or $b$ because $f(a) = f(b) = 0$ and $f(x) > 0$ inside. Thus the absolute maximum occurs at some point $c \in (a, b)$. By Theorem 3.4.3, $c$ is a critical point, and since $f$ is differentiable on $(a, b)$, $f'(c) = 0$.
* **Case 3.** Assume that $f(x) < 0$ at some point in $(a, b)$. The proof is similar to Case 2 using the absolute minimum. $\blacksquare$

#### Example 1
Find the two $x$-intercepts of $f(x) = x^2 - 5x + 4$ and confirm that $f'(c) = 0$ at some point $c$ between those intercepts.

**Solution.** $x^2 - 5x + 4 = (x - 1)(x - 4) = 0 \implies x = 1, 4$. $f'(x) = 2x - 5 = 0 \implies c = 5/2 \in (1, 4)$.

#### Example 2
The differentiability requirement in Rolle's Theorem is critical. For $f(x) = |x| - 1$ on $[-1, 1]$, $f(-1) = f(1) = 0$, but $f'(x)$ is undefined at $x = 0$ and there is no point where $f'(c) = 0$.

#### Example 3
For $f(x) = \sin x$ on $[0, 2\pi]$, $f(0) = f(2\pi) = 0$. $f'(x) = \cos x = 0$ has two solutions in $(0, 2\pi)$: $c_1 = \pi/2$ and $c_2 = 3\pi/2$.

---

### THE MEAN-VALUE THEOREM

> **3.8.2 THEOREM (Mean-Value Theorem)**  
> Let $f$ be continuous on the closed interval $[a, b]$ and differentiable on the open interval $(a, b)$. Then there is at least one point $c$ in $(a, b)$ such that
> $$f'(c) = \frac{f(b) - f(a)}{b - a} \tag{1}$$

**Proof.** The equation of the secant line joining $(a, f(a))$ and $(b, f(b))$ is
$$y = \frac{f(b) - f(a)}{b - a}(x - a) + f(a)$$
The difference function $v(x)$ between the curve and secant line is
$$v(x) = f(x) - \left[\frac{f(b) - f(a)}{b - a}(x - a) + f(a)\right] \tag{2}$$
$v(x)$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $v(a) = 0, v(b) = 0$. By Rolle's Theorem, there exists $c \in (a, b)$ such that $v'(c) = 0$. Since
$$v'(x) = f'(x) - \frac{f(b) - f(a)}{b - a}$$
we obtain $f'(c) = \frac{f(b) - f(a)}{b - a}$. $\blacksquare$

#### Example 4
Show that the function $f(x) = \frac{1}{4}x^3 + 1$ satisfies the hypotheses of the Mean-Value Theorem over $[0, 2]$, and find all values of $c \in (0, 2)$ at which the tangent line is parallel to the secant line joining $(0, f(0))$ and $(2, f(2))$.

**Solution.** $f(0) = 1, f(2) = 3$. Average slope $= \frac{3 - 1}{2 - 0} = 1$.
$$f'(c) = \frac{3c^2}{4} = 1 \implies 3c^2 = 4 \implies c = \pm\frac{2}{\sqrt{3}} \approx \pm 1.15$$
Only $c = 2/\sqrt{3} \in (0, 2)$.

#### Example 5 (Velocity Interpretation)
You are driving on a straight highway with speed limit $55\text{ mi/h}$. At 8:05 a.m. police clock your velocity at $50\text{ mi/h}$ and at 8:10 a.m. a second police car 5 miles down the road clocks your velocity at $55\text{ mi/h}$. Explain why the police have a right to charge you with a speeding violation.

**Solution.** You traveled $5\text{ miles}$ in $5\text{ minutes} = 1/12\text{ hr}$. Your average velocity was $\frac{5}{1/12} = 60\text{ mi/h}$. By the Mean-Value Theorem, your instantaneous velocity was $60\text{ mi/h}$ at least once.

---

### CONSEQUENCES OF THE MEAN-VALUE THEOREM

> **3.1.2 THEOREM (Revisited)**  
> Let $f$ be continuous on $[a, b]$ and differentiable on $(a, b)$.  
> (a) If $f'(x) > 0$ for all $x \in (a, b)$, then $f$ is increasing on $[a, b]$.  
> (b) If $f'(x) < 0$ for all $x \in (a, b)$, then $f$ is decreasing on $[a, b]$.  
> (c) If $f'(x) = 0$ for all $x \in (a, b)$, then $f$ is constant on $[a, b]$.

**Proof of (a).** Let $x_1, x_2 \in [a, b]$ with $x_1 < x_2$. On $[x_1, x_2]$, by the Mean-Value Theorem there exists $c \in (x_1, x_2)$ such that
$$f(x_2) - f(x_1) = f'(c)(x_2 - x_1)$$
Since $f'(c) > 0$ and $x_2 - x_1 > 0$, $f(x_2) - f(x_1) > 0 \implies f(x_1) < f(x_2)$. $\blacksquare$

---

### THE CONSTANT DIFFERENCE THEOREM

> **3.8.3 THEOREM (Constant Difference Theorem)**  
> If $f$ and $g$ are differentiable on an interval, and if $f'(x) = g'(x)$ for all $x$ in that interval, then $f - g$ is constant on the interval; that is, there is a constant $k$ such that
> $$f(x) = g(x) + k$$
> for all $x$ in the interval.

**Proof.** Let $F(x) = f(x) - g(x)$. Then $F'(x) = f'(x) - g'(x) = 0$ on the interval. By Theorem 3.1.2(c), $F(x) = k$ is constant. $\blacksquare$

---

### QUICK CHECK EXERCISES 3.8
*(See page 259 for answers.)*

1. Let $f(x) = x^2 - x$.  
   (a) An interval on which $f$ satisfies the hypotheses of Rolle's Theorem is $\underline{\hspace{1.5cm}}$.  
   (b) Find all values of $c$ that satisfy the conclusion of Rolle's Theorem for the function $f$ on the interval in part (a).
2. Use the accompanying graph of $f$ to find an interval $[a, b]$ on which Rolle's Theorem applies, and find all values of $c$ in that interval that satisfy the conclusion of the theorem.
3. Let $f(x) = x^2 - x$.  
   (a) Find a point $b$ such that the slope of the secant line through $(0, 0)$ and $(b, f(b))$ is 1.  
   (b) Find all values of $c$ that satisfy the conclusion of the Mean-Value Theorem for the function $f$ on the interval $[0, b]$, where $b$ is the point found in part (a).
4. Use the graph of $f$ in the accompanying figure to estimate all values of $c$ that satisfy the conclusion of the Mean-Value Theorem on the interval  
   (a) $[0, 8]$ (b) $[0, 4]$.
5. Find a function $f$ such that the graph of $f$ contains the point $(1, 5)$ and such that for every value of $x_0$ the tangent line to the graph of $f$ at $x_0$ is parallel to the tangent line to the graph of $y = x^2$ at $x_0$.

#### QUICK CHECK ANSWERS 3.8
1. (a) $[0, 1]$ (b) $c = \frac{1}{2}$  
2. $[-3, 3]; \quad c = -2, 0, 2$  
3. (a) $b = 2$ (b) $c = 1$  
4. (a) $1.5$ (b) $0.8$  
5. $f(x) = x^2 + 4$

---

### EXERCISE SET 3.8

**1–4 Verify that the hypotheses of Rolle's Theorem are satisfied on the given interval, and find all values of $c$ in that interval that satisfy the conclusion of the theorem.**

1. $f(x) = x^2 - 8x + 15; \quad [3, 5]$
2. $f(x) = \frac{1}{2}x - \sqrt{x}; \quad [0, 4]$
3. $f(x) = \cos x; \quad [\pi/2, 3\pi/2]$
4. $f(x) = (x^2 - 1)/(x - 2); \quad [-1, 1]$

**5–8 Verify that the hypotheses of the Mean-Value Theorem are satisfied on the given interval, and find all values of $c$ in that interval that satisfy the conclusion of the theorem.**

5. $f(x) = x^2 - x; \quad [-3, 5]$
6. $f(x) = x^3 + x - 4; \quad [-1, 2]$
7. $f(x) = \sqrt{25 - x^2}; \quad [-5, 3]$
8. $f(x) = x - \frac{1}{x}; \quad [3, 4]$

9. (a) Find an interval $[a, b]$ on which $f(x) = x^4 + x^3 - x^2 + x - 2$ satisfies the hypotheses of Rolle's Theorem.  
   (b) Generate the graph of $f'(x)$, and use it to make rough estimates of all values of $c$ in the interval obtained in part (a) that satisfy the conclusion of Rolle's Theorem.  
   (c) Use Newton's Method to improve on the rough estimates obtained in part (b).
10. Let $f(x) = x^3 - 4x$.  
    (a) Find the equation of the secant line through the points $(-2, f(-2))$ and $(1, f(1))$.  
    (b) Show that there is only one point $c$ in the interval $(-2, 1)$ that satisfies the conclusion of the Mean-Value Theorem for the secant line in part (a).  
    (c) Find the equation of the tangent line to the graph of $f$ at the point $(c, f(c))$.  
    (d) Use a graphing utility to generate the secant line in part (a) and the tangent line in part (c) in the same coordinate system, and confirm visually that the two lines seem parallel.

**11–14 True–False Determine whether the statement is true or false. Explain your answer.**

11. Rolle's Theorem says that if $f$ is a continuous function on $[a, b]$ and $f(a) = f(b)$, then there is a point between $a$ and $b$ at which the curve $y = f(x)$ has a horizontal tangent line.
12. If $f$ is continuous on a closed interval $[a, b]$ and differentiable on $(a, b)$, then there is a point between $a$ and $b$ at which the instantaneous rate of change of $f$ matches the average rate of change of $f$ over $[a, b]$.
13. The Constant Difference Theorem says that if two functions have derivatives that differ by a constant on an interval, then the functions are equal on the interval.
14. One application of the Mean-Value Theorem is to prove that a function with positive derivative on an interval must be increasing on that interval.

**FOCUS ON CONCEPTS**

15. Let $f(x) = \tan x$.  
    (a) Show that there is no point $c$ in the interval $(0, \pi)$ such that $f'(c) = 0$, even though $f(0) = f(\pi) = 0$.  
    (b) Explain why the result in part (a) does not contradict Rolle's Theorem.
16. Let $f(x) = x^{2/3}, a = -1,$ and $b = 8$.  
    (a) Show that there is no point $c$ in $(a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$.  
    (b) Explain why the result in part (a) does not contradict the Mean-Value Theorem.
17. (a) Show that if $f$ is differentiable on $(-\infty, +\infty)$, and if $y = f(x)$ and $y = f'(x)$ are graphed in the same coordinate system, then between any two $x$-intercepts of $f$ there is at least one $x$-intercept of $f'$.  
    (b) Give some examples that illustrate this.
18. Review Formulas (8) and (9) in Section 2.1 and use the Mean-Value Theorem to show that if $f$ is differentiable on $(-\infty, +\infty)$, then for any interval $[x_0, x_1]$ there is at least one point in $(x_0, x_1)$ where the instantaneous rate of change of $y$ with respect to $x$ is equal to the average rate of change over the interval.

**19–21 Use the result of Exercise 18 in these exercises.**

19. An automobile travels $4\text{ mi}$ along a straight road in $5\text{ min}$. Show that the speedometer reads exactly $48\text{ mi/h}$ at least once during the trip.
20. At 11 a.m. on a certain morning the outside temperature was $76^\circ\text{F}$. At 11 p.m. that evening it had dropped to $52^\circ\text{F}$.  
    (a) Show that at some instant during this period the temperature was decreasing at the rate of $2^\circ\text{F/h}$.  
    (b) Suppose that you know the temperature reached a high of $88^\circ\text{F}$ sometime between 11 a.m. and 11 p.m. Show that at some instant during this period the temperature was decreasing at a rate greater than $3^\circ\text{F/h}$.
21. Suppose that two runners in a $100\text{ m}$ dash finish in a tie. Show that they had the same velocity at least once during the race.
22. Use the fact that
    $$\frac{d}{dx}(3x^4 + x^2 - 4x) = 12x^3 + 2x - 4$$
    to show that the equation $12x^3 + 2x - 4 = 0$ has at least one solution in the interval $(0, 1)$.
23. (a) Use the Constant Difference Theorem (3.8.3) to show that if $f'(x) = g'(x)$ for all $x$ in the interval $(-\infty, +\infty)$, and if $f$ and $g$ have the same value at some point $x_0$, then $f(x) = g(x)$ for all $x$ in $(-\infty, +\infty)$.  
    (b) Use the result in part (a) to confirm the trigonometric identity $\sin^2 x + \cos^2 x = 1$.
24. (a) Use the Constant Difference Theorem (3.8.3) to show that if $f'(x) = g'(x)$ for all $x$ in $(-\infty, +\infty)$, and if $f(x_0) - g(x_0) = c$ at some point $x_0$, then $f(x) - g(x) = c$ for all $x$ in $(-\infty, +\infty)$.  
    (b) Use the result in part (a) to show that the function
    $$h(x) = (x - 1)^3 - (x^2 + 3)(x - 3)$$
    is constant for all $x$ in $(-\infty, +\infty)$, and find the constant.  
    (c) Check the result in part (b) by multiplying out and simplifying the formula for $h(x)$.

**FOCUS ON CONCEPTS**

25. (a) Use the Mean-Value Theorem to show that if $f$ is differentiable on an interval, and if $|f'(x)| \le M$ for all values of $x$ in the interval, then
    $$|f(x) - f(y)| \le M|x - y|$$
    for all values of $x$ and $y$ in the interval.  
    (b) Use the result in part (a) to show that $|\sin x - \sin y| \le |x - y|$ for all real values of $x$ and $y$.
26. (a) Use the Mean-Value Theorem to show that if $f$ is differentiable on an open interval, and if $|f'(x)| \ge M$ for all values of $x$ in the interval, then $|f(x) - f(y)| \ge M|x - y|$ for all values of $x$ and $y$ in the interval.  
    (b) Use the result in part (a) to show that $|\tan x - \tan y| \ge |x - y|$ for all values of $x$ and $y$ in the interval $(-\pi/2, \pi/2)$.  
    (c) Use the result in part (b) to show that $|\tan x + \tan y| \ge |x + y|$ for all values of $x$ and $y$ in the interval $(-\pi/2, \pi/2)$.
27. (a) Use the Mean-Value Theorem to show that
    $$\sqrt{y} - \sqrt{x} < \frac{y - x}{2\sqrt{x}}$$
    if $0 < x < y$.  
    (b) Use the result in part (a) to show that if $0 < x < y$, then $\sqrt{xy} < \frac{1}{2}(x + y)$.
28. Show that if $f$ is differentiable on an open interval and $f'(x) \neq 0$ on the interval, the equation $f(x) = 0$ can have at most one real root in the interval.
29. Use the result in Exercise 28 to show the following:  
    (a) The equation $x^3 + 4x - 1 = 0$ has exactly one real root.  
    (b) If $b^2 - 3ac < 0$ and if $a \neq 0$, then the equation $ax^3 + bx^2 + cx + d = 0$ has exactly one real root.
30. Use the inequality $\sqrt{3} < 1.8$ to prove that $1.7 < \sqrt{3} < 1.75$. [Hint: Let $f(x) = \sqrt{x}, a = 3,$ and $b = 4$ in the Mean-Value Theorem.]
31. Use the Mean-Value Theorem to prove that
    $$x - \frac{x^3}{6} < \sin x < x \quad (x > 0)$$
32. Show that if $f$ and $g$ are functions for which $f'(x) = g(x)$ and $g'(x) = f(x)$ for all $x$, then $f^2(x) - g^2(x)$ is a constant.
33. (a) Show that if $f$ and $g$ are functions for which $f'(x) = g(x)$ and $g'(x) = -f(x)$ for all $x$, then $f^2(x) + g^2(x)$ is a constant.  
    (b) Give an example of functions $f$ and $g$ with this property.

**FOCUS ON CONCEPTS**

34. Let $f$ and $g$ be continuous on $[a, b]$ and differentiable on $(a, b)$. Prove: If $f(a) = g(a)$ and $f(b) = g(b)$, then there is a point $c$ in $(a, b)$ such that $f'(c) = g'(c)$.
35. Illustrate the result in Exercise 36 by drawing an appropriate picture.
36. (a) Prove that if $f''(x) > 0$ for all $x$ in $(a, b)$, then $f'(x) = 0$ at most once in $(a, b)$.  
    (b) Give a geometric interpretation of the result in (a).
37. (a) Prove part (b) of Theorem 3.1.2.  
    (b) Prove part (c) of Theorem 3.1.2.
38. Use the Mean-Value Theorem to prove the following result: Let $f$ be continuous at $x_0$ and suppose that $\lim_{x \to x_0} f'(x)$ exists. Then $f$ is differentiable at $x_0$, and
    $$f'(x_0) = \lim_{x \to x_0} f'(x)$$
39. Let
    $$f(x) = \begin{cases} 3x^2, & x \le 1 \\ ax + b, & x > 1 \end{cases}$$
    Find the values of $a$ and $b$ so that $f$ will be differentiable at $x = 1$.
40. (a) Let
    $$f(x) = \begin{cases} x^2, & x \le 0 \\ x^2 + 1, & x > 0 \end{cases}$$
    Show that $\lim_{x \to 0^-} f'(x) = \lim_{x \to 0^+} f'(x)$ but that $f'(0)$ does not exist.  
    (b) Let
    $$f(x) = \begin{cases} x^2, & x \le 0 \\ x^3, & x > 0 \end{cases}$$
    Show that $f'(0)$ exists but $f''(0)$ does not.
41. Use the Mean-Value Theorem to prove the following result: The graph of a function $f$ has a point of vertical tangency at $(x_0, f(x_0))$ if $f$ is continuous at $x_0$ and $f'(x)$ approaches either $+\infty$ or $-\infty$ as $x \to x_0^+$ and as $x \to x_0^-$.
42. **Writing.** Suppose that $p(x)$ is a nonconstant polynomial with zeros at $x = a$ and $x = b$. Explain how both the Extreme-Value Theorem (3.4.2) and Rolle's Theorem can be used to show that $p$ has a critical point between $a$ and $b$.
43. **Writing.** Find and describe a physical situation that illustrates the Mean-Value Theorem.

---

## CHAPTER 3 REVIEW EXERCISES

1. (a) If $x_1 < x_2$, what relationship must hold between $f(x_1)$ and $f(x_2)$ if $f$ is increasing on an interval containing $x_1$ and $x_2$? Decreasing? Constant?  
   (b) What condition on $f'$ ensures that $f$ is increasing on an interval $[a, b]$? Decreasing? Constant?
2. (a) What condition on $f'$ ensures that $f$ is concave up on an open interval? Concave down?  
   (b) What condition on $f''$ ensures that $f$ is concave up on an open interval? Concave down?  
   (c) In words, what is an inflection point of $f$?

**3–8 Find: (a) the intervals on which $f$ is increasing, (b) the intervals on which $f$ is decreasing, (c) the open intervals on which $f$ is concave up, (d) the open intervals on which $f$ is concave down, and (e) the $x$-coordinates of all inflection points.**

3. $f(x) = x^2 - 5x + 6$
4. $f(x) = x^4 - 8x^2 + 16$
5. $f(x) = \frac{x^2}{x^2 + 2}$
6. $f(x) = \sqrt[3]{x + 2}$
7. $f(x) = x^{1/3}(x + 4)$
8. $f(x) = x^{4/3} - x^{1/3}$

**9–12 Analyze the trigonometric function $f$ over the specified interval, stating where $f$ is increasing, decreasing, concave up, and concave down, and stating the $x$-coordinates of all inflection points. Confirm that your results are consistent with the graph of $f$ generated with a graphing utility.**

9. $f(x) = \cos x; \quad [0, 2\pi]$
10. $f(x) = \tan x; \quad (-\pi/2, \pi/2)$
11. $f(x) = \sin x \cos x; \quad [0, \pi]$
12. $f(x) = \cos^2 x - 2\sin x; \quad [0, 2\pi]$

13. In each part, sketch a continuous curve $y = f(x)$ with the stated properties.  
    (a) $f(2) = 4, \ f'(2) = 1, \ f''(x) < 0 \text{ for } x < 2, \ f''(x) > 0 \text{ for } x > 2$  
    (b) $f(2) = 4, \ f''(x) > 0 \text{ for } x < 2, \ f''(x) < 0 \text{ for } x > 2, \ \lim_{x \to 2^-} f'(x) = +\infty, \ \lim_{x \to 2^+} f'(x) = +\infty$  
    (c) $f(2) = 4, \ f''(x) < 0 \text{ for } x \neq 2, \ \lim_{x \to 2^-} f'(x) = 1, \ \lim_{x \to 2^+} f'(x) = -1$
14. In parts (a)–(d), the graph of a polynomial with degree at most 6 is given. Find equations for polynomials that produce graphs with these shapes, and check your answers with a graphing utility.
15. For a general quadratic polynomial $f(x) = ax^2 + bx + c \ (a \neq 0)$, find conditions on $a, b,$ and $c$ to ensure that $f$ is always increasing or always decreasing on $[0, +\infty)$.
16. For the general cubic polynomial $f(x) = ax^3 + bx^2 + cx + d \ (a \neq 0)$, find conditions on $a, b, c,$ and $d$ to ensure that $f$ is always increasing or always decreasing on $(-\infty, +\infty)$.
17. (a) Where on the graph of $y = f(x)$ would you expect $y$ to be increasing or decreasing most rapidly with respect to $x$?  
    (b) In words, what is a relative extremum?  
    (c) State a procedure for determining where the relative extrema of $f$ occur.
18. Determine whether the statement is true or false. If it is false, give an example for which the statement fails.  
    (a) If $f$ has a relative maximum at $x_0$, then $f(x_0)$ is the largest value that $f(x)$ can have.  
    (b) If the largest value for $f$ on the interval $(a, b)$ is at $x_0$, then $f$ has a relative maximum at $x_0$.  
    (c) A function $f$ has a relative extremum at each of its critical points.
19. (a) According to the first derivative test, what conditions ensure that $f$ has a relative maximum at $x_0$? A relative minimum?  
    (b) According to the second derivative test, what conditions ensure that $f$ has a relative maximum at $x_0$? A relative minimum?

**20–22 Locate the critical points and identify which critical points correspond to stationary points.**

20. (a) $f(x) = x^3 + 3x^2 - 9x + 1$  
    (b) $f(x) = x^4 - 6x^2 - 3$
21. (a) $f(x) = \frac{x}{x^2 + 2}$  
    (b) $f(x) = \frac{x^2 - 3}{x^2 + 1}$
22. (a) $f(x) = x^{1/3}(x - 4)$  
    (b) $f(x) = x^{4/3} - 6x^{1/3}$

23. In each part, find all critical points, and use the first derivative test to classify them as relative maxima, relative minima, or neither.  
    (a) $f(x) = x^{1/3}(x - 7)^2$  
    (b) $f(x) = 2\sin x - \cos 2x, \quad 0 \le x \le 2\pi$  
    (c) $f(x) = 3x - (x - 1)^{3/2}$
24. In each part, find all critical points, and use the second derivative test (where possible) to classify them as relative maxima, relative minima, or neither.  
    (a) $f(x) = x^{-1/2} + \frac{1}{9}x^{1/2}$  
    (b) $f(x) = x^2 + 8/x$  
    (c) $f(x) = \sin^2 x - \cos x, \quad 0 \le x \le 2\pi$

**25–32 Give a graph of the function $f$, and identify the limits as $x \to \pm\infty$, as well as locations of all relative extrema, inflection points, and asymptotes (as appropriate).**

25. $f(x) = x^4 - 3x^3 + 3x^2 + 1$
26. $f(x) = x^5 - 4x^4 + 4x^3$
27. $f(x) = \tan(x^2 + 1)$
28. $f(x) = x - \cos x$
29. $f(x) = \frac{x^2}{x^2 + 2x + 5}$
30. $f(x) = \frac{25 - 9x^2}{x^3}$
31. $f(x) = \begin{cases} \frac{1}{2}x^2, & x \le 0 \\ -x^2, & x > 0 \end{cases}$
32. $f(x) = (1 + x)^{2/3}(3 - x)^{1/3}$

**33–38 Use any method to find the relative extrema of the function $f$.**

33. $f(x) = x^3 + 5x - 2$
34. $f(x) = x^4 - 2x^2 + 7$
35. $f(x) = x^{4/5}$
36. $f(x) = 2x + x^{2/3}$
37. $f(x) = \frac{x^2}{x^2 + 1}$
38. $f(x) = \frac{x}{x + 2}$

**39–40 When using a graphing utility, important features of a graph may be missed if the viewing window is not chosen appropriately. This is illustrated in Exercises 39 and 40.**

39. (a) Generate the graph of $f(x) = \frac{1}{3}x^3 - \frac{1}{400}x$ over the interval $[-5, 5]$, and make a conjecture about the locations and nature of all critical points.  
    (b) Find the exact locations of all the critical points, and classify them as relative maxima, relative minima, or neither.  
    (c) Confirm the results in part (b) by graphing $f$ over an appropriate interval.
40. (a) Generate the graph of
    $$f(x) = \frac{1}{5}x^5 - \frac{7}{8}x^4 + \frac{1}{3}x^3 + \frac{7}{2}x^2 - 6x$$
    over the interval $[-5, 5]$, and make a conjecture about the locations and nature of all critical points.  
    (b) Find the exact locations of all the critical points, and classify them as relative maxima, relative minima, or neither.  
    (c) Confirm the results in part (b) by graphing portions of $f$ over appropriate intervals.
41. (a) Use a graphing utility to generate the graphs of $y = x$ and $y = (x^3 - 8)/(x^2 + 1)$ together over the interval $[-5, 5]$, and make a conjecture about the relationship between the two graphs.  
    (b) Confirm your conjecture in part (a).
42. Use implicit differentiation to show that a function defined implicitly by $\sin x + \cos y = 2y$ has a critical point whenever $\cos x = 0$. Then use either the first or second derivative test to classify these critical points as relative maxima or minima.
43. Let
    $$f(x) = \frac{2x^3 + x^2 - 15x + 7}{(2x - 1)(3x^2 + x - 1)}$$
    Graph $y = f(x)$, and find the equations of all horizontal and vertical asymptotes. Explain why there is no vertical asymptote at $x = 1/2$, even though the denominator of $f$ is zero at that point.
44. [CAS] Let
    $$f(x) = \frac{x^5 - x^4 - 3x^3 + 2x + 4}{x^7 - 2x^6 - 3x^5 + 6x^4 + 4x - 8}$$
    (a) Use a CAS to factor the numerator and denominator of $f$, and use the results to determine the locations of all vertical asymptotes.  
    (b) Confirm that your answer is consistent with the graph of $f$.
45. (a) What inequality must $f(x)$ satisfy for the function $f$ to have an absolute maximum on an interval $I$ at $x_0$?  
    (b) What inequality must $f(x)$ satisfy for $f$ to have an absolute minimum on an interval $I$ at $x_0$?  
    (c) What is the difference between an absolute extremum and a relative extremum?
46. According to the Extreme-Value Theorem, what conditions on a function $f$ and a given interval guarantee that $f$ will have both an absolute maximum and an absolute minimum on the interval?
47. In each part, determine whether the statement is true or false, and justify your answer.  
    (a) If $f$ is differentiable on the open interval $(a, b)$, and if $f$ has an absolute extremum on that interval, then it must occur at a stationary point of $f$.  
    (b) If $f$ is continuous on the open interval $(a, b)$, and if $f$ has an absolute extremum on that interval, then it must occur at a stationary point of $f$.

**48–50 In each part, find the absolute minimum $m$ and the absolute maximum $M$ of $f$ on the given interval (if they exist), and state where the absolute extrema occur.**

48. (a) $f(x) = 1/x; \quad [-2, -1]$  
    (b) $f(x) = x^3 - x^4; \quad [-1, 3/2]$  
    (c) $f(x) = x - \tan x; \quad [-\pi/4, \pi/4]$
49. (a) $f(x) = x^2 - 3x - 1; \quad (-\infty, +\infty)$  
    (b) $f(x) = x^3 - 3x - 2; \quad (-\infty, +\infty)$  
    (c) $f(x) = -|x^2 - 2x|; \quad [1, 3]$
50. (a) $f(x) = 2x^5 - 5x^4 + 7; \quad (-1, 3)$  
    (b) $f(x) = (3 - x)/(2 - x); \quad (0, 2)$  
    (c) $f(x) = 2x/(x^2 + 3); \quad (0, 2]$  
    (d) $f(x) = x^2(x - 2)^{1/3}; \quad (0, 3]$

51. In each part, use a graphing utility to estimate the absolute maximum and minimum values of $f$, if any, on the stated interval, and then use calculus methods to find the exact values.  
    (a) $f(x) = (x^2 - 1)^2; \quad (-\infty, +\infty)$  
    (b) $f(x) = x/(x^2 + 1); \quad [0, +\infty)$  
    (c) $f(x) = 2\sec x - \tan x; \quad [0, \pi/4]$
52. Prove that $\tan x > x$ for all $x$ in $(0, \pi/2)$.
53. [CAS] Let
    $$f(x) = \frac{x^3 + 2}{x^4 + 1}$$
    (a) Generate the graph of $y = f(x)$, and use the graph to make rough estimates of the coordinates of the absolute extrema.  
    (b) Use a CAS to solve the equation $f'(x) = 0$ and then use it to make more accurate approximations of the coordinates in part (a).
54. A church window consists of a blue semicircular section surmounting a clear rectangular section. The blue glass lets through half as much light per unit area as the clear glass. Find the radius $r$ of the window that admits the most light if the perimeter of the entire window is to be $P$ feet.
55. Find the dimensions of the rectangle of maximum area that can be inscribed inside the ellipse $(x/4)^2 + (y/3)^2 = 1$.
56. [CAS] As shown in Figure Ex-56, suppose that a boat enters the river at the point $(1, 0)$ and maintains a heading toward the origin. As a result of the strong current, the boat follows the path
    $$y = \frac{x^{10/3} - 1}{2x^{2/3}}$$
    where $x$ and $y$ are in miles.  
    (a) Graph the path taken by the boat.  
    (b) Can the boat reach the origin? If not, discuss its fate and find how close it comes to the origin.
57. A sheet of cardboard 12 in square is used to make an open box by cutting squares of equal size from the four corners and folding up the sides. What size squares should be cut to obtain a box with largest possible volume?
58. Is it true or false that a particle in rectilinear motion is speeding up when its velocity is increasing and slowing down when its velocity is decreasing? Justify your answer.
59. (a) Can an object in rectilinear motion reverse direction if its acceleration is constant? Justify your answer using a velocity versus time curve.  
    (b) Can an object in rectilinear motion have increasing speed and decreasing acceleration? Justify your answer using a velocity versus time curve.
60. Suppose that the position function of a particle in rectilinear motion is given by the formula $s(t) = t/(2t^2 + 8)$ for $t \ge 0$.  
    (a) Use a graphing utility to generate the position, velocity, and acceleration versus time curves.  
    (b) Use the appropriate graph to make a rough estimate of the time when the particle reverses direction, and then find that time exactly.  
    (c) Find the position, velocity, and acceleration at the instant when the particle reverses direction.  
    (d) Use the appropriate graphs to make rough estimates of the time intervals on which the particle is speeding up and the time intervals on which it is slowing down, and then find those time intervals exactly.  
    (e) When does the particle have its maximum and minimum velocities?
61. [CAS] For parts (a)–(f), suppose that the position function of a particle in rectilinear motion is given by the formula
    $$s(t) = \frac{t^2 + 1}{t^4 + 1}, \quad t \ge 0$$
    (a) Use a CAS to find simplified formulas for the velocity function $v(t)$ and the acceleration function $a(t)$.  
    (b) Graph the position, velocity, and acceleration versus time curves.  
    (c) Use the appropriate graph to make a rough estimate of the time at which the particle is farthest from the origin and its distance from the origin at that time.  
    (d) Use the appropriate graph to make a rough estimate of the time interval during which the particle is moving in the positive direction.  
    (e) Use the appropriate graphs to make rough estimates of the time intervals during which the particle is speeding up and the time intervals during which it is slowing down.  
    (f) Use the appropriate graph to make a rough estimate of the maximum speed of the particle and the time at which the maximum speed occurs.
62. Draw an appropriate picture, and describe the basic idea of Newton's Method without using any formulas.
63. Use Newton's Method to approximate all three solutions of $x^3 - 4x + 1 = 0$.
64. Use Newton's Method to approximate the smallest positive solution of $\sin x + \cos x = 0$.
65. Use a graphing utility to determine the number of times the curve $y = x^3$ intersects the curve $y = (x/2) - 1$. Then apply Newton's Method to approximate the $x$-coordinates of all intersections.
66. According to **Kepler's law**, the planets in our solar system move in elliptical orbits around the Sun. If a planet's closest approach to the Sun occurs at time $t = 0$, then the distance $r$ from the center of the planet to the center of the Sun at some later time $t$ can be determined from the equation
    $$r = a(1 - e\cos\phi)$$
    where $a$ is the average distance between centers, $e$ is a positive constant that measures the "flatness" of the elliptical orbit, and $\phi$ is the solution of **Kepler's equation**
    $$\frac{2\pi t}{T} = \phi - e\sin\phi$$
    in which $T$ is the time it takes for one complete orbit of the planet. Estimate the distance from the Earth to the Sun when $t = 90\text{ days}$. [First find $\phi$ from Kepler's equation, and then use this value of $\phi$ to find the distance. Use $a = 150 \times 10^6\text{ km}, e = 0.0167,$ and $T = 365\text{ days}$.]
67. Using the formulas in Exercise 66, find the distance from the planet Mars to the Sun when $t = 1\text{ year}$. For Mars use $a = 228 \times 10^6\text{ km}, e = 0.0934,$ and $T = 1.88\text{ years}$.
68. Suppose that $f$ is continuous on the closed interval $[a, b]$ and differentiable on the open interval $(a, b)$, and suppose that $f(a) = f(b)$. Is it true or false that $f$ must have at least one stationary point in $(a, b)$? Justify your answer.
69. In each part, determine whether all of the hypotheses of Rolle's Theorem are satisfied on the stated interval. If not, state which hypotheses fail; if so, find all values of $c$ guaranteed in the conclusion of the theorem.  
    (a) $f(x) = \sqrt{4 - x^2}$ on $[-2, 2]$  
    (b) $f(x) = x^{2/3} - 1$ on $[-1, 1]$  
    (c) $f(x) = \sin(x^2)$ on $[0, \sqrt{\pi}]$
70. In each part, determine whether all of the hypotheses of the Mean-Value Theorem are satisfied on the stated interval. If not, state which hypotheses fail; if so, find all values of $c$ guaranteed in the conclusion of the theorem.  
    (a) $f(x) = |x - 1|$ on $[-2, 2]$  
    (b) $f(x) = \frac{x + 1}{x - 1}$ on $[2, 3]$  
    (c) $f(x) = \begin{cases} 3 - x^2, & \text{if } x \le 1 \\ 2/x, & \text{if } x > 1 \end{cases}$ on $[0, 2]$
71. Use the fact that
    $$\frac{d}{dx}(x^6 - 2x^2 + x) = 6x^5 - 4x + 1$$
    to show that the equation $6x^5 - 4x + 1 = 0$ has at least one solution in the interval $(0, 1)$.
72. Let $g(x) = x^3 - 4x + 6$. Find $f(x)$ so that $f'(x) = g'(x)$ and $f(1) = 2$.

---

## CHAPTER 3 MAKING CONNECTIONS

1. Suppose that $g(x)$ is a function that is defined and differentiable for all real numbers $x$ and that $g(x)$ has the following properties:  
   (i) $g(0) = 2$ and $g'(0) = -2/3$.  
   (ii) $g(4) = 3$ and $g'(4) = 3$.  
   (iii) $g(x)$ is concave up for $x < 4$ and concave down for $x > 4$.  
   (iv) $g(x) \ge -10$ for all $x$.  
   Use these properties to answer the following questions:  
   (a) How many zeros does $g$ have?  
   (b) How many zeros does $g'$ have?  
   (c) Exactly one of the following limits is possible:
   $$\lim_{x \to +\infty} g'(x) = -5, \quad \lim_{x \to +\infty} g'(x) = 0, \quad \lim_{x \to +\infty} g'(x) = 5$$
   Identify which of these results is possible and draw a rough sketch of the graph of such a function $g(x)$. Explain why the other two results are impossible.

2. The two graphs in Figure Ex-2 depict a function $r(x)$ and its derivative $r'(x)$.  
   (a) Approximate the coordinates of each inflection point on the graph of $y = r(x)$.  
   (b) Suppose that $f(x)$ is a function that is continuous everywhere and whose derivative satisfies
   $$f'(x) = (x^2 - 4) \cdot r(x)$$
   What are the critical points for $f(x)$? At each critical point, identify whether $f(x)$ has a (relative) maximum, minimum, or neither a maximum or minimum. Approximate $f''(1)$.

3. With the function $r(x)$ as provided in Exercise 2, let $g(x)$ be a function that is continuous everywhere such that $g'(x) = x - r(x)$. For which values of $x$ does $g(x)$ have an inflection point?

4. Suppose that $f$ is a function whose derivative is continuous everywhere. Assume that there exists a real number $c$ such that when Newton's Method is applied to $f$, the inequality
   $$|x_n - c| < \frac{1}{n}$$
   is satisfied for all values of $n = 1, 2, 3, \dots$.  
   (a) Explain why $|x_{n+1} - x_n| < \frac{2}{n}$ for all values of $n = 1, 2, 3, \dots$.  
   (b) Show that there exists a positive constant $M$ such that
   $$|f(x_n)| \le M|x_{n+1} - x_n| < \frac{2M}{n}$$
   for all values of $n = 1, 2, 3, \dots$.  
   (c) Prove that if $f(c) \neq 0$, then there exists a positive integer $N$ such that
   $$\frac{|f(c)|}{2} < |f(x_n)|$$
   if $n > N$. [Hint: Argue that $f(x) \to f(c)$ as $x \to c$ and then apply Definition 1.4.1 with $\epsilon = \frac{1}{2}|f(c)|$.]  
   (d) What can you conclude from parts (b) and (c)?

5. What are the important elements in the argument suggested by Exercise 4? Can you extend this argument to a wider collection of functions?

6. A bug crawling on a linoleum floor along the edge of a plush carpet encounters an irregularity in the form of a 2 in by 3 in rectangular section of carpet that juts out into the linoleum as illustrated in Figure Ex-6a. The bug crawls at $0.7\text{ in/s}$ on the linoleum, but only at $0.3\text{ in/s}$ through the carpet, and its goal is to travel from point $A$ to point $B$. Four possible routes from $A$ to $B$ are as follows: (i) crawl on linoleum along the edge of the carpet; (ii) crawl through the carpet to a point on the wider side of the rectangle, and finish the journey on linoleum along the edge of the carpet; (iii) crawl through the carpet to a point on the shorter side of the rectangle, and finish the journey on linoleum along the edge of the carpet; or (iv) crawl through the carpet directly to point $B$. (See Figure Ex-6b.)  
   (a) Calculate the times it would take the bug to crawl from $A$ to $B$ via routes (i) and (iv).  
   (b) Suppose the bug follows route (ii) and use $x$ to represent the total distance the bug crawls on linoleum. Identify the appropriate interval for $x$ in this case, and determine the shortest time for the bug to complete the journey using route (ii).  
   (c) Suppose the bug follows route (iii) and again use $x$ to represent the total distance the bug crawls on linoleum. Identify the appropriate interval for $x$ in this case, and determine the shortest time for the bug to complete the journey using route (iii).  
   (d) Which of routes (i), (ii), (iii), or (iv) is quickest? What is the shortest time for the bug to complete the journey?
