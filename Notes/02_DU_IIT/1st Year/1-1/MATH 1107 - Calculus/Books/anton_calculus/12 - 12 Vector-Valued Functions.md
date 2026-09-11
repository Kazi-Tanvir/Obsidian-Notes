# CHAPTER 12: VECTOR-VALUED FUNCTIONS

> The design of a roller coaster requires an understanding of the mathematical principles governing the motion of objects that move with varying speed and direction.

In this chapter we will consider functions whose values are vectors. Such functions provide a unified way of studying parametric curves in 2-space and 3-space and are a basic tool for analyzing the motion of particles along curved paths. We will begin by developing the calculus of vector-valued functions—we will show how to differentiate and integrate such functions, and we will develop some of the basic properties of these operations. We will then apply these calculus tools to define three fundamental vectors that can be used to describe such basic characteristics of curves as curvature and twisting tendencies. Once this is done, we will develop the concepts of velocity and acceleration for such motion, and we will apply these concepts to explain various physical phenomena. Finally, we will use the calculus of vector-valued functions to develop basic principles of gravitational attraction and to derive Kepler’s laws of planetary motion.

---

## 12.1 INTRODUCTION TO VECTOR-VALUED FUNCTIONS

In Section 11.5 we discussed parametric equations of lines in 3-space. In this section we will discuss more general parametric curves in 3-space, and we will show how vector notation can be used to express parametric equations in 2-space and 3-space in a more compact form. This will lead us to consider a new kind of function—namely, functions that associate vectors with real numbers. Such functions have many important applications in physics and engineering.

### PARAMETRIC CURVES IN 3-SPACE

Recall from Section 10.1 that if $f$ and $g$ are well-behaved functions, then the pair of parametric equations
$$x = f(t), \quad y = g(t) \tag{1}$$
generates a curve in 2-space that is traced in a specific direction as the parameter $t$ increases. We defined this direction to be the **orientation** of the curve or the **direction of increasing parameter**, and we called the curve together with its orientation the **graph** of the parametric equations or the **parametric curve** represented by the equations. Analogously, if $f, g,$ and $h$ are three well-behaved functions, then the parametric equations
$$x = f(t), \quad y = g(t), \quad z = h(t) \tag{2}$$
generate a curve in 3-space that is traced in a specific direction as $t$ increases. As in 2-space, this direction is called the **orientation** or **direction of increasing parameter**, and the curve together with its orientation is called the **graph** of the parametric equations or the **parametric curve** represented by the equations. If no restrictions are stated explicitly or are implied by the equations, then it will be understood that $t$ varies over the interval $(-\infty, +\infty)$.

#### Example 1
The parametric equations
$$x = 1 - t, \quad y = 3t, \quad z = 2t$$
represent a line in 3-space that passes through the point $(1, 0, 0)$ and is parallel to the vector $\langle -1, 3, 2 \rangle$. Since $x$ decreases as $t$ increases, the line has the orientation shown in Figure 12.1.1.

#### Example 2
Describe the parametric curve represented by the equations
$$x = a\cos t, \quad y = a\sin t, \quad z = ct$$
where $a$ and $c$ are positive constants.

**Solution.** As the parameter $t$ increases, the value of $z = ct$ also increases, so the point $(x, y, z)$ moves upward. However, as $t$ increases, the point $(x, y, z)$ also moves in a path directly over the circle
$$x = a\cos t, \quad y = a\sin t$$
in the $xy$-plane. The combination of these upward and circular motions produces a corkscrew-shaped curve that wraps around a right circular cylinder of radius $a$ centered on the $z$-axis (Figure 12.1.2). This curve is called a **circular helix**.

> The circular helix described in Example 2 occurs in nature. A classic example is the twin helix DNA molecule (deoxyribonucleic acid), which contains all inherited instructions for the development of living organisms.

---

### PARAMETRIC CURVES GENERATED WITH TECHNOLOGY

Except in the simplest cases, parametric curves can be difficult to visualize and draw without the help of a graphing utility. For example, the **tricuspoid** is the graph of the parametric equations
$$x = 2\cos t + \cos 2t, \quad y = 2\sin t - \sin 2t$$
Although it would be tedious to plot the tricuspoid by hand, a computer rendering is easy to obtain and reveals the significance of the name of the curve (Figure 12.1.3). However, note that the depiction of the tricuspoid in Figure 12.1.3 is incomplete, since the orientation of the curve is not indicated. This is often the case for curves that are generated with a graphing utility. (Some graphing utilities plot parametric curves slowly enough for the orientation to be discerned, or provide a feature for tracing the points along the curve in the direction of increasing parameter.)

Parametric curves in 3-space can be difficult to visualize correctly even with the help of a graphing utility. For example, Figure 12.1.4a shows a parametric curve called a **torus knot** that was produced with a CAS. However, it is unclear from this computer-generated figure whether the points of overlap are intersections or whether one portion of the curve is in front of the other. To resolve the visualization problem, some graphing utilities provide the capability of enclosing the curve within a thin tube, as in Figure 12.1.4b. Such graphs are called **tube plots**.

**TECHNOLOGY MASTERY**  
If you have a CAS, use it to generate the tricuspoid in Figure 12.1.3, and show that this parametric curve is oriented counterclockwise.

---

### PARAMETRIC EQUATIONS FOR INTERSECTIONS OF SURFACES

Curves in 3-space often arise as intersections of surfaces. For example, Figure 12.1.5a shows a portion of the intersection of the cylinders $z = x^3$ and $y = x^2$. One method for finding parametric equations for the curve of intersection is to choose one of the variables as the parameter and use the two equations to express the remaining two variables in terms of that parameter. In particular, if we choose $x = t$ as the parameter and substitute this into the equations $z = x^3$ and $y = x^2$, we obtain the parametric equations
$$x = t, \quad y = t^2, \quad z = t^3 \tag{3}$$
This curve is called a **twisted cubic**. The portion of the twisted cubic shown in Figure 12.1.5a corresponds to $t \ge 0$; a computer-generated graph of the twisted cubic for positive and negative values of $t$ is shown in Figure 12.1.5b. Some other examples and techniques for finding intersections of surfaces are discussed in the exercises.

---

### VECTOR-VALUED FUNCTIONS

The twisted cubic defined by the equations in (3) is the set of points of the form $(t, t^2, t^3)$ for real values of $t$. If we view each of these points as a terminal point for a vector $\mathbf{r}$ whose initial point is at the origin,
$$\mathbf{r} = \langle x, y, z \rangle = \langle t, t^2, t^3 \rangle = t\mathbf{i} + t^2\mathbf{j} + t^3\mathbf{k}$$
then we obtain $\mathbf{r}$ as a function of the parameter $t$, that is, $\mathbf{r} = \mathbf{r}(t)$. Since this function produces a vector, we say that $\mathbf{r} = \mathbf{r}(t)$ defines $\mathbf{r}$ as a **vector-valued function of a real variable**, or more simply, a **vector-valued function**. The vectors that we will consider in this text are either in 2-space or 3-space, so we will say that a vector-valued function is in 2-space or in 3-space according to the kind of vectors that it produces.

Whereas a vector-valued function in 3-space, such as (4), has three components, a vector-valued function in 2-space has only two components and hence has the form
$$\mathbf{r}(t) = \langle x(t), y(t) \rangle = x(t)\mathbf{i} + y(t)\mathbf{j}$$

If $\mathbf{r}(t)$ is a vector-valued function in 3-space, then for each allowable value of $t$ the vector $\mathbf{r} = \mathbf{r}(t)$ can be represented in terms of components as
$$\mathbf{r} = \mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k} \tag{4}$$
The functions $x(t), y(t),$ and $z(t)$ are called the **component functions** or the **components** of $\mathbf{r}(t)$.

#### Example 3
The component functions of
$$\mathbf{r}(t) = \langle t, t^2, t^3 \rangle = t\mathbf{i} + t^2\mathbf{j} + t^3\mathbf{k}$$
are
$$x(t) = t, \quad y(t) = t^2, \quad z(t) = t^3$$

The **domain** of a vector-valued function $\mathbf{r}(t)$ is the set of allowable values for $t$. If $\mathbf{r}(t)$ is defined in terms of component functions and the domain is not specified explicitly, then it will be understood that the domain is the intersection of the natural domains of the component functions; this is called the **natural domain** of $\mathbf{r}(t)$.

#### Example 4
Find the natural domain of
$$\mathbf{r}(t) = \langle \ln|t - 1|, e^t, \sqrt{t} \rangle = (\ln|t - 1|)\mathbf{i} + e^t\mathbf{j} + \sqrt{t}\mathbf{k}$$

**Solution.** The natural domains of the component functions
$$x(t) = \ln|t - 1|, \quad y(t) = e^t, \quad z(t) = \sqrt{t}$$
are $(-\infty, 1) \cup (1, +\infty), \; (-\infty, +\infty),$ and $[0, +\infty)$, respectively. The intersection of these sets is
$$[0, 1) \cup (1, +\infty)$$
(verify), so the natural domain of $\mathbf{r}(t)$ consists of all values of $t$ such that
$$0 \le t < 1 \quad \text{or} \quad t > 1$$

---

### GRAPHS OF VECTOR-VALUED FUNCTIONS

If $\mathbf{r}(t)$ is a vector-valued function in 2-space or 3-space, then we define the **graph** of $\mathbf{r}(t)$ to be the parametric curve described by the component functions for $\mathbf{r}(t)$. For example, if
$$\mathbf{r}(t) = \langle 1 - t, 3t, 2t \rangle = (1 - t)\mathbf{i} + 3t\mathbf{j} + 2t\mathbf{k} \tag{5}$$
then the graph of $\mathbf{r} = \mathbf{r}(t)$ is the graph of the parametric equations
$$x = 1 - t, \quad y = 3t, \quad z = 2t$$
Thus, the graph of (5) is the line in Figure 12.1.1.

#### Example 5
Describe the graph of the vector-valued function
$$\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\mathbf{k}$$

**Solution.** The corresponding parametric equations are
$$x = \cos t, \quad y = \sin t, \quad z = t$$
Thus, as we saw in Example 2, the graph is a circular helix wrapped around a cylinder of radius 1.

> *Strictly speaking, we should write $(\cos t)\mathbf{i}$ and $(\sin t)\mathbf{j}$ rather than $\cos t\,\mathbf{i}$ and $\sin t\,\mathbf{j}$ for clarity. However, it is a common practice to omit the parentheses in such cases, since no misinterpretation is possible.*

Up to now we have considered parametric curves to be paths traced by moving points. However, if a parametric curve is viewed as the graph of a vector-valued function, then we can also imagine the graph to be traced by the tip of a moving vector. For example, if the curve $C$ in 3-space is the graph of
$$\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$$
and if we position $\mathbf{r}(t)$ so its initial point is at the origin, then its terminal point will fall on the curve $C$ (as shown in Figure 12.1.6). Thus, when $\mathbf{r}(t)$ is positioned with its initial point at the origin, its terminal point will trace out the curve $C$ as the parameter $t$ varies, in which case we call $\mathbf{r}(t)$ the **radius vector** or the **position vector** for $C$. For simplicity, we will sometimes let the dependence on $t$ be understood and write $\mathbf{r}$ rather than $\mathbf{r}(t)$ for a radius vector.

#### Example 6
Sketch the graph and a radius vector of
(a) $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j}, \quad 0 \le t \le 2\pi$  
(b) $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + 2\mathbf{k}, \quad 0 \le t \le 2\pi$

**Solution (a).** The corresponding parametric equations are
$$x = \cos t, \quad y = \sin t \quad (0 \le t \le 2\pi)$$
so the graph is a circle of radius 1, centered at the origin, and oriented counterclockwise. The graph and a radius vector are shown in Figure 12.1.7.

**Solution (b).** The corresponding parametric equations are
$$x = \cos t, \quad y = \sin t, \quad z = 2 \quad (0 \le t \le 2\pi)$$
From the third equation, the tip of the radius vector traces a curve in the plane $z = 2$, and from the first two equations, the curve is a circle of radius 1 centered at the point $(0, 0, 2)$ and traced counterclockwise looking down the $z$-axis. The graph and a radius vector are shown in Figure 12.1.8.

---

### VECTOR FORM OF A LINE SEGMENT

Recall from Formula (9) of Section 11.5 that if $\mathbf{r}_0$ is a vector in 2-space or 3-space with its initial point at the origin, then the line that passes through the terminal point of $\mathbf{r}_0$ and is parallel to the vector $\mathbf{v}$ can be expressed in vector form as
$$\mathbf{r} = \mathbf{r}_0 + t\mathbf{v}$$
In particular, if $\mathbf{r}_0$ and $\mathbf{r}_1$ are vectors in 2-space or 3-space with their initial points at the origin, then the line that passes through the terminal points of these vectors can be expressed in vector form as
$$\mathbf{r} = \mathbf{r}_0 + t(\mathbf{r}_1 - \mathbf{r}_0) \quad \text{or} \quad \mathbf{r} = (1 - t)\mathbf{r}_0 + t\mathbf{r}_1 \tag{6–7}$$
as indicated in Figure 12.1.9.

It is common to call either (6) or (7) the **two-point vector form of a line** and to say, for simplicity, that the line passes through the points $\mathbf{r}_0$ and $\mathbf{r}_1$ (as opposed to saying that it passes through the terminal points of $\mathbf{r}_0$ and $\mathbf{r}_1$).

It is understood in (6) and (7) that $t$ varies from $-\infty$ to $+\infty$. However, if we restrict $t$ to vary over the interval $0 \le t \le 1$, then $\mathbf{r}$ will vary from $\mathbf{r}_0$ to $\mathbf{r}_1$. Thus, the equation
$$\mathbf{r} = (1 - t)\mathbf{r}_0 + t\mathbf{r}_1 \quad (0 \le t \le 1) \tag{8}$$
represents the **line segment** in 2-space or 3-space that is traced from $\mathbf{r}_0$ to $\mathbf{r}_1$.

---

### QUICK CHECK EXERCISES 12.1
*(See page 847 for answers.)*

1. (a) Express the parametric equations $x = \frac{1}{t}, \; y = \sqrt{t}, \; z = \sin^{-1} t$ as a single vector equation of the form $\mathbf{r} = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$.  
   (b) The vector equation in part (a) defines $\mathbf{r} = \mathbf{r}(t)$ as a vector-valued function. The domain of $\mathbf{r}(t)$ is $\underline{\quad}$ and $\mathbf{r}\left(\frac{1}{2}\right) = \underline{\quad}$.
2. Describe the graph of $\mathbf{r}(t) = \langle 1 + 2t, -1 + 3t \rangle$.
3. Describe the graph of $\mathbf{r}(t) = \sin^2 t\,\mathbf{i} + \cos^2 t\,\mathbf{j}$.
4. Find a vector equation for the curve of intersection of the surfaces $y = x^2$ and $z = y$ in terms of the parameter $x = t$.

---

### EXERCISE SET 12.1

**1–4 Find the domain of $\mathbf{r}(t)$ and the value of $\mathbf{r}(t_0)$.**
1. $\mathbf{r}(t) = \cos t\,\mathbf{i} - 3t\mathbf{j}; \quad t_0 = \pi$
2. $\mathbf{r}(t) = \langle \sqrt{3t + 1}, t^2 \rangle; \quad t_0 = 1$
3. $\mathbf{r}(t) = \cos\pi t\,\mathbf{i} - \ln t\,\mathbf{j} + \sqrt{t - 2}\,\mathbf{k}; \quad t_0 = 3$
4. $\mathbf{r}(t) = \langle 2e^{-t}, \sin^{-1} t, \ln(1 - t) \rangle; \quad t_0 = 0$

**5–6 Express the parametric equations as a single vector equation of the form $\mathbf{r} = x(t)\mathbf{i} + y(t)\mathbf{j}$ or $\mathbf{r} = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$.**
5. $x = 3\cos t, \quad y = t + \sin t$
6. $x = 2t, \quad y = 2\sin 3t, \quad z = 5\cos 3t$

**7–8 Find the parametric equations that correspond to the given vector equation.**
7. $\mathbf{r} = 3t^2\mathbf{i} - 2\mathbf{j}$
8. $\mathbf{r} = (2t - 1)\mathbf{i} - 3\sqrt{t}\mathbf{j} + \sin 3t\,\mathbf{k}$

**9–14 Describe the graph of the equation.**
9. $\mathbf{r} = (3 - 2t)\mathbf{i} + 5t\mathbf{j}$
10. $\mathbf{r} = 2\sin 3t\,\mathbf{i} - 2\cos 3t\,\mathbf{j}$
11. $\mathbf{r} = 2t\mathbf{i} - 3\mathbf{j} + (1 + 3t)\mathbf{k}$
12. $\mathbf{r} = 3\mathbf{i} + 2\cos t\,\mathbf{j} + 2\sin t\,\mathbf{k}$
13. $\mathbf{r} = 2\cos t\,\mathbf{i} - 3\sin t\,\mathbf{j} + \mathbf{k}$
14. $\mathbf{r} = -3\mathbf{i} + (1 - t^2)\mathbf{j} + t\mathbf{k}$

**15.**  
(a) Find the slope of the line in 2-space that is represented by the vector equation $\mathbf{r} = (1 - 2t)\mathbf{i} - (2 - 3t)\mathbf{j}$.  
(b) Find the coordinates of the point where the line $\mathbf{r} = (2 + t)\mathbf{i} + (1 - 2t)\mathbf{j} + 3t\mathbf{k}$ intersects the $xz$-plane.

**16.**  
(a) Find the $y$-intercept of the line in 2-space that is represented by the vector equation $\mathbf{r} = (3 + 2t)\mathbf{i} + 5t\mathbf{j}$.  
(b) Find the coordinates of the point where the line $\mathbf{r} = t\mathbf{i} + (1 + 2t)\mathbf{j} - 3t\mathbf{k}$ intersects the plane $3x - y - z = 2$.

**17–18 Sketch the line segment represented by each vector equation.**
17. (a) $\mathbf{r} = (1 - t)\mathbf{i} + t\mathbf{j}; \quad 0 \le t \le 1$  
    (b) $\mathbf{r} = (1 - t)(\mathbf{i} + \mathbf{j}) + t(\mathbf{i} - \mathbf{j}); \quad 0 \le t \le 1$
18. (a) $\mathbf{r} = (1 - t)(\mathbf{i} + \mathbf{j}) + t\mathbf{k}; \quad 0 \le t \le 1$  
    (b) $\mathbf{r} = (1 - t)(\mathbf{i} + \mathbf{j} + \mathbf{k}) + t(\mathbf{i} + \mathbf{j}); \quad 0 \le t \le 1$

**19–20 Write a vector equation for the line segment from $P$ to $Q$.**
19. $P(0, 4), \; Q(3, 0)$
20. $P(0, 0, 4), \; Q(2, 3, 0)$

**21–30 Sketch the graph of $\mathbf{r}(t)$ and show the direction of increasing $t$.**
21. $\mathbf{r}(t) = 2\mathbf{i} + t\mathbf{j}$
22. $\mathbf{r}(t) = \langle 3t - 4, 6t + 2 \rangle$
23. $\mathbf{r}(t) = (1 + \cos t)\mathbf{i} + (3 - \sin t)\mathbf{j}; \quad 0 \le t \le 2\pi$
24. $\mathbf{r}(t) = \langle 2\cos t, 5\sin t \rangle; \quad 0 \le t \le 2\pi$
25. $\mathbf{r}(t) = \cosh t\,\mathbf{i} + \sinh t\,\mathbf{j}$
26. $\mathbf{r}(t) = \sqrt{t}\mathbf{i} + (2t + 4)\mathbf{j}$
27. $\mathbf{r}(t) = 2\cos t\,\mathbf{i} + 2\sin t\,\mathbf{j} + t\mathbf{k}$
28. $\mathbf{r}(t) = 9\cos t\,\mathbf{i} + 4\sin t\,\mathbf{j} + t\mathbf{k}$
29. $\mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j} + 2\mathbf{k}$
30. $\mathbf{r}(t) = t\mathbf{i} + t\mathbf{j} + \sin t\,\mathbf{k}; \quad 0 \le t \le 2\pi$

**31–34 True–False Determine whether the statement is true or false. Explain your answer.**
31. The natural domain of a vector-valued function is the union of the domains of its component functions.
32. If $\mathbf{r}(t) = \langle x(t), y(t) \rangle$ is a vector-valued function in 2-space, then the graph of $\mathbf{r}(t)$ is a surface in 3-space.
33. If $\mathbf{r}_0$ and $\mathbf{r}_1$ are vectors in 3-space, then the graph of the vector-valued function $\mathbf{r}(t) = (1 - t)\mathbf{r}_0 + t\mathbf{r}_1 \; (0 \le t \le 1)$ is the straight line segment joining the terminal points of $\mathbf{r}_0$ and $\mathbf{r}_1$.
34. The graph of $\mathbf{r}(t) = \langle 2\cos t, 2\sin t, t \rangle$ is a circular helix.

**35–36 Sketch the curve of intersection of the surfaces, and find parametric equations for the intersection in terms of parameter $x = t$. Check your work with a graphing utility by generating the parametric curve over the interval $-1 \le t \le 1$.**
35. $z = x^2 + y^2, \quad x - y = 0$
36. $y + x = 0, \quad z = \sqrt{2 - x^2 - y^2}$

**37–38 Sketch the curve of intersection of the surfaces, and find a vector equation for the curve in terms of the parameter $x = t$.**
37. $9x^2 + y^2 + 9z^2 = 81, \quad y = x^2 \quad (z > 0)$
38. $y = x, \quad x + y + z = 1$

**39.** Show that the graph of $\mathbf{r} = t\sin t\,\mathbf{i} + t\cos t\,\mathbf{j} + t^2\mathbf{k}$ lies on the paraboloid $z = x^2 + y^2$.

