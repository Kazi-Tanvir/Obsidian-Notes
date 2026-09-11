# CHAPTER 5: APPLICATIONS OF THE DEFINITE INTEGRAL IN GEOMETRY, SCIENCE, AND ENGINEERING

*Calculus is essential for the computations required to land an astronaut on the Moon.*

In the last chapter we introduced the definite integral as the limit of Riemann sums in the context of finding areas. However, Riemann sums and definite integrals have applications that extend far beyond the area problem. In this chapter we will show how Riemann sums and definite integrals arise in such problems as finding the volume and surface area of a solid, finding the length of a plane curve, calculating the work done by a force, finding the center of gravity of a planar region, and finding the pressure and force exerted by a fluid on a submerged object.

Although these problems are diverse, the required calculations can all be approached by the same procedure that we used to find areas—breaking the required calculation into “small parts,” making an approximation for each part, adding the approximations from the parts to produce a Riemann sum that approximates the entire quantity to be calculated, and then taking the limit of the Riemann sums to produce an exact result.

---

## 5.1 AREA BETWEEN TWO CURVES

In the last chapter we showed how to find the area between a curve $y = f(x)$ and an interval on the $x$-axis. Here we will show how to find the area between two curves.

### A REVIEW OF RIEMANN SUMS

Before we consider the problem of finding the area between two curves it will be helpful to review the basic principle that underlies the calculation of area as a definite integral. Recall that if $f$ is continuous and nonnegative on $[a, b]$, then the definite integral for the area $A$ under $y = f(x)$ over the interval $[a, b]$ is obtained in four steps (Figure 5.1.1):

* Divide the interval $[a, b]$ into $n$ subintervals, and use those subintervals to divide the region under the curve $y = f(x)$ into $n$ strips.
* Assuming that the width of the $k$th strip is $\Delta x_k$, approximate the area of that strip by the area $f(x_k^*) \Delta x_k$ of a rectangle of width $\Delta x_k$ and height $f(x_k^*)$, where $x_k^*$ is a point in the $k$th subinterval.
* Add the approximate areas of the strips to approximate the entire area $A$ by the Riemann sum:
  $$A \approx \sum_{k=1}^n f(x_k^*) \Delta x_k$$
* Take the limit of the Riemann sums as the number of subintervals increases and all their widths approach zero. This causes the error in the approximations to approach zero and produces the following definite integral for the exact area $A$:
  $$A = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n f(x_k^*) \Delta x_k = \int_a^b f(x) dx$$

Figure 5.1.2 illustrates the effect that the limit process has on the various parts of the Riemann sum:
* The quantity $x_k^*$ in the Riemann sum becomes the variable $x$ in the definite integral.
* The interval width $\Delta x_k$ in the Riemann sum becomes the $dx$ in the definite integral.
* The interval $[a, b]$, which is the union of the subintervals with widths $\Delta x_1, \Delta x_2, \dots, \Delta x_n$, does not appear explicitly in the Riemann sum but is represented by the upper and lower limits of integration in the definite integral.

---

### AREA BETWEEN $y = f(x)$ AND $y = g(x)$

We will now consider the following extension of the area problem.

> **5.1.1 FIRST AREA PROBLEM**  
> Suppose that $f$ and $g$ are continuous functions on an interval $[a, b]$ and $f(x) \ge g(x)$ for $a \le x \le b$.  
> [This means that the curve $y = f(x)$ lies above the curve $y = g(x)$ and that the two can touch but not cross.] Find the area $A$ of the region bounded above by $y = f(x)$, below by $y = g(x)$, and on the sides by the lines $x = a$ and $x = b$ (Figure 5.1.3a).

To solve this problem we divide the interval $[a, b]$ into $n$ subintervals, which has the effect of subdividing the region into $n$ strips (Figure 5.1.3b). If we assume that the width of the $k$th strip is $\Delta x_k$, then the area of the strip can be approximated by the area of a rectangle of width $\Delta x_k$ and height $f(x_k^*) - g(x_k^*)$, where $x_k^*$ is a point in the $k$th subinterval. Adding these approximations yields the following Riemann sum that approximates the area $A$:
$$A \approx \sum_{k=1}^n [f(x_k^*) - g(x_k^*)] \Delta x_k$$

Taking the limit as $n$ increases and the widths of all the subintervals approach zero yields the following definite integral for the area $A$ between the curves:
$$A = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n [f(x_k^*) - g(x_k^*)] \Delta x_k = \int_a^b [f(x) - g(x)] dx$$

In summary, we have the following result.

> **5.1.2 AREA FORMULA**  
> If $f$ and $g$ are continuous functions on the interval $[a, b]$, and if $f(x) \ge g(x)$ for all $x$ in $[a, b]$, then the area of the region bounded above by $y = f(x)$, below by $y = g(x)$, on the left by the line $x = a$, and on the right by the line $x = b$ is
> $$A = \int_a^b [f(x) - g(x)] dx \tag{1}$$

#### Example 1
Find the area of the region bounded above by $y = x + 6$, bounded below by $y = x^2$, and bounded on the sides by the lines $x = 0$ and $x = 2$.

**Solution.** The region and a cross section are shown in Figure 5.1.4. The cross section extends from $g(x) = x^2$ on the bottom to $f(x) = x + 6$ on the top. If the cross section is moved through the region, then its leftmost position will be $x = 0$ and its rightmost position will be $x = 2$. Thus, from (1)
$$A = \int_0^2 [(x + 6) - x^2] dx = \left[\frac{x^2}{2} + 6x - \frac{x^3}{3}\right]_0^2 = \frac{34}{3} - 0 = \frac{34}{3}$$

It is possible that the upper and lower boundaries of a region may intersect at one or both endpoints, in which case the sides of the region will be points, rather than vertical line segments (Figure 5.1.5). When that occurs you will have to determine the points of intersection to obtain the limits of integration.

#### Example 2
Find the area of the region that is enclosed between the curves $y = x^2$ and $y = x + 6$.

**Solution.** A sketch of the region (Figure 5.1.6) shows that the lower boundary is $y = x^2$ and the upper boundary is $y = x + 6$. At the endpoints of the region, the upper and lower boundaries have the same $y$-coordinates; thus, to find the endpoints we equate
$$y = x^2 \quad\text{and}\quad y = x + 6 \tag{2}$$
This yields
$$x^2 = x + 6 \quad\text{or}\quad x^2 - x - 6 = 0 \quad\text{or}\quad (x + 2)(x - 3) = 0$$
from which we obtain $x = -2$ and $x = 3$.

Although the $y$-coordinates of the endpoints are not essential to our solution, they may be obtained from (2) by substituting $x = -2$ and $x = 3$ in either equation. This yields $y = 4$ and $y = 9$, so the upper and lower boundaries intersect at $(-2, 4)$ and $(3, 9)$.

From (1) with $f(x) = x + 6, g(x) = x^2, a = -2,$ and $b = 3$, we obtain the area
$$A = \int_{-2}^3 [(x + 6) - x^2] dx = \left[\frac{x^2}{2} + 6x - \frac{x^3}{3}\right]_{-2}^3 = \frac{27}{2} - \left(-\frac{22}{3}\right) = \frac{125}{6}$$

In the case where $f$ and $g$ are nonnegative on the interval $[a, b]$, the formula
$$A = \int_a^b [f(x) - g(x)] dx = \int_a^b f(x) dx - \int_a^b g(x) dx$$
states that the area $A$ between the curves can be obtained by subtracting the area under $y = g(x)$ from the area under $y = f(x)$ (Figure 5.1.7).

#### Example 3
Figure 5.1.8 shows velocity versus time curves for two race cars that move along a straight track, starting from rest at the same time. Give a physical interpretation of the area $A$ between the curves over the interval $0 \le t \le T$.

**Solution.** From (1)
$$A = \int_0^T [v_2(t) - v_1(t)] dt = \int_0^T v_2(t) dt - \int_0^T v_1(t) dt$$
Since $v_1$ and $v_2$ are nonnegative functions on $[0, T]$, it follows from Formula (4) of Section 4.7 that the integral of $v_1$ over $[0, T]$ is the distance traveled by car 1 during the time interval $0 \le t \le T$, and the integral of $v_2$ over $[0, T]$ is the distance traveled by car 2 during the same time interval. Since $v_1(t) \le v_2(t)$ on $[0, T]$, car 2 travels farther than car 1 does over the time interval $0 \le t \le T$, and the area $A$ represents the distance by which car 2 is ahead of car 1 at time $T$.

**Finding the Limits of Integration for the Area Between Two Curves**
* **Step 1.** Sketch the region and then draw a vertical line segment through the region at an arbitrary point $x$ on the $x$-axis, connecting the top and bottom boundaries (Figure 5.1.9a).
* **Step 2.** The $y$-coordinate of the top endpoint of the line segment sketched in Step 1 will be $f(x)$, the bottom one $g(x)$, and the length of the line segment will be $f(x) - g(x)$. This is the integrand in (1).
* **Step 3.** To determine the limits of integration, imagine moving the line segment left and then right. The leftmost position at which the line segment intersects the region is $x = a$ and the rightmost is $x = b$ (Figures 5.1.9b and 5.1.9c).

*There is a useful way of thinking about this procedure:*
If you view the vertical line segment as the “cross section” of the region at the point $x$, then Formula (1) states that the area between the curves is obtained by integrating the length of the cross section over the interval $[a, b]$.

It is possible for the upper or lower boundary of a region to consist of two or more different curves, in which case it will be convenient to subdivide the region into smaller pieces in order to apply Formula (1). This is illustrated in the next example.

#### Example 4
Find the area of the region enclosed by $x = y^2$ and $y = x - 2$.

**Solution.** To determine the appropriate boundaries of the region, we need to know where the curves $x = y^2$ and $y = x - 2$ intersect. In Example 2 we found intersections by equating the expressions for $y$. Here it is easier to rewrite the latter equation as $x = y + 2$ and equate the expressions for $x$, namely,
$$x = y^2 \quad\text{and}\quad x = y + 2 \tag{3}$$
This yields
$$y^2 = y + 2 \quad\text{or}\quad y^2 - y - 2 = 0 \quad\text{or}\quad (y + 1)(y - 2) = 0$$
from which we obtain $y = -1, y = 2$. Substituting these values in either equation in (3) we see that the corresponding $x$-values are $x = 1$ and $x = 4$, respectively, so the points of intersection are $(1, -1)$ and $(4, 2)$ (Figure 5.1.10a).

To apply Formula (1), the equations of the boundaries must be written so that $y$ is expressed explicitly as a function of $x$. The upper boundary can be written as $y = \sqrt{x}$ (rewrite $x = y^2$ as $y = \pm\sqrt{x}$ and choose the $+$ for the upper portion of the curve). The lower boundary consists of two parts:
$$y = -\sqrt{x} \quad\text{for } 0 \le x \le 1 \quad\text{and}\quad y = x - 2 \quad\text{for } 1 \le x \le 4$$
(Figure 5.1.10b). Because of this change in the formula for the lower boundary, it is necessary to divide the region into two parts and find the area of each part separately.

From (1) with $f(x) = \sqrt{x}, g(x) = -\sqrt{x}, a = 0,$ and $b = 1$, we obtain
$$A_1 = \int_0^1 [\sqrt{x} - (-\sqrt{x})] dx = 2\int_0^1 \sqrt{x} dx = 2\left[\frac{2}{3}x^{3/2}\right]_0^1 = \frac{4}{3} - 0 = \frac{4}{3}$$
From (1) with $f(x) = \sqrt{x}, g(x) = x - 2, a = 1,$ and $b = 4$, we obtain
$$A_2 = \int_1^4 [\sqrt{x} - (x - 2)] dx = \int_1^4 (\sqrt{x} - x + 2) dx = \left[\frac{2}{3}x^{3/2} - \frac{1}{2}x^2 + 2x\right]_1^4 = \left(\frac{16}{3} - 8 + 8\right) - \left(\frac{2}{3} - \frac{1}{2} + 2\right) = \frac{19}{6}$$
Thus, the area of the entire region is
$$A = A_1 + A_2 = \frac{4}{3} + \frac{19}{6} = \frac{9}{2}$$

---

### REVERSING THE ROLES OF $x$ AND $y$

Sometimes it is much easier to find the area of a region by integrating with respect to $y$ rather than $x$. We will now show how this can be done.

> **5.1.3 SECOND AREA PROBLEM**  
> Suppose that $w$ and $v$ are continuous functions of $y$ on an interval $[c, d]$ and that
> $$w(y) \ge v(y) \quad\text{for } c \le y \le d$$
> [This means that the curve $x = w(y)$ lies to the right of the curve $x = v(y)$ and that the two can touch but not cross.] Find the area $A$ of the region bounded on the left by $x = v(y)$, on the right by $x = w(y)$, and above and below by the lines $y = d$ and $y = c$ (Figure 5.1.11).

Proceeding as in the derivation of (1), but with the roles of $x$ and $y$ reversed, leads to the following analog of 5.1.2.

> **5.1.4 AREA FORMULA**  
> If $w$ and $v$ are continuous functions and if $w(y) \ge v(y)$ for all $y$ in $[c, d]$, then the area of the region bounded on the left by $x = v(y)$, on the right by $x = w(y)$, below by $y = c$, and above by $y = d$ is
> $$A = \int_c^d [w(y) - v(y)] dy \tag{4}$$

The guiding principle in applying this formula is the same as with (1): The integrand in (4) can be viewed as the length of the horizontal cross section at an arbitrary point $y$ on the $y$-axis, in which case Formula (4) states that the area can be obtained by integrating the length of the horizontal cross section over the interval $[c, d]$ on the $y$-axis (Figure 5.1.12).

In Example 4, we split the region into two parts to facilitate integrating with respect to $x$. In the next example we will see that splitting this region can be avoided if we integrate with respect to $y$.

#### Example 5
Find the area of the region enclosed by $x = y^2$ and $y = x - 2$, integrating with respect to $y$.

**Solution.** As indicated in Figure 5.1.10 the left boundary is $x = y^2$, the right boundary is $y = x - 2$, and the region extends over the interval $-1 \le y \le 2$. However, to apply (4) the equations for the boundaries must be written so that $x$ is expressed explicitly as a function of $y$. Thus, we rewrite $y = x - 2$ as $x = y + 2$. It now follows from (4) that
$$A = \int_{-1}^2 [(y + 2) - y^2] dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_{-1}^2 = \frac{9}{2}$$
which agrees with the result obtained in Example 4.

---

### QUICK CHECK EXERCISES 5.1
*(See page 355 for answers.)*

1. An integral expression for the area of the region between the curves $y = 20 - 3x^2$ and $y = 3\sqrt{x}$ and bounded on the sides by $x = 0$ and $x = 2$ is $\underline{\hspace{1.5cm}}$.
2. An integral expression for the area of the parallelogram bounded by $y = 2x + 8, y = 2x - 3, x = -1,$ and $x = 5$ is $\underline{\hspace{1.5cm}}$. The value of this integral is $\underline{\hspace{1.5cm}}$.
3. (a) The points of intersection for the circle $x^2 + y^2 = 4$ and the line $y = x + 2$ are $\underline{\hspace{1cm}}$ and $\underline{\hspace{1cm}}$.  
   (b) Expressed as a definite integral with respect to $x$, $\underline{\hspace{1.5cm}}$ gives the area of the region inside the circle $x^2 + y^2 = 4$ and above the line $y = x + 2$.  
   (c) Expressed as a definite integral with respect to $y$, $\underline{\hspace{1.5cm}}$ gives the area of the region described in part (b).
4. The area of the region enclosed by the curves $y = x^2$ and $y = \sqrt[3]{x}$ is $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 5.1
1. $\int_0^2 [(20 - 3x^2) - 3\sqrt{x}] dx$  
2. $\int_{-1}^5 [(2x + 8) - (2x - 3)] dx; \quad 66$  
3. (a) $(-2, 0); \ (0, 2)$ (b) $\int_{-2}^0 [\sqrt{4 - x^2} - (x + 2)] dx$ (c) $\int_0^2 [(y - 2) + \sqrt{4 - y^2}] dy$  
4. $\frac{5}{12}$

---

### EXERCISE SET 5.1

**1–4 Find the area of the shaded region.**
1. Region bounded by $y = x^2 + 1, y = x, x = -1, x = 2$.
2. Region bounded by $y = \sqrt{x}, y = -\frac{1}{4}x, x = 4$.
3. Region bounded by $x = y, x = 1/y^2, y = 2$.
4. Region bounded by $x = -y, x = 2 - y^2, y = -2, y = 2$.

**5–6 Find the area of the shaded region by (a) integrating with respect to $x$ and (b) integrating with respect to $y$.**
5. Region enclosed by $y = x^2, y = 2x$, with intersection at $(2, 4)$.
6. Region enclosed by $y^2 = 4x, y = 2x - 4$, with intersections at $(1, -2)$ and $(4, 4)$.

**7–14 Sketch the region enclosed by the curves and find its area.**
7. $y = x^2, y = \sqrt{x}, x = \frac{1}{4}, x = 1$
8. $y = x^3 - 4x, y = 0, x = 0, x = 2$
9. $y = \cos 2x, y = 0, x = \pi/4, x = \pi/2$
10. $y = \sec^2 x, y = 2, x = -\pi/4, x = \pi/4$
11. $x = \sin y, x = 0, y = \pi/4, y = 3\pi/4$
12. $x^2 = y, x = y - 2$
13. $y = 2 + |x - 1|, y = -\frac{1}{5}x + 7$
14. $y = x, y = 4x, y = -x + 2$

**15–20 Use a graphing utility, where helpful, to find the area of the region enclosed by the curves.**
15. $y = x^3 - 4x^2 + 3x, y = 0$
16. $y = x^3 - 2x^2, y = 2x^2 - 3x$
17. $y = \sin x, y = \cos x, x = 0, x = 2\pi$
18. $y = x^3 - 4x, y = 0$
19. $x = y^3 - y, x = 0$
20. $x = y^3 - 4y^2 + 3y, x = y^2 - y$

**21–24 True–False Determine whether the statement is true or false. Explain your answer. [In each exercise, assume that $f$ and $g$ are distinct continuous functions on $[a, b]$ and that $A$ denotes the area of the region bounded by the graphs of $y = f(x), y = g(x), x = a,$ and $x = b$.]**
21. If $f$ and $g$ differ by a positive constant $c$, then $A = c(b - a)$.
22. If $\int_a^b [f(x) - g(x)] dx = -3$, then $A = 3$.
23. If $\int_a^b [f(x) - g(x)] dx = 0$, then the graphs of $y = f(x)$ and $y = g(x)$ cross at least once on $[a, b]$.
24. If $A = |\int_a^b [f(x) - g(x)] dx|$, then the graphs of $y = f(x)$ and $y = g(x)$ don’t cross on $[a, b]$.

25. [CAS] Use a CAS to find the area enclosed by $y = 3 - 2x$ and $y = x^6 + 2x^5 - 3x^4 + x^2$.
26. [CAS] Use a CAS to find the exact area enclosed by the curves $y = x^5 - 2x^3 - 3x$ and $y = x^3$.
27. Find a horizontal line $y = k$ that divides the area between $y = x^2$ and $y = 9$ into two equal parts.
28. Find a vertical line $x = k$ that divides the area enclosed by $x = \sqrt{y}, x = 2,$ and $y = 0$ into two equal parts.
29. (a) Find the area of the region enclosed by the parabola $y = 2x - x^2$ and the $x$-axis.  
   (b) Find the value of $m$ so that the line $y = mx$ divides the region in part (a) into two regions of equal area.
30. Find the area between the curve $y = \sin x$ and the line segment joining the points $(0, 0)$ and $(5\pi/6, 1/2)$ on the curve.

**31–33 Use Newton’s Method (Section 3.7), where needed, to approximate the $x$-coordinates of the intersections of the curves to at least four decimal places, and then use those approximations to approximate the area of the region.**
31. The region that lies below the curve $y = \sin x$ and above the line $y = 0.2x$, where $x \ge 0$.
32. The region enclosed by the graphs of $y = x^2$ and $y = \cos x$.
33. The region that is enclosed by the curves $y = x^2 - 1$ and $y = 2\sin x$.

34. [CAS] Referring to the accompanying figure, use a CAS to estimate the value of $k$ so that the areas of the shaded regions are equal.  
   *Source: This exercise is based on Problem A1 that was posed in the Fifty-Fourth Annual William Lowell Putnam Mathematical Competition.*

#### FOCUS ON CONCEPTS
35. Two racers in adjacent lanes move with velocity functions $v_1(t)\text{ m/s}$ and $v_2(t)\text{ m/s}$, respectively. Suppose that the racers are even at time $t = 60\text{ s}$. Interpret the value of the integral $\int_0^{60} [v_2(t) - v_1(t)] dt$ in this context.
36. The accompanying figure shows acceleration versus time curves for two cars that move along a straight track, accelerating from rest at the starting line. What does the area $A$ between the curves over the interval $0 \le t \le T$ represent? Justify your answer.
37. The curves in the accompanying figure model the birth rates and death rates (in millions of people per year) for a country over a 50-year period. What does the area $A$ between the curves over the interval $[1960, 2010]$ represent? Justify your answer.
38. The accompanying figure shows the rate at which transdermal medication is absorbed into the bloodstream of an individual, as well as the rate at which the medication is eliminated from the bloodstream by metabolization. Both rates are in units of micrograms per hour ($\mu\text{g/h}$) and are displayed over an 8-hour period. What does the area $A$ between the curves over the interval $[0, 8]$ represent? Justify your answer.
39. Find the area of the region enclosed between the curve $x^{1/2} + y^{1/2} = a^{1/2}$ and the coordinate axes.
40. Show that the area of the ellipse in the accompanying figure is $\pi ab$. [*Hint:* Use a formula from geometry.]
41. **Writing.** Suppose that $f$ and $g$ are continuous on $[a, b]$ but that the graphs of $y = f(x)$ and $y = g(x)$ cross several times. Describe a step-by-step procedure for determining the area bounded by the graphs of $y = f(x), y = g(x), x = a,$ and $x = b$.
42. **Writing.** Suppose that $R$ and $S$ are two regions in the $xy$-plane that lie between a pair of lines $L_1$ and $L_2$ that are parallel to the $y$-axis. Assume that each line between $L_1$ and $L_2$ that is parallel to the $y$-axis intersects $R$ and $S$ in line segments of equal length. Give an informal argument that the area of $R$ is equal to the area of $S$. (Make reasonable assumptions about the boundaries of $R$ and $S$.)

---

## 5.2 VOLUMES BY SLICING; DISKS AND WASHERS

In the last section we showed that the area of a plane region bounded by two curves can be obtained by integrating the length of a general cross section over an appropriate interval. In this section we will see that the same basic principle can be used to find volumes of certain three-dimensional solids.

### VOLUMES BY SLICING

Recall that the underlying principle for finding the area of a plane region is to divide the region into thin strips, approximate the area of each strip by the area of a rectangle, add the approximations to form a Riemann sum, and take the limit of the Riemann sums to produce an integral for the area. Under appropriate conditions, the same strategy can be used to find the volume of a solid. The idea is to divide the solid into thin slabs, approximate the volume of each slab, add the approximations to form a Riemann sum, and take the limit of the Riemann sums to produce an integral for the volume (Figure 5.2.1).

What makes this method work is the fact that a thin slab has a cross section that does not vary much in size or shape, which, as we will see, makes its volume easy to approximate (Figure 5.2.2). Moreover, the thinner the slab, the less variation in its cross sections and the better the approximation. Thus, once we approximate the volumes of the slabs, we can set up a Riemann sum whose limit is the volume of the entire solid. We will give the details shortly, but first we need to discuss how to find the volume of a solid whose cross sections do not vary in size and shape (i.e., are congruent).

