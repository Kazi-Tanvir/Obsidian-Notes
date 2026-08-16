# CHAPTER 0: BEFORE CALCULUS

> The development of calculus in the seventeenth and eighteenth centuries was motivated by the need to understand physical phenomena such as the tides, the phases of the moon, the nature of light, and gravity.

One of the important themes in calculus is the analysis of relationships between physical or mathematical quantities. Such relationships can be described in terms of graphs, formulas, numerical data, or words. In this chapter we will develop the concept of a "function," which is the basic idea that underlies almost all mathematical and physical relationships, regardless of the form in which they are expressed. We will study properties of some of the most basic functions that occur in calculus.

---

## 0.1 FUNCTIONS

In this section we will define and develop the concept of a "function," which is the basic mathematical object that scientists and mathematicians use to describe relationships between variable quantities. Functions play a central role in calculus and its applications.

### DEFINITION OF A FUNCTION

Many scientific laws and engineering principles describe how one quantity depends on another. This idea was formalized in 1673 by Gottfried Wilhelm Leibniz who coined the term *function* to indicate the dependence of one quantity on another, as described in the following definition.

> **0.1.1 DEFINITION**  
> If a variable $y$ depends on a variable $x$ in such a way that each value of $x$ determines exactly one value of $y$, then we say that $y$ is a **function** of $x$.

Four common methods for representing functions are:
* **Numerically** by tables
* **Geometrically** by graphs
* **Algebraically** by formulas
* **Verbally**

The method of representation often depends on how the function arises. For example:
* **Table 0.1.1** shows the top qualifying speed $S$ for the Indianapolis 500 auto race as a function of the year $t$. There is exactly one value of $S$ for each value of $t$.

#### Table 0.1.1: Indianapolis 500 Qualifying Speeds
| Year $t$ | Speed $S$ (mi/h) | Year $t$ | Speed $S$ (mi/h) |
| :---: | :---: | :---: | :---: |
| 1994 | 228.011 | 2003 | 231.725 |
| 1995 | 231.604 | 2004 | 222.024 |
| 1996 | 233.100 | 2005 | 227.598 |
| 1997 | 218.263 | 2006 | 228.985 |
| 1998 | 223.503 | 2007 | 225.817 |
| 1999 | 225.179 | 2008 | 226.366 |
| 2000 | 223.471 | 2009 | 224.864 |
| 2001 | 226.037 | 2010 | 227.970 |
| 2002 | 231.342 | 2011 | 227.472 |

* **Figure 0.1.1** is a graphical record of an earthquake recorded on a seismograph. The graph describes the deflection $D$ of the seismograph needle as a function of the time $T$ elapsed since the wave left the earthquake's epicenter. There is exactly one value of $D$ for each value of $T$.
* Some of the most familiar functions arise from formulas; for example, the formula $C = 2\pi r$ expresses the circumference $C$ of a circle as a function of its radius $r$. There is exactly one value of $C$ for each value of $r$.
* Sometimes functions are described in words. For example, Isaac Newton's Law of Universal Gravitation is often stated as follows: *The gravitational force of attraction between two bodies in the Universe is directly proportional to the product of their masses and inversely proportional to the square of the distance between them.* This is the verbal description of the formula
  $$F = G\frac{m_1 m_2}{r^2}$$
  in which $F$ is the force of attraction, $m_1$ and $m_2$ are the masses, $r$ is the distance between them, and $G$ is a constant. If the masses are constant, then the verbal description defines $F$ as a function of $r$. There is exactly one value of $F$ for each value of $r$.

In the mid-eighteenth century the Swiss mathematician Leonhard Euler (pronounced "oiler") conceived the idea of denoting functions by letters of the alphabet, thereby making it possible to refer to functions without stating specific formulas, graphs, or tables. To understand Euler's idea, think of a function as a computer program that takes an input $x$, operates on it in some way, and produces exactly one output $y$. The computer program is an object in its own right, so we can give it a name, say $f$. Thus, the function $f$ (the computer program) associates a unique output $y$ with each input $x$ (Figure 0.1.2). This suggests the following definition.

> **0.1.2 DEFINITION**  
> A **function** $f$ is a rule that associates a unique output with each input. If the input is denoted by $x$, then the output is denoted by $f(x)$ (read "$f$ of $x$").

In this definition the term *unique* means "exactly one." Thus, a function cannot assign two different outputs to the same input. For example, Figure 0.1.3 shows a plot of weight versus age for a random sample of 100 college students. This plot does not describe $W$ as a function of $A$ because there are some values of $A$ with more than one corresponding value of $W$. This is to be expected, since two people with the same age can have different weights.

---

### INDEPENDENT AND DEPENDENT VARIABLES

For a given input $x$, the output of a function $f$ is called the **value of $f$ at $x$** or the **image of $x$ under $f$**. Sometimes we will want to denote the output by a single letter, say $y$, and write
$$y = f(x)$$
This equation expresses $y$ as a function of $x$; the variable $x$ is called the **independent variable** (or **argument**) of $f$, and the variable $y$ is called the **dependent variable** of $f$. This terminology is intended to suggest that $x$ is free to vary, but that once $x$ has a specific value a corresponding value of $y$ is determined. For now we will only consider functions in which the independent and dependent variables are real numbers, in which case we say that $f$ is a **real-valued function of a real variable**. Later, we will consider other kinds of functions.

#### Example 1
Table 0.1.2 describes a functional relationship $y = f(x)$ for which:
* $f(0) = 3$ ($f$ associates $y = 3$ with $x = 0$)
* $f(1) = 4$ ($f$ associates $y = 4$ with $x = 1$)
* $f(2) = -1$ ($f$ associates $y = -1$ with $x = 2$)
* $f(3) = 6$ ($f$ associates $y = 6$ with $x = 3$)

##### Table 0.1.2
| $x$ | 0 | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: | :---: |
| $y$ | 3 | 4 | -1 | 6 |

#### Example 2
The equation
$$y = 3x^2 - 4x + 2$$
has the form $y = f(x)$ in which the function $f$ is given by the formula
$$f(x) = 3x^2 - 4x + 2$$
For each input $x$, the corresponding output $y$ is obtained by substituting $x$ in this formula. For example,
* $f(0) = 3(0)^2 - 4(0) + 2 = 2$ ($f$ associates $y = 2$ with $x = 0$)
* $f(-1.7) = 3(-1.7)^2 - 4(-1.7) + 2 = 17.47$ ($f$ associates $y = 17.47$ with $x = -1.7$)
* $f(\sqrt{2}) = 3(\sqrt{2})^2 - 4\sqrt{2} + 2 = 8 - 4\sqrt{2}$ ($f$ associates $y = 8 - 4\sqrt{2}$ with $x = \sqrt{2}$)

> **Leonhard Euler (1707–1783)**  
> Euler was probably the most prolific mathematician who ever lived. It has been said that "Euler wrote mathematics as effortlessly as most men breathe." He was born in Basel, Switzerland, and was the son of a Protestant minister who had himself studied mathematics. Euler's genius developed early. He attended the University of Basel, where by age 16 he obtained both a Bachelor of Arts degree and a Master's degree in philosophy. While at Basel, Euler had the good fortune to be tutored one day a week in mathematics by a distinguished mathematician, Johann Bernoulli. At the urging of his father, Euler then began to study theology. The lure of mathematics was too great, however, and by age 18 Euler had begun to do mathematical research. Nevertheless, the influence of his father and his theological studies remained, and throughout his life Euler was a deeply religious, unaffected person. At various times Euler taught at St. Petersburg Academy of Sciences (in Russia), the University of Basel, and the Berlin Academy of Sciences.  
> Euler's energy and capacity for work were virtually boundless. His collected works form more than 100 quarto-sized volumes and it is believed that much of his work has been lost. What is particularly astonishing is that Euler was blind for the last 17 years of his life, and this was one of his most productive periods! Euler's flawless memory was phenomenal. Early in his life he memorized the entire *Aeneid* by Virgil, and at age 70 he could not only recite the entire work but could also state the first and last sentence on each page of the book from which he memorized the work. His ability to solve problems in his head was beyond belief. He worked out in his head major problems of lunar motion that baffled Isaac Newton and once did a complicated calculation in his head to settle an argument between two students whose computations differed in the fiftieth decimal place.  
> Following the development of calculus by Leibniz and Newton, results in mathematics developed rapidly in a disorganized way. Euler's genius gave coherence to the mathematical landscape. He was the first mathematician to bring the full power of calculus to bear on problems from physics. He made major contributions to virtually every branch of mathematics as well as to the theory of optics, planetary motion, electricity, magnetism, and general mechanics.

---

### GRAPHS OF FUNCTIONS

If $f$ is a real-valued function of a real variable, then the **graph of $f$** in the $xy$-plane is defined to be the graph of the equation $y = f(x)$. For example, the graph of the function $f(x) = x$ is the graph of the equation $y = x$, shown in Figure 0.1.4. That figure also shows the graphs of some other basic functions that may already be familiar to you ($y = x$, $y = x^2$, $y = x^3$, $y = 1/x$, $y = \sqrt{x}$, $y = \sqrt[3]{x}$). In Appendix A we discuss techniques for graphing functions using graphing technology.

> *Note:* Figure 0.1.4 shows only portions of the graphs. Where appropriate, and unless indicated otherwise, it is understood that graphs shown in this text extend indefinitely beyond the boundaries of the displayed figure.  
> Since $\sqrt{x}$ is imaginary for negative values of $x$, there are no points on the graph of $y = \sqrt{x}$ in the region where $x < 0$.

Graphs can provide valuable visual information about a function. For example, since the graph of a function $f$ in the $xy$-plane is the graph of the equation $y = f(x)$, the points on the graph of $f$ are of the form $(x, f(x))$; that is, the $y$-coordinate of a point on the graph of $f$ is the value of $f$ at the corresponding $x$-coordinate (Figure 0.1.5). The values of $x$ for which $f(x) = 0$ are the $x$-coordinates of the points where the graph of $f$ intersects the $x$-axis (Figure 0.1.6). These values are called the **zeros of $f$**, the **roots of $f(x) = 0$**, or the **$x$-intercepts** of the graph of $y = f(x)$.

---

### THE VERTICAL LINE TEST

Not every curve in the $xy$-plane is the graph of a function. For example, consider the curve in Figure 0.1.7, which is cut at two distinct points, $(a, b)$ and $(a, c)$, by a vertical line. This curve cannot be the graph of $y = f(x)$ for any function $f$; otherwise, we would have
$$f(a) = b \quad \text{and} \quad f(a) = c$$
which is impossible, since $f$ cannot assign two different values to $a$. Thus, there is no function $f$ whose graph is the given curve. This illustrates the following general result, which we will call the **vertical line test**.

> **0.1.3 THE VERTICAL LINE TEST**  
> A curve in the $xy$-plane is the graph of some function $f$ if and only if no vertical line intersects the curve more than once.

#### Example 3
The graph of the equation
$$x^2 + y^2 = 25$$
is a circle of radius 5 centered at the origin and hence there are vertical lines that cut the graph more than once (Figure 0.1.8). Thus this equation does not define $y$ as a function of $x$.

---

### THE ABSOLUTE VALUE FUNCTION

Recall that the **absolute value** or **magnitude** of a real number $x$ is defined by
$$|x| = \begin{cases} x, & x \ge 0 \\ -x, & x < 0 \end{cases}$$

The effect of taking the absolute value of a number is to strip away the minus sign if the number is negative and to leave the number unchanged if it is nonnegative. Thus,
$$|5| = 5, \quad \left|-\frac{4}{7}\right| = \frac{4}{7}, \quad |0| = 0$$

> *Note:* Symbols such as $+x$ and $-x$ are deceptive, since it is tempting to conclude that $+x$ is positive and $-x$ is negative. However, this need not be so, since $x$ itself can be positive or negative. For example, if $x$ is negative, say $x = -3$, then $-x = 3$ is positive and $+x = -3$ is negative.

A more detailed discussion of the properties of absolute value is given in Web Appendix F. However, for convenience we provide the following summary of its algebraic properties.

> **0.1.4 PROPERTIES OF ABSOLUTE VALUE**  
> If $a$ and $b$ are real numbers, then  
> (a) $|-a| = |a|$ — *A number and its negative have the same absolute value.*  
> (b) $|ab| = |a||b|$ — *The absolute value of a product is the product of the absolute values.*  
> (c) $|a/b| = |a|/|b|, \; b \neq 0$ — *The absolute value of a ratio is the ratio of the absolute values.*  
> (d) $|a + b| \le |a| + |b|$ — *The triangle inequality.*

The graph of the function $f(x) = |x|$ can be obtained by graphing the two parts of the equation
$$y = \begin{cases} x, & x \ge 0 \\ -x, & x < 0 \end{cases}$$
separately. Combining the two parts produces the V-shaped graph in Figure 0.1.9.

Absolute values have important relationships to square roots. To see why this is so, recall from algebra that every positive real number $x$ has two square roots, one positive and one negative. By definition, the symbol $\sqrt{x}$ denotes the *positive* square root of $x$.

> **WARNING**  
> To denote the negative square root you must write $-\sqrt{x}$. For example, the positive square root of 9 is $\sqrt{9} = 3$, whereas the negative square root of 9 is $-\sqrt{9} = -3$. (Do not make the mistake of writing $\sqrt{9} = \pm 3$.)

Care must be exercised in simplifying expressions of the form $\sqrt{x^2}$, since it is not always true that $\sqrt{x^2} = x$. This equation is correct if $x$ is nonnegative, but it is false if $x$ is negative. For example, if $x = -4$, then
$$\sqrt{x^2} = \sqrt{(-4)^2} = \sqrt{16} = 4 \neq x$$

A statement that is correct for all real values of $x$ is
$$\sqrt{x^2} = |x| \tag{1}$$

> **TECHNOLOGY MASTERY**  
> Verify (1) by using a graphing utility to show that the equations $y = \sqrt{x^2}$ and $y = |x|$ have the same graph.

---

### PIECEWISE-DEFINED FUNCTIONS

The absolute value function $f(x) = |x|$ is an example of a function that is defined **piecewise** in the sense that the formula for $f$ changes, depending on the value of $x$.

#### Example 4
Sketch the graph of the function defined piecewise by the formula
$$f(x) = \begin{cases} 0, & x \le -1 \\ \sqrt{1 - x^2}, & -1 < x < 1 \\ x, & x \ge 1 \end{cases}$$

**Solution.** The formula for $f$ changes at the points $x = -1$ and $x = 1$. (We call these the *breakpoints* for the formula.) A good procedure for graphing functions defined piecewise is to graph the function separately over the open intervals determined by the breakpoints, and then graph $f$ at the breakpoints themselves. For the function $f$ in this example the graph is the horizontal ray $y = 0$ on the interval $(-\infty, -1]$, it is the semicircle $y = \sqrt{1 - x^2}$ on the interval $(-1, 1)$, and it is the ray $y = x$ on the interval $[1, +\infty)$. The formula for $f$ specifies that the equation $y = 0$ applies at the breakpoint $-1$ [so $y = f(-1) = 0$], and it specifies that the equation $y = x$ applies at the breakpoint $1$ [so $y = f(1) = 1$]. The graph of $f$ is shown in Figure 0.1.10.

> **REMARK**  
> In Figure 0.1.10 the solid dot and open circle at the breakpoint $x = 1$ serve to emphasize that the point on the graph lies on the ray and not the semicircle. There is no ambiguity at the breakpoint $x = -1$ because the two parts of the graph join together continuously there.

#### Example 5
Increasing the speed at which air moves over a person's skin increases the rate of moisture evaporation and makes the person feel cooler. (This is why we fan ourselves in hot weather.) The *wind chill index* is the temperature at a wind speed of 4 mi/h that would produce the same sensation on exposed skin as the current temperature and wind speed combination. An empirical formula (i.e., a formula based on experimental data) for the wind chill index $W$ at $32^\circ\text{F}$ for a wind speed of $v\text{ mi/h}$ is
$$W = \begin{cases} 32, & 0 \le v \le 3 \\ 55.628 - 22.07v^{0.16}, & 3 < v \end{cases}$$
A computer-generated graph of $W(v)$ is shown in Figure 0.1.11.

---

### DOMAIN AND RANGE

If $x$ and $y$ are related by the equation $y = f(x)$, then the set of all allowable inputs ($x$-values) is called the **domain** of $f$, and the set of outputs ($y$-values) that result when $x$ varies over the domain is called the **range** of $f$. For example, if $f$ is the function defined by the table in Example 1, then the domain is the set $\{0, 1, 2, 3\}$ and the range is the set $\{-1, 3, 4, 6\}$.

Sometimes physical or geometric considerations impose restrictions on the allowable inputs of a function. For example, if $y$ denotes the area of a square of side $x$, then these variables are related by the equation $y = x^2$. Although this equation produces a unique value of $y$ for every real number $x$, the fact that lengths must be nonnegative imposes the requirement that $x \ge 0$.

> *Note:* One might argue that a physical square cannot have a side of length zero. However, it is often convenient mathematically to allow zero lengths, and we will do so throughout this text where appropriate.

When a function is defined by a mathematical formula, the formula itself may impose restrictions on the allowable inputs. For example, if $y = 1/x$, then $x = 0$ is not an allowable input since division by zero is undefined, and if $y = \sqrt{x}$, then negative values of $x$ are not allowable inputs because they produce imaginary values for $y$ and we have agreed to consider only real-valued functions of a real variable. In general, we make the following definition.

> **0.1.5 DEFINITION**  
> If a real-valued function of a real variable is defined by a formula, and if no domain is stated explicitly, then it is to be understood that the domain consists of all real numbers for which the formula yields a real value. This is called the **natural domain** of the function.

The domain and range of a function $f$ can be pictured by projecting the graph of $y = f(x)$ onto the coordinate axes as shown in Figure 0.1.12.

