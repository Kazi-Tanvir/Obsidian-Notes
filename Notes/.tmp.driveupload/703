# CHAPTER 14: MULTIPLE INTEGRALS

> Finding the areas of complex surfaces such as those used in the design of the Denver International Airport require integration methods studied in this chapter.

In this chapter we will extend the concept of a definite integral to functions of two and three variables. Whereas functions of one variable are usually integrated over intervals, functions of two variables are usually integrated over regions in 2-space and functions of three variables over regions in 3-space. Calculating such integrals will require some new techniques that will be a central focus in this chapter. Once we have developed the basic methods for integrating functions of two and three variables, we will show how such integrals can be used to calculate surface areas and volumes of solids; and we will also show how they can be used to find masses and centers of gravity of flat plates and three-dimensional solids. In addition to our study of integration, we will generalize the concept of a parametric curve in 2-space to a parametric surface in 3-space. This will allow us to work with a wider variety of surfaces than previously possible and will provide a powerful tool for generating surfaces using computers and other graphing utilities.

---

## 14.1 DOUBLE INTEGRALS

The notion of a definite integral can be extended to functions of two or more variables. In this section we will discuss the double integral, which is the extension to functions of two variables.

### VOLUME

Recall that the definite integral of a function of one variable
$$\int_a^b f(x)\,dx = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n f(x_k^*)\,\Delta x_k = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*)\,\Delta x_k \tag{1}$$
arose from the problem of finding areas under curves. Integrals of functions of two variables arise from the problem of finding volumes under surfaces.

> **14.1.1 THE VOLUME PROBLEM**  
> Given a function $f$ of two variables that is continuous and nonnegative on a region $R$ in the $xy$-plane, find the volume of the solid enclosed between the surface $z = f(x, y)$ and the region $R$ (Figure 14.1.1).

The procedure for finding the volume $V$ of the solid will be similar to the limiting process used for finding areas, except that now the approximating elements will be rectangular parallelepipeds rather than rectangles:
* Using lines parallel to the coordinate axes, divide the rectangle enclosing the region $R$ into subrectangles, and exclude from consideration all those subrectangles that contain any points outside of $R$. This leaves only rectangles that are subsets of $R$ (Figure 14.1.2). Assume that there are $n$ such rectangles, and denote the area of the $k$th such rectangle by $\Delta A_k$.
* Choose any arbitrary point in each subrectangle, and denote the point in the $k$th subrectangle by $(x_k^*, y_k^*)$. As shown in Figure 14.1.3, the product $f(x_k^*, y_k^*)\Delta A_k$ is the volume of a rectangular parallelepiped with base area $\Delta A_k$ and height $f(x_k^*, y_k^*)$, so the sum
$$\sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta A_k$$
can be viewed as an approximation to the volume $V$ of the entire solid.
* There are two sources of error in the approximation: first, the parallelepipeds have flat tops, whereas the surface $z = f(x, y)$ may be curved; second, the rectangles that form the bases of the parallelepipeds may not completely cover the region $R$. However, if we repeat the above process with more and more subdivisions in such a way that both the lengths and the widths of the subrectangles approach zero, then it is plausible that the errors of both types approach zero, and the exact volume of the solid will be
$$V = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta A_k$$

> **14.1.2 DEFINITION (Volume Under a Surface)**  
> If $f$ is a function of two variables that is continuous and nonnegative on a region $R$ in the $xy$-plane, then the volume of the solid enclosed between the surface $z = f(x, y)$ and the region $R$ is defined by
> $$V = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta A_k \tag{2}$$
> Here, $n \to +\infty$ indicates the process of increasing the number of subrectangles of the rectangle enclosing $R$ in such a way that both the lengths and the widths of the subrectangles approach zero.

If $f$ is continuous on $R$ and has both positive and negative values, then the limit
$$\lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta A_k \tag{3}$$
represents the **net signed volume** between the region $R$ and the surface $z = f(x, y)$.

---

### DEFINITION OF A DOUBLE INTEGRAL

> **14.1.4 DEFINITION**  
> The **double integral** of $f(x, y)$ over $R$ is
> $$\iint_R f(x, y)\,dA = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta A_k \tag{4}$$
> If $f$ is continuous and nonnegative on the region $R$, then the volume formula in (2) can be expressed as
> $$V = \iint_R f(x, y)\,dA \tag{5}$$

---

### EVALUATING DOUBLE INTEGRALS & FUBINI'S THEOREM

Partial definite integrals:
$$\int_a^b f(x, y)\,dx \quad \text{and} \quad \int_c^d f(x, y)\,dy$$
Iterated integrals:
$$\int_c^d \int_a^b f(x, y)\,dx\,dy = \int_c^d \left[\int_a^b f(x, y)\,dx\right]dy \tag{6}$$
$$\int_a^b \int_c^d f(x, y)\,dy\,dx = \int_a^b \left[\int_c^d f(x, y)\,dy\right]dx \tag{7}$$

#### Example 1
$$\int_0^1 xy^2\,dx = y^2 \int_0^1 x\,dx = y^2 \left[\frac{x^2}{2}\right]_{x=0}^1 = \frac{y^2}{2}$$
$$\int_0^1 xy^2\,dy = x \int_0^1 y^2\,dy = x \left[\frac{y^3}{3}\right]_{y=0}^1 = \frac{x}{3}$$

#### Example 2
Evaluate:  
(a) $\int_1^3 \int_2^4 (40 - 2xy)\,dy\,dx = \int_1^3 [40y - xy^2]_{y=2}^4\,dx = \int_1^3 (80 - 12x)\,dx = [80x - 6x^2]_1^3 = 112$.  
(b) $\int_2^4 \int_1^3 (40 - 2xy)\,dx\,dy = \int_2^4 [40x - x^2 y]_{x=1}^3\,dy = \int_2^4 (80 - 8y)\,dy = [80y - 4y^2]_2^4 = 112$.

> **14.1.3 THEOREM (Fubini's Theorem)**  
> Let $R$ be the rectangle defined by the inequalities $a \le x \le b, \; c \le y \le d$. If $f(x, y)$ is continuous on this rectangle, then
> $$\iint_R f(x, y)\,dA = \int_c^d \int_a^b f(x, y)\,dx\,dy = \int_a^b \int_c^d f(x, y)\,dy\,dx$$

> **Guido Fubini (1879–1943):** Italian mathematician. Fubini, the son of a mathematician, showed brilliance in mathematics as a young pupil in Venice. He entered college at the Scuola Normale Superiore di Pisa in 1896 and presented his doctoral thesis on the subject of elliptic geometry in 1900 at the young age of 20. He held teaching positions at various universities, finally settling at the University of Turin. In 1939, he accepted a position at Princeton University, where he stayed until his death four years later.

#### Example 3
Use a double integral to find the volume of the solid that is bounded above by the plane $z = 4 - x - y$ and below by the rectangle $R = [0, 1] \times [0, 2]$ (Figure 14.1.6).

**Solution.**
$$V = \iint_R (4 - x - y)\,dA = \int_0^2 \int_0^1 (4 - x - y)\,dx\,dy = \int_0^2 \left[4x - \frac{x^2}{2} - xy\right]_{x=0}^1 dy = \int_0^2 \left(\frac{7}{2} - y\right)dy = \left[\frac{7}{2}y - \frac{y^2}{2}\right]_0^2 = 5$$

#### Example 4
Evaluate the double integral $\iint_R y^2 x\,dA$ over the rectangle $R = \{(x, y) : -3 \le x \le 2, 0 \le y \le 1\}$.

**Solution.**
$$\iint_R y^2 x\,dA = \int_0^1 \int_{-3}^2 y^2 x\,dx\,dy = \int_0^1 \left[\frac{1}{2}y^2 x^2\right]_{x=-3}^2 dy = \int_0^1 \left(-\frac{5}{2}y^2\right)dy = \left[-\frac{5}{6}y^3\right]_0^1 = -\frac{5}{6}$$

---

### PROPERTIES OF DOUBLE INTEGRALS

* $\iint_R c f(x, y)\,dA = c \iint_R f(x, y)\,dA \quad (c \text{ a constant}) \tag{9}$
* $\iint_R [f(x, y) + g(x, y)]\,dA = \iint_R f(x, y)\,dA + \iint_R g(x, y)\,dA \tag{10}$
* $\iint_R [f(x, y) - g(x, y)]\,dA = \iint_R f(x, y)\,dA - \iint_R g(x, y)\,dA \tag{11}$
* $\iint_R f(x, y)\,dA = \iint_{R_1} f(x, y)\,dA + \iint_{R_2} f(x, y)\,dA \tag{12}$

---

### QUICK CHECK EXERCISES 14.1
*(See page 1008 for answers.)*

1. The double integral is defined as a limit of Riemann sums by $\iint_R f(x, y)\,dA = \underline{\quad}$.
2. The iterated integral $\int_1^5 \int_2^4 f(x, y)\,dx\,dy$ integrates $f$ over the rectangle defined by $\underline{\quad} \le x \le \underline{\quad}, \; \underline{\quad} \le y \le \underline{\quad}$.
3. Supply the missing integrand and limits of integration:
   $$\int_1^5 \int_2^4 (3x^2 - 2xy + y^2)\,dx\,dy = \int_{\square}^{\square} \underline{\quad}\,dy$$
4. The volume of the solid enclosed by the surface $z = x/y$ and the rectangle $0 \le x \le 4, 1 \le y \le e^2$ in the $xy$-plane is $\underline{\quad}$.

---

### EXERCISE SET 14.1

**1–12 Evaluate the iterated integrals.**
1. $\int_0^1 \int_0^2 (x + 3)\,dy\,dx$
2. $\int_1^3 \int_{-1}^1 (2x - 4y)\,dy\,dx$
3. $\int_2^4 \int_0^1 x^2 y\,dx\,dy$
4. $\int_{-2}^0 \int_{-1}^2 (x^2 + y^2)\,dx\,dy$
5. $\int_0^{\ln 3} \int_0^{\ln 2} e^{x+y}\,dy\,dx$
6. $\int_0^2 \int_0^1 y\sin x\,dy\,dx$
7. $\int_{-1}^0 \int_2^5 dx\,dy$
8. $\int_4^6 \int_{-3}^7 dy\,dx$
9. $\int_0^1 \int_0^1 \frac{x}{(xy+1)^2}\,dy\,dx$
10. $\int_{\pi/2}^\pi \int_1^2 x\cos xy\,dy\,dx$
11. $\int_0^{\ln 2} \int_0^1 x y e^{y^2 x}\,dy\,dx$
12. $\int_3^4 \int_1^2 \frac{1}{(x+y)^2}\,dy\,dx$

**13–16 Evaluate the double integral over the rectangular region $R$.**
13. $\iint_R 4xy^3\,dA; \quad R = \{(x, y) : -1 \le x \le 1, -2 \le y \le 2\}$
14. $\iint_R \frac{xy}{\sqrt{x^2+y^2+1}}\,dA; \quad R = \{(x, y) : 0 \le x \le 1, 0 \le y \le 1\}$
15. $\iint_R x\sqrt{1-x^2}\,dA; \quad R = \{(x, y) : 0 \le x \le 1, 2 \le y \le 3\}$
16. $\iint_R (x\sin y - y\sin x)\,dA; \quad R = \{(x, y) : 0 \le x \le \pi/2, 0 \le y \le \pi/3\}$

#### FOCUS ON CONCEPTS
17. (a) Let $f(x, y) = x^2 + y$, and as shown in the accompanying figure, let the rectangle $R = [0, 2] \times [0, 2]$ be subdivided into 16 subrectangles. Take $(x_k^*, y_k^*)$ to be the center of the $k$th rectangle, and approximate the double integral of $f$ over $R$ by the resulting Riemann sum.  
    (b) Compare the result in part (a) to the exact value of the integral.
18. (a) Let $f(x, y) = x - 2y$, and as shown in Exercise 17, let the rectangle $R = [0, 2] \times [0, 2]$ be subdivided into 16 subrectangles. Take $(x_k^*, y_k^*)$ to be the center of the $k$th rectangle, and approximate the double integral of $f$ over $R$ by the resulting Riemann sum.  
    (b) Compare the result in part (a) to the exact value of the integral.

**19–20 Each iterated integral represents the volume of a solid. Make a sketch of the solid. Use geometry to find the volume of the solid, and then evaluate the iterated integral.**
19. $\int_0^5 \int_1^2 4\,dx\,dy$
20. $\int_0^1 \int_0^1 (2 - x - y)\,dx\,dy$

**21–22 Each iterated integral represents the volume of a solid. Make a sketch of the solid. (You do not have to find the volume.)**
21. $\int_0^3 \int_0^4 \sqrt{25 - x^2 - y^2}\,dy\,dx$
22. $\int_{-2}^2 \int_{-2}^2 (x^2 + y^2)\,dx\,dy$

**23–26 True–False Determine whether the statement is true or false. Explain your answer.**
23. In the definition of a double integral $\iint_R f(x, y)\,dA = \lim_{n \to +\infty}\sum_{k=1}^n f(x_k^*, y_k^*)\Delta A_k$, the symbol $\Delta A_k$ represents a rectangular region within $R$ from which the point $(x_k^*, y_k^*)$ is taken.
24. If $R$ is the rectangle $\{(x, y) : 1 \le x \le 4, 0 \le y \le 3\}$ and $\int_0^3 f(x, y)\,dy = 2x$, then $\iint_R f(x, y)\,dA = 15$.
25. If $R$ is the rectangle $\{(x, y) : 1 \le x \le 5, 2 \le y \le 4\}$, then $\iint_R f(x, y)\,dA = \int_1^5 \int_2^4 f(x, y)\,dx\,dy$.
26. Suppose that for some region $R$ in the $xy$-plane $\iint_R f(x, y)\,dA = 0$. If $R$ is subdivided into two regions $R_1$ and $R_2$, then $\iint_{R_1} f(x, y)\,dA = -\iint_{R_2} f(x, y)\,dA$.

27. In this exercise, suppose that $f(x, y) = g(x)h(y)$ and $R = \{(x, y) : a \le x \le b, c \le y \le d\}$. Show that
    $$\iint_R f(x, y)\,dA = \left[\int_a^b g(x)\,dx\right]\left[\int_c^d h(y)\,dy\right]$$
28. Use the result in Exercise 27 to evaluate the integral $\int_0^{\ln 2} \int_{-1}^1 \sqrt{e^y + 1}\tan x\,dx\,dy$ by inspection. Explain your reasoning.

**29–32 Use a double integral to find the volume.**
29. The volume under the plane $z = 2x + y$ and over the rectangle $R = \{(x, y) : 3 \le x \le 5, 1 \le y \le 2\}$.
30. The volume under the surface $z = 3x^3 + 3x^2y$ and over the rectangle $R = \{(x, y) : 1 \le x \le 3, 0 \le y \le 2\}$.
31. The volume of the solid enclosed by the surface $z = x^2$ and the planes $x = 0, x = 2, y = 3, y = 0,$ and $z = 0$.
32. The volume in the first octant bounded by the coordinate planes, the plane $y = 4$, and the plane $(x/3) + (z/5) = 1$.
33. Evaluate the integral by choosing a convenient order of integration: $\iint_R x\cos(xy)\cos^2\pi x\,dA; \quad R = [0, 1/2] \times [0, \pi]$.
34. (a) Sketch the solid in the first octant that is enclosed by the planes $x = 0, z = 0, x = 5, z - y = 0,$ and $z = -2y + 6$.  
    (b) Find the volume of the solid by breaking it into two parts.

**35–40 The average value or mean value of a continuous function $f(x, y)$ over a rectangle $R = [a, b] \times [c, d]$ is defined as $f_{\text{ave}} = \frac{1}{A(R)}\iint_R f(x, y)\,dA$, where $A(R) = (b - a)(d - c)$ is the area of the rectangle $R$. Use this definition in these exercises.**
35. Find the average value of $f(x, y) = xy^2$ over the rectangle $[0, 8] \times [0, 6]$.
36. Find the average value of $f(x, y) = x^2 + 7y$ over the rectangle $[0, 3] \times [0, 6]$.
37. Find the average value of $f(x, y) = y\sin xy$ over the rectangle $[0, 1] \times [0, \pi/2]$.
38. Find the average value of $f(x, y) = x(x^2 + y)^{1/2}$ over the rectangle $[0, 1] \times [0, 3]$.
39. Suppose that the temperature in degrees Celsius at a point $(x, y)$ on a flat metal plate is $T(x, y) = 10 - 8x^2 - 2y^2$, where $x$ and $y$ are in meters. Find the average temperature of the rectangular portion of the plate for which $0 \le x \le 1$ and $0 \le y \le 2$.
40. Show that if $f(x, y)$ is constant on the rectangle $R = [a, b] \times [c, d]$, say $f(x, y) = k$, then $f_{\text{ave}} = k$ over $R$.

41. [CAS] Find a numerical approximation of $\int_0^2 \int_0^1 \sin\sqrt{x^3 + y^3}\,dx\,dy$.
42. [CAS] Find a numerical approximation of $\int_{-1}^1 \int_{-1}^1 e^{-(x^2+y^2)}\,dx\,dy$.
43. [CAS] Use a CAS to evaluate the iterated integrals $\int_0^1 \int_0^1 \frac{y-x}{(x+y)^3}\,dx\,dy$ and $\int_0^1 \int_0^1 \frac{y-x}{(x+y)^3}\,dy\,dx$. Does this contradict Theorem 14.1.3? Explain.
44. [CAS] Use a CAS to show that the volume $V$ under the surface $z = xy^3\sin xy$ over the rectangle $0 \le x \le \pi, 0 \le y \le 1$ is $V = 3/\pi$.
45. **Writing.** Discuss how computing a volume using an iterated double integral corresponds to the method of computing a volume by slicing (Section 5.2).
46. **Writing.** Discuss how the double integral property given in Formula (12) generalizes the single integral property in Theorem 4.5.5.

#### QUICK CHECK ANSWERS 14.1
1. $\lim_{n \to +\infty}\sum_{k=1}^n f(x_k^*, y_k^*)\Delta A_k$  
2. $2 \le x \le 4, \; 1 \le y \le 5$  
3. $\int_1^5 (56 - 12y + 2y^2)\,dy$  
4. 16

---

## 14.2 DOUBLE INTEGRALS OVER NONRECTANGULAR REGIONS

### ITERATED INTEGRALS WITH NONCONSTANT LIMITS OF INTEGRATION

$$\int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\,dx = \int_a^b \left[\int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\right]dx \tag{1}$$
$$\int_c^d \int_{h_1(y)}^{h_2(y)} f(x, y)\,dx\,dy = \int_c^d \left[\int_{h_1(y)}^{h_2(y)} f(x, y)\,dx\right]dy \tag{2}$$

#### Example 1
Evaluate:  
(a) $\int_0^1 \int_{-x}^{x^2} y^2 x\,dy\,dx = \int_0^1 \left[\frac{y^3 x}{3}\right]_{y=-x}^{x^2} dx = \int_0^1 \left(\frac{x^7}{3} + \frac{x^4}{3}\right)dx = \left[\frac{x^8}{24} + \frac{x^5}{15}\right]_0^1 = \frac{13}{120}$.  
(b) $\int_0^{\pi/3} \int_0^{\cos y} x\sin y\,dx\,dy = \int_0^{\pi/3} \left[\frac{x^2}{2}\sin y\right]_{x=0}^{\cos y} dy = \int_0^{\pi/3} \frac{1}{2}\cos^2 y\sin y\,dy = \left[-\frac{1}{6}\cos^3 y\right]_0^{\pi/3} = \frac{7}{48}$.

---

### DOUBLE INTEGRALS OVER NONRECTANGULAR REGIONS

> **14.2.1 DEFINITION**  
> (a) A **type I region** is bounded on the left and right by vertical lines $x = a$ and $x = b$ and is bounded below and above by continuous curves $y = g_1(x)$ and $y = g_2(x)$, where $g_1(x) \le g_2(x)$ for $a \le x \le b$ (Figure 14.2.1a).  
> (b) A **type II region** is bounded below and above by horizontal lines $y = c$ and $y = d$ and is bounded on the left and right by continuous curves $x = h_1(y)$ and $x = h_2(y)$ satisfying $h_1(y) \le h_2(y)$ for $c \le y \le d$ (Figure 14.2.1b).

> **14.2.2 THEOREM**  
> (a) If $R$ is a type I region on which $f(x, y)$ is continuous, then
> $$\iint_R f(x, y)\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\,dx \tag{3}$$
> (b) If $R$ is a type II region on which $f(x, y)$ is continuous, then
> $$\iint_R f(x, y)\,dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x, y)\,dx\,dy \tag{4}$$

