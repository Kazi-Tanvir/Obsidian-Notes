# CHAPTER 13: PARTIAL DERIVATIVES

> Three-dimensional surfaces have high points and low points that are analogous to the peaks and valleys of a mountain range. In this chapter we will use derivatives to locate these points and to study other features of such surfaces.

In this chapter we extend the calculus of one variable to functions of several variables ($z = f(x, y)$ or $w = f(x, y, z)$). We cover limits and continuity in multiple dimensions, partial derivatives, differentiability, total differentials, local linear approximations, chain rules, directional derivatives, gradients, tangent planes and normal lines, optimization (relative and absolute extrema, second partials test), and constrained optimization using Lagrange multipliers.

---

## 13.1 FUNCTIONS OF TWO OR MORE VARIABLES

### NOTATION, DOMAINS, AND GRAPHS
* **Functions of Two Variables:** $z = f(x, y)$ maps a point $(x, y) \in D \subseteq \mathbb{R}^2$ to a unique real value $z$. The graph is a surface in 3-space.
* **Natural Domain:** The largest set in the plane (or space) for which the formula produces real values.
* **Level Curves & Contour Maps:** The set of points $(x, y)$ satisfying $f(x, y) = k$. Projecting these horizontal traces onto the $xy$-plane forms a **contour map**.
* **Level Surfaces:** For $w = f(x, y, z)$, the set of points $(x, y, z)$ satisfying $f(x, y, z) = k$ forms a level surface in 3-space.

---

### QUICK CHECK EXERCISES 13.1
*(See page 917 for answers.)*
1. Domain of $\ln(xy)$ is points in 1st or 3rd quadrants ($xy > 0$); domain of $\ln x + \ln y$ is 1st quadrant ($x>0, y>0$).
2. For $f(x, y) = \frac{x-y}{x+y+1}$: (a) $f(2, 1) = 1/4$; (b) $f(1, 2) = -1/4$; (c) $f(a, a) = 0$; (d) $f(y+1, y) = \frac{1}{2y+2}$.
3. For $e^{x+y}$: (a) $k > 0$; (b) Parallel lines $x + y = \ln k$.
4. For $\frac{1}{x^2+y^2+z^2+1}$: (a) $0 < k \le 1$; (b) Spheres of radius $\sqrt{\frac{1-k}{k}}$ for $0 < k < 1$, single point $(0, 0, 0)$ for $k=1$.

---

## 13.2 LIMITS AND CONTINUITY

### LIMITS ALONG CURVES & GENERAL LIMITS

> **13.2.1 DEFINITION (General Limit in 2-Space)**
> $\lim_{(x, y) \to (x_0, y_0)} f(x, y) = L$ if for every $\epsilon > 0$, there exists $\delta > 0$ such that:
> $$|f(x, y) - L| < \epsilon \quad \text{whenever } 0 < \sqrt{(x - x_0)^2 + (y - y_0)^2} < \delta$$

* **Two-Path Test for Nonexistence of Limit (Theorem 13.2.2):**
  If $f(x, y)$ approaches different limits along two different paths as $(x, y) \to (x_0, y_0)$, or fails to have a limit along any path, then $\lim_{(x, y) \to (x_0, y_0)} f(x, y)$ does not exist.

### CONTINUITY (13.2.3)
$f(x, y)$ is continuous at $(x_0, y_0)$ if $\lim_{(x, y) \to (x_0, y_0)} f(x, y) = f(x_0, y_0)$.
* Polynomials and rational functions are continuous on their domains.
* Converting to polar coordinates ($x = r\cos\theta, y = r\sin\theta, r \to 0^+$) is often helpful to evaluate indeterminate limits at the origin.

---

### QUICK CHECK EXERCISES 13.2
*(See page 927 for answers.)*
1. For $f(x, y) = \frac{x^2 - y^2}{x^2 + y^2}$ as $(x, y) \to (0, 0)$: (a) along $x=0$: $-1$; (b) along $y=0$: $1$; (c) along $y=x$: $0$; (d) along $y=x^2$: $1$.
2. (a) 3; (b) 1; (c) 0.
3. $f(x_0, y_0)$; $(x_0, y_0)$.
4. $a \le 0$.

