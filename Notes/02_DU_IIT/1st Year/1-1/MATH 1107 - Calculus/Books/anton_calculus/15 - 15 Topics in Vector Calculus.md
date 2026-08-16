# CHAPTER 15: TOPICS IN VECTOR CALCULUS

> Results in this chapter provide tools for analyzing and understanding the behavior of hurricanes and other fluid flows.

The main theme of this chapter is the concept of a "flow." The body of mathematics that we will study here is concerned with analyzing flows of various types—the flow of a fluid or the flow of electricity, for example. Indeed, the early writings of Isaac Newton on calculus are replete with such nouns as "fluxion" and "fluent," which are rooted in the Latin *fluere* (to flow). We will begin this chapter by introducing the concept of a vector field, which is the mathematical description of a flow. In subsequent sections, we will introduce two new kinds of integrals that are used in a variety of applications to analyze properties of vector fields and flows. Finally, we conclude with three major theorems, Green's Theorem, the Divergence Theorem, and Stokes' Theorem. These theorems provide a deep insight into the nature of flows and are the basis for many of the most important principles in physics and engineering.

---

## 15.1 VECTOR FIELDS

In this section we will consider functions that associate vectors with points in 2-space or 3-space. We will see that such functions play an important role in the study of fluid flow, gravitational force fields, electromagnetic force fields, and a wide range of other applied problems.

### VECTOR FIELDS DEFINITION

> **15.1.1 DEFINITION**
> A **vector field in a plane** is a function that associates with each point $P$ in the plane a unique vector $\mathbf{F}(P)$ parallel to the plane. Similarly, a **vector field in 3-space** is a function that associates with each point $P$ in 3-space a unique vector $\mathbf{F}(P)$ in 3-space.

In coordinate systems:
* In 2-space ($xy$-plane):
  $$\mathbf{F}(x, y) = f(x, y)\mathbf{i} + g(x, y)\mathbf{j}$$
* In 3-space ($xyz$-coordinate system):
  $$\mathbf{F}(x, y, z) = f(x, y, z)\mathbf{i} + g(x, y, z)\mathbf{j} + h(x, y, z)\mathbf{k}$$

### GRAPHICAL REPRESENTATIONS OF VECTOR FIELDS
A vector field in 2-space or 3-space can be visualized geometrically by drawing representative field vectors $\mathbf{F}(x, y)$ or $\mathbf{F}(x, y, z)$ at selected points.
* Compact notation: $\mathbf{r} = x\mathbf{i} + y\mathbf{j}$ or $\mathbf{r} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$, writing the field as $\mathbf{F}(\mathbf{r})$ or simply $\mathbf{F}$.

---

### INVERSE-SQUARE FIELDS

According to Newton's Law of Universal Gravitation, particles with masses $m$ and $M$ attract each other with a force $\mathbf{F}$ of magnitude:
$$\|\mathbf{F}\| = \frac{GmM}{r^2} \tag{1}$$
If mass $M$ is at the origin and $\mathbf{r}$ is the radius vector to mass $m$, the force is directed along $-\mathbf{r}/\|\mathbf{r}\|$:
$$\mathbf{F}(\mathbf{r}) = -\frac{GmM}{\|\mathbf{r}\|^2}\frac{\mathbf{r}}{\|\mathbf{r}\|} = -\frac{GmM}{\|\mathbf{r}\|^3}\mathbf{r} \tag{2}$$

> **15.1.2 DEFINITION**
> If $\mathbf{r}$ is a radius vector in 2-space or 3-space, and if $c$ is a constant, then a vector field of the form
> $$\mathbf{F}(\mathbf{r}) = \frac{c}{\|\mathbf{r}\|^3}\mathbf{r} \tag{3}$$
> is called an **inverse-square field**.

* In 2-space:
  $$\mathbf{F}(x, y) = \frac{c}{(x^2 + y^2)^{3/2}}(x\mathbf{i} + y\mathbf{j}) \tag{4}$$
* In 3-space:
  $$\mathbf{F}(x, y, z) = \frac{c}{(x^2 + y^2 + z^2)^{3/2}}(x\mathbf{i} + y\mathbf{j} + z\mathbf{k}) \tag{5}$$