#### Example 2
Each of the iterated integrals in Example 1 is equal to a double integral over a region $R$. Identify the region $R$ in each case.

**Solution.** In Example 1(a), $R$ is the type I region bounded by $x = 0, x = 1, y = -x, y = x^2$. In Example 1(b), $R$ is the type II region bounded by $y = 0, y = \pi/3, x = 0, x = \cos y$.

#### Example 3
Evaluate $\iint_R xy\,dA$ over the region $R$ enclosed between $y = \frac{1}{2}x, y = \sqrt{x}, x = 2,$ and $x = 4$.

**Solution.** Treating $R$ as a type I region:
$$\iint_R xy\,dA = \int_2^4 \int_{x/2}^{\sqrt{x}} xy\,dy\,dx = \int_2^4 \left[\frac{xy^2}{2}\right]_{y=x/2}^{\sqrt{x}} dx = \int_2^4 \left(\frac{x^2}{2} - \frac{x^3}{8}\right)dx = \left[\frac{x^3}{6} - \frac{x^4}{32}\right]_2^4 = \frac{11}{6}$$

#### Example 4
Evaluate $\iint_R (2x - y^2)\,dA$ over the triangular region $R$ enclosed between the lines $y = -x + 1, y = x + 1,$ and $y = 3$.

**Solution.** Treating $R$ as a type II region ($x = 1 - y$ to $x = y - 1, 1 \le y \le 3$):
$$\iint_R (2x - y^2)\,dA = \int_1^3 \int_{1-y}^{y-1} (2x - y^2)\,dx\,dy = \int_1^3 [x^2 - y^2 x]_{x=1-y}^{y-1} dy = \int_1^3 (2y^2 - 2y^3)\,dy = \left[\frac{2y^3}{3} - \frac{y^4}{2}\right]_1^3 = -\frac{68}{3}$$

#### Example 5
Use a double integral to find the volume of the tetrahedron bounded by the coordinate planes and the plane $z = 4 - 4x - 2y$.

**Solution.**
$$V = \iint_R (4 - 4x - 2y)\,dA = \int_0^1 \int_0^{2-2x} (4 - 4x - 2y)\,dy\,dx = \int_0^1 (4 - 8x + 4x^2)\,dx = \frac{4}{3}$$

#### Example 6
Find the volume of the solid bounded by the cylinder $x^2 + y^2 = 4$ and the planes $y + z = 4$ and $z = 0$.

**Solution.**
$$V = \iint_R (4 - y)\,dA = \int_{-2}^2 \int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}} (4 - y)\,dy\,dx = \int_{-2}^2 8\sqrt{4 - x^2}\,dx = 8(2\pi) = 16\pi$$

---

### REVERSING THE ORDER OF INTEGRATION

#### Example 7
Evaluate $\int_0^2 \int_{y/2}^1 e^{x^2}\,dx\,dy$ by reversing the order of integration.

**Solution.** Region $R: y/2 \le x \le 1, 0 \le y \le 2 \implies 0 \le y \le 2x, 0 \le x \le 1$.
$$\int_0^2 \int_{y/2}^1 e^{x^2}\,dx\,dy = \int_0^1 \int_0^{2x} e^{x^2}\,dy\,dx = \int_0^1 2x e^{x^2}\,dx = [e^{x^2}]_0^1 = e - 1$$

---

### AREA CALCULATED AS A DOUBLE INTEGRAL

$$\text{area of } R = \iint_R 1\,dA = \iint_R dA \tag{7}$$

#### Example 8
Use a double integral to find the area of the region $R$ enclosed between the parabola $y = \frac{1}{2}x^2$ and the line $y = 2x$.

**Solution.**
$$\text{area of } R = \int_0^4 \int_{x^2/2}^{2x} dy\,dx = \int_0^4 \left(2x - \frac{1}{2}x^2\right)dx = \left[x^2 - \frac{x^3}{6}\right]_0^4 = \frac{16}{3}$$

---

### QUICK CHECK EXERCISES 14.2
*(See page 1018 for answers.)*

1. Supply the missing integrand and limits of integration:  
   (a) $\int_1^5 \int_2^{y/2} 6x^2 y\,dx\,dy = \int_{\square}^{\square} \underline{\quad}\,dy$  
   (b) $\int_1^5 \int_2^{x/2} 6x^2 y\,dy\,dx = \int_{\square}^{\square} \underline{\quad}\,dx$.
2. Let $R$ be the triangular region in the $xy$-plane with vertices $(0, 0), (3, 0),$ and $(0, 4)$. Supply the missing portions of the integrals:  
   (a) Treating $R$ as a type I region: $\iint_R f(x, y)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,\underline{\quad}$.  
   (b) Treating $R$ as a type II region: $\iint_R f(x, y)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,\underline{\quad}$.
3. Let $R$ be the triangular region in the $xy$-plane with vertices $(0, 0), (3, 3),$ and $(0, 4)$. Expressed as an iterated double integral, the area of $R$ is $A(R) = \underline{\quad}$.
4. The line $y = 2 - x$ and the parabola $y = x^2$ intersect at the points $(-2, 4)$ and $(1, 1)$. If $R$ is the region enclosed by $y = 2 - x$ and $y = x^2$, then $\iint_R (1 + 2y)\,dA = \underline{\quad}$.

---

### EXERCISE SET 14.2

**1–8 Evaluate the iterated integral.**
1. $\int_0^1 \int_{x^2}^x xy^2\,dy\,dx$
2. $\int_1^{3/2} \int_y^{3-y} y\,dx\,dy$
3. $\int_0^3 \int_0^{\sqrt{9-y^2}} y\,dx\,dy$
4. $\int_{1/4}^1 \int_{x^2}^x \sqrt{\frac{x}{y}}\,dy\,dx$
5. $\int_{\sqrt{\pi}}^{\sqrt{2\pi}} \int_0^{x^3} \sin(y/x)\,dy\,dx$
6. $\int_{-1}^1 \int_{-x^2}^{x^2} (x^2 - y)\,dy\,dx$
7. $\int_0^1 \int_0^x y\sqrt{x^2 - y^2}\,dy\,dx$
8. $\int_1^2 \int_0^{y^2} e^{x/y^2}\,dx\,dy$

#### FOCUS ON CONCEPTS
9. Let $R$ be the region shown in Figure Ex-9 (bounded by $y = x^2$ and $y = 2$). Fill in the missing limits of integration:  
   (a) $\iint_R f(x, y)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,dy\,dx$  
   (b) $\iint_R f(x, y)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,dx\,dy$.
10. Let $R$ be the region shown in Figure Ex-10 (bounded by $y = x^2$ and $y = \sqrt{x}$). Fill in the missing limits of integration:  
    (a) $\iint_R f(x, y)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,dy\,dx$  
    (b) $\iint_R f(x, y)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,dx\,dy$.
11. Let $R$ be the region shown in Figure Ex-11 (trapezoid with vertices $(1, 3), (2, 1), (4, 1), (5, 3)$). Fill in the missing limits of integration:  
    (a) $\iint_R f(x, y)\,dA = \int_1^2 \int_{\square}^{\square} f(x, y)\,dy\,dx + \int_2^4 \int_{\square}^{\square} f(x, y)\,dy\,dx + \int_4^5 \int_{\square}^{\square} f(x, y)\,dy\,dx$  
    (b) $\iint_R f(x, y)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,dx\,dy$.
12. Let $R$ be the circular region shown in Figure Ex-12 ($x^2 + y^2 \le 1$). Fill in the missing limits of integration:  
    (a) $\iint_R f(x, y)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,dy\,dx$  
    (b) $\iint_R f(x, y)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,dx\,dy$.
13. Evaluate $\iint_R xy\,dA$, where $R$ is the region in (a) Exercise 9 (b) Exercise 11.
14. Evaluate $\iint_R (x + y)\,dA$, where $R$ is the region in (a) Exercise 10 (b) Exercise 12.

**15–18 Evaluate the double integral in two ways using iterated integrals: (a) viewing $R$ as a type I region, and (b) viewing $R$ as a type II region.**
15. $\iint_R x^2\,dA; \quad R$ is the region bounded by $y = 16/x, y = x,$ and $x = 8$.
16. $\iint_R xy^2\,dA; \quad R$ is the region enclosed by $y = 1, y = 2, x = 0,$ and $y = x$.
17. $\iint_R (3x - 2y)\,dA; \quad R$ is the region enclosed by the circle $x^2 + y^2 = 1$.
18. $\iint_R y\,dA; \quad R$ is the region in the first quadrant enclosed between the circle $x^2 + y^2 = 25$ and the line $x + y = 5$.

**19–24 Evaluate the double integral.**
19. $\iint_R x(1 + y^2)^{-1/2}\,dA; \quad R$ is the region in the first quadrant enclosed by $y = x^2, y = 4,$ and $x = 0$.
20. $\iint_R x\cos y\,dA; \quad R$ is the triangular region bounded by the lines $y = x, y = 0,$ and $x = \pi$.
21. $\iint_R xy\,dA; \quad R$ is the region enclosed by $y = \sqrt{x}, y = 6 - x,$ and $y = 0$.
22. $\iint_R x\,dA; \quad R$ is the region enclosed by $y = \sin^{-1} x, x = 1/\sqrt{2},$ and $y = 0$.
23. $\iint_R (x - 1)\,dA; \quad R$ is the region in the first quadrant enclosed between $y = x$ and $y = x^3$.
24. $\iint_R x^2\,dA; \quad R$ is the region in the first quadrant enclosed by $xy = 1, y = x,$ and $y = 2x$.
25. Evaluate $\iint_R \sin(y^3)\,dA$, where $R$ is the region bounded by $y = \sqrt{x}, y = 2,$ and $x = 0$. [Hint: Choose the order of integration carefully.]
26. Evaluate $\iint_R x\,dA$, where $R$ is the region bounded by $x = \ln y, x = 0,$ and $y = e$.
27. (a) By hand or with the help of a graphing utility, make a sketch of the region $R$ enclosed between the curves $y = x + 2$ and $y = e^x$.  
    (b) Estimate the intersections of the curves in part (a).  
    (c) Viewing $R$ as a type I region, estimate $\iint_R x\,dA$.  
    (d) Viewing $R$ as a type II region, estimate $\iint_R x\,dA$.
28. (a) By hand or with the help of a graphing utility, make a sketch of the region $R$ enclosed between the curves $y = 4x^3 - x^4$ and $y = 3 - 4x + 4x^2$.  
    (b) Find the intersections of the curves in part (a).  
    (c) Find $\iint_R x\,dA$.

**29–32 Use double integration to find the area of the plane region enclosed by the given curves.**
29. $y = \sin x$ and $y = \cos x$, for $0 \le x \le \pi/4$.
30. $y^2 = -x$ and $3y - x = 4$.
31. $y^2 = 9 - x$ and $y^2 = 9 - 9x$.
32. $y = \cosh x, y = \sinh x, x = 0,$ and $x = 1$.

