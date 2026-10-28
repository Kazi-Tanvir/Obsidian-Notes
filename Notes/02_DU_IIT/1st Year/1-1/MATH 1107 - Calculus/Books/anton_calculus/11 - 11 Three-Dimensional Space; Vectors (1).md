# CHAPTER 11: THREE-DIMENSIONAL SPACE; VECTORS

> To describe fully the motion of a boat, one must specify its speed and direction of motion at each instant. Speed and direction together describe a "vector" quantity. We will study vectors in this chapter.

In this chapter we will discuss rectangular coordinate systems in three dimensions, and we will study the analytic geometry of lines, planes, and other basic surfaces. The second theme of this chapter is the study of vectors. These are the mathematical objects that physicists and engineers use to study forces, displacements, and velocities of objects moving on curved paths. More generally, vectors are used to represent all physical entities that involve both a magnitude and a direction for their complete description. We will introduce various algebraic operations on vectors, and we will apply these operations to problems involving force, work, and rotational tendencies in two and three dimensions. Finally, we will discuss cylindrical and spherical coordinate systems, which are appropriate in problems that involve various kinds of symmetries and also have specific applications in navigation and celestial mechanics.

---

## 11.1 RECTANGULAR COORDINATES IN 3-SPACE; SPHERES; CYLINDRICAL SURFACES

In this section we will discuss coordinate systems in three-dimensional space and some basic facts about surfaces in three dimensions.

### RECTANGULAR COORDINATE SYSTEMS

In the remainder of this text we will call three-dimensional space **3-space**, two-dimensional space (a plane) **2-space**, and one-dimensional space (a line) **1-space**. Just as points in 2-space can be placed in one-to-one correspondence with pairs of real numbers using two perpendicular coordinate lines, so points in 3-space can be placed in one-to-one correspondence with triples of real numbers by using three mutually perpendicular coordinate lines, called the **$x$-axis**, the **$y$-axis**, and the **$z$-axis**, positioned so that their origins coincide (Figure 11.1.1). The three coordinate axes form a **three-dimensional rectangular coordinate system** (or Cartesian coordinate system). The point of intersection of the coordinate axes is called the **origin** of the coordinate system.

Rectangular coordinate systems in 3-space fall into two categories: **left-handed** and **right-handed**. A right-handed system has the property that when the fingers of the right hand are cupped so that they curve from the positive $x$-axis toward the positive $y$-axis, the thumb points (roughly) in the direction of the positive $z$-axis (Figure 11.1.2). A similar property holds for a left-handed coordinate system. We will use only right-handed coordinate systems in this text.

The coordinate axes, taken in pairs, determine three **coordinate planes**: the **$xy$-plane**, the **$xz$-plane**, and the **$yz$-plane** (Figure 11.1.3). To each point $P$ in 3-space we can assign a triple of real numbers by passing three planes through $P$ parallel to the coordinate planes and letting $a, b,$ and $c$ be the coordinates of the intersections of those planes with the $x$-axis, $y$-axis, and $z$-axis, respectively (Figure 11.1.4). We call $a, b,$ and $c$ the **$x$-coordinate**, **$y$-coordinate**, and **$z$-coordinate** of $P$, respectively, and we denote the point $P$ by $(a, b, c)$ or by $P(a, b, c)$. Figure 11.1.5 shows the points $(4, 5, 6)$ and $(-3, 2, -4)$.

Just as the coordinate axes in a two-dimensional coordinate system divide 2-space into four quadrants, so the coordinate planes of a three-dimensional coordinate system divide 3-space into eight parts, called **octants**. The set of points with three positive coordinates forms the **first octant**; the remaining octants have no standard numbering.

You should be able to visualize the following facts about three-dimensional rectangular coordinate systems:

| Region | Description |
| :--- | :--- |
| **$xy$-plane** | Consists of all points of the form $(x, y, 0)$ |
| **$xz$-plane** | Consists of all points of the form $(x, 0, z)$ |
| **$yz$-plane** | Consists of all points of the form $(0, y, z)$ |
| **$x$-axis** | Consists of all points of the form $(x, 0, 0)$ |
| **$y$-axis** | Consists of all points of the form $(0, y, 0)$ |
| **$z$-axis** | Consists of all points of the form $(0, 0, z)$ |

---

### DISTANCE IN 3-SPACE; SPHERES

Recall that in 2-space the distance $d$ between the points $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ is
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \tag{1}$$
The distance formula in 3-space has the same form, but it has a third term to account for the added dimension. The distance between the points $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ is
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2} \tag{2}$$

#### Example 1
Find the distance $d$ between the points $(2, 3, -1)$ and $(4, -1, 3)$.

**Solution.** From Formula (2)
$$d = \sqrt{(4 - 2)^2 + (-1 - 3)^2 + (3 + 1)^2} = \sqrt{4 + 16 + 16} = \sqrt{36} = 6$$

