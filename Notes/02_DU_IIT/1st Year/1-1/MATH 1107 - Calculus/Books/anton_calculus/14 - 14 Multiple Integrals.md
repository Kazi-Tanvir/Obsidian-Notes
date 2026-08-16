# CHAPTER 14: MULTIPLE INTEGRALS

> Finding the areas of complex surfaces such as those used in the design of the Denver International Airport require integration methods studied in this chapter.

In this chapter we extend the definite integral to functions of two and three variables. We study double integrals over rectangles and general regions, double integrals in polar coordinates, surface area for Cartesian and parametric surfaces, triple integrals in rectangular, cylindrical, and spherical coordinates, general changes of variables via Jacobians, and physical applications including mass, centers of gravity, moments of inertia, and the Theorem of Pappus.

---

## 14.1 DOUBLE INTEGRALS

### VOLUME UNDER A SURFACE & DOUBLE INTEGRAL DEFINITION

> **14.1.2 & 14.1.4 DEFINITIONS**
> The **double integral** of $f(x, y)$ over a region $R$ is defined as the limit of Riemann sums:
> $$\iint_R f(x, y)\,dA = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta A_k \tag{4}$$
> * If $f(x, y) \ge 0$, $\iint_R f(x, y)\,dA = \text{Volume under } z = f(x, y) \text{ above } R$.
> * If $f(x, y)$ takes both signs, the double integral represents the **net signed volume**.

---

### FUBINI’S THEOREM (RECTANGULAR REGIONS)

> **14.1.3 THEOREM (Fubini's Theorem)**
> Let $R = [a, b] \times [c, d]$. If $f(x, y)$ is continuous on $R$:
> $$\iint_R f(x, y)\,dA = \int_c^d \int_a^b f(x, y)\,dx\,dy = \int_a^b \int_c^d f(x, y)\,dy\,dx \tag{6–7}$$

* **Special Separable Integrand:** If $f(x, y) = g(x)h(y)$, then $\iint_R f(x, y)\,dA = \left(\int_a^b g(x)\,dx\right)\left(\int_c^d h(y)\,dy\right)$.
* **Average Value:** $f_{\text{ave}} = \frac{1}{\text{Area}(R)}\iint_R f(x, y)\,dA$.

---

### QUICK CHECK EXERCISES 14.1
*(See page 1008 for answers.)*
1. $\lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*, y_k^*)\Delta A_k$.
2. $2 \le x \le 4, \; 1 \le y \le 5$.
3. $\int_1^5 (56 - 12y + 2y^2)\,dy$.
4. Volume $V = \int_1^{e^2} \int_0^4 \frac{x}{y}\,dx\,dy = \int_1^{e^2} \frac{8}{y}\,dy = 8[\ln y]_1^{e^2} = 16$.

---

## 14.2 DOUBLE INTEGRALS OVER NONRECTANGULAR REGIONS

### TYPE I AND TYPE II REGIONS

> **14.2.1 DEFINITION**
> * **Type I Region:** $a \le x \le b, \quad g_1(x) \le y \le g_2(x)$
>   $$\iint_R f(x, y)\,dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy\,dx \tag{3}$$
> * **Type II Region:** $c \le y \le d, \quad h_1(y) \le x \le h_2(y)$
>   $$\iint_R f(x, y)\,dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x, y)\,dx\,dy \tag{4}$$

* **Area as a Double Integral (14.2.7):**
  $$\text{Area}(R) = \iint_R 1\,dA = \iint_R dA$$
* **Reversing Order of Integration:** Changing from Type I to Type II (or vice versa) can evaluate integrals with non-elementary anti-derivatives (e.g., $\int_0^2 \int_{y/2}^1 e^{x^2}dx\,dy = \int_0^1 \int_0^{2x} e^{x^2}dy\,dx = e - 1$).

---

### QUICK CHECK EXERCISES 14.2
*(See page 1018 for answers.)*
1. (a) $\int_1^5 (\frac{1}{4}y^4 - 16y)\,dy$; (b) $\int_1^5 (\frac{3}{4}x^4 - 12x^2)\,dx$.
2. (a) $\int_0^3 \int_0^{-\frac{4}{3}x+4} f(x, y)\,dy\,dx$; (b) $\int_0^4 \int_0^{-\frac{3}{4}y+3} f(x, y)\,dx\,dy$.
3. $\int_0^3 \int_x^{-\frac{1}{3}x+4} dy\,dx = 6$.
4. $\int_{-2}^1 \int_{x^2}^{2-x} (1 + 2y)\,dy\,dx = 18.9$.