---

## 13.3 PARTIAL DERIVATIVES

### DEFINITIONS & NOTATION (13.3.1)
$$f_x(x_0, y_0) = \frac{\partial f}{\partial x}\Big|_{(x_0, y_0)} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x}$$
$$f_y(x_0, y_0) = \frac{\partial f}{\partial y}\Big|_{(x_0, y_0)} = \lim_{\Delta y \to 0} \frac{f(x_0, y_0 + \Delta y) - f(x_0, y_0)}{\Delta y}$$
* **Geometric Interpretation:** $f_x(x_0, y_0)$ is the slope of the surface in the $x$-direction (tangent to curve $C_1$ formed by slicing with $y = y_0$), and $f_y(x_0, y_0)$ is the slope in the $y$-direction.

### HIGHER-ORDER & MIXED PARTIALS
* $f_{xx} = \frac{\partial^2 f}{\partial x^2}, \quad f_{yy} = \frac{\partial^2 f}{\partial y^2}, \quad f_{xy} = \frac{\partial^2 f}{\partial y \partial x}, \quad f_{yx} = \frac{\partial^2 f}{\partial x \partial y}$

> **13.3.2 THEOREM (Clairaut's Theorem / Equality of Mixed Partials)**
> If $f_{xy}$ and $f_{yx}$ are continuous on an open disk, then:
> $$f_{xy} = f_{yx}$$

* **The 1D Wave Equation:** $\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$
* **Laplace's Equation:** $\frac{\partial^2 z}{\partial x^2} + \frac{\partial^2 z}{\partial y^2} = 0$

---

### QUICK CHECK EXERCISES 13.3
*(See page 940 for answers.)*
1. $f_x = \sin xy + xy\cos xy$; $f_y = x^2\cos xy$.
2. Slope in $x$-dir is 9; in $y$-dir is 12.
3. For $V = \frac{1}{3}\pi r^2 h$: (a) $\frac{\partial V}{\partial r} = \frac{2}{3}\pi rh$; (b) $\frac{\partial V}{\partial h} = \frac{1}{3}\pi r^2$.
4. $f_{xx} = 2y^3, f_{yy} = 6x^2 y, f_{xy} = f_{yx} = 6xy^2$.

---

## 13.4 DIFFERENTIABILITY, DIFFERENTIALS, AND LOCAL LINEARITY

### DEFINITION OF DIFFERENTIABILITY

> **13.4.1 DEFINITION**
> $f(x, y)$ is **differentiable** at $(x_0, y_0)$ if $f_x(x_0, y_0)$ and $f_y(x_0, y_0)$ exist and:
> $$\lim_{(\Delta x, \Delta y) \to (0, 0)} \frac{\Delta f - f_x(x_0, y_0)\Delta x - f_y(x_0, y_0)\Delta y}{\sqrt{(\Delta x)^2 + (\Delta y)^2}} = 0 \tag{4}$$
> Or equivalently: $\Delta f = f_x \Delta x + f_y \Delta y + \epsilon \sqrt{(\Delta x)^2 + (\Delta y)^2}$, where $\epsilon \to 0$.

* **Theorem 13.4.3:** Differentiability $\implies$ Continuity. (Converse is false, e.g. $z = \sqrt{x^2+y^2}$ at $(0, 0)$).
* **Theorem 13.4.4:** If $f_x$ and $f_y$ exist and are continuous on an open region, then $f$ is differentiable on that region.

---

### TOTAL DIFFERENTIAL & LOCAL LINEAR APPROXIMATION
* **Total Differential:**
  $$dz = f_x(x, y)dx + f_y(x, y)dy \tag{10}$$
  $$dw = f_x dx + f_y dy + f_z dz \tag{11}$$
* **Local Linear Approximation $L(x, y)$:**
  $$L(x, y) = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) \tag{15}$$
  *(The graph of $z = L(x, y)$ is the tangent plane to the surface at $(x_0, y_0)$).*

