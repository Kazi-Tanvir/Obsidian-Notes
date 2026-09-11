# APPENDICES

---

## APPENDIX A: GRAPHING FUNCTIONS USING CALCULATORS AND COMPUTER ALGEBRA SYSTEMS

### GRAPHING CALCULATORS AND COMPUTER ALGEBRA SYSTEMS

The development of new technology has significantly changed how and where mathematicians, engineers, and scientists perform their work, as well as their approach to problem solving. Among the most significant of these developments are programs called **Computer Algebra Systems (abbreviated CAS)**, the most common being *Mathematica* and *Maple*.

Computer algebra systems not only have graphing capabilities, but, as their name suggests, they can perform many of the symbolic computations that occur in algebra, calculus, and branches of higher mathematics. For example, it is a trivial task for a CAS to perform the factorization
$$x^6 + 23x^5 + 147x^4 - 139x^3 - 3464x^2 - 2112x + 23040 = (x + 5)(x - 3)^2(x + 8)^3$$
or the exact numerical computation
$$\left(\frac{63456}{3177295} - \frac{43907}{22854377}\right)^3 = \frac{2251912457164208291259320230122866923}{382895955819369204449565945369203764688375}$$

Technology has also made it possible to generate graphs of equations and functions in seconds that in the past might have taken hours. Figure A.1 shows the graphs of the function $f(x) = x^4 - x^3 - 2x^2$ produced with various graphing utilities; the first two were generated with the CAS programs, *Mathematica* and *Maple*, and the third with a graphing calculator. Graphing calculators produce coarser graphs than most computer programs but have the advantage of being compact and portable.

---

### VIEWING WINDOWS

Graphing utilities can only show a portion of the $xy$-plane in the viewing screen, so the first step in graphing an equation is to determine which rectangular portion of the $xy$-plane you want to display. This region is called the **viewing window** (or **viewing rectangle**). For example, in Figure A.1 the viewing window extends over the interval $[-3, 3]$ in the $x$-direction and over the interval $[-4, 4]$ in the $y$-direction, so we denote the viewing window by $[-3, 3] \times [-4, 4]$ (read "[-3, 3] by [-4, 4]"). In general, if the viewing window is $[a, b] \times [c, d]$, then the window extends between $x = a$ and $x = b$ in the $x$-direction and between $y = c$ and $y = d$ in the $y$-direction. We will call $[a, b]$ the **$x$-interval** for the window and $[c, d]$ the **$y$-interval** for the window (Figure A.2).

Different graphing utilities designate viewing windows in different ways. For example, the first two graphs in Figure A.1 were produced by the commands:
* `Plot[x^4 - x^3 - 2*x^2, {x, -3, 3}, PlotRange->{-4, 4}]` (*Mathematica*)
* `plot(x^4 - x^3 - 2*x^2, x = -3..3, y = -4..4);` (*Maple*)

and the last graph was produced on a graphing calculator by pressing the `GRAPH` button after setting the values for the variables that determine the $x$-interval and $y$-interval to be:
$$\text{xMin} = -3, \quad \text{xMax} = 3, \quad \text{yMin} = -4, \quad \text{yMax} = 4$$

> **TECHNOLOGY MASTERY**  
> Use your graphing utility to generate the graph of the function $f(x) = x^4 - x^3 - 2x^2$ in the window $[-3, 3] \times [-4, 4]$.

---

### TICK MARKS AND GRID LINES

To help locate points in a viewing window, graphing utilities provide methods for drawing **tick marks** (also called **scale marks**). With computer programs such as *Mathematica* and *Maple*, there are specific commands for designating the spacing between tick marks, but if the user does not specify the spacing, then the programs make certain default choices. For example, in the first two parts of Figure A.1, the tick marks shown were the default choices.

On some graphing calculators the spacing between tick marks is determined by two scale variables (also called **scale factors**), which we will denote by
$$\text{xScl} \quad \text{and} \quad \text{yScl}$$
(The notation varies among calculators.) These variables specify the spacing between the tick marks in the $x$- and $y$-directions, respectively. For example, in the third part of Figure A.1 the window and tick marks were designated by the settings:
$$\text{xMin} = -3, \quad \text{xMax} = 3, \quad \text{yMin} = -4, \quad \text{yMax} = 4, \quad \text{xScl} = 1, \quad \text{yScl} = 1$$

Most graphing utilities allow for variations in the design and positioning of tick marks. For example, Figure A.3 shows two variations of the graphs in Figure A.1; the first was generated on a computer using an option for placing the ticks and numbers on the edges of a box, and the second was generated on a graphing calculator using an option for drawing grid lines to simulate graph paper.

#### Example 1
Figure A.4 shows the window $[-5, 5] \times [-5, 5]$ with the tick marks spaced $0.5$ unit apart in the $x$-direction and $10$ units apart in the $y$-direction. No tick marks are actually visible in the $y$-direction because the tick mark at the origin is covered by the $x$-axis, and all other tick marks in that direction fall outside of the viewing window.

#### Example 2
Figure A.5 shows the window $[-10, 10] \times [-10, 10]$ with the tick marks spaced $0.1$ unit apart in the $x$- and $y$-directions. In this case the tick marks are so close together that they create thick lines on the coordinate axes. When this occurs you will usually want to increase the scale factors to reduce the number of tick marks to make them legible.

> **TECHNOLOGY MASTERY**  
> Graphing calculators provide a way of clearing all settings and returning them to *default values*. For example, on one calculator the default window is $[-10, 10] \times [-10, 10]$ and the default scale factors are $\text{xScl} = 1$ and $\text{yScl} = 1$. Read your documentation to determine the default values for your calculator and how to restore the default settings. If you are using a CAS, read your documentation to determine the commands for specifying the spacing between tick marks.

---

### CHOOSING A VIEWING WINDOW

When the graph of a function extends indefinitely in some direction, no single viewing window can show it all. In such cases the choice of the viewing window can affect one’s perception of how the graph looks. For example, Figure A.6 shows a computer-generated graph of $y = 9 - x^2$, and Figure A.7 shows four views of this graph generated on a calculator:
* In part (a) the graph falls completely outside of the window, so the window is blank (except for the ticks and axes).
* In part (b) the graph is broken into two pieces because it passes in and out of the window.
* In part (c) the graph appears to be a straight line because we have zoomed in on a very small segment of the curve.
* In part (d) we have a more revealing picture of the graph shape because the window encompasses the high point on the graph and the intersections with the $x$-axis.

#### Example 3
Use the domain and range of the function $f(x) = \sqrt{12 - 3x^2}$ to determine a viewing window that contains the entire graph.

**Solution.** The natural domain of $f$ is $[-2, 2]$ and the range is $[0, \sqrt{12}]$ (verify), so the entire graph will be contained in the viewing window $[-2, 2] \times [0, \sqrt{12}]$. For clarity, it is desirable to use a slightly larger window to avoid having the graph too close to the edges of the screen. For example, taking the viewing window to be $[-3, 3] \times [-1, 4]$ yields the graph in Figure A.8.

Sometimes it will be impossible to find a single window that shows all important features of a graph, in which case you will need to decide what is most important for the problem at hand and choose the window appropriately.

#### Example 4
Graph the equation $y = x^3 - 12x^2 + 18$ in the following windows and discuss the advantages and disadvantages of each window:
(a) $[-10, 10] \times [-10, 10]$ with $\text{xScl} = 1, \text{yScl} = 1$  
(b) $[-20, 20] \times [-20, 20]$ with $\text{xScl} = 1, \text{yScl} = 1$  
(c) $[-20, 20] \times [-300, 20]$ with $\text{xScl} = 1, \text{yScl} = 20$  
(d) $[-5, 15] \times [-300, 20]$ with $\text{xScl} = 1, \text{yScl} = 20$  
(e) $[1, 2] \times [-1, 1]$ with $\text{xScl} = 0.1, \text{yScl} = 0.1$

**Solution (a).** The window in Figure A.9a has chopped off the portion of the graph that intersects the $y$-axis, and it shows only two of three possible real roots for the given cubic polynomial. To remedy these problems we need to widen the window in both the $x$- and $y$-directions.

