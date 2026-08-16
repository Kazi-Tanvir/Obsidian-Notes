# CHAPTER 12: VECTOR-VALUED FUNCTIONS

> The design of a roller coaster requires an understanding of the mathematical principles governing the motion of objects that move with varying speed and direction.

In this chapter we consider functions whose values are vectors. Such functions provide a unified way of studying parametric curves in 2-space and 3-space and are a basic tool for analyzing particle motion along curved paths. We develop limits, derivatives, integrals, unit tangent/normal/binormal vectors ($\mathbf{TNB}$-frame), curvature, torsion, tangential and normal components of acceleration, projectile motion, and derive Kepler’s laws of planetary motion from Newton's laws of gravitation.

---

## 12.1 INTRODUCTION TO VECTOR-VALUED FUNCTIONS

### PARAMETRIC CURVES IN 3-SPACE & VECTOR-VALUED FUNCTIONS
* **Parametric Equations in 3-Space:** $x = f(t), \; y = g(t), \; z = h(t)$
* **Vector-Valued Function (12.1.4):**
  $$\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k}$$
  * Natural domain of $\mathbf{r}(t)$ is the intersection of domains of its component functions.
  * **Position Vector / Radius Vector:** $\mathbf{r}(t)$ drawn from origin $O$ to point $(x(t), y(t), z(t))$ on curve $C$.

#### Classic Curves:
* **Circular Helix:** $\mathbf{r}(t) = \langle a\cos t, a\sin t, ct \rangle$ ($a > 0, c > 0$)
* **Twisted Cubic:** $\mathbf{r}(t) = \langle t, t^2, t^3 \rangle$ (intersection of $y = x^2$ and $z = x^3$)
* **Two-Point Vector Form of Line Segment from $\mathbf{r}_0$ to $\mathbf{r}_1$:**
  $$\mathbf{r}(t) = (1 - t)\mathbf{r}_0 + t\mathbf{r}_1 \quad (0 \le t \le 1) \tag{8}$$

---

### QUICK CHECK EXERCISES 12.1
*(See page 847 for answers.)*
1. (a) $\mathbf{r} = \frac{1}{t}\mathbf{i} + \sqrt{t}\mathbf{j} + \sin^{-1} t\mathbf{k}$; (b) Domain $0 < t \le 1$; $\mathbf{r}(1/2) = 2\mathbf{i} + \frac{\sqrt{2}}{2}\mathbf{j} + \frac{\pi}{6}\mathbf{k}$.
2. Line through $(1, -1)$ with direction vector $\langle 2, 3 \rangle$.
3. Line segment in $xy$-plane from $(0, 1)$ to $(1, 0)$.
4. $\mathbf{r}(t) = \langle t, t^2, t^2 \rangle$.

---

## 12.2 CALCULUS OF VECTOR-VALUED FUNCTIONS

### LIMITS, CONTINUITY, AND DERIVATIVES

> **12.2.2 THEOREM (Componentwise Limits)**
> $$\lim_{t \to a} \mathbf{r}(t) = \left\langle \lim_{t \to a} x(t), \lim_{t \to a} y(t), \lim_{t \to a} z(t) \right\rangle$$
> $\mathbf{r}(t)$ is continuous at $t = a \iff \lim_{t \to a} \mathbf{r}(t) = \mathbf{r}(a)$.

> **12.2.5 THEOREM (Componentwise Differentiation)**
> $$\mathbf{r}'(t) = \frac{d\mathbf{r}}{dt} = \lim_{h \to 0} \frac{\mathbf{r}(t+h) - \mathbf{r}(t)}{h} = \langle x'(t), y'(t), z'(t) \rangle = x'(t)\mathbf{i} + y'(t)\mathbf{j} + z'(t)\mathbf{k}$$

* **Geometric Meaning (12.2.4):** $\mathbf{r}'(t)$ is tangent to curve $C$ at $\mathbf{r}(t)$ and points in direction of increasing parameter.
* **Tangent Line Equation at $t_0$:** $\mathbf{r} = \mathbf{r}(t_0) + t\mathbf{r}'(t_0)$.

---

### PRODUCT RULES & ORTHOGONALITY THEOREM

