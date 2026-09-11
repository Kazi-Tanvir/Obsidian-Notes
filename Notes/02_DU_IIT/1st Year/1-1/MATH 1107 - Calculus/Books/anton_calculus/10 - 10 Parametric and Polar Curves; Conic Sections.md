# CHAPTER 10: PARAMETRIC AND POLAR CURVES; CONIC SECTIONS

> Mathematical curves, such as the spirals in the center of a sunflower, can be described conveniently using ideas developed in this chapter.

In this chapter we will study alternative ways of expressing curves in the plane. We will begin by studying parametric curves: curves described in terms of component functions. This study will include methods for finding tangent lines to parametric curves. We will then introduce polar coordinate systems and discuss methods for finding tangent lines to polar curves, arc length of polar curves, and areas enclosed by polar curves. Our attention will then turn to a review of the basic properties of conic sections: parabolas, ellipses, and hyperbolas. Finally, we will consider conic sections in the context of polar coordinates and discuss some applications in astronomy.

---

## 10.1 PARAMETRIC EQUATIONS; TANGENT LINES AND ARC LENGTH FOR PARAMETRIC CURVES

Graphs of functions must pass the vertical line test, a limitation that excludes curves with self-intersections or even such basic curves as circles. In this section we will study an alternative method for describing curves algebraically that is not subject to the severe restriction of the vertical line test. We will then derive formulas required to find slopes, tangent lines, and arc lengths of these parametric curves. We will conclude with an investigation of a classic parametric curve known as the cycloid.

### PARAMETRIC EQUATIONS

Suppose that a particle moves along a curve $C$ in the $xy$-plane in such a way that its $x$- and $y$-coordinates, as functions of time, are
$$x = f(t), \quad y = g(t)$$
We call these the **parametric equations of motion** for the particle and refer to $C$ as the **trajectory** of the particle or the **graph** of the equations (Figure 10.1.1). The variable $t$ is called the **parameter** for the equations.

#### Example 1
Sketch the trajectory over the time interval $0 \le t \le 10$ of the particle whose parametric equations of motion are
$$x = t - 3 \sin t, \quad y = 4 - 3 \cos t \tag{1}$$

**Solution.** One way to sketch the trajectory is to choose a representative succession of times, plot the $(x, y)$ coordinates of points on the trajectory at those times, and connect the points with a smooth curve. The trajectory in Figure 10.1.2 was obtained in this way from the data in Table 10.1.1 in which the approximate coordinates of the particle are given at time increments of 1 unit. Observe that there is no $t$-axis in the picture; the values of $t$ appear only as labels on the plotted points, and even these are usually omitted unless it is important to emphasize the locations of the particle at specific times.

##### Table 10.1.1
| $t$ | $x$ | $y$ | $t$ | $x$ | $y$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0.0 | 1.0 | 6 | 6.8 | 1.1 |
| 1 | -1.5 | 2.4 | 7 | 5.0 | 1.7 |
| 2 | -0.7 | 5.2 | 8 | 5.0 | 4.4 |
| 3 | 2.6 | 7.0 | 9 | 7.8 | 6.7 |
| 4 | 6.3 | 6.0 | 10 | 11.6 | 6.5 |
| 5 | 7.9 | 3.1 | | | |

> **TECHNOLOGY MASTERY**  
> Read the documentation for your graphing utility to learn how to graph parametric equations, and then generate the trajectory in Example 1. Explore the behavior of the particle beyond time $t = 10$.

Although parametric equations commonly arise in problems of motion with time as the parameter, they arise in other contexts as well. Thus, unless the problem dictates that the parameter $t$ in the equations $x = f(t), \; y = g(t)$ represents time, it should be viewed simply as an independent variable that varies over some interval of real numbers. (In fact, there is no need to use the letter $t$ for the parameter; any letter not reserved for another purpose can be used.) If no restrictions on the parameter are stated explicitly or implied by the equations, then it is understood that it varies from $-\infty$ to $+\infty$. To indicate that a parameter $t$ is restricted to an interval $[a, b]$, we will write
$$x = f(t), \quad y = g(t) \quad (a \le t \le b)$$

#### Example 2
Find the graph of the parametric equations
$$x = \cos t, \quad y = \sin t \quad (0 \le t \le 2\pi) \tag{2}$$

**Solution.** One way to find the graph is to eliminate the parameter $t$ by noting that
$$x^2 + y^2 = \sin^2 t + \cos^2 t = 1$$
Thus, the graph is contained in the unit circle $x^2 + y^2 = 1$. Geometrically, the parameter $t$ can be interpreted as the angle swept out by the radial line from the origin to the point $(x, y) = (\cos t, \sin t)$ on the unit circle (Figure 10.1.3). As $t$ increases from 0 to $2\pi$, the point traces the circle counterclockwise, starting at $(1, 0)$ when $t = 0$ and completing one full revolution when $t = 2\pi$. One can obtain different portions of the circle by varying the interval over which the parameter varies. For example,
$$x = \cos t, \quad y = \sin t \quad (0 \le t \le \pi) \tag{3}$$
represents just the upper semicircle in Figure 10.1.3.

---

### ORIENTATION

The direction in which the graph of a pair of parametric equations is traced as the parameter increases is called the **direction of increasing parameter** or sometimes the **orientation** imposed on the curve by the equations. Thus, we make a distinction between a **curve**, which is a set of points, and a **parametric curve**, which is a curve with an orientation imposed on it by a set of parametric equations. For example, we saw in Example 2 that the circle represented parametrically by (2) is traced counterclockwise as $t$ increases and hence has counterclockwise orientation. As shown in Figures 10.1.2 and 10.1.3, the orientation of a parametric curve can be indicated by arrowheads.

To obtain parametric equations for the unit circle with clockwise orientation, we can replace $t$ by $-t$ in (2) and use the identities $\cos(-t) = \cos t$ and $\sin(-t) = -\sin t$. This yields
$$x = \cos t, \quad y = -\sin t \quad (0 \le t \le 2\pi)$$
Here, the circle is traced clockwise by a point that starts at $(1, 0)$ when $t = 0$ and completes one full revolution when $t = 2\pi$ (Figure 10.1.4).

> **TECHNOLOGY MASTERY**  
> When parametric equations are graphed using a calculator, the orientation can often be determined by watching the direction in which the graph is traced on the screen. However, many computers graph so fast that it is often hard to discern the orientation. See if you can use your graphing utility to confirm that (3) has a counterclockwise orientation.

#### Example 3
Graph the parametric curve
$$x = 2t - 3, \quad y = 6t - 7$$
by eliminating the parameter, and indicate the orientation on the graph.

**Solution.** To eliminate the parameter we will solve the first equation for $t$ as a function of $x$, and then substitute this expression for $t$ into the second equation:
$$t = \frac{1}{2}(x + 3)$$
$$y = 6\left(\frac{1}{2}\right)(x + 3) - 7$$
$$y = 3x + 2$$
Thus, the graph is a line of slope 3 and $y$-intercept 2. To find the orientation we must look to the original equations; the direction of increasing $t$ can be deduced by observing that $x$ increases as $t$ increases or by observing that $y$ increases as $t$ increases. Either piece of information tells us that the line is traced left to right as shown in Figure 10.1.5.

> **REMARK.** Not all parametric equations produce curves with definite orientations; if the equations are badly behaved, then the point tracing the curve may leap around sporadically or move back and forth, failing to determine a definite direction. For example, if
> $$x = \sin t, \quad y = \sin^2 t$$
> then the point $(x, y)$ moves along the parabola $y = x^2$. However, the value of $x$ varies periodically between $-1$ and 1, so the point $(x, y)$ moves periodically back and forth along the parabola between the points $(-1, 1)$ and $(1, 1)$ (as shown in Figure 10.1.6). Later in the text we will discuss restrictions that eliminate such erratic behavior, but for now we will just avoid such complications.

---

### EXPRESSING ORDINARY FUNCTIONS PARAMETRICALLY

An equation $y = f(x)$ can be expressed in parametric form by introducing the parameter $t = x$; this yields the parametric equations
$$x = t, \quad y = f(t)$$
For example, the portion of the curve $y = \cos x$ over the interval $[-2\pi, 2\pi]$ can be expressed parametrically as $x = t, \; y = \cos t \; (-2\pi \le t \le 2\pi)$ (Figure 10.1.7).

If a function $f$ is one-to-one, then it has an inverse function $f^{-1}$. In this case the equation $y = f^{-1}(x)$ is equivalent to $x = f(y)$. We can express the graph of $f^{-1}$ in parametric form by introducing the parameter $y = t$; this yields the parametric equations
$$x = f(t), \quad y = t$$
For example, Figure 10.1.8 shows the graph of $f(x) = x^5 + x + 1$ and its inverse. The graph of $f$ can be represented parametrically as
$$x = t, \quad y = t^5 + t + 1$$
and the graph of $f^{-1}$ can be represented parametrically as
$$x = t^5 + t + 1, \quad y = t$$

---

### TANGENT LINES TO PARAMETRIC CURVES

We will be concerned with curves that are given by parametric equations
$$x = f(t), \quad y = g(t)$$
in which $f(t)$ and $g(t)$ have continuous first derivatives with respect to $t$. It can be proved that if $dx/dt \neq 0$, then $y$ is a differentiable function of $x$, in which case the chain rule implies that
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} \tag{4}$$
This formula makes it possible to find $dy/dx$ directly from the parametric equations without eliminating the parameter.

#### Example 4
Find the slope of the tangent line to the unit circle
$$x = \cos t, \quad y = \sin t \quad (0 \le t \le 2\pi)$$
at the point where $t = \pi/6$ (Figure 10.1.9).

**Solution.** From (4), the slope at a general point on the circle is
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{\cos t}{-\sin t} = -\cot t \tag{5}$$
Thus, the slope at $t = \pi/6$ is
$$\left.\frac{dy}{dx}\right|_{t=\pi/6} = -\cot\frac{\pi}{6} = -\sqrt{3}$$

> *Note that Formula (5) makes sense geometrically because the radius from the origin to the point $P(\cos t, \sin t)$ has slope $m = \tan t$. Thus the tangent line at $P$, being perpendicular to the radius, has slope*
> $$-\frac{1}{m} = -\frac{1}{\tan t} = -\cot t$$
> *(Figure 10.1.10).*

It follows from Formula (4) that the tangent line to a parametric curve will be horizontal at those points where $dy/dt = 0$ and $dx/dt \neq 0$, since $dy/dx = 0$ at such points. Two different situations occur when $dx/dt = 0$. At points where $dx/dt = 0$ and $dy/dt \neq 0$, the right side of (4) has a nonzero numerator and a zero denominator; we will agree that the curve has **infinite slope** and a **vertical tangent line** at such points. At points where $dx/dt$ and $dy/dt$ are both zero, the right side of (4) becomes an indeterminate form; we call such points **singular points**. No general statement can be made about the behavior of parametric curves at singular points; they must be analyzed case by case.

#### Example 5
In a disastrous first flight, an experimental paper airplane follows the trajectory of the particle in Example 1:
$$x = t - 3\sin t, \quad y = 4 - 3\cos t \quad (t \ge 0)$$
but crashes into a wall at time $t = 10$ (Figure 10.1.11).
(a) At what times was the airplane flying horizontally?
(b) At what times was it flying vertically?

**Solution (a).** The airplane was flying horizontally at those times when $dy/dt = 0$ and $dx/dt \neq 0$. From the given trajectory we have
$$\frac{dy}{dt} = 3\sin t \quad \text{and} \quad \frac{dx}{dt} = 1 - 3\cos t \tag{6}$$
Setting $dy/dt = 0$ yields the equation $3\sin t = 0$, or, more simply, $\sin t = 0$. This equation has four solutions in the time interval $0 \le t \le 10$:
$$t = 0, \quad t = \pi, \quad t = 2\pi, \quad t = 3\pi$$
Since $dx/dt = 1 - 3\cos t \neq 0$ for these values of $t$ (verify), the airplane was flying horizontally at times
$$t = 0, \quad t = \pi \approx 3.14, \quad t = 2\pi \approx 6.28, \quad \text{and} \quad t = 3\pi \approx 9.42$$
which is consistent with Figure 10.1.11.

**Solution (b).** The airplane was flying vertically at those times when $dx/dt = 0$ and $dy/dt \neq 0$. Setting $dx/dt = 0$ in (6) yields the equation
$$1 - 3\cos t = 0 \quad \text{or} \quad \cos t = \frac{1}{3}$$
This equation has three solutions in the time interval $0 \le t \le 10$ (Figure 10.1.12):
$$t = \cos^{-1}\left(\frac{1}{3}\right), \quad t = 2\pi - \cos^{-1}\left(\frac{1}{3}\right), \quad t = 2\pi + \cos^{-1}\left(\frac{1}{3}\right)$$
Since $dy/dt = 3\sin t$ is not zero at these points (why?), it follows that the airplane was flying vertically at times
$$t = \cos^{-1}\left(\frac{1}{3}\right) \approx 1.23, \quad t \approx 2\pi - 1.23 \approx 5.05, \quad t \approx 2\pi + 1.23 \approx 7.51$$
which again is consistent with Figure 10.1.11.

#### Example 6
The curve represented by the parametric equations
$$x = t^2, \quad y = t^3 \quad (-\infty < t < +\infty)$$
is called a **semicubical parabola**. The parameter $t$ can be eliminated by cubing $x$ and squaring $y$, from which it follows that $y^2 = x^3$. The graph of this equation, shown in Figure 10.1.13, consists of two branches: an upper branch obtained by graphing $y = x^{3/2}$ and a lower branch obtained by graphing $y = -x^{3/2}$. The two branches meet at the origin, which corresponds to $t = 0$ in the parametric equations. This is a singular point because the derivatives $dx/dt = 2t$ and $dy/dt = 3t^2$ are both zero there.

#### Example 7
Without eliminating the parameter, find $dy/dx$ and $d^2y/dx^2$ at $(1, 1)$ and $(1, -1)$ on the semicubical parabola given by the parametric equations in Example 6.

**Solution.** From (4) we have
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{3t^2}{2t} = \frac{3}{2}t \quad (t \neq 0) \tag{7}$$
and from (4) applied to $y' = dy/dx$ we have
$$\frac{d^2y}{dx^2} = \frac{dy'/dx}{dx/dt} = \frac{dy'/dt}{dx/dt} = \frac{3/2}{2t} = \frac{3}{4t} \tag{8}$$
Since the point $(1, 1)$ on the curve corresponds to $t = 1$ in the parametric equations, it follows from (7) and (8) that
$$\left.\frac{dy}{dx}\right|_{t=1} = \frac{3}{2} \quad \text{and} \quad \left.\frac{d^2y}{dx^2}\right|_{t=1} = \frac{3}{4}$$
Similarly, the point $(1, -1)$ corresponds to $t = -1$ in the parametric equations, so applying (7) and (8) again yields
$$\left.\frac{dy}{dx}\right|_{t=-1} = -\frac{3}{2} \quad \text{and} \quad \left.\frac{d^2y}{dx^2}\right|_{t=-1} = -\frac{3}{4}$$

Note that the values we obtained for the first and second derivatives are consistent with the graph in Figure 10.1.13, since at $(1, 1)$ on the upper branch the tangent line has positive slope and the curve is concave up, and at $(1, -1)$ on the lower branch the tangent line has negative slope and the curve is concave down.

Finally, observe that we were able to apply Formulas (7) and (8) for both $t = 1$ and $t = -1$, even though the points $(1, 1)$ and $(1, -1)$ lie on different branches. In contrast, had we chosen to perform the same computations by eliminating the parameter, we would have had to obtain separate derivative formulas for $y = x^{3/2}$ and $y = -x^{3/2}$.

> **WARNING.** Although it is true that $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$, you cannot conclude that $\frac{d^2y}{dx^2}$ is the quotient of $d^2y/dt^2$ and $d^2x/dt^2$. To illustrate that this conclusion is erroneous, show that for the parametric curve in Example 7,
> $$\left.\frac{d^2y}{dx^2}\right|_{t=1} \neq \left.\frac{d^2y/dt^2}{d^2x/dt^2}\right|_{t=1}$$

---

### ARC LENGTH OF PARAMETRIC CURVES

The following result provides a formula for finding the arc length of a curve from parametric equations for the curve. Its derivation is similar to that of Formula (3) in Section 5.4 and will be omitted.

> **10.1.1 THEOREM (Arc Length Formula for Parametric Curves)**  
> If no segment of the curve represented by the parametric equations
> $$x = x(t), \quad y = y(t) \quad (a \le t \le b)$$
> is traced more than once as $t$ increases from $a$ to $b$, and if $dx/dt$ and $dy/dt$ are continuous functions for $a \le t \le b$, then the arc length $L$ of the curve is given by
> $$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt \tag{9}$$

> *Note:* Formulas (4) and (5) in Section 5.4 can be viewed as special cases of (9). For example, Formula (4) in Section 5.4 can be obtained from (9) by writing $y = f(x)$ parametrically as $x = t, \; y = f(t)$, and Formula (5) in Section 5.4 can be obtained by writing $x = g(y)$ parametrically as $x = g(t), \; y = t$.

#### Example 8
Use (9) to find the circumference of a circle of radius $a$ from the parametric equations
$$x = a\cos t, \quad y = a\sin t \quad (0 \le t \le 2\pi)$$

**Solution.**
$$L = \int_0^{2\pi} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt = \int_0^{2\pi} \sqrt{(-a\sin t)^2 + (a\cos t)^2}\,dt = \int_0^{2\pi} a\,dt = [at]_0^{2\pi} = 2\pi a$$

---

### THE CYCLOID (THE APPLE OF DISCORD)

The results of this section can be used to investigate a curve known as a **cycloid**. This curve, which is one of the most significant in the history of mathematics, can be generated by a point on a circle that rolls along a straight line (Figure 10.1.14). This curve has a fascinating history, which we will discuss shortly; but first we will show how to obtain parametric equations for it. For this purpose, let us assume that the circle has radius $a$ and rolls along the positive $x$-axis of a rectangular coordinate system. Let $P(x, y)$ be the point on the circle that traces the cycloid, and assume that $P$ is initially at the origin. We will take as our parameter the angle $\theta$ that is swept out by the radial line to $P$ as the circle rolls (Figure 10.1.14). It is standard here to regard $\theta$ as positive, even though it is generated by a clockwise rotation.

The motion of $P$ is a combination of the movement of the circle's center parallel to the $x$-axis and the rotation of $P$ about the center. As the radial line sweeps out an angle $\theta$, the point $P$ traverses an arc of length $a\theta$, and the circle moves a distance $a\theta$ along the $x$-axis. Thus, as suggested by Figure 10.1.15, the center moves to the point $(a\theta, a)$, and the coordinates of $P$ are
$$x = a\theta - a\sin\theta, \quad y = a - a\cos\theta \tag{10}$$
These are the equations of the cycloid in terms of the parameter $\theta$.

One of the reasons the cycloid is important in the history of mathematics is that the study of its properties helped to spur the development of early versions of differentiation and integration. Work on the cycloid was carried out by some of the most famous names in seventeenth century mathematics, including Johann and Jakob Bernoulli, Descartes, L'Hôpital, Newton, and Leibniz. The curve was named the "cycloid" by the Italian mathematician and astronomer, Galileo, who spent over 40 years investigating its properties. An early problem of interest was that of constructing tangent lines to the cycloid. This problem was first solved by Descartes, and then by Fermat, whom Descartes had challenged with the question. A modern solution to this problem follows directly from the parametric equations (10) and Formula (4). For example, using Formula (4), it is straightforward to show that the $x$-intercepts of the cycloid are cusps and that there is a horizontal tangent line to the cycloid halfway between adjacent $x$-intercepts (Exercise 60).

Another early problem was determining the arc length of an arch of the cycloid. This was solved in 1658 by the famous British architect and mathematician, Sir Christopher Wren. He showed that the arc length of one arch of the cycloid is exactly eight times the radius of the generating circle. [For a solution to this problem using Formula (9), see Exercise 71.]

The cycloid is also important historically because it provides the solution to two famous mathematical problems—the **brachistochrone problem** (from Greek words meaning "shortest time") and the **tautochrone problem** (from Greek words meaning "equal time"). The brachistochrone problem is to determine the shape of a wire along which a bead might slide from a point $P$ to another point $Q$, not directly below, in the shortest time. The tautochrone problem is to find the shape of a wire from $P$ to $Q$ such that two beads started at any points on the wire between $P$ and $Q$ reach $Q$ in the same amount of time. The solution to both problems turns out to be an inverted cycloid (Figure 10.1.16).

In June of 1696, Johann Bernoulli posed the brachistochrone problem in the form of a challenge to other mathematicians. At first, one might conjecture that the wire should form a straight line, since that shape results in the shortest distance from $P$ to $Q$. However, the inverted cycloid allows the bead to fall more rapidly at first, building up sufficient speed to reach $Q$ in the shortest time, even though it travels a longer distance. The problem was solved by Newton, Leibniz, and L'Hôpital, as well as by Johann Bernoulli and his older brother Jakob; it was formulated and solved incorrectly years earlier by Galileo, who thought the answer was a circular arc. In fact, Johann was so impressed with his brother Jakob's solution that he claimed it to be his own. (This was just one of many disputes about the cycloid that eventually led to the curve being known as the "apple of discord.") One solution of the brachistochrone problem leads to the differential equation
$$\left(1 + \left(\frac{dy}{dx}\right)^2\right)y = 2a \tag{11}$$
where $a$ is a positive constant. We leave it as an exercise (Exercise 72) to show that the cycloid provides a solution to this differential equation.

> **Johann (left) and Jakob (right) Bernoulli**  
> Members of an amazing Swiss family that included several generations of outstanding mathematicians and scientists. Nikolaus Bernoulli (1623–1708), a druggist, fled from Antwerp to escape religious persecution and ultimately settled in Basel, Switzerland. There he had three sons, Jakob I (also called Jacques or James), Nikolaus, and Johann I (also called Jean or John). The Roman numerals are used to distinguish family members with identical names (see the family tree below).  
> Following Newton and Leibniz, the Bernoulli brothers, Jakob I and Johann I, are considered by some to be the two most important founders of calculus. Jakob I was self-taught in mathematics. His father wanted him to study for the ministry, but he turned to mathematics and in 1686 became a professor at the University of Basel. When he started working in mathematics, he knew nothing of Newton's and Leibniz' work. He eventually became familiar with Newton's results, but because so little of Leibniz' work was published, Jakob duplicated many of Leibniz' results.  
> Jakob's younger brother Johann I was urged to enter into business by his father. Instead, he turned to medicine and studied mathematics under the guidance of his older brother. He eventually became a mathematics professor at Gröningen in Holland, and then, when Jakob died in 1705, Johann succeeded him as mathematics professor at Basel. Throughout their lives, Jakob I and Johann I had a mutual passion for criticizing each other's work, which frequently erupted into ugly confrontations. Leibniz tried to mediate the disputes, but Jakob, who resented Leibniz' superior intellect, accused him of siding with Johann, and thus Leibniz became entangled in the arguments. The brothers often worked on common problems that they posed as challenges to one another. Johann, interested in gaining fame, often used unscrupulous means to make himself appear the originator of his brother's results; Jakob occasionally retaliated. Thus, it is often difficult to determine who deserves credit for many results. However, both men made major contributions to the development of calculus. In addition to his work on calculus, Jakob helped establish fundamental principles in probability, including the Law of Large Numbers, which is a cornerstone of modern probability theory.  
> Among the other members of the Bernoulli family, Daniel, son of Johann I, is the most famous. He was a professor of mathematics at St. Petersburg Academy in Russia and subsequently a professor of anatomy and then physics at Basel. He did work in calculus and probability, but is best known for his work in physics. A basic law of fluid flow, called Bernoulli's principle, is named in his honor. He won the annual prize of the French Academy 10 times for work on vibrating strings, tides of the sea, and kinetic theory of gases.  
> Johann II succeeded his father as professor of mathematics at Basel. His research was on the theory of heat and sound. Nikolaus I was a mathematician and law scholar who worked on probability and series. On the recommendation of Leibniz, he was appointed professor of mathematics at Padua and then went to Basel as a professor of logic and then law. Nikolaus II was professor of jurisprudence in Switzerland and then professor of mathematics at St. Petersburg Academy. Johann III was a professor of mathematics and astronomy in Berlin and Jakob II succeeded his uncle Daniel as professor of mathematics at St. Petersburg Academy in Russia. Truly an incredible family!

