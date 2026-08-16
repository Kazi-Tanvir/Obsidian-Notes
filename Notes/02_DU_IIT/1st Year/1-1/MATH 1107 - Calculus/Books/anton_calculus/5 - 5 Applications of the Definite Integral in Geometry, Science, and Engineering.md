# CHAPTER 5: APPLICATIONS OF THE DEFINITE INTEGRAL IN GEOMETRY, SCIENCE, AND ENGINEERING

> Calculus is essential for the computations required to land an astronaut on the Moon.

In the last chapter we introduced the definite integral as the limit of Riemann sums in the context of finding areas. However, Riemann sums and definite integrals have applications that extend far beyond the area problem. In this chapter we will show how Riemann sums and definite integrals arise in such problems as finding the volume and surface area of a solid, finding the length of a plane curve, calculating the work done by a force, finding the center of gravity of a planar region, and finding the pressure and force exerted by a fluid on a submerged object.

Although these problems are diverse, the required calculations can all be approached by the same procedure that we used to find areas—breaking the required calculation into "small parts," making an approximation for each part, adding the approximations from the parts to produce a Riemann sum that approximates the entire quantity to be calculated, and then taking the limit of the Riemann sums to produce an exact result.

---

## 5.1 AREA BETWEEN TWO CURVES

### AREA BETWEEN $y = f(x)$ AND $y = g(x)$

> **5.1.1 FIRST AREA PROBLEM & 5.1.2 AREA FORMULA**  
> If $f$ and $g$ are continuous functions on the interval $[a, b]$, and if $f(x) \ge g(x)$ for all $x$ in $[a, b]$, then the area $A$ of the region bounded above by $y = f(x)$, below by $y = g(x)$, on the left by $x = a$, and on the right by $x = b$ is
> $$A = \int_a^b [f(x) - g(x)] dx \tag{1}$$

#### Examples:
* **Example 1:** Area between $y = x + 6$ and $y = x^2$ over $[0, 2]$:
  $$A = \int_0^2 [(x + 6) - x^2] dx = \left[\frac{x^2}{2} + 6x - \frac{x^3}{3}\right]_0^2 = \frac{34}{3}$$
* **Example 2:** Area enclosed between $y = x^2$ and $y = x + 6$:  
  Intersections at $x^2 = x + 6 \implies x = -2, 3$:
  $$A = \int_{-2}^3 [(x + 6) - x^2] dx = \frac{125}{6}$$
* **Example 3:** Velocity curves: Area between $v_2(t)$ and $v_1(t)$ over $[0, T]$ represents the distance by which car 2 is ahead of car 1 at time $T$.

---

### REVERSING THE ROLES OF $x$ AND $y$

> **5.1.4 AREA FORMULA (Integrating with respect to $y$)**  
> If $w(y) \ge v(y)$ for all $y \in [c, d]$:
> $$A = \int_c^d [w(y) - v(y)] dy \tag{4}$$

#### Example 5
Region enclosed by $x = y^2$ and $y = x - 2$ ($x = y + 2$):  
Intersections: $y^2 = y + 2 \implies y = -1, 2$:
$$A = \int_{-1}^2 [(y + 2) - y^2] dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_{-1}^2 = \frac{9}{2}$$

---

### QUICK CHECK EXERCISES 5.1
*(See page 355 for answers.)*
1. $\int_0^2 [(20 - 3x^2) - 3\sqrt{x}] dx$.  
2. $\int_{-1}^5 [(2x + 8) - (2x - 3)] dx = 66$.  
3. (a) $(-2, 0); (0, 2)$ (b) $\int_{-2}^0 [\sqrt{4 - x^2} - (x + 2)] dx$ (c) $\int_0^2 [(y - 2) + \sqrt{4 - y^2}] dy$.  
4. Area enclosed between $y = x^2$ and $y = \sqrt[3]{x}$ is $5/12$.

---

## 5.2 VOLUMES BY SLICING; DISKS AND WASHERS

### VOLUMES BY SLICING

> **5.2.2 & 5.2.3 THEOREMS (Volume Formulas)**  
> * Cross sections perpendicular to $x$-axis: $V = \int_a^b A(x) dx \tag{3}$  
> * Cross sections perpendicular to $y$-axis: $V = \int_c^d A(y) dy \tag{4}$

#### Example 1 (Square Pyramid)
Right pyramid with altitude $h$ and square base $a$:
$$A(y) = \frac{a^2}{h^2}(h - y)^2 \implies V = \int_0^h \frac{a^2}{h^2}(h - y)^2 dy = \frac{1}{3}a^2 h$$