Recall that the standard equation of the circle in 2-space that has center $(x_0, y_0)$ and radius $r$ is
$$(x - x_0)^2 + (y - y_0)^2 = r^2 \tag{3}$$
This follows from distance formula (1) and the fact that the circle consists of all points in 2-space whose distance from $(x_0, y_0)$ is $r$. Analogously, the standard equation of the **sphere** in 3-space that has center $(x_0, y_0, z_0)$ and radius $r$ is
$$(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = r^2 \tag{4}$$

| Equation | Graph |
| :--- | :--- |
| $(x - 3)^2 + (y - 2)^2 + (z - 1)^2 = 9$ | Sphere with center $(3, 2, 1)$ and radius 3 |
| $(x + 1)^2 + y^2 + (z + 4)^2 = 5$ | Sphere with center $(-1, 0, -4)$ and radius $\sqrt{5}$ |
| $x^2 + y^2 + z^2 = 1$ | Sphere with center $(0, 0, 0)$ and radius 1 |

If the terms in (4) are expanded and like terms are collected, then the resulting equation has the form
$$x^2 + y^2 + z^2 + Gx + Hy + Iz + J = 0 \tag{5}$$

#### Example 2
Find the center and radius of the sphere $x^2 + y^2 + z^2 - 2x - 4y + 8z + 17 = 0$.

**Solution.** We can put the equation in the form of (4) by completing the squares:
$$(x^2 - 2x) + (y^2 - 4y) + (z^2 + 8z) = -17$$
$$(x^2 - 2x + 1) + (y^2 - 4y + 4) + (z^2 + 8z + 16) = -17 + 21$$
$$(x - 1)^2 + (y - 2)^2 + (z + 4)^2 = 4$$
which is the equation of the sphere with center $(1, 2, -4)$ and radius 2.

In general, completing the squares in (5) produces an equation of the form
$$(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = k$$
* If $k > 0$, the graph is a sphere with center $(x_0, y_0, z_0)$ and radius $\sqrt{k}$.
* If $k = 0$, the sphere has radius zero, so the graph is the single point $(x_0, y_0, z_0)$.
* If $k < 0$, the equation has no graph.

> **11.1.1 THEOREM**  
> An equation of the form $x^2 + y^2 + z^2 + Gx + Hy + Iz + J = 0$ represents a sphere, a point, or has no graph.

---

### CYLINDRICAL SURFACES

The process of generating a surface by translating a plane curve parallel to some line is called **extrusion**, and surfaces that are generated by extrusion are called **cylindrical surfaces**.

> **11.1.2 THEOREM**  
> An equation that contains only two of the variables $x, y,$ and $z$ represents a cylindrical surface in an $xyz$-coordinate system. The surface can be obtained by graphing the equation in the coordinate plane of the two variables that appear in the equation and then translating that graph parallel to the axis of the missing variable.

#### Example 3
Sketch the graph of $x^2 + z^2 = 1$ in 3-space.

**Solution.** Since $y$ does not appear in this equation, the graph is a cylindrical surface generated by extrusion parallel to the $y$-axis. In the $xz$-plane the graph of the equation $x^2 + z^2 = 1$ is a circle. Thus, in 3-space the graph is a right circular cylinder along the $y$-axis (Figure 11.1.7).

#### Example 4
Sketch the graph of $z = \sin y$ in 3-space.

**Solution.** (See Figure 11.1.8.)

---

### QUICK CHECK EXERCISES 11.1
*(See page 773 for answers.)*

1. The distance between the points $(1, -2, 0)$ and $(4, 0, 5)$ is $\underline{\quad}$.
2. The graph of $(x - 3)^2 + (y - 2)^2 + (z + 1)^2 = 16$ is a $\underline{\quad}$ of radius $\underline{\quad}$ centered at $\underline{\quad}$.
3. The shortest distance from the point $(4, 0, 5)$ to the sphere $(x - 1)^2 + (y + 2)^2 + z^2 = 36$ is $\underline{\quad}$.
4. Let $S$ be the graph of $x^2 + z^2 + 6z = 16$ in 3-space.
   (a) The intersection of $S$ with the $xz$-plane is a circle with center $\underline{\quad}$ and radius $\underline{\quad}$.
   (b) The intersection of $S$ with the $xy$-plane is two lines, $x = \underline{\quad}$ and $x = \underline{\quad}$.
   (c) The intersection of $S$ with the $yz$-plane is two lines, $z = \underline{\quad}$ and $z = \underline{\quad}$.

---

### EXERCISE SET 11.1

1. In each part, find the coordinates of the eight corners of the box.  
   (a) Box with corners along axes  
   (b) Box in general position
2. A cube of side 4 has its geometric center at the origin and its faces parallel to the coordinate planes. Sketch the cube and give the coordinates of the corners.

#### FOCUS ON CONCEPTS
3. Suppose that a box has its faces parallel to the coordinate planes and the points $(4, 2, -2)$ and $(-6, 1, 1)$ are endpoints of a diagonal. Sketch the box and give the coordinates of the remaining six corners.
4. Suppose that a box has its faces parallel to the coordinate planes and the points $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$ are endpoints of a diagonal.  
   (a) Find the coordinates of the remaining six corners.  
   (b) Show that the midpoint of the line segment joining $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$ is $\left(\frac{1}{2}(x_1 + x_2), \frac{1}{2}(y_1 + y_2), \frac{1}{2}(z_1 + z_2)\right)$.
5. Interpret the graph of $x = 1$ in the contexts of: (a) a number line, (b) 2-space, (c) 3-space.
6. Consider the points $P(3, 1, 0)$ and $Q(1, 4, 4)$.  
   (a) Sketch the triangle with vertices $P, Q,$ and $(1, 4, 0)$. Without computing distances, explain why this triangle is a right triangle, and then apply the Theorem of Pythagoras twice to find the distance from $P$ to $Q$.  
   (b) Repeat part (a) using the points $P, Q,$ and $(3, 4, 0)$.  
   (c) Repeat part (a) using the points $P, Q,$ and $(1, 1, 4)$.
7. (a) Consider a box whose sides have lengths $a, b,$ and $c$. Use the Theorem of Pythagoras to show that a diagonal of the box has length $d = \sqrt{a^2 + b^2 + c^2}$.  
   (b) Use the result of part (a) to derive formula (2).
8. (a) Make a conjecture about the set of points in 3-space that are equidistant from the origin and the point $(1, 0, 0)$.  
   (b) Confirm your conjecture in part (a) by using distance formula (2).
9. Find the center and radius of the sphere that has $(1, -2, 4)$ and $(3, 4, -12)$ as endpoints of a diameter.
10. Show that $(4, 5, 2), (1, 7, 3),$ and $(2, 4, 5)$ are vertices of an equilateral triangle.
11. (a) Show that $(2, 1, 6), (4, 7, 9),$ and $(8, 5, -6)$ are the vertices of a right triangle.  
    (b) Which vertex is at the $90^\circ$ angle?  
    (c) Find the area of the triangle.
12. Find the distance from the point $(-5, 2, -3)$ to the:  
    (a) $xy$-plane (b) $xz$-plane (c) $yz$-plane (d) $x$-axis (e) $y$-axis (f) $z$-axis.
13. In each part, find the standard equation of the sphere that satisfies the stated conditions:  
    (a) Center $(7, 1, 1)$; radius $= 4$.  
    (b) Center $(1, 0, -1)$; diameter $= 8$.  
    (c) Center $(-1, 3, 2)$ and passing through the origin.  
    (d) A diameter has endpoints $(-1, 2, 1)$ and $(0, 2, 3)$.
14. Find equations of two spheres that are centered at the origin and are tangent to the sphere of radius 1 centered at $(3, -2, 4)$.
15. In each part, find an equation of the sphere with center $(2, -1, -3)$ and satisfying the given condition:  
    (a) Tangent to the $xy$-plane (b) Tangent to the $xz$-plane (c) Tangent to the $yz$-plane.
16. (a) Find an equation of the sphere that is inscribed in the cube that is centered at the point $(-2, 1, 3)$ and has sides of length 1 that are parallel to the coordinate planes.  
    (b) Find an equation of the sphere that is circumscribed about the cube in part (a).  
    (c) Find an equation of the sphere that is inscribed in the cube determined by the planes $x = 6, x = 2, y = 5, y = 9, z = 0,$ and $z = 4$.  
    (d) Find an equation of the sphere that is circumscribed about the cube in part (c).
17. A sphere has center in the first octant and is tangent to each of the three coordinate planes. Show that the center of the sphere is at a point of the form $(r, r, r)$, where $r$ is the radius of the sphere.
18. A sphere has center in the first octant and is tangent to each of the three coordinate planes. The distance from the origin to the sphere is $3 - \sqrt{3}$ units. Find an equation for the sphere.

**19–22 True–False Determine whether the statement is true or false. Explain your answer.**
19. By definition, a "cylindrical surface" is a right circular cylinder whose axis is parallel to one of the coordinate axes.
20. The graph of $x^2 + y^2 = 1$ in 3-space is a circle of radius 1 centered at the origin.
21. If a point belongs to both the $xy$-plane and the $xz$-plane, then the point lies on the $x$-axis.
22. A sphere with center $P(x_0, y_0, z_0)$ and radius $r$ consists of all points $(x, y, z)$ that satisfy the inequality $(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 \le r^2$.

**23–28 Describe the surface whose equation is given.**
23. $x^2 + y^2 + z^2 + 10x + 4y + 2z - 19 = 0$
24. $x^2 + y^2 + z^2 - y = 0$
25. $2x^2 + 2y^2 + 2z^2 - 2x - 3y + 5z - 2 = 0$
26. $x^2 + y^2 + z^2 + 2x - 2y + 2z + 3 = 0$
27. $x^2 + y^2 + z^2 - 3x + 4y - 8z + 25 = 0$
28. $x^2 + y^2 + z^2 - 2x - 6y - 8z + 1 = 0$

**29. In each part, sketch the portion of the surface that lies in the first octant:**  
(a) $y = x$ (b) $y = z$ (c) $x = z$

**30. In each part, sketch the graph of the equation in 3-space:**  
(a) $x = 1$ (b) $y = 1$ (c) $z = 1$

**31. In each part, sketch the graph of the equation in 3-space:**  
(a) $x^2 + y^2 = 25$ (b) $y^2 + z^2 = 25$ (c) $x^2 + z^2 = 25$

**32. In each part, sketch the graph of the equation in 3-space:**  
(a) $x = y^2$ (b) $z = x^2$ (c) $y = z^2$

**33. In each part, write an equation for the surface:**  
(a) The plane that contains the $x$-axis and the point $(0, 1, 2)$.  
(b) The plane that contains the $y$-axis and the point $(1, 0, 2)$.  
(c) The right circular cylinder that has radius 1 and is centered on the line parallel to the $z$-axis that passes through the point $(1, 1, 0)$.  
(d) The right circular cylinder that has radius 1 and is centered on the line parallel to the $y$-axis that passes through the point $(1, 0, 1)$.

**34. Find equations for the right circular cylinders shown, each having radius $a$ and tangent to two coordinate planes:**  
(a) Tangent to $xy$- and $yz$-planes, center along $(a, 0, a)$  
(b) Tangent to $xz$- and $yz$-planes, center along $(a, a, 0)$  
(c) Tangent to $xy$- and $xz$-planes, center along $(0, a, a)$

**35–44 Sketch the surface in 3-space.**
35. $y = \sin x$
36. $y = e^x$
37. $z = 1 - y^2$
38. $z = \cos x$
39. $2x + z = 3$
40. $2x + 3y = 6$
41. $4x^2 + 9z^2 = 36$
42. $z = \sqrt{3 - x}$
43. $y^2 - 4z^2 = 4$
44. $yz = 1$

45. Use a graphing utility to generate the curve $y = x^3/(1 + x^2)$ in the $xy$-plane, and then use the graph to help sketch the surface $z = y^3/(1 + y^2)$ in 3-space.
46. Use a graphing utility to generate the curve $y = x/(1 + x^4)$ in the $xy$-plane, and then use the graph to help sketch the surface $z = y/(1 + y^4)$ in 3-space.
47. If a bug walks on the sphere $x^2 + y^2 + z^2 + 2x - 2y - 4z - 3 = 0$, how close and how far can it get from the origin?
48. Describe the set of all points in 3-space whose coordinates satisfy the inequality $x^2 + y^2 + z^2 - 2x + 8z \le 8$.
49. Describe the set of all points in 3-space whose coordinates satisfy the inequality $y^2 + z^2 + 6y - 4z > 3$.
50. The distance between a point $P(x, y, z)$ and the point $A(1, -2, 0)$ is twice the distance between $P$ and the point $B(0, 1, 1)$. Show that the set of all such points is a sphere, and find the center and radius of the sphere.
51. As shown in the accompanying figure, a bowling ball of radius $R$ is placed inside a box just large enough to hold it, and it is secured for shipping by packing a Styrofoam sphere into each corner of the box. Find the radius of the largest Styrofoam sphere that can be used.
52. Consider the equation $x^2 + y^2 + z^2 + Gx + Hy + Iz + J = 0$ and let $K = G^2 + H^2 + I^2 - 4J$.  
    (a) Prove that the equation represents a sphere if $K > 0$, a point if $K = 0$, and has no graph if $K < 0$.  
    (b) In the case where $K > 0$, find the center and radius of the sphere.
53. (a) Show that the equation of the surface of revolution generated by revolving $y = f(x)$ in the $xy$-plane about the $x$-axis is $y^2 + z^2 = [f(x)]^2$.  
    (b) Find an equation of the surface of revolution generated by revolving $y = e^x$ in the $xy$-plane about the $x$-axis.  
    (c) Show that the ellipsoid $3x^2 + 4y^2 + 4z^2 = 16$ is a surface of revolution about the $x$-axis by finding a curve $y = f(x)$ in the $xy$-plane that generates it.
54. In each part, derive a formula for the stated surface of revolution:  
    (a) Revolve $x = f(y)$ in the $xy$-plane about the $y$-axis.  
    (b) Revolve $y = f(z)$ in the $yz$-plane about the $z$-axis.  
    (c) Revolve $z = f(x)$ in the $xz$-plane about the $x$-axis.
55. Show that for all values of $\theta$ and $\phi$, the point $(a\sin\phi\cos\theta, a\sin\phi\sin\theta, a\cos\phi)$ lies on the sphere $x^2 + y^2 + z^2 = a^2$.
56. **Writing.** Explain how you might determine whether a set of points in 3-space is the graph of an equation involving at most two of the variables $x, y,$ and $z$.
57. **Writing.** Discuss what happens geometrically when equations in $x, y,$ and $z$ are replaced by inequalities.

#### QUICK CHECK ANSWERS 11.1
1. $\sqrt{38}$  
2. sphere; 4; $(3, 2, -1)$  
3. $\sqrt{38} - 6$  
4. (a) $(0, 0, -3); 5$ (b) $4; -4$ (c) $2; -8$

---

## 11.2 VECTORS

Many physical quantities such as area, length, mass, and temperature are completely described once the magnitude of the quantity is given. Such quantities are called **"scalars."** Other physical quantities, called **"vectors,"** are not completely determined until both a magnitude and a direction are specified. For example, winds are usually described by giving their speed and direction, say $20\text{ mi/h}$ northeast. The wind speed and wind direction together form a vector quantity called the wind velocity. Other examples of vectors are force and displacement. In this section we will develop the basic mathematical properties of vectors.

### VECTORS IN PHYSICS AND ENGINEERING

A particle that moves along a line can move in only two directions, so its direction of motion can be described by taking one direction to be positive and the other negative. Thus, the displacement or change in position of the point can be described by a signed real number. For example, a displacement of $3$ ($=+3$) describes a position change of $3$ units in the positive direction, and a displacement of $-3$ describes a position change of $3$ units in the negative direction. However, for a particle that moves in two dimensions or three dimensions, a plus or minus sign is no longer sufficient to specify the direction of motion—other methods are required. One method is to use an arrow, called a **vector**, that points in the direction of motion and whose length represents the distance from the starting point to the ending point; this is called the **displacement vector** for the motion. For example, Figure 11.2.1a shows the displacement vector of a particle that moves from point $A$ to point $B$ along a circuitous path. Note that the length of the arrow describes the distance between the starting and ending points and not the actual distance traveled by the particle.

Arrows are not limited to describing displacements—they can be used to describe any physical quantity that involves both a magnitude and a direction. Two important examples are forces and velocities. For example, the arrow in Figure 11.2.1b represents a force vector of $10\text{ lb}$ acting in a specific direction on a block, and the arrows in Figure 11.2.1c show the velocity vector of a boat whose motor propels it parallel to the shore at $2\text{ mi/h}$ and the velocity vector of a $3\text{ mi/h}$ wind acting at an angle of $45^\circ$ with the shoreline. Intuition suggests that the two velocity vectors will combine to produce some net velocity for the boat at an angle to the shoreline. Thus, our first objective in this section is to define mathematical operations on vectors that can be used to determine the combined effect of vectors.

### VECTORS VIEWED GEOMETRICALLY

Vectors can be represented geometrically by arrows in 2-space or 3-space; the direction of the arrow specifies the direction of the vector, and the length of the arrow describes its magnitude. The tail of the arrow is called the **initial point** of the vector, and the tip of the arrow the **terminal point**. We will denote vectors with lowercase boldface type such as $\mathbf{a}, \mathbf{k}, \mathbf{v}, \mathbf{w},$ and $\mathbf{x}$. When discussing vectors, we will refer to real numbers as **scalars**. Scalars will be denoted by lowercase italic type such as $a, k, v, w,$ and $x$. Two vectors, $\mathbf{v}$ and $\mathbf{w}$, are considered to be **equal** (also called **equivalent**) if they have the same length and same direction, in which case we write $\mathbf{v} = \mathbf{w}$. Geometrically, two vectors are equal if they are translations of one another; thus, the three vectors in Figure 11.2.2a are equal, even though they are in different positions.

Because vectors are not affected by translation, the initial point of a vector $\mathbf{v}$ can be moved to any convenient point $A$ by making an appropriate translation. If the initial point of $\mathbf{v}$ is $A$ and the terminal point is $B$, then we write $\mathbf{v} = \vec{AB}$ when we want to emphasize the initial and terminal points (Figure 11.2.2b). If the initial and terminal points of a vector coincide, then the vector has length zero; we call this the **zero vector** and denote it by $\mathbf{0}$. The zero vector does not have a specific direction, so we will agree that it can be assigned any convenient direction in a specific problem.

There are various algebraic operations that are performed on vectors, all of whose definitions originated in physics. We begin with vector addition.

> **11.2.1 DEFINITION**  
> If $\mathbf{v}$ and $\mathbf{w}$ are vectors, then the **sum** $\mathbf{v} + \mathbf{w}$ is the vector from the initial point of $\mathbf{v}$ to the terminal point of $\mathbf{w}$ when the vectors are positioned so the initial point of $\mathbf{w}$ is at the terminal point of $\mathbf{v}$ (Figure 11.2.3a).

In Figure 11.2.3b we have constructed two sums, $\mathbf{v} + \mathbf{w}$ (from purple arrows) and $\mathbf{w} + \mathbf{v}$ (from green arrows). It is evident that
$$\mathbf{v} + \mathbf{w} = \mathbf{w} + \mathbf{v}$$
and that the sum (gray arrow) coincides with the diagonal of the parallelogram determined by $\mathbf{v}$ and $\mathbf{w}$ when these vectors are positioned so they have the same initial point.
Since the initial and terminal points of $\mathbf{0}$ coincide, it follows that
$$\mathbf{0} + \mathbf{v} = \mathbf{v} + \mathbf{0} = \mathbf{v}$$

> **11.2.2 DEFINITION**  
> If $\mathbf{v}$ is a nonzero vector and $k$ is a nonzero real number (a scalar), then the **scalar multiple** $k\mathbf{v}$ is defined to be the vector whose length is $|k|$ times the length of $\mathbf{v}$ and whose direction is the same as that of $\mathbf{v}$ if $k > 0$ and opposite to that of $\mathbf{v}$ if $k < 0$. We define $k\mathbf{v} = \mathbf{0}$ if $k = 0$ or $\mathbf{v} = \mathbf{0}$.

Figure 11.2.4 shows the geometric relationship between a vector $\mathbf{v}$ and various scalar multiples of it. Observe that if $k$ and $\mathbf{v}$ are nonzero, then the vectors $\mathbf{v}$ and $k\mathbf{v}$ lie on the same line if their initial points coincide and lie on parallel or coincident lines if they do not. Thus, we say that $\mathbf{v}$ and $k\mathbf{v}$ are **parallel vectors**. Observe also that the vector $(-1)\mathbf{v}$ has the same length as $\mathbf{v}$ but is oppositely directed. We call $(-1)\mathbf{v}$ the **negative** of $\mathbf{v}$ and denote it by $-\mathbf{v}$ (Figure 11.2.5). In particular, $-\mathbf{0} = (-1)\mathbf{0} = \mathbf{0}$.

Vector subtraction is defined in terms of addition and scalar multiplication by
$$\mathbf{v} - \mathbf{w} = \mathbf{v} + (-\mathbf{w})$$
The difference $\mathbf{v} - \mathbf{w}$ can be obtained geometrically by first constructing the vector $-\mathbf{w}$ and then adding $\mathbf{v}$ and $-\mathbf{w}$, say by the parallelogram method (Figure 11.2.6a). However, if $\mathbf{v}$ and $\mathbf{w}$ are positioned so their initial points coincide, then $\mathbf{v} - \mathbf{w}$ can be formed more directly, as shown in Figure 11.2.6b, by drawing the vector from the terminal point of $\mathbf{w}$ (the second term) to the terminal point of $\mathbf{v}$ (the first term). In the special case where $\mathbf{v} = \mathbf{w}$ the terminal points of the vectors coincide, so their difference is $\mathbf{0}$; that is,
$$\mathbf{v} + (-\mathbf{v}) = \mathbf{v} - \mathbf{v} = \mathbf{0}$$

---

### VECTORS IN COORDINATE SYSTEMS

Problems involving vectors are often best solved by introducing a rectangular coordinate system. If a vector $\mathbf{v}$ is positioned with its initial point at the origin of a rectangular coordinate system, then its terminal point will have coordinates of the form $(v_1, v_2)$ or $(v_1, v_2, v_3)$, depending on whether the vector is in 2-space or 3-space (Figure 11.2.7). We call these coordinates the **components** of $\mathbf{v}$, and we write $\mathbf{v}$ in **component form** using the bracket notation
$$\mathbf{v} = \langle v_1, v_2 \rangle \quad \text{or} \quad \mathbf{v} = \langle v_1, v_2, v_3 \rangle$$
In particular, the zero vectors in 2-space and 3-space are
$$\mathbf{0} = \langle 0, 0 \rangle \quad \text{and} \quad \mathbf{0} = \langle 0, 0, 0 \rangle$$
respectively.

Components provide a simple way of identifying equivalent vectors. For example, consider the vectors $\mathbf{v} = \langle v_1, v_2 \rangle$ and $\mathbf{w} = \langle w_1, w_2 \rangle$ in 2-space. If $\mathbf{v} = \mathbf{w}$, then the vectors have the same length and same direction, and this means that their terminal points coincide when their initial points are placed at the origin. It follows that $v_1 = w_1$ and $v_2 = w_2$, so we have shown that equivalent vectors have the same components. Conversely, if $v_1 = w_1$ and $v_2 = w_2$, then the terminal points of the vectors coincide when their initial points are placed at the origin. It follows that the vectors have the same length and same direction, so we have shown that vectors with the same components are equivalent. A similar argument holds for vectors in 3-space, so we have the following result.

> **11.2.3 THEOREM**  
> Two vectors are equivalent if and only if their corresponding components are equal.

For example, $\langle a, b, c \rangle = \langle 1, -4, 2 \rangle$ if and only if $a = 1, b = -4,$ and $c = 2$.

---

### ARITHMETIC OPERATIONS ON VECTORS

The next theorem shows how to perform arithmetic operations on vectors using components.

> **11.2.4 THEOREM**  
> If $\mathbf{v} = \langle v_1, v_2 \rangle$ and $\mathbf{w} = \langle w_1, w_2 \rangle$ are vectors in 2-space and $k$ is any scalar, then
> $$\mathbf{v} + \mathbf{w} = \langle v_1 + w_1, v_2 + w_2 \rangle \tag{1}$$
> $$\mathbf{v} - \mathbf{w} = \langle v_1 - w_1, v_2 - w_2 \rangle \tag{2}$$
> $$k\mathbf{v} = \langle kv_1, kv_2 \rangle \tag{3}$$
> Similarly, if $\mathbf{v} = \langle v_1, v_2, v_3 \rangle$ and $\mathbf{w} = \langle w_1, w_2, w_3 \rangle$ are vectors in 3-space and $k$ is any scalar, then
> $$\mathbf{v} + \mathbf{w} = \langle v_1 + w_1, v_2 + w_2, v_3 + w_3 \rangle \tag{4}$$
> $$\mathbf{v} - \mathbf{w} = \langle v_1 - w_1, v_2 - w_2, v_3 - w_3 \rangle \tag{5}$$
> $$k\mathbf{v} = \langle kv_1, kv_2, kv_3 \rangle \tag{6}$$

#### Example 1
If $\mathbf{v} = \langle -2, 0, 1 \rangle$ and $\mathbf{w} = \langle 3, 5, -4 \rangle$, then
* $\mathbf{v} + \mathbf{w} = \langle -2, 0, 1 \rangle + \langle 3, 5, -4 \rangle = \langle 1, 5, -3 \rangle$
* $3\mathbf{v} = \langle -6, 0, 3 \rangle$
* $-\mathbf{w} = \langle -3, -5, 4 \rangle$
* $\mathbf{w} - 2\mathbf{v} = \langle 3, 5, -4 \rangle - \langle -4, 0, 2 \rangle = \langle 7, 5, -6 \rangle$

---

### VECTORS WITH INITIAL POINT NOT AT THE ORIGIN

Recall that we defined the components of a vector to be the coordinates of its terminal point when its initial point is at the origin. We will now consider the problem of finding the components of a vector whose initial point is not at the origin. To be specific, suppose that $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ are points in 2-space and we are interested in finding the components of the vector $\vec{P_1P_2}$. As illustrated in Figure 11.2.9, we can write this vector as
$$\vec{P_1P_2} = \vec{OP_2} - \vec{OP_1} = \langle x_2, y_2 \rangle - \langle x_1, y_1 \rangle = \langle x_2 - x_1, y_2 - y_1 \rangle$$
Thus, we have shown that the components of the vector $\vec{P_1P_2}$ can be obtained by subtracting the coordinates of its initial point from the coordinates of its terminal point. Similar computations hold in 3-space, so we have established the following result.

> **11.2.5 THEOREM**  
> If $\vec{P_1P_2}$ is a vector in 2-space with initial point $P_1(x_1, y_1)$ and terminal point $P_2(x_2, y_2)$, then
> $$\vec{P_1P_2} = \langle x_2 - x_1, y_2 - y_1 \rangle \tag{7}$$
> Similarly, if $\vec{P_1P_2}$ is a vector in 3-space with initial point $P_1(x_1, y_1, z_1)$ and terminal point $P_2(x_2, y_2, z_2)$, then
> $$\vec{P_1P_2} = \langle x_2 - x_1, y_2 - y_1, z_2 - z_1 \rangle \tag{8}$$

#### Example 2
In 2-space the vector from $P_1(1, 3)$ to $P_2(4, -2)$ is
$$\vec{P_1P_2} = \langle 4 - 1, -2 - 3 \rangle = \langle 3, -5 \rangle$$
and in 3-space the vector from $A(0, -2, 5)$ to $B(3, 4, -1)$ is
$$\vec{AB} = \langle 3 - 0, 4 - (-2), -1 - 5 \rangle = \langle 3, 6, -6 \rangle$$

---

### RULES OF VECTOR ARITHMETIC

> **11.2.6 THEOREM**  
> For any vectors $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ and any scalars $k$ and $l$, the following relationships hold:
> (a) $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$  
> (b) $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$  
> (c) $\mathbf{u} + \mathbf{0} = \mathbf{0} + \mathbf{u} = \mathbf{u}$  
> (d) $\mathbf{u} + (-\mathbf{u}) = \mathbf{0}$  
> (e) $k(l\mathbf{u}) = (kl)\mathbf{u}$  
> (f) $k(\mathbf{u} + \mathbf{v}) = k\mathbf{u} + k\mathbf{v}$  
> (g) $(k + l)\mathbf{u} = k\mathbf{u} + l\mathbf{u}$  
> (h) $1\mathbf{u} = \mathbf{u}$

**PROOF (b) (Algebraic in 2-space)**  
Let $\mathbf{u} = \langle u_1, u_2 \rangle, \mathbf{v} = \langle v_1, v_2 \rangle,$ and $\mathbf{w} = \langle w_1, w_2 \rangle$. Then
$$(\mathbf{u} + \mathbf{v}) + \mathbf{w} = (\langle u_1, u_2 \rangle + \langle v_1, v_2 \rangle) + \langle w_1, w_2 \rangle$$
$$= \langle u_1 + v_1, u_2 + v_2 \rangle + \langle w_1, w_2 \rangle$$
$$= \langle (u_1 + v_1) + w_1, (u_2 + v_2) + w_2 \rangle$$
$$= \langle u_1 + (v_1 + w_1), u_2 + (v_2 + w_2) \rangle$$
$$= \langle u_1, u_2 \rangle + \langle v_1 + w_1, v_2 + w_2 \rangle = \mathbf{u} + (\mathbf{v} + \mathbf{w})$$

**PROOF (b) (Geometric)**  
Let $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ be represented by $\vec{PQ}, \vec{QR},$ and $\vec{RS}$ as shown in Figure 11.2.10. Then
$$\mathbf{v} + \mathbf{w} = \vec{QS} \quad \text{and} \quad \mathbf{u} + (\mathbf{v} + \mathbf{w}) = \vec{PS}$$
$$\mathbf{u} + \mathbf{v} = \vec{PR} \quad \text{and} \quad (\mathbf{u} + \mathbf{v}) + \mathbf{w} = \vec{PS}$$
Therefore, $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$. $\blacksquare$

---

### NORM OF A VECTOR

The distance between the initial and terminal points of a vector $\mathbf{v}$ is called the **length**, the **norm**, or the **magnitude** of $\mathbf{v}$ and is denoted by $\|\mathbf{v}\|$. This distance does not change if the vector is translated, so for purposes of calculating the norm we can assume that the vector is positioned with its initial point at the origin (Figure 11.2.12). This makes it evident that the norm of a vector $\mathbf{v} = \langle v_1, v_2 \rangle$ in 2-space is given by
$$\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2} \tag{9}$$
and the norm of a vector $\mathbf{v} = \langle v_1, v_2, v_3 \rangle$ in 3-space is given by
$$\|\mathbf{v}\| = \sqrt{v_1^2 + v_2^2 + v_3^2} \tag{10}$$

#### Example 3
Find the norms of $\mathbf{v} = \langle -2, 3 \rangle, 10\mathbf{v} = \langle -20, 30 \rangle,$ and $\mathbf{w} = \langle 2, 3, 6 \rangle$.

**Solution.** From (9) and (10)
$$\|\mathbf{v}\| = \sqrt{(-2)^2 + 3^2} = \sqrt{13}$$
$$\|10\mathbf{v}\| = \sqrt{(-20)^2 + 30^2} = \sqrt{1300} = 10\sqrt{13}$$
$$\|\mathbf{w}\| = \sqrt{2^2 + 3^2 + 6^2} = \sqrt{49} = 7$$

Note that $\|10\mathbf{v}\| = 10\|\mathbf{v}\|$ in Example 3. This is consistent with Definition 11.2.2, which stipulated that for any vector $\mathbf{v}$ and scalar $k$, the length of $k\mathbf{v}$ must be $|k|$ times the length of $\mathbf{v}$; that is,
$$\|k\mathbf{v}\| = |k|\|\mathbf{v}\| \tag{11}$$
Thus, for example, $\|3\mathbf{v}\| = |3|\|\mathbf{v}\| = 3\|\mathbf{v}\|$, $\|-2\mathbf{v}\| = |-2|\|\mathbf{v}\| = 2\|\mathbf{v}\|$, and $\|-1\mathbf{v}\| = |-1|\|\mathbf{v}\| = \|\mathbf{v}\|$.

---

### UNIT VECTORS

A vector of length 1 is called a **unit vector**. In an $xy$-coordinate system the unit vectors along the $x$- and $y$-axes are denoted by $\mathbf{i}$ and $\mathbf{j}$, respectively; and in an $xyz$-coordinate system the unit vectors along the $x$-, $y$-, and $z$-axes are denoted by $\mathbf{i}, \mathbf{j},$ and $\mathbf{k}$, respectively (Figure 11.2.13). Thus,
$$\mathbf{i} = \langle 1, 0 \rangle, \quad \mathbf{j} = \langle 0, 1 \rangle \quad (\text{In 2-space})$$
$$\mathbf{i} = \langle 1, 0, 0 \rangle, \quad \mathbf{j} = \langle 0, 1, 0 \rangle, \quad \mathbf{k} = \langle 0, 0, 1 \rangle \quad (\text{In 3-space})$$

Every vector in 2-space is expressible uniquely in terms of $\mathbf{i}$ and $\mathbf{j}$, and every vector in 3-space is expressible uniquely in terms of $\mathbf{i}, \mathbf{j},$ and $\mathbf{k}$ as follows:
$$\mathbf{v} = \langle v_1, v_2 \rangle = \langle v_1, 0 \rangle + \langle 0, v_2 \rangle = v_1\langle 1, 0 \rangle + v_2\langle 0, 1 \rangle = v_1\mathbf{i} + v_2\mathbf{j}$$
$$\mathbf{v} = \langle v_1, v_2, v_3 \rangle = v_1\langle 1, 0, 0 \rangle + v_2\langle 0, 1, 0 \rangle + v_3\langle 0, 0, 1 \rangle = v_1\mathbf{i} + v_2\mathbf{j} + v_3\mathbf{k}$$

#### Example 4
The following table provides some examples of vector notation in 2-space and 3-space:

| 2-SPACE | 3-SPACE |
| :--- | :--- |
| $\langle 2, 3 \rangle = 2\mathbf{i} + 3\mathbf{j}$ | $\langle 2, -3, 4 \rangle = 2\mathbf{i} - 3\mathbf{j} + 4\mathbf{k}$ |
| $\langle -4, 0 \rangle = -4\mathbf{i} + 0\mathbf{j} = -4\mathbf{i}$ | $\langle 0, 3, 0 \rangle = 3\mathbf{j}$ |
| $\langle 0, 0 \rangle = 0\mathbf{i} + 0\mathbf{j} = \mathbf{0}$ | $\langle 0, 0, 0 \rangle = 0\mathbf{i} + 0\mathbf{j} + 0\mathbf{k} = \mathbf{0}$ |
| $(3\mathbf{i} + 2\mathbf{j}) + (4\mathbf{i} + \mathbf{j}) = 7\mathbf{i} + 3\mathbf{j}$ | $(3\mathbf{i} + 2\mathbf{j} - \mathbf{k}) - (4\mathbf{i} - \mathbf{j} + 2\mathbf{k}) = -\mathbf{i} + 3\mathbf{j} - 3\mathbf{k}$ |
| $5(6\mathbf{i} - 2\mathbf{j}) = 30\mathbf{i} - 10\mathbf{j}$ | $2(\mathbf{i} + \mathbf{j} - \mathbf{k}) + 4(\mathbf{i} - \mathbf{j}) = 6\mathbf{i} - 2\mathbf{j} - 2\mathbf{k}$ |
| $\|2\mathbf{i} - 3\mathbf{j}\| = \sqrt{2^2 + (-3)^2} = \sqrt{13}$ | $\|\mathbf{i} + 2\mathbf{j} - 3\mathbf{k}\| = \sqrt{1^2 + 2^2 + (-3)^2} = \sqrt{14}$ |
| $\|v_1\mathbf{i} + v_2\mathbf{j}\| = \sqrt{v_1^2 + v_2^2}$ | $\|\langle v_1, v_2, v_3 \rangle\| = \sqrt{v_1^2 + v_2^2 + v_3^2}$ |

---

### NORMALIZING A VECTOR

A common problem in applications is to find a unit vector $\mathbf{u}$ that has the same direction as some given nonzero vector $\mathbf{v}$. This can be done by multiplying $\mathbf{v}$ by the reciprocal of its length; that is,
$$\mathbf{u} = \frac{1}{\|\mathbf{v}\|}\mathbf{v} = \frac{\mathbf{v}}{\|\mathbf{v}\|}$$
is a unit vector with the same direction as $\mathbf{v}$—the direction is the same because $k = 1/\|\mathbf{v}\|$ is a positive scalar, and the length is 1 because
$$\|\mathbf{u}\| = \|k\mathbf{v}\| = |k|\|\mathbf{v}\| = k\|\mathbf{v}\| = \frac{1}{\|\mathbf{v}\|}\|\mathbf{v}\| = 1$$
The process of multiplying a vector $\mathbf{v}$ by the reciprocal of its length to obtain a unit vector with the same direction is called **normalizing** $\mathbf{v}$.

#### Example 5
Find the unit vector that has the same direction as $\mathbf{v} = 2\mathbf{i} + 2\mathbf{j} - \mathbf{k}$.

**Solution.** The vector $\mathbf{v}$ has length
$$\|\mathbf{v}\| = \sqrt{2^2 + 2^2 + (-1)^2} = 3$$
so the unit vector $\mathbf{u}$ in the same direction as $\mathbf{v}$ is
$$\mathbf{u} = \frac{1}{3}\mathbf{v} = \frac{2}{3}\mathbf{i} + \frac{2}{3}\mathbf{j} - \frac{1}{3}\mathbf{k}$$

---

### VECTORS DETERMINED BY LENGTH AND ANGLE

If $\mathbf{v}$ is a nonzero vector with its initial point at the origin of an $xy$-coordinate system, and if $\theta$ is the angle from the positive $x$-axis to the radial line through $\mathbf{v}$, then the $x$-component of $\mathbf{v}$ can be written as $\|\mathbf{v}\|\cos\theta$ and the $y$-component as $\|\mathbf{v}\|\sin\theta$ (Figure 11.2.14); and hence $\mathbf{v}$ can be expressed in trigonometric form as
$$\mathbf{v} = \|\mathbf{v}\|\langle \cos\theta, \sin\theta \rangle \quad \text{or} \quad \mathbf{v} = \|\mathbf{v}\|\cos\theta\mathbf{i} + \|\mathbf{v}\|\sin\theta\mathbf{j} \tag{12}$$
In the special case of a unit vector $\mathbf{u}$ this simplifies to
$$\mathbf{u} = \langle \cos\theta, \sin\theta \rangle \quad \text{or} \quad \mathbf{u} = \cos\theta\mathbf{i} + \sin\theta\mathbf{j} \tag{13}$$

#### Example 6
(a) Find the vector of length 2 that makes an angle of $\pi/4$ with the positive $x$-axis.  
(b) Find the angle that the vector $\mathbf{v} = -\sqrt{3}\mathbf{i} + \mathbf{j}$ makes with the positive $x$-axis.

**Solution (a).** From (12)
$$\mathbf{v} = 2\cos\frac{\pi}{4}\mathbf{i} + 2\sin\frac{\pi}{4}\mathbf{j} = \sqrt{2}\mathbf{i} + \sqrt{2}\mathbf{j}$$

**Solution (b).** We will normalize $\mathbf{v}$, then use (13) to find $\sin\theta$ and $\cos\theta$, and then use these values to find $\theta$. Normalizing $\mathbf{v}$ yields
$$\frac{\mathbf{v}}{\|\mathbf{v}\|} = \frac{-\sqrt{3}\mathbf{i} + \mathbf{j}}{\sqrt{(-\sqrt{3})^2 + 1^2}} = -\frac{\sqrt{3}}{2}\mathbf{i} + \frac{1}{2}\mathbf{j}$$
Thus, $\cos\theta = -\sqrt{3}/2$ and $\sin\theta = 1/2$, from which we conclude that $\theta = 5\pi/6$.

---

### VECTORS DETERMINED BY LENGTH AND A VECTOR IN THE SAME DIRECTION

It is a common problem in many applications that a direction in 2-space or 3-space is determined by some known unit vector $\mathbf{u}$, and it is of interest to find the components of a vector $\mathbf{v}$ that has the same direction as $\mathbf{u}$ and some specified length $\|\mathbf{v}\|$. This can be done by expressing $\mathbf{v}$ as
$$\mathbf{v} = \|\mathbf{v}\|\mathbf{u}$$
and then reading off the components of $\|\mathbf{v}\|\mathbf{u}$.

#### Example 7
Figure 11.2.15 shows a vector $\mathbf{v}$ of length $\sqrt{5}$ that extends along the line through $A(0, 0, 4)$ and $B(2, 5, 0)$. Find the components of $\mathbf{v}$.

**Solution.** First we will find the components of the vector $\vec{AB}$, then we will normalize this vector to obtain a unit vector in the direction of $\mathbf{v}$, and then we will multiply this unit vector by $\|\mathbf{v}\|$ to obtain the vector $\mathbf{v}$. The computations are as follows:
$$\vec{AB} = \langle 2, 5, 0 \rangle - \langle 0, 0, 4 \rangle = \langle 2, 5, -4 \rangle$$
$$\|\vec{AB}\| = \sqrt{2^2 + 5^2 + (-4)^2} = \sqrt{45} = 3\sqrt{5}$$
$$\frac{\vec{AB}}{\|\vec{AB}\|} = \left\langle \frac{2}{3\sqrt{5}}, \frac{5}{3\sqrt{5}}, -\frac{4}{3\sqrt{5}} \right\rangle$$
$$\mathbf{v} = \|\mathbf{v}\|\left(\frac{\vec{AB}}{\|\vec{AB}\|}\right) = \sqrt{5}\left\langle \frac{2}{3\sqrt{5}}, \frac{5}{3\sqrt{5}}, -\frac{4}{3\sqrt{5}} \right\rangle = \left\langle \frac{2}{3}, \frac{5}{3}, -\frac{4}{3} \right\rangle$$

---

### RESULTANT OF TWO CONCURRENT FORCES

The effect that a force has on an object depends on the magnitude and direction of the force and the point at which it is applied. Thus, forces are regarded to be vector quantities and, indeed, the algebraic operations on vectors that we have defined in this section have their origin in the study of forces. For example, it is a fact of physics that if two forces $\mathbf{F}_1$ and $\mathbf{F}_2$ are applied at the same point on an object, then the two forces have the same effect on the object as the single force $\mathbf{F}_1 + \mathbf{F}_2$ applied at the point (Figure 11.2.16). Physicists and engineers call $\mathbf{F}_1 + \mathbf{F}_2$ the **resultant** of $\mathbf{F}_1$ and $\mathbf{F}_2$, and they say that the forces $\mathbf{F}_1$ and $\mathbf{F}_2$ are **concurrent** to indicate that they are applied at the same point.

In many applications, the magnitudes of two concurrent forces and the angle between them are known, and the problem is to find the magnitude and direction of the resultant. One approach to solving this problem is to use (12) to find the components of the concurrent forces, and then use (1) to find the components of the resultant. The next example illustrates this method.

#### Example 8
Suppose that two forces are applied to an eye bracket, as shown in Figure 11.2.17. Find the magnitude of the resultant and the angle $\theta$ that it makes with the positive $x$-axis.

**Solution.** Note that $\mathbf{F}_1$ makes an angle of $30^\circ$ with the positive $x$-axis and $\mathbf{F}_2$ makes an angle of $30^\circ + 40^\circ = 70^\circ$ with the positive $x$-axis. Since we are given that $\|\mathbf{F}_1\| = 200\text{ N}$ and $\|\mathbf{F}_2\| = 300\text{ N}$, (12) yields
$$\mathbf{F}_1 = 200\langle \cos 30^\circ, \sin 30^\circ \rangle = \langle 100\sqrt{3}, 100 \rangle$$
$$\mathbf{F}_2 = 300\langle \cos 70^\circ, \sin 70^\circ \rangle = \langle 300\cos 70^\circ, 300\sin 70^\circ \rangle$$
Therefore, the resultant $\mathbf{F} = \mathbf{F}_1 + \mathbf{F}_2$ has component form
$$\mathbf{F} = \mathbf{F}_1 + \mathbf{F}_2 = \langle 100\sqrt{3} + 300\cos 70^\circ, 100 + 300\sin 70^\circ \rangle$$
$$= 100\langle \sqrt{3} + 3\cos 70^\circ, 1 + 3\sin 70^\circ \rangle \approx \langle 275.8, 381.9 \rangle$$
The magnitude of the resultant is then
$$\|\mathbf{F}\| = 100\sqrt{(\sqrt{3} + 3\cos 70^\circ)^2 + (1 + 3\sin 70^\circ)^2} \approx 471\text{ N}$$
Let $\theta$ denote the angle $\mathbf{F}$ makes with the positive $x$-axis when the initial point of $\mathbf{F}$ is at the origin. Using (12) and equating the $x$-components of $\mathbf{F}$ yield
$$\|\mathbf{F}\|\cos\theta = 100\sqrt{3} + 300\cos 70^\circ \quad \text{or} \quad \cos\theta = \frac{100\sqrt{3} + 300\cos 70^\circ}{\|\mathbf{F}\|}$$
Since the terminal point of $\mathbf{F}$ is in the first quadrant, we have
$$\theta = \cos^{-1}\left(\frac{100\sqrt{3} + 300\cos 70^\circ}{\|\mathbf{F}\|}\right) \approx 54.2^\circ$$

---

### QUICK CHECK EXERCISES 11.2
*(See page 785 for answers.)*

1. If $\mathbf{v} = \langle 3, -1, 7 \rangle$ and $\mathbf{w} = \langle 4, 10, -5 \rangle$, then:  
   (a) $\|\mathbf{v}\| = \underline{\quad}$  
   (b) $\mathbf{v} + \mathbf{w} = \underline{\quad}$  
   (c) $\mathbf{v} - \mathbf{w} = \underline{\quad}$  
   (d) $2\mathbf{v} = \underline{\quad}$.
2. The unit vector in the direction of $\mathbf{v} = \langle 3, -1, 7 \rangle$ is $\underline{\quad}$.
3. The unit vector in 2-space that makes an angle of $\pi/3$ with the positive $x$-axis is $\underline{\quad}$.
4. Consider points $A(3, 4, 0)$ and $B(0, 0, 5)$.  
   (a) $\vec{AB} = \underline{\quad}$  
   (b) If $\mathbf{v}$ is a vector in the same direction as $\vec{AB}$ and the length of $\mathbf{v}$ is $\sqrt{2}$, then $\mathbf{v} = \underline{\quad}$.

---

### EXERCISE SET 11.2

**1–4 Sketch the vectors with their initial points at the origin.**
1. (a) $\langle 2, 5 \rangle$ (b) $\langle -5, -4 \rangle$ (c) $\langle 2, 0 \rangle$ (d) $-5\mathbf{i} + 3\mathbf{j}$ (e) $3\mathbf{i} - 2\mathbf{j}$ (f) $-6\mathbf{j}$
2. (a) $\langle -3, 7 \rangle$ (b) $\langle 6, -2 \rangle$ (c) $\langle 0, -8 \rangle$ (d) $4\mathbf{i} + 2\mathbf{j}$ (e) $-2\mathbf{i} - \mathbf{j}$ (f) $4\mathbf{i}$
3. (a) $\langle 1, -2, 2 \rangle$ (b) $\langle 2, 2, -1 \rangle$ (c) $-\mathbf{i} + 2\mathbf{j} + 3\mathbf{k}$ (d) $2\mathbf{i} + 3\mathbf{j} - \mathbf{k}$
4. (a) $\langle -1, 3, 2 \rangle$ (b) $\langle 3, 4, 2 \rangle$ (c) $2\mathbf{j} - \mathbf{k}$ (d) $\mathbf{i} - \mathbf{j} + 2\mathbf{k}$

**5–6 Find the components of the vector, and sketch an equivalent vector with its initial point at the origin.**
5. (a) Vector in the $xy$-plane from $(4, 1)$ to $(1, 5)$.  
   (b) Vector in 3-space from $(2, 3, 0)$ to $(0, 0, 4)$.
6. (a) Vector in the $xy$-plane from $(-3, 3)$ to $(2, 3)$.  
   (b) Vector in 3-space from $(3, 0, 4)$ to $(0, 4, 4)$.

**7–8 Find the components of the vector $\vec{P_1P_2}$.**
7. (a) $P_1(3, 5), P_2(2, 8)$  
   (b) $P_1(7, -2), P_2(0, 0)$  
   (c) $P_1(5, -2, 1), P_2(2, 4, 2)$
8. (a) $P_1(-6, -2), P_2(-4, -1)$  
   (b) $P_1(0, 0, 0), P_2(-1, 6, 1)$  
   (c) $P_1(4, 1, -3), P_2(9, 1, -3)$

9. (a) Find the terminal point of $\mathbf{v} = 3\mathbf{i} - 2\mathbf{j}$ if the initial point is $(1, -2)$.  
   (b) Find the initial point of $\mathbf{v} = \langle -3, 1, 2 \rangle$ if the terminal point is $(5, 0, -1)$.
10. (a) Find the terminal point of $\mathbf{v} = \langle 7, 6 \rangle$ if the initial point is $(2, -1)$.  
    (b) Find the terminal point of $\mathbf{v} = \mathbf{i} + 2\mathbf{j} - 3\mathbf{k}$ if the initial point is $(-2, 1, 4)$.

**11–12 Perform the stated operations on the given vectors $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$.**
11. $\mathbf{u} = 3\mathbf{i} - \mathbf{k}, \mathbf{v} = \mathbf{i} - \mathbf{j} + 2\mathbf{k}, \mathbf{w} = 3\mathbf{j}$  
    (a) $\mathbf{w} - \mathbf{v}$  
    (b) $6\mathbf{u} + 4\mathbf{w}$  
    (c) $-\mathbf{v} - 2\mathbf{w}$  
    (d) $4(3\mathbf{u} + \mathbf{v})$  
    (e) $-8(\mathbf{v} + \mathbf{w}) + 2\mathbf{u}$  
    (f) $3\mathbf{w} - (\mathbf{v} - \mathbf{w})$
12. $\mathbf{u} = \langle 2, -1, 3 \rangle, \mathbf{v} = \langle 4, 0, -2 \rangle, \mathbf{w} = \langle 1, 1, 3 \rangle$  
    (a) $\mathbf{u} - \mathbf{w}$  
    (b) $7\mathbf{v} + 3\mathbf{w}$  
    (c) $-\mathbf{w} + \mathbf{v}$  
    (d) $3(\mathbf{u} - 7\mathbf{v})$  
    (e) $-3\mathbf{v} - 8\mathbf{w}$  
    (f) $2\mathbf{v} - (\mathbf{u} + \mathbf{w})$

**13–14 Find the norm of $\mathbf{v}$.**
13. (a) $\mathbf{v} = \langle 1, -1 \rangle$ (b) $\mathbf{v} = -\mathbf{i} + 7\mathbf{j}$ (c) $\mathbf{v} = \langle -1, 2, 4 \rangle$ (d) $\mathbf{v} = -3\mathbf{i} + 2\mathbf{j} + \mathbf{k}$
14. (a) $\mathbf{v} = \langle 3, 4 \rangle$ (b) $\mathbf{v} = \sqrt{2}\mathbf{i} - \sqrt{7}\mathbf{j}$ (c) $\mathbf{v} = \langle 0, -3, 0 \rangle$ (d) $\mathbf{v} = \mathbf{i} + \mathbf{j} + \mathbf{k}$

15. Let $\mathbf{u} = \mathbf{i} - 3\mathbf{j} + 2\mathbf{k}, \mathbf{v} = \mathbf{i} + \mathbf{j},$ and $\mathbf{w} = 2\mathbf{i} + 2\mathbf{j} - 4\mathbf{k}$. Find:  
    (a) $\|\mathbf{u} + \mathbf{v}\|$  
    (b) $\|\mathbf{u}\| + \|\mathbf{v}\|$  
    (c) $\|-2\mathbf{u}\| + 2\|\mathbf{v}\|$  
    (d) $\|3\mathbf{u} - 5\mathbf{v} + \mathbf{w}\|$  
    (e) $\frac{1}{\|\mathbf{w}\|}\mathbf{w}$  
    (f) $\left\|\frac{1}{\|\mathbf{w}\|}\mathbf{w}\right\|$

16. Is it possible to have $\|\mathbf{u} - \mathbf{v}\| = \|\mathbf{u}\| + \|\mathbf{v}\|$ if $\mathbf{u}$ and $\mathbf{v}$ are nonzero vectors? Justify your conclusion geometrically.

**17–20 True–False Determine whether the statement is true or false. Explain your answer.**
17. The norm of the sum of two vectors is equal to the sum of the norms of the two vectors.
18. If two distinct vectors $\mathbf{v}$ and $\mathbf{w}$ are drawn with the same initial point, then a vector drawn between the terminal points of $\mathbf{v}$ and $\mathbf{w}$ will be either $\mathbf{v} - \mathbf{w}$ or $\mathbf{w} - \mathbf{v}$.
19. There are exactly two unit vectors that are parallel to a given nonzero vector.
20. Given a nonzero scalar $c$ and vectors $\mathbf{b}$ and $\mathbf{d}$, the vector equation $c\mathbf{a} + \mathbf{b} = \mathbf{d}$ has a unique solution $\mathbf{a}$.

**21–22 Find unit vectors that satisfy the stated conditions.**
21. (a) Same direction as $-\mathbf{i} + 4\mathbf{j}$.  
    (b) Oppositely directed to $6\mathbf{i} - 4\mathbf{j} + 2\mathbf{k}$.  
    (c) Same direction as the vector from the point $A(-1, 0, 2)$ to the point $B(3, 1, 1)$.
22. (a) Oppositely directed to $3\mathbf{i} - 4\mathbf{j}$.  
    (b) Same direction as $2\mathbf{i} - \mathbf{j} - 2\mathbf{k}$.  
    (c) Same direction as the vector from the point $A(-3, 2)$ to the point $B(1, -1)$.

**23–24 Find the vectors that satisfy the stated conditions.**
23. (a) Oppositely directed to $\mathbf{v} = \langle 3, -4 \rangle$ and half the length of $\mathbf{v}$.  
    (b) Length $\sqrt{17}$ and same direction as $\mathbf{v} = \langle 7, 0, -6 \rangle$.
24. (a) Same direction as $\mathbf{v} = -2\mathbf{i} + 3\mathbf{j}$ and three times the length of $\mathbf{v}$.  
    (b) Length 2 and oppositely directed to $\mathbf{v} = -3\mathbf{i} + 4\mathbf{j} + \mathbf{k}$.

25. In each part, find the component form of the vector $\mathbf{v}$ in 2-space that has the stated length and makes the stated angle $\theta$ with the positive $x$-axis.  
    (a) $\|\mathbf{v}\| = 3; \; \theta = \pi/4$  
    (b) $\|\mathbf{v}\| = 2; \; \theta = 90^\circ$  
    (c) $\|\mathbf{v}\| = 5; \; \theta = 120^\circ$  
    (d) $\|\mathbf{v}\| = 1; \; \theta = \pi$

26. Find the component forms of $\mathbf{v} + \mathbf{w}$ and $\mathbf{v} - \mathbf{w}$ in 2-space, given that $\|\mathbf{v}\| = 1, \|\mathbf{w}\| = 1$, $\mathbf{v}$ makes an angle of $\pi/6$ with the positive $x$-axis, and $\mathbf{w}$ makes an angle of $3\pi/4$ with the positive $x$-axis.

**27–28 Find the component form of $\mathbf{v} + \mathbf{w}$, given that $\mathbf{v}$ and $\mathbf{w}$ are unit vectors.**
27. $\mathbf{v}$ at angle $30^\circ$ with the positive $x$-axis and $\mathbf{w}$ at angle $135^\circ$ with the positive $x$-axis.
28. $\mathbf{v}$ along positive $y$-axis and $\mathbf{w}$ at angle $120^\circ$ clockwise from positive $x$-axis (fourth quadrant).

29. In each part, sketch the vector $\mathbf{u} + \mathbf{v} + \mathbf{w}$ and express it in component form:  
    (a) From grid coordinates.  
    (b) From grid coordinates.

30. In each part of Exercise 29, sketch the vector $\mathbf{u} - \mathbf{v} + \mathbf{w}$ and express it in component form.

31. Let $\mathbf{u} = \langle 1, 3 \rangle, \mathbf{v} = \langle 2, 1 \rangle, \mathbf{w} = \langle 4, -1 \rangle$. Find the vector $\mathbf{x}$ that satisfies $2\mathbf{u} - \mathbf{v} + \mathbf{x} = 7\mathbf{x} + \mathbf{w}$.

32. Let $\mathbf{u} = \langle -1, 1 \rangle, \mathbf{v} = \langle 0, 1 \rangle,$ and $\mathbf{w} = \langle 3, 4 \rangle$. Find the vector $\mathbf{x}$ that satisfies $\mathbf{u} - 2\mathbf{x} = \mathbf{x} - \mathbf{w} + 3\mathbf{v}$.

33. Find $\mathbf{u}$ and $\mathbf{v}$ if $\mathbf{u} + 2\mathbf{v} = 3\mathbf{i} - \mathbf{k}$ and $3\mathbf{u} - \mathbf{v} = \mathbf{i} + \mathbf{j} + \mathbf{k}$.

34. Find $\mathbf{u}$ and $\mathbf{v}$ if $\mathbf{u} + \mathbf{v} = \langle 2, -3 \rangle$ and $3\mathbf{u} + 2\mathbf{v} = \langle -1, 2 \rangle$.

35. Use vectors to find the lengths of the diagonals of the parallelogram that has $\mathbf{i} + \mathbf{j}$ and $\mathbf{i} - 2\mathbf{j}$ as adjacent sides.

36. Use vectors to find the fourth vertex of a parallelogram, three of whose vertices are $(0, 0), (1, 3),$ and $(2, 4)$. *[Note: There is more than one answer.]*

37. (a) Given that $\|\mathbf{v}\| = 3$, find all values of $k$ such that $\|k\mathbf{v}\| = 5$.  
    (b) Given that $k = -2$ and $\|k\mathbf{v}\| = 6$, find $\|\mathbf{v}\|$.

38. What do you know about $k$ and $\mathbf{v}$ if $\|k\mathbf{v}\| = 0$?

39. In each part, find two unit vectors in 2-space that satisfy the stated condition:  
    (a) Parallel to the line $y = 3x + 2$  
    (b) Parallel to the line $x + y = 4$  
    (c) Perpendicular to the line $y = -5x + 1$

40. In each part, find two unit vectors in 3-space that satisfy the stated condition:  
    (a) Perpendicular to the $xy$-plane  
    (b) Perpendicular to the $xz$-plane  
    (c) Perpendicular to the $yz$-plane

#### FOCUS ON CONCEPTS

41. Let $\mathbf{r} = \langle x, y \rangle$ be an arbitrary vector. In each part, describe the set of all points $(x, y)$ in 2-space that satisfy the stated condition:  
    (a) $\|\mathbf{r}\| = 1$  
    (b) $\|\mathbf{r}\| \le 1$  
    (c) $\|\mathbf{r}\| > 1$

42. Let $\mathbf{r} = \langle x, y \rangle$ and $\mathbf{r}_0 = \langle x_0, y_0 \rangle$. In each part, describe the set of all points $(x, y)$ in 2-space that satisfy the stated condition:  
    (a) $\|\mathbf{r} - \mathbf{r}_0\| = 1$  
    (b) $\|\mathbf{r} - \mathbf{r}_0\| \le 1$  
    (c) $\|\mathbf{r} - \mathbf{r}_0\| > 1$

43. Let $\mathbf{r} = \langle x, y, z \rangle$ be an arbitrary vector. In each part, describe the set of all points $(x, y, z)$ in 3-space that satisfy the stated condition:  
    (a) $\|\mathbf{r}\| = 1$  
    (b) $\|\mathbf{r}\| \le 1$  
    (c) $\|\mathbf{r}\| > 1$

44. Let $\mathbf{r}_1 = \langle x_1, y_1 \rangle, \mathbf{r}_2 = \langle x_2, y_2 \rangle,$ and $\mathbf{r} = \langle x, y \rangle$. Assuming that $k > \|\mathbf{r}_2 - \mathbf{r}_1\|$, describe the set of all points $(x, y)$ for which $\|\mathbf{r} - \mathbf{r}_1\| + \|\mathbf{r} - \mathbf{r}_2\| = k$.

**45–50 Find the magnitude of the resultant force and the angle that it makes with the positive $x$-axis.**
45. Force of $30\text{ lb}$ along positive $y$-axis and $60\text{ lb}$ along positive $x$-axis.
46. Force of $100\text{ N}$ at $60^\circ$ and force of $120\text{ N}$ along positive $x$-axis.
47. Force of $400\text{ N}$ at $120^\circ$ and force of $400\text{ N}$ at $-30^\circ$ (or $330^\circ$).
48. Force of $2\text{ lb}$ at $50^\circ$ and force of $4\text{ lb}$ at $-27^\circ$.
49. Three concurrent forces: $40\text{ N}$ at $180^\circ - 60^\circ = 120^\circ$, $50\text{ N}$ at $30^\circ$, and $75\text{ N}$ along positive $x$-axis.
50. Three concurrent forces: $150\text{ N}$ at $180^\circ - 75^\circ = 105^\circ$, $200\text{ N}$ at $60^\circ$, and $100\text{ N}$ along negative $y$-axis ($270^\circ$).

**51–52 A particle is said to be in static equilibrium if the resultant of all forces applied to it is zero. In these exercises, find the force $\mathbf{F}$ that must be applied to the point to produce static equilibrium. Describe $\mathbf{F}$ by specifying its magnitude and the angle that it makes with the positive $x$-axis.**
51. Concurrent forces of $8\text{ lb}$ along negative $x$-axis and $10\text{ lb}$ at $60^\circ$ above positive $x$-axis.
52. Concurrent forces of $150\text{ N}$ at $75^\circ$ above negative $x$-axis, $120\text{ N}$ at $45^\circ$ above positive $x$-axis, and $100\text{ N}$ along negative $y$-axis.

53. The accompanying figure shows a $250\text{ lb}$ traffic light supported by two flexible cables at angles $30^\circ$ and $45^\circ$ with the horizontal. The magnitudes of the forces that the cables apply to the eye ring are called the cable tensions. Find the tensions in the cables if the traffic light is in static equilibrium.
54. Find the tensions in the cables shown in Figure Ex-54 supporting a $200\text{ N}$ block at angles $30^\circ$ and $60^\circ$ with the horizontal if the block is in static equilibrium.
55. A block weighing $300\text{ lb}$ is suspended by cables $A$ and $B$ at angles $45^\circ$ and $30^\circ$ with the horizontal ceiling. Determine the forces that the block exerts along the cables.
56. A block weighing $100\text{ N}$ is suspended by cables $A$ and $B$ attached $10\text{ ft}$ and $20\text{ ft}$ horizontally from a center sag point $d$.  
    (a) Use a graphing utility to graph the forces that the block exerts along cables $A$ and $B$ as functions of the "sag" $d$.  
    (b) Does increasing the sag increase or decrease the forces on the cables?  
    (c) How much sag is required if the cables cannot tolerate forces in excess of $150\text{ N}$?

57. A vector $\mathbf{w}$ is said to be a **linear combination** of the vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ if $\mathbf{w}$ can be expressed as $\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2$, where $c_1$ and $c_2$ are scalars.  
    (a) Find scalars $c_1$ and $c_2$ to express the vector $4\mathbf{j}$ as a linear combination of the vectors $\mathbf{v}_1 = 2\mathbf{i} - \mathbf{j}$ and $\mathbf{v}_2 = 4\mathbf{i} + 2\mathbf{j}$.  
    (b) Show that the vector $\langle 3, 5 \rangle$ cannot be expressed as a linear combination of the vectors $\mathbf{v}_1 = \langle 1, -3 \rangle$ and $\mathbf{v}_2 = \langle -2, 6 \rangle$.

58. A vector $\mathbf{w}$ is a linear combination of the vectors $\mathbf{v}_1, \mathbf{v}_2,$ and $\mathbf{v}_3$ if $\mathbf{w}$ can be expressed as $\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3$, where $c_1, c_2,$ and $c_3$ are scalars.  
    (a) Find scalars $c_1, c_2,$ and $c_3$ to express $\langle -1, 1, 5 \rangle$ as a linear combination of $\mathbf{v}_1 = \langle 1, 0, 1 \rangle, \mathbf{v}_2 = \langle 3, 2, 0 \rangle,$ and $\mathbf{v}_3 = \langle 0, 1, 1 \rangle$.  
    (b) Show that the vector $2\mathbf{i} + \mathbf{j} - \mathbf{k}$ cannot be expressed as a linear combination of $\mathbf{v}_1 = \mathbf{i} - \mathbf{j}, \mathbf{v}_2 = 3\mathbf{i} + \mathbf{k},$ and $\mathbf{v}_3 = 4\mathbf{i} - \mathbf{j} + \mathbf{k}$.

59. Use a theorem from plane geometry to show that if $\mathbf{u}$ and $\mathbf{v}$ are vectors in 2-space or 3-space, then
    $$\|\mathbf{u} + \mathbf{v}\| \le \|\mathbf{u}\| + \|\mathbf{v}\|$$
    which is called the **triangle inequality for vectors**. Give some examples to illustrate this inequality.

60. Prove parts (a), (c), and (e) of Theorem 11.2.6 algebraically in 2-space.
61. Prove parts (d), (g), and (h) of Theorem 11.2.6 algebraically in 2-space.
62. Prove part (f) of Theorem 11.2.6 geometrically.

#### FOCUS ON CONCEPTS

63. Use vectors to prove that the line segment joining the midpoints of two sides of a triangle is parallel to the third side and half as long.
64. Use vectors to prove that the midpoints of the sides of a quadrilateral are the vertices of a parallelogram.
65. **Writing.** Do some research and then write a few paragraphs on the early history of the use of vectors in mathematics.
66. **Writing.** Write a paragraph that discusses some of the similarities and differences between the rules of "vector arithmetic" and the rules of arithmetic of real numbers.

#### QUICK CHECK ANSWERS 11.2
1. (a) $\sqrt{59}$ (b) $\langle 7, 9, 2 \rangle$ (c) $\langle -1, -11, 12 \rangle$ (d) $\langle 6, -2, 14 \rangle$  
2. $\frac{1}{\sqrt{59}}\mathbf{v} = \left\langle \frac{3}{\sqrt{59}}, -\frac{1}{\sqrt{59}}, \frac{7}{\sqrt{59}} \right\rangle$  
3. $\left\langle \frac{1}{2}, \frac{\sqrt{3}}{2} \right\rangle = \frac{1}{2}\mathbf{i} + \frac{\sqrt{3}}{2}\mathbf{j}$  
4. (a) $\langle -3, -4, 5 \rangle$ (b) $\frac{1}{5}\vec{AB} = \left\langle -\frac{3}{5}, -\frac{4}{5}, 1 \right\rangle$

---

## 11.3 DOT PRODUCT; PROJECTIONS

In the last section we defined three operations on vectors—addition, subtraction, and scalar multiplication. In scalar multiplication a vector is multiplied by a scalar and the result is a vector. In this section we will define a new kind of multiplication in which two vectors are multiplied to produce a scalar. This multiplication operation has many uses, some of which we will also discuss in this section.

### DEFINITION OF THE DOT PRODUCT

> **11.3.1 DEFINITION**  
> If $\mathbf{u} = \langle u_1, u_2 \rangle$ and $\mathbf{v} = \langle v_1, v_2 \rangle$ are vectors in 2-space, then the **dot product** of $\mathbf{u}$ and $\mathbf{v}$ is written as $\mathbf{u} \cdot \mathbf{v}$ and is defined as
> $$\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2$$
> Similarly, if $\mathbf{u} = \langle u_1, u_2, u_3 \rangle$ and $\mathbf{v} = \langle v_1, v_2, v_3 \rangle$ are vectors in 3-space, then their dot product is defined as
> $$\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3$$

In words, the dot product of two vectors is formed by multiplying their corresponding components and adding the resulting products. Note that the dot product of two vectors is a scalar.

#### Example 1
$$\langle 3, 5 \rangle \cdot \langle -1, 2 \rangle = 3(-1) + 5(2) = 7$$
$$\langle 2, 3 \rangle \cdot \langle -3, 2 \rangle = 2(-3) + 3(2) = 0$$
$$\langle 1, -3, 4 \rangle \cdot \langle 1, 5, 2 \rangle = 1(1) + (-3)(5) + 4(2) = -6$$
Here are the same computations expressed another way:
$$(3\mathbf{i} + 5\mathbf{j}) \cdot (-\mathbf{i} + 2\mathbf{j}) = 3(-1) + 5(2) = 7$$
$$(2\mathbf{i} + 3\mathbf{j}) \cdot (-3\mathbf{i} + 2\mathbf{j}) = 2(-3) + 3(2) = 0$$
$$(\mathbf{i} - 3\mathbf{j} + 4\mathbf{k}) \cdot (\mathbf{i} + 5\mathbf{j} + 2\mathbf{k}) = 1(1) + (-3)(5) + 4(2) = -6$$

---

### ALGEBRAIC PROPERTIES OF THE DOT PRODUCT

The following theorem provides some of the basic algebraic properties of the dot product.

> **11.3.2 THEOREM**  
> If $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ are vectors in 2- or 3-space and $k$ is a scalar, then:
> (a) $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$  
> (b) $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$  
> (c) $k(\mathbf{u} \cdot \mathbf{v}) = (k\mathbf{u}) \cdot \mathbf{v} = \mathbf{u} \cdot (k\mathbf{v})$  
> (d) $\mathbf{v} \cdot \mathbf{v} = \|\mathbf{v}\|^2$  
> (e) $\mathbf{0} \cdot \mathbf{v} = 0$

**PROOF (c)**  
Let $\mathbf{u} = \langle u_1, u_2, u_3 \rangle$ and $\mathbf{v} = \langle v_1, v_2, v_3 \rangle$. Then
$$k(\mathbf{u} \cdot \mathbf{v}) = k(u_1 v_1 + u_2 v_2 + u_3 v_3) = (k u_1)v_1 + (k u_2)v_2 + (k u_3)v_3 = (k\mathbf{u}) \cdot \mathbf{v}$$
Similarly, $k(\mathbf{u} \cdot \mathbf{v}) = \mathbf{u} \cdot (k\mathbf{v})$.

**PROOF (d)**  
$$\mathbf{v} \cdot \mathbf{v} = v_1 v_1 + v_2 v_2 + v_3 v_3 = v_1^2 + v_2^2 + v_3^2 = \|\mathbf{v}\|^2 \quad \blacksquare$$

The following alternative form of the formula in part (d) of Theorem 11.3.2 provides a useful way of expressing the norm of a vector in terms of a dot product:
$$\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}} \tag{1}$$