---

### QUICK CHECK EXERCISES 10.1
*(See page 705 for answers.)*

1. Find parametric equations for a circle of radius 2, centered at $(3, 5)$.
2. The graph of the curve described by the parametric equations $x = 4t - 1, \; y = 3t + 2$ is a straight line with slope $\underline{\quad}$ and $y$-intercept $\underline{\quad}$.
3. Suppose that a parametric curve $C$ is given by the equations $x = f(t), \; y = g(t)$ for $0 \le t \le 1$. Find parametric equations for $C$ that reverse the direction the curve is traced as the parameter increases from 0 to 1.
4. To find $dy/dx$ directly from the parametric equations $x = f(t), \; y = g(t)$ we can use the formula $dy/dx = \underline{\quad}$.
5. Let $L$ be the length of the curve $x = \ln t, \; y = \sin t \; (1 \le t \le \pi)$. An integral expression for $L$ is $\underline{\quad}$.

---

### EXERCISE SET 10.1

1. (a) By eliminating the parameter, sketch the trajectory over the time interval $0 \le t \le 5$ of the particle whose parametric equations of motion are
   $$x = t - 1, \quad y = t + 1$$
   (b) Indicate the direction of motion on your sketch.  
   (c) Make a table of $x$- and $y$-coordinates of the particle at times $t = 0, 1, 2, 3, 4, 5$.  
   (d) Mark the position of the particle on the curve at the times in part (c), and label those positions with the values of $t$.

2. (a) By eliminating the parameter, sketch the trajectory over the time interval $0 \le t \le 1$ of the particle whose parametric equations of motion are
   $$x = \cos(\pi t), \quad y = \sin(\pi t)$$
   (b) Indicate the direction of motion on your sketch.  
   (c) Make a table of $x$- and $y$-coordinates of the particle at times $t = 0, 0.25, 0.5, 0.75, 1$.  
   (d) Mark the position of the particle on the curve at the times in part (c), and label those positions with the values of $t$.

**3–12 Sketch the curve by eliminating the parameter, and indicate the direction of increasing $t$.**
3. $x = 3t - 4, \quad y = 6t + 2$
4. $x = t - 3, \quad y = 3t - 7 \quad (0 \le t \le 3)$
5. $x = 2\cos t, \quad y = 5\sin t \quad (0 \le t \le 2\pi)$
6. $x = \sqrt{t}, \quad y = 2t + 4$
7. $x = 3 + 2\cos t, \quad y = 2 + 4\sin t \quad (0 \le t \le 2\pi)$
8. $x = \sec t, \quad y = \tan t \quad (\pi \le t < 3\pi/2)$
9. $x = \cos 2t, \quad y = \sin t \quad (-\pi/2 \le t \le \pi/2)$
10. $x = 4t + 3, \quad y = 16t^2 - 9$
11. $x = 2\sin^2 t, \quad y = 3\cos^2 t \quad (0 \le t \le \pi/2)$
12. $x = \sec^2 t, \quad y = \tan^2 t \quad (0 \le t < \pi/2)$

**13–18 Find parametric equations for the curve, and check your work by generating the curve with a graphing utility.**
13. A circle of radius 5, centered at the origin, oriented clockwise.
14. The portion of the circle $x^2 + y^2 = 1$ that lies in the third quadrant, oriented counterclockwise.
15. A vertical line intersecting the $x$-axis at $x = 2$, oriented upward.
16. The ellipse $x^2/4 + y^2/9 = 1$, oriented counterclockwise.
17. The portion of the parabola $x = y^2$ joining $(1, -1)$ and $(1, 1)$, oriented down to up.
18. The circle of radius 4, centered at $(1, -3)$, oriented counterclockwise.

19. (a) Use a graphing utility to generate the trajectory of a particle whose equations of motion over the time interval $0 \le t \le 5$ are
    $$x = 6t - \frac{1}{2}t^3, \quad y = 1 + \frac{1}{2}t^2$$
    (b) Make a table of $x$- and $y$-coordinates of the particle at times $t = 0, 1, 2, 3, 4, 5$.  
    (c) At what times is the particle on the $y$-axis?  
    (d) During what time interval is $y < 5$?  
    (e) At what time does the $x$-coordinate of the particle reach a maximum?

20. (a) Use a graphing utility to generate the trajectory of a paper airplane whose equations of motion for $t \ge 0$ are
    $$x = t - 2\sin t, \quad y = 3 - 2\cos t$$
    (b) Assuming that the plane flies in a room in which the floor is at $y = 0$, explain why the plane will not crash into the floor. [For simplicity, ignore the physical size of the plane by treating it as a particle.]  
    (c) How high must the ceiling be to ensure that the plane does not touch or crash into it?

**21–22 Graph the equation using a graphing utility.**
21. (a) $x = y^2 + 2y + 1$  
    (b) $x = \sin y, \quad -2\pi \le y \le 2\pi$
22. (a) $x = y + 2y^3 - y^5$  
    (b) $x = \tan y, \quad -\pi/2 < y < \pi/2$

#### FOCUS ON CONCEPTS
23. In each part, match the parametric equation with one of the curves labeled (I)–(VI), and explain your reasoning.
    (a) $x = \sqrt{t}, \quad y = \sin 3t$  
    (b) $x = 2\cos t, \quad y = 3\sin t$  
    (c) $x = t\cos t, \quad y = t\sin t$  
    (d) $x = \frac{3t}{1+t^3}, \quad y = \frac{3t^2}{1+t^3}$  
    (e) $x = \frac{t^3}{1+t^2}, \quad y = \frac{2t^2}{1+t^2}$  
    (f) $x = \frac{1}{2}\cos t, \quad y = \sin 2t$

24. (a) Identify the orientation of the curves in Exercise 23.  
    (b) Explain why the parametric curve
    $$x = t^2, \quad y = t^4 \quad (-1 \le t \le 1)$$
    does not have a definite orientation.

25. (a) Suppose that the line segment from the point $P(x_0, y_0)$ to $Q(x_1, y_1)$ is represented parametrically by
    $$x = x_0 + (x_1 - x_0)t, \quad y = y_0 + (y_1 - y_0)t \quad (0 \le t \le 1)$$
    and that $R(x, y)$ is the point on the line segment corresponding to a specified value of $t$. Show that $t = r/q$, where $r$ is the distance from $P$ to $R$ and $q$ is the distance from $P$ to $Q$.  
    (b) What value of $t$ produces the midpoint between points $P$ and $Q$?  
    (c) What value of $t$ produces the point that is three-fourths of the way from $P$ to $Q$?

26. Find parametric equations for the line segment joining $P(2, -1)$ and $Q(3, 1)$, and use the result in Exercise 25 to find
    (a) the midpoint between $P$ and $Q$  
    (b) the point that is one-fourth of the way from $P$ to $Q$  
    (c) the point that is three-fourths of the way from $P$ to $Q$.

27. (a) Show that the line segment joining the points $(x_0, y_0)$ and $(x_1, y_1)$ can be represented parametrically as
    $$x = x_0 + (x_1 - x_0)\frac{t - t_0}{t_1 - t_0}, \quad y = y_0 + (y_1 - y_0)\frac{t - t_0}{t_1 - t_0} \quad (t_0 \le t \le t_1)$$
    (b) Which way is the line segment oriented?  
    (c) Find parametric equations for the line segment traced from $(3, -1)$ to $(1, 4)$ as $t$ varies from 1 to 2, and check your result with a graphing utility.

28. (a) By eliminating the parameter, show that if $a$ and $c$ are not both zero, then the graph of the parametric equations
    $$x = at + b, \quad y = ct + d \quad (t_0 \le t \le t_1)$$
    is a line segment.  
    (b) Sketch the parametric curve
    $$x = 2t - 1, \quad y = t + 1 \quad (1 \le t \le 2)$$
    and indicate its orientation.  
    (c) What can you say about the line in part (a) if $a$ or $c$ (but not both) is zero?  
    (d) What do the equations represent if $a$ and $c$ are both zero?

**29–32 Use a graphing utility and parametric equations to display the graphs of $f$ and $f^{-1}$ on the same screen.**
29. $f(x) = x^3 + 0.2x - 1, \quad -1 \le x \le 2$
30. $f(x) = \sqrt{x^2 + 2} + x, \quad -5 \le x \le 5$
31. $f(x) = \cos(\cos 0.5x), \quad 0 \le x \le 3$
32. $f(x) = x + \sin x, \quad 0 \le x \le 6$