---

## 14.3 DOUBLE INTEGRALS IN POLAR COORDINATES

### POLAR DOUBLE INTEGRALS

> **14.3.3 THEOREM**
> For a simple polar region $R = \{ (r, \theta) : \alpha \le \theta \le \beta, \; r_1(\theta) \le r \le r_2(\theta) \}$:
> $$\iint_R f(r, \theta)\,dA = \int_\alpha^\beta \int_{r_1(\theta)}^{r_2(\theta)} f(r, \theta)\, r\,dr\,d\theta \tag{7}$$
> *(Note the extra factor of $r$ in the area element $dA = r\,dr\,d\theta$).*

* **Conversion from Rectangular to Polar:**
  $$\iint_R f(x, y)\,dA = \iint_R f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta \tag{9}$$

---

### QUICK CHECK EXERCISES 14.3
*(See page 1025 for answers.)*
1. $1 \le r \le 2\sin\theta, \; \pi/6 \le \theta \le 5\pi/6$.
2. $\int_0^{\pi/2} \int_3^{10} f(r, \theta)\,r\,dr\,d\theta$.
3. $V = \int_0^\pi \int_0^{\sin\theta} \sqrt{1 - r^2}\,r\,dr\,d\theta$.
4. $\int_0^{\pi/4} \int_1^{\sec\theta} \frac{1}{r}\,dr\,d\theta$.

---

## 14.4 SURFACE AREA; PARAMETRIC SURFACES

### EXPLICIT SURFACE AREA: $z = f(x, y)$
$$S = \iint_R \sqrt{\left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2 + 1}\,dA \tag{2}$$

---

### PARAMETRIC SURFACES & SURFACE AREA
* **Parametric Surface:** $\mathbf{r}(u, v) = x(u, v)\mathbf{i} + y(u, v)\mathbf{j} + z(u, v)\mathbf{k}$.
* **Tangent Vectors & Normal:**
  $$\mathbf{r}_u = \frac{\partial \mathbf{r}}{\partial u}, \quad \mathbf{r}_v = \frac{\partial \mathbf{r}}{\partial v}, \quad \mathbf{n} = \frac{\mathbf{r}_u \times \mathbf{r}_v}{\|\mathbf{r}_u \times \mathbf{r}_v\|}$$
* **Parametric Surface Area (14.4.12):**
  $$S = \iint_R \|\mathbf{r}_u \times \mathbf{r}_v\|\,dA_{uv}$$

---

### QUICK CHECK EXERCISES 14.4
*(See page 1039 for answers.)*
1. $\sqrt{(\partial z/\partial x)^2 + (\partial z/\partial y)^2 + 1}$.
2. (a) Circles of radius $1-u$ centered at $(1-u, 0, 0)$ parallel to $yz$-plane; (b) Line segments joining $(1, \cos v, \sin v)$ to origin $(0, 0, 0)$.
3. $\mathbf{r}_u = -\mathbf{i} - \cos v\mathbf{j} - \sin v\mathbf{k}, \; \mathbf{r}_v = -(1-u)\sin v\mathbf{j} + (1-u)\cos v\mathbf{k}$.
4. $\mathbf{n} = \frac{1}{\sqrt{8}}(-2\mathbf{i} + \sqrt{3}\mathbf{j} + \mathbf{k})$.
5. $S = \iint_R \|\mathbf{r}_u \times \mathbf{r}_v\|\,dA$.

---

## 14.5 TRIPLE INTEGRALS

### DEFINITION & FUBINI’S THEOREM (BOX REGIONS)

> **14.5.1 THEOREM (Triple Integral over a Box)**
> Over box $G = [a, b] \times [c, d] \times [k, l]$:
> $$\iiint_G f(x, y, z)\,dV = \int_a^b \int_c^d \int_k^l f(x, y, z)\,dz\,dy\,dx \tag{2}$$
> *(Any of the 6 integration orders may be used).*

* **Simple $xy$-Solid:** $G = \{ (x, y, z) : (x, y) \in R, \; g_1(x, y) \le z \le g_2(x, y) \}$
  $$\iiint_G f(x, y, z)\,dV = \iint_R \left[ \int_{g_1(x, y)}^{g_2(x, y)} f(x, y, z)\,dz \right] dA \tag{3}$$
* **Volume of Solid $G$:** $V(G) = \iiint_G 1\,dV$.

---

