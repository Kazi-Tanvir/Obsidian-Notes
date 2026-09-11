# CHAPTER 13: PARTIAL DERIVATIVES

> Three-dimensional surfaces have high points and low points that are analogous to the peaks and valleys of a mountain range. In this chapter we will use derivatives to locate these points and to study other features of such surfaces.

In this chapter we will extend many of the basic concepts of calculus to functions of two or more variables, commonly called functions of several variables. We will begin by discussing limits and continuity for functions of two and three variables, then we will define derivatives of such functions, and then we will use these derivatives to study tangent planes, rates of change, slopes of surfaces, and maximization and minimization problems. Although many of the basic ideas that we developed for functions of one variable will carry over in a natural way, functions of several variables are intrinsically more complicated than functions of one variable, so we will need to develop new tools and new ideas to deal with such functions.

---

## 13.1 FUNCTIONS OF TWO OR MORE VARIABLES

In previous sections we studied real-valued functions of a real variable and vector-valued functions of a real variable. In this section we will consider real-valued functions of two or more real variables.

### NOTATION AND TERMINOLOGY

There are many familiar formulas in which a given variable depends on two or more other variables. For example, the area $A$ of a triangle depends on the base length $b$ and height $h$ by the formula $A = \frac{1}{2}bh$; the volume $V$ of a rectangular box depends on the length $l$, the width $w$, and the height $h$ by the formula $V = lwh$; and the arithmetic average $\bar{x}$ of $n$ real numbers, $x_1, x_2, \dots, x_n$, depends on those numbers by the formula
$$\bar{x} = \frac{1}{n}(x_1 + x_2 + \dots + x_n)$$

Thus, we say that:
* $A$ is a function of the two variables $b$ and $h$;
* $V$ is a function of the three variables $l$, $w$, and $h$;
* $\bar{x}$ is a function of the $n$ variables $x_1, x_2, \dots, x_n$.

The terminology and notation for functions of two or more variables is similar to that for functions of one variable. For example, the expression
$$z = f(x, y)$$
means that $z$ is a function of $x$ and $y$ in the sense that a unique value of the dependent variable $z$ is determined by specifying values for the independent variables $x$ and $y$. Similarly,
$$w = f(x, y, z)$$
expresses $w$ as a function of $x$, $y$, and $z$, and
$$u = f(x_1, x_2, \dots, x_n)$$
expresses $u$ as a function of $x_1, x_2, \dots, x_n$.

As with functions of one variable, the independent variables of a function of two or more variables may be restricted to lie in some set $D$, which we call the **domain** of $f$. Sometimes the domain will be determined by physical restrictions on the variables. If the function is defined by a formula and if there are no physical restrictions or other restrictions stated explicitly, then it is understood that the domain consists of all points for which the formula yields a real value for the dependent variable. We call this the **natural domain** of the function. The following definitions summarize this discussion.

> **13.1.1 DEFINITION**  
> A **function $f$ of two variables**, $x$ and $y$, is a rule that assigns a unique real number $f(x, y)$ to each point $(x, y)$ in some set $D$ in the $xy$-plane.

> **13.1.2 DEFINITION**  
> A **function $f$ of three variables**, $x, y,$ and $z$, is a rule that assigns a unique real number $f(x, y, z)$ to each point $(x, y, z)$ in some set $D$ in three-dimensional space.

By extension, one can define the notion of "$n$-dimensional space" in which a "point" is a sequence of $n$ real numbers $(x_1, x_2, \dots, x_n)$, and a function of $n$ real variables is a rule that assigns a unique real number $f(x_1, x_2, \dots, x_n)$ to each point in some set in this space.

#### Example 1
Let $f(x, y) = \sqrt{y + 1} + \ln(x^2 - y)$. Find $f(e, 0)$ and sketch the natural domain of $f$.

**Solution.** By substitution,
$$f(e, 0) = \sqrt{0 + 1} + \ln(e^2 - 0) = \sqrt{1} + \ln(e^2) = 1 + 2 = 3$$
To find the natural domain of $f$, we note that $\sqrt{y + 1}$ is defined only when $y \ge -1$, while $\ln(x^2 - y)$ is defined only when $0 < x^2 - y$ or $y < x^2$. Thus, the natural domain of $f$ consists of all points in the $xy$-plane for which $-1 \le y < x^2$. To sketch the natural domain, we first sketch the parabola $y = x^2$ as a "dashed" curve and the line $y = -1$ as a solid curve. The natural domain of $f$ is then the region lying above or on the line $y = -1$ and below the parabola $y = x^2$ (Figure 13.1.1).

#### Example 2
Let $f(x, y, z) = \sqrt{1 - x^2 - y^2 - z^2}$. Find $f\left(0, \frac{1}{2}, -\frac{1}{2}\right)$ and the natural domain of $f$.

**Solution.** By substitution,
$$f\left(0, \frac{1}{2}, -\frac{1}{2}\right) = \sqrt{1 - (0)^2 - \left(\frac{1}{2}\right)^2 - \left(-\frac{1}{2}\right)^2} = \sqrt{\frac{1}{2}} = \frac{1}{\sqrt{2}}$$
Because of the square root sign, we must have $0 \le 1 - x^2 - y^2 - z^2$ in order to have a real value for $f(x, y, z)$. Rewriting this inequality in the form
$$x^2 + y^2 + z^2 \le 1$$
we see that the natural domain of $f$ consists of all points on or within the sphere $x^2 + y^2 + z^2 = 1$.

---

### FUNCTIONS DESCRIBED BY TABLES

Sometimes it is either desirable or necessary to represent a function of two variables in table form, rather than as an explicit formula. For example, the U.S. National Weather Service uses the formula
$$W = 35.74 + 0.6215T + (0.4275T - 35.75)v^{0.16} \tag{1}$$
to model the wind chill index $W$ (in $^\circ\text{F}$) as a function of the temperature $T$ (in $^\circ\text{F}$) and the wind speed $v$ (in $\text{mi/h}$) for wind speeds greater than $3\text{ mi/h}$. This formula is sufficiently complex that it is difficult to get an intuitive feel for the relationship between the variables. One can get a clearer sense of the relationship by selecting sample values of $T$ and $v$ and constructing a table, such as Table 13.1.1, in which we have rounded the values of $W$ to the nearest integer.

#### Table 13.1.1: Wind Chill Index
| Wind Speed $v$ (mi/h) \ Temperature $T$ ($^\circ$F) | 20 | 25 | 30 | 35 |
| :---: | :---: | :---: | :---: | :---: |
| **5** | 13 | 19 | 25 | 31 |
| **15** | 6 | 13 | 19 | 25 |
| **25** | 3 | 9 | 16 | 23 |
| **35** | 0 | 7 | 14 | 21 |
| **45** | -2 | 5 | 12 | 19 |

For example, if the temperature is $30^\circ\text{F}$ and the wind speed is $5\text{ mi/h}$, it feels as if the temperature is $25^\circ\text{F}$. If the wind speed increases to $15\text{ mi/h}$, the temperature then feels as if it has dropped to $19^\circ\text{F}$. Note that in this case, an increase in wind speed of $10\text{ mi/h}$ causes a $6^\circ\text{F}$ decrease in the wind chill index. To estimate wind chill values not displayed in the table, we can use linear interpolation. For example, suppose that the temperature is $30^\circ\text{F}$ and the wind speed is $7\text{ mi/h}$. A reasonable estimate for the drop in the wind chill index from its value when the wind speed is $5\text{ mi/h}$ would be $\frac{2}{10} \cdot 6^\circ\text{F} = 1.2^\circ\text{F}$. The resulting estimate in wind chill would then be $25^\circ - 1.2^\circ = 23.8^\circ\text{F}$.

---

### GRAPHS OF FUNCTIONS OF TWO VARIABLES

Recall that for a function $f$ of one variable, the graph of $f(x)$ in the $xy$-plane was defined to be the graph of the equation $y = f(x)$. Similarly, if $f$ is a function of two variables, we define the **graph of $f(x, y)$** in $xyz$-space to be the graph of the equation $z = f(x, y)$. In general, such a graph will be a surface in 3-space.

#### Example 3
In each part, describe the graph of the function in an $xyz$-coordinate system:
(a) $f(x, y) = 1 - x - \frac{1}{2}y$  
(b) $f(x, y) = \sqrt{1 - x^2 - y^2}$  
(c) $f(x, y) = -\sqrt{x^2 + y^2}$  

**Solution (a).** By definition, the graph of the given function is the graph of the equation
$$z = 1 - x - \frac{1}{2}y$$
which is a plane. A triangular portion of the plane can be sketched by plotting the intersections with the coordinate axes $(1, 0, 0)$, $(0, 2, 0)$, $(0, 0, 1)$ and joining them with line segments (Figure 13.1.2a).

**Solution (b).** By definition, the graph of the given function is the graph of the equation
$$z = \sqrt{1 - x^2 - y^2} \tag{2}$$
After squaring both sides, this can be rewritten as $x^2 + y^2 + z^2 = 1$, which represents a sphere of radius 1, centered at the origin. Since (2) imposes the added condition that $z \ge 0$, the graph is just the upper hemisphere (Figure 13.1.2b).

**Solution (c).** The graph of the given function is the graph of the equation
$$z = -\sqrt{x^2 + y^2} \tag{3}$$
After squaring, we obtain $z^2 = x^2 + y^2$, which is the equation of a circular cone. Since (3) imposes the condition that $z \le 0$, the graph is just the lower nappe of the cone (Figure 13.1.2c).

---

### LEVEL CURVES

We are all familiar with topographic (or contour) maps in which a three-dimensional landscape is represented by two-dimensional contour lines or curves of constant elevation. Passing horizontal planes of constant elevation $z = k$ through a surface $z = f(x, y)$ produces intersection curves $f(x, y) = k$. The projection of this intersection onto the $xy$-plane is called the **level curve of height $k$** (or **level curve with constant $k$**). A set of level curves for $z = f(x, y)$ is called a **contour plot** or **contour map** of $f$.

#### Example 4
The graph of the function $f(x, y) = y^2 - x^2$ in $xyz$-space is the hyperbolic paraboloid (saddle surface). The level curves have equations of the form $y^2 - x^2 = k$. For $k > 0$ these curves are hyperbolas opening along lines parallel to the $y$-axis; for $k < 0$ they are hyperbolas opening along lines parallel to the $x$-axis; and for $k = 0$ the level curve consists of the intersecting lines $y + x = 0$ and $y - x = 0$.

#### Example 5
Sketch the contour plot of $f(x, y) = 4x^2 + y^2$ using level curves of height $k = 0, 1, 2, 3, 4, 5$.

**Solution.** The graph of the surface $z = 4x^2 + y^2$ is an elliptic paraboloid. The level curve of height $k$ has the equation $4x^2 + y^2 = k$. If $k = 0$, then the graph is the single point $(0, 0)$. For $k > 0$ we can rewrite the equation as
$$\frac{x^2}{k/4} + \frac{y^2}{k} = 1$$
which represents a family of ellipses with $x$-intercepts $\pm\sqrt{k}/2$ and $y$-intercepts $\pm\sqrt{k}$.

#### Example 6
Let $f(r, L)$ be the monthly payment on a 5-year car loan as a function of the interest rate $r$ and the loan amount $L$. Use Figure 13.1.7 in each part:
(a) Estimate the monthly payment on a loan of $\$3000$ at an interest rate of $7\%$.  
(b) Estimate the monthly payment on a loan of $\$5000$ at an interest rate of $3\%$.  
(c) Estimate the loan amount if the monthly payment is $\$80$ and the interest rate is $3\%$.  

**Solution (a).** Since the point $(7, 3000)$ appears to lie on the contour labeled 60, we estimate the monthly payment to be $\$60$.  
**Solution (b).** Since the point $(3, 5000)$ appears to be midway between the contours labeled 80 and 100, we estimate the monthly payment to be $\$90$.  
**Solution (c).** The vertical line $x = 3$ intersects the contour labeled 80 at a point whose $L$ coordinate appears to be 4500. Hence, we estimate the loan amount to be $\$4500$.

---

### LEVEL SURFACES

If $k$ is a constant, then the graph of the equation $f(x, y, z) = k$ will generally be a surface in 3-space, which we call the **level surface with constant $k$**.

#### Example 7
Describe the level surfaces of:  
(a) $f(x, y, z) = x^2 + y^2 + z^2$  
(b) $f(x, y, z) = z^2 - x^2 - y^2$  

**Solution (a).** The level surfaces have equations of the form $x^2 + y^2 + z^2 = k$. For $k > 0$ the graph is a sphere of radius $\sqrt{k}$, centered at the origin; for $k = 0$ the graph is the single point $(0, 0, 0)$; and for $k < 0$ there is no level surface.  
**Solution (b).** The level surfaces have equations $z^2 - x^2 - y^2 = k$. This equation represents a circular cone if $k = 0$, a hyperboloid of two sheets if $k > 0$, and a hyperboloid of one sheet if $k < 0$.

---

### QUICK CHECK EXERCISES 13.1

1. The domain of $f(x, y) = \ln xy$ is $\underline{\quad\text{points }(x, y)\text{ in the first or third quadrants}\quad}$ and the domain of $g(x, y) = \ln x + \ln y$ is $\underline{\quad\text{points }(x, y)\text{ in the first quadrant}\quad}$.
2. Let $f(x, y) = \frac{x - y}{x + y + 1}$.  
   (a) $f(2, 1) = \underline{\quad 1/4 \quad}$  
   (b) $f(1, 2) = \underline{\quad -1/4 \quad}$  
   (c) $f(a, a) = \underline{\quad 0 \quad}$  
   (d) $f(y + 1, y) = \underline{\quad 1/(2y + 2) \quad}$  
3. Let $f(x, y) = e^{x+y}$.  
   (a) For what values of $k$ will the graph of the level curve $f(x, y) = k$ be nonempty? **Answer:** $k > 0$  
   (b) Describe the level curves $f(x, y) = k$ for the values of $k$ obtained in part (a). **Answer:** the lines $x + y = \ln k$  
4. Let $f(x, y, z) = \frac{1}{x^2 + y^2 + z^2 + 1}$.  
   (a) For what values of $k$ will the graph of the level surface $f(x, y, z) = k$ be nonempty? **Answer:** $0 < k \le 1$  
   (b) Describe the level surfaces $f(x, y, z) = k$ for the values of $k$ obtained in part (a). **Answer:** spheres of radius $\sqrt{(1 - k)/k}$ for $0 < k < 1$, the single point $(0, 0, 0)$ for $k = 1$.

---

### EXERCISE SET 13.1

**1–8 These exercises are concerned with functions of two variables.**

1. Let $f(x, y) = x^2 y + 1$. Find:  
   (a) $f(2, 1) = (2)^2(1) + 1 = 5$  
   (b) $f(1, 2) = (1)^2(2) + 1 = 3$  
   (c) $f(0, 0) = (0)^2(0) + 1 = 1$  
   (d) $f(1, -3) = (1)^2(-3) + 1 = -2$  
   (e) $f(3a, a) = (3a)^2(a) + 1 = 9a^3 + 1$  
   (f) $f(ab, a - b) = (ab)^2(a - b) + 1 = a^3 b^2 - a^2 b^3 + 1$