**33–36 True–False Determine whether the statement is true or false. Explain your answer.**
33. The equation $y = 1 - x^2$ can be described parametrically by $x = \sin t, \; y = \cos^2 t$.
34. The graph of the parametric equations $x = f(t), \; y = t$ is the reflection of the graph of $y = f(x)$ about the $x$-axis.
35. For the parametric curve $x = x(t), \; y = 3t^4 - 2t^3$, the derivative of $y$ with respect to $x$ is computed by
    $$\frac{dy}{dx} = \frac{12t^3 - 6t^2}{x'(t)}$$
36. The curve represented by the parametric equations
    $$x = t^3, \quad y = t + t^6 \quad (-\infty < t < +\infty)$$
    is concave down for $t < 0$.

37. Parametric curves can be defined piecewise by using different formulas for different values of the parameter. Sketch the curve that is represented piecewise by the parametric equations
    $$\begin{cases} x = 2t, \quad y = 4t^2 & (0 \le t \le 1/2) \\ x = 2 - 2t, \quad y = 2t & (1/2 \le t \le 1) \end{cases}$$

38. Find parametric equations for the rectangle with vertices $(1/2, 1/2), (-1/2, 1/2), (-1/2, -1/2),$ and $(1/2, -1/2)$, assuming that the rectangle is traced counterclockwise as $t$ varies from 0 to 1, starting at $(1/2, 1/2)$ when $t = 0$. [*Hint:* Represent the rectangle piecewise, letting $t$ vary from 0 to $1/4$ for the first edge, from $1/4$ to $1/2$ for the second edge, and so forth.]

39. (a) Find parametric equations for the ellipse that is centered at the origin and has intercepts $(4, 0), (-4, 0), (0, 3),$ and $(0, -3)$.  
    (b) Find parametric equations for the ellipse that results by translating the ellipse in part (a) so that its center is at $(-1, 2)$.  
    (c) Confirm your results in parts (a) and (b) using a graphing utility.

40. We will show later in the text that if a projectile is fired from ground level with an initial speed of $v_0$ meters per second at an angle $\alpha$ with the horizontal, and if air resistance is neglected, then its position after $t$ seconds, relative to the coordinate system is
    $$x = (v_0\cos\alpha)t, \quad y = (v_0\sin\alpha)t - \frac{1}{2}gt^2$$
    where $g \approx 9.8\text{ m/s}^2$.  
    (a) By eliminating the parameter, show that the trajectory lies on the graph of a quadratic polynomial.  
    (b) Use a graphing utility to sketch the trajectory if $\alpha = 30^\circ$ and $v_0 = 1000\text{ m/s}$.  
    (c) Using the trajectory in part (b), how high does the shell rise?  
    (d) Using the trajectory in part (b), how far does the shell travel horizontally?

#### FOCUS ON CONCEPTS
41. (a) Find the slope of the tangent line to the parametric curve $x = t/2, \; y = t^2 + 1$ at $t = -1$ and at $t = 1$ without eliminating the parameter.  
    (b) Check your answers in part (a) by eliminating the parameter and differentiating an appropriate function of $x$.

42. (a) Find the slope of the tangent line to the parametric curve $x = 3\cos t, \; y = 4\sin t$ at $t = \pi/4$ and at $t = 7\pi/4$ without eliminating the parameter.  
    (b) Check your answers in part (a) by eliminating the parameter and differentiating an appropriate function of $x$.

43. For the parametric curve in Exercise 41, make a conjecture about the sign of $d^2y/dx^2$ at $t = -1$ and at $t = 1$, and confirm your conjecture without eliminating the parameter.

44. For the parametric curve in Exercise 42, make a conjecture about the sign of $d^2y/dx^2$ at $t = \pi/4$ and at $t = 7\pi/4$, and confirm your conjecture without eliminating the parameter.

**45–50 Find $dy/dx$ and $d^2y/dx^2$ at the given point without eliminating the parameter.**
45. $x = \sqrt{t}, \quad y = 2t + 4; \quad t = 1$
46. $x = \frac{1}{2}t^2 + 1, \quad y = \frac{1}{3}t^3 - t; \quad t = 2$
47. $x = \sec t, \quad y = \tan t; \quad t = \pi/3$
48. $x = \sinh t, \quad y = \cosh t; \quad t = 0$
49. $x = \theta + \cos\theta, \quad y = 1 + \sin\theta; \quad \theta = \pi/6$
50. $x = \cos\phi, \quad y = 3\sin\phi; \quad \phi = 5\pi/6$

51. (a) Find the equation of the tangent line to the curve
    $$x = e^t, \quad y = e^{-t}$$
    at $t = 1$ without eliminating the parameter.  
    (b) Find the equation of the tangent line in part (a) by eliminating the parameter.

52. (a) Find the equation of the tangent line to the curve
    $$x = 2t + 4, \quad y = 8t^2 - 2t + 4$$
    at $t = 1$ without eliminating the parameter.  
    (b) Find the equation of the tangent line in part (a) by eliminating the parameter.

**53–54 Find all values of $t$ at which the parametric curve has (a) a horizontal tangent line and (b) a vertical tangent line.**
53. $x = 2\sin t, \quad y = 4\cos t \quad (0 \le t \le 2\pi)$
54. $x = 2t^3 - 15t^2 + 24t + 7, \quad y = t^2 + t + 1$

55. In the mid-1850s the French physicist Jules Antoine Lissajous (1822–1880) became interested in parametric equations of the form
    $$x = \sin at, \quad y = \sin bt$$
    in the course of studying vibrations that combine two perpendicular sinusoidal motions. If $a/b$ is a rational number, then the combined effect of the oscillations is a periodic motion along a path called a **Lissajous curve**.  
    (a) Use a graphing utility to generate the complete graph of the Lissajous curves corresponding to $a = 1, b = 2$; $a = 2, b = 3$; $a = 3, b = 4$; and $a = 4, b = 5$.  
    (b) The Lissajous curve
    $$x = \sin t, \quad y = \sin 2t \quad (0 \le t \le 2\pi)$$
    crosses itself at the origin (see Figure Ex-55). Find equations for the two tangent lines at the origin.

56. The prolate cycloid
    $$x = 2 - \pi\cos t, \quad y = 2t - \pi\sin t \quad (-\pi \le t \le \pi)$$
    crosses itself at a point on the $x$-axis (see Figure Ex-56). Find equations for the two tangent lines at that point.

57. Show that the curve $x = t^2, \; y = t^3 - 4t$ intersects itself at the point $(4, 0)$, and find equations for the two tangent lines to the curve at the point of intersection.

58. Show that the curve with parametric equations
    $$x = t^2 - 3t + 5, \quad y = t^3 + t^2 - 10t + 9$$
    intersects itself at the point $(3, 1)$, and find equations for the two tangent lines to the curve at the point of intersection.

59. (a) Use a graphing utility to generate the graph of the parametric curve
    $$x = \cos^3 t, \quad y = \sin^3 t \quad (0 \le t \le 2\pi)$$
    and make a conjecture about the values of $t$ at which singular points occur.  
    (b) Confirm your conjecture in part (a) by calculating appropriate derivatives.

60. Verify that the cycloid described by Formula (10) has cusps at its $x$-intercepts and horizontal tangent lines at midpoints between adjacent $x$-intercepts (see Figure 10.1.14).

61. (a) What is the slope of the tangent line at time $t$ to the trajectory of the paper airplane in Example 5?  
    (b) What was the airplane's approximate angle of inclination when it crashed into the wall?

62. Suppose that a bee follows the trajectory
    $$x = t - 2\cos t, \quad y = 2 - 2\sin t \quad (0 \le t \le 10)$$
    (a) At what times was the bee flying horizontally?  
    (b) At what times was the bee flying vertically?

63. Consider the family of curves described by the parametric equations
    $$x = a\cos t + h, \quad y = b\sin t + k \quad (0 \le t < 2\pi)$$
    where $a \neq 0$ and $b \neq 0$. Describe the curves in this family if
    (a) $h$ and $k$ are fixed but $a$ and $b$ can vary  
    (b) $a$ and $b$ are fixed but $h$ and $k$ can vary  
    (c) $a = 1$ and $b = 1$, but $h$ and $k$ vary so that $h = k + 1$.

64. (a) Use a graphing utility to study how the curves in the family
    $$x = 2a\cos^2 t, \quad y = 2a\cos t\sin t \quad (-2\pi < t < 2\pi)$$
    change as $a$ varies from 0 to 5.  
    (b) Confirm your conclusion algebraically.  
    (c) Write a brief paragraph that describes your findings.

**65–70 Find the exact arc length of the curve over the stated interval.**
65. $x = t^2, \quad y = \frac{1}{3}t^3 \quad (0 \le t \le 1)$
66. $x = \sqrt{t} - 2, \quad y = 2t^{3/4} \quad (1 \le t \le 16)$
67. $x = \cos 3t, \quad y = \sin 3t \quad (0 \le t \le \pi)$
68. $x = \sin t + \cos t, \quad y = \sin t - \cos t \quad (0 \le t \le \pi)$
69. $x = e^{2t}(\sin t + \cos t), \quad y = e^{2t}(\sin t - \cos t) \quad (-1 \le t \le 1)$
70. $x = 2\sin^{-1} t, \quad y = \ln(1 - t^2) \quad (0 \le t \le 1/2)$

71. (a) Use Formula (9) to show that the length $L$ of one arch of a cycloid is given by
    $$L = a\int_0^{2\pi} \sqrt{2(1 - \cos\theta)}\,d\theta$$
    (b) Use a CAS to show that $L$ is eight times the radius of the wheel that generates the cycloid (see Figure Ex-71).

72. Use the parametric equations in Formula (10) to verify that the cycloid provides one solution to the differential equation
    $$\left(1 + \left(\frac{dy}{dx}\right)^2\right)y = 2a$$
    where $a$ is a positive constant.

#### FOCUS ON CONCEPTS
73. The amusement park rides illustrated in Figure Ex-73 consist of two connected rotating arms of length 1—an inner arm that rotates counterclockwise at 1 radian per second and an outer arm that can be programmed to rotate either clockwise at 2 radians per second (the Scrambler ride) or counterclockwise at 2 radians per second (the Calypso ride). The center of the rider cage is at the end of the outer arm.  
    (a) Show that in the Scrambler ride the center of the cage has parametric equations
    $$x = \cos t + \cos 2t, \quad y = \sin t - \sin 2t$$
    (b) Find parametric equations for the center of the cage in the Calypso ride, and use a graphing utility to confirm that the center traces the curve shown in Figure Ex-73.  
    (c) Do you think that a rider travels the same distance in one revolution of the Scrambler ride as in one revolution of the Calypso ride? Justify your conclusion.

74. (a) If a thread is unwound from a fixed circle while being held taut (i.e., tangent to the circle), then the end of the thread traces a curve called an **involute of a circle**. Show that if the circle is centered at the origin, has radius $a$, and the end of the thread is initially at the point $(a, 0)$, then the involute can be expressed parametrically as
    $$x = a(\cos\theta + \theta\sin\theta), \quad y = a(\sin\theta - \theta\cos\theta)$$
    where $\theta$ is the angle shown in part (a) of Figure Ex-74.  
    (b) Assuming that the dog in part (b) of Figure Ex-74 unwinds its leash while keeping it taut, for what values of $\theta$ in the interval $0 \le \theta \le 2\pi$ will the dog be walking North? South? East? West?  
    (c) Use a graphing utility to generate the curve traced by the dog, and show that it is consistent with your answer in part (b).

**75–80 If $f'(t)$ and $g'(t)$ are continuous functions, and if no segment of the curve**
$$x = f(t), \quad y = g(t) \quad (a \le t \le b)$$
**is traced more than once, then it can be shown that the area of the surface generated by revolving this curve about the $x$-axis is**
$$S = \int_a^b 2\pi y \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$$
**and the area of the surface generated by revolving the curve about the $y$-axis is**
$$S = \int_a^b 2\pi x \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$$
*[The derivations are similar to those used to obtain Formulas (4) and (5) in Section 5.5.] Use the formulas above in these exercises.*

75. Find the area of the surface generated by revolving $x = t^2, \; y = 3t \; (0 \le t \le 2)$ about the $x$-axis.
76. Find the area of the surface generated by revolving the curve $x = e^t\cos t, \; y = e^t\sin t \; (0 \le t \le \pi/2)$ about the $x$-axis.
77. Find the area of the surface generated by revolving the curve $x = \cos^2 t, \; y = \sin^2 t \; (0 \le t \le \pi/2)$ about the $y$-axis.
78. Find the area of the surface generated by revolving $x = 6t, \; y = 4t^2 \; (0 \le t \le 1)$ about the $y$-axis.
79. By revolving the semicircle
    $$x = r\cos t, \quad y = r\sin t \quad (0 \le t \le \pi)$$
    about the $x$-axis, show that the surface area of a sphere of radius $r$ is $4\pi r^2$.
80. The equations
    $$x = a\phi - a\sin\phi, \quad y = a - a\cos\phi \quad (0 \le \phi \le 2\pi)$$
    represent one arch of a cycloid. Show that the surface area generated by revolving this curve about the $x$-axis is given by $S = 64\pi a^2/3$.
81. **Writing.** Consult appropriate reference works and write an essay on American mathematician Nathaniel Bowditch (1773–1838) and his investigation of Bowditch curves (better known as Lissajous curves; see Exercise 55).
82. **Writing.** What are some of the advantages of expressing a curve parametrically rather than in the form $y = f(x)$?

#### QUICK CHECK ANSWERS 10.1
1. $x = 3 + 2\cos t, \quad y = 5 + 2\sin t \quad (0 \le t \le 2\pi)$
2. $\frac{3}{4}; \quad 2.75$
3. $x = f(1 - t), \quad y = g(1 - t)$
4. $\frac{dy/dt}{dx/dt} = \frac{g'(t)}{f'(t)}$
5. $\int_1^\pi \sqrt{(1/t)^2 + \cos^2 t}\,dt$

---

## 10.2 POLAR COORDINATES

Up to now we have specified the location of a point in the plane by means of coordinates relative to two perpendicular coordinate axes. However, sometimes a moving point has a special affinity for some fixed point, such as a planet moving in an orbit under the central attraction of the Sun. In such cases, the path of the particle is best described by its angular direction and its distance from the fixed point. In this section we will discuss a new kind of coordinate system that is based on this idea.

### POLAR COORDINATE SYSTEMS

A polar coordinate system in a plane consists of a fixed point $O$, called the **pole** (or **origin**), and a ray emanating from the pole, called the **polar axis**. In such a coordinate system we can associate with each point $P$ in the plane a pair of **polar coordinates** $(r, \theta)$, where $r$ is the distance from $P$ to the pole and $\theta$ is an angle from the polar axis to the ray $OP$ (Figure 10.2.1). The number $r$ is called the **radial coordinate** of $P$ and the number $\theta$ the **angular coordinate** (or **polar angle**) of $P$. In Figure 10.2.2, the points $(6, \pi/4)$, $(5, 2\pi/3)$, $(3, 5\pi/4)$, and $(4, 11\pi/6)$ are plotted in polar coordinate systems. If $P$ is the pole, then $r = 0$, but there is no clearly defined polar angle. We will agree that an arbitrary angle can be used in this case; that is, $(0, \theta)$ are polar coordinates of the pole for all choices of $\theta$.

The polar coordinates of a point are not unique. For example, the polar coordinates
$$(1, 7\pi/4), \quad (1, -\pi/4), \quad \text{and} \quad (1, 15\pi/4)$$
all represent the same point (Figure 10.2.3).

In general, if a point $P$ has polar coordinates $(r, \theta)$, then
$$(r, \theta + 2n\pi) \quad \text{and} \quad (r, \theta - 2n\pi)$$
are also polar coordinates of $P$ for any nonnegative integer $n$. Thus, every point has infinitely many pairs of polar coordinates.

As defined above, the radial coordinate $r$ of a point $P$ is nonnegative, since it represents the distance from $P$ to the pole. However, it will be convenient to allow for negative values of $r$ as well. To motivate an appropriate definition, consider the point $P$ with polar coordinates $(3, 5\pi/4)$. As shown in Figure 10.2.4, we can reach this point by rotating the polar axis through an angle of $5\pi/4$ and then moving 3 units from the pole along the terminal side of the angle, or we can reach the point $P$ by rotating the polar axis through an angle of $\pi/4$ and then moving 3 units from the pole along the extension of the terminal side. This suggests that the point $(3, 5\pi/4)$ might also be denoted by $(-3, \pi/4)$, with the minus sign serving to indicate that the point is on the extension of the angle's terminal side rather than on the terminal side itself.

In general, the terminal side of the angle $\theta + \pi$ is the extension of the terminal side of $\theta$, so we define negative radial coordinates by agreeing that
$$(-r, \theta) \quad \text{and} \quad (r, \theta + \pi)$$
are polar coordinates of the same point.

---

### RELATIONSHIP BETWEEN POLAR AND RECTANGULAR COORDINATES

Frequently, it will be useful to superimpose a rectangular $xy$-coordinate system on top of a polar coordinate system, making the positive $x$-axis coincide with the polar axis. If this is done, then every point $P$ will have both rectangular coordinates $(x, y)$ and polar coordinates $(r, \theta)$. As suggested by Figure 10.2.5, these coordinates are related by the equations
$$x = r\cos\theta, \quad y = r\sin\theta \tag{1}$$
These equations are well suited for finding $x$ and $y$ when $r$ and $\theta$ are known. However, to find $r$ and $\theta$ when $x$ and $y$ are known, it is preferable to use the identities $\sin^2\theta + \cos^2\theta = 1$ and $\tan\theta = \sin\theta/\cos\theta$ to rewrite (1) as
$$r^2 = x^2 + y^2, \quad \tan\theta = \frac{y}{x} \tag{2}$$

#### Example 1
Find the rectangular coordinates of the point $P$ whose polar coordinates are $(r, \theta) = (6, 2\pi/3)$ (Figure 10.2.6).

**Solution.** Substituting the polar coordinates $r = 6$ and $\theta = 2\pi/3$ in (1) yields
$$x = 6\cos\frac{2\pi}{3} = 6\left(-\frac{1}{2}\right) = -3$$
$$y = 6\sin\frac{2\pi}{3} = 6\left(\frac{\sqrt{3}}{2}\right) = 3\sqrt{3}$$
Thus, the rectangular coordinates of $P$ are $(x, y) = (-3, 3\sqrt{3})$.

#### Example 2
Find polar coordinates of the point $P$ whose rectangular coordinates are $(-2, -2\sqrt{3})$ (Figure 10.2.7).

**Solution.** We will find the polar coordinates $(r, \theta)$ of $P$ that satisfy the conditions $r > 0$ and $0 \le \theta < 2\pi$. From the first equation in (2),
$$r^2 = x^2 + y^2 = (-2)^2 + (-2\sqrt{3})^2 = 4 + 12 = 16$$
so $r = 4$. From the second equation in (2),
$$\tan\theta = \frac{y}{x} = \frac{-2\sqrt{3}}{-2} = \sqrt{3}$$
From this and the fact that $(-2, -2\sqrt{3})$ lies in the third quadrant, it follows that the angle satisfying the requirement $0 \le \theta < 2\pi$ is $\theta = 4\pi/3$. Thus, $(r, \theta) = (4, 4\pi/3)$ are polar coordinates of $P$. All other polar coordinates of $P$ are expressible in the form
$$\left(4, \frac{4\pi}{3} + 2n\pi\right) \quad \text{or} \quad \left(-4, \frac{\pi}{3} + 2n\pi\right)$$
where $n$ is an integer.

---

### GRAPHS IN POLAR COORDINATES

We will now consider the problem of graphing equations in $r$ and $\theta$, where $\theta$ is assumed to be measured in radians. Some examples of such equations are
$$r = 1, \quad \theta = \pi/4, \quad r = \theta, \quad r = \sin\theta, \quad r = \cos 2\theta$$
In a rectangular coordinate system the graph of an equation in $x$ and $y$ consists of all points whose coordinates $(x, y)$ satisfy the equation. However, in a polar coordinate system, points have infinitely many different pairs of polar coordinates, so that a given point may have some polar coordinates that satisfy an equation and others that do not. Given an equation in $r$ and $\theta$, we define its **graph in polar coordinates** to consist of all points with at least one pair of coordinates $(r, \theta)$ that satisfy the equation.

#### Example 3
Sketch the graphs of (a) $r = 1$ and (b) $\theta = \pi/4$ in polar coordinates.

**Solution (a).** For all values of $\theta$, the point $(1, \theta)$ is 1 unit away from the pole. Since $\theta$ is arbitrary, the graph is the circle of radius 1 centered at the pole (Figure 10.2.8a).

**Solution (b).** For all values of $r$, the point $(r, \pi/4)$ lies on a line that makes an angle of $\pi/4$ with the polar axis (Figure 10.2.8b). Positive values of $r$ correspond to points on the line in the first quadrant and negative values of $r$ to points on the line in the third quadrant. Thus, in absence of any restriction on $r$, the graph is the entire line. Observe, however, that had we imposed the restriction $r \ge 0$, the graph would have been just the ray in the first quadrant.

Equations $r = f(\theta)$ that express $r$ as a function of $\theta$ are especially important. One way to graph such an equation is to choose some typical values of $\theta$, calculate the corresponding values of $r$, and then plot the resulting pairs $(r, \theta)$ in a polar coordinate system. The next two examples illustrate this process.

#### Example 4
Sketch the graph of $r = \theta \; (\theta \ge 0)$ in polar coordinates by plotting points.

**Solution.** Observe that as $\theta$ increases, so does $r$; thus, the graph is a curve that spirals out from the pole as $\theta$ increases. A reasonably accurate sketch of the spiral can be obtained by plotting the points that correspond to values of $\theta$ that are integer multiples of $\pi/2$, keeping in mind that the value of $r$ is always equal to the value of $\theta$ (Figure 10.2.9).

#### Example 5
Sketch the graph of the equation $r = \sin\theta$ in polar coordinates by plotting points.

**Solution.** Table 10.2.1 shows the coordinates of points on the graph at increments of $\pi/6$.

##### Table 10.2.1
| $\theta$ (radians) | 0 | $\frac{\pi}{6}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{5\pi}{6}$ | $\pi$ | $\frac{7\pi}{6}$ | $\frac{4\pi}{3}$ | $\frac{3\pi}{2}$ | $\frac{5\pi}{3}$ | $\frac{11\pi}{6}$ | $2\pi$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $r = \sin\theta$ | 0 | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | 1 | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | 0 | $-\frac{1}{2}$ | $-\frac{\sqrt{3}}{2}$ | $-1$ | $-\frac{\sqrt{3}}{2}$ | $-\frac{1}{2}$ | 0 |
| $(r, \theta)$ | $(0, 0)$ | $(\frac{1}{2}, \frac{\pi}{6})$ | $(\frac{\sqrt{3}}{2}, \frac{\pi}{3})$ | $(1, \frac{\pi}{2})$ | $(\frac{\sqrt{3}}{2}, \frac{2\pi}{3})$ | $(\frac{1}{2}, \frac{5\pi}{6})$ | $(0, \pi)$ | $(-\frac{1}{2}, \frac{7\pi}{6})$ | $(-\frac{\sqrt{3}}{2}, \frac{4\pi}{3})$ | $(-1, \frac{3\pi}{2})$ | $(-\frac{\sqrt{3}}{2}, \frac{5\pi}{3})$ | $(-\frac{1}{2}, \frac{11\pi}{6})$ | $(0, 2\pi)$ |

These points are plotted in Figure 10.2.10. Note, however, that there are 13 points listed in the table but only 6 distinct plotted points. This is because the pairs from $\theta = \pi$ on yield duplicates of the preceding points. For example, $(-1/2, 7\pi/6)$ and $(1/2, \pi/6)$ represent the same point.

Observe that the points in Figure 10.2.10 appear to lie on a circle. We can confirm that this is so by expressing the polar equation $r = \sin\theta$ in terms of $x$ and $y$. To do this, we multiply the equation through by $r$ to obtain
$$r^2 = r\sin\theta$$
which now allows us to apply Formulas (1) and (2) to rewrite the equation as
$$x^2 + y^2 = y$$
Rewriting this equation as $x^2 + y^2 - y = 0$ and then completing the square yields
$$x^2 + \left(y - \frac{1}{2}\right)^2 = \frac{1}{4}$$
which is a circle of radius $1/2$ centered at the point $(0, 1/2)$ in the $xy$-plane.

It is often useful to view the equation $r = f(\theta)$ as an equation in rectangular coordinates (rather than polar coordinates) and graphed in a rectangular $\theta r$-coordinate system. For example, Figure 10.2.11 shows the graph of $r = \sin\theta$ displayed using rectangular $\theta r$-coordinates:
* At $\theta = 0$ we have $r = 0$, which corresponds to the pole $(0, 0)$ on the polar graph.
* As $\theta$ varies from 0 to $\pi/2$, the value of $r$ increases from 0 to 1, so the point $(r, \theta)$ moves along the circle from the pole to the high point at $(1, \pi/2)$.
* As $\theta$ varies from $\pi/2$ to $\pi$, the value of $r$ decreases from 1 back to 0, so the point $(r, \theta)$ moves along the circle from the high point back to the pole.
* As $\theta$ varies from $\pi$ to $3\pi/2$, the values of $r$ are negative, varying from 0 to $-1$. Thus, the point $(r, \theta)$ moves along the circle from the pole to the high point at $(1, \pi/2)$, which is the same as the point $(-1, 3\pi/2)$. This duplicates the motion that occurred for $0 \le \theta \le \pi/2$.
* As $\theta$ varies from $3\pi/2$ to $2\pi$, the value of $r$ varies from $-1$ to 0. Thus, the point $(r, \theta)$ moves along the circle from the high point back to the pole, duplicating the motion that occurred for $\pi/2 \le \theta \le \pi$.

#### Example 6
Sketch the graph of $r = \cos 2\theta$ in polar coordinates.

**Solution.** Instead of plotting points, we will use the graph of $r = \cos 2\theta$ in rectangular coordinates (Figure 10.2.12) to visualize how the polar graph of this equation is generated. The analysis and the resulting polar graph are shown in Figure 10.2.13. This curve is called a **four-petal rose**.

---

### SYMMETRY TESTS

Observe that the polar graph of $r = \cos 2\theta$ in Figure 10.2.13 is symmetric about the $x$-axis and the $y$-axis. This symmetry could have been predicted from the following theorem, which is suggested by Figure 10.2.14 (we omit the proof).

> **10.2.1 THEOREM (Symmetry Tests)**  
> (a) A curve in polar coordinates is symmetric about the $x$-axis if replacing $\theta$ by $-\theta$ in its equation produces an equivalent equation (Figure 10.2.14a).  
> (b) A curve in polar coordinates is symmetric about the $y$-axis if replacing $\theta$ by $\pi - \theta$ in its equation produces an equivalent equation (Figure 10.2.14b).  
> (c) A curve in polar coordinates is symmetric about the origin if replacing $\theta$ by $\theta + \pi$, or replacing $r$ by $-r$ in its equation produces an equivalent equation (Figure 10.2.14c).

> *The converse of each part of Theorem 10.2.1 is false. See Exercise 79.*

#### Example 7
Use Theorem 10.2.1 to confirm that the graph of $r = \cos 2\theta$ in Figure 10.2.13 is symmetric about the $x$-axis and $y$-axis.

**Solution.** To test for symmetry about the $x$-axis, we replace $\theta$ by $-\theta$. This yields
$$r = \cos(-2\theta) = \cos 2\theta$$
Thus, replacing $\theta$ by $-\theta$ does not alter the equation.  
To test for symmetry about the $y$-axis, we replace $\theta$ by $\pi - \theta$. This yields
$$r = \cos 2(\pi - \theta) = \cos(2\pi - 2\theta) = \cos(-2\theta) = \cos 2\theta$$
Thus, replacing $\theta$ by $\pi - \theta$ does not alter the equation.

#### Example 8
Sketch the graph of $r = a(1 - \cos\theta)$ in polar coordinates, assuming $a$ to be a positive constant.

**Solution.** Observe first that replacing $\theta$ by $-\theta$ does not alter the equation, so we know in advance that the graph is symmetric about the polar axis. Thus, if we graph the upper half of the curve, then we can obtain the lower half by reflection about the polar axis.  
As in our previous examples, we will first graph the equation in rectangular $\theta r$-coordinates (Figure 10.2.15a):
* As $\theta$ varies from 0 to $\pi/3$, $r$ increases from 0 to $a/2$.
* As $\theta$ varies from $\pi/3$ to $\pi/2$, $r$ increases from $a/2$ to $a$.
* As $\theta$ varies from $\pi/2$ to $2\pi/3$, $r$ increases from $a$ to $3a/2$.
* As $\theta$ varies from $2\pi/3$ to $\pi$, $r$ increases from $3a/2$ to $2a$.

This produces the polar curve shown in Figure 10.2.15b. The rest of the curve can be obtained by continuing the preceding analysis from $\pi$ to $2\pi$ or by reflecting the portion already graphed about the $x$-axis (Figure 10.2.15c). This heart-shaped curve is called a **cardioid** (from the Greek word *kardia* meaning "heart").

#### Example 9
Sketch the graph of $r^2 = 4\cos 2\theta$ in polar coordinates.

**Solution.** This equation does not express $r$ as a function of $\theta$, since solving for $r$ in terms of $\theta$ yields two functions:
$$r = 2\sqrt{\cos 2\theta} \quad \text{and} \quad r = -2\sqrt{\cos 2\theta}$$
Thus, to graph the equation $r^2 = 4\cos 2\theta$ we will have to graph the two functions separately and then combine those graphs.  
We will start with the graph of $r = 2\sqrt{\cos 2\theta}$. Observe first that this equation is not changed if we replace $\theta$ by $-\theta$ or if we replace $\theta$ by $\pi - \theta$. Thus, the graph is symmetric about the $x$-axis and the $y$-axis. This means that the entire graph can be obtained by graphing the portion in the first quadrant, reflecting that portion about the $y$-axis to obtain the portion in the second quadrant, and then reflecting those two portions about the $x$-axis to obtain the portions in the third and fourth quadrants.  
To begin the analysis, we will graph the equation $r = 2\sqrt{\cos 2\theta}$ in rectangular $\theta r$-coordinates (Figure 10.2.16a). Note that there are gaps over the intervals $\pi/4 < \theta < 3\pi/4$ and $5\pi/4 < \theta < 7\pi/4$ because $\cos 2\theta$ is negative for those values:
* As $\theta$ varies from 0 to $\pi/4$, $r$ decreases from 2 to 0.
* As $\theta$ varies from $\pi/4$ to $\pi/2$, no points are generated on the polar graph.

This produces the portion of the graph shown in Figure 10.2.16b. Completing the graph by reflection yields Figure 10.2.16c. The resulting propeller-shaped graph is called a **lemniscate** (from the Greek word *lemniscos* for a looped ribbon resembling the number 8). The equation $r = 2\sqrt{\cos 2\theta}$ has the same graph as $r = -2\sqrt{\cos 2\theta}$, but traced in a diagonally opposite manner. Thus, the graph of $r^2 = 4\cos 2\theta$ consists of two identical superimposed lemniscates.

---

### FAMILIES OF LINES AND RAYS THROUGH THE POLE
* $\theta = \theta_0$: line passing through the pole making an angle $\theta_0$ with the polar axis (Figure 10.2.17a).
* $\theta = \theta_0 \; (r \ge 0)$: ray emanating from the pole making an angle $\theta_0$ with the polar axis (Figure 10.2.17b).

### FAMILIES OF CIRCLES
We consider three families of circles in which $a > 0$:
$$r = a, \quad r = 2a\cos\theta, \quad r = 2a\sin\theta \tag{3–5}$$
* $r = a$: circle of radius $a$ centered at the pole.
* $r = 2a\cos\theta$: circle of radius $a$ centered on the $x$-axis at $(a, 0)$ and tangent to the $y$-axis at the origin.
* $r = 2a\sin\theta$: circle of radius $a$ centered on the $y$-axis at $(0, a)$ and tangent to the $x$-axis at the origin.

### FAMILIES OF ROSE CURVES
Equations of the form
$$r = a\sin n\theta, \quad r = a\cos n\theta \tag{6–7}$$
where $a > 0$ and $n$ is a positive integer represent **roses** (Figure 10.2.19):
* $n$ equally spaced petals of radius $a$ if $n$ is odd (traced once over $0 \le \theta < \pi$).
* $2n$ equally spaced petals of radius $a$ if $n$ is even (traced once over $0 \le \theta < 2\pi$).

### FAMILIES OF CARDIOIDS AND LIMAÇONS
Equations of the form
$$r = a \pm b\sin\theta, \quad r = a \pm b\cos\theta \tag{8–9}$$
where $a > 0, b > 0$ represent **limaçons** (from Latin *limax* for snail/slug; Figure 10.2.20):
* $a/b < 1$: Limaçon with inner loop
* $a/b = 1$: Cardioid
* $1 < a/b < 2$: Dimpled limaçon
* $a/b \ge 2$: Convex limaçon

#### Example 10
Figure 10.2.21 shows the family of limaçons $r = a + \cos\theta$ with $a$ varying from 0.25 to 2.50 in steps of 0.25. The loops get smaller until the cardioid is reached at $a = 1$, then evolve through dimpled into convex.

### FAMILIES OF SPIRALS
* **Archimedean spiral:** $r = a\theta$
* **Parabolic spiral:** $r = a\sqrt{\theta}$
* **Logarithmic spiral:** $r = ae^{b\theta}$
* **Lituus spiral:** $r = a/\sqrt{\theta}$
* **Hyperbolic spiral:** $r = a/\theta$

### GENERATING POLAR CURVES WITH GRAPHING UTILITIES
To graph a polar curve $r = f(\theta)$ parametrically:
$$x = f(\theta)\cos\theta, \quad y = f(\theta)\sin\theta \tag{10}$$

#### Example 11
Express the polar equation $r = 2 + \cos\left(\frac{5\theta}{2}\right)$ parametrically, and generate the polar graph from the parametric equations using a graphing utility.

**Solution.** Substituting $r$ in $x = r\cos\theta$ and $y = r\sin\theta$ yields
$$x = \left[2 + \cos\left(\frac{5\theta}{2}\right)\right]\cos\theta, \quad y = \left[2 + \cos\left(\frac{5\theta}{2}\right)\right]\sin\theta$$
The smallest positive integer $n$ such that $5(\theta + 2n\pi)/2$ repeats modulo $2\pi$ is $n = 2$. Thus, the entire graph is traced in two revolutions ($0 \le \theta \le 4\pi$), yielding Figure 10.2.23.

---

### QUICK CHECK EXERCISES 10.2
*(See page 719 for answers.)*

1. (a) Rectangular coordinates of a point $(x, y)$ may be recovered from its polar coordinates $(r, \theta)$ by means of the equations $x = \underline{\quad}$ and $y = \underline{\quad}$.  
   (b) Polar coordinates $(r, \theta)$ may be recovered from rectangular coordinates $(x, y)$ by means of the equations $r^2 = \underline{\quad}$ and $\tan\theta = \underline{\quad}$.
2. Find the rectangular coordinates of the points whose polar coordinates are given:  
   (a) $(4, \pi/3)$ (b) $(2, -\pi/6)$ (c) $(6, -2\pi/3)$ (d) $(4, 5\pi/4)$
3. In each part, find polar coordinates satisfying the stated conditions for the point whose rectangular coordinates are $(1, \sqrt{3})$:  
   (a) $r \ge 0$ and $0 \le \theta < 2\pi$  
   (b) $r \le 0$ and $0 \le \theta < 2\pi$
4. In each part, state the name that describes the polar curve most precisely: a rose, a line, a circle, a limaçon, a cardioid, a spiral, a lemniscate, or none of these.  
   (a) $r = 1 - \theta$ (b) $r = 1 + 2\sin\theta$ (c) $r = \sin 2\theta$ (d) $r = \cos^2\theta$ (e) $r = \csc\theta$ (f) $r = 2 + 2\cos\theta$ (g) $r = -2\sin\theta$

---

### EXERCISE SET 10.2

**1–2 Plot the points in polar coordinates.**
1. (a) $(3, \pi/4)$ (b) $(5, 2\pi/3)$ (c) $(1, \pi/2)$ (d) $(4, 7\pi/6)$ (e) $(-6, -\pi)$ (f) $(-1, 9\pi/4)$
2. (a) $(2, -\pi/3)$ (b) $(3/2, -7\pi/4)$ (c) $(-3, 3\pi/2)$ (d) $(-5, -\pi/6)$ (e) $(2, 4\pi/3)$ (f) $(0, \pi)$

**3–4 Find the rectangular coordinates of the points whose polar coordinates are given.**
3. (a) $(6, \pi/6)$ (b) $(7, 2\pi/3)$ (c) $(-6, -5\pi/6)$ (d) $(0, -\pi)$ (e) $(7, 17\pi/6)$ (f) $(-5, 0)$
4. (a) $(-2, \pi/4)$ (b) $(6, -\pi/4)$ (c) $(4, 9\pi/4)$ (d) $(3, 0)$ (e) $(-4, -3\pi/2)$ (f) $(0, 3\pi)$

5. In each part, a point is given in rectangular coordinates. Find two pairs of polar coordinates for the point, one pair satisfying $r \ge 0$ and $0 \le \theta < 2\pi$, and the second pair satisfying $r \ge 0$ and $-2\pi < \theta \le 0$.  
   (a) $(-5, 0)$ (b) $(2\sqrt{3}, -2)$ (c) $(0, -2)$ (d) $(-8, -8)$ (e) $(-3, 3\sqrt{3})$ (f) $(1, 1)$

6. In each part, find polar coordinates satisfying the stated conditions for the point whose rectangular coordinates are $(-\sqrt{3}, 1)$.  
   (a) $r \ge 0$ and $0 \le \theta < 2\pi$  
   (b) $r \le 0$ and $0 \le \theta < 2\pi$  
   (c) $r \ge 0$ and $-2\pi < \theta \le 0$  
   (d) $r \le 0$ and $-\pi < \theta \le \pi$

**7–8 Use a calculating utility, where needed, to approximate the polar coordinates of the points whose rectangular coordinates are given.**
7. (a) $(3, 4)$ (b) $(6, -8)$ (c) $(-1, \tan^{-1} 1)$
8. (a) $(-3, 4)$ (b) $(-3, 1.7)$ (c) $(2, \sin^{-1}(1/2))$

**9–10 Identify the curve by transforming the given polar equation to rectangular coordinates.**
9. (a) $r = 2$  
   (b) $r\sin\theta = 4$  
   (c) $r = 3\cos\theta$  
   (d) $r = \frac{6}{3\cos\theta + 2\sin\theta}$
10. (a) $r = 5\sec\theta$  
    (b) $r = 2\sin\theta$  
    (c) $r = 4\cos\theta + 4\sin\theta$  
    (d) $r = \sec\theta\tan\theta$

**11–12 Express the given equations in polar coordinates.**
11. (a) $x = 3$ (b) $x^2 + y^2 = 7$ (c) $x^2 + y^2 + 6y = 0$ (d) $9xy = 4$
12. (a) $y = -3$ (b) $x^2 + y^2 = 5$ (c) $x^2 + y^2 + 4x = 0$ (d) $x^2(x^2 + y^2) = y^2$

#### FOCUS ON CONCEPTS
**13–16 A graph is given in a rectangular $\theta r$-coordinate system. Sketch the corresponding graph in polar coordinates.**
13. Sinusoidal wave between $-3$ and 3.
14. Sinusoidal wave between $-2$ and 2.
15. Wave shifted vertically between $-1$ and 7.
16. Sine wave between 2 and 4.

**17–20 Find an equation for the given polar graph.**
17. (a) Circle radius $5/2$ on $x$-axis: $r = 5\cos\theta$. (b) Circle radius 3 on $y$-axis: $r = 6\sin\theta$. (c) Cardioid: $r = 1 + \cos\theta$ (or $r = 2(1+\cos\theta)$ depending on scale).
18. (a) Limaçon with inner loop (b) Circle (c) Three-petal rose
19. (a) Four-petal rose (b) Limaçon (c) Lemniscate
20. (a) Cardioid (b) Five-petal rose (c) Circle

**21–46 Sketch the curve in polar coordinates.**
21. $\theta = \pi/3$
22. $\theta = -3\pi/4$
23. $r = 3$
24. $r = 4\cos\theta$
25. $r = 6\sin\theta$
26. $r - 2 = 2\cos\theta$
27. $r = 3(1 + \sin\theta)$
28. $r = 5 - 5\sin\theta$
29. $r = 4 - 4\cos\theta$
30. $r = 1 + 2\sin\theta$
31. $r = -1 - \cos\theta$
32. $r = 4 + 3\cos\theta$
33. $r = 3 - \sin\theta$
34. $r = 3 + 4\cos\theta$
35. $r - 5 = 3\sin\theta$
36. $r = 5 - 2\cos\theta$
37. $r = -3 - 4\sin\theta$
38. $r^2 = \cos 2\theta$
39. $r^2 = 16\sin 2\theta$
40. $r = 4\theta \quad (\theta \ge 0)$
41. $r = 4\theta \quad (\theta \le 0)$
42. $r = 4\theta$
43. $r = -2\cos 2\theta$
44. $r = 3\sin 2\theta$
45. $r = 9\sin 4\theta$
46. $r = 2\cos 3\theta$

**47–50 True–False Determine whether the statement is true or false. Explain your answer.**
47. The polar coordinate pairs $(-1, \pi/3)$ and $(1, -2\pi/3)$ describe the same point.
48. If the graph of $r = f(\theta)$ drawn in rectangular $\theta r$-coordinates is symmetric about the $r$-axis, then the graph of $r = f(\theta)$ drawn in polar coordinates is symmetric about the $x$-axis.
49. The portion of the polar graph of $r = \sin 2\theta$ for values of $\theta$ between $\pi/2$ and $\pi$ is contained in the second quadrant.
50. The graph of a dimpled limaçon passes through the polar origin.

**51–55 Determine a shortest parameter interval on which a complete graph of the polar equation can be generated, and then use a graphing utility to generate the polar graph.**
51. $r = \cos(\theta/2)$
52. $r = \sin(\theta/2)$
53. $r = 1 - 2\sin(\theta/4)$
54. $r = 0.5 + \cos(\theta/3)$
55. $r = \cos(\theta/5)$

56. The accompanying figure shows the graph of the "butterfly curve"
    $$r = e^{\cos\theta} - 2\cos 4\theta + \sin^3\left(\frac{\theta}{4}\right)$$
    Determine a shortest parameter interval on which the complete butterfly can be generated, and then check your answer using a graphing utility.

57. The accompanying figure shows the Archimedean spiral $r = \theta/2$ produced with a graphing calculator.  
    (a) What interval of values for $\theta$ do you think was used to generate the graph?  
    (b) Duplicate the graph with your own graphing utility.

58. Find equations for the two families of circles in the accompanying figure.

59. (a) Show that if $a$ varies, then the polar equation
    $$r = a\sec\theta \quad (-\pi/2 < \theta < \pi/2)$$
    describes a family of lines perpendicular to the polar axis.  
    (b) Show that if $b$ varies, then the polar equation
    $$r = b\csc\theta \quad (0 < \theta < \pi)$$
    describes a family of lines parallel to the polar axis.

#### FOCUS ON CONCEPTS
60. The accompanying figure shows graphs of the Archimedean spiral $r = \theta$ and the parabolic spiral $r = \sqrt{\theta}$. Which is which? Explain your reasoning.

**61–62 A polar graph of $r = f(\theta)$ is given over the stated interval. Sketch the graph of (a) $r = f(-\theta)$ (b) $r = f(\theta - \pi/2)$ (c) $r = f(\theta + \pi/2)$ (d) $r = -f(\theta)$.**
61. $0 \le \theta \le \pi/2$
62. $\pi/2 \le \theta \le \pi$

**63–64 Use the polar graph from the indicated exercise to sketch the graph of (a) $r = f(\theta) + 1$ (b) $r = 2f(\theta) - 1$.**
63. Exercise 61
64. Exercise 62

65. Show that if the polar graph of $r = f(\theta)$ is rotated counterclockwise around the origin through an angle $\alpha$, then $r = f(\theta - \alpha)$ is an equation for the rotated curve. [*Hint:* If $(r_0, \theta_0)$ is any point on the original graph, then $(r_0, \theta_0 + \alpha)$ is a point on the rotated graph.]

66. Use the result in Exercise 65 to find an equation for the lemniscate that results when the lemniscate in Example 9 is rotated counterclockwise through an angle of $\pi/2$.

67. Use the result in Exercise 65 to find an equation for the cardioid $r = 1 + \cos\theta$ after it has been rotated through the given angle, and check your answer with a graphing utility:  
    (a) $\pi/4$ (b) $\pi/2$ (c) $\pi$ (d) $5\pi/4$

68. (a) Show that if $A$ and $B$ are not both zero, then the graph of the polar equation
    $$r = A\sin\theta + B\cos\theta$$
    is a circle. Find its radius.  
    (b) Derive Formulas (4) and (5) from the formula given in part (a).

69. Find the highest point on the cardioid $r = 1 + \cos\theta$.
70. Find the leftmost point on the upper half of the cardioid $r = 1 + \cos\theta$.

71. Show that in a polar coordinate system the distance $d$ between the points $(r_1, \theta_1)$ and $(r_2, \theta_2)$ is
    $$d = \sqrt{r_1^2 + r_2^2 - 2r_1 r_2\cos(\theta_1 - \theta_2)}$$

**72–74 Use the formula obtained in Exercise 71 to find the distance between the two points indicated in polar coordinates.**
72. $(3, \pi/6)$ and $(2, \pi/3)$
73. Successive tips of the four-petal rose $r = \cos 2\theta$. Check your answer using geometry.
74. Successive tips of the three-petal rose $r = \sin 3\theta$. Check your answer using trigonometry.

75. In the late seventeenth century the Italian astronomer Giovanni Domenico Cassini (1625–1712) introduced the family of curves
    $$(x^2 + y^2 + a^2)^2 - b^4 - 4a^2 x^2 = 0 \quad (a > 0, b > 0)$$
    in his studies of the relative motions of the Earth and the Sun. These curves, which are called **Cassini ovals**, have one of three basic shapes.  
    (a) Show that if $a = b$, then the polar equation of the Cassini oval is $r^2 = 2a^2\cos 2\theta$, which is a lemniscate.  
    (b) Use the formula in Exercise 71 to show that the lemniscate in part (a) is the curve traced by a point that moves in such a way that the product of its distances from the polar points $(a, 0)$ and $(a, \pi)$ is $a^2$.

**76–77 Vertical and horizontal asymptotes of polar curves can sometimes be detected by investigating the behavior of $x = r\cos\theta$ and $y = r\sin\theta$ as $\theta$ varies. This idea is used in these exercises.**
76. Show that the hyperbolic spiral $r = 1/\theta \; (\theta > 0)$ has a horizontal asymptote at $y = 1$ by showing that $y \to 1$ and $x \to +\infty$ as $\theta \to 0^+$. Confirm this result by generating the spiral with a graphing utility.
77. Show that the spiral $r = 1/\theta^2$ does not have any horizontal asymptotes.

78. Prove that a rose with an even number of petals is traced out exactly once as $\theta$ varies over the interval $0 \le \theta < 2\pi$ and a rose with an odd number of petals is traced out exactly once as $\theta$ varies over the interval $0 \le \theta < \pi$.

79. (a) Use a graphing utility to confirm that the graph of $r = 2 - \sin(\theta/2) \; (0 \le \theta \le 4\pi)$ is symmetric about the $x$-axis.  
    (b) Show that replacing $\theta$ by $-\theta$ in the polar equation $r = 2 - \sin(\theta/2)$ does not produce an equivalent equation. Why does this not contradict the symmetry demonstrated in part (a)?

80. **Writing.** Use a graphing utility to investigate how the family of polar curves $r = 1 + a\cos n\theta$ is affected by changing the values of $a$ and $n$, where $a$ is a positive real number and $n$ is a positive integer. Write a brief paragraph to explain your conclusions.
81. **Writing.** Why do you think the adjective "polar" was chosen in the name "polar coordinates"?

#### QUICK CHECK ANSWERS 10.2
1. (a) $r\cos\theta; \quad r\sin\theta$ (b) $x^2 + y^2; \quad y/x$
2. (a) $(2, 2\sqrt{3})$ (b) $(\sqrt{3}, -1)$ (c) $(-3, -3\sqrt{3})$ (d) $(-2\sqrt{2}, -2\sqrt{2})$
3. (a) $(2, \pi/3)$ (b) $(-2, 4\pi/3)$
4. (a) spiral (b) limaçon (c) rose (d) none of these (e) line (f) cardioid (g) circle

---

## 10.3 TANGENT LINES, ARC LENGTH, AND AREA FOR POLAR CURVES

In this section we will derive the formulas required to find slopes, tangent lines, and arc lengths of polar curves. We will then show how to find areas of regions that are bounded by polar curves.

### TANGENT LINES TO POLAR CURVES

Our first objective in this section is to find a method for obtaining slopes of tangent lines to polar curves of the form $r = f(\theta)$ in which $r$ is a differentiable function of $\theta$. We showed in the last section that a curve of this form can be expressed parametrically in terms of the parameter $\theta$ by substituting $f(\theta)$ for $r$ in the equations $x = r\cos\theta$ and $y = r\sin\theta$. This yields
$$x = f(\theta)\cos\theta, \quad y = f(\theta)\sin\theta$$
from which we obtain
$$\frac{dx}{d\theta} = -f(\theta)\sin\theta + f'(\theta)\cos\theta = -r\sin\theta + \frac{dr}{d\theta}\cos\theta$$
$$\frac{dy}{d\theta} = f(\theta)\cos\theta + f'(\theta)\sin\theta = r\cos\theta + \frac{dr}{d\theta}\sin\theta \tag{1}$$
Thus, if $dx/d\theta$ and $dy/d\theta$ are continuous and if $dx/d\theta \neq 0$, then $y$ is a differentiable function of $x$, and Formula (4) in Section 10.1 with $\theta$ in place of $t$ yields
$$\frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta} = \frac{r\cos\theta + \sin\theta\frac{dr}{d\theta}}{-r\sin\theta + \cos\theta\frac{dr}{d\theta}} \tag{2}$$