#### Example 6
Find the natural domain of
(a) $f(x) = x^3$  
(b) $f(x) = 1/[(x - 1)(x - 3)]$  
(c) $f(x) = \tan x$  
(d) $f(x) = \sqrt{x^2 - 5x + 6}$

**Solution (a).** The function $f$ has real values for all real $x$, so its natural domain is the interval $(-\infty, +\infty)$.

**Solution (b).** The function $f$ has real values for all real $x$, except $x = 1$ and $x = 3$, where divisions by zero occur. Thus, the natural domain is
$$\{x : x \neq 1 \text{ and } x \neq 3\} = (-\infty, 1) \cup (1, 3) \cup (3, +\infty)$$

**Solution (c).** Since $f(x) = \tan x = \sin x / \cos x$, the function $f$ has real values except where $\cos x = 0$, and this occurs when $x$ is an odd integer multiple of $\pi/2$. Thus, the natural domain consists of all real numbers except
$$x = \pm \frac{\pi}{2}, \pm \frac{3\pi}{2}, \pm \frac{5\pi}{2}, \dots$$

**Solution (d).** The function $f$ has real values, except when the expression inside the radical is negative. Thus the natural domain consists of all real numbers $x$ such that
$$x^2 - 5x + 6 = (x - 3)(x - 2) \ge 0$$
This inequality is satisfied if $x \le 2$ or $x \ge 3$ (verify), so the natural domain of $f$ is
$$(-\infty, 2] \cup [3, +\infty)$$

---

In some cases we will state the domain explicitly when defining a function. For example, if $f(x) = x^2$ is the area of a square of side $x$, then we can write
$$f(x) = x^2, \quad x \ge 0$$
to indicate that we take the domain of $f$ to be the set of nonnegative real numbers (Figure 0.1.13).

---

### THE EFFECT OF ALGEBRAIC OPERATIONS ON THE DOMAIN

Algebraic expressions are frequently simplified by canceling common factors in the numerator and denominator. However, care must be exercised when simplifying formulas for functions in this way, since this process can alter the domain.

#### Example 7
The natural domain of the function
$$f(x) = \frac{x^2 - 4}{x - 2} \tag{2}$$
consists of all real $x$ except $x = 2$. However, if we factor the numerator and then cancel the common factor in the numerator and denominator, we obtain
$$f(x) = \frac{(x - 2)(x + 2)}{x - 2} = x + 2 \tag{3}$$
Since the right side of (3) has a value of $f(2) = 4$ and $f(2)$ was undefined in (2), the algebraic simplification has changed the function. Geometrically, the graph of (3) is the line in Figure 0.1.14a, whereas the graph of (2) is the same line but with a hole at $x = 2$, since the function is undefined there (Figure 0.1.14b). In short, the geometric effect of the algebraic cancellation is to eliminate the hole in the original graph.

Sometimes alterations to the domain of a function that result from algebraic simplification are irrelevant to the problem at hand and can be ignored. However, if the domain must be preserved, then one must impose the restrictions on the simplified function explicitly. For example, if we wanted to preserve the domain of the function in Example 7, then we would have to express the simplified form of the function as
$$f(x) = x + 2, \quad x \neq 2$$

#### Example 8
Find the domain and range of
(a) $f(x) = 2 + \sqrt{x - 1}$  
(b) $f(x) = (x + 1)/(x - 1)$

**Solution (a).** Since no domain is stated explicitly, the domain of $f$ is its natural domain, $[1, +\infty)$. As $x$ varies over the interval $[1, +\infty)$, the value of $\sqrt{x - 1}$ varies over the interval $[0, +\infty)$, so the value of $f(x) = 2 + \sqrt{x - 1}$ varies over the interval $[2, +\infty)$, which is the range of $f$. The domain and range are highlighted in green on the $x$- and $y$-axes in Figure 0.1.15.

**Solution (b).** The given function $f$ is defined for all real $x$, except $x = 1$, so the natural domain of $f$ is
$$\{x : x \neq 1\} = (-\infty, 1) \cup (1, +\infty)$$
To determine the range it will be convenient to introduce a dependent variable
$$y = \frac{x + 1}{x - 1} \tag{4}$$
Although the set of possible $y$-values is not immediately evident from this equation, the graph of (4), which is shown in Figure 0.1.16, suggests that the range of $f$ consists of all $y$, except $y = 1$. To see that this is so, we solve (4) for $x$ in terms of $y$:
$$\begin{aligned}
(x - 1)y &= x + 1 \\
xy - y &= x + 1 \\
xy - x &= y + 1 \\
x(y - 1) &= y + 1 \\
x &= \frac{y + 1}{y - 1}
\end{aligned}$$
It is now evident from the right side of this equation that $y = 1$ is not in the range; otherwise we would have a division by zero. No other values of $y$ are excluded by this equation, so the range of the function $f$ is $\{y : y \neq 1\} = (-\infty, 1) \cup (1, +\infty)$, which agrees with the result obtained graphically.

---

### DOMAIN AND RANGE IN APPLIED PROBLEMS

In applications, physical considerations often impose restrictions on the domain and range of a function.

#### Example 9
An open box is to be made from a 16-inch by 30-inch piece of cardboard by cutting out squares of equal size from the four corners and bending up the sides (Figure 0.1.17a).
(a) Let $V$ be the volume of the box that results when the squares have sides of length $x$. Find a formula for $V$ as a function of $x$.  
(b) Find the domain of $V$.  
(c) Use the graph of $V$ given in Figure 0.1.17c to estimate the range of $V$.  
(d) Describe in words what the graph tells you about the volume.

**Solution (a).** As shown in Figure 0.1.17b, the resulting box has dimensions $16 - 2x$ by $30 - 2x$ by $x$, so the volume $V(x)$ is given by
$$V(x) = (16 - 2x)(30 - 2x)x = 480x - 92x^2 + 4x^3$$

**Solution (b).** The domain is the set of $x$-values and the range is the set of $V$-values. Because $x$ is a length, it must be nonnegative, and because we cannot cut out squares whose sides are more than 8 in long (why?), the $x$-values in the domain must satisfy
$$0 \le x \le 8$$

**Solution (c).** From the graph of $V$ versus $x$ in Figure 0.1.17c we estimate that the $V$-values in the range satisfy
$$0 \le V \le 725$$
Note that this is an approximation. Later we will show how to find the range exactly.

**Solution (d).** The graph tells us that the box of maximum volume occurs for a value of $x$ that is between 3 and 4 and that the maximum volume is approximately $725\text{ in}^3$. The graph also shows that the volume decreases toward zero as $x$ gets closer to 0 or 8, which should make sense to you intuitively.

---

In applications involving time, formulas for functions are often expressed in terms of a variable $t$ whose starting value is taken to be $t = 0$.

#### Example 10
At 8:05 A.M. a car is clocked at 100 ft/s by a radar detector that is positioned at the edge of a straight highway. Assuming that the car maintains a constant speed between 8:05 A.M. and 8:06 A.M., find a function $D(t)$ that expresses the distance traveled by the car during that time interval as a function of the time $t$.

**Solution.** It would be clumsy to use the actual clock time for the variable $t$, so let us agree to use the elapsed time in seconds, starting with $t = 0$ at 8:05 A.M. and ending with $t = 60$ at 8:06 A.M. At each instant, the distance traveled (in ft) is equal to the speed of the car (in ft/s) multiplied by the elapsed time (in s). Thus,
$$D(t) = 100t, \quad 0 \le t \le 60$$
The graph of $D$ versus $t$ is shown in Figure 0.1.18.

---

### ISSUES OF SCALE AND UNITS

In geometric problems where you want to preserve the "true" shape of a graph, you must use units of equal length on both axes. For example, if you graph a circle in a coordinate system in which 1 unit in the $y$-direction is smaller than 1 unit in the $x$-direction, then the circle will be squashed vertically into an elliptical shape (Figure 0.1.19).

> *Note:* In applications where the variables on the two axes have unrelated units (say, centimeters on the $y$-axis and seconds on the $x$-axis), then nothing is gained by requiring the units to have equal lengths; choose the lengths to make the graph as clear as possible.

However, sometimes it is inconvenient or impossible to display a graph using units of equal length. For example, consider the equation
$$y = x^2$$
If we want to show the portion of the graph over the interval $-3 \le x \le 3$, then there is no problem using units of equal length, since $y$ only varies from 0 to 9 over that interval. However, if we want to show the portion of the graph over the interval $-10 \le x \le 10$, then there is a problem keeping the units equal in length, since the value of $y$ varies between 0 and 100. In this case the only reasonable way to show all of the graph that occurs over the interval $-10 \le x \le 10$ is to compress the unit of length along the $y$-axis, as illustrated in Figure 0.1.20.

---

### QUICK CHECK EXERCISES 0.1
*(See page 15 for answers.)*

1. Let $f(x) = \sqrt{x + 1} + 4$.  
   (a) The natural domain of $f$ is $\underline{\hspace{2cm}}$.  
   (b) $f(3) = \underline{\hspace{2cm}}$.  
   (c) $f(t^2 - 1) = \underline{\hspace{2cm}}$.  
   (d) $f(x) = 7$ if $x = \underline{\hspace{2cm}}$.  
   (e) The range of $f$ is $\underline{\hspace{2cm}}$.  

2. Line segments in an $xy$-plane form "letters" as depicted: **LIMIT**  
   (a) If the $y$-axis is parallel to the letter I, which of the letters represent the graph of $y = f(x)$ for some function $f$?  
   (b) If the $y$-axis is perpendicular to the letter I, which of the letters represent the graph of $y = f(x)$ for some function $f$?  

3. The accompanying figure (Figure Ex-3) shows the complete graph of $y = f(x)$.  
   (a) The domain of $f$ is $\underline{\hspace{2cm}}$.  
   (b) The range of $f$ is $\underline{\hspace{2cm}}$.  
   (c) $f(-3) = \underline{\hspace{2cm}}$.  
   (d) $f(1/2) = \underline{\hspace{2cm}}$.  
   (e) The solutions to $f(x) = -\frac{3}{2}$ are $x = \underline{\hspace{2cm}}$ and $x = \underline{\hspace{2cm}}$.  

4. The accompanying table gives a 5-day forecast of high and low temperatures in degrees Fahrenheit ($^\circ\text{F}$).
   | Day | MON | TUE | WED | THURS | FRI |
   | :--- | :---: | :---: | :---: | :---: | :---: |
   | **HIGH** | 75 | 71 | 65 | 70 | 73 |
   | **LOW** | 52 | 56 | 48 | 50 | 52 |
   (a) Suppose that $x$ and $y$ denote the respective high and low temperature predictions for each of the 5 days. Is $y$ a function of $x$? If so, give the domain and range of this function.  
   (b) Suppose that $x$ and $y$ denote the respective low and high temperature predictions for each of the 5 days. Is $y$ a function of $x$? If so, give the domain and range of this function.  

5. Let $l$, $w$, and $A$ denote the length, width, and area of a rectangle, respectively, and suppose that the width of the rectangle is half the length.  
   (a) If $l$ is expressed as a function of $w$, then $l = \underline{\hspace{2cm}}$.  
   (b) If $A$ is expressed as a function of $l$, then $A = \underline{\hspace{2cm}}$.  
   (c) If $w$ is expressed as a function of $A$, then $w = \underline{\hspace{2cm}}$.  

---

### EXERCISE SET 0.1

1. Use the accompanying graph (Figure Ex-1) to answer the following questions, making reasonable approximations where needed.  
   (a) For what values of $x$ is $y = 1$?  
   (b) For what values of $x$ is $y = 3$?  
   (c) For what values of $y$ is $x = 3$?  
   (d) For what values of $x$ is $y \le 0$?  
   (e) What are the maximum and minimum values of $y$ and for what values of $x$ do they occur?  

2. Use the accompanying table to answer the questions posed in Exercise 1.
   | $x$ | -2 | -1 | 0 | 2 | 3 | 4 | 5 | 6 |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | $y$ | 5 | 1 | -2 | 7 | -1 | 1 | 0 | 9 |

3. In each part of the accompanying figure (Figure Ex-3), determine whether the graph defines $y$ as a function of $x$.

4. In each part, compare the natural domains of $f$ and $g$.  
   (a) $f(x) = \frac{x^2 + x}{x + 1}$; $g(x) = x$  
   (b) $f(x) = \frac{x\sqrt{x} + \sqrt{x}}{x + 1}$; $g(x) = \sqrt{x}$  

#### FOCUS ON CONCEPTS
5. The accompanying graph (Figure Ex-5) shows the median income in U.S. households (adjusted for inflation) between 1990 and 2005. Use the graph to answer the following questions, making reasonable approximations where needed.  
   (a) When was the median income at its maximum value, and what was the median income when that occurred?  
   (b) When was the median income at its minimum value, and what was the median income when that occurred?  
   (c) The median income was declining during the 2-year period between 2000 and 2002. Was it declining more rapidly during the first year or the second year of that period? Explain your reasoning.  

6. Use the median income graph in Exercise 5 to answer the following questions, making reasonable approximations where needed.  
   (a) What was the average yearly growth of median income between 1993 and 1999?  
   (b) The median income was increasing during the 6-year period between 1993 and 1999. Was it increasing more rapidly during the first 3 years or the last 3 years of that period? Explain your reasoning.  
   (c) Consider the statement: "After years of decline, median income this year was finally higher than that of last year." In what years would this statement have been correct?  

7. Find $f(0), f(2), f(-2), f(3), f(\sqrt{2})$, and $f(3t)$.  
   (a) $f(x) = 3x^2 - 2$  
   (b) $f(x) = \begin{cases} \frac{1}{x}, & x > 3 \\ 2x, & x \le 3 \end{cases}$  

8. Find $g(3), g(-1), g(\pi), g(-1.1)$, and $g(t^2 - 1)$.  
   (a) $g(x) = \frac{x + 1}{x - 1}$  
   (b) $g(x) = \begin{cases} \sqrt{x + 1}, & x \ge 1 \\ 3, & x < 1 \end{cases}$  

**9–10** Find the natural domain and determine the range of each function. If you have a graphing utility, use it to confirm that your result is consistent with the graph produced by your graphing utility. [*Note:* Set your graphing utility in radian mode when graphing trigonometric functions.]
9. (a) $f(x) = \frac{1}{x - 3}$  
   (b) $F(x) = \frac{x}{|x|}$  
   (c) $g(x) = \sqrt{x^2 - 3}$  
   (d) $G(x) = \sqrt{x^2 - 2x + 5}$  
   (e) $h(x) = \frac{1}{1 - \sin x}$  
   (f) $H(x) = \sqrt{\frac{x^2 - 4}{x - 2}}$  

10. (a) $f(x) = \sqrt{3 - x}$  
    (b) $F(x) = \sqrt{4 - x^2}$  
    (c) $g(x) = 3 + \sqrt{x}$  
    (d) $G(x) = x^3 + 2$  
    (e) $h(x) = 3\sin x$  
    (f) $H(x) = (\sin\sqrt{x})^{-2}$  

#### FOCUS ON CONCEPTS
11. (a) If you had a device that could record the Earth's population continuously, would you expect the graph of population versus time to be a continuous (unbroken) curve? Explain what might cause breaks in the curve.  
    (b) Suppose that a hospital patient receives an injection of an antibiotic every 8 hours and that between injections the concentration $C$ of the antibiotic in the bloodstream decreases as the antibiotic is absorbed by the tissues. What might the graph of $C$ versus the elapsed time $t$ look like?  

12. (a) If you had a device that could record the temperature of a room continuously over a 24-hour period, would you expect the graph of temperature versus time to be a continuous (unbroken) curve? Explain your reasoning.  
    (b) If you had a computer that could track the number of boxes of cereal on the shelf of a market continuously over a 1-week period, would you expect the graph of the number of boxes on the shelf versus time to be a continuous (unbroken) curve? Explain your reasoning.  

13. A boat is bobbing up and down on some gentle waves. Suddenly it gets hit by a large wave and sinks. Sketch a rough graph of the height of the boat above the ocean floor as a function of time.  

14. A cup of hot coffee sits on a table. You pour in some cool milk and let it sit for an hour. Sketch a rough graph of the temperature of the coffee as a function of time.  

**15–18** As seen in Example 3, the equation $x^2 + y^2 = 25$ does not define $y$ as a function of $x$. Each graph in these exercises is a portion of the circle $x^2 + y^2 = 25$. In each case, determine whether the graph defines $y$ as a function of $x$, and if so, give a formula for $y$ in terms of $x$.  
15. (Upper half circle from $x = -5$ to $x = 5$)  
16. (Right half circle from $y = -5$ to $y = 5$)  
17. (Top-left quadrant of circle from $x = -5$ to $x = 0$)  
18. (Bottom-right quadrant of circle from $x = 0$ to $x = 5$)  

**19–22 True–False** Determine whether the statement is true or false. Explain your answer.  
19. A curve that crosses the $x$-axis at two different points cannot be the graph of a function.  
20. The natural domain of a real-valued function defined by a formula consists of all those real numbers for which the formula yields a real value.  
21. The range of the absolute value function is all positive real numbers.  
22. If $g(x) = 1/\sqrt{f(x)}$, then the domain of $g$ consists of all those real numbers $x$ for which $f(x) \neq 0$.  

23. Use the equation $y = x^2 - 6x + 8$ to answer the following questions.  
    (a) For what values of $x$ is $y = 0$?  
    (b) For what values of $x$ is $y = -10$?  
    (c) For what values of $x$ is $y \ge 0$?  
    (d) Does $y$ have a minimum value? A maximum value? If so, find them.  

24. Use the equation $y = 1 + \sqrt{x}$ to answer the following questions.  
    (a) For what values of $x$ is $y = 4$?  
    (b) For what values of $x$ is $y = 0$?  
    (c) For what values of $x$ is $y \ge 6$?  
    (d) Does $y$ have a minimum value? A maximum value? If so, find them.  