* **Scalar Product Rule:** $\frac{d}{dt}[f(t)\mathbf{r}(t)] = f(t)\mathbf{r}'(t) + f'(t)\mathbf{r}(t)$
* **Dot Product Rule (6):** $\frac{d}{dt}[\mathbf{r}_1(t) \cdot \mathbf{r}_2(t)] = \mathbf{r}_1(t) \cdot \mathbf{r}_2'(t) + \mathbf{r}_1'(t) \cdot \mathbf{r}_2(t)$
* **Cross Product Rule (7):** $\frac{d}{dt}[\mathbf{r}_1(t) \times \mathbf{r}_2(t)] = \mathbf{r}_1(t) \times \mathbf{r}_2'(t) + \mathbf{r}_1'(t) \times \mathbf{r}_2(t)$

> **12.2.8 THEOREM (Constant Norm Orthogonality)**
> If $\|\mathbf{r}(t)\|$ is constant for all $t$, then:
> $$\mathbf{r}(t) \cdot \mathbf{r}'(t) = 0 \quad (\mathbf{r}(t) \text{ and } \mathbf{r}'(t) \text{ are orthogonal})$$

---

### INTEGRATION OF VECTOR-VALUED FUNCTIONS
* **Definite Integral (12.2.9 & FTC 17):**
  $$\int_a^b \mathbf{r}(t)\,dt = \left\langle \int_a^b x(t)\,dt, \int_a^b y(t)\,dt, \int_a^b z(t)\,dt \right\rangle = \mathbf{R}(b) - \mathbf{R}(a)$$

---

### QUICK CHECK EXERCISES 12.2
*(See page 858 for answers.)*
1. (a) $9\mathbf{i} + 6\mathbf{j}$; (b) $\langle \frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2} \rangle$.
2. (a) $\mathbf{r}'(t) = 5\mathbf{i} + (1-2t)\mathbf{j}$; (b) $\mathbf{r}'(t) = \langle -1/t^2, \sec^2 t, 2e^{2t} \rangle$.
3. (a) $\langle 6, 4, 2 \rangle$; (b) $\langle -4, 0, 4 \rangle$; (c) $\mathbf{0}$; (d) $-28$.
4. (a) $\langle 1, 1/3, 2/\pi \rangle$; (b) $\frac{1}{2}t^2\mathbf{i} - t^3\mathbf{j} + e^t\mathbf{k} + \mathbf{C}$.

---

## 12.3 CHANGE OF PARAMETER; ARC LENGTH

### SMOOTH PARAMETRIZATIONS & ARC LENGTH FORMULA
* $\mathbf{r}(t)$ is **smooth** if $\mathbf{r}'(t)$ is continuous and $\mathbf{r}'(t) \neq \mathbf{0}$ for all $t$.
* **Arc Length Formula (Theorem 12.3.1):**
  $$L = \int_a^b \left\|\frac{d\mathbf{r}}{dt}\right\|dt = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}\,dt \tag{5}$$

---

### ARC LENGTH PARAMETRIZATION

> **12.3.3 & 12.3.4 THEOREMS**
> Arc length parameter $s$ with reference point $\mathbf{r}(t_0)$:
> $$s(t) = \int_{t_0}^t \left\|\frac{d\mathbf{r}}{du}\right\|du \implies \frac{ds}{dt} = \left\|\frac{d\mathbf{r}}{dt}\right\| \tag{10, 16}$$
> When parametrized by arc length $s$:
> $$\left\|\frac{d\mathbf{r}}{ds}\right\| = 1 \tag{17}$$

---

### QUICK CHECK EXERCISES 12.3
*(See page 868 for answers.)*
1. Arc length of the graph of $\mathbf{r}(t)$ from $t=a$ to $t=b$.
2. $\left\|\frac{d\mathbf{r}}{ds}\right\| = 1$; arc length is $b - a$.
3. $s = \int_{t_0}^t \left\|\frac{d\mathbf{r}}{du}\right\|du$.
4. $\mathbf{r}_1'(\pi/3) = \langle -3, 3, \sqrt{3} \rangle$.

---

## 12.4 UNIT TANGENT, NORMAL, AND BINORMAL VECTORS

### THE $\mathbf{TNB}$-FRAME (FRENET FRAME)

* **Unit Tangent Vector (12.4.1):**
  $$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|} \quad (\mathbf{T}(s) = \mathbf{r}'(s))$$
* **Principal Unit Normal Vector (12.4.2):**
  $$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|} \quad \left(\mathbf{N}(s) = \frac{\mathbf{r}''(s)}{\|\mathbf{r}''(s)\|}\right)$$
  *(In 2-space, $\mathbf{N}$ always points inward toward the concave side).*