#### Example 1
Find the slope of the tangent line to the circle $r = 4\cos\theta$ at the point where $\theta = \pi/4$.

**Solution.** From (2) with $r = 4\cos\theta$, so that $dr/d\theta = -4\sin\theta$, we obtain
$$\frac{dy}{dx} = \frac{4\cos^2\theta - 4\sin^2\theta}{-8\sin\theta\cos\theta} = -\frac{\cos^2\theta - \sin^2\theta}{2\sin\theta\cos\theta}$$
Using the double-angle formulas for sine and cosine,
$$\frac{dy}{dx} = -\frac{\cos 2\theta}{\sin 2\theta} = -\cot 2\theta$$
Thus, at the point where $\theta = \pi/4$ the slope of the tangent line is
$$m = \left.\frac{dy}{dx}\right|_{\theta=\pi/4} = -\cot\frac{\pi}{2} = 0$$
which implies that the circle has a horizontal tangent line at the point where $\theta = \pi/4$ (Figure 10.3.1).

#### Example 2
Find the points on the cardioid $r = 1 - \cos\theta$ at which there is a horizontal tangent line, a vertical tangent line, or a singular point.

**Solution.** A horizontal tangent line will occur where $dy/d\theta = 0$ and $dx/d\theta \neq 0$, a vertical tangent line where $dy/d\theta \neq 0$ and $dx/d\theta = 0$, and a singular point where $dy/d\theta = 0$ and $dx/d\theta = 0$. We could find these derivatives from the formulas in (1). However, an alternative approach is to go back to basic principles and express the cardioid parametrically by substituting $r = 1 - \cos\theta$ in the conversion formulas $x = r\cos\theta$ and $y = r\sin\theta$. This yields
$$x = (1 - \cos\theta)\cos\theta, \quad y = (1 - \cos\theta)\sin\theta \quad (0 \le \theta \le 2\pi)$$
Differentiating these equations with respect to $\theta$ and then simplifying yields (verify)
$$\frac{dx}{d\theta} = \sin\theta(2\cos\theta - 1), \quad \frac{dy}{d\theta} = (1 - \cos\theta)(1 + 2\cos\theta)$$
Thus, $dx/d\theta = 0$ if $\sin\theta = 0$ or $\cos\theta = 1/2$, and $dy/d\theta = 0$ if $\cos\theta = 1$ or $\cos\theta = -1/2$. The solutions of $dx/d\theta = 0$ on the interval $0 \le \theta \le 2\pi$ are
$$\frac{dx}{d\theta} = 0: \quad \theta = 0, \; \frac{\pi}{3}, \; \pi, \; \frac{5\pi}{3}, \; 2\pi$$
and the solutions of $dy/d\theta = 0$ on the interval $0 \le \theta \le 2\pi$ are
$$\frac{dy}{d\theta} = 0: \quad \theta = 0, \; \frac{2\pi}{3}, \; \frac{4\pi}{3}, \; 2\pi$$
Thus, horizontal tangent lines occur at $\theta = 2\pi/3$ and $\theta = 4\pi/3$; vertical tangent lines occur at $\theta = \pi/3, \pi,$ and $5\pi/3$; and singular points occur at $\theta = 0$ and $\theta = 2\pi$ (Figure 10.3.2). Note, however, that $r = 0$ at both singular points, so there is really only one singular point on the cardioid—the pole.

---

### TANGENT LINES TO POLAR CURVES AT THE ORIGIN

Formula (2) reveals some useful information about the behavior of a polar curve $r = f(\theta)$ that passes through the origin. If we assume that $r = 0$ and $dr/d\theta \neq 0$ when $\theta = \theta_0$, then it follows from Formula (2) that the slope of the tangent line to the curve at $\theta = \theta_0$ is
$$\frac{dy}{dx} = \frac{0 + \sin\theta_0\frac{dr}{d\theta}}{0 + \cos\theta_0\frac{dr}{d\theta}} = \frac{\sin\theta_0}{\cos\theta_0} = \tan\theta_0$$
(Figure 10.3.3). However, $\tan\theta_0$ is also the slope of the line $\theta = \theta_0$, so we can conclude that this line is tangent to the curve at the origin. Thus, we have established the following result.

> **10.3.1 THEOREM**  
> If the polar curve $r = f(\theta)$ passes through the origin at $\theta = \theta_0$, and if $dr/d\theta \neq 0$ at $\theta = \theta_0$, then the line $\theta = \theta_0$ is tangent to the curve at the origin.

This theorem tells us that equations of the tangent lines at the origin to the curve $r = f(\theta)$ can be obtained by solving the equation $f(\theta) = 0$. It is important to keep in mind, however, that $r = f(\theta)$ may be zero for more than one value of $\theta$, so there may be more than one tangent line at the origin.

#### Example 3
The three-petal rose $r = \sin 3\theta$ in Figure 10.3.4 has three tangent lines at the origin, which can be found by solving the equation
$$\sin 3\theta = 0$$
It was shown in Exercise 78 of Section 10.2 that the complete rose is traced once as $\theta$ varies over the interval $0 \le \theta < \pi$, so we need only look for solutions in this interval:
$$\theta = 0, \quad \theta = \frac{\pi}{3}, \quad \text{and} \quad \theta = \frac{2\pi}{3}$$
Since $dr/d\theta = 3\cos 3\theta \neq 0$ for these values of $\theta$, these three lines are tangent to the rose at the origin.

---

### ARC LENGTH OF A POLAR CURVE

A formula for the arc length of a polar curve $r = f(\theta)$ can be derived by expressing the curve in parametric form and applying Formula (9) of Section 10.1 for the arc length of a parametric curve.