**40.** Show that the graph of $\mathbf{r} = t\mathbf{i} + \frac{1 + t}{t}\mathbf{j} + \frac{1 - t^2}{t}\mathbf{k}, \quad t > 0$ lies in the plane $x - y + z + 1 = 0$.

#### FOCUS ON CONCEPTS
**41.** Show that the graph of $\mathbf{r} = \sin t\,\mathbf{i} + 2\cos t\,\mathbf{j} + \sqrt{3}\sin t\,\mathbf{k}$ is a circle, and find its center and radius. [*Hint:* Show that the curve lies on both a sphere and a plane.]

**42.** Show that the graph of $\mathbf{r} = 3\cos t\,\mathbf{i} + 3\sin t\,\mathbf{j} + 3\sin t\,\mathbf{k}$ is an ellipse, and find the lengths of the major and minor axes. [*Hint:* Show that the graph lies on both a circular cylinder and a plane and use the result in Exercise 44 of Section 10.4.]

**43.** For the helix $\mathbf{r} = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} + ct\mathbf{k}$, find the value of $c$ ($c > 0$) so that the helix will make one complete turn in a distance of 3 units measured along the $z$-axis.

**44.** How many revolutions will the circular helix $\mathbf{r} = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} + 0.2t\mathbf{k}$ make in a distance of 10 units measured along the $z$-axis?

**45.** Show that the curve $\mathbf{r} = t\cos t\,\mathbf{i} + t\sin t\,\mathbf{j} + t\mathbf{k}, \quad t \ge 0$, lies on the cone $z = \sqrt{x^2 + y^2}$. Describe the curve.

**46.** Describe the curve $\mathbf{r} = a\cos t\,\mathbf{i} + b\sin t\,\mathbf{j} + ct\mathbf{k}$, where $a, b,$ and $c$ are positive constants such that $a \neq b$.

**47.** In each part, match the vector equation with one of the accompanying graphs, and explain your reasoning.  
(a) $\mathbf{r} = t\mathbf{i} - t\mathbf{j} + \sqrt{2 - t^2}\mathbf{k}$  
(b) $\mathbf{r} = \sin\pi t\,\mathbf{i} - t\mathbf{j} + t\mathbf{k}$  
(c) $\mathbf{r} = \sin t\,\mathbf{i} + \cos t\,\mathbf{j} + \sin 2t\,\mathbf{k}$  
(d) $\mathbf{r} = \frac{1}{2}t\mathbf{i} + \cos 3t\,\mathbf{j} + \sin 3t\,\mathbf{k}$

**48.** Check your conclusions in Exercise 47 by generating the curves with a graphing utility.

**49.**  
(a) Find parametric equations for the curve of intersection of the circular cylinder $x^2 + y^2 = 9$ and the parabolic cylinder $z = x^2$ in terms of a parameter $t$ for which $x = 3\cos t$.  
(b) Use a graphing utility to generate the curve of intersection in part (a).

**50.**  
(a) Sketch the graph of $\mathbf{r}(t) = \left\langle 2t, \frac{2}{1 + t^2} \right\rangle$.  
(b) Prove that the curve in part (a) is also the graph of the function $y = \frac{8}{4 + x^2}$.  
*(The graphs of $y = a^3/(a^2 + x^2)$ are known as the "witch of Agnesi".)*

**51. Writing** Consider the curve $C$ of intersection of the cone $z = \sqrt{x^2 + y^2}$ and the plane $z = y + 2$. Sketch and identify the curve $C$, and describe a procedure for finding a vector-valued function $\mathbf{r}(t)$ whose graph is $C$.

**52. Writing** Suppose that $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ are vector-valued functions in 2-space. Explain why solving the equation $\mathbf{r}_1(t) = \mathbf{r}_2(t)$ may not produce all of the points where the graphs of these functions intersect.

#### QUICK CHECK ANSWERS 12.1
1. (a) $\mathbf{r} = \frac{1}{t}\mathbf{i} + \sqrt{t}\mathbf{j} + \sin^{-1} t\,\mathbf{k}$ (b) $0 < t \le 1; \; 2\mathbf{i} + \frac{\sqrt{2}}{2}\mathbf{j} + \frac{\pi}{6}\mathbf{k}$  
2. The graph is a line through $(1, -1)$ with direction vector $2\mathbf{i} + 3\mathbf{j}$.  
3. The graph is the line segment in the $xy$-plane from $(0, 1)$ to $(1, 0)$.  
4. $\mathbf{r} = \langle t, t^2, t^2 \rangle$

---

## 12.2 CALCULUS OF VECTOR-VALUED FUNCTIONS

In this section we will define limits, derivatives, and integrals of vector-valued functions and discuss their properties.

### LIMITS AND CONTINUITY

Our first goal in this section is to develop a notion of what it means for a vector-valued function $\mathbf{r}(t)$ in 2-space or 3-space to approach a limiting vector $\mathbf{L}$ as $t$ approaches a number $a$. That is, we want to define
$$\lim_{t \to a} \mathbf{r}(t) = \mathbf{L} \tag{1}$$

One way to motivate a reasonable definition of (1) is to position $\mathbf{r}(t)$ and $\mathbf{L}$ with their initial points at the origin and interpret this limit to mean that the terminal point of $\mathbf{r}(t)$ approaches the terminal point of $\mathbf{L}$ as $t$ approaches $a$ or, equivalently, that the vector $\mathbf{r}(t)$ approaches the vector $\mathbf{L}$ in both length and direction as $t$ approaches $a$ (Figure 12.2.1). Algebraically, this is equivalent to stating that
$$\lim_{t \to a} \|\mathbf{r}(t) - \mathbf{L}\| = 0 \tag{2}$$
(Figure 12.2.2). Thus, we make the following definition.

> **12.2.1 DEFINITION**  
> Let $\mathbf{r}(t)$ be a vector-valued function that is defined for all $t$ in some open interval containing the number $a$, except that $\mathbf{r}(t)$ need not be defined at $a$. We will write
> $$\lim_{t \to a} \mathbf{r}(t) = \mathbf{L}$$
> if and only if
> $$\lim_{t \to a} \|\mathbf{r}(t) - \mathbf{L}\| = 0$$

> *Note that $\|\mathbf{r}(t) - \mathbf{L}\|$ is a real number for each value of $t$, so even though this expression involves a vector-valued function, the limit $\lim_{t \to a} \|\mathbf{r}(t) - \mathbf{L}\|$ is an ordinary limit of a real-valued function.*

It is clear intuitively that $\mathbf{r}(t)$ will approach a limiting vector $\mathbf{L}$ as $t$ approaches $a$ if and only if the component functions of $\mathbf{r}(t)$ approach the corresponding components of $\mathbf{L}$. This suggests the following theorem, whose formal proof is omitted.

> **12.2.2 THEOREM**  
> (a) If $\mathbf{r}(t) = \langle x(t), y(t) \rangle = x(t)\mathbf{i} + y(t)\mathbf{j}$, then
> $$\lim_{t \to a} \mathbf{r}(t) = \left\langle \lim_{t \to a} x(t), \lim_{t \to a} y(t) \right\rangle = \left(\lim_{t \to a} x(t)\right)\mathbf{i} + \left(\lim_{t \to a} y(t)\right)\mathbf{j}$$
> provided the limits of the component functions exist. Conversely, the limits of the component functions exist provided $\mathbf{r}(t)$ approaches a limiting vector as $t$ approaches $a$.  
> (b) If $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$, then
> $$\lim_{t \to a} \mathbf{r}(t) = \left\langle \lim_{t \to a} x(t), \lim_{t \to a} y(t), \lim_{t \to a} z(t) \right\rangle = \left(\lim_{t \to a} x(t)\right)\mathbf{i} + \left(\lim_{t \to a} y(t)\right)\mathbf{j} + \left(\lim_{t \to a} z(t)\right)\mathbf{k}$$
> provided the limits of the component functions exist. Conversely, the limits of the component functions exist provided $\mathbf{r}(t)$ approaches a limiting vector as $t$ approaches $a$.

#### Example 1
Let $\mathbf{r}(t) = t^2\mathbf{i} + e^t\mathbf{j} - (2\cos\pi t)\mathbf{k}$. Then
$$\lim_{t \to 0}\mathbf{r}(t) = \left(\lim_{t \to 0}t^2\right)\mathbf{i} + \left(\lim_{t \to 0}e^t\right)\mathbf{j} - \left(\lim_{t \to 0}2\cos\pi t\right)\mathbf{k} = \mathbf{j} - 2\mathbf{k}$$
Alternatively, using the angle bracket notation for vectors,
$$\lim_{t \to 0}\mathbf{r}(t) = \lim_{t \to 0}\langle t^2, e^t, -2\cos\pi t \rangle = \left\langle \lim_{t \to 0}t^2, \lim_{t \to 0}e^t, \lim_{t \to 0}(-2\cos\pi t) \right\rangle = \langle 0, 1, -2 \rangle$$

Motivated by the definition of continuity for real-valued functions, we define a vector-valued function $\mathbf{r}(t)$ to be **continuous at $t = a$** if
$$\lim_{t \to a}\mathbf{r}(t) = \mathbf{r}(a) \tag{3}$$
That is, $\mathbf{r}(a)$ is defined, the limit of $\mathbf{r}(t)$ as $t \to a$ exists, and the two are equal. As in the case for real-valued functions, we say that $\mathbf{r}(t)$ is **continuous on an interval $I$** if it is continuous at each point of $I$ [with the understanding that at an endpoint in $I$ the two-sided limit in (3) is replaced by the appropriate one-sided limit]. It follows from Theorem 12.2.2 that a vector-valued function is continuous at $t = a$ if and only if its component functions are continuous at $t = a$.

---

### DERIVATIVES

The derivative of a vector-valued function is defined by a limit similar to that for the derivative of a real-valued function.

> **12.2.3 DEFINITION**  
> If $\mathbf{r}(t)$ is a vector-valued function, we define the **derivative of $\mathbf{r}$ with respect to $t$** to be the vector-valued function $\mathbf{r}'$ given by
> $$\mathbf{r}'(t) = \lim_{h \to 0} \frac{\mathbf{r}(t + h) - \mathbf{r}(t)}{h} \tag{4}$$
> The domain of $\mathbf{r}'$ consists of all values of $t$ in the domain of $\mathbf{r}(t)$ for which the limit exists.

The function $\mathbf{r}(t)$ is **differentiable at $t$** if the limit in (4) exists. All of the standard notations for derivatives continue to apply:
$$\frac{d}{dt}[\mathbf{r}(t)], \quad \frac{d\mathbf{r}}{dt}, \quad \mathbf{r}'(t), \quad \text{or} \quad \mathbf{r}'$$

It is important to keep in mind that $\mathbf{r}'(t)$ is a vector, not a number, and hence has a magnitude and a direction for each value of $t$ [except if $\mathbf{r}'(t) = \mathbf{0}$, in which case $\mathbf{r}'(t)$ has magnitude zero but no specific direction].

> **12.2.4 GEOMETRIC INTERPRETATION OF THE DERIVATIVE**  
> Suppose that $C$ is the graph of a vector-valued function $\mathbf{r}(t)$ in 2-space or 3-space and that $\mathbf{r}'(t)$ exists and is nonzero for a given value of $t$. If the vector $\mathbf{r}'(t)$ is positioned with its initial point at the terminal point of the radius vector $\mathbf{r}(t)$, then $\mathbf{r}'(t)$ is tangent to $C$ and points in the direction of increasing parameter.

> **12.2.5 THEOREM**  
> If $\mathbf{r}(t)$ is a vector-valued function, then $\mathbf{r}$ is differentiable at $t$ if and only if each of its component functions is differentiable at $t$, in which case the component functions of $\mathbf{r}'(t)$ are the derivatives of the corresponding component functions of $\mathbf{r}(t)$.

**Proof.** For simplicity, we give the proof in 2-space; the proof in 3-space is identical, except for the additional component. Assume that $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j}$. Then
$$\mathbf{r}'(t) = \lim_{h \to 0}\frac{\mathbf{r}(t + h) - \mathbf{r}(t)}{h} = \lim_{h \to 0}\frac{[x(t + h)\mathbf{i} + y(t + h)\mathbf{j}] - [x(t)\mathbf{i} + y(t)\mathbf{j}]}{h}$$
$$= \left(\lim_{h \to 0}\frac{x(t + h) - x(t)}{h}\right)\mathbf{i} + \left(\lim_{h \to 0}\frac{y(t + h) - y(t)}{h}\right)\mathbf{j} = x'(t)\mathbf{i} + y'(t)\mathbf{j} \quad \blacksquare$$

#### Example 2
Let $\mathbf{r}(t) = t^2\mathbf{i} + e^t\mathbf{j} - (2\cos\pi t)\mathbf{k}$. Then
$$\mathbf{r}'(t) = \frac{d}{dt}(t^2)\mathbf{i} + \frac{d}{dt}(e^t)\mathbf{j} - \frac{d}{dt}(2\cos\pi t)\mathbf{k} = 2t\mathbf{i} + e^t\mathbf{j} + (2\pi\sin\pi t)\mathbf{k}$$

---

### DERIVATIVE RULES

> **12.2.6 THEOREM (Rules of Differentiation)**  
> Let $\mathbf{r}(t), \mathbf{r}_1(t),$ and $\mathbf{r}_2(t)$ be differentiable vector-valued functions that are all in 2-space or all in 3-space, and let $f(t)$ be a differentiable real-valued function, $k$ a scalar, and $\mathbf{c}$ a constant vector (that is, a vector whose value does not depend on $t$). Then the following rules of differentiation hold:
> (a) $\frac{d}{dt}[\mathbf{c}] = \mathbf{0}$  
> (b) $\frac{d}{dt}[k\mathbf{r}(t)] = k\frac{d}{dt}[\mathbf{r}(t)]$  
> (c) $\frac{d}{dt}[\mathbf{r}_1(t) + \mathbf{r}_2(t)] = \frac{d}{dt}[\mathbf{r}_1(t)] + \frac{d}{dt}[\mathbf{r}_2(t)]$  
> (d) $\frac{d}{dt}[\mathbf{r}_1(t) - \mathbf{r}_2(t)] = \frac{d}{dt}[\mathbf{r}_1(t)] - \frac{d}{dt}[\mathbf{r}_2(t)]$  
> (e) $\frac{d}{dt}[f(t)\mathbf{r}(t)] = f(t)\frac{d}{dt}[\mathbf{r}(t)] + \frac{d}{dt}[f(t)]\mathbf{r}(t)$

---

### TANGENT LINES TO GRAPHS OF VECTOR-VALUED FUNCTIONS

> **12.2.7 DEFINITION**  
> Let $P$ be a point on the graph of a vector-valued function $\mathbf{r}(t)$, and let $\mathbf{r}(t_0)$ be the radius vector from the origin to $P$ (Figure 12.2.4). If $\mathbf{r}'(t_0)$ exists and $\mathbf{r}'(t_0) \neq \mathbf{0}$, then we call $\mathbf{r}'(t_0)$ a **tangent vector** to the graph of $\mathbf{r}(t)$ at $\mathbf{r}(t_0)$, and we call the line through $P$ that is parallel to the tangent vector the **tangent line** to the graph of $\mathbf{r}(t)$ at $\mathbf{r}(t_0)$.

Let $\mathbf{r}_0 = \mathbf{r}(t_0)$ and $\mathbf{v}_0 = \mathbf{r}'(t_0)$. It follows from Formula (9) of Section 11.5 that the tangent line to the graph of $\mathbf{r}(t)$ at $\mathbf{r}_0$ is given by the vector equation
$$\mathbf{r} = \mathbf{r}_0 + t\mathbf{v}_0 \tag{5}$$

#### Example 3
Find parametric equations of the tangent line to the circular helix
$$x = \cos t, \quad y = \sin t, \quad z = t$$
where $t = t_0$, and use that result to find parametric equations for the tangent line at the point where $t = \pi$.

**Solution.** The vector equation of the helix is $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\mathbf{k}$, so we have
$$\mathbf{r}_0 = \mathbf{r}(t_0) = \cos t_0\mathbf{i} + \sin t_0\mathbf{j} + t_0\mathbf{k}$$
$$\mathbf{v}_0 = \mathbf{r}'(t_0) = (-\sin t_0)\mathbf{i} + \cos t_0\mathbf{j} + \mathbf{k}$$
It follows from (5) that the vector equation of the tangent line at $t = t_0$ is
$$\mathbf{r} = \cos t_0\mathbf{i} + \sin t_0\mathbf{j} + t_0\mathbf{k} + t[(-\sin t_0)\mathbf{i} + \cos t_0\mathbf{j} + \mathbf{k}]$$
$$= (\cos t_0 - t\sin t_0)\mathbf{i} + (\sin t_0 + t\cos t_0)\mathbf{j} + (t_0 + t)\mathbf{k}$$
Thus, the parametric equations of the tangent line at $t = t_0$ are
$$x = \cos t_0 - t\sin t_0, \quad y = \sin t_0 + t\cos t_0, \quad z = t_0 + t$$
In particular, the tangent line at $t = \pi$ has parametric equations
$$x = -1, \quad y = -t, \quad z = \pi + t$$
The graph of the helix and this tangent line are shown in Figure 12.2.5.

#### Example 4
Let $\mathbf{r}_1(t) = (\tan^{-1} t)\mathbf{i} + (\sin t)\mathbf{j} + t^2\mathbf{k}$ and $\mathbf{r}_2(t) = (t^2 - t)\mathbf{i} + (2t - 2)\mathbf{j} + (\ln t)\mathbf{k}$. The graphs of $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ intersect at the origin. Find the degree measure of the acute angle between the tangent lines to the graphs of $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ at the origin.

**Solution.** The graph of $\mathbf{r}_1(t)$ passes through the origin at $t = 0$, where its tangent vector is
$$\mathbf{r}_1'(0) = \left\langle \frac{1}{1 + t^2}, \cos t, 2t \right\rangle\Bigg|_{t=0} = \langle 1, 1, 0 \rangle$$
The graph of $\mathbf{r}_2(t)$ passes through the origin at $t = 1$ (verify), where its tangent vector is
$$\mathbf{r}_2'(1) = \left\langle 2t - 1, 2, \frac{1}{t} \right\rangle\Bigg|_{t=1} = \langle 1, 2, 1 \rangle$$
By Theorem 11.3.3, the angle $\theta$ between these two tangent vectors satisfies
$$\cos\theta = \frac{\langle 1, 1, 0 \rangle \cdot \langle 1, 2, 1 \rangle}{\|\langle 1, 1, 0 \rangle\| \|\langle 1, 2, 1 \rangle\|} = \frac{1 + 2 + 0}{\sqrt{2}\sqrt{6}} = \frac{3}{\sqrt{12}} = \frac{\sqrt{3}}{2}$$
It follows that $\theta = \pi/6$ radians, or $30^\circ$.

---

### DERIVATIVES OF DOT AND CROSS PRODUCTS

$$\frac{d}{dt}[\mathbf{r}_1(t) \cdot \mathbf{r}_2(t)] = \mathbf{r}_1(t) \cdot \frac{d\mathbf{r}_2}{dt} + \frac{d\mathbf{r}_1}{dt} \cdot \mathbf{r}_2(t) \tag{6}$$
$$\frac{d}{dt}[\mathbf{r}_1(t) \times \mathbf{r}_2(t)] = \mathbf{r}_1(t) \times \frac{d\mathbf{r}_2}{dt} + \frac{d\mathbf{r}_1}{dt} \times \mathbf{r}_2(t) \tag{7}$$

> *Note that in (6) the order of the factors in each term on the right does not matter, but in (7) it does.*

> **12.2.8 THEOREM**  
> If $\mathbf{r}(t)$ is a differentiable vector-valued function in 2-space or 3-space and $\|\mathbf{r}(t)\|$ is constant for all $t$, then
> $$\mathbf{r}(t) \cdot \mathbf{r}'(t) = 0 \tag{8}$$
> that is, $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal vectors for all $t$.

**Proof.** It follows from (6) with $\mathbf{r}_1(t) = \mathbf{r}_2(t) = \mathbf{r}(t)$ that
$$\frac{d}{dt}[\mathbf{r}(t) \cdot \mathbf{r}(t)] = \mathbf{r}(t) \cdot \frac{d\mathbf{r}}{dt} + \frac{d\mathbf{r}}{dt} \cdot \mathbf{r}(t) \quad \text{or, equivalently,} \quad \frac{d}{dt}[\|\mathbf{r}(t)\|^2] = 2\mathbf{r}(t) \cdot \frac{d\mathbf{r}}{dt} \tag{9}$$
But $\|\mathbf{r}(t)\|^2$ is constant, so its derivative is zero. Thus $2\mathbf{r}(t) \cdot \frac{d\mathbf{r}}{dt} = 0$, from which (8) follows. $\blacksquare$

#### Example 5
Just as a tangent line to a circle in 2-space is perpendicular to the radius at the point of tangency, so a tangent vector to a curve on the surface of a sphere in 3-space that is centered at the origin is orthogonal to the radius vector at the point of tangency (Figure 12.2.6). To see that this is so, suppose that the graph of $\mathbf{r}(t)$ lies on the surface of a sphere of positive radius $k$ centered at the origin. For each value of $t$ we have $\|\mathbf{r}(t)\| = k$, so by Theorem 12.2.8 $\mathbf{r}(t) \cdot \mathbf{r}'(t) = 0$ and hence the radius vector $\mathbf{r}(t)$ and the tangent vector $\mathbf{r}'(t)$ are orthogonal.

---

### DEFINITE INTEGRALS OF VECTOR-VALUED FUNCTIONS