---

### ANGLE BETWEEN VECTORS

Suppose that $\mathbf{u}$ and $\mathbf{v}$ are nonzero vectors in 2-space or 3-space that are positioned so their initial points coincide. We define the **angle between $\mathbf{u}$ and $\mathbf{v}$** to be the angle $\theta$ determined by the vectors that satisfies the condition $0 \le \theta \le \pi$ (Figure 11.3.1). In 2-space, $\theta$ is the smallest counterclockwise angle through which one of the vectors can be rotated until it aligns with the other.

> **11.3.3 THEOREM**  
> If $\mathbf{u}$ and $\mathbf{v}$ are nonzero vectors in 2-space or 3-space, and if $\theta$ is the angle between them, then
> $$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|} \tag{2}$$

**PROOF**  
Suppose that the vectors $\mathbf{u}, \mathbf{v},$ and $\mathbf{v} - \mathbf{u}$ are positioned to form three sides of a triangle, as shown in Figure 11.3.2. It follows from the law of cosines that
$$\|\mathbf{v} - \mathbf{u}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta \tag{3}$$
Using the properties of the dot product in Theorem 11.3.2, we can rewrite the left side of this equation as
$$\|\mathbf{v} - \mathbf{u}\|^2 = (\mathbf{v} - \mathbf{u}) \cdot (\mathbf{v} - \mathbf{u})$$
$$= (\mathbf{v} - \mathbf{u}) \cdot \mathbf{v} - (\mathbf{v} - \mathbf{u}) \cdot \mathbf{u}$$
$$= \mathbf{v} \cdot \mathbf{v} - \mathbf{u} \cdot \mathbf{v} - \mathbf{v} \cdot \mathbf{u} + \mathbf{u} \cdot \mathbf{u}$$
$$= \|\mathbf{v}\|^2 - 2\mathbf{u} \cdot \mathbf{v} + \|\mathbf{u}\|^2$$
Substituting this back into (3) yields
$$\|\mathbf{v}\|^2 - 2\mathbf{u} \cdot \mathbf{v} + \|\mathbf{u}\|^2 = \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2\|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$
which we can simplify and rewrite as
$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta$$
Finally, dividing both sides of this equation by $\|\mathbf{u}\|\|\mathbf{v}\|$ yields (2). $\blacksquare$

#### Example 2
Find the angle between the vector $\mathbf{u} = \mathbf{i} - 2\mathbf{j} + 2\mathbf{k}$ and:
(a) $\mathbf{v} = -3\mathbf{i} + 6\mathbf{j} + 2\mathbf{k}$  
(b) $\mathbf{w} = 2\mathbf{i} + 7\mathbf{j} + 6\mathbf{k}$  
(c) $\mathbf{z} = -3\mathbf{i} + 6\mathbf{j} - 6\mathbf{k}$

**Solution (a).**
$$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|} = \frac{-11}{(3)(7)} = -\frac{11}{21}$$
Thus,
$$\theta = \cos^{-1}\left(-\frac{11}{21}\right) \approx 2.12\text{ radians} \approx 121.6^\circ$$

**Solution (b).**
$$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{w}}{\|\mathbf{u}\|\|\mathbf{w}\|} = \frac{0}{\|\mathbf{u}\|\|\mathbf{w}\|} = 0$$
Thus, $\theta = \pi/2$, which means that the vectors are perpendicular.

**Solution (c).**
$$\cos\theta = \frac{\mathbf{u} \cdot \mathbf{z}}{\|\mathbf{u}\|\|\mathbf{z}\|} = \frac{-27}{(3)(9)} = -1$$
Thus, $\theta = \pi$, which means that the vectors are oppositely directed. (In retrospect, we could have seen this without computing $\theta$, since $\mathbf{z} = -3\mathbf{u}$.)

---

### INTERPRETING THE SIGN OF THE DOT PRODUCT

It will often be convenient to express Formula (2) as
$$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|\|\mathbf{v}\|\cos\theta \tag{4}$$
which expresses the dot product of $\mathbf{u}$ and $\mathbf{v}$ in terms of the lengths of these vectors and the angle between them. Since $\mathbf{u}$ and $\mathbf{v}$ are assumed to be nonzero vectors, this version of the formula makes it clear that the sign of $\mathbf{u} \cdot \mathbf{v}$ is the same as the sign of $\cos\theta$. Thus, we can tell from the dot product whether the angle between two vectors is acute or obtuse or whether the vectors are perpendicular (Figure 11.3.3):
* $\mathbf{u} \cdot \mathbf{v} > 0 \iff 0 \le \theta < \pi/2$ (acute)
* $\mathbf{u} \cdot \mathbf{v} < 0 \iff \pi/2 < \theta \le \pi$ (obtuse)
* $\mathbf{u} \cdot \mathbf{v} = 0 \iff \theta = \pi/2$ (orthogonal)

> **REMARK**  
> The terms "perpendicular," "orthogonal," and "normal" are all commonly used to describe geometric objects that meet at right angles. For consistency, we will say that two vectors are orthogonal, a vector is normal to a plane, and two planes are perpendicular. Moreover, although the zero vector does not make a well-defined angle with other vectors, we will consider $\mathbf{0}$ to be orthogonal to all vectors. This convention allows us to say that $\mathbf{u}$ and $\mathbf{v}$ are orthogonal vectors if and only if $\mathbf{u} \cdot \mathbf{v} = 0$, and makes Formula (4) valid if $\mathbf{u}$ or $\mathbf{v}$ (or both) is zero.

---

### DIRECTION ANGLES

In an $xy$-coordinate system, the direction of a nonzero vector $\mathbf{v}$ is completely determined by the angles $\alpha$ and $\beta$ between $\mathbf{v}$ and the unit vectors $\mathbf{i}$ and $\mathbf{j}$ (Figure 11.3.4), and in an $xyz$-coordinate system the direction is completely determined by the angles $\alpha, \beta,$ and $\gamma$ between $\mathbf{v}$ and the unit vectors $\mathbf{i}, \mathbf{j},$ and $\mathbf{k}$ (Figure 11.3.5). In both 2-space and 3-space the angles between a nonzero vector $\mathbf{v}$ and the vectors $\mathbf{i}, \mathbf{j},$ and $\mathbf{k}$ are called the **direction angles** of $\mathbf{v}$, and the cosines of those angles are called the **direction cosines** of $\mathbf{v}$. Formulas for the direction cosines of a vector can be obtained from Formula (2). For example, if $\mathbf{v} = v_1\mathbf{i} + v_2\mathbf{j} + v_3\mathbf{k}$, then
$$\cos\alpha = \frac{\mathbf{v} \cdot \mathbf{i}}{\|\mathbf{v}\|\|\mathbf{i}\|} = \frac{v_1}{\|\mathbf{v}\|}, \quad \cos\beta = \frac{\mathbf{v} \cdot \mathbf{j}}{\|\mathbf{v}\|\|\mathbf{j}\|} = \frac{v_2}{\|\mathbf{v}\|}, \quad \cos\gamma = \frac{\mathbf{v} \cdot \mathbf{k}}{\|\mathbf{v}\|\|\mathbf{k}\|} = \frac{v_3}{\|\mathbf{v}\|}$$

> **11.3.4 THEOREM**  
> The direction cosines of a nonzero vector $\mathbf{v} = v_1\mathbf{i} + v_2\mathbf{j} + v_3\mathbf{k}$ are
> $$\cos\alpha = \frac{v_1}{\|\mathbf{v}\|}, \quad \cos\beta = \frac{v_2}{\|\mathbf{v}\|}, \quad \cos\gamma = \frac{v_3}{\|\mathbf{v}\|}$$

The direction cosines of a vector $\mathbf{v} = v_1\mathbf{i} + v_2\mathbf{j} + v_3\mathbf{k}$ can be computed by normalizing $\mathbf{v}$ and reading off the components of $\mathbf{v}/\|\mathbf{v}\|$, since
$$\frac{\mathbf{v}}{\|\mathbf{v}\|} = \frac{v_1}{\|\mathbf{v}\|}\mathbf{i} + \frac{v_2}{\|\mathbf{v}\|}\mathbf{j} + \frac{v_3}{\|\mathbf{v}\|}\mathbf{k} = (\cos\alpha)\mathbf{i} + (\cos\beta)\mathbf{j} + (\cos\gamma)\mathbf{k}$$
The direction cosines of a vector satisfy the equation
$$\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1 \tag{5}$$

#### Example 3
Find the direction cosines of the vector $\mathbf{v} = 2\mathbf{i} - 4\mathbf{j} + 4\mathbf{k}$, and approximate the direction angles to the nearest degree.

**Solution.** First we will normalize the vector $\mathbf{v}$ and then read off the components. We have $\|\mathbf{v}\| = \sqrt{4 + 16 + 16} = 6$, so that $\mathbf{v}/\|\mathbf{v}\| = \frac{1}{3}\mathbf{i} - \frac{2}{3}\mathbf{j} + \frac{2}{3}\mathbf{k}$. Thus,
$$\cos\alpha = \frac{1}{3}, \quad \cos\beta = -\frac{2}{3}, \quad \cos\gamma = \frac{2}{3}$$
With the help of a calculating utility we obtain
$$\alpha = \cos^{-1}\left(\frac{1}{3}\right) \approx 71^\circ, \quad \beta = \cos^{-1}\left(-\frac{2}{3}\right) \approx 132^\circ, \quad \gamma = \cos^{-1}\left(\frac{2}{3}\right) \approx 48^\circ$$

#### Example 4
Find the angle between a diagonal of a cube and one of its edges.

**Solution.** Assume that the cube has side $a$, and introduce a coordinate system as shown in Figure 11.3.6. In this coordinate system the vector
$$\mathbf{d} = a\mathbf{i} + a\mathbf{j} + a\mathbf{k}$$
is a diagonal of the cube and the unit vectors $\mathbf{i}, \mathbf{j},$ and $\mathbf{k}$ run along the edges. By symmetry, the diagonal makes the same angle with each edge, so it is sufficient to find the angle between $\mathbf{d}$ and $\mathbf{i}$ (the direction angle $\alpha$). Thus,
$$\cos\alpha = \frac{\mathbf{d} \cdot \mathbf{i}}{\|\mathbf{d}\|\|\mathbf{i}\|} = \frac{a}{\|\mathbf{d}\|} = \frac{a}{\sqrt{3a^2}} = \frac{1}{\sqrt{3}}$$
and hence
$$\alpha = \cos^{-1}\left(\frac{1}{\sqrt{3}}\right) \approx 0.955\text{ radian} \approx 54.7^\circ$$

---

### DECOMPOSING VECTORS INTO ORTHOGONAL COMPONENTS

In many applications it is desirable to "decompose" a vector into a sum of two orthogonal vectors with convenient specified directions. For example, Figure 11.3.7 shows a block on an inclined plane. The downward force $\mathbf{F}$ that gravity exerts on the block can be decomposed into the sum
$$\mathbf{F} = \mathbf{F}_1 + \mathbf{F}_2$$
where the force $\mathbf{F}_1$ is parallel to the ramp and the force $\mathbf{F}_2$ is perpendicular to the ramp. The forces $\mathbf{F}_1$ and $\mathbf{F}_2$ are useful because $\mathbf{F}_1$ is the force that pulls the block along the ramp, and $\mathbf{F}_2$ is the force that the block exerts against the ramp.

Suppose that $\mathbf{e}_1$ and $\mathbf{e}_2$ are two orthogonal unit vectors in 2-space, and suppose that we want to express a given vector $\mathbf{v}$ as a sum
$$\mathbf{v} = \mathbf{w}_1 + \mathbf{w}_2$$
so that $\mathbf{w}_1$ is a scalar multiple of $\mathbf{e}_1$ and $\mathbf{w}_2$ is a scalar multiple of $\mathbf{e}_2$ (Figure 11.3.8a). That is, we want to find scalars $k_1$ and $k_2$ such that
$$\mathbf{v} = k_1\mathbf{e}_1 + k_2\mathbf{e}_2 \tag{6}$$
We can find $k_1$ by taking the dot product of $\mathbf{v}$ with $\mathbf{e}_1$:
$$\mathbf{v} \cdot \mathbf{e}_1 = (k_1\mathbf{e}_1 + k_2\mathbf{e}_2) \cdot \mathbf{e}_1 = k_1(\mathbf{e}_1 \cdot \mathbf{e}_1) + k_2(\mathbf{e}_2 \cdot \mathbf{e}_1) = k_1\|\mathbf{e}_1\|^2 + 0 = k_1$$
Similarly, $\mathbf{v} \cdot \mathbf{e}_2 = k_2$. Substituting these expressions for $k_1$ and $k_2$ in (6) yields
$$\mathbf{v} = (\mathbf{v} \cdot \mathbf{e}_1)\mathbf{e}_1 + (\mathbf{v} \cdot \mathbf{e}_2)\mathbf{e}_2 \tag{7}$$
In this formula we call $(\mathbf{v} \cdot \mathbf{e}_1)\mathbf{e}_1$ and $(\mathbf{v} \cdot \mathbf{e}_2)\mathbf{e}_2$ the **vector components** of $\mathbf{v}$ along $\mathbf{e}_1$ and $\mathbf{e}_2$, respectively; and we call $\mathbf{v} \cdot \mathbf{e}_1$ and $\mathbf{v} \cdot \mathbf{e}_2$ the **scalar components** of $\mathbf{v}$ along $\mathbf{e}_1$ and $\mathbf{e}_2$, respectively. If $\theta$ denotes the angle between $\mathbf{v}$ and $\mathbf{e}_1$, and the angle between $\mathbf{v}$ and $\mathbf{e}_2$ is $\pi/2$ or less, then the scalar components of $\mathbf{v}$ can be written in trigonometric form as
$$\mathbf{v} \cdot \mathbf{e}_1 = \|\mathbf{v}\|\cos\theta \quad \text{and} \quad \mathbf{v} \cdot \mathbf{e}_2 = \|\mathbf{v}\|\sin\theta \tag{8}$$
Moreover, the vector components of $\mathbf{v}$ can be expressed as
$$(\mathbf{v} \cdot \mathbf{e}_1)\mathbf{e}_1 = (\|\mathbf{v}\|\cos\theta)\mathbf{e}_1 \quad \text{and} \quad (\mathbf{v} \cdot \mathbf{e}_2)\mathbf{e}_2 = (\|\mathbf{v}\|\sin\theta)\mathbf{e}_2 \tag{9}$$
and the decomposition (6) can be expressed as
$$\mathbf{v} = (\|\mathbf{v}\|\cos\theta)\mathbf{e}_1 + (\|\mathbf{v}\|\sin\theta)\mathbf{e}_2 \tag{10}$$

#### Example 5
Let $\mathbf{v} = \langle 2, 3 \rangle, \mathbf{e}_1 = \langle \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \rangle,$ and $\mathbf{e}_2 = \langle -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \rangle$. Find the scalar components of $\mathbf{v}$ along $\mathbf{e}_1$ and $\mathbf{e}_2$ and the vector components of $\mathbf{v}$ along $\mathbf{e}_1$ and $\mathbf{e}_2$.

**Solution.** The scalar components of $\mathbf{v}$ along $\mathbf{e}_1$ and $\mathbf{e}_2$ are
$$\mathbf{v} \cdot \mathbf{e}_1 = 2\left(\frac{1}{\sqrt{2}}\right) + 3\left(\frac{1}{\sqrt{2}}\right) = \frac{5}{\sqrt{2}}$$
$$\mathbf{v} \cdot \mathbf{e}_2 = 2\left(-\frac{1}{\sqrt{2}}\right) + 3\left(\frac{1}{\sqrt{2}}\right) = \frac{1}{\sqrt{2}}$$
so the vector components are
$$(\mathbf{v} \cdot \mathbf{e}_1)\mathbf{e}_1 = \frac{5}{\sqrt{2}}\left\langle \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right\rangle = \left\langle \frac{5}{2}, \frac{5}{2} \right\rangle$$
$$(\mathbf{v} \cdot \mathbf{e}_2)\mathbf{e}_2 = \frac{1}{\sqrt{2}}\left\langle -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right\rangle = \left\langle -\frac{1}{2}, \frac{1}{2} \right\rangle$$

#### Example 6
A rope is attached to a $100\text{ lb}$ block on a ramp that is inclined at an angle of $30^\circ$ with the ground (Figure 11.3.9a). How much force does the block exert against the ramp, and how much force must be applied to the rope in a direction parallel to the ramp to prevent the block from sliding down the ramp? (Assume that the ramp is smooth, that is, exerts no frictional forces.)

**Solution.** Let $\mathbf{F}$ denote the downward force of gravity on the block (so $\|\mathbf{F}\| = 100\text{ lb}$), and let $\mathbf{F}_1$ and $\mathbf{F}_2$ be the vector components of $\mathbf{F}$ parallel and perpendicular to the ramp (as shown in Figure 11.3.9b). The lengths of $\mathbf{F}_1$ and $\mathbf{F}_2$ are
$$\|\mathbf{F}_1\| = \|\mathbf{F}\|\cos 60^\circ = 100\left(\frac{1}{2}\right) = 50\text{ lb}$$
$$\|\mathbf{F}_2\| = \|\mathbf{F}\|\sin 60^\circ = 100\left(\frac{\sqrt{3}}{2}\right) \approx 86.6\text{ lb}$$
Thus, the block exerts a force of approximately $86.6\text{ lb}$ against the ramp, and it requires a force of $50\text{ lb}$ to prevent the block from sliding down the ramp.

---

### ORTHOGONAL PROJECTIONS