**33–36 True–False Determine whether the statement is true or false. Explain your answer.**
33. $\int_0^1 \int_{x^2}^{2x} f(x, y)\,dy\,dx = \int_{x^2}^{2x} \int_0^1 f(x, y)\,dx\,dy$.
34. If a region $R$ is bounded below by $y = g_1(x)$ and above by $y = g_2(x)$ for $a \le x \le b$, then $\iint_R f(x, y)\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\,dx$.
35. If $R$ is the region in the $xy$-plane enclosed by $y = x^2$ and $y = 1$, then $\iint_R f(x, y)\,dA = 2\int_0^1 \int_{x^2}^1 f(x, y)\,dy\,dx$.
36. The area of a region $R$ in the $xy$-plane is given by $\iint_R xy\,dA$.

**37–38 Use double integration to find the volume of the solid.**
37. Solid bounded by plane $3x + 2y + 4z = 12$ in the first octant.
38. Solid bounded by cylinder $x^2 + y^2 = 4$ and cylinder $x^2 + z^2 = 4$.

**39–44 Use double integration to find the volume of each solid.**
39. The solid bounded by the cylinder $x^2 + y^2 = 9$ and the planes $z = 0$ and $z = 3 - x$.
40. The solid in the first octant bounded above by the paraboloid $z = x^2 + 3y^2$, below by the plane $z = 0$, and laterally by $y = x^2$ and $y = x$.
41. The solid bounded above by the paraboloid $z = 9x^2 + y^2$, below by the plane $z = 0$, and laterally by the planes $x = 0, y = 0, x = 3,$ and $y = 2$.
42. The solid enclosed by $y^2 = x, z = 0,$ and $x + z = 1$.
43. The wedge cut from the cylinder $4x^2 + y^2 = 9$ by the planes $z = 0$ and $z = y + 3$.
44. The solid in the first octant bounded above by $z = 9 - x^2$, below by $z = 0$, and laterally by $y^2 = 3x$.

45. [CAS] Use a double integral and a CAS to find the volume of the solid bounded above by the paraboloid $z = 1 - x^2 - y^2$ and below by the $xy$-plane.
46. [CAS] Use a double integral and a CAS to find the volume of the solid in the first octant bounded by $z = x^2 + y^2$, cylinder $x^2 + y^2 = 4$, and coordinate planes.

**47–52 Express the integral as an equivalent integral with the order of integration reversed.**
47. $\int_0^2 \int_0^{\sqrt{x}} f(x, y)\,dy\,dx$
48. $\int_0^4 \int_{2y}^8 f(x, y)\,dx\,dy$
49. $\int_0^2 \int_1^{e^y} f(x, y)\,dx\,dy$
50. $\int_1^e \int_0^{\ln x} f(x, y)\,dy\,dx$
51. $\int_0^1 \int_{\sin^{-1} y}^{\pi/2} f(x, y)\,dx\,dy$
52. $\int_0^1 \int_{y^2}^{\sqrt{y}} f(x, y)\,dx\,dy$

**53–56 Evaluate the integral by first reversing the order of integration.**
53. $\int_0^1 \int_{4x}^4 e^{-y^2}\,dy\,dx$
54. $\int_0^2 \int_{y/2}^1 \cos(x^2)\,dx\,dy$
55. $\int_0^4 \int_{\sqrt{y}}^2 e^{x^3}\,dx\,dy$
56. $\int_1^3 \int_0^{\ln x} x\,dy\,dx$

57. [CAS] Try to evaluate the integral with a CAS using the stated order of integration, and then by reversing the order of integration:  
    (a) $\int_0^4 \int_{\sqrt{x}}^2 \sin\pi y^3\,dy\,dx$  
    (b) $\int_0^1 \int_{\sin^{-1} y}^{\pi/2} \sec^2(\cos x)\,dx\,dy$.
58. Use the appropriate Wallis formula to find the volume of the solid enclosed between $z = x^2 + y^2$, the cylinder $x^2 + y^2 = 4$, and the $xy$-plane.
59. Evaluate $\iint_R xy^2\,dA$ over the region $R$ shown in Figure Ex-59 (step region with $-2 \le x \le 2$).
60. Give a geometric argument to show that $\int_0^1 \int_0^{\sqrt{1-y^2}} \sqrt{1 - x^2 - y^2}\,dx\,dy = \frac{\pi}{6}$.

**61–62 The average value or mean value of a continuous function $f(x, y)$ over a region $R$ in the $xy$-plane is defined as $f_{\text{ave}} = \frac{1}{A(R)}\iint_R f(x, y)\,dA$. Use this definition in these exercises.**
61. Find the average value of $1/(1 + x^2)$ over the triangular region with vertices $(0, 0), (1, 1),$ and $(0, 1)$.
62. Find the average value of $f(x, y) = x^2 - xy$ over the region enclosed by $y = x$ and $y = 3x - x^2$.
63. Suppose that the temperature in degrees Celsius at a point $(x, y)$ on a flat metal plate is $T(x, y) = 5xy + x^2$, where $x$ and $y$ are in meters. Find the average temperature of the diamond-shaped portion of the plate for which $|2x + y| \le 4$ and $|2x - y| \le 4$.
64. A circular lens of radius 2 inches has thickness $1 - (r^2/4)$ inches at all points $r$ inches from the center of the lens. Find the average thickness of the lens.
65. [CAS] Use a CAS to approximate the intersections of $y = \sin x$ and $y = x/2$, and then approximate the volume of the solid below $z = \sqrt{1 + x + y}$ and above the region enclosed by the curves in the first octant.
66. **Writing.** Describe the steps you would follow to find the limits of integration that express a double integral over a nonrectangular region as an iterated double integral. Illustrate with an example.
67. **Writing.** Describe the steps you would follow to reverse the order of integration in an iterated double integral. Illustrate with an example.

#### QUICK CHECK ANSWERS 14.2
1. (a) $\int_1^5 (\frac{1}{4}y^4 - 16y)\,dy$ (b) $\int_1^5 (\frac{3}{4}x^4 - 12x^2)\,dx$  
2. (a) $\int_0^3 \int_0^{-\frac{4}{3}x+4} f(x, y)\,dy\,dx$ (b) $\int_0^4 \int_0^{-\frac{3}{4}y+3} f(x, y)\,dx\,dy$  
3. $\int_0^3 \int_x^{-\frac{1}{3}x+4} dy\,dx = 6$  
4. $\int_{-2}^1 \int_{x^2}^{2-x} (1 + 2y)\,dy\,dx = 18.9$

---

## 14.3 DOUBLE INTEGRALS IN POLAR COORDINATES

### SIMPLE POLAR REGIONS

> **14.3.1 DEFINITION**  
> A **simple polar region** in a polar coordinate system is a region enclosed between two rays, $\theta = \alpha$ and $\theta = \beta$, and two continuous polar curves, $r = r_1(\theta)$ and $r = r_2(\theta)$, where:  
> (i) $\alpha \le \beta$  
> (ii) $\beta - \alpha \le 2\pi$  
> (iii) $0 \le r_1(\theta) \le r_2(\theta)$

A **polar rectangle** is given by $r_1 \le r \le r_2, \; \alpha \le \theta \le \beta$.

> **14.3.2 THE VOLUME PROBLEM IN POLAR COORDINATES**  
> Given a function $f(r, \theta)$ continuous and nonnegative on simple polar region $R$, find the volume enclosed between $R$ and $z = f(r, \theta)$.
> $$V = \lim_{n \to +\infty} \sum_{k=1}^n f(r_k^*, \theta_k^*)\,\Delta A_k \tag{1}$$
> Since $\Delta A_k = r_k^*\Delta r_k\Delta\theta_k$, we define the **polar double integral**:
> $$\iint_R f(r, \theta)\,dA = \lim_{n \to +\infty} \sum_{k=1}^n f(r_k^*, \theta_k^*)\,\Delta A_k \tag{3}$$

> **14.3.3 THEOREM**  
> If $R$ is a simple polar region bounded by $\theta = \alpha, \theta = \beta, r = r_1(\theta), r = r_2(\theta)$, and if $f(r, \theta)$ is continuous on $R$, then:
> $$\iint_R f(r, \theta)\,dA = \int_\alpha^\beta \int_{r_1(\theta)}^{r_2(\theta)} f(r, \theta)\,r\,dr\,d\theta \tag{7}$$

#### Example 1
Evaluate $\iint_R \sin\theta\,dA$ where $R$ is in the first quadrant outside $r = 2$ and inside $r = 2(1 + \cos\theta)$.

**Solution.**
$$\iint_R \sin\theta\,dA = \int_0^{\pi/2} \int_2^{2(1+\cos\theta)} (\sin\theta)r\,dr\,d\theta = 2\int_0^{\pi/2} [(1 + \cos\theta)^2 \sin\theta - \sin\theta]\,d\theta = 2\left[-\frac{1}{3}(1 + \cos\theta)^3 + \cos\theta\right]_0^{\pi/2} = \frac{8}{3}$$

#### Example 2
Find volume of sphere $x^2 + y^2 + z^2 = a^2$ ($r^2 + z^2 = a^2$).

**Solution.**
$$V = 2\iint_R \sqrt{a^2 - r^2}\,dA = \int_0^{2\pi} \int_0^a \sqrt{a^2 - r^2}(2r)\,dr\,d\theta = \int_0^{2\pi} \left[-\frac{2}{3}(a^2 - r^2)^{3/2}\right]_{r=0}^a d\theta = \frac{4}{3}\pi a^3$$

---

### FINDING AREAS & CONVERTING TO POLAR COORDINATES

$$\text{area of } R = \iint_R 1\,dA = \iint_R dA \tag{8}$$

#### Example 3
Find area enclosed by three-petaled rose $r = \sin 3\theta$.

**Solution.**
$$A = 3\iint_{\text{petal}} dA = 3\int_0^{\pi/3} \int_0^{\sin 3\theta} r\,dr\,d\theta = \frac{3}{2}\int_0^{\pi/3} \sin^2 3\theta\,d\theta = \frac{3}{4}\int_0^{\pi/3} (1 - \cos 6\theta)\,d\theta = \frac{\pi}{4}$$

* **Converting from Rectangular to Polar Coordinates:**
  $$\iint_R f(x, y)\,dA = \iint_R f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta \tag{9}$$

#### Example 4
Evaluate $\int_{-1}^1 \int_0^{\sqrt{1-x^2}} (x^2 + y^2)^{3/2}\,dy\,dx$.

**Solution.** Semicircle of radius 1 ($0 \le r \le 1, 0 \le \theta \le \pi$):
$$\int_{-1}^1 \int_0^{\sqrt{1-x^2}} (x^2 + y^2)^{3/2}\,dy\,dx = \int_0^\pi \int_0^1 (r^3)r\,dr\,d\theta = \int_0^\pi \frac{1}{5}\,d\theta = \frac{\pi}{5}$$

---

### QUICK CHECK EXERCISES 14.3
*(See page 1025 for answers.)*

1. The polar region inside the circle $r = 2\sin\theta$ and outside the circle $r = 1$ is a simple polar region given by $\underline{\quad} \le r \le \underline{\quad}, \; \underline{\quad} \le \theta \le \underline{\quad}$.
2. Let $R$ be the region in the first quadrant enclosed between the circles $x^2 + y^2 = 9$ and $x^2 + y^2 = 100$. Supply the missing limits:
   $$\iint_R f(r, \theta)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(r, \theta)r\,dr\,d\theta$$
3. Let $V$ be the volume of the solid bounded above by the hemisphere $z = \sqrt{1 - r^2}$ and bounded below by the disk $r = \sin\theta$. Expressed as a double integral in polar coordinates, $V = \underline{\quad}$.
4. Express the iterated integral as a double integral in polar coordinates:
   $$\int_{1/\sqrt{2}}^1 \int_{\sqrt{1-x^2}}^x \left(\frac{1}{x^2 + y^2}\right)dy\,dx = \underline{\quad}$$

---

### EXERCISE SET 14.3

**1–6 Evaluate the iterated integral.**
1. $\int_0^{\pi/2} \int_0^{\sin\theta} r\cos\theta\,dr\,d\theta$
2. $\int_0^\pi \int_0^{1+\cos\theta} r\,dr\,d\theta$
3. $\int_0^{\pi/2} \int_0^{a\sin\theta} r^2\,dr\,d\theta$
4. $\int_0^{\pi/6} \int_0^{\cos 3\theta} r\,dr\,d\theta$
5. $\int_0^\pi \int_0^{1-\sin\theta} r^2\cos\theta\,dr\,d\theta$
6. $\int_0^{\pi/2} \int_0^{\cos\theta} r^3\,dr\,d\theta$

**7–10 Use a double integral in polar coordinates to find the area of the region described.**
7. The region enclosed by the cardioid $r = 1 - \cos\theta$.
8. The region enclosed by the rose $r = \sin 2\theta$.
9. The region in the first quadrant bounded by $r = 1$ and $r = \sin 2\theta$, with $\pi/4 \le \theta \le \pi/2$.
10. The region inside the circle $x^2 + y^2 = 4$ and to the right of the line $x = 1$.

#### FOCUS ON CONCEPTS
11–12 Let $R$ be the region described. Sketch $R$ and fill in the missing limits of integration: $\iint_R f(r, \theta)\,dA = \int_{\square}^{\square} \int_{\square}^{\square} f(r, \theta)r\,dr\,d\theta$.  
11. The region inside the circle $r = 4\sin\theta$ and outside the circle $r = 2$.  
12. The region inside the circle $r = 1$ and outside the cardioid $r = 1 + \cos\theta$.

**13–16 Express the volume of the solid described as a double integral in polar coordinates.**
13. Inside of $x^2 + y^2 + z^2 = 9$, outside of $x^2 + y^2 = 1$.
14. Below $z = \sqrt{x^2+y^2}$, inside of $x^2 + y^2 = 2y$, above $z = 0$.
15. Below $z = 1 - x^2 - y^2$, inside of $x^2 + y^2 - x = 0$, above $z = 0$.
16. Below $z = (x^2 + y^2)^{-1/2}$, outside of $x^2 + y^2 = 1$, inside of $x^2 + y^2 = 9$, above $z = 0$.

**17–20 Find the volume of the solid described in the indicated exercise.**
17. Exercise 13
18. Exercise 14
19. Exercise 15
20. Exercise 16

21. Find the volume of the solid in the first octant bounded above by $z = r\sin\theta$, below by $xy$-plane, and laterally by $x = 0$ and $r = 3\sin\theta$.
22. Find the volume of the solid inside the surface $r^2 + z^2 = 4$ and outside $r = 2\cos\theta$.

**23–26 Use polar coordinates to evaluate the double integral.**
23. $\iint_R \sin(x^2 + y^2)\,dA$, where $R$ is the region enclosed by $x^2 + y^2 = 9$.
24. $\iint_R \sqrt{9 - x^2 - y^2}\,dA$, where $R$ is first-quadrant within $x^2 + y^2 = 9$.
25. $\iint_R \frac{1}{1 + x^2 + y^2}\,dA$, where $R$ is sector in first quadrant bounded by $y = 0, y = x, x^2 + y^2 = 4$.
26. $\iint_R 2y\,dA$, where $R$ is first-quadrant bounded above by $(x - 1)^2 + y^2 = 1$ and below by $y = x$.