**Solution (b).** The window in Figure A.9b shows the intersection of the graph with the $y$-axis and the three real roots, but it has chopped off the portion of the graph between the two positive roots. Moreover, the ticks in the $y$-direction are nearly illegible because they are so close together. We need to extend the window in the negative $y$-direction and increase $\text{yScl}$. We do not know how far to extend the window, so some experimentation will be required to obtain what we want.

**Solution (c).** The window in Figure A.9c shows all of the main features of the graph. However, we have some wasted space in the $x$-direction. We can improve the picture by shortening the window in the $x$-direction appropriately.

**Solution (d).** The window in Figure A.9d shows all of the main features of the graph without a lot of wasted space. However, the window does not provide a clear view of the roots. To get a closer view of the roots we must forget about showing all of the main features of the graph and choose windows that zoom in on the roots themselves.

**Solution (e).** The window in Figure A.9e displays very little of the graph, but it clearly shows that the root in the interval $[1, 2]$ is approximately $1.3$.

> **TECHNOLOGY MASTERY**  
> Sometimes you will want to determine the viewing window by choosing the $x$-interval and allowing the graphing utility to determine a $y$-interval that encompasses the maximum and minimum values of the function over the $x$-interval. Most graphing utilities provide some method for doing this, so read your documentation to determine how to use this feature. Allowing the graphing utility to determine the $y$-interval of the window takes some of the guesswork out of problems like that in part (b) of the preceding example.

---

### ZOOMING

The process of enlarging or reducing the size of a viewing window is called **zooming**. If you reduce the size of the window, you see less of the graph as a whole, but more detail of the part shown; this is called **zooming in**. In contrast, if you enlarge the size of the window, you see more of the graph as a whole, but less detail of the part shown; this is called **zooming out**. Most graphing calculators provide menu items for zooming in or zooming out by fixed factors. For example, on one calculator the amount of enlargement or reduction is controlled by setting values for two **zoom factors**, denoted by `xFact` and `yFact`. If
$$\text{xFact} = 10 \quad \text{and} \quad \text{yFact} = 5$$
then each time a zoom command is executed the viewing window is enlarged or reduced by a factor of 10 in the $x$-direction and a factor of 5 in the $y$-direction. With computer programs such as *Mathematica* and *Maple*, zooming is controlled by adjusting the $x$-interval and $y$-interval directly; however, there are ways to automate this by programming.

---

### COMPRESSION

Enlarging the viewing window for a graph has the geometric effect of compressing the graph, since more of the graph is packed into the calculator screen. If the compression is sufficiently great, then some of the detail in the graph may be lost. Thus, the choice of the viewing window frequently depends on whether you want to see more of the graph or more of the detail. Figure A.10 shows two views of the equation
$$y = x^5(x - 2)$$
In part (a) of the figure the $y$-interval is very large, resulting in a vertical compression that obscures the detail in the vicinity of the $x$-axis. In part (b) the $y$-interval is smaller, and consequently we see more of the detail in the vicinity of the $x$-axis but less of the graph in the $y$-direction.

#### Example 5
The function $f(x) = x + 0.01\sin(50\pi x)$ is the sum of $f_1(x) = x$, whose graph is the line $y = x$, and $f_2(x) = 0.01\sin(50\pi x)$, whose graph is a sinusoidal curve with amplitude $0.01$ and period $2\pi/(50\pi) = 0.04$. This suggests that the graph of $f(x)$ will follow the general path of the line $y = x$ but will have bumps resulting from the contributions of the sinusoidal oscillations, as shown in part (c) of Figure A.11. Generate the four graphs shown in Figure A.11 and explain why the oscillations are visible only in part (c).

**Solution.** To generate the four graphs, you first need to put your utility in radian mode. (In this text we follow the convention that angles are measured in radians unless degree measure is specified.) Because the windows in successive parts of the example are decreasing in size by a factor of 10, calculator users can generate successive graphs by using the zoom feature with the zoom factors set to 10 in both the $x$- and $y$-directions.
(a) In Figure A.11a the graph appears to be a straight line because the vertical compression has hidden the small sinusoidal oscillations (their amplitude is only $0.01$).
(b) In Figure A.11b small bumps begin to appear on the line because there is less vertical compression.
(c) In Figure A.11c the oscillations have become clear because the vertical scale is more in keeping with the amplitude of the oscillations.
(d) In Figure A.11d the graph appears to be a straight line because we have zoomed in on such a small portion of the curve.

---

### ASPECT RATIO DISTORTION

Figure A.12a shows a circle of radius 5 and two perpendicular lines graphed in the window $[-10, 10] \times [-10, 10]$ with $\text{xScl} = 1$ and $\text{yScl} = 1$. However, the circle is distorted and the lines do not appear perpendicular because the calculator has not used the same length for 1 unit on the $x$-axis and 1 unit on the $y$-axis. (Compare the spacing between the ticks on the axes.) This is called **aspect ratio distortion**. Many calculators provide a menu item for automatically correcting the distortion by adjusting the viewing window appropriately. For example, one calculator makes this correction to the viewing window $[-10, 10] \times [-10, 10]$ by changing it to
$$[-16.9970674487, 16.9970674487] \times [-10, 10]$$
(Figure A.12b). With computer programs such as *Mathematica* and *Maple*, aspect ratio distortion is controlled with adjustments to the physical dimensions of the viewing window on the computer screen, rather than altering the $x$- and $y$-intervals of the viewing window.

---

### SAMPLING ERROR

The viewing window of a graphing utility is composed of a rectangular grid of small rectangular blocks called **pixels**. For black-and-white displays each pixel has two states—an activated (or dark) state and a deactivated (or light) state. A graph is formed by activating appropriate pixels to produce the curve shape. In one popular calculator the grid of pixels consists of 63 rows of 127 pixels each (Figure A.13), in which case we say that the screen has a **resolution** of $127 \times 63$ (pixels in each row $\times$ number of rows). A typical resolution for a computer screen is $1280 \times 1024$. The greater the resolution, the smoother the graphs tend to appear on the screen.

> **TECHNOLOGY MASTERY**  
> If you are using a graphing calculator, read the documentation to determine its resolution.

The procedure that a graphing utility uses to generate a graph is similar to plotting points by hand: When an equation is entered and a window is chosen, the utility selects the $x$-coordinates of certain pixels (the choice of which depends on the window being used) and computes the corresponding $y$-coordinates. It then activates the pixels whose coordinates most closely match those of the calculated points and uses a built-in algorithm to activate additional intermediate pixels to create the curve shape. This process is not perfect, and it is possible that a particular window will produce a false impression about the graph shape because important characteristics of the graph occur between the computed points. This is called **sampling error**. For example, Figure A.14 shows the graph of $y = \cos(10\pi x)$ produced by a popular calculator in four different windows. (Your calculator may produce different results.) The graph in part (a) has the correct shape, but the other three do not because of sampling error:
* In part (b) the plotted pixels happened to fall at the peaks of the cosine curve, giving the false impression that the graph is a horizontal line.
* In part (c) the plotted pixels fell at successively higher points along the graph.
* In part (d) the plotted points fell in some regular pattern that created yet another misleading impression of the graph shape.

> **REMARK**  
> For trigonometric graphs with rapid oscillations, Figure A.14 suggests that restricting the $x$-interval to a few periods is likely to produce a more accurate representation about the graph shape.

---

### FALSE GAPS

Sometimes graphs that are continuous appear to have gaps when they are generated on a calculator. These **false gaps** typically occur where the graph rises so rapidly that vertical space is opened up between successive pixels.

#### Example 6
Figure A.15 shows the graph of the semicircle $y = \sqrt{9 - x^2}$ in two viewing windows. Although this semicircle has $x$-intercepts at the points $x = \pm 3$, part (a) of the figure shows false gaps at those points because there are no pixels with $x$-coordinates $\pm 3$ in the window selected. In part (b) no gaps occur because there are pixels with $x$-coordinates $x = \pm 3$ in the window being used.

---

### FALSE LINE SEGMENTS

In addition to creating false gaps in continuous graphs, calculators can err in the opposite direction by placing **false line segments** in the gaps of discontinuous curves.