---

### METHOD OF DISKS AND WASHERS

* **Disks about $x$-axis:** $V = \int_a^b \pi [f(x)]^2 dx \tag{5}$
* **Washers about $x$-axis:** $V = \int_a^b \pi ([f(x)]^2 - [g(x)]^2) dx \tag{6}$
* **Disks about $y$-axis:** $V = \int_c^d \pi [u(y)]^2 dy \tag{7}$
* **Washers about $y$-axis:** $V = \int_c^d \pi ([w(y)]^2 - [v(y)]^2) dy \tag{8}$

#### Examples:
* **Example 2:** $y = \sqrt{x}$ about $x$-axis on $[1, 4] \implies V = \int_1^4 \pi x dx = \frac{15\pi}{2}$.
* **Example 3 (Sphere):** Revolve $y = \sqrt{r^2 - x^2}$ on $[-r, r]$ about $x$-axis $\implies V = \frac{4}{3}\pi r^3$.
* **Example 4:** Region between $y = \frac{1}{2} + x^2$ and $y = x$ on $[0, 2]$ about $x$-axis $\implies V = \frac{69\pi}{10}$.
* **Example 5:** $y = \sqrt{x}, y = 2, x = 0$ about $y$-axis ($x = y^2$) $\implies V = \int_0^2 \pi y^4 dy = \frac{32\pi}{5}$.
* **Example 6 (Rotated about $y = -1$):** Region under $y = x^2$ on $[0, 2] \implies V = \int_0^2 \pi [(x^2 + 1)^2 - 1^2] dx = \frac{176\pi}{15}$.

> **Cavalieri's Principle (1635)**  
> Solids with equal heights and equal cross-sectional areas at equal distances from the base have equal volumes.

---

### QUICK CHECK EXERCISES 5.2
*(See page 365 for answers.)*
1. $\int_1^3 3x^2 dx = 26$.  
2. (a) $\pi\sin x$ (b) $\int_0^\pi \pi\sin x dx$ (c) $2\pi$.  
3. (a) 0 to 2; $\pi[(2x+1)^2 - (x^2+1)^2] = \pi[-x^4 + 2x^2 + 4x]$ (b) $\int_0^2 \pi[-x^4 + 2x^2 + 4x]dx$.  
4. (a) 1 to 2; $\pi[(y - 1) - (y - 1)^2]$ (b) $\int_1^2 \pi[-y^2 + 3y - 2]dy$.

---

## 5.3 VOLUMES BY CYLINDRICAL SHELLS

### CYLINDRICAL SHELLS ABOUT THE $y$-AXIS

A cylindrical shell of average radius $r$, height $h$, and thickness $\Delta r$ has volume:
$$\Delta V = 2\pi r h \Delta r = 2\pi \cdot [\text{average radius}] \cdot [\text{height}] \cdot [\text{thickness}]$$

> **5.3.2 THEOREM**  
> If $f$ is continuous and nonnegative on $[a, b]$ ($0 \le a < b$), the volume $V$ generated by revolving the region under $y = f(x)$ about the $y$-axis is
> $$V = \int_a^b 2\pi x f(x) dx \tag{2}$$

#### Examples:
* **Example 1:** $y = \sqrt{x}$ on $[1, 4]$ about $y$-axis $\implies V = \int_1^4 2\pi x^{3/2} dx = \frac{124\pi}{5}$.
* **Example 2:** Region between $y = x$ and $y = x^2$ about $y$-axis $\implies V = \int_0^1 2\pi x(x - x^2)dx = \frac{\pi}{6}$.
* **Example 3:** Region under $y = x^2$ on $[0, 2]$ about $y = -1$ using horizontal shells $\implies V = \int_0^4 2\pi(y + 1)(2 - \sqrt{y})dy = \frac{176\pi}{15}$.

---

### QUICK CHECK EXERCISES 5.3
*(See page 371 for answers.)*
1. (a) $2\pi x(1 + \sqrt{x})$ (b) $\int_1^4 2\pi x(1 + \sqrt{x}) dx$.  
2. (a) $2\pi(5 - x)(1 + \sqrt{x})$ (b) $\int_1^4 2\pi(5 - x)(1 + \sqrt{x}) dx$.  
3. $\int_0^4 2\pi y [4 - (y - 2)^2] dy$.

---

## 5.4 LENGTH OF A PLANE CURVE

### ARC LENGTH FORMULAS