> **10.3.2 THEOREM (Arc Length Formula for Polar Curves)**  
> If no segment of the polar curve $r = f(\theta)$ is traced more than once as $\theta$ increases from $\alpha$ to $\beta$, and if $dr/d\theta$ is continuous for $\alpha \le \theta \le \beta$, then the arc length $L$ from $\theta = \alpha$ to $\theta = \beta$ is
> $$L = \int_\alpha^\beta \sqrt{[f(\theta)]^2 + [f'(\theta)]^2}\,d\theta = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta \tag{3}$$

#### Example 4
Find the arc length of the spiral $r = e^\theta$ in Figure 10.3.5 between $\theta = 0$ and $\theta = \pi$.

**Solution.**
$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta = \int_0^\pi \sqrt{(e^\theta)^2 + (e^\theta)^2}\,d\theta = \int_0^\pi \sqrt{2}e^\theta\,d\theta = \left[\sqrt{2}e^\theta\right]_0^\pi = \sqrt{2}(e^\pi - 1) \approx 31.3$$

#### Example 5
Find the total arc length of the cardioid $r = 1 + \cos\theta$.

**Solution.** The cardioid is traced out once as $\theta$ varies from $\theta = 0$ to $\theta = 2\pi$. Thus,
$$L = \int_0^{2\pi} \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta = \int_0^{2\pi} \sqrt{(1 + \cos\theta)^2 + (-\sin\theta)^2}\,d\theta = \sqrt{2}\int_0^{2\pi} \sqrt{1 + \cos\theta}\,d\theta$$
$$= 2\int_0^{2\pi} \sqrt{\cos^2\frac{1}{2}\theta}\,d\theta = 2\int_0^{2\pi} \left|\cos\frac{1}{2}\theta\right|\,d\theta$$
Since $\cos\frac{1}{2}\theta$ changes sign at $\pi$, and the cardioid is symmetric about the polar axis (Figure 10.3.6):
$$L = 2\int_0^{2\pi} \left|\cos\frac{1}{2}\theta\right|\,d\theta = 4\int_0^\pi \cos\frac{1}{2}\theta\,d\theta = \left[8\sin\frac{1}{2}\theta\right]_0^\pi = 8$$

---

### AREA IN POLAR COORDINATES

> **10.3.3 AREA PROBLEM IN POLAR COORDINATES**  
> Suppose that $\alpha$ and $\beta$ are angles that satisfy the condition $\alpha < \beta \le \alpha + 2\pi$ and suppose that $f(\theta)$ is continuous and nonnegative for $\alpha \le \theta \le \beta$. Find the area of the region $R$ enclosed by the polar curve $r = f(\theta)$ and the rays $\theta = \alpha$ and $\theta = \beta$ (Figure 10.3.7).

Partitioning the region into $n$ wedges with central angles $\Delta\theta_1, \Delta\theta_2, \dots, \Delta\theta_n$ and approximating the area $A_k$ of the $k$th wedge by the area of a circular sector of radius $f(\theta_k^*)$ and angle $\Delta\theta_k$:
$$A = \sum_{k=1}^n A_k \approx \sum_{k=1}^n \frac{1}{2}[f(\theta_k^*)]^2\,\Delta\theta_k$$
Taking the limit as $\max\Delta\theta_k \to 0$:
$$A = \lim_{\max\Delta\theta_k \to 0} \sum_{k=1}^n \frac{1}{2}[f(\theta_k^*)]^2\,\Delta\theta_k = \int_\alpha^\beta \frac{1}{2}[f(\theta)]^2\,d\theta$$

> **10.3.4 THEOREM (Area in Polar Coordinates)**  
> If $\alpha$ and $\beta$ are angles that satisfy the condition $\alpha < \beta \le \alpha + 2\pi$, and if $f(\theta)$ is continuous and either nonnegative or nonpositive for $\alpha \le \theta \le \beta$, then the area $A$ of the region $R$ enclosed by the polar curve $r = f(\theta) \; (\alpha \le \theta \le \beta)$ and the lines $\theta = \alpha$ and $\theta = \beta$ is
> $$A = \int_\alpha^\beta \frac{1}{2}[f(\theta)]^2\,d\theta = \int_\alpha^\beta \frac{1}{2}r^2\,d\theta \tag{6}$$

#### Area in Polar Coordinates: Limits of Integration
* **Step 1.** Sketch the region $R$ whose area is to be determined.
* **Step 2.** Draw an arbitrary "radial line" from the pole to the boundary curve $r = f(\theta)$.
* **Step 3.** Ask, "Over what interval of values must $\theta$ vary in order for the radial line to sweep out the region $R$?"
* **Step 4.** Your answer in Step 3 will determine the lower and upper limits of integration.

#### Example 6
Find the area of the region in the first quadrant that is within the cardioid $r = 1 - \cos\theta$.

**Solution.** From (6) with $\alpha = 0$ and $\beta = \pi/2$:
$$A = \int_0^{\pi/2} \frac{1}{2}r^2\,d\theta = \frac{1}{2}\int_0^{\pi/2}(1 - \cos\theta)^2\,d\theta = \frac{1}{2}\int_0^{\pi/2}(1 - 2\cos\theta + \cos^2\theta)\,d\theta$$
$$= \frac{1}{2}\int_0^{\pi/2}\left(\frac{3}{2} - 2\cos\theta + \frac{1}{2}\cos 2\theta\right)d\theta = \frac{1}{2}\left[\frac{3}{2}\theta - 2\sin\theta + \frac{1}{4}\sin 2\theta\right]_0^{\pi/2} = \frac{3}{8}\pi - 1$$

#### Example 7
Find the entire area within the cardioid of Example 6.

**Solution.** For the radial line to sweep out the entire cardioid, $\theta$ must vary from 0 to $2\pi$:
$$A = \int_0^{2\pi} \frac{1}{2}r^2\,d\theta = \frac{1}{2}\int_0^{2\pi}(1 - \cos\theta)^2\,d\theta = \frac{3\pi}{2}$$
*Alternative Solution:* By symmetry about the $x$-axis, $A = 2\int_0^\pi \frac{1}{2}r^2\,d\theta = \int_0^\pi (1 - \cos\theta)^2\,d\theta = \frac{3\pi}{2}$.

#### Example 8
Find the area of the region enclosed by the rose curve $r = \cos 2\theta$.

**Solution.** The area in the first quadrant swept out for $0 \le \theta \le \pi/4$ is one-eighth of the total area inside the rose. Thus,
$$A = 8\int_0^{\pi/4} \frac{1}{2}r^2\,d\theta = 4\int_0^{\pi/4}\cos^2 2\theta\,d\theta = 2\int_0^{\pi/4}(1 + \cos 4\theta)\,d\theta = \left[2\theta + \frac{1}{2}\sin 4\theta\right]_0^{\pi/4} = \frac{\pi}{2}$$

#### Example 9
Find the area of the region that is inside of the cardioid $r = 4 + 4\cos\theta$ and outside of the circle $r = 6$.

**Solution.** Points of intersection: $4 + 4\cos\theta = 6 \implies \cos\theta = 1/2 \implies \theta = \pm\pi/3$.  
Integrating over $[-\pi/3, \pi/3]$:
$$A = \int_{-\pi/3}^{\pi/3} \frac{1}{2}(4 + 4\cos\theta)^2\,d\theta - \int_{-\pi/3}^{\pi/3} \frac{1}{2}(6)^2\,d\theta = \int_{-\pi/3}^{\pi/3}(16\cos\theta + 8\cos^2\theta - 10)\,d\theta$$
$$= [16\sin\theta + (4\theta + 2\sin 2\theta) - 10\theta]_{-\pi/3}^{\pi/3} = 18\sqrt{3} - 4\pi$$

---

### INTERSECTIONS OF POLAR GRAPHS

Because a point can be represented in different ways in polar coordinates, equating equations will not always produce all intersections. For example, $r = 1 - \cos\theta$ and $r = 1 + \cos\theta$ intersect at $(1, \pi/2), (1, 3\pi/2),$ and the pole (Figure 10.3.13). Equating formulas gives $\cos\theta = 0 \implies \theta = \pi/2, 3\pi/2$, which finds $(1, \pi/2)$ and $(1, 3\pi/2)$ but misses the pole. The pole is missed because $r = 1 - \cos\theta$ passes through the pole at $\theta = 0$ while $r = 1 + \cos\theta$ passes through the pole at $\theta = \pi$. Therefore, graphing is recommended when finding intersections.

---

### QUICK CHECK EXERCISES 10.3
*(See page 729 for answers.)*

1. (a) To obtain $dy/dx$ directly from the polar equation $r = f(\theta)$, we can use the formula
   $$\frac{dy}{dx} = \frac{dy/d\theta}{dx/d\theta} = \underline{\quad}$$
   (b) Use the formula in part (a) to find $dy/dx$ directly from the polar equation $r = \csc\theta$.
2. (a) What conditions on $f(\theta_0)$ and $f'(\theta_0)$ guarantee that the line $\theta = \theta_0$ is tangent to the polar curve $r = f(\theta)$ at the origin?  
   (b) What are the values of $\theta_0$ in $[0, 2\pi]$ at which the lines $\theta = \theta_0$ are tangent at the origin to the four-petal rose $r = \cos 2\theta$?
3. (a) To find the arc length $L$ of the polar curve $r = f(\theta) \; (\alpha \le \theta \le \beta)$, we can use the formula $L = \underline{\quad}$.  
   (b) The polar curve $r = \sec\theta \; (0 \le \theta \le \pi/4)$ has arc length $L = \underline{\quad}$.
4. The area of the region enclosed by a nonnegative polar curve $r = f(\theta) \; (\alpha \le \theta \le \beta)$ and the lines $\theta = \alpha$ and $\theta = \beta$ is given by the definite integral $\underline{\quad}$.
5. Find the area of the circle $r = a$ by integration.

---

### EXERCISE SET 10.3

**1–6 Find the slope of the tangent line to the polar curve for the given value of $\theta$.**
1. $r = 2\sin\theta; \quad \theta = \pi/6$
2. $r = 1 + \cos\theta; \quad \theta = \pi/2$
3. $r = 1/\theta; \quad \theta = 2$
4. $r = a\sec 2\theta; \quad \theta = \pi/6$
5. $r = \sin 3\theta; \quad \theta = \pi/4$
6. $r = 4 - 3\sin\theta; \quad \theta = \pi$

**7–8 Calculate the slopes of the tangent lines indicated in the accompanying figures.**
7. $r = 2 + 2\sin\theta$
8. $r = 1 - 2\sin\theta$

**9–10 Find polar coordinates of all points at which the polar curve has a horizontal or a vertical tangent line.**
9. $r = a(1 + \cos\theta)$
10. $r = a\sin\theta$

**11–12 Use a graphing utility to make a conjecture about the number of points on the polar curve at which there is a horizontal tangent line, and confirm your conjecture by finding appropriate derivatives.**
11. $r = \sin\theta\cos^2\theta$
12. $r = 1 - 2\sin\theta$

**13–18 Sketch the polar curve and find polar equations of the tangent lines to the curve at the pole.**
13. $r = 2\cos 3\theta$
14. $r = 4\sin\theta$
15. $r = 4\sqrt{\cos 2\theta}$
16. $r = \sin 2\theta$
17. $r = 1 - 2\cos\theta$
18. $r = 2\theta$

**19–22 Use Formula (3) to calculate the arc length of the polar curve.**
19. The entire circle $r = a$
20. The entire circle $r = 2a\cos\theta$
21. The entire cardioid $r = a(1 - \cos\theta)$
22. $r = e^{3\theta}$ from $\theta = 0$ to $\theta = 2$

23. (a) Show that the arc length of one petal of the rose $r = \cos n\theta$ is given by
    $$2\int_0^{\pi/(2n)} \sqrt{1 + (n^2 - 1)\sin^2 n\theta}\,d\theta$$
    (b) Use the numerical integration capability of a calculating utility to approximate the arc length of one petal of the four-petal rose $r = \cos 2\theta$.  
    (c) Use the numerical integration capability of a calculating utility to approximate the arc length of one petal of the $n$-petal rose $r = \cos n\theta$ for $n = 2, 3, 4, \dots, 20$; then make a conjecture about the limit of these arc lengths as $n \to +\infty$.

24. (a) Sketch the spiral $r = e^{-\theta/8} \; (0 \le \theta < +\infty)$.  
    (b) Find an improper integral for the total arc length of the spiral.  
    (c) Show that the integral converges and find the total arc length of the spiral.

25. Write down, but do not evaluate, an integral for the area of each shaded region:  
    (a) $r = 1 - \cos\theta$  
    (b) $r = 2\cos\theta$  
    (c) $r = \sin 2\theta$  
    (d) $r = \theta$  
    (e) $r = 1 - \sin\theta$  
    (f) $r = \cos 2\theta$

26. Find the area of the shaded region in Exercise 25(d).

27. In each part, find the area of the circle by integration:  
    (a) $r = 2a\sin\theta$  
    (b) $r = 2a\cos\theta$

28. (a) Show that $r = 2\sin\theta + 2\cos\theta$ is a circle.  
    (b) Find the area of the circle using a geometric formula and then by integration.

**29–34 Find the area of the region described.**
29. The region that is enclosed by the cardioid $r = 2 + 2\sin\theta$.
30. The region in the first quadrant within the cardioid $r = 1 + \cos\theta$.
31. The region enclosed by the rose $r = 4\cos 3\theta$.
32. The region enclosed by the rose $r = 2\sin 2\theta$.
33. The region enclosed by the inner loop of the limaçon $r = 1 + 2\cos\theta$. [*Hint:* $r \le 0$ over the interval of integration.]
34. The region swept out by a radial line from the pole to the curve $r = 2/\theta$ as $\theta$ varies over the interval $1 \le \theta \le 3$.

**35–38 Find the area of the shaded region.**
35. Between $r = \sqrt{\cos 2\theta}$ and $r = 2\cos\theta$.
36. Between $r = 1 + \cos\theta$ and $r = \cos\theta$.
37. Between $r = 4\sqrt{3}\sin\theta$ and $r = 4\cos\theta$.
38. Between $r = 1 + \cos\theta$ and $r = 3\cos\theta$.

**39–46 Find the area of the region described.**
39. The region inside the circle $r = 3\sin\theta$ and outside the cardioid $r = 1 + \sin\theta$.
40. The region outside the cardioid $r = 2 - 2\cos\theta$ and inside the circle $r = 4$.
41. The region inside the cardioid $r = 2 + 2\cos\theta$ and outside the circle $r = 3$.
42. The region that is common to the circles $r = 2\cos\theta$ and $r = 2\sin\theta$.
43. The region between the loops of the limaçon $r = \frac{1}{2} + \cos\theta$.
44. The region inside the cardioid $r = 2 + 2\cos\theta$ and to the right of the line $r\cos\theta = \frac{3}{2}$.
45. The region inside the circle $r = 2$ and to the right of the line $r = \sqrt{2}\sec\theta$.
46. The region inside the rose $r = 2a\cos 2\theta$ and outside the circle $r = a\sqrt{2}$.

**47–50 True–False Determine whether the statement is true or false. Explain your answer.**
47. The $x$-axis is tangent to the polar curve $r = \cos(\theta/2)$ at $\theta = 3\pi$.
48. The arc length of the polar curve $r = \sqrt{\theta}$ for $0 \le \theta \le \pi/2$ is given by
    $$L = \int_0^{\pi/2} \sqrt{1 + \frac{1}{4\theta}}\,d\theta$$
49. The area of a sector with central angle $\theta$ taken from a circle of radius $r$ is $\theta r^2$.
50. The expression
    $$\frac{1}{2}\int_{-\pi/4}^{\pi/4} (1 - \sqrt{2}\cos\theta)^2\,d\theta$$
    computes the area enclosed by the inner loop of the limaçon $r = 1 - \sqrt{2}\cos\theta$.

#### FOCUS ON CONCEPTS
51. (a) Find the error: The area that is inside the lemniscate $r^2 = a^2\cos 2\theta$ is
    $$A = \int_0^{2\pi} \frac{1}{2}r^2\,d\theta = \int_0^{2\pi} \frac{1}{2}a^2\cos 2\theta\,d\theta = \left[\frac{1}{4}a^2\sin 2\theta\right]_0^{2\pi} = 0$$
    (b) Find the correct area.  
    (c) Find the area inside the lemniscate $r^2 = 4\cos 2\theta$ and outside the circle $r = \sqrt{2}$.

52. Find the area inside the curve $r^2 = \sin 2\theta$.

53. A radial line is drawn from the origin to the spiral $r = a\theta \; (a > 0 \text{ and } \theta \ge 0)$. Find the area swept out during the second revolution of the radial line that was not swept out during the first revolution.

54. Suppose that a rod with one end fixed at the pole of a polar coordinate system rotates counterclockwise at the constant rate of $1\text{ rad/s}$. At time $t = 0$ a bug on the rod is $10\text{ mm}$ from the pole and is moving outward along the rod at the constant speed of $2\text{ mm/s}$.  
    (a) Find an equation of the form $r = f(\theta)$ for the path of motion of the bug, assuming that $\theta = 0$ when $t = 0$.  
    (b) Find the distance the bug travels along the path in part (a) during the first $5\text{ s}$. Round your answer to the nearest tenth of a millimeter.

55. (a) Show that the Folium of Descartes $x^3 - 3xy + y^3 = 0$ can be expressed in polar coordinates as
    $$r = \frac{3\sin\theta\cos\theta}{\cos^3\theta + \sin^3\theta}$$
    (b) Use a CAS to show that the area inside of the loop is $\frac{3}{2}$.

56. (a) What is the area that is enclosed by one petal of the rose $r = a\cos n\theta$ if $n$ is an even integer?  
    (b) What is the area that is enclosed by one petal of the rose $r = a\cos n\theta$ if $n$ is an odd integer?  
    (c) Use a CAS to show that the total area enclosed by the rose $r = a\cos n\theta$ is $\pi a^2/2$ if the number of petals is even.  
    (d) Use a CAS to show that the total area enclosed by the rose $r = a\cos n\theta$ is $\pi a^2/4$ if the number of petals is odd.

57. One of the most famous problems in Greek antiquity was "squaring the circle," that is, using a straightedge and compass to construct a square whose area is equal to that of a given circle. It was proved in the nineteenth century that no such construction is possible. However, show that the shaded areas in Figure Ex-57 are equal, thereby "squaring the crescent."

58. Use a graphing utility to generate the polar graph of the equation $r = \cos 3\theta + 2$, and find the area that it encloses.

59. Use a graphing utility to generate the graph of the bifolium $r = 2\cos\theta\sin^2\theta$, and find the area of the upper loop.

60. Use Formula (9) of Section 10.1 to derive the arc length formula for polar curves, Formula (3).

61. Let $P(r, \theta)$ be a point on the polar curve $r = f(\theta)$, let $\psi$ be the smallest counterclockwise angle from the extended radius $OP$ to the tangent line at $P$, and let $\phi$ be the angle of inclination of the tangent line. Derive the formula
    $$\tan\psi = \frac{r}{dr/d\theta}$$
    by substituting $\tan\phi$ for $dy/dx$ in Formula (2) and applying the trigonometric identity
    $$\tan(\phi - \theta) = \frac{\tan\phi - \tan\theta}{1 + \tan\phi\tan\theta}$$

**62–63 Use the formula for $\psi$ obtained in Exercise 61.**
62. (a) Use the trigonometric identity $\tan\frac{\theta}{2} = \frac{1 - \cos\theta}{\sin\theta}$ to show that if $(r, \theta)$ is a point on the cardioid $r = 1 - \cos\theta \; (0 \le \theta < 2\pi)$, then $\psi = \theta/2$.  
    (b) Sketch the cardioid and show the angle $\psi$ at the points where the cardioid crosses the $y$-axis.  
    (c) Find the angle $\psi$ at the points where the cardioid crosses the $y$-axis.

63. Show that for a logarithmic spiral $r = ae^{b\theta}$, the angle from the radial line to the tangent line is constant along the spiral (see Figure Ex-63). [*Note:* For this reason, logarithmic spirals are sometimes called **equiangular spirals**.]

64. (a) In the discussion associated with Exercises 75–80 of Section 10.1, formulas were given for the area of the surface of revolution that is generated by revolving a parametric curve about the $x$-axis or $y$-axis. Use those formulas to derive the following formulas for the areas of the surfaces of revolution that are generated by revolving the portion of the polar curve $r = f(\theta)$ from $\theta = \alpha$ to $\theta = \beta$ about the polar axis and about the line $\theta = \pi/2$:
    $$S = \int_\alpha^\beta 2\pi r\sin\theta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta \quad (\text{About } \theta = 0)$$
    $$S = \int_\alpha^\beta 2\pi r\cos\theta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta \quad (\text{About } \theta = \pi/2)$$
    (b) State conditions under which these formulas hold.

**65–68 Sketch the surface, and use the formulas in Exercise 64 to find the surface area.**
65. The surface generated by revolving the circle $r = \cos\theta$ about the line $\theta = \pi/2$.
66. The surface generated by revolving the spiral $r = e^\theta \; (0 \le \theta \le \pi/2)$ about the line $\theta = \pi/2$.
67. The "apple" generated by revolving the upper half of the cardioid $r = 1 - \cos\theta \; (0 \le \theta \le \pi)$ about the polar axis.
68. The sphere of radius $a$ generated by revolving the semicircle $r = a$ in the upper half-plane about the polar axis.

69. **Writing.**  
    (a) Show that if $0 \le \theta_1 < \theta_2 \le \pi$ and if $r_1$ and $r_2$ are positive, then the area $A$ of a triangle with vertices $(0, 0), (r_1, \theta_1),$ and $(r_2, \theta_2)$ is
    $$A = \frac{1}{2}r_1 r_2\sin(\theta_2 - \theta_1)$$
    (b) Use the formula obtained in part (a) to describe an approach to answer Area Problem 10.3.3 that uses an approximation of the region $R$ by triangles instead of circular wedges. Reconcile your approach with Formula (6).

70. **Writing.** In order to find the area of a region bounded by two polar curves it is often necessary to determine their points of intersection. Give an example to illustrate that the points of intersection of curves $r = f(\theta)$ and $r = g(\theta)$ may not coincide with solutions to $f(\theta) = g(\theta)$. Discuss some strategies for determining intersection points of polar curves and provide examples to illustrate your strategies.

#### QUICK CHECK ANSWERS 10.3
1. (a) $\frac{r\cos\theta + \sin\theta(dr/d\theta)}{-r\sin\theta + \cos\theta(dr/d\theta)}$ (b) $\frac{dy}{dx} = 0$
2. (a) $f(\theta_0) = 0, \; f'(\theta_0) \neq 0$ (b) $\theta_0 = \frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$
3. (a) $\int_\alpha^\beta \sqrt{r^2 + (dr/d\theta)^2}\,d\theta$ (b) 1
4. $\int_\alpha^\beta \frac{1}{2}[f(\theta)]^2\,d\theta = \int_\alpha^\beta \frac{1}{2}r^2\,d\theta$
5. $\int_0^{2\pi} \frac{1}{2}a^2\,d\theta = \pi a^2$

---

## 10.4 CONIC SECTIONS

In this section we will discuss some of the basic geometric properties of parabolas, ellipses, and hyperbolas. These curves play an important role in calculus and also arise naturally in a broad range of applications in such fields as planetary motion, design of telescopes and antennas, geodetic positioning, and medicine, to name a few.

### CONIC SECTIONS

Circles, ellipses, parabolas, and hyperbolas are called **conic sections** or **conics** because they can be obtained as intersections of a plane with a double-napped circular cone (Figure 10.4.1). If the plane passes through the vertex of the double-napped cone, then the intersection is a point, a pair of intersecting lines, or a single line. These are called **degenerate conic sections**.

---

### DEFINITIONS OF THE CONIC SECTIONS

Although we could derive properties of parabolas, ellipses, and hyperbolas by defining them as intersections with a double-napped cone, it will be better suited to calculus if we begin with equivalent definitions that are based on their geometric properties.

> **10.4.1 DEFINITION**  
> A **parabola** is the set of all points in the plane that are equidistant from a fixed line and a fixed point not on the line.

The line is called the **directrix** of the parabola, and the point is called the **focus** (Figure 10.4.2). A parabola is symmetric about the line that passes through the focus at right angles to the directrix. This line, called the **axis** or the **axis of symmetry** of the parabola, intersects the parabola at a point called the **vertex**.

> **10.4.2 DEFINITION**  
> An **ellipse** is the set of all points in the plane, the sum of whose distances from two fixed points is a given positive constant that is greater than the distance between the fixed points.

The two fixed points are called the **foci** (plural of "focus") of the ellipse, and the midpoint of the line segment joining the foci is called the **center** (Figure 10.4.3a). To help visualize Definition 10.4.2, imagine that two ends of a string are tacked to the foci and a pencil traces a curve as it is held tight against the string (Figure 10.4.3b). The resulting curve will be an ellipse since the sum of the distances to the foci is a constant, namely, the total length of the string. Note that if the foci coincide, the ellipse reduces to a circle. For ellipses other than circles, the line segment through the foci and across the ellipse is called the **major axis** (Figure 10.4.3c), and the line segment across the ellipse, through the center, and perpendicular to the major axis is called the **minor axis**. The endpoints of the major axis are called **vertices**.

> **10.4.3 DEFINITION**  
> A **hyperbola** is the set of all points in the plane, the difference of whose distances from two fixed distinct points is a given positive constant that is less than the distance between the fixed points.

The two fixed points are called the **foci** of the hyperbola, and the term "difference" that is used in the definition is understood to mean the distance to the farther focus minus the distance to the closer focus. As a result, the points on the hyperbola form two branches, each "wrapping around" the closer focus (Figure 10.4.4a). The midpoint of the line segment joining the foci is called the **center** of the hyperbola, the line through the foci is called the **focal axis**, and the line through the center that is perpendicular to the focal axis is called the **conjugate axis**. The hyperbola intersects the focal axis at two points called the **vertices**.

Associated with every hyperbola is a pair of lines, called the **asymptotes** of the hyperbola. These lines intersect at the center of the hyperbola and have the property that as a point $P$ moves along the hyperbola away from the center, the vertical distance between $P$ and one of the asymptotes approaches zero (Figure 10.4.4b).

---

### EQUATIONS OF PARABOLAS IN STANDARD POSITION

It is traditional in the study of parabolas to denote the distance between the focus and the vertex by $p$. The vertex is equidistant from the focus and the directrix, so the distance between the vertex and the directrix is also $p$; consequently, the distance between the focus and the directrix is $2p$ (Figure 10.4.5). The parabola passes through two of the corners of a box that extends from the vertex to the focus along the axis of symmetry and extends $2p$ units above and $2p$ units below the axis of symmetry.

The equation of a parabola is simplest if the vertex is the origin and the axis of symmetry is along the $x$-axis or $y$-axis. The four standard positions of a parabola are:
* $y^2 = 4px$ (opens right; focus $(p, 0)$, directrix $x = -p$)
* $y^2 = -4px$ (opens left; focus $(-p, 0)$, directrix $x = p$)
* $x^2 = 4py$ (opens up; focus $(0, p)$, directrix $y = -p$)
* $x^2 = -4py$ (opens down; focus $(0, -p)$, directrix $y = p$)

To derive the equation for the parabola with focus $(p, 0)$ and directrix $x = -p$, let $P(x, y)$ be any point on the parabola. Since $PF = PD$:
$$\sqrt{(x - p)^2 + y^2} = \sqrt{(x + p)^2}$$
Squaring and simplifying yields
$$y^2 = 4px$$

#### Sketching a Parabola from Its Standard Equation
* **Step 1.** Determine whether the axis of symmetry is along the $x$-axis or the $y$-axis ($y^2$-term $\implies x$-axis; $x^2$-term $\implies y$-axis).
* **Step 2.** Determine which way the parabola opens from the sign of the linear term coefficient.
* **Step 3.** Determine $p$ and draw a box extending $p$ units from origin along axis of symmetry and $2p$ units on each side.
* **Step 4.** Sketch the parabola through the vertex and corners of the box.

#### Example 1
Sketch the graphs of the parabolas (a) $x^2 = 12y$ and (b) $y^2 + 8x = 0$, and show the focus and directrix of each.

**Solution (a).** $x^2 = 12y \implies 4p = 12 \implies p = 3$. The parabola opens upward, focus is $(0, 3)$, and directrix is $y = -3$ (Figure 10.4.9).  
**Solution (b).** $y^2 = -8x \implies 4p = 8 \implies p = 2$. The parabola opens left, focus is $(-2, 0)$, and directrix is $x = 2$ (Figure 10.4.10).

#### Example 2
Find an equation of the parabola that is symmetric about the $y$-axis, has its vertex at the origin, and passes through the point $(5, 2)$.

**Solution.** The equation has the form $x^2 = 4py$. Substituting $(5, 2)$ gives $5^2 = 4p(2) \implies 4p = 25/2$. Thus, $x^2 = \frac{25}{2}y$.

---

### EQUATIONS OF ELLIPSES IN STANDARD POSITION

It is traditional to denote the length of the major axis by $2a$, minor axis by $2b$, and distance between foci by $2c$ (Figure 10.4.11). $a$ is the semimajor axis and $b$ the semiminor axis.  
Basic relationship:
$$a = \sqrt{b^2 + c^2} \quad \text{or} \quad c = \sqrt{a^2 - b^2} \tag{6–7}$$
For all points on the ellipse, the sum of distances to the foci is $2a$.

Standard equations of an ellipse centered at origin:
* $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \quad (a > b)$: major axis on $x$-axis, foci $(\pm c, 0)$
* $\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1 \quad (a > b)$: major axis on $y$-axis, foci $(0, \pm c)$

#### Sketching an Ellipse from Its Standard Equation
* **Step 1.** Determine major axis from larger denominator ($a^2 > b^2$).
* **Step 2.** Find $a$ and $b$, draw a box extending $a$ units along major axis and $b$ units along minor axis.
* **Step 3.** Sketch the ellipse inscribed in the box touching coordinate axes at vertices.

#### Example 3
Sketch the graphs of (a) $\frac{x^2}{9} + \frac{y^2}{16} = 1$ and (b) $x^2 + 2y^2 = 4$, showing the foci of each.

**Solution (a).** $a^2 = 16 \implies a = 4$, $b^2 = 9 \implies b = 3$. Major axis along $y$-axis. $c = \sqrt{16 - 9} = \sqrt{7} \approx 2.6$. Foci: $(0, \pm\sqrt{7})$.  
**Solution (b).** $\frac{x^2}{4} + \frac{y^2}{2} = 1 \implies a = 2, b = \sqrt{2}$. Major axis along $x$-axis. $c = \sqrt{4 - 2} = \sqrt{2} \approx 1.4$. Foci: $(\pm\sqrt{2}, 0)$.

#### Example 4
Find an equation for the ellipse with foci $(0, \pm 2)$ and major axis with endpoints $(0, \pm 4)$.

**Solution.** $a = 4, c = 2 \implies b^2 = a^2 - c^2 = 16 - 4 = 12$. Equation: $\frac{x^2}{12} + \frac{y^2}{16} = 1$.

---

### EQUATIONS OF HYPERBOLAS IN STANDARD POSITION

Distance between vertices is $2a$, distance between foci is $2c$, and $b = \sqrt{c^2 - a^2}$ or $c = \sqrt{a^2 + b^2}$. For all points on the hyperbola, the difference of distances to the foci is $2a$.

Standard equations of a hyperbola centered at origin:
* $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$: focal axis on $x$-axis, vertices $(\pm a, 0)$, asymptotes $y = \pm\frac{b}{a}x$
* $\frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$: focal axis on $y$-axis, vertices $(0, \pm a)$, asymptotes $y = \pm\frac{a}{b}x$

> **A Quick Way to Find Asymptotes:** Replace 1 by 0 on the right side of the hyperbola equation and solve for $y$ in terms of $x$.

#### Example 5
Sketch the graphs of (a) $\frac{x^2}{4} - \frac{y^2}{9} = 1$ and (b) $y^2 - x^2 = 1$, showing their vertices, foci, and asymptotes.

**Solution (a).** $a = 2, b = 3, c = \sqrt{4 + 9} = \sqrt{13} \approx 3.6$. Vertices: $(\pm 2, 0)$, foci: $(\pm\sqrt{13}, 0)$, asymptotes: $y = \pm\frac{3}{2}x$.  
**Solution (b).** $a = 1, b = 1, c = \sqrt{2}$. Vertices: $(0, \pm 1)$, foci: $(0, \pm\sqrt{2})$, asymptotes: $y = \pm x$ (*equilateral hyperbola*).

#### Example 6
Find the equation of the hyperbola with vertices $(0, \pm 8)$ and asymptotes $y = \pm\frac{4}{3}x$.

**Solution.** $a = 8 \implies \frac{a}{b} = \frac{8}{b} = \frac{4}{3} \implies b = 6$. Equation: $\frac{y^2}{64} - \frac{x^2}{36} = 1$.

---

### TRANSLATED CONICS

Replacing $x$ by $x - h$ and $y$ by $y - k$:

#### Parabolas with vertex $(h, k)$:
* $(y - k)^2 = 4p(x - h)$ [Opens right]
* $(y - k)^2 = -4p(x - h)$ [Opens left]
* $(x - h)^2 = 4p(y - k)$ [Opens up]
* $(x - h)^2 = -4p(y - k)$ [Opens down]

#### Ellipses with center $(h, k)$ ($a > b$):
* $\frac{(x - h)^2}{a^2} + \frac{(y - k)^2}{b^2} = 1$ [Major axis horizontal]
* $\frac{(x - h)^2}{b^2} + \frac{(y - k)^2}{a^2} = 1$ [Major axis vertical]

#### Hyperbolas with center $(h, k)$:
* $\frac{(x - h)^2}{a^2} - \frac{(y - k)^2}{b^2} = 1$ [Focal axis horizontal]
* $\frac{(y - k)^2}{a^2} - \frac{(x - h)^2}{b^2} = 1$ [Focal axis vertical]

#### Example 7
Find an equation for the parabola that has its vertex at $(1, 2)$ and its focus at $(4, 2)$.

**Solution.** Opens right, $p = 3$, $(h, k) = (1, 2) \implies (y - 2)^2 = 12(x - 1)$.

#### Example 8
Describe the graph of $y^2 - 8x - 6y - 23 = 0$.

**Solution.** Completing the square: $(y - 3)^2 = 8(x + 4)$. Parabola with vertex $(-4, 3)$, opens right, $p = 2$, focus $(-2, 3)$, directrix $x = -6$.

#### Example 9
Describe the graph of $16x^2 + 9y^2 - 64x - 54y + 1 = 0$.

**Solution.** Completing squares: $16(x - 2)^2 + 9(y - 3)^2 = 144 \implies \frac{(x - 2)^2}{9} + \frac{(y - 3)^2}{16} = 1$. Ellipse with center $(2, 3)$, major axis vertical, $a = 4, b = 3, c = \sqrt{7}$, endpoints of major axis $(2, 7)$ and $(2, -1)$, endpoints of minor axis $(-1, 3)$ and $(5, 3)$, foci $(2, 3 \pm \sqrt{7})$.

#### Example 10
Describe the graph of $x^2 - y^2 - 4x + 8y - 21 = 0$.

**Solution.** Completing squares: $(x - 2)^2 - (y - 4)^2 = 9 \implies \frac{(x - 2)^2}{9} - \frac{(y - 4)^2}{9} = 1$. Hyperbola with center $(2, 4)$, focal axis horizontal, $a = 3, b = 3, c = 3\sqrt{2}$, vertices $(-1, 4)$ and $(5, 4)$, foci $(2 \pm 3\sqrt{2}, 4)$, asymptotes $y = x + 2$ and $y = -x + 6$.

---

### REFLECTION PROPERTIES & APPLICATIONS

> **10.4.4 THEOREM (Reflection Property of Parabolas)**  
> The tangent line at a point $P$ on a parabola makes equal angles with the line through $P$ parallel to the axis of symmetry and the line through $P$ and the focus (Figure 10.4.30a).

> **10.4.5 THEOREM (Reflection Property of Ellipses)**  
> A line tangent to an ellipse at a point $P$ makes equal angles with the lines joining $P$ to the foci (Figure 10.4.30b).

> **10.4.6 THEOREM (Reflection Property of Hyperbolas)**  
> A line tangent to a hyperbola at a point $P$ makes equal angles with the lines joining $P$ to the foci (Figure 10.4.30c).

* Parabolic antennas, flashlights, headlights, and telescopes reflect incoming parallel waves to the focus or produce parallel beams from a light source at the focus.
* Whispering galleries in buildings use elliptical ceilings with common foci.
* Hyperbolic navigation systems (LORAN, GPS) determine position via intersection of hyperbolas from synchronized transmitters.

---

### QUICK CHECK EXERCISES 10.4
*(See page 748 for answers.)*

1. Identify the conic:  
   (a) The set of points in the plane, the sum of whose distances to two fixed points is a positive constant greater than the distance between the fixed points is $\underline{\quad}$.  
   (b) The set of points in the plane, the difference of whose distances to two fixed points is a positive constant less than the distance between the fixed points is $\underline{\quad}$.  
   (c) The set of points in the plane that are equidistant from a fixed line and a fixed point not on the line is $\underline{\quad}$.
2. (a) The equation of the parabola with focus $(p, 0)$ and directrix $x = -p$ is $\underline{\quad}$.  
   (b) The equation of the parabola with focus $(0, p)$ and directrix $y = -p$ is $\underline{\quad}$.
3. (a) Suppose that an ellipse has semimajor axis $a$ and semiminor axis $b$. Then for all points on the ellipse, the sum of the distances to the foci is equal to $\underline{\quad}$.  
   (b) The two standard equations of an ellipse with semimajor axis $a$ and semiminor axis $b$ are $\underline{\quad}$ and $\underline{\quad}$.  
   (c) Suppose that an ellipse has semimajor axis $a$, semiminor axis $b$, and foci $(\pm c, 0)$. Then $c$ may be obtained from $a$ and $b$ by the equation $c = \underline{\quad}$.
4. (a) Suppose that a hyperbola has semifocal axis $a$ and semiconjugate axis $b$. Then for all points on the hyperbola, the difference of the distance to the farther focus minus the distance to the closer focus is equal to $\underline{\quad}$.  
   (b) The two standard equations of a hyperbola with semifocal axis $a$ and semiconjugate axis $b$ are $\underline{\quad}$ and $\underline{\quad}$.  
   (c) Suppose that a hyperbola in standard position has semifocal axis $a$, semiconjugate axis $b$, and foci $(\pm c, 0)$. Then $c$ may be obtained from $a$ and $b$ by the equation $c = \underline{\quad}$. The equations of the asymptotes of this hyperbola are $y = \pm\underline{\quad}$.

---

### EXERCISE SET 10.4

#### FOCUS ON CONCEPTS
1. In parts (a)–(f), find the equation of the conic from the given graphs.
2. (a) Find the focus and directrix for each parabola in Exercise 1.  
   (b) Find the foci of the ellipses in Exercise 1.  
   (c) Find the foci and the equations of the asymptotes of the hyperbolas in Exercise 1.

**3–6 Sketch the parabola, and label the focus, vertex, and directrix.**
3. (a) $y^2 = 4x$ (b) $x^2 = -8y$
4. (a) $y^2 = -10x$ (b) $x^2 = 4y$
5. (a) $(y - 1)^2 = -12(x + 4)$ (b) $(x - 1)^2 = 2(y - 1/2)$
6. (a) $y^2 - 6y - 2x + 1 = 0$ (b) $y = 4x^2 + 8x + 5$

**7–10 Sketch the ellipse, and label the foci, vertices, and ends of the minor axis.**
7. (a) $\frac{x^2}{16} + \frac{y^2}{9} = 1$ (b) $9x^2 + y^2 = 9$
8. (a) $\frac{x^2}{25} + \frac{y^2}{4} = 1$ (b) $4x^2 + y^2 = 36$
9. (a) $(x + 3)^2 + 4(y - 5)^2 = 16$ (b) $\frac{1}{4}x^2 + \frac{1}{9}(y + 2)^2 - 1 = 0$
10. (a) $9x^2 + 4y^2 - 18x + 24y + 9 = 0$ (b) $5x^2 + 9y^2 + 20x - 54y = -56$

**11–14 Sketch the hyperbola, and label the vertices, foci, and asymptotes.**
11. (a) $\frac{x^2}{16} - \frac{y^2}{9} = 1$ (b) $9y^2 - x^2 = 36$
12. (a) $\frac{y^2}{9} - \frac{x^2}{25} = 1$ (b) $16x^2 - 25y^2 = 400$
13. (a) $\frac{(y + 4)^2}{3} - \frac{(x - 2)^2}{5} = 1$ (b) $16(x + 1)^2 - 8(y - 3)^2 = 16$
14. (a) $x^2 - 4y^2 + 2x + 8y - 7 = 0$ (b) $16x^2 - y^2 - 32x - 6y = 57$

**15–18 Find an equation for the parabola that satisfies the given conditions.**
15. (a) Vertex $(0, 0)$; focus $(3, 0)$. (b) Vertex $(0, 0)$; directrix $y = 1/4$.
16. (a) Focus $(6, 0)$; directrix $x = -6$. (b) Focus $(1, 1)$; directrix $y = -2$.
17. Axis $y = 0$; passes through $(3, 2)$ and $(2, -\sqrt{2})$.
18. Vertex $(5, -3)$; axis parallel to the $y$-axis; passes through $(9, 5)$.

**19–22 Find an equation for the ellipse that satisfies the given conditions.**
19. (a) Ends of major axis $(\pm 3, 0)$; ends of minor axis $(0, \pm 2)$. (b) Length of minor axis 8; foci $(0, \pm 3)$.
20. (a) Foci $(\pm 1, 0)$; $b = \sqrt{2}$. (b) $c = 2\sqrt{3}$; $a = 4$; center at the origin; foci on a coordinate axis (two answers).
21. (a) Ends of major axis $(0, \pm 6)$; passes through $(-3, 2)$. (b) Foci $(-1, 1)$ and $(-1, 3)$; minor axis of length 4.
22. (a) Center at $(0, 0)$; major and minor axes along the coordinate axes; passes through $(3, 2)$ and $(1, 6)$. (b) Foci $(2, 1)$ and $(2, -3)$; major axis of length 6.

**23–26 Find an equation for a hyperbola that satisfies the given conditions.**
23. (a) Vertices $(\pm 2, 0)$; foci $(\pm 3, 0)$. (b) Vertices $(0, \pm 2)$; asymptotes $y = \pm\frac{2}{3}x$.
24. (a) Asymptotes $y = \pm\frac{3}{2}x$; $b = 4$. (b) Foci $(0, \pm 5)$; asymptotes $y = \pm 2x$.
25. (a) Asymptotes $y = \pm\frac{3}{4}x$; $c = 5$. (b) Foci $(\pm 3, 0)$; asymptotes $y = \pm 2x$.
26. (a) Vertices $(0, 6)$ and $(6, 6)$; foci 10 units apart. (b) Asymptotes $y = x - 2$ and $y = -x + 4$; passes through the origin.

**27–30 True–False Determine whether the statement is true or false. Explain your answer.**
27. A hyperbola is the set of all points in the plane that are equidistant from a fixed line and a fixed point not on the line.
28. If an ellipse is not a circle, then the foci of an ellipse lie on the major axis of the ellipse.
29. If a parabola has equation $y^2 = 4px$, where $p$ is a positive constant, then the perpendicular distance from the parabola's focus to its directrix is $p$.
30. The hyperbola $(y^2/a^2) - x^2 = 1$ has asymptotes the lines $y = \pm x/a$.

31. (a) As illustrated in Figure Ex-31, a parabolic arch spans a road $40\text{ ft}$ wide. How high is the arch if a center section of the road $20\text{ ft}$ wide has a minimum clearance of $12\text{ ft}$?  
    (b) How high would the center be if the arch were the upper half of an ellipse?

32. (a) Find an equation for the parabolic arch with base $b$ and height $h$, shown in Figure Ex-32.  
    (b) Find the area under the arch.

33. Show that the vertex is the closest point on a parabola to the focus. [*Suggestion:* Introduce a convenient coordinate system and use Definition 10.4.1.]

34. Suppose that a comet moves in a parabolic orbit with the Sun at its focus and that the line from the Sun to the comet makes an angle of $60^\circ$ with the axis of the parabola when the comet is 40 million miles from the center of the Sun. Use the result in Exercise 33 to determine how close the comet will come to the center of the Sun.

35. For the parabolic reflector in Figure Ex-35, how far from the vertex should the light source be placed to produce a beam of parallel rays?

36. (a) Show that the right and left branches of the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ can be represented parametrically as
    $$x = a\cosh t, \quad y = b\sinh t \quad (-\infty < t < +\infty)$$
    $$x = -a\cosh t, \quad y = b\sinh t \quad (-\infty < t < +\infty)$$
    (b) Use a graphing utility to generate both branches of the hyperbola $x^2 - y^2 = 1$ on the same screen.

37. (a) Show that the right and left branches of the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ can be represented parametrically as
    $$x = a\sec t, \quad y = b\tan t \quad (-\pi/2 < t < \pi/2)$$
    $$x = -a\sec t, \quad y = b\tan t \quad (-\pi/2 < t < \pi/2)$$
    (b) Use a graphing utility to generate both branches of the hyperbola $x^2 - y^2 = 1$ on the same screen.

38. Find an equation of the parabola traced by a point that moves so that its distance from $(2, 4)$ is the same as its distance to the $x$-axis.
39. Find an equation of the ellipse traced by a point that moves so that the sum of its distances to $(4, 1)$ and $(4, 5)$ is 12.
40. Find the equation of the hyperbola traced by a point that moves so that the difference between its distances to $(0, 0)$ and $(1, 1)$ is 1.

41. Suppose that the base of a solid is elliptical with a major axis of length 9 and a minor axis of length 4. Find the volume of the solid if the cross sections perpendicular to the major axis are squares (see Figure Ex-41).
42. Suppose that the base of a solid is elliptical with a major axis of length 9 and a minor axis of length 4. Find the volume of the solid if the cross sections perpendicular to the minor axis are equilateral triangles (see Figure Ex-42).
43. Show that an ellipse with semimajor axis $a$ and semiminor axis $b$ has area $A = \pi ab$.

#### FOCUS ON CONCEPTS
44. Show that if a plane is not parallel to the axis of a right circular cylinder, then the intersection of the plane and cylinder is an ellipse (possibly a circle). [*Hint:* Let $\theta$ be the angle shown in Figure Ex-44, introduce coordinate axes, and express $x'$ and $y'$ in terms of $x$ and $y$.]

45. A carpenter needs to cut an elliptical hole in a sloped roof through which a circular vent pipe of diameter $D$ is to be inserted vertically. The carpenter wants to draw the outline of the hole on the roof using a pencil, two tacks, and a piece of string (as in Figure 10.4.3b). The center point of the ellipse is known, and common sense suggests that its major axis must be perpendicular to the drip line of the roof. The carpenter needs to determine the length $L$ of the string and the distance $T$ between a tack and the center point. The architect's plans show that the pitch of the roof is $p$ ($\text{pitch} = \text{rise over run}$). Find $T$ and $L$ in terms of $D$ and $p$.

46. Suppose that two observers are stationed at the points $F_1(c, 0)$ and $F_2(-c, 0)$ in an $xy$-coordinate system. Suppose also that the sound of an explosion in the $xy$-plane is heard by the $F_1$ observer $t$ seconds before it is heard by the $F_2$ observer. Assuming that the speed of sound is a constant $v$, show that the explosion occurred somewhere on the hyperbola
    $$\frac{x^2}{v^2t^2/4} - \frac{y^2}{c^2 - (v^2t^2/4)} = 1$$

47. Suppose that two transmitting stations are positioned $100\text{ km}$ apart at points $F_1(50, 0)$ and $F_2(-50, 0)$ on a straight shoreline. Suppose also that a ship is traveling parallel to the shoreline but $200\text{ km}$ at sea. Find the coordinates of the ship if the stations transmit a pulse simultaneously, but the pulse from station $F_1$ is received by the ship $100\text{ microseconds}$ sooner than the pulse from station $F_2$. [Assume that the pulses travel at the speed of light ($299,792,458\text{ m/s}$).]

48. A nuclear cooling tower is to have a height of $h$ feet and the shape of the solid that is generated by revolving the region $R$ enclosed by the right branch of the hyperbola $1521x^2 - 225y^2 = 342,225$ and the lines $x = 0, \; y = -h/2,$ and $y = h/2$ about the $y$-axis.  
    (a) Find the volume of the tower.  
    (b) Find the lateral surface area of the tower.

49. Let $R$ be the region that is above the $x$-axis and enclosed between the curve $b^2x^2 - a^2y^2 = a^2b^2$ and the line $x = \sqrt{a^2 + b^2}$.  
    (a) Sketch the solid generated by revolving $R$ about the $x$-axis, and find its volume.  
    (b) Sketch the solid generated by revolving $R$ about the $y$-axis, and find its volume.

50. The tank of an oil truck is $18\text{ ft}$ long and has elliptical cross sections that are $6\text{ ft}$ wide and $4\text{ ft}$ high.  
    (a) Show that the volume $V$ of oil in the tank (in cubic feet) when it is filled to a depth of $h$ feet is
    $$V = 27\left[4\sin^{-1}\left(\frac{h - 2}{2}\right) + (h - 2)\sqrt{4h - h^2} + 2\pi\right]$$
    (b) Use the numerical root-finding capability of a CAS to determine how many inches from the bottom of a dipstick the calibration marks should be placed to indicate when the tank is $1/4, 1/2,$ and $3/4$ full.

51. Prove: The line tangent to the parabola $x^2 = 4py$ at the point $(x_0, y_0)$ is $x_0 x = 2p(y + y_0)$.
52. Prove: The line tangent to the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ at the point $(x_0, y_0)$ has the equation $\frac{x x_0}{a^2} + \frac{y y_0}{b^2} = 1$.
53. Prove: The line tangent to the hyperbola $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ at the point $(x_0, y_0)$ has the equation $\frac{x x_0}{a^2} - \frac{y y_0}{b^2} = 1$.
54. Use the results in Exercises 52 and 53 to show that if an ellipse and a hyperbola have the same foci, then at each point of intersection their tangent lines are perpendicular.

55. Find two values of $k$ such that the line $x + 2y = k$ is tangent to the ellipse $x^2 + 4y^2 = 8$. Find the points of tangency.
56. Find the coordinates of all points on the hyperbola $4x^2 - y^2 = 4$ where the two lines that pass through the point and the foci are perpendicular.
57. A line tangent to the hyperbola $4x^2 - y^2 = 36$ intersects the $y$-axis at the point $(0, 4)$. Find the point(s) of tangency.

58. Consider the second-degree equation
    $$Ax^2 + Cy^2 + Dx + Ey + F = 0$$
    where $A$ and $C$ are not both 0. Show by completing the square:  
    (a) If $AC > 0$, then the equation represents an ellipse, a circle, a point, or has no graph.  
    (b) If $AC < 0$, then the equation represents a hyperbola or a pair of intersecting lines.  
    (c) If $AC = 0$, then the equation represents a parabola, a pair of parallel lines, or has no graph.

59. In each part, use the result in Exercise 58 to make a statement about the graph of the equation, and then check your conclusion by completing the square and identifying the graph:  
    (a) $x^2 - 5y^2 - 2x - 10y - 9 = 0$  
    (b) $x^2 - 3y^2 - 6y - 3 = 0$  
    (c) $4x^2 + 8y^2 + 16x + 16y + 20 = 0$  
    (d) $3x^2 + y^2 + 12x + 2y + 13 = 0$  
    (e) $x^2 + 8x + 2y + 14 = 0$  
    (f) $5x^2 + 40x + 2y + 94 = 0$

60. Derive the equation $x^2 = 4py$ in Figure 10.4.6.
61. Derive the equation $(x^2/b^2) + (y^2/a^2) = 1$ given in Figure 10.4.14.
62. Derive the equation $(x^2/a^2) - (y^2/b^2) = 1$ given in Figure 10.4.22.
63. Prove Theorem 10.4.4. [*Hint:* Choose coordinate axes so that the parabola has the equation $x^2 = 4py$. Show that the tangent line at $P(x_0, y_0)$ intersects the $y$-axis at $Q(0, -y_0)$ and that the triangle whose three vertices are at $P, Q,$ and the focus is isosceles.]
64. Given two intersecting lines, let $L_2$ be the line with the larger angle of inclination $\phi_2$, and let $L_1$ be the line with the smaller angle of inclination $\phi_1$. We define the angle $\theta$ between $L_1$ and $L_2$ by $\theta = \phi_2 - \phi_1$ (Figure Ex-64).  
    (a) Prove: If $L_1$ and $L_2$ are not perpendicular, then
    $$\tan\theta = \frac{m_2 - m_1}{1 + m_1 m_2}$$
    where $L_1$ and $L_2$ have slopes $m_1$ and $m_2$.  
    (b) Prove Theorem 10.4.5.  
    (c) Prove Theorem 10.4.6.

65. **Writing.** Suppose that you want to draw an ellipse that has given values for the lengths of the major and minor axes by using the method shown in Figure 10.4.3b. Assuming that the axes are drawn, explain how a compass can be used to locate the positions for the tacks.
66. **Writing.** List the forms for standard equations of parabolas, ellipses, and hyperbolas, and write a summary of techniques for sketching conic sections from their standard equations.

#### QUICK CHECK ANSWERS 10.4
1. (a) an ellipse (b) a hyperbola (c) a parabola
2. (a) $y^2 = 4px$ (b) $x^2 = 4py$
3. (a) $2a$ (b) $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1; \quad \frac{x^2}{b^2} + \frac{y^2}{a^2} = 1$ (c) $\sqrt{a^2 - b^2}$
4. (a) $2a$ (b) $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1; \quad \frac{y^2}{a^2} - \frac{x^2}{b^2} = 1$ (c) $\sqrt{a^2 + b^2}; \quad \frac{b}{a}x$

---

## 10.5 ROTATION OF AXES; SECOND-DEGREE EQUATIONS

In the preceding section we obtained equations of conic sections with axes parallel to the coordinate axes. In this section we will study the equations of conics that are "tilted" relative to the coordinate axes. This will lead us to investigate rotations of coordinate axes.

### QUADRATIC EQUATIONS IN $x$ AND $y$

Equations of the form
$$Ax^2 + Cy^2 + Dx + Ey + F = 0 \tag{1}$$
can represent conic sections. Equation (1) is a special case of the more general equation
$$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0 \tag{2}$$
which, if $A, B,$ and $C$ are not all zero, is called a **quadratic equation in $x$ and $y$**. If $B \neq 0$, then (2) contains a cross-product term $Bxy$, and the graph of the conic section represented by the equation has its axis or axes "tilted" relative to the coordinate axes.

For example, consider the ellipse with foci $F_1(1, 2)$ and $F_2(-1, -2)$ and such that the sum of the distances from each point $P(x, y)$ on the ellipse to the foci is 6 units:
$$\sqrt{(x - 1)^2 + (y - 2)^2} + \sqrt{(x + 1)^2 + (y + 2)^2} = 6$$
Squaring and simplifying yields
$$8x^2 - 4xy + 5y^2 = 36$$

---

### ROTATION OF AXES

Let the axes of an $xy$-coordinate system be rotated about the origin through an angle $\theta$ to produce a new $x'y'$-coordinate system (Figure 10.5.2):
$$x = r\cos(\theta + \alpha), \quad y = r\sin(\theta + \alpha) \tag{3}$$
$$x' = r\cos\alpha, \quad y' = r\sin\alpha \tag{4}$$
Using angle sum identities:
$$x = x'\cos\theta - y'\sin\theta$$
$$y = x'\sin\theta + y'\cos\theta \tag{5}$$
These are called the **rotation equations**.

Solving (5) for $x'$ and $y'$ in terms of $x$ and $y$ yields:
$$x' = x\cos\theta + y\sin\theta$$
$$y' = -x\sin\theta + y\cos\theta \tag{6}$$

#### Example 1
Suppose that the axes of an $xy$-coordinate system are rotated through an angle of $\theta = 45^\circ$ to obtain an $x'y'$-coordinate system. Find the equation of the curve
$$x^2 - xy + y^2 - 6 = 0$$
in $x'y'$-coordinates.

**Solution.** Substituting $\sin 45^\circ = 1/\sqrt{2}$ and $\cos 45^\circ = 1/\sqrt{2}$ in (5):
$$x = \frac{x'}{\sqrt{2}} - \frac{y'}{\sqrt{2}}, \quad y = \frac{x'}{\sqrt{2}} + \frac{y'}{\sqrt{2}}$$
Substituting into $x^2 - xy + y^2 - 6 = 0$ yields:
$$\frac{x'^2}{12} + \frac{y'^2}{4} = 1$$
which is the equation of an ellipse (Figure 10.5.3).

#### Example 2
Find the new coordinates of the point $(2, 4)$ if the coordinate axes are rotated through an angle of $\theta = 30^\circ$.

**Solution.** From (6) with $x = 2, y = 4, \cos 30^\circ = \sqrt{3}/2, \sin 30^\circ = 1/2$:
$$x' = 2\left(\frac{\sqrt{3}}{2}\right) + 4\left(\frac{1}{2}\right) = \sqrt{3} + 2$$
$$y' = -2\left(\frac{1}{2}\right) + 4\left(\frac{\sqrt{3}}{2}\right) = -1 + 2\sqrt{3}$$
Thus, $(x', y') = (\sqrt{3} + 2, -1 + 2\sqrt{3})$.

---

### ELIMINATING THE CROSS-PRODUCT TERM

> **10.5.1 THEOREM**  
> If the equation
> $$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0 \tag{7}$$
> is such that $B \neq 0$, and if an $x'y'$-coordinate system is obtained by rotating the $xy$-axes through an angle $\theta$ satisfying
> $$\cot 2\theta = \frac{A - C}{B} \quad \left(0 < \theta < \frac{\pi}{2}\right) \tag{8}$$
> then, in $x'y'$-coordinates, Equation (7) will have the form
> $$A'x'^2 + C'y'^2 + D'x' + E'y' + F' = 0$$

**Proof.** Substituting (5) into (7) yields
$$A'x'^2 + B'x'y' + C'y'^2 + D'x' + E'y' + F' = 0$$
where
$$A' = A\cos^2\theta + B\cos\theta\sin\theta + C\sin^2\theta$$
$$B' = B(\cos^2\theta - \sin^2\theta) + 2(C - A)\sin\theta\cos\theta = B\cos 2\theta - (A - C)\sin 2\theta$$
$$C' = A\sin^2\theta - B\sin\theta\cos\theta + C\cos^2\theta$$
$$D' = D\cos\theta + E\sin\theta$$
$$E' = -D\sin\theta + E\cos\theta$$
$$F' = F \tag{9}$$
Setting $B' = 0$ gives $B\cos 2\theta = (A - C)\sin 2\theta \implies \cot 2\theta = \frac{A - C}{B}$.

#### Example 3
Identify and sketch the curve $xy = 1$.

**Solution.** $A = 0, B = 1, C = 0 \implies \cot 2\theta = \frac{0 - 0}{1} = 0 \implies 2\theta = \pi/2 \implies \theta = \pi/4 = 45^\circ$.  
Substituting $x = \frac{x'}{\sqrt{2}} - \frac{y'}{\sqrt{2}}$ and $y = \frac{x'}{\sqrt{2}} + \frac{y'}{\sqrt{2}}$ into $xy = 1$ yields:
$$\frac{x'^2}{2} - \frac{y'^2}{2} = 1$$
which is an equilateral hyperbola with vertices at $(\pm\sqrt{2}, 0)$ in the $x'y'$-system (Figure 10.5.4).

#### Example 4
Identify and sketch the curve
$$153x^2 - 192xy + 97y^2 - 30x - 40y - 200 = 0$$

**Solution.** $A = 153, B = -192, C = 97 \implies \cot 2\theta = -\frac{56}{192} = -\frac{7}{24}$.  
From the right triangle in Figure 10.5.5, $\cos 2\theta = -\frac{7}{25}$, so:
$$\cos\theta = \sqrt{\frac{1 + \cos 2\theta}{2}} = \sqrt{\frac{1 - 7/25}{2}} = \frac{3}{5}$$
$$\sin\theta = \sqrt{\frac{1 - \cos 2\theta}{2}} = \sqrt{\frac{1 + 7/25}{2}} = \frac{4}{5}$$
Rotation equations: $x = \frac{3}{5}x' - \frac{4}{5}y', \quad y = \frac{4}{5}x' + \frac{3}{5}y'$.  
Substituting into the equation and simplifying yields:
$$25x'^2 + 225y'^2 - 50x' - 200 = 0 \implies x'^2 + 9y'^2 - 2x' - 8 = 0 \implies \frac{(x' - 1)^2}{9} + y'^2 = 1$$
This is an ellipse with center $(1, 0)$ in the $x'y'$-system, $a = 3, b = 1$ (Figure 10.5.6).

---

### QUICK CHECK EXERCISES 10.5
*(See page 754 for answers.)*

1. Suppose that an $xy$-coordinate system is rotated $\theta$ radians to produce a new $x'y'$-coordinate system.  
   (a) $x$ and $y$ may be obtained from $x', y',$ and $\theta$ using the rotation equations $x = \underline{\quad}$ and $y = \underline{\quad}$.  
   (b) $x'$ and $y'$ may be obtained from $x, y,$ and $\theta$ using the equations $x' = \underline{\quad}$ and $y' = \underline{\quad}$.
2. If the equation $Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0$ is such that $B \neq 0$, then the $xy$-term in this equation can be eliminated by a rotation of axes through an angle $\theta$ satisfying $\cot 2\theta = \underline{\quad}$.
3. In each part, determine a rotation angle $\theta$ that will eliminate the $xy$-term:  
   (a) $2x^2 + xy + 2y^2 + x - y = 0$  
   (b) $x^2 + 2\sqrt{3}xy + 3y^2 - 2x + y = 1$  
   (c) $3x^2 + \sqrt{3}xy + 2y^2 + y = 0$
4. Express $2x^2 + xy + 2y^2 = 1$ in the $x'y'$-coordinate system obtained by rotating the $xy$-coordinate system through the angle $\theta = \pi/4$.

---

### EXERCISE SET 10.5

1. Let an $x'y'$-coordinate system be obtained by rotating an $xy$-coordinate system through an angle of $\theta = 60^\circ$.  
   (a) Find the $x'y'$-coordinates of the point whose $xy$-coordinates are $(-2, 6)$.  
   (b) Find an equation of the curve $\sqrt{3}xy + y^2 = 6$ in $x'y'$-coordinates.  
   (c) Sketch the curve in part (b), showing both $xy$-axes and $x'y'$-axes.

2. Let an $x'y'$-coordinate system be obtained by rotating an $xy$-coordinate system through an angle of $\theta = 30^\circ$.  
   (a) Find the $x'y'$-coordinates of the point whose $xy$-coordinates are $(1, -\sqrt{3})$.  
   (b) Find an equation of the curve $2x^2 + 2\sqrt{3}xy = 3$ in $x'y'$-coordinates.  
   (c) Sketch the curve in part (b), showing both $xy$-axes and $x'y'$-axes.

**3–12 Rotate the coordinate axes to remove the $xy$-term. Then identify the type of conic and sketch its graph.**
3. $xy = -9$
4. $x^2 - xy + y^2 - 2 = 0$
5. $x^2 + 4xy - 2y^2 - 6 = 0$
6. $31x^2 + 10\sqrt{3}xy + 21y^2 - 144 = 0$
7. $x^2 + 2\sqrt{3}xy + 3y^2 + 2\sqrt{3}x - 2y = 0$
8. $34x^2 - 24xy + 41y^2 - 25 = 0$
9. $9x^2 - 24xy + 16y^2 - 80x - 60y + 100 = 0$
10. $5x^2 - 6xy + 5y^2 - 8\sqrt{2}x + 8\sqrt{2}y = 8$
11. $52x^2 - 72xy + 73y^2 + 40x + 30y - 75 = 0$
12. $6x^2 + 24xy - y^2 - 12x + 26y + 11 = 0$

13. Let an $x'y'$-coordinate system be obtained by rotating an $xy$-coordinate system through an angle of $45^\circ$. Use (6) to find an equation of the curve $3x'^2 + y'^2 = 6$ in $xy$-coordinates.
14. Let an $x'y'$-coordinate system be obtained by rotating an $xy$-coordinate system through an angle of $30^\circ$. Use (5) to find an equation in $x'y'$-coordinates of the curve $y = x^2$.

#### FOCUS ON CONCEPTS
15. Let an $x'y'$-coordinate system be obtained by rotating an $xy$-coordinate system through an angle $\theta$. Prove: For every value of $\theta$, the equation $x^2 + y^2 = r^2$ becomes the equation $x'^2 + y'^2 = r^2$. Give a geometric explanation.
16. Derive (6) by solving the rotation equations in (5) for $x'$ and $y'$ in terms of $x$ and $y$.
17. Let an $x'y'$-coordinate system be obtained by rotating an $xy$-coordinate system through an angle $\theta$. Explain how to find the $xy$-coordinates of a point whose $x'y'$-coordinates are known.
18. Let an $x'y'$-coordinate system be obtained by rotating an $xy$-coordinate system through an angle $\theta$. Explain how to find the $xy$-equation of a line whose $x'y'$-equation is known.

**19–22 Show that the graph of the given equation is a parabola. Find its vertex, focus, and directrix.**
19. $x^2 + 2xy + y^2 + 4\sqrt{2}x - 4\sqrt{2}y = 0$
20. $x^2 - 2\sqrt{3}xy + 3y^2 - 8\sqrt{3}x - 8y = 0$
21. $9x^2 - 24xy + 16y^2 - 80x - 60y + 100 = 0$
22. $x^2 + 2\sqrt{3}xy + 3y^2 + 16\sqrt{3}x - 16y - 96 = 0$

**23–26 Show that the graph of the given equation is an ellipse. Find its foci, vertices, and the ends of its minor axis.**
23. $288x^2 - 168xy + 337y^2 - 3600 = 0$
24. $25x^2 - 14xy + 25y^2 - 288 = 0$
25. $31x^2 + 10\sqrt{3}xy + 21y^2 - 32x + 32\sqrt{3}y - 80 = 0$
26. $43x^2 - 14\sqrt{3}xy + 57y^2 - 36\sqrt{3}x - 36y - 540 = 0$

**27–30 Show that the graph of the given equation is a hyperbola. Find its foci, vertices, and asymptotes.**
27. $x^2 - 10\sqrt{3}xy + 11y^2 + 64 = 0$
28. $17x^2 - 312xy + 108y^2 - 900 = 0$
29. $32y^2 - 52xy - 7x^2 + 72\sqrt{5}x - 144\sqrt{5}y + 900 = 0$
30. $2\sqrt{2}y^2 + 5\sqrt{2}xy + 2\sqrt{2}x^2 + 18x + 18y + 36\sqrt{2} = 0$

31. Show that the graph of the equation
    $$\sqrt{x} + \sqrt{y} = 1$$
    is a portion of a parabola. [*Hint:* First rationalize the equation and then perform a rotation of axes.]

#### FOCUS ON CONCEPTS
32. Derive the expression for $B'$ in (9).
33. Use (9) to prove that $B^2 - 4AC = B'^2 - 4A'C'$ for all values of $\theta$.
34. Use (9) to prove that $A + C = A' + C'$ for all values of $\theta$.
35. Prove: If $A = C$ in (7), then the cross-product term can be eliminated by rotating through $45^\circ$.
36. Prove: If $B \neq 0$, then the graph of $x^2 + Bxy + F = 0$ is a hyperbola if $F \neq 0$ and two intersecting lines if $F = 0$.

#### QUICK CHECK ANSWERS 10.5
1. (a) $x'\cos\theta - y'\sin\theta; \quad x'\sin\theta + y'\cos\theta$  
   (b) $x\cos\theta + y\sin\theta; \quad -x\sin\theta + y\cos\theta$
2. $\frac{A - C}{B}$
3. (a) $\pi/4$ (b) $\pi/3$ (c) $\pi/6$
4. $5x'^2 + 3y'^2 = 2$

---

## 10.6 CONIC SECTIONS IN POLAR COORDINATES

It will be shown later in the text that if an object moves in a gravitational field that is directed toward a fixed point (such as the center of the Sun), then the path of that object must be a conic section with the fixed point at a focus. For example, planets in our solar system move along elliptical paths with the Sun at a focus, and the comets move along parabolic, elliptical, or hyperbolic paths with the Sun at a focus, depending on the conditions under which they were born. For applications of this type it is usually desirable to express the equations of the conic sections in polar coordinates with the pole at a focus. In this section we will show how to do this.

### THE FOCUS–DIRECTRIX CHARACTERIZATION OF CONICS

> **10.6.1 THEOREM (Focus–Directrix Property of Conics)**  
> Suppose that a point $P$ moves in the plane determined by a fixed point (called the focus) and a fixed line (called the directrix), where the focus does not lie on the directrix. If the point moves in such a way that its distance to the focus divided by its distance to the directrix is some constant $e$ (called the eccentricity), then the curve traced by the point is a conic section. Moreover, the conic is
> (a) a parabola if $e = 1$  
> (b) an ellipse if $0 < e < 1$  
> (c) a hyperbola if $e > 1$.

For the ellipse, rewritten from Equation (8) of Section 10.4:
$$\sqrt{(x - c)^2 + y^2} = a - \frac{c}{a}x = \frac{c}{a}\left(\frac{a^2}{c} - x\right)$$
Thus, $PF = \frac{c}{a}PD$, so $PF/PD$ is constant, and the eccentricity is
$$e = \frac{c}{a} \tag{1}$$

### ECCENTRICITY OF AN ELLIPSE AS A MEASURE OF FLATNESS

The eccentricity of an ellipse can be viewed as a measure of its flatness—as $e$ approaches 0 the ellipses become more and more circular, and as $e$ approaches 1 they become more and more flat (Figure 10.6.2). Table 10.6.1 shows the orbital eccentricities of various celestial objects.

##### Table 10.6.1: Orbital Eccentricities
| Celestial Body | Eccentricity |
| :--- | :---: |
| Mercury | 0.206 |
| Venus | 0.007 |
| Earth | 0.017 |
| Mars | 0.093 |
| Jupiter | 0.048 |
| Saturn | 0.056 |
| Uranus | 0.046 |
| Neptune | 0.010 |
| Pluto | 0.249 |
| Halley's comet | 0.970 |

---

### POLAR EQUATIONS OF CONICS

> **10.6.2 THEOREM**  
> If a conic section with eccentricity $e$ is positioned in a polar coordinate system so that its focus is at the pole and the corresponding directrix is $d$ units from the pole and is either parallel or perpendicular to the polar axis, then the equation of the conic has one of four possible forms, depending on its orientation:
> * Directrix right of pole ($x = d$): $r = \frac{ed}{1 + e\cos\theta}$
> * Directrix left of pole ($x = -d$): $r = \frac{ed}{1 - e\cos\theta}$
> * Directrix above pole ($y = d$): $r = \frac{ed}{1 + e\sin\theta}$
> * Directrix below pole ($y = -d$): $r = \frac{ed}{1 - e\sin\theta}$

#### SKETCHING CONICS IN POLAR COORDINATES

#### Example 1
Sketch the graph of $r = \frac{2}{1 - \cos\theta}$ in polar coordinates.

**Solution.** $d = 2, e = 1 \implies$ parabola with focus at pole, directrix 2 units left ($x = -2$), opens right, $p = 1$ (Figure 10.6.4).

#### Ellipse Dimensions in Polar Coordinates:
Let $r_0$ be the closest vertex distance (perihelion) and $r_1$ the farthest vertex distance (aphelion):
$$r_0 = a - c \quad \text{and} \quad r_1 = a + c \tag{7}$$
$$a = \frac{1}{2}(r_1 + r_0), \quad c = \frac{1}{2}(r_1 - r_0) \tag{8–9}$$
$$b = \sqrt{r_0 r_1} \tag{10}$$

#### Example 2
Find the constants $a, b,$ and $c$ for the ellipse $r = \frac{6}{2 + \cos\theta}$.

**Solution.** Dividing numerator and denominator by 2:
$$r = \frac{3}{1 + \frac{1}{2}\cos\theta}$$
Matches form with $d = 6, e = 1/2$. Setting $\theta = 0 \implies r_0 = 2$; setting $\theta = \pi \implies r_1 = 6$.  
$$a = \frac{1}{2}(6 + 2) = 4, \quad b = \sqrt{(2)(6)} = 2\sqrt{3}, \quad c = \frac{1}{2}(6 - 2) = 2$$

#### Hyperbola Dimensions in Polar Coordinates:
$$r_0 = c - a \quad \text{and} \quad r_1 = c + a \tag{11}$$
$$a = \frac{1}{2}(r_1 - r_0), \quad c = \frac{1}{2}(r_1 + r_0) \tag{12–13}$$
$$b = \sqrt{r_0 r_1} \tag{14}$$

#### Example 3
Sketch the graph of $r = \frac{2}{1 + 2\sin\theta}$ in polar coordinates.

**Solution.** $d = 1, e = 2 \implies$ hyperbola with directrix 1 unit above pole ($y = 1$).  
Setting $\theta = \pi/2 \implies r_0 = 2/3$; setting $\theta = 3\pi/2 \implies r_1 = 2$.  
$$a = \frac{1}{2}\left(2 - \frac{2}{3}\right) = \frac{2}{3}, \quad b = \sqrt{\left(\frac{2}{3}\right)(2)} = \frac{2\sqrt{3}}{3}, \quad c = \frac{1}{2}\left(2 + \frac{2}{3}\right) = \frac{4}{3}$$

---

### APPLICATIONS IN ASTRONOMY

In 1609 Johannes Kepler published *Astronomia Nova* in which he stated his three laws of planetary motion:

> **10.6.3 KEPLER'S LAWS**  
> * **First law (Law of Orbits):** Each planet moves in an elliptical orbit with the Sun at a focus.  
> * **Second law (Law of Areas):** The radial line from the center of the Sun to the center of a planet sweeps out equal areas in equal times.  
> * **Third law (Law of Periods):** The square of a planet's period (the time it takes the planet to complete one orbit about the Sun) is proportional to the cube of the semimajor axis of its orbit:
>   $$T = a^{3/2} \tag{15}$$
>   *(with $T$ in Earth years and $a$ in astronomical units, $\text{AU}$).*

> **Johannes Kepler (1571–1630)**  
> German astronomer and physicist. Kepler, whose work provided our contemporary view of planetary motion, led a fascinating but ill-starred life. His alcoholic father made him work in a family-owned tavern as a child, later withdrawing him from elementary school and hiring him out as a field laborer, where the boy contracted smallpox, permanently crippling his hands and impairing his eyesight. In later years, Kepler's first wife and several children died, his mother was accused of witchcraft, and being a Protestant he was often subjected to persecution by Catholic authorities. He was often impoverished, eking out a living as an astrologer and prognosticator. Looking back on his unhappy childhood, Kepler described his father as "criminally inclined" and "quarrelsome" and his mother as "garrulous" and "bad-tempered." However, it was his mother who left an indelible mark on the six-year-old Kepler by showing him the comet of 1577; and in later life he personally prepared her defense against the witchcraft charges.  
> Kepler became acquainted with the work of Copernicus as a student at the University of Tübingen, where he received his master's degree in 1591. He continued on as a theological student, but at the urging of the university officials he abandoned his clerical studies and accepted a position as a mathematician and teacher in Graz, Austria. However, he was expelled from the city when it came under Catholic control, and in 1600 he finally moved on to Prague, where he became an assistant at the observatory of the famous Danish astronomer Tycho Brahe. Brahe was a brilliant and meticulous astronomical observer who amassed the most accurate astronomical data known at that time; and when Brahe died in 1601 Kepler inherited the treasure-trove of data. After eight years of intense labor, Kepler deciphered the underlying principles buried in the data and in 1609 published his monumental work, *Astronomia Nova*, in which he stated his first two laws of planetary motion. Commenting on his discovery of elliptical orbits, Kepler wrote, "I was almost driven to madness in considering and calculating this matter. I could not find out why the planet would rather go on an elliptical orbit (rather than a circle). Oh ridiculous me!" It ultimately remained for Isaac Newton to discover the laws of gravitation that explained the reason for elliptical orbits.

Polar equation of ellipse in terms of $a$ and $e$:
$$r = \frac{a(1 - e^2)}{1 \pm e\cos\theta} \quad \text{or} \quad r = \frac{a(1 - e^2)}{1 \pm e\sin\theta} \tag{17–18}$$
$$r_0 = a(1 - e), \quad r_1 = a(1 + e) \tag{19–20}$$

#### Example 4
Halley's comet (last seen in 1986) has an eccentricity of $0.97$ and a semimajor axis of $a = 18.1\text{ AU}$.  
(a) Find the equation of its orbit in the polar coordinate system shown in Figure 10.6.12.  
(b) Find the period of its orbit.  
(c) Find its perihelion and aphelion distances.

**Solution (a).** $a(1 - e^2) = 18.1[1 - (0.97)^2] \approx 1.07 \implies r = \frac{1.07}{1 + 0.97\cos\theta}$.  
**Solution (b).** $T = (18.1)^{3/2} \approx 77\text{ years}$.  
**Solution (c).** $r_0 = 18.1(1 - 0.97) \approx 0.543\text{ AU} \approx 81,500,000\text{ km}$; $r_1 = 18.1(1 + 0.97) \approx 35.7\text{ AU} \approx 5,350,000,000\text{ km}$.

#### Example 5
An Apollo lunar lander orbits the Moon in an elliptic orbit with eccentricity $e = 0.12$ and semimajor axis $a = 2015\text{ km}$. Assuming the Moon to be a sphere of radius $1740\text{ km}$, find the minimum and maximum heights of the lander above the lunar surface (Figure 10.6.13).

**Solution.**
$$d_{\min} = r_0 - 1740 = 2015(1 - 0.12) - 1740 = 2015(0.88) - 1740 = 33.2\text{ km}$$
$$d_{\max} = r_1 - 1740 = 2015(1 + 0.12) - 1740 = 2015(1.12) - 1740 = 516.8\text{ km}$$

---

### QUICK CHECK EXERCISES 10.6
*(See page 763 for answers.)*

1. In each part, name the conic section described:  
   (a) The set of points whose distance to the point $(2, 3)$ is half the distance to the line $x + y = 1$ is $\underline{\quad}$.  
   (b) The set of points whose distance to the point $(2, 3)$ is equal to the distance to the line $x + y = 1$ is $\underline{\quad}$.  
   (c) The set of points whose distance to the point $(2, 3)$ is twice the distance to the line $x + y = 1$ is $\underline{\quad}$.
2. In each part: (i) Identify the polar graph as a parabola, an ellipse, or a hyperbola; (ii) state whether the directrix is above, below, to the left, or to the right of the pole; and (iii) find the distance from the pole to the directrix.  
   (a) $r = \frac{1}{4 + \cos\theta}$  
   (b) $r = \frac{1}{1 - 4\cos\theta}$  
   (c) $r = \frac{1}{4 + 4\sin\theta}$  
   (d) $r = \frac{4}{1 - \sin\theta}$
3. If the distance from a vertex of an ellipse to the nearest focus is $r_0$, and if the distance from that vertex to the farthest focus is $r_1$, then the semimajor axis is $a = \underline{\quad}$ and the semiminor axis is $b = \underline{\quad}$.
4. If the distance from a vertex of a hyperbola to the nearest focus is $r_0$, and if the distance from that vertex to the farthest focus is $r_1$, then the semifocal axis is $a = \underline{\quad}$ and the semiconjugate axis is $b = \underline{\quad}$.

---

### EXERCISE SET 10.6

**1–2 Find the eccentricity and the distance from the pole to the directrix, and sketch the graph in polar coordinates.**
1. (a) $r = \frac{3}{2 - 2\cos\theta}$ (b) $r = \frac{3}{2 + \sin\theta}$
2. (a) $r = \frac{4}{2 + 3\cos\theta}$ (b) $r = \frac{5}{3 + 3\sin\theta}$

**3–4 Use Formulas (3)–(6) to identify the type of conic and its orientation. Check your answer by generating the graph with a graphing utility.**
3. (a) $r = \frac{8}{1 - \sin\theta}$ (b) $r = \frac{16}{4 + 3\sin\theta}$
4. (a) $r = \frac{4}{2 - 3\sin\theta}$ (b) $r = \frac{12}{4 + \cos\theta}$

**5–6 Find a polar equation for the conic that has its focus at the pole and satisfies the stated conditions. Points are in polar coordinates and directrices in rectangular coordinates for simplicity.**
5. (a) Ellipse; $e = 3/4$; directrix $x = 2$.  
   (b) Parabola; directrix $x = 1$.  
   (c) Hyperbola; $e = 4/3$; directrix $y = 3$.
6. (a) Ellipse; ends of major axis $(2, \pi/2)$ and $(6, 3\pi/2)$.  
   (b) Parabola; vertex $(2, \pi)$.  
   (c) Hyperbola; $e = \sqrt{2}$; vertex $(2, 0)$.

**7–8 Find the distances from the pole to the vertices, and then apply Formulas (8)–(10) to find the equation of the ellipse in rectangular coordinates.**
7. (a) $r = \frac{6}{2 + \sin\theta}$ (b) $r = \frac{1}{2 - \cos\theta}$
8. (a) $r = \frac{6}{5 + 2\cos\theta}$ (b) $r = \frac{8}{4 - 3\sin\theta}$

**9–10 Find the distances from the pole to the vertices, and then apply Formulas (12)–(14) to find the equation of the hyperbola in rectangular coordinates.**
9. (a) $r = \frac{3}{1 + 2\sin\theta}$ (b) $r = \frac{5}{2 - 3\cos\theta}$
10. (a) $r = \frac{4}{1 - 2\sin\theta}$ (b) $r = \frac{15}{2 + 8\cos\theta}$

**11–12 Find a polar equation for the ellipse that has its focus at the pole and satisfies the stated conditions.**
11. (a) Directrix to the right of the pole; $a = 8; \; e = 1/2$.  
    (b) Directrix below the pole; $a = 4; \; e = 3/5$.
12. (a) Directrix to the left of the pole; $b = 4; \; e = 3/5$.  
    (b) Directrix above the pole; $c = 5; \; e = 1/5$.

13. Find the polar equation of an equilateral hyperbola with a focus at the pole and vertex $(5, 0)$.

#### FOCUS ON CONCEPTS
14. Prove that a hyperbola is an equilateral hyperbola if and only if $e = \sqrt{2}$.
15. (a) Show that the coordinates of the point $P$ on the hyperbola in Figure 10.6.1 satisfy the equation
    $$\sqrt{(x - c)^2 + y^2} = \frac{c}{a}x - a$$
    (b) Use the result obtained in part (a) to show that $PF/PD = c/a$.

16. (a) Show that the eccentricity of an ellipse can be expressed in terms of $r_0$ and $r_1$ as
    $$e = \frac{r_1 - r_0}{r_1 + r_0}$$
    (b) Show that $\frac{r_1}{r_0} = \frac{1 + e}{1 - e}$.

17. (a) Show that the eccentricity of a hyperbola can be expressed in terms of $r_0$ and $r_1$ as
    $$e = \frac{r_1 + r_0}{r_1 - r_0}$$
    (b) Show that $\frac{r_1}{r_0} = \frac{e + 1}{e - 1}$.

18. (a) Sketch the curves $r = \frac{1}{1 + \cos\theta}$ and $r = \frac{1}{1 - \cos\theta}$.  
    (b) Find polar coordinates of the intersections of the curves in part (a).  
    (c) Show that the curves are orthogonal, that is, their tangent lines are perpendicular at the points of intersection.

**19–22 True–False Determine whether the statement is true or false. Explain your answer.**
19. If an ellipse is not a circle, then the eccentricity of the ellipse is less than one.
20. A parabola has eccentricity greater than one.
21. If one ellipse has foci that are farther apart than those of a second ellipse, then the eccentricity of the first is greater than that of the second.
22. If $d$ is a positive constant, then the conic section with polar equation $r = \frac{d}{1 + \cos\theta}$ is a parabola.

**23–28 Use the following values, where needed:**
* $\text{radius of the Earth} = 4000\text{ mi} = 6440\text{ km}$
* $1\text{ year (Earth year)} = 365\text{ days (Earth days)}$
* $1\text{ AU} = 92.9 \times 10^6\text{ mi} = 150 \times 10^6\text{ km}$

23. The dwarf planet Pluto has eccentricity $e = 0.249$ and semimajor axis $a = 39.5\text{ AU}$.  
    (a) Find the period $T$ in years.  
    (b) Find the perihelion and aphelion distances.  
    (c) Choose a polar coordinate system with the center of the Sun at the pole, and find a polar equation of Pluto's orbit in that coordinate system.  
    (d) Make a sketch of the orbit with reasonably accurate proportions.

24. (a) Let $a$ be the semimajor axis of a planet's orbit around the Sun, and let $T$ be its period. Show that if $T$ is measured in days and $a$ is measured in kilometers, then
    $$T = (365 \times 10^{-9})(a/150)^{3/2}$$
    (b) Use the result in part (a) to find the period of the planet Mercury in days, given that its semimajor axis is $a = 57.95 \times 10^6\text{ km}$.  
    (c) Choose a polar coordinate system with the Sun at the pole, and find an equation for the orbit of Mercury in that coordinate system given that the eccentricity of the orbit is $e = 0.206$.  
    (d) Use a graphing utility to generate the orbit of Mercury from the equation obtained in part (c).

25. The Hale–Bopp comet, discovered independently on July 23, 1995 by Alan Hale and Thomas Bopp, has an orbital eccentricity of $e = 0.9951$ and a period of 2380 years.  
    (a) Find its semimajor axis in astronomical units (AU).  
    (b) Find its perihelion and aphelion distances.  
    (c) Choose a polar coordinate system with the center of the Sun at the pole, and find an equation for the Hale–Bopp orbit in that coordinate system.  
    (d) Make a sketch of the Hale–Bopp orbit with reasonably accurate proportions.

26. Mars has a perihelion distance of $204,520,000\text{ km}$ and an aphelion distance of $246,280,000\text{ km}$.  
    (a) Use these data to calculate the eccentricity, and compare your answer to the value given in Table 10.6.1.  
    (b) Find the period of Mars.  
    (c) Choose a polar coordinate system with the center of the Sun at the pole, and find an equation for the orbit of Mars in that coordinate system.  
    (d) Use a graphing utility to generate the orbit of Mars from the equation obtained in part (c).

27. Vanguard 1 was launched in March 1958 into an orbit around the Earth with eccentricity $e = 0.21$ and semimajor axis $8864.5\text{ km}$. Find the minimum and maximum heights of Vanguard 1 above the surface of the Earth.

28. The planet Jupiter is believed to have a rocky core of radius $10,000\text{ km}$ surrounded by two layers of hydrogen—a $40,000\text{ km}$ thick layer of compressed metallic-like hydrogen and a $20,000\text{ km}$ thick layer of ordinary molecular hydrogen. The visible features, such as the Great Red Spot, are at the outer surface of the molecular hydrogen layer. On November 6, 1997 the spacecraft Galileo was placed in a Jovian orbit to study the moon Europa. The orbit had eccentricity $0.814580$ and semimajor axis $3,514,918.9\text{ km}$. Find Galileo's minimum and maximum heights above the molecular hydrogen layer (Figure Ex-28).

29. **Writing.** Discuss how a hyperbola's eccentricity $e$ affects the shape of the hyperbola. How is the shape affected as $e$ approaches 1? As $e$ approaches $+\infty$? Draw some pictures to illustrate your conclusions.

30. **Writing.** Discuss the relationship between the eccentricity $e$ of an ellipse and the distance $z$ between the directrix and center of the ellipse. For example, if the foci remain fixed, what happens to $z$ as $e$ approaches 0?

#### QUICK CHECK ANSWERS 10.6
1. (a) an ellipse (b) a parabola (c) a hyperbola
2. (a) (i) ellipse (ii) to the right of the pole (iii) distance = 1  
   (b) (i) hyperbola (ii) to the left of the pole (iii) distance = $1/4$  
   (c) (i) parabola (ii) above the pole (iii) distance = $1/4$  
   (d) (i) parabola (ii) below the pole (iii) distance = 4
3. $\frac{1}{2}(r_1 + r_0); \quad \sqrt{r_0 r_1}$
4. $\frac{1}{2}(r_1 - r_0); \quad \sqrt{r_0 r_1}$

---

## CHAPTER 10 REVIEW EXERCISES

1. Find parametric equations for the portion of the circle $x^2 + y^2 = 2$ that lies outside the first quadrant, oriented clockwise. Check your work by generating the curve with a graphing utility.

2. (a) Suppose that the equations $x = f(t), \; y = g(t)$ describe a curve $C$ as $t$ increases from 0 to 1. Find parametric equations that describe the same curve $C$ but traced in the opposite direction as $t$ increases from 0 to 1.  
   (b) Check your work using the parametric graphing feature of a graphing utility by generating the line segment between $(1, 2)$ and $(4, 0)$ in both possible directions as $t$ increases from 0 to 1.

3. (a) Find the slope of the tangent line to the parametric curve $x = t^2 + 1, \; y = t/2$ at $t = -1$ and $t = 1$ without eliminating the parameter.  
   (b) Check your answers in part (a) by eliminating the parameter and differentiating a function of $x$.

4. Find $dy/dx$ and $d^2y/dx^2$ at $t = 2$ for the parametric curve $x = \frac{1}{2}t^2, \; y = \frac{1}{3}t^3$.

5. Find all values of $t$ at which a tangent line to the parametric curve $x = 2\cos t, \; y = 4\sin t$ is (a) horizontal (b) vertical.

6. Find the exact arc length of the curve
   $$x = 1 - 5t^4, \quad y = 4t^5 - 1 \quad (0 \le t \le 1)$$

7. In each part, find the rectangular coordinates of the point whose polar coordinates are given:  
   (a) $(-8, \pi/4)$ (b) $(7, -\pi/4)$ (c) $(8, 9\pi/4)$ (d) $(5, 0)$ (e) $(-2, -3\pi/2)$ (f) $(0, \pi)$

8. Express the point whose $xy$-coordinates are $(-1, 1)$ in polar coordinates with:  
   (a) $r > 0, \; 0 \le \theta < 2\pi$  
   (b) $r < 0, \; 0 \le \theta < 2\pi$  
   (c) $r > 0, \; -\pi < \theta \le \pi$  
   (d) $r < 0, \; -\pi < \theta \le \pi$

9. In each part, use a calculating utility to approximate the polar coordinates of the point whose rectangular coordinates are given:  
   (a) $(4, 3)$ (b) $(2, -5)$ (c) $(1, \tan^{-1} 1)$

10. In each part, state the name that describes the polar curve most precisely: a rose, a line, a circle, a limaçon, a cardioid, a spiral, a lemniscate, or none of these.  
    (a) $r = 3\cos\theta$ (b) $r = \cos 3\theta$ (c) $r = \frac{3}{\cos\theta}$ (d) $r = 3 - \cos\theta$ (e) $r = 1 - 3\cos\theta$ (f) $r^2 = 3\cos\theta$ (g) $r = (3\cos\theta)^2$ (h) $r = 1 + 3\theta$

11. In each part, identify the curve by converting the polar equation to rectangular coordinates. Assume that $a > 0$.  
    (a) $r = a\sec^2\frac{\theta}{2}$  
    (b) $r^2\cos 2\theta = a^2$  
    (c) $r = 4\csc\left(\theta - \frac{\pi}{4}\right)$  
    (d) $r = 4\cos\theta + 8\sin\theta$

12. In each part, express the given equation in polar coordinates:  
    (a) $x = 7$ (b) $x^2 + y^2 = 9$ (c) $x^2 + y^2 - 6y = 0$ (d) $4xy = 9$

**13–17 Sketch the curve in polar coordinates.**
13. $\theta = \pi/6$
14. $r = 6\cos\theta$
15. $r = 3(1 - \sin\theta)$
16. $r^2 = \sin 2\theta$
17. $r = 3 - \cos\theta$

18. (a) Show that the maximum value of the $y$-coordinate of points on the curve $r = 1/\sqrt{\theta}$ for $\theta$ in the interval $(0, \pi]$ occurs when $\tan\theta = 2\theta$.  
    (b) Use a calculating utility to solve the equation in part (a) to at least four decimal-place accuracy.  
    (c) Use the result of part (b) to approximate the maximum value of $y$ for $0 < \theta \le \pi$.

19. (a) Find the minimum and maximum $x$-coordinates of points on the cardioid $r = 1 - \cos\theta$.  
    (b) Find the minimum and maximum $y$-coordinates of points on the cardioid in part (a).

20. Determine the slope of the tangent line to the polar curve $r = 1 + \sin\theta$ at $\theta = \pi/4$.

21. A parametric curve of the form
    $$x = a\cot t + b\cos t, \quad y = a + b\sin t \quad (0 < t < 2\pi)$$
    is called a **conchoid of Nicomedes** (see Figure Ex-21 for the case $0 < a < b$).  
    (a) Describe how the conchoid $x = \cot t + 4\cos t, \; y = 1 + 4\sin t$ is generated as $t$ varies over the interval $0 < t < 2\pi$.  
    (b) Find the horizontal asymptote of the conchoid given in part (a).  
    (c) For what values of $t$ does the conchoid in part (a) have a horizontal tangent line? A vertical tangent line?  
    (d) Find a polar equation $r = f(\theta)$ for the conchoid in part (a), and then find polar equations for the tangent lines to the conchoid at the pole.

22. (a) Find the arc length of the polar curve $r = 1/\theta$ for $\pi/4 \le \theta \le \pi/2$.  
    (b) What can you say about the arc length of the portion of the curve that lies inside the circle $r = 1$?

23. Find the area of the region that is enclosed by the cardioid $r = 2 + 2\cos\theta$.
24. Find the area of the region in the first quadrant within the cardioid $r = 1 + \sin\theta$.
25. Find the area of the region that is common to the circles $r = 1, \; r = 2\cos\theta,$ and $r = 2\sin\theta$.
26. Find the area of the region that is inside the cardioid $r = a(1 + \sin\theta)$ and outside the circle $r = a\sin\theta$.

**27–30 Sketch the parabola, and label the focus, vertex, and directrix.**
27. $y^2 = 6x$
28. $x^2 = -9y$
29. $(y + 1)^2 = -7(x - 4)$
30. $(x - 1/2)^2 = 2(y - 1)$

**31–34 Sketch the ellipse, and label the foci, the vertices, and the ends of the minor axis.**
31. $\frac{x^2}{4} + \frac{y^2}{25} = 1$
32. $4x^2 + 9y^2 = 36$
33. $9(x - 1)^2 + 16(y - 3)^2 = 144$
34. $3(x + 2)^2 + 4(y + 1)^2 = 12$

**35–37 Sketch the hyperbola, and label the vertices, foci, and asymptotes.**
35. $\frac{x^2}{16} - \frac{y^2}{4} = 1$
36. $9y^2 - 4x^2 = 36$
37. $\frac{(x - 2)^2}{9} - \frac{(y - 4)^2}{4} = 1$

38. In each part, sketch the graph of the conic section with reasonably accurate proportions:  
    (a) $x^2 - 4x + 8y + 36 = 0$  
    (b) $3x^2 + 4y^2 - 30x - 8y + 67 = 0$  
    (c) $4x^2 - 5y^2 - 8x - 30y - 21 = 0$

**39–41 Find an equation for the conic described.**
39. A parabola with vertex $(0, 0)$ and focus $(0, -4)$.
40. An ellipse with the ends of the major axis $(0, \pm\sqrt{5})$ and the ends of the minor axis $(\pm 1, 0)$.
41. A hyperbola with vertices $(0, \pm 3)$ and asymptotes $y = \pm x$.

42. Hanging cables form parabolic arcs if they are subjected to uniformly distributed downward forces along their length.  
    (a) Assuming a parabolic model, find an equation for the cable in Figure Ex-42 (span $4200\text{ ft}$, sag $470\text{ ft}$), taking the $y$-axis to be vertical and the origin at the low point of the cable.  
    (b) Find the length of the cable between the supports.

43. Projectile trajectory with launch speed $v_0$, angle $\alpha$, height $y_0$:
    $$x = (v_0\cos\alpha)t, \quad y = y_0 + (v_0\sin\alpha)t - \frac{1}{2}gt^2$$
    (a) Show that the trajectory is a parabola.  
    (b) Find the coordinates of the vertex.

44. Mickey Mantle's April 17, 1953 Griffith Stadium home run ($50\text{ ft}$ wall at $391\text{ ft}$, initial height $3\text{ ft}$, angle $45^\circ$, $g = 32\text{ ft/s}^2$):  
    (a) Speed of the ball as it left the bat.  
    (b) Maximum height of the ball.  
    (c) Distance along the ground from home plate to where the ball struck the ground.

**45–47 Rotate the coordinate axes to remove the $xy$-term, and then name the conic.**
45. $x^2 + y^2 - 3xy - 3 = 0$
46. $7x^2 + 2\sqrt{3}xy + 5y^2 - 4 = 0$
47. $4\sqrt{5}x^2 + 4\sqrt{5}xy + \sqrt{5}y^2 + 5x - 10y = 0$

48. Rotate the coordinate axes to show that the graph of
    $$17x^2 - 312xy + 108y^2 + 1080x - 1440y + 4500 = 0$$
    is a hyperbola. Then find its vertices, foci, and asymptotes.

49. In each part: (i) Identify the polar graph as a parabola, an ellipse, or a hyperbola; (ii) state whether the directrix is above, below, to the left, or to the right of the pole; and (iii) find the distance from the pole to the directrix.  
    (a) $r = \frac{1}{3 + \cos\theta}$  
    (b) $r = \frac{1}{1 - 3\cos\theta}$  
    (c) $r = \frac{1}{3(1 + \sin\theta)}$  
    (d) $r = \frac{3}{1 - \sin\theta}$

**50–51 Find an equation in $xy$-coordinates for the conic section that satisfies the given conditions.**
50. (a) Ellipse with eccentricity $e = 2/7$ and ends of the minor axis at the points $(0, \pm 3)$.  
    (b) Parabola with vertex at the origin, focus on the $y$-axis, and directrix passing through the point $(7, 4)$.  
    (c) Hyperbola that has the same foci as the ellipse $3x^2 + 16y^2 = 48$ and asymptotes $y = \pm 2x/3$.
51. (a) Ellipse with center $(-3, 2)$, vertex $(2, 2)$, and eccentricity $e = 4/5$.  
    (b) Parabola with focus $(-2, -2)$ and vertex $(-2, 0)$.  
    (c) Hyperbola with vertex $(-1, 7)$ and asymptotes $y - 5 = \pm 8(x + 1)$.

52. Use the parametric equations $x = a\cos t, \; y = b\sin t$ to show that the circumference $C$ of an ellipse with semimajor axis $a$ and eccentricity $e$ is
    $$C = 4a\int_0^{\pi/2} \sqrt{1 - e^2\sin^2 u}\,du$$

53. Use Simpson's rule or the numerical integration capability of a graphing utility to approximate the circumference of the ellipse $4x^2 + 9y^2 = 36$ from the integral obtained in Exercise 52.

54. (a) Calculate the eccentricity of the Earth's orbit, given that the ratio of the distance between the center of the Earth and the center of the Sun at perihelion to the distance between the centers at aphelion is $59/61$.  
    (b) Find the distance between the center of the Earth and the center of the Sun at perihelion, given that the average value of the perihelion and aphelion distances between the centers is 93 million miles.  
    (c) Use the result in Exercise 52 and Simpson's rule or the numerical integration capability of a graphing utility to approximate the distance that the Earth travels in 1 year (one revolution around the Sun).

---

## CHAPTER 10 MAKING CONNECTIONS

1. **Clothoid or Cornu Spiral:**  
   The Fresnel sine and cosine functions are defined as
   $$S(x) = \int_0^x \sin\left(\frac{\pi t^2}{2}\right)dt \quad \text{and} \quad C(x) = \int_0^x \cos\left(\frac{\pi t^2}{2}\right)dt$$
   The parametric curve
   $$x = C(t) = \int_0^t \cos\left(\frac{\pi u^2}{2}\right)du, \quad y = S(t) = \int_0^t \sin\left(\frac{\pi u^2}{2}\right)du \quad (-\infty < t < +\infty)$$
   is called a **clothoid** or **Cornu spiral** in honor of the French scientist Marie Alfred Cornu (1841–1902).  
   (a) Use a CAS to graph the Cornu spiral.  
   (b) Describe the behavior of the spiral as $t \to +\infty$ and as $t \to -\infty$.  
   (c) Find the arc length of the spiral for $-1 \le t \le 1$.

2. (a) Figure Ex-2 shows an ellipse with semimajor axis $a$ and semiminor axis $b$. Express the coordinates of the points $P, Q,$ and $R$ in terms of $t$.  
   (b) How does the geometric interpretation of the parameter $t$ differ between a circle $x = a\cos t, \; y = a\sin t$ and an ellipse $x = a\cos t, \; y = b\sin t$?

3. Figure Ex-3 shows Kepler's method for constructing a parabola. A piece of string the length of the left edge of the drafting triangle is tacked to the vertex $Q$ of the triangle and the other end to a fixed point $F$. A pencil holds the string taut against the base of the triangle as the edge opposite $Q$ slides along a horizontal line $L$ below $F$. Show that the pencil traces an arc of a parabola with focus $F$ and directrix $L$.

4. Figure Ex-4 shows a method for constructing a hyperbola. A corner of a ruler is pinned to a fixed point $F_1$ and the ruler is free to rotate about that point. A piece of string whose length is less than that of the ruler is tacked to a point $F_2$ and to the free corner $Q$ of the ruler on the same edge as $F_1$. A pencil holds the string taut against the top edge of the ruler as the ruler rotates about the point $F_1$. Show that the pencil traces an arc of a hyperbola with foci $F_1$ and $F_2$.

5. Consider an ellipse $E$ with semimajor axis $a$ and semiminor axis $b$, and set $c = \sqrt{a^2 - b^2}$.  
   (a) Show that the ellipsoid that results when $E$ is revolved about its major axis has volume $V = \frac{4}{3}\pi a b^2$ and surface area
   $$S = 2\pi a b\left[\frac{b}{a} + \frac{a}{c}\sin^{-1}\left(\frac{c}{a}\right)\right]$$
   (b) Show that the ellipsoid that results when $E$ is revolved about its minor axis has volume $V = \frac{4}{3}\pi a^2 b$ and surface area
   $$S = 2\pi a b\left[\frac{a}{b} + \frac{b}{c}\ln\left(\frac{a + c}{b}\right)\right]$$

---

## EXPANDING THE CALCULUS HORIZON
To learn how polar coordinates and conic sections can be used to analyze the possibility of a collision between a comet and Earth, see the module entitled *Comet Collision* at: `www.wiley.com/college/anton`