25. As shown in the accompanying figure (Figure Ex-25), a pendulum of constant length $L$ makes an angle $\theta$ with its vertical position. Express the height $h$ as a function of the angle $\theta$.  

26. Express the length $L$ of a chord of a circle with radius 10 cm as a function of the central angle $\theta$ (see Figure Ex-26).  

**27–28** Express the function in piecewise form without using absolute values. [*Suggestion:* It may help to generate the graph of the function.]  
27. (a) $f(x) = |x| + 3x + 1$  
    (b) $g(x) = |x| + |x - 1|$  
28. (a) $f(x) = 3 + |2x - 5|$  
    (b) $g(x) = 3|x - 2| - |x + 1|$  

29. As shown in Figure Ex-29, an open box is to be constructed from a rectangular sheet of metal, 8 in by 15 in, by cutting out squares with sides of length $x$ from each corner and bending up the sides.  
    (a) Express the volume $V$ as a function of $x$.  
    (b) Find the domain of $V$.  
    (c) Plot the graph of the function $V$ obtained in part (a) and estimate the range of this function.  
    (d) In words, describe how the volume $V$ varies with $x$, and discuss how one might construct boxes of maximum volume.  

30. Repeat Exercise 29 assuming the box is constructed in the same fashion from a 6-inch-square sheet of metal.  

31. A construction company has adjoined a $1000\text{ ft}^2$ rectangular enclosure to its office building. Three sides of the enclosure are fenced in. The side of the building adjacent to the enclosure is 100 ft long and a portion of this side is used as the fourth side of the enclosure. Let $x$ and $y$ be the dimensions of the enclosure, where $x$ is measured parallel to the building, and let $L$ be the length of fencing required for those dimensions.  
    (a) Find a formula for $L$ in terms of $x$ and $y$.  
    (b) Find a formula that expresses $L$ as a function of $x$ alone.  
    (c) What is the domain of the function in part (b)?  
    (d) Plot the function in part (b) and estimate the dimensions of the enclosure that minimize the amount of fencing required.  

32. As shown in Figure Ex-32, a camera is mounted at a point 3000 ft from the base of a rocket launching pad. The rocket rises vertically when launched, and the camera's elevation angle is continually adjusted to follow the bottom of the rocket.  
    (a) Express the height $x$ as a function of the elevation angle $\theta$.  
    (b) Find the domain of the function in part (a).  
    (c) Plot the graph of the function in part (a) and use it to estimate the height of the rocket when the elevation angle is $\pi/4 \approx 0.7854\text{ radian}$. Compare this estimate to the exact height.  

33. A soup company wants to manufacture a can in the shape of a right circular cylinder that will hold $500\text{ cm}^3$ of liquid. The material for the top and bottom costs $0.02\text{ cent/cm}^2$, and the material for the sides costs $0.01\text{ cent/cm}^2$.  
    (a) Estimate the radius $r$ and the height $h$ of the can that costs the least to manufacture. [*Suggestion:* Express the cost $C$ in terms of $r$.]  
    (b) Suppose that the tops and bottoms of radius $r$ are punched out from square sheets with sides of length $2r$ and the scraps are waste. If you allow for the cost of the waste, would you expect the can of least cost to be taller or shorter than the one in part (a)? Explain.  
    (c) Estimate the radius, height, and cost of the can in part (b), and determine whether your conjecture was correct.  

34. The designer of a sports facility wants to put a quarter-mile (1320 ft) running track around a football field, oriented as in Figure Ex-34. The football field is 360 ft long (including the end zones) and 160 ft wide. The track consists of two straightaways and two semicircles, with the straightaways extending at least the length of the football field.  
    (a) Show that it is possible to construct a quarter-mile track around the football field. [*Suggestion:* Find the shortest track that can be constructed around the field.]  
    (b) Let $L$ be the length of a straightaway (in feet), and let $x$ be the distance (in feet) between a sideline of the football field and a straightaway. Make a graph of $L$ versus $x$.  
    (c) Use the graph to estimate the value of $x$ that produces the shortest straightaways, and then find this value of $x$ exactly.  
    (d) Use the graph to estimate the length of the longest possible straightaways, and then find that length exactly.  

**35–36** (i) Explain why the function $f$ has one or more holes in its graph, and state the $x$-values at which those holes occur. (ii) Find a function $g$ whose graph is identical to that of $f$, but without the holes.  
35. $f(x) = \frac{(x + 2)(x^2 - 1)}{(x + 2)(x - 1)}$  
36. $f(x) = \frac{x^2 + |x|}{|x|}$  

37. In 2001 the National Weather Service introduced a new wind chill temperature (WCT) index. For a given outside temperature $T$ and wind speed $v$, the wind chill temperature index is the equivalent temperature that exposed skin would feel with a wind speed of $v\text{ mi/h}$. Based on a more accurate model of cooling due to wind, the new formula is
    $$\text{WCT} = \begin{cases} T, & 0 \le v \le 3 \\ 35.74 + 0.6215T - 35.75v^{0.16} + 0.4275Tv^{0.16}, & 3 < v \end{cases}$$
    where $T$ is the temperature in $^\circ\text{F}$, $v$ is the wind speed in mi/h, and $\text{WCT}$ is the equivalent temperature in $^\circ\text{F}$. Find the $\text{WCT}$ to the nearest degree if $T = 25^\circ\text{F}$ and  
    (a) $v = 3\text{ mi/h}$  
    (b) $v = 15\text{ mi/h}$  
    (c) $v = 46\text{ mi/h}$.  
    *Source:* Adapted from UMAP Module 658, *Windchill*, W. Bosch and L. Cobb, COMAP, Arlington, MA.  

**38–40** Use the formula for the wind chill temperature index described in Exercise 37.  
38. Find the air temperature to the nearest degree if the $\text{WCT}$ is reported as $-60^\circ\text{F}$ with a wind speed of $48\text{ mi/h}$.  
39. Find the air temperature to the nearest degree if the $\text{WCT}$ is reported as $-10^\circ\text{F}$ with a wind speed of $48\text{ mi/h}$.  
40. Find the wind speed to the nearest mile per hour if the $\text{WCT}$ is reported as $5^\circ\text{F}$ with an air temperature of $20^\circ\text{F}$.  

#### QUICK CHECK ANSWERS 0.1
1. (a) $[-1, +\infty)$ (b) 6 (c) $|t| + 4$ (d) 8 (e) $[4, +\infty)$  
2. (a) M (b) I  
3. (a) $[-3, 3)$ (b) $[-2, 2]$ (c) $-1$ (d) 1 (e) $-\frac{3}{4}; -\frac{3}{2}$  
4. (a) yes; domain: $\{65, 70, 71, 73, 75\}$; range: $\{48, 50, 52, 56\}$ (b) no  
5. (a) $l = 2w$ (b) $A = l^2/2$ (c) $w = \sqrt{A/2}$  

---

## 0.2 NEW FUNCTIONS FROM OLD

Just as numbers can be added, subtracted, multiplied, and divided to produce other numbers, so functions can be added, subtracted, multiplied, and divided to produce other functions. In this section we will discuss these operations and some others that have no analogs in ordinary arithmetic.

### ARITHMETIC OPERATIONS ON FUNCTIONS

Two functions, $f$ and $g$, can be added, subtracted, multiplied, and divided in a natural way to form new functions $f + g$, $f - g$, $fg$, and $f / g$. For example, $f + g$ is defined by the formula
$$(f + g)(x) = f(x) + g(x) \tag{1}$$
which states that for each input the value of $f + g$ is obtained by adding the values of $f$ and $g$. Equation (1) provides a formula for $f + g$ but does not say anything about the domain of $f + g$. However, for the right side of this equation to be defined, $x$ must lie in the domains of both $f$ and $g$, so we define the domain of $f + g$ to be the intersection of these two domains. More generally, we make the following definition.

> **0.2.1 DEFINITION**  
> Given functions $f$ and $g$, we define
> $$\begin{aligned}
> (f + g)(x) &= f(x) + g(x) \\
> (f - g)(x) &= f(x) - g(x) \\
> (fg)(x) &= f(x)g(x) \\
> (f/g)(x) &= f(x)/g(x)
> \end{aligned}$$
> For the functions $f + g$, $f - g$, and $fg$ we define the domain to be the intersection of the domains of $f$ and $g$, and for the function $f/g$ we define the domain to be the intersection of the domains of $f$ and $g$ but with the points where $g(x) = 0$ excluded (to avoid division by zero).

> *Note:* If $f$ is a constant function, that is, $f(x) = c$ for all $x$, then the product of $f$ and $g$ is $cg$, so multiplying a function by a constant is a special case of multiplying two functions.

#### Example 1
Let
$$f(x) = 1 + \sqrt{x - 2} \quad \text{and} \quad g(x) = x - 3$$
Find the domains and formulas for the functions $f + g$, $f - g$, $fg$, $f/g$, and $7f$.

**Solution.** First, we will find the formulas and then the domains. The formulas are
$$\begin{aligned}
(f + g)(x) &= f(x) + g(x) = (1 + \sqrt{x - 2}) + (x - 3) = x - 2 + \sqrt{x - 2} \tag{2} \\
(f - g)(x) &= f(x) - g(x) = (1 + \sqrt{x - 2}) - (x - 3) = 4 - x + \sqrt{x - 2} \tag{3} \\
(fg)(x) &= f(x)g(x) = (1 + \sqrt{x - 2})(x - 3) \tag{4} \\
(f/g)(x) &= f(x)/g(x) = \frac{1 + \sqrt{x - 2}}{x - 3} \tag{5} \\
(7f)(x) &= 7f(x) = 7 + 7\sqrt{x - 2} \tag{6}
\end{aligned}$$

The domains of $f$ and $g$ are $[2, +\infty)$ and $(-\infty, +\infty)$, respectively (their natural domains). Thus, it follows from Definition 0.2.1 that the domains of $f + g$, $f - g$, and $fg$ are the intersection of these two domains, namely,
$$[2, +\infty) \cap (-\infty, +\infty) = [2, +\infty) \tag{7}$$
Moreover, since $g(x) = 0$ if $x = 3$, the domain of $f/g$ is (7) with $x = 3$ removed, namely,
$$[2, 3) \cup (3, +\infty)$$
Finally, the domain of $7f$ is the same as the domain of $f$.

---

We saw in the last example that the domains of the functions $f + g$, $f - g$, $fg$, and $f/g$ were the natural domains resulting from the formulas obtained for these functions. The following example shows that this will not always be the case.

#### Example 2
Show that if $f(x) = \sqrt{x}$, $g(x) = \sqrt{x}$, and $h(x) = x$, then the domain of $fg$ is not the same as the natural domain of $h$.

**Solution.** The natural domain of $h(x) = x$ is $(-\infty, +\infty)$. Note that
$$(fg)(x) = \sqrt{x}\sqrt{x} = x = h(x)$$
on the domain of $fg$. The domains of both $f$ and $g$ are $[0, +\infty)$, so the domain of $fg$ is
$$[0, +\infty) \cap [0, +\infty) = [0, +\infty)$$
by Definition 0.2.1. Since the domains of $fg$ and $h$ are different, it would be misleading to write $(fg)(x) = x$ without including the restriction that this formula holds only for $x \ge 0$.

---

### COMPOSITION OF FUNCTIONS

We now consider an operation on functions, called **composition**, which has no direct analog in ordinary arithmetic. Informally stated, the operation of composition is performed by substituting some function for the independent variable of another function. For example, suppose that
$$f(x) = x^2 \quad \text{and} \quad g(x) = x + 1$$
If we substitute $g(x)$ for $x$ in the formula for $f$, we obtain a new function
$$f(g(x)) = (g(x))^2 = (x + 1)^2$$
which we denote by $f \circ g$. Thus,
$$(f \circ g)(x) = f(g(x)) = (g(x))^2 = (x + 1)^2$$

In general, we make the following definition.

> **0.2.2 DEFINITION**  
> Given functions $f$ and $g$, the **composition of $f$ with $g$**, denoted by $f \circ g$, is the function defined by
> $$(f \circ g)(x) = f(g(x))$$
> The domain of $f \circ g$ is defined to consist of all $x$ in the domain of $g$ for which $g(x)$ is in the domain of $f$.

> *Note:* Although the domain of $f \circ g$ may seem complicated at first glance, it makes sense intuitively: To compute $f(g(x))$ one needs $x$ in the domain of $g$ to compute $g(x)$, and one needs $g(x)$ in the domain of $f$ to compute $f(g(x))$.

#### Example 3
Let $f(x) = x^2 + 3$ and $g(x) = \sqrt{x}$. Find  
(a) $(f \circ g)(x)$  
(b) $(g \circ f)(x)$

**Solution (a).** The formula for $f(g(x))$ is
$$f(g(x)) = [g(x)]^2 + 3 = (\sqrt{x})^2 + 3 = x + 3$$
Since the domain of $g$ is $[0, +\infty)$ and the domain of $f$ is $(-\infty, +\infty)$, the domain of $f \circ g$ consists of all $x$ in $[0, +\infty)$ such that $g(x) = \sqrt{x}$ lies in $(-\infty, +\infty)$; thus, the domain of $f \circ g$ is $[0, +\infty)$. Therefore,
$$(f \circ g)(x) = x + 3, \quad x \ge 0$$

**Solution (b).** The formula for $g(f(x))$ is
$$g(f(x)) = \sqrt{f(x)} = \sqrt{x^2 + 3}$$
Since the domain of $f$ is $(-\infty, +\infty)$ and the domain of $g$ is $[0, +\infty)$, the domain of $g \circ f$ consists of all $x$ in $(-\infty, +\infty)$ such that $f(x) = x^2 + 3$ lies in $[0, +\infty)$. Thus, the domain of $g \circ f$ is $(-\infty, +\infty)$. Therefore,
$$(g \circ f)(x) = \sqrt{x^2 + 3}$$
There is no need to indicate that the domain is $(-\infty, +\infty)$, since this is the natural domain of $\sqrt{x^2 + 3}$.

> *Note:* Note that the functions $f \circ g$ and $g \circ f$ in Example 3 are not the same. Thus, the order in which functions are composed can (and usually will) make a difference in the end result.

---

Compositions can also be defined for three or more functions; for example, $(f \circ g \circ h)(x)$ is computed as
$$(f \circ g \circ h)(x) = f(g(h(x)))$$
In other words, first find $h(x)$, then find $g(h(x))$, and then find $f(g(h(x)))$.

#### Example 4
Find $(f \circ g \circ h)(x)$ if
$$f(x) = \sqrt{x}, \quad g(x) = 1/x, \quad h(x) = x^3$$

**Solution.**
$$(f \circ g \circ h)(x) = f(g(h(x))) = f(g(x^3)) = f(1/x^3) = \sqrt{1/x^3} = 1/x^{3/2}$$

---

### EXPRESSING A FUNCTION AS A COMPOSITION

Many problems in mathematics are solved by "decomposing" functions into compositions of simpler functions. For example, consider the function $h$ given by
$$h(x) = (x + 1)^2$$
To evaluate $h(x)$ for a given value of $x$, we would first compute $x + 1$ and then square the result. These two operations are performed by the functions
$$g(x) = x + 1 \quad \text{and} \quad f(x) = x^2$$
We can express $h$ in terms of $f$ and $g$ by writing
$$h(x) = (x + 1)^2 = [g(x)]^2 = f(g(x))$$
so we have succeeded in expressing $h$ as the composition $h = f \circ g$.

The thought process in this example suggests a general procedure for decomposing a function $h$ into a composition $h = f \circ g$:
* Think about how you would evaluate $h(x)$ for a specific value of $x$, trying to break the evaluation into two steps performed in succession.
* The first operation in the evaluation will determine a function $g$ and the second a function $f$.
* The formula for $h$ can then be written as $h(x) = f(g(x))$.

For descriptive purposes, we will refer to $g$ as the **"inside function"** and $f$ as the **"outside function"** in the expression $f(g(x))$. The inside function performs the first operation and the outside function performs the second.

#### Example 5
Express $\sin(x^3)$ as a composition of two functions.

**Solution.** To evaluate $\sin(x^3)$, we would first compute $x^3$ and then take the sine, so $g(x) = x^3$ is the inside function and $f(x) = \sin x$ the outside function. Therefore,
$$\sin(x^3) = f(g(x)) \quad [g(x) = x^3 \text{ and } f(x) = \sin x]$$

#### Table 0.2.1: Composing Functions
| Function | $g(x)$ Inside | $f(x)$ Outside | Composition |
| :---: | :---: | :---: | :---: |
| $(x^2 + 1)^{10}$ | $x^2 + 1$ | $x^{10}$ | $(x^2 + 1)^{10} = f(g(x))$ |
| $\sin^3 x$ | $\sin x$ | $x^3$ | $\sin^3 x = f(g(x))$ |
| $\tan(x^5)$ | $x^5$ | $\tan x$ | $\tan(x^5) = f(g(x))$ |
| $\sqrt{4 - 3x}$ | $4 - 3x$ | $\sqrt{x}$ | $\sqrt{4 - 3x} = f(g(x))$ |
| $8 + \sqrt{x}$ | $\sqrt{x}$ | $8 + x$ | $8 + \sqrt{x} = f(g(x))$ |
| $\frac{1}{x + 1}$ | $x + 1$ | $\frac{1}{x}$ | $\frac{1}{x + 1} = f(g(x))$ |

> **REMARK**  
> There is always more than one way to express a function as a composition. For example, here are two ways to express $(x^2 + 1)^{10}$ as a composition that differ from that in Table 0.2.1:
> * $(x^2 + 1)^{10} = [(x^2 + 1)^2]^5 = f(g(x)) \quad [g(x) = (x^2 + 1)^2 \text{ and } f(x) = x^5]$
> * $(x^2 + 1)^{10} = [(x^2 + 1)^3]^{10/3} = f(g(x)) \quad [g(x) = (x^2 + 1)^3 \text{ and } f(x) = x^{10/3}]$