---

### QUICK CHECK EXERCISES 13.4
*(See page 949 for answers.)*
1. (a) $f_x(x_0, y_0)\Delta x + f_y(x_0, y_0)\Delta y$; (b) Limit in Eq. (4) is 0.
2. (a) $dz = e^{y^2}dx + 2xy e^{y^2}dy$; (b) $dw = \sin(yz)dx + xz\cos(yz)dy + xy\cos(yz)dz$.
3. $L(x, y) = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$.
4. $f(0.9, -1.95) \approx 4 + 2(-0.1) - 3(0.05) = 3.65$.

---

## 13.5 THE CHAIN RULE

### CHAIN RULES FOR FUNCTIONS OF SEVERAL VARIABLES

> **13.5.1 THEOREM (One Independent Parameter $t$)**
> If $z = f(x, y)$ where $x = x(t), y = y(t)$:
> $$\frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt} \tag{5}$$
> If $w = f(x, y, z)$ where $x = x(t), y = y(t), z = z(t)$:
> $$\frac{dw}{dt} = \frac{\partial w}{\partial x}\frac{dx}{dt} + \frac{\partial w}{\partial y}\frac{dy}{dt} + \frac{\partial w}{\partial z}\frac{dz}{dt} \tag{6}$$

> **13.5.2 THEOREM (Two Independent Parameters $u, v$)**
> If $z = f(x, y)$ with $x = x(u, v), y = y(u, v)$:
> $$\frac{\partial z}{\partial u} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial u} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial u}, \quad \frac{\partial z}{\partial v} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial v} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial v} \tag{7–8}$$

---

### IMPLICIT DIFFERENTIATION FORMULAS
* For $f(x, y) = c$ (Theorem 13.5.3):
  $$\frac{dy}{dx} = -\frac{\partial f/\partial x}{\partial f/\partial y} = -\frac{f_x}{f_y} \tag{14}$$
* For $F(x, y, z) = c$ (Theorem 13.5.4):
  $$\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}, \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z} \tag{17}$$

---

### QUICK CHECK EXERCISES 13.5
*(See page 959 for answers.)*
1. $\frac{dz}{dt} = y^2 \frac{dx}{dt} + 2xy \frac{dy}{dt} = 1(-2) + 2(1)(-1)(3) = -8$.
2. Slope $m = -\frac{f_x}{f_y} = -\frac{3}{-1} = 3$.
3. $\frac{dA}{dt} = w\frac{dl}{dt} + l\frac{dw}{dt} = 2(3) + 5(4) = 26\text{ ft}^2/\text{s}$.
4. $\frac{\partial z}{\partial u} = 1, \; \frac{\partial z}{\partial v} = 1$.

---

## 13.6 DIRECTIONAL DERIVATIVES AND GRADIENTS

### DIRECTIONAL DERIVATIVES & THE GRADIENT

> **13.6.1 & 13.6.4 DEFINITIONS**
> For unit vector $\mathbf{u} = \langle u_1, u_2 \rangle$:
> $$D_\mathbf{u} f(x_0, y_0) = \lim_{s \to 0} \frac{f(x_0 + s u_1, y_0 + s u_2) - f(x_0, y_0)}{s} = \nabla f(x_0, y_0) \cdot \mathbf{u} \tag{2, 10}$$
> * **Gradient Vector:**
>   $$\nabla f(x, y) = f_x(x, y)\mathbf{i} + f_y(x, y)\mathbf{j} = \langle f_x, f_y \rangle$$
>   $$\nabla f(x, y, z) = f_x\mathbf{i} + f_y\mathbf{j} + f_z\mathbf{k} = \langle f_x, f_y, f_z \rangle$$

---