* **Coulomb's Law (Example 1):** Electrostatic force field created by charge $Q$ on charge $q$:
  $$\mathbf{F}(\mathbf{r}) = \frac{qQ}{4\pi \epsilon_0 \|\mathbf{r}\|^3}\mathbf{r} \quad \left(c = \frac{qQ}{4\pi\epsilon_0}\right)$$

---

### GRADIENT FIELDS & CONSERVATIVE FIELDS

The **gradient field** of a differentiable scalar function $\phi$ is:
$$\nabla\phi = \frac{\partial\phi}{\partial x}\mathbf{i} + \frac{\partial\phi}{\partial y}\mathbf{j} + \frac{\partial\phi}{\partial z}\mathbf{k}$$
At each point where $\nabla\phi \neq \mathbf{0}$, the vector points in the direction of maximum rate of increase of $\phi$ and is orthogonal to the level surfaces/curves of $\phi$.

> **15.1.3 DEFINITION**
> A vector field $\mathbf{F}$ in 2-space or 3-space is said to be **conservative** in a region if it is the gradient field for some function $\phi$ in that region, that is, if
> $$\mathbf{F} = \nabla\phi$$
> The function $\phi$ is called a **potential function** for $\mathbf{F}$ in the region.

* **Example 3:** For inverse-square fields, $\phi = -\frac{c}{\|\mathbf{r}\|} = -\frac{c}{(x^2 + y^2 + z^2)^{1/2}}$ is a potential function on any region not containing the origin.

---

### DIVERGENCE AND CURL

> **15.1.4 DEFINITION (Divergence)**
> If $\mathbf{F}(x, y, z) = f(x, y, z)\mathbf{i} + g(x, y, z)\mathbf{j} + h(x, y, z)\mathbf{k}$, the **divergence** of $\mathbf{F}$ is:
> $$\text{div}\,\mathbf{F} = \frac{\partial f}{\partial x} + \frac{\partial g}{\partial y} + \frac{\partial h}{\partial z} \tag{7}$$

> **15.1.5 DEFINITION (Curl)**
> The **curl** of $\mathbf{F}$ is the vector field:
> $$\text{curl}\,\mathbf{F} = \left(\frac{\partial h}{\partial y} - \frac{\partial g}{\partial z}\right)\mathbf{i} + \left(\frac{\partial f}{\partial z} - \frac{\partial h}{\partial x}\right)\mathbf{j} + \left(\frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}\right)\mathbf{k} \tag{8}$$
> In determinant mnemonic form:
> $$\text{curl}\,\mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ f & g & h \end{vmatrix} \tag{9}$$

---

### THE $\nabla$ OPERATOR & THE LAPLACIAN $\nabla^2$

* **Del Operator:**
  $$\nabla = \frac{\partial}{\partial x}\mathbf{i} + \frac{\partial}{\partial y}\mathbf{j} + \frac{\partial}{\partial z}\mathbf{k} \tag{11}$$
* **Divergence in dot notation:** $\text{div}\,\mathbf{F} = \nabla \cdot \mathbf{F}$
* **Curl in cross notation:** $\text{curl}\,\mathbf{F} = \nabla \times \mathbf{F}$
* **Laplacian Operator:**
  $$\nabla^2 = \nabla \cdot \nabla = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} \tag{14}$$
* **Laplace's Equation:** $\nabla^2\phi = \text{div}(\nabla\phi) = 0$, or $\frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2} + \frac{\partial^2\phi}{\partial z^2} = 0$.

---

### QUICK CHECK EXERCISES 15.1
*(See page 1093 for answers.)*
1. The function $\phi(x, y, z) = xy + yz + xz$ is a potential for the vector field $\mathbf{F} = \underline{\hspace{2cm}}$.  
   **Answer:** $(y + z)\mathbf{i} + (x + z)\mathbf{j} + (x + y)\mathbf{k}$
2. The vector field $\mathbf{F}(x, y, z) = \underline{\hspace{2cm}}$, defined for $(x, y, z) \neq (0, 0, 0)$, is always directed toward the origin and is of length equal to the distance from $(x, y, z)$ to the origin.  
   **Answer:** $-\mathbf{r} = -x\mathbf{i} - y\mathbf{j} - z\mathbf{k}$