> **5.4.2 DEFINITION**  
> If $y = f(x)$ is a smooth curve on $[a, b]$ ($f'$ continuous), the **arc length** $L$ is
> $$L = \int_a^b \sqrt{1 + [f'(x)]^2} dx = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx \tag{3–4}$$
> If $x = g(y)$ on $[c, d]$:
> $$L = \int_c^d \sqrt{1 + [g'(y)]^2} dy = \int_c^d \sqrt{1 + \left(\frac{dx}{dy}\right)^2} dy \tag{5}$$
> Parametric curve $x = x(t), y = y(t)$ for $a \le t \le b$:
> $$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt$$

#### Example 1
Arc length of $y = x^{3/2}$ from $(1, 1)$ to $(2, 2\sqrt{2})$:
$$L = \int_1^2 \sqrt{1 + \frac{9}{4}x} dx = \frac{22\sqrt{22} - 13\sqrt{13}}{27} \approx 2.09$$

---

### QUICK CHECK EXERCISES 5.4
*(See page 377 for answers.)*
1. continuous.  
2. $\int_a^b \sqrt{1 + [f'(x)]^2} dx$.  
3. $\sqrt{(\pi - 1)^2 + 1}$.  
4. (a) $\int_0^2 \sqrt{1 + 4x^2} dx$ (b) $\int_0^4 \sqrt{1 + \frac{1}{4y}} dy$.

---

## 5.5 AREA OF A SURFACE OF REVOLUTION

### SURFACE AREA FORMULAS

Frustum lateral area: $S = \pi(r_1 + r_2)l$.

> **5.5.2 DEFINITION**  
> For a smooth nonnegative function $y = f(x)$ on $[a, b]$:
> * **Revolved about $x$-axis:**
>   $$S = \int_a^b 2\pi f(x) \sqrt{1 + [f'(x)]^2} dx = \int_a^b 2\pi y \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx \tag{4}$$
> * **Revolved about $y$-axis ($x = g(y)$ on $[c, d]$):**
>   $$S = \int_c^d 2\pi g(y) \sqrt{1 + [g'(y)]^2} dy = \int_c^d 2\pi x \sqrt{1 + \left(\frac{dx}{dy}\right)^2} dy \tag{5}$$

#### Examples:
* **Example 1:** $y = x^3$ on $[0, 1]$ about $x$-axis $\implies S = \int_0^1 2\pi x^3 \sqrt{1 + 9x^4} dx = \frac{\pi}{27}(10^{3/2} - 1) \approx 3.56$.
* **Example 2:** $y = x^2$ on $[1, 2]$ about $y$-axis $\implies S = \frac{\pi}{6}(17^{3/2} - 5^{3/2}) \approx 30.85$.
* **Surface of a Sphere:** $S = 4\pi r^2$.

---

### QUICK CHECK EXERCISES 5.5
*(See page 382 for answers.)*
1. $\int_a^b 2\pi f(x)\sqrt{1 + [f'(x)]^2} dx$.  
2. $3\sqrt{10}\pi$.  
3. $\int_3^6 2\pi\left(\frac{x}{3}\right)\frac{\sqrt{10}}{3} dx = \int_3^6 \frac{2\sqrt{10}\pi}{9}x dx$.  
4. $\int_1^2 (2\pi)(3y)\sqrt{10} dy$.

---

## 5.6 WORK

### WORK DONE BY FORCES

* **Constant Force:** $W = F \cdot d \tag{1}$  
  *Units:* Joules ($\text{J} = \text{N}\cdot\text{m}$), Ergs ($\text{dyn}\cdot\text{cm}$), Foot-pounds ($\text{ft}\cdot\text{lb}$).

> **5.6.3 DEFINITION (Variable Force)**  
> $$W = \int_a^b F(x) dx \tag{2}$$

* **Hooke's Law:** $F(x) = kx \implies W = \int_0^d kx dx = \frac{1}{2}kd^2$.
* **Pumping Water from Tanks:** Slice water into horizontal slabs of thickness $\Delta x$, compute weight of slab $F_k \approx \rho (\text{Area}) \Delta x$, lift distance $x_k^*$, integrate:
  $$W = \int_a^b \rho x A(x) dx$$

### WORK–ENERGY RELATIONSHIP

> **5.6.4 NEWTON'S SECOND LAW & KINETIC ENERGY**  
> $$F = ma = m\frac{dv}{dt} \implies W = \int_a^b F(x) dx = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2 = K_f - K_i \tag{6}$$
> where kinetic energy $K = \frac{1}{2}mv^2$.

---

### QUICK CHECK EXERCISES 5.6
*(See page 391 for answers.)*
1. $50\text{ ft}\cdot\text{lb}$.  
2. joule; erg.  
3. $\int_a^b F(x) dx$.  
4. $\int_2^5 (10 - 2x) dx = 9\text{ J}$.

---

## 5.7 MOMENTS, CENTERS OF GRAVITY, AND CENTROIDS

### MOMENTS AND EQUILIBRIUM
* Moment about a point: $\text{Moment} = m(x - a)$.
* System in equilibrium if $\sum m_k(x_k - a) = 0$.

### CENTER OF GRAVITY & CENTROID OF A LAMINA
For a lamina bounded by $y = f(x), y = 0, x = a, x = b$ with constant density $\delta$:
* **Mass:** $M = \delta A = \delta \int_a^b f(x) dx$
* **Centroid $(\bar{x}, \bar{y})$:**
  $$\bar{x} = \frac{M_y}{M} = \frac{\int_a^b x f(x) dx}{\int_a^b f(x) dx} = \frac{1}{A}\int_a^b x f(x) dx \tag{8}$$
  $$\bar{y} = \frac{M_x}{M} = \frac{\int_a^b \frac{1}{2}[f(x)]^2 dx}{\int_a^b f(x) dx} = \frac{1}{A}\int_a^b \frac{1}{2}[f(x)]^2 dx \tag{9}$$

#### Centroid Between Two Curves $y = f(x)$ and $y = g(x)$:
$$\bar{x} = \frac{1}{A}\int_a^b x[f(x) - g(x)] dx, \quad \bar{y} = \frac{1}{A}\int_a^b \frac{1}{2}([f(x)]^2 - [g(x)]^2) dx$$

> **5.7.2 THEOREM (Theorem of Pappus)**  
> If a bounded plane region $R$ is revolved about a line $L$ in its plane not crossing $R$:
> $$\text{Volume } V = (\text{Area of } R) \cdot (\text{distance traveled by centroid}) = A \cdot (2\pi r_{\text{centroid}})$$

---

### QUICK CHECK EXERCISES 5.7
*(See page 400 for answers.)*
1. $\delta A$.  
2. first moment about the $y$-axis; $\int_a^b \delta x f(x) dx$.  
3. Centroid of $R$ between $x^2$ and $2 - x$: $(5/14, 32/35)$.  
4. $V = (7/6)(2\pi \cdot 6) = 14\pi$.

---

## 5.8 FLUID PRESSURE AND FORCE

### DEFINITIONS & FORMULAS
* **Pressure:** $P = \frac{F}{A}$ (Pascals $\text{Pa} = \text{N/m}^2$, $\text{lb/ft}^2$, psi).
* **Weight Density:** $\rho = \frac{w}{V}$ (Fresh water: $9810\text{ N/m}^3 = 62.4\text{ lb/ft}^3$).
* **Horizontal Surface at Depth $h$:** $F = \rho h A, \quad P = \rho h$.

> **5.8.3 DEFINITION (Fluid Force on a Vertical Surface)**  
> If the surface extends from depth $x = a$ to $x = b$, with width $w(x)$ and depth $h(x)$:
> $$F = \int_a^b \rho h(x) w(x) dx \tag{8}$$
> For inclined surface at angle $\theta$ with vertical:
> $$F = \int_a^b \rho h(x) w(x) \sec\theta dx$$

> **Blaise Pascal (1623–1662)**  
> Formulated Pascal's Principle (fluid pressure at a point is isotropic / same in all directions).

---

### QUICK CHECK EXERCISES 5.8
*(See page 406 for answers.)*
1. pascal; pounds per square inch.  
2. $P = (9810)(10) = 98{,}100\text{ Pa}$; $F = 98{,}100 \times 6 = 588{,}600\text{ N}$.  
3. $\int_a^b \rho h(x) w(x) dx$.  
4. $\int_0^3 9810[(5 + x)2] dx$.

---

## CHAPTER 5 REVIEW EXERCISES
Exercises 1–23 covering area between curves, volumes by disks/washers/shells, arc length, surface area, work, centroids, theorem of Pappus, and fluid force.

---

## CHAPTER 5 MAKING CONNECTIONS
Connections between fluid force at the centroid ($F = \rho \bar{h} A$), mass of inhomogeneous circular laminas, work via expanding piston model, and proofs of Archimedes' principle of buoyancy using cylindrical shells.