#### Example 7
Figure A.16a shows the graph of $y = 1/(x - 1)$ in the default window on a calculator. Although the graph appears to contain vertical line segments near $x = 1$, they should not be there. There is actually a gap in the curve at $x = 1$, since a division by zero occurs at that point (Figure A.16b).

---

### ERRORS OF OMISSION

Most graphing utilities use logarithms to evaluate functions with fractional exponents such as $f(x) = x^{2/3} = \sqrt[3]{x^2}$. However, because logarithms are only defined for positive numbers, many (but not all) graphing utilities will omit portions of the graphs of functions with fractional exponents. For example, one calculator graphs $y = x^{2/3}$ as in Figure A.17a, whereas the actual graph is as in Figure A.17b. (For a way to circumvent this problem, see the discussion preceding Exercise 23.)

> **TECHNOLOGY MASTERY**  
> Determine whether your graphing utility produces the graph of the equation $y = x^{2/3}$ for both positive and negative values of $x$.

---

### WHAT IS THE TRUE SHAPE OF A GRAPH?

Although graphing utilities are powerful tools for generating graphs quickly, they can produce misleading graphs as a result of compression, sampling error, false gaps, and false line segments. In short, graphing utilities can suggest graph shapes, but they cannot establish them with certainty. Thus, the more you know about the functions you are graphing, the easier it will be to choose good viewing windows, and the better you will be able to judge the reasonableness of the results produced by your graphing utility.

---

### GENERATING PARAMETRIC CURVES WITH GRAPHING UTILITIES

Many graphing utilities allow you to graph equations of the form $y = f(x)$ but not equations of the form $x = g(y)$. Sometimes you will be able to rewrite $x = g(y)$ in the form $y = f(x)$; however, if this is inconvenient or impossible, then you can graph $x = g(y)$ by introducing a parameter $t = y$ and expressing the equation in the parametric form $x = g(t), \; y = t$. (You may have to experiment with various intervals for $t$ to produce a complete graph.)

#### Example 8
Use a graphing utility to graph the equation $x = 3y^5 - 5y^3 + 1$.

**Solution.** If we let $t = y$ be the parameter, then the equation can be written in parametric form as
$$x = 3t^5 - 5t^3 + 1, \quad y = t$$
Figure A.18 shows the graph of these equations for $-1.5 \le t \le 1.5$.

Some parametric curves are so complex that it is virtually impossible to visualize them without using some kind of graphing utility. Figure A.19 shows three such curves:
1. $x = 31\cos t - 7\cos(31/7)t, \; y = 31\sin t - 7\sin(31/7)t \quad (0 \le t \le 14\pi)$
2. $x = 17\cos t + 7\cos(17/7)t, \; y = 17\sin t - 7\sin(17/7)t \quad (0 \le t \le 14\pi)$
3. $x = \cos t + (1/2)\cos 7t + (1/3)\sin 17t, \; y = \sin t + (1/2)\sin 7t + (1/3)\cos 17t \quad (0 \le t \le 2\pi)$

---

### GRAPHING INVERSE FUNCTIONS WITH GRAPHING UTILITIES

Most graphing utilities cannot graph inverse functions directly. However, there is a way of graphing inverse functions by expressing the graphs parametrically. To see how this can be done, suppose that we are interested in graphing the inverse of a one-to-one function $f$. We know that the equation $y = f(x)$ can be expressed parametrically as
$$x = t, \quad y = f(t) \tag{1}$$
and we know that the graph of $f^{-1}$ can be obtained by interchanging $x$ and $y$, since this reflects the graph of $f$ about the line $y = x$. Thus, from (1) the graph of $f^{-1}$ can be represented parametrically as
$$x = f(t), \quad y = t \tag{2}$$

For example, Figure A.20 shows the graph of $f(x) = x^5 + x + 1$ and its inverse generated with a graphing utility. The graph of $f$ was generated from the parametric equations
$$x = t, \quad y = t^5 + t + 1$$
and the graph of $f^{-1}$ was generated from the parametric equations
$$x = t^5 + t + 1, \quad y = t$$

---

### TRANSLATION

If a parametric curve $C$ is given by the equations $x = f(t), \; y = g(t)$, then adding a constant to $f(t)$ translates the curve $C$ in the $x$-direction, and adding a constant to $g(t)$ translates it in the $y$-direction. Thus, a circle of radius $r$, centered at $(x_0, y_0)$ can be represented parametrically as
$$x = x_0 + r\cos t, \quad y = y_0 + r\sin t \quad (0 \le t \le 2\pi)$$
(Figure A.21). If desired, we can eliminate the parameter from these equations by noting that
$$(x - x_0)^2 + (y - y_0)^2 = (r\cos t)^2 + (r\sin t)^2 = r^2$$
Thus, we have obtained the familiar equation in rectangular coordinates for a circle of radius $r$, centered at $(x_0, y_0)$:
$$(x - x_0)^2 + (y - y_0)^2 = r^2$$

---

### SCALING

If a parametric curve $C$ is given by the equations $x = f(t), \; y = g(t)$, then multiplying $f(t)$ by a constant stretches or compresses $C$ in the $x$-direction, and multiplying $g(t)$ by a constant stretches or compresses $C$ in the $y$-direction. For example, we would expect the parametric equations
$$x = 3\cos t, \quad y = 2\sin t \quad (0 \le t \le 2\pi)$$
to represent an ellipse, centered at the origin, since the graph of these equations results from stretching the unit circle
$$x = \cos t, \quad y = \sin t \quad (0 \le t \le 2\pi)$$
by a factor of 3 in the $x$-direction and a factor of 2 in the $y$-direction. In general, if $a$ and $b$ are positive constants, then the parametric equations
$$x = a\cos t, \quad y = b\sin t \quad (0 \le t \le 2\pi) \tag{3}$$
represent an ellipse, centered at the origin, and extending between $-a$ and $a$ on the $x$-axis and between $-b$ and $b$ on the $y$-axis (Figure A.22). The numbers $a$ and $b$ are called the **semiaxes** of the ellipse. If desired, we can eliminate the parameter $t$ in (3) and rewrite the equations in rectangular coordinates as
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \tag{4}$$

> **TECHNOLOGY MASTERY**  
> Use the parametric capability of your graphing utility to generate an ellipse that is centered at the origin and that extends between $-4$ and $4$ in the $x$-direction and between $-3$ and $3$ in the $y$-direction. Generate an ellipse with the same dimensions, but translated so that its center is at the point $(2, 3)$.

---

### EXERCISE SET A

1–4 Use a graphing utility to generate the graph of $f$ in the given viewing windows, and specify the window that you think gives the best view of the graph.
1. $f(x) = x^4 - x^2$  
   (a) $[-50, 50] \times [-50, 50]$ (b) $[-5, 5] \times [-5, 5]$ (c) $[-2, 2] \times [-2, 2]$ (d) $[-2, 2] \times [-1, 1]$ (e) $[-1.5, 1.5] \times [-0.5, 0.5]$
2. $f(x) = x^5 - x^3$  
   (a) $[-50, 50] \times [-50, 50]$ (b) $[-5, 5] \times [-5, 5]$ (c) $[-2, 2] \times [-2, 2]$ (d) $[-2, 2] \times [-1, 1]$ (e) $[-1.5, 1.5] \times [-0.5, 0.5]$
3. $f(x) = x^2 + 12$  
   (a) $[-1, 1] \times [13, 15]$ (b) $[-2, 2] \times [11, 15]$ (c) $[-4, 4] \times [10, 28]$ (d) A window of your choice
4. $f(x) = -12 - x^2$  
   (a) $[-1, 1] \times [-15, -13]$ (b) $[-2, 2] \times [-15, -11]$ (c) $[-4, 4] \times [-28, -10]$ (d) A window of your choice

5–6 Use the domain and range of $f$ to determine a viewing window that contains the entire graph, and generate the graph in that window.
5. $f(x) = \sqrt{16 - 2x^2}$
6. $f(x) = \sqrt{3 - 2x - x^2}$