2. Let $f(x, y) = x + \sqrt[3]{xy}$. Find:  
   (a) $f(t, t^2) = t + \sqrt[3]{t \cdot t^2} = t + t = 2t$  
   (b) $f(x, x^2) = x + \sqrt[3]{x \cdot x^2} = x + x = 2x$  
   (c) $f(2y^2, 4y) = 2y^2 + \sqrt[3]{(2y^2)(4y)} = 2y^2 + \sqrt[3]{8y^3} = 2y^2 + 2y$

3. Let $f(x, y) = xy + 3$. Find:  
   (a) $f(x + y, x - y) = (x + y)(x - y) + 3 = x^2 - y^2 + 3$  
   (b) $f(xy, 3x^2 y^3) = (xy)(3x^2 y^3) + 3 = 3x^3 y^4 + 3$

4. Let $g(x) = x\sin x$. Find:  
   (a) $g(x/y) = \frac{x}{y}\sin\left(\frac{x}{y}\right)$  
   (b) $g(xy) = xy\sin(xy)$  
   (c) $g(x - y) = (x - y)\sin(x - y)$

5. Find $F(g(x), h(y))$ if $F(x, y) = x e^{xy}, g(x) = x^3$, and $h(y) = 3y + 1$.  
   **Solution:** $F(g(x), h(y)) = x^3 e^{x^3(3y + 1)}$.

6. Find $g(u(x, y), v(x, y))$ if $g(x, y) = y\sin(x^2 y), u(x, y) = x^2 y^3$, and $v(x, y) = \pi xy$.  
   **Solution:** $g(u(x, y), v(x, y)) = \pi xy \sin\left((x^2 y^3)^2 (\pi xy)\right) = \pi xy \sin(\pi x^5 y^7)$.

7. Let $f(x, y) = x + 3x^2 y^2, x(t) = t^2$, and $y(t) = t^3$. Find:  
   (a) $f(x(t), y(t)) = t^2 + 3(t^2)^2 (t^3)^2 = t^2 + 3t^4 t^6 = t^2 + 3t^{10}$  
   (b) $f(x(0), y(0)) = 0 + 3(0)^{10} = 0$  
   (c) $f(x(2), y(2)) = (2)^2 + 3(2)^{10} = 4 + 3(1024) = 3076$

8. Let $g(x, y) = y e^{-3x}, x(t) = \ln(t^2 + 1)$, and $y(t) = \sqrt{t}$. Find $g(x(t), y(t))$.  
   **Solution:** $g(x(t), y(t)) = \sqrt{t} e^{-3\ln(t^2 + 1)} = \sqrt{t}(t^2 + 1)^{-3} = \frac{\sqrt{t}}{(t^2 + 1)^3}$.

**9–10 Medication concentration modeling:**  
$C(x, t) = 0.2x(e^{-0.2t} - e^{-t})$, where $x$ is dosage in mg and $t$ is hours since administration.

9. (a) Estimate $C(25, 3)$ to two decimal places:  
   $C(25, 3) = 0.2(25)(e^{-0.6} - e^{-3}) = 5(0.54881 - 0.04979) \approx 2.50\text{ mg/L}$.  
   (b) If dosage is $100\text{ mg}$: $C(100, t) = 20(e^{-0.2t} - e^{-t})$.  
   (c) After 1 hour: $C(x, 1) = 0.2x(e^{-0.2} - e^{-1}) \approx 0.09x\text{ mg/L}$.

10. (a) Concentration reaches effective level after $0.5\text{ h}$. It remains effective until $C(x, t)$ drops below the threshold (determined from graph/numeric values).  
    (b) Maximum concentration occurs when $\frac{dC}{dt} = 0 \implies -0.2e^{-0.2t} + e^{-t} = 0 \implies e^{0.8t} = 5 \implies t = \frac{\ln 5}{0.8} \approx 2.01\text{ h}$. $C_{\max} = 20(e^{-0.402} - e^{-2.01}) \approx 10.7\text{ mg/L}$.

**11–14 Estimates using Table 13.1.1 (Wind Chill Index):**
11. (a) $T = 25^\circ\text{F}, v = 7\text{ mi/h} \implies W \approx 19 - \frac{2}{10}(6) = 17.8^\circ\text{F} \approx 18^\circ\text{F}$.  
    (b) $T = 28^\circ\text{F}, v = 5\text{ mi/h} \implies W \approx 19 + \frac{3}{5}(6) = 22.6^\circ\text{F} \approx 23^\circ\text{F}$.
12. (a) $T = 35^\circ\text{F}, v = 14\text{ mi/h} \implies W \approx 31 - \frac{9}{10}(6) = 25.6^\circ\text{F} \approx 26^\circ\text{F}$.  
    (b) $T = 32^\circ\text{F}, v = 15\text{ mi/h} \implies W \approx 19 + \frac{2}{5}(6) = 21.4^\circ\text{F} \approx 21^\circ\text{F}$.
13. (a) $W = 16^\circ\text{F}, v = 25\text{ mi/h} \implies T = 30^\circ\text{F}$.  
    (b) $W = 6^\circ\text{F}, v = 25\text{ mi/h} \implies T \approx 22.5^\circ\text{F}$.
14. (a) $W = 7^\circ\text{F}, T = 25^\circ\text{F} \implies v = 35\text{ mi/h}$.  
    (b) $W = 15^\circ\text{F}, T = 30^\circ\text{F} \implies v \approx 30\text{ mi/h}$.

**15–16 Relative Humidity and Wet-Bulb Depression:**
15. (a) Air temperature $20^\circ\text{C}$, wet-bulb reading $16^\circ\text{C} \implies \text{depression} = 4^\circ\text{C} \implies \text{humidity} = 66\%$.  
    (b) Air temperature $25^\circ\text{C}$, depression $3.5^\circ\text{C} \implies \text{humidity} \approx \frac{77+70}{2} = 73.5\%$.  
    (c) Air temperature $22^\circ\text{C}$, depression $5^\circ\text{C} \implies \text{humidity} \approx 59 + \frac{2}{5}(63-59) = 60.6\%$.
16. (a) Air temp $30^\circ\text{C}$, relative humidity $73\% \implies \text{depression} = 4^\circ\text{C}$.  
    (b) Air temp $15^\circ\text{C}$, depression $4.25^\circ\text{C} \implies \text{humidity} \approx 62 - 0.25(9) = 59.75\%$.  
    (c) Air temp $26^\circ\text{C}$, depression $3^\circ\text{C} \implies \text{humidity} \approx 77 + 0.2(2) = 77.4\%$.

**17–20 Functions of three variables:**
17. Let $f(x, y, z) = xy^2 z^3 + 3$. Find:  
    (a) $f(2, 1, 2) = 2(1)^2(2)^3 + 3 = 16 + 3 = 19$  
    (b) $f(-3, 2, 1) = (-3)(4)(1) + 3 = -12 + 3 = -9$  
    (c) $f(0, 0, 0) = 3$  
    (d) $f(a, a, a) = a \cdot a^2 \cdot a^3 + 3 = a^6 + 3$  
    (e) $f(t, t^2, -t) = t(t^2)^2(-t)^3 + 3 = t \cdot t^4 (-t^3) + 3 = -t^8 + 3$  
    (f) $f(a+b, a-b, b) = (a+b)(a-b)^2 b^3 + 3$
18. Let $f(x, y, z) = zxy + x$. Find:  
    (a) $f(x+y, x-y, x^2) = x^2(x+y)(x-y) + (x+y) = x^2(x^2 - y^2) + x + y = x^4 - x^2 y^2 + x + y$  
    (b) $f(xy, y/x, xz) = (xz)(xy)(y/x) + xy = x y^2 z + xy$
19. $F(f(x), g(y), h(z))$ where $F(x, y, z) = y e^{xyz}, f(x) = x^2, g(y) = y+1, h(z) = z^2$:  
    $F = (y+1)e^{x^2(y+1)z^2}$.
20. $g(u(x, y, z), v(x, y, z), w(x, y, z))$ where $g(x, y, z) = z\sin xy, u = x^2 z^3, v = \pi xyz, w = xy/z$:  
    $g = \frac{xy}{z}\sin((x^2 z^3)(\pi xyz)) = \frac{xy}{z}\sin(\pi x^3 y z^4)$.

**21–22 Functions of four or more variables:**
21. (a) $f(x, y, z, t) = x^2 y^3 \sqrt{z+t} \implies f(\sqrt{5}, 2, \pi, 3\pi) = 5(8)\sqrt{4\pi} = 40(2\sqrt{\pi}) = 80\sqrt{\pi}$.  
    (b) $f(x_1, \dots, x_n) = \sum_{k=1}^n k x_k \implies f(1, 1, \dots, 1) = \sum_{k=1}^n k = \frac{n(n+1)}{2}$.
22. (a) $f(u, v, \lambda, \phi) = e^{u+v}\cos\lambda\tan\phi \implies f(-2, 2, 0, \pi/4) = e^0 \cos 0 \tan(\pi/4) = 1 \cdot 1 \cdot 1 = 1$.  
    (b) $f(x_1, \dots, x_n) = x_1^2 + x_2^2 + \dots + x_n^2 \implies f(1, 2, \dots, n) = \sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$.

**23–26 Domains of functions of two variables:**
23. $f(x, y) = \ln(1 - x^2 - y^2)$: Domain is $1 - x^2 - y^2 > 0 \implies x^2 + y^2 < 1$ (open unit disk, dashed boundary).
24. $f(x, y) = \sqrt{x^2 + y^2 - 4}$: Domain is $x^2 + y^2 \ge 4$ (exterior and boundary of circle of radius 2, solid boundary).
25. $f(x, y) = \frac{1}{x - y^2}$: Domain is $x \ne y^2$ (entire $xy$-plane except parabola $x = y^2$, dashed boundary).
26. $f(x, y) = \ln xy$: Domain is $xy > 0$, i.e., first and third quadrants (excluding axes, dashed boundaries).

**27–28 Describe domain in words:**
27. (a) $f(x, y) = x e^{-\sqrt{y+2}}$: The half-plane consisting of all points on or above the line $y = -2$.  
    (b) $f(x, y, z) = \sqrt{25 - x^2 - y^2 - z^2}$: The solid sphere of radius 5 centered at the origin, including its spherical boundary.  
    (c) $f(x, y, z) = e^{xyz}$: All of 3-dimensional space ($\mathbb{R}^3$).
28. (a) $f(x, y) = \frac{\sqrt{4 - x^2}}{y^2 + 3}$: The vertical strip $-2 \le x \le 2$ in the $xy$-plane.  
    (b) $f(x, y) = \ln(y - 2x)$: The open half-plane lying strictly above the line $y = 2x$.  
    (c) $f(x, y, z) = \frac{xyz}{x + y + z}$: All points in 3-space except those lying on the plane $x + y + z = 0$.

**29–32 True–False:**
29. **True.** The composition requires $-1 \le t \le 1$ for $\sin^{-1} t$ and $t \ge 0$ for $\sqrt{t}$, giving $0 \le t \le 1$.
30. **False.** The contour $f(x, y) = m$ is the line $y = mx$ with the origin $(0, 0)$ removed (where $f$ is undefined).
31. **False.** The domain is the region inside and on the infinite cylinder $x^2 + y^2 \le 1$ in 3-space, not just a 2D disk.
32. **True.** Every level surface has the form $x + 2y + 3z = k$, which is a plane.

**33–42 Sketch the graph of $f(x, y)$:**
33. $f(x, y) = 3$: Horizontal plane $z = 3$.
34. $f(x, y) = \sqrt{9 - x^2 - y^2}$: Upper hemisphere of radius 3 centered at the origin.
35. $f(x, y) = \sqrt{x^2 + y^2}$: Upper nappe of circular cone $z = \sqrt{x^2 + y^2}$.
36. $f(x, y) = x^2 + y^2$: Circular paraboloid opening upwards with vertex at the origin.
37. $f(x, y) = x^2 - y^2$: Hyperbolic paraboloid (saddle surface).
38. $f(x, y) = 4 - x^2 - y^2$: Circular paraboloid opening downward with vertex at $(0, 0, 4)$.
39. $f(x, y) = \sqrt{x^2 + y^2 + 1}$: Upper sheet of circular hyperboloid of two sheets $z^2 - x^2 - y^2 = 1$.
40. $f(x, y) = \sqrt{x^2 + y^2 - 1}$: Upper half of hyperboloid of one sheet $x^2 + y^2 - z^2 = 1$.
41. $f(x, y) = y + 1$: Plane $z = y + 1$ parallel to the $x$-axis.
42. $f(x, y) = x^2$: Parabolic cylinder $z = x^2$ parallel to the $y$-axis.

**43–44 Geometric description of level curves:**
43. (a) $5x^2 - 5y^2 = k$: Hyperbolas (or intersecting lines if $k = 0$).  
    (b) $y - 4x^2 = k \implies y = 4x^2 + k$: Parabolas.  
    (c) $x^2 + 3y^2 = k$: Noncircular ellipses.  
    (d) $3x^2 = k \implies x = \pm\sqrt{k/3}$: Pairs of parallel vertical lines.
44. (a) $x^2 - 2xy + y^2 = (x - y)^2 = k$: Parallel lines $x - y = \pm\sqrt{k}$.  
    (b) $2x^2 + 2y^2 = k$: Circles.  
    (c) $x^2 - 2x - y^2 = k \implies (x - 1)^2 - y^2 = k + 1$: Hyperbolas.  
    (d) $2y^2 - x = k \implies x = 2y^2 - k$: Parabolas.

**45–46 Car Loan monthly payment (Figure 13.1.7):**
45. (a) $L = 6000, r = 11\% \implies \text{Payment} \approx \$130/\text{month}$.  
    (b) If $r$ drops to $9\%$ and payment stays $\$130$, $L \approx \$6300 \implies$ can borrow $\approx \$300$ more.
46. (a) $L = 3000, r = 4\% \implies \text{Payment} \approx \$55/\text{month}$.  
    (b) If $r = 7\%$ and payment is $\$55$, $L \approx \$2750 \implies \$250$ less.

**47–48 Focus on Concepts (Contour Plots & Surfaces):**
47. (a) $f(x, y) = \sqrt{x^2 + y^2}$ (cone: equally spaced concentric circular contours).  
    (b) $f(x, y) = x^2 + y^2$ (paraboloid: circular contours become closer together as distance from origin increases).  
    (c) $f(x, y) = 1 - x^2 - y^2$ (inverted paraboloid: center has largest value, contours grow closer outwards).
48. (a) Match with surface (III) (egg-crate / periodic ripples).  
    (b) Match with surface (I) (saddle surface).  
    (c) Match with surface (IV) (monkey saddle / cubic).  
    (d) Match with surface (II) (peaks and pits).

49. **Contour map analysis (Figure Ex-49):**  
    (a) Point $B$ (elevation $\approx 350\text{ ft}$) is higher than point $A$ (elevation $\approx 150\text{ ft}$).  
    (b) Slope is steeper at point $B$ because the contour lines are much closer together.  
    (c) Moving from $A$ with $y$ fixed and $x$ increasing moves toward higher contour lines $\implies$ elevation increases.  
    (d) Moving from $B$ with $y$ fixed and $x$ increasing moves toward lower contour lines $\implies$ elevation decreases.  
    (e) Moving from $A$ with $x$ fixed and $y$ decreasing crosses lower contours $\implies$ elevation decreases.  
    (f) Moving from $B$ with $x$ fixed and $y$ decreasing crosses lower contours $\implies$ elevation decreases.