3. An inverse-square field is one that can be written in the form $\mathbf{F}(\mathbf{r}) = \underline{\hspace{2cm}}$.  
   **Answer:** $\frac{c}{\|\mathbf{r}\|^3}\mathbf{r}$
4. The vector field $\mathbf{F}(x, y, z) = yz\mathbf{i} + xy^2\mathbf{j} + yz^2\mathbf{k}$ has divergence $\underline{\hspace{2cm}}$ and curl $\underline{\hspace{2cm}}$.  
   **Answer:** $\text{div}\,\mathbf{F} = 2xy + 2yz$; $\text{curl}\,\mathbf{F} = z^2\mathbf{i} + y\mathbf{j} + (y^2 - z)\mathbf{k}$

---

## 15.2 LINE INTEGRALS

### DEFINITION OF LINE INTEGRALS WITH RESPECT TO ARC LENGTH $s$

> **15.2.1 DEFINITION**
> If $C$ is a smooth curve in 2-space or 3-space, the **line integral of $f$ with respect to $s$ along $C$** is:
> $$\int_C f(x, y)\,ds = \lim_{\max \Delta s_k \to 0} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta s_k \tag{3}$$
> $$\int_C f(x, y, z)\,ds = \lim_{\max \Delta s_k \to 0} \sum_{k=1}^n f(x_k^*, y_k^*, z_k^*)\,\Delta s_k \tag{4}$$

#### Applications & Interpretations:
* **Mass of a Thin Wire:** $M = \int_C f(x, y, z)\,ds$, where $f$ is linear mass density.
* **Arc Length:** $L = \int_C 1\,ds$.
* **Area of a Vertical Curtain/Sheet:** $A = \int_C f(x, y)\,ds$ ($f(x, y) \ge 0$).
* **Independence of Orientation:** $\int_{-C} f\,ds = \int_C f\,ds$.

#### Evaluation Formulas:
If $C$ is parametrized smoothly by $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$ ($a \le t \le b$):
$$\int_C f(x, y, z)\,ds = \int_a^b f(x(t), y(t), z(t)) \|\mathbf{r}'(t)\|\,dt = \int_a^b f(x(t), y(t), z(t)) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}\,dt \tag{10, 12}$$

---

### LINE INTEGRALS WITH RESPECT TO $x, y, \text{ AND } z$

$$\int_C f(x, y)\,dx = \lim_{\max \Delta s_k \to 0}\sum_{k=1}^n f(x_k^*, y_k^*)\Delta x_k, \quad \int_C f(x, y)\,dy = \lim_{\max \Delta s_k \to 0}\sum_{k=1}^n f(x_k^*, y_k^*)\Delta y_k \tag{16–17}$$

* **Reversal of Orientation:** Reversing the curve direction negates the integral:
  $$\int_{-C} f\,dx = -\int_C f\,dx, \quad \int_{-C} g\,dy = -\int_C g\,dy \tag{18–19}$$
* **Evaluation:**
  $$\int_C f(x, y)\,dx + g(x, y)\,dy = \int_a^b \left[ f(x(t), y(t))x'(t) + g(x(t), y(t))y'(t) \right] dt \tag{23}$$

---

### INTEGRATING A VECTOR FIELD ALONG A CURVE; WORK

> **15.2.2 & 15.2.3 DEFINITIONS**
> For vector field $\mathbf{F}$ and smooth oriented curve $C$:
> $$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C f\,dx + g\,dy + h\,dz = \int_a^b \mathbf{F}(\mathbf{r}(t))\cdot \mathbf{r}'(t)\,dt \tag{26–29}$$
> In terms of unit tangent $\mathbf{T} = \mathbf{r}'(s)$:
> $$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C (\mathbf{F}\cdot \mathbf{T})\,ds \tag{30}$$
> * **Work performed by force field $\mathbf{F}$:** $W = \int_C \mathbf{F}\cdot d\mathbf{r} \tag{34}$.
> * **Piecewise Smooth Curves:** $\int_C = \int_{C_1} + \int_{C_2} + \dots + \int_{C_n}$.

---

### QUICK CHECK EXERCISES 15.2
*(See page 1111 for answers.)*
1. The area of the surface extending upward from the line segment $y = x$ ($0 \le x \le 1$) in the $xy$-plane to the plane $z = 2x + 1$ is $\underline{\hspace{2cm}}$.  
   **Answer:** $2\sqrt{2}$