If $\mathbf{r}(t)$ is a vector-valued function that is continuous on the interval $a \le t \le b$, then we define the **definite integral** of $\mathbf{r}(t)$ over this interval as a limit of Riemann sums:
$$\int_a^b \mathbf{r}(t)\,dt = \lim_{\max \Delta t_k \to 0} \sum_{k=1}^n \mathbf{r}(t_k^*)\Delta t_k \tag{10}$$

In component form:
$$\int_a^b \mathbf{r}(t)\,dt = \left(\int_a^b x(t)\,dt\right)\mathbf{i} + \left(\int_a^b y(t)\,dt\right)\mathbf{j} \quad \text{2-space} \tag{11}$$
$$\int_a^b \mathbf{r}(t)\,dt = \left(\int_a^b x(t)\,dt\right)\mathbf{i} + \left(\int_a^b y(t)\,dt\right)\mathbf{j} + \left(\int_a^b z(t)\,dt\right)\mathbf{k} \quad \text{3-space} \tag{12}$$

#### Example 6
Let $\mathbf{r}(t) = t^2\mathbf{i} + e^t\mathbf{j} - (2\cos\pi t)\mathbf{k}$. Then
$$\int_0^1 \mathbf{r}(t)\,dt = \left(\int_0^1 t^2\,dt\right)\mathbf{i} + \left(\int_0^1 e^t\,dt\right)\mathbf{j} - \left(\int_0^1 2\cos\pi t\,dt\right)\mathbf{k}$$
$$= \left[\frac{t^3}{3}\right]_0^1\mathbf{i} + [e^t]_0^1\mathbf{j} - \left[\frac{2}{\pi}\sin\pi t\right]_0^1\mathbf{k} = \frac{1}{3}\mathbf{i} + (e - 1)\mathbf{j}$$

---

### RULES OF INTEGRATION

> **12.2.9 THEOREM (Rules of Integration)**  
> Let $\mathbf{r}(t), \mathbf{r}_1(t),$ and $\mathbf{r}_2(t)$ be vector-valued functions in 2-space or 3-space that are continuous on the interval $a \le t \le b$, and let $k$ be a scalar. Then:
> (a) $\int_a^b k\mathbf{r}(t)\,dt = k\int_a^b \mathbf{r}(t)\,dt$  
> (b) $\int_a^b [\mathbf{r}_1(t) + \mathbf{r}_2(t)]\,dt = \int_a^b \mathbf{r}_1(t)\,dt + \int_a^b \mathbf{r}_2(t)\,dt$  
> (c) $\int_a^b [\mathbf{r}_1(t) - \mathbf{r}_2(t)]\,dt = \int_a^b \mathbf{r}_1(t)\,dt - \int_a^b \mathbf{r}_2(t)\,dt$

---

### ANTIDERIVATIVES OF VECTOR-VALUED FUNCTIONS

An antiderivative for a vector-valued function $\mathbf{r}(t)$ is a vector-valued function $\mathbf{R}(t)$ such that $\mathbf{R}'(t) = \mathbf{r}(t) \tag{13}$.
$$\int \mathbf{r}(t)\,dt = \mathbf{R}(t) + \mathbf{C} \tag{14}$$
where $\mathbf{C}$ represents an arbitrary constant vector.

#### Example 7
$$\int (2t\mathbf{i} + 3t^2\mathbf{j})\,dt = \left(\int 2t\,dt\right)\mathbf{i} + \left(\int 3t^2\,dt\right)\mathbf{j} = (t^2 + C_1)\mathbf{i} + (t^3 + C_2)\mathbf{j} = (t^2\mathbf{i} + t^3\mathbf{j}) + \mathbf{C}$$
where $\mathbf{C} = C_1\mathbf{i} + C_2\mathbf{j}$ is an arbitrary vector constant of integration.

Vector differentiation and integration are inverse operations:
$$\frac{d}{dt}\left[\int \mathbf{r}(t)\,dt\right] = \mathbf{r}(t) \quad \text{and} \quad \int \mathbf{r}'(t)\,dt = \mathbf{r}(t) + \mathbf{C} \tag{15–16}$$

**Fundamental Theorem of Calculus (Vector Form):**
$$\int_a^b \mathbf{r}(t)\,dt = \mathbf{R}(t)\Bigg|_a^b = \mathbf{R}(b) - \mathbf{R}(a) \tag{17}$$

#### Example 8
Evaluate the definite integral $\int_0^2 (2t\mathbf{i} + 3t^2\mathbf{j})\,dt$.  
**Solution.** Integrating the components yields
$$\int_0^2 (2t\mathbf{i} + 3t^2\mathbf{j})\,dt = [t^2]_0^2\mathbf{i} + [t^3]_0^2\mathbf{j} = 4\mathbf{i} + 8\mathbf{j}$$

#### Example 9
Find $\mathbf{r}(t)$ given that $\mathbf{r}'(t) = \langle 3, 2t \rangle$ and $\mathbf{r}(1) = \langle 2, 5 \rangle$.  
**Solution.** Integrating $\mathbf{r}'(t)$ yields $\mathbf{r}(t) = \int \langle 3, 2t \rangle\,dt = \langle 3t, t^2 \rangle + \mathbf{C}$.  
Substituting $t = 1$: $\mathbf{r}(1) = \langle 3, 1 \rangle + \mathbf{C} = \langle 2, 5 \rangle \implies \mathbf{C} = \langle -1, 4 \rangle$.  
Thus, $\mathbf{r}(t) = \langle 3t - 1, t^2 + 4 \rangle$.

---

### QUICK CHECK EXERCISES 12.2
*(See page 858 for answers.)*

1. (a) $\lim_{t \to 3}(t^2\mathbf{i} + 2t\mathbf{j}) = \underline{\quad}$  
   (b) $\lim_{t \to \pi/4}\langle \cos t, \sin t \rangle = \underline{\quad}$
2. Find $\mathbf{r}'(t)$.  
   (a) $\mathbf{r}(t) = (4 + 5t)\mathbf{i} + (t - t^2)\mathbf{j}$  
   (b) $\mathbf{r}(t) = \left\langle \frac{1}{t}, \tan t, e^{2t} \right\rangle$
3. Suppose that $\mathbf{r}_1(0) = \langle 3, 2, 1 \rangle, \; \mathbf{r}_2(0) = \langle 1, 2, 3 \rangle, \; \mathbf{r}_1'(0) = \langle 0, 0, 0 \rangle,$ and $\mathbf{r}_2'(0) = \langle -6, -4, -2 \rangle$. Use this information to evaluate the derivative of each function at $t = 0$.  
   (a) $\mathbf{r}(t) = 2\mathbf{r}_1(t) - \mathbf{r}_2(t)$  
   (b) $\mathbf{r}(t) = \cos t\,\mathbf{r}_1(t) + e^{2t}\mathbf{r}_2(t)$  
   (c) $\mathbf{r}(t) = \mathbf{r}_1(t) \times \mathbf{r}_2(t)$  
   (d) $f(t) = \mathbf{r}_1(t) \cdot \mathbf{r}_2(t)$
4. (a) $\int_0^1 \langle 2t, t^2, \sin\pi t \rangle\,dt = \underline{\quad}$  
   (b) $\int (t\mathbf{i} - 3t^2\mathbf{j} + e^t\mathbf{k})\,dt = \underline{\quad}$

---

### EXERCISE SET 12.2

**1–4 Find the limit.**
1. $\lim_{t \to +\infty}\left\langle \frac{t^2 + 1}{3t^2 + 2}, \frac{1}{t} \right\rangle$
2. $\lim_{t \to 0^+}\left(\sqrt{t}\mathbf{i} + \frac{\sin t}{t}\mathbf{j}\right)$
3. $\lim_{t \to 2}(t\mathbf{i} - 3\mathbf{j} + t^2\mathbf{k})$
4. $\lim_{t \to 1}\left\langle \frac{3}{t^2}, \frac{\ln t}{t^2 - 1}, \sin 2t \right\rangle$

**5–6 Determine whether $\mathbf{r}(t)$ is continuous at $t = 0$. Explain your reasoning.**
5. (a) $\mathbf{r}(t) = 3\sin t\,\mathbf{i} - 2t\mathbf{j}$  
   (b) $\mathbf{r}(t) = t^2\mathbf{i} + \frac{1}{t}\mathbf{j} + t\mathbf{k}$
6. (a) $\mathbf{r}(t) = e^t\mathbf{i} + \mathbf{j} + \csc t\,\mathbf{k}$  
   (b) $\mathbf{r}(t) = 5\mathbf{i} - \sqrt{3t + 1}\mathbf{j} + e^{2t}\mathbf{k}$

**7.** Sketch the circle $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j}$, and in each part draw the vector with its correct length:  
(a) $\mathbf{r}'(\pi/4)$ (b) $\mathbf{r}''(\pi)$ (c) $\mathbf{r}(2\pi) - \mathbf{r}(3\pi/2)$

**8.** Sketch the circle $\mathbf{r}(t) = \cos t\,\mathbf{i} - \sin t\,\mathbf{j}$, and in each part draw the vector with its correct length:  
(a) $\mathbf{r}'(\pi/4)$ (b) $\mathbf{r}''(\pi)$ (c) $\mathbf{r}(2\pi) - \mathbf{r}(3\pi/2)$

**9–10 Find $\mathbf{r}'(t)$.**
9. $\mathbf{r}(t) = 4\mathbf{i} - \cos t\,\mathbf{j}$
10. $\mathbf{r}(t) = (\tan^{-1} t)\mathbf{i} + t\cos t\,\mathbf{j} - \sqrt{t}\mathbf{k}$

**11–14 Find the vector $\mathbf{r}'(t_0)$; then sketch the graph of $\mathbf{r}(t)$ in 2-space and draw the tangent vector $\mathbf{r}'(t_0)$.**
11. $\mathbf{r}(t) = \langle t, t^2 \rangle; \quad t_0 = 2$
12. $\mathbf{r}(t) = t^3\mathbf{i} + t^2\mathbf{j}; \quad t_0 = 1$
13. $\mathbf{r}(t) = \sec t\,\mathbf{i} + \tan t\,\mathbf{j}; \quad t_0 = 0$
14. $\mathbf{r}(t) = 2\sin t\,\mathbf{i} + 3\cos t\,\mathbf{j}; \quad t_0 = \pi/6$

**15–16 Find the vector $\mathbf{r}'(t_0)$; then sketch the graph of $\mathbf{r}(t)$ in 3-space and draw the tangent vector $\mathbf{r}'(t_0)$.**
15. $\mathbf{r}(t) = 2\sin t\,\mathbf{i} + \mathbf{j} + 2\cos t\,\mathbf{k}; \quad t_0 = \pi/2$
16. $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\mathbf{k}; \quad t_0 = \pi/4$

**17–18 Use a graphing utility to generate the graph of $\mathbf{r}(t)$ and the graph of the tangent line at $t_0$ on the same screen.**
17. $\mathbf{r}(t) = \sin\pi t\,\mathbf{i} + t^2\mathbf{j}; \quad t_0 = \frac{1}{2}$
18. $\mathbf{r}(t) = 3\sin t\,\mathbf{i} + 4\cos t\,\mathbf{j}; \quad t_0 = \pi/4$

**19–22 Find parametric equations of the line tangent to the graph of $\mathbf{r}(t)$ at the point where $t = t_0$.**
19. $\mathbf{r}(t) = t^2\mathbf{i} + (2 - \ln t)\mathbf{j}; \quad t_0 = 1$
20. $\mathbf{r}(t) = e^{2t}\mathbf{i} - 2\cos 3t\,\mathbf{j}; \quad t_0 = 0$
21. $\mathbf{r}(t) = 2\cos\pi t\,\mathbf{i} + 2\sin\pi t\,\mathbf{j} + 3t\mathbf{k}; \quad t_0 = \frac{1}{3}$
22. $\mathbf{r}(t) = \ln t\,\mathbf{i} + e^{-t}\mathbf{j} + t^3\mathbf{k}; \quad t_0 = 2$

**23–26 Find a vector equation of the line tangent to the graph of $\mathbf{r}(t)$ at the point $P_0$ on the curve.**
23. $\mathbf{r}(t) = (2t - 1)\mathbf{i} + \sqrt{3t + 4}\mathbf{j}; \quad P_0(-1, 2)$
24. $\mathbf{r}(t) = 4\cos t\,\mathbf{i} - 3t\mathbf{j}; \quad P_0(2, -\pi)$
25. $\mathbf{r}(t) = t^2\mathbf{i} - \frac{1}{t + 1}\mathbf{j} + (4 - t^2)\mathbf{k}; \quad P_0(4, 1, 0)$
26. $\mathbf{r}(t) = \sin t\,\mathbf{i} + \cosh t\,\mathbf{j} + (\tan^{-1} t)\mathbf{k}; \quad P_0(0, 1, 0)$

**27.** Let $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + \mathbf{k}$. Find:  
(a) $\lim_{t \to 0}(\mathbf{r}(t) - \mathbf{r}'(t))$  
(b) $\lim_{t \to 0}(\mathbf{r}(t) \times \mathbf{r}'(t))$  
(c) $\lim_{t \to 0}(\mathbf{r}(t) \cdot \mathbf{r}'(t))$

**28.** Let $\mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j} + t^3\mathbf{k}$. Find $\lim_{t \to 1} \mathbf{r}(t) \cdot (\mathbf{r}'(t) \times \mathbf{r}''(t))$.

**29–30 Calculate $\frac{d}{dt}[\mathbf{r}_1(t) \cdot \mathbf{r}_2(t)]$ and $\frac{d}{dt}[\mathbf{r}_1(t) \times \mathbf{r}_2(t)]$ first by differentiating the product directly and then by applying Formulas (6) and (7).**
29. $\mathbf{r}_1(t) = 2t\mathbf{i} + 3t^2\mathbf{j} + t^3\mathbf{k}, \quad \mathbf{r}_2(t) = t^4\mathbf{k}$
30. $\mathbf{r}_1(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\mathbf{k}, \quad \mathbf{r}_2(t) = \mathbf{i} + t\mathbf{k}$

**31–34 Evaluate the indefinite integral.**
31. $\int (3\mathbf{i} + 4t\mathbf{j})\,dt$
32. $\int \left(t^2\mathbf{i} - 2t\mathbf{j} + \frac{1}{t}\mathbf{k}\right)dt$
33. $\int \langle te^t, \ln t \rangle\,dt$
34. $\int \langle e^{-t}, e^t, 3t^2 \rangle\,dt$

**35–40 Evaluate the definite integral.**
35. $\int_0^{\pi/2} \langle \cos 2t, \sin 2t \rangle\,dt$
36. $\int_0^1 (t^2\mathbf{i} + t^3\mathbf{j})\,dt$
37. $\int_0^2 \|t\mathbf{i} + t^2\mathbf{j}\|\,dt$
38. $\int_{-3}^3 \langle (3 - t)^{3/2}, (3 + t)^{3/2}, 1 \rangle\,dt$
39. $\int_1^9 (t^{1/2}\mathbf{i} + t^{-1/2}\mathbf{j})\,dt$
40. $\int_0^1 (e^{2t}\mathbf{i} + e^{-t}\mathbf{j} + t\mathbf{k})\,dt$

**41–44 True–False Determine whether the statement is true or false. Explain your answer.**
41. If a vector-valued function $\mathbf{r}(t)$ is continuous at $t = a$, then the limit $\lim_{h \to 0}\frac{\mathbf{r}(a + h) - \mathbf{r}(a)}{h}$ exists.
42. If $\mathbf{r}(t)$ is a vector-valued function in 2-space and $\|\mathbf{r}(t)\|$ is constant, then $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are parallel vectors for all $t$.
43. If $\mathbf{r}(t)$ is a vector-valued function that is continuous on the interval $a \le t \le b$, then $\int_a^b \mathbf{r}(t)\,dt$ is a vector.
44. If $\mathbf{r}(t)$ is a vector-valued function that is continuous on the interval $[a, b]$, then for $a < t < b$, $\frac{d}{dt}\left[\int_a^t \mathbf{r}(u)\,du\right] = \mathbf{r}(t)$.

**45–48 Solve the vector initial-value problem for $\mathbf{y}(t)$ by integrating and using the initial conditions to find the constants of integration.**
45. $\mathbf{y}'(t) = 2t\mathbf{i} + 3t^2\mathbf{j}, \quad \mathbf{y}(0) = \mathbf{i} - \mathbf{j}$
46. $\mathbf{y}'(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j}, \quad \mathbf{y}(0) = \mathbf{i} - \mathbf{j}$
47. $\mathbf{y}''(t) = \mathbf{i} + e^t\mathbf{j}, \quad \mathbf{y}(0) = 2\mathbf{i}, \quad \mathbf{y}'(0) = \mathbf{j}$
48. $\mathbf{y}''(t) = 12t^2\mathbf{i} - 2t\mathbf{j}, \quad \mathbf{y}(0) = 2\mathbf{i} - 4\mathbf{j}, \quad \mathbf{y}'(0) = \mathbf{0}$

**49.**  
(a) Find the points where the curve $\mathbf{r} = t\mathbf{i} + t^2\mathbf{j} - 3t\mathbf{k}$ intersects the plane $2x - y + z = -2$.  
(b) For the curve and plane in part (a), find, to the nearest degree, the acute angle that the tangent line to the curve makes with a line normal to the plane at each point of intersection.

**50.** Find where the tangent line to the curve $\mathbf{r} = e^{-2t}\mathbf{i} + \cos t\,\mathbf{j} + 3\sin t\,\mathbf{k}$ at the point $(1, 1, 0)$ intersects the $yz$-plane.

**51–52 Show that the graphs of $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ intersect at the point $P$. Find, to the nearest degree, the acute angle between the tangent lines to the graphs of $\mathbf{r}_1(t)$ and $\mathbf{r}_2(t)$ at the point $P$.**
51. $\mathbf{r}_1(t) = t^2\mathbf{i} + t\mathbf{j} + 3t^3\mathbf{k}, \quad \mathbf{r}_2(t) = (t - 1)\mathbf{i} + \frac{1}{4}t^2\mathbf{j} + (5 - t)\mathbf{k}; \quad P(1, 1, 3)$
52. $\mathbf{r}_1(t) = 2e^{-t}\mathbf{i} + \cos t\,\mathbf{j} + (t^2 + 3)\mathbf{k}, \quad \mathbf{r}_2(t) = (1 - t)\mathbf{i} + t^2\mathbf{j} + (t^3 + 4)\mathbf{k}; \quad P(2, 1, 3)$

#### FOCUS ON CONCEPTS
**53.** Use Formula (7) to derive the differentiation formula
$$\frac{d}{dt}[\mathbf{r}(t) \times \mathbf{r}'(t)] = \mathbf{r}(t) \times \mathbf{r}''(t)$$

**54.** Let $\mathbf{u} = \mathbf{u}(t), \mathbf{v} = \mathbf{v}(t),$ and $\mathbf{w} = \mathbf{w}(t)$ be differentiable vector-valued functions. Use Formulas (6) and (7) to show that
$$\frac{d}{dt}[\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})] = \frac{d\mathbf{u}}{dt} \cdot [\mathbf{v} \times \mathbf{w}] + \mathbf{u} \cdot \left[\frac{d\mathbf{v}}{dt} \times \mathbf{w}\right] + \mathbf{u} \cdot \left[\mathbf{v} \times \frac{d\mathbf{w}}{dt}\right]$$

**55.** Let $u_1, u_2, u_3, v_1, v_2, v_3, w_1, w_2,$ and $w_3$ be differentiable functions of $t$. Use Exercise 54 to show that
$$\frac{d}{dt}\begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix} = \begin{vmatrix} u_1' & u_2' & u_3' \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix} + \begin{vmatrix} u_1 & u_2 & u_3 \\ v_1' & v_2' & v_3' \\ w_1 & w_2 & w_3 \end{vmatrix} + \begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1' & w_2' & w_3' \end{vmatrix}$$

**56.** Prove Theorem 12.2.6 for 2-space.
**57.** Derive Formulas (6) and (7) for 3-space.
**58.** Prove Theorem 12.2.9 for 2-space.

**59. Writing** Explain what it means for a vector-valued function $\mathbf{r}(t)$ to be differentiable, and discuss geometric interpretations of $\mathbf{r}'(t)$.

**60. Writing** Let $\mathbf{r}(t) = \langle t^2, t^3 + 1 \rangle$ and define $\theta(t)$ to be the angle between $\mathbf{r}(t)$ and $\mathbf{r}'(t)$. The graph of $\theta = \theta(t)$ is shown in Figure Ex-60. Interpret important features of this graph in terms of information about $\mathbf{r}(t)$ and $\mathbf{r}'(t)$. Accompany your discussion with a graph of $\mathbf{r}(t)$, highlighting particular instances of the vectors $\mathbf{r}(t)$ and $\mathbf{r}'(t)$.

#### QUICK CHECK ANSWERS 12.2
1. (a) $9\mathbf{i} + 6\mathbf{j}$ (b) $\langle \frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2} \rangle$  
2. (a) $\mathbf{r}'(t) = 5\mathbf{i} + (1 - 2t)\mathbf{j}$ (b) $\mathbf{r}'(t) = \left\langle -\frac{1}{t^2}, \sec^2 t, 2e^{2t} \right\rangle$  
3. (a) $\langle 6, 4, 2 \rangle$ (b) $\langle -4, 0, 4 \rangle$ (c) $\mathbf{0}$ (d) $-28$  
4. (a) $\left\langle 1, \frac{1}{3}, \frac{2}{\pi} \right\rangle$ (b) $\frac{t^2}{2}\mathbf{i} - t^3\mathbf{j} + e^t\mathbf{k} + \mathbf{C}$

---

## 12.3 CHANGE OF PARAMETER; ARC LENGTH

We observed in earlier sections that a curve in 2-space or 3-space can be represented parametrically in more than one way. For example, in Section 10.1 we gave two parametric representations of a circle—one in which the circle was traced clockwise and the other in which it was traced counterclockwise. Sometimes it will be desirable to change the parameter for a parametric curve to a different parameter that is better suited for the problem at hand. In this section we will investigate issues associated with changes of parameter, and we will show that arc length plays a special role in parametric representations of curves.

### SMOOTH PARAMETRIZATIONS

Graphs of vector-valued functions range from continuous and smooth to discontinuous and wildly erratic. In this text we will not be concerned with graphs of the latter type, so we will need to impose restrictions to eliminate the unwanted behavior. We will say that a curve represented by $\mathbf{r}(t)$ is **smoothly parametrized by $\mathbf{r}(t)$**, or that $\mathbf{r}(t)$ is a **smooth function of $t$** if $\mathbf{r}'(t)$ is continuous and $\mathbf{r}'(t) \neq \mathbf{0}$ for any allowable value of $t$. Geometrically, this means that a smoothly parametrized curve can have no abrupt changes in direction as the parameter increases.

> *Mathematically, "smoothness" is a property of the parametrization and not of the curve itself. Exercise 38 gives an example of a curve that is well-behaved geometrically and has one parametrization that is smooth and another that is not.*

#### Example 1
Determine whether the following vector-valued functions are smooth.  
(a) $\mathbf{r}(t) = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} + ct\mathbf{k} \quad (a > 0, c > 0)$  
(b) $\mathbf{r}(t) = t^2\mathbf{i} + t^3\mathbf{j}$