* **Unit Binormal Vector (12.4.9 & 11):**
  $$\mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t) = \frac{\mathbf{r}'(t) \times \mathbf{r}''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}$$

### THREE FUNDAMENTAL PLANES
* **Osculating Plane:** Spanned by $\mathbf{T}$ and $\mathbf{N}$ (normal vector $\mathbf{B}$).
* **Normal Plane:** Spanned by $\mathbf{N}$ and $\mathbf{B}$ (normal vector $\mathbf{T}$).
* **Rectifying Plane:** Spanned by $\mathbf{T}$ and $\mathbf{B}$ (normal vector $\mathbf{N}$).

---

### QUICK CHECK EXERCISES 12.4
*(See page 873 for answers.)*
1. $\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{\|\mathbf{r}'(t)\|}, \; \mathbf{N}(t) = \frac{\mathbf{T}'(t)}{\|\mathbf{T}'(t)\|}, \; \mathbf{B}(t) = \mathbf{T}(t) \times \mathbf{N}(t)$.
2. $\mathbf{T}(s) = \mathbf{r}'(s), \; \mathbf{N}(s) = \frac{\mathbf{r}''(s)}{\|\mathbf{r}''(s)\|}$.
3. $\mathbf{B}(t) = \frac{\mathbf{r}'(t) \times \mathbf{r}''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}, \; \mathbf{B}(s) = \frac{\mathbf{r}'(s) \times \mathbf{r}''(s)}{\|\mathbf{r}''(s)\|}$.
4. $\mathbf{T}(0) = \langle 2/3, 1/3, 2/3 \rangle, \; \mathbf{N}(0) = \langle -1/(3\sqrt{2}), 4/(3\sqrt{2}), -1/(3\sqrt{2}) \rangle, \; \mathbf{B}(0) = \langle -1/\sqrt{2}, 0, 1/\sqrt{2} \rangle$.

---

## 12.5 CURVATURE

### DEFINITION & FORMULAS

> **12.5.1 DEFINITION (Curvature $\kappa$)**
> $$\kappa(s) = \left\|\frac{d\mathbf{T}}{ds}\right\| = \|\mathbf{r}''(s)\| \tag{1}$$

> **12.5.2 THEOREM (General Parameter Formulas)**
> $$\kappa(t) = \frac{\|\mathbf{T}'(t)\|}{\|\mathbf{r}'(t)\|} = \frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3} \tag{2–3}$$

* **For 2D Curve $y = f(x)$:**
  $$\kappa(x) = \frac{|y''|}{[1 + (y')^2]^{3/2}}$$
* **For 2D Parametric Curve $x=x(t), y=y(t)$:**
  $$\kappa(t) = \frac{|x'y'' - y'x''|}{(x'^2 + y'^2)^{3/2}}$$
* **For Polar Curve $r = f(\theta)$:**
  $$\kappa(\theta) = \frac{|r^2 + 2(r')^2 - r r''|}{[r^2 + (r')^2]^{3/2}}$$
* **Curvature of a Circle of radius $a$:** $\kappa = 1/a$. Line: $\kappa = 0$.
* **Radius of Curvature:** $\rho = \frac{1}{\kappa}$. Center of curvature lies along $\mathbf{N}$ at distance $\rho$.

---

### FRENET-SERRET FORMULAS & TORSION
$$\frac{d\mathbf{T}}{ds} = \kappa \mathbf{N}, \quad \frac{d\mathbf{N}}{ds} = -\kappa \mathbf{T} + \tau \mathbf{B}, \quad \frac{d\mathbf{B}}{ds} = -\tau \mathbf{N}$$
* **Torsion $\tau(t)$ (Twisting out of osculating plane):**
  $$\tau(t) = \frac{[\mathbf{r}'(t) \times \mathbf{r}''(t)] \cdot \mathbf{r}'''(t)}{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|^2}$$

---

### QUICK CHECK EXERCISES 12.5
*(See page 881 for answers.)*
1. $\kappa(s) = \|d\mathbf{T}/ds\| = \|\mathbf{r}''(s)\|$.
2. (a) $\frac{\|\mathbf{T}'(t)\|}{\|\mathbf{r}'(t)\|}$; (b) $\frac{\|\mathbf{r}'(t) \times \mathbf{r}''(t)\|}{\|\mathbf{r}'(t)\|^3}$.
3. $\kappa(s) = |d\phi/ds|$.
4. $\kappa = 1/2$.

---

## 12.6 MOTION ALONG A CURVE

### VELOCITY, SPEED, ACCELERATION (12.6.1)
* **Position:** $\mathbf{r}(t)$
* **Velocity:** $\mathbf{v}(t) = \mathbf{r}'(t) = \frac{ds}{dt}\mathbf{T}(t)$
* **Speed:** $v(t) = \|\mathbf{v}(t)\| = \frac{ds}{dt}$
* **Acceleration:** $\mathbf{a}(t) = \mathbf{v}'(t) = \mathbf{r}''(t)$
* **Displacement over $[t_1, t_2]$:** $\Delta \mathbf{r} = \mathbf{r}(t_2) - \mathbf{r}(t_1) = \int_{t_1}^{t_2} \mathbf{v}(t)\,dt$
* **Distance Traveled:** $s = \int_{t_1}^{t_2} \|\mathbf{v}(t)\|\,dt$

---

### TANGENTIAL AND NORMAL COMPONENTS OF ACCELERATION

> **12.6.2 & 12.6.3 THEOREMS**
> $$\mathbf{a} = a_T \mathbf{T} + a_N \mathbf{N} \tag{14}$$
> * **Tangential Component:**
>   $$a_T = \frac{d^2s}{dt^2} = \frac{\mathbf{v} \cdot \mathbf{a}}{\|\mathbf{v}\|}$$
> * **Normal Component:**
>   $$a_N = \kappa\left(\frac{ds}{dt}\right)^2 = \frac{\|\mathbf{v} \times \mathbf{a}\|}{\|\mathbf{v}\|} = \sqrt{\|\mathbf{a}\|^2 - a_T^2}$$
>
> *(Note: $\mathbf{a}$ always lies in the osculating $\mathbf{TN}$-plane; the binormal component is 0).*

---

### PROJECTILE MOTION (Parabolic Trajectory)
Assuming constant gravity $\mathbf{a} = -g\mathbf{j}$, launch speed $v_0$, angle $\alpha$, launch height $s_0$:
* **Position:** $\mathbf{r}(t) = (v_0\cos\alpha)t\mathbf{i} + \left(s_0 + (v_0\sin\alpha)t - \frac{1}{2}gt^2\right)\mathbf{j} \tag{26}$
* **Max Height ($s_0=0$):** $y_{\max} = \frac{(v_0\sin\alpha)^2}{2g}$
* **Range ($s_0=0$):** $R = \frac{v_0^2\sin 2\alpha}{g}$ (Maximum range at $\alpha = 45^\circ$).

---

### QUICK CHECK EXERCISES 12.6
*(See page 895 for answers.)*
1. $\mathbf{v}(t) = d\mathbf{r}/dt, \; \mathbf{a}(t) = d\mathbf{v}/dt = d^2\mathbf{r}/dt^2, \; ds/dt = \|\mathbf{v}(t)\|$.
2. $\mathbf{r}(t_2) - \mathbf{r}(t_1); \; \int_{t_1}^{t_2} \|\mathbf{v}(t)\|dt$.
3. $a_T = d^2s/dt^2; \; a_N = \kappa(ds/dt)^2$.
4. $\mathbf{a} = -g\mathbf{j}; \; \mathbf{v}(t) = -gt\mathbf{j} + \mathbf{v}_0; \; s_0\mathbf{j}; \; \mathbf{v}_0$.

---

## 12.7 KEPLER’S LAWS OF PLANETARY MOTION

### NEWTON’S GRAVITATION & CENTRAL FORCES
* **Central Force Field:** $\mathbf{F} = -\frac{GMm}{r^3}\mathbf{r} \implies \mathbf{a} = -\frac{GM}{r^3}\mathbf{r}$.
* **Planar Motion:** $\mathbf{r} \times \mathbf{v} = \mathbf{b} = r_0 v_0 \mathbf{k}$ (constant angular momentum vector).

---

### DERIVATION OF KEPLER’S LAWS
1. **First Law (Law of Orbits):** Orbit is a conic section in polar coordinates:
   $$r = \frac{k}{1 + e\cos\theta}, \quad e = \frac{r_0 v_0^2}{GM} - 1$$
   * Ellipse if $e < 1$, Parabola if $e = 1$, Hyperbola if $e > 1$.
   * **Escape Speed:** $v_{\text{esc}} = \sqrt{\frac{2GM}{r_0}}$.
2. **Second Law (Law of Areas):** $\frac{dA}{dt} = \frac{1}{2}r_0 v_0 = \text{constant}$ (Equal areas swept in equal times).
3. **Third Law (Law of Periods):**
   $$T^2 = \left(\frac{4\pi^2}{GM}\right)a^3 \implies T = \frac{2\pi}{\sqrt{GM}}a^{3/2}$$