7–14 Generate the graph of $f$ in a viewing window that you think is appropriate.
7. $f(x) = x^2 - 9x - 36$
8. $f(x) = \frac{x + 7}{x - 9}$
9. $f(x) = 2\cos(80x)$
10. $f(x) = 12\sin(x/80)$
11. $f(x) = 300 - 10x^2 + 0.01x^3$
12. $f(x) = x(30 - 2x)(25 - 2x)$
13. $f(x) = x^2 + \frac{1}{x}$
14. $f(x) = \sqrt{11x - 18}$

15–16 Generate the graph of $f$ and determine whether your graphs contain false line segments. Sketch the actual graph and see if you can make the false line segments disappear by changing the viewing window.
15. $f(x) = \frac{x}{x^2 - 1}$
16. $f(x) = \frac{x^2}{4 - x^2}$

17. The graph of the equation $x^2 + y^2 = 16$ is a circle of radius 4 centered at the origin.  
    (a) Find a function whose graph is the upper semicircle and graph it.  
    (b) Find a function whose graph is the lower semicircle and graph it.  
    (c) Graph the upper and lower semicircles together. If the combined graphs do not appear circular, see if you can adjust the viewing window to eliminate the aspect ratio distortion.  
    (d) Graph the portion of the circle in the first quadrant.  
    (e) Is there a function whose graph is the right half of the circle? Explain.

18. In each part, graph the equation by solving for $y$ in terms of $x$ and graphing the resulting functions together.  
    (a) $x^2/4 + y^2/9 = 1$  
    (b) $y^2 - x^2 = 1$

19. Read the documentation for your graphing utility to determine how to graph functions involving absolute values, and graph the given equation.  
    (a) $y = |x|$  
    (b) $y = |x - 1|$  
    (c) $y = |x| - 1$  
    (d) $y = |\sin x|$  
    (e) $y = \sin |x|$  
    (f) $y = |x| - |x + 1|$

20. Based on your knowledge of the absolute value function, sketch the graph of $f(x) = |x|/x$. Check your result using a graphing utility.

21–22 Most graphing utilities provide some way of graphing functions that are defined piecewise; read the documentation for your graphing utility to find out how to do this. However, if your goal is just to find the general shape of the graph, you can graph each portion of the function separately and combine the pieces with a hand-drawn sketch. Use this method in these exercises.
21. Draw the graph of
$$f(x) = \begin{cases} \sqrt[3]{x - 2}, & x \le 2 \\ x^3 - 2x - 4, & x > 2 \end{cases}$$
22. Draw the graph of
$$f(x) = \begin{cases} x^3 - x^2, & x \le 1 \\ \frac{1}{1 - x}, & 1 < x < 4 \\ x^2\cos\sqrt{x}, & 4 \le x \end{cases}$$

23–24 We noted in the text that for functions involving fractional exponents (or radicals), graphing utilities sometimes omit portions of the graph. If $f(x) = x^{p/q}$, where $p/q$ is a positive fraction in lowest terms, then you can circumvent this problem as follows:
* If $p$ is even and $q$ is odd, then graph $g(x) = |x|^{p/q}$ instead of $f(x)$.
* If $p$ is odd and $q$ is odd, then graph $g(x) = (|x|/x)|x|^{p/q}$ instead of $f(x)$.
23. (a) Generate the graphs of $f(x) = x^{2/5}$ and $g(x) = |x|^{2/5}$, and determine whether your graphing utility missed part of the graph of $f$.  
    (b) Generate the graphs of the functions $f(x) = x^{1/5}$ and $g(x) = (|x|/x)|x|^{1/5}$, and determine whether your graphing utility missed part of the graph of $f$.  
    (c) Generate a graph of the function $f(x) = (x - 1)^{4/5}$ that shows all of its important features.  
    (d) Generate a graph of the function $f(x) = (x + 1)^{3/4}$ that shows all of its important features.
24. The graphs of $y = (x^2 - 4)^{2/3}$ and $y = [(x^2 - 4)^2]^{1/3}$ should be the same. Does your graphing utility produce the same graph for both equations? If not, what do you think is happening?

25. In each part, graph the function for various values of $c$, and write a paragraph or two that describes how changes in $c$ affect the graph in each case.  
    (a) $y = cx^2$  
    (b) $y = x^2 + cx$  
    (c) $y = x^2 + x + c$

26. The graph of an equation of the form $y^2 = x(x - a)(x - b)$ (where $0 < a < b$) is called a **bipartite cubic**.  
    (a) Graph the bipartite cubic $y^2 = x(x - 1)(x - 2)$ by solving for $y$ in terms of $x$ and graphing the two resulting functions.  
    (b) Find the $x$-intercepts of the bipartite cubic $y^2 = x(x - a)(x - b)$ and make a conjecture about how changes in the values of $a$ and $b$ would affect the graph. Test your conjecture by graphing the bipartite cubic for various values of $a$ and $b$.

27. Based on your knowledge of the graphs of $y = x$ and $y = \sin x$, make a sketch of the graph of $y = x\sin x$. Check your conclusion using a graphing utility.
28. What do you think the graph of $y = \sin(1/x)$ looks like? Test your conclusion using a graphing utility. [Suggestion: Examine the graph on a succession of smaller and smaller intervals centered at $x = 0$.]

29–30 Graph the equation using a graphing utility.
29. (a) $x = y^2 + 2y + 1$  
    (b) $x = \sin y, \; -2\pi \le y \le 2\pi$
30. (a) $x = y + 2y^3 - y^5$  
    (b) $x = \tan y, \; -\pi/2 < y < \pi/2$

31–34 Use a graphing utility and parametric equations to display the graphs of $f$ and $f^{-1}$ on the same screen.
31. $f(x) = x^3 + 0.2x - 1, \quad -1 \le x \le 2$
32. $f(x) = \sqrt{x^2 + 2} + x, \quad -5 \le x \le 5$
33. $f(x) = \cos(\cos 0.5x), \quad 0 \le x \le 3$
34. $f(x) = x + \sin x, \quad 0 \le x \le 6$

35. (a) Find parametric equations for the ellipse that is centered at the origin and has intercepts $(4, 0)$, $(-4, 0)$, $(0, 3)$, and $(0, -3)$.  
    (b) Find parametric equations for the ellipse that results by translating the ellipse in part (a) so that its center is at $(-1, 2)$.  
    (c) Confirm your results in parts (a) and (b) using a graphing utility.

---

## APPENDIX B: TRIGONOMETRY REVIEW

### ANGLES

Angles in the plane can be generated by rotating a ray about its endpoint. The starting position of the ray is called the **initial side** of the angle, the final position is called the **terminal side** of the angle, and the point at which the initial and terminal sides meet is called the **vertex** of the angle. We allow for the possibility that the ray may make more than one complete revolution. Angles are considered to be **positive** if generated counterclockwise and **negative** if generated clockwise (Figure B.1).