**Solution (a).** We have
$$\mathbf{r}'(t) = -a\sin t\,\mathbf{i} + a\cos t\,\mathbf{j} + c\mathbf{k}$$
The components are continuous functions, and there is no value of $t$ for which all three of them are zero (verify), so $\mathbf{r}(t)$ is a smooth function. The graph of $\mathbf{r}(t)$ is the circular helix in Figure 12.1.2.

**Solution (b).** We have
$$\mathbf{r}'(t) = 2t\mathbf{i} + 3t^2\mathbf{j}$$
Although the components are continuous functions, they are both equal to zero if $t = 0$, so $\mathbf{r}(t)$ is not a smooth function. The graph of $\mathbf{r}(t)$, which is shown in Figure 12.3.1, is a semicubical parabola traced in the upward direction (see Example 6 of Section 10.1). Observe that for values of $t$ slightly less than zero the angle between $\mathbf{r}'(t)$ and $\mathbf{i}$ is near $\pi$, and for values of $t$ slightly larger than zero the angle is near 0; hence there is a sudden reversal in the direction of the tangent vector as $t$ increases through $t = 0$ (see Exercise 44).

---

### ARC LENGTH FROM THE VECTOR VIEWPOINT

Recall from Theorem 10.1.1 that the arc length $L$ of a parametric curve
$$x = x(t), \quad y = y(t) \quad (a \le t \le b) \tag{1}$$
is given by the formula
$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt \tag{2}$$
Analogously, the arc length $L$ of a parametric curve
$$x = x(t), \quad y = y(t), \quad z = z(t) \quad (a \le t \le b) \tag{3}$$
in 3-space is given by the formula
$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}\,dt \tag{4}$$

Formulas (2) and (4) have vector forms that we can obtain by letting
$$\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} \quad \text{or} \quad \mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$$
It follows that
$$\frac{d\mathbf{r}}{dt} = \frac{dx}{dt}\mathbf{i} + \frac{dy}{dt}\mathbf{j} \quad \text{or} \quad \frac{d\mathbf{r}}{dt} = \frac{dx}{dt}\mathbf{i} + \frac{dy}{dt}\mathbf{j} + \frac{dz}{dt}\mathbf{k}$$
and hence
$$\left\|\frac{d\mathbf{r}}{dt}\right\| = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \quad \text{or} \quad \left\|\frac{d\mathbf{r}}{dt}\right\| = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}$$

Substituting these expressions in (2) and (4) leads us to the following theorem.

> **12.3.1 THEOREM**  
> If $C$ is the graph in 2-space or 3-space of a smooth vector-valued function $\mathbf{r}(t)$, then its arc length $L$ from $t = a$ to $t = b$ is
> $$L = \int_a^b \left\|\frac{d\mathbf{r}}{dt}\right\|\,dt \tag{5}$$

#### Example 2
Find the arc length of that portion of the circular helix $x = \cos t, \; y = \sin t, \; z = t$ from $t = 0$ to $t = \pi$.

**Solution.** Set $\mathbf{r}(t) = (\cos t)\mathbf{i} + (\sin t)\mathbf{j} + t\mathbf{k} = \langle \cos t, \sin t, t \rangle$. Then
$$\mathbf{r}'(t) = \langle -\sin t, \cos t, 1 \rangle \quad \text{and} \quad \|\mathbf{r}'(t)\| = \sqrt{(-\sin t)^2 + (\cos t)^2 + 1} = \sqrt{2}$$
From Theorem 12.3.1 the arc length of the helix is
$$L = \int_0^\pi \left\|\frac{d\mathbf{r}}{dt}\right\|\,dt = \int_0^\pi \sqrt{2}\,dt = \sqrt{2}\pi$$

---

### ARC LENGTH AS A PARAMETER

For many purposes the best parameter to use for representing a curve in 2-space or 3-space parametrically is the length of arc measured along the curve from some fixed reference point. This can be done as follows:

**Using Arc Length as a Parameter**
* **Step 1.** Select an arbitrary point on the curve $C$ to serve as a reference point.
* **Step 2.** Starting from the reference point, choose one direction along the curve to be the positive direction and the other to be the negative direction.
* **Step 3.** If $P$ is a point on the curve, let $s$ be the "signed" arc length along $C$ from the reference point to $P$, where $s$ is positive if $P$ is in the positive direction from the reference point and $s$ is negative if $P$ is in the negative direction (Figure 12.3.2).

By this procedure, a unique point $P$ on the curve is determined when a value for $s$ is given. For example, $s = 2$ determines the point that is 2 units along the curve in the positive direction from the reference point, and $s = -3/2$ determines the point that is $3/2$ units along the curve in the negative direction from the reference point.

Let us now treat $s$ as a variable. As the value of $s$ changes, the corresponding point $P$ moves along $C$ and the coordinates of $P$ become functions of $s$. Thus, in 2-space the coordinates of $P$ are $(x(s), y(s))$, and in 3-space they are $(x(s), y(s), z(s))$. Therefore, in 2-space or 3-space the curve $C$ is given by the parametric equations
$$x = x(s), \quad y = y(s) \quad \text{or} \quad x = x(s), \quad y = y(s), \quad z = z(s)$$
A parametric representation of a curve with arc length as the parameter is called an **arc length parametrization** of the curve.

#### Example 3
Find the arc length parametrization of the circle $x^2 + y^2 = a^2$ with counterclockwise orientation and $(a, 0)$ as the reference point.

**Solution.** The circle with counterclockwise orientation can be represented by the parametric equations
$$x = a\cos t, \quad y = a\sin t \quad (0 \le t \le 2\pi) \tag{6}$$
in which $t$ can be interpreted as the angle in radian measure from the positive $x$-axis to the radius from the origin to the point $P(x, y)$ (Figure 12.3.3). If we take the positive direction for measuring the arc length to be counterclockwise, and we take $(a, 0)$ to be the reference point, then $s$ and $t$ are related by
$$s = at \quad \text{or} \quad t = s/a$$
Making this change of variable in (6) and noting that $s$ increases from $0$ to $2\pi a$ as $t$ increases from $0$ to $2\pi$ yields the following arc length parametrization of the circle:
$$x = a\cos(s/a), \quad y = a\sin(s/a) \quad (0 \le s \le 2\pi a)$$

---

### CHANGE OF PARAMETER

In many situations the solution of a problem can be simplified by choosing the parameter in a vector-valued function or a parametric curve in the right way. The two most common parameters for curves in 2-space or 3-space are time and arc length. However, there are other useful possibilities as well (Figure 12.3.4).

A **change of parameter** in a vector-valued function $\mathbf{r}(t)$ is a substitution $t = g(\tau)$ that produces a new vector-valued function $\mathbf{r}(g(\tau))$ having the same graph as $\mathbf{r}(t)$, but possibly traced differently as the parameter $\tau$ increases.

#### Example 4
Find a change of parameter $t = g(\tau)$ for the circle
$$\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} \quad (0 \le t \le 2\pi)$$
such that  
(a) the circle is traced counterclockwise as $\tau$ increases over the interval $[0, 1]$;  
(b) the circle is traced clockwise as $\tau$ increases over the interval $[0, 1]$.

**Solution (a).** The given circle is traced counterclockwise as $t$ increases. Thus, if we choose $g$ to be an increasing function, then it will follow from the relationship $t = g(\tau)$ that $t$ increases when $\tau$ increases, thereby ensuring that the circle will be traced counterclockwise as $\tau$ increases. We also want to choose $g$ so that $t$ increases from $0$ to $2\pi$ as $\tau$ increases from $0$ to $1$. A simple choice of $g$ is the linear function graphed in Figure 12.3.5a:
$$t = g(\tau) = 2\pi\tau \tag{7}$$
The resulting representation of the circle in terms of the parameter $\tau$ is
$$\mathbf{r}(g(\tau)) = \cos 2\pi\tau\,\mathbf{i} + \sin 2\pi\tau\,\mathbf{j} \quad (0 \le \tau \le 1)$$

**Solution (b).** To ensure that the circle is traced clockwise, we will choose $g$ to be a decreasing function such that $t$ decreases from $2\pi$ to $0$ as $\tau$ increases from $0$ to $1$. A simple choice of $g$ is the linear function (Figure 12.3.5b):
$$t = g(\tau) = 2\pi(1 - \tau) \tag{8}$$
The resulting representation of the circle in terms of the parameter $\tau$ is
$$\mathbf{r}(g(\tau)) = \cos(2\pi(1 - \tau))\mathbf{i} + \sin(2\pi(1 - \tau))\mathbf{j} = \cos 2\pi\tau\,\mathbf{i} - \sin 2\pi\tau\,\mathbf{j} \quad (0 \le \tau \le 1)$$

---

### CHAIN RULE FOR VECTOR FUNCTIONS

> **12.3.2 THEOREM (Chain Rule)**  
> Let $\mathbf{r}(t)$ be a vector-valued function in 2-space or 3-space that is differentiable with respect to $t$. If $t = g(\tau)$ is a change of parameter in which $g$ is differentiable with respect to $\tau$, then $\mathbf{r}(g(\tau))$ is differentiable with respect to $\tau$ and
> $$\frac{d\mathbf{r}}{d\tau} = \frac{d\mathbf{r}}{dt}\frac{dt}{d\tau} \tag{9}$$

A change of parameter $t = g(\tau)$ in which $\mathbf{r}(g(\tau))$ is smooth if $\mathbf{r}(t)$ is smooth is called a **smooth change of parameter**. It follows from (9) that $t = g(\tau)$ will be a smooth change of parameter if $dt/d\tau$ is continuous and $dt/d\tau \neq 0$ for all values of $\tau$.
* **Positive changes of parameter:** $dt/d\tau > 0$ for all $\tau$ (preserves orientation).
* **Negative changes of parameter:** $dt/d\tau < 0$ for all $\tau$ (reverses orientation).

#### Example 5
In Example 4 the change of parameter in Formula (7) is positive since $dt/d\tau = 2\pi > 0$, and the change of parameter given by Formula (8) is negative since $dt/d\tau = -2\pi < 0$. The positive change of parameter preserved the orientation of the circle, and the negative change of parameter reversed it.

---

### FINDING ARC LENGTH PARAMETRIZATIONS

> **12.3.3 THEOREM**  
> Let $C$ be the graph of a smooth vector-valued function $\mathbf{r}(t)$ in 2-space or 3-space, and let $\mathbf{r}(t_0)$ be any point on $C$. Then the following formula defines a positive change of parameter from $t$ to $s$, where $s$ is an arc length parameter having $\mathbf{r}(t_0)$ as its reference point (Figure 12.3.6):
> $$s = \int_{t_0}^t \left\|\frac{d\mathbf{r}}{du}\right\|\,du \tag{10}$$

In component form:
$$s = \int_{t_0}^t \sqrt{\left(\frac{dx}{du}\right)^2 + \left(\frac{dy}{du}\right)^2}\,du \quad \text{2-space} \tag{11}$$
$$s = \int_{t_0}^t \sqrt{\left(\frac{dx}{du}\right)^2 + \left(\frac{dy}{du}\right)^2 + \left(\frac{dz}{du}\right)^2}\,du \quad \text{3-space} \tag{12}$$

#### Example 6
Find the arc length parametrization of the circular helix
$$\mathbf{r} = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + t\mathbf{k} \tag{13}$$
that has reference point $\mathbf{r}(0) = (1, 0, 0)$ and the same orientation as the given helix.

**Solution.** Taking $t_0 = 0$ in Formula (10):
$$\mathbf{r} = \cos u\,\mathbf{i} + \sin u\,\mathbf{j} + u\mathbf{k}, \quad \frac{d\mathbf{r}}{du} = (-\sin u)\mathbf{i} + \cos u\,\mathbf{j} + \mathbf{k}, \quad \left\|\frac{d\mathbf{r}}{du}\right\| = \sqrt{(-\sin u)^2 + \cos^2 u + 1} = \sqrt{2}$$
$$s = \int_0^t \left\|\frac{d\mathbf{r}}{du}\right\|\,du = \int_0^t \sqrt{2}\,du = [\sqrt{2}u]_0^t = \sqrt{2}t$$
Thus, $t = s/\sqrt{2}$, so (13) can be reparametrized in terms of $s$ as
$$\mathbf{r} = \cos\left(\frac{s}{\sqrt{2}}\right)\mathbf{i} + \sin\left(\frac{s}{\sqrt{2}}\right)\mathbf{j} + \frac{s}{\sqrt{2}}\mathbf{k}$$

#### Example 7
A bug walks along the trunk of a tree following a path modeled by the circular helix in Example 6. The bug starts at the reference point $(1, 0, 0)$ and walks up the helix for a distance of 10 units. What are the bug’s final coordinates?

**Solution.** Expressed parametrically, $x = \cos(s/\sqrt{2}), \; y = \sin(s/\sqrt{2}), \; z = s/\sqrt{2}$. At $s = 10$:
$$\left(\cos\left(\frac{10}{\sqrt{2}}\right), \sin\left(\frac{10}{\sqrt{2}}\right), \frac{10}{\sqrt{2}}\right) \approx (0.705, 0.709, 7.07)$$

#### Example 8
Recall from Formula (9) of Section 11.5 that the equation $\mathbf{r} = \mathbf{r}_0 + t\mathbf{v} \tag{14}$ is the vector form of the line that passes through the terminal point of $\mathbf{r}_0$ and is parallel to the vector $\mathbf{v}$. Find the arc length parametrization of the line that has reference point $\mathbf{r}_0$ and the same orientation as the given line.

**Solution.** Taking $t_0 = 0$ in (10), $s = \int_0^t \|\mathbf{v}\|\,du = \|\mathbf{v}\|t \implies t = s/\|\mathbf{v}\|$. Reparametrizing in terms of $s$:
$$\mathbf{r} = \mathbf{r}_0 + s\left(\frac{\mathbf{v}}{\|\mathbf{v}\|}\right) \tag{15}$$

#### Example 9
Find the arc length parametrization of the line $x = 2t + 1, \; y = 3t - 2$ that has the same orientation as the given line and uses $(1, -2)$ as the reference point.

**Solution.** The line passes through $(1, -2)$ and is parallel to $\mathbf{v} = 2\mathbf{i} + 3\mathbf{j}$. Since $\frac{\mathbf{v}}{\|\mathbf{v}\|} = \frac{2}{\sqrt{13}}\mathbf{i} + \frac{3}{\sqrt{13}}\mathbf{j}$, the parametric equations in terms of $s$ are
$$x = \frac{2}{\sqrt{13}}s + 1, \quad y = \frac{3}{\sqrt{13}}s - 2$$

---

### PROPERTIES OF ARC LENGTH PARAMETRIZATIONS

> **12.3.4 THEOREM**  
> (a) If $C$ is the graph of a smooth vector-valued function $\mathbf{r}(t)$ in 2-space or 3-space, where $t$ is a general parameter, and if $s$ is the arc length parameter for $C$ defined by Formula (10), then for every value of $t$ the tangent vector has length
> $$\left\|\frac{d\mathbf{r}}{dt}\right\| = \frac{ds}{dt} \tag{16}$$
> (b) If $C$ is the graph of a smooth vector-valued function $\mathbf{r}(s)$ in 2-space or 3-space, where $s$ is an arc length parameter, then for every value of $s$ the tangent vector to $C$ has length
> $$\left\|\frac{d\mathbf{r}}{ds}\right\| = 1 \tag{17}$$
> (c) If $C$ is the graph of a smooth vector-valued function $\mathbf{r}(t)$ in 2-space or 3-space, and if $\|d\mathbf{r}/dt\| = 1$ for every value of $t$, then for any value of $t_0$ in the domain of $\mathbf{r}$, the parameter $s = t - t_0$ is an arc length parameter that has its reference point at the point on $C$ where $t = t_0$.

**Component forms:**
$$\frac{ds}{dt} = \left\|\frac{d\mathbf{r}}{dt}\right\| = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \quad \text{2-space} \tag{18}$$
$$\frac{ds}{dt} = \left\|\frac{d\mathbf{r}}{dt}\right\| = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2} \quad \text{3-space} \tag{19}$$
$$\left\|\frac{d\mathbf{r}}{ds}\right\| = \sqrt{\left(\frac{dx}{ds}\right)^2 + \left(\frac{dy}{ds}\right)^2} = 1 \quad \text{2-space} \tag{20}$$
$$\left\|\frac{d\mathbf{r}}{ds}\right\| = \sqrt{\left(\frac{dx}{ds}\right)^2 + \left(\frac{dy}{ds}\right)^2 + \left(\frac{dz}{ds}\right)^2} = 1 \quad \text{3-space} \tag{21}$$

---

### QUICK CHECK EXERCISES 12.3
*(See page 868 for answers.)*

1. If $\mathbf{r}(t)$ is a smooth vector-valued function, then the integral $\int_a^b \|d\mathbf{r}/dt\|\,dt$ may be interpreted geometrically as the $\underline{\quad}$.
2. If $\mathbf{r}(s)$ is a smooth vector-valued function parametrized by arc length $s$, then $\|d\mathbf{r}/ds\| = \underline{\quad}$ and the arc length of the graph of $\mathbf{r}$ over the interval $a \le s \le b$ is $\underline{\quad}$.
3. If $\mathbf{r}(t)$ is a smooth vector-valued function, then the arc length parameter $s$ having $\mathbf{r}(t_0)$ as the reference point may be defined by the integral $s = \int_{t_0}^t \underline{\quad}\,du$.
4. Suppose that $\mathbf{r}(t)$ is a smooth vector-valued function of $t$ with $\mathbf{r}'(1) = \langle \sqrt{3}, -\sqrt{3}, -1 \rangle$, and let $\mathbf{r}_1(t)$ be defined by the equation $\mathbf{r}_1(t) = \mathbf{r}(2\cos t)$. Then $\mathbf{r}_1'(\pi/3) = \underline{\quad}$.

---

### EXERCISE SET 12.3

**1–4 Determine whether $\mathbf{r}(t)$ is a smooth function of the parameter $t$.**
1. $\mathbf{r}(t) = t^3\mathbf{i} + (3t^2 - 2t)\mathbf{j} + t^2\mathbf{k}$
2. $\mathbf{r}(t) = \cos t^2\mathbf{i} + \sin t^2\mathbf{j} + e^{-t}\mathbf{k}$
3. $\mathbf{r}(t) = te^{-t}\mathbf{i} + (t^2 - 2t)\mathbf{j} + \cos\pi t\,\mathbf{k}$
4. $\mathbf{r}(t) = \sin\pi t\,\mathbf{i} + (2t - \ln t)\mathbf{j} + (t^2 - t)\mathbf{k}$

**5–8 Find the arc length of the parametric curve.**
5. $x = \cos^3 t, \quad y = \sin^3 t, \quad z = 2; \quad 0 \le t \le \pi/2$
6. $x = 3\cos t, \quad y = 3\sin t, \quad z = 4t; \quad 0 \le t \le \pi$
7. $x = e^t, \quad y = e^{-t}, \quad z = \sqrt{2}t; \quad 0 \le t \le 1$
8. $x = \frac{1}{2}t, \quad y = \frac{1}{3}(1 - t)^{3/2}, \quad z = \frac{1}{3}(1 + t)^{3/2}; \quad -1 \le t \le 1$

**9–12 Find the arc length of the graph of $\mathbf{r}(t)$.**
9. $\mathbf{r}(t) = t^3\mathbf{i} + t\mathbf{j} + \frac{1}{2}\sqrt{6}t^2\mathbf{k}; \quad 1 \le t \le 3$
10. $\mathbf{r}(t) = (4 + 3t)\mathbf{i} + (2 - 2t)\mathbf{j} + (5 + t)\mathbf{k}; \quad 3 \le t \le 4$
11. $\mathbf{r}(t) = 3\cos t\,\mathbf{i} + 3\sin t\,\mathbf{j} + t\mathbf{k}; \quad 0 \le t \le 2\pi$
12. $\mathbf{r}(t) = t^2\mathbf{i} + (\cos t + t\sin t)\mathbf{j} + (\sin t - t\cos t)\mathbf{k}; \quad 0 \le t \le \pi$