2. Suppose that a wire has equation $y = 1 - x$ ($0 \le x \le 1$) and mass density $\delta(x, y) = 2 - x$. Mass is $\underline{\hspace{2cm}}$.  
   **Answer:** $\frac{3\sqrt{2}}{2}$
3. If $C: x = \sin t, y = \cos t, z = t$ ($0 \le t \le 2\pi$), then $\int_C y\,dx - x\,dy + dz = \underline{\hspace{2cm}}$.  
   **Answer:** $4\pi$
4. If $C$ is the unit circle $x^2 + y^2 = 1$ counterclockwise and $\mathbf{F}(x, y) = x\mathbf{i} + y\mathbf{j}$, then $\int_C \mathbf{F}\cdot d\mathbf{r} = \underline{\hspace{2cm}}$.  
   **Answer:** $0$

---

## 15.3 INDEPENDENCE OF PATH; CONSERVATIVE VECTOR FIELDS

### THE FUNDAMENTAL THEOREM OF LINE INTEGRALS

> **15.3.1 THEOREM (Fundamental Theorem of Line Integrals)**
> If $\mathbf{F} = \nabla\phi$ is a conservative vector field on an open connected region $D$, and $C$ is any piecewise smooth curve from $(x_0, y_0, z_0)$ to $(x_1, y_1, z_1)$ in $D$:
> $$\int_C \mathbf{F}\cdot d\mathbf{r} = \int_C \nabla\phi\cdot d\mathbf{r} = \phi(x_1, y_1, z_1) - \phi(x_0, y_0, z_0) \tag{3–5, 18}$$

---

### EQUIVALENCE CONDITIONS FOR CONSERVATIVE FIELDS

> **15.3.2 THEOREM**
> On an open connected region $D$, the following are equivalent:
> 1. $\mathbf{F}$ is conservative on $D$ ($\mathbf{F} = \nabla\phi$).
> 2. $\oint_C \mathbf{F}\cdot d\mathbf{r} = 0$ for every piecewise smooth closed curve $C$ in $D$.
> 3. $\int_C \mathbf{F}\cdot d\mathbf{r}$ is independent of path in $D$.

---

### CONSERVATIVE FIELD TEST

> **15.3.3 THEOREM (Conservative Field Test in 2-Space)**
> Let $\mathbf{F}(x, y) = f(x, y)\mathbf{i} + g(x, y)\mathbf{j}$. If $\mathbf{F}$ is conservative, then:
> $$\frac{\partial f}{\partial y} = \frac{\partial g}{\partial x} \tag{9}$$
> Conversely, if $D$ is **simply connected** (no holes) and $\frac{\partial f}{\partial y} = \frac{\partial g}{\partial x}$ throughout $D$, then $\mathbf{F}$ is conservative on $D$.

* **In 3-Space:** $\mathbf{F} = f\mathbf{i} + g\mathbf{j} + h\mathbf{k}$ is conservative on a simply connected region $\iff \text{curl}\,\mathbf{F} = \mathbf{0}$, i.e.,
  $$\frac{\partial f}{\partial y} = \frac{\partial g}{\partial x}, \quad \frac{\partial f}{\partial z} = \frac{\partial h}{\partial x}, \quad \frac{\partial g}{\partial z} = \frac{\partial h}{\partial y} \tag{19}$$

* **Conservation of Energy:**
  $$W = \int_C \mathbf{F}\cdot d\mathbf{r} = -[V(x_1, y_1, z_1) - V(x_0, y_0, z_0)] = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2 \implies \frac{1}{2}mv_i^2 + V_i = \frac{1}{2}mv_f^2 + V_f$$

---

### QUICK CHECK EXERCISES 15.3
*(See page 1121 for answers.)*
1. If $C$ is a piecewise smooth curve from $(1, 2, 3)$ to $(4, 5, 6)$, then $\int_C dx + 2\,dy + 3\,dz = \underline{\hspace{2cm}}$.  
   **Answer:** $18$
2. If $C$ is the right half of $x^2 + y^2 = 1$ ($x \ge 0$) counterclockwise, $f(x, y) = ye^x$, then $\int_C \nabla f\cdot d\mathbf{r} = \underline{\hspace{2cm}}$.  
   **Answer:** $2$