### PROPERTIES OF THE GRADIENT (Theorem 13.6.5)
Since $D_\mathbf{u} f = \nabla f \cdot \mathbf{u} = \|\nabla f\|\cos\theta$:
1. $f$ increases **most rapidly** in the direction of $\nabla f$, with maximum rate of increase $\|\nabla f\|$.
2. $f$ decreases **most rapidly** in the direction of $-\nabla f$, with minimum rate of change $-\|\nabla f\|$.
3. $D_\mathbf{u} f = 0$ in directions orthogonal to $\nabla f$ ($\theta = \pi/2$).
4. **Theorem 13.6.6:** $\nabla f(x_0, y_0)$ is perpendicular (normal) to the level curve $f(x, y) = c$ at $(x_0, y_0)$.

---

### QUICK CHECK EXERCISES 13.6
*(See page 971 for answers.)*
1. $\nabla f(1, 1, 1) = \langle y^2 z^3, 2xyz^3, 3xy^2 z^2 \rangle|_{(1,1,1)} = \langle 1, 2, 3 \rangle$.
2. $D_\mathbf{u}f(2, 1) = \frac{d}{ds}[3se^s]|_{s=0} = 3$.
3. Directional derivative along $\mathbf{a} = 3\mathbf{i}+4\mathbf{j}$ ($\mathbf{u} = \frac{3}{5}\mathbf{i}+\frac{4}{5}\mathbf{j}$): $\nabla f \cdot \mathbf{u} = 6(3/5)+8(4/5) = 10$. Tangent slope to level curve: $-f_x/f_y = -6/8 = -3/4$.
4. Max directional derivative is $\|\nabla f\| = \sqrt{4+4+1} = 3$; Min is $-3$.

---

## 13.7 TANGENT PLANES AND NORMAL VECTORS

### TANGENT PLANES TO SURFACES

* **Level Surface $F(x, y, z) = c$ (Definition 13.7.1):**
  * Normal vector: $\mathbf{n} = \nabla F(x_0, y_0, z_0) = \langle F_x, F_y, F_z \rangle$.
  * **Tangent Plane:**
    $$F_x(x_0, y_0, z_0)(x - x_0) + F_y(x_0, y_0, z_0)(y - y_0) + F_z(x_0, y_0, z_0)(z - z_0) = 0 \tag{3}$$
  * **Normal Line:**
    $$x = x_0 + F_x t, \quad y = y_0 + F_y t, \quad z = z_0 + F_z t \tag{4}$$
* **Explicit Surface $z = f(x, y)$ (Theorem 13.7.2):**
  $$z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0) \tag{5}$$
* **Tangent Line to Intersection of Two Surfaces $F=0, G=0$:**
  $$\mathbf{T} \parallel \nabla F(x_0, y_0, z_0) \times \nabla G(x_0, y_0, z_0)$$

---

### QUICK CHECK EXERCISES 13.7
*(See page 977 for answers.)*
1. Tangent plane: $2(x-1) + y + (z+1) = 0 \implies 2x+y+z=1$. Normal line: $x=1+2t, y=t, z=-1+t$.
2. Tangent plane: $z = 4 + 2(x-3) - 3(y-1)$. Normal line: $x=3+2t, y=1-3t, z=4-t$.
3. For $z = x^2\sqrt{y}$ at $(2, 4, 8)$: Tangent plane: $z = 8 + 8(x-2) + (y-4)$. Normal line: $x=2+8t, y=4+t, z=8-t$.
4. Tangent line to circle: $x = 2+t, y = 1, z = 2-t$.

---

## 13.8 MAXIMA AND MINIMA OF FUNCTIONS OF TWO VARIABLES

### CRITICAL POINTS & EXTREME-VALUE THEOREM
* **Critical Points (13.8.5):** Points $(x_0, y_0)$ where $f_x = 0$ and $f_y = 0$, or where at least one partial derivative does not exist.
* **Extreme-Value Theorem (13.8.3):** A continuous function $f(x, y)$ on a **closed and bounded** set $R$ achieves both an absolute maximum and an absolute minimum on $R$.

---

### SECOND PARTIALS TEST