**27–34 Evaluate the iterated integral by converting to polar coordinates.**
27. $\int_0^1 \int_0^{\sqrt{1-x^2}} (x^2 + y^2)\,dy\,dx$
28. $\int_{-2}^2 \int_{-\sqrt{4-y^2}}^{\sqrt{4-y^2}} e^{-(x^2+y^2)}\,dx\,dy$
29. $\int_0^2 \int_0^{\sqrt{2x-x^2}} \sqrt{x^2 + y^2}\,dy\,dx$
30. $\int_0^1 \int_0^{\sqrt{1-y^2}} \cos(x^2 + y^2)\,dx\,dy$
31. $\int_0^a \int_0^{\sqrt{a^2-x^2}} \frac{dy\,dx}{(1 + x^2 + y^2)^{3/2}} \quad (a > 0)$
32. $\int_0^1 \int_y^{\sqrt{y}} \sqrt{x^2 + y^2}\,dx\,dy$
33. $\int_0^{\sqrt{2}} \int_y^{\sqrt{4-y^2}} \frac{1}{\sqrt{1 + x^2 + y^2}}\,dx\,dy$
34. $\int_{-4}^0 \int_{-\sqrt{16-x^2}}^{\sqrt{16-x^2}} 3x\,dy\,dx$

**35–38 True–False Determine whether the statement is true or false. Explain your answer.**
35. The disk of radius 2 that is centered at the origin is a polar rectangle.
36. If $f$ is continuous and nonnegative on a simple polar region $R$, then the volume of the solid enclosed between $R$ and $z = f(r, \theta)$ is $\iint_R f(r, \theta)r\,dA$.
37. If $R$ is the region in the first quadrant between $r = 1$ and $r = 2$, then $\iint_R f(r, \theta)\,dA = \int_0^{\pi/2} \int_1^2 f(r, \theta)\,dr\,d\theta$.
38. The area enclosed by the circle $r = \sin\theta$ is given by $A = \int_0^{2\pi} \int_0^{\sin\theta} r\,dr\,d\theta$.

39. Use a double integral in polar coordinates to find the volume of a cylinder of radius $a$ and height $h$.
40. Suppose that a geyser, centered at the origin of a polar coordinate system, sprays water in a circular pattern such that depth $D(r) = ke^{-r}$. Find the total volume of water sprayed inside circle of radius $R$.
41. Evaluate $\iint_R x^2\,dA$ over the region $R$ shown in Figure Ex-41 (between $y = \frac{1}{3}x, y = 2x, y = \sqrt{4 - x^2}$).
42. Show that the shaded area in Figure Ex-42 is $a^2\phi - \frac{1}{2}a^2\sin 2\phi$.
43. (a) Use a double integral in polar coordinates to find the volume of the oblate spheroid $\frac{x^2}{a^2} + \frac{y^2}{a^2} + \frac{z^2}{c^2} = 1 \; (0 < c < a)$.  
    (b) Use the result and the WGS-84 model ($a = 6378.1370\text{ km}, c = 6356.5231\text{ km}$) to find the volume of the Earth in cubic meters.
44. Use polar coordinates to find the volume of the solid above $xy$-plane, inside cylinder $x^2 + y^2 - ay = 0$, and inside ellipsoid $\frac{x^2}{a^2} + \frac{y^2}{a^2} + \frac{z^2}{c^2} = 1$.
45. Find the area of the region enclosed by the lemniscate $r^2 = 2a^2\cos 2\theta$.
46. Find the area in the first quadrant that is inside $r = 4\sin\theta$ and outside lemniscate $r^2 = 8\cos 2\theta$.

#### QUICK CHECK ANSWERS 14.3
1. $1 \le r \le 2\sin\theta, \; \pi/6 \le \theta \le 5\pi/6$  
2. $\int_0^{\pi/2} \int_3^{10} f(r, \theta)r\,dr\,d\theta$  
3. $\int_0^\pi \int_0^{\sin\theta} r\sqrt{1 - r^2}\,dr\,d\theta$  
4. $\int_0^{\pi/4} \int_1^{\sec\theta} \frac{1}{r}\,dr\,d\theta$

---

## 14.4 SURFACE AREA; PARAMETRIC SURFACES

### SURFACE AREA FOR $z = f(x, y)$

> **14.4.1 FORMULA**  
> If $f$ has continuous first partial derivatives on $R$, the surface area $S$ of $z = f(x, y)$ over $R$ is:
> $$S = \iint_R \sqrt{\left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2 + 1}\,dA \tag{2}$$

#### Example 1
Find the surface area of the portion of $z = \sqrt{4 - x^2}$ that lies above the rectangle $R = [0, 1] \times [0, 4]$.

**Solution.**
$$S = \iint_R \sqrt{\left(-\frac{x}{\sqrt{4-x^2}}\right)^2 + 0 + 1}\,dA = \int_0^4 \int_0^1 \frac{2}{\sqrt{4-x^2}}\,dx\,dy = 2\int_0^4 \left[\sin^{-1}(x/2)\right]_0^1 dy = 2\int_0^4 \frac{\pi}{6}\,dy = \frac{4\pi}{3}$$

#### Example 2
Find surface area of paraboloid $z = x^2 + y^2$ below $z = 1$.

**Solution.**
$$S = \iint_R \sqrt{4x^2 + 4y^2 + 1}\,dA = \int_0^{2\pi} \int_0^1 \sqrt{4r^2 + 1}\,r\,dr\,d\theta = \frac{\pi}{6}(5\sqrt{5} - 1)$$

---

### PARAMETRIC REPRESENTATION OF SURFACES

Parametric equations with two parameters $u, v$:
$$x = x(u, v), \quad y = y(u, v), \quad z = z(u, v) \tag{3}$$
Vector form: $\mathbf{r}(u, v) = x(u, v)\mathbf{i} + y(u, v)\mathbf{j} + z(u, v)\mathbf{k}$.

#### Example 3 & 4
Paraboloid $z = 4 - x^2 - y^2$:
* Cartesian parameters: $x = u, y = v, z = 4 - u^2 - v^2$.
* Cylindrical parameters: $x = r\cos\theta, y = r\sin\theta, z = 4 - r^2$.

#### Example 5
Sphere $x^2 + y^2 + z^2 = 1 \implies x = \sin\phi\cos\theta, y = \sin\phi\sin\theta, z = \cos\phi \; (0 \le \theta \le 2\pi, 0 \le \phi \le \pi)$.

#### Example 6
Cylinder $x^2 + z^2 = 9 \; (0 \le y \le 5) \implies x = 3\cos v, y = u, z = 3\sin v \; (0 \le u \le 5, 0 \le v \le 2\pi)$.

#### Example 7
Surface of revolution of $y = f(x)$ about $x$-axis:
$$x = u, \quad y = f(u)\cos v, \quad z = f(u)\sin v \tag{6}$$

---

### TANGENT PLANES & SURFACE AREA OF PARAMETRIC SURFACES

Partial derivatives: $\mathbf{r}_u = \frac{\partial\mathbf{r}}{\partial u}, \quad \mathbf{r}_v = \frac{\partial\mathbf{r}}{\partial v}$.  
Normal vector: $\mathbf{r}_u \times \mathbf{r}_v$. Principal unit normal: $\mathbf{n} = \frac{\mathbf{r}_u \times \mathbf{r}_v}{\|\mathbf{r}_u \times \mathbf{r}_v\|} \tag{10}$.

> **14.4.2 FORMULA (Parametric Surface Area)**  
> $$S = \iint_R \left\|\frac{\partial\mathbf{r}}{\partial u} \times \frac{\partial\mathbf{r}}{\partial v}\right\| dA \tag{12}$$

#### Example 10 (Whitney's Umbrella)
$x = uv, y = u, z = v^2$ at $u = 2, v = -1 \implies \mathbf{r}_u \times \mathbf{r}_v = -2\mathbf{i} - 2\mathbf{j} - 2\mathbf{k} \implies x + y + z = 1$.

#### Example 12
Surface area of cone $x = u, y = u\cos v, z = u\sin v \; (0 \le u \le 2, 0 \le v \le 2\pi)$:
$$S = \int_0^{2\pi} \int_0^2 \sqrt{2}u\,du\,dv = 4\pi\sqrt{2}$$

---

### QUICK CHECK EXERCISES 14.4
*(See page 1039 for answers.)*

1. Surface area of $z = f(x, y)$ over $R$: $S = \iint_R \underline{\quad}\,dA$.
2. Parametric surface $x = 1 - u, y = (1 - u)\cos v, z = (1 - u)\sin v \; (0 \le u \le 1, 0 \le v \le 2\pi)$:  
   (a) Describe constant $u$-curves.  
   (b) Describe constant $v$-curves.
3. If $\mathbf{r}(u, v) = (1 - u)\mathbf{i} + [(1 - u)\cos v]\mathbf{j} + [(1 - u)\sin v]\mathbf{k}$, find $\frac{\partial\mathbf{r}}{\partial u}$ and $\frac{\partial\mathbf{r}}{\partial v}$.
4. Principal unit normal to $\mathbf{r}$ in Exercise 3 at $u = 1/2, v = \pi/6$.
5. Surface area formula for $\sigma: \mathbf{r}(u, v)$.

---

### EXERCISE SET 14.4

**1–4 Express the area of the given surface as an iterated double integral, and then find the surface area.**
1. The portion of the cylinder $y^2 + z^2 = 9$ that is above the rectangle $R = \{(x, y) : 0 \le x \le 2, -3 \le y \le 3\}$.
2. The portion of the plane $2x + 2y + z = 8$ in the first octant.
3. The portion of the cone $z^2 = 4x^2 + 4y^2$ that is above the region in the first quadrant bounded by $y = x$ and $y = x^2$.
4. The portion of the surface $z = 2x + y^2$ that is above the triangular region with vertices $(0, 0), (0, 1),$ and $(1, 1)$.

**5–10 Express the area of the given surface as an iterated double integral in polar coordinates, and then find the surface area.**
5. The portion of the cone $z = \sqrt{x^2+y^2}$ that lies inside the cylinder $x^2 + y^2 = 2x$.
6. The portion of the paraboloid $z = 1 - x^2 - y^2$ that is above the $xy$-plane.
7. The portion of the surface $z = xy$ that is above the sector in the first quadrant bounded by $y = x/\sqrt{3}, y = 0,$ and $x^2 + y^2 = 9$.
8. The portion of the paraboloid $2z = x^2 + y^2$ that is inside the cylinder $x^2 + y^2 = 8$.
9. The portion of the sphere $x^2 + y^2 + z^2 = 16$ between the planes $z = 1$ and $z = 2$.
10. The portion of the sphere $x^2 + y^2 + z^2 = 8$ that is inside the cone $z = \sqrt{x^2+y^2}$.

**11–12 Sketch the parametric surface.**
11. (a) $x = u, y = v, z = \sqrt{u^2+v^2}$ (b) $x = u, y = \sqrt{u^2+v^2}, z = v$ (c) $x = \sqrt{u^2+v^2}, y = u, z = v$
12. (a) $x = u, y = v, z = u^2 + v^2$ (b) $x = u, y = u^2 + v^2, z = v$ (c) $x = u^2 + v^2, y = u, z = v$

**13–14 Find a parametric representation of the surface in terms of parameters $u = x$ and $v = y$.**
13. (a) $2z - 3x + 4y = 5$ (b) $z = x^2$
14. (a) $z + zx^2 - y = 0$ (b) $y^2 - 3z = 5$

15. (a) Parametric equations for portion of cylinder $x^2 + y^2 = 5$ between $z = 0$ and $z = 1$.  
    (b) Parametric equations for portion of cylinder $x^2 + z^2 = 4$ between $y = 1$ and $y = 3$.
16. (a) Parametric equations for portion of plane $x + y = 1$ between $z = -1$ and $z = 1$.  
    (b) Parametric equations for portion of plane $y - 2z = 5$ between $x = 0$ and $x = 3$.
17. Parametric equations for surface generated by revolving $y = \sin x$ about $x$-axis.
18. Parametric equations for surface generated by revolving $y - e^x = 0$ about $x$-axis.

**19–24 Find a parametric representation of the surface in terms of parameters $r$ and $\theta$ (cylindrical coordinates).**
19. $z = \frac{1}{1 + x^2 + y^2}$
20. $z = e^{-(x^2+y^2)}$
21. $z = 2xy$
22. $z = x^2 - y^2$
23. Portion of sphere $x^2 + y^2 + z^2 = 9$ on or above $z = 2$.
24. Portion of cone $z = \sqrt{x^2+y^2}$ on or below $z = 3$.

25. Parametric representation of cone $z = \sqrt{3x^2+3y^2}$ in terms of $\rho, \theta$.
26. Describe cylinder $x^2 + y^2 = 9$ in terms of $\theta, \phi$.

#### FOCUS ON CONCEPTS
**27–32 Eliminate parameters to obtain equation in rectangular coordinates, and describe the surface.**
27. $x = 2u + v, y = u - v, z = 3v$.
28. $x = u\cos v, y = u^2, z = u\sin v \; (0 \le u \le 2, 0 \le v < 2\pi)$.
29. $x = 3\sin u, y = 2\cos u, z = 2v \; (0 \le u < 2\pi, 1 \le v \le 2)$.
30. $x = \sqrt{u}\cos v, y = \sqrt{u}\sin v, z = u \; (0 \le u \le 4, 0 \le v < 2\pi)$.
31. $\mathbf{r}(u, v) = 3u\cos v\mathbf{i} + 4u\sin v\mathbf{j} + u\mathbf{k} \; (0 \le u \le 1, 0 \le v < 2\pi)$.
32. $\mathbf{r}(u, v) = \sin u\cos v\mathbf{i} + 2\sin u\sin v\mathbf{j} + 3\cos u\mathbf{k} \; (0 \le u \le \pi, 0 \le v < 2\pi)$.

33–34 Parametric representations and facsimile equations for cone and paraboloid.  
35–38 Domain restrictions on $u, v$ and $\phi, \theta$ for portions of cylinders and spheres.

**39–44 Find an equation of the tangent plane to the parametric surface at the stated point.**
39. $x = u, y = v, z = u^2 + v^2; \quad (1, 2, 5)$
40. $x = u^2, y = v^2, z = u + v; \quad (1, 4, 3)$
41. $x = 3v\sin u, y = 2v\cos u, z = u^2; \quad (0, 2, 0)$
42. $\mathbf{r} = uv\mathbf{i} + (u - v)\mathbf{j} + (u + v)\mathbf{k}; \quad u = 1, v = 2$
43. $\mathbf{r} = u\cos v\mathbf{i} + u\sin v\mathbf{j} + v\mathbf{k}; \quad u = 1/2, v = \pi/4$
44. $\mathbf{r} = uv\mathbf{i} + u e^v\mathbf{j} + v e^u\mathbf{k}; \quad u = \ln 2, v = 0$

**45–46 Find the area of the given surface.**
45. Portion of paraboloid $\mathbf{r}(u, v) = u\cos v\mathbf{i} + u\sin v\mathbf{j} + u^2\mathbf{k}$ for $1 \le u \le 2, 0 \le v \le 2\pi$.
46. Portion of cone $\mathbf{r}(u, v) = u\cos v\mathbf{i} + u\sin v\mathbf{j} + u\mathbf{k}$ for $0 \le u \le 2v, 0 \le v \le \pi/2$.

**47–50 True–False Determine whether the statement is true or false. Explain your answer.**
47. If $f$ has continuous first partial derivatives in the interior of $R$, the surface area is $\iint_R \sqrt{[f(x, y)]^2 + 1}\,dA$.
48. If $z = f(x, y)$, and $\mathbf{q} = \langle 1, 0, \partial z/\partial x \rangle, \mathbf{r} = \langle 0, 1, \partial z/\partial y \rangle$, then $S = \iint_R \|\mathbf{q} \times \mathbf{r}\|\,dA$.
49. If $\mathbf{r}(u, v)$ has nonzero partial derivatives, $\mathbf{r}_u \times \mathbf{r}_v$ is normal to the surface.
50. For $f(x, y) = ax + by$, the surface area over $R$ is $\|\langle 1, 0, a \rangle \times \langle 0, 1, b \rangle\|\text{Area}(R)$.