The vector components of $\mathbf{v}$ along $\mathbf{e}_1$ and $\mathbf{e}_2$ in (7) are also called the **orthogonal projections** of $\mathbf{v}$ on $\mathbf{e}_1$ and $\mathbf{e}_2$ and are commonly denoted by
$$\operatorname{proj}_{\mathbf{e}_1}\mathbf{v} = (\mathbf{v} \cdot \mathbf{e}_1)\mathbf{e}_1 \quad \text{and} \quad \operatorname{proj}_{\mathbf{e}_2}\mathbf{v} = (\mathbf{v} \cdot \mathbf{e}_2)\mathbf{e}_2$$
In general, if $\mathbf{e}$ is a unit vector, then we define the orthogonal projection of $\mathbf{v}$ on $\mathbf{e}$ to be
$$\operatorname{proj}_{\mathbf{e}}\mathbf{v} = (\mathbf{v} \cdot \mathbf{e})\mathbf{e} \tag{11}$$
The orthogonal projection of $\mathbf{v}$ on an arbitrary nonzero vector $\mathbf{b}$ can be obtained by normalizing $\mathbf{b}$ and then applying Formula (11); that is,
$$\operatorname{proj}_{\mathbf{b}}\mathbf{v} = \left(\mathbf{v} \cdot \frac{\mathbf{b}}{\|\mathbf{b}\|}\right)\frac{\mathbf{b}}{\|\mathbf{b}\|}$$
which can be rewritten as
$$\operatorname{proj}_{\mathbf{b}}\mathbf{v} = \frac{\mathbf{v} \cdot \mathbf{b}}{\|\mathbf{b}\|^2}\mathbf{b} \tag{12}$$
Moreover, subtracting $\operatorname{proj}_{\mathbf{b}}\mathbf{v}$ from $\mathbf{v}$ produces a vector $\mathbf{v} - \operatorname{proj}_{\mathbf{b}}\mathbf{v}$ that is orthogonal to $\mathbf{b}$; we call this the **vector component of $\mathbf{v}$ orthogonal to $\mathbf{b}$**.

#### Example 7
Find the orthogonal projection of $\mathbf{v} = \mathbf{i} + \mathbf{j} + \mathbf{k}$ on $\mathbf{b} = 2\mathbf{i} + 2\mathbf{j}$, and then find the vector component of $\mathbf{v}$ orthogonal to $\mathbf{b}$.

**Solution.** We have
$$\mathbf{v} \cdot \mathbf{b} = (\mathbf{i} + \mathbf{j} + \mathbf{k}) \cdot (2\mathbf{i} + 2\mathbf{j}) = 2 + 2 + 0 = 4$$
$$\|\mathbf{b}\|^2 = 2^2 + 2^2 = 8$$
Thus, the orthogonal projection of $\mathbf{v}$ on $\mathbf{b}$ is
$$\operatorname{proj}_{\mathbf{b}}\mathbf{v} = \frac{\mathbf{v} \cdot \mathbf{b}}{\|\mathbf{b}\|^2}\mathbf{b} = \frac{4}{8}(2\mathbf{i} + 2\mathbf{j}) = \mathbf{i} + \mathbf{j}$$
and the vector component of $\mathbf{v}$ orthogonal to $\mathbf{b}$ is
$$\mathbf{v} - \operatorname{proj}_{\mathbf{b}}\mathbf{v} = (\mathbf{i} + \mathbf{j} + \mathbf{k}) - (\mathbf{i} + \mathbf{j}) = \mathbf{k}$$

---

### WORK

In Section 5.6 we discussed the work done by a constant force acting on an object that moves along a line. We defined the work $W$ done on the object by a constant force of magnitude $F$ acting in the direction of motion over a distance $d$ to be
$$W = Fd = \text{force} \times \text{distance} \tag{13}$$
If we let $\mathbf{F}$ denote a force vector of magnitude $\|\mathbf{F}\| = F$ acting in the direction of motion, then we can write (13) as $W = \|\mathbf{F}\|d$. Furthermore, if we assume that the object moves along a line from point $P$ to point $Q$, then $d = \|\vec{PQ}\|$, so that the work can be expressed entirely in vector form as
$$W = \|\mathbf{F}\|\|\vec{PQ}\|$$
The vector $\vec{PQ}$ is called the **displacement vector** for the object. In the case where a constant force $\mathbf{F}$ is not in the direction of motion, but rather makes an angle $\theta$ with the displacement vector, then we define the work $W$ done by $\mathbf{F}$ to be
$$W = (\|\mathbf{F}\|\cos\theta)\|\vec{PQ}\| = \mathbf{F} \cdot \vec{PQ} \tag{14}$$

#### Example 8
(a) A wagon is pulled horizontally by exerting a constant force of $10\text{ lb}$ on the handle at an angle of $60^\circ$ with the horizontal. How much work is done in moving the wagon $50\text{ ft}$?  
(b) A force of $\mathbf{F} = 3\mathbf{i} - \mathbf{j} + 2\mathbf{k}\text{ lb}$ is applied to a point that moves on a line from $P(-1, 1, 2)$ to $Q(3, 0, -2)$. If distance is measured in feet, how much work is done?

**Solution (a).** With $\|\mathbf{F}\| = 10, \theta = 60^\circ,$ and $\|\vec{PQ}\| = 50$, it follows that the work done is
$$W = (\|\mathbf{F}\|\cos\theta)\|\vec{PQ}\| = 10 \cdot \frac{1}{2} \cdot 50 = 250\text{ ft}\cdot\text{lb}$$

**Solution (b).** Since $\vec{PQ} = (3 - (-1))\mathbf{i} + (0 - 1)\mathbf{j} + (-2 - 2)\mathbf{k} = 4\mathbf{i} - \mathbf{j} - 4\mathbf{k}$, the work done is
$$W = \mathbf{F} \cdot \vec{PQ} = (3\mathbf{i} - \mathbf{j} + 2\mathbf{k}) \cdot (4\mathbf{i} - \mathbf{j} - 4\mathbf{k}) = 12 + 1 - 8 = 5\text{ ft}\cdot\text{lb}$$

---

### QUICK CHECK EXERCISES 11.3
*(See page 794 for answers.)*

1. $\langle 3, 1, -2 \rangle \cdot \langle 6, 0, 5 \rangle = \underline{\quad}$.
2. Suppose that $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ are vectors in 3-space such that $\|\mathbf{u}\| = 5, \mathbf{u} \cdot \mathbf{v} = 7,$ and $\mathbf{u} \cdot \mathbf{w} = -3$.  
   (a) $\mathbf{u} \cdot \mathbf{u} = \underline{\quad}$  
   (b) $\mathbf{v} \cdot \mathbf{u} = \underline{\quad}$  
   (c) $\mathbf{u} \cdot (\mathbf{v} - \mathbf{w}) = \underline{\quad}$  
   (d) $\mathbf{u} \cdot (2\mathbf{w}) = \underline{\quad}$.
3. For the vectors $\mathbf{u}$ and $\mathbf{v}$ in the preceding exercise, if the angle between $\mathbf{u}$ and $\mathbf{v}$ is $\pi/3$, then $\|\mathbf{v}\| = \underline{\quad}$.
4. The direction cosines of $\langle 2, -1, 3 \rangle$ are $\cos\alpha = \underline{\quad}, \cos\beta = \underline{\quad},$ and $\cos\gamma = \underline{\quad}$.
5. The orthogonal projection of $\mathbf{v} = 10\mathbf{i}$ on $\mathbf{b} = -3\mathbf{i} + \mathbf{j}$ is $\underline{\quad}$.

---

### EXERCISE SET 11.3

**1. In each part, find the dot product of the vectors and the cosine of the angle between them.**  
(a) $\mathbf{u} = \mathbf{i} + 2\mathbf{j}, \mathbf{v} = 6\mathbf{i} - 8\mathbf{j}$  
(b) $\mathbf{u} = \langle -7, -3 \rangle, \mathbf{v} = \langle 0, 1 \rangle$  
(c) $\mathbf{u} = \mathbf{i} - 3\mathbf{j} + 7\mathbf{k}, \mathbf{v} = 8\mathbf{i} - 2\mathbf{j} - 2\mathbf{k}$  
(d) $\mathbf{u} = \langle -3, 1, 2 \rangle, \mathbf{v} = \langle 4, 2, -5 \rangle$

**2. In each part use the given information to find $\mathbf{u} \cdot \mathbf{v}$.**  
(a) $\|\mathbf{u}\| = 1, \|\mathbf{v}\| = 2$, the angle between $\mathbf{u}$ and $\mathbf{v}$ is $\pi/6$.  
(b) $\|\mathbf{u}\| = 2, \|\mathbf{v}\| = 3$, the angle between $\mathbf{u}$ and $\mathbf{v}$ is $135^\circ$.

**3. In each part, determine whether $\mathbf{u}$ and $\mathbf{v}$ make an acute angle, an obtuse angle, or are orthogonal.**  
(a) $\mathbf{u} = 7\mathbf{i} + 3\mathbf{j} + 5\mathbf{k}, \mathbf{v} = -8\mathbf{i} + 4\mathbf{j} + 2\mathbf{k}$  
(b) $\mathbf{u} = 6\mathbf{i} + \mathbf{j} + 3\mathbf{k}, \mathbf{v} = 4\mathbf{i} - 6\mathbf{k}$  
(c) $\mathbf{u} = \langle 1, 1, 1 \rangle, \mathbf{v} = \langle -1, 0, 0 \rangle$  
(d) $\mathbf{u} = \langle 4, 1, 6 \rangle, \mathbf{v} = \langle -3, 0, 2 \rangle$

#### FOCUS ON CONCEPTS

4. Does the triangle in 3-space with vertices $(-1, 2, 3), (2, -2, 0),$ and $(3, 1, -4)$ have an obtuse angle? Justify your answer.
5. The accompanying figure shows eight vectors that are equally spaced around a circle of radius 1. Find the dot product of $\mathbf{v}_0$ with each of the other seven vectors.
6. The accompanying figure shows six vectors that are equally spaced around a circle of radius 5. Find the dot product of $\mathbf{v}_0$ with each of the other five vectors.
7. (a) Use vectors to show that $A(2, -1, 1), B(3, 2, -1),$ and $C(7, 0, -2)$ are vertices of a right triangle. At which vertex is the right angle?  
   (b) Use vectors to find the interior angles of the triangle with vertices $(-1, 0), (2, -1),$ and $(1, 4)$. Express your answers to the nearest degree.
8. (a) Show that if $\mathbf{v} = a\mathbf{i} + b\mathbf{j}$ is a vector in 2-space, then the vectors $\mathbf{v}_1 = -b\mathbf{i} + a\mathbf{j}$ and $\mathbf{v}_2 = b\mathbf{i} - a\mathbf{j}$ are both orthogonal to $\mathbf{v}$.  
   (b) Use the result in part (a) to find two unit vectors that are orthogonal to the vector $\mathbf{v} = 3\mathbf{i} - 2\mathbf{j}$. Sketch the vectors $\mathbf{v}, \mathbf{v}_1,$ and $\mathbf{v}_2$.
9. Explain why each of the following expressions makes no sense:  
   (a) $\mathbf{u} \cdot (\mathbf{v} \cdot \mathbf{w})$  
   (b) $(\mathbf{u} \cdot \mathbf{v}) + \mathbf{w}$  
   (c) $\|\mathbf{u} \cdot \mathbf{v}\|$  
   (d) $k \cdot (\mathbf{u} + \mathbf{v})$
10. Explain why each of the following expressions makes sense:  
    (a) $(\mathbf{u} \cdot \mathbf{v})\mathbf{w}$  
    (b) $(\mathbf{u} \cdot \mathbf{v})(\mathbf{v} \cdot \mathbf{w})$  
    (c) $\mathbf{u} \cdot \mathbf{v} + k$  
    (d) $(k\mathbf{u}) \cdot \mathbf{v}$
11. Verify parts (b) and (c) of Theorem 11.3.2 for the vectors $\mathbf{u} = 6\mathbf{i} - \mathbf{j} + 2\mathbf{k}, \mathbf{v} = 2\mathbf{i} + 7\mathbf{j} + 4\mathbf{k}, \mathbf{w} = \mathbf{i} + \mathbf{j} - 3\mathbf{k}$ and $k = -5$.
12. Let $\mathbf{u} = \langle 1, 2 \rangle, \mathbf{v} = \langle 4, -2 \rangle,$ and $\mathbf{w} = \langle 6, 0 \rangle$. Find:  
    (a) $\mathbf{u} \cdot (7\mathbf{v} + \mathbf{w})$  
    (b) $\|(\mathbf{u} \cdot \mathbf{w})\mathbf{w}\|$  
    (c) $\|\mathbf{u}\|(\mathbf{v} \cdot \mathbf{w})$  
    (d) $(\|\mathbf{u}\|\mathbf{v}) \cdot \mathbf{w}$
13. Find $r$ so that the vector from the point $A(1, -1, 3)$ to the point $B(3, 0, 5)$ is orthogonal to the vector from $A$ to the point $P(r, r, r)$.
14. Find two unit vectors in 2-space that make an angle of $45^\circ$ with $4\mathbf{i} + 3\mathbf{j}$.

**15–16 Find the direction cosines of $\mathbf{v}$ and confirm that they satisfy Equation (5). Then use the direction cosines to approximate the direction angles to the nearest degree.**
15. (a) $\mathbf{v} = \mathbf{i} + \mathbf{j} - \mathbf{k}$  
    (b) $\mathbf{v} = 2\mathbf{i} - 2\mathbf{j} + \mathbf{k}$
16. (a) $\mathbf{v} = 3\mathbf{i} - 2\mathbf{j} - 6\mathbf{k}$  
    (b) $\mathbf{v} = 3\mathbf{i} - 4\mathbf{k}$

#### FOCUS ON CONCEPTS

17. Show that the direction cosines of a vector satisfy $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$.
18. Let $\theta$ and $\lambda$ be the angles shown in Figure Ex-18. Show that the direction cosines of $\mathbf{v}$ can be expressed as
    $$\cos\alpha = \cos\lambda\cos\theta, \quad \cos\beta = \cos\lambda\sin\theta, \quad \cos\gamma = \sin\lambda$$
    *[Hint: Express $\mathbf{v}$ in component form and normalize.]*
19. The accompanying figure shows a cube.  
    (a) Find the angle between the vectors $\mathbf{d}$ and $\mathbf{u}$ to the nearest degree.  
    (b) Make a conjecture about the angle between the vectors $\mathbf{d}$ and $\mathbf{v}$, and confirm your conjecture by computing the angle.
20. Show that two nonzero vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are orthogonal if and only if their direction cosines satisfy
    $$\cos\alpha_1\cos\alpha_2 + \cos\beta_1\cos\beta_2 + \cos\gamma_1\cos\gamma_2 = 0$$
21. Use the result in Exercise 18 to find the direction angles of the vector shown in Figure Ex-21 to the nearest degree ($\theta = 60^\circ, \lambda = 30^\circ$).
22. Find, to the nearest degree, the acute angle formed by two diagonals of a cube.
23. Find, to the nearest degree, the angles that a diagonal of a box with dimensions $10\text{ cm}$ by $15\text{ cm}$ by $25\text{ cm}$ makes with the edges of the box.

**24. In each part, find the vector component of $\mathbf{v}$ along $\mathbf{b}$ and the vector component of $\mathbf{v}$ orthogonal to $\mathbf{b}$. Then sketch the vectors $\mathbf{v}, \operatorname{proj}_{\mathbf{b}}\mathbf{v},$ and $\mathbf{v} - \operatorname{proj}_{\mathbf{b}}\mathbf{v}$.**  
(a) $\mathbf{v} = 2\mathbf{i} - \mathbf{j}, \mathbf{b} = 3\mathbf{i} + 4\mathbf{j}$  
(b) $\mathbf{v} = \langle 4, 5 \rangle, \mathbf{b} = \langle 1, -2 \rangle$  
(c) $\mathbf{v} = -3\mathbf{i} - 2\mathbf{j}, \mathbf{b} = 2\mathbf{i} + \mathbf{j}$

**25. In each part, find the vector component of $\mathbf{v}$ along $\mathbf{b}$ and the vector component of $\mathbf{v}$ orthogonal to $\mathbf{b}$.**  
(a) $\mathbf{v} = 2\mathbf{i} - \mathbf{j} + 3\mathbf{k}, \mathbf{b} = \mathbf{i} + 2\mathbf{j} + 2\mathbf{k}$  
(b) $\mathbf{v} = \langle 4, -1, 7 \rangle, \mathbf{b} = \langle 2, 3, -6 \rangle$

**26–27 Express the vector $\mathbf{v}$ as the sum of a vector parallel to $\mathbf{b}$ and a vector orthogonal to $\mathbf{b}$.**  
26. (a) $\mathbf{v} = 2\mathbf{i} - 4\mathbf{j}, \mathbf{b} = \mathbf{i} + \mathbf{j}$  
    (b) $\mathbf{v} = 3\mathbf{i} + \mathbf{j} - 2\mathbf{k}, \mathbf{b} = 2\mathbf{i} - \mathbf{k}$  
    (c) $\mathbf{v} = 4\mathbf{i} - 2\mathbf{j} + 6\mathbf{k}, \mathbf{b} = -2\mathbf{i} + \mathbf{j} - 3\mathbf{k}$  
27. (a) $\mathbf{v} = \langle -3, 5 \rangle, \mathbf{b} = \langle 1, 1 \rangle$  
    (b) $\mathbf{v} = \langle -2, 1, 6 \rangle, \mathbf{b} = \langle 0, -2, 1 \rangle$  
    (c) $\mathbf{v} = \langle 1, 4, 1 \rangle, \mathbf{b} = \langle 3, -2, 5 \rangle$

**28–31 True–False Determine whether the statement is true or false. Explain your answer.**  
28. If $\mathbf{a} \cdot \mathbf{b} = \mathbf{a} \cdot \mathbf{c}$ and $\mathbf{a} \neq \mathbf{0}$, then $\mathbf{b} = \mathbf{c}$.  
29. If $\mathbf{v}$ and $\mathbf{w}$ are nonzero orthogonal vectors, then $\|\mathbf{v} + \mathbf{w}\| \neq 0$.  
30. If $\mathbf{u}$ is a unit vector that is parallel to a nonzero vector $\mathbf{v}$, then $\mathbf{u} \cdot \mathbf{v} = \pm\|\mathbf{v}\|$.  
31. If $\mathbf{v}$ and $\mathbf{b}$ are nonzero vectors, then the orthogonal projection of $\mathbf{v}$ on $\mathbf{b}$ is a vector that is parallel to $\mathbf{b}$.

32. If $L$ is a line in 2-space or 3-space that passes through the points $A$ and $B$, then the distance from a point $P$ to the line $L$ is equal to the length of the component of the vector $\vec{AP}$ that is orthogonal to the vector $\vec{AB}$ (see Figure Ex-32). Use this result to find the distance from the point $P(1, 0)$ to the line through $A(2, -3)$ and $B(5, 1)$.
33. Use the method of Exercise 32 to find the distance from the point $P(-3, 1, 2)$ to the line through $A(1, 1, 0)$ and $B(-2, 3, -4)$.
34. As shown in Figure Ex-34, a child with mass $34\text{ kg}$ is seated on a smooth (frictionless) playground slide that is inclined at an angle of $27^\circ$ with the horizontal. Estimate the force that the child exerts on the slide, and estimate how much force must be applied in the direction of $P$ to prevent the child from sliding down the slide. Take the acceleration due to gravity to be $9.8\text{ m/s}^2$.
35. For the child in Exercise 34, estimate how much force must be applied in the direction of $Q$ (shown in Figure Ex-35) to prevent the child from sliding down the slide?
36. Suppose that the slide in Exercise 34 is $4\text{ m}$ long. Estimate the work done by gravity if the child slides from the top of the slide to the bottom.
37. A box is dragged along the floor by a rope that applies a force of $50\text{ lb}$ at an angle of $60^\circ$ with the floor. How much work is done in moving the box $15\text{ ft}$?
38. Find the work done by a force $\mathbf{F} = -3\mathbf{j}\text{ pounds}$ applied to a point that moves on a line from $(1, 3)$ to $(4, 7)$. Assume that distance is measured in feet.
39. A force of $\mathbf{F} = 4\mathbf{i} - 6\mathbf{j} + \mathbf{k}\text{ newtons}$ is applied to a point that moves a distance of $15\text{ meters}$ in the direction of the vector $\mathbf{i} + \mathbf{j} + \mathbf{k}$. How much work is done?
40. A boat travels $100\text{ meters}$ due north while the wind exerts a force of $500\text{ newtons}$ toward the northeast. How much work does the wind do?

#### FOCUS ON CONCEPTS

41. Let $\mathbf{u}$ and $\mathbf{v}$ be adjacent sides of a parallelogram. Use vectors to prove that the diagonals of the parallelogram are perpendicular if the sides are equal in length.
42. Let $\mathbf{u}$ and $\mathbf{v}$ be adjacent sides of a parallelogram. Use vectors to prove that the parallelogram is a rectangle if the diagonals are equal in length.
43. Prove that
    $$\|\mathbf{u} + \mathbf{v}\|^2 + \|\mathbf{u} - \mathbf{v}\|^2 = 2\|\mathbf{u}\|^2 + 2\|\mathbf{v}\|^2$$
    and interpret the result geometrically by translating it into a theorem about parallelograms.
44. Prove: $\mathbf{u} \cdot \mathbf{v} = \frac{1}{4}\|\mathbf{u} + \mathbf{v}\|^2 - \frac{1}{4}\|\mathbf{u} - \mathbf{v}\|^2$.
45. Show that if $\mathbf{v}_1, \mathbf{v}_2,$ and $\mathbf{v}_3$ are mutually orthogonal nonzero vectors in 3-space, and if a vector $\mathbf{v}$ in 3-space is expressed as
    $$\mathbf{v} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3$$
    then the scalars $c_1, c_2,$ and $c_3$ are given by the formulas
    $$c_i = \frac{\mathbf{v} \cdot \mathbf{v}_i}{\|\mathbf{v}_i\|^2}, \quad i = 1, 2, 3$$
46. Show that the three vectors
    $$\mathbf{v}_1 = 3\mathbf{i} - \mathbf{j} + 2\mathbf{k}, \quad \mathbf{v}_2 = \mathbf{i} + \mathbf{j} - \mathbf{k}, \quad \mathbf{v}_3 = \mathbf{i} - 5\mathbf{j} - 4\mathbf{k}$$
    are mutually orthogonal, and then use the result of Exercise 45 to find scalars $c_1, c_2,$ and $c_3$ so that
    $$c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3 = \mathbf{i} - \mathbf{j} + \mathbf{k}$$
47. For each $x$ in $(-\infty, +\infty)$, let $\mathbf{u}(x)$ be the vector from the origin to the point $P(x, y)$ on the curve $y = x^2 + 1$, and $\mathbf{v}(x)$ the vector from the origin to the point $Q(x, y)$ on the line $y = -x - 1$.  
    (a) Use a CAS to find, to the nearest degree, the minimum angle between $\mathbf{u}(x)$ and $\mathbf{v}(x)$ for $x$ in $(-\infty, +\infty)$.  
    (b) Determine whether there are any real values of $x$ for which $\mathbf{u}(x)$ and $\mathbf{v}(x)$ are orthogonal.
48. Let $\mathbf{u}$ be a unit vector in the $xy$-plane of an $xyz$-coordinate system, and let $\mathbf{v}$ be a unit vector in the $yz$-plane. Let $\theta_1$ be the angle between $\mathbf{u}$ and $\mathbf{i}$, let $\theta_2$ be the angle between $\mathbf{v}$ and $\mathbf{k}$, and let $\theta$ be the angle between $\mathbf{u}$ and $\mathbf{v}$.  
    (a) Show that $\cos\theta = \pm\sin\theta_1\sin\theta_2$.  
    (b) Find $\theta$ if $\theta$ is acute and $\theta_1 = \theta_2 = 45^\circ$.  
    (c) Use a CAS to find, to the nearest degree, the maximum and minimum values of $\theta$ if $\theta$ is acute and $\theta_2 = 2\theta_1$.
49. Prove parts (b) and (e) of Theorem 11.3.2 for vectors in 3-space.
50. **Writing.** Discuss some of the similarities and differences between the multiplication properties of real numbers and those of the dot product of vectors.
51. **Writing.** Discuss the merits of the following claim: "Suppose an algebraic identity involves only the addition, subtraction, and multiplication of real numbers. If the numbers are replaced by vectors, and the multiplication is replaced by the dot product, then an identity involving vectors will result."

#### QUICK CHECK ANSWERS 11.3
1. 8  
2. (a) 25 (b) 7 (c) 10 (d) -6  
3. $14/5$  
4. $\frac{2}{\sqrt{14}}; -\frac{1}{\sqrt{14}}; \frac{3}{\sqrt{14}}$  
5. $9\mathbf{i} - 3\mathbf{j}$

---

## 11.4 CROSS PRODUCT

In many applications of vectors in mathematics, physics, and engineering, there is a need to find a vector that is orthogonal to two given vectors. In this section we will discuss a new type of vector multiplication that can be used for this purpose.

### DETERMINANTS

Some of the concepts that we will develop in this section require basic ideas about **determinants**, which are functions that assign numerical values to square arrays of numbers. For example, if $a_1, a_2, b_1,$ and $b_2$ are real numbers, then we define a **$2 \times 2$ determinant** by
$$\begin{vmatrix} a_1 & a_2 \\ b_1 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1 \tag{1}$$
For example,
$$\begin{vmatrix} 3 & -2 \\ 4 & 5 \end{vmatrix} = (3)(5) - (-2)(4) = 15 + 8 = 23$$
A **$3 \times 3$ determinant** is defined in terms of $2 \times 2$ determinants by
$$\begin{vmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{vmatrix} = a_1 \begin{vmatrix} b_2 & b_3 \\ c_2 & c_3 \end{vmatrix} - a_2 \begin{vmatrix} b_1 & b_3 \\ c_1 & c_3 \end{vmatrix} + a_3 \begin{vmatrix} b_1 & b_2 \\ c_1 & c_2 \end{vmatrix} \tag{2}$$
For example,
$$\begin{vmatrix} 3 & -2 & -5 \\ 1 & 4 & -4 \\ 0 & 3 & 2 \end{vmatrix} = 3 \begin{vmatrix} 4 & -4 \\ 3 & 2 \end{vmatrix} - (-2) \begin{vmatrix} 1 & -4 \\ 0 & 2 \end{vmatrix} + (-5) \begin{vmatrix} 1 & 4 \\ 0 & 3 \end{vmatrix} = 3(20) + 2(2) - 5(3) = 49$$

> **11.4.1 THEOREM**  
> (a) If two rows in the array of a determinant are the same, then the value of the determinant is 0.  
> (b) Interchanging two rows in the array of a determinant multiplies its value by $-1$.

**PROOF (a)**  
$$\begin{vmatrix} a_1 & a_2 \\ a_1 & a_2 \end{vmatrix} = a_1 a_2 - a_2 a_1 = 0$$

**PROOF (b)**  
$$\begin{vmatrix} b_1 & b_2 \\ a_1 & a_2 \end{vmatrix} = b_1 a_2 - b_2 a_1 = -(a_1 b_2 - a_2 b_1) = -\begin{vmatrix} a_1 & a_2 \\ b_1 & b_2 \end{vmatrix} \quad \blacksquare$$

---

### CROSS PRODUCT

> **11.4.2 DEFINITION**  
> If $\mathbf{u} = \langle u_1, u_2, u_3 \rangle$ and $\mathbf{v} = \langle v_1, v_2, v_3 \rangle$ are vectors in 3-space, then the **cross product** $\mathbf{u} \times \mathbf{v}$ is the vector defined by
> $$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} u_2 & u_3 \\ v_2 & v_3 \end{vmatrix}\mathbf{i} - \begin{vmatrix} u_1 & u_3 \\ v_1 & v_3 \end{vmatrix}\mathbf{j} + \begin{vmatrix} u_1 & u_2 \\ v_1 & v_2 \end{vmatrix}\mathbf{k} \tag{3}$$
> or, equivalently,
> $$\mathbf{u} \times \mathbf{v} = (u_2 v_3 - u_3 v_2)\mathbf{i} - (u_1 v_3 - u_3 v_1)\mathbf{j} + (u_1 v_2 - u_2 v_1)\mathbf{k} \tag{4}$$

We can rewrite (3) symbolically as
$$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} \tag{5}$$

#### Example 1
Let $\mathbf{u} = \langle 1, 2, -2 \rangle$ and $\mathbf{v} = \langle 3, 0, 1 \rangle$. Find (a) $\mathbf{u} \times \mathbf{v}$ and (b) $\mathbf{v} \times \mathbf{u}$.

**Solution (a).**
$$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 2 & -2 \\ 3 & 0 & 1 \end{vmatrix} = \begin{vmatrix} 2 & -2 \\ 0 & 1 \end{vmatrix}\mathbf{i} - \begin{vmatrix} 1 & -2 \\ 3 & 1 \end{vmatrix}\mathbf{j} + \begin{vmatrix} 1 & 2 \\ 3 & 0 \end{vmatrix}\mathbf{k} = 2\mathbf{i} - 7\mathbf{j} - 6\mathbf{k}$$

**Solution (b).** Reversing $\mathbf{u}$ and $\mathbf{v}$ interchanges the second and third rows, which reverses the sign:
$$\mathbf{v} \times \mathbf{u} = -(\mathbf{u} \times \mathbf{v}) = -2\mathbf{i} + 7\mathbf{j} + 6\mathbf{k}$$

#### Example 2
Show that $\mathbf{u} \times \mathbf{u} = \mathbf{0}$ for any vector $\mathbf{u}$ in 3-space.

**Solution.** If the two factors in a cross product are the same, each $2 \times 2$ determinant has identical rows and is zero. Thus, $\mathbf{u} \times \mathbf{u} = \mathbf{0}$.

---

### ALGEBRAIC PROPERTIES OF THE CROSS PRODUCT

> **11.4.3 THEOREM**  
> If $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ are any vectors in 3-space and $k$ is any scalar, then:
> (a) $\mathbf{u} \times \mathbf{v} = -(\mathbf{v} \times \mathbf{u})$  
> (b) $\mathbf{u} \times (\mathbf{v} + \mathbf{w}) = (\mathbf{u} \times \mathbf{v}) + (\mathbf{u} \times \mathbf{w})$  
> (c) $(\mathbf{u} + \mathbf{v}) \times \mathbf{w} = (\mathbf{u} \times \mathbf{w}) + (\mathbf{v} \times \mathbf{w})$  
> (d) $k(\mathbf{u} \times \mathbf{v}) = (k\mathbf{u}) \times \mathbf{v} = \mathbf{u} \times (k\mathbf{v})$  
> (e) $\mathbf{u} \times \mathbf{0} = \mathbf{0} \times \mathbf{u} = \mathbf{0}$  
> (f) $\mathbf{u} \times \mathbf{u} = \mathbf{0}$

Standard cross products of unit coordinate vectors:
$$\mathbf{i} \times \mathbf{j} = \mathbf{k}, \quad \mathbf{j} \times \mathbf{k} = \mathbf{i}, \quad \mathbf{k} \times \mathbf{i} = \mathbf{j}$$
$$\mathbf{j} \times \mathbf{i} = -\mathbf{k}, \quad \mathbf{k} \times \mathbf{j} = -\mathbf{i}, \quad \mathbf{i} \times \mathbf{k} = -\mathbf{j} \tag{6}$$

> **WARNING**  
> The associative law does NOT hold for cross products:
> $$\mathbf{i} \times (\mathbf{j} \times \mathbf{j}) = \mathbf{i} \times \mathbf{0} = \mathbf{0} \quad \text{and} \quad (\mathbf{i} \times \mathbf{j}) \times \mathbf{j} = \mathbf{k} \times \mathbf{j} = -\mathbf{i}$$
> Thus, $\mathbf{u} \times \mathbf{v} \times \mathbf{w}$ is ambiguous without parentheses.