### QUICK CHECK EXERCISES 14.5
*(See page 1048 for answers.)*
1. $3 \le x \le 6, \; 1 \le y \le 5, \; 2 \le z \le 4$.
2. (a) $\int_0^4 \int_0^{\sqrt{4-y}} \int_{y+x^2}^4 f\,dz\,dx\,dy$; (b) $\int_0^2 \int_0^{4-x^2} \int_{y+x^2}^4 f\,dz\,dy\,dx$; (c) $\int_0^2 \int_{x^2}^4 \int_0^{z-x^2} f\,dy\,dz\,dx$.
3. $V = \frac{128}{15}$.

---

## 14.6 TRIPLE INTEGRALS IN CYLINDRICAL AND SPHERICAL COORDINATES

### CYLINDRICAL COORDINATES ($dV = r\,dz\,dr\,d\theta$)

> **14.6.1 THEOREM**
> $$\iiint_G f(r, \theta, z)\,dV = \int_{\theta_1}^{\theta_2} \int_{r_1(\theta)}^{r_2(\theta)} \int_{g_1(r, \theta)}^{g_2(r, \theta)} f(r, \theta, z)\,r\,dz\,dr\,d\theta \tag{5}$$

---

### SPHERICAL COORDINATES ($dV = \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$)

> **14.6.9 THEOREM**
> $$\iiint_G f(\rho, \theta, \phi)\,dV = \int_{\theta_1}^{\theta_2} \int_{\phi_1}^{\phi_2} \int_{\rho_1(\theta, \phi)}^{\rho_2(\theta, \phi)} f(\rho, \theta, \phi)\,\rho^2\sin\phi\,d\rho\,d\phi\,d\theta \tag{9}$$

#### Common Solid Limits in Spherical Coordinates:
* **Full Sphere of radius $\rho_0$:** $0 \le \rho \le \rho_0, \; 0 \le \phi \le \pi, \; 0 \le \theta \le 2\pi$
* **Cone $\phi = \phi_0$ inside Sphere:** $0 \le \rho \le \rho_0, \; 0 \le \phi \le \phi_0, \; 0 \le \theta \le 2\pi$

---

### QUICK CHECK EXERCISES 14.6
*(See page 1058 for answers.)*
1. (a) $V = \frac{1}{2}(3^2 - 1^2)(\frac{\pi}{2} - \frac{\pi}{6})(5) = \frac{20\pi}{3}$; (b) $V = \frac{1}{3}(3^3 - 1^3)(\frac{\pi}{2} - \frac{\pi}{6})(1 - \cos(\pi/3)) = \frac{13\pi}{9}$.
2. (a) $\int_0^{2\pi}\int_0^{\sqrt{3}}\int_1^{\sqrt{4-r^2}} r\,dz\,dr\,d\theta$; (b) $\int_0^{2\pi}\int_0^{\sqrt{3}}\int_1^{\sqrt{4-r^2}} \frac{rz}{r^2+z^2}\,dz\,dr\,d\theta$.
3. (a) $\int_0^{2\pi}\int_0^{\pi/3}\int_{\sec\phi}^2 \rho^2\sin\phi\,d\rho\,d\phi\,d\theta$; (b) $\int_0^{2\pi}\int_0^{\pi/3}\int_{\sec\phi}^2 \rho\cos\phi\sin\phi\,d\rho\,d\phi\,d\theta$.

---

## 14.7 CHANGE OF VARIABLES IN MULTIPLE INTEGRALS; JACOBIANS

### THE JACOBIAN DETERMINANT (14.7.1 & 14.7.3)
* **In 2 Dimensions:**
  $$J(u, v) = \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}$$
  * Polar coordinates: $\frac{\partial(x, y)}{\partial(r, \theta)} = r$.
* **In 3 Dimensions:**
  $$J(u, v, w) = \frac{\partial(x, y, z)}{\partial(u, v, w)} = \begin{vmatrix} x_u & x_v & x_w \\ y_u & y_v & y_w \\ z_u & z_v & z_w \end{vmatrix}$$
  * Cylindrical coordinates: $J = r$.
  * Spherical coordinates: $J = \rho^2\sin\phi$.

### CHANGE OF VARIABLES FORMULA

> **14.7.2 & 14.7.4 THEOREMS**
> $$\iint_R f(x, y)\,dx\,dy = \iint_S f(x(u, v), y(u, v)) \left|\frac{\partial(x, y)}{\partial(u, v)}\right| du\,dv \tag{9}$$
> $$\iiint_R f(x, y, z)\,dx\,dy\,dz = \iiint_S f(x(u, v, w), y(u, v, w), z(u, v, w)) \left|\frac{\partial(x, y, z)}{\partial(u, v, w)}\right| du\,dv\,dw \tag{14}$$