One of the simplest examples of a solid with congruent cross sections is a right circular cylinder of radius $r$, since all cross sections taken perpendicular to the central axis are circular regions of radius $r$. The volume $V$ of a right circular cylinder of radius $r$ and height $h$ can be expressed in terms of the height and the area of a cross section as
$$V = \pi r^2 h = [\text{area of a cross section}] \times [\text{height}] \tag{1}$$

This is a special case of a more general volume formula that applies to solids called *right cylinders*. A **right cylinder** is a solid that is generated when a plane region is translated along a line or axis that is perpendicular to the region (Figure 5.2.3).

If a right cylinder is generated by translating a region of area $A$ through a distance $h$, then $h$ is called the **height** (or sometimes the **width**) of the cylinder, and the volume $V$ of the cylinder is defined to be
$$V = A \cdot h = [\text{area of a cross section}] \times [\text{height}] \tag{2}$$
(Figure 5.2.4). Note that this is consistent with Formula (1) for the volume of a right circular cylinder.

We now have all of the tools required to solve the following problem.

> **5.2.1 PROBLEM**  
> Let $S$ be a solid that extends along the $x$-axis and is bounded on the left and right, respectively, by the planes that are perpendicular to the $x$-axis at $x = a$ and $x = b$ (Figure 5.2.5). Find the volume $V$ of the solid, assuming that its cross-sectional area $A(x)$ is known at each $x$ in the interval $[a, b]$.

To solve this problem we begin by dividing the interval $[a, b]$ into $n$ subintervals, thereby dividing the solid into $n$ slabs as shown in the left part of Figure 5.2.6. If we assume that the width of the $k$th subinterval is $\Delta x_k$, then the volume of the $k$th slab can be approximated by the volume $A(x_k^*) \Delta x_k$ of a right cylinder of width (height) $\Delta x_k$ and cross-sectional area $A(x_k^*)$, where $x_k^*$ is a point in the $k$th subinterval (see the right part of Figure 5.2.6).

Adding these approximations yields the following Riemann sum that approximates the volume $V$:
$$V \approx \sum_{k=1}^n A(x_k^*) \Delta x_k$$

Taking the limit as $n$ increases and the widths of all the subintervals approach zero yields the definite integral
$$V = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n A(x_k^*) \Delta x_k = \int_a^b A(x) dx$$

In summary, we have the following result.

> **5.2.2 VOLUME FORMULA**  
> Let $S$ be a solid bounded by two parallel planes perpendicular to the $x$-axis at $x = a$ and $x = b$. If, for each $x$ in $[a, b]$, the cross-sectional area of $S$ perpendicular to the $x$-axis is $A(x)$, then the volume of the solid is
> $$V = \int_a^b A(x) dx \tag{3}$$
> provided $A(x)$ is integrable.

*It is understood in our calculations of volume that the units of volume are the cubed units of length [e.g., cubic inches ($\text{in}^3$) or cubic meters ($\text{m}^3$)].*

There is a similar result for cross sections perpendicular to the $y$-axis.

> **5.2.3 VOLUME FORMULA**  
> Let $S$ be a solid bounded by two parallel planes perpendicular to the $y$-axis at $y = c$ and $y = d$. If, for each $y$ in $[c, d]$, the cross-sectional area of $S$ perpendicular to the $y$-axis is $A(y)$, then the volume of the solid is
> $$V = \int_c^d A(y) dy \tag{4}$$
> provided $A(y)$ is integrable.

In words, these formulas state:
*The volume of a solid can be obtained by integrating the cross-sectional area from one end of the solid to the other.*

#### Example 1
Derive the formula for the volume of a right pyramid whose altitude is $h$ and whose base is a square with sides of length $a$.

**Solution.** As illustrated in Figure 5.2.7a, we introduce a rectangular coordinate system in which the $y$-axis passes through the apex and is perpendicular to the base, and the $x$-axis passes through the base and is parallel to a side of the base.

At any $y$ in the interval $[0, h]$ on the $y$-axis, the cross section perpendicular to the $y$-axis is a square. If $s$ denotes the length of a side of this square, then by similar triangles (Figure 5.2.7b)
$$\frac{\frac{1}{2}s}{\frac{1}{2}a} = \frac{h - y}{h} \quad\text{or}\quad s = \frac{a}{h}(h - y)$$
Thus, the area $A(y)$ of the cross section at $y$ is
$$A(y) = s^2 = \frac{a^2}{h^2}(h - y)^2$$
and by (4) the volume is
$$V = \int_0^h A(y) dy = \int_0^h \frac{a^2}{h^2}(h - y)^2 dy = \frac{a^2}{h^2}\int_0^h (h - y)^2 dy = \frac{a^2}{h^2}\left[-\frac{1}{3}(h - y)^3\right]_{y=0}^h = \frac{a^2}{h^2}\left[0 + \frac{1}{3}h^3\right] = \frac{1}{3}a^2 h$$
That is, the volume is $\frac{1}{3}$ of the area of the base times the altitude.

---

### SOLIDS OF REVOLUTION
A **solid of revolution** is a solid that is generated by revolving a plane region about a line that lies in the same plane as the region; the line is called the **axis of revolution**. Many familiar solids are of this type (Figure 5.2.8).

### VOLUMES BY DISKS PERPENDICULAR TO THE $x$-AXIS
We will be interested in the following general problem.

> **5.2.4 PROBLEM**  
> Let $f$ be continuous and nonnegative on $[a, b]$, and let $R$ be the region that is bounded above by $y = f(x)$, below by the $x$-axis, and on the sides by the lines $x = a$ and $x = b$ (Figure 5.2.9a). Find the volume of the solid of revolution that is generated by revolving the region $R$ about the $x$-axis.

We can solve this problem by slicing. For this purpose, observe that the cross section of the solid taken perpendicular to the $x$-axis at the point $x$ is a circular disk of radius $f(x)$ (Figure 5.2.9b). The area of this region is
$$A(x) = \pi [f(x)]^2$$
Thus, from (3) the volume of the solid is
$$V = \int_a^b \pi [f(x)]^2 dx \tag{5}$$
Because the cross sections are disk shaped, the application of this formula is called the **method of disks**.

#### Example 2
Find the volume of the solid that is obtained when the region under the curve $y = \sqrt{x}$ over the interval $[1, 4]$ is revolved about the $x$-axis (Figure 5.2.10).

**Solution.** From (5), the volume is
$$V = \int_a^b \pi [f(x)]^2 dx = \int_1^4 \pi x dx = \left[\frac{\pi x^2}{2}\right]_1^4 = 8\pi - \frac{\pi}{2} = \frac{15\pi}{2}$$

#### Example 3
Derive the formula for the volume of a sphere of radius $r$.

**Solution.** As indicated in Figure 5.2.11, a sphere of radius $r$ can be generated by revolving the upper semicircular disk enclosed between the $x$-axis and
$$x^2 + y^2 = r^2$$
about the $x$-axis. Since the upper half of this circle is the graph of $y = f(x) = \sqrt{r^2 - x^2}$, it follows from (5) that the volume of the sphere is
$$V = \int_a^b \pi [f(x)]^2 dx = \int_{-r}^r \pi (r^2 - x^2) dx = \pi \left[r^2 x - \frac{x^3}{3}\right]_{-r}^r = \frac{4}{3}\pi r^3$$

---

### VOLUMES BY WASHERS PERPENDICULAR TO THE $x$-AXIS
Not all solids of revolution have solid interiors; some have holes or channels that create interior surfaces, as in Figure 5.2.8d. So we will also be interested in problems of the following type.

> **5.2.5 PROBLEM**  
> Let $f$ and $g$ be continuous and nonnegative on $[a, b]$, and suppose that $f(x) \ge g(x)$ for all $x$ in the interval $[a, b]$. Let $R$ be the region that is bounded above by $y = f(x)$, below by $y = g(x)$, and on the sides by the lines $x = a$ and $x = b$ (Figure 5.2.12a). Find the volume of the solid of revolution that is generated by revolving the region $R$ about the $x$-axis (Figure 5.2.12b).

We can solve this problem by slicing. For this purpose, observe that the cross section of the solid taken perpendicular to the $x$-axis at the point $x$ is the annular or “washer-shaped” region with inner radius $g(x)$ and outer radius $f(x)$ (Figure 5.2.12b); its area is
$$A(x) = \pi [f(x)]^2 - \pi [g(x)]^2 = \pi \left([f(x)]^2 - [g(x)]^2\right)$$
Thus, from (3) the volume of the solid is
$$V = \int_a^b \pi \left([f(x)]^2 - [g(x)]^2\right) dx \tag{6}$$
Because the cross sections are washer shaped, the application of this formula is called the **method of washers**.

#### Example 4
Find the volume of the solid generated when the region between the graphs of the equations $f(x) = \frac{1}{2} + x^2$ and $g(x) = x$ over the interval $[0, 2]$ is revolved about the $x$-axis.

**Solution.** First sketch the region (Figure 5.2.13a); then imagine revolving it about the $x$-axis (Figure 5.2.13b). From (6) the volume is
$$V = \int_a^b \pi \left([f(x)]^2 - [g(x)]^2\right) dx = \int_0^2 \pi \left[\left(\frac{1}{2} + x^2\right)^2 - x^2\right] dx = \int_0^2 \pi \left(\frac{1}{4} + x^4\right) dx = \pi \left[\frac{x}{4} + \frac{x^5}{5}\right]_0^2 = \frac{69\pi}{10}$$

---

### VOLUMES BY DISKS AND WASHERS PERPENDICULAR TO THE $y$-AXIS
The methods of disks and washers have analogs for regions that are revolved about the $y$-axis (Figures 5.2.14 and 5.2.15). Using the method of slicing and Formula (4), you should be able to deduce the following formulas for the volumes of the solids in the figures:
$$V = \int_c^d \pi [u(y)]^2 dy \quad\text{(Disks)} \tag{7}$$
$$V = \int_c^d \pi \left([w(y)]^2 - [v(y)]^2\right) dy \quad\text{(Washers)} \tag{8}$$

#### Example 5
Find the volume of the solid generated when the region enclosed by $y = \sqrt{x}, y = 2,$ and $x = 0$ is revolved about the $y$-axis.

**Solution.** First sketch the region and the solid (Figure 5.2.16). The cross sections taken perpendicular to the $y$-axis are disks, so we will apply (7). But first we must rewrite $y = \sqrt{x}$ as $x = y^2$. Thus, from (7) with $u(y) = y^2$, the volume is
$$V = \int_c^d \pi [u(y)]^2 dy = \int_0^2 \pi y^4 dy = \left[\frac{\pi y^5}{5}\right]_0^2 = \frac{32\pi}{5}$$

---

### OTHER AXES OF REVOLUTION
It is possible to use the method of disks and the method of washers to find the volume of a solid of revolution whose axis of revolution is a line other than one of the coordinate axes. Instead of developing a new formula for each situation, we will appeal to Formulas (3) and (4) and integrate an appropriate cross-sectional area to find the volume.

#### Example 6
Find the volume of the solid generated when the region under the curve $y = x^2$ over the interval $[0, 2]$ is rotated about the line $y = -1$.

**Solution.** First sketch the region and the axis of revolution; then imagine revolving the region about the axis (Figure 5.2.17). At each $x$ in the interval $0 \le x \le 2$, the cross section of the solid perpendicular to the axis $y = -1$ is a washer with outer radius $x^2 + 1$ and inner radius $1$. Since the area of this washer is
$$A(x) = \pi \left([x^2 + 1]^2 - 1^2\right) = \pi (x^4 + 2x^2)$$
it follows by (3) that the volume of the solid is
$$V = \int_0^2 A(x) dx = \int_0^2 \pi (x^4 + 2x^2) dx = \pi \left[\frac{1}{5}x^5 + \frac{2}{3}x^3\right]_0^2 = \frac{176\pi}{15}$$

---

### QUICK CHECK EXERCISES 5.2
*(See page 365 for answers.)*

1. A solid $S$ extends along the $x$-axis from $x = 1$ to $x = 3$. For $x$ between 1 and 3, the cross-sectional area of $S$ perpendicular to the $x$-axis is $3x^2$. An integral expression for the volume of $S$ is $\underline{\hspace{1.5cm}}$. The value of this integral is $\underline{\hspace{1.5cm}}$.
2. A solid $S$ is generated by revolving the region between the $x$-axis and the curve $y = \sqrt{\sin x} \ (0 \le x \le \pi)$ about the $x$-axis.  
   (a) For $x$ between 0 and $\pi$, the cross-sectional area of $S$ perpendicular to the $x$-axis at $x$ is $A(x) = \underline{\hspace{1.5cm}}$.  
   (b) An integral expression for the volume of $S$ is $\underline{\hspace{1.5cm}}$.  
   (c) The value of the integral in part (b) is $\underline{\hspace{1.5cm}}$.
3. A solid $S$ is generated by revolving the region enclosed by the line $y = 2x + 1$ and the curve $y = x^2 + 1$ about the $x$-axis.  
   (a) For $x$ between $\underline{\hspace{1cm}}$ and $\underline{\hspace{1cm}}$, the cross-sectional area of $S$ perpendicular to the $x$-axis at $x$ is $A(x) = \underline{\hspace{1.5cm}}$.  
   (b) An integral expression for the volume of $S$ is $\underline{\hspace{1.5cm}}$.
4. A solid $S$ is generated by revolving the region enclosed by the line $y = x + 1$ and the curve $y = x^2 + 1$ about the $y$-axis.  
   (a) For $y$ between $\underline{\hspace{1cm}}$ and $\underline{\hspace{1cm}}$, the cross-sectional area of $S$ perpendicular to the $y$-axis at $y$ is $A(y) = \underline{\hspace{1.5cm}}$.  
   (b) An integral expression for the volume of $S$ is $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 5.2
1. $\int_1^3 3x^2 dx; \quad 26$  
2. (a) $\pi \sin x$ (b) $\int_0^\pi \pi \sin x dx$ (c) $2\pi$  
3. (a) $0; \ 2; \ \pi[(2x + 1)^2 - (x^2 + 1)^2] = \pi[-x^4 + 2x^2 + 4x]$ (b) $\int_0^2 \pi[-x^4 + 2x^2 + 4x] dx$  
4. (a) $1; \ 2; \ \pi[(y - 1) - (y - 1)^2] = \pi[-y^2 + 3y - 2]$ (b) $\int_1^2 \pi[-y^2 + 3y - 2] dy$

---

### EXERCISE SET 5.2

**1–8 Find the volume of the solid that results when the shaded region is revolved about the indicated axis.**
1. Region bounded by $y = \sqrt{3 - x}, x = -1, x = 2, y = 0$; revolved about the $x$-axis.
2. Region bounded by $y = x, y = 2 - x^2, x = 0$; revolved about the $x$-axis.
3. Region bounded by $y = 3 - 2x, x = 0, y = 0$; revolved about the $y$-axis.
4. Region bounded by $y = 1/x, x = 1, x = 2, y = 0$; revolved about the $y$-axis.
5. Region bounded by $y = \sqrt{\cos x}, x = 0, x = \pi/2, y = 0$; revolved about the $x$-axis.
6. Region bounded by $y = x^2, y = x^3$; revolved about the $x$-axis.
7. Region bounded by $x = \sqrt{1 + y}, y = 0, y = 3, x = 0$; revolved about the $y$-axis.
8. Region bounded by $y = x^2 - 1, x = 2, y = 0$; revolved about the $y$-axis.

9. Find the volume of the solid whose base is the region bounded between the curve $y = x^2$ and the $x$-axis from $x = 0$ to $x = 2$ and whose cross sections taken perpendicular to the $x$-axis are squares.
10. Find the volume of the solid whose base is the region bounded between the curve $y = \sec x$ and the $x$-axis from $x = \pi/4$ to $x = \pi/3$ and whose cross sections taken perpendicular to the $x$-axis are squares.

**11–14 Find the volume of the solid that results when the region enclosed by the given curves is revolved about the $x$-axis.**
11. $y = \sqrt{25 - x^2}, y = 3$
12. $y = 9 - x^2, y = 0$
13. $x = \sqrt{y}, x = y/4$
14. $y = \sin x, y = \cos x, x = 0, x = \pi/4$  
    [*Hint:* Use the identity $\cos 2x = \cos^2 x - \sin^2 x$.]

15. Find the volume of the solid whose base is the region bounded between the curve $y = x^3$ and the $y$-axis from $y = 0$ to $y = 1$ and whose cross sections taken perpendicular to the $y$-axis are squares.
16. Find the volume of the solid whose base is the region enclosed between the curve $x = 1 - y^2$ and the $y$-axis and whose cross sections taken perpendicular to the $y$-axis are squares.

**17–20 Find the volume of the solid that results when the region enclosed by the given curves is revolved about the $y$-axis.**
17. $x = \csc y, y = \pi/4, y = 3\pi/4, x = 0$
18. $y = x^2, x = y^2$
19. $x = y^2, x = y + 2$
20. $x = 1 - y^2, x = 2 + y^2, y = -1, y = 1$

**21–24 True–False Determine whether the statement is true or false. Explain your answer. [In these exercises, assume that a solid $S$ of volume $V$ is bounded by two parallel planes perpendicular to the $x$-axis at $x = a$ and $x = b$ and that for each $x$ in $[a, b]$, $A(x)$ denotes the cross-sectional area of $S$ perpendicular to the $x$-axis.]**
21. If each cross section of $S$ perpendicular to the $x$-axis is a square, then $S$ is a rectangular parallelepiped (i.e., is box shaped).
22. If each cross section of $S$ is a disk or a washer, then $S$ is a solid of revolution.
23. If $x$ is in centimeters (cm), then $A(x)$ must be a quadratic function of $x$, since units of $A(x)$ will be square centimeters ($\text{cm}^2$).
24. The average value of $A(x)$ on the interval $[a, b]$ is given by $V/(b - a)$.

25. Find the volume of the solid that results when the region above the $x$-axis and below the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \ (a > 0, b > 0)$ is revolved about the $x$-axis.
26. Let $V$ be the volume of the solid that results when the region enclosed by $y = 1/x, y = 0, x = 2,$ and $x = b \ (0 < b < 2)$ is revolved about the $x$-axis. Find the value of $b$ for which $V = 3$.
27. Find the volume of the solid generated when the region enclosed by $y = \sqrt{x + 1}, y = \sqrt{2x},$ and $y = 0$ is revolved about the $x$-axis. [*Hint:* Split the solid into two parts.]
28. Find the volume of the solid generated when the region enclosed by $y = \sqrt{x}, y = 6 - x,$ and $y = 0$ is revolved about the $x$-axis. [*Hint:* Split the solid into two parts.]

#### FOCUS ON CONCEPTS
29. Suppose that $f$ is a continuous function on $[a, b]$, and let $R$ be the region between the curve $y = f(x)$ and the line $y = k$ from $x = a$ to $x = b$. Using the method of disks, derive with explanation a formula for the volume of a solid generated by revolving $R$ about the line $y = k$. State and explain additional assumptions, if any, that you need about $f$ for your formula.
30. Suppose that $v$ and $w$ are continuous functions on $[c, d]$, and let $R$ be the region between the curves $x = v(y)$ and $x = w(y)$ from $y = c$ to $y = d$. Using the method of washers, derive with explanation a formula for the volume of a solid generated by revolving $R$ about the line $x = k$. State and explain additional assumptions, if any, that you need about $v$ and $w$ for your formula.
31. Consider the solid generated by revolving the shaded region in Exercise 1 about the line $y = 2$.  
   (a) Make a conjecture as to which is larger: the volume of this solid or the volume of the solid in Exercise 1. Explain the basis of your conjecture.  
   (b) Check your conjecture by calculating this volume and comparing it to the volume obtained in Exercise 1.
32. Consider the solid generated by revolving the shaded region in Exercise 4 about the line $x = 2.5$.  
   (a) Make a conjecture as to which is larger: the volume of this solid or the volume of the solid in Exercise 4. Explain the basis of your conjecture.  
   (b) Check your conjecture by expressing the difference in the two volumes as a single definite integral. [*Hint:* Sketch the graph of the integrand.]
33. Find the volume of the solid that results when the region enclosed by $y = \sqrt{x}, y = 0,$ and $x = 9$ is revolved about the line $x = 9$.
34. Find the volume of the solid that results when the region in Exercise 33 is revolved about the line $y = 3$.
35. Find the volume of the solid that results when the region enclosed by $x = y^2$ and $x = y$ is revolved about the line $y = -1$.
36. Find the volume of the solid that results when the region in Exercise 35 is revolved about the line $x = -1$.
37. Find the volume of the solid that results when the region enclosed by $y = x^2$ and $y = x^3$ is revolved about the line $x = 1$.
38. Find the volume of the solid that results when the region in Exercise 37 is revolved about the line $y = -1$.
39. A nose cone for a space reentry vehicle is designed so that a cross section, taken $x\text{ ft}$ from the tip and perpendicular to the axis of symmetry, is a circle of radius $\frac{1}{4}x^2\text{ ft}$. Find the volume of the nose cone given that its length is $20\text{ ft}$.
40. A certain solid is $1\text{ ft}$ high, and a horizontal cross section taken $x\text{ ft}$ above the bottom of the solid is an annulus of inner radius $x^2\text{ ft}$ and outer radius $\sqrt{x}\text{ ft}$. Find the volume of the solid.
41. Find the volume of the solid whose base is the region bounded between the curves $y = x$ and $y = x^2$, and whose cross sections perpendicular to the $x$-axis are squares.
42. The base of a certain solid is the region enclosed by $y = \sqrt{x}, y = 0,$ and $x = 4$. Every cross section perpendicular to the $x$-axis is a semicircle with its diameter across the base. Find the volume of the solid.
43. In parts (a)–(c) find the volume of the solid whose base is enclosed by the circle $x^2 + y^2 = 1$ and whose cross sections taken perpendicular to the $x$-axis are as indicated: (a) semicircles (b) squares (c) equilateral triangles.
44. As shown in the accompanying figure, a cathedral dome is designed with three semicircular supports of radius $r$ so that each horizontal cross section is a regular hexagon. Show that the volume of the dome is $r^3\sqrt{3}$.

**45–46 [CAS] Use a CAS to estimate the volume of the solid that results when the region enclosed by the curves is revolved about the stated axis.**
45. $y = \sin^8 x, y = 2x/\pi, x = 0, x = \pi/2$; $x$-axis
46. $y = \pi^2 \sin x \cos^3 x, y = 4x^2, x = 0, x = \pi/4$; $x$-axis

47. The accompanying figure shows a spherical cap of radius $\rho$ and height $h$ cut from a sphere of radius $r$. Show that the volume $V$ of the spherical cap can be expressed as  
   (a) $V = \frac{1}{3}\pi h^2(3r - h)$  
   (b) $V = \frac{1}{6}\pi h(3\rho^2 + h^2)$.
48. If fluid enters a hemispherical bowl with a radius of $10\text{ ft}$ at a rate of $\frac{1}{2}\text{ ft}^3\text{/min}$, how fast will the fluid be rising when the depth is $5\text{ ft}$? [*Hint:* See Exercise 47.]
49. The accompanying figure shows the dimensions of a small lightbulb at 10 equally spaced points.  
   (a) Use formulas from geometry to make a rough estimate of the volume enclosed by the glass portion of the bulb.  
   (b) Use the average of left and right endpoint approximations to approximate the volume.