3. A potential function for $\mathbf{F} = yz\mathbf{i} + (xz + z)\mathbf{j} + (xy + y + 1)\mathbf{k}$ is $\phi(x, y, z) = \underline{\hspace{2cm}}$.  
   **Answer:** $xyz + yz + z$
4. If $x^5 y^a \mathbf{i} + x^b y^c \mathbf{j}$ is conservative, then $a = \underline{\hspace{1cm}}, b = \underline{\hspace{1cm}}, c = \underline{\hspace{1cm}}$.  
   **Answer:** $a = 6, b = 6, c = 5$

---

## 15.4 GREEN’S THEOREM

### GREEN’S THEOREM STATEMENT

> **15.4.1 THEOREM (Green's Theorem)**
> Let $R$ be a simply connected plane region whose boundary is a simple, closed, piecewise smooth curve $C$ oriented counterclockwise (positive orientation). If $f(x, y)$ and $g(x, y)$ have continuous first partial derivatives on an open set containing $R$:
> $$\oint_C f(x, y)\,dx + g(x, y)\,dy = \iint_R \left(\frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}\right)\,dA \tag{1, 5}$$

---

### AREA FORMULAS VIA GREEN’S THEOREM

$$\text{Area}(R) = \iint_R 1\,dA = \oint_C x\,dy = -\oint_C y\,dx = \frac{1}{2}\oint_C -y\,dx + x\,dy \tag{6}$$

* **Multiply Connected Regions:** If $R$ has holes, outer boundary $C_1$ is oriented counterclockwise, inner boundaries $C_2, \dots, C_{n+1}$ are oriented clockwise:
  $$\iint_R \left(\frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}\right)\,dA = \oint_{C_1} (f\,dx + g\,dy) + \oint_{C_2} (f\,dx + g\,dy) + \dots + \oint_{C_{n+1}} (f\,dx + g\,dy) \tag{7}$$

---

### QUICK CHECK EXERCISES 15.4
*(See page 1129 for answers.)*
1. If $C$ is the square with vertices $(\pm 1, \pm 1)$ counterclockwise: $\int_C -y\,dx + x\,dy = \underline{\hspace{2cm}}$.  
   **Answer:** $8$ ($2 \times \text{Area} = 2 \times 4 = 8$)
2. If $C$ is triangle $(0, 0), (1, 0), (1, 1)$ counterclockwise: $\int_C 2xy\,dx + (x^2 + x)\,dy = \underline{\hspace{2cm}}$.  
   **Answer:** $\frac{1}{2}$
3. If $C$ is the counterclockwise unit circle: $\int_C (y^3 - y - x)\,dx + (x^3 + x + y)\,dy = \underline{\hspace{2cm}}$.  
   **Answer:** $2\pi$
4. Region $R$ and functions for $\int_0^1 \int_0^{\sqrt{1-x^2}}(2x+2y)\,dy\,dx = \int_0^{\pi/2}(\sin^3 t + \cos^3 t)\,dt$:  
   **Answer:** $R: x^2 + y^2 \le 1$ ($x \ge 0, y \ge 0$), $f(x, y) = -y^2, g(x, y) = x^2$

---

## 15.5 SURFACE INTEGRALS

### DEFINITION & PARAMETRIC SURFACES

> **15.5.1 DEFINITION**
> For a smooth parametric surface $\sigma$:
> $$\iint_\sigma f(x, y, z)\,dS = \lim_{n \to \infty} \sum_{k=1}^n f(x_k^*, y_k^*, z_k^*)\,\Delta S_k \tag{3}$$

> **15.5.2 THEOREM**
> If $\sigma$ is represented by $\mathbf{r}(u, v) = x(u, v)\mathbf{i} + y(u, v)\mathbf{j} + z(u, v)\mathbf{k}$ over region $R$ in $uv$-plane:
> $$\iint_\sigma f(x, y, z)\,dS = \iint_R f(x(u, v), y(u, v), z(u, v)) \left\| \frac{\partial\mathbf{r}}{\partial u} \times \frac{\partial\mathbf{r}}{\partial v} \right\| dA \tag{6}$$

---