* **Inverse Property:** $\frac{\partial(x, y)}{\partial(u, v)} = \frac{1}{\frac{\partial(u, v)}{\partial(x, y)}}$.

---

### QUICK CHECK EXERCISES 14.7
*(See page 1071 for answers.)*
1. (a) Parallelogram with vertices $(1, 3), (-3, 5), (-1, 11), (3, 9)$; (b) $u = \frac{1}{7}(x+2y), v = \frac{1}{7}(y-3x)$.
2. $S$ is region in $uv$-plane, $R = T(S)$ in $xy$-plane.
3. (a) $J = 1(1) - (-2)(3) = 7$; (b) $\int_0^2 \int_1^3 7 e^{7u}\,du\,dv$.
4. $\frac{\partial(x, y, z)}{\partial(u, v, w)} = 2vw$.

---

## 14.8 CENTERS OF GRAVITY USING MULTIPLE INTEGRALS

### 2D LAMINAS (MASS, MOMENTS, AND CENTROID)
* **Mass:** $M = \iint_R \delta(x, y)\,dA \tag{3}$
* **First Moments:** $M_y = \iint_R x\delta(x, y)\,dA, \quad M_x = \iint_R y\delta(x, y)\,dA$
* **Center of Gravity:**
  $$\bar{x} = \frac{M_y}{M} = \frac{\iint_R x\delta(x, y)\,dA}{\iint_R \delta(x, y)\,dA}, \quad \bar{y} = \frac{M_x}{M} = \frac{\iint_R y\delta(x, y)\,dA}{\iint_R \delta(x, y)\,dA} \tag{9–10}$$
* **Centroid ($\delta = \text{constant}$):** $\bar{x} = \frac{1}{\text{Area}(R)}\iint_R x\,dA, \quad \bar{y} = \frac{1}{\text{Area}(R)}\iint_R y\,dA$.
* **Moments of Inertia:**
  $$I_x = \iint_R y^2\delta\,dA, \quad I_y = \iint_R x^2\delta\,dA, \quad I_z = I_0 = \iint_R (x^2+y^2)\delta\,dA = I_x + I_y$$

---

### 3D SOLIDS
* **Mass:** $M = \iiint_G \delta(x, y, z)\,dV \tag{15}$
* **Center of Gravity:**
  $$\bar{x} = \frac{1}{M}\iiint_G x\delta\,dV, \quad \bar{y} = \frac{1}{M}\iiint_G y\delta\,dV, \quad \bar{z} = \frac{1}{M}\iiint_G z\delta\,dV \tag{16}$$
* **Moments of Inertia:**
  $$I_x = \iiint_G (y^2+z^2)\delta\,dV, \quad I_y = \iiint_G (x^2+z^2)\delta\,dV, \quad I_z = \iiint_G (x^2+y^2)\delta\,dV$$

---

### THEOREM OF PAPPUS
$$\text{Volume} = (\text{Area of } R) \times (\text{distance traveled by centroid}) = 2\pi \bar{r} A$$

---

### QUICK CHECK EXERCISES 14.8
*(See page 1080 for answers.)*
1. $M = \iint_R \delta(x, y)\,dA$.
2. First moment about $y$-axis; $M_y = \iint_R x\delta(x, y)\,dA$.
3. Centroid is $(\bar{x}, \bar{y}) = \left(\frac{5}{14}, \frac{32}{35}\right)$.

---

## CHAPTER 14 MAKING CONNECTIONS: THE GAUSSIAN INTEGRAL

> **Evaluation of $\int_0^{+\infty} e^{-x^2}dx$:**
> Let $I = \int_0^{+\infty} e^{-x^2}dx$. Then:
> $$I^2 = \int_0^{+\infty} \int_0^{+\infty} e^{-(x^2+y^2)}\,dx\,dy = \int_0^{\pi/2} \int_0^{+\infty} e^{-r^2} r\,dr\,d\theta = \frac{\pi}{2}\left[-\frac{1}{2}e^{-r^2}\right]_0^\infty = \frac{\pi}{4}$$
> $$\implies I = \int_0^{+\infty} e^{-x^2}dx = \frac{\sqrt{\pi}}{2} \quad \text{and} \quad \int_{-\infty}^{+\infty} e^{-x^2}dx = \sqrt{\pi}$$