**13–16 Calculate $d\mathbf{r}/d\tau$ by the chain rule, and then check your result by expressing $\mathbf{r}$ in terms of $\tau$ and differentiating.**
13. $\mathbf{r} = t\mathbf{i} + t^2\mathbf{j}; \quad t = 4\tau + 1$
14. $\mathbf{r} = \langle 3\cos t, 3\sin t \rangle; \quad t = \pi\tau$
15. $\mathbf{r} = e^t\mathbf{i} + 4e^{-t}\mathbf{j}; \quad t = \tau^2$
16. $\mathbf{r} = \mathbf{i} + 3t^{3/2}\mathbf{j} + t\mathbf{k}; \quad t = 1/\tau$

**17–20 True–False Determine whether the statement is true or false. Explain your answer.**
17. If $\mathbf{r}(t)$ is a smooth vector-valued function in 2-space, then $\int_a^b \|\mathbf{r}'(t)\|\,dt$ is a vector.
18. If the line $y = x$ is parametrized by the vector-valued function $\mathbf{r}(t)$, then $\mathbf{r}(t)$ is smooth.
19. If $\mathbf{r}(s)$ parametrizes the graph of $y = |x|$ in 2-space by arc length, then $\mathbf{r}(s)$ is smooth.
20. If a curve $C$ in the plane is parametrized by the smooth vector-valued function $\mathbf{r}(s)$, where $s$ is an arc length parameter, then $\int_{-1}^3 \|\mathbf{r}'(s)\|\,ds = 4$.

**21.**  
(a) Find the arc length parametrization of the line $x = t, \; y = t$ that has the same orientation as the given line and has reference point $(0, 0)$.  
(b) Find the arc length parametrization of the line $x = t, \; y = t, \; z = t$ that has the same orientation as the given line and has reference point $(0, 0, 0)$.

**22.** Find arc length parametrizations of the lines in Exercise 21 that have the stated reference points but are oriented opposite to the given lines.

**23.**  
(a) Find the arc length parametrization of the line $x = 1 + t, \; y = 3 - 2t, \; z = 4 + 2t$ that has the same direction as the given line and has reference point $(1, 3, 4)$.  
(b) Use the parametric equations obtained in part (a) to find the point on the line that is 25 units from the reference point in the direction of increasing parameter.

**24.**  
(a) Find the arc length parametrization of the line $x = -5 + 3t, \; y = 2t, \; z = 5 + t$ that has the same direction as the given line and has reference point $(-5, 0, 5)$.  
(b) Use the parametric equations obtained in part (a) to find the point on the line that is 10 units from the reference point in the direction of increasing parameter.

**25–30 Find an arc length parametrization of the curve that has the same orientation as the given curve and for which the reference point corresponds to $t = 0$.**
25. $\mathbf{r}(t) = (3 + \cos t)\mathbf{i} + (2 + \sin t)\mathbf{j}; \quad 0 \le t \le 2\pi$
26. $\mathbf{r}(t) = \cos^3 t\,\mathbf{i} + \sin^3 t\,\mathbf{j}; \quad 0 \le t \le \pi/2$
27. $\mathbf{r}(t) = \frac{1}{3}t^3\mathbf{i} + \frac{1}{2}t^2\mathbf{j}; \quad t \ge 0$
28. $\mathbf{r}(t) = (1 + t)^2\mathbf{i} + (1 + t)^3\mathbf{j}; \quad 0 \le t \le 1$
29. $\mathbf{r}(t) = e^t\cos t\,\mathbf{i} + e^t\sin t\,\mathbf{j}; \quad 0 \le t \le \pi/2$
30. $\mathbf{r}(t) = \sin e^t\,\mathbf{i} + \cos e^t\,\mathbf{j} + \sqrt{3}e^t\mathbf{k}; \quad t \ge 0$

**31.** Show that the arc length of the circular helix $x = a\cos t, \; y = a\sin t, \; z = ct$ for $0 \le t \le t_0$ is $t_0\sqrt{a^2 + c^2}$.

**32.** Use the result in Exercise 31 to show the circular helix $\mathbf{r} = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} + ct\mathbf{k}$ can be expressed as
$$\mathbf{r} = \left(a\cos\frac{s}{w}\right)\mathbf{i} + \left(a\sin\frac{s}{w}\right)\mathbf{j} + \frac{cs}{w}\mathbf{k}$$
where $w = \sqrt{a^2 + c^2}$ and $s$ is an arc length parameter with reference point at $(a, 0, 0)$.

**33.** Find an arc length parametrization of the cycloid
$$x = at - a\sin t, \quad y = a - a\cos t \quad (0 \le t \le 2\pi)$$
with $(0, 0)$ as the reference point.

**34.** Show that in cylindrical coordinates a curve given by the parametric equations $r = r(t), \; \theta = \theta(t), \; z = z(t)$ for $a \le t \le b$ has arc length
$$L = \int_a^b \sqrt{\left(\frac{dr}{dt}\right)^2 + r^2\left(\frac{d\theta}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}\,dt$$
[*Hint:* Use the relationships $x = r\cos\theta, \; y = r\sin\theta$.]

**35.** In each part, use the formula in Exercise 34 to find the arc length of the curve.  
(a) $r = e^{2t}, \; \theta = t, \; z = e^{2t}; \quad 0 \le t \le \ln 2$  
(b) $r = t^2, \; \theta = \ln t, \; z = \frac{1}{3}t^3; \quad 1 \le t \le 2$

**36.** Show that in spherical coordinates a curve given by the parametric equations $\rho = \rho(t), \; \theta = \theta(t), \; \phi = \phi(t)$ for $a \le t \le b$ has arc length
$$L = \int_a^b \sqrt{\left(\frac{d\rho}{dt}\right)^2 + \rho^2\sin^2\phi\left(\frac{d\theta}{dt}\right)^2 + \rho^2\left(\frac{d\phi}{dt}\right)^2}\,dt$$
[*Hint:* $x = \rho\sin\phi\cos\theta, \; y = \rho\sin\phi\sin\theta, \; z = \rho\cos\phi$.]

**37.** In each part, use the formula in Exercise 36 to find the arc length of the curve.  
(a) $\rho = e^{-t}, \; \theta = 2t, \; \phi = \pi/4; \quad 0 \le t \le 2$  
(b) $\rho = 2t, \; \theta = \ln t, \; \phi = \pi/6; \quad 1 \le t \le 5$

#### FOCUS ON CONCEPTS
**38.**  
(a) Sketch the graph of $\mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j}$. Show that $\mathbf{r}(t)$ is a smooth vector-valued function but the change of parameter $t = \tau^3$ produces a vector-valued function that is not smooth, yet has the same graph as $\mathbf{r}(t)$.  
(b) Examine how the two vector-valued functions are traced, and see if you can explain what causes the problem.

**39.** Find a change of parameter $t = g(\tau)$ for the semicircle $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} \; (0 \le t \le \pi)$ such that  
(a) the semicircle is traced counterclockwise as $\tau$ varies over the interval $[0, 1]$  
(b) the semicircle is traced clockwise as $\tau$ varies over the interval $[0, 1]$.

**40.** What change of parameter $t = g(\tau)$ would you make if you wanted to trace the graph of $\mathbf{r}(t) \; (0 \le t \le 1)$ in the opposite direction with $\tau$ varying from 0 to 1?

**41.** As illustrated in Figure Ex-41, copper cable with a diameter of $\frac{1}{2}$ inch is to be wrapped in a circular helix around a cylinder that has a 12-inch diameter. What length of cable (measured along its centerline) will make one complete turn around the cylinder in a distance of 20 inches (between centerlines) measured parallel to the axis of the cylinder?

**42.** Let $\mathbf{r}(t) = \langle \cos t, \sin t, t^{3/2} \rangle$. Find:  
(a) $\|\mathbf{r}'(t)\|$ (b) $\frac{ds}{dt}$ (c) $\int_0^2 \|\mathbf{r}'(t)\|\,dt$.

**43.** Let $\mathbf{r}(t) = \ln t\,\mathbf{i} + 2t\mathbf{j} + t^2\mathbf{k}$. Find:  
(a) $\|\mathbf{r}'(t)\|$ (b) $\frac{ds}{dt}$ (c) $\int_1^3 \|\mathbf{r}'(t)\|\,dt$.

**44.** Let $\mathbf{r}(t) = t^2\mathbf{i} + t^3\mathbf{j}$ (see Figure 12.3.1). Let $\theta(t)$ be the angle between $\mathbf{r}'(t)$ and $\mathbf{i}$. Show that
$$\theta(t) \to \pi \quad \text{as } t \to 0^- \quad \text{and} \quad \theta(t) \to 0 \quad \text{as } t \to 0^+$$

**45.** Prove: If $\mathbf{r}(t)$ is a smoothly parametrized function, then the angles between $\mathbf{r}'(t)$ and the vectors $\mathbf{i}, \mathbf{j},$ and $\mathbf{k}$ are continuous functions of $t$.

**46.** Prove the vector form of the chain rule for 2-space (Theorem 12.3.2) by expressing $\mathbf{r}(t)$ in terms of components.

**47. Writing** The triangle with vertices $(0, 0), (1, 0),$ and $(0, 1)$ has three "corners." Discuss whether it is possible to have a smooth vector-valued function whose graph is this triangle. Also discuss whether it is possible to have a differentiable vector-valued function whose graph is this triangle.

#### QUICK CHECK ANSWERS 12.3
1. arc length of the graph of $\mathbf{r}(t)$ from $t = a$ to $t = b$  
2. $1; \; b - a$  
3. $\left\|\frac{d\mathbf{r}}{du}\right\|$  
4. $\langle -3, 3, \sqrt{3} \rangle$

---

## 12.4 UNIT TANGENT, NORMAL, AND BINORMAL VECTORS

In this section we will discuss some of the fundamental geometric properties of vector-valued functions. Our work here will have important applications to the study of motion along a curved path in 2-space or 3-space and to the study of the geometric properties of curves and surfaces.

### UNIT TANGENT VECTORS

Recall that if $C$ is the graph of a smooth vector-valued function $\mathbf{r}(t)$ in 2-space or 3-space, then the vector $\mathbf{r}'(t)$ is nonzero, tangent to $C$, and points in the direction of increasing parameter. Thus, by normalizing $\mathbf{r}'(t)$ we obtain a unit vector
$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|} \tag{1}$$
that is tangent to $C$ and points in the direction of increasing parameter. We call $\mathbf{T}(t)$ the **unit tangent vector** to $C$ at $t$.

> *As a general rule, we will position $\mathbf{T}(t)$ with its initial point at the terminal point of $\mathbf{r}(t)$, as in Figure 12.4.1. This will ensure that $\mathbf{T}(t)$ is actually tangent to the graph of $\mathbf{r}(t)$ and not simply parallel to the tangent line.*

#### Example 1
Find the unit tangent vector to the graph of $\mathbf{r}(t) = t^2\mathbf{i} + t^3\mathbf{j}$ at the point where $t = 2$.

**Solution.** Since $\mathbf{r}'(t) = 2t\mathbf{i} + 3t^2\mathbf{j}$, we obtain
$$\mathbf{T}(2) = \frac{\mathbf{r}'(2)}{\|\mathbf{r}'(2)\|} = \frac{4\mathbf{i} + 12\mathbf{j}}{\sqrt{160}} = \frac{4\mathbf{i} + 12\mathbf{j}}{4\sqrt{10}} = \frac{1}{\sqrt{10}}\mathbf{i} + \frac{3}{\sqrt{10}}\mathbf{j}$$
The graph of $\mathbf{r}(t)$ and the vector $\mathbf{T}(2)$ are shown in Figure 12.4.2.

---

### UNIT NORMAL VECTORS

Recall from Theorem 12.2.8 that if a vector-valued function $\mathbf{r}(t)$ has constant norm, then $\mathbf{r}(t)$ and $\mathbf{r}'(t)$ are orthogonal vectors. In particular, $\mathbf{T}(t)$ has constant norm 1, so $\mathbf{T}(t)$ and $\mathbf{T}'(t)$ are orthogonal vectors. This implies that $\mathbf{T}'(t)$ is perpendicular to the tangent line to $C$ at $t$, so we say that $\mathbf{T}'(t)$ is normal to $C$ at $t$. It follows that if $\mathbf{T}'(t) \neq \mathbf{0}$, and if we normalize $\mathbf{T}'(t)$, then we obtain a unit vector
$$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|} \tag{2}$$
that is normal to $C$ and points in the same direction as $\mathbf{T}'(t)$. We call $\mathbf{N}(t)$ the **principal unit normal vector** to $C$ at $t$, or more simply, the **unit normal vector**. Observe that the unit normal vector is defined only at points where $\mathbf{T}'(t) \neq \mathbf{0}$. Unless stated otherwise, we will assume that this condition is satisfied. In particular, this excludes straight lines.

**REMARK.** In 2-space there are two unit vectors that are orthogonal to $\mathbf{T}(t)$, and in 3-space there are infinitely many such vectors (Figure 12.4.3). In both cases the principal unit normal is that particular normal that points in the direction of $\mathbf{T}'(t)$.

#### Example 2
Find $\mathbf{T}(t)$ and $\mathbf{N}(t)$ for the circular helix
$$x = a\cos t, \quad y = a\sin t, \quad z = ct \quad (a > 0)$$

**Solution.** The radius vector for the helix is $\mathbf{r}(t) = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} + ct\mathbf{k}$ (Figure 12.4.4). Thus,
$$\mathbf{r}'(t) = (-a\sin t)\mathbf{i} + a\cos t\,\mathbf{j} + c\mathbf{k}$$
$$\|\mathbf{r}'(t)\| = \sqrt{(-a\sin t)^2 + (a\cos t)^2 + c^2} = \sqrt{a^2 + c^2}$$
$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|} = -\frac{a\sin t}{\sqrt{a^2 + c^2}}\mathbf{i} + \frac{a\cos t}{\sqrt{a^2 + c^2}}\mathbf{j} + \frac{c}{\sqrt{a^2 + c^2}}\mathbf{k}$$
$$\mathbf{T}'(t) = -\frac{a\cos t}{\sqrt{a^2 + c^2}}\mathbf{i} - \frac{a\sin t}{\sqrt{a^2 + c^2}}\mathbf{j}$$
$$\|\mathbf{T}'(t)\| = \sqrt{\left(-\frac{a\cos t}{\sqrt{a^2 + c^2}}\right)^2 + \left(-\frac{a\sin t}{\sqrt{a^2 + c^2}}\right)^2} = \frac{a}{\sqrt{a^2 + c^2}}$$
$$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|} = (-\cos t)\mathbf{i} - (\sin t)\mathbf{j} = -(\cos t\,\mathbf{i} + \sin t\,\mathbf{j})$$
Note that the $\mathbf{k}$ component of the principal unit normal $\mathbf{N}(t)$ is zero for every value of $t$, so this vector always lies in a horizontal plane, pointing directly toward the $z$-axis (Figure 12.4.5).

---

### INWARD UNIT NORMAL VECTORS IN 2-SPACE

For a nonlinear parametric curve $C$ in 2-space, the unit normal vector always points toward the concave side of $C$. Let $\phi(t)$ be the angle from the positive $x$-axis to $\mathbf{T}(t)$, and let $\mathbf{n}(t)$ be the unit vector that results when $\mathbf{T}(t)$ is rotated counterclockwise through an angle of $\pi/2$ (Figure 12.4.6):
$$\mathbf{T}(t) = \cos\phi(t)\mathbf{i} + \sin\phi(t)\mathbf{j} \tag{3}$$
$$\mathbf{n}(t) = -\sin\phi(t)\mathbf{i} + \cos\phi(t)\mathbf{j} \tag{4}$$
Differentiating $\mathbf{T}(t)$ with respect to $t$ gives:
$$\frac{d\mathbf{T}}{dt} = \mathbf{n}(t)\frac{d\phi}{dt} \tag{5}$$
Since $d\phi/dt > 0$ when $\phi$ increases (turning left) and $d\phi/dt < 0$ when $\phi$ decreases (turning right), $\mathbf{T}'(t) = d\mathbf{T}/dt$ points "inward" toward the concave side of the curve in all cases, and hence so does $\mathbf{N}(t)$. For this reason, $\mathbf{N}(t)$ is also called the **inward unit normal** when applied to curves in 2-space.

---

### COMPUTING T AND N FOR CURVES PARAMETRIZED BY ARC LENGTH

When $\mathbf{r}(s)$ is parametrized by arc length, $\|\mathbf{r}'(s)\| = 1$. Thus:
$$\mathbf{T}(s) = \mathbf{r}'(s) \tag{6}$$
$$\mathbf{N}(s) = \frac{\mathbf{r}''(s)}{\|\mathbf{r}''(s)\|} \tag{7}$$

#### Example 3
The circle of radius $a$ with counterclockwise orientation and centered at the origin can be represented by $\mathbf{r} = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} \; (0 \le t \le 2\pi) \tag{8}$. Parametrize this circle by arc length and find $\mathbf{T}(s)$ and $\mathbf{N}(s)$.

**Solution.** Substituting $t = s/a$ into (8) gives $\mathbf{r}(s) = a\cos(s/a)\mathbf{i} + a\sin(s/a)\mathbf{j} \; (0 \le s \le 2\pi a)$.  
$$\mathbf{r}'(s) = -\sin(s/a)\mathbf{i} + \cos(s/a)\mathbf{j}$$
$$\mathbf{r}''(s) = -(1/a)\cos(s/a)\mathbf{i} - (1/a)\sin(s/a)\mathbf{j}$$
$$\|\mathbf{r}''(s)\| = 1/a$$
$$\mathbf{T}(s) = \mathbf{r}'(s) = -\sin(s/a)\mathbf{i} + \cos(s/a)\mathbf{j}$$
$$\mathbf{N}(s) = \frac{\mathbf{r}''(s)}{\|\mathbf{r}''(s)\|} = -\cos(s/a)\mathbf{i} - \sin(s/a)\mathbf{j}$$
so $\mathbf{N}(s)$ points toward the center of the circle for all $s$ (Figure 12.4.9).

---

### BINORMAL VECTORS IN 3-SPACE

If $C$ is the graph of a vector-valued function $\mathbf{r}(t)$ in 3-space, then we define the **binormal vector** to $C$ at $t$ to be
$$\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t) \tag{9}$$
$\{\mathbf{T}(t), \mathbf{N}(t), \mathbf{B}(t)\}$ forms a right-handed triad of mutually orthogonal unit vectors:
$$\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t), \quad \mathbf{N}(t) = \mathbf{B}(t) \times \mathbf{T}(t), \quad \mathbf{T}(t) = \mathbf{N}(t) \times \mathbf{B}(t) \tag{10}$$

At each point on a smooth curve $C$ in 3-space, these vectors determine three mutually perpendicular planes (Figure 12.4.10):
* **Osculating plane:** The $TN$-plane (normal vector is $\mathbf{B}$).
* **Normal plane:** The $NB$-plane (normal vector is $\mathbf{T}$).
* **Rectifying plane:** The $TB$-plane (normal vector is $\mathbf{N}$).

The coordinate system determined by $\mathbf{T}(t), \mathbf{N}(t),$ and $\mathbf{B}(t)$ is called the **TNB-frame** or the **Frenet frame** (Figure 12.4.12).