---

### NEW FUNCTIONS FROM OLD (GEOMETRIC TRANSFORMATIONS)

The remainder of this section will be devoted to considering the geometric effect of performing basic operations on functions. This will enable us to use known graphs of functions to visualize or sketch graphs of related functions. For example, Figure 0.2.1 shows the graphs of yearly new car sales $N(t)$ and used car sales $U(t)$ over a certain time period. Those graphs can be used to construct the graph of the total car sales
$$T(t) = N(t) + U(t)$$
by adding the values of $N(t)$ and $U(t)$ for each value of $t$. In general, the graph of $y = f(x) + g(x)$ can be constructed from the graphs of $y = f(x)$ and $y = g(x)$ by adding corresponding $y$-values for each $x$.

#### Example 6
Referring to Figure 0.1.4 for the graphs of $y = \sqrt{x}$ and $y = 1/x$, make a sketch that shows the general shape of the graph of $y = \sqrt{x} + 1/x$ for $x \ge 0$.

**Solution.** To add the corresponding $y$-values of $y = \sqrt{x}$ and $y = 1/x$ graphically, just imagine them to be "stacked" on top of one another. This yields the sketch in Figure 0.2.2.

---

### TRANSLATIONS

Table 0.2.2 illustrates the geometric effect on the graph of $y = f(x)$ of adding or subtracting a positive constant $c$ to $f$ or to its independent variable $x$. For example, the first result in the table illustrates that adding a positive constant $c$ to a function $f$ adds $c$ to each $y$-coordinate of its graph, thereby shifting the graph of $f$ up by $c$ units. Similarly, subtracting $c$ from $f$ shifts the graph down by $c$ units. On the other hand, if a positive constant $c$ is added to $x$, then the value of $y = f(x + c)$ at $x - c$ is $f(x)$; and since the point $x - c$ is $c$ units to the left of $x$ on the $x$-axis, the graph of $y = f(x + c)$ must be the graph of $y = f(x)$ shifted left by $c$ units. Similarly, subtracting $c$ from $x$ shifts the graph of $y = f(x)$ right by $c$ units.

#### Table 0.2.2: Translation Principles
| Operation on $y = f(x)$ | New Equation | Geometric Effect | Example |
| :--- | :--- | :--- | :--- |
| Add a positive constant $c$ to $f(x)$ | $y = f(x) + c$ | Translates the graph of $y = f(x)$ up $c$ units | $y = x^2 + 2$ (shifts $y = x^2$ up 2) |
| Subtract a positive constant $c$ from $f(x)$ | $y = f(x) - c$ | Translates the graph of $y = f(x)$ down $c$ units | $y = x^2 - 2$ (shifts $y = x^2$ down 2) |
| Add a positive constant $c$ to $x$ | $y = f(x + c)$ | Translates the graph of $y = f(x)$ left $c$ units | $y = (x + 2)^2$ (shifts $y = x^2$ left 2) |
| Subtract a positive constant $c$ from $x$ | $y = f(x - c)$ | Translates the graph of $y = f(x)$ right $c$ units | $y = (x - 2)^2$ (shifts $y = x^2$ right 2) |

#### Example 7
Sketch the graph of
(a) $y = \sqrt{x - 3}$  
(b) $y = \sqrt{x + 3}$

**Solution.** Using the translation principles given in Table 0.2.2, the graph of the equation $y = \sqrt{x - 3}$ can be obtained by translating the graph of $y = \sqrt{x}$ right 3 units. The graph of $y = \sqrt{x + 3}$ can be obtained by translating the graph of $y = \sqrt{x}$ left 3 units (Figure 0.2.3).

#### Example 8
Sketch the graph of $y = x^2 - 4x + 5$.

**Solution.** Completing the square on the first two terms yields
$$y = (x^2 - 4x + 4) - 4 + 5 = (x - 2)^2 + 1$$
(see Web Appendix H for a review of this technique). In this form we see that the graph can be obtained by translating the graph of $y = x^2$ right 2 units because of the $x - 2$, and up 1 unit because of the $+1$ (Figure 0.2.4).

---

### REFLECTIONS

The graph of $y = f(-x)$ is the reflection of the graph of $y = f(x)$ about the $y$-axis because the point $(x, y)$ on the graph of $f(x)$ is replaced by $(-x, y)$. Similarly, the graph of $y = -f(x)$ is the reflection of the graph of $y = f(x)$ about the $x$-axis because the point $(x, y)$ on the graph of $f(x)$ is replaced by $(x, -y)$ [the equation $y = -f(x)$ is equivalent to $-y = f(x)$]. This is summarized in Table 0.2.3.

#### Table 0.2.3: Reflection Principles
| Operation on $y = f(x)$ | New Equation | Geometric Effect | Example |
| :--- | :--- | :--- | :--- |
| Replace $x$ by $-x$ | $y = f(-x)$ | Reflects the graph of $y = f(x)$ about the $y$-axis | $y = \sqrt{-x}$ reflects $y = \sqrt{x}$ across $y$-axis |
| Multiply $f(x)$ by $-1$ | $y = -f(x)$ | Reflects the graph of $y = f(x)$ about the $x$-axis | $y = -\sqrt{x}$ reflects $y = \sqrt{x}$ across $x$-axis |

#### Example 9
Sketch the graph of $y = \sqrt[3]{2 - x}$.

**Solution.** Using the translation and reflection principles in Tables 0.2.2 and 0.2.3, we can obtain the graph by a reflection followed by a translation as follows: First reflect the graph of $y = \sqrt[3]{x}$ about the $y$-axis to obtain the graph of $y = \sqrt[3]{-x}$, then translate this graph right 2 units to obtain the graph of the equation $y = \sqrt[3]{-(x - 2)} = \sqrt[3]{2 - x}$ (Figure 0.2.5).

#### Example 10
Sketch the graph of $y = 4 - |x - 2|$.

**Solution.** The graph can be obtained by a reflection and two translations: First translate the graph of $y = |x|$ right 2 units to obtain the graph of $y = |x - 2|$; then reflect this graph about the $x$-axis to obtain the graph of $y = -|x - 2|$; and then translate this graph up 4 units to obtain the graph of the equation $y = -|x - 2| + 4 = 4 - |x - 2|$ (Figure 0.2.6).

---

### STRETCHES AND COMPRESSIONS

Multiplying $f(x)$ by a positive constant $c$ has the geometric effect of stretching the graph of $y = f(x)$ in the $y$-direction by a factor of $c$ if $c > 1$ and compressing it in the $y$-direction by a factor of $1/c$ if $0 < c < 1$. For example, multiplying $f(x)$ by 2 doubles each $y$-coordinate, thereby stretching the graph vertically by a factor of 2, and multiplying by $\frac{1}{2}$ cuts each $y$-coordinate in half, thereby compressing the graph vertically by a factor of 2.

Similarly, multiplying $x$ by a positive constant $c$ has the geometric effect of compressing the graph of $y = f(x)$ by a factor of $c$ in the $x$-direction if $c > 1$ and stretching it by a factor of $1/c$ if $0 < c < 1$. [If this seems backwards to you, then think of it this way: The value of $2x$ changes twice as fast as $x$, so a point moving along the $x$-axis from the origin will only have to move half as far for $y = f(2x)$ to have the same value as $y = f(x)$, thereby creating a horizontal compression of the graph.] All of this is summarized in Table 0.2.4.

#### Table 0.2.4: Stretching and Compressing Principles
| Operation on $y = f(x)$ | New Equation | Geometric Effect | Example |
| :--- | :--- | :--- | :--- |
| Multiply $f(x)$ by $c$ ($c > 1$) | $y = cf(x)$ | Stretches the graph of $y = f(x)$ vertically by a factor of $c$ | $y = 2\cos x$ (amplitude is 2) |
| Multiply $f(x)$ by $c$ ($0 < c < 1$) | $y = cf(x)$ | Compresses the graph of $y = f(x)$ vertically by a factor of $1/c$ | $y = \frac{1}{2}\cos x$ (amplitude is $\frac{1}{2}$) |
| Multiply $x$ by $c$ ($c > 1$) | $y = f(cx)$ | Compresses the graph of $y = f(x)$ horizontally by a factor of $c$ | $y = \cos 2x$ (period compressed to $\pi$) |
| Multiply $x$ by $c$ ($0 < c < 1$) | $y = f(cx)$ | Stretches the graph of $y = f(x)$ horizontally by a factor of $1/c$ | $y = \cos \frac{1}{2}x$ (period stretched to $4\pi$) |

---

### SYMMETRY

Figure 0.2.7 illustrates three types of symmetries: **symmetry about the $x$-axis**, **symmetry about the $y$-axis**, and **symmetry about the origin**. As illustrated in the figure, a curve is symmetric about the $x$-axis if for each point $(x, y)$ on the graph the point $(x, -y)$ is also on the graph, and it is symmetric about the $y$-axis if for each point $(x, y)$ on the graph the point $(-x, y)$ is also on the graph. A curve is symmetric about the origin if for each point $(x, y)$ on the graph, the point $(-x, -y)$ is also on the graph. (Equivalently, a graph is symmetric about the origin if rotating the graph $180^\circ$ about the origin leaves it unchanged.) This suggests the following symmetry tests.

> **0.2.3 THEOREM (Symmetry Tests)**  
> (a) A plane curve is symmetric about the $y$-axis if and only if replacing $x$ by $-x$ in its equation produces an equivalent equation.  
> (b) A plane curve is symmetric about the $x$-axis if and only if replacing $y$ by $-y$ in its equation produces an equivalent equation.  
> (c) A plane curve is symmetric about the origin if and only if replacing both $x$ by $-x$ and $y$ by $-y$ in its equation produces an equivalent equation.

#### Example 11
Use Theorem 0.2.3 to identify symmetries in the graph of $x = y^2$.

**Solution.** Replacing $y$ by $-y$ yields $x = (-y)^2$, which simplifies to the original equation $x = y^2$. Thus, the graph is symmetric about the $x$-axis. The graph is not symmetric about the $y$-axis because replacing $x$ by $-x$ yields $-x = y^2$, which is not equivalent to the original equation $x = y^2$. Similarly, the graph is not symmetric about the origin because replacing $x$ by $-x$ and $y$ by $-y$ yields $-x = (-y)^2$, which simplifies to $-x = y^2$, and this is again not equivalent to the original equation. These results are consistent with the graph of $x = y^2$ shown in Figure 0.2.8.

---

### EVEN AND ODD FUNCTIONS

A function $f$ is said to be an **even function** if
$$f(-x) = f(x) \tag{8}$$
and is said to be an **odd function** if
$$f(-x) = -f(x) \tag{9}$$

Geometrically, the graphs of even functions are symmetric about the $y$-axis because replacing $x$ by $-x$ in the equation $y = f(x)$ yields $y = f(-x)$, which is equivalent to the original equation $y = f(x)$ by (8) (see Figure 0.2.9). Similarly, it follows from (9) that graphs of odd functions are symmetric about the origin (see Figure 0.2.10). Some examples of even functions are $x^2, x^4, x^6$, and $\cos x$; and some examples of odd functions are $x^3, x^5, x^7$, and $\sin x$.

---

### QUICK CHECK EXERCISES 0.2
*(See page 27 for answers.)*

1. Let $f(x) = 3\sqrt{x} - 2$ and $g(x) = |x|$. In each part, give the formula for the function and state the corresponding domain.  
   (a) $f + g$: $\underline{\hspace{2cm}}$ Domain: $\underline{\hspace{2cm}}$  
   (b) $f - g$: $\underline{\hspace{2cm}}$ Domain: $\underline{\hspace{2cm}}$  
   (c) $fg$: $\underline{\hspace{2cm}}$ Domain: $\underline{\hspace{2cm}}$  
   (d) $f/g$: $\underline{\hspace{2cm}}$ Domain: $\underline{\hspace{2cm}}$  

2. Let $f(x) = 2 - x^2$ and $g(x) = \sqrt{x}$. In each part, give the formula for the composition and state the corresponding domain.  
   (a) $f \circ g$: $\underline{\hspace{2cm}}$ Domain: $\underline{\hspace{2cm}}$  
   (b) $g \circ f$: $\underline{\hspace{2cm}}$ Domain: $\underline{\hspace{2cm}}$  

3. The graph of $y = 1 + (x - 2)^2$ may be obtained by shifting the graph of $y = x^2$ (left/right) by $\underline{\hspace{1cm}}$ unit(s) and then shifting this new graph (up/down) by $\underline{\hspace{1cm}}$ unit(s).  

4. Let
   $$f(x) = \begin{cases} |x + 1|, & -2 \le x \le 0 \\ |x - 1|, & 0 < x \le 2 \end{cases}$$
   (a) The letter of the alphabet that most resembles the graph of $f$ is $\underline{\hspace{1cm}}$.  
   (b) Is $f$ an even function?  

---

### EXERCISE SET 0.2

#### FOCUS ON CONCEPTS
1. The graph of a function $f$ is shown in Figure Ex-1. Sketch the graphs of the following equations.  
   (a) $y = f(x) - 1$  
   (b) $y = f(x - 1)$  
   (c) $y = \frac{1}{2}f(x)$  
   (d) $y = f\left(-\frac{1}{2}x\right)$  

2. Use the graph in Exercise 1 to sketch the graphs of the following equations.  
   (a) $y = -f(-x)$  
   (b) $y = f(2 - x)$  
   (c) $y = 1 - f(2 - x)$  
   (d) $y = \frac{1}{2}f(2x)$  

3. The graph of a function $f$ is shown in Figure Ex-3. Sketch the graphs of the following equations.  
   (a) $y = f(x + 1)$  
   (b) $y = f(2x)$  
   (c) $y = |f(x)|$  
   (d) $y = 1 - |f(x)|$  

4. Use the graph in Exercise 3 to sketch the graph of the equation $y = f(|x|)$.  

**5–24** Sketch the graph of the equation by translating, reflecting, compressing, and stretching the graph of $y = x^2$, $y = \sqrt{x}$, $y = 1/x$, $y = |x|$, or $y = \sqrt[3]{x}$ appropriately. Then use a graphing utility to confirm that your sketch is correct.  
5. $y = -2(x + 1)^2 - 3$  
6. $y = \frac{1}{2}(x - 3)^2 + 2$  
7. $y = x^2 + 6x$  
8. $y = \frac{1}{2}(x^2 - 2x + 3)$  
9. $y = 3 - \sqrt{x + 1}$  
10. $y = 1 + \sqrt{x - 4}$  
11. $y = \frac{1}{2}\sqrt{x} + 1$  
12. $y = -\sqrt{3x}$  
13. $y = \frac{1}{x - 3}$  
14. $y = \frac{1}{1 - x}$  
15. $y = 2 - \frac{1}{x + 1}$  
16. $y = \frac{x - 1}{x}$  
17. $y = |x + 2| - 2$  
18. $y = 1 - |x - 3|$  
19. $y = |2x - 1| + 1$  
20. $y = \sqrt{x^2 - 4x + 4}$  
21. $y = 1 - 2\sqrt[3]{x}$  
22. $y = \sqrt[3]{x - 2} - 3$  
23. $y = 2 + \sqrt[3]{x + 1}$  
24. $y + \sqrt[3]{x - 2} = 0$  

25. (a) Sketch the graph of $y = x + |x|$ by adding the corresponding $y$-coordinates on the graphs of $y = x$ and $y = |x|$.  
    (b) Express the equation $y = x + |x|$ in piecewise form with no absolute values, and confirm that the graph you obtained in part (a) is consistent with this equation.  

26. Sketch the graph of $y = x + (1/x)$ by adding corresponding $y$-coordinates on the graphs of $y = x$ and $y = 1/x$. Use a graphing utility to confirm that your sketch is correct.  

**27–28** Find formulas for $f + g$, $f - g$, $fg$, and $f/g$, and state the domains of the functions.  
27. $f(x) = 2\sqrt{x - 1}, \quad g(x) = \sqrt{x - 1}$  
28. $f(x) = \frac{x}{1 + x^2}, \quad g(x) = \frac{1}{x}$  

29. Let $f(x) = \sqrt{x}$ and $g(x) = x^3 + 1$. Find  
    (a) $f(g(2))$  
    (b) $g(f(4))$  
    (c) $f(f(16))$  
    (d) $g(g(0))$  
    (e) $f(2 + h)$  
    (f) $g(3 + h)$  

30. Let $g(x) = \sqrt{x}$. Find  
    (a) $g(5s + 2)$  
    (b) $g(\sqrt{x} + 2)$  
    (c) $3g(5x)$  
    (d) $\frac{1}{g(x)}$  
    (e) $g(g(x))$  
    (f) $(g(x))^2 - g(x^2)$  
    (g) $g(1/\sqrt{x})$  
    (h) $g((x - 1)^2)$  
    (i) $g(x + h)$  

**31–34** Find formulas for $f \circ g$ and $g \circ f$, and state the domains of the compositions.  
31. $f(x) = x^2, \quad g(x) = \sqrt{1 - x}$  
32. $f(x) = \sqrt{x - 3}, \quad g(x) = \sqrt{x^2 + 3}$  
33. $f(x) = \frac{1 + x}{1 - x}, \quad g(x) = \frac{x}{1 - x}$  
34. $f(x) = \frac{x}{1 + x^2}, \quad g(x) = \frac{1}{x}$  

**35–36** Find a formula for $f \circ g \circ h$.  
35. $f(x) = x^2 + 1, \quad g(x) = \frac{1}{x}, \quad h(x) = x^3$  
36. $f(x) = \frac{1}{1 + x}, \quad g(x) = \sqrt[3]{x}, \quad h(x) = \frac{1}{x^3}$  

**37–42** Express $f$ as a composition of two functions; that is, find $g$ and $h$ such that $f = g \circ h$. [*Note:* Each exercise has more than one solution.]  
37. (a) $f(x) = \sqrt{x + 2}$  
    (b) $f(x) = |x^2 - 3x + 5|$  