50. **Weather map isobars (Figure Ex-50):**  
    (a) Wind speed is greater in Medicine Hat because isobars are packed more tightly.  
    (b) $\Delta p \approx 1012 - 994 = 18\text{ mb}$. Average rate of change $\approx \frac{18\text{ mb}}{1400\text{ mi}} \approx 0.013\text{ mb/mi}$.

**51–56 Sketch level curves $z = k$:**
51. $z = x^2 + y^2; k = 0, 1, 2, 3, 4$: Concentric circles of radii $0, 1, \sqrt{2}, \sqrt{3}, 2$.
52. $z = y/x; k = -2, -1, 0, 1, 2$: Lines through origin $y = kx$ (excluding the origin).
53. $z = x^2 + y; k = -2, -1, 0, 1, 2$: Parabolas opening downward $y = -x^2 + k$.
54. $z = x^2 + 9y^2; k = 0, 1, 2, 3, 4$: Concentric ellipses with semi-major axes along $x$.
55. $z = x^2 - y^2; k = -2, -1, 0, 1, 2$: Hyperbolas opening along $x$ ($k > 0$), along $y$ ($k < 0$), and lines $y = \pm x$ ($k = 0$).
56. $z = y\csc x; k = -2, -1, 0, 1, 2$: Curves $y = k\sin x$ for $x \ne n\pi$.

**57–60 Sketch level surfaces $f(x, y, z) = k$:**
57. $4x^2 + y^2 + 4z^2 = 16 \implies \frac{x^2}{4} + \frac{y^2}{16} + \frac{z^2}{4} = 1$: Ellipsoid centered at origin.
58. $x^2 + y^2 - z^2 = 0$: Right circular cone with vertex at the origin along the $z$-axis.
59. $z - x^2 - y^2 + 4 = 7 \implies z = x^2 + y^2 + 3$: Circular paraboloid opening upwards with vertex at $(0, 0, 3)$.
60. $4x - 2y + z = 1$: Plane with normal vector $\langle 4, -2, 1 \rangle$.

**61–64 Describe level surfaces in words:**
61. $f(x, y, z) = (x - 2)^2 + y^2 + z^2$: Family of concentric spheres centered at $(2, 0, 0)$ for $k > 0$.
62. $f(x, y, z) = 3x - y + 2z$: Family of parallel planes with normal vector $\langle 3, -1, 2 \rangle$.
63. $f(x, y, z) = x^2 + z^2$: Family of concentric right circular cylinders centered along the $y$-axis for $k > 0$.
64. $f(x, y, z) = z - x^2 - y^2$: Family of circular paraboloids opening in the positive $z$-direction with vertices at $(0, 0, k)$.

**65–68 Level curves and surfaces through given points:**
65. $f(x, y) = x^2 - 2x^3 + 3xy$:  
    (a) $P(-1, 1) \implies k = 1 - 2(-1) + 3(-1)(1) = 0 \implies x^2 - 2x^3 + 3xy = 0$.  
    (b) $P(0, 0) \implies k = 0 \implies x^2 - 2x^3 + 3xy = 0$.  
    (c) $P(2, -1) \implies k = 4 - 2(8) + 3(2)(-1) = -18 \implies x^2 - 2x^3 + 3xy = -18$.
66. $f(x, y) = y e^x$:  
    (a) $P(\ln 2, 1) \implies k = 1 \cdot e^{\ln 2} = 2 \implies y e^x = 2$.  
    (b) $P(0, 3) \implies k = 3e^0 = 3 \implies y e^x = 3$.  
    (c) $P(1, -2) \implies k = -2e \implies y e^x = -2e$.
67. $f(x, y, z) = x^2 + y^2 - z$:  
    (a) $P(1, -2, 0) \implies k = 1 + 4 - 0 = 5 \implies x^2 + y^2 - z = 5$.  
    (b) $P(1, 0, 3) \implies k = 1 + 0 - 3 = -2 \implies x^2 + y^2 - z = -2$.  
    (c) $P(0, 0, 0) \implies k = 0 \implies x^2 + y^2 - z = 0$.
68. $f(x, y, z) = xyz + 3$:  
    (a) $P(1, 0, 2) \implies k = 0 + 3 = 3 \implies xyz = 0$.  
    (b) $P(-2, 4, 1) \implies k = -8 + 3 = -5 \implies xyz + 3 = -5 \implies xyz = -8$.  
    (c) $P(0, 0, 0) \implies k = 3 \implies xyz = 0$.

69. **Isothermal curves:** $T(x, y) = xy$ on $x > 0, y > 0$.  
    (a) $xy = 1, xy = 2, xy = 3$: Hyperbolas in the first quadrant.  
    (b) At $(1, 4)$, $T = 4$. Constant temperature path is the hyperbola $y = 4/x$.

70. **Equipotential curves:** $V(x, y) = \frac{8}{\sqrt{16 + x^2 + y^2}}$.  
    $V = 2.0 \implies 16 + x^2 + y^2 = 16 \implies (0, 0)$.  
    $V = 1.0 \implies 16 + x^2 + y^2 = 64 \implies x^2 + y^2 = 48$ (circle of radius $\sqrt{48}$).  
    $V = 0.5 \implies 16 + x^2 + y^2 = 256 \implies x^2 + y^2 = 240$ (circle of radius $\sqrt{240}$).

71–74. Graphing utility and CAS problems for level curves and 3D surface plots.

75. **Transformations:**  
    (a) $g(x, y) = f(x - 1, y)$: Shifted 1 unit in positive $x$-direction.  
    (b) $g(x, y) = 1 + f(x, y)$: Shifted 1 unit upward in positive $z$-direction.  
    (c) $g(x, y) = -f(x, y + 1)$: Shifted 1 unit in negative $y$-direction and reflected across the $xy$-plane.

76. (a) $f(x, y) = e^{-(x^2 + y^2)}$: Bell-shaped surface of revolution centered at origin.  
    (b) For larger $a > 0$, the surface is compressed radially toward the $z$-axis (steeper bell).

77–78. **Writing exercises** on domains, physical constraints, and geometric representations (3D graphs vs contour maps).

---

## 13.2 LIMITS AND CONTINUITY

### LIMITS ALONG CURVES

For a function of one variable there are two one-sided limits at a point $x_0$: $\lim_{x\to x_0^+} f(x)$ and $\lim_{x\to x_0^-} f(x)$. For functions of two or three variables, there are infinitely many curves along which one point can approach another.

If $C$ is a smooth parametric curve in 2-space or 3-space represented by $x = x(t), y = y(t)$ (or $x = x(t), y = y(t), z = z(t)$), and if $x_0 = x(t_0), y_0 = y(t_0), z_0 = z(t_0)$, then:
$$\lim_{\substack{(x, y)\to(x_0, y_0) \\ (\text{along } C)}} f(x, y) = \lim_{t\to t_0} f(x(t), y(t)) \tag{1}$$
$$\lim_{\substack{(x, y, z)\to(x_0, y_0, z_0) \\ (\text{along } C)}} f(x, y, z) = \lim_{t\to t_0} f(x(t), y(t), z(t)) \tag{2}$$

#### Example 1
Find the limit of $f(x, y) = -\frac{xy}{x^2 + y^2}$ as $(x, y) \to (0, 0)$ along:  
(a) the $x$-axis: $x = t, y = 0 \implies \lim_{t\to 0} 0 = 0$.  
(b) the $y$-axis: $x = 0, y = t \implies \lim_{t\to 0} 0 = 0$.  
(c) the line $y = x$: $x = t, y = t \implies \lim_{t\to 0} \left(-\frac{t^2}{2t^2}\right) = -\frac{1}{2}$.  
(d) the line $y = -x$: $x = t, y = -t \implies \lim_{t\to 0} \left(\frac{t^2}{2t^2}\right) = \frac{1}{2}$.  
(e) the parabola $y = x^2$: $x = t, y = t^2 \implies \lim_{t\to 0} \left(-\frac{t^3}{t^2 + t^4}\right) = \lim_{t\to 0}\left(-\frac{t}{1 + t^2}\right) = 0$.

---

### GENERAL LIMITS OF FUNCTIONS OF TWO VARIABLES

> **13.2.1 DEFINITION**  
> Let $f$ be a function of two variables defined on an open disk centered at $(x_0, y_0)$, except possibly at $(x_0, y_0)$. We write
> $$\lim_{(x, y)\to(x_0, y_0)} f(x, y) = L \tag{3}$$
> if given any $\epsilon > 0$, there exists $\delta > 0$ such that $|f(x, y) - L| < \epsilon$ whenever $0 < \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta$.

> **13.2.2 THEOREM**  
> (a) If $f(x, y) \to L$ as $(x, y) \to (x_0, y_0)$, then $f(x, y) \to L$ along any smooth curve.  
> (b) If the limit of $f(x, y)$ fails to exist along some smooth curve, or if $f(x, y)$ has different limits along two different smooth curves, then the limit of $f(x, y)$ does not exist as $(x, y) \to (x_0, y_0)$.

#### Example 3
The limit $\lim_{(x, y)\to(0, 0)} -\frac{xy}{x^2 + y^2}$ does not exist because it equals $0$ along the $x$-axis and $-1/2$ along the line $y = x$.

---

### CONTINUITY

> **13.2.3 DEFINITION**  
> A function $f(x, y)$ is **continuous at $(x_0, y_0)$** if $f(x_0, y_0)$ is defined and $\lim_{(x, y)\to(x_0, y_0)} f(x, y) = f(x_0, y_0)$.

> **13.2.4 THEOREM**  
> (a) If $g(x)$ is continuous at $x_0$ and $h(y)$ is continuous at $y_0$, then $f(x, y) = g(x)h(y)$ is continuous at $(x_0, y_0)$.  
> (b) If $h(x, y)$ is continuous at $(x_0, y_0)$ and $g(u)$ is continuous at $u = h(x_0, y_0)$, then $f(x, y) = g(h(x, y))$ is continuous at $(x_0, y_0)$.  
> (c) If $f(x, y)$ is continuous at $(x_0, y_0)$, and if $x(t), y(t)$ are continuous at $t_0$ with $x(t_0) = x_0, y(t_0) = y_0$, then $f(x(t), y(t))$ is continuous at $t_0$.

#### Example 7 (Limits using Polar Coordinates)
Find $\lim_{(x, y)\to(0, 0)} (x^2 + y^2)\ln(x^2 + y^2)$.