There are two standard measurement systems for describing the size of an angle: **degree measure** and **radian measure**. In degree measure, one degree (written $1^\circ$) is the measure of an angle generated by $1/360$ of one revolution. Thus, there are $360^\circ$ in an angle of one revolution, $180^\circ$ in an angle of one-half revolution, $90^\circ$ in an angle of one-quarter revolution (a right angle), and so forth. Degrees are divided into sixty equal parts, called minutes, and minutes are divided into sixty equal parts, called seconds. Thus, one minute (written $1'$) is $1/60$ of a degree, and one second (written $1''$) is $1/60$ of a minute. Smaller subdivisions of a degree are expressed as fractions of a second.

In radian measure, angles are measured by the length of the arc that the angle subtends on a circle of radius 1 when the vertex is at the center. One unit of arc on a circle of radius 1 is called **one radian** (written $1\text{ radian}$ or $1\text{ rad}$) (Figure B.2), and hence the entire circumference of a circle of radius 1 is $2\pi\text{ radians}$. It follows that an angle of $360^\circ$ subtends an arc of $2\pi\text{ radians}$, an angle of $180^\circ$ subtends an arc of $\pi\text{ radians}$, an angle of $90^\circ$ subtends an arc of $\pi/2\text{ radians}$, and so forth. Figure B.3 and Table B.1 show the relationship between degree measure and radian measure for some important positive angles.

#### Table B.1: Degree and Radian Measure
| Degrees | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $120^\circ$ | $135^\circ$ | $150^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Radians** | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\frac{2\pi}{3}$ | $\frac{3\pi}{4}$ | $\frac{5\pi}{6}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |

From the fact that $\pi\text{ radians}$ corresponds to $180^\circ$, we obtain the following formulas:
$$1^\circ = \frac{\pi}{180}\text{ rad} \approx 0.01745\text{ rad} \tag{1}$$
$$1\text{ rad} = \left(\frac{180}{\pi}\right)^\circ \approx 57^\circ 17' 44.8'' \tag{2}$$

#### Example 1
(a) Express $146^\circ$ in radians:
$$146^\circ = \left(\frac{\pi}{180}\cdot 146\right)\text{ rad} = \frac{73\pi}{90}\text{ rad} \approx 2.5482\text{ rad}$$
(b) Express $3\text{ radians}$ in degrees:
$$3\text{ rad} = \left(3\cdot \frac{180}{\pi}\right)^\circ = \left(\frac{540}{\pi}\right)^\circ \approx 171.9^\circ$$

---

### RELATIONSHIPS BETWEEN ARC LENGTH, ANGLE, RADIUS, AND AREA

For two concentric circles, the ratio of the arc lengths subtended by a central angle is equal to the ratio of the corresponding radii: $\frac{s_1}{s_2} = \frac{r_1}{r_2}$ (Figure B.4). In particular, if $s$ is the arc length subtended on a circle of radius $r$ by a central angle of $\theta\text{ radians}$, then by comparison with the arc length subtended on a circle of radius 1:
$$\frac{s}{\theta} = \frac{r}{1} \implies \theta = \frac{s}{r} \quad \text{and} \quad s = r\theta \tag{3–4}$$

The area $A$ of a circular sector of radius $r$ and central angle $\theta\text{ radians}$ satisfies $\frac{A}{\pi r^2} = \frac{\theta}{2\pi}$, yielding:
$$A = \frac{1}{2}r^2\theta \tag{5}$$

---

### TRIGONOMETRIC FUNCTIONS FOR RIGHT TRIANGLES

For a positive acute angle $\theta$ in a right triangle with adjacent side $x$, opposite side $y$, and hypotenuse $r = \sqrt{x^2 + y^2}$:
$$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}} = \frac{y}{r}, \quad \csc\theta = \frac{\text{hypotenuse}}{\text{opposite}} = \frac{r}{y}$$
$$\cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{x}{r}, \quad \sec\theta = \frac{\text{hypotenuse}}{\text{adjacent}} = \frac{r}{x} \tag{6}$$
$$\tan\theta = \frac{\text{opposite}}{\text{adjacent}} = \frac{y}{x}, \quad \cot\theta = \frac{\text{adjacent}}{\text{opposite}} = \frac{x}{y}$$

#### Table B.2: Values for $45^\circ$, $30^\circ$, and $60^\circ$
* $\sin 45^\circ = 1/\sqrt{2}, \quad \cos 45^\circ = 1/\sqrt{2}, \quad \tan 45^\circ = 1, \quad \csc 45^\circ = \sqrt{2}, \quad \sec 45^\circ = \sqrt{2}, \quad \cot 45^\circ = 1$
* $\sin 30^\circ = 1/2, \quad \cos 30^\circ = \sqrt{3}/2, \quad \tan 30^\circ = 1/\sqrt{3}, \quad \csc 30^\circ = 2, \quad \sec 30^\circ = 2/\sqrt{3}, \quad \cot 30^\circ = \sqrt{3}$
* $\sin 60^\circ = \sqrt{3}/2, \quad \cos 60^\circ = 1/2, \quad \tan 60^\circ = \sqrt{3}, \quad \csc 60^\circ = 2/\sqrt{3}, \quad \sec 60^\circ = 2, \quad \cot 60^\circ = 1/\sqrt{3}$

---

### ANGLES IN RECTANGULAR COORDINATE SYSTEMS

An angle is in **standard position** in an $xy$-coordinate system if its vertex is at the origin and its initial side is on the positive $x$-axis. Construct a circle of radius $r$ centered at the origin, and let $P(x, y)$ be the intersection of the terminal side of $\theta$ with this circle.

> **B.1 DEFINITION**  
> $$\sin\theta = \frac{y}{r}, \quad \cos\theta = \frac{x}{r}, \quad \tan\theta = \frac{y}{x}$$
> $$\csc\theta = \frac{r}{y}, \quad \sec\theta = \frac{r}{x}, \quad \cot\theta = \frac{x}{y}$$

When $r = 1$ (unit circle), the point is $(x, y) = (\cos\theta, \sin\theta)$, giving:
$$\tan\theta = \frac{\sin\theta}{\cos\theta}, \quad \cot\theta = \frac{\cos\theta}{\sin\theta} = \frac{1}{\tan\theta}, \quad \sec\theta = \frac{1}{\cos\theta}, \quad \csc\theta = \frac{1}{\sin\theta} \tag{7–10}$$

#### Table B.3: Values of Trigonometric Functions for Common Angles
| $\theta$ | $0$ ($0^\circ$) | $\pi/6$ ($30^\circ$) | $\pi/4$ ($45^\circ$) | $\pi/3$ ($60^\circ$) | $\pi/2$ ($90^\circ$) | $2\pi/3$ ($120^\circ$) | $3\pi/4$ ($135^\circ$) | $5\pi/6$ ($150^\circ$) | $\pi$ ($180^\circ$) | $3\pi/2$ ($270^\circ$) | $2\pi$ ($360^\circ$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$\sin\theta$** | $0$ | $1/2$ | $1/\sqrt{2}$ | $\sqrt{3}/2$ | $1$ | $\sqrt{3}/2$ | $1/\sqrt{2}$ | $1/2$ | $0$ | $-1$ | $0$ |
| **$\cos\theta$** | $1$ | $\sqrt{3}/2$ | $1/\sqrt{2}$ | $1/2$ | $0$ | $-1/2$ | $-1/\sqrt{2}$ | $-\sqrt{3}/2$ | $-1$ | $0$ | $1$ |
| **$\tan\theta$** | $0$ | $1/\sqrt{3}$ | $1$ | $\sqrt{3}$ | — | $-\sqrt{3}$ | $-1$ | $-1/\sqrt{3}$ | $0$ | — | $0$ |
| **$\csc\theta$** | — | $2$ | $\sqrt{2}$ | $2/\sqrt{3}$ | $1$ | $2/\sqrt{3}$ | $\sqrt{2}$ | $2$ | — | $-1$ | — |
| **$\sec\theta$** | $1$ | $2/\sqrt{3}$ | $\sqrt{2}$ | $2$ | — | $-2$ | $-\sqrt{2}$ | $-2/\sqrt{3}$ | $-1$ | — | $1$ |
| **$\cot\theta$** | — | $\sqrt{3}$ | $1$ | $1/\sqrt{3}$ | $0$ | $-1/\sqrt{3}$ | $-1$ | $-\sqrt{3}$ | — | $0$ | — |

---

### TRIGONOMETRIC IDENTITIES

* **Pythagorean Identities:**
  $$\sin^2\theta + \cos^2\theta = 1 \tag{11}$$
  $$\tan^2\theta + 1 = \sec^2\theta \tag{12}$$
  $$1 + \cot^2\theta = \csc^2\theta \tag{13}$$

* **Symmetry & Periodicity Identities:**
  $$\sin(\pi - \theta) = \sin\theta, \quad \sin(\pi + \theta) = -\sin\theta, \quad \sin(-\theta) = -\sin\theta \tag{14–16}$$
  $$\cos(\pi - \theta) = -\cos\theta, \quad \cos(\pi + \theta) = -\cos\theta, \quad \cos(-\theta) = \cos\theta \tag{17–19}$$
  $$\tan(\pi - \theta) = -\tan\theta, \quad \tan(\pi + \theta) = \tan\theta, \quad \tan(-\theta) = -\tan\theta \tag{20–22}$$
  $$\sin(\theta \pm 2n\pi) = \sin\theta, \quad \cos(\theta \pm 2n\pi) = \cos\theta \quad (n = 0, 1, 2, \dots) \tag{25–26}$$
  $$\tan(\theta \pm n\pi) = \tan\theta \quad (n = 0, 1, 2, \dots) \tag{29}$$
  $$\sin\left(\frac{\pi}{2} - \theta\right) = \cos\theta, \quad \cos\left(\frac{\pi}{2} - \theta\right) = \sin\theta, \quad \tan\left(\frac{\pi}{2} - \theta\right) = \cot\theta \tag{30–32}$$

> **B.2 THEOREM (Law of Cosines)**  
> If the sides of a triangle have lengths $a$, $b$, and $c$, and if $\theta$ is the angle between the sides with lengths $a$ and $b$, then
> $$c^2 = a^2 + b^2 - 2ab\cos\theta$$

* **Addition and Subtraction Formulas:**
  $$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta \tag{34, 36}$$
  $$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta \tag{35, 37}$$
  $$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta} \tag{38–39}$$