51. Use parametric equations to derive the formula for the surface area of a sphere of radius $a$: $S = 4\pi a^2$.
52. Use parametric equations to derive lateral surface area of right circular cylinder: $S = 2\pi rh$.
53. Show lateral surface area of cone $z = (h/a)\sqrt{x^2+y^2}$ between $z = 0$ and $z = h$ is $S = \pi a\sqrt{a^2+h^2}$.
54. (a) Parametric equations for torus generated by revolving $(x - a)^2 + z^2 = b^2 \; (0 < b < a)$ about $z$-axis:  
    $x = (a + b\cos v)\cos u, \quad y = (a + b\cos v)\sin u, \quad z = b\sin v \quad (0 \le u \le 2\pi, 0 \le v \le 2\pi)$.  
    (b) CAS generation of torus.
55. Find surface area of torus in Exercise 54(a): $S = 4\pi^2 ab$.
56. [CAS] Graph helicoid $x = u\cos v, y = u\sin v, z = v \; (0 \le u \le 5, 0 \le v \le 4\pi)$ and approximate surface area.
57. [CAS] Graph pseudosphere $x = \cos u\sin v, y = \sin u\sin v, z = \cos v + \ln|\tan(v/2)|$ and approximate surface area between $z = -1$ and $z = 1$.
58. (a) Parametric equations for surface revolving $z = f(x)$ about $z$-axis.  
    (b) Surface revolving $z = 1/x^2$ about $z$-axis.
59–61 Parametric equations of quadric surfaces:  
59. $x = a\cos u\cos v, y = b\sin u\cos v, z = c\sin v$ (Ellipsoid).  
60. $x = a\cos u\cosh v, y = b\sin u\cosh v, z = c\sinh v$ (Hyperboloid of one sheet).  
61. $x = a\sinh v, y = b\sinh u\cosh v, z = c\cosh u\cosh v$ (Hyperboloid of two sheets).
62. **Writing.** Schwartz's cylinder area paradox (1890).

#### QUICK CHECK ANSWERS 14.4
1. $\sqrt{(\partial z/\partial x)^2 + (\partial z/\partial y)^2 + 1}$  
2. (a) circles of radius $1 - u$ centered at $(1 - u, 0, 0)$ parallel to $yz$-plane (b) line segments joining $(1, \cos v, \sin v)$ and $(0, 0, 0)$  
3. $\mathbf{r}_u = -\mathbf{i} - \cos v\mathbf{j} - \sin v\mathbf{k}; \; \mathbf{r}_v = -(1 - u)\sin v\mathbf{j} + (1 - u)\cos v\mathbf{k}$  
4. $\frac{1}{\sqrt{8}}(-2\mathbf{i} + \sqrt{3}\mathbf{j} + \mathbf{k})$  
5. $\|\mathbf{r}_u \times \mathbf{r}_v\|$

---

## 14.5 TRIPLE INTEGRALS

### DEFINITION OF A TRIPLE INTEGRAL

> **14.5.1 DEFINITION**  
> The **triple integral** of $f(x, y, z)$ over closed solid region $G$ is
> $$\iiint_G f(x, y, z)\,dV = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*, y_k^*, z_k^*)\,\Delta V_k \tag{1}$$
> Volume: $\text{volume of } G = \iiint_G dV \tag{5}$.

Properties: linearity, constant multiples, additivity over subregions $G = G_1 \cup G_2$.

> **14.5.1 THEOREM (Fubini's Theorem for Triple Integrals)**  
> Let $G$ be the rectangular box $a \le x \le b, c \le y \le d, k \le z \le l$. If $f$ is continuous on $G$:
> $$\iiint_G f(x, y, z)\,dV = \int_a^b \int_c^d \int_k^l f(x, y, z)\,dz\,dy\,dx \tag{2}$$
> (and any of the 6 possible orders of integration).

#### Example 1
Evaluate $\iiint_G 12xy^2 z^3\,dV$ over $[-1, 2] \times [0, 3] \times [0, 2]$.

**Solution.**
$$\int_{-1}^2 \int_0^3 \int_0^2 12xy^2 z^3\,dz\,dy\,dx = \int_{-1}^2 \int_0^3 48xy^2\,dy\,dx = \int_{-1}^2 432x\,dx = [216x^2]_{-1}^2 = 648$$

> **14.5.2 THEOREM (Simple $xy$-Solid)**  
> If $G$ is bounded above by $z = g_2(x, y)$, below by $z = g_1(x, y)$, over projection region $R$ in $xy$-plane:
> $$\iiint_G f(x, y, z)\,dV = \iint_R \left[\int_{g_1(x, y)}^{g_2(x, y)} f(x, y, z)\,dz\right]dA \tag{3}$$

#### Example 2
Evaluate $\iiint_G z\,dV$ where $G$ is the wedge in the first octant cut from $y^2 + z^2 \le 1$ by $y = x$ and $x = 0$.

**Solution.**
$$\iiint_G z\,dV = \int_0^1 \int_0^y \int_0^{\sqrt{1-y^2}} z\,dz\,dx\,dy = \int_0^1 \frac{1}{2}(y - y^3)\,dy = \frac{1}{8}$$

#### Example 3
Volume within cylinder $x^2 + y^2 = 9$ and between planes $z = 1$ and $x + z = 5$.

**Solution.**
$$V = \int_{-3}^3 \int_{-\sqrt{9-x^2}}^{\sqrt{9-x^2}} \int_1^{5-x} dz\,dy\,dx = \int_{-3}^3 (8 - 2x)\sqrt{9 - x^2}\,dx = 8\left(\frac{9\pi}{2}\right) = 36\pi$$

#### Example 4
Volume enclosed between paraboloids $z = 5x^2 + 5y^2$ and $z = 6 - 7x^2 - y^2$.

**Solution.** Intersect on elliptic cylinder $2x^2 + y^2 = 1$.
$$V = \int_{-1/\sqrt{2}}^{1/\sqrt{2}} \int_{-\sqrt{1-2x^2}}^{\sqrt{1-2x^2}} \int_{5x^2+5y^2}^{6-7x^2-y^2} dz\,dy\,dx = 8\int_{-1/\sqrt{2}}^{1/\sqrt{2}} (1 - 2x^2)^{3/2}\,dx = \frac{3\pi}{\sqrt{2}}$$

#### Example 5
Integrate $\iiint_G z\,dV$ from Example 2 by integrating first with respect to $x$: $\int_0^1 \int_0^{\sqrt{1-y^2}} \int_0^y z\,dx\,dz\,dy = \frac{1}{8}$.

---

### QUICK CHECK EXERCISES 14.5
*(See page 1048 for answers.)*

1. The iterated integral $\int_1^5 \int_2^4 \int_3^6 f(x, y, z)\,dx\,dz\,dy$ integrates $f$ over the rectangular box defined by $\underline{\quad} \le x \le \underline{\quad}, \underline{\quad} \le y \le \underline{\quad}, \underline{\quad} \le z \le \underline{\quad}$.
2. Let $G$ be the solid in the first octant bounded below by $z = y + x^2$ and above by $z = 4$. Supply missing limits:  
   (a) $\iiint_G f(x, y, z)\,dV = \int_{\square}^{\square} \int_{\square}^{\square} \int_{y+x^2}^4 f(x, y, z)\,dz\,dx\,dy$  
   (b) $\iiint_G f(x, y, z)\,dV = \int_{\square}^{\square} \int_{\square}^{\square} \int_{y+x^2}^4 f(x, y, z)\,dz\,dy\,dx$  
   (c) $\iiint_G f(x, y, z)\,dV = \int_{\square}^{\square} \int_{\square}^{\square} \int_{\square}^{\square} f(x, y, z)\,dy\,dz\,dx$.
3. The volume of the solid $G$ in Quick Check Exercise 2 is $\underline{\quad}$.

---

### EXERCISE SET 14.5

**1–8 Evaluate the iterated integral.**
1. $\int_{-1}^1 \int_0^2 \int_0^1 (x^2 + y^2 + z^2)\,dx\,dy\,dz$
2. $\int_{1/3}^{1/2} \int_0^\pi \int_0^1 zx\sin xy\,dz\,dy\,dx$
3. $\int_0^2 \int_{-1}^{y^2} \int_{-1}^z yz\,dx\,dz\,dy$
4. $\int_0^{\pi/4} \int_0^1 \int_0^{x^2} x\cos y\,dz\,dx\,dy$
5. $\int_0^3 \int_0^{\sqrt{9-z^2}} \int_0^x xy\,dy\,dx\,dz$
6. $\int_1^3 \int_x^{x^2} \int_0^{\ln z} x e^y\,dy\,dz\,dx$
7. $\int_0^2 \int_0^{\sqrt{4-x^2}} \int_{-5+x^2+y^2}^{3-x^2-y^2} x\,dz\,dy\,dx$
8. $\int_1^2 \int_z^2 \int_0^{\sqrt{3}y} \frac{y}{x^2+y^2}\,dx\,dy\,dz$

**9–12 Evaluate the triple integral.**
9. $\iiint_G xy\sin yz\,dV$, where $G$ is the rectangular box $0 \le x \le \pi, 0 \le y \le 1, 0 \le z \le \pi/6$.
10. $\iiint_G y\,dV$, where $G$ is the solid enclosed by $z = y$, $xy$-plane, and parabolic cylinder $y = 1 - x^2$.
11. $\iiint_G xyz\,dV$, where $G$ is first octant solid bounded by $z = 2 - x^2, z = 0, y = x, y = 0$.
12. $\iiint_G \cos(z/y)\,dV$, where $G$ is $\pi/6 \le y \le \pi/2, y \le x \le \pi/2, 0 \le z \le xy$.

13. [CAS] Approximate $\iiint_G \frac{\sqrt{x+z^2}}{y}\,dV$ over $[0, 3] \times [1, 2] \times [-2, 1]$.
14. [CAS] Approximate $\iiint_G e^{-x^2-y^2-z^2}\,dV$ over spherical region $x^2 + y^2 + z^2 \le 1$.

**15–18 Use a triple integral to find the volume of the solid.**
15. The solid in the first octant bounded by the coordinate planes and the plane $3x + 6y + 4z = 12$.
16. The solid bounded by $z = \sqrt{y}$ and planes $x + y = 1, x = 0, z = 0$.
17. The solid bounded by $y = x^2$ and planes $y + z = 4, z = 0$.
18. The wedge in the first octant cut from $y^2 + z^2 \le 1$ by $y = x$ and $x = 0$.

#### FOCUS ON CONCEPTS
19–20 Fill in missing limits of integration for solids enclosed by paraboloids shown in figures:  
19. $z = 4x^2 + y^2$ and $z = 4 - 3y^2$.  
20. $z = 3x^2 + y^2$ and $z = 8 - x^2 - y^2$.

21–24 Set up iterated triple integrals for volume:  
21. Surfaces in Exercise 19.  
22. Surfaces in Exercise 20.  
23. Elliptic cylinder $x^2 + 9y^2 = 9$ and planes $z = 0, z = x + 3$.  
24. Cylinders $x^2 + y^2 = 1$ and $x^2 + z^2 = 1$.

25–26 Sketch solids whose volume is given by iterated integrals:  
25. (a) $\int_{-1}^1 \int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}} \int_0^{y+1} dz\,dy\,dx$ (b) $\int_0^9 \int_0^{y/3} \int_0^{\sqrt{y^2-9x^2}} dz\,dx\,dy$ (c) $\int_0^1 \int_0^{\sqrt{1-x^2}} \int_0^2 dy\,dz\,dx$.  
26. (a) $\int_0^3 \int_{x^2}^9 \int_0^2 dz\,dy\,dx$ (b) $\int_0^2 \int_0^{2-y} \int_0^{2-x-y} dz\,dx\,dy$ (c) $\int_{-2}^2 \int_0^{4-y^2} \int_0^2 dx\,dz\,dy$.

**27–30 True–False Determine whether the statement is true or false. Explain your answer.**
27. If $G$ is rectangular solid $[1, 3] \times [2, 5] \times [-1, 1]$, then $\iiint_G f(x, y, z)\,dV = \int_1^3 \int_{-1}^1 \int_2^5 f(x, y, z)\,dy\,dz\,dx$.
28. If $G$ is simple $xy$-solid, triple integral can be expressed with outermost integration with respect to $z$.
29. If $G$ is unit ball in first octant, $\iiint_G f\,dV = \int_0^1 \int_0^1 \int_0^{\sqrt{1-x^2-y^2}} f\,dz\,dy\,dx$.
30. If $\text{volume}(G) = \iiint_G f(x, y, z)\,dV$, then $f(x, y, z) = 1$ everywhere.

31. Show that if $f(x, y, z) = f(x)g(y)h(z)$ over $[a, b] \times [c, d] \times [k, l]$, then $\iiint_G f(x, y, z)\,dV = \left[\int_a^b f(x)\,dx\right]\left[\int_c^d g(y)\,dy\right]\left[\int_k^l h(z)\,dz\right]$.
32. Use Exercise 31 to evaluate:  
    (a) $\iiint_G xy^2\sin z\,dV$ on $[-1, 1] \times [0, 1] \times [0, \pi/2]$.  
    (b) $\iiint_G e^{2x+y-z}\,dV$ on $[0, 1] \times [0, \ln 3] \times [0, \ln 2]$.

**33–36 The average value of $f(x, y, z)$ over solid $G$ is $f_{\text{ave}} = \frac{1}{V(G)}\iiint_G f(x, y, z)\,dV$.**
33. Average value of $f(x, y, z) = x + y + z$ over tetrahedron with vertices $(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)$.
34. Average value of $f(x, y, z) = xyz$ over unit ball $x^2 + y^2 + z^2 \le 1$.
35. [CAS] Approximate average distance from origin to a point in solid of Example 4.
36. [CAS] Approximate average distance from $(z, z, z)$ to $(x, y, 0)$ in unit cube.
37. (a) List six different iterated integrals for volume of tetrahedron $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} \le 1$ in first octant. (b) Evaluate any one to show $V = \frac{1}{6}abc$.
38. Derive volume of ellipsoid $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ as $V = \frac{4}{3}\pi abc$.

**39–40 Express each integral as an equivalent integral in which the $z$-integration is performed first, $y$-integration second, and $x$-integration last ($dz\,dy\,dx$).**
39. (a) $\int_0^5 \int_0^2 \int_0^{\sqrt{4-y^2}} f(x, y, z)\,dx\,dy\,dz$  
    (b) $\int_0^9 \int_0^{3-\sqrt{x}} \int_0^z f(x, y, z)\,dy\,dz\,dx$  
    (c) $\int_0^4 \int_y^{8-y} \int_0^{\sqrt{4-y}} f(x, y, z)\,dx\,dz\,dy$
40. (a) $\int_0^3 \int_0^{\sqrt{9-z^2}} \int_0^{\sqrt{9-y^2-z^2}} f(x, y, z)\,dx\,dy\,dz$  
    (b) $\int_0^4 \int_0^2 \int_0^{x/2} f(x, y, z)\,dy\,dz\,dx$  
    (c) $\int_0^4 \int_0^{4-y} \int_0^{\sqrt{z}} f(x, y, z)\,dx\,dz\,dy$

41. **Writing.** Projection onto coordinate planes to find triple integral limits.

#### QUICK CHECK ANSWERS 14.5
1. $3 \le x \le 6, 1 \le y \le 5, 2 \le z \le 4$  
2. (a) $\int_0^4 \int_0^{\sqrt{4-y}} \int_{y+x^2}^4 f(x, y, z)\,dz\,dx\,dy$ (b) $\int_0^2 \int_0^{4-x^2} \int_{y+x^2}^4 f(x, y, z)\,dz\,dy\,dx$ (c) $\int_0^2 \int_{x^2}^4 \int_0^{z-x^2} f(x, y, z)\,dy\,dz\,dx$  
3. $128/15$