**Solution.** Substituting $x = r\cos\theta, y = r\sin\theta, r^2 = x^2 + y^2$, where $r \to 0^+$:
$$\lim_{r\to 0^+} r^2 \ln(r^2) = \lim_{r\to 0^+} \frac{2\ln r}{1/r^2} \overset{\text{L'H}}{=} \lim_{r\to 0^+} \frac{2/r}{-2/r^3} = \lim_{r\to 0^+} (-r^2) = 0$$

---

### QUICK CHECK EXERCISES 13.2

1. Let $f(x, y) = \frac{x^2 - y^2}{x^2 + y^2}$. Limit as $(x, y) \to (0, 0)$ along:  
   (a) $x = 0 \implies -1$  
   (b) $y = 0 \implies 1$  
   (c) $y = x \implies 0$  
   (d) $y = x^2 \implies 1$
2. (a) $\lim_{(x, y)\to(3, 2)} x\cos\pi y = 3\cos(2\pi) = 3$  
   (b) $\lim_{(x, y)\to(0, 1)} e^{x y^2} = e^0 = 1$  
   (c) $\lim_{(x, y)\to(0, 0)} (x^2 + y^2)\sin\left(\frac{1}{x^2 + y^2}\right) = 0$ (by Squeeze Theorem)
3. A function $f(x, y)$ is continuous at $(x_0, y_0)$ provided $f(x_0, y_0)$ exists and provided $f(x, y)$ has limit $\underline{\quad f(x_0, y_0)\quad}$ as $(x, y)$ approaches $\underline{\quad (x_0, y_0)\quad}$.
4. All values of $a$ such that $f(x, y) = \sqrt{x^2 - a y^2 + 1}$ is continuous everywhere: **Answer:** $a \le 0$.

---

### EXERCISE SET 13.2

**1–6 Use limit laws and continuity properties to evaluate the limit:**
1. $\lim_{(x, y)\to(1, 3)} (4x y^2 - x) = 4(1)(9) - 1 = 35$
2. $\lim_{(x, y)\to(0, 0)} \frac{4x - y}{\sin y - 1} = \frac{0 - 0}{0 - 1} = 0$
3. $\lim_{(x, y)\to(-1, 2)} \frac{x y^3}{x + y} = \frac{(-1)(8)}{-1 + 2} = -8$
4. $\lim_{(x, y)\to(1, -3)} e^{2x - y^2} = e^{2(1) - 9} = e^{-7}$
5. $\lim_{(x, y)\to(0, 0)} \ln(1 + x^2 y^3) = \ln(1 + 0) = 0$
6. $\lim_{(x, y)\to(4, -2)} x\sqrt[3]{y^3 + 2x} = 4\sqrt[3]{-8 + 8} = 0$

**7–8 Show limit does not exist along coordinate axes:**
7. (a) $\lim_{(x, y)\to(0, 0)} \frac{3}{x^2 + 2y^2} = +\infty$ (does not exist).  
   (b) Along $y = 0$: $\lim_{x\to 0} \frac{x}{2x^2} = \lim_{x\to 0} \frac{1}{2x}$ (DNE); along $x = 0$: $\lim_{y\to 0} \frac{y}{y^2} = \lim_{y\to 0} \frac{1}{y}$ (DNE).
8. (a) Along $y = 0$: $\lim_{x\to 0} \frac{x}{x^2} = \lim_{x\to 0} \frac{1}{x}$ (DNE).  
   (b) $\lim_{(x, y)\to(0, 0)} \frac{\cos xy}{x^2 + y^2} = +\infty$ (DNE).

**9–12 Evaluate limits using substitution $z = x^2 + y^2$:**
9. $\lim_{z\to 0^+} \frac{\sin z}{z} = 1$
10. $\lim_{z\to 0^+} \frac{1 - \cos z}{z} = 0$
11. $\lim_{z\to 0^+} e^{-1/z} = 0$
12. $\lim_{z\to 0^+} \frac{e^{-1/\sqrt{z}}}{\sqrt{z}} = \lim_{u\to\infty} \frac{u}{e^u} = 0$

**13–22 Determine whether limit exists; if so, find value:**
13. $\lim_{(x, y)\to(0, 0)} \frac{x^4 - y^4}{x^2 + y^2} = \lim_{(x, y)\to(0, 0)} (x^2 - y^2) = 0$
14. $\lim_{(x, y)\to(0, 0)} \frac{x^4 - 16y^4}{x^2 + 4y^2} = \lim_{(x, y)\to(0, 0)} (x^2 - 4y^2) = 0$
15. $\lim_{(x, y)\to(0, 0)} \frac{xy}{3x^2 + 2y^2}$: Along $y = kx$, limit is $\frac{k}{3 + 2k^2}$ (depends on $k \implies$ DNE).
16. $\lim_{(x, y)\to(0, 0)} \frac{1 - x^2 - y^2}{x^2 + y^2} = +\infty \implies$ DNE.
17. $\lim_{(x, y, z)\to(2, -1, 2)} \frac{x z^2}{\sqrt{x^2 + y^2 + z^2}} = \frac{2(4)}{\sqrt{4 + 1 + 4}} = \frac{8}{3}$
18. $\lim_{(x, y, z)\to(2, 0, -1)} \ln(2x + y - z) = \ln(4 + 0 - (-1)) = \ln 5$
19. $\lim_{(x, y, z)\to(0, 0, 0)} \frac{\sin(x^2 + y^2 + z^2)}{\sqrt{x^2 + y^2 + z^2}} = \lim_{\rho\to 0^+} \frac{\sin(\rho^2)}{\rho} = \lim_{\rho\to 0^+} \rho \cdot \frac{\sin(\rho^2)}{\rho^2} = 0$
20. $\lim_{\rho\to 0^+} \frac{\sin\rho}{\rho^2} = +\infty \implies$ DNE.
21. $\lim_{\rho\to 0^+} \frac{e^\rho}{\rho} = +\infty \implies$ DNE.
22. $\lim_{\rho\to 0^+} \tan^{-1}(1/\rho^2) = \frac{\pi}{2}$

**23–26 Convert to polar coordinates:**
23. $\lim_{r\to 0^+} r\ln(r^2) = 0$
24. $\lim_{r\to 0^+} r\sin\theta \ln(r^2) = 0$
25. $\lim_{r\to 0^+} \frac{r^4 \cos^2\theta \sin^2\theta}{r} = \lim_{r\to 0^+} r^3 \cos^2\theta \sin^2\theta = 0$
26. $\lim_{(x, y)\to(0, 0)} \frac{xy}{\sqrt{x^2 + 2y^2}} = \lim_{r\to 0^+} \frac{r^2 \cos\theta\sin\theta}{r\sqrt{\cos^2\theta + 2\sin^2\theta}} = 0$

**27–28 Convert to spherical coordinates:**
27. $\lim_{\rho\to 0^+} \frac{\rho^3 \sin^2\phi\cos\phi\sin\theta\cos\theta}{\rho^2} = \lim_{\rho\to 0^+} \rho (\sin^2\phi\cos\phi\sin\theta\cos\theta) = 0$
28. $\lim_{(x, y, z)\to(0, 0, 0)} \frac{\sin x \sin y}{\sqrt{x^2 + 2y^2 + 3z^2}} = 0$ (bounded by $|\sin x| \le |x|$).

**29–32 True–False:**
29. **True.** By definition of an open set.
30. **False.** Limit must be the same along all paths, not just coordinate axes.
31. **False.** (Counterexample: $f = 1$ on rational points, $-1$ on irrational points; $g = -f$).
32. **True.** $\lim_{(x, y)\to(0, 0)} \frac{x^2 + y^2}{f(x^2 + y^2)} = \frac{0}{L} = 0$ since $L \ne 0$.

**33–40 Focus on Concepts & Removable Discontinuities:**
33. (a) No limit, since the graph shows different heights approaching $(0, 0)$.  
    (b) Along $y = mx$: $\lim_{x\to 0} \frac{m x^3}{x^4 + m^2 x^2} = \lim_{x\to 0} \frac{mx}{x^2 + m^2} = 0$. This does not guarantee the limit is 0 for all paths.  
    (c) Along $y = x^2$: $\lim_{x\to 0} \frac{x^4}{2x^4} = 1/2$.  
    (d) No limit exists (consistent with (a)).
34. (a) Along $y = mx \implies \lim_{x\to 0} \frac{m x^4}{2x^6 + m^2 x^2} = 0$; along $y = kx^2 \implies \lim_{x\to 0} \frac{k x^5}{2x^6 + k^2 x^4} = 0$.  
    (b) Along $y = x^3$: $\lim_{x\to 0} \frac{x^6}{3x^6} = 1/3 \ne 0 \implies$ limit does not exist.
35. (a) Along $x = at, y = bt, z = ct$: $\lim_{t\to 0} \frac{abc t^3}{a^2 t^2 + (b^4 + c^4)t^4} = 0$.  
    (b) Along $x = t^2, y = t, z = t$: $\lim_{t\to 0} \frac{t^4}{3t^4} = 1/3 \ne 0 \implies$ limit does not exist.
36. $\lim_{(x, y)\to(0, 1)} \tan^{-1}\left(\frac{x^2 + 1}{x^2 + (y-1)^2}\right) = \tan^{-1}(+\infty) = \pi/2$.
37. $\lim_{(x, y)\to(0, 1)} \tan^{-1}\left(\frac{x^2 - 1}{x^2 + (y-1)^2}\right) = \tan^{-1}(-\infty) = -\pi/2$.
38. Since $\lim_{(x, y)\to(0, 0)} \frac{\sin(x^2 + y^2)}{x^2 + y^2} = 1 = f(0, 0)$, $f$ is continuous at $(0, 0)$.
39. $\lim_{(x, y)\to(0, 0)} \frac{x^2}{x^2 + y^2}$ does not exist $\implies$ not removable.
40. $\lim_{(x, y)\to(0, 0)} (x^2 + 7y^2) = 0 \ne -4 \implies$ removable discontinuity (redefining $f(0, 0) = 0$ makes it continuous).

**41–52 Region of continuity:**
41. $y\ln(1 + x)$: Continuous on $x > -1$.
42. $\sqrt{x - y}$: Continuous on $x \ge y$.
43. $\frac{x^2 y}{\sqrt{25 - x^2 - y^2}}$: Continuous on $x^2 + y^2 < 25$.
44. $\ln(2x - y + 1)$: Continuous on $2x - y + 1 > 0$.
45. $\frac{y}{11x^2 + 3}$: Continuous on all of $\mathbb{R}^2$.
46. $e^{1 - xy}$: Continuous on all of $\mathbb{R}^2$.
47. $\sin^{-1}(xy)$: Continuous on $-1 \le xy \le 1$.
48. $\tan^{-1}(y - x)$: Continuous on all of $\mathbb{R}^2$.
49. $3x^2 e^{yz}\cos(xyz)$: Continuous everywhere in $\mathbb{R}^3$.
50. $\ln(4 - x^2 - y^2 - z^2)$: Continuous on open ball $x^2 + y^2 + z^2 < 4$.
51. $\frac{y+1}{x^2 + z^2 - 1}$: Continuous everywhere except on circular cylinder $x^2 + z^2 = 1$.
52. $\sin\sqrt{x^2 + y^2 + 3z^2}$: Continuous everywhere in $\mathbb{R}^3$.

---

## 13.3 PARTIAL DERIVATIVES

### DEFINITIONS AND BASIC PROPERTIES

> **13.3.1 DEFINITION**  
> If $z = f(x, y)$ and $(x_0, y_0)$ is a point in the domain of $f$, then the **partial derivative of $f$ with respect to $x$ at $(x_0, y_0)$** is:
> $$f_x(x_0, y_0) = \left.\frac{d}{dx}[f(x, y_0)]\right|_{x=x_0} = \lim_{\Delta x\to 0} \frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x} \tag{1}$$
> The **partial derivative of $f$ with respect to $y$ at $(x_0, y_0)$** is:
> $$f_y(x_0, y_0) = \left.\frac{d}{dy}[f(x_0, y)]\right|_{y=y_0} = \lim_{\Delta y\to 0} \frac{f(x_0, y_0 + \Delta y) - f(x_0, y_0)}{\Delta y} \tag{2}$$

#### Example 1 & 2
For $f(x, y) = 2x^3 y^2 + 2y + 4x$:
* $f_x(x, y) = 6x^2 y^2 + 4 \implies f_x(1, 3) = 6(1)(9) + 4 = 58$.
* $f_y(x, y) = 4x^3 y + 2 \implies f_y(1, 3) = 4(1)(3) + 2 = 14$.

---

### HIGHER-ORDER PARTIAL DERIVATIVES

For a function $f(x, y)$, the four second-order partial derivatives are:
$$f_{xx} = \frac{\partial^2 f}{\partial x^2} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right), \quad f_{yy} = \frac{\partial^2 f}{\partial y^2} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right)$$
$$f_{xy} = \frac{\partial^2 f}{\partial y \partial x} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right), \quad f_{yx} = \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)$$

> **13.3.2 THEOREM (Equality of Mixed Partials)**  
> Let $f$ be a function of two variables. If $f_{xy}$ and $f_{yx}$ are continuous on some open disk, then $f_{xy} = f_{yx}$ on that disk.

---

### THE WAVE EQUATION

The one-dimensional wave equation modeling a vibrating string of length $L$ is:
$$\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} \tag{6}$$

#### Example 14
Show that $u(x, t) = \sin(x - ct)$ satisfies the wave equation (6).  
**Solution.** $\frac{\partial^2 u}{\partial x^2} = -\sin(x - ct)$ and $\frac{\partial^2 u}{\partial t^2} = -c^2 \sin(x - ct) = c^2 \frac{\partial^2 u}{\partial x^2}$.

---

### QUICK CHECK EXERCISES 13.3

1. Let $f(x, y) = x\sin xy$. Then $f_x(x, y) = \underline{\;\sin xy + xy\cos xy\;}$ and $f_y(x, y) = \underline{\;x^2 \cos xy\;}$.
2. The slope of $z = xy^2$ in $x$-direction at $(2, 3)$ is $\underline{\;9\;}$, and in $y$-direction is $\underline{\;12\;}$.
3. $V = \frac{1}{3}\pi r^2 h$.  
   (a) Instantaneous rate with respect to $r$: $\frac{\partial V}{\partial r} = \frac{2}{3}\pi rh$.  
   (b) Instantaneous rate with respect to $h$: $\frac{\partial V}{\partial h} = \frac{1}{3}\pi r^2$.
4. Second-order partials of $f(x, y) = x^2 y^3$:  
   $f_{xx} = 2y^3, f_{yy} = 6x^2 y, f_{xy} = f_{yx} = 6xy^2$.

---

### EXERCISE SET 13.3

1. $f(x, y) = 3x^3 y^2$:  
   (a) $f_x = 9x^2 y^2$ (b) $f_y = 6x^3 y$ (c) $f_x(1, y) = 9y^2$ (d) $f_x(x, 1) = 9x^2$  
   (e) $f_y(1, y) = 6y$ (f) $f_y(x, 1) = 6x^3$ (g) $f_x(1, 2) = 36$ (h) $f_y(1, 2) = 12$.
2. $z = e^{2x}\sin y$:  
   (a) $\partial z/\partial x = 2e^{2x}\sin y$ (b) $\partial z/\partial y = e^{2x}\cos y$  
   (c) $\left.\frac{\partial z}{\partial x}\right|_{(0, y)} = 2\sin y$ (d) $\left.\frac{\partial z}{\partial x}\right|_{(x, 0)} = 0$  
   (e) $\left.\frac{\partial z}{\partial y}\right|_{(0, y)} = \cos y$ (f) $\left.\frac{\partial z}{\partial y}\right|_{(x, 0)} = e^{2x}$  
   (g) $\left.\frac{\partial z}{\partial x}\right|_{(\ln 2, 0)} = 0$ (h) $\left.\frac{\partial z}{\partial y}\right|_{(\ln 2, 0)} = 4$.

**3–10 Partial derivatives:**
3. $z = 9x^2 y - 3x^5 y \implies \partial z/\partial x = 18xy - 15x^4 y, \partial z/\partial y = 9x^2 - 3x^5$.
4. $f(x, y) = 10x^2 y^4 - 6xy^2 + 10x^2 \implies f_x = 20xy^4 - 6y^2 + 20x, f_y = 40x^2 y^3 - 12xy$.
5. $z = (x^2 + 5x - 2y)^8 \implies \partial z/\partial x = 8(2x+5)(x^2+5x-2y)^7, \partial z/\partial y = -16(x^2+5x-2y)^7$.
6. $f(x, y) = 1/(xy^2 - x^2 y) \implies f_x = -\frac{y^2 - 2xy}{(xy^2 - x^2 y)^2}, f_y = -\frac{2xy - x^2}{(xy^2 - x^2 y)^2}$.
7. $\frac{\partial}{\partial p}(e^{-7p/q}) = -\frac{7}{q}e^{-7p/q}, \frac{\partial}{\partial q}(e^{-7p/q}) = \frac{7p}{q^2}e^{-7p/q}$.
8. $\frac{\partial}{\partial x}(x e^{\sqrt{15xy}}) = e^{\sqrt{15xy}}\left(1 + \frac{\sqrt{15xy}}{2}\right), \frac{\partial}{\partial y}(x e^{\sqrt{15xy}}) = \frac{x\sqrt{15x}}{2\sqrt{y}}e^{\sqrt{15xy}}$.
9. $z = \sin(5x^3 y + 7xy^2) \implies \partial z/\partial x = (15x^2 y + 7y^2)\cos(5x^3 y + 7xy^2), \partial z/\partial y = (5x^3 + 14xy)\cos(5x^3 y + 7xy^2)$.
10. $f(x, y) = \cos(2xy^2 - 3x^2 y^2) \implies f_x = -(2y^2 - 6xy^2)\sin(2xy^2 - 3x^2 y^2), f_y = -(4xy - 6x^2 y)\sin(2xy^2 - 3x^2 y^2)$.

**11–14 Slopes and rates of change:**
11. $f(x, y) = \sqrt{3x + 2y}$: (a) $f_x(4, 2) = \frac{3}{2\sqrt{16}} = \frac{3}{8}$. (b) $f_y(4, 2) = \frac{2}{2\sqrt{16}} = \frac{1}{4}$.
12. $f(x, y) = x e^{-y} + 5y$: (a) $f_x(3, 0) = e^0 = 1$. (b) $f_y(3, 0) = -3e^0 + 5 = 2$.
13. $z = \sin(y^2 - 4x)$: (a) $\partial z/\partial x(2, 1) = -4\cos(1 - 8) = -4\cos(-7) = -4\cos 7$. (b) $\partial z/\partial y(2, 1) = 2(1)\cos(-7) = 2\cos 7$.
14. $z = (x + y)^{-1}$: (a) $\partial z/\partial x(-2, 4) = -(2)^{-2} = -1/4$. (b) $\partial z/\partial y(-2, 4) = -1/4$.

**15–20 Concepts and Graphs:**
15. From figure: $f_x(1, 2) = \frac{4 - 0}{1 - 2} = -4$, $f_y(1, 2) = \frac{4 - 3}{2 - 0} = \frac{1}{2}$.
16. Since contours increase in value as $x$ increases, $f_x(x_0, y_0) > 0$. As $y$ increases, contour values decrease $\implies f_y(x_0, y_0) < 0$.
17–18. Estimates using baseball range table.
19. Matching $f, f_x, f_y$ by looking at stationary points and slopes of traces.
20. At point $P$: $\partial z/\partial x > 0, \partial^2 z/\partial x^2 < 0, \partial z/\partial y < 0, \partial^2 z/\partial y^2 > 0$.

**21–24 True–False:**
21. **True.** Along $y = 2$, $f$ is constant $\implies f_x(4, 2) = 0$.
22. **True.** In the plane $x = 3$, $z = y^2 \implies \partial z/\partial y = 2y = 2(4) = 8$.
23. **True.** A plane has equation $z = Ax + By + C \implies f_x = A, f_y = B$ are constants.
24. **False.** $f_{xy} = 2y + 2$ and $f_{yx} = 2y$; since $f_{xy} \ne f_{yx}$, no such polynomial exists.