Direct formulas in terms of $\mathbf{r}(t)$ and $\mathbf{r}(s)$:
$$\mathbf{B}(t) = \frac{\mathbf{r}'(t) \times \mathbf{r}''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|} \tag{11}$$
$$\mathbf{B}(s) = \frac{\mathbf{r}'(s) \times \mathbf{r}''(s)}{\|\mathbf{r}''(s)\|} \tag{12}$$

---

### QUICK CHECK EXERCISES 12.4
*(See page 873 for answers.)*

1. If $C$ is the graph of a smooth vector-valued function $\mathbf{r}(t)$, then the unit tangent, unit normal, and binormal to $C$ at $t$ are defined, respectively, by $\mathbf{T}(t) = \underline{\quad}, \; \mathbf{N}(t) = \underline{\quad}, \; \mathbf{B}(t) = \underline{\quad}$.
2. If $C$ is the graph of a smooth vector-valued function $\mathbf{r}(s)$ parametrized by arc length, then the definitions of the unit tangent and unit normal to $C$ at $s$ simplify, respectively, to $\mathbf{T}(s) = \underline{\quad}$ and $\mathbf{N}(s) = \underline{\quad}$.
3. If $C$ is the graph of a smooth vector-valued function $\mathbf{r}(t)$, then the unit binormal vector to $C$ at $t$ may be computed directly in terms of $\mathbf{r}'(t)$ and $\mathbf{r}''(t)$ by the formula $\mathbf{B}(t) = \underline{\quad}$. When $t = s$ is the arc length parameter, this formula simplifies to $\mathbf{B}(s) = \underline{\quad}$.
4. Suppose that $C$ is the graph of a smooth vector-valued function $\mathbf{r}(s)$ parametrized by arc length with $\mathbf{r}'(0) = \langle 2/3, 1/3, 2/3 \rangle$ and $\mathbf{r}''(0) = \langle -3, 12, -3 \rangle$. Then $\mathbf{T}(0) = \underline{\quad}, \; \mathbf{N}(0) = \underline{\quad}, \; \mathbf{B}(0) = \underline{\quad}$.

---

### EXERCISE SET 12.4

#### FOCUS ON CONCEPTS
**1.** In each part, sketch the unit tangent and normal vectors at the points $P, Q,$ and $R$, taking into account the orientation of the curve $C$.  
(a) Figure Ex-1a  
(b) Figure Ex-1b

**2.** Make a rough sketch that shows the ellipse $\mathbf{r}(t) = 3\cos t\,\mathbf{i} + 2\sin t\,\mathbf{j}$ for $0 \le t \le 2\pi$ and the unit tangent and normal vectors at the points $t = 0, \; t = \pi/4, \; t = \pi/2,$ and $t = \pi$.

**3.** In the marginal note associated with Example 8 of Section 12.3, we observed that a line $\mathbf{r} = \mathbf{r}_0 + t\mathbf{v}$ can be parametrized in terms of an arc length parameter $s$ with reference point $\mathbf{r}_0$ by normalizing $\mathbf{v}$. Use this result to show that the tangent line to the graph of $\mathbf{r}(t)$ at the point $t_0$ can be expressed as $\mathbf{r} = \mathbf{r}(t_0) + s\mathbf{T}(t_0)$, where $s$ is an arc length parameter with reference point $\mathbf{r}(t_0)$.

**4.** Use the result in Exercise 3 to show that the tangent line to the parabola $x = t, \; y = t^2$ at the point $(1, 1)$ can be expressed parametrically as $x = 1 + \frac{s}{\sqrt{5}}, \quad y = 1 + \frac{2s}{\sqrt{5}}$.

**5–12 Find $\mathbf{T}(t)$ and $\mathbf{N}(t)$ at the given point.**
5. $\mathbf{r}(t) = (t^2 - 1)\mathbf{i} + t\mathbf{j}; \quad t = 1$
6. $\mathbf{r}(t) = \frac{1}{2}t^2\mathbf{i} + \frac{1}{3}t^3\mathbf{j}; \quad t = 1$
7. $\mathbf{r}(t) = 5\cos t\,\mathbf{i} + 5\sin t\,\mathbf{j}; \quad t = \pi/3$
8. $\mathbf{r}(t) = \ln t\,\mathbf{i} + t\mathbf{j}; \quad t = e$
9. $\mathbf{r}(t) = 4\cos t\,\mathbf{i} + 4\sin t\,\mathbf{j} + t\mathbf{k}; \quad t = \pi/2$
10. $\mathbf{r}(t) = t\mathbf{i} + \frac{1}{2}t^2\mathbf{j} + \frac{1}{3}t^3\mathbf{k}; \quad t = 0$
11. $x = e^t\cos t, \quad y = e^t\sin t, \quad z = e^t; \quad t = 0$
12. $x = \cosh t, \quad y = \sinh t, \quad z = t; \quad t = \ln 2$

**13–14 Use the result in Exercise 3 to find parametric equations for the tangent line to the graph of $\mathbf{r}(t)$ at $t_0$ in terms of an arc length parameter $s$.**
13. $\mathbf{r}(t) = \sin t\,\mathbf{i} + \cos t\,\mathbf{j} + \frac{1}{2}t^2\mathbf{k}; \quad t_0 = 0$
14. $\mathbf{r}(t) = t\mathbf{i} + t\mathbf{j} + \sqrt{9 - t^2}\mathbf{k}; \quad t_0 = 1$

**15–18 Use the formula $\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)$ to find $\mathbf{B}(t)$, and then check your answer by using Formula (11) to find $\mathbf{B}(t)$ directly from $\mathbf{r}(t)$.**
15. $\mathbf{r}(t) = 3\sin t\,\mathbf{i} + 3\cos t\,\mathbf{j} + 4t\mathbf{k}$
16. $\mathbf{r}(t) = e^t\sin t\,\mathbf{i} + e^t\cos t\,\mathbf{j} + 3\mathbf{k}$
17. $\mathbf{r}(t) = (\sin t - t\cos t)\mathbf{i} + (\cos t + t\sin t)\mathbf{j} + \mathbf{k}$
18. $\mathbf{r}(t) = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} + ct\mathbf{k} \quad (a \neq 0, c \neq 0)$

**19–20 Find $\mathbf{T}(t), \mathbf{N}(t),$ and $\mathbf{B}(t)$ for the given value of $t$. Then find equations for the osculating, normal, and rectifying planes at the point that corresponds to that value of $t$.**
19. $\mathbf{r}(t) = \cos t\,\mathbf{i} + \sin t\,\mathbf{j} + \mathbf{k}; \quad t = \pi/4$
20. $\mathbf{r}(t) = e^t\mathbf{i} + e^t\cos t\,\mathbf{j} + e^t\sin t\,\mathbf{k}; \quad t = 0$

**21–24 True–False Determine whether the statement is true or false. Explain your answer.**
21. If $C$ is the graph of a smooth vector-valued function $\mathbf{r}(t)$ in 2-space, then the unit tangent vector $\mathbf{T}(t)$ to $C$ is orthogonal to $\mathbf{r}(t)$ and points in the direction of increasing parameter.
22. If $C$ is the graph of a smooth vector-valued function $\mathbf{r}(t)$ in 2-space, then the angle measured in the counterclockwise direction from the unit tangent vector $\mathbf{T}(t)$ to the unit normal vector $\mathbf{N}(t)$ is $\pi/2$.
23. If the smooth vector-valued function $\mathbf{r}(s)$ is parametrized by arc length and $\mathbf{r}''(s)$ is defined, then $\mathbf{r}'(s)$ and $\mathbf{r}''(s)$ are orthogonal vectors.
24. The binormal vector $\mathbf{B}(t)$ to the graph of a vector-valued function $\mathbf{r}(t)$ in 3-space is the dot product of unit tangent and unit normal vectors, $\mathbf{T}(t)$ and $\mathbf{N}(t)$.

**25. Writing** Look up the definition of "osculating" in a dictionary and discuss why "osculating plane" is an appropriate term for the $TN$-plane.

**26. Writing** Discuss some of the advantages of parametrizing a curve by arc length.

#### QUICK CHECK ANSWERS 12.4
1. $\frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}; \; \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}; \; \mathbf{T}(t) \times \mathbf{N}(t)$  
2. $\mathbf{r}'(s); \; \frac{\mathbf{r}''(s)}{\|\mathbf{r}''(s)\|}$  
3. $\frac{\mathbf{r}'(t) \times \mathbf{r}''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}; \; \frac{\mathbf{r}'(s) \times \mathbf{r}''(s)}{\|\mathbf{r}''(s)\|}$  
4. $\left\langle \frac{2}{3}, \frac{1}{3}, \frac{2}{3} \right\rangle; \; \left\langle -\frac{1}{3\sqrt{2}}, \frac{4}{3\sqrt{2}}, -\frac{1}{3\sqrt{2}} \right\rangle; \; \left\langle -\frac{1}{\sqrt{2}}, 0, \frac{1}{\sqrt{2}} \right\rangle$

---

## 12.5 CURVATURE

In this section we will consider the problem of obtaining a numerical measure of how sharply a curve in 2-space or 3-space bends. Our results will have applications in geometry and in the study of motion along a curved path.

### DEFINITION OF CURVATURE

Suppose that $C$ is the graph of a smooth vector-valued function in 2-space or 3-space that is parametrized in terms of arc length. The "sharpness" of the bend in $C$ is closely related to $d\mathbf{T}/ds$, which is the rate of change of the unit tangent vector $\mathbf{T}$ with respect to $s$ (Figure 12.5.1).

> **12.5.1 DEFINITION**  
> If $C$ is a smooth curve in 2-space or 3-space that is parametrized by arc length, then the **curvature** of $C$, denoted by $\kappa = \kappa(s)$ ($\kappa = \text{Greek "kappa"}$), is defined by
> $$\kappa(s) = \left\|\frac{d\mathbf{T}}{ds}\right\| = \|\mathbf{r}''(s)\| \tag{1}$$

#### Example 1
In Example 3 of Section 12.4 we showed that the circle of radius $a$, centered at the origin, can be parametrized in terms of arc length as $\mathbf{r}(s) = a\cos(s/a)\mathbf{i} + a\sin(s/a)\mathbf{j} \; (0 \le s \le 2\pi a)$. Thus,
$$\mathbf{r}''(s) = -\frac{1}{a}\cos\left(\frac{s}{a}\right)\mathbf{i} - \frac{1}{a}\sin\left(\frac{s}{a}\right)\mathbf{j}$$
and hence from (1)
$$\kappa(s) = \|\mathbf{r}''(s)\| = \sqrt{\left[-\frac{1}{a}\cos\left(\frac{s}{a}\right)\right]^2 + \left[-\frac{1}{a}\sin\left(\frac{s}{a}\right)\right]^2} = \frac{1}{a}$$
so the circle has constant curvature $1/a$.

#### Example 2
A line parametrized by arc length is $\mathbf{r} = \mathbf{r}_0 + s\mathbf{u}$, where $\mathbf{u}$ is a unit vector. Thus $\mathbf{r}'(s) = \mathbf{u}$ and $\mathbf{r}''(s) = \mathbf{0}$, so $\kappa(s) = \|\mathbf{r}''(s)\| = 0$.

---

### FORMULAS FOR CURVATURE

> **12.5.2 THEOREM**  
> If $\mathbf{r}(t)$ is a smooth vector-valued function in 2-space or 3-space, then for each value of $t$ at which $\mathbf{T}'(t)$ and $\mathbf{r}''(t)$ exist, the curvature $\kappa$ can be expressed as
> (a) $\kappa(t) = \frac{\|\mathbf{T}'(t)\|}{\|\mathbf{r}'(t)\|} \tag{2}$  
> (b) $\kappa(t) = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3} \tag{3}$

**Proof (a).** It follows from Formula (1) and Formula (16) of Section 12.3 that
$$\kappa(t) = \left\|\frac{d\mathbf{T}}{ds}\right\| = \left\|\frac{d\mathbf{T}/dt}{ds/dt}\right\| = \frac{\|\mathbf{T}'(t)\|}{\|\mathbf{r}'(t)\|}$$

**Proof (b).** From Formula (1) of Section 12.4, $\mathbf{r}'(t) = \|\mathbf{r}'(t)\|\mathbf{T}(t) \tag{4}$. Differentiating yields
$$\mathbf{r}''(t) = \|\mathbf{r}'(t)\|'\mathbf{T}(t) + \|\mathbf{r}'(t)\|\mathbf{T}'(t) \tag{5}$$
Since $\mathbf{T}'(t) = \|\mathbf{T}'(t)\|\mathbf{N}(t) = \kappa(t)\|\mathbf{r}'(t)\|\mathbf{N}(t)$, substituting gives
$$\mathbf{r}''(t) = \|\mathbf{r}'(t)\|'\mathbf{T}(t) + \kappa(t)\|\mathbf{r}'(t)\|^2\mathbf{N}(t) \tag{6}$$
Thus, taking the cross product of (4) and (6):
$$\mathbf{r}'(t) \times \mathbf{r}''(t) = \|\mathbf{r}'(t)\|\|\mathbf{r}'(t)\|'(\mathbf{T}(t) \times \mathbf{T}(t)) + \kappa(t)\|\mathbf{r}'(t)\|^3(\mathbf{T}(t) \times \mathbf{N}(t)) = \kappa(t)\|\mathbf{r}'(t)\|^3\mathbf{B}(t)$$
Taking norms of both sides yields $\|\mathbf{r}'(t) \times \mathbf{r}''(t)\| = \kappa(t)\|\mathbf{r}'(t)\|^3$, from which (3) follows. $\blacksquare$

#### Example 3
Find $\kappa(t)$ for the circular helix $x = a\cos t, \; y = a\sin t, \; z = ct \quad (a > 0)$.

**Solution.** $\mathbf{r}(t) = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} + ct\mathbf{k}$.
$$\mathbf{r}'(t) = (-a\sin t)\mathbf{i} + (a\cos t)\mathbf{j} + c\mathbf{k}$$
$$\mathbf{r}''(t) = (-a\cos t)\mathbf{i} + (-a\sin t)\mathbf{j}$$
$$\mathbf{r}'(t) \times \mathbf{r}''(t) = (ac\sin t)\mathbf{i} - (ac\cos t)\mathbf{j} + a^2\mathbf{k}$$
$$\|\mathbf{r}'(t)\| = \sqrt{a^2 + c^2}, \quad \|\mathbf{r}'(t) \times \mathbf{r}''(t)\| = a\sqrt{a^2 + c^2}$$
$$\kappa(t) = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3} = \frac{a\sqrt{a^2 + c^2}}{(\sqrt{a^2 + c^2})^3} = \frac{a}{a^2 + c^2}$$

#### Example 4
The graph of the vector equation $\mathbf{r} = 2\cos t\,\mathbf{i} + 3\sin t\,\mathbf{j} \; (0 \le t \le 2\pi)$ is an ellipse (Figure 12.5.2). Find the curvature at the endpoints of the major and minor axes.

**Solution.** Treating the ellipse in 3-space with zero $\mathbf{k}$ component:
$$\mathbf{r}'(t) \times \mathbf{r}''(t) = 6\mathbf{k}, \quad \|\mathbf{r}'(t) \times \mathbf{r}''(t)\| = 6, \quad \|\mathbf{r}'(t)\| = \sqrt{4\sin^2 t + 9\cos^2 t}$$
$$\kappa(t) = \frac{6}{[4\sin^2 t + 9\cos^2 t]^{3/2}} \tag{7}$$
* Minor axis endpoints $(2, 0)$ and $(-2, 0)$ correspond to $t = 0$ and $t = \pi$: $\kappa(0) = \kappa(\pi) = \frac{6}{9^{3/2}} = \frac{6}{27} = \frac{2}{9}$.
* Major axis endpoints $(0, 3)$ and $(0, -3)$ correspond to $t = \pi/2$ and $t = 3\pi/2$: $\kappa(\pi/2) = \kappa(3\pi/2) = \frac{6}{4^{3/2}} = \frac{6}{8} = \frac{3}{4}$.

---

### RADIUS OF CURVATURE & OSCULATING CIRCLE

* **Radius of curvature:** $\rho = \frac{1}{\kappa}$
* **Osculating circle (or circle of curvature):** The circle of radius $\rho = 1/\kappa$ sharing a common tangent with $C$ at $P$, and centered on the concave side of the curve at the **center of curvature** (Figure 12.5.6).

---

### AN INTERPRETATION OF CURVATURE IN 2-SPACE

For a plane curve with angle of inclination $\phi$:
$$\kappa(s) = \left|\frac{d\phi}{ds}\right| \tag{8}$$
Curvature is the magnitude of the rate of change of the direction angle $\phi$ with respect to arc length $s$.

---

### FORMULA SUMMARY