---

## 14.6 TRIPLE INTEGRALS IN CYLINDRICAL AND SPHERICAL COORDINATES

### CYLINDRICAL COORDINATES

Volume element: $dV = r\,dz\,dr\,d\theta \tag{3}$.

> **14.6.1 THEOREM**  
> If $G$ is a simple cylindrical solid with $z$ between $g_1(r, \theta)$ and $g_2(r, \theta)$ over polar region $R$:
> $$\iiint_G f(r, \theta, z)\,dV = \int_{\theta_1}^{\theta_2} \int_{r_1(\theta)}^{r_2(\theta)} \int_{g_1(r, \theta)}^{g_2(r, \theta)} f(r, \theta, z)\,r\,dz\,dr\,d\theta \tag{5}$$

#### Example 1
Volume bounded above by $z = \sqrt{25 - x^2 - y^2}$, below by $z = 0$, laterally by $x^2 + y^2 = 9$:
$$V = \int_0^{2\pi} \int_0^3 \int_0^{\sqrt{25-r^2}} r\,dz\,dr\,d\theta = \int_0^{2\pi} \left[-\frac{1}{3}(25 - r^2)^{3/2}\right]_0^3 d\theta = \frac{122\pi}{3}$$

#### Example 2
Evaluate $\int_{-3}^3 \int_{-\sqrt{9-x^2}}^{\sqrt{9-x^2}} \int_0^{9-x^2-y^2} x^2\,dz\,dy\,dx$ using cylindrical coordinates:
$$\int_0^{2\pi} \int_0^3 \int_0^{9-r^2} (r^2\cos^2\theta)r\,dz\,dr\,d\theta = \int_0^{2\pi} \frac{243}{4}\cos^2\theta\,d\theta = \frac{243\pi}{4}$$

---

### SPHERICAL COORDINATES

Volume element: $dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta \tag{8–9}$.
$$\iiint_G f(\rho, \theta, \phi)\,dV = \iiint f(\rho, \theta, \phi)\,\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$$

#### Example 3
Volume bounded above by sphere $\rho = 4$ and below by cone $\phi = \pi/4$:
$$V = \int_0^{2\pi} \int_0^{\pi/4} \int_0^4 \rho^2\sin\phi\,d\rho\,d\phi\,d\theta = \frac{64\pi}{3}(2 - \sqrt{2}) \approx 39.26$$

#### Example 4
Evaluate $\int_{-2}^2 \int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}} \int_0^{\sqrt{4-x^2-y^2}} z^2\sqrt{x^2+y^2+z^2}\,dz\,dy\,dx$:
$$\int_0^{2\pi} \int_0^{\pi/2} \int_0^2 \rho^5\cos^2\phi\sin\phi\,d\rho\,d\phi\,d\theta = \frac{64\pi}{9}$$

---

### QUICK CHECK EXERCISES 14.6
*(See page 1058 for answers.)*

1. (a) Volume of cylindrical wedge $1 \le r \le 3, \pi/6 \le \theta \le \pi/2, 0 \le z \le 5$: $V = \underline{\quad}$.  
   (b) Volume of spherical wedge $1 \le \rho \le 3, \pi/6 \le \theta \le \pi/2, 0 \le \phi \le \pi/3$: $V = \underline{\quad}$.
2. Solid $G$ inside sphere radius 2 and above $z = 1$: supply limits for cylindrical iterated integrals: (a) volume (b) $\iiint_G \frac{z}{x^2+y^2+z^2}\,dV$.
3. Solid $G$ in Quick Check 2: supply limits in spherical coordinates: (a) volume (b) $\iiint_G \frac{z}{x^2+y^2+z^2}\,dV$.

---

### EXERCISE SET 14.6

**1–4 Evaluate the iterated integral.**
1. $\int_0^{2\pi} \int_0^1 \int_0^{\sqrt{1-r^2}} zr\,dz\,dr\,d\theta$
2. $\int_0^{\pi/2} \int_0^{\cos\theta} \int_0^{r^2} r\sin\theta\,dz\,dr\,d\theta$
3. $\int_0^{\pi/2} \int_0^{\pi/2} \int_0^1 \rho^3\sin\phi\cos\phi\,d\rho\,d\phi\,d\theta$
4. $\int_0^{2\pi} \int_0^{\pi/4} \int_0^{a\sec\phi} \rho^2\sin\phi\,d\rho\,d\phi\,d\theta \quad (a > 0)$

#### FOCUS ON CONCEPTS
**5–8 Sketch the region $G$ and identify the function $f$ corresponding to the iterated integrals in Exercises 1–4.**
5. Exercise 1
6. Exercise 2
7. Exercise 3
8. Exercise 4

**9–12 Use cylindrical coordinates to find the volume of the solid.**
9. The solid enclosed by the paraboloid $z = x^2 + y^2$ and the plane $z = 9$.
10. The solid bounded above by the sphere $x^2 + y^2 + z^2 = 1$ and below by the cone $z = \sqrt{x^2+y^2}$.
11. The solid inside the surface $r^2 + z^2 = 20$ but not above the surface $z = r^2$.
12. The solid enclosed between the cone $z = (hr)/a$ and the plane $z = h$.

**13–16 Use spherical coordinates to find the volume of the solid.**
13. The solid bounded above by the sphere $\rho = 4$ and below by the cone $\phi = \pi/3$.
14. The solid within the cone $\phi = \pi/4$ and between the spheres $\rho = 1$ and $\rho = 2$.
15. The solid enclosed by the sphere $x^2 + y^2 + z^2 = 4a^2$ and the planes $z = 0$ and $z = a$.
16. The solid within the sphere $x^2 + y^2 + z^2 = 9$, outside the cone $z = \sqrt{x^2+y^2}$, and above the $xy$-plane.

**17–20 Use cylindrical or spherical coordinates to evaluate the integral.**
17. $\int_0^a \int_0^{\sqrt{a^2-x^2}} \int_0^{a^2-x^2-y^2} x^2\,dz\,dy\,dx \quad (a > 0)$
18. $\int_{-1}^1 \int_0^{\sqrt{1-x^2}} \int_0^{\sqrt{1-x^2-y^2}} e^{-(x^2+y^2+z^2)^{3/2}}\,dz\,dy\,dx$
19. $\int_0^2 \int_0^{\sqrt{4-y^2}} \int_{\sqrt{x^2+y^2}}^{\sqrt{8-x^2-y^2}} z^2\,dz\,dx\,dy$
20. $\int_{-3}^3 \int_{-\sqrt{9-y^2}}^{\sqrt{9-y^2}} \int_{-\sqrt{9-x^2-y^2}}^{\sqrt{9-x^2-y^2}} \sqrt{x^2+y^2+z^2}\,dz\,dx\,dy$

**21–24 True–False Determine whether the statement is true or false. Explain your answer.**
21. A rectangular triple integral can be expressed as an iterated integral in cylindrical coordinates as $\iiint_G f(x, y, z)\,dV = \iiint f(r\cos\theta, r\sin\theta, z)r^2\,dz\,dr\,d\theta$.
22. If $0 \le \rho_1 < \rho_2, 0 \le \theta_1 < \theta_2 \le 2\pi, 0 \le \phi_1 < \phi_2 \le \pi$, then the volume of the spherical wedge is $\int_{\theta_1}^{\theta_2} \int_{\phi_1}^{\phi_2} \int_{\rho_1}^{\rho_2} \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$.
23. If $G$ is the region between spheres of radius 1 and 3 above cone $z = \sqrt{x^2+y^2}$, volume is $\int_0^{\pi/4} \int_0^{2\pi} \int_1^3 \rho^2\sin\phi\,d\rho\,d\theta\,d\phi$.
24. If $G$ is the solid in Exercise 23 and $f$ is continuous, $\iiint_G f\,dV = \int_0^{\pi/4} \int_0^{2\pi} \int_1^3 F(\rho, \theta, \phi)\rho^2\sin\phi\,d\rho\,d\theta\,d\phi$ where $F(\rho, \theta, \phi) = f(\rho\sin\phi\sin\theta, \rho\sin\phi\cos\theta, \rho\cos\phi)$.

25. [CAS] (a) Evaluate $\int_{-2}^2 \int_1^4 \int_{\pi/6}^{\pi/3} \frac{r\tan^3\theta}{\sqrt{1+z^2}}\,d\theta\,dr\,dz$.  
    (b) Find $f(x, y, z)$ and region $G$ matching the integral in rectangular coordinates.
26. [CAS] Evaluate $\int_0^{\pi/2} \int_0^{\pi/4} \int_0^{\cos\theta} \rho^{17}\cos\phi\cos^{19}\theta\,d\rho\,d\phi\,d\theta$.
27. Find the volume enclosed by $x^2 + y^2 + z^2 = a^2$ using: (a) cylindrical coordinates (b) spherical coordinates.
28. Let $G$ be the solid in the first octant bounded by $x^2 + y^2 + z^2 = 4$ and coordinate planes. Evaluate $\iiint_G xyz\,dV$: (a) rectangular (b) cylindrical (c) spherical.
29. Find the volume of the solid in the first octant bounded by $\rho = 2$, coordinate planes, and cones $\phi = \pi/6$ and $\phi = \pi/3$.
30. Volume of spherical wedge derivation:  
    (a) Show volume bounded by sphere $\rho = \rho_0$, cone $\phi = \phi_0$, and $\theta_1, \theta_2$ is $V = \frac{1}{3}\rho_0^3(1 - \cos\phi_0)(\theta_2 - \theta_1)$.  
    (b) Deduce $\Delta V = \frac{\rho_2^3 - \rho_1^3}{3}(\cos\phi_1 - \cos\phi_2)(\theta_2 - \theta_1)$.  
    (c) Apply Mean-Value Theorem to obtain $\Delta V = \rho^{*2}\sin\phi^*\Delta\rho\Delta\phi\Delta\theta$.
31. **Writing.** Outermost variable $\theta$ with constant limits and rotational symmetry.

#### QUICK CHECK ANSWERS 14.6
1. (a) $\frac{20\pi}{3}$ (b) $\frac{13\pi}{9}$  
2. (a) $\int_0^{2\pi} \int_0^{\sqrt{3}} \int_1^{\sqrt{4-r^2}} r\,dz\,dr\,d\theta$ (b) $\int_0^{2\pi} \int_0^{\sqrt{3}} \int_1^{\sqrt{4-r^2}} \frac{rz}{r^2+z^2}\,dz\,dr\,d\theta$  
3. (a) $\int_0^{2\pi} \int_0^{\pi/3} \int_{\sec\phi}^2 \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$ (b) $\int_0^{2\pi} \int_0^{\pi/3} \int_{\sec\phi}^2 \rho\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta$

---

## 14.7 CHANGE OF VARIABLES IN MULTIPLE INTEGRALS; JACOBIANS

### CHANGE OF VARIABLE & TRANSFORMATIONS

Single integral: $\int_a^b f(x)\,dx = \int_\alpha^\beta f(g(u))|g'(u)|\,du \tag{1}$.

Transformation $T: x = x(u, v), y = y(u, v) \tag{2}$.

> **Carl Gustav Jacob Jacobi (1804–1851):** German mathematician who made fundamental contributions to elliptic functions, dynamics, and determinants.

> **14.7.1 DEFINITION (Jacobian in 2 Variables)**  
> $$J(u, v) = \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial y}{\partial u}\frac{\partial x}{\partial v}$$
> Area relationship: $\Delta A \approx \left|\frac{\partial(x, y)}{\partial(u, v)}\right|\Delta u\Delta v \tag{8}$.

> **14.7.2 THEOREM (Change of Variables in Double Integrals)**  
> $$\iint_R f(x, y)\,dA_{xy} = \iint_S f(x(u, v), y(u, v))\left|\frac{\partial(x, y)}{\partial(u, v)}\right|\,dA_{uv} \tag{9}$$

#### Example 2
Evaluate $\iint_R \frac{x-y}{x+y}\,dA$ over region enclosed by $x - y = 0, x - y = 1, x + y = 1, x + y = 3$.

**Solution.** Let $u = x + y, v = x - y \implies x = \frac{1}{2}(u + v), y = \frac{1}{2}(u - v) \implies \frac{\partial(x, y)}{\partial(u, v)} = -1/2$.
$$\iint_R \frac{x-y}{x+y}\,dA = \frac{1}{2}\int_0^1 \int_1^3 \frac{v}{u}\,du\,dv = \frac{1}{4}\ln 3$$

#### Example 3
Evaluate $\iint_R e^{xy}\,dA$ where $R$ is enclosed by $y = x/2, y = x, y = 1/x, y = 2/x$.

**Solution.** Let $u = y/x, v = xy \implies x = \sqrt{v/u}, y = \sqrt{uv} \implies \frac{\partial(x, y)}{\partial(u, v)} = -\frac{1}{2u}$.
$$\iint_R e^{xy}\,dA = \frac{1}{2}\int_1^2 \int_{1/2}^1 \frac{e^v}{u}\,du\,dv = \frac{1}{2}(e^2 - e)\ln 2$$

---

### CHANGE OF VARIABLES IN TRIPLE INTEGRALS

> **14.7.3 DEFINITION (Jacobian in 3 Variables)**  
> $$J(u, v, w) = \frac{\partial(x, y, z)}{\partial(u, v, w)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\ \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w} \end{vmatrix}$$

> **14.7.4 THEOREM (Change of Variables in Triple Integrals)**  
> $$\iiint_R f(x, y, z)\,dV_{xyz} = \iiint_S f(x(u, v, w), y(u, v, w), z(u, v, w))\left|\frac{\partial(x, y, z)}{\partial(u, v, w)}\right|\,dV_{uvw} \tag{14}$$

#### Example 4
Find volume of ellipsoid $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$.

**Solution.** Let $x = au, y = bv, z = cw \implies J = abc$. Region $S$ is unit ball $u^2 + v^2 + w^2 \le 1$.
$$V = \iiint_G dV = abc\iiint_S dV_{uvw} = abc\left(\frac{4}{3}\pi\right) = \frac{4}{3}\pi abc$$

---

### QUICK CHECK EXERCISES 14.7
*(See page 1071 for answers.)*

1. Let $T$ be defined by $x = u - 2v, y = 3u + v$.  
   (a) Sketch image under $T$ of rectangle $1 \le u \le 3, 0 \le v \le 2$.  
   (b) Solve for $u$ and $v$ in terms of $x$ and $y$.
2. State the relationship between $R$ and $S$ in change of variables formula.
3. Let $T$ be the transformation in Quick Check Exercise 1:  
   (a) The Jacobian $\partial(x, y)/\partial(u, v)$ is $\underline{\quad}$.  
   (b) Fill in missing integrand and limits: $\iint_R e^{x+2y}\,dA = \int_{\square}^{\square} \int_{\square}^{\square} \underline{\quad}\,du\,dv$.
4. The Jacobian of $x = uv, y = vw, z = 2w$ is $\underline{\quad}$.

---

### EXERCISE SET 14.7

**1–4 Find the Jacobian $\partial(x, y)/\partial(u, v)$.**
1. $x = u + 4v, y = 3u - 5v$
2. $x = u + 2v^2, y = 2u^2 - v$
3. $x = \sin u + \cos v, y = -\cos u + \sin v$
4. $x = \frac{2u}{u^2+v^2}, y = -\frac{2v}{u^2+v^2}$

**5–8 Solve for $x$ and $y$ in terms of $u$ and $v$, and then find the Jacobian $\partial(x, y)/\partial(u, v)$.**
5. $u = 2x - 5y, v = x + 2y$
6. $u = e^x, v = y e^{-x}$
7. $u = x^2 - y^2, v = x^2 + y^2 \quad (x > 0, y > 0)$
8. $u = xy, v = xy^3 \quad (x > 0, y > 0)$