**25–36 Partial derivatives:**
25. $z = 4e^{x^2 y^3} \implies z_x = 8xy^3 e^{x^2 y^3}, z_y = 12x^2 y^2 e^{x^2 y^3}$.
26. $z = \cos(x^5 y^4) \implies z_x = -5x^4 y^4 \sin(x^5 y^4), z_y = -4x^5 y^3 \sin(x^5 y^4)$.
27. $z = x^3 \ln(1 + x y^{-3/5}) \implies z_x = 3x^2 \ln(1 + x y^{-3/5}) + \frac{x^3 y^{-3/5}}{1 + x y^{-3/5}}, z_y = -\frac{3}{5}\frac{x^4 y^{-8/5}}{1 + x y^{-3/5}}$.
28. $z = e^{xy}\sin 4y^2 \implies z_x = y e^{xy}\sin 4y^2, z_y = x e^{xy}\sin 4y^2 + 8y e^{xy}\cos 4y^2$.
29. $z = \frac{xy}{x^2 + y^2} \implies z_x = \frac{y(y^2 - x^2)}{(x^2 + y^2)^2}, z_y = \frac{x(x^2 - y^2)}{(x^2 + y^2)^2}$.
30. $z = \frac{x^2 y^3}{\sqrt{x + y}} \implies z_x = \frac{2xy^3(x+y) - \frac{1}{2}x^2 y^3}{(x+y)^{3/2}} = \frac{x y^3(3x + 4y)}{2(x+y)^{3/2}}, z_y = \frac{x^2 y^2(2x + 5y)}{2(x+y)^{3/2}}$.
31. $f(x, y) = \sqrt{3x^5 y - 7x^3 y} \implies f_x = \frac{15x^4 y - 21x^2 y}{2\sqrt{3x^5 y - 7x^3 y}}, f_y = \frac{3x^5 - 7x^3}{2\sqrt{3x^5 y - 7x^3 y}}$.
32. $f(x, y) = \frac{x+y}{x-y} \implies f_x = -\frac{2y}{(x-y)^2}, f_y = \frac{2x}{(x-y)^2}$.
33. $f(x, y) = y^{-3/2}\tan^{-1}(x/y) \implies f_x = \frac{y^{-1/2}}{x^2 + y^2}, f_y = -\frac{3}{2}y^{-5/2}\tan^{-1}(x/y) - \frac{x y^{-3/2}}{x^2 + y^2}$.
34. $f(x, y) = x^3 e^{-y} + y^3 \sec\sqrt{x} \implies f_x = 3x^2 e^{-y} + \frac{y^3}{2\sqrt{x}}\sec\sqrt{x}\tan\sqrt{x}, f_y = -x^3 e^{-y} + 3y^2 \sec\sqrt{x}$.
35. $f(x, y) = (y^2 \tan x)^{-4/3} \implies f_x = -\frac{4}{3}(y^2\tan x)^{-7/3} y^2 \sec^2 x, f_y = -\frac{8}{3}(y^2\tan x)^{-7/3} y \tan x$.
36. $f(x, y) = \cosh(\sqrt{x})\sinh^2(xy^2) \implies f_x = \frac{\sinh\sqrt{x}}{2\sqrt{x}}\sinh^2(xy^2) + 2y^2\cosh\sqrt{x}\sinh(xy^2)\cosh(xy^2), f_y = 4xy\cosh\sqrt{x}\sinh(xy^2)\cosh(xy^2)$.

**37–52 Three variables and implicit forms:**
37. $f_x(3, 1) = -6, f_y(3, 1) = -21$.
38. $\partial f/\partial x(1, 1) = 3e, \partial f/\partial y(1, 1) = 2e$.
39. $\partial z/\partial x(1, 2) = \frac{1}{\sqrt{17}}, \partial z/\partial y(1, 2) = \frac{8}{\sqrt{17}}$.
40. $\partial w/\partial x(1/2, \pi) = -\pi/2, \partial w/\partial y(1/2, \pi) = -1/8$.
41–52 Evaluations and implicit partial differentiation formulas.

**55–68 Applied problems, tangent lines, and implicit differentiation.**

**69–76 Implicit differentiation for $z(x, y)$ and $w(x, y, z)$.**

**77–80 Leibniz rule / Fundamental Theorem of Calculus:**
77. $f(x, y) = \int_y^x e^{t^2} dt \implies f_x = e^{x^2}, f_y = -e^{y^2}$.
78. $f(x, y) = \int_1^{xy} e^{t^2} dt \implies f_x = y e^{x^2 y^2}, f_y = x e^{x^2 y^2}$.
79. $f_x = 2xy^3 \sin(x^6 y^9), f_y = 3x^2 y^2 \sin(x^6 y^9)$.
80. $f_x = \sin((x-y)^3) - \sin((x+y)^3), f_y = -\sin((x-y)^3) - \sin((x+y)^3)$.

**81–92 Higher-order partials and Equality of Mixed Partials:**
81. $z = \sqrt{x}\cos y \implies z_{xx} = -\frac{1}{4}x^{-3/2}\cos y, z_{yy} = -\sqrt{x}\cos y, z_{xy} = z_{yx} = -\frac{\sin y}{2\sqrt{x}}$.
82. $f_{xx} = 8 + 84x^2 y^5, f_{yy} = 140x^4 y^3, f_{xy} = f_{yx} = 140x^3 y^4$.
83. $f_{xx} = 6\cos(3x^2 + 6y^2) - 36x^2 \sin(3x^2 + 6y^2), f_{yy} = 12\cos(3x^2 + 6y^2) - 144y^2 \sin(3x^2 + 6y^2), f_{xy} = -72xy\sin(3x^2 + 6y^2)$.
84. $f_{xx} = 0, f_{yy} = 4xe^{2y}, f_{xy} = f_{yx} = 2e^{2y}$.
85–92 Confirmation that $f_{xy} = f_{yx}$ for polynomial, trigonometric, exponential, rational, and logarithmic functions.

**101–106 Classical PDEs (Laplace, Heat, Wave, Cauchy–Riemann):**
101. Show $\frac{\partial^2 z}{\partial x^2} + \frac{\partial^2 z}{\partial y^2} = 0$ for (a) $z = x^2 - y^2 + 2xy$, (b) $z = e^x \sin y + e^y \cos x$, (c) $z = \ln(x^2 + y^2) + 2\tan^{-1}(y/x)$.
102. Show $\frac{\partial z}{\partial t} = c^2 \frac{\partial^2 z}{\partial x^2}$ for $z = e^{-t}\sin(x/c)$ and $z = e^{-t}\cos(x/c)$.
103. $u(x, t) = \sin(c\omega t)\sin(\omega x)$ satisfies $\frac{\partial^2 u}{\partial t^2} = -c^2 \omega^2 u$ and $c^2 \frac{\partial^2 u}{\partial x^2} = -c^2 \omega^2 u$.
104. Verify Cauchy–Riemann equations $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$.
105. Proof that $u, v, u+v$ satisfy Laplace's equation if they satisfy Cauchy–Riemann.

**107–121 Functions of $n$ variables, piece-wise limits, and concept problems.**

---

## 13.4 DIFFERENTIABILITY, DIFFERENTIALS, AND LOCAL LINEARITY

### DIFFERENTIABILITY

> **13.4.1 DEFINITION**  
> A function $f(x, y)$ is **differentiable at $(x_0, y_0)$** provided $f_x(x_0, y_0)$ and $f_y(x_0, y_0)$ both exist and
> $$\lim_{(\Delta x, \Delta y)\to(0, 0)} \frac{\Delta f - f_x(x_0, y_0)\Delta x - f_y(x_0, y_0)\Delta y}{\sqrt{(\Delta x)^2 + (\Delta y)^2}} = 0 \tag{4}$$
> where $\Delta f = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0)$.

> **13.4.2 DEFINITION**  
> A function $f(x, y, z)$ is **differentiable at $(x_0, y_0, z_0)$** provided $f_x, f_y, f_z$ exist and
> $$\lim_{(\Delta x, \Delta y, \Delta z)\to(0, 0, 0)} \frac{\Delta f - f_x \Delta x - f_y \Delta y - f_z \Delta z}{\sqrt{(\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2}} = 0 \tag{6}$$

> **13.4.3 THEOREM**  
> If a function is differentiable at a point, then it is continuous at that point.

> **13.4.4 THEOREM**  
> If all first-order partial derivatives of $f$ exist and are continuous at a point, then $f$ is differentiable at that point.

---

### TOTAL DIFFERENTIALS & LOCAL LINEAR APPROXIMATION

* **Total Differential:**
  $$dz = f_x(x, y)\,dx + f_y(x, y)\,dy \tag{10}$$
  $$dw = f_x(x, y, z)\,dx + f_y(x, y, z)\,dy + f_z(x, y, z)\,dz \tag{11}$$
* **Local Linear Approximation:**
  $$L(x, y) = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) \tag{15}$$

---

### QUICK CHECK EXERCISES 13.4

1. (a) $\Delta f \approx \underline{\;f_x(x_0, y_0)\Delta x + f_y(x_0, y_0)\Delta y\;}$  
   (b) The limit is $\underline{\;\lim_{(\Delta x, \Delta y)\to(0, 0)} \frac{\Delta f - f_x(x_0, y_0)\Delta x - f_y(x_0, y_0)\Delta y}{\sqrt{(\Delta x)^2 + (\Delta y)^2}} = 0\;}$.
2. (a) $z = x e^{y^2} \implies dz = e^{y^2} dx + 2xy e^{y^2} dy$.  
   (b) $w = x\sin(yz) \implies dw = \sin(yz) dx + xz\cos(yz) dy + xy\cos(yz) dz$.
3. $L(x, y) = \underline{\;f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)\;}$.
4. $f(0.9, -1.95) \approx 4 + 2(0.9 - 1) - 3(-1.95 - (-2)) = 4 + 2(-0.1) - 3(0.05) = 4 - 0.2 - 0.15 = 3.65$.

---

### EXERCISE SET 13.4

**1–4 Linear approximations from partials:**
1. $f(3.01, 3.98) \approx 5 + 2(0.01) - 1(-0.02) = 5.04$.
2. $f(-0.99, 2.02) \approx 2 + 1(0.01) + 3(0.02) = 2.07$.
3. $f(1.01, 2.02, 3.03) \approx 4 + 1(0.01) + 2(0.02) + 3(0.03) = 4.14$.
4. $f(1.98, 0.99, -1.97) \approx 0 - 1(-0.02) + 1(-0.01) - 2(0.03) = 0.02 - 0.01 - 0.06 = -0.05$.

**9–20 Differentials $dz$ and $dw$:**
9. $dz = 7\,dx - 2\,dy$
10. $dz = y e^{xy}\,dx + x e^{xy}\,dy$
11. $dz = 3x^2 y^2\,dx + 2x^3 y\,dy$
12. $dz = (10xy^5 - 2)\,dx + (25x^2 y^4 + 4)\,dy$
13. $dz = \frac{y}{1 + x^2 y^2}\,dx + \frac{x}{1 + x^2 y^2}\,dy$
14. $dz = -3e^{-3x}\cos 6y\,dx - 6e^{-3x}\sin 6y\,dy$
15. $dw = 8\,dx - 3\,dy + 4\,dz$
16. $dw = yz e^{xyz}\,dx + xz e^{xyz}\,dy + xy e^{xyz}\,dz$
17. $dw = 3x^2 y^2 z\,dx + 2x^3 y z\,dy + x^3 y^2\,dz$
18. $dw = (8xy^3 z^7 - 3y)\,dx + (12x^2 y^2 z^7 - 3x)\,dy + (28x^2 y^3 z^6 + 1)\,dz$
19. $dw = \frac{yz}{1 + x^2 y^2 z^2}\,dx + \frac{xz}{1 + x^2 y^2 z^2}\,dy + \frac{xy}{1 + x^2 y^2 z^2}\,dz$
20. $dw = \frac{1}{2\sqrt{x}}\,dx + \frac{1}{2\sqrt{y}}\,dy + \frac{1}{2\sqrt{z}}\,dz$

**21–26 Approximation of $\Delta f$ by total differential:**
21. $\Delta f \approx (2x + 2y - 4)\Delta x + 2x \Delta y = 2(0.01) + 2(0.04) = 0.10$. Exact $\Delta f = 0.1009$.
22. $df = \frac{1}{3}x^{-2/3}y^{1/2}\Delta x + \frac{1}{2}x^{1/3}y^{-1/2}\Delta y = \frac{1}{4}(-0.22) + \frac{1}{3}(0.03) = -0.045$.
23–26 Total differential applications for two and three variables.

**27–30 True–False:**
27. **False.** Existence of partials does not guarantee differentiability.
28. **False.** Only true if $f$ is continuous at $(x_0, y_0)$.
29. **True.** Continuous partials imply differentiability, which implies continuity.
30. **True.** The graph of $L(x, y)$ is a plane.

**31–68 Applied percentage error problems, pendulum, Ideal Gas Law, resistor networks, and theoretical proofs.**

---

## 13.5 THE CHAIN RULE

### CHAIN RULES FOR ONE INDEPENDENT VARIABLE

> **13.5.1 THEOREM (Chain Rules for Derivatives)**  
> If $x = x(t), y = y(t)$ are differentiable at $t$, and $z = f(x, y)$ is differentiable at $(x(t), y(t))$, then:
> $$\frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt} \tag{5}$$
> If $w = f(x, y, z)$ with $x(t), y(t), z(t)$, then:
> $$\frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt} + \frac{\partial w}{\partial z}\frac{dz}{dt} \tag{6}$$

---

### CHAIN RULES FOR TWO INDEPENDENT VARIABLES

> **13.5.2 THEOREM (Chain Rules for Partial Derivatives)**  
> If $z = f(x, y)$ and $x = x(u, v), y = y(u, v)$, then:
> $$\frac{\partial z}{\partial u} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial u} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial u}, \quad \frac{\partial z}{\partial v} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial v} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial v} \tag{7-8}$$

---

### IMPLICIT DIFFERENTIATION

> **13.5.3 THEOREM**  
> If $f(x, y) = c$ defines $y$ implicitly as a differentiable function of $x$, and $\partial f/\partial y \ne 0$:
> $$\frac{dy}{dx} = -\frac{\partial f/\partial x}{\partial f/\partial y} \tag{14}$$

> **13.5.4 THEOREM**  
> If $f(x, y, z) = c$ defines $z$ implicitly as a differentiable function of $x$ and $y$, and $\partial f/\partial z \ne 0$:
> $$\frac{\partial z}{\partial x} = -\frac{\partial f/\partial x}{\partial f/\partial z}, \quad \frac{\partial z}{\partial y} = -\frac{\partial f/\partial y}{\partial f/\partial z}$$

---

### QUICK CHECK EXERCISES 13.5

1. $\frac{dz}{dt} = y^2 \frac{dx}{dt} + 2xy\frac{dy}{dt} = (1)(-2) + 2(1)(-1)(3) = -2 - 6 = \underline{\;-8\;}$.
2. Tangent slope $= \frac{dy}{dx} = -\frac{f_x}{f_y} = -\frac{3}{-1} = \underline{\;3\;}$.
3. $\frac{dA}{dt} = w\frac{dl}{dt} + l\frac{dw}{dt} = 2(3) + 5(4) = 6 + 20 = \underline{\;26\text{ ft}^2/\text{s}\;}$.
4. $\frac{\partial z}{\partial u} = \frac{1}{y}\frac{\partial x}{\partial u} - \frac{x}{y^2}\frac{\partial y}{\partial u} = 1(4) - 3(1) = \underline{\;1\;}$; $\frac{\partial z}{\partial v} = \frac{1}{1}(-2) - 3(-1) = \underline{\;1\;}$.