---

### GEOMETRIC PROPERTIES OF THE CROSS PRODUCT

> **11.4.4 THEOREM**  
> If $\mathbf{u}$ and $\mathbf{v}$ are vectors in 3-space, then:  
> (a) $\mathbf{u} \cdot (\mathbf{u} \times \mathbf{v}) = 0$ ($\mathbf{u} \times \mathbf{v}$ is orthogonal to $\mathbf{u}$)  
> (b) $\mathbf{v} \cdot (\mathbf{u} \times \mathbf{v}) = 0$ ($\mathbf{u} \times \mathbf{v}$ is orthogonal to $\mathbf{v}$)

**PROOF (a)**  
Let $\mathbf{u} = \langle u_1, u_2, u_3 \rangle$ and $\mathbf{v} = \langle v_1, v_2, v_3 \rangle$. Then
$$\mathbf{u} \cdot (\mathbf{u} \times \mathbf{v}) = u_1(u_2 v_3 - u_3 v_2) + u_2(u_3 v_1 - u_1 v_3) + u_3(u_1 v_2 - u_2 v_1) = 0 \quad \blacksquare$$

#### Example 3
Find a vector that is orthogonal to both of the vectors $\mathbf{u} = \langle 2, -1, 3 \rangle$ and $\mathbf{v} = \langle -7, 2, -1 \rangle$.

**Solution.**
$$\mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2 & -1 & 3 \\ -7 & 2 & -1 \end{vmatrix} = -5\mathbf{i} - 19\mathbf{j} - 3\mathbf{k}$$

> **11.4.5 THEOREM**  
> Let $\mathbf{u}$ and $\mathbf{v}$ be nonzero vectors in 3-space, and let $\theta$ be the angle between these vectors when they are positioned so their initial points coincide.  
> (a) $\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\|\|\mathbf{v}\|\sin\theta$  
> (b) The area $A$ of the parallelogram that has $\mathbf{u}$ and $\mathbf{v}$ as adjacent sides is
> $$A = \|\mathbf{u} \times \mathbf{v}\| \tag{8}$$
> (c) $\mathbf{u} \times \mathbf{v} = \mathbf{0}$ if and only if $\mathbf{u}$ and $\mathbf{v}$ are parallel vectors, that is, if and only if they are scalar multiples of one another.

**PROOF (a)**  
$$\|\mathbf{u}\|\|\mathbf{v}\|\sin\theta = \|\mathbf{u}\|\|\mathbf{v}\|\sqrt{1 - \cos^2\theta} = \sqrt{\|\mathbf{u}\|^2\|\mathbf{v}\|^2 - (\mathbf{u} \cdot \mathbf{v})^2}$$
$$= \sqrt{(u_1^2 + u_2^2 + u_3^2)(v_1^2 + v_2^2 + v_3^2) - (u_1 v_1 + u_2 v_2 + u_3 v_3)^2}$$
$$= \sqrt{(u_2 v_3 - u_3 v_2)^2 + (u_1 v_3 - u_3 v_1)^2 + (u_1 v_2 - u_2 v_1)^2} = \|\mathbf{u} \times \mathbf{v}\| \quad \blacksquare$$

**PROOF (b)**  
The parallelogram with adjacent sides $\mathbf{u}$ and $\mathbf{v}$ has base $\|\mathbf{u}\|$ and altitude $\|\mathbf{v}\|\sin\theta$. Thus, its area $A = (\text{base})(\text{altitude}) = \|\mathbf{u}\|\|\mathbf{v}\|\sin\theta = \|\mathbf{u} \times \mathbf{v}\|$. $\blacksquare$

#### Example 4
Find the area of the triangle that is determined by the points $P_1(2, 2, 0), P_2(-1, 0, 2),$ and $P_3(0, 4, 3)$.

**Solution.** The area $A$ of the triangle is half the area of the parallelogram determined by $\vec{P_1P_2} = \langle -3, -2, 2 \rangle$ and $\vec{P_1P_3} = \langle -2, 2, 3 \rangle$:
$$\vec{P_1P_2} \times \vec{P_1P_3} = \langle -10, 5, -10 \rangle \implies A = \frac{1}{2}\|\vec{P_1P_2} \times \vec{P_1P_3}\| = \frac{1}{2}\sqrt{100 + 25 + 100} = \frac{15}{2}$$

---

### SCALAR TRIPLE PRODUCTS

If $\mathbf{u} = \langle u_1, u_2, u_3 \rangle, \mathbf{v} = \langle v_1, v_2, v_3 \rangle,$ and $\mathbf{w} = \langle w_1, w_2, w_3 \rangle$ are vectors in 3-space, then the number $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$ is called the **scalar triple product** of $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$:
$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix} \tag{9}$$

#### Example 5
Calculate the scalar triple product $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$ of $\mathbf{u} = 3\mathbf{i} - 2\mathbf{j} - 5\mathbf{k}, \mathbf{v} = \mathbf{i} + 4\mathbf{j} - 4\mathbf{k}, \mathbf{w} = 3\mathbf{j} + 2\mathbf{k}$.

**Solution.**
$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \begin{vmatrix} 3 & -2 & -5 \\ 1 & 4 & -4 \\ 0 & 3 & 2 \end{vmatrix} = 49$$

> **11.4.6 THEOREM**  
> Let $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ be nonzero vectors in 3-space.  
> (a) The volume $V$ of the parallelepiped that has $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ as adjacent edges is
> $$V = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})| \tag{10}$$
> (b) $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = 0$ if and only if $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ lie in the same plane.

**PROOF (a)**  
Area of base $= \|\mathbf{v} \times \mathbf{w}\|$, altitude $h = \|\operatorname{proj}_{\mathbf{v} \times \mathbf{w}}\mathbf{u}\| = \frac{|\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})|}{\|\mathbf{v} \times \mathbf{w}\|}$.  
Thus, $V = (\text{area of base})(\text{height}) = \|\mathbf{v} \times \mathbf{w}\| h = |\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})|$. $\blacksquare$

---

### ALGEBRAIC PROPERTIES OF THE SCALAR TRIPLE PRODUCT

* Cyclic permutations leave value invariant:
  $$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \mathbf{w} \cdot (\mathbf{u} \times \mathbf{v}) = \mathbf{v} \cdot (\mathbf{w} \times \mathbf{u}) \tag{11}$$
* Interchanging dot and cross:
  $$\mathbf{u} \cdot \mathbf{v} \times \mathbf{w} = \mathbf{u} \times \mathbf{v} \cdot \mathbf{w} \tag{12}$$

---

### MOMENTS AND ROTATIONAL MOTION IN 3-SPACE

The tendency of rotation about a point $P$ caused by a force $\mathbf{F}$ applied at $Q$ is measured by
$$\|\vec{PQ}\|\|\mathbf{F}_2\| = \|\vec{PQ}\|\|\mathbf{F}\|\sin\theta = \|\vec{PQ} \times \mathbf{F}\| \tag{15}$$
This is called the **scalar moment** (or **torque**) of $\mathbf{F}$ about $P$. The vector $\vec{PQ} \times \mathbf{F}$ is called the **vector moment** (or **torque vector**) of $\mathbf{F}$ about $P$.

#### Example 6
Figure 11.4.8a shows a force $\mathbf{F}$ of $100\text{ N}$ applied in the positive $z$-direction at the point $Q(1, 1, 1)$ of a cube whose sides have a length of $1\text{ m}$. Assuming that the cube is free to rotate about $P(0, 0, 0)$, find the scalar moment of the force about $P$, and describe the direction of rotation.

**Solution.** $\mathbf{F} = 100\mathbf{k}, \vec{PQ} = \mathbf{i} + \mathbf{j} + \mathbf{k}$.
$$\vec{PQ} \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 1 \\ 0 & 0 & 100 \end{vmatrix} = 100\mathbf{i} - 100\mathbf{j}$$
Scalar moment $= \|100\mathbf{i} - 100\mathbf{j}\| = 100\sqrt{2} \approx 141\text{ N}\cdot\text{m}$, counterclockwise looking along $100(\mathbf{i} - \mathbf{j})$ toward its initial point.

---

### QUICK CHECK EXERCISES 11.4
*(See page 805 for answers.)*

1. (a) $\begin{vmatrix} 3 & 2 \\ 4 & 5 \end{vmatrix} = \underline{\quad}$  
   (b) $\begin{vmatrix} 3 & 2 & 1 \\ 3 & 2 & 1 \\ 5 & 5 & 5 \end{vmatrix} = \underline{\quad}$.
2. $\langle 1, 2, 0 \rangle \times \langle 3, 0, 4 \rangle = \underline{\quad}$.
3. Suppose that $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ are vectors in 3-space such that $\mathbf{u} \times \mathbf{v} = \langle 2, 7, 3 \rangle$ and $\mathbf{u} \times \mathbf{w} = \langle -5, 4, 0 \rangle$.  
   (a) $\mathbf{u} \times \mathbf{u} = \underline{\quad}$  
   (b) $\mathbf{v} \times \mathbf{u} = \underline{\quad}$  
   (c) $\mathbf{u} \times (\mathbf{v} + \mathbf{w}) = \underline{\quad}$  
   (d) $\mathbf{u} \times (2\mathbf{w}) = \underline{\quad}$.
4. Let $\mathbf{u} = \mathbf{i} - 5\mathbf{k}, \mathbf{v} = 2\mathbf{i} - 4\mathbf{j} + \mathbf{k},$ and $\mathbf{w} = 3\mathbf{i} - 2\mathbf{j} + 5\mathbf{k}$.  
   (a) $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \underline{\quad}$  
   (b) The volume of the parallelepiped that has $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ as adjacent edges is $V = \underline{\quad}$.

---

### EXERCISE SET 11.4

**1. (a) Use a determinant to find the cross product $\mathbf{i} \times (\mathbf{i} + \mathbf{j} + \mathbf{k})$.**  
(b) Check your answer in part (a) by rewriting the cross product as $\mathbf{i} \times (\mathbf{i} + \mathbf{j} + \mathbf{k}) = (\mathbf{i} \times \mathbf{i}) + (\mathbf{i} \times \mathbf{j}) + (\mathbf{i} \times \mathbf{k})$ and evaluating each term.

**2. In each part, use the two methods in Exercise 1 to find:**  
(a) $\mathbf{j} \times (\mathbf{i} + \mathbf{j} + \mathbf{k})$  
(b) $\mathbf{k} \times (\mathbf{i} + \mathbf{j} + \mathbf{k})$

**3–6 Find $\mathbf{u} \times \mathbf{v}$ and check that it is orthogonal to both $\mathbf{u}$ and $\mathbf{v}$.**
3. $\mathbf{u} = \langle 1, 2, -3 \rangle, \mathbf{v} = \langle -4, 1, 2 \rangle$
4. $\mathbf{u} = 3\mathbf{i} + 2\mathbf{j} - \mathbf{k}, \mathbf{v} = -\mathbf{i} - 3\mathbf{j} + \mathbf{k}$
5. $\mathbf{u} = \langle 0, 1, -2 \rangle, \mathbf{v} = \langle 3, 0, -4 \rangle$
6. $\mathbf{u} = 4\mathbf{i} + \mathbf{k}, \mathbf{v} = 2\mathbf{i} - \mathbf{j}$

7. Let $\mathbf{u} = \langle 2, -1, 3 \rangle, \mathbf{v} = \langle 0, 1, 7 \rangle,$ and $\mathbf{w} = \langle 1, 4, 5 \rangle$. Find:  
   (a) $\mathbf{u} \times (\mathbf{v} \times \mathbf{w})$  
   (b) $(\mathbf{u} \times \mathbf{v}) \times \mathbf{w}$  
   (c) $(\mathbf{u} \times \mathbf{v}) \times (\mathbf{v} \times \mathbf{w})$  
   (d) $(\mathbf{v} \times \mathbf{w}) \times (\mathbf{u} \times \mathbf{v})$

8. Use a CAS or a calculating utility that can compute determinants or cross products to solve Exercise 7.

9. Find the direction cosines of $\mathbf{u} \times \mathbf{v}$ for the vectors $\mathbf{u}$ and $\mathbf{v}$ in Figure Ex-9 (where $\mathbf{u} = \langle 1, 1, 1 \rangle, \mathbf{v} = \langle 1, 1, 0 \rangle$).

10. Find two unit vectors that are orthogonal to both $\mathbf{u} = -7\mathbf{i} + 3\mathbf{j} + \mathbf{k}$ and $\mathbf{v} = 2\mathbf{i} + 4\mathbf{k}$.

11. Find two unit vectors that are normal to the plane determined by the points $A(0, -2, 1), B(1, -1, -2),$ and $C(-1, 1, 0)$.

12. Find two unit vectors that are parallel to the $yz$-plane and are orthogonal to the vector $3\mathbf{i} - \mathbf{j} + 2\mathbf{k}$.

**13–16 True–False Determine whether the statement is true or false. Explain your answer.**
13. If the cross product of two nonzero vectors is the zero vector, then each of the two vectors is a scalar multiple of the other.
14. For any three vectors $\mathbf{a}, \mathbf{b},$ and $\mathbf{c}$, we have $\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a} \times \mathbf{b}) \times \mathbf{c}$.
15. If $\mathbf{v} \times \mathbf{u} = \mathbf{v} \times \mathbf{w}$ and if $\mathbf{v} \neq \mathbf{0}$, then $\mathbf{u} = \mathbf{w}$.
16. If $\mathbf{u} = a\mathbf{v} + b\mathbf{w}$, then $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = 0$.

**17–18 Find the area of the parallelogram that has $\mathbf{u}$ and $\mathbf{v}$ as adjacent sides.**
17. $\mathbf{u} = \mathbf{i} - \mathbf{j} + 2\mathbf{k}, \mathbf{v} = 3\mathbf{j} + \mathbf{k}$
18. $\mathbf{u} = 2\mathbf{i} + 3\mathbf{j}, \mathbf{v} = -\mathbf{i} + 2\mathbf{j} - 2\mathbf{k}$

**19–20 Find the area of the triangle with vertices $P, Q,$ and $R$.**
19. $P(1, 5, -2), Q(0, 0, 0), R(3, 5, 1)$
20. $P(2, 0, -3), Q(1, 4, 5), R(7, 2, 9)$

**21–24 Find $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$.**
21. $\mathbf{u} = 2\mathbf{i} - 3\mathbf{j} + \mathbf{k}, \mathbf{v} = 4\mathbf{i} + \mathbf{j} - 3\mathbf{k}, \mathbf{w} = \mathbf{j} + 5\mathbf{k}$
22. $\mathbf{u} = \langle 1, -2, 2 \rangle, \mathbf{v} = \langle 0, 3, 2 \rangle, \mathbf{w} = \langle -4, 1, -3 \rangle$
23. $\mathbf{u} = \langle 2, 1, 0 \rangle, \mathbf{v} = \langle 1, -3, 1 \rangle, \mathbf{w} = \langle 4, 0, 1 \rangle$
24. $\mathbf{u} = \mathbf{i}, \mathbf{v} = \mathbf{i} + \mathbf{j}, \mathbf{w} = \mathbf{i} + \mathbf{j} + \mathbf{k}$

**25–26 Use a scalar triple product to find the volume of the parallelepiped that has $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ as adjacent edges.**
25. $\mathbf{u} = \langle 2, -6, 2 \rangle, \mathbf{v} = \langle 0, 4, -2 \rangle, \mathbf{w} = \langle 2, 2, -4 \rangle$
26. $\mathbf{u} = 3\mathbf{i} + \mathbf{j} + 2\mathbf{k}, \mathbf{v} = 4\mathbf{i} + 5\mathbf{j} + \mathbf{k}, \mathbf{w} = \mathbf{i} + 2\mathbf{j} + 4\mathbf{k}$

**27. In each part, use a scalar triple product to determine whether the vectors lie in the same plane.**  
(a) $\mathbf{u} = \langle 1, -2, 1 \rangle, \mathbf{v} = \langle 3, 0, -2 \rangle, \mathbf{w} = \langle 5, -4, 0 \rangle$  
(b) $\mathbf{u} = 5\mathbf{i} - 2\mathbf{j} + \mathbf{k}, \mathbf{v} = 4\mathbf{i} - \mathbf{j} + \mathbf{k}, \mathbf{w} = \mathbf{i} - \mathbf{j}$  
(c) $\mathbf{u} = \langle 4, -8, 1 \rangle, \mathbf{v} = \langle 2, 1, -2 \rangle, \mathbf{w} = \langle 3, -4, 12 \rangle$

**28. Suppose that $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = 3$. Find:**  
(a) $\mathbf{u} \cdot (\mathbf{w} \times \mathbf{v})$  
(b) $(\mathbf{v} \times \mathbf{w}) \cdot \mathbf{u}$  
(c) $\mathbf{w} \cdot (\mathbf{u} \times \mathbf{v})$  
(d) $\mathbf{v} \cdot (\mathbf{u} \times \mathbf{w})$  
(e) $(\mathbf{u} \times \mathbf{w}) \cdot \mathbf{v}$  
(f) $\mathbf{v} \cdot (\mathbf{w} \times \mathbf{w})$

**29. Consider the parallelepiped with adjacent edges $\mathbf{u} = 3\mathbf{i} + 2\mathbf{j} + \mathbf{k}, \mathbf{v} = \mathbf{i} + \mathbf{j} + 2\mathbf{k}, \mathbf{w} = \mathbf{i} + 3\mathbf{j} + 3\mathbf{k}$.**  
(a) Find the volume.  
(b) Find the area of the face determined by $\mathbf{u}$ and $\mathbf{w}$.  
(c) Find the angle between $\mathbf{u}$ and the plane containing the face determined by $\mathbf{v}$ and $\mathbf{w}$.

30. Show that in 3-space the distance $d$ from a point $P$ to the line $L$ through points $A$ and $B$ can be expressed as
    $$d = \frac{\|\vec{AP} \times \vec{AB}\|}{\|\vec{AB}\|}$$

**31. Use the result in Exercise 30 to find the distance between the point $P$ and the line through the points $A$ and $B$.**  
(a) $P(-3, 1, 2), A(1, 1, 0), B(-2, 3, -4)$  
(b) $P(4, 3), A(2, 1), B(0, 2)$

32. It is a theorem of solid geometry that the volume of a tetrahedron is $\frac{1}{3}(\text{area of base})\cdot(\text{height})$. Use this result to prove that the volume of a tetrahedron with adjacent edges given by the vectors $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ is $\frac{1}{6}|\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})|$.

33. Use the result of Exercise 32 to find the volume of the tetrahedron with vertices $P(-1, 2, 0), Q(2, 1, -3), R(1, 0, 1), S(3, -2, 3)$.

34. Let $\theta$ be the angle between the vectors $\mathbf{u} = 2\mathbf{i} + 3\mathbf{j} - 6\mathbf{k}$ and $\mathbf{v} = 2\mathbf{i} + 3\mathbf{j} + 6\mathbf{k}$.  
    (a) Use the dot product to find $\cos\theta$.  
    (b) Use the cross product to find $\sin\theta$.  
    (c) Confirm that $\sin^2\theta + \cos^2\theta = 1$.

#### FOCUS ON CONCEPTS

35. Let $A, B, C,$ and $D$ be four distinct points in 3-space. If $\vec{AB} \times \vec{CD} \neq \mathbf{0}$ and $\vec{AC} \cdot (\vec{AB} \times \vec{CD}) = 0$, explain why the line through $A$ and $B$ must intersect the line through $C$ and $D$.
36. Let $A, B,$ and $C$ be three distinct noncollinear points in 3-space. Describe the set of all points $P$ that satisfy the vector equation $\vec{AP} \cdot (\vec{AB} \times \vec{AC}) = 0$.
37. What can you say about the angle between nonzero vectors $\mathbf{u}$ and $\mathbf{v}$ if $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u} \times \mathbf{v}\|$?
38. Show that if $\mathbf{u}$ and $\mathbf{v}$ are vectors in 3-space, then
    $$\|\mathbf{u} \times \mathbf{v}\|^2 = \|\mathbf{u}\|^2\|\mathbf{v}\|^2 - (\mathbf{u} \cdot \mathbf{v})^2$$
    *[Note: This result is sometimes called Lagrange's identity.]*
39. The accompanying figure shows a force $\mathbf{F}$ of $10\text{ lb}$ applied in the positive $y$-direction to the point $Q(1, 1, 1)$ of a cube whose sides have a length of $1\text{ ft}$. In each part, find the scalar moment of $\mathbf{F}$ about the point $P$, and describe the direction of rotation, if any, if the cube is free to rotate about $P$.  
    (a) $P$ is the point $(0, 0, 0)$.  
    (b) $P$ is the point $(1, 0, 0)$.  
    (c) $P$ is the point $(1, 0, 1)$.
40. The accompanying figure shows a force $\mathbf{F}$ of $1000\text{ N}$ applied to the corner of a box.  
    (a) Find the scalar moment of $\mathbf{F}$ about the point $P$.  
    (b) Find the direction angles of the vector moment of $\mathbf{F}$ about the point $P$ to the nearest degree.
41. As shown in Figure Ex-41, a force of $200\text{ N}$ is applied at an angle of $18^\circ$ to a point near the end of a monkey wrench ($200\text{ mm}$ length, $30\text{ mm}$ offset). Find the scalar moment of the force about the center of the bolt. *[Note: Treat this as a problem in two dimensions.]*
42. Prove parts (b) and (c) of Theorem 11.4.3.
43. Prove parts (d) and (e) of Theorem 11.4.3.
44. Prove part (b) of Theorem 11.4.1 for $3 \times 3$ determinants. *[Note: Just give the proof for the first two rows.]* Then use (b) to prove (a).

#### FOCUS ON CONCEPTS

45. Expressions of the form $\mathbf{u} \times (\mathbf{v} \times \mathbf{w})$ and $(\mathbf{u} \times \mathbf{v}) \times \mathbf{w}$ are called **vector triple products**. It can be proved with some effort that
    $$\mathbf{u} \times (\mathbf{v} \times \mathbf{w}) = (\mathbf{u} \cdot \mathbf{w})\mathbf{v} - (\mathbf{u} \cdot \mathbf{v})\mathbf{w}$$
    $$(\mathbf{u} \times \mathbf{v}) \times \mathbf{w} = (\mathbf{w} \cdot \mathbf{u})\mathbf{v} - (\mathbf{w} \cdot \mathbf{v})\mathbf{u}$$
    These expressions can be summarized with the following mnemonic rule:
    $$\text{vector triple product} = (\text{outer} \cdot \text{remote})\text{adjacent} - (\text{outer} \cdot \text{adjacent})\text{remote}$$
    See if you can figure out what the expressions "outer," "remote," and "adjacent" mean in this rule, and then use the rule to find the two vector triple products of the vectors $\mathbf{u} = \mathbf{i} + 3\mathbf{j} - \mathbf{k}, \mathbf{v} = \mathbf{i} + \mathbf{j} + 2\mathbf{k}, \mathbf{w} = 3\mathbf{i} - \mathbf{j} + 2\mathbf{k}$.
46. (a) Use the result in Exercise 45 to show that $\mathbf{u} \times (\mathbf{v} \times \mathbf{w})$ lies in the same plane as $\mathbf{v}$ and $\mathbf{w}$, and $(\mathbf{u} \times \mathbf{v}) \times \mathbf{w}$ lies in the same plane as $\mathbf{u}$ and $\mathbf{v}$.  
    (b) Use a geometrical argument to justify the results in part (a).
47. In each part, use the result in Exercise 45 to prove the vector identity:  
    (a) $(\mathbf{a} \times \mathbf{b}) \times (\mathbf{c} \times \mathbf{d}) = (\mathbf{a} \times \mathbf{b} \cdot \mathbf{d})\mathbf{c} - (\mathbf{a} \times \mathbf{b} \cdot \mathbf{c})\mathbf{d}$  
    (b) $(\mathbf{a} \times \mathbf{b}) \times \mathbf{c} + (\mathbf{b} \times \mathbf{c}) \times \mathbf{a} + (\mathbf{c} \times \mathbf{a}) \times \mathbf{b} = \mathbf{0}$
48. Prove: If $\mathbf{a}, \mathbf{b}, \mathbf{c},$ and $\mathbf{d}$ lie in the same plane when positioned with a common initial point, then $(\mathbf{a} \times \mathbf{b}) \times (\mathbf{c} \times \mathbf{d}) = \mathbf{0}$.
49. Use a CAS to approximate the minimum area of a triangle if two of its vertices are $(2, -1, 0)$ and $(3, 2, 2)$ and its third vertex is on the curve $y = \ln x$ in the $xy$-plane.
50. If a force $\mathbf{F}$ is applied to an object at a point $Q$, then the line through $Q$ parallel to $\mathbf{F}$ is called the line of action of the force. We defined the vector moment of $\mathbf{F}$ about a point $P$ to be $\vec{PQ} \times \mathbf{F}$. Show that if $Q'$ is any point on the line of action of $\mathbf{F}$, then $\vec{PQ'} \times \mathbf{F} = \vec{PQ} \times \mathbf{F}$; that is, it is not essential to use the point of application to compute the vector moment—any point on the line of action will do. *[Hint: Write $\vec{PQ'} = \vec{PQ} + \vec{QQ'}$ and use properties of the cross product.]*
51. **Writing.** Discuss some of the similarities and differences between the multiplication of real numbers and the cross product of vectors.
52. **Writing.** In your own words, describe what it means to say that the cross-product operation is "coordinate independent," and state why this fact is significant.

#### QUICK CHECK ANSWERS 11.4
1. (a) 7 (b) 0  
2. $8\mathbf{i} - 4\mathbf{j} - 6\mathbf{k}$  
3. (a) $\langle 0, 0, 0 \rangle$ (b) $\langle -2, -7, -3 \rangle$ (c) $\langle -3, 11, 3 \rangle$ (d) $\langle -10, 8, 0 \rangle$  
4. (a) -58 (b) 58

---

## 11.5 PARAMETRIC EQUATIONS OF LINES

In this section we will discuss parametric equations of lines in 2-space and 3-space. In 3-space, parametric equations of lines are especially important because they generally provide the most convenient form for representing lines algebraically.

### LINES DETERMINED BY A POINT AND A VECTOR

A line in 2-space or 3-space can be determined uniquely by specifying a point on the line and a nonzero vector parallel to the line (Figure 11.5.1). For example, consider a line $L$ in 3-space that passes through the point $P_0(x_0, y_0, z_0)$ and is parallel to the nonzero vector $\mathbf{v} = \langle a, b, c \rangle$. Then $L$ consists precisely of those points $P(x, y, z)$ for which the vector $\vec{P_0P}$ is parallel to $\mathbf{v}$ (Figure 11.5.2). In other words, the point $P(x, y, z)$ is on $L$ if and only if $\vec{P_0P}$ is a scalar multiple of $\mathbf{v}$, say
$$\vec{P_0P} = t\mathbf{v}$$
This equation can be written as
$$\langle x - x_0, y - y_0, z - z_0 \rangle = \langle ta, tb, tc \rangle$$
which implies that
$$x - x_0 = ta, \quad y - y_0 = tb, \quad z - z_0 = tc$$
Thus, $L$ can be described by the parametric equations
$$x = x_0 + at, \quad y = y_0 + bt, \quad z = z_0 + ct$$
A similar description applies to lines in 2-space. We summarize these descriptions in the following theorem.

> **11.5.1 THEOREM**  
> (a) The line in 2-space that passes through the point $P_0(x_0, y_0)$ and is parallel to the nonzero vector $\mathbf{v} = \langle a, b \rangle = a\mathbf{i} + b\mathbf{j}$ has parametric equations
> $$x = x_0 + at, \quad y = y_0 + bt \tag{1}$$
> (b) The line in 3-space that passes through the point $P_0(x_0, y_0, z_0)$ and is parallel to the nonzero vector $\mathbf{v} = \langle a, b, c \rangle = a\mathbf{i} + b\mathbf{j} + c\mathbf{k}$ has parametric equations
> $$x = x_0 + at, \quad y = y_0 + bt, \quad z = z_0 + ct \tag{2}$$

> **REMARK**  
> Although it is not stated explicitly, it is understood in Equations (1) and (2) that $-\infty < t < +\infty$, which reflects the fact that lines extend indefinitely.

#### Example 1
Find parametric equations of the line:  
(a) passing through $(4, 2)$ and parallel to $\mathbf{v} = \langle -1, 5 \rangle$;  
(b) passing through $(1, 2, -3)$ and parallel to $\mathbf{v} = 4\mathbf{i} + 5\mathbf{j} - 7\mathbf{k}$;  
(c) passing through the origin in 3-space and parallel to $\mathbf{v} = \langle 1, 1, 1 \rangle$.

**Solution (a).** From (1) with $x_0 = 4, y_0 = 2, a = -1,$ and $b = 5$ we obtain
$$x = 4 - t, \quad y = 2 + 5t$$

**Solution (b).** From (2) we obtain
$$x = 1 + 4t, \quad y = 2 + 5t, \quad z = -3 - 7t$$

**Solution (c).** From (2) with $x_0 = 0, y_0 = 0, z_0 = 0, a = 1, b = 1,$ and $c = 1$ we obtain
$$x = t, \quad y = t, \quad z = t$$

#### Example 2
(a) Find parametric equations of the line $L$ passing through the points $P_1(2, 4, -1)$ and $P_2(5, 0, 7)$.  
(b) Where does the line intersect the $xy$-plane?

**Solution (a).** The vector $\vec{P_1P_2} = \langle 3, -4, 8 \rangle$ is parallel to $L$ and the point $P_1(2, 4, -1)$ lies on $L$, so it follows from (2) that $L$ has parametric equations
$$x = 2 + 3t, \quad y = 4 - 4t, \quad z = -1 + 8t \tag{3}$$
Had we used $P_2$ as the point on $L$ rather than $P_1$, we would have obtained the equations
$$x = 5 + 3t, \quad y = -4t, \quad z = 7 + 8t$$
Although these equations look different from those obtained using $P_1$, the two sets of equations are actually equivalent in that both generate $L$ as $t$ varies from $-\infty$ to $+\infty$.

**Solution (b).** It follows from (3) in part (a) that the line intersects the $xy$-plane at the point where $z = -1 + 8t = 0$, that is, when $t = \frac{1}{8}$. Substituting this value of $t$ in (3) yields the point of intersection
$$(x, y, z) = \left(\frac{19}{8}, \frac{7}{2}, 0\right)$$

#### Example 3
Let $L_1$ and $L_2$ be the lines
$$L_1 : x = 1 + 4t, \quad y = 5 - 4t, \quad z = -1 + 5t$$
$$L_2 : x = 2 + 8t, \quad y = 4 - 3t, \quad z = 5 + t$$
(a) Are the lines parallel?  
(b) Do the lines intersect?

**Solution (a).** The line $L_1$ is parallel to the vector $4\mathbf{i} - 4\mathbf{j} + 5\mathbf{k}$, and the line $L_2$ is parallel to the vector $8\mathbf{i} - 3\mathbf{j} + \mathbf{k}$. These vectors are not parallel since neither is a scalar multiple of the other. Thus, the lines are not parallel.