### NONPARAMETRIC SURFACES

> **15.5.3 THEOREM**
> * For $z = g(x, y)$ projecting onto $R$ in $xy$-plane:
>   $$\iint_\sigma f(x, y, z)\,dS = \iint_R f(x, y, g(x, y)) \sqrt{\left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2 + 1}\,dA \tag{8}$$
> * Similar formulas hold for $y = g(x, z)$ and $x = g(y, z)$ (Formulas 9, 10).

---

### QUICK CHECK EXERCISES 15.5
*(See page 1138 for answers.)*
1. (a) For $\mathbf{r}(u, v)$, replace $dS$ with $\left\|\frac{\partial\mathbf{r}}{\partial u}\times\frac{\partial\mathbf{r}}{\partial v}\right\|dA$. (b) For $z=g(x, y)$, replace $dS$ with $\sqrt{(\partial z/\partial x)^2 + (\partial z/\partial y)^2 + 1}\,dA$.
2. For triangle $(1, 0, 0), (0, 1, 0), (0, 0, 1)$: $\iint_\sigma (x+y+z)\,dS = \frac{\sqrt{3}}{2}$.
3. For sphere radius 2: $\iint_\sigma (x^2 + y^2 + z^2)\,dS = 4(4\pi \cdot 2^2) = 64\pi$.
4. Mass of lamina: $M = \iint_\sigma f(x, y, z)\,dS$.

---

## 15.6 APPLICATIONS OF SURFACE INTEGRALS; FLUX

### FLUX OF A VECTOR FIELD

> **15.6.1 & 15.6.2 THEOREMS (Flux)**
> The **flux** of vector field $\mathbf{F}$ across an oriented surface $\sigma$ with unit normal $\mathbf{n}$ is:
> $$\Phi = \iint_\sigma \mathbf{F}\cdot \mathbf{n}\,dS \tag{4}$$
> * **Parametric surface $\mathbf{r}(u, v)$:**
>   $$\Phi = \iint_R \mathbf{F}\cdot \left(\frac{\partial\mathbf{r}}{\partial u} \times \frac{\partial\mathbf{r}}{\partial v}\right) dA \tag{5}$$
> * **Nonparametric surface $z = g(x, y)$:**
>   $$\text{Upward: } \Phi = \iint_R \mathbf{F}\cdot \left(-\frac{\partial z}{\partial x}\mathbf{i} - \frac{\partial z}{\partial y}\mathbf{j} + \mathbf{k}\right) dA \tag{12}$$
>   $$\text{Downward: } \Phi = \iint_R \mathbf{F}\cdot \left(\frac{\partial z}{\partial x}\mathbf{i} + \frac{\partial z}{\partial y}\mathbf{j} - \mathbf{k}\right) dA \tag{13}$$

---

### QUICK CHECK EXERCISES 15.6
*(See page 1148 for answers.)*
1. (a) $\iint_\sigma \mathbf{F}\cdot\mathbf{n}\,dS$; (b) $4\pi$.
2. (a) $\iint_R \mathbf{F}\cdot\left(\frac{\partial\mathbf{r}}{\partial u}\times\frac{\partial\mathbf{r}}{\partial v}\right)dA$; (b) $0$.
3. (a) $\iint_R \mathbf{F}\cdot\left(-\frac{\partial z}{\partial x}\mathbf{i} - \frac{\partial z}{\partial y}\mathbf{j} + \mathbf{k}\right)dA$; (b) $\frac{1}{2}$.
4. The net volume of fluid crossing $\sigma$ in the positive direction per unit time.

---

## 15.7 THE DIVERGENCE THEOREM

### THE DIVERGENCE THEOREM (GAUSS’S THEOREM)

> **15.7.1 THEOREM (The Divergence Theorem)**
> Let $G$ be a solid bounded by a closed, piecewise smooth surface $\sigma$ oriented outward. If $\mathbf{F}$ has continuous first partial derivatives on an open set containing $G$:
> $$\iint_\sigma \mathbf{F}\cdot \mathbf{n}\,dS = \iiint_G \text{div}\,\mathbf{F}\,dV \tag{1}$$