---

### EXERCISE SET 13.5

**1–10 Chain Rule evaluations:**
1. $z = 3x^2 y^3, x = t^4, y = t^2 \implies \frac{dz}{dt} = 6xy^3(4t^3) + 9x^2 y^2(2t) = 6(t^4)(t^6)(4t^3) + 9(t^8)(t^4)(2t) = 42t^{13}$.
2. $z = \ln(2x^2 + y), x = \sqrt{t}, y = t^{2/3} \implies \frac{dz}{dt} = \frac{4x(1/(2\sqrt{t})) + \frac{2}{3}t^{-1/3}}{2x^2 + y} = \frac{2 + \frac{2}{3}t^{-1/3}}{2t + t^{2/3}}$.
3. $z = 3\cos x - \sin xy, x = 1/t, y = 3t \implies xy = 3 \implies \frac{dz}{dt} = \frac{3}{t^2}\sin(1/t)$.
4. $z = \sqrt{1 + x - 2xy^4}, x = \ln t, y = t \implies \frac{dz}{dt} = \frac{1/t - 2t^4(1/t) - 8(\ln t)t^3}{2\sqrt{1 + \ln t - 2t^4\ln t}}$.
5. $z = e^{1 - xy}, x = t^{1/3}, y = t^3 \implies xy = t^{10/3} \implies \frac{dz}{dt} = -\frac{10}{3}t^{7/3}e^{1 - t^{10/3}}$.
6. $z = \cosh^2 xy, x = t/2, y = e^t \implies \frac{dz}{dt} = 2\cosh(xy)\sinh(xy)\left(\frac{1}{2}e^t + \frac{t}{2}e^t\right) = \frac{1}{2}(1+t)e^t \sinh(t e^t)$.
7. $w = 5x^2 y^3 z^4, x = t^2, y = t^3, z = t^5 \implies w = 5t^{33} \implies \frac{dw}{dt} = 165 t^{32}$.
8. $w = \ln(3x^2 - 2y + 4z^3), x = t^{1/2}, y = t^{2/3}, z = t^{-2} \implies \frac{dw}{dt} = \frac{3 - \frac{4}{3}t^{-1/3} - 24t^{-7}}{3t - 2t^{2/3} + 4t^{-6}}$.
9. $w = 5\cos xy - \sin xz, x = 1/t, y = t, z = t^3 \implies w = 5\cos 1 - \sin(t^2) \implies \frac{dw}{dt} = -2t\cos(t^2)$.
10. $w = \sqrt{1 + x - 2yz^4 x}, x = \ln t, y = t, z = 4t$.

**11–36 Focus on Concepts, multivariable chain rule, polar/spherical coordinate conversions.**

**37–40 True–False:**
37. **False.** $\partial z$ and $\partial x$ do not have independent existence as standard ratios.
38. **True.** General chain rule for $n$ variables.
39. **False.** Second derivative involves product rule and second-order partial terms.
40. **True.** Along $y = x$, $f(t, t) = c \implies f_x(t, t) + f_y(t, t) = 0 \implies f_y(t, t) = -f_x(t, t)$.

**41–71 Implicit differentiation, wave equations, and theoretical derivations (Mean Value Theorem in 2D).**

---

## 13.6 DIRECTIONAL DERIVATIVES AND GRADIENTS

### DIRECTIONAL DERIVATIVES & THE GRADIENT

> **13.6.1 DEFINITION**  
> If $f(x, y)$ is a function of $x$ and $y$, and $\mathbf{u} = u_1\mathbf{i} + u_2\mathbf{j}$ is a unit vector, the **directional derivative of $f$ in the direction of $\mathbf{u}$ at $(x_0, y_0)$** is:
> $$D_{\mathbf{u}}f(x_0, y_0) = \left.\frac{d}{ds}[f(x_0 + s u_1, y_0 + s u_2)]\right|_{s=0} \tag{2}$$

> **13.6.4 DEFINITION**  
> The **gradient of $f$** is defined by:
> $$\nabla f(x, y) = f_x(x, y)\mathbf{i} + f_y(x, y)\mathbf{j} \tag{8}$$
> $$\nabla f(x, y, z) = f_x(x, y, z)\mathbf{i} + f_y(x, y, z)\mathbf{j} + f_z(x, y, z)\mathbf{k} \tag{9}$$

> **13.6.3 THEOREM**  
> $$D_{\mathbf{u}}f(x_0, y_0) = \nabla f(x_0, y_0) \cdot \mathbf{u} \tag{10}$$

> **13.6.5 THEOREM (Properties of Gradient)**  
> (a) If $\nabla f = \mathbf{0}$, all directional derivatives are zero.  
> (b) Maximum rate of increase occurs in the direction of $\nabla f$, with maximum value $\|\nabla f\|$.  
> (c) Maximum rate of decrease occurs in the direction of $-\nabla f$, with minimum value $-\|\nabla f\|$.

> **13.6.6 THEOREM**  
> $\nabla f(x_0, y_0)$ is normal to the level curve $f(x, y) = c$ passing through $(x_0, y_0)$.

---

### QUICK CHECK EXERCISES 13.6

1. $\nabla f(1, 1, 1)$ for $f(x, y, z) = x y^2 z^3$: $\nabla f = \langle y^2 z^3, 2xyz^3, 3xy^2 z^2 \rangle \implies \underline{\;\langle 1, 2, 3 \rangle\;}$.
2. $D_{\mathbf{u}}f(2, 1) = \left.\frac{d}{ds}(3s e^s)\right|_{s=0} = \left.(3e^s + 3s e^s)\right|_{s=0} = \underline{\;3\;}$.
3. $D_{\mathbf{u}}f(0, 0) = (6\mathbf{i} + 8\mathbf{j}) \cdot \left(\frac{3}{5}\mathbf{i} + \frac{4}{5}\mathbf{j}\right) = \frac{18 + 32}{5} = \underline{\;10\;}$. Normal vector is $\langle 6, 8 \rangle \implies$ tangent slope $= \underline{\;-3/4\;}$.
4. Max value $= \|\langle 2, -2, 1 \rangle\| = \sqrt{4 + 4 + 1} = \underline{\;3\;}$; min value $= \underline{\;-3\;}$.

---

### EXERCISE SET 13.6

**1–8 Find $D_{\mathbf{u}}f$ at $P$:**
1. $f(x, y) = (1 + xy)^{3/2}, P(3, 1), \mathbf{u} = \frac{1}{\sqrt{2}}\mathbf{i} + \frac{1}{\sqrt{2}}\mathbf{j} \implies \nabla f(3, 1) = \langle 3, 9 \rangle \implies D_{\mathbf{u}}f = \frac{3 + 9}{\sqrt{2}} = 6\sqrt{2}$.
2. $f(x, y) = \sin(5x - 3y), P(3, 5), \mathbf{u} = \frac{3}{5}\mathbf{i} - \frac{4}{5}\mathbf{j} \implies \nabla f(3, 5) = \langle 5, -3 \rangle \implies D_{\mathbf{u}}f = \frac{15 + 12}{5} = \frac{27}{5}$.
3. $f(x, y) = \ln(1 + x^2 + y), P(0, 0), \mathbf{u} = -\frac{1}{\sqrt{10}}\mathbf{i} - \frac{3}{\sqrt{10}}\mathbf{j} \implies \nabla f(0, 0) = \langle 0, 1 \rangle \implies D_{\mathbf{u}}f = -\frac{3}{\sqrt{10}}$.
4. $f(x, y) = \frac{cx + dy}{x - y}, P(3, 4), \mathbf{u} = \frac{4}{5}\mathbf{i} + \frac{3}{5}\mathbf{j}$.
5. $f(x, y, z) = 4x^5 y^2 z^3, P(2, -1, 1), \mathbf{u} = \frac{1}{3}\mathbf{i} + \frac{2}{3}\mathbf{j} - \frac{2}{3}\mathbf{k} \implies \nabla f(2, -1, 1) = \langle 160, -64, 96 \rangle \implies D_{\mathbf{u}}f = \frac{160 - 128 - 192}{3} = -\frac{160}{3}$.
6–8 Directional derivatives for three-variable functions.

**9–18 Directional derivatives in the direction of vector $\mathbf{a}$ (normalize $\mathbf{u} = \mathbf{a}/\|\mathbf{a}\|$):**
9. $f(x, y) = 4x^3 y^2, P(2, 1), \mathbf{a} = 4\mathbf{i} - 3\mathbf{j} \implies \mathbf{u} = \frac{4}{5}\mathbf{i} - \frac{3}{5}\mathbf{j}, \nabla f(2, 1) = \langle 48, 32 \rangle \implies D_{\mathbf{u}}f = \frac{192 - 96}{5} = \frac{96}{5}$.
10. $f(x, y) = 9x^3 - 2y^3, P(1, 0), \mathbf{a} = \mathbf{i} - \mathbf{j} \implies D_{\mathbf{u}}f = \frac{27}{\sqrt{2}}$.
11–18 Calculations for remaining functions.

**19–22 Angle with positive $x$-axis:**
19. $f(x, y) = \sqrt{xy}, P(1, 4), \theta = \pi/3 \implies \mathbf{u} = \langle 1/2, \sqrt{3}/2 \rangle, \nabla f(1, 4) = \langle 1, 1/4 \rangle \implies D_{\mathbf{u}}f = \frac{1}{2} + \frac{\sqrt{3}}{8}$.
20. $\theta = \pi/2 \implies \mathbf{u} = \mathbf{j}, \nabla f(-1, -2) = \langle -4/9, 2/9 \rangle \implies D_{\mathbf{u}}f = 2/9$.
21–22 Trigonometric/hyperbolic evaluations.

**23–28 Directions between points and along axes.**

**29–32 Focus on Concepts:**
29. System of equations for $\nabla f(1, 2) \cdot \mathbf{u} = -5$ and $\nabla f(1, 2) \cdot \mathbf{v} = 10 \implies f_x(1, 2) = 5, f_y(1, 2) = 10$.
30. Direction from $(-5, 1)$ to $(-4, 3)$ is $\mathbf{a} = \langle 1, 2 \rangle \implies \mathbf{u} = \frac{1}{\sqrt{5}}\langle 1, 2 \rangle \implies D_{\mathbf{u}}f = \frac{-3 + 4}{\sqrt{5}} = \frac{1}{\sqrt{5}}$.
31–32 Gradient direction perpendicular to level curves and magnitude inversely proportional to spacing.

**33–46 Gradients:**
33. $\nabla z = \langle -7y\cos(7y^2 - 7xy), (14y - 7x)\cos(7y^2 - 7xy) \rangle$.
34. $\nabla z = \langle \frac{42}{y}\cos(6x/y), -\frac{42x}{y^2}\cos(6x/y) \rangle$.
35. $\nabla z = \langle -\frac{84y}{(6x-7y)^2}, \frac{84x}{(6x-7y)^2} \rangle$.
36. $\nabla z = \langle \frac{48y e^{3y}}{(x+8y)^2}, \frac{6x(3x+24y-8)e^{3y}}{(x+8y)^2} \rangle$.
37. $\nabla w = \langle -9x^8, -3y^2, 12z^{11} \rangle$.
38. $\nabla w = \langle e^{8y}\sin 6z, 8x e^{8y}\sin 6z, 6x e^{8y}\cos 6z \rangle$.
39. $\nabla w = \frac{x\mathbf{i} + y\mathbf{j} + z\mathbf{k}}{x^2 + y^2 + z^2}$.
40. $\nabla w = \langle -5e^{-5x}\sec(x^2 yz) + 2xyz e^{-5x}\sec(x^2 yz)\tan(x^2 yz), x^2 z e^{-5x}\sec(x^2 yz)\tan(x^2 yz), x^2 y e^{-5x}\sec(x^2 yz)\tan(x^2 yz) \rangle$.

**47–70 Level curves, normal unit vectors, steepest ascent/descent, True-False:**
47–50 Sketch level curves and draw gradient vector perpendicular to tangent.
51. $\nabla f(1, -2) = \langle -16, 4 \rangle \implies \mathbf{u} = \pm \frac{\langle -4, 1 \rangle}{\sqrt{17}}$.
52. $\nabla f(2, -3) = \langle -33, 10 \rangle \implies \mathbf{u} = \pm \frac{\langle -33, 10 \rangle}{\sqrt{1189}}$.
53–60 Directions of most rapid increase: $\mathbf{u} = \frac{\nabla f}{\|\nabla f\|}$, rate $= \|\nabla f\|$.
61–66 Directions of most rapid decrease: $\mathbf{u} = -\frac{\nabla f}{\|\nabla f\|}$, rate $= -\|\nabla f\|$.
67. **False.** Directional derivative is only defined for unit vectors.
68. **True.** Gradient is perpendicular to tangent line $y = 0$ at origin.
69. **True.**
70. **False.** Function may increase initially and then decrease along the ray.

**71–97 Applied heat-seeking trajectories, electric potential, gradient identities, and vector calculus proofs.**

---

## 13.7 TANGENT PLANES AND NORMAL VECTORS

### TANGENT PLANES TO LEVEL SURFACES $F(x, y, z) = c$

> **13.7.1 DEFINITION**  
> If $F(x, y, z) = c$ is a level surface with continuous first-order partial derivatives and $\nabla F(x_0, y_0, z_0) \ne \mathbf{0}$, then $\mathbf{n} = \nabla F(x_0, y_0, z_0)$ is a normal vector, and the **tangent plane** at $P_0(x_0, y_0, z_0)$ is:
> $$F_x(x_0, y_0, z_0)(x - x_0) + F_y(x_0, y_0, z_0)(y - y_0) + F_z(x_0, y_0, z_0)(z - z_0) = 0 \tag{3}$$
> The **normal line** is:
> $$x = x_0 + F_x(x_0, y_0, z_0)t, \quad y = y_0 + F_y(x_0, y_0, z_0)t, \quad z = z_0 + F_z(x_0, y_0, z_0)t \tag{4}$$

> **13.7.2 THEOREM (Tangent Plane to $z = f(x, y)$)**  
> $$z = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) \tag{5}$$

---

### QUICK CHECK EXERCISES 13.7

1. Tangent plane: $2(x - 1) + 1(y - 0) + 1(z + 1) = 0 \implies \underline{\;2(x - 1) + y + (z + 1) = 0\;}$.  
   Normal line: $\underline{\;x = 1 + 2t, y = t, z = -1 + t\;}$.
2. Tangent plane: $\underline{\;z = 4 + 2(x - 3) - 3(y - 1)\;}$.  
   Normal line: $\underline{\;x = 3 + 2t, y = 1 - 3t, z = 4 - t\;}$.
3. Tangent plane to $z = x^2 \sqrt{y}$ at $(2, 4, 8)$: $z_x = 2x\sqrt{y} = 8, z_y = \frac{x^2}{2\sqrt{y}} = 1 \implies \underline{\;z = 8 + 8(x - 2) + (y - 4)\;}$.  
   Normal line: $\underline{\;x = 2 + 8t, y = 4 + t, z = 8 - t\;}$.
4. Intersection tangent line: $\mathbf{n}_1 \times \mathbf{n}_2 = \langle 4, 2, 4 \rangle \times \langle 1, 1, 1 \rangle = \langle -2, 0, 2 \rangle \parallel \langle 1, 0, -1 \rangle$.  
   Line: $\underline{\;x = 2 + t, y = 1, z = 2 - t\;}$.