$$\mathbf{T}(s) = \mathbf{r}'(s) \tag{9}$$
$$\mathbf{N}(s) = \frac{1}{\kappa(s)}\frac{d\mathbf{T}}{ds} = \frac{\mathbf{r}''(s)}{\|\mathbf{r}''(s)\|} = \frac{\mathbf{r}''(s)}{\kappa(s)} \tag{10}$$
$$\mathbf{B}(s) = \frac{\mathbf{r}'(s) \times \mathbf{r}''(s)}{\|\mathbf{r}''(s)\|} = \frac{\mathbf{r}'(s) \times \mathbf{r}''(s)}{\kappa(s)} \tag{11}$$
$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|} \tag{12}$$
$$\mathbf{B}(t) = \frac{\mathbf{r}'(t) \times \mathbf{r}''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|} \tag{13}$$
$$\mathbf{N}(t) = \mathbf{B}(t) \times \mathbf{T}(t) \tag{14}$$

---

### QUICK CHECK EXERCISES 12.5
*(See page 881 for answers.)*

1. If $C$ is a smooth curve parametrized by arc length, then the curvature is defined by $\kappa(s) = \underline{\quad}$.
2. Let $\mathbf{r}(t)$ be a smooth vector-valued function with curvature $\kappa(t)$.  
   (a) $\kappa(t) = \underline{\quad}$ in terms of $\mathbf{T}'(t)$ and $\mathbf{r}'(t)$.  
   (b) $\kappa(t) = \underline{\quad}$ directly in terms of $\mathbf{r}'(t)$ and $\mathbf{r}''(t)$.
3. Suppose that $C$ is the graph of a smooth vector-valued function $\mathbf{r}(s) = \langle x(s), y(s) \rangle$ parametrized by arc length and that the unit tangent $\mathbf{T}(s) = \langle \cos\phi(s), \sin\phi(s) \rangle$. Then $\kappa(s) = \underline{\quad}$.
4. Suppose that $C$ is a smooth curve and that $x^2 + y^2 = 4$ is the osculating circle to $C$ at $P(1, \sqrt{3})$. Then the curvature of $C$ at $P$ is $\underline{\quad}$.

---

### EXERCISE SET 12.5

#### FOCUS ON CONCEPTS
**1–2 Use the osculating circle shown in the figure to estimate the curvature at the indicated point.**
1. Osculating circle of radius $0.5$ at origin $\implies \kappa \approx 2$.
2. Osculating circle of radius $3$ at $(0, 3) \implies \kappa \approx 1/3$.

**3–4 For a plane curve $y = f(x)$ the curvature at $(x, f(x))$ is a function $\kappa(x)$. In these exercises the graphs of $f(x)$ and $\kappa(x)$ are shown. Determine which is which and explain your reasoning.**

**5–12 Use Formula (3) to find $\kappa(t)$.**
5. $\mathbf{r}(t) = t^2\mathbf{i} + t^3\mathbf{j}$
6. $\mathbf{r}(t) = 4\cos t\,\mathbf{i} + \sin t\,\mathbf{j}$
7. $\mathbf{r}(t) = e^{3t}\mathbf{i} + e^{-t}\mathbf{j}$
8. $x = 1 - t^3, \quad y = t - t^2$
9. $\mathbf{r}(t) = 4\cos t\,\mathbf{i} + 4\sin t\,\mathbf{j} + t\mathbf{k}$
10. $\mathbf{r}(t) = t\mathbf{i} + \frac{1}{2}t^2\mathbf{j} + \frac{1}{3}t^3\mathbf{k}$
11. $x = \cosh t, \quad y = \sinh t, \quad z = t$
12. $\mathbf{r}(t) = \mathbf{i} + t\mathbf{j} + t^2\mathbf{k}$

**13–16 Find the curvature and the radius of curvature at the stated point.**
13. $\mathbf{r}(t) = 3\cos t\,\mathbf{i} + 4\sin t\,\mathbf{j} + t\mathbf{k}; \quad t = \pi/2$
14. $\mathbf{r}(t) = e^t\mathbf{i} + e^{-t}\mathbf{j} + t\mathbf{k}; \quad t = 0$
15. $x = e^t\cos t, \quad y = e^t\sin t, \quad z = e^t; \quad t = 0$
16. $x = \sin t, \quad y = \cos t, \quad z = \frac{1}{2}t^2; \quad t = 0$

**17–18 Confirm that $s$ is an arc length parameter by showing that $\|d\mathbf{r}/ds\| = 1$, and then apply Formula (1) to find $\kappa(s)$.**
17. $\mathbf{r} = \sin\left(\frac{1 + s}{2}\right)\mathbf{i} + \cos\left(\frac{1 + s}{2}\right)\mathbf{j} + \sqrt{3}\left(\frac{1 + s}{2}\right)\mathbf{k}$
18. $\mathbf{r} = \left(1 - \frac{2}{3}s\right)^{3/2}\mathbf{i} + \left(\frac{2}{3}s\right)^{3/2}\mathbf{j} \quad \left(0 \le s \le \frac{3}{2}\right)$

**19–22 True–False Determine whether the statement is true or false. Explain your answer.**
19. A circle of radius 2 has constant curvature $\frac{1}{2}$.
20. A vertical line in 2-space has undefined curvature.
21. If $\mathbf{r}(s)$ is parametrized by arc length, then the curvature of the graph of $\mathbf{r}(s)$ is the length of $\mathbf{r}''(s)$.
22. If $C$ is a curve in 2-space, then the osculating circle to $C$ at a point $P$ has radius equal to the curvature of $C$ at $P$.

**23.**  
(a) Use Formula (3) to show that in 2-space the curvature of a smooth parametric curve $x = x(t), \; y = y(t)$ is
$$\kappa(t) = \frac{|x' y'' - y' x''|}{(x'^2 + y'^2)^{3/2}}$$
(b) Use the result in part (a) to show that in 2-space the curvature of the plane curve given by $y = f(x)$ is
$$\kappa(x) = \frac{|d^2y/dx^2|}{[1 + (dy/dx)^2]^{3/2}}$$
[*Hint:* Express $y = f(x)$ parametrically with $x = t$ as the parameter.]

**24.** Use part (b) of Exercise 23 to show that the curvature of $y = f(x)$ can be expressed in terms of the angle of inclination $\phi$ of the tangent line as
$$\kappa(\phi) = \left|\frac{d^2y}{dx^2}\cos^3\phi\right|$$
[*Hint:* $\tan\phi = dy/dx$.]

**25–28 Use the result in Exercise 23(b) to find the curvature at the stated point.**
25. $y = \sin x; \quad x = \pi/2$
26. $y = \tan x; \quad x = \pi/4$
27. $y = e^{-x}; \quad x = 1$
28. $y^2 - 4x^2 = 9; \quad (2, 5)$

**29–32 Use the result in Exercise 23(a) to find the curvature at the stated point.**
29. $x = t^2, \quad y = t^3; \quad t = \frac{1}{2}$
30. $x = e^{3t}, \quad y = e^{-t}; \quad t = 0$
31. $x = t, \quad y = 1/t; \quad t = 1$
32. $x = 2\sin 2t, \quad y = 3\sin t; \quad t = \pi/2$

**33.** In each part, use the formulas in Exercise 23 to help find the radius of curvature at the stated points. Then sketch the graph together with the osculating circles at those points.  
(a) $y = \cos x$ at $x = 0$ and $x = \pi$  
(b) $x = 2\cos t, \; y = \sin t \; (0 \le t \le 2\pi)$ at $t = 0$ and $t = \pi/2$

**34.** Use the formula in Exercise 23(a) to find $\kappa(t)$ for the curve $x = e^{-t}\cos t, \; y = e^{-t}\sin t$. Then sketch the graph of $\kappa(t)$.

**35–36 Generate the graph of $y = f(x)$ using a graphing utility, and then make a conjecture about the shape of the graph of $y = \kappa(x)$. Check your conjecture by generating the graph of $y = \kappa(x)$.**
35. $f(x) = xe^{-x}$ for $0 \le x \le 5$
36. $f(x) = x^3 - x$ for $-1 \le x \le 1$

**37.**  
(a) Use a CAS and part (b) of Exercise 23 to find $\kappa(x)$ for $f(x) = x^4 - 2x^2$.  
(b) Use the CAS to generate the graphs of $f(x) = x^4 - 2x^2$ and $\kappa(x)$ on the same screen for $-2 \le x \le 2$.  
(c) Find the radius of curvature at each relative extremum.  
(d) Make a sketch showing the graph of $f(x)$ and the osculating circles at the relative extrema.

**38.**  
(a) Use a CAS to graph the parametric curve $x = t\cos t, \; y = t\sin t$ for $t \ge 0$.  
(b) Make a conjecture about the behavior of the curvature $\kappa(t)$ as $t \to +\infty$.  
(c) Use the CAS and part (a) of Exercise 23 to find $\kappa(t)$.  
(d) Check your conjecture by finding the limit of $\kappa(t)$ as $t \to +\infty$.

**39.** Use the formula in Exercise 23(a) to show that for a curve in polar coordinates described by $r = f(\theta)$ the curvature is
$$\kappa(\theta) = \frac{|r^2 + 2(dr/d\theta)^2 - r(d^2r/d\theta^2)|}{[r^2 + (dr/d\theta)^2]^{3/2}}$$

**40.** Use the result in Exercise 39 to show that a circle has constant curvature.

**41–44 Use the formula in Exercise 39 to find the curvature at the indicated point.**
41. $r = 1 + \cos\theta; \quad \theta = \pi/2$
42. $r = e^{2\theta}; \quad \theta = 1$
43. $r = \sin 3\theta; \quad \theta = 0$
44. $r = \theta; \quad \theta = 1$

**45.** Find the radius of curvature of the parabola $y^2 = 4px$ at $(0, 0)$.
**46.** At what point(s) does $y = e^x$ have maximum curvature?
**47.** At what point(s) does $4x^2 + 9y^2 = 36$ have minimum radius of curvature?
**48.** Find the maximum and minimum values of the radius of curvature for the curve $x = \cos t, \; y = \sin t, \; z = \cos t$.
**49.** Use the formula in Exercise 39 to show that the curvature of the polar curve $r = e^{a\theta}$ is inversely proportional to $r$.
**50.** Use the formula in Exercise 39 and a CAS to show that the curvature of the lemniscate $r = \sqrt{a\cos 2\theta}$ is directly proportional to $r$.

**51.**  
(a) Use the result in Exercise 24 to show that for the parabola $y = x^2$ the curvature $\kappa(\phi)$ at points where the tangent line has an angle of inclination of $\phi$ is $\kappa(\phi) = |2\cos^3\phi|$.  
(b) Find the radius of curvature of the parabola where the tangent line has slope 1.  
(c) Make a sketch showing the osculating circle at that point.

**52.** The evolute of a smooth parametric curve $C$ in 2-space is the curve formed from the centers of curvature of $C$. The accompanying figure shows the ellipse $x = 3\cos t, \; y = 2\sin t \; (0 \le t \le 2\pi)$ and its evolute graphed together.  
(a) Which points on the evolute correspond to $t = 0$ and $t = \pi/2$?  
(b) In what direction is the evolute traced as $t$ increases from 0 to $2\pi$?  
(c) What does the evolute of a circle look like? Explain your reasoning.

#### FOCUS ON CONCEPTS (Smooth Transitions)
**53.** Show that the transition at $x = 0$ from the horizontal line $y = 0$ for $x \le 0$ to the parabola $y = x^2$ for $x > 0$ is not smooth, whereas the transition to $y = x^3$ for $x > 0$ is smooth.
**54.** (a) Sketch $y = x^2$ for $x < 0, \; y = x^4$ for $x \ge 0$. (b) Show transition at $x = 0$ is not smooth.
**55.** Find $a$ so that there is a smooth transition from the circle of radius $r$ centered at $(0, r)$ to the parabola $y = ax^2$ at $x = 0$.
**56.** Find $a, b,$ and $c$ so that there is a smooth transition at $x = 0$ from $y = e^x$ for $x \le 0$ to $y = ax^2 + bx + c$ for $x > 0$.
**57.** Explain why it is always possible to find $a, b, c$ for a smooth transition from $y = f(x) \; (x \le 0)$ to $y = ax^2 + bx + c$.

**58–61 Frenet–Serret Formulas and Torsion:**  
58. Show that $\frac{d\mathbf{T}}{ds} = \kappa(s)\mathbf{N}(s)$.  
59. (a) Show $d\mathbf{B}/ds \perp \mathbf{B}(s)$. (b) Show $d\mathbf{B}/ds \perp \mathbf{T}(s)$. (c) Conclude $\frac{d\mathbf{B}}{ds} = -\tau(s)\mathbf{N}(s)$, defining torsion $\tau(s)$. (d) Show $\tau(s) = 0$ for plane curves.  
60. Show that $\frac{d\mathbf{N}}{ds} = -\kappa\mathbf{T} + \tau\mathbf{B}$.  
61. Derive $\tau = \frac{[\mathbf{r}'(s) \times \mathbf{r}''(s)] \cdot \mathbf{r}'''(s)}{\|\mathbf{r}''(s)\|^2}$ and $\mathbf{B} = \frac{\mathbf{r}'(s) \times \mathbf{r}''(s)}{\|\mathbf{r}''(s)\|}$.  
62. Derive general parameter formula $\tau(t) = \frac{[\mathbf{r}'(t) \times \mathbf{r}''(t)] \cdot \mathbf{r}'''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|^2}$.

**63–66 Use the formula in Exercise 62(d) to find the torsion $\tau = \tau(t)$.**  
63. Twisted cubic $\mathbf{r}(t) = 2t\mathbf{i} + t^2\mathbf{j} + \frac{1}{3}t^3\mathbf{k}$  
64. Circular helix $\mathbf{r}(t) = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} + ct\mathbf{k}$  
65. $\mathbf{r}(t) = e^t\mathbf{i} + e^{-t}\mathbf{j} + \sqrt{2}t\mathbf{k}$  
66. $\mathbf{r}(t) = (t - \sin t)\mathbf{i} + (1 - \cos t)\mathbf{j} + t\mathbf{k}$

**67. Writing** Osculating circle crossing curve at inflection points.  
**68. Writing** Graph of radius of curvature versus $\theta$ for the cardioid $r = 1 + \cos\theta$.

#### QUICK CHECK ANSWERS 12.5
1. $\left\|\frac{d\mathbf{T}}{ds}\right\| = \|\mathbf{r}''(s)\|$  
2. (a) $\frac{\|\mathbf{T}'(t)\|}{\|\mathbf{r}'(t)\|}$ (b) $\frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}$  
3. $\left|\frac{d\phi}{ds}\right|$  
4. $\frac{1}{2}$

---

## 12.6 MOTION ALONG A CURVE

In earlier sections we considered the motion of a particle along a line. In that situation there are only two directions in which the particle can move—the positive direction or the negative direction. Motion in 2-space or 3-space is more complicated because there are infinitely many directions in which a particle can move. In this section we will show how vectors can be used to analyze motion along curves in 2-space or 3-space.

### VELOCITY, ACCELERATION, AND SPEED

Let us assume that the motion of a particle in 2-space or 3-space is described by a smooth vector-valued function $\mathbf{r}(t)$ in which the parameter $t$ denotes time; we will call this the **position function** or **trajectory** of the particle.

We define the direction of motion at time $t$ to be the direction of the unit tangent vector $\mathbf{T}(t)$, and we define the speed to be $ds/dt$—the instantaneous rate of change of the arc length traveled by the particle from an arbitrary reference point.
$$\mathbf{v}(t) = \frac{ds}{dt}\mathbf{T}(t) \tag{1}$$
which we call the **velocity** of the particle at time $t$ (Figure 12.6.1).

> **12.6.1 DEFINITION**  
> If $\mathbf{r}(t)$ is the position function of a particle moving along a curve in 2-space or 3-space, then the **instantaneous velocity**, **instantaneous acceleration**, and **instantaneous speed** of the particle at time $t$ are defined by
> $$\text{velocity} = \mathbf{v}(t) = \frac{d\mathbf{r}}{dt} \tag{2}$$
> $$\text{acceleration} = \mathbf{a}(t) = \frac{d\mathbf{v}}{dt} = \frac{d^2\mathbf{r}}{dt^2} \tag{3}$$
> $$\text{speed} = \|\mathbf{v}(t)\| = \frac{ds}{dt} \tag{4}$$

| Quantity | 2-Space | 3-Space |
| :--- | :--- | :--- |
| **Position** | $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j}$ | $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$ |
| **Velocity** | $\mathbf{v}(t) = \frac{dx}{dt}\mathbf{i} + \frac{dy}{dt}\mathbf{j}$ | $\mathbf{v}(t) = \frac{dx}{dt}\mathbf{i} + \frac{dy}{dt}\mathbf{j} + \frac{dz}{dt}\mathbf{k}$ |
| **Acceleration** | $\mathbf{a}(t) = \frac{d^2x}{dt^2}\mathbf{i} + \frac{d^2y}{dt^2}\mathbf{j}$ | $\mathbf{a}(t) = \frac{d^2x}{dt^2}\mathbf{i} + \frac{d^2y}{dt^2}\mathbf{j} + \frac{d^2z}{dt^2}\mathbf{k}$ |
| **Speed** | $\|\mathbf{v}(t)\| = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}$ | $\|\mathbf{v}(t)\| = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}$ |

#### Example 1
A particle moves along a circular path in such a way that its $x$- and $y$-coordinates at time $t$ are $x = 2\cos t, \; y = 2\sin t$.  
(a) Find the instantaneous velocity and speed of the particle at time $t$.  
(b) Sketch the path, position, and velocity at $t = \pi/4$.  
(c) Show that at each instant the acceleration vector is perpendicular to the velocity vector.

**Solution (a).** $\mathbf{r}(t) = 2\cos t\,\mathbf{i} + 2\sin t\,\mathbf{j} \implies \mathbf{v}(t) = \mathbf{r}'(t) = -2\sin t\,\mathbf{i} + 2\cos t\,\mathbf{j}$, speed $\|\mathbf{v}(t)\| = 2$.  
**Solution (b).** At $t = \pi/4$: $\mathbf{r}(\pi/4) = \sqrt{2}\mathbf{i} + \sqrt{2}\mathbf{j}, \; \mathbf{v}(\pi/4) = -\sqrt{2}\mathbf{i} + \sqrt{2}\mathbf{j}$ (Figure 12.6.2).  
**Solution (c).** $\mathbf{a}(t) = \mathbf{v}'(t) = -2\cos t\,\mathbf{i} - 2\sin t\,\mathbf{j} = -\mathbf{r}(t)$. Thus $\mathbf{v}(t) \cdot \mathbf{a}(t) = 0$, so $\mathbf{v} \perp \mathbf{a}$.

#### Example 2
A particle moves through 3-space with velocity $\mathbf{v}(t) = \mathbf{i} + t\mathbf{j} + t^2\mathbf{k}$. Find the coordinates at $t = 1$ given that the particle is at $(-1, 2, 4)$ at $t = 0$.

**Solution.** $\mathbf{r}(t) = \int \mathbf{v}(t)\,dt = t\mathbf{i} + \frac{t^2}{2}\mathbf{j} + \frac{t^3}{3}\mathbf{k} + \mathbf{C}$.  
At $t = 0$: $\mathbf{r}(0) = \mathbf{C} = -\mathbf{i} + 2\mathbf{j} + 4\mathbf{k}$.  
Thus $\mathbf{r}(t) = (t - 1)\mathbf{i} + \left(\frac{t^2}{2} + 2\right)\mathbf{j} + \left(\frac{t^3}{3} + 4\right)\mathbf{k}$.  
At $t = 1$: $\mathbf{r}(1) = 0\mathbf{i} + \frac{5}{2}\mathbf{j} + \frac{13}{3}\mathbf{k} \implies \left(0, \frac{5}{2}, \frac{13}{3}\right)$.

---

### DISPLACEMENT AND DISTANCE TRAVELED

* **Displacement:** $\Delta\mathbf{r} = \mathbf{r}(t_2) - \mathbf{r}(t_1) = \int_{t_1}^{t_2} \mathbf{v}(t)\,dt \tag{7–8}$
* **Distance traveled:** $s = \int_{t_1}^{t_2} \|\mathbf{v}(t)\|\,dt \tag{9}$

#### Example 3
For helix $\mathbf{r}(t) = (4\cos\pi t)\mathbf{i} + (4\sin\pi t)\mathbf{j} + t\mathbf{k}$, find distance traveled and displacement for $1 \le t \le 5$.  
**Solution.** $\|\mathbf{v}(t)\| = \sqrt{16\pi^2 + 1} \implies s = \int_1^5 \sqrt{16\pi^2 + 1}\,dt = 4\sqrt{16\pi^2 + 1}$.  
Displacement $\Delta\mathbf{r} = \mathbf{r}(5) - \mathbf{r}(1) = (-4\mathbf{i} + 5\mathbf{k}) - (-4\mathbf{i} + \mathbf{k}) = 4\mathbf{k}$.

---

### NORMAL AND TANGENTIAL COMPONENTS OF ACCELERATION

> **12.6.2 THEOREM**  
> If a particle moves along a smooth curve $C$ in 2-space or 3-space, then:
> $$\mathbf{v} = \frac{ds}{dt}\mathbf{T}, \quad \mathbf{a} = \frac{d^2s}{dt^2}\mathbf{T} + \kappa\left(\frac{ds}{dt}\right)^2\mathbf{N} \tag{10–11}$$
> Expressed as $\mathbf{a} = a_T \mathbf{T} + a_N \mathbf{N} \tag{14}$ where:
> $$a_T = \frac{d^2s}{dt^2}, \quad a_N = \kappa\left(\frac{ds}{dt}\right)^2 \tag{12–13}$$

> *The acceleration vector always lies in the osculating plane ($TN$-plane); the binormal component of acceleration is always zero.*

> **12.6.3 THEOREM**  
> $$a_T = \frac{\mathbf{v} \cdot \mathbf{a}}{\|\mathbf{v}\|}, \quad a_N = \frac{\|\mathbf{v} \times \mathbf{a}\|}{\|\mathbf{v}\|}, \quad \kappa = \frac{\|\mathbf{v} \times \mathbf{a}\|}{\|\mathbf{v}\|^3} \tag{15–17}$$
> Also: $a_N = \sqrt{\|\mathbf{a}\|^2 - a_T^2} \tag{18}$.

#### Example 4
For twisted cubic $\mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j} + t^3\mathbf{k}$:  
(a) At general time $t$: $\mathbf{v} = \mathbf{i} + 2t\mathbf{j} + 3t^2\mathbf{k}, \; \mathbf{a} = 2\mathbf{j} + 6t\mathbf{k}$.  
$a_T = \frac{4t + 18t^3}{\sqrt{1 + 4t^2 + 9t^4}}, \quad a_N = 2\sqrt{\frac{9t^4 + 9t^2 + 1}{9t^4 + 4t^2 + 1}}$.  
(b) At $t = 1$: $a_T = \frac{22}{\sqrt{14}} \approx 5.88, \quad a_N = 2\sqrt{\frac{19}{14}} \approx 2.33$.  
(c) Vector components at $t = 1$: $a_T\mathbf{T} = \frac{11}{7}\mathbf{i} + \frac{22}{7}\mathbf{j} + \frac{33}{7}\mathbf{k}, \quad a_N\mathbf{N} = -\frac{11}{7}\mathbf{i} - \frac{8}{7}\mathbf{j} + \frac{9}{7}\mathbf{k}$.  
(d) Curvature at $t = 1$: $\kappa = \frac{\sqrt{76}}{(\sqrt{14})^3} = \frac{1}{14}\sqrt{\frac{38}{7}} \approx 0.17$.

---

### A MODEL OF PROJECTILE MOTION

Under Newton's second law $\mathbf{F} = m\mathbf{a} = -mg\mathbf{j} \implies \mathbf{a} = -g\mathbf{j} \tag{20}$.
$$\mathbf{v}(t) = -gt\mathbf{j} + \mathbf{v}_0 \tag{21}$$
$$\mathbf{r}(t) = \left(-\frac{1}{2}gt^2 + s_0\right)\mathbf{j} + t\mathbf{v}_0 \tag{24}$$

With launch angle $\alpha$ and initial speed $v_0 = \|\mathbf{v}_0\|$:
$$\mathbf{r}(t) = (v_0\cos\alpha)t\mathbf{i} + \left(s_0 + (v_0\sin\alpha)t - \frac{1}{2}gt^2\right)\mathbf{j} \tag{26}$$
$$x = (v_0\cos\alpha)t, \quad y = s_0 + (v_0\sin\alpha)t - \frac{1}{2}gt^2 \tag{27}$$
$$v_x = v_0\cos\alpha, \quad v_y = v_0\sin\alpha - gt \tag{28}$$
$$y = s_0 + (\tan\alpha)x - \left(\frac{g}{2v_0^2\cos^2\alpha}\right)x^2 \tag{29}$$

#### Example 5
Shell fired with muzzle speed $800$ ft/s at elevation $45^\circ$, $s_0 = 0, g = 32$ ft/s$^2$:  
(a) $x = 400\sqrt{2}t, \quad y = 400\sqrt{2}t - 16t^2 \tag{30}$.  
(b) Max height occurs when $dy/dt = 0 \implies t = \frac{25\sqrt{2}}{2} \implies y = 5000$ ft.  
(c) Ground impact at $y = 0 \implies t = 25\sqrt{2} \implies x = 20,000$ ft.  
(d) Impact speed $= 800$ ft/s.

---

### QUICK CHECK EXERCISES 12.6
*(See page 895 for answers.)*

1. $\mathbf{v}(t) = \underline{\quad}, \; \mathbf{a}(t) = \underline{\quad}, \; \frac{ds}{dt} = \underline{\quad}$.
2. Displacement is $\underline{\quad}$, and distance $s$ is given by $\underline{\quad}$.
3. Tangential scalar component $a_T = \underline{\quad}$, normal scalar component $a_N = \underline{\quad}$.
4. For $\mathbf{r}(t) = \left(-\frac{1}{2}gt^2 + s_0\right)\mathbf{j} + t\mathbf{v}_0$: $\mathbf{a} = \underline{\quad}, \; \mathbf{v}(t) = \underline{\quad}$, initial position $\underline{\quad}$, initial velocity $\underline{\quad}$.

---

### EXERCISE SET 12.6

**1–4 Find velocity, acceleration, and speed at arbitrary time $t$, and sketch the path and vectors at indicated time $t$.**
1. $\mathbf{r}(t) = 3\cos t\,\mathbf{i} + 3\sin t\,\mathbf{j}; \quad t = \pi/3$
2. $\mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j}; \quad t = 2$
3. $\mathbf{r}(t) = e^t\mathbf{i} + e^{-t}\mathbf{j}; \quad t = 0$
4. $\mathbf{r}(t) = (2 + 4t)\mathbf{i} + (1 - t)\mathbf{j}; \quad t = 1$

**5–8 Find velocity, speed, and acceleration at given time $t$.**
5. $\mathbf{r}(t) = t\mathbf{i} + \frac{1}{2}t^2\mathbf{j} + \frac{1}{3}t^3\mathbf{k}; \quad t = 1$
6. $x = 1 + 3t, \quad y = 2 - 4t, \quad z = 7 + t; \quad t = 2$
7. $x = 2\cos t, \quad y = 2\sin t, \quad z = t; \quad t = \pi/4$
8. $\mathbf{r}(t) = e^t\sin t\,\mathbf{i} + e^t\cos t\,\mathbf{j} + t\mathbf{k}; \quad t = \pi/2$

#### FOCUS ON CONCEPTS
**9.** For elliptic motion $x = a\cos\omega t, \; y = b\sin\omega t$: (a) Show acceleration is directed toward origin. (b) Show $\|\mathbf{a}\|$ is proportional to distance from origin.
**10.** Vibrating particle $\mathbf{r}(t) = 16\sin\pi t\,\mathbf{i} + 4\cos 2\pi t\,\mathbf{j}$.
**11.** Motion with zero acceleration is linear motion.
**12.** Constant speed implies acceleration is normal to path.
**13–16 Minimum and maximum speed calculations and graphs.**

**17–20 Find position and velocity vectors from acceleration and initial conditions.**
17. $\mathbf{a}(t) = -\cos t\,\mathbf{i} - \sin t\,\mathbf{j}; \quad \mathbf{v}(0) = \mathbf{i}; \quad \mathbf{r}(0) = \mathbf{j}$
18. $\mathbf{a}(t) = \mathbf{i} + e^{-t}\mathbf{j}; \quad \mathbf{v}(0) = 2\mathbf{i} + \mathbf{j}; \quad \mathbf{r}(0) = \mathbf{i} - \mathbf{j}$
19. $\mathbf{a}(t) = \sin t\,\mathbf{i} + \cos t\,\mathbf{j} + e^t\mathbf{k}; \quad \mathbf{v}(0) = \mathbf{k}; \quad \mathbf{r}(0) = -\mathbf{i} + \mathbf{k}$
20. $\mathbf{a}(t) = (t + 1)^{-2}\mathbf{j} - e^{-2t}\mathbf{k}; \quad \mathbf{v}(0) = 3\mathbf{i} - \mathbf{j}; \quad \mathbf{r}(0) = 2\mathbf{k}$