* **Double-Angle and Half-Angle Formulas:**
  $$\sin 2\alpha = 2\sin\alpha\cos\alpha \tag{40}$$
  $$\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha \tag{41, 43, 44}$$
  $$\tan 2\alpha = \frac{2\tan\alpha}{1 - \tan^2\alpha} \tag{42}$$
  $$\cos^2\left(\frac{\alpha}{2}\right) = \frac{1 + \cos\alpha}{2}, \quad \sin^2\left(\frac{\alpha}{2}\right) = \frac{1 - \cos\alpha}{2} \tag{45–46}$$

* **Product-to-Sum and Sum-to-Product Formulas:**
  $$\sin\alpha\cos\beta = \frac{1}{2}[\sin(\alpha - \beta) + \sin(\alpha + \beta)] \tag{47}$$
  $$\sin\alpha\sin\beta = \frac{1}{2}[\cos(\alpha - \beta) - \cos(\alpha + \beta)] \tag{48}$$
  $$\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha - \beta) + \cos(\alpha + \beta)] \tag{49}$$
  $$\sin\alpha + \sin\beta = 2\sin\left(\frac{\alpha+\beta}{2}\right)\cos\left(\frac{\alpha-\beta}{2}\right) \tag{50}$$
  $$\sin\alpha - \sin\beta = 2\cos\left(\frac{\alpha+\beta}{2}\right)\sin\left(\frac{\alpha-\beta}{2}\right) \tag{51}$$
  $$\cos\alpha + \cos\beta = 2\cos\left(\frac{\alpha+\beta}{2}\right)\cos\left(\frac{\alpha-\beta}{2}\right) \tag{52}$$
  $$\cos\alpha - \cos\beta = -2\sin\left(\frac{\alpha+\beta}{2}\right)\sin\left(\frac{\alpha-\beta}{2}\right) \tag{53}$$

* **Angle of Inclination:**
  The slope of a nonvertical line $L$ with angle of inclination $\phi$ ($0^\circ \le \phi < 180^\circ$ or $0 \le \phi < \pi$) is:
  $$m = \tan\phi \tag{54}$$

---

### EXERCISE SET B

1–2 Express the angles in radians.  
1. (a) $75^\circ$ (b) $390^\circ$ (c) $20^\circ$ (d) $138^\circ$  
2. (a) $420^\circ$ (b) $15^\circ$ (c) $225^\circ$ (d) $165^\circ$

3–4 Express the angles in degrees.  
3. (a) $\pi/15$ (b) $1.5$ (c) $8\pi/5$ (d) $3\pi$  
4. (a) $\pi/10$ (b) $2$ (c) $2\pi/5$ (d) $7\pi/6$

5–6 Find the exact values of all six trigonometric functions of $\theta$.  
5. (a) Right triangle with hypotenuse 5, adjacent 2. (b) Right triangle with adjacent 4, opposite 3. (c) Right triangle with adjacent 1, opposite 3.  
6. (a) Right triangle with adjacent 2, opposite 1. (b) Right triangle with hypotenuse 4, adjacent 3. (c) Right triangle with hypotenuse 4, adjacent 1.

7–12 The angle $\theta$ is an acute angle of a right triangle. Solve by drawing an appropriate right triangle (no calculator).  
7. Find $\sin\theta$ and $\cos\theta$ given $\tan\theta = 3$.  
8. Find $\sin\theta$ and $\tan\theta$ given $\cos\theta = 2/3$.  
9. Find $\tan\theta$ and $\csc\theta$ given $\sec\theta = 5/2$.  
10. Find $\cot\theta$ and $\sec\theta$ given $\csc\theta = 4$.  
11. Find the length of the side adjacent to $\theta$ given that the hypotenuse has length 6 and $\cos\theta = 0.3$.  
12. Find the length of the hypotenuse given that the side opposite $\theta$ has length 2.4 and $\sin\theta = 0.8$.

13–14 Find values of all six trigonometric functions of $\theta$ without a calculator.  
13. (a) $225^\circ$ (b) $-210^\circ$ (c) $5\pi/3$ (d) $-3\pi/2$  
14. (a) $330^\circ$ (b) $-120^\circ$ (c) $9\pi/4$ (d) $-3\pi$

15–16 Find exact values of the remaining five trigonometric functions of $\theta$.  
15. (a) $\cos\theta = 3/5, \; 0 < \theta < \pi/2$ (b) $\cos\theta = 3/5, \; -\pi/2 < \theta < 0$ (c) $\tan\theta = -1/\sqrt{3}, \; \pi/2 < \theta < \pi$ (d) $\tan\theta = -1/\sqrt{3}, \; -\pi/2 < \theta < 0$ (e) $\csc\theta = \sqrt{2}, \; 0 < \theta < \pi/2$ (f) $\csc\theta = \sqrt{2}, \; \pi/2 < \theta < \pi$  
16. (a) $\sin\theta = 1/4, \; 0 < \theta < \pi/2$ (b) $\sin\theta = 1/4, \; \pi/2 < \theta < \pi$ (c) $\cot\theta = 1/3, \; 0 < \theta < \pi/2$ (d) $\cot\theta = 1/3, \; \pi < \theta < 3\pi/2$ (e) $\sec\theta = -5/2, \; \pi/2 < \theta < \pi$ (f) $\sec\theta = -5/2, \; \pi < \theta < 3\pi/2$

17–18 Use a calculating utility to find $x$ to four decimal places.  
17. (a) Right triangle: opposite 3, angle $25^\circ$, find hypotenuse $x$. (b) Right triangle: opposite 3, angle $2\pi/9$, find hypotenuse $x$.  
18. (a) Right triangle: adjacent 2, angle $20^\circ$, find hypotenuse $x$. (b) Right triangle: adjacent 3, angle $3\pi/11$, find hypotenuse $x$.

19. In each part, let $\theta$ be an acute angle of a right triangle. Express the remaining five trigonometric functions in terms of $a$.  
    (a) $\sin\theta = a/3$ (b) $\tan\theta = a/5$ (c) $\sec\theta = a$

20–27 Find all values of $\theta$ (in radians) that satisfy the equation (no calculator).  
20. (a) $\cos\theta = -1/\sqrt{2}$ (b) $\sin\theta = -1/\sqrt{2}$  
21. (a) $\tan\theta = -1$ (b) $\cos\theta = 1/2$  
22. (a) $\sin\theta = -1/2$ (b) $\tan\theta = \sqrt{3}$  
23. (a) $\tan\theta = 1/\sqrt{3}$ (b) $\sin\theta = -\sqrt{3}/2$  
24. (a) $\sin\theta = -1$ (b) $\cos\theta = -1$  
25. (a) $\cot\theta = -1$ (b) $\cot\theta = \sqrt{3}$  
26. (a) $\sec\theta = -2$ (b) $\csc\theta = -2$  
27. (a) $\csc\theta = 2/\sqrt{3}$ (b) $\sec\theta = 2/\sqrt{3}$

28–29 Find the values of all six trigonometric functions of $\theta$.  
28. Point $(-4, -3)$ on the terminal side of $\theta$.  
29. Point $(-2\sqrt{21}, 4)$ on the terminal side of $\theta$.