---

### EXERCISE SET 13.7

**1–12 Tangent planes and normal lines:**
1. $x^2 + y^2 + 4z^2 = 12$ at $(2, 2, 1)$: $\nabla F = \langle 2x, 2y, 8z \rangle \implies \mathbf{n} = \langle 4, 4, 8 \rangle \parallel \langle 1, 1, 2 \rangle$.  
   (a) Tangent plane: $1(x - 2) + 1(y - 2) + 2(z - 1) = 0 \implies x + y + 2z = 6$.  
   (b) Normal line: $x = 2 + t, y = 2 + t, z = 1 + 2t$.  
   (c) Angle with $xy$-plane: $\cos\theta = \frac{2}{\sqrt{6}} \implies \theta = \cos^{-1}(2/\sqrt{6}) \approx 35.3^\circ$.
2. $xz - yz^3 + yz^2 = 2$ at $(2, -1, 1)$: $\nabla F = \langle z, -z^3 + z^2, x - 3yz^2 + 2yz \rangle \implies \mathbf{n} = \langle 1, 0, 3 \rangle$.  
   (a) Tangent plane: $1(x - 2) + 0(y + 1) + 3(z - 1) = 0 \implies x + 3z = 5$.  
   (b) Normal line: $x = 2 + t, y = -1, z = 1 + 3t$.  
   (c) Angle: $\cos\theta = \frac{3}{\sqrt{10}} \implies \theta = \cos^{-1}(3/\sqrt{10}) \approx 18.4^\circ$.
3. $x^2 + y^2 + z^2 = 25$ at $(-3, 0, 4) \implies -3x + 4z = 25$; normal line: $x = -3 - 3t, y = 0, z = 4 + 4t$.
4. $x^2 y - 4z^2 = -7$ at $(-3, 1, -2) \implies -6(x + 3) + 9(y - 1) + 16(z + 2) = 0 \implies -6x + 9y + 16z = -5$.
5. $x^2 - xyz = 56$ at $(-4, 5, 2) \implies -18(x + 4) + 8(y - 5) + 20(z - 2) = 0 \implies -9x + 4y + 10z = 76$.
6. $z = x^2 + y^2$ at $(2, -3, 13) \implies z = 13 + 4(x - 2) - 6(y + 3) \implies 4x - 6y - z = 13$.
7. $z = 4x^3 y^2 + 2y$ at $(1, -2, 12) \implies z = 12 + 48(x - 1) - 14(y + 2) \implies 48x - 14y - z = 64$.
8. $z = \frac{1}{2}x^7 y^{-2}$ at $(2, 4, 4) \implies 14x - 2y - z = 16$.
9. $z = x e^{-y}$ at $(1, 0, 1) \implies x - y - z = 0$.
10. $z = \ln\sqrt{x^2 + y^2}$ at $(-1, 0, 0) \implies -x - z = 1 \implies x + z = -1$.
11. $z = e^{3y}\sin 3x$ at $(\pi/6, 0, 1) \implies 3y - z = -1$.
12. $z = x^{1/2} + y^{1/2}$ at $(4, 9, 5) \implies \frac{1}{4}x + \frac{1}{6}y - z = -\frac{5}{2} \implies 3x + 2y - 12z = -30$.

**13–41 Focus on Concepts, parallel/orthogonal tangent planes, line intersections, and geometric proofs.**

---

## 13.8 MAXIMA AND MINIMA OF FUNCTIONS OF TWO VARIABLES

### DEFINITIONS AND EXTREME VALUE THEOREM

> **13.8.1 & 13.8.2 DEFINITIONS**  
> A function $f(x, y)$ has a **relative maximum (minimum)** at $(x_0, y_0)$ if $f(x_0, y_0) \ge f(x, y)$ ($f(x_0, y_0) \le f(x, y)$) for all $(x, y)$ in some open disk centered at $(x_0, y_0)$.

> **13.8.3 THEOREM (Extreme-Value Theorem)**  
> If $f(x, y)$ is continuous on a closed and bounded set $R$, then $f$ attains both an absolute maximum and an absolute minimum on $R$.

> **13.8.5 DEFINITION**  
> A point $(x_0, y_0)$ is a **critical point** of $f(x, y)$ if $f_x(x_0, y_0) = 0$ and $f_y(x_0, y_0) = 0$, or if either partial derivative fails to exist.

---

### THE SECOND PARTIALS TEST

> **13.8.6 THEOREM (The Second Partials Test)**  
> Let $(x_0, y_0)$ be a critical point of $f(x, y)$ with continuous second partials, and let
> $$D = f_{xx}(x_0, y_0)f_{yy}(x_0, y_0) - f_{xy}^2(x_0, y_0)$$
> (a) If $D > 0$ and $f_{xx}(x_0, y_0) > 0$, then $f$ has a **relative minimum** at $(x_0, y_0)$.  
> (b) If $D > 0$ and $f_{xx}(x_0, y_0) < 0$, then $f$ has a **relative maximum** at $(x_0, y_0)$.  
> (c) If $D < 0$, then $f$ has a **saddle point** at $(x_0, y_0)$.  
> (d) If $D = 0$, the test is **inconclusive**.

---

### QUICK CHECK EXERCISES 13.8

1. $f(x, y) = x^3 + xy + y^2 \implies f_x = 3x^2 + y = 0, f_y = x + 2y = 0 \implies x = -2y \implies 12y^2 + y = 0 \implies y = 0$ or $y = -1/12$.  
   Critical points: $\underline{\;(0, 0)\text{ and }\left(\frac{1}{6}, -\frac{1}{12}\right)\;}$.
2. (a) $D = (2)(2) - 4 = 0 \implies \underline{\;\text{no information}\;}$.  
   (b) $D = (-2)(2) - 4 = -8 < 0 \implies \underline{\;\text{saddle point at }(0, 0)\;}$.  
   (c) $D = (3)(2) - 4 = 2 > 0, f_{xx} = 3 > 0 \implies \underline{\;\text{relative minimum at }(0, 0)\;}$.  
   (d) $D = (-3)(-2) - 4 = 2 > 0, f_{xx} = -3 < 0 \implies \underline{\;\text{relative maximum at }(0, 0)\;}$.
3. $f(x, y) = x^3 - 3xy + y^3 \implies f_x = 3x^2 - 3y = 0, f_y = -3x + 3y^2 = 0 \implies y = x^2, x^4 - x = 0 \implies (0, 0), (1, 1)$.  
   $f_{xx} = 6x, f_{yy} = 6y, f_{xy} = -3 \implies D = 36xy - 9$.  
   (a) At $(0, 0)$: $D = -9 < 0 \implies \underline{\;\text{saddle point at }(0, 0)\;}$.  
   (b) At $(-1, -1)$: not a critical point $\implies \underline{\;\text{no information}\;}$.  
   (c) At $(1, 1)$: $D = 27 > 0, f_{xx} = 6 > 0 \implies \underline{\;\text{relative minimum at }(1, 1)\;}$.
4. $S = 2xy + 2xz + 2yz = 2 \implies z(2x + 2y) = 2 - 2xy \implies z = \frac{1 - xy}{x + y}$.  
   $V = xyz = \underline{\;\frac{xy(1 - xy)}{x + y}\;}$.

---

### EXERCISE SET 13.8

**1–4 Extrema by inspection & completing squares:**
1. (a) Absolute minimum $= 0$ at $(2, -1)$; no absolute maximum.  
   (b) Absolute maximum $= 1$ at $(0, 0)$; no absolute minimum.  
   (c) No absolute extrema.
2. (a) Absolute maximum $= 1$ at $(-1, 5)$; no absolute minimum.  
   (b) No absolute extrema.  
   (c) Saddle point at $(0, 0)$; no absolute extrema.
3. $f(x, y) = (x - 3)^2 + (y + 2)^2 \implies$ Absolute minimum $= 0$ at $(3, -2)$.
4. $f(x, y) = 4 - (x + 1)^2 - 2(y - 1)^2 \implies$ Absolute maximum $= 4$ at $(-1, 1)$.

**9–20 Relative extrema and saddle points:**
9. $f(x, y) = y^2 + xy + 3y + 2x + 3 \implies f_x = y + 2 = 0 \implies y = -2; f_y = 2y + x + 3 = 0 \implies x = 1$.  
   $f_{xx} = 0, f_{yy} = 2, f_{xy} = 1 \implies D = 0 - 1 = -1 < 0 \implies$ Saddle point at $(1, -2)$.
10. $f_x = 2x + y - 2 = 0, f_y = x - 2 = 0 \implies x = 2, y = -2$. $D = -1 < 0 \implies$ Saddle point at $(2, -2)$.
11. $f_x = 2x + y - 3 = 0, f_y = x + 2y = 0 \implies x = 2, y = -1$. $D = (2)(2) - 1 = 3 > 0, f_{xx} = 2 > 0 \implies$ Relative minimum at $(2, -1)$.
12. $f_x = y - 3x^2 = 0, f_y = x - 2y = 0 \implies x = 2y \implies y = 12y^2 \implies (0, 0)$ and $(1/6, 1/12)$.  
    At $(0, 0)$: $D = -1 < 0 \implies$ Saddle point.  
    At $(1/6, 1/12)$: $D = (-1)(-2) - 1 = 1 > 0, f_{xx} = -1 < 0 \implies$ Relative maximum at $(1/6, 1/12)$.
13. $f(x, y) = x^2 + y^2 + \frac{2}{xy} \implies$ Relative minima at $(1, 1)$ and $(-1, -1)$ with value $4$.
14. $f_x = e^y = 0$ has no solution $\implies$ No relative extrema or saddle points.
15. $f_x = 2x = 0 \implies x = 0; f_y = 1 - e^y = 0 \implies y = 0$. $D = 2(0 - e^0) = 2 > 0, f_{xx} = 2 > 0 \implies$ Relative minimum at $(0, 0)$.
16. Relative minimum at $(1, 2)$ with value $6$.
17. No relative extrema (saddle points along grid).
18. Saddle points at $(n\pi, 0)$.
19. Relative maximum at $(-1, 0)$ with value $e^1 = e$.
20. Relative minimum at $(a, b)$ if $ab > 0$.

**23–26 True–False:**
23. **False.** Continuous function on closed disk must have absolute extrema, but they may occur on the boundary where partial derivatives in $\mathbb{R}^2$ do not vanish.
24. **False.** A function can have infinitely many critical points (e.g., $f(x, y) = \sin(x^2 + y^2)$).
25. **False.** Must also know that $D > 0$ and $f_{xx} \ne 0$.
26. **True.** Saddle point with $f(x_0, y_0) = 0$ branches into both positive and negative directions.

**31–36 Absolute extrema on closed and bounded sets:**
31. $f(x, y) = xy - x - 3y$ on triangle $(0, 0), (0, 4), (5, 0) \implies$ Absolute maximum $= 0$ at $(0, 0)$, Absolute minimum $= -12$ at $(0, 4)$.
32. $f(x, y) = xy - 2x$ on triangle $(0, 0), (0, 4), (4, 0) \implies$ Absolute maximum $= 0$, Absolute minimum $= -8$ at $(4, 0)$.
33–36 Absolute extrema on squares, rectangles, and disks.

**37–48 Applied Optimization:**
37. Numbers $x, y, z > 0$ with $x + y + z = 48$ maximizing $xyz \implies x = y = z = 16$.
38. Numbers $x + y + z = 27$ minimizing $x^2 + y^2 + z^2 \implies x = y = z = 9$.
39. Point on $x + y + z = 5$ in first octant maximizing $x y^2 z^2 \implies x = 1, y = 2, z = 2$.
40. Points on $x^2 - yz = 5$ closest to origin: $(0, \sqrt{5}, -\sqrt{5})$ and $(0, -\sqrt{5}, \sqrt{5})$.
41. Inscribed box in sphere of radius $a$: dimensions $\frac{2a}{\sqrt{3}} \times \frac{2a}{\sqrt{3}} \times \frac{2a}{\sqrt{3}}$, maximum volume $= \frac{8a^3}{3\sqrt{3}}$.
42. Airline suitcase $x + y + z \le 129 \implies x = y = z = 43\text{ cm}$.
43. Open box of volume $V$: dimensions $x = y = (2V)^{1/3}, z = \frac{1}{2}(2V)^{1/3}$.
48. Sheet metal width $27$: $x = 9\text{ in}, \phi = 60^\circ$.

**49–57 Least Squares Regression line formulas and applications:**
$$m = \frac{n\sum x_i y_i - \sum x_i \sum y_i}{n\sum x_i^2 - (\sum x_i)^2}, \quad b = \frac{1}{n}\left(\sum y_i - m\sum x_i\right)$$

---

## 13.9 LAGRANGE MULTIPLIERS

### CONSTRAINED EXTREMUM PRINCIPLES

> **13.9.3 THEOREM (Two Variables and One Constraint)**  
> Let $f$ and $g$ have continuous first partial derivatives on an open set containing the constraint curve $g(x, y) = 0$, with $\nabla g \ne \mathbf{0}$. If $f$ has a constrained relative extremum, it occurs at $(x_0, y_0)$ where:
> $$\nabla f(x_0, y_0) = \lambda \nabla g(x_0, y_0) \tag{4}$$

> **13.9.4 THEOREM (Three Variables and One Constraint)**  
> For $f(x, y, z)$ subject to $g(x, y, z) = 0$ with $\nabla g \ne \mathbf{0}$:
> $$\nabla f(x_0, y_0, z_0) = \lambda \nabla g(x_0, y_0, z_0)$$

---

### QUICK CHECK EXERCISES 13.9

1. (a) They are the same line. (b) They are the same plane.
2. Max of $x + y$ subject to $x^2 + y^2 = 1$: $\nabla f = \langle 1, 1 \rangle, \nabla g = \langle 2x, 2y \rangle \implies x = y = 1/\sqrt{2} \implies \underline{\;\sqrt{2}\;}$.
3. Max of $x + y + z$ subject to $x^2 + y^2 + z^2 = 1$: $x = y = z = 1/\sqrt{3} \implies \underline{\;\sqrt{3}\;}$.
4. Max and min of $2x + 3y$ on $x + y = 1, x \ge 0, y \ge 0$: Max is $\underline{\;3\;}$ at $(0, 1)$, Min is $\underline{\;2\;}$ at $(1, 0)$.

---

### EXERCISE SET 13.9

**1–4 Focus on Concepts:**
1. (a) Level curve $xy = 4$ is tangent to $x + y = 4$ at $(2, 2) \implies$ maximum value is $4$.  
   (b) The line $x + y = 4$ extends to regions where $xy \to -\infty$, so there is no minimum.  
   (c) $\nabla f = \langle y, x \rangle = \lambda \langle 1, 1 \rangle \implies y = x = 2$.
2. (a) Minimum value $x^2 + y^2 = 25$ at $(3, 4)$ where $3x + 4y = 25$ is tangent to circle.  
   (b) Points on line farther from origin have arbitrarily large $x^2 + y^2$, so no maximum.

**5–12 Maxima and minima using Lagrange multipliers:**
5. $f(x, y) = xy$ subject to $4x^2 + 8y^2 = 16 \implies \nabla f = \langle y, x \rangle = \lambda \langle 8x, 16y \rangle$.  
   Maximum value $= 1$ at $(\sqrt{2}, 1)$ and $(-\sqrt{2}, -1)$; minimum value $= -1$ at $(\sqrt{2}, -1)$ and $(-\sqrt{2}, 1)$.