**Solution (b).** For $L_1$ and $L_2$ to intersect at some point $(x_0, y_0, z_0)$ these coordinates would have to satisfy the equations of both lines. In other words, there would have to exist values $t_1$ and $t_2$ for the parameters such that
$$1 + 4t_1 = 2 + 8t_2$$
$$5 - 4t_1 = 4 - 3t_2$$
$$-1 + 5t_1 = 5 + t_2 \tag{4}$$
Adding the first two equations eliminates $t_1$:
$$6 = 6 + 5t_2 \implies t_2 = 0$$
Substituting $t_2 = 0$ into the first equation yields $t_1 = \frac{1}{4}$. However, the values $t_1 = \frac{1}{4}$ and $t_2 = 0$ do not satisfy the third equation in (4) (since $-1 + 5(1/4) = 1/4 \neq 5$), so the lines do not intersect.

Two lines in 3-space that are not parallel and do not intersect are called **skew lines**. Any two skew lines lie in parallel planes (Figure 11.5.3).

---

### LINE SEGMENTS

Parametric equations of a line segment can be obtained by finding parametric equations for the entire line, and then restricting the parameter appropriately so that only the desired segment is generated.

#### Example 4
Find parametric equations describing the line segment joining the points $P_1(2, 4, -1)$ and $P_2(5, 0, 7)$.

**Solution.** The line through $P_1$ and $P_2$ has parametric equations $x = 2 + 3t, y = 4 - 4t, z = -1 + 8t$. With these equations, the point $P_1$ corresponds to $t = 0$ and $P_2$ to $t = 1$. Thus, the line segment joining $P_1$ and $P_2$ is given by
$$x = 2 + 3t, \quad y = 4 - 4t, \quad z = -1 + 8t \quad (0 \le t \le 1)$$

---

### VECTOR EQUATIONS OF LINES

Vector notation can be used to express the parametric equations of a line compactly:
$$\langle x, y \rangle = \langle x_0, y_0 \rangle + t\langle a, b \rangle \tag{5}$$
$$\langle x, y, z \rangle = \langle x_0, y_0, z_0 \rangle + t\langle a, b, c \rangle \tag{6}$$
Setting $\mathbf{r} = \langle x, y \rangle, \mathbf{r}_0 = \langle x_0, y_0 \rangle, \mathbf{v} = \langle a, b \rangle$ in 2-space and $\mathbf{r} = \langle x, y, z \rangle, \mathbf{r}_0 = \langle x_0, y_0, z_0 \rangle, \mathbf{v} = \langle a, b, c \rangle$ in 3-space yields
$$\mathbf{r} = \mathbf{r}_0 + t\mathbf{v} \tag{9}$$

#### Example 5
The equation $\langle x, y, z \rangle = \langle -1, 0, 2 \rangle + t\langle 1, 5, -4 \rangle$ represents the line in 3-space that passes through $(-1, 0, 2)$ and is parallel to $\langle 1, 5, -4 \rangle$.

#### Example 6
Find an equation of the line in 3-space that passes through the points $P_1(2, 4, -1)$ and $P_2(5, 0, 7)$.

**Solution.** The vector $\vec{P_1P_2} = \langle 3, -4, 8 \rangle$ is parallel to the line, so a vector equation is
$$\langle x, y, z \rangle = \langle 2, 4, -1 \rangle + t\langle 3, -4, 8 \rangle$$

---

### QUICK CHECK EXERCISES 11.5
*(See page 812 for answers.)*

1. Let $L$ be the line through $(2, 5)$ and parallel to $\mathbf{v} = \langle 3, -1 \rangle$.  
   (a) Parametric equations of $L$ are $x = \underline{\quad}, y = \underline{\quad}$.  
   (b) A vector equation of $L$ is $\langle x, y \rangle = \underline{\quad}$.
2. Parametric equations for the line through $(5, 3, 7)$ and parallel to the line $x = 3 - t, y = 2, z = 8 + 4t$ are $x = \underline{\quad}, y = \underline{\quad}, z = \underline{\quad}$.
3. Parametric equations for the line segment joining the points $(3, 0, 11)$ and $(2, 6, 7)$ are $x = \underline{\quad}, y = \underline{\quad}, z = \underline{\quad} \; (\underline{\quad})$.
4. The line through the points $(-3, 8, -4)$ and $(1, 0, 8)$ intersects the $yz$-plane at $\underline{\quad}$.

---

### EXERCISE SET 11.5

**1. (a) Find parametric equations for the lines through the corner of the unit square shown in part (a) of Figure Ex-1.**  
**(b) Find parametric equations for the lines through the corner of the unit cube shown in part (b) of Figure Ex-1.**

**2. (a) Find parametric equations for the line segments in the unit square in part (a) of Figure Ex-2.**  
**(b) Find parametric equations for the line segments in the unit cube shown in part (b) of Figure Ex-2.**

**3–4 Find parametric equations for the line through $P_1$ and $P_2$ and also for the line segment joining those points.**
3. (a) $P_1(3, -2), P_2(5, 1)$  
   (b) $P_1(5, -2, 1), P_2(2, 4, 2)$
4. (a) $P_1(0, 1), P_2(-3, -4)$  
   (b) $P_1(-1, 3, 5), P_2(-1, 3, 2)$

**5–6 Find parametric equations for the line whose vector equation is given.**
5. (a) $\langle x, y \rangle = \langle 2, -3 \rangle + t\langle 1, -4 \rangle$  
   (b) $x\mathbf{i} + y\mathbf{j} + z\mathbf{k} = \mathbf{k} + t(\mathbf{i} - \mathbf{j} + \mathbf{k})$
6. (a) $x\mathbf{i} + y\mathbf{j} = (3\mathbf{i} - 4\mathbf{j}) + t(2\mathbf{i} + \mathbf{j})$  
   (b) $\langle x, y, z \rangle = \langle -1, 0, 2 \rangle + t\langle -1, 3, 0 \rangle$

**7–8 Find a point $P$ on the line and a vector $\mathbf{v}$ parallel to the line by inspection.**
7. (a) $x\mathbf{i} + y\mathbf{j} = (2\mathbf{i} - \mathbf{j}) + t(4\mathbf{i} - \mathbf{j})$  
   (b) $\langle x, y, z \rangle = \langle -1, 2, 4 \rangle + t\langle 5, 7, -8 \rangle$
8. (a) $\langle x, y \rangle = \langle -1, 5 \rangle + t\langle 2, 3 \rangle$  
   (b) $x\mathbf{i} + y\mathbf{j} + z\mathbf{k} = (\mathbf{i} + \mathbf{j} - 2\mathbf{k}) + t\mathbf{j}$

**9–10 Express the given parametric equations of a line using bracket notation and also using $\mathbf{i}, \mathbf{j}, \mathbf{k}$ notation.**
9. (a) $x = -3 + t, y = 4 + 5t$  
   (b) $x = 2 - t, y = -3 + 5t, z = t$
10. (a) $x = t, y = -2 + t$  
    (b) $x = 1 + t, y = -7 + 3t, z = 4 - 5t$

**11–14 True–False Determine whether the statement is true or false. Explain your answer. In these exercises $L_0$ and $L_1$ are lines in 3-space whose parametric equations are**
$$L_0: x = x_0 + a_0 t, \; y = y_0 + b_0 t, \; z = z_0 + c_0 t$$
$$L_1: x = x_1 + a_1 t, \; y = y_1 + b_1 t, \; z = z_1 + c_1 t$$
11. By definition, if $L_1$ and $L_2$ do not intersect, then $L_1$ and $L_2$ are parallel.
12. If $L_1$ and $L_2$ are parallel, then $\mathbf{v}_0 = \langle a_0, b_0, c_0 \rangle$ is a scalar multiple of $\mathbf{v}_1 = \langle a_1, b_1, c_1 \rangle$.
13. If $L_1$ and $L_2$ intersect at a point $(x, y, z)$, then there exists a single value of $t$ such that the equations of $L_0$ and $L_1$ are satisfied.
14. If $L_0$ passes through the origin, then the vectors $\langle a_0, b_0, c_0 \rangle$ and $\langle x_0, y_0, z_0 \rangle$ are parallel.

**15–22 Find parametric equations of the line that satisfies the stated conditions.**
15. The line through $(-5, 2)$ that is parallel to $2\mathbf{i} - 3\mathbf{j}$.
16. The line through $(0, 3)$ that is parallel to the line $x = -5 + t, y = 1 - 2t$.
17. The line that is tangent to the circle $x^2 + y^2 = 25$ at the point $(3, -4)$.
18. The line that is tangent to the parabola $y = x^2$ at the point $(-2, 4)$.
19. The line through $(-1, 2, 4)$ that is parallel to $3\mathbf{i} - 4\mathbf{j} + \mathbf{k}$.
20. The line through $(2, -1, 5)$ that is parallel to $\langle -1, 2, 7 \rangle$.
21. The line through $(-2, 0, 5)$ that is parallel to the line given by $x = 1 + 2t, y = 4 - t, z = 6 + 2t$.
22. The line through the origin that is parallel to the line given by $x = t, y = -1 + t, z = 2$.

23. Where does the line $x = 1 + 3t, y = 2 - t$ intersect:  
    (a) the $x$-axis  
    (b) the $y$-axis  
    (c) the parabola $y = x^2$?
24. Where does the line $\langle x, y \rangle = \langle 4t, 3t \rangle$ intersect the circle $x^2 + y^2 = 25$?

**25–26 Find the intersections of the lines with the $xy$-plane, the $xz$-plane, and the $yz$-plane.**
25. $x = -2, y = 4 + 2t, z = -3 + t$
26. $x = -1 + 2t, y = 3 + t, z = 4 - t$

27. Where does the line $x = 1 + t, y = 3 - t, z = 2t$ intersect the cylinder $x^2 + y^2 = 16$?
28. Where does the line $x = 2 - t, y = 3t, z = -1 + 2t$ intersect the plane $2y + 3z = 6$?

**29–30 Show that the lines $L_1$ and $L_2$ intersect, and find their point of intersection.**
29. $L_1 : x = 2 + t, y = 2 + 3t, z = 3 + t$  
    $L_2 : x = 2 + t, y = 3 + 4t, z = 4 + 2t$
30. $L_1 : x + 1 = 4t, y - 3 = t, z - 1 = 0$  
    $L_2 : x + 13 = 12t, y - 1 = 6t, z - 2 = 3t$

**31–32 Show that the lines $L_1$ and $L_2$ are skew.**
31. $L_1 : x = 1 + 7t, y = 3 + t, z = 5 - 3t$  
    $L_2 : x = 4 - t, y = 6, z = 7 + 2t$
32. $L_1 : x = 2 + 8t, y = 6 - 8t, z = 10t$  
    $L_2 : x = 3 + 8t, y = 5 - 3t, z = 6 + t$

**33–34 Determine whether the lines $L_1$ and $L_2$ are parallel.**
33. $L_1 : x = 3 - 2t, y = 4 + t, z = 6 - t$  
    $L_2 : x = 5 - 4t, y = -2 + 2t, z = 7 - 2t$
34. $L_1 : x = 5 + 3t, y = 4 - 2t, z = -2 + 3t$  
    $L_2 : x = -1 + 9t, y = 5 - 6t, z = 3 + 8t$

**35–36 Determine whether the points $P_1, P_2,$ and $P_3$ lie on the same line.**
35. $P_1(6, 9, 7), P_2(9, 2, 0), P_3(0, -5, -3)$
36. $P_1(1, 0, 1), P_2(3, -4, -3), P_3(4, -6, -5)$

**37–38 Show that the lines $L_1$ and $L_2$ are the same.**
37. $L_1 : x = 3 - t, y = 1 + 2t$  
    $L_2 : x = -1 + 3t, y = 9 - 6t$
38. $L_1 : x = 1 + 3t, y = -2 + t, z = 2t$  
    $L_2 : x = 4 - 6t, y = -1 - 2t, z = 2 - 4t$

#### FOCUS ON CONCEPTS

39. Sketch the vectors $\mathbf{r}_0 = \langle -1, 2 \rangle$ and $\mathbf{v} = \langle 1, 1 \rangle$, and then sketch the six vectors $\mathbf{r}_0 \pm \mathbf{v}, \mathbf{r}_0 \pm 2\mathbf{v}, \mathbf{r}_0 \pm 3\mathbf{v}$. Draw the line $L: x = -1 + t, y = 2 + t$, and describe the relationship between $L$ and the vectors you sketched. What is the vector equation of $L$?
40. Sketch the vectors $\mathbf{r}_0 = \langle 0, 2, 1 \rangle$ and $\mathbf{v} = \langle 1, 0, 1 \rangle$, and then sketch the vectors $\mathbf{r}_0 + \mathbf{v}, \mathbf{r}_0 + 2\mathbf{v},$ and $\mathbf{r}_0 + 3\mathbf{v}$. Draw the line $L: x = t, y = 2, z = 1 + t$, and describe the relationship between $L$ and the vectors you sketched. What is the vector equation of $L$?
41. Sketch the vectors $\mathbf{r}_0 = \langle -2, 0 \rangle$ and $\mathbf{r}_1 = \langle 1, 3 \rangle$, and then sketch the vectors $\frac{1}{3}\mathbf{r}_0 + \frac{2}{3}\mathbf{r}_1, \frac{1}{2}\mathbf{r}_0 + \frac{1}{2}\mathbf{r}_1, \frac{2}{3}\mathbf{r}_0 + \frac{1}{3}\mathbf{r}_1$. Draw the line segment $(1 - t)\mathbf{r}_0 + t\mathbf{r}_1 \; (0 \le t \le 1)$. If $n$ is a positive integer, what is the position of the point on this line segment corresponding to $t = 1/n$, relative to the points $(-2, 0)$ and $(1, 3)$?
42. Sketch the vectors $\mathbf{r}_0 = \langle 2, 0, 4 \rangle$ and $\mathbf{r}_1 = \langle 0, 4, 0 \rangle$, and then sketch the vectors $\frac{1}{4}\mathbf{r}_0 + \frac{3}{4}\mathbf{r}_1, \frac{1}{2}\mathbf{r}_0 + \frac{1}{2}\mathbf{r}_1, \frac{3}{4}\mathbf{r}_0 + \frac{1}{4}\mathbf{r}_1$. Draw the line segment $(1 - t)\mathbf{r}_0 + t\mathbf{r}_1 \; (0 \le t \le 1)$. If $n$ is a positive integer, what is the position of the point on this line segment corresponding to $t = 1/n$, relative to the points $(2, 0, 4)$ and $(0, 4, 0)$?

**43–44 Describe the line segment represented by the vector equation.**
43. $\langle x, y \rangle = \langle 1, 0 \rangle + t\langle -2, 3 \rangle \quad (0 \le t \le 2)$
44. $\langle x, y, z \rangle = \langle -2, 1, 4 \rangle + t\langle 3, 0, -1 \rangle \quad (0 \le t \le 3)$

45. Find the point on the line segment joining $P_1(3, 6)$ and $P_2(8, -4)$ that is $\frac{2}{5}$ of the way from $P_1$ to $P_2$.
46. Find the point on the line segment joining $P_1(1, 4, -3)$ and $P_2(1, 5, -1)$ that is $\frac{2}{3}$ of the way from $P_1$ to $P_2$.

**47–48 Use the method in Exercise 32 of Section 11.3 to find the distance from the point $P$ to the line $L$, and then check your answer using the method in Exercise 30 of Section 11.4.**
47. $P(-2, 1, 1); \; L: x = 3 - t, y = t, z = 1 + 2t$
48. $P(1, 4, -3); \; L: x = 2 + t, y = -1 - t, z = 3t$

**49–50 Show that the lines $L_1$ and $L_2$ are parallel, and find the distance between them.**
49. $L_1 : x = 2 - t, y = 2t, z = 1 + t$  
    $L_2 : x = 1 + 2t, y = 3 - 4t, z = 5 - 2t$
50. $L_1 : x = 2t, y = 3 + 4t, z = 2 - 6t$  
    $L_2 : x = 1 + 3t, y = 6t, z = -9t$

51. (a) Find parametric equations for the line through the points $(x_0, y_0, z_0)$ and $(x_1, y_1, z_1)$.  
    (b) Find parametric equations for the line through the point $(x_1, y_1, z_1)$ and parallel to the line $x = x_0 + at, y = y_0 + bt, z = z_0 + ct$.

52. Let $L$ be the line that passes through the point $(x_0, y_0, z_0)$ and is parallel to the vector $\mathbf{v} = \langle a, b, c \rangle$, where $a, b,$ and $c$ are nonzero. Show that a point $(x, y, z)$ lies on the line $L$ if and only if
    $$\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}$$
    These equations, which are called the **symmetric equations** of $L$, provide a nonparametric representation of $L$.

53. (a) Describe the line whose symmetric equations are $\frac{x - 1}{2} = \frac{y + 3}{4} = z - 5$.  
    (b) Find parametric equations for the line in part (a).

54. Consider the lines $L_1$ and $L_2$ whose symmetric equations are
    $$L_1 : \frac{x - 1}{2} = \frac{y + 3/2}{1} = \frac{z + 1}{2}$$
    $$L_2 : \frac{x - 4}{-1} = \frac{y - 3}{-2} = \frac{z + 4}{2}$$
    (a) Are $L_1$ and $L_2$ parallel? Perpendicular?  
    (b) Find parametric equations for $L_1$ and $L_2$.  
    (c) Do $L_1$ and $L_2$ intersect? If so, where?

55. Let $L_1$ and $L_2$ be the lines whose parametric equations are
    $$L_1 : x = 1 + 2t, y = 2 - t, z = 4 - 2t$$
    $$L_2 : x = 9 + t, y = 5 + 3t, z = -4 - t$$
    (a) Show that $L_1$ and $L_2$ intersect at the point $(7, -1, -2)$.  
    (b) Find, to the nearest degree, the acute angle between $L_1$ and $L_2$ at their intersection.  
    (c) Find parametric equations for the line that is perpendicular to $L_1$ and $L_2$ and passes through their point of intersection.

56. Let $L_1$ and $L_2$ be the lines whose parametric equations are
    $$L_1 : x = 4t, y = 1 - 2t, z = 2 + 2t$$
    $$L_2 : x = 1 + t, y = 1 - t, z = -1 + 4t$$
    (a) Show that $L_1$ and $L_2$ intersect at the point $(2, 0, 3)$.  
    (b) Find, to the nearest degree, the acute angle between $L_1$ and $L_2$ at their intersection.  
    (c) Find parametric equations for the line that is perpendicular to $L_1$ and $L_2$ and passes through their point of intersection.

**57–58 Find parametric equations of the line that contains the point $P$ and intersects the line $L$ at a right angle, and find the distance between $P$ and $L$.**
57. $P(0, 2, 1); \; L: x = 2t, y = 1 - t, z = 2 + t$
58. $P(3, 1, -2); \; L: x = -2 + 2t, y = 4 + 2t, z = 2 + t$

59. Two bugs are walking along lines in 3-space. At time $t$ bug 1 is at the point $(x, y, z)$ on the line
    $$x = 4 - t, \quad y = 1 + 2t, \quad z = 2 + t$$
    and at the same time $t$ bug 2 is at the point $(x, y, z)$ on the line
    $$x = t, \quad y = 1 + t, \quad z = 1 + 2t$$
    Assume that distance is in centimeters and that time is in minutes.  
    (a) Find the distance between the bugs at time $t = 0$.  
    (b) Use a graphing utility to graph the distance between the bugs as a function of time from $t = 0$ to $t = 5$.  
    (c) What does the graph tell you about the distance between the bugs?  
    (d) How close do the bugs get?

60. Suppose that the temperature $T$ at a point $(x, y, z)$ on the line $x = t, y = 1 + t, z = 3 - 2t$ is $T = 25x^2 yz$. Use a CAS or a calculating utility with a root-finding capability to approximate the maximum temperature on that portion of the line that extends from the $xz$-plane to the $xy$-plane.
61. **Writing.** Give some examples of geometric problems that can be solved using the parametric equations of a line, and describe their solution. For example, how would you find the points of intersection of a line and a sphere?
62. **Writing.** Discuss how the vector equation of a line can be used to model the motion of a point that is moving with constant velocity in 3-space.

#### QUICK CHECK ANSWERS 11.5
1. (a) $2 + 3t; 5 - t$ (b) $\langle 2, 5 \rangle + t\langle 3, -1 \rangle$  
2. $5 - t; 3; 7 + 4t$  
3. $3 - t; 6t; 11 - 4t; 0 \le t \le 1$  
4. $(0, 2, 5)$

---

## 11.6 PLANES IN 3-SPACE

In this section we will use vectors to derive equations of planes in 3-space, and then we will use these equations to solve various geometric problems.

### PLANES PARALLEL TO THE COORDINATE PLANES

The graph of the equation $x = a$ in an $xyz$-coordinate system consists of all points of the form $(a, y, z)$, where $y$ and $z$ are arbitrary. One such point is $(a, 0, 0)$, and all others are in the plane that passes through this point and is parallel to the $yz$-plane (Figure 11.6.1). Similarly, the graph of $y = b$ is the plane through $(0, b, 0)$ that is parallel to the $xz$-plane, and the graph of $z = c$ is the plane through $(0, 0, c)$ that is parallel to the $xy$-plane.

---

### PLANES DETERMINED BY A POINT AND A NORMAL VECTOR

A plane in 3-space can be determined uniquely by specifying a point in the plane and a vector perpendicular to the plane (Figure 11.6.2). A vector perpendicular to a plane is called a **normal** to the plane.

Suppose that we want to find an equation of the plane passing through $P_0(x_0, y_0, z_0)$ and perpendicular to the vector $\mathbf{n} = \langle a, b, c \rangle$. Define the vectors $\mathbf{r}_0$ and $\mathbf{r}$ as
$$\mathbf{r}_0 = \langle x_0, y_0, z_0 \rangle \quad \text{and} \quad \mathbf{r} = \langle x, y, z \rangle$$
It should be evident from Figure 11.6.3 that the plane consists precisely of those points $P(x, y, z)$ for which the vector $\mathbf{r} - \mathbf{r}_0$ is orthogonal to $\mathbf{n}$; or, expressed as an equation,
$$\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0 \tag{1}$$
If preferred, we can express this vector equation in terms of components as
$$\langle a, b, c \rangle \cdot \langle x - x_0, y - y_0, z - z_0 \rangle = 0 \tag{2}$$
from which we obtain
$$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0 \tag{3}$$
This is called the **point-normal form** of the equation of a plane.

#### Example 1
Find an equation of the plane passing through the point $(3, -1, 7)$ and perpendicular to the vector $\mathbf{n} = \langle 4, 2, -5 \rangle$.

**Solution.** From (3), a point-normal form of the equation is
$$4(x - 3) + 2(y + 1) - 5(z - 7) = 0 \tag{4}$$
Multiplying out the terms and simplifying yields
$$4x + 2y - 5z + 25 = 0$$

> **11.6.1 THEOREM**  
> If $a, b, c,$ and $d$ are constants, and $a, b,$ and $c$ are not all zero, then the graph of the equation
> $$ax + by + cz + d = 0 \tag{6}$$
> is a plane that has the vector $\mathbf{n} = \langle a, b, c \rangle$ as a normal.

**PROOF**  
Since $a, b,$ and $c$ are not all zero, there is at least one point $(x_0, y_0, z_0)$ whose coordinates satisfy Equation (6). For example, if $a \neq 0$, then such a point is $(-d/a, 0, 0)$, and similarly if $b \neq 0$ or $c \neq 0$. Thus, let $(x_0, y_0, z_0)$ be any point whose coordinates satisfy (6); that is,
$$ax_0 + by_0 + cz_0 + d = 0$$
Subtracting this equation from (6) yields
$$a(x - x_0) + b(y - y_0) + c(z - z_0) = 0$$
which is the point-normal form of a plane with normal $\mathbf{n} = \langle a, b, c \rangle$. $\blacksquare$

Equation (6) is called the **general form** of the equation of a plane.

#### Example 2
Determine whether the planes $3x - 4y + 5z = 0$ and $-6x + 8y - 10z - 4 = 0$ are parallel.

**Solution.** A normal to the first plane is $\mathbf{n}_1 = \langle 3, -4, 5 \rangle$ and a normal to the second plane is $\mathbf{n}_2 = \langle -6, 8, -10 \rangle$. Since $\mathbf{n}_2 = -2\mathbf{n}_1$, the normals are parallel, and hence so are the planes.

#### Example 3
Find an equation of the plane through the points $P_1(1, 2, -1), P_2(2, 3, 1),$ and $P_3(3, -1, 2)$.

**Solution.** The vectors $\vec{P_1P_2} = \langle 1, 1, 2 \rangle$ and $\vec{P_1P_3} = \langle 2, -3, 3 \rangle$ are parallel to the plane. Therefore,
$$\vec{P_1P_2} \times \vec{P_1P_3} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 2 \\ 2 & -3 & 3 \end{vmatrix} = 9\mathbf{i} + \mathbf{j} - 5\mathbf{k}$$
is normal to the plane. By using this normal and the point $P_1(1, 2, -1)$, we obtain
$$9(x - 1) + (y - 2) - 5(z + 1) = 0 \implies 9x + y - 5z - 16 = 0$$

#### Example 4
Determine whether the line $x = 3 + 8t, y = 4 + 5t, z = -3 - t$ is parallel to the plane $x - 3y + 5z = 12$.

**Solution.** The vector $\mathbf{v} = \langle 8, 5, -1 \rangle$ is parallel to the line and the vector $\mathbf{n} = \langle 1, -3, 5 \rangle$ is normal to the plane. For the line and plane to be parallel, $\mathbf{v}$ and $\mathbf{n}$ must be orthogonal. But $\mathbf{v} \cdot \mathbf{n} = (8)(1) + (5)(-3) + (-1)(5) = -12 \neq 0$. Thus, the line and plane are not parallel.

#### Example 5
Find the intersection of the line and plane in Example 4.

**Solution.** If $(x_0, y_0, z_0)$ is the point of intersection, then:
$$x_0 - 3y_0 + 5z_0 = 12 \tag{7}$$
$$x_0 = 3 + 8t_0, \quad y_0 = 4 + 5t_0, \quad z_0 = -3 - t_0 \tag{8}$$
Substituting (8) into (7):
$$(3 + 8t_0) - 3(4 + 5t_0) + 5(-3 - t_0) = 12 \implies t_0 = -3$$
Substituting $t_0 = -3$ into (8) yields $(x_0, y_0, z_0) = (-21, -11, 0)$.

---

### INTERSECTING PLANES

If $\mathbf{n}_1$ and $\mathbf{n}_2$ are normals to two intersecting planes, the acute angle $\theta$ between the planes satisfies:
$$\cos\theta = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{\|\mathbf{n}_1\|\|\mathbf{n}_2\|} \tag{9}$$

#### Example 6
Find the acute angle of intersection between the two planes $2x - 4y + 4z = 6$ and $6x + 2y - 3z = 4$.

**Solution.** $\mathbf{n}_1 = \langle 2, -4, 4 \rangle, \mathbf{n}_2 = \langle 6, 2, -3 \rangle$.
$$\cos\theta = \frac{|\mathbf{n}_1 \cdot \mathbf{n}_2|}{\|\mathbf{n}_1\|\|\mathbf{n}_2\|} = \frac{|-8|}{\sqrt{36}\sqrt{49}} = \frac{4}{21} \implies \theta = \cos^{-1}\left(\frac{4}{21}\right) \approx 79^\circ$$

#### Example 7
Find an equation for the line $L$ of intersection of the planes in Example 6.

**Solution.** $\mathbf{v} = \mathbf{n}_1 \times \mathbf{n}_2 = \langle 2, -4, 4 \rangle \times \langle 6, 2, -3 \rangle = \langle 4, 30, 28 \rangle$. Setting $z = 0$ gives the system $2x - 4y = 6, 6x + 2y = 4 \implies x = 1, y = -1$. Thus, $P(1, -1, 0)$ is on $L$, and a vector equation for $L$ is
$$\langle x, y, z \rangle = \langle 1, -1, 0 \rangle + t\langle 4, 30, 28 \rangle$$

---

### DISTANCE PROBLEMS INVOLVING PLANES

> **11.6.2 THEOREM**  
> The distance $D$ between a point $P_0(x_0, y_0, z_0)$ and the plane $ax + by + cz + d = 0$ is
> $$D = \frac{|ax_0 + by_0 + cz_0 + d|}{\sqrt{a^2 + b^2 + c^2}} \tag{10}$$

**PROOF**  
Let $Q(x_1, y_1, z_1)$ be any point in the plane, and position the normal $\mathbf{n} = \langle a, b, c \rangle$ at $Q$. The distance $D$ is the length of the orthogonal projection of $\vec{QP_0}$ on $\mathbf{n}$:
$$D = \|\operatorname{proj}_{\mathbf{n}}\vec{QP_0}\| = \frac{|\vec{QP_0} \cdot \mathbf{n}|}{\|\mathbf{n}\|} = \frac{|a(x_0 - x_1) + b(y_0 - y_1) + c(z_0 - z_1)|}{\sqrt{a^2 + b^2 + c^2}}$$
Since $ax_1 + by_1 + cz_1 + d = 0 \implies d = -ax_1 - by_1 - cz_1$, combining yields (10). $\blacksquare$

#### Example 8
Find the distance $D$ between the point $(1, -4, -3)$ and the plane $2x - 3y + 6z = -1$.

**Solution.** Rewrite the plane as $2x - 3y + 6z + 1 = 0$. From (10):
$$D = \frac{|(2)(1) + (-3)(-4) + 6(-3) + 1|}{\sqrt{2^2 + (-3)^2 + 6^2}} = \frac{|-3|}{7} = \frac{3}{7}$$

#### Example 9
Find the distance between the parallel planes $x + 2y - 2z = 3$ and $2x + 4y - 4z = 7$.

**Solution.** Setting $y = z = 0$ in $x + 2y - 2z = 3$ gives $P_0(3, 0, 0)$. The distance from $P_0$ to $2x + 4y - 4z - 7 = 0$ is
$$D = \frac{|(2)(3) + 4(0) + (-4)(0) - 7|}{\sqrt{2^2 + 4^2 + (-4)^2}} = \frac{1}{6}$$

#### Example 10
Find the distance between the skew lines $L_1 : x = 1 + 4t, y = 5 - 4t, z = -1 + 5t$ and $L_2 : x = 2 + 8t, y = 4 - 3t, z = 5 + t$.

**Solution.** $\mathbf{u}_1 = \langle 4, -4, 5 \rangle$ and $\mathbf{u}_2 = \langle 8, -3, 1 \rangle$. The normal to the parallel planes containing $L_1$ and $L_2$ is
$$\mathbf{n} = \mathbf{u}_1 \times \mathbf{u}_2 = 11\mathbf{i} + 36\mathbf{j} + 20\mathbf{k}$$
Plane $P_2$ containing $L_2$ (using $Q_2(2, 4, 5)$ at $t = 0$) is $11(x - 2) + 36(y - 4) + 20(z - 5) = 0 \implies 11x + 36y + 20z - 266 = 0$. Point $Q_1(1, 5, -1)$ lies on $L_1$. The distance is
$$D = \frac{|(11)(1) + (36)(5) + (20)(-1) - 266|}{\sqrt{11^2 + 36^2 + 20^2}} = \frac{95}{\sqrt{1817}}$$

---

### QUICK CHECK EXERCISES 11.6
*(See page 821 for answers.)*