30. Find all values of $\theta$ (in radians) such that: (a) $\sin\theta = 1$ (b) $\cos\theta = 1$ (c) $\tan\theta = 1$ (d) $\csc\theta = 1$ (e) $\sec\theta = 1$ (f) $\cot\theta = 1$.  
31. Find all values of $\theta$ (in radians) such that: (a) $\sin\theta = 0$ (b) $\cos\theta = 0$ (c) $\tan\theta = 0$ (d) $\csc\theta$ is undefined (e) $\sec\theta$ is undefined (f) $\cot\theta$ is undefined.  
32. How could you use a ruler and protractor to approximate $\sin 17^\circ$ and $\cos 17^\circ$?  
33. Find the length of the circular arc on a circle of radius 4 cm subtended by an angle of (a) $\pi/6$ (b) $150^\circ$.  
34. Find the radius of a circular sector that has an angle of $\pi/3$ and a circular arc length of 7 units.  
35. A point $P$ moving counterclockwise on a circle of radius 5 cm traverses an arc length of 2 cm. What is the angle swept out by a radius from the center to $P$?  
36. Find a formula for the area $A$ of a circular sector in terms of its radius $r$ and arc length $s$.  
37. A right circular cone is made from a circular piece of paper of radius $R$ by cutting out a sector of angle $\theta$ radians and gluing the cut edges together. Find (a) the radius $r$ of the base in terms of $R$ and $\theta$ (b) the height $h$ in terms of $R$ and $\theta$.  
38. Show that the lateral surface area of a right circular cone of base radius $r$ and slant height $L$ is $S = \pi rL$.  
39. Two sides of a triangle have lengths 3 cm and 7 cm and meet at an angle of $60^\circ$. Find the area of the triangle.  
40. Let $ABC$ be a triangle with angles $A = 30^\circ$ and $B = 45^\circ$. If the side opposite $B$ has length 9, find the remaining sides and angle $C$.  
41. A 10-foot ladder leans against a house and makes an angle of $67^\circ$ with level ground. How far is the top of the ladder above ground?  
42. From 120 ft on level ground from a building, angle of elevation to top is $76^\circ$. Find building height.  
43. Window elevation angles on 2nd and 3rd floors are $\alpha$ and $\beta$ from distance $d$. Find distance $h$ between window bottoms.  
44. Elevation angle to top of tower is $\alpha$; from $d$ units closer it is $\beta$. Find height $h$ of tower.  
45. If $\cos\theta = 2/3$ and $0 < \theta < \pi/2$, find (a) $\sin 2\theta$ (b) $\cos 2\theta$.  
46. If $\tan\alpha = 3/4$ and $\tan\beta = 2$, where $0 < \alpha < \pi/2$ and $0 < \beta < \pi/2$, find (a) $\sin(\alpha - \beta)$ (b) $\cos(\alpha + \beta)$.  
47. Express $\sin 3\theta$ and $\cos 3\theta$ in terms of $\sin\theta$ and $\cos\theta$.  
48–58 Derive the given trigonometric identities.  
59. Prove: $\text{Area} = \frac{1}{2}bc\sin A$.  
60. Prove the law of sines: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$.  
61. Express cofunctions in terms of $\sin\theta$ or $\cos\theta$.  
62–65 Derive addition, product-to-sum, and sum-to-product identities.  
66. (a) Express $3\sin\alpha + 5\cos\alpha$ as $C\sin(\alpha + \phi)$. (b) General form $A\sin\alpha + B\cos\alpha = C\sin(\alpha + \phi)$.  
67. Show diagonal of parallelogram is $d = \sqrt{a^2 + b^2 + 2ab\cos\theta}$.  
68–69 Find angle of inclination of line with slope $m$.  
70–71 Find angle of inclination of given line equations.

---

## APPENDIX C: SOLVING POLYNOMIAL EQUATIONS

### A BRIEF REVIEW OF POLYNOMIALS

If $n$ is a nonnegative integer, a polynomial of degree $n$ is:
$$p(x) = c_n x^n + c_{n-1} x^{n-1} + \dots + c_1 x + c_0 \quad (c_n \neq 0)$$
The numbers $c_0, c_1, \dots, c_n$ are the **coefficients**; $c_n$ is the **leading coefficient**, $c_n x^n$ is the **leading term**, and $c_0$ is the **constant term**. Polynomials of degree 1, 2, 3, 4, and 5 are called *linear, quadratic, cubic, quartic,* and *quintic*, respectively.

> **C.1 THEOREM**  
> If complex roots are allowed, and if roots are counted according to their multiplicities, then a polynomial of degree $n$ has exactly $n$ roots.

---

### THE REMAINDER THEOREM AND FACTOR THEOREM

> **C.2 THEOREM (Division Algorithm)**  
> If $p(x)$ and $s(x)$ are polynomials, and $s(x) \neq 0$, then $p(x) = s(x)q(x) + r(x)$, where $q(x)$ is the quotient and $r(x)$ is the remainder ($r(x) = 0$ or $\deg(r) < \deg(s)$).

> **C.3 THEOREM (Remainder Theorem)**  
> If a polynomial $p(x)$ is divided by $x - c$, then the remainder is $p(c)$.

> **C.4 THEOREM (Factor Theorem)**  
> A polynomial $p(x)$ has a factor $x - c$ if and only if $p(c) = 0$.

#### Equivalent Statements:
* $x - c$ is a factor of $p(x)$.
* $p(c) = 0$.
* $c$ is a zero of $p(x)$.
* $c$ is a root of the equation $p(x) = 0$.
* $c$ is a solution of the equation $p(x) = 0$.
* $c$ is an $x$-intercept of $y = p(x)$.

#### Example 1
By Remainder Theorem, dividing $p(x) = 2x^3 + 3x^2 - 4x - 3$ by $x + 4$ gives $p(-4) = 2(-4)^3 + 3(-4)^2 - 4(-4) - 3 = -67$.

#### Example 2 & 3
Confirm $x - 1$ is a factor of $p(x) = x^3 - 3x^2 - 13x + 15$. Factoring quotient yields $p(x) = (x - 1)(x - 5)(x + 3)$.

---

### METHODS FOR FINDING ROOTS

> **C.5 THEOREM (Rational Root Theorem)**  
> Suppose $p(x) = c_n x^n + \dots + c_0$ is a polynomial with integer coefficients:  
> (a) If $r$ is an integer zero of $p(x)$, then $r$ must be a divisor of the constant term $c_0$.  
> (b) If $r = a/b$ is a rational zero of $p(x)$ in lowest terms, then $a$ must divide $c_0$, and $b$ must divide the leading coefficient $c_n$.

#### Example 4
Solve $x^3 + 3x^2 - 7x - 21 = 0 \implies (x + 3)(x^2 - 7) = 0 \implies x = -3, \; x = \pm\sqrt{7} \approx \pm 2.65$.

---

### EXERCISE SET C

1–2 Find quotient $q(x)$ and remainder $r(x)$ for polynomial divisions.  
3–4 Use synthetic division to find quotient $q(x)$ and remainder $r(x)$.  
5–6 Synthetic division and Remainder Theorem evaluations.  
7–8 Express $p(x) = (x - c)q(x) + r$.  
9. Candidates for rational zeros.  
10. Find all integer zeros of degree 6 polynomial.  
11–15 Factor polynomials completely into linear/irreducible factors.  
16. CAS check for factorizations.  
17–21 Find all real solutions of polynomial equations.  
22. CAS verification of solutions.  
23. Find $k$ such that $x - 1$ is a factor of $p(x) = k^2 x^3 - 7kx + 10$.  
24. Factor check for $x^7 + 2187$.  
25. Volume of sliced cube application ($196\text{ cm}^3 \implies \text{side} = 7\text{ cm}$).  
26. Rational and real numbers exceeding their cubes by 1.  
27. Factor Theorem proofs for $x^n - y^n$ and $x^n + y^n$.

---

## APPENDIX D: SELECTED PROOFS

### PROOFS OF BASIC LIMIT THEOREMS

> **D.1 THEOREM (Limit Laws)**  
> Let $a$ be any real number, $k$ a constant, and $\lim_{x \to a} f(x) = L_1, \; \lim_{x \to a} g(x) = L_2$:  
> (a) $\lim_{x \to a} k = k$  
> (b) $\lim_{x \to a} [f(x) + g(x)] = L_1 + L_2$  
> (c) $\lim_{x \to a} [f(x)g(x)] = L_1 L_2$