38. (a) $f(x) = x^2 + 1$  
    (b) $f(x) = \frac{1}{x - 3}$  
39. (a) $f(x) = \sin^2 x$  
    (b) $f(x) = \frac{3}{5 + \cos x}$  
40. (a) $f(x) = 3\sin(x^2)$  
    (b) $f(x) = 3\sin^2 x + 4\sin x$  
41. (a) $f(x) = (1 + \sin(x^2))^3$  
    (b) $f(x) = \sqrt{1 - \sqrt[3]{x}}$  
42. (a) $f(x) = \frac{1}{1 - x^2}$  
    (b) $f(x) = |5 + 2x|$  

**43–46 True–False** Determine whether the statement is true or false. Explain your answer.  
43. The domain of $f + g$ is the intersection of the domains of $f$ and $g$.  
44. The domain of $f \circ g$ consists of all values of $x$ in the domain of $g$ for which $g(x) \neq 0$.  
45. The graph of an even function is symmetric about the $y$-axis.  
46. The graph of $y = f(x + 2) + 3$ is obtained by translating the graph of $y = f(x)$ right 2 units and up 3 units.  

#### FOCUS ON CONCEPTS
47. Use the data in Table Ex-47 to make a plot of $y = f(g(x))$.
   | $x$ | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | $f(x)$ | -4 | -3 | -2 | -1 | 0 | 1 | 2 |
   | $g(x)$ | -1 | 0 | 1 | 2 | 3 | -2 | -3 |

48. Find the domain of $g \circ f$ for the functions $f$ and $g$ in Exercise 47.  

49. Sketch the graph of $y = f(g(x))$ for the functions graphed in Figure Ex-49.  

50. Sketch the graph of $y = g(f(x))$ for the functions graphed in Exercise 49.  

51. Use the graphs of $f$ and $g$ in Exercise 49 to estimate the solutions of the equations $f(g(x)) = 0$ and $g(f(x)) = 0$.  

52. Use the table given in Exercise 47 to solve the equations $f(g(x)) = 0$ and $g(f(x)) = 0$.  

**53–56** Find
$$\frac{f(x + h) - f(x)}{h} \quad \text{and} \quad \frac{f(w) - f(x)}{w - x}$$
Simplify as much as possible.  
53. $f(x) = 3x^2 - 5$  
54. $f(x) = x^2 + 6x$  
55. $f(x) = 1/x$  
56. $f(x) = 1/x^2$  

57. Classify the functions whose values are given in Table Ex-57 as even, odd, or neither.
   | $x$ | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | $f(x)$ | 5 | 3 | 2 | 3 | 1 | -3 | 5 |
   | $g(x)$ | 4 | 1 | -2 | 0 | 2 | -1 | -4 |
   | $h(x)$ | 2 | -5 | 8 | -2 | 8 | -5 | 2 |

58. Complete Table Ex-58 so that the graph of $y = f(x)$ is symmetric about  
    (a) the $y$-axis  
    (b) the origin.
   | $x$ | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | $f(x)$ | 1 | | -1 | 0 | | -5 | |

59. The accompanying figure (Figure Ex-59) shows a portion of a graph. Complete the graph so that the entire graph is symmetric about  
    (a) the $x$-axis  
    (b) the $y$-axis  
    (c) the origin.  

60. The accompanying figure (Figure Ex-60) shows a portion of the graph of a function $f$. Complete the graph assuming that  
    (a) $f$ is an even function  
    (b) $f$ is an odd function.  

**61–62** Classify the functions graphed in the accompanying figures as even, odd, or neither.  
61. (a) and (b) in Figure Ex-61  
62. (a) and (b) in Figure Ex-62  

63. In each part, classify the function as even, odd, or neither.  
    (a) $f(x) = x^2$  
    (b) $f(x) = x^3$  
    (c) $f(x) = |x|$  
    (d) $f(x) = x + 1$  
    (e) $f(x) = \frac{x^5 - x}{1 + x^2}$  
    (f) $f(x) = 2$  

64. Suppose that the function $f$ has domain all real numbers. Determine whether each function can be classified as even or odd. Explain.  
    (a) $g(x) = \frac{f(x) + f(-x)}{2}$  
    (b) $h(x) = \frac{f(x) - f(-x)}{2}$  

65. Suppose that the function $f$ has domain all real numbers. Show that $f$ can be written as the sum of an even function and an odd function. [*Hint:* See Exercise 64.]  

**66–67** Use Theorem 0.2.3 to determine whether the graph has symmetries about the $x$-axis, the $y$-axis, or the origin.  
66. (a) $x = 5y^2 + 9$  
    (b) $x^2 - 2y^2 = 3$  
    (c) $xy = 5$  
67. (a) $x^4 = 2y^3 + y$  
    (b) $y = \frac{x}{3 + x^2}$  
    (c) $y^2 = |x| - 5$  

**68–69** (i) Use a graphing utility to graph the equation in the first quadrant. [*Note:* To do this you will have to solve the equation for $y$ in terms of $x$.] (ii) Use symmetry to make a hand-drawn sketch of the entire graph. (iii) Confirm your work by generating the graph of the equation in the remaining three quadrants.  
68. $9x^2 + 4y^2 = 36$  
69. $4x^2 + 16y^2 = 16$  

70. The graph of the equation $x^{2/3} + y^{2/3} = 1$, which is shown in Figure Ex-70, is called a **four-cusped hypocycloid**.  
    (a) Use Theorem 0.2.3 to confirm that this graph is symmetric about the $x$-axis, the $y$-axis, and the origin.  
    (b) Find a function $f$ whose graph in the first quadrant coincides with the four-cusped hypocycloid, and use a graphing utility to confirm your work.  
    (c) Repeat part (b) for the remaining three quadrants.  

71. The equation $y = |f(x)|$ can be written as
    $$y = \begin{cases} f(x), & f(x) \ge 0 \\ -f(x), & f(x) < 0 \end{cases}$$
    which shows that the graph of $y = |f(x)|$ can be obtained from the graph of $y = f(x)$ by retaining the portion that lies on or above the $x$-axis and reflecting about the $x$-axis the portion that lies below the $x$-axis. Use this method to obtain the graph of $y = |2x - 3|$ from the graph of $y = 2x - 3$.  

**72–73** Use the method described in Exercise 71.  
72. Sketch the graph of $y = |1 - x^2|$.  
73. Sketch the graph of  
    (a) $f(x) = |\cos x|$  
    (b) $f(x) = \cos x + |\cos x|$.  

74. The **greatest integer function**, $\lfloor x \rfloor$, is defined to be the greatest integer that is less than or equal to $x$. For example, $\lfloor 2.7 \rfloor = 2$, $\lfloor -2.3 \rfloor = -3$, and $\lfloor 4 \rfloor = 4$. In each part, sketch the graph of $y = f(x)$.  
    (a) $f(x) = \lfloor x \rfloor$  
    (b) $f(x) = \lfloor x^2 \rfloor$  
    (c) $f(x) = \lfloor x \rfloor^2$  
    (d) $f(x) = \lfloor \sin x \rfloor$  

75. Is it ever true that $f \circ g = g \circ f$ if $f$ and $g$ are nonconstant functions? If not, prove it; if so, give some examples for which it is true.  

#### QUICK CHECK ANSWERS 0.2
1. (a) $(f + g)(x) = 3\sqrt{x} - 2 + x; \; x \ge 0$  
   (b) $(f - g)(x) = 3\sqrt{x} - 2 - x; \; x \ge 0$  
   (c) $(fg)(x) = 3x^{3/2} - 2x; \; x \ge 0$  
   (d) $(f/g)(x) = \frac{3\sqrt{x} - 2}{x}; \; x > 0$  
2. (a) $(f \circ g)(x) = 2 - x; \; x \ge 0$  
   (b) $(g \circ f)(x) = \sqrt{2 - x^2}; \; -\sqrt{2} \le x \le \sqrt{2}$  
3. right; 2; up; 1  
4. (a) W (b) yes  

---

## 0.3 FAMILIES OF FUNCTIONS

Functions are often grouped into families according to the form of their defining formulas or other common characteristics. In this section we will discuss some of the most basic families of functions.

### FAMILIES OF CURVES

The graph of a constant function $f(x) = c$ is the graph of the equation $y = c$, which is the horizontal line shown in Figure 0.3.1a. If we vary $c$, then we obtain a set or **family of horizontal lines** such as those in Figure 0.3.1b.

Constants that are varied to produce families of curves are called **parameters**. For example, recall that an equation of the form $y = mx + b$ represents a line of slope $m$ and $y$-intercept $b$. If we keep $b$ fixed and treat $m$ as a parameter, then we obtain a family of lines whose members all have $y$-intercept $b$ (Figure 0.3.2a), and if we keep $m$ fixed and treat $b$ as a parameter, we obtain a family of parallel lines whose members all have slope $m$ (Figure 0.3.2b).

---

### POWER FUNCTIONS; THE FAMILY $y = x^n$

A function of the form $f(x) = x^p$, where $p$ is constant, is called a **power function**. For the moment, let us consider the case where $p$ is a positive integer, say $p = n$. The graphs of the curves $y = x^n$ for $n = 1, 2, 3, 4$, and $5$ are shown in Figure 0.3.3. The first graph is the line with slope 1 that passes through the origin, and the second is a parabola that opens up and has its vertex at the origin (see Web Appendix H).

For $n \ge 2$ the shape of the curve $y = x^n$ depends on whether $n$ is even or odd (Figure 0.3.4):
* **For even values of $n$**, the functions $f(x) = x^n$ are even, so their graphs are symmetric about the $y$-axis. The graphs all have the general shape of the graph of $y = x^2$, and each graph passes through the points $(-1, 1)$, $(0, 0)$, and $(1, 1)$. As $n$ increases, the graphs become flatter over the interval $-1 < x < 1$ and steeper over the intervals $x > 1$ and $x < -1$.
* **For odd values of $n$**, the functions $f(x) = x^n$ are odd, so their graphs are symmetric about the origin. The graphs all have the general shape of the curve $y = x^3$, and each graph passes through the points $(-1, -1)$, $(0, 0)$, and $(1, 1)$. As $n$ increases, the graphs become flatter over the interval $-1 < x < 1$ and steeper over the intervals $x > 1$ and $x < -1$.

> **REMARK**  
> The flattening and steepening effects can be understood by considering what happens when a number $x$ is raised to higher and higher powers: If $-1 < x < 1$, then the absolute value of $x^n$ decreases as $n$ increases, thereby causing the graphs to become flatter on this interval as $n$ increases (try raising $\frac{1}{2}$ or $-\frac{1}{2}$ to higher and higher powers). On the other hand, if $x > 1$ or $x < -1$, then the absolute value of $x^n$ increases as $n$ increases, thereby causing the graphs to become steeper on these intervals as $n$ increases (try raising 2 or $-2$ to higher and higher powers).

---

### THE FAMILY $y = x^{-n}$

If $p$ is a negative integer, say $p = -n$, then the power functions $f(x) = x^p$ have the form $f(x) = x^{-n} = 1/x^n$. Figure 0.3.5 shows the graphs of $y = 1/x$ and $y = 1/x^2$. The graph of $y = 1/x$ is called an **equilateral hyperbola** (for reasons to be discussed later).

As illustrated in Figure 0.3.5, the shape of the curve $y = 1/x^n$ depends on whether $n$ is even or odd:
* **For even values of $n$**, the functions $f(x) = 1/x^n$ are even, so their graphs are symmetric about the $y$-axis. The graphs all have the general shape of the curve $y = 1/x^2$, and each graph passes through the points $(-1, 1)$ and $(1, 1)$. As $n$ increases, the graphs become steeper over the intervals $-1 < x < 0$ and $0 < x < 1$ and become flatter over the intervals $x > 1$ and $x < -1$.
* **For odd values of $n$**, the functions $f(x) = 1/x^n$ are odd, so their graphs are symmetric about the origin. The graphs all have the general shape of the curve $y = 1/x$, and each graph passes through the points $(1, 1)$ and $(-1, -1)$. As $n$ increases, the graphs become steeper over the intervals $-1 < x < 0$ and $0 < x < 1$ and become flatter over the intervals $x > 1$ and $x < -1$.
* For both even and odd values of $n$ the graph $y = 1/x^n$ has a break at the origin (called a **discontinuity**), which occurs because division by zero is undefined.

---

### INVERSE PROPORTIONS

Recall that a variable $y$ is said to be **inversely proportional** to a variable $x$ if there is a positive constant $k$, called the **constant of proportionality**, such that
$$y = \frac{k}{x} \tag{1}$$
Since $k$ is assumed to be positive, the graph of (1) has the same shape as $y = 1/x$ but is compressed or stretched in the $y$-direction. Also, it should be evident from (1) that doubling $x$ multiplies $y$ by $\frac{1}{2}$, tripling $x$ multiplies $y$ by $\frac{1}{3}$, and so forth.

Equation (1) can be expressed as $xy = k$, which tells us that the product of inversely proportional variables is a positive constant. This is a useful form for identifying inverse proportionality in experimental data.

#### Example 1
Table 0.3.1 shows some experimental data.

##### Table 0.3.1
| $x$ | 0.8 | 1 | 2.5 | 4 | 6.25 | 10 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $y$ | 6.25 | 5 | 2 | 1.25 | 0.8 | 0.5 |

(a) Explain why the data suggest that $y$ is inversely proportional to $x$.  
(b) Express $y$ as a function of $x$.  
(c) Graph your function and the data together for $x > 0$.

**Solution.** For every data point we have $xy = 5$, so $y$ is inversely proportional to $x$ and $y = 5/x$. The graph of this equation with the data points is shown in Figure 0.3.6.

Inverse proportions arise in various laws of physics. For example, **Boyle's law** in physics states that if a fixed amount of an ideal gas is held at a constant temperature, then the product of the pressure $P$ exerted by the gas and the volume $V$ that it occupies is constant; that is,
$$PV = k$$
This implies that the variables $P$ and $V$ are inversely proportional to one another. Figure 0.3.7 shows a typical graph of volume versus pressure under the conditions of Boyle's law. Note how doubling the pressure corresponds to halving the volume, as expected.

---

### POWER FUNCTIONS WITH NONINTEGER EXPONENTS

If $p = 1/n$, where $n$ is a positive integer, then the power functions $f(x) = x^p$ have the form
$$f(x) = x^{1/n} = \sqrt[n]{x}$$
In particular, if $n = 2$, then $f(x) = \sqrt{x}$, and if $n = 3$, then $f(x) = \sqrt[3]{x}$. The graphs of these functions are shown in parts (a) and (b) of Figure 0.3.8.

Since every real number has a real cube root, the domain of the function $f(x) = \sqrt[3]{x}$ is $(-\infty, +\infty)$, and hence the graph of $y = \sqrt[3]{x}$ extends over the entire $x$-axis. In contrast, the graph of $y = \sqrt{x}$ extends only over the interval $[0, +\infty)$ because $\sqrt{x}$ is imaginary for negative $x$. As illustrated in Figure 0.3.8c, the graphs of $y = \sqrt{x}$ and $y = -\sqrt{x}$ form the upper and lower halves of the parabola $x = y^2$. In general, the graph of $y = \sqrt[n]{x}$ extends over the entire $x$-axis if $n$ is odd, but extends only over the interval $[0, +\infty)$ if $n$ is even.

Power functions can have other fractional exponents. Some examples are
$$f(x) = x^{2/3}, \quad f(x) = \sqrt[5]{x^3}, \quad f(x) = x^{-7/8} \tag{2}$$
The graph of $f(x) = x^{2/3}$ is shown in Figure 0.3.9. We will discuss expressions involving irrational exponents later.

> **TECHNOLOGY MASTERY**  
> Graphing utilities sometimes omit portions of the graph of a function involving fractional exponents (or radicals). If $f(x) = x^{p/q}$, where $p/q$ is a positive fraction in lowest terms, then you can circumvent this problem as follows:  
> * If $p$ is even and $q$ is odd, then graph $g(x) = |x|^{p/q}$ instead of $f(x)$.  
> * If $p$ is odd and $q$ is odd, then graph $g(x) = (|x|/x)|x|^{p/q}$ instead of $f(x)$.  
> Use a graphing utility to generate graphs of $f(x) = \sqrt[5]{x^3}$ and $f(x) = x^{-7/8}$ that show all of their significant features.

---

### POLYNOMIALS

A **polynomial** in $x$ is a function that is expressible as a sum of finitely many terms of the form $cx^n$, where $c$ is a constant and $n$ is a nonnegative integer. Some examples of polynomials are
$$2x + 1, \quad 3x^2 + 5x - \sqrt{2}, \quad x^3, \quad 4 \; (= 4x^0), \quad 5x^7 - x^4 + 3$$

The function $(x^2 - 4)^3$ is also a polynomial because it can be expanded by the binomial formula (see the inside front cover) and expressed as a sum of terms of the form $cx^n$:
$$(x^2 - 4)^3 = (x^2)^3 - 3(x^2)^2(4) + 3(x^2)(4^2) - (4^3) = x^6 - 12x^4 + 48x^2 - 64 \tag{3}$$

A general polynomial can be written in either of the following forms, depending on whether one wants the powers of $x$ in ascending or descending order:
$$\begin{aligned}
&c_0 + c_1 x + c_2 x^2 + \dots + c_n x^n \\
&c_n x^n + c_{n-1} x^{n-1} + \dots + c_1 x + c_0
\end{aligned}$$