1. The point-normal form of the equation of the plane through $(0, 3, 5)$ and perpendicular to $\langle -4, 1, 7 \rangle$ is $\underline{\quad}$.
2. A normal vector for the plane $4x - 2y + 7z - 11 = 0$ is $\underline{\quad}$.
3. A normal vector for the plane through the points $(2, 5, 1), (3, 7, 0),$ and $(2, 5, 2)$ is $\underline{\quad}$.
4. The acute angle of intersection of the planes $x + y - 2z = 5$ and $3y - 4z = 6$ is $\underline{\quad}$.
5. The distance between the point $(9, 8, 3)$ and the plane $x + y - 2z = 5$ is $\underline{\quad}$.

---

### EXERCISE SET 11.6

1. Find equations of the planes $P_1, P_2,$ and $P_3$ that are parallel to the coordinate planes and pass through the corner $(3, 4, 5)$ of the box shown in Figure Ex-1.
2. Find equations of the planes $P_1, P_2,$ and $P_3$ that are parallel to the coordinate planes and pass through the corner $(x_0, y_0, z_0)$ of the box shown in Figure Ex-2.

**3–6 Find an equation of the plane that passes through the point $P$ and has the vector $\mathbf{n}$ as a normal.**
3. $P(2, 6, 1); \; \mathbf{n} = \langle 1, 4, 2 \rangle$
4. $P(-1, -1, 2); \; \mathbf{n} = \langle -1, 7, 6 \rangle$
5. $P(1, 0, 0); \; \mathbf{n} = \langle 0, 0, 1 \rangle$
6. $P(0, 0, 0); \; \mathbf{n} = \langle 2, -3, -4 \rangle$

**7–10 Find an equation of the plane indicated in the figure.**
7. Plane with intercepts $(1, 0, 0), (0, 1, 0), (0, 0, 1)$.
8. Plane passing through $(1, 0, 0), (0, 1, 0),$ and parallel to $z$-axis.
9. Plane passing through $(0, 1, 0), (0, 0, 1),$ and parallel to $x$-axis.
10. Plane passing through $(1, 0, 0), (0, 0, 1),$ and parallel to $y$-axis.

**11–12 Find an equation of the plane that passes through the given points.**
11. $(-2, 1, 1), (0, 2, 3),$ and $(1, 0, -1)$
12. $(3, 2, 1), (2, 1, -1),$ and $(-1, 3, 2)$

**13–14 Determine whether the planes are parallel, perpendicular, or neither.**
13. (a) $2x - 8y - 6z - 2 = 0$ and $-x + 4y + 3z - 5 = 0$  
    (b) $3x - 2y + z = 1$ and $4x + 5y - 2z = 4$  
    (c) $x - y + 3z - 2 = 0$ and $2x + z = 1$
14. (a) $3x - 2y + z = 4$ and $6x - 4y + 3z = 7$  
    (b) $y = 4x - 2z + 3$ and $x = \frac{1}{4}y + \frac{1}{2}z$  
    (c) $x + 4y + 7z = 3$ and $5x - 3y + z = 0$

**15–16 Determine whether the line and plane are parallel, perpendicular, or neither.**
15. (a) $x = 4 + 2t, y = -t, z = -1 - 4t; \; 3x + 2y + z - 7 = 0$  
    (b) $x = t, y = 2t, z = 3t; \; x - y + 2z = 5$  
    (c) $x = -1 + 2t, y = 4 + t, z = 1 - t; \; 4x + 2y - 2z = 7$
16. (a) $x = 3 - t, y = 2 + t, z = 1 - 3t; \; 2x + 2y - 5 = 0$  
    (b) $x = 1 - 2t, y = t, z = -t; \; 6x - 3y + 3z = 1$  
    (c) $x = t, y = 1 - t, z = 2 + t; \; x + y + z = 1$

**17–18 Determine whether the line and plane intersect; if so, find the coordinates of the intersection.**
17. (a) $x = t, y = t, z = t; \; 3x - 2y + z - 5 = 0$  
    (b) $x = 2 - t, y = 3 + t, z = t; \; 2x + y + z = 1$
18. (a) $x = 3t, y = 5t, z = -t; \; 2x - y + z + 1 = 0$  
    (b) $x = 1 + t, y = -1 + 3t, z = 2 + 4t; \; x - y + 4z = 7$

**19–20 Find the acute angle of intersection of the planes to the nearest degree.**
19. $x = 0$ and $2x - y + z - 4 = 0$
20. $x + 2y - 2z = 5$ and $6x - 3y + 2z = 8$

**21–24 True–False Determine whether the statement is true or false. Explain your answer.**
21. Every plane has exactly two unit normal vectors.
22. If a plane is parallel to one of the coordinate planes, then its normal vector is parallel to one of the three vectors $\mathbf{i}, \mathbf{j},$ or $\mathbf{k}$.
23. If two planes intersect in a line $L$, then $L$ is parallel to the cross product of the normals to the two planes.
24. If $a^2 + b^2 + c^2 = 1$, then the distance from $P(x_0, y_0, z_0)$ to the plane $ax + by + cz = 0$ is $|\langle a, b, c \rangle \cdot \langle x_0, y_0, z_0 \rangle|$.

**25–34 Find an equation of the plane that satisfies the stated conditions.**
25. The plane through the origin that is parallel to the plane $4x - 2y + 7z + 12 = 0$.
26. The plane that contains the line $x = -2 + 3t, y = 4 + 2t, z = 3 - t$ and is perpendicular to the plane $x - 2y + z = 5$.
27. The plane through the point $(-1, 4, 2)$ that contains the line of intersection of the planes $4x - y + z - 2 = 0$ and $2x + y - 2z - 3 = 0$.
28. The plane through $(-1, 4, -3)$ that is perpendicular to the line $x - 2 = t, y + 3 = 2t, z = -t$.
29. The plane through $(1, 2, -1)$ that is perpendicular to the line of intersection of the planes $2x + y + z = 2$ and $x + 2y + z = 3$.
30. The plane through the points $P_1(-2, 1, 4), P_2(1, 0, 3)$ that is perpendicular to the plane $4x - y + 3z = 2$.
31. The plane through $(-1, 2, -5)$ that is perpendicular to the planes $2x - y + z = 1$ and $x + y - 2z = 3$.
32. The plane that contains the point $(2, 0, 3)$ and the line $x = -1 + t, y = t, z = -4 + 2t$.
33. The plane whose points are equidistant from $(2, -1, 1)$ and $(3, 1, 5)$.
34. The plane that contains the line $x = 3t, y = 1 + t, z = 2t$ and is parallel to the intersection of the planes $y + z = -1$ and $2x - y + z = 0$.

35. Find parametric equations of the line through the point $(5, 0, -2)$ that is parallel to the planes $x - 4y + 2z = 0$ and $2x + 3y - z + 1 = 0$.
36. Let $L$ be the line $x = 3t + 1, y = -5t, z = t$.  
    (a) Show that $L$ lies in the plane $2x + y - z = 2$.  
    (b) Show that $L$ is parallel to the plane $x + y + 2z = 0$. Is the line above, below, or on this plane?
37. Show that the lines $x = -2 + t, y = 3 + 2t, z = 4 - t$ and $x = 3 - t, y = 4 - 2t, z = t$ are parallel and find an equation of the plane they determine.
38. Show that the lines $L_1 : x + 1 = 4t, y - 3 = t, z - 1 = 0$ and $L_2 : x + 13 = 12t, y - 1 = 6t, z - 2 = 3t$ intersect and find an equation of the plane they determine.

#### FOCUS ON CONCEPTS

39. Do the points $(1, 0, -1), (0, 2, 3), (-2, 1, 1),$ and $(4, 2, 3)$ lie in the same plane? Justify your answer two different ways.
40. Show that if $a, b,$ and $c$ are nonzero, then the plane whose intercepts with the coordinate axes are $x = a, y = b,$ and $z = c$ is given by the equation
    $$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$$

**41–42 Find parametric equations of the line of intersection of the planes.**
41. $-2x + 3y + 7z + 2 = 0$ and $x + 2y - 3z + 5 = 0$
42. $3x - 5y + 2z = 0$ and $z = 0$

**43–44 Find the distance between the point and the plane.**
43. $(1, -2, 3); \; 2x - 2y + z = 4$
44. $(0, 1, 5); \; 3x + 6y - 2z - 5 = 0$

**45–46 Find the distance between the given parallel planes.**
45. $-2x + y + z = 0$ and $6x - 3y - 3z - 5 = 0$
46. $x + y + z = 1$ and $x + y + z = -1$

**47–48 Find the distance between the given skew lines.**
47. $x = 1 + 7t, y = 3 + t, z = 5 - 3t$ and $x = 4 - t, y = 6, z = 7 + 2t$
48. $x = 3 - t, y = 4 + 4t, z = 1 + 2t$ and $x = t, y = 3, z = 2t$

49. Find an equation of the sphere with center $(2, 1, -3)$ that is tangent to the plane $x - 3y + 2z = 4$.
50. Locate the point of intersection of the plane $2x + y - z = 0$ and the line through $(3, 1, 0)$ that is perpendicular to the plane.
51. Show that the line $x = -1 + t, y = 3 + 2t, z = -t$ and the plane $2x - 2y - 2z + 3 = 0$ are parallel, and find the distance between them.

#### FOCUS ON CONCEPTS

52. Formulas (1), (2), (3), (5), and (10), which apply to planes in 3-space, have analogs for lines in 2-space.  
    (a) Draw an analog of Figure 11.6.3 in 2-space to illustrate that the equation of the line that passes through the point $P(x_0, y_0)$ and is perpendicular to the vector $\mathbf{n} = \langle a, b \rangle$ can be expressed as $\mathbf{n} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$ where $\mathbf{r} = \langle x, y \rangle$ and $\mathbf{r}_0 = \langle x_0, y_0 \rangle$.  
    (b) Show that the vector equation in part (a) can be expressed as $a(x - x_0) + b(y - y_0) = 0$. This is called the point-normal form of a line.  
    (c) Using the proof of Theorem 11.6.1 as a guide, show that if $a$ and $b$ are not both zero, then the graph of the equation $ax + by + c = 0$ is a line that has $\mathbf{n} = \langle a, b \rangle$ as a normal.  
    (d) Using the proof of Theorem 11.6.2 as a guide, show that the distance $D$ between a point $P(x_0, y_0)$ and the line $ax + by + c = 0$ is
    $$D = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$$  
    (e) Use the formula in part (d) to find the distance between the point $P(-3, 5)$ and the line $y = -2x + 1$.

53. (a) Show that the distance $D$ between parallel planes $ax + by + cz + d_1 = 0$ and $ax + by + cz + d_2 = 0$ is
    $$D = \frac{|d_1 - d_2|}{\sqrt{a^2 + b^2 + c^2}}$$  
    (b) Use the formula in part (a) to solve Exercise 45.

54. **Writing.** Explain why any line in 3-space must lie in some vertical plane. Must any line in 3-space also lie in some horizontal plane?
55. **Writing.** Given two planes, discuss the various possibilities for the set of points they have in common. Then consider the set of points that three planes can have in common.

#### QUICK CHECK ANSWERS 11.6
1. $-4x + (y - 3) + 7(z - 5) = 0$  
2. $\langle 4, -2, 7 \rangle$  
3. $\langle 2, -1, 0 \rangle$  
4. $\cos^{-1}\frac{11}{5\sqrt{6}} \approx 26^\circ$  
5. $\sqrt{6}$

---

---

## 11.7 QUADRIC SURFACES

In this section we will define and classify quadric surfaces, which are the three-dimensional analogs of the conic sections.

### QUADRIC SURFACES

A **quadric surface** (or **quadric**) is the graph of a second-degree polynomial equation in $x, y,$ and $z$. The general form of such an equation is
$$Ax^2 + By^2 + Cz^2 + Dxy + Exz + Fyz + Gx + Hy + Iz + J = 0 \tag{4}$$
where $A, B, C, \dots, J$ are constants and at least one of the coefficients $A, B, C, D, E, F$ is nonzero.

By translating and rotating the coordinate axes, the general equation of a quadric surface can be brought into one of two standard forms:
$$Ax^2 + By^2 + Cz^2 + J = 0 \quad \text{or} \quad Ax^2 + By^2 + Iz = 0$$
Quadric surfaces are classified into six basic types:
1. **Ellipsoid**
2. **Hyperboloid of one sheet**
3. **Hyperboloid of two sheets**
4. **Elliptic cone**
5. **Elliptic paraboloid**
6. **Hyperbolic paraboloid**

---

### TABLE 11.7.1: QUADRIC SURFACES (STANDARD ORIENTATION)

| Surface | Standard Equation | Traces |
| :--- | :--- | :--- |
| **Ellipsoid** | $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ | * $xy$-plane ($z = 0$): $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ (ellipse)<br>* $xz$-plane ($y = 0$): $\frac{x^2}{a^2} + \frac{z^2}{c^2} = 1$ (ellipse)<br>* $yz$-plane ($x = 0$): $\frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ (ellipse)<br>* Parallel to coordinate planes: Ellipses for $|x| < a, |y| < b, |z| < c$. |
| **Hyperboloid of One Sheet** | $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$ | * $xy$-plane ($z = 0$): $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ (ellipse)<br>* $xz$-plane ($y = 0$): $\frac{x^2}{a^2} - \frac{z^2}{c^2} = 1$ (hyperbola)<br>* $yz$-plane ($x = 0$): $\frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$ (hyperbola)<br>* Parallel to $xy$-plane ($z = k$): Ellipses $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 + \frac{k^2}{c^2}$. |
| **Hyperboloid of Two Sheets** | $\frac{z^2}{c^2} - \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | * $xy$-plane ($z = 0$): No trace<br>* $xz$-plane ($y = 0$): $\frac{z^2}{c^2} - \frac{x^2}{a^2} = 1$ (hyperbola)<br>* $yz$-plane ($x = 0$): $\frac{z^2}{c^2} - \frac{y^2}{b^2} = 1$ (hyperbola)<br>* Parallel to $xy$-plane ($|z| = k > c$): Ellipses $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{k^2}{c^2} - 1$. |
| **Elliptic Cone** | $z^2 = \frac{x^2}{a^2} + \frac{y^2}{b^2}$ | * $xy$-plane ($z = 0$): Point $(0, 0, 0)$<br>* $xz$-plane ($y = 0$): Pair of intersecting lines $z = \pm\frac{c}{a}x$<br>* $yz$-plane ($x = 0$): Pair of intersecting lines $z = \pm\frac{c}{b}y$<br>* Parallel to $xy$-plane ($z = k \neq 0$): Ellipses $\frac{x^2}{a^2} + \frac{y^2}{b^2} = k^2$. |
| **Elliptic Paraboloid** | $z = \frac{x^2}{a^2} + \frac{y^2}{b^2}$ | * $xy$-plane ($z = 0$): Point $(0, 0, 0)$<br>* $xz$-plane ($y = 0$): Parabola $z = \frac{x^2}{a^2}$<br>* $yz$-plane ($x = 0$): Parabola $z = \frac{y^2}{b^2}$<br>* Parallel to $xy$-plane ($z = k > 0$): Ellipses $\frac{x^2}{a^2} + \frac{y^2}{b^2} = k$. |
| **Hyperbolic Paraboloid** | $z = \frac{y^2}{b^2} - \frac{x^2}{a^2}$ | * $xy$-plane ($z = 0$): Pair of intersecting lines $y = \pm\frac{b}{a}x$<br>* $xz$-plane ($y = 0$): Parabola $z = -\frac{x^2}{a^2}$ (opens downward)<br>* $yz$-plane ($x = 0$): Parabola $z = \frac{y^2}{b^2}$ (opens upward)<br>* Parallel to $xy$-plane ($z = k \neq 0$): Hyperbolas $\frac{y^2}{b^2} - \frac{x^2}{a^2} = k$. |

---

### TRANSLATIONS AND REFLECTIONS OF QUADRIC SURFACES

If the center or vertex of a quadric surface is translated from the origin to $(x_0, y_0, z_0)$, its equation is obtained by replacing $x, y, z$ with $x - x_0, y - y_0, z - z_0$.

#### Example 1
Describe the surface $x^2 + \frac{y^2}{4} + \frac{z^2}{9} = 1$.

**Solution.** This is an ellipsoid in standard position with $a = 1, b = 2,$ and $c = 3$. The traces in the $xy$-, $xz$-, and $yz$-planes are the ellipses
$$x^2 + \frac{y^2}{4} = 1, \quad x^2 + \frac{z^2}{9} = 1, \quad \frac{y^2}{4} + \frac{z^2}{9} = 1$$

#### Example 2
Describe the surface $z = x^2 + y^2$.

**Solution.** This is an elliptic paraboloid (specifically a circular paraboloid) with $a = b = 1$. The trace in the $xy$-plane is the single point $(0, 0, 0)$; for $z = k > 0$, the horizontal traces are circles $x^2 + y^2 = k$ of radius $\sqrt{k}$. The vertical traces in the $xz$- and $yz$-planes are parabolas $z = x^2$ and $z = y^2$.

#### Example 3
Describe the surface $z = y^2 - x^2$.

**Solution.** This is a hyperbolic paraboloid with $a = b = 1$. In the $xy$-plane ($z = 0$), the trace is the pair of lines $y = \pm x$. In the planes $z = k$, the traces are hyperbolas $y^2 - x^2 = k$ (opening along the $y$-axis for $k > 0$ and along the $x$-axis for $k < 0$). In the $yz$-plane ($x = 0$), the trace is the parabola $z = y^2$ (opening upward), and in the $xz$-plane ($y = 0$), the trace is $z = -x^2$ (opening downward). The origin is a **saddle point**.

#### Example 4
Describe the surface $x^2 + \frac{y^2}{4} - \frac{z^2}{9} = 1$.

**Solution.** This is a hyperboloid of one sheet with axis along the $z$-axis. The trace in the $xy$-plane is the ellipse $x^2 + y^2/4 = 1$. Horizontal traces in planes $z = k$ are ellipses $x^2 + y^2/4 = 1 + k^2/9$. Vertical traces in the $xz$- and $yz$-planes are hyperbolas $x^2 - z^2/9 = 1$ and $y^2/4 - z^2/9 = 1$.

#### Example 5
Describe the surface $\frac{z^2}{4} - \frac{x^2}{9} - \frac{y^2}{16} = 1$.

**Solution.** This is a hyperboloid of two sheets opening along the $z$-axis. There is no trace in the $xy$-plane. For $|z| > 2$, horizontal traces in planes $z = k$ are ellipses $x^2/9 + y^2/16 = k^2/4 - 1$. Vertical traces in $xz$- and $yz$-planes are hyperbolas $z^2/4 - x^2/9 = 1$ and $z^2/4 - y^2/16 = 1$.

#### Example 6
Describe the surface $z^2 = x^2 + \frac{y^2}{4}$.

**Solution.** This is an elliptic cone opening along the $z$-axis. The trace in the $xy$-plane is the origin $(0, 0, 0)$. In planes $z = k \neq 0$, traces are ellipses $x^2 + y^2/4 = k^2$. Traces in $xz$- and $yz$-planes are the pairs of intersecting lines $z = \pm x$ and $z = \pm y/2$.

#### Example 7
Describe the surface $y = x^2 + z^2$.

**Solution.** This is a circular paraboloid opening along the positive $y$-axis (the axis of the paraboloid corresponds to the variable that appears to the first power). Traces in planes $y = k > 0$ are circles $x^2 + z^2 = k$.

#### Example 8
Describe the surface $\frac{x^2}{4} - \frac{y^2}{9} + z^2 = 1$.

**Solution.** This is a hyperboloid of one sheet whose axis is the $y$-axis (the axis corresponds to the variable with the negative coefficient). Traces parallel to the $xz$-plane are ellipses $x^2/4 + z^2 = 1 + k^2/9$.

#### Example 9
Describe the surface $z = \sqrt{1 - x^2 - y^2}$.

**Solution.** Squaring both sides gives $z^2 = 1 - x^2 - y^2$ or $x^2 + y^2 + z^2 = 1$, which is a sphere of radius 1 centered at the origin. Since $z = \sqrt{1 - x^2 - y^2} \ge 0$, the surface is the upper hemisphere of this sphere.

#### Example 10
Describe the surface $x^2 - y^2 + 4z^2 - 2x - 4y + 8z + 1 = 0$.

**Solution.** Completing the square in $x, y,$ and $z$:
$$(x^2 - 2x + 1) - (y^2 + 4y + 4) + 4(z^2 + 2z + 1) = -1 + 1 - 4 + 4 = 0$$
$$(x - 1)^2 - (y + 2)^2 + 4(z + 1)^2 = 0$$
$$(y + 2)^2 = (x - 1)^2 + 4(z + 1)^2 \implies (y + 2)^2 = (x - 1)^2 + \frac{(z + 1)^2}{(1/2)^2}$$
This is an elliptic cone with vertex at $(1, -2, -1)$ and opening along the line $x = 1, z = -1$ parallel to the $y$-axis.

---

### QUICK CHECK EXERCISES 11.7
*(See page 832 for answers.)*

1. Describe the trace of the quadric surface $4x^2 + y^2 + z^2 = 9$ in the given plane.  
   (a) $x = 0$  
   (b) $y = 0$  
   (c) $z = 1$
2. Describe the trace of the quadric surface $4x^2 + z^2 - y^2 = 9$ in the given plane.  
   (a) $x = 0$  
   (b) $y = 0$  
   (c) $z = 1$
3. Describe the trace of the quadric surface $4x^2 + y^2 - z = 0$ in the given plane.  
   (a) $x = 0$  
   (b) $y = 0$  
   (c) $z = 1$
4. Classify the quadric surface as an ellipsoid, hyperboloid of one sheet, hyperboloid of two sheets, elliptic cone, elliptic paraboloid, or hyperbolic paraboloid.  
   (a) $\frac{x^2}{36} + \frac{y^2}{25} - z = 0$  
   (b) $\frac{x^2}{36} + \frac{y^2}{25} + z^2 = 1$  
   (c) $\frac{x^2}{36} - \frac{y^2}{25} + z = 0$  
   (d) $\frac{x^2}{36} + \frac{y^2}{25} - z^2 = 1$  
   (e) $\frac{x^2}{36} + \frac{y^2}{25} - z^2 = 0$  
   (f) $z^2 - \frac{x^2}{36} - \frac{y^2}{25} = 1$

---

### EXERCISE SET 11.7

**1–2 Match the given equation with one of the standard forms in Table 11.7.1, and then identify the quadric surface and the values of $a, b,$ and $c$.**
1. (a) $\frac{x^2}{4} + \frac{y^2}{9} + \frac{z^2}{16} = 1$  
   (b) $z = \frac{x^2}{4} + \frac{y^2}{9}$  
   (c) $z^2 = \frac{x^2}{4} + \frac{y^2}{9}$  
   (d) $\frac{x^2}{4} + \frac{y^2}{9} - \frac{z^2}{16} = 1$
2. (a) $\frac{z^2}{16} - \frac{x^2}{4} - \frac{y^2}{9} = 1$  
   (b) $z = \frac{y^2}{9} - \frac{x^2}{4}$  
   (c) $x^2 + y^2 + z^2 = 9$  
   (d) $z = x^2 + y^2$

**3–4 Find the equation of the quadric surface that results when:**
3. (a) the paraboloid $z = x^2 + y^2$ is reflected about the $xy$-plane;  
   (b) the paraboloid $z = x^2 + y^2$ is reflected about the $xz$-plane;  
   (c) the hyperboloid $x^2 + y^2 - z^2 = 1$ is reflected about the $yz$-plane.
4. (a) the cone $z^2 = x^2 + y^2$ is reflected about the $xy$-plane;  
   (b) the hyperbolic paraboloid $z = y^2 - x^2$ is reflected about the $xy$-plane;  
   (c) the ellipsoid $x^2 + 2y^2 + 3z^2 = 1$ is reflected about the $xz$-plane.

**5–6 Determine the orientation and describe the surface.**
5. (a) $y = \frac{x^2}{4} + \frac{z^2}{9}$  
   (b) $x = \frac{y^2}{9} - \frac{z^2}{4}$  
   (c) $\frac{y^2}{9} - \frac{x^2}{4} - \frac{z^2}{16} = 1$
6. (a) $x^2 = \frac{y^2}{4} + \frac{z^2}{9}$  
   (b) $\frac{y^2}{4} + \frac{z^2}{9} - \frac{x^2}{16} = 1$  
   (c) $\frac{y^2}{4} + \frac{z^2}{9} + \frac{x^2}{16} = 1$

**7–8 Find the equations of the traces in the coordinate planes $x = 0, y = 0,$ and $z = 0$.**
7. (a) $4x^2 + 9y^2 + 36z^2 = 36$  
   (b) $4x^2 + 9y^2 - 36z^2 = 36$  
   (c) $4x^2 - 9y^2 - 36z^2 = 36$
8. (a) $z = 4x^2 + 9y^2$  
   (b) $z = 9y^2 - 4x^2$  
   (c) $36z^2 = 4x^2 + 9y^2$

**9–10 Identify the conic section formed by the trace of the given surface in the given plane.**
9. (a) $x^2 + 4y^2 + 9z^2 = 36; \; y = 2$  
   (b) $x^2 + 4y^2 - 9z^2 = 36; \; z = 1$  
   (c) $x^2 + 4y^2 - 9z^2 = 36; \; x = 4$
10. (a) $z = x^2 + 4y^2; \; z = 4$  
    (b) $z = 4y^2 - x^2; \; z = 4$  
    (c) $z = 4y^2 - x^2; \; y = 2$

**11–14 True–False Determine whether the statement is true or false. Explain your answer.**
11. Every trace of an ellipsoid is an ellipse.
12. The hyperboloid of one sheet $x^2 + y^2 - z^2 = 1$ and the elliptic cone $x^2 + y^2 - z^2 = 0$ have identical traces in the plane $z = 0$.
13. Every trace of a hyperbolic paraboloid is a hyperbola.
14. An elliptic paraboloid centered at the origin has no trace in the plane $z = -1$ if it opens upward.

**15–26 Identify and sketch the quadric surface.**
15. $\frac{x^2}{9} + \frac{y^2}{16} + \frac{z^2}{4} = 1$
16. $\frac{x^2}{4} + \frac{y^2}{25} + \frac{z^2}{9} = 1$
17. $\frac{x^2}{9} + \frac{y^2}{16} - \frac{z^2}{4} = 1$
18. $\frac{x^2}{4} - \frac{y^2}{9} + \frac{z^2}{16} = 1$
19. $\frac{z^2}{4} - \frac{x^2}{9} - \frac{y^2}{16} = 1$
20. $\frac{y^2}{9} - \frac{x^2}{4} - \frac{z^2}{16} = 1$
21. $z = \frac{x^2}{4} + \frac{y^2}{9}$
22. $y = \frac{x^2}{9} + \frac{z^2}{4}$
23. $z = \frac{y^2}{9} - \frac{x^2}{4}$
24. $x = \frac{y^2}{4} - \frac{z^2}{9}$
25. $z^2 = \frac{x^2}{4} + \frac{y^2}{9}$
26. $y^2 = \frac{x^2}{9} + \frac{z^2}{4}$

**27–32 Identify the quadric surface whose equation is given.**
27. $4x^2 + y^2 + 4z^2 = 16$
28. $4x^2 - y^2 + 4z^2 = 16$
29. $4x^2 - y^2 - 4z^2 = 16$
30. $z = 4x^2 + 4y^2$
31. $z = 4x^2 - y^2$
32. $z^2 = 4x^2 + y^2$

**33–36 Describe the portion of the quadric surface represented by the equation.**
33. $z = \sqrt{1 - x^2 - y^2}$
34. $z = -\sqrt{1 - x^2 - y^2}$
35. $z = \sqrt{x^2 + y^2}$
36. $z = -\sqrt{x^2 + y^2}$

**37–40 Identify the quadric surface by completing the square.**
37. $x^2 + y^2 + z^2 - 2x - 4y - 6z + 5 = 0$
38. $x^2 + 4y^2 - z^2 - 2x + 8y + 4z = 0$
39. $x^2 - y^2 - z^2 - 4x + 2y + 4z - 2 = 0$
40. $z = x^2 + 2y^2 - 4x + 4y + 6$

#### FOCUS ON CONCEPTS

41. (a) Find the foci of the elliptical trace of the ellipsoid $\frac{x^2}{16} + \frac{y^2}{9} + \frac{z^2}{4} = 1$ in the $xy$-plane.  
    (b) Find the foci of the elliptical trace of this ellipsoid in the $xz$-plane.  
    (c) Find the foci of the elliptical trace of this ellipsoid in the $yz$-plane.
42. Show that the area of the elliptical trace of the ellipsoid $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ in the plane $z = k \; (|k| < c)$ is $A = \pi ab\left(1 - \frac{k^2}{c^2}\right)$. *[Hint: The area of an ellipse $\frac{x^2}{A^2} + \frac{y^2}{B^2} = 1$ is $\pi AB$.]*
43. Find the vertices and foci of the parabolic trace of the hyperbolic paraboloid $z = \frac{y^2}{4} - \frac{x^2}{9}$ in the plane $x = k$.
44. Find the vertices and foci of the parabolic trace of the hyperbolic paraboloid $z = \frac{y^2}{4} - \frac{x^2}{9}$ in the plane $y = k$.
45. Find the foci of the hyperbolic trace of the hyperbolic paraboloid $z = \frac{y^2}{4} - \frac{x^2}{9}$ in the plane $z = 4$.
46. Find the foci of the hyperbolic trace of the hyperbolic paraboloid $z = \frac{y^2}{4} - \frac{x^2}{9}$ in the plane $z = -4$.

**47–48 Find an equation for the surface consisting of all points that satisfy the stated condition.**
47. Equidistant from the point $(0, 0, 4)$ and the plane $z = -4$.
48. Equidistant from the point $(0, 2, 0)$ and the plane $y = -2$.

**49–50 Find an equation of the surface generated by revolving the given curve about the indicated axis.**
49. $y = x^2$ in the $xy$-plane about the $y$-axis.
50. $z = 2y$ in the $yz$-plane about the $z$-axis.

51. Show that the surface consisting of all points $P(x, y, z)$ whose distance to the $z$-axis is twice the distance to the $xy$-plane is an elliptic cone.
52. Show that the surface consisting of all points $P(x, y, z)$ whose distance to the point $(0, 0, 1)$ is half the distance to the $xy$-plane is an ellipsoid.
53. An ellipsoid of revolution of the form $\frac{x^2}{a^2} + \frac{y^2}{a^2} + \frac{z^2}{c^2} = 1$ with $a > c$ is called an **oblate spheroid**.  
    (a) Show that the cross section in the $xy$-plane is a circle of radius $a$.  
    (b) Show that the cross section in any plane containing the $z$-axis is an ellipse with major axis of length $2a$ and minor axis of length $2c$.
54. The Earth is approximately an oblate spheroid with equatorial radius $a \approx 6378.1370\text{ km}$ and polar radius $c \approx 6356.5231\text{ km}$ (WGS-84 reference ellipsoid). Write an equation for the surface of the Earth assuming the center is at the origin and the polar axis is along the $z$-axis.
55. Use the method of slicing (Section 6.1) and the result of Exercise 42 to show that the volume of the ellipsoid $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$ is $V = \frac{4}{3}\pi abc$.
56. **Writing.** Discuss the relationship between the traces of a quadric surface and the geometric shape of the surface. Explain how analyzing traces in planes parallel to the coordinate planes helps to identify the quadric surface.
57. **Writing.** Summarize the general procedure for classifying a quadric surface from its algebraic equation, including the role of completing the square and analyzing signs of the quadratic terms.