6. $f(x, y) = x^2 - y^2$ subject to $x^2 + y^2 = 25 \implies$ Maximum value $= 25$ at $(\pm 5, 0)$; minimum value $= -25$ at $(0, \pm 5)$.
7. $f(x, y) = 4x^3 + y^2$ subject to $2x^2 + y^2 = 1 \implies$ Maximum value $= \sqrt{2}$ at $(1/\sqrt{2}, 0)$; minimum value $= -\sqrt{2}$ at $(-1/\sqrt{2}, 0)$.
8. $f(x, y) = x - 3y - 1$ subject to $x^2 + 3y^2 = 16 \implies$ Maximum value $= 7$ at $(2, -2)$; minimum value $= -9$ at $(-2, 2)$.
9. $f(x, y, z) = 2x + y - 2z$ subject to $x^2 + y^2 + z^2 = 4 \implies$ Maximum value $= 6$ at $(4/3, 2/3, -4/3)$; minimum value $= -6$ at $(-4/3, -2/3, 4/3)$.
10. $f(x, y, z) = 3x + 6y + 2z$ subject to $2x^2 + 4y^2 + z^2 = 70 \implies$ Maximum value $= 35$ at $(3, 3, 5)$; minimum value $= -35$ at $(-3, -3, -5)$.
11. $f(x, y, z) = xyz$ subject to $x^2 + y^2 + z^2 = 1 \implies$ Maximum value $= \frac{1}{3\sqrt{3}}$, minimum value $= -\frac{1}{3\sqrt{3}}$.
12. $f(x, y, z) = x^4 + y^4 + z^4$ subject to $x^2 + y^2 + z^2 = 1 \implies$ Maximum value $= 1$ at $(\pm 1, 0, 0), (0, \pm 1, 0), (0, 0, \pm 1)$; minimum value $= 1/3$ at $(\pm 1/\sqrt{3}, \pm 1/\sqrt{3}, \pm 1/\sqrt{3})$.

**13–16 True–False:**
13. **False.** A Lagrange multiplier $\lambda$ is a scalar, not a vector.
14. **False.** Condition is $\nabla f = \lambda \nabla g$.
15. **False.** The advantage of Lagrange multipliers is that solving for variables explicitly is not required.
16. **True.**

**17–24 Applied problems using Lagrange Multipliers:**
17. Closest point on $2x - 4y = 3$ to origin: $(3/10, -3/5)$.
18. Closest point on $y = 2x + 3$ to $(4, 2)$: $(4/5, 23/5)$.
19. Closest point on $x + 2y + z = 1$ to origin: $(1/6, 1/3, 1/6)$.
20. Closest point on $4x + 3y + z = 2$ to $(1, -1, 1)$: $(1 + 4\lambda, -1 + 3\lambda, 1 + \lambda) \implies \lambda = 0 \implies (1, -1, 1)$ lies on plane.
21. Points on $x^2 + y^2 = 45$ closest/farthest to $(1, 2)$: $(3, 6)$ and $(-3, -6)$.
22. Closest points on $xy - z^2 = 1$ to origin: $(1, 1, 0)$ and $(-1, -1, 0)$.
23. Vector in 3-space of length 5 with largest component sum: $\langle \frac{5}{\sqrt{3}}, \frac{5}{\sqrt{3}}, \frac{5}{\sqrt{3}} \rangle$.
24. Highest temp $= 125$, lowest temp $= 0$.

**25–36 Additional exercises and proofs.**

---

## CHAPTER 13 REVIEW EXERCISES

1. Let $f(x, y) = e^x \ln y$. Find:  
   (a) $f(\ln y, e^x) = e^{\ln y} \ln(e^x) = yx = xy$.  
   (b) $f(r + s, rs) = e^{r+s}\ln(rs)$.

2. Sketch domain of $f$:  
   (a) $f(x, y) = \ln(xy - 1) \implies xy > 1$ (region between branches of hyperbola $xy = 1$, dashed boundary).  
   (b) $f(x, y) = (\sin^{-1} x)/e^y \implies -1 \le x \le 1, y \in \mathbb{R}$ (vertical strip between $x = -1$ and $x = 1$, solid boundaries).

3. Level curves of cone $z = \sqrt{x^2 + y^2}$ are circles $x^2 + y^2 = k^2$ spaced linearly with $k$. Level curves of paraboloid $z = x^2 + y^2$ are circles $x^2 + y^2 = k$ with radii $\sqrt{k}$ that get closer together as $k$ increases.

4. (a) For $k > 0$, $a^2 x^2 + a^2 y^2 + z^2 = k$ represents a family of ellipsoids of revolution with circular cross sections parallel to the $xy$-plane.  
   (b) $f(x, y, z) = z - x^2 - y^2$.

5. $f(x, y) = \frac{x^4 - x + y - x^3 y}{x - y} = \frac{x^3(x - y) - (x - y)}{x - y} = x^3 - 1$ for $x \ne y$.  
   (a) $\lim_{(x, y)\to(0, 0)} f(x, y) = -1$.  
   (b) Since $f(0, 0)$ is undefined, $f$ is not continuous at $(0, 0)$.

6. $f(x, y) = \begin{cases} \frac{x^4 - y^4}{x^2 + y^2}, & (x, y) \ne (0, 0) \\ 0, & (x, y) = (0, 0) \end{cases}$  
   (a) $\lim_{(x, y)\to(0, 0)} \frac{(x^2 - y^2)(x^2 + y^2)}{x^2 + y^2} = 0$.  
   (b) Since $\lim f(x, y) = f(0, 0) = 0$, $f$ is continuous at $(0, 0)$.

7. (a) $\partial P/\partial x$ is the marginal profit with respect to standard monitors; $\partial P/\partial y$ is the marginal profit with respect to high-resolution monitors.  
   (b) $\partial T/\partial x$ and $\partial T/\partial y$ are spatial temperature gradients; $\partial T/\partial t$ is the time rate of change of temperature at $(x, y)$.

8. (a) $\frac{\partial z}{\partial x} = \lim_{\Delta x\to 0}\frac{f(x+\Delta x, y) - f(x, y)}{\Delta x}, \frac{\partial z}{\partial y} = \lim_{\Delta y\to 0}\frac{f(x, y+\Delta y) - f(x, y)}{\Delta y}$.  
   (b) Slopes of tangent lines in planes parallel to the $x$- and $y$-axes.  
   (c) Rates of change of $z$ with respect to distance in directions parallel to coordinate axes.

9. $P = 10T/V$:  
   (a) $\frac{\partial P}{\partial T} = \frac{10}{V} = \frac{10}{2.5} = 4 \implies \frac{dP}{dt} = 4(3) = 12\text{ N}/(\text{m}^2\cdot\text{min})$.  
   (b) $\frac{\partial P}{\partial V} = -\frac{10T}{V^2} = -\frac{500}{6.25} = -80 \implies \frac{dP}{dt} = (-80)(-3) = 240\text{ N}/(\text{m}^2\cdot\text{min})$.

10. $z = 5 - 4x^2 - y^2$ at $(1, -2, -3)$:  
    (a) Plane $x = 1 \implies \frac{\partial z}{\partial y} = -2y = 4$.  
    (b) Plane $y = -2 \implies \frac{\partial z}{\partial x} = -8x = -8$.

11–14. Verification of equality of mixed partial derivatives and Laplace equations.

15. $\Delta f = f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0)$ is the exact change in $f$; $df = f_x \Delta x + f_y \Delta y$ is the linear approximation to $\Delta f$.

16. $w = x^2 y - 2xy + y^2 x$:  
    $dw = (2xy - 2y + y^2)dx + (x^2 - 2x + 2xy)dy$. At $(1, 0)$, $dx = 0.1, dy = -0.1 \implies dw = 0(0.1) - 1(-0.1) = 0.1$.  
    Exact $\Delta w = (1.1)^2(-0.1) - 2(1.1)(-0.1) + (-0.1)^2(1.1) = -0.121 + 0.22 + 0.011 = 0.11$.

17. $V = \frac{1}{3}x^2 h \implies dV = \frac{2}{3}xh\,dx + \frac{1}{3}x^2\,dh = \frac{2}{3}(1)(2)(-0.1) + \frac{1}{3}(1)^2(0.2) = -\frac{0.4}{3} + \frac{0.2}{3} = -0.067\text{ m}^3$.

18. $L(x, y) = \sin(\pi/3) + \pi\cos(\pi/3)(x - 1/3) + \frac{1}{3}\cos(\pi/3)(y - \pi) = \frac{\sqrt{3}}{2} + \frac{\pi}{2}(x - 1/3) + \frac{1}{6}(y - \pi)$.

19. $\frac{dz}{dt} = \frac{\partial z}{\partial x}x'(0) + \frac{\partial z}{\partial y}y'(0) \implies 2 = 4(-1/2) + 2 y'(0) \implies 2 = -2 + 2y'(0) \implies y'(0) = 2$.

20. (a) $\frac{dy}{dx} = -\frac{6x - 5y + y\sec^2(xy)}{-5x + x\sec^2(xy)}$.  
    (b) $\frac{dy}{dx} = -\frac{\ln y + \cos(x - y)}{x/y - \cos(x - y)}$.

21. $\frac{d^2 y}{dx^2} = -\frac{f_{xx} f_y^2 - 2f_{xy} f_x f_y + f_{yy} f_x^2}{f_y^3}$.

23. (a) $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$.  
    (b) When $\mathbf{u}$ is orthogonal to $\nabla f$ or $\nabla f = \mathbf{0}$.  
    (c) Maximum in direction of $\nabla f$; minimum in direction of $-\nabla f$.

25. $f(x, y) = y\ln(x + y), P(-3, 5), \mathbf{u} = \frac{3}{5}\mathbf{i} + \frac{4}{5}\mathbf{j} \implies \nabla f(-3, 5) = \langle 5/2, \ln 2 + 5/2 \rangle \implies D_{\mathbf{u}}f = \frac{3}{2} + \frac{4}{5}\ln 2 + 2 = \frac{7}{2} + \frac{4}{5}\ln 2$.

26. $\nabla f(0, 0) = 2\mathbf{i} + \frac{3}{2}\mathbf{j} \implies \|\nabla f\| = 5/2$.  
    (a) $\mathbf{u} = \frac{4}{5}\mathbf{i} + \frac{3}{5}\mathbf{j}$, Max value $= 5/2$.  
    (b) $\mathbf{u} = -\frac{4}{5}\mathbf{i} - \frac{3}{5}\mathbf{j}$, Min value $= -5/2$.

28. (a) $z = x^2 e^{2y}, P_0(1, \ln 2, 4) \implies$ Tangent plane: $8x + 8y - z = 8\ln 2 + 4$.  
    (b) $x^2 y^3 z^4 + xyz = 2, P_0(2, 1, -1) \implies$ Tangent plane: $3x + 4y - 10z = 20$.

30. Normal line to $x^{2/3} + y^{2/3} + z^{2/3} = 1$: tangent plane has intercepts $x_0^{1/3}, y_0^{1/3}, z_0^{1/3}$, and $(x_0^{1/3})^2 + (y_0^{1/3})^2 + (z_0^{1/3})^2 = x_0^{2/3} + y_0^{2/3} + z_0^{2/3} = 1$.

33–36. Classification of critical points.

37–39. Optimization and resistor power network:  
In resistor network, $I_1 R_1 = I_2 R_2 = I_3 R_3 = V \implies I_1 : I_2 : I_3 = \frac{1}{R_1} : \frac{1}{R_2} : \frac{1}{R_3}$.

40–42. Cobb–Douglas production models.

---

## CHAPTER 13 MAKING CONNECTIONS

1. **Polar conversion of derivatives:**  
   Given $x = r\cos\theta, y = r\sin\theta$:
   $$\frac{\partial z}{\partial r} = \frac{\partial z}{\partial x}\cos\theta + \frac{\partial z}{\partial y}\sin\theta \implies r\frac{\partial z}{\partial r} = x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y}$$
   $$\frac{\partial z}{\partial \theta} = \frac{\partial z}{\partial x}(-r\sin\theta) + \frac{\partial z}{\partial y}(r\cos\theta) = -y\frac{\partial z}{\partial x} + x\frac{\partial z}{\partial y}$$

2. **Homogeneous functions of degree $n$:**  
   $f(tx, ty) = t^n f(x, y)$ for $t > 0$.  
   (a) $f(tx, ty) = 3(tx)^2 + (ty)^2 = t^2(3x^2 + y^2) \implies n = 2$.  
   (b) $f(tx, ty) = \sqrt{(tx)^2 + (ty)^2} = t\sqrt{x^2 + y^2} \implies n = 1$.  
   (c) $f(tx, ty) = (tx)^2(ty) - 2(ty)^3 = t^3(x^2 y - 2y^3) \implies n = 3$.  
   (d) $f(tx, ty) = \frac{5}{((tx)^2 + 2(ty)^2)^2} = t^{-4} \frac{5}{(x^2 + 2y^2)^2} \implies n = -4$.

3. **Proof for polar form of homogeneous function:**  
   If $f$ is homogeneous of degree $n$, in polar coordinates $f(r\cos\theta, r\sin\theta) = r^n f(\cos\theta, \sin\theta) = r^n g(\theta)$, where $g(\theta) = f(\cos\theta, \sin\theta)$ is $2\pi$-periodic. Conversely, if $z = r^n g(\theta)$, then $f(tx, ty) = (tr)^n g(\theta) = t^n r^n g(\theta) = t^n f(x, y)$.

4. **Euler's Theorem for Homogeneous Functions:**  
   (a) Let $u = tx, v = ty$. Then $f(u, v) = t^n f(x, y)$. Differentiating both sides with respect to $t$:
   $$\frac{\partial f}{\partial u}\frac{du}{dt} + \frac{\partial f}{\partial v}\frac{dv}{dt} = n t^{n-1} f(x, y) \implies x\frac{\partial f}{\partial u} + y\frac{\partial f}{\partial v} = n t^{n-1} f(x, y)$$
   Setting $t = 1$ yields $u = x, v = y$, so:
   $$x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y} = nf(x, y)$$
   (b) Using $z = r^n g(\theta)$ from Exercise 3:
   $$r\frac{\partial z}{\partial r} = r(n r^{n-1} g(\theta)) = n r^n g(\theta) = n z$$
   Combining with $r\frac{\partial z}{\partial r} = x\frac{\partial z}{\partial x} + y\frac{\partial z}{\partial y}$ from Exercise 1 gives $x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y} = nf(x, y)$.  
   (c) Direct verification confirms $x f_x + y f_y = n f$ for all parts of Exercise 2.

5. **Converse of Euler's Theorem:**  
   Given $x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y} = nf$, convert to polar form using Exercise 1:
   $$r\frac{\partial z}{\partial r} = n z \implies r\frac{\partial z}{\partial r} - nz = 0$$
   Dividing both sides by $r^{n+1}$:
   $$\frac{1}{r^n}\frac{\partial z}{\partial r} - \frac{n}{r^{n+1}}z = 0 \implies \frac{\partial}{\partial r}\left(\frac{z}{r^n}\right) = 0$$
   Integrating with respect to $r$ shows that $\frac{z}{r^n}$ is independent of $r$, hence $\frac{z}{r^n} = g(\theta) \implies z = r^n g(\theta)$. By Exercise 3, $f(x, y)$ is homogeneous of degree $n$.