50. Use the result in Exercise 47 to find the volume of the solid that remains when a hole of radius $r/2$ is drilled through the center of a sphere of radius $r$, and then check your answer by integrating.
51. As shown in the accompanying figure, a cocktail glass with a bowl shaped like a hemisphere of diameter $8\text{ cm}$ contains a cherry with a diameter of $2\text{ cm}$. If the glass is filled to a depth of $h\text{ cm}$, what is the volume of liquid it contains? [*Hint:* First consider the case where the cherry is partially submerged, then the case where it is totally submerged.]
52. Find the volume of the torus that results when the region enclosed by the circle of radius $r$ with center at $(h, 0), h > r,$ is revolved about the $y$-axis. [*Hint:* Use an appropriate formula from plane geometry to help evaluate the definite integral.]
53. A wedge is cut from a right circular cylinder of radius $r$ by two planes, one perpendicular to the axis of the cylinder and the other making an angle $\theta$ with the first. Find the volume of the wedge by slicing perpendicular to the $y$-axis as shown in the accompanying figure.
54. Find the volume of the wedge described in Exercise 53 by slicing perpendicular to the $x$-axis.
55. Two right circular cylinders of radius $r$ have axes that intersect at right angles. Find the volume of the solid common to the two cylinders. [*Hint:* One-eighth of the solid is sketched in the accompanying figure.]
56. In 1635 Bonaventura Cavalieri, a student of Galileo, stated the following result, called **Cavalieri’s principle**: *If two solids have the same height, and if the areas of their cross sections taken parallel to and at equal distances from their bases are always equal, then the solids have the same volume.* Use this result to find the volume of the oblique cylinder in the accompanying figure. (See Exercise 42 of Section 5.1 for a planar version of Cavalieri’s principle.)
57. **Writing.** Use the results of this section to derive Cavalieri’s principle (Exercise 56).
58. **Writing.** Write a short paragraph that explains how Formulas (4)–(8) may all be viewed as consequences of Formula (3).

---

## 5.3 VOLUMES BY CYLINDRICAL SHELLS

The methods for computing volumes that have been discussed so far depend on our ability to compute the cross-sectional area of the solid and to integrate that area across the solid. In this section we will develop another method for finding volumes that may be applicable when the cross-sectional area cannot be found or the integration is too difficult.

### CYLINDRICAL SHELLS
In this section we will be interested in the following problem.

> **5.3.1 PROBLEM**  
> Let $f$ be continuous and nonnegative on $[a, b] \ (0 \le a < b)$, and let $R$ be the region that is bounded above by $y = f(x)$, below by the $x$-axis, and on the sides by the lines $x = a$ and $x = b$. Find the volume $V$ of the solid of revolution $S$ that is generated by revolving the region $R$ about the $y$-axis (Figure 5.3.1).

Sometimes problems of the above type can be solved by the method of disks or washers perpendicular to the $y$-axis, but when that method is not applicable or the resulting integral is difficult, the method of cylindrical shells, which we will discuss here, will often work.

A **cylindrical shell** is a solid enclosed by two concentric right circular cylinders (Figure 5.3.2). The volume $V$ of a cylindrical shell with inner radius $r_1$, outer radius $r_2$, and height $h$ can be written as
$$V = [\text{area of cross section}] \cdot [\text{height}] = (\pi r_2^2 - \pi r_1^2)h = \pi (r_2 + r_1)(r_2 - r_1)h = 2\pi \cdot \left[\frac{1}{2}(r_1 + r_2)\right] \cdot h \cdot (r_2 - r_1)$$
But $\frac{1}{2}(r_1 + r_2)$ is the average radius of the shell and $r_2 - r_1$ is its thickness, so
$$V = 2\pi \cdot [\text{average radius}] \cdot [\text{height}] \cdot [\text{thickness}] \tag{1}$$

We will now show how this formula can be used to solve Problem 5.3.1. The underlying idea is to divide the interval $[a, b]$ into $n$ subintervals, thereby subdividing the region $R$ into $n$ strips, $R_1, R_2, \dots, R_n$ (Figure 5.3.3a). When the region $R$ is revolved about the $y$-axis, these strips generate “tube-like” solids $S_1, S_2, \dots, S_n$ that are nested one inside the other and together comprise the entire solid $S$ (Figure 5.3.3b). Thus, the volume $V$ of the solid can be obtained by adding together the volumes of the tubes; that is,
$$V = V(S_1) + V(S_2) + \dots + V(S_n)$$

As a rule, the tubes will have curved upper surfaces, so there will be no simple formulas for their volumes. However, if the strips are thin, then we can approximate each strip by a rectangle (Figure 5.3.4a). These rectangles, when revolved about the $y$-axis, will produce cylindrical shells whose volumes closely approximate the volumes of the tubes generated by the original strips (Figure 5.3.4b). We will show that by adding the volumes of the cylindrical shells we can obtain a Riemann sum that approximates the volume $V$, and by taking the limit of the Riemann sums we can obtain an integral for the exact volume $V$.

To implement this idea, suppose that the $k$th strip extends from $x_{k-1}$ to $x_k$ and that the width of this strip is $\Delta x_k = x_k - x_{k-1}$. If we let $x_k^*$ be the midpoint of the interval $[x_{k-1}, x_k]$, and if we construct a rectangle of height $f(x_k^*)$ over the interval, then revolving this rectangle about the $y$-axis produces a cylindrical shell of average radius $x_k^*$, height $f(x_k^*)$, and thickness $\Delta x_k$ (Figure 5.3.5). From (1), the volume $V_k$ of this cylindrical shell is
$$V_k = 2\pi x_k^* f(x_k^*) \Delta x_k$$

Adding the volumes of the $n$ cylindrical shells yields the following Riemann sum that approximates the volume $V$:
$$V \approx \sum_{k=1}^n 2\pi x_k^* f(x_k^*) \Delta x_k$$

Taking the limit as $n$ increases and the widths of all the subintervals approach zero yields the definite integral
$$V = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n 2\pi x_k^* f(x_k^*) \Delta x_k = \int_a^b 2\pi x f(x) dx$$

In summary, we have the following result.

> **5.3.2 VOLUME BY CYLINDRICAL SHELLS ABOUT THE $y$-AXIS**  
> Let $f$ be continuous and nonnegative on $[a, b] \ (0 \le a < b)$, and let $R$ be the region that is bounded above by $y = f(x)$, below by the $x$-axis, and on the sides by the lines $x = a$ and $x = b$. Then the volume $V$ of the solid of revolution that is generated by revolving the region $R$ about the $y$-axis is given by
> $$V = \int_a^b 2\pi x f(x) dx \tag{2}$$

#### Example 1
Use cylindrical shells to find the volume of the solid generated when the region enclosed between $y = \sqrt{x}, x = 1, x = 4,$ and the $x$-axis is revolved about the $y$-axis.

**Solution.** First sketch the region (Figure 5.3.6a); then imagine revolving it about the $y$-axis (Figure 5.3.6b). Since $f(x) = \sqrt{x}, a = 1,$ and $b = 4$, Formula (2) yields
$$V = \int_1^4 2\pi x \sqrt{x} dx = 2\pi \int_1^4 x^{3/2} dx = \left[2\pi \cdot \frac{2}{5} x^{5/2}\right]_1^4 = \frac{4\pi}{5}[32 - 1] = \frac{124\pi}{5}$$

---

### VARIATIONS OF THE METHOD OF CYLINDRICAL SHELLS
The method of cylindrical shells is applicable in a variety of situations that do not fit the conditions required by Formula (2). For example, the region may be enclosed between two curves, or the axis of revolution may be some line other than the $y$-axis. However, rather than develop a separate formula for every possible situation, we will give a general way of thinking about the method of cylindrical shells that can be adapted to each new situation as it arises.

For this purpose, we will need to reexamine the integrand in Formula (2): At each $x$ in the interval $[a, b]$, the vertical line segment from the $x$-axis to the curve $y = f(x)$ can be viewed as the cross section of the region $R$ at $x$ (Figure 5.3.7a). When the region $R$ is revolved about the $y$-axis, the cross section at $x$ sweeps out the surface of a right circular cylinder of height $f(x)$ and radius $x$ (Figure 5.3.7b). The area of this surface is $2\pi x f(x)$ (Figure 5.3.7c), which is the integrand in (2). Thus, Formula (2) can be viewed informally in the following way:

> **5.3.3 AN INFORMAL VIEWPOINT ABOUT CYLINDRICAL SHELLS**  
> The volume $V$ of a solid of revolution that is generated by revolving a region $R$ about an axis can be obtained by integrating the area of the surface generated by an arbitrary cross section of $R$ taken parallel to the axis of revolution.

#### Example 2
Use cylindrical shells to find the volume of the solid generated when the region $R$ in the first quadrant enclosed between $y = x$ and $y = x^2$ is revolved about the $y$-axis (Figure 5.3.8a).

**Solution.** As illustrated in part (b) of Figure 5.3.8, at each $x$ in $[0, 1]$ the cross section of $R$ parallel to the $y$-axis generates a cylindrical surface of height $x - x^2$ and radius $x$. Since the area of this surface is $2\pi x(x - x^2)$, the volume of the solid is
$$V = \int_0^1 2\pi x(x - x^2) dx = 2\pi \int_0^1 (x^2 - x^3) dx = 2\pi \left[\frac{x^3}{3} - \frac{x^4}{4}\right]_0^1 = 2\pi \left[\frac{1}{3} - \frac{1}{4}\right] = \frac{\pi}{6}$$

#### Example 3
Use cylindrical shells to find the volume of the solid generated when the region $R$ under $y = x^2$ over the interval $[0, 2]$ is revolved about the line $y = -1$.

**Solution.** First draw the axis of revolution; then imagine revolving the region about the axis (Figure 5.3.9a). As illustrated in Figure 5.3.9b, at each $y$ in the interval $0 \le y \le 4$, the cross section of $R$ parallel to the $x$-axis generates a cylindrical surface of height $2 - \sqrt{y}$ and radius $y + 1$. Since the area of this surface is $2\pi(y + 1)(2 - \sqrt{y})$, it follows that the volume of the solid is
$$\int_0^4 2\pi(y + 1)(2 - \sqrt{y}) dy = 2\pi \int_0^4 (2y - y^{3/2} + 2 - y^{1/2}) dy = 2\pi \left[y^2 - \frac{2}{5}y^{5/2} + 2y - \frac{2}{3}y^{3/2}\right]_0^4 = \frac{176\pi}{15}$$

*Note that the volume found in Example 3 agrees with the volume of the same solid found by the method of washers in Example 6 of Section 5.2.*

---

### QUICK CHECK EXERCISES 5.3
*(See page 371 for answers.)*

1. Let $R$ be the region between the $x$-axis and the curve $y = 1 + \sqrt{x}$ for $1 \le x \le 4$.  
   (a) For $x$ between 1 and 4, the area of the cylindrical surface generated by revolving the vertical cross section of $R$ at $x$ about the $y$-axis is $\underline{\hspace{1.5cm}}$.  
   (b) Using cylindrical shells, an integral expression for the volume of the solid generated by revolving $R$ about the $y$-axis is $\underline{\hspace{1.5cm}}$.
2. Let $R$ be the region described in Quick Check Exercise 1.  
   (a) For $x$ between 1 and 4, the area of the cylindrical surface generated by revolving the vertical cross section of $R$ at $x$ about the line $x = 5$ is $\underline{\hspace{1.5cm}}$.  
   (b) Using cylindrical shells, an integral expression for the volume of the solid generated by revolving $R$ about the line $x = 5$ is $\underline{\hspace{1.5cm}}$.
3. A solid $S$ is generated by revolving the region enclosed by the curves $x = (y - 2)^2$ and $x = 4$ about the $x$-axis. Using cylindrical shells, an integral expression for the volume of $S$ is $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 5.3
1. (a) $2\pi x(1 + \sqrt{x})$ (b) $\int_1^4 2\pi x(1 + \sqrt{x}) dx$  
2. (a) $2\pi(5 - x)(1 + \sqrt{x})$ (b) $\int_1^4 2\pi(5 - x)(1 + \sqrt{x}) dx$  
3. $\int_0^4 2\pi y [4 - (y - 2)^2] dy$

---

### EXERCISE SET 5.3

**1–4 Use cylindrical shells to find the volume of the solid generated when the shaded region is revolved about the indicated axis.**
1. Region bounded by $y = x^2, x = 1, x = 2, y = 0$; revolved about the $y$-axis.
2. Region bounded by $y = x, y = \sqrt{4 - x^2}, x = 0$; revolved about the $y$-axis.
3. Region bounded by $x = 2y - 2y^2, x = 0$; revolved about the $x$-axis.
4. Region bounded by $y = \sqrt{x + 2}, y = x, y = 0$; revolved about the $x$-axis.

**5–10 Use cylindrical shells to find the volume of the solid generated when the region enclosed by the given curves is revolved about the $y$-axis.**
5. $y = x^3, x = 1, y = 0$
6. $y = \sqrt{x}, x = 4, x = 9, y = 0$
7. $y = 1/x, y = 0, x = 1, x = 3$
8. $y = \cos(x^2), x = 0, x = \frac{1}{2}\sqrt{\pi}, y = 0$
9. $y = 2x - 1, y = -2x + 3, x = 2$
10. $y = 2x - x^2, y = 0$

**11–14 Use cylindrical shells to find the volume of the solid generated when the region enclosed by the given curves is revolved about the $x$-axis.**
11. $y^2 = x, y = 1, x = 0$
12. $x = 2y, y = 2, y = 3, x = 0$
13. $y = x^2, x = 1, y = 0$
14. $xy = 4, x + y = 5$

**15–18 True–False Determine whether the statement is true or false. Explain your answer.**
15. The volume of a cylindrical shell is equal to the product of the thickness of the shell with the surface area of a cylinder whose height is that of the shell and whose radius is equal to the average of the inner and outer radii of the shell.
16. The method of cylindrical shells is a special case of the method of integration of cross-sectional area that was discussed in Section 5.2.
17. In the method of cylindrical shells, integration is over an interval on a coordinate axis that is perpendicular to the axis of revolution of the solid.
18. The Riemann sum approximation
    $$V \approx \sum_{k=1}^n 2\pi x_k^* f(x_k^*) \Delta x_k \quad\left(\text{where } x_k^* = \frac{x_k + x_{k-1}}{2}\right)$$
    for the volume of a solid of revolution is exact when $f$ is a constant function.

19. [CAS] Use a CAS to find the volume of the solid generated when the region enclosed by $y = \sin x$ and $y = 0$ for $0 \le x \le \pi$ is revolved about the $y$-axis.
20. [CAS] Use a CAS to find the volume of the solid generated when the region enclosed by $y = \cos x, y = 0,$ and $x = 0$ for $0 \le x \le \pi/2$ is revolved about the $y$-axis.
21. [CAS] Consider the region to the right of the $y$-axis, to the left of the vertical line $x = k \ (0 < k < \pi)$, and between the curve $y = \sin x$ and the $x$-axis. Use a CAS to estimate the value of $k$ so that the solid generated by revolving the region about the $y$-axis has a volume of 8 cubic units.

#### FOCUS ON CONCEPTS
22. Let $R_1$ and $R_2$ be regions of the form shown in the accompanying figure. Use cylindrical shells to find a formula for the volume of the solid that results when  
   (a) region $R_1$ is revolved about the $y$-axis  
   (b) region $R_2$ is revolved about the $x$-axis.
23. (a) Use cylindrical shells to find the volume of the solid that is generated when the region under the curve $y = x^3 - 3x^2 + 2x$ over $[0, 1]$ is revolved about the $y$-axis.  
   (b) For this problem, is the method of cylindrical shells easier or harder than the method of slicing discussed in the last section? Explain.
24. Let $f$ be continuous and nonnegative on $[a, b]$, and let $R$ be the region that is enclosed by $y = f(x)$ and $y = 0$ for $a \le x \le b$. Using the method of cylindrical shells, derive with explanation a formula for the volume of the solid generated by revolving $R$ about the line $x = k$, where $k \le a$.

**25–26 Using the method of cylindrical shells, set up but do not evaluate an integral for the volume of the solid generated when the region $R$ is revolved about (a) the line $x = 1$ and (b) the line $y = -1$.**
25. $R$ is the region bounded by the graphs of $y = x, y = 0,$ and $x = 1$.
26. $R$ is the region in the first quadrant bounded by the graphs of $y = \sqrt{1 - x^2}, y = 0,$ and $x = 0$.

27. Use cylindrical shells to find the volume of the solid that is generated when the region that is enclosed by $y = 1/x^3, x = 1, x = 2, y = 0$ is revolved about the line $x = -1$.
28. Use cylindrical shells to find the volume of the solid that is generated when the region that is enclosed by $y = x^3, y = 1, x = 0$ is revolved about the line $y = 1$.
29. Use cylindrical shells to find the volume of the cone generated when the triangle with vertices $(0, 0), (0, r), (h, 0)$, where $r > 0$ and $h > 0$, is revolved about the $x$-axis.
30. The region enclosed between the curve $y^2 = kx$ and the line $x = \frac{1}{4}k$ is revolved about the line $x = \frac{1}{2}k$. Use cylindrical shells to find the volume of the resulting solid. (Assume $k > 0$.)
31. As shown in the accompanying figure, a cylindrical hole is drilled all the way through the center of a sphere. Show that the volume of the remaining solid depends only on the length $L$ of the hole, not on the size of the sphere.
32. Use cylindrical shells to find the volume of the torus obtained by revolving the circle $x^2 + y^2 = a^2$ about the line $x = b$, where $b > a > 0$. [*Hint:* It may help in the integration to think of an integral as an area.]
33. Let $V_x$ and $V_y$ be the volumes of the solids that result when the region enclosed by $y = 1/x, y = 0, x = \frac{1}{2},$ and $x = b \ (b > \frac{1}{2})$ is revolved about the $x$-axis and $y$-axis, respectively. Is there a value of $b$ for which $V_x = V_y$?
34. **Writing.** Faced with the problem of computing the volume of a solid of revolution, how would you go about deciding whether to use the method of disks/washers or the method of cylindrical shells?
35. **Writing.** With both the method of disks/washers and with the method of cylindrical shells, we integrate an “area” to get the volume of a solid of revolution. However, these two approaches differ in very significant ways. Write a brief paragraph that discusses these differences.

---

## 5.4 LENGTH OF A PLANE CURVE

In this section we will use the tools of calculus to study the problem of finding the length of a plane curve.

### ARC LENGTH
Our first objective is to define what we mean by the **length** (also called the **arc length**) of a plane curve $y = f(x)$ over an interval $[a, b]$ (Figure 5.4.1). Once that is done we will be able to focus on the problem of computing arc lengths. To avoid some complications that would otherwise occur, we will impose the requirement that $f'$ be continuous on $[a, b]$, in which case we will say that $y = f(x)$ is a **smooth curve** on $[a, b]$ or that $f$ is a **smooth function** on $[a, b]$. Thus, we will be concerned with the following problem.

> **5.4.1 ARC LENGTH PROBLEM**  
> Suppose that $y = f(x)$ is a smooth curve on the interval $[a, b]$. Define and find a formula for the arc length $L$ of the curve $y = f(x)$ over the interval $[a, b]$.

*Intuitively, you might think of the arc length of a curve as the number obtained by aligning a piece of string with the curve and then measuring the length of the string after it is straightened out.*

To define the arc length of a curve we start by breaking the curve into small segments. Then we approximate the curve segments by line segments and add the lengths of the line segments to form a Riemann sum. Figure 5.4.2 illustrates how such line segments tend to become better and better approximations to a curve as the number of segments increases. As the number of segments increases, the corresponding Riemann sums approach a definite integral whose value we will take to be the arc length $L$ of the curve.

To implement our idea for solving Problem 5.4.1, divide the interval $[a, b]$ into $n$ subintervals by inserting points $x_1, x_2, \dots, x_{n-1}$ between $a = x_0$ and $b = x_n$. As shown in Figure 5.4.3a, let $P_0, P_1, \dots, P_n$ be the points on the curve with $x$-coordinates $a = x_0, x_1, x_2, \dots, x_{n-1}, b = x_n$ and join these points with straight line segments. These line segments form a polygonal path that we can regard as an approximation to the curve $y = f(x)$. As indicated in Figure 5.4.3b, the length $L_k$ of the $k$th line segment in the polygonal path is
$$L_k = \sqrt{(\Delta x_k)^2 + (\Delta y_k)^2} = \sqrt{(\Delta x_k)^2 + [f(x_k) - f(x_{k-1})]^2} \tag{1}$$

If we now add the lengths of these line segments, we obtain the following approximation to the length $L$ of the curve:
$$L \approx \sum_{k=1}^n L_k = \sum_{k=1}^n \sqrt{(\Delta x_k)^2 + [f(x_k) - f(x_{k-1})]^2} \tag{2}$$

To put this in the form of a Riemann sum we will apply the Mean-Value Theorem (3.8.2). This theorem implies that there is a point $x_k^*$ between $x_{k-1}$ and $x_k$ such that
$$\frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}} = f'(x_k^*) \quad\text{or}\quad f(x_k) - f(x_{k-1}) = f'(x_k^*) \Delta x_k$$
and hence we can rewrite (2) as
$$L \approx \sum_{k=1}^n \sqrt{(\Delta x_k)^2 + [f'(x_k^*)]^2 (\Delta x_k)^2} = \sum_{k=1}^n \sqrt{1 + [f'(x_k^*)]^2} \Delta x_k$$

Thus, taking the limit as $n$ increases and the widths of all the subintervals approach zero yields the following integral that defines the arc length $L$:
$$L = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n \sqrt{1 + [f'(x_k^*)]^2} \Delta x_k = \int_a^b \sqrt{1 + [f'(x)]^2} dx$$

In summary, we have the following definition.