The constants $c_0, c_1, \dots, c_n$ are called the **coefficients** of the polynomial. When a polynomial is expressed in one of these forms, the highest power of $x$ that occurs with a nonzero coefficient is called the **degree** of the polynomial. Nonzero constant polynomials are considered to have degree 0, since we can write $c = cx^0$. Polynomials of degree 1, 2, 3, 4, and 5 are described as **linear**, **quadratic**, **cubic**, **quartic**, and **quintic**, respectively. For example:
* $3 + 5x$ — Has degree 1 (linear)
* $x^2 - 3x + 1$ — Has degree 2 (quadratic)
* $2x^3 - 7$ — Has degree 3 (cubic)
* $8x^4 - 9x^3 + 5x - 3$ — Has degree 4 (quartic)
* $\sqrt{3} + x^3 + x^5$ — Has degree 5 (quintic)
* $(x^2 - 4)^3$ — Has degree 6 [see (3)]

> *Note:* The constant 0 is a polynomial called the **zero polynomial**. In this text we will take the degree of the zero polynomial to be undefined. Other texts may use different conventions for the degree of the zero polynomial.

The natural domain of a polynomial in $x$ is $(-\infty, +\infty)$, since the only operations involved are multiplication and addition; the range depends on the particular polynomial. We already know that the graphs of polynomials of degree 0 and 1 are lines and that the graphs of polynomials of degree 2 are parabolas. Figure 0.3.10 shows the graphs of some typical polynomials of higher degree. Later, we will discuss polynomial graphs in detail, but for now it suffices to observe that graphs of polynomials are very well behaved in the sense that they have no discontinuities or sharp corners. As illustrated in Figure 0.3.10, the graphs of polynomials wander up and down for awhile in a roller-coaster fashion, but eventually that behavior stops and the graphs steadily rise or fall indefinitely as one travels along the curve in either the positive or negative direction. We will see later that the number of peaks and valleys is less than the degree of the polynomial.

---

### RATIONAL FUNCTIONS

A function that can be expressed as a ratio of two polynomials is called a **rational function**. If $P(x)$ and $Q(x)$ are polynomials, then the domain of the rational function
$$f(x) = \frac{P(x)}{Q(x)}$$
consists of all values of $x$ such that $Q(x) \neq 0$. For example, the domain of the rational function
$$f(x) = \frac{x^2 + 2x}{x^2 - 1}$$
consists of all values of $x$, except $x = 1$ and $x = -1$. Its graph is shown in Figure 0.3.11 along with the graphs of two other typical rational functions.

The graphs of rational functions with nonconstant denominators differ from the graphs of polynomials in some essential ways:
* Unlike polynomials whose graphs are continuous (unbroken) curves, the graphs of rational functions have discontinuities at the points where the denominator is zero.
* Unlike polynomials, rational functions may have numbers at which they are not defined. Near such points, many rational functions have graphs that closely approximate a vertical line, called a **vertical asymptote**. These are represented by the dashed vertical lines in Figure 0.3.11.
* Unlike the graphs of nonconstant polynomials, which eventually rise or fall indefinitely, the graphs of many rational functions eventually get closer and closer to some horizontal line, called a **horizontal asymptote**, as one traverses the curve in either the positive or negative direction. The horizontal asymptotes are represented by the dashed horizontal lines in the first two parts of Figure 0.3.11. In the third part of the figure the $x$-axis is a horizontal asymptote.

---

### ALGEBRAIC FUNCTIONS

Functions that can be constructed from polynomials by applying finitely many algebraic operations (addition, subtraction, multiplication, division, and root extraction) are called **algebraic functions**. Some examples are
$$f(x) = \sqrt{x^2 - 4}, \quad f(x) = 3\sqrt[3]{x}(2 + x), \quad f(x) = x^{2/3}(x + 2)^2$$
As illustrated in Figure 0.3.12, the graphs of algebraic functions vary widely, so it is difficult to make general statements about them. Later in this text we will develop general calculus methods for analyzing such functions.

---

### THE FAMILIES $y = A\sin Bx$ AND $y = A\cos Bx$

Many important applications lead to trigonometric functions of the form
$$f(x) = A\sin(Bx - C) \quad \text{and} \quad g(x) = A\cos(Bx - C) \tag{4}$$
where $A, B$, and $C$ are nonzero constants. The graphs of such functions can be obtained by stretching, compressing, translating, and reflecting the graphs of $y = \sin x$ and $y = \cos x$ appropriately.

> *Note:* In this text we will assume that the independent variable of a trigonometric function is in radians unless otherwise stated. A review of trigonometric functions can be found in Appendix B.

To see why this is so, let us start with the case where $C = 0$ and consider how the graphs of the equations
$$y = A\sin Bx \quad \text{and} \quad y = A\cos Bx$$
relate to the graphs of $y = \sin x$ and $y = \cos x$. If $A$ and $B$ are positive, then the effect of the constant $A$ is to stretch or compress the graphs of $y = \sin x$ and $y = \cos x$ vertically and the effect of the constant $B$ is to compress or stretch the graphs of $\sin x$ and $\cos x$ horizontally. For example, the graph of $y = 2\sin 4x$ can be obtained by stretching the graph of $y = \sin x$ vertically by a factor of 2 and compressing it horizontally by a factor of 4. (Recall from Section 0.2 that the multiplier of $x$ stretches when it is less than 1 and compresses when it is greater than 1.) Thus, as shown in Figure 0.3.13, the graph of $y = 2\sin 4x$ varies between $-2$ and 2, and repeats every $2\pi/4 = \pi/2$ units.

In general, if $A$ and $B$ are positive numbers, then the graphs of
$$y = A\sin Bx \quad \text{and} \quad y = A\cos Bx$$
oscillate between $-A$ and $A$ and repeat every $2\pi/B$ units, so we say that these functions have **amplitude $A$** and **period $2\pi/B$**. In addition, we define the **frequency** of these functions to be the reciprocal of the period, that is, the frequency is $B/(2\pi)$. If $A$ or $B$ is negative, then these constants cause reflections of the graphs about the axes as well as compressing or stretching them; and in this case the amplitude, period, and frequency are given by
$$\text{amplitude} = |A|, \quad \text{period} = \frac{2\pi}{|B|}, \quad \text{frequency} = \frac{|B|}{2\pi}$$

#### Example 2
Make sketches of the following graphs that show the period and amplitude.  
(a) $y = 3\sin 2\pi x$  
(b) $y = -3\cos 0.5x$  
(c) $y = 1 + \sin x$

**Solution (a).** The equation is of the form $y = A\sin Bx$ with $A = 3$ and $B = 2\pi$, so the graph has the shape of a sine function, but it has an amplitude of $A = 3$ and a period of $2\pi/B = 2\pi/(2\pi) = 1$ (Figure 0.3.14a).

**Solution (b).** The equation is of the form $y = A\cos Bx$ with $A = -3$ and $B = 0.5$, so the graph has the shape of a cosine curve that has been reflected about the $x$-axis (because $A = -3$ is negative), but with amplitude $|A| = 3$ and period $2\pi/B = 2\pi/0.5 = 4\pi$ (Figure 0.3.14b).

**Solution (c).** The graph has the shape of a sine curve that has been translated up 1 unit (Figure 0.3.14c).

---

### THE FAMILIES $y = A\sin(Bx - C)$ AND $y = A\cos(Bx - C)$

To investigate the graphs of the more general families
$$y = A\sin(Bx - C) \quad \text{and} \quad y = A\cos(Bx - C)$$
it will be helpful to rewrite these equations as
$$y = A\sin\left[B\left(x - \frac{C}{B}\right)\right] \quad \text{and} \quad y = A\cos\left[B\left(x - \frac{C}{B}\right)\right]$$
In this form we see that the graphs of these equations can be obtained by translating the graphs of $y = A\sin Bx$ and $y = A\cos Bx$ to the left or right, depending on the sign of $C/B$. For example, if $C/B > 0$, then the graph of
$$y = A\sin[B(x - C/B)] = A\sin(Bx - C)$$
can be obtained by translating the graph of $y = A\sin Bx$ to the right by $C/B$ units (Figure 0.3.15). If $C/B < 0$, the graph of $y = A\sin(Bx - C)$ is obtained by translating the graph of $y = A\sin Bx$ to the left by $|C/B|$ units.

#### Example 3
Find the amplitude and period of
$$y = 3\cos\left(2x + \frac{\pi}{2}\right)$$
and determine how the graph of $y = 3\cos 2x$ should be translated to produce the graph of this equation. Confirm your results by graphing the equation on a calculator or computer.

**Solution.** The equation can be rewritten as
$$y = 3\cos\left[2x - \left(-\frac{\pi}{2}\right)\right] = 3\cos\left[2\left(x - \left(-\frac{\pi}{4}\right)\right)\right]$$
which is of the form
$$y = A\cos\left[B\left(x - \frac{C}{B}\right)\right]$$
with $A = 3$, $B = 2$, and $C/B = -\pi/4$. It follows that the amplitude is $A = 3$, the period is $2\pi/B = \pi$, and the graph is obtained by translating the graph of $y = 3\cos 2x$ left by $|C/B| = \pi/4$ units (Figure 0.3.16).

---

### QUICK CHECK EXERCISES 0.3
*(See page 38 for answers.)*

1. Consider the family of functions $y = x^n$, where $n$ is an integer. The graphs of $y = x^n$ are symmetric with respect to the $y$-axis if $n$ is $\underline{\hspace{2cm}}$. These graphs are symmetric with respect to the origin if $n$ is $\underline{\hspace{2cm}}$. The $y$-axis is a vertical asymptote for these graphs if $n$ is $\underline{\hspace{2cm}}$.  
2. What is the natural domain of a polynomial?  
3. Consider the family of functions $y = x^{1/n}$, where $n$ is a nonzero integer. Find the natural domain of these functions if $n$ is  
   (a) positive and even  
   (b) positive and odd  
   (c) negative and even  
   (d) negative and odd.  
4. Classify each equation as a polynomial, rational, algebraic, or not an algebraic function.  
   (a) $y = \sqrt{x} + 2$  
   (b) $y = \sqrt{3x^4 - x + 1}$  
   (c) $y = 5x^3 + \cos 4x$  
   (d) $y = \frac{x^2 + 5}{2x - 7}$  
   (e) $y = 3x^2 + 4x^{-2}$  
5. The graph of $y = A\sin Bx$ has amplitude $\underline{\hspace{2cm}}$ and is periodic with period $\underline{\hspace{2cm}}$.  

---

### EXERCISE SET 0.3

1. (a) Find an equation for the family of lines whose members have slope $m = 3$.  
   (b) Find an equation for the member of the family that passes through $(-1, 3)$.  
   (c) Sketch some members of the family, and label them with their equations. Include the line in part (b).  

2. Find an equation for the family of lines whose members are perpendicular to those in Exercise 1.  

3. (a) Find an equation for the family of lines with $y$-intercept $b = 2$.  
   (b) Find an equation for the member of the family whose angle of inclination is $135^\circ$.  
   (c) Sketch some members of the family, and label them with their equations. Include the line in part (b).  

4. Find an equation for  
   (a) the family of lines that pass through the origin  
   (b) the family of lines with $x$-intercept $a = 1$  
   (c) the family of lines that pass through the point $(1, -2)$  
   (d) the family of lines parallel to $2x + 4y = 1$.  

5. Find an equation for the family of lines tangent to the circle with center at the origin and radius 3.  

6. Find an equation for the family of lines that pass through the intersection of $5x - 3y + 11 = 0$ and $2x - 9y + 7 = 0$.  

7. The U.S. Internal Revenue Service uses a 10-year linear depreciation schedule to determine the value of various business items. This means that an item is assumed to have a value of zero at the end of the tenth year and that at intermediate times the value is a linear function of the elapsed time. Sketch some typical depreciation lines, and explain the practical significance of the $y$-intercepts.  

8. Find all lines through $(6, -1)$ for which the product of the $x$- and $y$-intercepts is 3.  

#### FOCUS ON CONCEPTS
**9–10** State a geometric property common to all lines in the family, and sketch five of the lines.  
9. (a) The family $y = -x + b$  
   (b) The family $y = mx - 1$  
   (c) The family $y = m(x + 4) + 2$  
   (d) The family $x - ky = 1$  

10. (a) The family $y = b$  
    (b) The family $Ax + 2y + 1 = 0$  
    (c) The family $2x + By + 1 = 0$  
    (d) The family $y - 1 = m(x + 1)$  

11. In each part, match the equation with one of the accompanying graphs (Figure Ex-11: I, II, III, IV, V, VI).  
    (a) $y = \sqrt[5]{x}$  
    (b) $y = 2x^5$  
    (c) $y = -1/x^8$  
    (d) $y = \sqrt{x^2 - 1}$  
    (e) $y = \sqrt[4]{x - 2}$  
    (f) $y = -\sqrt[5]{x^2}$  

12. The accompanying table (Table Ex-12) gives approximate values of three functions: one of the form $kx^2$, one of the form $kx^{-3}$, and one of the form $kx^{3/2}$. Identify which is which, and estimate $k$ in each case.
   | $x$ | 0.25 | 0.37 | 2.1 | 4.0 | 5.8 | 6.2 | 7.9 | 9.3 |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | $f(x)$ | 640 | 197 | 1.08 | 0.156 | 0.0513 | 0.0420 | 0.0203 | 0.0124 |
   | $g(x)$ | 0.0312 | 0.0684 | 2.20 | 8.00 | 16.8 | 19.2 | 31.2 | 43.2 |
   | $h(x)$ | 0.250 | 0.450 | 6.09 | 16.0 | 27.9 | 30.9 | 44.4 | 56.7 |

**13–14** Sketch the graph of the equation for $n = 1, 3,$ and $5$ in one coordinate system and for $n = 2, 4,$ and $6$ in another coordinate system. If you have a graphing utility, use it to check your work.  
13. (a) $y = -x^n$  
    (b) $y = 2x^{-n}$  
    (c) $y = (x - 1)^{1/n}$  
14. (a) $y = 2x^n$  
    (b) $y = -x^{-n}$  
    (c) $y = -3(x + 2)^{1/n}$  

15. (a) Sketch the graph of $y = ax^2$ for $a = \pm 1, \pm 2,$ and $\pm 3$ in a single coordinate system.  
    (b) Sketch the graph of $y = x^2 + b$ for $b = \pm 1, \pm 2,$ and $\pm 3$ in a single coordinate system.  
    (c) Sketch some typical members of the family of curves $y = ax^2 + b$.  

16. (a) Sketch the graph of $y = a\sqrt{x}$ for $a = \pm 1, \pm 2,$ and $\pm 3$ in a single coordinate system.  
    (b) Sketch the graph of $y = \sqrt{x} + b$ for $b = \pm 1, \pm 2,$ and $\pm 3$ in a single coordinate system.  
    (c) Sketch some typical members of the family of curves $y = a\sqrt{x} + b$.  

**17–18** Sketch the graph of the equation by making appropriate transformations to the graph of a basic power function. If you have a graphing utility, use it to check your work.  
17. (a) $y = 2(x + 1)^2$  
    (b) $y = -3(x - 2)^3$  
    (c) $y = \frac{-3}{(x + 1)^2}$  
    (d) $y = \frac{1}{(x - 3)^5}$  
18. (a) $y = 1 - \sqrt{x + 2}$  
    (b) $y = 1 - \sqrt[3]{x + 2}$  
    (c) $y = \frac{5}{(1 - x)^3}$  
    (d) $y = \frac{2}{(4 + x)^4}$  

19. Sketch the graph of $y = x^2 + 2x$ by completing the square and making appropriate transformations to the graph of $y = x^2$.  

20. (a) Use the graph of $y = \sqrt{x}$ to help sketch the graph of $y = \sqrt{|x|}$.  
    (b) Use the graph of $y = \sqrt[3]{x}$ to help sketch the graph of $y = \sqrt[3]{|x|}$.  

21. As discussed in this section, Boyle's law states that at a constant temperature the pressure $P$ exerted by a gas is related to the volume $V$ by the equation $PV = k$.  
    (a) Find the appropriate units for the constant $k$ if pressure (which is force per unit area) is in newtons per square meter ($\text{N/m}^2$) and volume is in cubic meters ($\text{m}^3$).  
    (b) Find $k$ if the gas exerts a pressure of $20{,}000\text{ N/m}^2$ when the volume is 1 liter ($0.001\text{ m}^3$).  
    (c) Make a table that shows the pressures for volumes of 0.25, 0.5, 1.0, 1.5, and 2.0 liters.  
    (d) Make a graph of $P$ versus $V$.  

22. A manufacturer of cardboard drink containers wants to construct a closed rectangular container that has a square base and will hold $\frac{1}{10}\text{ liter}$ ($100\text{ cm}^3$). Estimate the dimensions of the container that will require the least amount of material for its manufacture.  

**23–24** A variable $y$ is said to be *inversely proportional to the square* of a variable $x$ if $y$ is related to $x$ by an equation of the form $y = k/x^2$, where $k$ is a nonzero constant, called the constant of proportionality. This terminology is used in these exercises.  
23. According to Coulomb's law, the force $F$ of attraction between positive and negative point charges is inversely proportional to the square of the distance $x$ between them.  
    (a) Assuming that the force of attraction between two point charges is 0.0005 newton when the distance between them is 0.3 meter, find the constant of proportionality (with proper units).  
    (b) Find the force of attraction between the point charges when they are 3 meters apart.  
    (c) Make a graph of force versus distance for the two charges.  
    (d) What happens to the force as the particles get closer and closer together? What happens as they get farther and farther apart?  

24. It follows from Newton's Law of Universal Gravitation that the weight $W$ of an object (relative to the Earth) is inversely proportional to the square of the distance $x$ between the object and the center of the Earth, that is, $W = C/x^2$.  
    (a) Assuming that a weather satellite weighs 2000 pounds on the surface of the Earth and that the Earth is a sphere of radius 4000 miles, find the constant $C$.  
    (b) Find the weight of the satellite when it is 1000 miles above the surface of the Earth.  
    (c) Make a graph of the satellite's weight versus its distance from the center of the Earth.  
    (d) Is there any distance from the center of the Earth at which the weight of the satellite is zero? Explain your reasoning.  