* **Physical Interpretation:** Divergence as limiting flux density:
  $$\text{div}\,\mathbf{F}(P_0) = \lim_{\text{vol}(G)\to 0} \frac{1}{\text{vol}(G)}\iint_{\sigma(G)} \mathbf{F}\cdot \mathbf{n}\,dS \tag{9}$$
* **Sources and Sinks:** $\text{div}\,\mathbf{F} > 0 \implies \text{source}$; $\text{div}\,\mathbf{F} < 0 \implies \text{sink}$; $\text{div}\,\mathbf{F} = 0 \implies \text{incompressible without sources/sinks}$.
* **Gauss's Law for Inverse-Square Fields (15.7.2):** For $\mathbf{F}(\mathbf{r}) = \frac{c}{\|\mathbf{r}\|^3}\mathbf{r}$, outward flux across any closed surface enclosing the origin is $\Phi = 4\pi c$.

---

### QUICK CHECK EXERCISES 15.7
*(See page 1158 for answers.)*
1. $\iint_\sigma \mathbf{F}\cdot\mathbf{n}\,dS; \; \iiint_G \text{div}\,\mathbf{F}\,dV$.
2. $3$.
3. source; sink; $\text{div}\,\mathbf{F} = 0$.
4. $4\pi c; \; 0$.

---

## 15.8 STOKES’ THEOREM

### STOKES’ THEOREM STATEMENT

> **15.8.1 THEOREM (Stokes' Theorem)**
> Let $\sigma$ be a piecewise smooth oriented surface bounded by a simple, closed, piecewise smooth curve $C$ with positive orientation (right-hand rule). If $\mathbf{F}$ has continuous first partial derivatives on an open set containing $\sigma$:
> $$\oint_C \mathbf{F}\cdot d\mathbf{r} = \oint_C (\mathbf{F}\cdot \mathbf{T})\,ds = \iint_\sigma (\text{curl}\,\mathbf{F})\cdot \mathbf{n}\,dS \tag{2–3}$$

* **Green's Theorem as a Special Case:** When $\sigma$ is a flat planar region in $xy$-plane with normal $\mathbf{k}$, Stokes' Theorem reduces directly to Green's Theorem.
* **Curl as Circulation Density:**
  $$\text{curl}\,\mathbf{F}(P_0)\cdot \mathbf{n} = \lim_{a \to 0} \frac{1}{A(\sigma_a)}\oint_{C_a} \mathbf{F}\cdot \mathbf{T}\,ds \tag{9}$$
  Maximum circulation density occurs when $\mathbf{n}$ aligns with $\text{curl}\,\mathbf{F}(P_0)$.
* **Irrotational Field:** If $\text{curl}\,\mathbf{F} = \mathbf{0}$ throughout a region, $\mathbf{F}$ is irrotational.

---

### QUICK CHECK EXERCISES 15.8
*(See page 1166 for answers.)*
1. $\int_C \mathbf{F}\cdot \mathbf{T}\,ds; \; \iint_\sigma (\text{curl}\,\mathbf{F})\cdot \mathbf{n}\,dS$.
2. $3\pi a^2$.
3. (a) $\iint_{\sigma_1}(\text{curl}\,\mathbf{F})\cdot\mathbf{n}\,dS; \; \iint_{\sigma_2}(\text{curl}\,\mathbf{F})\cdot\mathbf{n}\,dS$; (b) $3\pi a^2$.
4. curl.

---

## CHAPTER 15 MAKING CONNECTIONS

1. **Work-Kinetic Energy Theorem for Free Motion:**
   $$\int_C \mathbf{F}\cdot \mathbf{T}\,ds = \int_C m\left(\frac{dv}{dt}\right)ds = m\int_a^b v(t)\frac{dv}{dt}dt = \frac{1}{2}m[v(b)]^2 - \frac{1}{2}m[v(a)]^2$$
2. **Constrained Motion:** For resultant force $\mathbf{F} + \mathbf{S}$, since support force $\mathbf{S} \perp \mathbf{T}$ ($\mathbf{S}\cdot\mathbf{T} = 0$), work performed by $\mathbf{F}$ equals change in kinetic energy.
3. **Conservation of Energy:** $\frac{1}{2}mv_i^2 + V_i = \frac{1}{2}mv_f^2 + V_f$.
4. **Inclined Slide:** $v = \sqrt{2gl\sin\theta}$.