> **5.4.2 DEFINITION**  
> If $y = f(x)$ is a smooth curve on the interval $[a, b]$, then the **arc length** $L$ of this curve over $[a, b]$ is defined as
> $$L = \int_a^b \sqrt{1 + [f'(x)]^2} dx \tag{3}$$

This result provides both a definition and a formula for computing arc lengths. Where convenient, (3) can also be expressed as
$$L = \int_a^b \sqrt{1 + [f'(x)]^2} dx = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx \tag{4}$$

Moreover, for a curve expressed in the form $x = g(y)$, where $g'$ is continuous on $[c, d]$, the arc length $L$ from $y = c$ to $y = d$ can be expressed as
$$L = \int_c^d \sqrt{1 + [g'(y)]^2} dy = \int_c^d \sqrt{1 + \left(\frac{dx}{dy}\right)^2} dy \tag{5}$$

#### Example 1
Find the arc length of the curve $y = x^{3/2}$ from $(1, 1)$ to $(2, 2\sqrt{2})$ (Figure 5.4.4) in two ways: (a) using Formula (4) and (b) using Formula (5).

**Solution (a).** $\frac{dy}{dx} = \frac{3}{2}x^{1/2}$ and since the curve extends from $x = 1$ to $x = 2$, it follows from (4) that
$$L = \int_1^2 \sqrt{1 + \left(\frac{3}{2}x^{1/2}\right)^2} dx = \int_1^2 \sqrt{1 + \frac{9}{4}x} dx$$
To evaluate this integral we make the $u$-substitution
$$u = 1 + \frac{9}{4}x, \quad du = \frac{9}{4}dx$$
and then change the $x$-limits of integration ($x = 1, x = 2$) to the corresponding $u$-limits ($u = \frac{13}{4}, u = \frac{22}{4}$):
$$L = \frac{4}{9}\int_{13/4}^{22/4} u^{1/2} du = \left[\frac{8}{27}u^{3/2}\right]_{13/4}^{22/4} = \frac{8}{27}\left[\left(\frac{22}{4}\right)^{3/2} - \left(\frac{13}{4}\right)^{3/2}\right] = \frac{22\sqrt{22} - 13\sqrt{13}}{27} \approx 2.09$$

**Solution (b).** To apply Formula (5) we must first rewrite the equation $y = x^{3/2}$ so that $x$ is expressed as a function of $y$. This yields $x = y^{2/3}$ and $\frac{dx}{dy} = \frac{2}{3}y^{-1/3}$. Since the curve extends from $y = 1$ to $y = 2\sqrt{2}$, it follows from (5) that
$$L = \int_1^{2\sqrt{2}} \sqrt{1 + \frac{4}{9}y^{-2/3}} dy = \frac{1}{3}\int_1^{2\sqrt{2}} y^{-1/3}\sqrt{9y^{2/3} + 4} dy$$
To evaluate this integral we make the $u$-substitution $u = 9y^{2/3} + 4, du = 6y^{-1/3} dy$ and change the $y$-limits of integration ($y = 1, y = 2\sqrt{2}$) to the corresponding $u$-limits ($u = 13, u = 22$). This gives
$$L = \frac{1}{18}\int_{13}^{22} u^{1/2} du = \left[\frac{1}{27}u^{3/2}\right]_{13}^{22} = \frac{1}{27}[(22)^{3/2} - (13)^{3/2}] = \frac{22\sqrt{22} - 13\sqrt{13}}{27}$$
The answer in part (b) agrees with that in part (a); however, the integration in part (b) is more tedious. In problems where there is a choice between using (4) or (5), it is often the case that one of the formulas leads to a simpler integral than the other.

---

### FINDING ARC LENGTH BY NUMERICAL METHODS
In Chapter 7 we will develop some techniques of integration that will enable us to find exact values of more integrals encountered in arc length calculations; however, generally speaking, most such integrals are impossible to evaluate in terms of elementary functions. In these cases one usually approximates the integral using a numerical method such as the midpoint rule discussed in Section 4.4.

#### Example 2
From (4), the arc length of $y = \sin x$ from $x = 0$ to $x = \pi$ is given by the integral
$$L = \int_0^\pi \sqrt{1 + (\cos x)^2} dx$$
This integral cannot be evaluated in terms of elementary functions; however, using a calculating utility with a numerical integration capability yields the approximation $L \approx 3.8202$.

---

### QUICK CHECK EXERCISES 5.4
*(See page 377 for answers.)*

1. A function $f$ is smooth on $[a, b]$ if $f'$ is $\underline{\hspace{1.5cm}}$ on $[a, b]$.
2. If a function $f$ is smooth on $[a, b]$, then the length of the curve $y = f(x)$ over $[a, b]$ is $\underline{\hspace{1.5cm}}$.
3. The distance between points $(1, 0)$ and $(\pi, 1)$ is $\underline{\hspace{1.5cm}}$.
4. Let $L$ be the length of the curve $y = x^2$ from $(0, 0)$ to $(2, 4)$.  
   (a) Integrating with respect to $x$, an integral expression for $L$ is $\underline{\hspace{1.5cm}}$.  
   (b) Integrating with respect to $y$, an integral expression for $L$ is $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 5.4
1. continuous  
2. $\int_a^b \sqrt{1 + [f'(x)]^2} dx$  
3. $\sqrt{(\pi - 1)^2 + 1}$  
4. (a) $\int_0^2 \sqrt{1 + 4x^2} dx$ (b) $\int_0^4 \sqrt{1 + \frac{1}{4y}} dy$

---

### EXERCISE SET 5.4

1. Use the Theorem of Pythagoras to find the length of the line segment $y = 2x$ from $(1, 2)$ to $(2, 4)$, and confirm that the value is consistent with the length computed using  
   (a) Formula (4) (b) Formula (5).
2. Use the Theorem of Pythagoras to find the length of the line segment $y = 5x$ from $(0, 0)$ to $(1, 5)$, and confirm that the value is consistent with the length computed using  
   (a) Formula (4) (b) Formula (5).

**3–8 Find the exact arc length of the curve over the interval.**
3. $y = 3x^{3/2} - 1$ from $x = 0$ to $x = 1$
4. $x = \frac{1}{3}(y^2 + 2)^{3/2}$ from $y = 0$ to $y = 1$
5. $y = x^{2/3}$ from $x = 1$ to $x = 8$
6. $y = (x^6 + 8)/(16x^2)$ from $x = 2$ to $x = 3$
7. $24xy = y^4 + 48$ from $y = 2$ to $y = 4$
8. $x = \frac{1}{8}y^4 + \frac{1}{4}y^{-2}$ from $y = 1$ to $y = 4$

**9–12 True–False Determine whether the statement is true or false. Explain your answer.**
9. The graph of $y = \sqrt{1 - x^2}$ is a smooth curve on $[-1, 1]$.
10. The approximation $L \approx \sum_{k=1}^n \sqrt{(\Delta x_k)^2 + [f(x_k) - f(x_{k-1})]^2}$ for arc length is not expressed in the form of a Riemann sum.
11. The approximation $L \approx \sum_{k=1}^n \sqrt{1 + [f'(x_k^*)]^2} \Delta x_k$ for arc length is exact when $f$ is a linear function of $x$.
12. In our definition of the arc length for the graph of $y = f(x)$, we need $f'(x)$ to be a continuous function in order for $f$ to satisfy the hypotheses of the Mean-Value Theorem (3.8.2).

#### FOCUS ON CONCEPTS
13. Consider the curve $y = x^{2/3}$.  
   (a) Sketch the portion of the curve between $x = -1$ and $x = 8$.  
   (b) Explain why Formula (4) cannot be used to find the arc length of the curve sketched in part (a).  
   (c) Find the arc length of the curve sketched in part (a).
14. The curve segment $y = x^2$ from $x = 1$ to $x = 2$ may also be expressed as the graph of $x = \sqrt{y}$ from $y = 1$ to $y = 4$. Set up two integrals that give the arc length of this curve segment, one by integrating with respect to $x$, and the other by integrating with respect to $y$. Demonstrate a substitution that verifies that these two integrals are equal.
15. Consider the curve segments $y = x^2$ from $x = \frac{1}{2}$ to $x = 2$ and $y = \sqrt{x}$ from $x = \frac{1}{4}$ to $x = 4$.  
   (a) Graph the two curve segments and use your graphs to explain why the lengths of these two curve segments should be equal.  
   (b) Set up integrals that give the arc lengths of the curve segments by integrating with respect to $x$. Demonstrate a substitution that verifies that these two integrals are equal.  
   (c) Set up integrals that give the arc lengths of the curve segments by integrating with respect to $y$.  
   (d) Approximate the arc length of each curve segment using Formula (2) with $n = 10$ equal subintervals.  
   (e) Which of the two approximations in part (d) is more accurate? Explain.  
   (f) Use the midpoint approximation with $n = 10$ subintervals to approximate each arc length integral in part (b).  
   (g) Use a calculating utility with numerical integration capabilities to approximate the arc length integrals in part (b) to four decimal places.
16. Follow the directions of Exercise 15 for the curve segments $y = x^{8/3}$ from $x = 10^{-3}$ to $x = 1$ and $y = x^{3/8}$ from $x = 10^{-8}$ to $x = 1$.
17. Follow the directions of Exercise 15 for the curve segment $y = 1 + 1/x$ from $x = 1$ to $x = 3$ and for the curve segment $y = 1/(x - 1)$ from $x = 4/3$ to $x = 2$.
18. Let $y = f(x)$ be a smooth curve on the closed interval $[a, b]$. Prove that if $m$ and $M$ are nonnegative numbers such that $m \le |f'(x)| \le M$ for all $x$ in $[a, b]$, then the arc length $L$ of $y = f(x)$ over the interval $[a, b]$ satisfies the inequalities
    $$(b - a)\sqrt{1 + m^2} \le L \le (b - a)\sqrt{1 + M^2}$$
19. Use the result of Exercise 18 to show that the arc length $L$ of $y = \sec x$ over the interval $0 \le x \le \pi/3$ satisfies
    $$\frac{\pi}{3} \le L \le \frac{\pi}{3}\sqrt{13}$$

20. [CAS] A basketball player makes a successful shot from the free throw line. Suppose that the path of the ball from the moment of release to the moment it enters the hoop is described by
    $$y = 2.15 + 2.09x - 0.41x^2, \quad 0 \le x \le 4.6$$
    where $x$ is the horizontal distance (in meters) from the point of release, and $y$ is the vertical distance (in meters) above the floor. Use a CAS or a scientific calculator with a numerical integration capability to approximate the distance the ball travels from the moment it is released to the moment it enters the hoop. Round your answer to two decimal places.
21. [CAS] The central span of the Golden Gate Bridge in California is $4200\text{ ft}$ long and is suspended from cables that rise $500\text{ ft}$ above the roadway on either side. Approximately how long is the portion of a cable that lies between the support towers on one side of the roadway? [*Hint:* As suggested by the accompanying figure, assume the cable is modeled by a parabola $y = ax^2$ that passes through the point $(2100, 500)$. Use a CAS or a calculating utility with a numerical integration capability to approximate the length of the cable. Round your answer to the nearest foot.]
22. [CAS] As shown in the accompanying figure, a horizontal beam with dimensions $2\text{ in} \times 6\text{ in} \times 16\text{ ft}$ is fixed at both ends and is subjected to a uniformly distributed load of $120\text{ lb/ft}$. As a result of the load, the centerline of the beam undergoes a deflection that is described by
    $$y = -1.67 \times 10^{-8}(x^4 - 2Lx^3 + L^2 x^2)$$
    ($0 \le x \le 192$), where $L = 192\text{ in}$ is the length of the unloaded beam, $x$ is the horizontal distance along the beam measured in inches from the left end, and $y$ is the deflection of the centerline in inches.  
    (a) Graph $y$ versus $x$ for $0 \le x \le 192$.  
    (b) Find the maximum deflection of the centerline.  
    (c) Use a CAS or a calculator with a numerical integration capability to find the length of the centerline of the loaded beam. Round your answer to two decimal places.
23. [CAS] A golfer makes a successful chip shot to the green. Suppose that the path of the ball from the moment it is struck to the moment it hits the green is described by
    $$y = 12.54x - 0.41x^2$$
    where $x$ is the horizontal distance (in yards) from the point where the ball is struck, and $y$ is the vertical distance (in yards) above the fairway. Use a CAS or a calculating utility with a numerical integration capability to find the distance the ball travels from the moment it is struck to the moment it hits the green. Assume that the fairway and green are at the same level and round your answer to two decimal places.

**24–30 These exercises assume familiarity with the basic concepts of parametric curves. If needed, an introduction to this material is provided in Web Appendix I.**
24. [CAS] Assume that no segment of the curve $x = x(t), y = y(t), (a \le t \le b)$ is traced more than once as $t$ increases from $a$ to $b$. Divide the interval $[a, b]$ into $n$ subintervals by inserting points $t_1, t_2, \dots, t_{n-1}$ between $a = t_0$ and $b = t_n$. Let $L$ denote the arc length of the curve. Give an informal argument for the approximation
    $$L \approx \sum_{k=1}^n \sqrt{[x(t_k) - x(t_{k-1})]^2 + [y(t_k) - y(t_{k-1})]^2}$$
    If $dx/dt$ and $dy/dt$ are continuous functions for $a \le t \le b$, then it can be shown that as $\max \Delta t_k \to 0$, this sum converges to
    $$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt$$

**25–28 Use the arc length formula from Exercise 24 to find the arc length of the curve.**
25. $x = \frac{1}{3}t^3, y = \frac{1}{2}t^2 \ (0 \le t \le 1)$
26. $x = (1 + t)^2, y = (1 + t)^3 \ (0 \le t \le 1)$
27. $x = \cos 2t, y = \sin 2t \ (0 \le t \le \pi/2)$
28. $x = \cos t + t\sin t, y = \sin t - t\cos t \ (0 \le t \le \pi)$

29. [CAS] (a) Show that the total arc length of the ellipse $x = 2\cos t, y = \sin t \ (0 \le t \le 2\pi)$ is given by
    $$4\int_0^{\pi/2} \sqrt{1 + 3\sin^2 t} dt$$
    (b) Use a CAS or a scientific calculator with a numerical integration capability to approximate the arc length in part (a). Round your answer to two decimal places.  
    (c) Suppose that the parametric equations in part (a) describe the path of a particle moving in the $xy$-plane, where $t$ is time in seconds and $x$ and $y$ are in centimeters. Use a CAS or a scientific calculator with a numerical integration capability to approximate the distance traveled by the particle from $t = 1.5\text{ s}$ to $t = 4.8\text{ s}$. Round your answer to two decimal places.
30. Show that the total arc length of the ellipse $x = a\cos t, y = b\sin t, 0 \le t \le 2\pi$ for $a > b > 0$ is given by
    $$4a\int_0^{\pi/2} \sqrt{1 - k^2\cos^2 t} dt$$
    where $k = \sqrt{a^2 - b^2}/a$.
31. **Writing.** In our discussion of Arc Length Problem 5.4.1, we derived the approximation
    $$L \approx \sum_{k=1}^n \sqrt{1 + [f'(x_k^*)]^2} \Delta x_k$$
    Discuss the geometric meaning of this approximation. (Be sure to address the appearance of the derivative $f'$.)
32. **Writing.** Give examples in which Formula (4) for arc length cannot be applied directly, and describe how you would go about finding the arc length of the curve in each case. (Discuss both the use of alternative formulas and the use of numerical methods.)

---

## 5.5 AREA OF A SURFACE OF REVOLUTION

In this section we will consider the problem of finding the area of a surface that is generated by revolving a plane curve about a line.

### SURFACE AREA
A **surface of revolution** is a surface that is generated by revolving a plane curve about an axis that lies in the same plane as the curve. For example, the surface of a sphere can be generated by revolving a semicircle about its diameter, and the lateral surface of a right circular cylinder can be generated by revolving a line segment about an axis that is parallel to it (Figure 5.5.1).

In this section we will be concerned with the following problem.

> **5.5.1 SURFACE AREA PROBLEM**  
> Suppose that $f$ is a smooth, nonnegative function on $[a, b]$ and that a surface of revolution is generated by revolving the portion of the curve $y = f(x)$ between $x = a$ and $x = b$ about the $x$-axis (Figure 5.5.2). Define what is meant by the area $S$ of the surface, and find a formula for computing it.

To motivate an appropriate definition for the area $S$ of a surface of revolution, we will decompose the surface into small sections whose areas can be approximated by elementary formulas, add the approximations of the areas of the sections to form a Riemann sum that approximates $S$, and then take the limit of the Riemann sums to obtain an integral for the exact value of $S$.

To implement this idea, divide the interval $[a, b]$ into $n$ subintervals by inserting points $x_1, x_2, \dots, x_{n-1}$ between $a = x_0$ and $b = x_n$. As illustrated in Figure 5.5.3a, the corresponding points on the graph of $f$ define a polygonal path that approximates the curve $y = f(x)$ over the interval $[a, b]$. As illustrated in Figure 5.5.3b, when this polygonal path is revolved about the $x$-axis, it generates a surface consisting of $n$ parts, each of which is a portion of a right circular cone called a **frustum** (from the Latin meaning “bit” or “piece”). Thus, the area of each part of the approximating surface can be obtained from the formula
$$S = \pi(r_1 + r_2)l \tag{1}$$
for the lateral area $S$ of a frustum of slant height $l$ and base radii $r_1$ and $r_2$ (Figure 5.5.4).

As suggested by Figure 5.5.5, the $k$th frustum has radii $f(x_{k-1})$ and $f(x_k)$ and height $\Delta x_k$. Its slant height is the length $L_k$ of the $k$th line segment in the polygonal path, which from Formula (1) of Section 5.4 is
$$L_k = \sqrt{(\Delta x_k)^2 + [f(x_k) - f(x_{k-1})]^2}$$
This makes the lateral area $S_k$ of the $k$th frustum
$$S_k = \pi [f(x_{k-1}) + f(x_k)] \sqrt{(\Delta x_k)^2 + [f(x_k) - f(x_{k-1})]^2}$$

If we add these areas, we obtain the following approximation to the area $S$ of the entire surface:
$$S \approx \sum_{k=1}^n \pi [f(x_{k-1}) + f(x_k)] \sqrt{(\Delta x_k)^2 + [f(x_k) - f(x_{k-1})]^2} \tag{2}$$

To put this in the form of a Riemann sum we will apply the Mean-Value Theorem (3.8.2). This theorem implies that there is a point $x_k^*$ between $x_{k-1}$ and $x_k$ such that
$$\frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}} = f'(x_k^*) \quad\text{or}\quad f(x_k) - f(x_{k-1}) = f'(x_k^*) \Delta x_k$$
and hence we can rewrite (2) as
$$S \approx \sum_{k=1}^n \pi [f(x_{k-1}) + f(x_k)] \sqrt{(\Delta x_k)^2 + [f'(x_k^*)]^2(\Delta x_k)^2} = \sum_{k=1}^n \pi [f(x_{k-1}) + f(x_k)] \sqrt{1 + [f'(x_k^*)]^2} \Delta x_k \tag{3}$$

However, this is not yet a Riemann sum because it involves the variables $x_{k-1}$ and $x_k$. To eliminate these variables from the expression, observe that the average value of the numbers $f(x_{k-1})$ and $f(x_k)$ lies between these numbers, so the continuity of $f$ and the Intermediate-Value Theorem (1.5.8) imply that there is a point $x_k^{**}$ between $x_{k-1}$ and $x_k$ such that
$$\frac{1}{2}[f(x_{k-1}) + f(x_k)] = f(x_k^{**})$$
Thus, (2) can be expressed as
$$S \approx \sum_{k=1}^n 2\pi f(x_k^{**}) \sqrt{1 + [f'(x_k^*)]^2} \Delta x_k$$

Although this expression is close to a Riemann sum in form, it is not a true Riemann sum because it involves two variables $x_k^*$ and $x_k^{**}$, rather than $x_k^*$ alone. However, it is proved in advanced calculus courses that this has no effect on the limit because of the continuity of $f$. Thus, we can assume that $x_k^{**} = x_k^*$ when taking the limit, and this suggests that $S$ can be defined as
$$S = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n 2\pi f(x_k^*) \sqrt{1 + [f'(x_k^*)]^2} \Delta x_k = \int_a^b 2\pi f(x) \sqrt{1 + [f'(x)]^2} dx$$

In summary, we have the following definition.

> **5.5.2 DEFINITION**  
> If $f$ is a smooth, nonnegative function on $[a, b]$, then the **surface area** $S$ of the surface of revolution that is generated by revolving the portion of the curve $y = f(x)$ between $x = a$ and $x = b$ about the $x$-axis is defined as
> $$S = \int_a^b 2\pi f(x) \sqrt{1 + [f'(x)]^2} dx$$

This result provides both a definition and a formula for computing surface areas. Where convenient, this formula can also be expressed as
$$S = \int_a^b 2\pi f(x) \sqrt{1 + [f'(x)]^2} dx = \int_a^b 2\pi y \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx \tag{4}$$

Moreover, if $g$ is nonnegative and $x = g(y)$ is a smooth curve on the interval $[c, d]$, then the area of the surface that is generated by revolving the portion of a curve $x = g(y)$ between $y = c$ and $y = d$ about the $y$-axis can be expressed as
$$S = \int_c^d 2\pi g(y) \sqrt{1 + [g'(y)]^2} dy = \int_c^d 2\pi x \sqrt{1 + \left(\frac{dx}{dy}\right)^2} dy \tag{5}$$

#### Example 1
Find the area of the surface that is generated by revolving the portion of the curve $y = x^3$ between $x = 0$ and $x = 1$ about the $x$-axis.

**Solution.** First sketch the curve; then imagine revolving it about the $x$-axis (Figure 5.5.6). Since $y = x^3$, we have $dy/dx = 3x^2$, and hence from (4) the surface area $S$ is
$$S = \int_0^1 2\pi y \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx = \int_0^1 2\pi x^3 \sqrt{1 + (3x^2)^2} dx = 2\pi \int_0^1 x^3(1 + 9x^4)^{1/2} dx$$
$$= \frac{2\pi}{36}\int_1^{10} u^{1/2} du \quad [u = 1 + 9x^4, du = 36x^3 dx]$$
$$= \frac{2\pi}{36}\cdot\frac{2}{3}\left[u^{3/2}\right]_{u=1}^{10} = \frac{\pi}{27}(10^{3/2} - 1) \approx 3.56$$

#### Example 2
Find the area of the surface that is generated by revolving the portion of the curve $y = x^2$ between $x = 1$ and $x = 2$ about the $y$-axis.

**Solution.** First sketch the curve; then imagine revolving it about the $y$-axis (Figure 5.5.7). Because the curve is revolved about the $y$-axis we will apply Formula (5). Toward this end, we rewrite $y = x^2$ as $x = \sqrt{y}$ and observe that the $y$-values corresponding to $x = 1$ and $x = 2$ are $y = 1$ and $y = 4$. Since $x = \sqrt{y}$, we have $dx/dy = 1/(2\sqrt{y})$, and hence from (5) the surface area $S$ is
$$S = \int_1^4 2\pi x \sqrt{1 + \left(\frac{dx}{dy}\right)^2} dy = \int_1^4 2\pi\sqrt{y}\sqrt{1 + \left(\frac{1}{2\sqrt{y}}\right)^2} dy = \pi \int_1^4 \sqrt{4y + 1} dy$$
$$= \frac{\pi}{4}\int_5^{17} u^{1/2} du \quad [u = 4y + 1, du = 4 dy]$$
$$= \frac{\pi}{4}\cdot\frac{2}{3}\left[u^{3/2}\right]_{u=5}^{17} = \frac{\pi}{6}(17^{3/2} - 5^{3/2}) \approx 30.85$$

---

### QUICK CHECK EXERCISES 5.5
*(See page 382 for answers.)*

1. If $f$ is a smooth, nonnegative function on $[a, b]$, then the surface area $S$ of the surface of revolution generated by revolving the portion of the curve $y = f(x)$ between $x = a$ and $x = b$ about the $x$-axis is $\underline{\hspace{1.5cm}}$.
2. The lateral area of the frustum with slant height $\sqrt{10}$ and base radii $r_1 = 1$ and $r_2 = 2$ is $\underline{\hspace{1.5cm}}$.
3. An integral expression for the area of the surface generated by rotating the line segment joining $(3, 1)$ and $(6, 2)$ about the $x$-axis is $\underline{\hspace{1.5cm}}$.
4. An integral expression for the area of the surface generated by rotating the line segment joining $(3, 1)$ and $(6, 2)$ about the $y$-axis is $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 5.5
1. $\int_a^b 2\pi f(x)\sqrt{1 + [f'(x)]^2} dx$  
2. $3\sqrt{10}\pi$  
3. $\int_3^6 (2\pi)\left(\frac{x}{3}\right)\sqrt{\frac{10}{9}} dx = \int_3^6 \frac{2\sqrt{10}\pi}{9}x dx$  
4. $\int_1^2 (2\pi)(3y)\sqrt{10} dy$

---

### EXERCISE SET 5.5

**1–4 Find the area of the surface generated by revolving the given curve about the $x$-axis.**
1. $y = 7x, 0 \le x \le 1$
2. $y = \sqrt{x}, 1 \le x \le 4$
3. $y = \sqrt{4 - x^2}, -1 \le x \le 1$
4. $x = \sqrt[3]{y}, 1 \le y \le 8$

**5–8 Find the area of the surface generated by revolving the given curve about the $y$-axis.**
5. $x = 9y + 1, 0 \le y \le 2$
6. $x = y^3, 0 \le y \le 1$
7. $x = \sqrt{9 - y^2}, -2 \le y \le 2$
8. $x = 2\sqrt{1 - y}, -1 \le y \le 0$

**9–12 [CAS] Use a CAS to find the exact area of the surface generated by revolving the curve about the stated axis.**
9. $y = \sqrt{x} - \frac{1}{3}x^{3/2}, 1 \le x \le 3$; $x$-axis
10. $y = \frac{1}{3}x^3 + \frac{1}{4}x^{-1}, 1 \le x \le 2$; $x$-axis
11. $8xy^2 = 2y^6 + 1, 1 \le y \le 2$; $y$-axis
12. $x = \sqrt{16 - y}, 0 \le y \le 15$; $y$-axis

**13–14 [CAS] Use a CAS or a calculating utility with a numerical integration capability to approximate the area of the surface generated by revolving the curve about the stated axis. Round your answer to two decimal places.**
13. $y = \sin x, 0 \le x \le \pi$; $x$-axis
14. $x = \tan y, 0 \le y \le \pi/4$; $y$-axis

**15–18 True–False Determine whether the statement is true or false. Explain your answer.**
15. The lateral surface area $S$ of a right circular cone with height $h$ and base radius $r$ is $S = \pi r\sqrt{r^2 + h^2}$.
16. The lateral surface area of a frustum of slant height $l$ and base radii $r_1$ and $r_2$ is equal to the lateral surface area of a right circular cylinder of height $l$ and radius equal to the average of $r_1$ and $r_2$.
17. The approximation $S \approx \sum_{k=1}^n 2\pi f(x_k^{**})\sqrt{1 + [f'(x_k^*)]^2}\Delta x_k$ for surface area is exact if $f$ is a positive-valued constant function.
18. The expression $\sum_{k=1}^n 2\pi f(x_k^{**})\sqrt{1 + [f'(x_k^*)]^2}\Delta x_k$ is not a true Riemann sum for $\int_a^b 2\pi f(x)\sqrt{1 + [f'(x)]^2} dx$.

**19–20 Approximate the area of the surface using Formula (2) with $n = 20$ subintervals of equal width. Round your answer to two decimal places.**
19. The surface of Exercise 13.
20. The surface of Exercise 14.

#### FOCUS ON CONCEPTS
21. Assume that $y = f(x)$ is a smooth curve on the interval $[a, b]$ and assume that $f(x) \ge 0$ for $a \le x \le b$. Derive a formula for the surface area generated when the curve $y = f(x), a \le x \le b$, is revolved about the line $y = -k \ (k > 0)$.
22. Would it be circular reasoning to use Definition 5.5.2 to find the surface area of a frustum of a right circular cone? Explain your answer.
23. Show that the area of the surface of a sphere of radius $r$ is $4\pi r^2$. [*Hint:* Revolve the semicircle $y = \sqrt{r^2 - x^2}$ about the $x$-axis.]
24. The accompanying figure shows a spherical cap of height $h$ cut from a sphere of radius $r$. Show that the surface area $S$ of the cap is $S = 2\pi rh$. [*Hint:* Revolve an appropriate portion of the circle $x^2 + y^2 = r^2$ about the $y$-axis.]
25. The portion of a sphere that is cut by two parallel planes is called a *zone*. Use the result of Exercise 24 to show that the surface area of a zone depends on the radius of the sphere and the distance between the planes, but not on the location of the zone.
26. Let $y = f(x)$ be a smooth curve on the interval $[a, b]$ and assume that $f(x) \ge 0$ for $a \le x \le b$. By the Extreme-Value Theorem (3.4.2), the function $f$ has a maximum value $K$ and a minimum value $k$ on $[a, b]$. Prove: If $L$ is the arc length of the curve $y = f(x)$ between $x = a$ and $x = b$, and if $S$ is the area of the surface that is generated by revolving this curve about the $x$-axis, then
    $$2\pi k L \le S \le 2\pi KL$$
27. Use the results of Exercise 26 above and Exercise 19 in Section 5.4 to show that the area $S$ of the surface generated by revolving the curve $y = \sec x, 0 \le x \le \pi/3$, about the $x$-axis satisfies
    $$\frac{2\pi^2}{3} \le S \le \frac{4\pi^2}{3}\sqrt{13}$$
28. Let $y = f(x)$ be a smooth curve on $[a, b]$ and assume that $f(x) \ge 0$ for $a \le x \le b$. Let $A$ be the area under the curve $y = f(x)$ between $x = a$ and $x = b$, and let $S$ be the area of the surface obtained when this section of curve is revolved about the $x$-axis.  
    (a) Prove that $2\pi A \le S$.  
    (b) For what functions $f$ is $2\pi A = S$?

**29–35 These exercises assume familiarity with the basic concepts of parametric curves. If needed, an introduction to this material is provided in Web Appendix I.**  
**29–30 For these exercises, divide the interval $[a, b]$ into $n$ subintervals by inserting points $t_1, t_2, \dots, t_{n-1}$ between $a = t_0$ and $b = t_n$, and assume that $x'(t)$ and $y'(t)$ are continuous functions and that no segment of the curve $x = x(t), y = y(t) \ (a \le t \le b)$ is traced more than once.**
29. Let $S$ be the area of the surface generated by revolving the curve $x = x(t), y = y(t) \ (a \le t \le b)$ about the $x$-axis. Explain how $S$ can be approximated by
    $$S \approx \sum_{k=1}^n \left(\pi [y(t_{k-1}) + y(t_k)] \times \sqrt{[x(t_k) - x(t_{k-1})]^2 + [y(t_k) - y(t_{k-1})]^2}\right)$$
    Using results from advanced calculus, it can be shown that as $\max \Delta t_k \to 0$, this sum converges to
    $$S = \int_a^b 2\pi y(t)\sqrt{[x'(t)]^2 + [y'(t)]^2} dt \tag{A}$$
30. Let $S$ be the area of the surface generated by revolving the curve $x = x(t), y = y(t) \ (a \le t \le b)$ about the $y$-axis. Explain how $S$ can be approximated by
    $$S \approx \sum_{k=1}^n \left(\pi [x(t_{k-1}) + x(t_k)] \times \sqrt{[x(t_k) - x(t_{k-1})]^2 + [y(t_k) - y(t_{k-1})]^2}\right)$$
    Using results from advanced calculus, it can be shown that as $\max \Delta t_k \to 0$, this sum converges to
    $$S = \int_a^b 2\pi x(t)\sqrt{[x'(t)]^2 + [y'(t)]^2} dt \tag{B}$$

**31–35 Use Formulas (A) and (B) from Exercises 29 and 30.**
31. Find the area of the surface generated by revolving the parametric curve $x = t^2, y = 2t \ (0 \le t \le 4)$ about the $x$-axis.
32. [CAS] Use a CAS to find the area of the surface generated by revolving the parametric curve $x = \cos^2 t, y = 5\sin t \ (0 \le t \le \pi/2)$ about the $x$-axis.
33. Find the area of the surface generated by revolving the parametric curve $x = t, y = 2t^2 \ (0 \le t \le 1)$ about the $y$-axis.
34. Find the area of the surface generated by revolving the parametric curve $x = \cos^2 t, y = \sin^2 t \ (0 \le t \le \pi/2)$ about the $y$-axis.
35. By revolving the semicircle $x = r\cos t, y = r\sin t \ (0 \le t \le \pi)$ about the $x$-axis, show that the surface area of a sphere of radius $r$ is $4\pi r^2$.
36. **Writing.** Compare the derivation of Definition 5.5.2 with that of Definition 5.4.2. Discuss the geometric features that result in similarities in the two definitions.
37. **Writing.** Discuss what goes wrong if we replace the frustums of right circular cones by right circular cylinders in the derivation of Definition 5.5.2.

---

## 5.6 WORK

In this section we will use the integration tools developed in the preceding chapter to study some of the basic principles of “work,” which is one of the fundamental concepts in physics and engineering.

### THE ROLE OF WORK IN PHYSICS AND ENGINEERING
In this section we will be concerned with two related concepts, work and energy. To put these ideas in a familiar setting, when you push a stalled car for a certain distance you are performing work, and the effect of your work is to make the car move. The energy of motion caused by the work is called the *kinetic energy* of the car. The exact connection between work and kinetic energy is governed by a principle of physics called the *work–energy relationship*. Although we will touch on this idea in this section, a detailed study of the relationship between work and energy will be left for courses in physics and engineering. Our primary goal here will be to explain the role of integration in the study of work.

### WORK DONE BY A CONSTANT FORCE APPLIED IN THE DIRECTION OF MOTION
When a stalled car is pushed, the speed that the car attains depends on the force $F$ with which it is pushed and the distance $d$ over which that force is applied (Figure 5.6.1). Force and distance appear in the following definition of work.

> **5.6.1 DEFINITION**  
> If a constant force of magnitude $F$ is applied in the direction of motion of an object, and if that object moves a distance $d$, then we define the **work** $W$ performed by the force on the object to be
> $$W = F \cdot d \tag{1}$$

*If you push against an immovable object, such as a brick wall, you may tire yourself out, but you will not perform any work. Why?*

Common units for measuring force are newtons (N) in the International System of Units (SI), dynes (dyn) in the centimeter-gram-second (CGS) system, and pounds (lb) in the British Engineering (BE) system. One newton is the force required to give a mass of $1\text{ kg}$ an acceleration of $1\text{ m/s}^2$, one dyne is the force required to give a mass of $1\text{ g}$ an acceleration of $1\text{ cm/s}^2$, and one pound of force is the force required to give a mass of $1\text{ slug}$ an acceleration of $1\text{ ft/s}^2$.

It follows from Definition 5.6.1 that work has units of force times distance. The most common units of work are newton-meters ($\text{N}\cdot\text{m}$), dyne-centimeters ($\text{dyn}\cdot\text{cm}$), and foot-pounds ($\text{ft}\cdot\text{lb}$). As indicated in Table 5.6.1, one newton-meter is also called a **joule** (J), and one dyne-centimeter is also called an **erg**. One foot-pound is approximately $1.36\text{ J}$.

#### Table 5.6.1: Units of Force and Work
| SYSTEM | FORCE $\times$ | DISTANCE $=$ | WORK |
| :--- | :--- | :--- | :--- |
| SI | newton (N) | meter (m) | joule (J) |
| CGS | dyne (dyn) | centimeter (cm) | erg |
| BE | pound (lb) | foot (ft) | foot-pound ($\text{ft}\cdot\text{lb}$) |

**Conversion Factors:**
* $1\text{ N} = 10^5\text{ dyn} \approx 0.225\text{ lb}$
* $1\text{ lb} \approx 4.45\text{ N}$
* $1\text{ J} = 10^7\text{ erg} \approx 0.738\text{ ft}\cdot\text{lb}$
* $1\text{ ft}\cdot\text{lb} \approx 1.36\text{ J} = 1.36 \times 10^7\text{ erg}$

#### Example 1
An object moves $5\text{ ft}$ along a line while subjected to a constant force of $100\text{ lb}$ in its direction of motion. The work done is
$$W = F \cdot d = 100 \cdot 5 = 500\text{ ft}\cdot\text{lb}$$
An object moves $25\text{ m}$ along a line while subjected to a constant force of $4\text{ N}$ in its direction of motion. The work done is
$$W = F \cdot d = 4 \cdot 25 = 100\text{ N}\cdot\text{m} = 100\text{ J}$$

#### Example 2
In the 1976 Olympics, Vasili Alexeev astounded the world by lifting a record-breaking $562\text{ lb}$ from the floor to above his head (about $2\text{ m}$). Equally astounding was the feat of strongman Paul Anderson, who in 1957 braced himself on the floor and used his back to lift $6270\text{ lb}$ of lead and automobile parts a distance of $1\text{ cm}$. Who did more work?

**Solution.** To lift an object one must apply sufficient force to overcome the gravitational force that the Earth exerts on that object. The force that the Earth exerts on an object is that object’s weight; thus, in performing their feats, Alexeev applied a force of $562\text{ lb}$ over a distance of $2\text{ m}$ and Anderson applied a force of $6270\text{ lb}$ over a distance of $1\text{ cm}$. Pounds are units in the BE system, meters are units in SI, and centimeters are units in the CGS system. We will need to decide on the measurement system we want to use and be consistent. Let us agree to use SI and express the work of the two men in joules. Using the conversion factor in Table 5.6.1 we obtain
$$562\text{ lb} \approx 562\text{ lb} \times 4.45\text{ N/lb} \approx 2500\text{ N}$$
$$6270\text{ lb} \approx 6270\text{ lb} \times 4.45\text{ N/lb} \approx 27,900\text{ N}$$
Using these values and the fact that $1\text{ cm} = 0.01\text{ m}$ we obtain
$$\text{Alexeev's work} = (2500\text{ N}) \times (2\text{ m}) = 5000\text{ J}$$
$$\text{Anderson's work} = (27,900\text{ N}) \times (0.01\text{ m}) = 279\text{ J}$$
Therefore, even though Anderson’s lift required a tremendous upward force, it was applied over such a short distance that Alexeev did more work.

---

### WORK DONE BY A VARIABLE FORCE APPLIED IN THE DIRECTION OF MOTION
Many important problems are concerned with finding the work done by a variable force that is applied in the direction of motion. For example, Figure 5.6.2a shows a spring in its natural state (neither compressed nor stretched). If we want to pull the block horizontally (Figure 5.6.2b), then we would have to apply more and more force to the block to overcome the increasing force of the stretching spring. Thus, our next objective is to define what is meant by the work performed by a variable force and to find a formula for computing it. This will require calculus.

> **5.6.2 PROBLEM**  
> Suppose that an object moves in the positive direction along a coordinate line while subjected to a variable force $F(x)$ that is applied in the direction of motion. Define what is meant by the work $W$ performed by the force on the object as the object moves from $x = a$ to $x = b$, and find a formula for computing the work.

The basic idea for solving this problem is to break up the interval $[a, b]$ into subintervals that are sufficiently small that the force does not vary much on each subinterval. This will allow us to treat the force as constant on each subinterval and to approximate the work on each subinterval using Formula (1). By adding the approximations to the work on the subintervals, we will obtain a Riemann sum that approximates the work $W$ over the entire interval, and by taking the limit of the Riemann sums we will obtain an integral for $W$.

To implement this idea, divide the interval $[a, b]$ into $n$ subintervals by inserting points $x_1, x_2, \dots, x_{n-1}$ between $a = x_0$ and $b = x_n$. We can use Formula (1) to approximate the work $W_k$ done in the $k$th subinterval by choosing any point $x_k^*$ in this interval and regarding the force to have a constant value $F(x_k^*)$ throughout the interval. Since the width of the $k$th subinterval is $x_k - x_{k-1} = \Delta x_k$, this yields the approximation
$$W_k \approx F(x_k^*) \Delta x_k$$

Adding these approximations yields the following Riemann sum that approximates the work $W$ done over the entire interval:
$$W \approx \sum_{k=1}^n F(x_k^*) \Delta x_k$$

Taking the limit as $n$ increases and the widths of all the subintervals approach zero yields the definite integral
$$W = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n F(x_k^*) \Delta x_k = \int_a^b F(x) dx$$

In summary, we have the following result.

> **5.6.3 DEFINITION**  
> Suppose that an object moves in the positive direction along a coordinate line over the interval $[a, b]$ while subjected to a variable force $F(x)$ that is applied in the direction of motion. Then we define the **work** $W$ performed by the force on the object to be
> $$W = \int_a^b F(x) dx \tag{2}$$

**Hooke’s law** [Robert Hooke (1635–1703), English physicist] states that under appropriate conditions a spring that is stretched $x$ units beyond its natural length pulls back with a force
$$F(x) = kx$$
where $k$ is a constant (called the **spring constant** or **spring stiffness**). The value of $k$ depends on such factors as the thickness of the spring and the material used in its composition. Since $k = F(x)/x$, the constant $k$ has units of force per unit length.

#### Example 3
A spring exerts a force of $5\text{ N}$ when stretched $1\text{ m}$ beyond its natural length.  
(a) Find the spring constant $k$.  
(b) How much work is required to stretch the spring $1.8\text{ m}$ beyond its natural length?

**Solution (a).** From Hooke’s law, $F(x) = kx$. From the data, $F(x) = 5\text{ N}$ when $x = 1\text{ m}$, so $5 = k \cdot 1$. Thus, the spring constant is $k = 5$ newtons per meter (N/m). This means that the force $F(x)$ required to stretch the spring $x$ meters is
$$F(x) = 5x \tag{3}$$

**Solution (b).** Place the spring along a coordinate line as shown in Figure 5.6.3. We want to find the work $W$ required to stretch the spring over the interval from $x = 0$ to $x = 1.8$. From (2) and (3) the work $W$ required is
$$W = \int_a^b F(x) dx = \int_0^{1.8} 5x dx = \left[\frac{5x^2}{2}\right]_0^{1.8} = 8.1\text{ J}$$

#### Example 4
An astronaut’s weight (or more precisely, Earth weight) is the force exerted on the astronaut by the Earth’s gravity. As the astronaut moves upward into space, the gravitational pull of the Earth decreases, and hence so does his or her weight. If the Earth is assumed to be a sphere of radius $4000\text{ mi}$, then it follows from Newton’s Law of Universal Gravitation that an astronaut who weighs $150\text{ lb}$ on Earth will have a weight of
$$w(x) = \frac{2,400,000,000}{x^2}\text{ lb}, \quad x \ge 4000$$
at a distance of $x$ miles from the Earth’s center (Exercise 25). Use this formula to estimate the work in foot-pounds required to lift the astronaut 220 miles upward to the International Space Station.

**Solution.** Since the Earth has a radius of $4000\text{ mi}$, the astronaut is lifted from a point that is $4000\text{ mi}$ from the Earth’s center to a point that is $4220\text{ mi}$ from the Earth’s center. Thus, from (2), the work $W$ required to lift the astronaut is
$$W = \int_{4000}^{4220} \frac{2,400,000,000}{x^2} dx = \left[-\frac{2,400,000,000}{x}\right]_{4000}^{4220} \approx -568,720 + 600,000 = 31,280\text{ mile}\cdot\text{pounds}$$
$$= (31,280\text{ mi}\cdot\text{lb}) \times (5280\text{ ft/mi}) \approx 1.65 \times 10^8\text{ ft}\cdot\text{lb}$$

---

### CALCULATING WORK FROM BASIC PRINCIPLES
Some problems cannot be solved by mechanically substituting into formulas, and one must return to basic principles to obtain solutions. This is illustrated in the next example.

#### Example 5
Figure 5.6.4a shows a conical container of radius $10\text{ ft}$ and height $30\text{ ft}$. Suppose that this container is filled with water to a depth of $15\text{ ft}$. How much work is required to pump all of the water out through a hole in the top of the container?

**Solution.** Our strategy will be to divide the water into thin layers, approximate the work required to move each layer to the top of the container, add the approximations for the layers to obtain a Riemann sum that approximates the total work, and then take the limit of the Riemann sums to produce an integral for the total work.

To implement this idea, introduce an $x$-axis as shown in Figure 5.6.4a, and divide the water into $n$ layers with $\Delta x_k$ denoting the thickness of the $k$th layer. This division induces a partition of the interval $[15, 30]$ into $n$ subintervals. Although the upper and lower surfaces of the $k$th layer are at different distances from the top, the difference will be small if the layer is thin, and we can reasonably assume that the entire layer is concentrated at a single point $x_k^*$ (Figure 5.6.4a). Thus, the work $W_k$ required to move the $k$th layer to the top of the container is approximately
$$W_k \approx F_k x_k^* \tag{4}$$
where $F_k$ is the force required to lift the $k$th layer. But the force required to lift the $k$th layer is the force needed to overcome gravity, and this is the same as the weight of the layer. If the layer is very thin, we can approximate the volume of the $k$th layer with the volume of a cylinder of height $\Delta x_k$ and radius $r_k$, where (by similar triangles)
$$\frac{r_k}{x_k^*} = \frac{10}{30} = \frac{1}{3} \quad\text{or, equivalently,}\quad r_k = x_k^*/3$$
(Figure 5.6.4b). Therefore, the volume of the $k$th layer of water is approximately
$$\pi r_k^2 \Delta x_k = \pi(x_k^*/3)^2 \Delta x_k = \frac{\pi}{9}(x_k^*)^2 \Delta x_k$$

Since the weight density of water is $62.4\text{ lb/ft}^3$, it follows that
$$F_k \approx \frac{62.4\pi}{9}(x_k^*)^2 \Delta x_k$$
Thus, from (4)
$$W_k \approx \left[\frac{62.4\pi}{9}(x_k^*)^2 \Delta x_k\right] x_k^* = \frac{62.4\pi}{9}(x_k^*)^3 \Delta x_k$$
and hence the work $W$ required to move all $n$ layers has the approximation
$$W = \sum_{k=1}^n W_k \approx \sum_{k=1}^n \frac{62.4\pi}{9}(x_k^*)^3 \Delta x_k$$

To find the exact value of the work we take the limit as $\max \Delta x_k \to 0$. This yields
$$W = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n \frac{62.4\pi}{9}(x_k^*)^3 \Delta x_k = \int_{15}^{30} \frac{62.4\pi}{9}x^3 dx = \frac{62.4\pi}{9}\left[\frac{x^4}{4}\right]_{15}^{30} = 1,316,250\pi \approx 4,135,000\text{ ft}\cdot\text{lb}$$

---

### THE WORK–ENERGY RELATIONSHIP
When you see an object in motion, you can be certain that somehow work has been expended to create that motion. For example, when you drop a stone from a building, the stone gathers speed because the force of the Earth’s gravity is performing work on it, and when a hockey player strikes a puck with a hockey stick, the work performed on the puck during the brief period of contact with the stick creates the enormous speed of the puck across the ice. However, experience shows that the speed obtained by an object depends not only on the amount of work done, but also on the mass of the object. For example, the work required to throw a $5\text{ oz}$ baseball $50\text{ mi/h}$ would accelerate a $10\text{ lb}$ bowling ball to less than $9\text{ mi/h}$.

Using the method of substitution for definite integrals, we will derive a simple equation that relates the work done on an object to the object’s mass and velocity. Furthermore, this equation will allow us to motivate an appropriate definition for the “energy of motion” of an object. As in Definition 5.6.3, we will assume that an object moves in the positive direction along a coordinate line over the interval $[a, b]$ while subjected to a force $F(x)$ that is applied in the direction of motion. We let $m$ denote the mass of the object, and we let $x = x(t), v = v(t) = x'(t),$ and $a = a(t) = v'(t)$ denote the respective position, velocity, and acceleration of the object at time $t$. We will need the following important result from physics that relates the force acting on an object with the mass and acceleration of the object.

> **5.6.4 NEWTON’S SECOND LAW OF MOTION**  
> If an object with mass $m$ is subjected to a force $F$, then the object undergoes an acceleration $a$ that satisfies the equation
> $$F = ma \tag{5}$$

It follows from Newton’s Second Law of Motion that $F(x(t)) = ma(t) = mv'(t)$. Assume that $x(t_0) = a$ and $x(t_1) = b$ with $v(t_0) = v_i$ and $v(t_1) = v_f$ the initial and final velocities of the object, respectively. Then
$$W = \int_a^b F(x) dx = \int_{x(t_0)}^{x(t_1)} F(x) dx = \int_{t_0}^{t_1} F(x(t))x'(t) dt \quad [\text{By Theorem 4.9.1 with } x = x(t), dx = x'(t)dt]$$
$$= \int_{t_0}^{t_1} mv'(t)v(t) dt = \int_{t_0}^{t_1} mv(t)v'(t) dt = \int_{v(t_0)}^{v(t_1)} mv dv \quad [\text{By Theorem 4.9.1 with } v = v(t), dv = v'(t)dt]$$
$$= \int_{v_i}^{v_f} mv dv = \left[\frac{1}{2}mv^2\right]_{v_i}^{v_f} = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2$$

We see from the equation
$$W = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2 \tag{6}$$
that the work done on the object is equal to the change in the quantity $\frac{1}{2}mv^2$ from its initial value to its final value. We will refer to Equation (6) as the **work–energy relationship**. If we define the “energy of motion” or **kinetic energy** of our object to be given by
$$K = \frac{1}{2}mv^2 \tag{7}$$
then Equation (6) tells us that the work done on an object is equal to the change in the object’s kinetic energy. Loosely speaking, we may think of work done on an object as being “transformed” into kinetic energy of the object. The units of kinetic energy are the same as the units of work. For example, in SI kinetic energy is measured in joules (J).

#### Example 6
A space probe of mass $m = 5.00 \times 10^4\text{ kg}$ travels in deep space subjected only to the force of its own engine. Starting at a time when the speed of the probe is $v = 1.10 \times 10^4\text{ m/s}$, the engine is fired continuously over a distance of $2.50 \times 10^6\text{ m}$ with a constant force of $4.00 \times 10^5\text{ N}$ in the direction of motion. What is the final speed of the probe?

**Solution.** Since the force applied by the engine is constant and in the direction of motion, the work $W$ expended by the engine on the probe is
$$W = \text{force} \times \text{distance} = (4.00 \times 10^5\text{ N}) \times (2.50 \times 10^6\text{ m}) = 1.00 \times 10^{12}\text{ J}$$
From (6), the final kinetic energy $K_f = \frac{1}{2}mv_f^2$ of the probe can be expressed in terms of the work $W$ and the initial kinetic energy $K_i = \frac{1}{2}mv_i^2$ as
$$K_f = W + K_i$$
Thus, from the known mass and initial speed we have
$$K_f = (1.00 \times 10^{12}\text{ J}) + \frac{1}{2}(5.00 \times 10^4\text{ kg})(1.10 \times 10^4\text{ m/s})^2 = 4.025 \times 10^{12}\text{ J}$$
The final kinetic energy is $K_f = \frac{1}{2}mv_f^2$, so the final speed of the probe is
$$v_f = \sqrt{\frac{2K_f}{m}} = \sqrt{\frac{2(4.025 \times 10^{12})}{5.00 \times 10^4}} \approx 1.27 \times 10^4\text{ m/s}$$

---

### QUICK CHECK EXERCISES 5.6
*(See page 391 for answers.)*

1. If a constant force of $5\text{ lb}$ moves an object $10\text{ ft}$, then the work done by the force on the object is $\underline{\hspace{1.5cm}}$.
2. A newton-meter is also called a $\underline{\hspace{1.5cm}}$. A dyne-centimeter is also called an $\underline{\hspace{1.5cm}}$.
3. Suppose that an object moves in the positive direction along a coordinate line over the interval $[a, b]$. The work performed on the object by a variable force $F(x)$ applied in the direction of motion is $W = \underline{\hspace{1.5cm}}$.
4. A force $F(x) = 10 - 2x\text{ N}$ applied in the positive $x$-direction moves an object $3\text{ m}$ from $x = 2$ to $x = 5$. The work done by the force on the object is $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 5.6
1. $50\text{ ft}\cdot\text{lb}$  
2. joule; erg  
3. $\int_a^b F(x) dx$  
4. $9\text{ J}$

---

### EXERCISE SET 5.6

#### FOCUS ON CONCEPTS
1. A variable force $F(x)$ in the positive $x$-direction is graphed in the accompanying figure (linear from $(0, 4)$ to $(3, 1)$). Find the work done by the force on a particle that moves from $x = 0$ to $x = 3$.
2. A variable force $F(x)$ in the positive $x$-direction is graphed in the accompanying figure (horizontal at $F = 40$ from $x = 0$ to $x = 1$, then linear down to $(5, 0)$). Find the work done by the force on a particle that moves from $x = 0$ to $x = 5$.
3. For the variable force $F(x)$ in Exercise 2, consider the distance $d$ for which the work done by the force on the particle when the particle moves from $x = 0$ to $x = d$ is half of the work done when the particle moves from $x = 0$ to $x = 5$. By inspecting the graph of $F$, is $d$ more or less than 2.5? Explain, and then find the exact value of $d$.
4. Suppose that a variable force $F(x)$ is applied in the positive $x$-direction so that an object moves from $x = a$ to $x = b$. Relate the work done by the force on the object and the average value of $F$ over $[a, b]$, and illustrate this relationship graphically.
5. A constant force of $10\text{ lb}$ in the positive $x$-direction is applied to a particle whose velocity versus time curve is shown in the accompanying figure (linear $v(t) = t$). Find the work done by the force on the particle from time $t = 0$ to $t = 5$.

6. A spring exerts a force of $6\text{ N}$ when it is stretched from its natural length of $4\text{ m}$ to a length of $4\frac{1}{2}\text{ m}$. Find the work required to stretch the spring from its natural length to a length of $6\text{ m}$.
7. A spring exerts a force of $100\text{ N}$ when it is stretched $0.2\text{ m}$ beyond its natural length. How much work is required to stretch the spring $0.8\text{ m}$ beyond its natural length?
8. A spring whose natural length is $15\text{ cm}$ exerts a force of $45\text{ N}$ when stretched to a length of $20\text{ cm}$.  
   (a) Find the spring constant (in newtons/meter).  
   (b) Find the work that is done in stretching the spring $3\text{ cm}$ beyond its natural length.  
   (c) Find the work done in stretching the spring from a length of $20\text{ cm}$ to a length of $25\text{ cm}$.
9. Assume that $10\text{ ft}\cdot\text{lb}$ of work is required to stretch a spring $1\text{ ft}$ beyond its natural length. What is the spring constant?

**10–13 True–False Determine whether the statement is true or false. Explain your answer.**
10. In order to support the weight of a parked automobile, the surface of a driveway must do work against the force of gravity on the vehicle.
11. A force of $10\text{ lb}$ in the direction of motion of an object that moves $5\text{ ft}$ in $2\text{ s}$ does six times the work of a force of $10\text{ lb}$ in the direction of motion of an object that moves $5\text{ ft}$ in $12\text{ s}$.
12. It follows from Hooke’s law that in order to double the distance a spring is stretched beyond its natural length, four times as much work is required.
13. In the International System of Units, work and kinetic energy have the same units.

14. A cylindrical tank of radius $5\text{ ft}$ and height $9\text{ ft}$ is two-thirds filled with water. Find the work required to pump all the water over the upper rim.
15. Solve Exercise 14 assuming that the tank is half-filled with water.
16. A cone-shaped water reservoir is $20\text{ ft}$ in diameter across the top and $15\text{ ft}$ deep. If the reservoir is filled to a depth of $10\text{ ft}$, how much work is required to pump all the water to the top of the reservoir?
17. The vat shown in the accompanying figure (trapezoidal cross section top width $6\text{ m}$, bottom width $4\text{ m}$, height $3\text{ m}$, length $10\text{ m}$) contains water to a depth of $2\text{ m}$. Find the work required to pump all the water to the top of the vat. [Use $9810\text{ N/m}^3$ as the weight density of water.]
18. The cylindrical tank shown in the accompanying figure (horizontal cylinder radius $4\text{ ft}$, length $10\text{ ft}$) is filled with a liquid weighing $50\text{ lb/ft}^3$. Find the work required to pump all the liquid to a level $1\text{ ft}$ above the top of the tank.
19. A swimming pool is built in the shape of a rectangular parallelepiped $10\text{ ft}$ deep, $15\text{ ft}$ wide, and $20\text{ ft}$ long.  
    (a) If the pool is filled to $1\text{ ft}$ below the top, how much work is required to pump all the water into a drain at the top edge of the pool?  
    (b) A one-horsepower motor can do $550\text{ ft}\cdot\text{lb}$ of work per second. What size motor is required to empty the pool in 1 hour?
20. How much work is required to fill the swimming pool in Exercise 19 to $1\text{ ft}$ below the top if the water is pumped in through an opening located at the bottom of the pool?
21. A $100\text{ ft}$ length of steel chain weighing $15\text{ lb/ft}$ is dangling from a pulley. How much work is required to wind the chain onto the pulley?
22. A $3\text{ lb}$ bucket containing $20\text{ lb}$ of water is hanging at the end of a $20\text{ ft}$ rope that weighs $4\text{ oz/ft}$. The other end of the rope is attached to a pulley. How much work is required to wind the length of rope onto the pulley, assuming that the rope is wound onto the pulley at a rate of $2\text{ ft/s}$ and that as the bucket is being lifted, water leaks from the bucket at a rate of $0.5\text{ lb/s}$?
23. A rocket weighing 3 tons is filled with 40 tons of liquid fuel. In the initial part of the flight, fuel is burned off at a constant rate of 2 tons per $1000\text{ ft}$ of vertical height. How much work in foot-tons ($\text{ft}\cdot\text{ton}$) is done lifting the rocket $3000\text{ ft}$?
24. It follows from Coulomb’s law in physics that two like electrostatic charges repel each other with a force inversely proportional to the square of the distance between them. Suppose that two charges $A$ and $B$ repel with a force of $k$ newtons when they are positioned at points $A(-a, 0)$ and $B(a, 0)$, where $a$ is measured in meters. Find the work $W$ required to move charge $A$ along the $x$-axis to the origin if charge $B$ remains stationary.
25. It follows from Newton’s Law of Universal Gravitation that the gravitational force exerted by the Earth on an object above the Earth’s surface varies inversely as the square of its distance from the Earth’s center. Thus, an object’s weight $w(x)$ is related to its distance $x$ from the Earth’s center by a formula of the form
    $$w(x) = \frac{k}{x^2}$$
    where $k$ is a constant of proportionality that depends on the mass of the object.  
    (a) Use this fact and the assumption that the Earth is a sphere of radius $4000\text{ mi}$ to obtain the formula for $w(x)$ in Example 4.  
    (b) Find a formula for the weight $w(x)$ of a satellite that is $x\text{ mi}$ from the Earth’s surface if its weight on Earth is $6000\text{ lb}$.  
    (c) How much work is required to lift the satellite from the surface of the Earth to an orbital position that is $1000\text{ mi}$ high?
26. (a) The formula $w(x) = k/x^2$ in Exercise 25 is applicable to all celestial bodies. Assuming that the Moon is a sphere of radius $1080\text{ mi}$, find the force that the Moon exerts on an astronaut who is $x\text{ mi}$ from the surface of the Moon if her weight on the Moon’s surface is $20\text{ lb}$.  
    (b) How much work is required to lift the astronaut to a point that is $10.8\text{ mi}$ above the Moon’s surface?
27. The world’s first commercial high-speed magnetic levitation (MAGLEV) train, a $30\text{ km}$ double-track project connecting Shanghai, China, to Pudong International Airport, began full revenue service in 2003. Suppose that a MAGLEV train has a mass $m = 4.00 \times 10^5\text{ kg}$ and that starting at a time when the train has a speed of $20\text{ m/s}$ the engine applies a force of $6.40 \times 10^5\text{ N}$ in the direction of motion over a distance of $3.00 \times 10^3\text{ m}$. Use the work–energy relationship (6) to find the final speed of the train.
28. Assume that a Mars probe of mass $m = 2.00 \times 10^3\text{ kg}$ is subjected only to the force of its own engine. Starting at a time when the speed of the probe is $v = 1.00 \times 10^4\text{ m/s}$, the engine is fired continuously over a distance of $1.50 \times 10^5\text{ m}$ with a constant force of $2.00 \times 10^5\text{ N}$ in the direction of motion. Use the work–energy relationship (6) to find the final speed of the probe.
29. On August 10, 1972 a meteorite with an estimated mass of $4 \times 10^6\text{ kg}$ and an estimated speed of $15\text{ km/s}$ skipped across the atmosphere above the western United States and Canada but fortunately did not hit the Earth.  
    (a) Assuming that the meteorite had hit the Earth with a speed of $15\text{ km/s}$, what would have been its change in kinetic energy in joules (J)?  
    (b) Express the energy as a multiple of the explosive energy of 1 megaton of TNT, which is $4.2 \times 10^{15}\text{ J}$.  
    (c) The energy associated with the Hiroshima atomic bomb was 13 kilotons of TNT. To how many such bombs would the meteorite impact have been equivalent?
30. **Writing.** After reading Examples 3–5, a student classifies work problems as either “pushing/pulling” or “pumping.” Describe these categories in your own words and discuss the methods used to solve each type. Give examples to illustrate that these categories are not mutually exclusive.
31. **Writing.** How might you recognize that a problem can be solved by means of the work–energy relationship? That is, what sort of “givens” and “unknowns” would suggest such a solution? Discuss two or three examples.

---

## 5.7 MOMENTS, CENTERS OF GRAVITY, AND CENTROIDS

Suppose that a rigid physical body is acted on by a constant gravitational field. Because the body is composed of many particles, each of which is affected by gravity, the action of the gravitational field on the body consists of a large number of forces distributed over the entire body. However, it is a fact of physics that these individual forces can be replaced by a single force acting at a point called the **center of gravity** of the body. In this section we will show how integrals can be used to locate centers of gravity.

### DENSITY AND MASS OF A LAMINA
Let us consider an idealized flat object that is thin enough to be viewed as a two-dimensional plane region (Figure 5.7.1). Such an object is called a **lamina**. A lamina is called **homogeneous** if its composition is uniform throughout and **inhomogeneous** otherwise. We will consider homogeneous laminas in this section. Inhomogeneous laminas will be discussed in Chapter 14. The density of a homogeneous lamina is defined to be its mass per unit area. Thus, the density $\delta$ of a homogeneous lamina of mass $M$ and area $A$ is given by $\delta = M/A$. Notice that the mass $M$ of a homogeneous lamina can be expressed as
$$M = \delta A \tag{1}$$

#### Example 1
A triangular lamina with vertices $(0, 0), (0, 1),$ and $(1, 0)$ has density $\delta = 3$. Find its total mass.

**Solution.** Referring to (1) and Figure 5.7.2, the mass $M$ of the lamina is
$$M = \delta A = 3 \cdot \frac{1}{2} = \frac{3}{2}\text{ (unit of mass)}$$

---

### CENTER OF GRAVITY OF A LAMINA
Assume that the acceleration due to the force of gravity is constant and acts downward, and suppose that a lamina occupies a region $R$ in a horizontal $xy$-plane. It can be shown that there exists a unique point $(\bar{x}, \bar{y})$ (which may or may not belong to $R$) such that the effect of gravity on the lamina is “equivalent” to that of a single force acting at the point $(\bar{x}, \bar{y})$. This point is called the **center of gravity** of the lamina, and if it is in $R$, then the lamina will balance horizontally on the point of a support placed at $(\bar{x}, \bar{y})$. For example, the center of gravity of a homogeneous disk is at the center of the disk, and the center of gravity of a homogeneous rectangular region is at the center of the rectangle. For an irregularly shaped homogeneous lamina, locating the center of gravity requires calculus.

> **5.7.1 PROBLEM**  
> Let $f$ be a positive continuous function on the interval $[a, b]$. Suppose that a homogeneous lamina with constant density $\delta$ occupies a region $R$ in a horizontal $xy$-plane bounded by the graphs of $y = f(x), y = 0, x = a,$ and $x = b$. Find the coordinates $(\bar{x}, \bar{y})$ of the center of gravity of the lamina.

To motivate the solution, consider what happens if we try to balance the lamina on a knife-edge parallel to the $x$-axis. Suppose the lamina in Figure 5.7.3 is placed on a knife-edge along a line $y = c$ that does not pass through the center of gravity. Because the lamina behaves as if its entire mass is concentrated at the center of gravity $(\bar{x}, \bar{y})$, the lamina will be rotationally unstable and the force of gravity will cause a rotation about $y = c$. Similarly, the lamina will undergo a rotation if placed on a knife-edge along $y = d$. However, if the knife-edge runs along the line $y = \bar{y}$ through the center of gravity, the lamina will be in perfect balance. Similarly, the lamina will be in perfect balance on a knife-edge along the line $x = \bar{x}$ through the center of gravity. This suggests that the center of gravity of a lamina can be determined as the intersection of two lines of balance, one parallel to the $x$-axis and the other parallel to the $y$-axis. In order to find these lines of balance, we will need some preliminary results about rotations.

Children on a seesaw learn by experience that a lighter child can balance a heavier one by sitting farther from the fulcrum or pivot point. This is because the tendency for an object to produce rotation is proportional not only to its mass but also to the distance between the object and the fulcrum. To make this more precise, consider an $x$-axis, which we view as a weightless beam. If a mass $m$ is located on the axis at $x$, then the tendency for that mass to produce a rotation of the beam about a point $a$ on the axis is measured by the following quantity, called the **moment of $m$ about $x = a$**:
$$\left[\text{moment of } m \text{ about } a\right] = m(x - a)$$

The number $x - a$ is called the **lever arm**. Depending on whether the mass is to the right or left of $a$, the lever arm is either the distance between $x$ and $a$ or the negative of this distance (Figure 5.7.4). Positive lever arms result in positive moments and clockwise rotations, and negative lever arms result in negative moments and counterclockwise rotations.

Suppose that masses $m_1, m_2, \dots, m_n$ are located at $x_1, x_2, \dots, x_n$ on a coordinate axis and a fulcrum is positioned at the point $a$ (Figure 5.7.5). Depending on whether the sum of the moments about $a$,
$$\sum_{k=1}^n m_k(x_k - a) = m_1(x_1 - a) + m_2(x_2 - a) + \dots + m_n(x_n - a)$$
is positive, negative, or zero, a weightless beam along the axis will rotate clockwise about $a$, rotate counterclockwise about $a$, or balance perfectly. In the last case, the system of masses is said to be in **equilibrium**.

The preceding ideas can be extended to masses distributed in two-dimensional space. If we imagine the $xy$-plane to be a weightless sheet supporting a mass $m$ located at a point $(x, y)$, then the tendency for the mass to produce a rotation of the sheet about the line $x = a$ is $m(x - a)$, called the **moment of $m$ about $x = a$**, and the tendency for the mass to produce a rotation about the line $y = c$ is $m(y - c)$, called the **moment of $m$ about $y = c$** (Figure 5.7.6). In summary,
$$\left[\text{moment of } m \text{ about the line } x = a\right] = m(x - a) \quad\text{and}\quad \left[\text{moment of } m \text{ about the line } y = c\right] = m(y - c) \tag{2–3}$$

If a number of masses are distributed throughout the $xy$-plane, then the plane (viewed as a weightless sheet) will balance on a knife-edge along the line $x = a$ if the sum of the moments about the line is zero. Similarly, the plane will balance on a knife-edge along the line $y = c$ if the sum of the moments about that line is zero.

We are now ready to solve Problem 5.7.1. The basic idea for solving this problem is to divide the lamina into strips whose areas may be approximated by the areas of rectangles. These area approximations, along with Formulas (2) and (3), will allow us to create a Riemann sum that approximates the moment of the lamina about a horizontal or vertical line. By taking the limit of Riemann sums we will then obtain an integral for the moment of a lamina about a horizontal or vertical line. We observe that since the lamina balances on the lines $x = \bar{x}$ and $y = \bar{y}$, the moment of the lamina about those lines should be zero. This observation will enable us to calculate $\bar{x}$ and $\bar{y}$.

To implement this idea, we divide the interval $[a, b]$ into $n$ subintervals by inserting the points $x_1, x_2, \dots, x_{n-1}$ between $a = x_0$ and $b = x_n$. This has the effect of dividing the lamina $R$ into $n$ strips $R_1, R_2, \dots, R_n$ (Figure 5.7.7a). Suppose that the $k$th strip extends from $x_{k-1}$ to $x_k$ and that the width of this strip is $\Delta x_k = x_k - x_{k-1}$.

We will let $x_k^*$ be the midpoint of the $k$th subinterval and we will approximate $R_k$ by a rectangle of width $\Delta x_k$ and height $f(x_k^*)$. From (1), the mass $\Delta M_k$ of this rectangle is $\Delta M_k = \delta f(x_k^*) \Delta x_k$, and we will assume that the rectangle behaves as if its entire mass is concentrated at its center $(x_k^*, y_k^*) = (x_k^*, \frac{1}{2}f(x_k^*))$ (Figure 5.7.7b). It then follows from (2) and (3) that the moments of $R_k$ about the lines $x = \bar{x}$ and $y = \bar{y}$ may be approximated by $(x_k^* - \bar{x})\Delta M_k$ and $(y_k^* - \bar{y})\Delta M_k$, respectively. Adding these approximations yields the following Riemann sums that approximate the moment of the entire lamina about the lines $x = \bar{x}$ and $y = \bar{y}$:
$$\sum_{k=1}^n (x_k^* - \bar{x})\Delta M_k = \sum_{k=1}^n (x_k^* - \bar{x})\delta f(x_k^*) \Delta x_k$$
$$\sum_{k=1}^n (y_k^* - \bar{y})\Delta M_k = \sum_{k=1}^n \left(\frac{f(x_k^*)}{2} - \bar{y}\right)\delta f(x_k^*) \Delta x_k$$

Taking the limits as $n$ increases and the widths of all the rectangles approach zero yields the definite integrals
$$\int_a^b (x - \bar{x})\delta f(x) dx \quad\text{and}\quad \int_a^b \left(\frac{f(x)}{2} - \bar{y}\right)\delta f(x) dx$$
that represent the moments of the lamina about the lines $x = \bar{x}$ and $y = \bar{y}$. Since the lamina balances on those lines, the moments of the lamina about those lines should be zero:
$$\int_a^b (x - \bar{x})\delta f(x) dx = \int_a^b \left(\frac{f(x)}{2} - \bar{y}\right)\delta f(x) dx = 0$$

Since $\bar{x}$ and $\bar{y}$ are constant, these equations can be rewritten as
$$\int_a^b \delta x f(x) dx = \bar{x}\int_a^b \delta f(x) dx$$
$$\int_a^b \frac{1}{2}\delta [f(x)]^2 dx = \bar{y}\int_a^b \delta f(x) dx$$
from which we obtain the following formulas for the center of gravity of the lamina:

> **CENTER OF GRAVITY $(\bar{x}, \bar{y})$ OF A LAMINA**
> $$\bar{x} = \frac{\int_a^b \delta x f(x) dx}{\int_a^b \delta f(x) dx}, \quad \bar{y} = \frac{\int_a^b \frac{1}{2}\delta [f(x)]^2 dx}{\int_a^b \delta f(x) dx} \tag{4–5}$$

Observe that in both formulas the denominator is the mass $M$ of the lamina. The numerator in the formula for $\bar{x}$ is denoted by $M_y$ and is called the **first moment of the lamina about the $y$-axis**; the numerator of the formula for $\bar{y}$ is denoted by $M_x$ and is called the **first moment of the lamina about the $x$-axis**. Thus, we can write (4) and (5) as:

> **ALTERNATIVE FORMULAS FOR CENTER OF GRAVITY $(\bar{x}, \bar{y})$ OF A LAMINA**
> $$\bar{x} = \frac{M_y}{M} = \frac{1}{\text{mass of } R}\int_a^b \delta x f(x) dx \tag{6}$$
> $$\bar{y} = \frac{M_x}{M} = \frac{1}{\text{mass of } R}\int_a^b \frac{1}{2}\delta [f(x)]^2 dx \tag{7}$$

#### Example 2
Find the center of gravity of the triangular lamina with vertices $(0, 0), (0, 1),$ and $(1, 0)$ and density $\delta = 3$.

**Solution.** The lamina is shown in Figure 5.7.2. In Example 1 we found the mass of the lamina to be $M = 3/2$. The moment of the lamina about the $y$-axis is
$$M_y = \int_0^1 \delta x f(x) dx = \int_0^1 3x(-x + 1) dx = \int_0^1 (-3x^2 + 3x) dx = \left[-x^3 + \frac{3}{2}x^2\right]_0^1 = -1 + \frac{3}{2} = \frac{1}{2}$$
and the moment about the $x$-axis is
$$M_x = \int_0^1 \frac{1}{2}\delta [f(x)]^2 dx = \int_0^1 \frac{3}{2}(-x + 1)^2 dx = \int_0^1 \frac{3}{2}(x^2 - 2x + 1) dx = \frac{3}{2}\left[\frac{1}{3}x^3 - x^2 + x\right]_0^1 = \frac{3}{2}\left(\frac{1}{3}\right) = \frac{1}{2}$$
From (6) and (7),
$$\bar{x} = \frac{M_y}{M} = \frac{1/2}{3/2} = \frac{1}{3}, \quad \bar{y} = \frac{M_x}{M} = \frac{1/2}{3/2} = \frac{1}{3}$$
so the center of gravity is $(1/3, 1/3)$.

---

### CENTROID OF A REGION $R$
In the case of a homogeneous lamina, the center of gravity of a lamina occupying the region $R$ is called the **centroid** of the region $R$. Since the lamina is homogeneous, $\delta$ is constant. The factor $\delta$ in (4) and (5) may thus be moved through the integral signs and canceled, and (4) and (5) can be expressed as:

> **CENTROID OF A REGION $R$**
> $$\bar{x} = \frac{\int_a^b x f(x) dx}{\int_a^b f(x) dx} = \frac{1}{\text{area of } R}\int_a^b x f(x) dx \tag{8}$$
> $$\bar{y} = \frac{\int_a^b \frac{1}{2}[f(x)]^2 dx}{\int_a^b f(x) dx} = \frac{1}{\text{area of } R}\int_a^b \frac{1}{2}[f(x)]^2 dx \tag{9}$$

*Since the density factor has canceled, we may interpret the centroid as a geometric property of the region, and distinguish it from the center of gravity, which is a physical property of an idealized object that occupies the region.*

#### Example 3
Find the centroid of the semicircular region in Figure 5.7.8.

**Solution.** By symmetry, $\bar{x} = 0$ since the $y$-axis is obviously a line of balance. To find $\bar{y}$, first note that the equation of the semicircle is $y = f(x) = \sqrt{a^2 - x^2}$. From (9),
$$\bar{y} = \frac{1}{\text{area of } R}\int_{-a}^a \frac{1}{2}[f(x)]^2 dx = \frac{1}{\frac{1}{2}\pi a^2}\int_{-a}^a \frac{1}{2}(a^2 - x^2) dx = \frac{1}{\pi a^2}\left[a^2 x - \frac{1}{3}x^3\right]_{-a}^a$$
$$= \frac{1}{\pi a^2}\left[\left(a^3 - \frac{1}{3}a^3\right) - \left(-a^3 + \frac{1}{3}a^3\right)\right] = \frac{1}{\pi a^2}\left(\frac{4a^3}{3}\right) = \frac{4a}{3\pi}$$
so the centroid is $(0, 4a/3\pi)$.

---

### OTHER TYPES OF REGIONS
The strategy used to find the center of gravity of the region in Problem 5.7.1 can be used to find the center of gravity of regions that are not of that form.

Consider a homogeneous lamina that occupies the region $R$ between two continuous functions $f(x)$ and $g(x)$ over the interval $[a, b]$, where $f(x) \ge g(x)$ for $a \le x \le b$. To find the center of gravity of this lamina we can subdivide it into $n$ strips using lines parallel to the $y$-axis. If $x_k^*$ is the midpoint of the $k$th strip, the strip can be approximated by a rectangle of width $\Delta x_k$ and height $f(x_k^*) - g(x_k^*)$. We assume that the entire mass of the $k$th rectangle is concentrated at its center $(x_k^*, y_k^*) = (x_k^*, \frac{1}{2}(f(x_k^*) + g(x_k^*)))$ (Figure 5.7.9). Continuing the argument as in the solution of Problem 5.7.1, we find that the center of gravity of the lamina is
$$\bar{x} = \frac{\int_a^b x(f(x) - g(x)) dx}{\int_a^b (f(x) - g(x)) dx} = \frac{1}{\text{area of } R}\int_a^b x(f(x) - g(x)) dx \tag{10}$$
$$\bar{y} = \frac{\int_a^b \frac{1}{2}([f(x)]^2 - [g(x)]^2) dx}{\int_a^b (f(x) - g(x)) dx} = \frac{1}{\text{area of } R}\int_a^b \frac{1}{2}([f(x)]^2 - [g(x)]^2) dx \tag{11}$$

Note that the density of the lamina does not appear in Equations (10) and (11). This reflects the fact that the centroid is a geometric property of $R$.

#### Example 4
Find the centroid of the region $R$ enclosed between the curves $y = x^2$ and $y = x + 6$.

**Solution.** To begin, we note that the two curves intersect when $x = -2$ and $x = 3$ and that $x + 6 \ge x^2$ over that interval (Figure 5.7.10). The area of $R$ is
$$\int_{-2}^3 [(x + 6) - x^2] dx = \frac{125}{6}$$
From (10) and (11),
$$\bar{x} = \frac{1}{\text{area of } R}\int_{-2}^3 x[(x + 6) - x^2] dx = \frac{6}{125}\left[\frac{1}{3}x^3 + 3x^2 - \frac{1}{4}x^4\right]_{-2}^3 = \frac{6}{125}\cdot\frac{125}{12} = \frac{1}{2}$$
and
$$\bar{y} = \frac{1}{\text{area of } R}\int_{-2}^3 \frac{1}{2}((x + 6)^2 - (x^2)^2) dx = \frac{6}{125}\int_{-2}^3 \frac{1}{2}(x^2 + 12x + 36 - x^4) dx$$
$$= \frac{6}{125}\cdot\frac{1}{2}\left[\frac{1}{3}x^3 + 6x^2 + 36x - \frac{1}{5}x^5\right]_{-2}^3 = \frac{6}{125}\cdot\frac{250}{3} = 4$$
so the centroid of $R$ is $(1/2, 4)$.

Suppose that $w$ is a continuous function of $y$ on an interval $[c, d]$ with $w(y) \ge 0$ for $c \le y \le d$. Consider a lamina that occupies a region $R$ bounded above by $y = d$, below by $y = c$, on the left by the $y$-axis, and on the right by $x = w(y)$ (Figure 5.7.11). To find the center of gravity of this lamina, we note that the roles of $x$ and $y$ in Problem 5.7.1 have been reversed. We now imagine the lamina to be subdivided into $n$ strips using lines parallel to the $x$-axis. We let $y_k^*$ be the midpoint of the $k$th subinterval and approximate the strip by a rectangle of width $\Delta y_k$ and height $w(y_k^*)$. We assume that the entire mass of the $k$th rectangle is concentrated at its center $(x_k^*, y_k^*) = (\frac{1}{2}w(y_k^*), y_k^*)$ (Figure 5.7.11). Continuing the argument as in the solution of Problem 5.7.1, we find that the center of gravity of the lamina is
$$\bar{x} = \frac{\int_c^d \frac{1}{2}(w(y))^2 dy}{\int_c^d w(y) dy} = \frac{1}{\text{area of } R}\int_c^d \frac{1}{2}(w(y))^2 dy \tag{12}$$
$$\bar{y} = \frac{\int_c^d y w(y) dy}{\int_c^d w(y) dy} = \frac{1}{\text{area of } R}\int_c^d y w(y) dy \tag{13}$$

#### Example 5
Find the centroid of the region $R$ enclosed between the curves $y = \sqrt{x}, y = 1, y = 2,$ and the $y$-axis (Figure 5.7.12).

**Solution.** Note that $x = w(y) = y^2$ and that the area of $R$ is
$$\int_1^2 y^2 dy = \frac{7}{3}$$
From (12) and (13),
$$\bar{x} = \frac{1}{\text{area of } R}\int_1^2 \frac{1}{2}(y^2)^2 dy = \frac{3}{7}\cdot\left[\frac{1}{10}y^5\right]_1^2 = \frac{3}{7}\cdot\frac{31}{10} = \frac{93}{70}$$
$$\bar{y} = \frac{1}{\text{area of } R}\int_1^2 y(y^2) dy = \frac{3}{7}\cdot\left[\frac{1}{4}y^4\right]_1^2 = \frac{3}{7}\cdot\frac{15}{4} = \frac{45}{28}$$
so the centroid of $R$ is $(93/70, 45/28) \approx (1.329, 1.607)$.

---

### THEOREM OF PAPPUS
The following theorem, due to the Greek mathematician Pappus, gives an important relationship between the centroid of a plane region $R$ and the volume of the solid generated when the region is revolved about a line.

> **5.7.2 THEOREM (Theorem of Pappus)**  
> If $R$ is a bounded plane region and $L$ is a line that lies in the plane of $R$ such that $R$ is entirely on one side of $L$, then the volume of the solid formed by revolving $R$ about $L$ is given by
> $$\text{volume} = (\text{area of } R) \cdot (\text{distance traveled by the centroid})$$

**PROOF.** We prove this theorem in the special case where $L$ is the $y$-axis, the region $R$ is in the first quadrant, and the region $R$ is of the form given in Problem 5.7.1. (A more general proof will be outlined in the Exercises of Section 14.8.) In this case, the volume $V$ of the solid formed by revolving $R$ about $L$ can be found by the method of cylindrical shells (Section 5.3) to be
$$V = 2\pi \int_a^b x f(x) dx$$
Thus, it follows from (8) that
$$V = 2\pi \bar{x}[\text{area of } R]$$
This completes the proof since $2\pi \bar{x}$ is the distance traveled by the centroid when $R$ is revolved about the $y$-axis. $\blacksquare$

#### Example 6
Use Pappus’ Theorem to find the volume $V$ of the torus generated by revolving a circular region of radius $b$ about a line at a distance $a$ (greater than $b$) from the center of the circle (Figure 5.7.13).

**Solution.** By symmetry, the centroid of a circular region is its center. Thus, the distance traveled by the centroid is $2\pi a$. Since the area of a circle of radius $b$ is $\pi b^2$, it follows from Pappus’ Theorem that the volume of the torus is
$$V = (2\pi a)(\pi b^2) = 2\pi^2 a b^2$$

> **Pappus of Alexandria (4th century A.D.)**  
> Greek mathematician. Pappus lived during the early Christian era when mathematical activity was in a period of decline. His main contributions to mathematics appeared in a series of eight books called *The Collection* (written about 340 A.D.). This work, which survives only partially, contained some original results but was devoted mostly to statements, refinements, and proofs of results by earlier mathematicians. Pappus’ Theorem, stated without proof in Book VII of *The Collection*, was probably known and proved in earlier times. This result is sometimes called *Guldin’s Theorem* in recognition of the Swiss mathematician, Paul Guldin (1577–1643), who rediscovered it independently.

---

### QUICK CHECK EXERCISES 5.7
*(See page 400 for answers.)*

1. The total mass of a homogeneous lamina of area $A$ and density $\delta$ is $\underline{\hspace{1.5cm}}$.
2. A homogeneous lamina of mass $M$ and density $\delta$ occupies a region in the $xy$-plane bounded by the graphs of $y = f(x), y = 0, x = a,$ and $x = b$, where $f$ is a nonnegative continuous function defined on an interval $[a, b]$. The $x$-coordinate of the center of gravity of the lamina is $M_y/M$, where $M_y$ is called the $\underline{\hspace{1.5cm}}$ and is given by the integral $\underline{\hspace{1.5cm}}$.
3. Let $R$ be the region between the graphs of $y = x^2$ and $y = 2 - x$ for $0 \le x \le 1$. The area of $R$ is $7/6$ and the centroid of $R$ is $\underline{\hspace{1.5cm}}$.
4. If the region $R$ in Quick Check Exercise 3 is used to generate a solid $G$ by rotating $R$ about a horizontal line 6 units above its centroid, then the volume of $G$ is $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 5.7
1. $\delta A$  
2. first moment about the $y$-axis; $\int_a^b \delta x f(x) dx$  
3. $(5/14, 32/35)$  
4. $14\pi$

---

### EXERCISE SET 5.7

#### FOCUS ON CONCEPTS
1. Masses $m_1 = 5, m_2 = 10,$ and $m_3 = 20$ are positioned on a weightless beam as shown in the accompanying figure (at positions $x = 0, 5, 10$).  
   (a) Suppose that the fulcrum is positioned at $x = 5$. Without computing the sum of moments about 5, determine whether the sum is positive, zero, or negative. Explain.  
   (b) Where should the fulcrum be placed so that the beam is in equilibrium?
2. Masses $m_1 = 10, m_2 = 3, m_3 = 4,$ and $m$ are positioned on a weightless beam, with the fulcrum positioned at point 4, as shown in the accompanying figure (at positions $x = 0, 2, 3, 6$).  
   (a) Suppose that $m = 14$. Without computing the sum of the moments about 4, determine whether the sum is positive, zero, or negative. Explain.  
   (b) For what value of $m$ is the beam in equilibrium?

**3–6 Find the centroid of the region by inspection and confirm your answer by integrating.**
3. Square with vertices $(0, 0), (1, 0), (1, 1), (0, 1)$.
4. Diamond with vertices $(1, 0), (0, 1), (-1, 0), (0, -1)$.
5. Rectangle with vertices $(0, 0), (2, 0), (2, 1), (0, 1)$.
6. Disk $x^2 + y^2 \le 1$.

**7–18 Find the centroid of the region.**
7. Region bounded by $y = x, y = 0, x = 1$.
8. Region bounded by $y = x^2, y = 0, x = 1$.
9. Region bounded by $y = 2 - x^2, y = x$.
10. Region bounded by $y = \sqrt{1 - x^2}, y = 0, x = 0$ (first quadrant quarter-circle).
11. The triangle with vertices $(0, 0), (2, 0),$ and $(0, 1)$.
12. The triangle with vertices $(0, 0), (1, 1),$ and $(2, 0)$.
13. The region bounded by the graphs of $y = x^2$ and $x + y = 6$.
14. The region bounded on the left by the $y$-axis, on the right by the line $x = 2$, below by the parabola $y = x^2$, and above by the line $y = x + 6$.
15. The region bounded by the graphs of $y = x^2$ and $y = x + 2$.
16. The region bounded by the graphs of $y = x^2$ and $y = 1$.
17. The region bounded by the graphs of $y = \sqrt{x}$ and $y = x^2$.
18. The region bounded by the graphs of $y = \sqrt{x}$ and $y = x^3$.

#### FOCUS ON CONCEPTS
19. Use symmetry considerations to argue that the centroid of an isosceles triangle lies on the median to the base of the triangle.
20. Use symmetry considerations to argue that the centroid of an ellipse lies at the intersection of the major and minor axes of the ellipse.

**21–24 Find the mass and center of gravity of the lamina with density $\delta$.**
21. A lamina bounded by the $x$-axis, the line $x = 1$, and the curve $y = \sqrt{x}; \delta = 2$.
22. A lamina bounded by the graph of $x = y^4$ and the line $x = 1; \delta = 15$.
23. A lamina bounded by the graph of $y = |x|$ and the line $y = 1; \delta = 3$.
24. A lamina bounded by the $x$-axis and the graph of the equation $y = 1 - x^2; \delta = 3$.

**25–26 [CAS] Use a CAS to find the mass and center of gravity of the lamina with density $\delta$.**
25. A lamina bounded by $y = \sin x, y = 0, x = 0,$ and $x = \pi; \delta = 4$.
26. A lamina bounded by the graphs of $y = \cos x, y = \sin x, x = 0,$ and $x = \pi/4; \delta = 1 + \sqrt{2}$.

**27–30 True–False Determine whether the statement is true or false. Explain your answer. [In Exercise 30, assume that the (rotated) square lies in the $xy$-plane to the right of the $y$-axis.]**
27. The centroid of a rectangle is the intersection of the diagonals of the rectangle.
28. The centroid of a rhombus is the intersection of the diagonals of the rhombus.
29. The centroid of an equilateral triangle is the intersection of the medians of the triangle.
30. By rotating a square about its center, it is possible to change the volume of the solid of revolution generated by revolving the square about the $y$-axis.

31. Find the centroid of the triangle with vertices $(0, 0), (a, b),$ and $(a, -b)$.
32. Prove that the centroid of a triangle is the point of intersection of the three medians of the triangle. [*Hint:* Choose coordinates so that the vertices of the triangle are located at $(0, -a), (0, a),$ and $(b, c)$.]
33. Find the centroid of the isosceles trapezoid with vertices $(-a, 0), (a, 0), (-b, c),$ and $(b, c)$.
34. Prove that the centroid of a parallelogram is the point of intersection of the diagonals of the parallelogram. [*Hint:* Choose coordinates so that the vertices of the parallelogram are located at $(0, 0), (0, a), (b, c),$ and $(b, a + c)$.]
35. Use the Theorem of Pappus and the fact that the volume of a sphere of radius $a$ is $V = \frac{4}{3}\pi a^3$ to show that the centroid of the lamina that is bounded by the $x$-axis and the semicircle $y = \sqrt{a^2 - x^2}$ is $(0, 4a/(3\pi))$. (This problem was solved directly in Example 3.)
36. Use the Theorem of Pappus and the result of Exercise 35 to find the volume of the solid generated when the region bounded by the $x$-axis and the semicircle $y = \sqrt{a^2 - x^2}$ is revolved about  
    (a) the line $y = -a$  
    (b) the line $y = x - a$.
37. Use the Theorem of Pappus and the fact that the area of an ellipse with semiaxes $a$ and $b$ is $\pi ab$ to find the volume of the elliptical torus generated by revolving the ellipse
    $$\frac{(x - k)^2}{a^2} + \frac{y^2}{b^2} = 1$$
    about the $y$-axis. Assume that $k > a$.
38. Use the Theorem of Pappus to find the volume of the solid that is generated when the region enclosed by $y = x^2$ and $y = 8 - x^2$ is revolved about the $x$-axis.
39. Use the Theorem of Pappus to find the centroid of the triangular region with vertices $(0, 0), (a, 0),$ and $(0, b)$, where $a > 0$ and $b > 0$. [*Hint:* Revolve the region about the $x$-axis to obtain $\bar{y}$ and about the $y$-axis to obtain $\bar{x}$.]
40. **Writing.** Suppose that a region $R$ in the plane is decomposed into two regions $R_1$ and $R_2$ whose areas are $A_1$ and $A_2$, respectively, and whose centroids are $(\bar{x}_1, \bar{y}_1)$ and $(\bar{x}_2, \bar{y}_2)$, respectively. Investigate the problem of expressing the centroid of $R$ in terms of $A_1, A_2, (\bar{x}_1, \bar{y}_1),$ and $(\bar{x}_2, \bar{y}_2)$. Write a short report on your investigations, supporting your reasoning with plausible arguments. Can you extend your results to decompositions of $R$ into more than two regions?
41. **Writing.** How might you recognize that a problem can be solved by means of the Theorem of Pappus? That is, what sort of “givens” and “unknowns” would suggest such a solution? Discuss two or three examples.

---

## 5.8 FLUID PRESSURE AND FORCE

In this section we will use the integration tools developed in the preceding chapter to study the pressures and forces exerted by fluids on submerged objects.

### WHAT IS A FLUID?
A **fluid** is a substance that flows to conform to the boundaries of any container in which it is placed. Fluids include liquids, such as water, oil, and mercury, as well as gases, such as helium, oxygen, and air. The study of fluids falls into two categories: **fluid statics** (the study of fluids at rest) and **fluid dynamics** (the study of fluids in motion). In this section we will be concerned only with fluid statics; toward the end of this text we will investigate problems in fluid dynamics.

### THE CONCEPT OF PRESSURE
The effect that a force has on an object depends on how that force is spread over the surface of the object. For example, when you walk on soft snow with boots, the weight of your body crushes the snow and you sink into it. However, if you put on a pair of snowshoes to spread the weight of your body over a greater surface area, then the weight of your body has less of a crushing effect on the snow. The concept that accounts for both the magnitude of a force and the area over which it is applied is called **pressure**.

> **5.8.1 DEFINITION**  
> If a force of magnitude $F$ is applied to a surface of area $A$, then we define the **pressure** $P$ exerted by the force on the surface to be
> $$P = \frac{F}{A} \tag{1}$$

It follows from this definition that pressure has units of force per unit area. The most common units of pressure are newtons per square meter ($\text{N/m}^2$) in SI and pounds per square inch ($\text{lb/in}^2$) or pounds per square foot ($\text{lb/ft}^2$) in the BE system. As indicated in Table 5.8.1, one newton per square meter is called a **pascal** (Pa). A pressure of $1\text{ Pa}$ is quite small ($1\text{ Pa} \approx 1.45 \times 10^{-4}\text{ lb/in}^2$), so in countries using SI, tire pressure gauges are usually calibrated in kilopascals (kPa), which is 1000 pascals.

#### Table 5.8.1: Units of Force and Pressure
| SYSTEM | FORCE $\div$ | AREA $=$ | PRESSURE |
| :--- | :--- | :--- | :--- |
| SI | newton (N) | square meter ($\text{m}^2$) | pascal (Pa) |
| BE | pound (lb) | square foot ($\text{ft}^2$) | $\text{lb/ft}^2$ |
| BE | pound (lb) | square inch ($\text{in}^2$) | $\text{lb/in}^2$ (psi) |

**Conversion Factors:**
* $1\text{ Pa} \approx 1.45 \times 10^{-4}\text{ lb/in}^2 \approx 2.09 \times 10^{-2}\text{ lb/ft}^2$
* $1\text{ lb/in}^2 \approx 6.89 \times 10^3\text{ Pa}$
* $1\text{ lb/ft}^2 \approx 47.9\text{ Pa}$

In this section we will be interested in pressures and forces on objects submerged in fluids. Pressures themselves have no directional characteristics, but the forces that they create always act perpendicular to the face of the submerged object. Thus, in Figure 5.8.1 the water pressure creates horizontal forces on the sides of the tank, vertical forces on the bottom of the tank, and forces that vary in direction, so as to be perpendicular to the different parts of the swimmer’s body.

> **Blaise Pascal (1623–1662)**  
> French mathematician and scientist. Pascal’s mother died when he was three years old and his father, a highly educated magistrate, personally provided the boy’s early education. Although Pascal showed an inclination for science and mathematics, his father refused to tutor him in those subjects until he mastered Latin and Greek. Pascal’s sister and primary biographer claimed that he independently discovered the first thirty-two propositions of Euclid without ever reading a book on geometry. (However, it is generally agreed that the story is apocryphal.) Nevertheless, the precocious Pascal published a highly respected essay on conic sections by the time he was sixteen years old. Descartes, who read the essay, thought it so brilliant that he could not believe that it was written by such a young man. By age 18 his health began to fail and until his death he was in frequent pain. However, his creativity was unimpaired.  
> Pascal’s contributions to physics include the discovery that air pressure decreases with altitude and the principle of fluid pressure that bears his name. However, the originality of his work is questioned by some historians. Pascal made major contributions to a branch of mathematics called “projective geometry,” and he helped to develop probability theory through a series of letters with Fermat.  
> In 1646, Pascal’s health problems resulted in a deep emotional crisis that led him to become increasingly concerned with religious matters. Although born a Catholic, he converted to a religious doctrine called Jansenism and spent most of his final years writing on religion and philosophy.

#### Example 1
Referring to Figure 5.8.1, suppose that the back of the swimmer’s hand has a surface area of $8.4 \times 10^{-3}\text{ m}^2$ and that the pressure acting on it is $5.1 \times 10^4\text{ Pa}$ (a realistic value near the bottom of a deep diving pool). Find the force that acts on the swimmer’s hand.

**Solution.** From (1), the force $F$ is
$$F = PA = (5.1 \times 10^4\text{ N/m}^2)(8.4 \times 10^{-3}\text{ m}^2) \approx 4.3 \times 10^2\text{ N}$$
This is quite a large force (nearly $100\text{ lb}$ in the BE system).

---

### FLUID DENSITY
Scuba divers know that the pressure and forces on their bodies increase with the depth they dive. This is caused by the weight of the water and air above—the deeper the diver goes, the greater the weight above and so the greater the pressure and force exerted on the diver.

To calculate pressures and forces on submerged objects, we need to know something about the characteristics of the fluids in which they are submerged. For simplicity, we will assume that the fluids under consideration are homogeneous, by which we mean that any two samples of the fluid with the same volume have the same mass. It follows from this assumption that the mass per unit volume is a constant $\delta$ that depends on the physical characteristics of the fluid but not on the size or location of the sample; we call
$$\delta = \frac{m}{V} \tag{2}$$
the **mass density** of the fluid. Sometimes it is more convenient to work with weight per unit volume than with mass per unit volume. Thus, we define the **weight density** $\rho$ of a fluid to be
$$\rho = \frac{w}{V} \tag{3}$$
where $w$ is the weight of a fluid sample of volume $V$. Thus, if the weight density of a fluid is known, then the weight $w$ of a fluid sample of volume $V$ can be computed from the formula $w = \rho V$. Table 5.8.2 shows some typical weight densities.

#### Table 5.8.2: Weight Densities
| SI | $\text{N/m}^3$ | BE SYSTEM | $\text{lb/ft}^3$ |
| :--- | :--- | :--- | :--- |
| Machine oil | 4708 | Machine oil | 30.0 |
| Gasoline | 6602 | Gasoline | 42.0 |
| Fresh water | 9810 | Fresh water | 62.4 |
| Seawater | 10,045 | Seawater | 64.0 |
| Mercury | 133,416 | Mercury | 849.0 |

*All densities are affected by variations in temperature and pressure. Weight densities are also affected by variations in $g$.*

---

### FLUID PRESSURE
To calculate fluid pressures and forces we will need to make use of an experimental observation. Suppose that a flat surface of area $A$ is submerged in a homogeneous fluid of weight density $\rho$ such that the entire surface lies between depths $h_1$ and $h_2$, where $h_1 \le h_2$ (Figure 5.8.2). Experiments show that on both sides of the surface, the fluid exerts a force that is perpendicular to the surface and whose magnitude $F$ satisfies the inequalities
$$\rho h_1 A \le F \le \rho h_2 A \tag{4}$$
Thus, it follows from (1) that the pressure $P = F/A$ on a given side of the surface satisfies the inequalities
$$\rho h_1 \le P \le \rho h_2 \tag{5}$$

Note that it is now a straightforward matter to calculate fluid force and pressure on a flat surface that is submerged horizontally at depth $h$, for then $h = h_1 = h_2$ and inequalities (4) and (5) become the equalities
$$F = \rho h A \tag{6}$$
and
$$P = \rho h \tag{7}$$

#### Example 2
Find the fluid pressure and force on the top of a flat circular plate of radius $2\text{ m}$ that is submerged horizontally in water at a depth of $6\text{ m}$ (Figure 5.8.3).

**Solution.** Since the weight density of water is $\rho = 9810\text{ N/m}^3$, it follows from (7) that the fluid pressure is
$$P = \rho h = (9810)(6) = 58,860\text{ Pa}$$
and it follows from (6) that the fluid force is
$$F = \rho h A = \rho h(\pi r^2) = (9810)(6)(4\pi) = 235,440\pi \approx 739,700\text{ N}$$

---

### FLUID FORCE ON A VERTICAL SURFACE
It was easy to calculate the fluid force on the horizontal plate in Example 2 because each point on the plate was at the same depth. The problem of finding the fluid force on a vertical surface is more complicated because the depth, and hence the pressure, is not constant over the surface. To find the fluid force on a vertical surface we will need calculus.

> **5.8.2 PROBLEM**  
> Suppose that a flat surface is immersed vertically in a fluid of weight density $\rho$ and that the submerged portion of the surface extends from $x = a$ to $x = b$ along an $x$-axis whose positive direction is down (Figure 5.8.4a). For $a \le x \le b$, suppose that $w(x)$ is the width of the surface and that $h(x)$ is the depth of the point $x$. Define what is meant by the fluid force $F$ on the surface, and find a formula for computing it.

The basic idea for solving this problem is to divide the surface into horizontal strips whose areas may be approximated by areas of rectangles. These area approximations, along with inequalities (4), will allow us to create a Riemann sum that approximates the total force on the surface. By taking a limit of Riemann sums we will then obtain an integral for $F$.

To implement this idea, we divide the interval $[a, b]$ into $n$ subintervals by inserting the points $x_1, x_2, \dots, x_{n-1}$ between $a = x_0$ and $b = x_n$. This has the effect of dividing the surface into $n$ strips of area $A_k, k = 1, 2, \dots, n$ (Figure 5.8.4b). It follows from (4) that the force $F_k$ on the $k$th strip satisfies the inequalities
$$\rho h(x_{k-1})A_k \le F_k \le \rho h(x_k)A_k \quad\text{or, equivalently,}\quad h(x_{k-1}) \le \frac{F_k}{\rho A_k} \le h(x_k)$$
Since the depth function $h(x)$ increases linearly, there must exist a point $x_k^*$ between $x_{k-1}$ and $x_k$ such that
$$h(x_k^*) = \frac{F_k}{\rho A_k} \quad\text{or, equivalently,}\quad F_k = \rho h(x_k^*)A_k$$

We now approximate the area $A_k$ of the $k$th strip of the surface by the area of a rectangle of width $w(x_k^*)$ and height $\Delta x_k = x_k - x_{k-1}$ (Figure 5.8.4c). It follows that $F_k$ may be approximated as
$$F_k = \rho h(x_k^*)A_k \approx \rho h(x_k^*) \cdot w(x_k^*) \Delta x_k$$

Adding these approximations yields the following Riemann sum that approximates the total force $F$ on the surface:
$$F = \sum_{k=1}^n F_k \approx \sum_{k=1}^n \rho h(x_k^*) w(x_k^*) \Delta x_k$$

Taking the limit as $n$ increases and the widths of all the subintervals approach zero yields the definite integral
$$F = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n \rho h(x_k^*) w(x_k^*) \Delta x_k = \int_a^b \rho h(x) w(x) dx$$

In summary, we have the following result.

> **5.8.3 DEFINITION**  
> Suppose that a flat surface is immersed vertically in a fluid of weight density $\rho$ and that the submerged portion of the surface extends from $x = a$ to $x = b$ along an $x$-axis whose positive direction is down (Figure 5.8.4a). For $a \le x \le b$, suppose that $w(x)$ is the width of the surface and that $h(x)$ is the depth of the point $x$. Then we define the **fluid force** $F$ on the surface to be
> $$F = \int_a^b \rho h(x) w(x) dx \tag{8}$$

#### Example 3
The face of a dam is a vertical rectangle of height $100\text{ ft}$ and width $200\text{ ft}$ (Figure 5.8.5a). Find the total fluid force exerted on the face when the water surface is level with the top of the dam.

**Solution.** Introduce an $x$-axis with its origin at the water surface as shown in Figure 5.8.5b. At a point $x$ on this axis, the width of the dam in feet is $w(x) = 200$ and the depth in feet is $h(x) = x$. Thus, from (8) with $\rho = 62.4\text{ lb/ft}^3$ (the weight density of water) we obtain as the total force on the face
$$F = \int_0^{100} (62.4)(x)(200) dx = 12,480\int_0^{100} x dx = 12,480\left[\frac{x^2}{2}\right]_0^{100} = 62,400,000\text{ lb}$$

#### Example 4
A plate in the form of an isosceles triangle with base $10\text{ ft}$ and altitude $4\text{ ft}$ is submerged vertically in machine oil as shown in Figure 5.8.6a. Find the fluid force $F$ against the plate surface if the oil has weight density $\rho = 30\text{ lb/ft}^3$.

**Solution.** Introduce an $x$-axis as shown in Figure 5.8.6b. By similar triangles, the width of the plate, in feet, at a depth of $h(x) = (3 + x)\text{ ft}$ satisfies
$$\frac{w(x)}{10} = \frac{x}{4}, \quad\text{so } w(x) = \frac{5}{2}x$$
Thus, it follows from (8) that the force on the plate is
$$F = \int_a^b \rho h(x) w(x) dx = \int_0^4 (30)(3 + x)\left(\frac{5}{2}x\right) dx = 75\int_0^4 (3x + x^2) dx = 75\left[\frac{3x^2}{2} + \frac{x^3}{3}\right]_0^4 = 3400\text{ lb}$$

---

### QUICK CHECK EXERCISES 5.8
*(See page 406 for answers.)*

1. The pressure unit equivalent to a newton per square meter ($\text{N/m}^2$) is called a $\underline{\hspace{1.5cm}}$. The pressure unit psi stands for $\underline{\hspace{1.5cm}}$.
2. Given that the weight density of water is $9810\text{ N/m}^3$, the fluid pressure on a rectangular $2\text{ m} \times 3\text{ m}$ flat plate submerged horizontally in water at a depth of $10\text{ m}$ is $\underline{\hspace{1.5cm}}$. The fluid force on the plate is $\underline{\hspace{1.5cm}}$.
3. Suppose that a flat surface is immersed vertically in a fluid of weight density $\rho$ and that the submerged portion of the surface extends from $x = a$ to $x = b$ along an $x$-axis whose positive direction is down. If, for $a \le x \le b$, the surface has width $w(x)$ and depth $h(x)$, then the fluid force on the surface is $F = \underline{\hspace{1.5cm}}$.
4. A rectangular plate $2\text{ m}$ wide and $3\text{ m}$ high is submerged vertically in water so that the top of the plate is $5\text{ m}$ below the water surface. An integral expression for the force of the water on the plate surface is $F = \underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 5.8
1. pascal; pounds per square inch  
2. $98,100\text{ Pa}; \ 588,600\text{ N}$  
3. $\int_a^b \rho h(x) w(x) dx$  
4. $\int_0^3 9810[(5 + x)2] dx$

---

### EXERCISE SET 5.8
*In this exercise set, refer to Table 5.8.2 for weight densities of fluids, where needed.*

1. A flat rectangular plate is submerged horizontally in water.  
   (a) Find the force (in lb) and the pressure (in $\text{lb/ft}^2$) on the top surface of the plate if its area is $100\text{ ft}^2$ and the surface is at a depth of $5\text{ ft}$.  
   (b) Find the force (in N) and the pressure (in Pa) on the top surface of the plate if its area is $25\text{ m}^2$ and the surface is at a depth of $10\text{ m}$.
2. (a) Find the force (in N) on the deck of a sunken ship if its area is $160\text{ m}^2$ and the pressure acting on it is $6.0 \times 10^5\text{ Pa}$.  
   (b) Find the force (in lb) on a diver’s face mask if its area is $60\text{ in}^2$ and the pressure acting on it is $100\text{ lb/in}^2$.

**3–8 The flat surfaces shown are submerged vertically in water. Find the fluid force against each surface.**
3. Vertical rectangle of width $4\text{ ft}$ and height $2\text{ ft}$, top edge at surface.
4. Vertical rectangle of width $4\text{ m}$ and height $2\text{ m}$, top edge $1\text{ m}$ below surface.
5. Semicircular plate with diameter $10\text{ m}$ along the water surface.
6. Inverted isosceles triangle with base $4\text{ ft}$ along water surface and altitude $4\text{ ft}$.
7. Trapezoidal plate with top width $6\text{ m}$, bottom width $8\text{ m}$, height $10\text{ m}$, submerged $2\text{ m}$ below surface.
8. Trapezoidal dam face top width $16\text{ ft}$, bottom width $8\text{ ft}$, height $4\text{ ft}$, top edge $4\text{ ft}$ below surface.

9. Suppose that a flat surface is immersed vertically in a fluid of weight density $\rho$. If $\rho$ is doubled, is the force on the plate also doubled? Explain your reasoning.
10. An oil tank is shaped like a right circular cylinder of diameter $4\text{ ft}$. Find the total fluid force against one end when the axis is horizontal and the tank is half filled with oil of weight density $50\text{ lb/ft}^3$.
11. A square plate of side $a$ feet is dipped in a liquid of weight density $\rho\text{ lb/ft}^3$. Find the fluid force on the plate if a vertex is at the surface and a diagonal is perpendicular to the surface.

**12–15 True–False Determine whether the statement is true or false. Explain your answer.**
12. In the International System of Units, pressure and force have the same units.
13. In a cylindrical water tank (with vertical axis), the fluid force on the base of the tank is equal to the weight of water in the tank.
14. In a rectangular water tank, the fluid force on any side of the tank must be less than the fluid force on the base of the tank.
15. In any water tank with a flat base, no matter what the shape of the tank, the fluid force on the base is at most equal to the weight of water in the tank.

**16–19 Formula (8) gives the fluid force on a flat surface immersed vertically in a fluid. More generally, if a flat surface is immersed so that it makes an angle of $0 \le \theta < \pi/2$ with the vertical, then the fluid force on the surface is given by**
$$F = \int_a^b \rho h(x) w(x) \sec\theta dx$$
**Use this formula in these exercises.**
16. Derive the formula given above for the fluid force on a flat surface immersed at an angle in a fluid.
17. The accompanying figure shows a rectangular swimming pool whose bottom is an inclined plane (width $10\text{ ft}$, length $16\text{ ft}$, shallow end depth $4\text{ ft}$, deep end depth $8\text{ ft}$). Find the fluid force on the bottom when the pool is filled to the top.
18. By how many feet should the water in the pool of Exercise 17 be lowered in order for the force on the bottom to be reduced by a factor of $\frac{1}{2}$?
19. The accompanying figure shows a dam whose face is an inclined rectangle ($60^\circ$ to horizontal / $30^\circ$ to vertical, slant height $100\text{ m}$, width $200\text{ m}$). Find the fluid force on the face when the water is level with the top of this dam.
20. An observation window on a submarine is a square with $2\text{ ft}$ sides. Using $\rho_0$ for the weight density of seawater, find the fluid force on the window when the submarine has descended so that the window is vertical and its top is at a depth of $h$ feet.

#### FOCUS ON CONCEPTS
21. (a) Show: If the submarine in Exercise 20 descends vertically at a constant rate, then the fluid force on the window increases at a constant rate.  
    (b) At what rate is the force on the window increasing if the submarine is descending vertically at $20\text{ ft/min}$?
22. (a) Let $D = D_a$ denote a disk of radius $a$ submerged in a fluid of weight density $\rho$ such that the center of $D$ is $h$ units below the surface of the fluid. For each value of $r$ in the interval $(0, a]$, let $D_r$ denote the disk of radius $r$ that is concentric with $D$. Select a side of the disk $D$ and define $P(r)$ to be the fluid pressure on the chosen side of $D_r$. Use (5) to prove that
    $$\lim_{r \to 0^+} P(r) = \rho h$$
    (b) Explain why the result in part (a) may be interpreted to mean that fluid pressure at a given depth is the same in all directions. (This statement is one version of a result known as *Pascal’s Principle*.)
23. **Writing.** Suppose that we model the Earth’s atmosphere as a “fluid.” Atmospheric pressure at sea level is $P = 14.7\text{ lb/in}^2$ and the weight density of air at sea level is about $\rho = 4.66 \times 10^{-5}\text{ lb/in}^3$. With these numbers, what would Formula (7) yield as the height of the atmosphere above the Earth? Do you think this answer is reasonable? If not, explain how we might modify our assumptions to yield a more plausible answer.
24. **Writing.** Suppose that the weight density $\rho$ of a fluid is a function $\rho = \rho(x)$ of the depth $x$ within the fluid. How do you think that Formula (7) for fluid pressure will need to be modified? Support your answer with plausible arguments.

---

## CHAPTER 5 REVIEW EXERCISES

1. Describe the method of slicing for finding volumes, and use that method to derive an integral formula for finding volumes by the method of disks.
2. State an integral formula for finding a volume by the method of cylindrical shells, and use Riemann sums to derive the formula.
3. State an integral formula for finding the arc length of a smooth curve $y = f(x)$ over an interval $[a, b]$, and use Riemann sums to derive the formula.
4. State an integral formula for the work $W$ done by a variable force $F(x)$ applied in the direction of motion to an object moving from $x = a$ to $x = b$, and use Riemann sums to derive the formula.
5. State an integral formula for the fluid force $F$ exerted on a vertical flat surface immersed in a fluid of weight density $\rho$, and use Riemann sums to derive the formula.
6. Let $R$ be the region in the first quadrant enclosed by $y = x^2, y = 2 + x,$ and $x = 0$. In each part, set up, but do not evaluate, an integral or a sum of integrals that will solve the problem.  
   (a) Find the area of $R$ by integrating with respect to $x$.  
   (b) Find the area of $R$ by integrating with respect to $y$.  
   (c) Find the volume of the solid generated by revolving $R$ about the $x$-axis by integrating with respect to $x$.  
   (d) Find the volume of the solid generated by revolving $R$ about the $x$-axis by integrating with respect to $y$.  
   (e) Find the volume of the solid generated by revolving $R$ about the $y$-axis by integrating with respect to $x$.  
   (f) Find the volume of the solid generated by revolving $R$ about the $y$-axis by integrating with respect to $y$.  
   (g) Find the volume of the solid generated by revolving $R$ about the line $y = -3$ by integrating with respect to $x$.  
   (h) Find the volume of the solid generated by revolving $R$ about the line $x = 5$ by integrating with respect to $x$.
7. (a) Set up a sum of definite integrals that represents the total shaded area between the curves $y = f(x)$ and $y = g(x)$ in the accompanying figure.  
   (b) Find the total area enclosed between $y = x^3$ and $y = x$ over the interval $[-1, 2]$.
8. The accompanying figure shows velocity versus time curves for two cars that move along a straight track, accelerating from rest at a common starting line ($v_1(t) = 3t, v_2(t) = t^2/20$).  
   (a) How far apart are the cars after 60 seconds?  
   (b) How far apart are the cars after $T$ seconds, where $0 \le T \le 60$?
9. Let $R$ be the region enclosed by the curves $y = x^2 + 4, y = x^3,$ and the $y$-axis. Find and evaluate a definite integral that represents the volume of the solid generated by revolving $R$ about the $x$-axis.
10. A football has the shape of the solid generated by revolving the region bounded between the $x$-axis and the parabola $y = 4R(x^2 - \frac{1}{4}L^2)/L^2$ about the $x$-axis. Find its volume.
11. Find the volume of the solid whose base is the region bounded between the curves $y = \sqrt{x}$ and $y = 1/x$ for $1 \le x \le 4$ and whose cross sections perpendicular to the $x$-axis are squares.
12. Consider the region enclosed by $y = x^3, y = 0,$ and $x = 2$. Set up, but do not evaluate, an integral that represents the volume of the solid generated by revolving the region about the $x$-axis using  
    (a) disks (b) cylindrical shells.
13. Find the arc length in the second quadrant of the curve $x^{2/3} + y^{2/3} = 4$ from $x = -8$ to $x = -1$.
14. Let $C$ be the curve $y = x^8$ between $x = 1$ and $x = 3$. In each part, set up, but do not evaluate, an integral that solves the problem.  
    (a) Find the arc length of $C$ by integrating with respect to $x$.  
    (b) Find the arc length of $C$ by integrating with respect to $y$.
15. Find the area of the surface generated by revolving the curve $y = \sqrt{25 - x}, 9 \le x \le 16,$ about the $x$-axis.
16. Let $C$ be the curve $27x - y^3 = 0$ between $y = 0$ and $y = 2$. In each part, set up, but do not evaluate, an integral or a sum of integrals that solves the problem.  
    (a) Find the area of the surface generated by revolving $C$ about the $x$-axis by integrating with respect to $x$.  
    (b) Find the area of the surface generated by revolving $C$ about the $y$-axis by integrating with respect to $y$.  
    (c) Find the area of the surface generated by revolving $C$ about the line $y = -2$ by integrating with respect to $y$.
17. Consider the solid generated by revolving the region enclosed by $y = \sec x, x = 0, x = \pi/3,$ and $y = 0$ about the $x$-axis. Find the average value of the area of a cross section of this solid taken perpendicular to the $x$-axis.
18. Consider the solid generated by revolving the region enclosed by $y = \sqrt{a^2 - x^2}$ and $y = 0$ about the $x$-axis. Without performing an integration, find the average value of the area of a cross section of this solid taken perpendicular to the $x$-axis.
19. (a) A spring exerts a force of $0.5\text{ N}$ when stretched $0.25\text{ m}$ beyond its natural length. Assuming that Hooke’s law applies, how much work was performed in stretching the spring to this length?  
    (b) How far beyond its natural length can the spring be stretched with $25\text{ J}$ of work?
20. A boat is anchored so that the anchor is $150\text{ ft}$ below the surface of the water. In the water, the anchor weighs $2000\text{ lb}$ and the chain weighs $30\text{ lb/ft}$. How much work is required to raise the anchor to the surface?

**21–22 Find the centroid of the region.**
21. The region bounded by $y^2 = 4x$ and $y^2 = 8(x - 2)$.
22. The upper half of the ellipse $(x/a)^2 + (y/b)^2 = 1$.

23. In each part, set up, but do not evaluate, an integral that solves the problem.  
    (a) Find the fluid force exerted on a side of a box that has a $3\text{ m}$ square base and is filled to a depth of $1\text{ m}$ with a liquid of weight density $\rho\text{ N/m}^3$.  
    (b) Find the fluid force exerted by a liquid of weight density $\rho\text{ lb/ft}^3$ on a face of the vertical plate shown in part (a) of the accompanying figure (trapezoid $4\text{ ft}$ top width, $2\text{ ft}$ bottom width, $2\text{ ft}$ high, $1\text{ ft}$ below surface).  
    (c) Find the fluid force exerted on the parabolic dam in part (b) of the accompanying figure (parabolic face width $25\text{ m}$, depth $10\text{ m}$) by water that extends to the top of the dam.

---

## CHAPTER 5 MAKING CONNECTIONS

1. Suppose that $f$ is a nonnegative function defined on $[0, 1]$ such that the area between the graph of $f$ and the interval $[0, 1]$ is $A_1$ and such that the area of the region $R$ between the graph of $g(x) = f(x^2)$ and the interval $[0, 1]$ is $A_2$. In each part, express your answer in terms of $A_1$ and $A_2$.  
   (a) What is the volume of the solid of revolution generated by revolving $R$ about the $y$-axis?  
   (b) Find a value of $a$ such that if the $xy$-plane were horizontal, the region $R$ would balance on the line $x = a$.
2. A water tank has the shape of a conical frustum with radius of the base $5\text{ ft}$, radius of the top $10\text{ ft}$ and (vertical) height $15\text{ ft}$. Suppose the tank is filled with water and consider the problem of finding the work required to pump all the water out through a hole in the top of the tank.  
   (a) Solve this problem using the method of Example 5 in Section 5.6.  
   (b) Solve this problem using Definition 5.6.3. [*Hint:* Think of the base as the head of a piston that expands to a watertight fit against the sides of the tank as the piston is pushed upward. What important result about water pressure do you need to use?]
3. A disk of radius $a$ is an inhomogeneous lamina whose density is a function $f(r)$ of the distance $r$ to the center of the lamina. Modify the argument used to derive the method of cylindrical shells to find a formula for the mass of the lamina.
4. Compare Formula (10) in Section 5.7 with Formula (8) in Section 5.8. Then give a plausible argument that the force on a flat surface immersed vertically in a fluid of constant weight density is equal to the product of the area of the surface and the pressure at the centroid of the surface. Conclude that the force on the surface is the same as if the surface were immersed horizontally at the depth of the centroid.
5. Archimedes’ Principle states that a solid immersed in a fluid experiences a buoyant force equal to the weight of the fluid displaced by the solid.  
   (a) Use the results of Section 5.8 to verify Archimedes’ Principle in the case of (i) a box-shaped solid with a pair of faces parallel to the surface of the fluid, (ii) a solid cylinder with vertical axis, and (iii) a cylindrical shell with vertical axis.  
   (b) Give a plausible argument for Archimedes’ Principle in the case of a solid of revolution immersed in fluid such that the axis of revolution of the solid is vertical. [*Hint:* Approximate the solid by a union of cylindrical shells and use the result from part (a).]