**25–28 True–False** Determine whether the statement is true or false. Explain your answer.  
25. Each curve in the family $y = 2x + b$ is parallel to the line $y = 2x$.  
26. Each curve in the family $y = x^2 + bx + c$ is a translation of the graph of $y = x^2$.  
27. If a curve passes through the point $(2, 6)$ and $y$ is inversely proportional to $x$, then the constant of proportionality is 3.  
28. Curves in the family $y = -5\sin(A\pi x)$ have amplitude 5 and period $2/|A|$.  

#### FOCUS ON CONCEPTS
29. In each part, match the equation with one of the accompanying graphs (Figure Ex-29: I, II, III, IV), and give the equations for the horizontal and vertical asymptotes.  
    (a) $y = \frac{x^2}{x^2 - x - 2}$  
    (b) $y = \frac{x - 1}{x^2 - x - 6}$  
    (c) $y = \frac{2x^4}{x^4 + 1}$  
    (d) $y = \frac{4}{(x + 2)^2}$  

30. Find an equation of the form $y = k/(x^2 + bx + c)$ whose graph is a reasonable match to that in Figure Ex-30. If you have a graphing utility, use it to check your work.  

**31–32** Find an equation of the form $y = D + A\sin Bx$ or $y = D + A\cos Bx$ for each graph.  
31. Graphs (a), (b), (c) in Figure Ex-31.  
32. Graphs (a), (b), (c) in Figure Ex-32.  

33. In each part, find an equation for the graph that has the form $y = y_0 + A\sin(Bx - C)$. (Parts (a), (b), (c) in Figure Ex-33).  

34. In the United States, a standard electrical outlet supplies sinusoidal electrical current with a maximum voltage of $V = 120\sqrt{2}\text{ volts}$ (V) at a frequency of 60 hertz (Hz). Write an equation that expresses $V$ as a function of the time $t$, assuming that $V = 0$ if $t = 0$. [*Note:* $1\text{ Hz} = 1\text{ cycle per second}$.]  

**35–36** Find the amplitude and period, and sketch at least two periods of the graph by hand. If you have a graphing utility, use it to check your work.  
35. (a) $y = 3\sin 4x$  
    (b) $y = -2\cos \pi x$  
    (c) $y = 2 + \cos\left(\frac{x}{2}\right)$  
36. (a) $y = -1 - 4\sin 2x$  
    (b) $y = \frac{1}{2}\cos(3x - \pi)$  
    (c) $y = -4\sin\left(\frac{x}{3} + 2\pi\right)$  

37. Equations of the form
    $$x = A_1 \sin \omega t + A_2 \cos \omega t$$
    arise in the study of vibrations and other periodic motion. Express the equation
    $$x = \sqrt{2}\sin 2\pi t + \sqrt{6}\cos 2\pi t$$
    in the form $x = A\sin(\omega t + \theta)$, and use a graphing utility to confirm that both equations have the same graph.  

38. Determine the number of solutions of $x = 2\sin x$, and use a graphing or calculating utility to estimate them.  

#### QUICK CHECK ANSWERS 0.3
1. even; odd; negative  
2. $(-\infty, +\infty)$  
3. (a) $[0, +\infty)$ (b) $(-\infty, +\infty)$ (c) $(0, +\infty)$ (d) $(-\infty, 0) \cup (0, +\infty)$  
4. (a) algebraic (b) polynomial (c) not algebraic (d) rational (e) rational  
5. $|A|$; $2\pi/|B|$  

---

## 0.4 INVERSE FUNCTIONS

In everyday language the term "inversion" conveys the idea of a reversal. For example, in meteorology a temperature inversion is a reversal in the usual temperature properties of air layers, and in music a melodic inversion reverses an ascending interval to the corresponding descending interval. In mathematics the term **inverse** is used to describe functions that reverse one another in the sense that each undoes the effect of the other. In this section we discuss this fundamental mathematical idea.

### INVERSE FUNCTIONS

The idea of solving an equation $y = f(x)$ for $x$ as a function of $y$, say $x = g(y)$, is one of the most important ideas in mathematics. Sometimes, solving an equation is a simple process; for example, using basic algebra the equation
$$y = x^3 + 1 \quad [y = f(x)]$$
can be solved for $x$ as a function of $y$:
$$x = \sqrt[3]{y - 1} \quad [x = g(y)]$$
The first equation is better for computing $y$ if $x$ is known, and the second is better for computing $x$ if $y$ is known (Figure 0.4.1).

Our primary interest in this section is to identify relationships that may exist between the functions $f$ and $g$ when an equation $y = f(x)$ is expressed as $x = g(y)$, or conversely. For example, consider the functions $f(x) = x^3 + 1$ and $g(y) = \sqrt[3]{y - 1}$ discussed above. When these functions are composed in either order, they cancel out the effect of one another in the sense that
$$\begin{aligned}
g(f(x)) &= \sqrt[3]{f(x) - 1} = \sqrt[3]{(x^3 + 1) - 1} = x \\
f(g(y)) &= [g(y)]^3 + 1 = (\sqrt[3]{y - 1})^3 + 1 = y \tag{1}
\end{aligned}$$
Pairs of functions with these two properties are so important that there is special terminology for them.

> **0.4.1 DEFINITION**  
> If the functions $f$ and $g$ satisfy the two conditions
> $$\begin{aligned}
> g(f(x)) &= x \quad \text{for every } x \text{ in the domain of } f \\
> f(g(y)) &= y \quad \text{for every } y \text{ in the domain of } g
> \end{aligned}$$
> then we say that $f$ is an **inverse** of $g$ and $g$ is an **inverse** of $f$ or that $f$ and $g$ are **inverse functions**.

It can be shown (Exercise 35) that if a function $f$ has an inverse, then that inverse is unique. Thus, if a function $f$ has an inverse, then we are entitled to talk about *the* inverse of $f$, in which case we denote it by the symbol $f^{-1}$.

> **WARNING**  
> If $f$ is a function, then the $-1$ in the symbol $f^{-1}$ always denotes an inverse and never an exponent. That is,
> $$f^{-1}(x) \text{ never means } \frac{1}{f(x)}$$

#### Example 1
The computations in (1) show that $g(y) = \sqrt[3]{y - 1}$ is the inverse of $f(x) = x^3 + 1$. Thus, we can express $g$ in inverse notation as
$$f^{-1}(y) = \sqrt[3]{y - 1}$$
and we can express the equations in Definition 0.4.1 as
$$\begin{aligned}
f^{-1}(f(x)) &= x \quad \text{for every } x \text{ in the domain of } f \\
f(f^{-1}(y)) &= y \quad \text{for every } y \text{ in the domain of } f^{-1} \tag{2}
\end{aligned}$$
We will call these the **cancellation equations** for $f$ and $f^{-1}$.

---

### CHANGING THE INDEPENDENT VARIABLE

The formulas in (2) use $x$ as the independent variable for $f$ and $y$ as the independent variable for $f^{-1}$. Although it is often convenient to use different independent variables for $f$ and $f^{-1}$, there will be occasions on which it is desirable to use the same independent variable for both. For example, if we want to graph the functions $f$ and $f^{-1}$ together in the same $xy$-coordinate system, then we would want to use $x$ as the independent variable and $y$ as the dependent variable for both functions. Thus, to graph the functions $f(x) = x^3 + 1$ and $f^{-1}(y) = \sqrt[3]{y - 1}$ of Example 1 in the same $xy$-coordinate system, we would change the independent variable $y$ to $x$, use $y$ as the dependent variable for both functions, and graph the equations
$$y = x^3 + 1 \quad \text{and} \quad y = \sqrt[3]{x - 1}$$

We will talk more about graphs of inverse functions later in this section, but for reference we give the following reformulation of the cancellation equations in (2) using $x$ as the independent variable for both $f$ and $f^{-1}$:
$$\begin{aligned}
f^{-1}(f(x)) &= x \quad \text{for every } x \text{ in the domain of } f \\
f(f^{-1}(x)) &= x \quad \text{for every } x \text{ in the domain of } f^{-1} \tag{3}
\end{aligned}$$

#### Example 2
Confirm each of the following.  
(a) The inverse of $f(x) = 2x$ is $f^{-1}(x) = \frac{1}{2}x$.  
(b) The inverse of $f(x) = x^3$ is $f^{-1}(x) = x^{1/3}$.

**Solution (a).**
$$\begin{aligned}
f^{-1}(f(x)) &= f^{-1}(2x) = \frac{1}{2}(2x) = x \\
f(f^{-1}(x)) &= f\left(\frac{1}{2}x\right) = 2\left(\frac{1}{2}x\right) = x
\end{aligned}$$

**Solution (b).**
$$\begin{aligned}
f^{-1}(f(x)) &= f^{-1}(x^3) = (x^3)^{1/3} = x \\
f(f^{-1}(x)) &= f(x^{1/3}) = (x^{1/3})^3 = x
\end{aligned}$$

> *Note:* The results in Example 2 should make sense to you intuitively, since the operations of multiplying by 2 and multiplying by $\frac{1}{2}$ in either order cancel the effect of one another, as do the operations of cubing and taking a cube root.

#### Example 3
Given that the function $f$ has an inverse and that $f(3) = 5$, find $f^{-1}(5)$.

**Solution.** Apply $f^{-1}$ to both sides of the equation $f(3) = 5$ to obtain
$$f^{-1}(f(3)) = f^{-1}(5)$$
and now apply the first equation in (3) to conclude that $f^{-1}(5) = 3$.

> *Note:* In general, if a function $f$ has an inverse and $f(a) = b$, then the procedure in Example 3 shows that $a = f^{-1}(b)$; that is, $f^{-1}$ maps each output of $f$ back into the corresponding input (Figure 0.4.2).

---

### DOMAIN AND RANGE OF INVERSE FUNCTIONS

The equations in (3) imply the following relationships between the domains and ranges of $f$ and $f^{-1}$:
$$\begin{aligned}
\text{domain of } f^{-1} &= \text{range of } f \\
\text{range of } f^{-1} &= \text{domain of } f \tag{4}
\end{aligned}$$

One way to show that two sets are the same is to show that each is a subset of the other. Thus we can establish the first equality in (4) by showing that the domain of $f^{-1}$ is a subset of the range of $f$ and that the range of $f$ is a subset of the domain of $f^{-1}$. We do this as follows: The first equation in (3) implies that $f^{-1}$ is defined at $f(x)$ for all values of $x$ in the domain of $f$, and this implies that the range of $f$ is a subset of the domain of $f^{-1}$. Conversely, if $x$ is in the domain of $f^{-1}$, then the second equation in (3) implies that $x$ is in the range of $f$ because it is the image of $f^{-1}(x)$. Thus, the domain of $f^{-1}$ is a subset of the range of $f$. We leave the proof of the second equation in (4) as an exercise.

---

### A METHOD FOR FINDING INVERSE FUNCTIONS

At the beginning of this section we observed that solving $y = f(x) = x^3 + 1$ for $x$ as a function of $y$ produces $x = f^{-1}(y) = \sqrt[3]{y - 1}$. The following theorem shows that this is not accidental.

> **0.4.2 THEOREM**  
> If an equation $y = f(x)$ can be solved for $x$ as a function of $y$, say $x = g(y)$, then $f$ has an inverse and that inverse is $g(y) = f^{-1}(y)$.

**Proof.** Substituting $y = f(x)$ into $x = g(y)$ yields $x = g(f(x))$, which confirms the first equation in Definition 0.4.1, and substituting $x = g(y)$ into $y = f(x)$ yields $y = f(g(y))$, which confirms the second equation in Definition 0.4.1. ■

Theorem 0.4.2 provides us with the following procedure for finding the inverse of a function.

> **A Procedure for Finding the Inverse of a Function $f$**  
> **Step 1.** Write down the equation $y = f(x)$.  
> **Step 2.** If possible, solve this equation for $x$ as a function of $y$.  
> **Step 3.** The resulting equation will be $x = f^{-1}(y)$, which provides a formula for $f^{-1}$ with $y$ as the independent variable.  
> **Step 4.** If $y$ is acceptable as the independent variable for the inverse function, then you are done, but if you want to have $x$ as the independent variable, then you need to interchange $x$ and $y in the equation $x = f^{-1}(y)$ to obtain $y = f^{-1}(x)$.

> *Alternative:* An alternative way to obtain a formula for $f^{-1}(x)$ with $x$ as the independent variable is to reverse the roles of $x$ and $y$ at the outset and solve the equation $x = f(y)$ for $y$ as a function of $x$.

#### Example 4
Find a formula for the inverse of $f(x) = \sqrt{3x - 2}$ with $x$ as the independent variable, and state the domain of $f^{-1}$.

**Solution.** Following the procedure stated above, we first write
$$y = \sqrt{3x - 2}$$
Then we solve this equation for $x$ as a function of $y$:
$$\begin{aligned}
y^2 &= 3x - 2 \\
x &= \frac{1}{3}(y^2 + 2)
\end{aligned}$$
which tells us that
$$f^{-1}(y) = \frac{1}{3}(y^2 + 2) \tag{5}$$
Since we want $x$ to be the independent variable, we reverse $x$ and $y$ in (5) to produce the formula
$$f^{-1}(x) = \frac{1}{3}(x^2 + 2) \tag{6}$$
We know from (4) that the domain of $f^{-1}$ is the range of $f$. In general, this need not be the same as the natural domain of the formula for $f^{-1}$. Indeed, in this example the natural domain of (6) is $(-\infty, +\infty)$, whereas the range of $f(x) = \sqrt{3x - 2}$ is $[0, +\infty)$. Thus, if we want to make the domain of $f^{-1}$ clear, we must express it explicitly by rewriting (6) as
$$f^{-1}(x) = \frac{1}{3}(x^2 + 2), \quad x \ge 0$$

---

### EXISTENCE OF INVERSE FUNCTIONS

The procedure we gave above for finding the inverse of a function $f$ was based on solving the equation $y = f(x)$ for $x$ as a function of $y$. This procedure can fail for two reasons—the function $f$ may not have an inverse, or it may have an inverse but the equation $y = f(x)$ cannot be solved explicitly for $x$ as a function of $y$. Thus, it is important to establish conditions that ensure the existence of an inverse, even if it cannot be found explicitly.

If a function $f$ has an inverse, then it must assign distinct outputs to distinct inputs. For example, the function $f(x) = x^2$ cannot have an inverse because it assigns the same value to $x = 2$ and $x = -2$, namely,
$$f(2) = f(-2) = 4$$
Thus, if $f(x) = x^2$ were to have an inverse, then the equation $f(2) = 4$ would imply that $f^{-1}(4) = 2$, and the equation $f(-2) = 4$ would imply that $f^{-1}(4) = -2$. But this is impossible because $f^{-1}(4)$ cannot have two different values. Another way to see that $f(x) = x^2$ has no inverse is to attempt to find the inverse by solving the equation $y = x^2$ for $x$ as a function of $y$. We run into trouble immediately because the resulting equation $x = \pm\sqrt{y}$ does not express $x$ as a single function of $y$.

A function that assigns distinct outputs to distinct inputs is said to be **one-to-one** or **invertible**, so we know from the preceding discussion that if a function $f$ has an inverse, then it must be one-to-one. The converse is also true, thereby establishing the following theorem.

> **0.4.3 THEOREM**  
> A function has an inverse if and only if it is one-to-one.

Stated algebraically, a function $f$ is one-to-one if and only if $f(x_1) \neq f(x_2)$ whenever $x_1 \neq x_2$; stated geometrically, a function $f$ is one-to-one if and only if the graph of $y = f(x)$ is cut at most once by any horizontal line (Figure 0.4.3). The latter statement together with Theorem 0.4.3 provides the following geometric test for determining whether a function has an inverse.

> **0.4.4 THEOREM (The Horizontal Line Test)**  
> A function has an inverse function if and only if its graph is cut at most once by any horizontal line.

#### Example 5
Use the horizontal line test to show that $f(x) = x^2$ has no inverse but that $f(x) = x^3$ does.

**Solution.** Figure 0.4.4 shows a horizontal line that cuts the graph of $y = x^2$ more than once, so $f(x) = x^2$ is not invertible. Figure 0.4.5 shows that the graph of $y = x^3$ is cut at most once by any horizontal line, so $f(x) = x^3$ is invertible. [Recall from Example 2 that the inverse of $f(x) = x^3$ is $f^{-1}(x) = x^{1/3}$.]

#### Example 6
Explain why the function $f$ that is graphed in Figure 0.4.6 has an inverse, and find $f^{-1}(3)$.

**Solution.** The function $f$ has an inverse since its graph passes the horizontal line test. To evaluate $f^{-1}(3)$, we view $f^{-1}(3)$ as that number $x$ for which $f(x) = 3$. From the graph we see that $f(2) = 3$, so $f^{-1}(3) = 2$.

---

### INCREASING OR DECREASING FUNCTIONS ARE INVERTIBLE

A function whose graph is always rising as it is traversed from left to right is said to be an **increasing function**, and a function whose graph is always falling as it is traversed from left to right is said to be a **decreasing function**. If $x_1$ and $x_2$ are points in the domain of a function $f$, then $f$ is increasing if
$$f(x_1) < f(x_2) \quad \text{whenever } x_1 < x_2$$
and $f$ is decreasing if
$$f(x_1) > f(x_2) \quad \text{whenever } x_1 < x_2$$
(Figure 0.4.7). It is evident geometrically that increasing and decreasing functions pass the horizontal line test and hence are invertible.

---

### GRAPHS OF INVERSE FUNCTIONS

Our next objective is to explore the relationship between the graphs of $f$ and $f^{-1}$. For this purpose, it will be desirable to use $x$ as the independent variable for both functions so we can compare the graphs of $y = f(x)$ and $y = f^{-1}(x)$.