> **13.8.6 THEOREM (The Second Partials Test)**
> Let $(x_0, y_0)$ be a critical point of $f(x, y)$, and define the discriminant:
> $$D = f_{xx}(x_0, y_0)f_{yy}(x_0, y_0) - [f_{xy}(x_0, y_0)]^2$$
> 1. If $D > 0$ and $f_{xx}(x_0, y_0) > 0 \implies$ **Relative Minimum** at $(x_0, y_0)$.
> 2. If $D > 0$ and $f_{xx}(x_0, y_0) < 0 \implies$ **Relative Maximum** at $(x_0, y_0)$.
> 3. If $D < 0 \implies$ **Saddle Point** at $(x_0, y_0)$.
> 4. If $D = 0 \implies$ **Inconclusive** (test fails).

---

### ABSOLUTE EXTREMA ON CLOSED AND BOUNDED SETS
1. Find all critical points in the interior of $R$ and evaluate $f$.
2. Find all potential extreme points on the boundary of $R$ (by parametrizing the boundary segments).
3. The largest of these values is the absolute maximum, and the smallest is the absolute minimum.

---

### QUICK CHECK EXERCISES 13.8
*(See page 989 for answers.)*
1. Critical points of $x^3 + xy + y^2$: $(0, 0)$ and $(1/6, -1/12)$.
2. (a) $D = 4 - 4 = 0$ (Inconclusive); (b) $D = -4 - 4 = -8 < 0$ (Saddle point); (c) $D = 6 - 4 = 2 > 0, f_{xx} = 3 > 0$ (Relative min); (d) $D = 6 - 4 = 2 > 0, f_{xx} = -3 < 0$ (Relative max).
3. For $x^3 - 3xy + y^3$: (a) $(0, 0)$ is a saddle point; (b) $(-1, -1)$ not a critical point; (c) $(1, 1)$ is a relative minimum.
4. $V = \frac{xy(1-xy)}{x+y}$.

---

## 13.9 LAGRANGE MULTIPLIERS

### CONSTRAINED EXTREMA (ONE CONSTRAINT)

> **13.9.3 & 13.9.4 THEOREMS**
> To maximize/minimize $f(x, y)$ or $f(x, y, z)$ subject to constraint $g(x, y) = 0$ or $g(x, y, z) = 0$:
> Find all values of $x, y, z$ and scalar $\lambda$ (Lagrange multiplier) satisfying:
> $$\nabla f = \lambda \nabla g \quad \text{and} \quad g = 0$$

#### Example 1
Maximize $f(x, y) = xy$ subject to $x^2 + y^2 = 1$:
* $\nabla f = \langle y, x \rangle, \quad \nabla g = \langle 2x, 2y \rangle \implies y = 2\lambda x, \; x = 2\lambda y \implies y^2 = x^2$.
* $2x^2 = 1 \implies x = \pm 1/\sqrt{2}, \; y = \pm 1/\sqrt{2}$.
* Max value is $1/2$ at $(1/\sqrt{2}, 1/\sqrt{2})$ and $(-1/\sqrt{2}, -1/\sqrt{2})$.
* Min value is $-1/2$ at $(1/\sqrt{2}, -1/\sqrt{2})$ and $(-1/\sqrt{2}, 1/\sqrt{2})$.

---

### QUICK CHECK EXERCISES 13.9
*(See page 997 for answers.)*
1. (a) They are the same line; (b) They are the same plane.
2. Max of $x+y$ on $x^2+y^2=1$ is $\sqrt{2}$.
3. Max of $x+y+z$ on $x^2+y^2+z^2=1$ is $\sqrt{3}$.
4. Max is 3 (at $(0, 1)$); Min is 2 (at $(1, 0)$).

---

## CHAPTER 13 MAKING CONNECTIONS: EULER'S HOMOGENEOUS FUNCTION THEOREM

> **Euler's Theorem for Homogeneous Functions:**
> If $f(x, y)$ is homogeneous of degree $n$ (meaning $f(tx, ty) = t^n f(x, y)$ for $t > 0$), then:
> $$x\frac{\partial f}{\partial x} + y\frac{\partial f}{\partial y} = n f(x, y)$$