*Proof (a):* Given $\epsilon > 0$, $|k - k| = 0 < \epsilon$ holds for all $0 < |x - a| < \delta$ for any $\delta > 0$.  
*Proof (b):* Choose $\delta_1, \delta_2$ such that $|f(x) - L_1| < \epsilon/2$ and $|g(x) - L_2| < \epsilon/2$. For $\delta = \min(\delta_1, \delta_2)$, $|(f(x) + g(x)) - (L_1 + L_2)| \le |f(x) - L_1| + |g(x) - L_2| < \epsilon$.  
*Proof (c):* Uses rewritten product $|L_1(g(x) - L_2) + L_2(f(x) - L_1) + (f(x) - L_1)(g(x) - L_2)| < \epsilon$ and four delta bounds bounded by $\delta = \min(\delta_1, \delta_2, \delta_3, \delta_4)$.

---

### PROOF OF A BASIC CONTINUITY PROPERTY

> **D.2 THEOREM (Theorem 1.5.5)**  
> If $\lim_{x \to c} g(x) = L$ and $f$ is continuous at $L$, then $\lim_{x \to c} f(g(x)) = f(L)$. That is, $\lim_{x \to c} f(g(x)) = f(\lim_{x \to c} g(x))$.

*Proof:* Continuity of $f$ at $L$ provides $\delta_1 > 0$ such that $|f(u) - f(L)| < \epsilon$ when $|u - L| < \delta_1$. Limit of $g$ provides $\delta > 0$ such that $|g(x) - L| < \delta_1$ when $0 < |x - c| < \delta$. Substituting $u = g(x)$ completes the proof.

---

### PROOF OF THE CHAIN RULE

> **D.3 THEOREM**  
> If $f$ is differentiable at $x$ and $y = f(x)$, then $\Delta y = f'(x)\Delta x + \epsilon\Delta x$, where $\epsilon \to 0$ as $\Delta x \to 0$ and $\epsilon = 0$ if $\Delta x = 0$.

> **D.4 THEOREM (The Chain Rule - Theorem 2.6.1)**  
> If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then the composition $f \circ g$ is differentiable at $x$, and $\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx}$.

*Proof:* From Theorem D.3, $\Delta u = g'(x)\Delta x + \epsilon_1\Delta x$ and $\Delta y = f'(u)\Delta u + \epsilon_2\Delta u$. Substituting and dividing by $\Delta x \neq 0$ yields $\frac{\Delta y}{\Delta x} = [f'(u) + \epsilon_2][g'(x) + \epsilon_1]$. Taking $\Delta x \to 0$ gives $\frac{dy}{dx} = f'(u)g'(x) = \frac{dy}{du}\frac{du}{dx}$.

---

### PROOF THAT RELATIVE EXTREMA OCCUR AT CRITICAL POINTS

> **D.5 THEOREM (Theorem 4.2.2)**  
> Suppose $f$ is defined on an open interval containing $x_0$. If $f$ has a relative extremum at $x = x_0$, then $x = x_0$ is a critical point of $f$ ($f'(x_0) = 0$ or $f$ is not differentiable at $x_0$).

*Proof:* For relative maximum at $x_0$, difference quotient $\frac{f(x_0 + h) - f(x_0)}{h} \ge 0$ for $h < 0$, giving $f'(x_0) \ge 0$, and $\le 0$ for $h > 0$, giving $f'(x_0) \le 0$. Thus $f'(x_0) = 0$.

---

### PROOFS OF TWO SUMMATION FORMULAS

> **D.6 THEOREM (Theorem 5.4.2)**  
> (a) $\sum_{k=1}^n k = \frac{n(n+1)}{2}$  
> (b) $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$  
> (c) $\sum_{k=1}^n k^3 = \left[\frac{n(n+1)}{2}\right]^2$

*Proof (a):* Adding sum forwards and backwards gives $2\sum_{k=1}^n k = n(n+1)$.  
*Proof (b):* Telescoping identity $\sum_{k=1}^n [(k+1)^3 - k^3] = (n+1)^3 - 1 = 3\sum k^2 + 3\sum k + n$. Solving for $\sum k^2$ yields $\frac{n(n+1)(2n+1)}{6}$.

---

### PROOF OF THE LIMIT COMPARISON TEST

> **D.7 THEOREM (Theorem 9.5.4)**  
> Let $\sum a_k$ and $\sum b_k$ be series with positive terms and $\rho = \lim_{k \to +\infty} \frac{a_k}{b_k}$. If $\rho$ is finite and $\rho > 0$, then both series converge or both diverge.

*Proof:* Choosing $\epsilon = \rho/2$ yields index $K$ such that $\frac{1}{2}\rho b_k < a_k < \frac{3}{2}\rho b_k$ for $k \ge K$. Applying direct comparison proves mutual convergence or divergence.

---

### PROOF OF THE RATIO TEST

> **D.8 THEOREM (Theorem 9.5.5)**  
> Let $\sum u_k$ be a series with positive terms and $\rho = \lim_{k \to +\infty} \frac{u_{k+1}}{u_k}$.  
> (a) If $\rho < 1$, converges. (b) If $\rho > 1$ or $\rho = +\infty$, diverges. (c) If $\rho = 1$, inconclusive.

*Proof (a):* Choose $r$ with $\rho < r < 1$. For $k \ge K$, $u_{k+1} < r u_k$, dominating the series by a convergent geometric series $\sum r^k u_K$.  
*Proof (b):* For $k \ge K$, $u_{k+1} > u_k > 0$, so $\lim u_k \neq 0$, and the series diverges by the divergence test.

---

### PROOF OF THE REMAINDER ESTIMATION THEOREM

> **D.9 THEOREM (Theorem 9.7.4)**  
> If $f$ can be differentiated $n + 1$ times on an interval containing $x_0$ and $|f^{(n+1)}(x)| \le M$, then $|R_n(x)| \le \frac{M}{(n+1)!}|x - x_0|^{n+1}$.

*Proof:* Successively integrate $-M \le R_n^{(n+1)}(t) \le M$ from $x_0$ to $x$ using $R_n^{(k)}(x_0) = 0$ for $k = 0, 1, \dots, n$ total $n + 1$ times.

---

### PROOF OF THE EQUALITY OF MIXED PARTIALS

> **D.10 THEOREM (Theorem 13.3.2)**  
> If $f_{xy}$ and $f_{yx}$ are continuous on an open disk, then $f_{xy} = f_{yx}$ on that disk.

*Proof:* Let $w(\Delta x, \Delta y) = f(x+\Delta x, y+\Delta y) - f(x+\Delta x, y) - f(x, y+\Delta y) + f(x, y)$. Applying the Mean-Value Theorem twice gives $w(\Delta x, \Delta y) = f_{xy}(c, d)\Delta x\Delta y$ and symmetrically $f_{yx}(\bar{c}, \bar{d})\Delta x\Delta y$. Taking limits as $(\Delta x, \Delta y) \to (0, 0)$ establishes $f_{xy}(x, y) = f_{yx}(x, y)$.

---

### PROOF OF THE TWO-VARIABLE CHAIN RULE FOR DERIVATIVES

> **D.11 THEOREM (Theorem 13.5.1)**  
> If $x = x(t)$ and $y = y(t)$ are differentiable at $t$, and $z = f(x, y)$ is differentiable at $(x(t), y(t))$, then $z = f(x(t), y(t))$ is differentiable at $t$ and
> $$\frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}$$

*Proof:* By differentiability of $f$, $\Delta z = \frac{\partial z}{\partial x}\Delta x + \frac{\partial z}{\partial y}\Delta y + \epsilon(\Delta x, \Delta y)\sqrt{(\Delta x)^2 + (\Delta y)^2}$. Dividing by $\Delta t$ and evaluating $\lim_{\Delta t \to 0} \frac{\epsilon\sqrt{(\Delta x)^2 + (\Delta y)^2}}{\Delta t} = 0 \cdot \sqrt{(dx/dt)^2 + (dy/dt)^2} = 0$ yields the chain rule equation.