If $(a, b)$ is a point on the graph $y = f(x)$, then $b = f(a)$. This is equivalent to the statement that $a = f^{-1}(b)$, which means that $(b, a)$ is a point on the graph of $y = f^{-1}(x)$. In short, reversing the coordinates of a point on the graph of $f$ produces a point on the graph of $f^{-1}$. Similarly, reversing the coordinates of a point on the graph of $f^{-1}$ produces a point on the graph of $f$ (verify). However, the geometric effect of reversing the coordinates of a point is to reflect that point about the line $y = x$ (Figure 0.4.8), and hence the graphs of $y = f(x)$ and $y = f^{-1}(x)$ are reflections of one another about this line (Figure 0.4.9). In summary, we have the following result.

> **0.4.5 THEOREM**  
> If $f$ has an inverse, then the graphs of $y = f(x)$ and $y = f^{-1}(x)$ are reflections of one another about the line $y = x$; that is, each graph is the mirror image of the other with respect to that line.

#### Example 7
Figure 0.4.10 shows the graphs of the inverse functions discussed in Examples 2 and 4:
* $y = 2x$ and $y = \frac{1}{2}x$ reflected about $y = x$
* $y = x^3$ and $y = x^{1/3}$ reflected about $y = x$
* $y = \sqrt{3x - 2}$ and $y = \frac{1}{3}(x^2 + 2), \; x \ge 0$ reflected about $y = x$

---

### RESTRICTING DOMAINS FOR INVERTIBILITY

If a function $g$ is obtained from a function $f$ by placing restrictions on the domain of $f$, then $g$ is called a **restriction** of $f$. Thus, for example, the function
$$g(x) = x^3, \quad x \ge 0$$
is a restriction of the function $f(x) = x^3$. More precisely, it is called the restriction of $x^3$ to the interval $[0, +\infty)$.

Sometimes it is possible to create an invertible function from a function that is not invertible by restricting the domain appropriately. For example, we showed earlier that $f(x) = x^2$ is not invertible. However, consider the restricted functions
$$f_1(x) = x^2, \quad x \ge 0 \quad \text{and} \quad f_2(x) = x^2, \quad x \le 0$$
the union of whose graphs is the complete graph of $f(x) = x^2$ (Figure 0.4.11). These restricted functions are each one-to-one (hence invertible), since their graphs pass the horizontal line test. As illustrated in Figure 0.4.12, their inverses are
$$f_1^{-1}(x) = \sqrt{x} \quad \text{and} \quad f_2^{-1}(x) = -\sqrt{x}$$

---

### QUICK CHECK EXERCISES 0.4
*(See page 46 for answers.)*

1. In each part, determine whether the function $f$ is one-to-one.  
   (a) $f(t)$ is the number of people in line at a movie theater at time $t$.  
   (b) $f(x)$ is the measured high temperature (rounded to the nearest $^\circ\text{F}$) in a city on the $x\text{th}$ day of the year.  
   (c) $f(v)$ is the weight of $v$ cubic inches of lead.  

2. A student enters a number on a calculator, doubles it, adds 8 to the result, divides the sum by 2, subtracts 3 from the quotient, and then cubes the difference. If the resulting number is $x$, then $\underline{\hspace{2cm}}$ was the student's original number.  

3. If $(3, -2)$ is a point on the graph of an odd invertible function $f$, then $\underline{\hspace{2cm}}$ and $\underline{\hspace{2cm}}$ are points on the graph of $f^{-1}$.  

---

### EXERCISE SET 0.4

1. In (a)–(d), determine whether $f$ and $g$ are inverse functions.  
   (a) $f(x) = 4x, \quad g(x) = \frac{1}{4}x$  
   (b) $f(x) = 3x + 1, \quad g(x) = 3x - 1$  
   (c) $f(x) = \sqrt[3]{x - 2}, \quad g(x) = x^3 + 2$  
   (d) $f(x) = x^4, \quad g(x) = \sqrt[4]{x}$  

2. Check your answers to Exercise 1 with a graphing utility by determining whether the graphs of $f$ and $g$ are reflections of one another about the line $y = x$.  

3. In each part, use the horizontal line test to determine whether the function $f$ is one-to-one.  
   (a) $f(x) = 3x + 2$  
   (b) $f(x) = \sqrt{x - 1}$  
   (c) $f(x) = |x|$  
   (d) $f(x) = x^3$  
   (e) $f(x) = x^2 - 2x + 2$  
   (f) $f(x) = \sin x$  

4. In each part, generate the graph of the function $f$ with a graphing utility, and determine whether $f$ is one-to-one.  
   (a) $f(x) = x^3 - 3x + 2$  
   (b) $f(x) = x^3 - 3x^2 + 3x - 1$  

#### FOCUS ON CONCEPTS
5. In each part, determine whether the function $f$ defined by the table is one-to-one.  
   (a)
   | $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | $f(x)$ | -2 | -1 | 0 | 1 | 2 | 3 |
   (b)
   | $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | $f(x)$ | 4 | -7 | 6 | -3 | 1 | 4 |

6. A face of a broken clock lies in the $xy$-plane with the center of the clock at the origin and 3:00 in the direction of the positive $x$-axis. When the clock broke, the tip of the hour hand stopped on the graph of $y = f(x)$, where $f$ is a function that satisfies $f(0) = 0$.  
   (a) Are there any times of the day that cannot appear in such a configuration? Explain.  
   (b) How does your answer to part (a) change if $f$ must be an invertible function?  
   (c) How do your answers to parts (a) and (b) change if it was the tip of the minute hand that stopped on the graph of $f$?  

7. (a) Figure Ex-7 shows the graph of a function $f$ over its domain $-8 \le x \le 8$. Explain why $f$ has an inverse, and use the graph to find $f^{-1}(2)$, $f^{-1}(-1)$, and $f^{-1}(0)$.  
   (b) Find the domain and range of $f^{-1}$.  
   (c) Sketch the graph of $f^{-1}$.  

8. (a) Explain why the function $f$ graphed in Figure Ex-8 has no inverse function on its domain $-3 \le x \le 4$.  
   (b) Subdivide the domain into three adjacent intervals on each of which the function $f$ has an inverse.  

**9–16** Find a formula for $f^{-1}(x)$.  
9. $f(x) = 7x - 6$  
10. $f(x) = \frac{x + 1}{x - 1}$  
11. $f(x) = 3x^3 - 5$  
12. $f(x) = \sqrt[5]{4x + 2}$  
13. $f(x) = 3/x^2, \quad x < 0$  
14. $f(x) = 5/(x^2 + 1), \quad x \ge 0$  
15. $f(x) = \begin{cases} 5/2 - x, & x < 2 \\ 1/x, & x \ge 2 \end{cases}$  
16. $f(x) = \begin{cases} 2x, & x \le 0 \\ x^2, & x > 0 \end{cases}$  

**17–20** Find a formula for $f^{-1}(x)$, and state the domain of the function $f^{-1}$.  
17. $f(x) = (x + 2)^4, \quad x \ge 0$  
18. $f(x) = \sqrt{x + 3}$  
19. $f(x) = -\sqrt{3 - 2x}$  
20. $f(x) = x - 5x^2, \quad x \ge 1$  

**21–24 True–False** Determine whether the statement is true or false. Explain your answer.  
21. If $f$ is an invertible function such that $f(2) = 2$, then $f^{-1}(2) = \frac{1}{2}$.  
22. If $f$ and $g$ are inverse functions, then $f$ and $g$ have the same domain.  
23. A one-to-one function is invertible.  
24. If the graph of a function $f$ is symmetric about the line $y = x$, then $f$ is invertible.  

25. Let $f(x) = ax^2 + bx + c, \; a > 0$. Find $f^{-1}$ if the domain of $f$ is restricted to  
    (a) $x \ge -b/(2a)$  
    (b) $x \le -b/(2a)$.  

#### FOCUS ON CONCEPTS
26. The formula $F = \frac{9}{5}C + 32$, where $C \ge -273.15$, expresses the Fahrenheit temperature $F$ as a function of the Celsius temperature $C$.  
    (a) Find a formula for the inverse function.  
    (b) In words, what does the inverse function tell you?  
    (c) Find the domain and range of the inverse function.  

27. (a) One meter is about $6.214 \times 10^{-4}\text{ miles}$. Find a formula $y = f(x)$ that expresses a length $y$ in meters as a function of the same length $x$ in miles.  
    (b) Find a formula for the inverse of $f$.  
    (c) Describe what the formula $x = f^{-1}(y)$ tells you in practical terms.  

28. Let $f(x) = x^2, \; x > 1$, and $g(x) = \sqrt{x}$.  
    (a) Show that $f(g(x)) = x, \; x > 1$, and $g(f(x)) = x, \; x > 1$.  
    (b) Show that $f$ and $g$ are not inverses by showing that the graphs of $y = f(x)$ and $y = g(x)$ are not reflections of one another about $y = x$.  
    (c) Do parts (a) and (b) contradict one another? Explain.  

29. (a) Show that $f(x) = (3 - x)/(1 - x)$ is its own inverse.  
    (b) What does the result in part (a) tell you about the graph of $f$?  

30. Sketch the graph of a function that is one-to-one on $(-\infty, +\infty)$, yet not increasing on $(-\infty, +\infty)$ and not decreasing on $(-\infty, +\infty)$.  

31. Let $f(x) = 2x^3 + 5x + 3$. Find $x$ if $f^{-1}(x) = 1$.  

32. Let $f(x) = \frac{x^3}{x^2 + 1}$. Find $x$ if $f^{-1}(x) = 2$.  

33. Prove that if $a^2 + bc \neq 0$, then the graph of
    $$f(x) = \frac{ax + b}{cx - a}$$
    is symmetric about the line $y = x$.  

34. (a) Prove: If $f$ and $g$ are one-to-one, then so is the composition $f \circ g$.  
    (b) Prove: If $f$ and $g$ are one-to-one, then
    $$(f \circ g)^{-1} = g^{-1} \circ f^{-1}$$

35. Prove: A one-to-one function $f$ cannot have two different inverses.  

#### QUICK CHECK ANSWERS 0.4
1. (a) not one-to-one (b) not one-to-one (c) one-to-one  
2. $\sqrt[3]{x} - 1$  
3. $(-2, 3)$; $(2, -3)$  

---

## CHAPTER 0 REVIEW EXERCISES

1. Sketch the graph of the function
   $$f(x) = \begin{cases} -1, & x \le -5 \\ \sqrt{25 - x^2}, & -5 < x < 5 \\ x - 5, & x \ge 5 \end{cases}$$

2. Use the graphs of the functions $f$ and $g$ in Figure Ex-2 to solve the following problems.  
   (a) Find the values of $f(-2)$ and $g(3)$.  
   (b) For what values of $x$ is $f(x) = g(x)$?  
   (c) For what values of $x$ is $f(x) < 2$?  
   (d) What are the domain and range of $f$?  
   (e) What are the domain and range of $g$?  
   (f) Find the zeros of $f$ and $g$.  

3. A glass filled with water that has a temperature of $40^\circ\text{F}$ is placed in a room in which the temperature is a constant $70^\circ\text{F}$. Sketch a rough graph that reasonably describes the temperature of the water in the glass as a function of the elapsed time.  

4. You want to paint the top of a circular table. Find a formula that expresses the amount of paint required as a function of the radius, and discuss all of the assumptions you have made in finding the formula.  

5. A rectangular storage container with an open top and a square base has a volume of 8 cubic meters. Material for the base costs \$5 per square meter and material for the sides \$2 per square meter.  
   (a) Find a formula that expresses the total cost of materials as a function of the length of a side of the base.  
   (b) What is the domain of the cost function obtained in part (a)?  

6. A ball of radius 3 inches is coated uniformly with plastic.  
   (a) Express the volume of the plastic as a function of its thickness.  
   (b) What is the domain of the volume function obtained in part (a)?  

7. A box with a closed top is to be made from a 6 ft by 10 ft piece of cardboard by cutting out four squares of equal size (see Figure Ex-7), folding along the dashed lines, and tucking the two extra flaps inside.  
   (a) Find a formula that expresses the volume of the box as a function of the length of the sides of the cut-out squares.  
   (b) Find an inequality that specifies the domain of the function in part (a).  
   (c) Use the graph of the volume function to estimate the dimensions of the box of largest volume.  

8. Let $C$ denote the graph of $y = 1/x, \; x > 0$.  
   (a) Express the distance between the point $P(1, 0)$ and a point $Q$ on $C$ as a function of the $x$-coordinate of $Q$.  
   (b) What is the domain of the distance function obtained in part (a)?  
   (c) Use the graph of the distance function obtained in part (a) to estimate the point $Q$ on $C$ that is closest to the point $P$.  

9. Sketch the graph of the equation $x^2 - 4y^2 = 0$.  

10. Generate the graph of $f(x) = x^4 - 24x^3 - 25x^2$ in two different viewing windows, each of which illustrates a different property of $f$. Identify each viewing window and a characteristic of the graph of $f$ that is illustrated well in the window.  

11. Complete the following table (Table Ex-11).
   | $x$ | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | $f(x)$ | 0 | -1 | 2 | 1 | 3 | -2 | -3 | 4 | -4 |
   | $g(x)$ | 3 | 2 | 1 | -3 | -1 | -4 | 4 | -2 | 0 |
   | $(f \circ g)(x)$ | | | | | | | | | |
   | $(g \circ f)(x)$ | | | | | | | | | |

12. Let $f(x) = -x^2$ and $g(x) = 1/\sqrt{x}$. Find formulas for $f \circ g$ and $g \circ f$ and state the domain of each composition.  

13. Given that $f(x) = x^2 + 1$ and $g(x) = 3x + 2$, find all values of $x$ such that $f(g(x)) = g(f(x))$.  

14. Let $f(x) = (2x - 1)/(x + 1)$ and $g(x) = 1/(x - 1)$.  
    (a) Find $f(g(x))$.  
    (b) Is the natural domain of the function $h(x) = (3 - x)/x$ the same as the domain of $f \circ g$? Explain.  

15. Given that
    $$f(x) = \frac{x}{x - 1}, \quad g(x) = \frac{1}{x}, \quad h(x) = x^2 - 1$$
    find a formula for $f \circ g \circ h$ and state the domain of this composition.  

16. Given that $f(x) = 2x + 1$ and $h(x) = 2x^2 + 4x + 1$, find a function $g$ such that $f(g(x)) = h(x)$.  

17. In each part, classify the function as even, odd, or neither.  
    (a) $x^2 \sin x$  
    (b) $\sin^2 x$  
    (c) $x + x^2$  
    (d) $\sin x \tan x$  

18. (a) Write an equation for the graph that is obtained by reflecting the graph of $y = |x - 1|$ about the $y$-axis, then stretching that graph vertically by a factor of 2, then translating that graph down 3 units, and then reflecting that graph about the $x$-axis.  
    (b) Sketch the original graph and the final graph.  

19. In each part, describe the family of curves.  
    (a) $(x - a)^2 + (y - a^2)^2 = 1$  
    (b) $y = a + (x - 2a)^2$  

20. Find an equation for a parabola that passes through the points $(2, 0)$, $(8, 18)$, and $(-8, 18)$.  

21. Suppose that the expected low temperature in Anchorage, Alaska (in $^\circ\text{F}$), is modeled by the equation
    $$T = 50\sin\left[\frac{2\pi}{365}(t - 101)\right] + 25$$
    where $t$ is in days and $t = 0$ corresponds to January 1.  
    (a) Sketch the graph of $T$ versus $t$ for $0 \le t \le 365$.  
    (b) Use the model to predict when the coldest day of the year will occur.  
    (c) Based on this model, how many days during the year would you expect the temperature to be below $0^\circ\text{F}$?  

22. Figure Ex-22 shows a model for the tide variation in an inlet to San Francisco Bay during a 24-hour period. Find an equation of the form $y = y_0 + y_1 \sin(at + b)$ for the model, assuming that $t = 0$ corresponds to midnight.  

23. Figure Ex-23 shows the graphs of the equations $y = 1 + 2\sin x$ and $y = 2\sin(x/2) + 2\cos(x/2)$ for $-2\pi \le x \le 2\pi$. Without the aid of a calculator, label each curve by its equation, and find the coordinates of the points $A, B, C,$ and $D$. Explain your reasoning.  

24. The electrical resistance $R$ in ohms ($\Omega$) for a pure metal wire is related to its temperature $T$ in $^\circ\text{C}$ by the formula
    $$R = R_0(1 + kT)$$
    in which $R_0$ and $k$ are positive constants.  
    (a) Make a hand-drawn sketch of the graph of $R$ versus $T$, and explain the geometric significance of $R_0$ and $k$ for your graph.  
    (b) In theory, the resistance $R$ of a pure metal wire drops to zero when the temperature reaches absolute zero ($T = -273^\circ\text{C}$). What information does this give you about $k$?  
    (c) A tungsten bulb filament has a resistance of $1.1\,\Omega$ at a temperature of $20^\circ\text{C}$. What information does this give you about $R_0$ for the filament?  
    (d) At what temperature will the tungsten filament have a resistance of $1.5\,\Omega$?  

25. (a) State conditions under which two functions, $f$ and $g$, will be inverses, and give several examples of such functions.  
    (b) In words, what is the relationship between the graphs of $y = f(x)$ and $y = g(x)$ when $f$ and $g$ are inverse functions?  
    (c) What is the relationship between the domains and ranges of inverse functions $f$ and $g$?  
    (d) What condition must be satisfied for a function $f$ to have an inverse? Give some examples of functions that do not have inverses.  

26. Let $f(x) = (ax + b)/(cx + d)$. What conditions on $a, b, c,$ and $d$ guarantee that $f^{-1}$ exists? Find $f^{-1}(x)$.  

27. In each part, find $f^{-1}(x)$ if the inverse exists.  
    (a) $f(x) = 8x^3 - 1$  
    (b) $f(x) = x^2 - 2x + 1$  
    (c) $f(x) = 3/(x + 1)$  
    (d) $f(x) = (x + 2)/(x - 1)$  