**9–12 Find the Jacobian $\partial(x, y, z)/\partial(u, v, w)$.**
9. $x = 3u + v, y = u - 2w, z = v + w$
10. $x = u - uv, y = uv - uvw, z = uvw$
11. $u = xy, v = y, w = x + z$
12. $u = x + y + z, v = x + y - z, w = x - y + z$

**13–16 True–False Determine whether the statement is true or false. Explain your answer.**
13. If $\mathbf{r} = x(u, v)\mathbf{i} + y(u, v)\mathbf{j}$, then $|\partial(x, y)/\partial(u, v)|$ gives the perimeter of the parallelogram generated by $\mathbf{r}_u$ and $\mathbf{r}_v$.
14. If $\mathbf{r}$ maps $0 \le u \le 2, 1 \le v \le 5$ to $R$, then $\text{Area}(R) = \int_1^5 \int_0^2 |\partial(x, y)/\partial(u, v)|\,du\,dv$.
15. The Jacobian of $x = r\cos\theta, y = r\sin\theta$ is $r^2$.
16. The Jacobian of $x = \rho\sin\phi\cos\theta, y = \rho\sin\phi\sin\theta, z = \rho\cos\phi$ is $\rho^2\sin\phi$.

#### FOCUS ON CONCEPTS
**17–20 Sketch the image in the $xy$-plane of the set $S$ under the given transformation.**
17. $S: [0, 1] \times [0, 1]; \quad x = u^2 - v^2, y = 2uv$
18. $S: u + v \le 1, u \ge 0, v \ge 0; \quad x = 3u + 4v, y = 4u$
19. $S: u^2 + v^2 \le 1; \quad x = 2u, y = 3v$
20. $S: 1 \le u \le 2, 0 \le v \le \pi/2; \quad x = u\cos v, y = u\sin v$

21. Use $u = x - 2y, v = 2x + y$ to find $\iint_R \frac{x-2y}{2x+y}\,dA$ over $x - 2y = 1, x - 2y = 4, 2x + y = 1, 2x + y = 3$.
22. Use $u = x + y, v = x - y$ to find $\iint_R (x - y)e^{x^2-y^2}\,dA$ over $x + y = 0, x + y = 1, x - y = 1, x - y = 4$.
23. Use $u = \frac{1}{2}(x + y), v = \frac{1}{2}(x - y)$ to find $\iint_R \sin\frac{1}{2}(x+y)\cos\frac{1}{2}(x-y)\,dA$ over triangle $(0, 0), (2, 0), (1, 1)$.
24. Use $u = y/x, v = xy$ to find $\iint_R xy^3\,dA$ over first-quadrant region enclosed by $y = x, y = 3x, xy = 1, xy = 4$.

**25–27 Use $x = au, y = bv$ to map ellipse to unit disk and evaluate in polar coordinates.**
25. $\iint_R \sqrt{16x^2 + 9y^2}\,dA$ over $(x^2/9) + (y^2/16) \le 1$.
26. $\iint_R e^{-(x^2+4y^2)}\,dA$ over $(x^2/4) + y^2 \le 1$.
27. $\iint_R \sin(4x^2 + 9y^2)\,dA$ over first quadrant of $4x^2 + 9y^2 \le 1$.
28. Show that the area of the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} \le 1$ is $\pi ab$.

**29–30 Use $x = au, y = bv, z = cw$ to map ellipsoid to unit ball and evaluate in spherical coordinates.**
29. $\iiint_G x^2\,dV$ over $9x^2 + 4y^2 + z^2 \le 36$.
30. $\iiint_G (y^2 + z^2)\,dV$ over $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} \le 1$.

**31–34 Find a transformation $u = f(x, y), v = g(x, y)$ mapping region $R$ in $xy$-plane to rectangle $S$ in $uv$-plane.**
31. Annular sector between radii 1 and 2 in upper half plane.
32. Region between $y = x, y = x + 2, y = -x + 1, y = -x + 3$.
33. Region bounded by $y = 2x, y = 2x - 2, y = x/2, y = (x+3)/2$.
34. Region bounded by $y = x^2, y = x^2 - 1, y = 2 - x^2, y = 4 - x^2$.

**35–38 Evaluate the integral by making an appropriate change of variables.**
35. $\iint_R \frac{y-4x}{y+4x}\,dA$, where $R$ is enclosed by $y = 4x, y = 4x + 2, y = 2 - 4x, y = 5 - 4x$.
36. $\iint_R (x^2 - y^2)\,dA$, where $R$ is enclosed by $y = -x, y = 1 - x, y = x, y = x + 2$.
37. $\iint_R \frac{\sin(x-y)}{\cos(x+y)}\,dA$, where $R$ is triangular region bounded by $y = 0, y = x, x + y = \pi/4$.
38. $\iint_R e^{(y-x)/(y+x)}\,dA$, where $R$ is trapezoid with vertices $(0, 1), (1, 0), (0, 4), (4, 0)$.

39. Find area of first-quadrant region enclosed by $y = x, y = 2x, x = y^2, x = 4y^2$.
40. Volume bounded above by $x + y + z = 9$, below by $xy$-plane, laterally by elliptic cylinder $4x^2 + 9y^2 = 36$.
41. Use $u = x, v = z - y, w = xy$ to find $\iiint_G (z - y)^2 xy\,dV$ over $x = 1, x = 3, z = y, z = y + 1, xy = 2, xy = 4$.
42. Use $u = xy, v = yz, w = xz$ to find volume of first octant region enclosed by $xy = 1, xy = 2, yz = 1, yz = 3, xz = 1, xz = 4$.
43. (a) 2x2 determinant product identity. (b) Prove $\frac{\partial(x, y)}{\partial(u, v)}\cdot\frac{\partial(u, v)}{\partial(x, y)} = 1$.

**44–46 Use inverse Jacobian $\frac{\partial(x, y)}{\partial(u, v)} = \frac{1}{\partial(u, v)/\partial(x, y)}$ to evaluate:**
44. $\iint_R \sin(xy)\,dA$ with $u = xy, v = xy^4$ over $xy = \pi, xy = 2\pi, xy^4 = 1, xy^4 = 2$.
45. $\iint_R xy\,dA$ with $u = x^2 - y^2, v = x^2 + y^2$ over $x^2 - y^2 = 1, x^2 - y^2 = 4, x^2 + y^2 = 9, x^2 + y^2 = 16$.
46. $\iint_R (x^4 - y^4)e^{xy}\,dA$ with $u = xy, v = x^2 - y^2$ over $xy = 1, xy = 3, x^2 - y^2 = 3, x^2 - y^2 = 4$.

47. Volume of oblique parallelepiped bounded by $x + y + 2z = \pm 3, x - 2y + z = \pm 2, 4x + y + z = \pm 6$ is $V = 16$.
48. (a) Show cylindrical Jacobian is $r$. (b) Show spherical Jacobian is $\rho^2\sin\phi$.
49–50 **Writing.** Motivations for multivariable substitutions; level curves and coordinate choice.

#### QUICK CHECK ANSWERS 14.7
1. (a) Parallelogram with vertices $(1, 3), (-3, 5), (-1, 11), (3, 9)$ (b) $u = \frac{1}{7}(x + 2y), v = \frac{1}{7}(y - 3x)$  
2. $S$ is a region in the $uv$-plane and $R$ is the image of $S$ in the $xy$-plane under $T$  
3. (a) 7 (b) $\int_0^2 \int_1^3 7e^{7u}\,du\,dv$  
4. $2vw$

---

## 14.8 CENTERS OF GRAVITY USING MULTIPLE INTEGRALS

### DENSITY & MASS OF AN INHOMOGENEOUS LAMINA

Density: $\delta(x, y) = \lim_{\Delta A \to 0}\frac{\Delta M}{\Delta A} \tag{1}$.

> **14.8.1 THEOREM (Mass of a Lamina)**  
> $$M = \iint_R \delta(x, y)\,dA \tag{3}$$

#### Example 1
Triangular lamina with vertices $(0, 0), (0, 1), (1, 0)$ and $\delta(x, y) = xy$:
$$M = \iint_R xy\,dA = \int_0^1 \int_0^{1-x} xy\,dy\,dx = \int_0^1 \left(\frac{1}{2}x^3 - x^2 + \frac{1}{2}x\right)dx = \frac{1}{24}$$

---

### CENTER OF GRAVITY & CENTROID OF A LAMINA

Moments: $M_y = \iint_R x\delta(x, y)\,dA, \quad M_x = \iint_R y\delta(x, y)\,dA$.

> **Center of Gravity $(\bar{x}, \bar{y})$ of a Lamina:**
> $$\bar{x} = \frac{M_y}{M} = \frac{\iint_R x\delta(x, y)\,dA}{\iint_R \delta(x, y)\,dA}, \quad \bar{y} = \frac{M_x}{M} = \frac{\iint_R y\delta(x, y)\,dA}{\iint_R \delta(x, y)\,dA} \tag{9–12}$$

> **Centroid $(\bar{x}, \bar{y})$ of a Region $R$:**
> $$\bar{x} = \frac{1}{\text{area of } R}\iint_R x\,dA, \quad \bar{y} = \frac{1}{\text{area of } R}\iint_R y\,dA \tag{13–14}$$

#### Example 2
Center of gravity of lamina in Example 1:
$$M_y = \int_0^1 \int_0^{1-x} x^2 y\,dy\,dx = \frac{1}{60}, \quad M_x = \int_0^1 \int_0^{1-x} xy^2\,dy\,dx = \frac{1}{60} \implies (\bar{x}, \bar{y}) = \left(\frac{2}{5}, \frac{2}{5}\right)$$

#### Example 3
Centroid of semicircle $y = \sqrt{a^2 - x^2}$:
$$\bar{x} = 0, \quad \bar{y} = \frac{1}{\frac{1}{2}\pi a^2}\int_0^\pi \int_0^a (r\sin\theta)r\,dr\,d\theta = \frac{4a}{3\pi} \implies (\bar{x}, \bar{y}) = \left(0, \frac{4a}{3\pi}\right)$$

---

### CENTER OF GRAVITY & CENTROID OF A SOLID

* Mass: $M = \iiint_G \delta(x, y, z)\,dV \tag{15}$.
* Center of gravity: $\bar{x} = \frac{1}{M}\iiint_G x\delta\,dV, \; \bar{y} = \frac{1}{M}\iiint_G y\delta\,dV, \; \bar{z} = \frac{1}{M}\iiint_G z\delta\,dV \tag{16}$.
* Centroid: $\bar{x} = \frac{1}{V}\iiint_G x\,dV, \; \bar{y} = \frac{1}{V}\iiint_G y\,dV, \; \bar{z} = \frac{1}{V}\iiint_G z\,dV \tag{17}$.

#### Example 4
Cylindrical solid $x^2 + y^2 \le a^2, 0 \le z \le h$ with $\delta = kz$:
$$M = \frac{1}{2}kh^2\pi a^2, \quad \bar{z} = \frac{2}{3}h \implies (\bar{x}, \bar{y}, \bar{z}) = \left(0, 0, \frac{2}{3}h\right)$$

#### Example 5
Centroid of solid between $z = \sqrt{x^2+y^2}$ and sphere $x^2 + y^2 + z^2 = 16$:
$$V = \frac{64\pi}{3}(2 - \sqrt{2}), \quad \bar{z} = \frac{1}{V}\int_0^{2\pi} \int_0^{\pi/4} \int_0^4 (\rho\cos\phi)\rho^2\sin\phi\,d\rho\,d\phi\,d\theta = \frac{3}{2(2-\sqrt{2})} \approx 2.561$$

---

### QUICK CHECK EXERCISES 14.8
*(See page 1080 for answers.)*

1. Total mass of lamina with continuous density $\delta(x, y)$ over $R$: $M = \underline{\quad}$.
2. $\bar{x} = M_y / M$, where $M_y$ is called the $\underline{\quad}$ and is given by double integral $\underline{\quad}$.
3. Centroid of region between $y = x^2$ and $y = 2 - x$ for $0 \le x \le 1$ ($\text{Area} = 7/6$): $\underline{\quad}$.

---

### EXERCISE SET 14.8

**1–4 Find the mass and center of gravity of the lamina.**
1. A lamina with density $\delta(x, y) = x + y$ is bounded by the $x$-axis, the line $x = 1$, and the curve $y = \sqrt{x}$.
2. A lamina with density $\delta(x, y) = y$ is bounded by $y = \sin x, y = 0, x = 0,$ and $x = \pi$.
3. A lamina with density $\delta(x, y) = xy$ is in the first quadrant and is bounded by the circle $x^2 + y^2 = a^2$ and the coordinate axes.
4. A lamina with density $\delta(x, y) = x^2 + y^2$ is bounded by the $x$-axis and the upper half of the circle $x^2 + y^2 = 1$.

#### FOCUS ON CONCEPTS
**5–6 For the given density function, make a conjecture about the coordinates of the center of gravity and confirm by integrating.**
5. $\delta(x, y) = |x + y - 1|$ on $[0, 1] \times [0, 1]$.
6. $\delta(x, y) = 1 + x^2 + y^2$ on $[0, 1] \times [0, 1]$.

**7–8 Make a conjecture about the centroid of the region and confirm by integrating.**
7. Unit cube in first octant.
8. Right circular cylinder of radius 1 and height 2 centered on $z$-axis with base in $xy$-plane.

**9–12 True–False Determine whether the statement is true or false. Explain your answer.**
9. The center of gravity of a homogeneous lamina in a plane is located at the lamina's centroid.
10. The mass of a two-dimensional lamina is the product of its area and the density of the lamina at its centroid.
11. The coordinates of the center of gravity of a two-dimensional lamina are the lamina's first moments about the $y$- and $x$-axes, respectively.
12. The density of a solid in 3-space is measured in units of mass per unit area.

13. Show that in polar coordinates the formulas for the centroid $(\bar{x}, \bar{y})$ of a region $R$ are:
    $$\bar{x} = \frac{1}{\text{area of } R}\iint_R r^2\cos\theta\,dr\,d\theta, \quad \bar{y} = \frac{1}{\text{area of } R}\iint_R r^2\sin\theta\,dr\,d\theta$$

**14–17 Use the result of Exercise 13 to find the centroid $(\bar{x}, \bar{y})$ of the region.**
14. The region enclosed by the cardioid $r = a(1 + \sin\theta)$.
15. The petal of the rose $r = \sin 2\theta$ in the first quadrant.
16. The region above the $x$-axis and between the circles $x^2 + y^2 = a^2$ and $x^2 + y^2 = b^2 \; (a < b)$.
17. The region enclosed between the $y$-axis and the right half of the circle $x^2 + y^2 = a^2$.

18. Let $R$ be the rectangle bounded by $x = 0, x = 3, y = 0, y = 2$. By inspection, find the centroid of $R$ and use it to evaluate $\iint_R x\,dA$ and $\iint_R y\,dA$.

**19–24 Find the centroid of the solid.**
19. The tetrahedron in the first octant enclosed by the coordinate planes and the plane $x + y + z = 1$.
20. The solid bounded by the parabolic cylinder $z = 1 - y^2$ and the planes $x + z = 1, x = 0, z = 0$.
21. The solid bounded by the surface $z = y^2$ and the planes $x = 0, x = 1, z = 1$.
22. The solid in the first octant bounded by $z = xy$ and planes $z = 0, x = 2, y = 2$.
23. The solid in the first octant bounded by the sphere $x^2 + y^2 + z^2 = a^2$ and coordinate planes.
24. The solid enclosed by the $xy$-plane and the hemisphere $z = \sqrt{a^2 - x^2 - y^2}$.