#### QUICK CHECK ANSWERS 11.7
1. (a) ellipse (b) ellipse (c) ellipse  
2. (a) hyperbola (b) ellipse (c) hyperbola  
3. (a) parabola (b) parabola (c) ellipse  
4. (a) elliptic paraboloid (b) ellipsoid (c) hyperbolic paraboloid (d) hyperboloid of one sheet (e) elliptic cone (f) hyperboloid of two sheets

---

---

## 11.8 CYLINDRICAL AND SPHERICAL COORDINATES

In this section we will introduce two new coordinate systems in 3-space: **cylindrical coordinates** and **spherical coordinates**. These systems are especially useful for problems that involve symmetries about a line or a point.

### CYLINDRICAL COORDINATES

The **cylindrical coordinate system** is the three-dimensional analog of polar coordinates in 2-space. In this system, a point $P$ in 3-space is represented by an ordered triple $(r, \theta, z)$, where:
* $r$ and $\theta$ are polar coordinates for the vertical projection of $P$ on the $xy$-plane (with $r \ge 0$ and $0 \le \theta < 2\pi$).
* $z$ is the directed distance from the $xy$-plane to $P$ (the same as the $z$-coordinate in rectangular coordinates).

The relationships between rectangular coordinates $(x, y, z)$ and cylindrical coordinates $(r, \theta, z)$ are:
* **Cylindrical to Rectangular:**
  $$x = r\cos\theta, \quad y = r\sin\theta, \quad z = z \tag{1}$$
* **Rectangular to Cylindrical:**
  $$r = \sqrt{x^2 + y^2}, \quad \tan\theta = \frac{y}{x}, \quad z = z \tag{2}$$

#### Example 1
(a) Find the rectangular coordinates of the point with cylindrical coordinates $(r, \theta, z) = (4, 2\pi/3, 5)$.  
(b) Find the cylindrical coordinates of the point with rectangular coordinates $(x, y, z) = (1, -\sqrt{3}, 2)$.

**Solution (a).** From (1):
$$x = 4\cos\left(\frac{2\pi}{3}\right) = 4\left(-\frac{1}{2}\right) = -2$$
$$y = 4\sin\left(\frac{2\pi}{3}\right) = 4\left(\frac{\sqrt{3}}{2}\right) = 2\sqrt{3}$$
$$z = 5$$
Thus, the rectangular coordinates are $(x, y, z) = (-2, 2\sqrt{3}, 5)$.

**Solution (b).** From (2):
$$r = \sqrt{1^2 + (-\sqrt{3})^2} = \sqrt{1 + 3} = 2$$
$$\tan\theta = \frac{-\sqrt{3}}{1} = -\sqrt{3}$$
Since $(1, -\sqrt{3})$ lies in the fourth quadrant of the $xy$-plane, we take $\theta = 2\pi - \pi/3 = 5\pi/3$. Since $z = 2$, the cylindrical coordinates are $(r, \theta, z) = (2, 5\pi/3, 2)$.

---

### SPHERICAL COORDINATES

In the **spherical coordinate system**, a point $P$ in 3-space is represented by an ordered triple $(\rho, \theta, \phi)$, where:
* $\rho = \|\vec{OP}\|$ is the distance from the origin to $P$ ($\rho \ge 0$).
* $\theta$ is the angle between the positive $x$-axis and the projection of $\vec{OP}$ onto the $xy$-plane ($0 \le \theta < 2\pi$, identical to $\theta$ in cylindrical coordinates).
* $\phi$ is the angle between the positive $z$-axis and the vector $\vec{OP}$ ($0 \le \phi \le \pi$). The angle $\phi$ is called the **polar angle** or **cone angle**.

The relationships between rectangular, cylindrical, and spherical coordinates are:
* **Spherical to Rectangular:**
  $$x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi \tag{3}$$
* **Spherical to Cylindrical:**
  $$r = \rho\sin\phi, \quad \theta = \theta, \quad z = \rho\cos\phi \tag{4}$$
* **Rectangular to Spherical:**
  $$\rho = \sqrt{x^2 + y^2 + z^2}, \quad \tan\theta = \frac{y}{x}, \quad \cos\phi = \frac{z}{\sqrt{x^2 + y^2 + z^2}} \tag{5}$$

#### Example 2
(a) Find the rectangular coordinates of the point with spherical coordinates $(\rho, \theta, \phi) = (4, \pi/3, \pi/4)$.  
(b) Find the spherical coordinates of the point with rectangular coordinates $(x, y, z) = (1, -1, \sqrt{6})$.

**Solution (a).** From (3):
$$x = 4\sin\left(\frac{\pi}{4}\right)\cos\left(\frac{\pi}{3}\right) = 4\left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right) = \sqrt{2}$$
$$y = 4\sin\left(\frac{\pi}{4}\right)\sin\left(\frac{\pi}{3}\right) = 4\left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) = \sqrt{6}$$
$$z = 4\cos\left(\frac{\pi}{4}\right) = 4\left(\frac{\sqrt{2}}{2}\right) = 2\sqrt{2}$$
Thus, $(x, y, z) = (\sqrt{2}, \sqrt{6}, 2\sqrt{2})$.

**Solution (b).** From (5):
$$\rho = \sqrt{1^2 + (-1)^2 + (\sqrt{6})^2} = \sqrt{1 + 1 + 6} = \sqrt{8} = 2\sqrt{2}$$
$$\tan\theta = \frac{-1}{1} = -1 \implies \theta = \frac{7\pi}{4} \quad (\text{since } x > 0, y < 0)$$
$$\cos\phi = \frac{z}{\rho} = \frac{\sqrt{6}}{2\sqrt{2}} = \frac{\sqrt{3}}{2} \implies \phi = \frac{\pi}{6}$$
Thus, $(\rho, \theta, \phi) = (2\sqrt{2}, 7\pi/4, \pi/6)$.

---

### CONSTANT SURFACES

* **Cylindrical Coordinates:**
  * $r = c$ (constant): Right circular cylinder of radius $c$ centered on the $z$-axis.
  * $\theta = c$ (constant): Vertical half-plane making angle $c$ with the positive $x$-axis.
  * $z = c$ (constant): Horizontal plane.
* **Spherical Coordinates:**
  * $\rho = c$ (constant): Sphere of radius $c$ centered at the origin.
  * $\theta = c$ (constant): Vertical half-plane making angle $c$ with the positive $x$-axis.
  * $\phi = c$ (constant): Half-cone opening along the positive $z$-axis (for $0 < c < \pi/2$), the $xy$-plane (for $c = \pi/2$), or half-cone opening downward (for $\pi/2 < c < \pi$).

#### Example 3
Find equations of the cone $z = \sqrt{x^2 + y^2}$ in cylindrical and spherical coordinates.

**Solution.** In cylindrical coordinates, $x^2 + y^2 = r^2$, so the equation becomes $z = r$.  
In spherical coordinates, substituting $z = \rho\cos\phi$ and $r = \rho\sin\phi$ gives $\rho\cos\phi = \rho\sin\phi \implies \tan\phi = 1 \implies \phi = \pi/4$.

#### Example 4
Find an equation in spherical coordinates for the sphere $x^2 + y^2 + (z - 1)^2 = 1$.

**Solution.** Expanding the equation gives $x^2 + y^2 + z^2 - 2z = 0$, so $\rho^2 - 2\rho\cos\phi = 0$. Since $\rho \neq 0$ for points other than the origin, we obtain
$$\rho = 2\cos\phi$$

---

### QUICK CHECK EXERCISES 11.8
*(See page 838 for answers.)*

1. State the formulas for converting from cylindrical coordinates $(r, \theta, z)$ to rectangular coordinates $(x, y, z)$: $x = \underline{\quad}, y = \underline{\quad}, z = \underline{\quad}$.
2. State the formulas for converting from spherical coordinates $(\rho, \theta, \phi)$ to rectangular coordinates $(x, y, z)$: $x = \underline{\quad}, y = \underline{\quad}, z = \underline{\quad}$.
3. State the formulas for converting from spherical coordinates $(\rho, \theta, \phi)$ to cylindrical coordinates $(r, \theta, z)$: $r = \underline{\quad}, \theta = \underline{\quad}, z = \underline{\quad}$.
4. Find the cylindrical and spherical coordinates of the point whose rectangular coordinates are $(\sqrt{2}, -\sqrt{2}, 2\sqrt{3})$.  
   (a) Cylindrical: $\underline{\quad}$  
   (b) Spherical: $\underline{\quad}$
5. Express the equation of the sphere of radius 5 centered at the origin in:  
   (a) Rectangular coordinates: $\underline{\quad}$  
   (b) Cylindrical coordinates: $\underline{\quad}$  
   (c) Spherical coordinates: $\underline{\quad}$.

---

### EXERCISE SET 11.8

**1–2 Convert the rectangular coordinates to cylindrical coordinates.**
1. (a) $(3, 3, 7)$  
   (b) $(-1, \sqrt{3}, 2)$  
   (c) $(0, 5, 1)$  
   (d) $(-2, -2, -1)$
2. (a) $(0, -2, 3)$  
   (b) $(4, 0, -2)$  
   (c) $(-\sqrt{2}, -\sqrt{2}, 4)$  
   (d) $(2\sqrt{3}, 2, -1)$

**3–4 Convert the cylindrical coordinates to rectangular coordinates.**
3. (a) $(4, \pi/6, 3)$  
   (b) $(2, 2\pi/3, -1)$  
   (c) $(5, \pi, 2)$  
   (d) $(0, \pi/2, 4)$
4. (a) $(6, 5\pi/4, -3)$  
   (b) $(1, 3\pi/2, 0)$  
   (c) $(8, 7\pi/6, 5)$  
   (d) $(3, 0, -4)$

**5–6 Convert the rectangular coordinates to spherical coordinates.**
5. (a) $(1, 1, \sqrt{2})$  
   (b) $(1, -\sqrt{3}, 2)$  
   (c) $(-\sqrt{2}, \sqrt{2}, 2\sqrt{3})$  
   (d) $(0, 0, -4)$
6. (a) $(0, 2, 0)$  
   (b) $(-3, 0, 0)$  
   (c) $(-\sqrt{3}, -1, 2\sqrt{3})$  
   (d) $(0, 0, 5)$

**7–8 Convert the spherical coordinates to rectangular coordinates.**
7. (a) $(4, \pi/4, \pi/6)$  
   (b) $(2, \pi/3, \pi/2)$  
   (c) $(6, 3\pi/4, 2\pi/3)$  
   (d) $(5, 0, \pi)$
8. (a) $(3, \pi/2, \pi/4)$  
   (b) $(8, 5\pi/6, \pi/3)$  
   (c) $(1, 7\pi/4, 3\pi/4)$  
   (d) $(2, \pi, 0)$

**9–10 Convert the cylindrical coordinates to spherical coordinates.**
9. (a) $(2, \pi/4, 2)$  
   (b) $(\sqrt{3}, \pi/6, 1)$  
   (c) $(4, \pi/2, 0)$  
   (d) $(0, 0, -2)$
10. (a) $(1, 3\pi/4, \sqrt{3})$  
    (b) $(2\sqrt{3}, 5\pi/3, -2)$  
    (c) $(3, 0, 3\sqrt{3})$  
    (d) $(0, \pi, 5)$

**11–12 Convert the spherical coordinates to cylindrical coordinates.**
11. (a) $(4, \pi/3, \pi/4)$  
    (b) $(2, \pi/2, \pi/2)$  
    (c) $(6, 5\pi/6, \pi/6)$  
    (d) $(8, \pi, 2\pi/3)$
12. (a) $(3, 3\pi/4, \pi/3)$  
    (b) $(5, 7\pi/4, \pi/2)$  
    (c) $(2, 0, 3\pi/4)$  
    (d) $(4, 4\pi/3, \pi/6)$

13. Use a CAS to convert the rectangular coordinates $(1.5, -2.7, 3.8)$ to (a) cylindrical coordinates and (b) spherical coordinates.
14. Use a CAS to convert the spherical coordinates $(5.2, 1.3, 0.9)$ to (a) rectangular coordinates and (b) cylindrical coordinates.

**15–18 True–False Determine whether the statement is true or false. Explain your answer.**
15. The cylindrical coordinate $(r, \theta, z)$ of a point $P$ is unique if $r > 0$ and $0 \le \theta < 2\pi$.
16. The spherical coordinate $(\rho, \theta, \phi)$ of a point $P$ is unique if $\rho > 0, 0 \le \theta < 2\pi,$ and $0 \le \phi \le \pi$, with the exception of points on the $z$-axis.
17. The equation $r = \sin\theta$ in cylindrical coordinates represents a cylinder.
18. The equation $\rho = \sin\phi$ in spherical coordinates represents a sphere.

**19–26 An equation is given in cylindrical coordinates. Express the equation in rectangular coordinates and sketch the graph.**
19. $r = 3$
20. $\theta = \pi/4$
21. $z = r^2$
22. $z = r\cos\theta$
23. $r = 2\sin\theta$
24. $r = 4\cos\theta$
25. $r^2 + z^2 = 9$
26. $z = 4 - r^2$

**27–34 An equation is given in spherical coordinates. Express the equation in rectangular coordinates and sketch the graph.**
27. $\rho = 4$
28. $\theta = \pi/3$
29. $\phi = \pi/4$
30. $\phi = 2\pi/3$
31. $\rho = 2\sec\phi$
32. $\rho = 4\csc\phi\sec\theta$
33. $\rho = 4\cos\phi$
34. $\rho = 2\sin\phi\sin\theta$

**35–46 Convert the equation in rectangular coordinates to (a) cylindrical coordinates and (b) spherical coordinates.**
35. $x^2 + y^2 + z^2 = 16$
36. $z = x^2 + y^2$
37. $z = \sqrt{x^2 + y^2}$
38. $x^2 + y^2 = 4$
39. $x = 2$
40. $y = 3$
41. $z = 5$
42. $x^2 + y^2 - z^2 = 1$
43. $x^2 + y^2 + z^2 - 2z = 0$
44. $x^2 + y^2 + z^2 - 4x = 0$
45. $2x + 3y + 4z = 1$
46. $x^2 + y^2 = 2x$

**47–50 Describe the solid in 3-space described by the inequalities.**
47. $0 \le r \le 2, \quad 0 \le \theta \le \pi/2, \quad 0 \le z \le 3$
48. $1 \le r \le 3, \quad 0 \le \theta \le 2\pi, \quad 0 \le z \le 4$
49. $0 \le \rho \le 2, \quad 0 \le \theta \le 2\pi, \quad 0 \le \phi \le \pi/4$
50. $1 \le \rho \le 2, \quad 0 \le \theta \le \pi, \quad \pi/4 \le \phi \le \pi/2$

51. The city of St. Petersburg, Russia, is located at approximately latitude $60^\circ\text{ N}$ and longitude $30^\circ\text{ E}$. Assuming the Earth is a sphere of radius $R = 6370\text{ km}$, find the spherical coordinates of St. Petersburg if the origin is at the center of the Earth, the positive $z$-axis passes through the North Pole, and the prime meridian lies in the $xz$-plane.
52. Find parametric equations in cylindrical coordinates for the curve of intersection of the cylinder $r = a$ and the surface $z = \sin\theta$.
53. A bug is crawling up a circular cylinder of radius $R = 2\text{ cm}$ at a constant speed of $1\text{ cm/s}$ while the cylinder rotates about its axis at a constant rate of $\omega = 1\text{ rad/s}$. If the bug starts at $(2, 0, 0)$ at time $t = 0$, find its position $(r(t), \theta(t), z(t))$ in cylindrical coordinates as a function of $t$.
54. For the bug in Exercise 53, find its distance from the origin at time $t = 5\text{ s}$.
55. **Writing.** Discuss the relative advantages and disadvantages of rectangular, cylindrical, and spherical coordinates for describing surfaces in 3-space. Give examples of surfaces that have simple equations in one system but complicated equations in another.
56. **Writing.** Explain how spherical coordinates are related to the latitude, longitude, and elevation used in geography and the zenith angle and azimuth used in celestial navigation.

#### QUICK CHECK ANSWERS 11.8
1. $r\cos\theta; r\sin\theta; z$  
2. $\rho\sin\phi\cos\theta; \rho\sin\phi\sin\theta; \rho\cos\phi$  
3. $\rho\sin\phi; \theta; \rho\cos\phi$  
4. (a) $(2, 7\pi/4, 2\sqrt{3})$ (b) $(4, 7\pi/4, \pi/6)$  
5. (a) $x^2 + y^2 + z^2 = 25$ (b) $r^2 + z^2 = 25$ (c) $\rho = 5$

---

## CHAPTER 11 REVIEW EXERCISES

1. (a) State the difference between a vector and a scalar. Give examples of each.  
   (b) How do you determine whether two vectors are orthogonal using the dot product?  
   (c) How do you determine whether two vectors are parallel using the cross product?  
   (d) How do you determine whether three vectors are coplanar using the scalar triple product?
2. (a) Show that if $\mathbf{u}$ and $\mathbf{v}$ are vectors of equal length, then $\mathbf{u} + \mathbf{v}$ and $\mathbf{u} - \mathbf{v}$ are orthogonal.  
   (b) Show that four points $A, B, C,$ and $D$ in 3-space lie in the same plane if and only if $\vec{AB} \cdot (\vec{AC} \times \vec{AD}) = 0$.  
   (c) Find a vector force $\mathbf{F}$ that cancels the resultant of the forces $\mathbf{F}_1 = 2\mathbf{i} + 3\mathbf{j}$ and $\mathbf{F}_2 = -\mathbf{i} + 4\mathbf{j}$.  
   (d) Find an equation of the sphere centered at $(1, -2, 2)$ that passes through the origin.
3. (a) Sketch a diagram showing the direction angles $\alpha, \beta, \gamma$ of a vector $\mathbf{v}$ in 3-space.  
   (b) Find a unit vector in 2-space that makes an angle of $120^\circ$ with the positive $x$-axis.  
   (c) Show that the triangle with vertices $A(1, 1, 1), B(2, 4, 3),$ and $C(3, 2, 5)$ is an acute triangle.  
   (d) If $\mathbf{u}$ and $\mathbf{v}$ are orthogonal unit vectors, find $\|\mathbf{u} \times \mathbf{v}\|$.
4. (a) Construct a multiplication table for the cross products of the standard unit basis vectors $\mathbf{i}, \mathbf{j}, \mathbf{k}$.  
   (b) State the geometric interpretation of the magnitude of the cross product $\|\mathbf{u} \times \mathbf{v}\|$.  
   (c) State the geometric interpretation of the absolute value of the scalar triple product $|\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})|$.  
   (d) Find an equation of the plane that passes through the origin and is perpendicular to the line $x = 1 + 2t, y = 3 - t, z = 4 + 3t$.
5. Find an equation of the sphere with center $(-3, 5, -4)$ that is tangent to:  
   (a) the $xy$-plane  
   (b) the $xz$-plane  
   (c) the $yz$-plane.
6. Find the largest and smallest distances from the point $(1, 1, 1)$ to the sphere $x^2 + y^2 + z^2 - 2y + 6z - 6 = 0$.
7. Find the coordinates of the fourth vertex of the parallelogram that has three of its vertices at $P(3, 4), Q(1, 1),$ and $R(5, 2)$. *[Note: There is more than one answer.]*
8. Let $\mathbf{u} = \langle 3, 5, -1 \rangle$ and $\mathbf{v} = \langle 2, -2, 3 \rangle$. Find:  
   (a) $2\mathbf{u} + 5\mathbf{v}$  
   (b) a unit vector in the direction of $\mathbf{v}$  
   (c) $\|\mathbf{u}\|$  
   (d) $\|\mathbf{u} - \mathbf{v}\|$.
9. Let $\mathbf{a} = c\mathbf{i} + \mathbf{j}$ and $\mathbf{b} = 4\mathbf{i} + 3\mathbf{j}$. Find the value(s) of $c$ such that:  
   (a) $\mathbf{a}$ and $\mathbf{b}$ are orthogonal;  
   (b) the angle between $\mathbf{a}$ and $\mathbf{b}$ is $\pi/4$;  
   (c) the angle between $\mathbf{a}$ and $\mathbf{b}$ is $\pi/6$;  
   (d) $\mathbf{a}$ and $\mathbf{b}$ are parallel.
10. Let $\mathbf{r}_0 = \langle x_0, y_0, z_0 \rangle$ be a fixed nonzero vector and let $\mathbf{r} = \langle x, y, z \rangle$. Describe the set of points $(x, y, z)$ that satisfy:  
    (a) $\mathbf{r} \cdot \mathbf{r}_0 = 0$  
    (b) $(\mathbf{r} - \mathbf{r}_0) \cdot \mathbf{r}_0 = 0$.
11. Show that if $\mathbf{u}$ and $\mathbf{v}$ are unit vectors and $\theta$ is the angle between them, then
    $$\|\mathbf{u} - \mathbf{v}\| = 2\sin\left(\frac{\theta}{2}\right)$$
12. Find a vector of length 5 that has direction angles $\alpha = 60^\circ, \beta = 120^\circ,$ and $\gamma = 135^\circ$, or explain why no such vector exists.
13. Find the work done by a constant force $\mathbf{F} = 3\mathbf{i} - 4\mathbf{j} + \mathbf{k}\text{ lb}$ applied to an object that moves along a straight line from $P(5, 7, 0)$ to $Q(6, 6, 6)$, where distance is in feet.
14. Two forces $\mathbf{F}_1 = 2\mathbf{i} - \mathbf{j} + 3\mathbf{k}\text{ N}$ and $\mathbf{F}_2 = 3\mathbf{i} + 2\mathbf{j} - \mathbf{k}\text{ N}$ act on a particle as it moves along a straight line from $P(-1, -2, 3)$ to $Q(0, 2, 0)$, where distance is in meters. Find the total work done by the resultant force.
15. (a) Find the area of the triangle with vertices $A(1, 0, 1), B(0, 2, 3),$ and $C(2, 1, 0)$.  
    (b) Find the length of the altitude from vertex $C$ to the side $AB$.
16. Determine whether each statement is true or false for all vectors $\mathbf{u}, \mathbf{v},$ and $\mathbf{w}$ in 3-space:  
    (a) If $\mathbf{u} \cdot \mathbf{v} = 0$ and $\mathbf{u} \times \mathbf{v} = \mathbf{0}$, then either $\mathbf{u} = \mathbf{0}$ or $\mathbf{v} = \mathbf{0}$.  
    (b) If $\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{w}$ and $\mathbf{u} \neq \mathbf{0}$, then $\mathbf{v} = \mathbf{w}$.  
    (c) If $\mathbf{u} \times \mathbf{v} = \mathbf{u} \times \mathbf{w}$ and $\mathbf{u} \neq \mathbf{0}$, then $\mathbf{v} = \mathbf{w}$.  
    (d) If $\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{w}$ and $\mathbf{u} \times \mathbf{v} = \mathbf{u} \times \mathbf{w}$ with $\mathbf{u} \neq \mathbf{0}$, then $\mathbf{v} = \mathbf{w}$.
17. Let $A(1, 1, 1), B(2, 3, 4), C(6, 5, 2),$ and $D(7, 7, 5)$ be vertices of a parallelepiped.  
    (a) Find the volume of the parallelepiped.  
    (b) Find the distance from vertex $D$ to the plane containing $A, B,$ and $C$.
18. A force $\mathbf{F}$ of magnitude $9\text{ lb}$ acts on a lever as shown in Figure Ex-18.  
    (a) Express the force $\mathbf{F}$ in component form.  
    (b) Find the vector moment of $\mathbf{F}$ about the origin.  
    (c) Find the scalar moment of $\mathbf{F}$ about the origin.
19. Find parametric equations of the line that passes through $(4, 1, 2)$ and is parallel to the vector $\langle 1, -1, 0 \rangle$.
20. Let $P_1$ and $P_2$ be the planes $2x + y - z = 3$ and $x + 2y + z = 3$.  
    (a) Find parametric equations for the line of intersection of $P_1$ and $P_2$.  
    (b) Find the acute angle between $P_1$ and $P_2$ to the nearest degree.
21. Find an equation of the plane that passes through $(1, 1, 4)$ and is parallel to the plane $x + 5y - z + 8 = 0$.
22. Find an equation of the plane that passes through $(4, 3, 0)$ and is parallel to the vectors $\mathbf{v}_1 = \mathbf{i} + \mathbf{k}$ and $\mathbf{v}_2 = 2\mathbf{j} - \mathbf{k}$.
23. Prove that the planes $a_1 x + b_1 y + c_1 z + d_1 = 0$ and $a_2 x + b_2 y + c_2 z + d_2 = 0$ are perpendicular if and only if $a_1 a_2 + b_1 b_2 + c_1 c_2 = 0$.
24. (a) Describe the traces of the quadric surface $x^2 - y^2 + z^2 = 1$ in the coordinate planes.  
    (b) Find the reflection of the point $(2, -3, 5)$ about the origin.  
    (c) Describe the curve of intersection of the cylinder $r = 2$ and the sphere $\rho = 4$.
25. Identify the following quadric surfaces by completing the square:  
    (a) $x^2 + 2y^2 - 4z^2 - 4x + 4y + 8z - 4 = 0$  
    (b) $z = 2x^2 + y^2 - 4x + 2y + 5$.
26. Express the rectangular equation in (i) cylindrical coordinates and (ii) spherical coordinates:  
    (a) $x^2 + y^2 + z^2 = 9$  
    (b) $x^2 + y^2 = 2z$  
    (c) $x^2 + y^2 - z^2 = 0$.
27. Express the following equations in rectangular coordinates and identify the surface:  
    (a) $r = 2\cos\theta$  
    (b) $\rho = 4\sec\phi$  
    (c) $\rho = 2\sin\phi\cos\theta$.
28. Describe the solid region defined by $0 \le r \le 3, 0 \le \theta \le \pi, 0 \le z \le 5$ in cylindrical coordinates.
29. Describe the solid region defined by $0 \le \rho \le 4, 0 \le \theta \le 2\pi, 0 \le \phi \le \pi/3$ in spherical coordinates.
30. Describe the solid region defined by $1 \le r \le 2, 0 \le \theta \le 2\pi, r^2 \le z \le 4$ in cylindrical coordinates.
31. Describe the solid region defined by $2 \le \rho \le 4, 0 \le \theta \le 2\pi, \pi/6 \le \phi \le \pi/2$ in spherical coordinates.
32. The surface $\rho = a(1 - \cos\phi)$ in spherical coordinates ($a > 0$) resembles an apple (cardioid of revolution).  
    (a) Show that the surface is symmetric about the $z$-axis.  
    (b) Find the distance from the origin to the top ($z > 0$) and bottom ($z < 0$) of the surface.

---

## CHAPTER 11 MAKING CONNECTIONS

1. **Rotation Operator in 2-Space.** Let $R$ be the operator that rotates each vector in 2-space counterclockwise through an angle of $90^\circ$.  
   (a) Show that $R(x\mathbf{i} + y\mathbf{j}) = -y\mathbf{i} + x\mathbf{j}$.  
   (b) Show that $R$ is linear; that is, $R(\mathbf{u} + \mathbf{v}) = R(\mathbf{u}) + R(\mathbf{v})$ and $R(c\mathbf{u}) = cR(\mathbf{u})$ for any scalar $c$.  
   (c) Show that $\mathbf{u} \cdot R(\mathbf{u}) = 0$ for all $\mathbf{u}$.  
   (d) Show that $\|R(\mathbf{u})\| = \|\mathbf{u}\|$ for all $\mathbf{u}$.
2. **Polygon Normal Vector Sum.**  
   (a) Let $T$ be a triangle in 2-space with edge vectors $\mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3$ directed counterclockwise around the boundary, and let $\mathbf{n}_1, \mathbf{n}_2, \mathbf{n}_3$ be outward normal vectors whose lengths equal the lengths of the corresponding sides. Prove that
   $$\mathbf{n}_1 + \mathbf{n}_2 + \mathbf{n}_3 = \mathbf{0}$$  
   (b) Generalize the result in part (a) to an arbitrary convex $n$-sided polygon.
3. **Polyhedron Outward Normal Theorem.**  
   (a) Let $T$ be a tetrahedron in 3-space with triangular faces $F_1, F_2, F_3, F_4$. For each face $F_k$, let $\mathbf{N}_k$ denote the outward normal vector to $F_k$ whose length is equal to the area of $F_k$. Prove that
   $$\mathbf{N}_1 + \mathbf{N}_2 + \mathbf{N}_3 + \mathbf{N}_4 = \mathbf{0}$$  
   *[Hint: Express each outward normal vector as a cross product of edge vectors.]*  
   (b) Generalize the result in part (a) to any convex polyhedron in 3-space.
4. **Law of Cosines and Pythagorean Theorem for Tetrahedra.**  
   (a) Let a tetrahedron have three mutually perpendicular faces meeting at a vertex $O$ with areas $A_1, A_2, A_3$, and let the fourth opposite face have area $A$. Use the result of Exercise 3 to prove that
   $$A^2 = A_1^2 + A_2^2 + A_3^2$$
   This is known as **de Gua's theorem** (the 3D Pythagorean theorem for tetrahedra).  
   (b) For an arbitrary tetrahedron with face areas $A_1, A_2, A_3, A_4$ and dihedral angles $\theta_{ij}$ between faces $F_i$ and $F_j$, use Exercise 3 to prove the **Law of Cosines for Tetrahedra**:
   $$A_4^2 = A_1^2 + A_2^2 + A_3^2 - 2A_1 A_2\cos\theta_{12} - 2A_2 A_3\cos\theta_{23} - 2A_1 A_3\cos\theta_{13}$$
5. **Great Circle Distance on a Sphere.**  
   Let $P_1(\rho, \theta_1, \phi_1)$ and $P_2(\rho, \theta_2, \phi_2)$ be two points on a sphere of radius $\rho$ centered at the origin.  
   (a) Convert $P_1$ and $P_2$ to rectangular coordinates and compute $\vec{OP_1} \cdot \vec{OP_2}$.  
   (b) Show that the angle $\gamma$ between $\vec{OP_1}$ and $\vec{OP_2}$ satisfies
   $$\cos\gamma = \cos\phi_1\cos\phi_2 + \cos(\theta_1 - \theta_2)\sin\phi_1\sin\phi_2$$  
   (c) Show that the great-circle distance $d$ along the sphere between $P_1$ and $P_2$ is
   $$d = \rho\cos^{-1}\left(\cos\phi_1\cos\phi_2 + \cos(\theta_1 - \theta_2)\sin\phi_1\sin\phi_2\right)$$
6. **Great Circle Navigation Application.**  
   Use the great-circle distance formula from Exercise 5 to find the shortest distance along the Earth's surface between:  
   * Point $A$: Latitude $40^\circ\text{ N}$, Longitude $60^\circ\text{ W}$  
   * Point $B$: Latitude $20^\circ\text{ N}$, Longitude $40^\circ\text{ W}$  
   Assume the Earth is a sphere of radius $R = 6370\text{ km}$. Convert latitudes and longitudes to spherical angles $(\phi, \theta)$ and compute $d$ to the nearest kilometer.