**21–24 Angles between $\mathbf{v}$ and $\mathbf{a}$, displacements of electrons and protons.**
**25–28 Find displacement and distance traveled over indicated time interval.**
25. $\mathbf{r} = t^2\mathbf{i} + \frac{1}{3}t^3\mathbf{j}; \quad 1 \le t \le 3$
26. $\mathbf{r} = (1 - 3\sin t)\mathbf{i} + 3\cos t\,\mathbf{j}; \quad 0 \le t \le 3\pi/2$
27. $\mathbf{r} = e^t\mathbf{i} + e^{-t}\mathbf{j} + \sqrt{2}t\mathbf{k}; \quad 0 \le t \le \ln 3$
28. $\mathbf{r} = \cos 2t\,\mathbf{i} + (1 - \cos 2t)\mathbf{j} + \left(3 + \frac{1}{2}\cos 2t\right)\mathbf{k}; \quad 0 \le t \le \pi$

**29–30 Same path with constant vs varying speed.**
**31–36 Find scalar/vector components $a_T, a_N$ and curvature $\kappa$.**
31. $\mathbf{r} = e^{-t}\mathbf{i} + e^t\mathbf{j}; \quad t = 0$
32. $\mathbf{r} = \cos(t^2)\mathbf{i} + \sin(t^2)\mathbf{j}; \quad t = \sqrt{\pi/2}$
33. $\mathbf{r} = (t^3 - 2t)\mathbf{i} + (t^2 - 4)\mathbf{j}; \quad t = 1$
34. $\mathbf{r} = e^t\cos t\,\mathbf{i} + e^t\sin t\,\mathbf{j}; \quad t = \pi/4$
35. $\mathbf{r} = e^t\mathbf{i} + e^{-2t}\mathbf{j} + t\mathbf{k}; \quad t = 0$
36. $\mathbf{r} = 3\sin t\,\mathbf{i} + 2\cos t\,\mathbf{j} - \sin 2t\,\mathbf{k}; \quad t = \pi/2$

**37–40 Given $\mathbf{v}$ and $\mathbf{a}$ at an instant, find $a_T, a_N, \mathbf{T}, \mathbf{N}$.**
37. $\mathbf{v} = -4\mathbf{j}, \quad \mathbf{a} = 2\mathbf{i} + 3\mathbf{j}$
38. $\mathbf{v} = 2\mathbf{i} + 2\mathbf{j} + \mathbf{k}, \quad \mathbf{a} = \mathbf{i} + 2\mathbf{k}$
39. $\|\mathbf{v}\| = \sqrt{t^2 + e^{-3t}}; \quad t = 0$
40. $\|\mathbf{v}\| = \sqrt{(4t - 1)^2 + \cos^2\pi t}; \quad t = 1/4$

**41.** Fermi Lab accelerator proton normal acceleration.
**42.** Acceleration vector tangent at inflection points where $f''(x) = 0$.
**43–44 Normal acceleration as a function of $x$ along curves.**
**45–46 Find $a_N$ at $t = 1$ from given vector data.**
**47–50 True–False.**
**51.** Derive Formula (18) from Formula (14).
**52.** Automobile maximum allowable speed around 1000 m curve.
**53.** Centripetal frictional force on 500 kg go-cart ($F = m\kappa(ds/dt)^2$).
**54–70 Projectile Motion Problems:** Cannon shells, rock thrown from 168 ft building, baseball hit at angle, ski jump trajectory (259 ft incline), fire hose over building corner, train braking on curved track.
**71–72 Writing.** Forces sensed in car; derivation of projectile model.

#### QUICK CHECK ANSWERS 12.6
1. $\frac{d\mathbf{r}}{dt}; \; \frac{d\mathbf{v}}{dt} = \frac{d^2\mathbf{r}}{dt^2}; \; \|\mathbf{v}(t)\|$  
2. $\mathbf{r}(t_2) - \mathbf{r}(t_1); \; \int_{t_1}^{t_2}\|\mathbf{v}(t)\|\,dt$  
3. $\frac{d^2s}{dt^2}; \; \kappa(ds/dt)^2$  
4. $-g\mathbf{j}; \; -gt\mathbf{j} + \mathbf{v}_0; \; s_0\mathbf{j}; \; \mathbf{v}_0$

---

## 12.7 KEPLER’S LAWS OF PLANETARY MOTION

One of the great advances in the history of astronomy occurred in the early 1600s when Johannes Kepler deduced from empirical data that all planets in our solar system move in elliptical orbits with the Sun at a focus. Subsequently, Isaac Newton showed mathematically that such planetary motion is the consequence of an inverse-square law of gravitational attraction. In this section we will use the concepts developed in the preceding sections of this chapter to derive three basic laws of planetary motion, known as **Kepler’s laws**.

### KEPLER'S LAWS

> **12.7.1 KEPLER’S LAWS**  
> • **First law (Law of Orbits):** Each planet moves in an elliptical orbit with the Sun at a focus.  
> • **Second law (Law of Areas):** Equal areas are swept out in equal times by the line from the Sun to a planet.  
> • **Third law (Law of Periods):** The square of a planet’s period (the time it takes the planet to complete one orbit about the Sun) is proportional to the cube of the semimajor axis of its orbit.

---

### CENTRAL FORCES

A force $\mathbf{F}$ directed toward a fixed point $O$ is a **central force**.
$$\mathbf{r} \times \mathbf{a} = \mathbf{0} \implies \frac{d}{dt}(\mathbf{r} \times \mathbf{v}) = \mathbf{r} \times \frac{d\mathbf{v}}{dt} + \frac{d\mathbf{r}}{dt} \times \mathbf{v} = (\mathbf{r} \times \mathbf{a}) + (\mathbf{v} \times \mathbf{v}) = \mathbf{0} \tag{1}$$
Integrating gives:
$$\mathbf{r} \times \mathbf{v} = \mathbf{b} \tag{2}$$
where $\mathbf{b}$ is constant. Hence the orbit lies entirely in a fixed plane containing the center of force (the **ecliptic**).

---

### NEWTON'S LAW OF UNIVERSAL GRAVITATION

> **12.7.2 NEWTON’S LAW OF UNIVERSAL GRAVITATION**  
> Every particle of matter in the Universe attracts every other particle of matter in the Universe with a force of magnitude
> $$\|\mathbf{F}\| = \frac{GMm}{r^2} \tag{3}$$
> In vector form:
> $$\mathbf{F} = -\frac{GMm}{r^3}\mathbf{r} \tag{4} \implies \mathbf{a} = -\frac{GM}{r^3}\mathbf{r} = -\frac{GM}{r^2}\mathbf{u} \tag{5, 9}$$

Derivation in polar coordinates yields the trajectory equation:
$$r = \frac{r_0^2 v_0^2 / GM}{1 + \left(\frac{r_0 v_0^2}{GM} - 1\right)\cos\theta} = \frac{k}{1 + e\cos\theta} \tag{19–20}$$
where
$$k = \frac{r_0^2 v_0^2}{GM}, \quad e = \frac{r_0 v_0^2}{GM} - 1 \tag{21–22}$$
* $e < 1 \implies$ Ellipse (Kepler's First Law).
* **Escape speed:** $v_{\text{esc}} = \sqrt{\frac{2GM}{r_0}} \tag{23}$.
* **Kepler's Second Law:** $\frac{dA}{dt} = \frac{1}{2}r_0 v_0 = \text{constant} \tag{25}$.
* **Kepler's Third Law:** $T^2 = \frac{4\pi^2}{GM}a^3 \tag{28} \implies T = \frac{2\pi}{\sqrt{GM}}a^{3/2} \tag{29}$.

---

### ARTIFICIAL SATELLITES

| Attracting Body | International System | British Engineering System |
| :--- | :--- | :--- |
| **Earth** | $GM = 3.99 \times 10^{14}\text{ m}^3/\text{s}^2 = 3.99 \times 10^5\text{ km}^3/\text{s}^2$ | $GM = 1.41 \times 10^{16}\text{ ft}^3/\text{s}^2 = 1.24 \times 10^{12}\text{ mi}^3/\text{h}^2$ |
| **Sun** | $GM = 1.33 \times 10^{20}\text{ m}^3/\text{s}^2 = 1.33 \times 10^{11}\text{ km}^3/\text{s}^2$ | $GM = 4.69 \times 10^{21}\text{ ft}^3/\text{s}^2 = 4.13 \times 10^{17}\text{ mi}^3/\text{h}^2$ |
| **Moon** | $GM = 4.90 \times 10^{12}\text{ m}^3/\text{s}^2 = 4.90 \times 10^3\text{ km}^3/\text{s}^2$ | $GM = 1.73 \times 10^{14}\text{ ft}^3/\text{s}^2 = 1.53 \times 10^{10}\text{ mi}^3/\text{h}^2$ |

* **Apogee/Aphelion:** Maximum distance from attracting center.
* **Perigee/Perihelion:** Minimum distance from attracting center.

#### Example 1
Find the altitude in miles of a communications satellite in geosynchronous orbit ($T = 24$ h, radius of Earth $= 4000$ mi).  
**Solution.** $a = \sqrt[3]{\frac{GMT^2}{4\pi^2}} = \sqrt[3]{\frac{(1.24 \times 10^{12})(24)^2}{4\pi^2}} \approx 26,250$ mi.  
Altitude $h \approx 26,250 - 4000 = 22,250$ mi.

---

### QUICK CHECK EXERCISES 12.7
*(See page 902 for answers.)*

1. (a) $\|\mathbf{F}\| = \frac{GMm}{r^2}$ (b) $\mathbf{F} = -\frac{GMm}{r^3}\mathbf{r}$.
2. Escape speed $v_{\text{esc}} = \sqrt{\frac{2GM}{r_0}}$.
3. Power $= 3$ ($T^2 \propto a^3$).
4. $e = \frac{r_0 v_0^2}{GM} - 1$.

---

### EXERCISE SET 12.7

#### FOCUS ON CONCEPTS
**1.** Orbit speed $v = \frac{v_0}{1 + e}\sqrt{e^2 + 2e\cos\theta + 1}$; speed max at perigee, min at apogee.
**2.** Speed at minor axis $v = v_0\sqrt{\frac{1 - e}{1 + e}}$.
**3.** $v_{\max} = v_{\min}\frac{1 + e}{1 - e}$.
**4.** Circular orbit speed $v = \sqrt{\frac{GM}{r_0}}$.
**5.** Orthogonality of $\mathbf{r}$ and $\mathbf{v}$ at apsides; $r_{\max}v_{\min} = r_{\min}v_{\max}$.
**6.** Derivation of ratio of speeds from orbital radii.
**7.** Speed in km/s of satellite 200 km above Earth.
**8.** Speed in mi/h of geosynchronous satellite.
**9.** Escape speed in km/s for space probe 300 km above Earth.
**10.** Estimation of Sun's mass in kg ($M \approx 2 \times 10^{30}$ kg).
**11.** Moon's orbit around Earth (perigee, apogee, and period in days).
**12.** Vanguard 1 orbit parameters (semimajor axis, eccentricity, period in minutes).
**13.** Space probe thruster firing and resulting elliptical orbit parameters.
**14.** Proof of nonnegativity of $e$.

#### QUICK CHECK ANSWERS 12.7
1. (a) $\frac{GMm}{r^2}$ (b) $-\frac{GMm}{r^3}\mathbf{r}$  
2. $\sqrt{\frac{2GM}{r_0}}$  
3. $3$  
4. $e = \frac{r_0 v_0^2}{GM} - 1$

---

## CHAPTER 12 REVIEW EXERCISES

1. In words, what is meant by the graph of a vector-valued function?
**2–5 Describe the graph of the equation.**
2. $\mathbf{r} = (2 - 3t)\mathbf{i} - 4t\mathbf{j}$
3. $\mathbf{r} = 3\sin 2t\,\mathbf{i} + 3\cos 2t\,\mathbf{j}$
4. $\mathbf{r} = 3\cos t\,\mathbf{i} + 2\sin t\,\mathbf{j} - \mathbf{k}$
5. $\mathbf{r} = -2\mathbf{i} + t\mathbf{j} + (t^2 - 1)\mathbf{k}$

6. Describe the graph of the vector-valued function:  
(a) $\mathbf{r} = \mathbf{r}_0 + t(\mathbf{r}_1 - \mathbf{r}_0)$  
(b) $\mathbf{r} = \mathbf{r}_0 + t(\mathbf{r}_1 - \mathbf{r}_0) \quad (0 \le t \le 1)$  
(c) $\mathbf{r} = \mathbf{r}_0 + t\mathbf{r}'(t_0)$

7. Show that the graph of $\mathbf{r}(t) = t\sin\pi t\,\mathbf{i} + t\mathbf{j} + t\cos\pi t\,\mathbf{k}$ lies on the surface of a cone, and sketch the cone.
8. Find parametric equations for the intersection of the surfaces $y = x^2$ and $2x^2 + y^2 + 6z^2 = 24$, and sketch the intersection.
9. In words, give a geometric description of the statement $\lim_{t \to a}\mathbf{r}(t) = \mathbf{L}$.
10. Evaluate $\lim_{t \to 0}\left(e^{-t}\mathbf{i} + \frac{1 - \cos t}{t}\mathbf{j} + t^2\mathbf{k}\right)$.
11. Find parametric equations of the line tangent to the graph of $\mathbf{r}(t) = (t + \cos 2t)\mathbf{i} - (t^2 + t)\mathbf{j} + \sin t\,\mathbf{k}$ at the point where $t = 0$.
12. Suppose $\mathbf{r}_1(0) = \langle -1, 1, 2 \rangle, \; \mathbf{r}_2(0) = \langle 1, 2, 1 \rangle, \; \mathbf{r}_1'(0) = \langle 1, 0, 1 \rangle, \; \mathbf{r}_2'(0) = \langle 4, 0, 2 \rangle$. Evaluate at $t = 0$:  
(a) $(3\mathbf{r}_1 + 2\mathbf{r}_2)'(0)$ (b) $([\ln(t + 1)]\mathbf{r}_1)'(0)$ (c) $(\mathbf{r}_1 \times \mathbf{r}_2)'(0)$ (d) $(\mathbf{r}_1 \cdot \mathbf{r}_2)'(0)$.
13. Evaluate $\int (\cos t\,\mathbf{i} + \sin t\,\mathbf{j})\,dt$.
14. Evaluate $\int_0^{\pi/3}\langle \cos 3t, -\sin 3t \rangle\,dt$.
15. Solve the initial-value problem $\mathbf{y}'(t) = t^2\mathbf{i} + 2t\mathbf{j}, \quad \mathbf{y}(0) = \mathbf{i} + \mathbf{j}$.
16. Solve $\frac{d\mathbf{r}}{dt} = \mathbf{r}, \quad \mathbf{r}(0) = \mathbf{r}_0$.
17. Find the arc length of $\mathbf{r}(t) = e^{\sqrt{2}t}\mathbf{i} + e^{-\sqrt{2}t}\mathbf{j} + 2t\mathbf{k} \quad (0 \le t \le \sqrt{2}\ln 2)$.
18. Given $\mathbf{r}'(0) = 3\mathbf{i} - \mathbf{j} + \mathbf{k}$ and $\mathbf{r}_1(t) = \mathbf{r}(2 - e^t\ln 2)$, find $\mathbf{r}_1'(1)$.
19. Find the arc length parametrization of the line through $P(-1, 4, 3)$ and $Q(0, 2, 5)$ with reference point $P$.
20. Find the arc length parametrization of $\mathbf{r}(t) = \langle e^t\cos t, -e^t\sin t \rangle \; (0 \le t \le \pi/2)$ with reference point $\mathbf{r}(0)$.
21. State the definitions of $\mathbf{T}(t), \mathbf{N}(t),$ and $\mathbf{B}(t)$.
22. Find $\mathbf{T}(0), \mathbf{N}(0),$ and $\mathbf{B}(0)$ for $\mathbf{r}(t) = \left\langle 2\cos t, 2\cos t + \frac{3}{\sqrt{5}}\sin t, \cos t - \frac{6}{\sqrt{5}}\sin t \right\rangle$.
23. State the definition of "curvature" and explain what it means geometrically.
24. Given $\mathbf{r}'(0) = \mathbf{i}$ and $\mathbf{r}''(0) = \mathbf{i} + 2\mathbf{j}$, find the curvature at $t = 0$.
**25–28 Find the curvature at the stated point.**  
25. $\mathbf{r}(t) = 2\cos t\,\mathbf{i} + 3\sin t\,\mathbf{j} - t\mathbf{k}; \quad t = \pi/2$  
26. $\mathbf{r}(t) = \langle 2t, e^{2t}, e^{-2t} \rangle; \quad t = 0$  
27. $y = \cos x; \quad x = \pi/2$  
28. $y = \ln x; \quad x = 1$
29. Physical interpretations of: (a) $\|d\mathbf{r}/dt\|$ (b) $\int_{t_0}^{t_1}\|d\mathbf{r}/dt\|\,dt$ (c) $\|\mathbf{r}(t)\|$.
30. Motion on sphere; constant speed implies $\mathbf{a} \perp \mathbf{v}$.
31. Uniform circular motion kinematics: $\mathbf{r}(t) = R\cos\omega t\,\mathbf{i} + R\sin\omega t\,\mathbf{j}$, speed $v = R\omega$, acceleration $a = R\omega^2$, period $T = 2\pi/\omega = 2\pi R/v$.
32. Centripetal acceleration, force $F = mv^2/R$, and astronaut in orbit.
33. Given $\mathbf{v}_0 = \mathbf{i} + 2\mathbf{j} - \mathbf{k}, \; \mathbf{a}(t) = 2t^2\mathbf{i} + \mathbf{j} + \cos 2t\,\mathbf{k}$, find position and speed at $t = 1$.
34. Show $\frac{d}{dt}\|\mathbf{v}\| = \frac{1}{\|\mathbf{v}\|}(\mathbf{v} \cdot \mathbf{a})$.
35. Escape speed for space probe 600 km above Earth.
36. Speed of rocket tracked by radar: $v = b\sec^2\theta\frac{d\theta}{dt}$.
37. Maximum height a ball can hit gym wall 60 ft away with 25 ft ceiling.

---

## CHAPTER 12 MAKING CONNECTIONS

**1.**  
(a) Show that $\mathbf{N}(t) = \frac{\mathbf{r}'(t) \times \mathbf{r}''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|} \times \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}$.  
(b) Show that this can be expressed as $\mathbf{N}(t) = \frac{(\mathbf{r}'(t) \times \mathbf{r}''(t)) \times \mathbf{r}'(t)}{\|(\mathbf{r}'(t) \times \mathbf{r}''(t)) \times \mathbf{r}'(t)\|}$.  
(c) Use part (b) to find $\mathbf{N}(t)$ for:  
(i) $\mathbf{r}(t) = (t^2 - 1)\mathbf{i} + t\mathbf{j}; \quad t = 1$  
(ii) $\mathbf{r}(t) = 4\cos t\,\mathbf{i} + 4\sin t\,\mathbf{j} + t\mathbf{k}; \quad t = \pi/2$

**2.**  
(a) Use the vector triple product identity to show $\mathbf{N}(t) = \frac{\mathbf{u}(t)}{\|\mathbf{u}(t)\|}$ where $\mathbf{u}(t) = \|\mathbf{r}'(t)\|^2\mathbf{r}''(t) - (\mathbf{r}'(t) \cdot \mathbf{r}''(t))\mathbf{r}'(t)$.  
(b) Use part (a) to find $\mathbf{N}(t)$ for:  
(i) $\mathbf{r}(t) = \sin t\,\mathbf{i} + \cos t\,\mathbf{j} + t\mathbf{k}$  
(ii) $\mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j} + t^3\mathbf{k}$

**3. Cornu Spiral in Highway Design:**  
Parametric equations $x = \int_0^t \cos\left(\frac{\pi u^2}{2}\right)du, \quad y = \int_0^t \sin\left(\frac{\pi u^2}{2}\right)du$.  
(a) Express as $\mathbf{r}(t)$ and show $s = t$ is arc length parameter with reference point $(0, 0)$.  
(b) Show $\kappa(s) = \pi|s|$ (linear growth of curvature from straight highway into curved exit ramp).  
(c) Behavior of curvature as $s \to +\infty$.

**4. Roller Coaster Loops (Werner Stengel, 1975):**  
Design of clothoid/Cornu loops for Six Flags Magic Mountain Revolution roller coaster.

**5. Circular Helix Torsion and Binormal Vector:**  
For $\mathbf{r} = a\cos t\,\mathbf{i} + a\sin t\,\mathbf{j} + ct\mathbf{k}$ ($a > 0, w = \sqrt{a^2 + c^2}$), show:
$$\tau = \frac{c}{w^2}, \quad \mathbf{B} = \left(\frac{c}{w}\sin\frac{s}{w}\right)\mathbf{i} - \left(\frac{c}{w}\cos\frac{s}{w}\right)\mathbf{j} + \frac{a}{w}\mathbf{k}$$

**6. Radial and Transverse Components of Velocity and Acceleration in Polar Coordinates:**  
With $\mathbf{r} = r(t)\mathbf{e}_r(t)$ where $\mathbf{e}_r(t) = \cos\theta(t)\mathbf{i} + \sin\theta(t)\mathbf{j}$ and $\mathbf{e}_\theta(t) = -\sin\theta(t)\mathbf{i} + \cos\theta(t)\mathbf{j}$:  
(a) Show $\mathbf{e}_r$ is radial unit vector and $\mathbf{e}_\theta$ is transverse unit vector.  
(b) Show $\mathbf{v} = \frac{dr}{dt}\mathbf{e}_r + r\frac{d\theta}{dt}\mathbf{e}_\theta$.  
(c) Show $\mathbf{a} = \left[\frac{d^2r}{dt^2} - r\left(\frac{d\theta}{dt}\right)^2\right]\mathbf{e}_r + \left[r\frac{d^2\theta}{dt^2} + 2\frac{dr}{dt}\frac{d\theta}{dt}\right]\mathbf{e}_\theta$.

---

## EXPANDING THE CALCULUS HORIZON
*Blammo the Human Cannonball* (available online at `www.wiley.com/college/anton`).