**25–28 Find the mass and center of gravity of the solid.**
25. The cube with density $\delta(x, y, z) = a - x$ defined by $0 \le x \le a, 0 \le y \le a, 0 \le z \le a$.
26. The cylindrical solid with density $\delta(x, y, z) = h - z$ enclosed by $x^2 + y^2 = a^2, z = 0, z = h$.
27. The solid with density $\delta(x, y, z) = yz$ enclosed by $z = 1 - y^2 \; (y \ge 0), z = 0, y = 0, x = -1, x = 1$.
28. The solid with density $\delta(x, y, z) = xz$ enclosed by $y = 9 - x^2 \; (x \ge 0), x = 0, y = 0, z = 0, z = 1$.

29. Center of gravity of square lamina $[0, 1] \times [0, 1]$ if:  
    (a) Density proportional to square of distance from origin.  
    (b) Density proportional to distance from $y$-axis.
30. Center of gravity of cube $[0, 1]^3$ if:  
    (a) Density proportional to square of distance to origin.  
    (b) Density proportional to sum of distances to coordinate planes.
31. [CAS] Approximate centroid of solid bounded above by $z = 1/(1 + x^2 + y^2)$, below by $xy$-plane, laterally by $y = 0$ and $y = \sin x \; (0 \le x \le \pi)$.
32. Solid bounded above by $z = 1/(x^2 + y^2 + 1)$, below by $xy$-plane, laterally by $x^2 + y^2 = a^2$:  
    (a) Behavior of $\bar{z}$ as $a \to 0^+$ and $a \to +\infty$.  
    (b) Exact formula for $\bar{z}$ and limits.  
    (c) Estimate $a$ for centroid $(0, 0, 0.25)$.

**33–34 Use cylindrical coordinates.**
33. Mass of solid with density $\delta(x, y, z) = 3 - z$ bounded by cone $z = \sqrt{x^2+y^2}$ and plane $z = 3$.
34. Mass of cylinder $r \le a, 0 \le z \le h$ if density proportional to distance from base ($\delta = kz$).

**35–36 Use spherical coordinates.**
35. Mass of sphere of radius $a$ if density proportional to distance from center ($\delta = k\rho$).
36. Mass of solid between spheres $\rho = 1$ and $\rho = 2$ with density $\delta = (x^2 + y^2 + z^2)^{-1/2}$.

**37–38 Use cylindrical coordinates to find the centroid of the solid.**
37. Solid bounded above by sphere $x^2 + y^2 + z^2 = 2$ and below by paraboloid $z = x^2 + y^2$.
38. Solid bounded by cone $z = \sqrt{x^2+y^2}$ and plane $z = 2$.

**39–40 Use the Wallis sine and cosine formulas.**
39. Centroid of solid bounded above by $z = x^2 + y^2$, below by $z = 0$, laterally by $(x - 1)^2 + y^2 = 1$.
40. Mass of solid in first octant bounded above by $z = 4 - x^2 - y^2$, below by $z = 0$, laterally by $x^2 + y^2 = 2x, y = 0$, with $\delta = z$.

**41–42 Use spherical coordinates to find the centroid of the solid.**
41. Solid in first octant bounded by coordinate planes and sphere $x^2 + y^2 + z^2 = a^2$.
42. Solid bounded above by sphere $\rho = 4$ and below by cone $\phi = \pi/3$.

43. Mass of solid inside sphere $x^2 + y^2 + z^2 = 1$ above cone $z = \sqrt{x^2+y^2}$ with $\delta = \sqrt{x^2+y^2+z^2}$.
44. Center of gravity of solid bounded by $z = 1 - x^2 - y^2$ and $xy$-plane with $\delta = x^2 + y^2 + z^2$.
45. Center of gravity of solid bounded by cylinder $x^2 + y^2 = 1$, cone $z = \sqrt{x^2+y^2}$, and $xy$-plane with $\delta = z$.
46. Center of gravity of hemisphere $z = \sqrt{a^2-x^2-y^2}$ if density is proportional to distance from origin.
47. Centroid of solid enclosed by hemispheres $y = \sqrt{9-x^2-z^2}, y = \sqrt{4-x^2-z^2},$ and $y = 0$.
48. Stellar mass model with density $\delta = \delta_0 e^{-(\rho/R)^3}$.

**49–50 Moments of Inertia of a Lamina:**
$$I_x = \iint_R y^2\delta(x, y)\,dA, \quad I_y = \iint_R x^2\delta(x, y)\,dA, \quad I_z = \iint_R (x^2 + y^2)\delta(x, y)\,dA$$
49. Rectangular lamina $[0, a] \times [0, b]$ with constant density $\delta$: show $I_x = \frac{\delta a b^3}{3}, I_y = \frac{\delta a^3 b}{3}, I_z = \frac{\delta a b(a^2 + b^2)}{3}$.
50. Circular lamina $x^2 + y^2 \le a^2$ with constant density $\delta$: show $I_x = I_y = \frac{\delta\pi a^4}{4}, I_z = \frac{\delta\pi a^4}{2}$.

**51–54 Moments of Inertia of a Solid:**
$$I_x = \iiint_G (y^2 + z^2)\delta\,dV, \quad I_y = \iiint_G (x^2 + z^2)\delta\,dV, \quad I_z = \iiint_G (x^2 + y^2)\delta\,dV$$
51. $I_z$ for solid cylinder $x^2 + y^2 \le a^2, 0 \le z \le h$.
52. $I_y$ for solid cylinder $x^2 + y^2 \le a^2, 0 \le z \le h$.
53. $I_z$ for hollow cylinder $a_1^2 \le x^2 + y^2 \le a_2^2, 0 \le z \le h$.
54. $I_z$ for solid sphere $x^2 + y^2 + z^2 \le a^2$.

**55–59 Theorem of Pappus:**  
$\text{volume} = (\text{area of } R) \cdot (\text{distance traveled by centroid})$.
55. Prove the Theorem of Pappus: (a) subregions (b) $V = \iint_R 2\pi x\,dA = 2\pi\bar{x}A$.
56. Volume revolving semicircle $y = \sqrt{a^2-x^2}$ about: (a) $y = -a$ (b) $y = x - a$.
57. Elliptical torus volume revolving $(x - k)^2/a^2 + y^2/b^2 = 1$ about $y$-axis ($k > a$): $V = 2\pi^2 k a b$.
58. Volume revolving region between $y = x^2$ and $y = 8 - x^2$ about $x$-axis.
59. Centroid of right triangle with vertices $(0, 0), (a, 0), (0, b)$ using Pappus.
60. Volume of helical tube of radius $1/2$ along $x = \cos t, y = \sin t, z = t/4 \; (0 \le t \le 4\pi)$.
61. **Writing.** Physical interpretation of center of gravity.

#### QUICK CHECK ANSWERS 14.8
1. $\iint_R \delta(x, y)\,dA$  
2. first moment about the $y$-axis; $\iint_R x\delta(x, y)\,dA$  
3. $(5/14, 32/35)$

---

## CHAPTER 14 REVIEW EXERCISES

1. The double integral over a region $R$ in the $xy$-plane is defined as $\iint_R f(x, y)\,dA = \lim_{n \to +\infty}\sum_{k=1}^n f(x_k^*, y_k^*)\Delta A_k$. Describe the procedure on which this definition is based.
2. The triple integral over a solid $G$ in an $xyz$-coordinate system is defined as $\iiint_G f(x, y, z)\,dV = \lim_{n \to +\infty}\sum_{k=1}^n f(x_k^*, y_k^*, z_k^*)\Delta V_k$. Describe the procedure on which this definition is based.
3. (a) Express the area of a region $R$ in the $xy$-plane as a double integral.  
   (b) Express the volume of a region $G$ in an $xyz$-coordinate system as a triple integral.  
   (c) Express the area of the portion of the surface $z = f(x, y)$ that lies above the region $R$ in the $xy$-plane as a double integral.
4. (a) Write down parametric equations for a sphere of radius $a$ centered at the origin.  
   (b) Write down parametric equations for the right circular cylinder of radius $a$ and height $h$ that is centered on the $z$-axis, has its base in the $xy$-plane, and extends in the positive $z$-direction.
5. Let $R$ be the region in Figure Ex-5 ($0 \le y \le 1, 1 - \sqrt{1-y^2} \le x \le 1 + \sqrt{1-y^2}$). Fill in the missing limits of integration in $\int_{\square}^{\square} \int_{\square}^{\square} f(x, y)\,dx\,dy$.
6. Let $R$ be the region shown in Figure Ex-6. Fill in the missing limits of integration in $\int_0^2 \int_{\square}^{\square} f(x, y)\,dy\,dx + \int_2^3 \int_{\square}^{\square} f(x, y)\,dy\,dx$.
7. (a) Find constants $a, b, c, d$ such that $x = au + bv, y = cu + dv$ maps unit square $S$ into parallelogram $R$ with vertices $(0, 0), (2, 1), (3, 3), (1, 2)$.  
   (b) Find the area of the parallelogram $R$ by integrating over $S$, and check using geometry.
8. Give a geometric argument to show that $0 < \int_0^\pi \int_0^\pi \sin\sqrt{xy}\,dy\,dx < \pi^2$.
9. Evaluate $\int_{1/2}^1 \int_0^{2x} \cos(\pi x^2)\,dy\,dx$.
10. Evaluate $\int_0^2 \int_{-y}^{2y} x e^{y^3}\,dx\,dy$.
11. Express $\int_0^2 \int_0^{x/2} e^x e^y\,dy\,dx$ with order of integration reversed.
12. Express $\int_0^\pi \int_y^\pi \frac{\sin x}{x}\,dx\,dy$ with order of integration reversed.
13. Sketch the region whose area is represented by $\int_0^{\pi/2} \int_{\tan(x/2)}^{\sin x} dy\,dx$.
14. Sketch the region whose area is represented by $\int_{\pi/6}^{\pi/2} \int_a^{a(1+\cos\theta)} r\,dr\,d\theta \quad (a > 0)$.
15. Evaluate $\iint_R x^2\sin y^2\,dA$, where $R$ is bounded by $y = x^3, y = -x^3, y = 8$.
16. Evaluate $\iint_R (4 - x^2 - y^2)\,dA$, where $R$ is first-quadrant sector bounded by $x^2 + y^2 = 4$ and coordinate axes.
17. Convert to rectangular coordinates and evaluate: $\int_0^{\pi/2} \int_0^{2a\sin\theta} r\sin 2\theta\,dr\,d\theta$.
18. Convert to polar coordinates and evaluate: $\int_0^{\sqrt{2}} \int_x^{\sqrt{4-x^2}} 4xy\,dy\,dx$.
19. Find the area of the region bounded by $y = 2x^3, 2x + y = 4,$ and the $x$-axis using a double integral.
20. Find the area of the region enclosed by the rose $r = \cos 3\theta$.
21. Convert to cylindrical coordinates and evaluate: $\int_{-2}^2 \int_{-\sqrt{4-x^2}}^{\sqrt{4-x^2}} \int_{(x^2+y^2)^2}^{16} x^2\,dz\,dy\,dx$.
22. Convert to spherical coordinates and evaluate: $\int_0^1 \int_0^{\sqrt{1-x^2}} \int_0^{\sqrt{1-x^2-y^2}} \frac{1}{1 + x^2 + y^2 + z^2}\,dz\,dy\,dx$.
23. Let $G$ be the region bounded above by sphere $\rho = a$ and below by cone $\phi = \pi/3$. Express $\iiint_G (x^2 + y^2)\,dV$ in (a) spherical (b) cylindrical (c) rectangular coordinates.
24. Let $G = \{(x, y, z) : x^2 + y^2 \le z \le 4x\}$. Express volume of $G$ in (a) rectangular (b) cylindrical coordinates.
25. Find the volume bounded below by cone $\phi = \pi/6$ and above by plane $z = a$.
26. Find the volume enclosed between surfaces $x = y^2 + z^2$ and $x = 1 - y^2$.
27. Area of portion of $z = 3y + 2x^2 + 4$ above triangle $(0, 0), (1, 1), (1, -1)$.
28. Surface area of portion of hyperbolic paraboloid $\mathbf{r}(u, v) = (u + v)\mathbf{i} + (u - v)\mathbf{j} + uv\mathbf{k}$ for $u^2 + v^2 \le 4$.
29. Tangent plane to $\mathbf{r} = u\mathbf{i} + v\mathbf{j} + (u^2 + v^2)\mathbf{k}$ at $u = 1, v = 2$.
30. Tangent plane to $x = u\cosh v, y = u\sinh v, z = u^2$ at $(-3, 0, 9)$.
31. Describe the procedure for transforming a double integral over $R$ to an integral over $S$ in the $uv$-plane.
32. Use $u = x - 3y, v = 3x + y$ to find $\iint_R \frac{x-3y}{(3x+y)^2}\,dA$ over $x - 3y = 0, x - 3y = 4, 3x + y = 1, 3x + y = 3$.
33. Solid $G: 1 - e^x \le y \le 3 - e^x, 1 - y \le 2z \le 2 - y, y \le e^x \le y + 4$:  
    (a) Find Jacobian $\partial(x, y, z)/\partial(u, v, w)$ for $u = e^x + y, v = y + 2z, w = e^x - y$.  
    (b) Find volume of $G$.
34. Find average distance from a point inside sphere of radius $a$ to the center.
35. Find centroid of region bounded by $y^2 = 4x$ and $y^2 = 8(x - 2)$.
36. Find centroid of upper half of ellipse $(x/a)^2 + (y/b)^2 = 1$.
37. Find centroid of solid cone with vertex $(0, 0, h)$ and base $x^2 + y^2 \le a^2$ in $xy$-plane.
38. Find centroid of solid bounded by $y = x^2, z = 0, y + z = 4$.

---

## CHAPTER 14 MAKING CONNECTIONS

1. Gaussian integral $I = \int_0^{+\infty} e^{-x^2}\,dx$:  
   (a) Show $I^2 = \int_0^{+\infty}\int_0^{+\infty} e^{-(x^2+y^2)}\,dx\,dy$.  
   (b) Evaluate in polar coordinates: $I^2 = \int_0^{\pi/2}\int_0^{+\infty} e^{-r^2}r\,dr\,d\theta = \pi/4$.  
   (c) Conclude $I = \sqrt{\pi}/2$.
2. Show that $\int_0^{+\infty} \int_0^{+\infty} \frac{1}{(1 + x^2 + y^2)^2}\,dx\,dy = \frac{\pi}{4}$.
3. [CAS] (a) Numerical approximation of $\int_{-1}^1 \int_0^{\sqrt{1-x^2}} e^{-(x^2+y^2)^2}\,dy\,dx$.  
   (b) Compare to polar conversion approximation.
4. [CAS] (a) Find region $G$ maximizing $\iiint_G (1 - x^2 - y^2 - z^2)\,dV$ (the unit ball).  
   (b) Numerical CAS approximation of max value.  
   (c) Exact maximum value: $\frac{8\pi}{15}$.
5. [CAS] **Astroidal sphere** $x^{2/3} + y^{2/3} + z^{2/3} = a^{2/3}$:  
   (a) Parametric representation $x = a(\sin u\cos v)^3, y = a(\sin u\sin v)^3, z = a(\cos u)^3 \; (0 \le u \le \pi, 0 \le v \le 2\pi)$.  
   (b) Surface area for $a = 1$: $\approx 4.4506$.
6. Find volume of astroidal sphere using transformation $x = \rho(\sin\phi\cos\theta)^3, y = \rho(\sin\phi\sin\theta)^3, z = \rho\cos^3\phi \; (0 \le \rho \le a, 0 \le \phi \le \pi, 0 \le \theta \le 2\pi)$:
   $$V = \frac{4}{35}\pi a^3$$
