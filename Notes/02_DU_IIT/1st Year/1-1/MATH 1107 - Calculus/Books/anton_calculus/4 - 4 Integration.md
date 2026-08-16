# CHAPTER 4: INTEGRATION

> If a dragster moves with varying velocity over a certain time interval, it is possible to find the distance it travels during that time interval using techniques of calculus.

In this chapter we will begin with an overview of the problem of finding areas—we will discuss what the term "area" means, and we will outline two approaches to defining and calculating areas. Following this overview, we will discuss the Fundamental Theorem of Calculus, which is the theorem that relates the problems of finding tangent lines and areas, and we will discuss techniques for calculating areas. We will then use the ideas in this chapter to define the average value of a function, to continue our study of rectilinear motion, and to examine some consequences of the chain rule in integral calculus.

---

## 4.1 AN OVERVIEW OF THE AREA PROBLEM

### THE AREA PROBLEM & THE METHOD OF EXHAUSTION

Formulas for the areas of polygons were known in early civilizations, but curved boundaries presented major challenges. Archimedes made the first real progress by inscribing regular polygons in a circle and letting the number of sides $n \to \infty$ (**method of exhaustion**).

> **Archimedes (287 B.C.–212 B.C.)**  
> Greatest mathematician of antiquity. Developed the method of exhaustion for calculating areas and volumes, approximated $\pi$ ($3\frac{10}{71} < \pi < 3\frac{1}{7}$), founded hydrostatics ("Eureka!"), and discovered laws of levers.

> **4.1.1 THE AREA PROBLEM**  
> Given a function $f$ that is continuous and nonnegative on an interval $[a, b]$, find the area between the graph of $f$ and the interval $[a, b]$ on the $x$-axis.

### THE RECTANGLE METHOD FOR FINDING AREAS
Divide $[a, b]$ into $n$ equal subintervals of width $\Delta x = (b - a)/n$. Construct approximating rectangles of height $f(x_k^*)$ over each subinterval:
$$A = \lim_{n \to +\infty} A_n$$
For $f(x) = x^2$ on $[0, 1]$ using right endpoints:
$$A_n = \sum_{k=1}^n \left(\frac{k}{n}\right)^2 \frac{1}{n} = \frac{1}{n^3}\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6n^3} \implies \lim_{n \to \infty} A_n = \frac{1}{3}$$

### THE ANTIDERIVATIVE METHOD FOR FINDING AREAS
If $A(x)$ is the area under $y = f(x)$ from $a$ to $x$:
$$A'(x) = f(x) \tag{2}$$
Thus, $A(x)$ is an **antiderivative** of $f(x)$.

---

### QUICK CHECK EXERCISES 4.1
*(See page 271 for answers.)*
1. Region below $f(x) = \sqrt{1 - x^2}$ on $[-1, 1]$: (a) Area is semicircle $\pi/2$ (b) Rectangle estimate.  
2. $A_n = 2 + 2/n \implies A = \lim_{n \to \infty} A_n = 2$.  
3. Area under $y = x^2$ on $[0, 3]$ is $A(3) = \frac{1}{3}(3^3) = 9$.  
4. $f(x) = x \implies A(x) = x^2/2 \implies A'(x) = x = f(x)$.  
5. $A(x) = x + \sin x \implies f(x) = A'(x) = 1 + \cos x$.

---

## 4.2 THE INDEFINITE INTEGRAL

### ANTIDERIVATIVES & THE INDEFINITE INTEGRAL

> **4.2.1 DEFINITION**  
> A function $F$ is called an **antiderivative** of $f$ on an open interval if $F'(x) = f(x)$ for all $x$ in the interval.

> **4.2.2 THEOREM**  
> If $F(x)$ is any antiderivative of $f(x)$ on an open interval, then every antiderivative of $f(x)$ on that interval can be expressed in the form
> $$\int f(x) dx = F(x) + C$$
> where $C$ is an arbitrary **constant of integration**, and $\int$ is the **integral sign** (introduced by Leibniz in 1675).

### INTEGRATION FORMULAS (Table 4.2.1)
$$\begin{aligned}
\int x^r dx &= \frac{x^{r+1}}{r+1} + C \quad (r \neq -1) & \int dx &= x + C \\
\int \cos x dx &= \sin x + C & \int \sin x dx &= -\cos x + C \\
\int \sec^2 x dx &= \tan x + C & \int \csc^2 x dx &= -\cot x + C \\
\int \sec x \tan x dx &= \sec x + C & \int \csc x \cot x dx &= -\csc x + C
\end{aligned}$$

### PROPERTIES OF INDEFINITE INTEGRALS

> **4.2.3 THEOREM**  
> (a) $\int cf(x) dx = c\int f(x) dx$  
> (b) $\int [f(x) + g(x)] dx = \int f(x) dx + \int g(x) dx$  
> (c) $\int [f(x) - g(x)] dx = \int f(x) dx - \int g(x) dx$

### DIFFERENTIAL EQUATIONS & SLOPE FIELDS
* **Initial-Value Problem:** $\frac{dy}{dx} = f(x), \; y(x_0) = y_0$.
* **Slope Field (Direction Field):** A visual field of tangent line segments indicating the direction of integral curves at grid points.

---

### QUICK CHECK EXERCISES 4.2
*(See page 281 for answers.)*
1. $F'(x) = f(x)$.  
2. (a) $\int \frac{1}{2\sqrt{x}} dx = \sqrt{x} + C$ (b) $\int \cos x dx = \sin x + C$.  
3. (a) $\int (x^3 + x + 5)dx = \frac{1}{4}x^4 + \frac{1}{2}x^2 + 5x + C$ (b) $\int (\sec^2 x - \csc x \cot x)dx = \tan x + \csc x + C$.  
4. $f(x) = 2x + 1$; $G(x) = x^2 + x + 3$.  
5. Slope at $(0, 5)$ is 0; slope at $(-4, 1)$ is $-8/12 = -2/3$.

---

## 4.3 INTEGRATION BY SUBSTITUTION

### $u$-SUBSTITUTION METHOD

Based on the chain rule:
$$\int f(g(x))g'(x) dx = \int f(u) du = F(u) + C \quad \text{where } u = g(x), \; du = g'(x)dx$$

#### Guidelines for $u$-Substitution:
1. Choose $u = g(x)$ (typically the "inside" function).
2. Compute $du = g'(x)dx$.
3. Express the entire integral in terms of $u$ and $du$.
4. Evaluate the resulting integral in $u$.
5. Replace $u$ by $g(x)$ to obtain the final antiderivative in $x$.

#### Examples:
* $\int (x^2 + 1)^{50}(2x) dx = \frac{(x^2 + 1)^{51}}{51} + C$
* $\int \cos(5x) dx = \frac{1}{5}\sin(5x) + C$
* $\int x^2\sqrt{x - 1} dx$ ($u = x - 1 \implies x = u + 1$): $\int (u + 1)^2 u^{1/2} du = \frac{2}{7}(x-1)^{7/2} + \frac{4}{5}(x-1)^{5/2} + \frac{2}{3}(x-1)^{3/2} + C$.
* $\int \cos^3 x dx = \int (1 - \sin^2 x)\cos x dx = \sin x - \frac{1}{3}\sin^3 x + C$.

---

### QUICK CHECK EXERCISES 4.3
*(See page 287 for answers.)*
1. (a) $u = 1 + x^3, du = 3x^2 dx$ (b) $u = x^2, du = 2x dx$ (c) $u = 1 + 9x^2, du = 18x dx$.  
2. (a) $u^{-1/3}$ (b) $-u$ (c) $2\sqrt[3]{u}$.

---

## 4.4 THE DEFINITION OF AREA AS A LIMIT; SIGMA NOTATION

### SIGMA NOTATION & PROPERTIES

$$\sum_{k=m}^n f(k) = f(m) + f(m+1) + \dots + f(n)$$

> **4.4.1 & 4.4.2 THEOREMS (Sum Formulas)**  
> * $\sum_{k=1}^n c a_k = c \sum_{k=1}^n a_k$  
> * $\sum_{k=1}^n (a_k \pm b_k) = \sum a_k \pm \sum b_k$  
> * $\sum_{k=1}^n 1 = n$  
> * $\sum_{k=1}^n k = \frac{n(n+1)}{2}$  
> * $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$  
> * $\sum_{k=1}^n k^3 = \left[\frac{n(n+1)}{2}\right]^2$

---

### PRECISE DEFINITION OF AREA AND NET SIGNED AREA

> **4.4.3 & 4.4.5 DEFINITIONS (Area and Net Signed Area)**  
> For a continuous function $f$ on $[a, b]$, partition $[a, b]$ into $n$ equal subintervals of width $\Delta x = \frac{b - a}{n}$:
> $$\text{Net Signed Area } A = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*) \Delta x$$
> where sample points $x_k^*$ can be chosen as:
> * Left endpoint: $x_k^* = a + (k - 1)\Delta x$
> * Right endpoint: $x_k^* = a + k\Delta x$
> * Midpoint: $x_k^* = a + (k - \frac{1}{2})\Delta x$

---

### QUICK CHECK EXERCISES 4.4
*(See page 299 for answers.)*
1. (a) $\frac{1}{2k}; \frac{1}{2(j+1)}$ (b) $\sum_{k=1}^5 10^k$.  
2. Closed forms: (a) $\frac{n(n+1)}{2}$ (b) $3n(n+1) + n$ (c) $\frac{n(n+1)(2n+1)}{6}$.  
3. Partition of $[1, 3]$ into $n = 4$: (a) $\Delta x = 0.5$ (b) Left: 1, 1.5, 2, 2.5 (c) Mid: 1.25, 1.75, 2.25, 2.75 (d) Right: 1.5, 2, 2.5, 3.  
4. Left endpoint approximation for $x^2$ on $[1, 3]$: 6.75.  
5. $\lim_{n \to \infty} \sum \frac{6k + 1}{n^2} = 3$.

---

## 4.5 THE DEFINITE INTEGRAL

### RIEMANN SUMS & DEFINITION OF INTEGRABILITY

> **4.5.1 DEFINITION (The Definite Integral / Riemann Integral)**  
> Let $f$ be defined on a finite closed interval $[a, b]$. If a partition $P$ has subinterval lengths $\Delta x_k$ and mesh size $\max \Delta x_k$, then
> $$\int_a^b f(x) dx = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n f(x_k^*) \Delta x_k$$
> provided this limit exists independently of the choice of partition and sample points $x_k^*$.

> **Georg Friedrich Bernhard Riemann (1826–1866)**  
> Master mathematician whose rigorous formulation of the integral and groundbreaking contributions to non-Euclidean geometry laid the foundation for modern physics and general relativity.

> **4.5.2 THEOREM**  
> If $f$ is continuous on $[a, b]$, then $f$ is integrable on $[a, b]$, and $\int_a^b f(x)dx$ equals the net signed area.

### PROPERTIES OF THE DEFINITE INTEGRAL

> **4.5.3 & 4.5.4 DEFINITIONS & THEOREMS**  
> * $\int_a^a f(x) dx = 0$  
> * $\int_b^a f(x) dx = -\int_a^b f(x) dx$  
> * $\int_a^b c f(x) dx = c\int_a^b f(x) dx$  
> * $\int_a^b [f(x) \pm g(x)] dx = \int_a^b f(x) dx \pm \int_a^b g(x) dx$  
> * $\int_a^b f(x) dx = \int_a^c f(x) dx + \int_c^b f(x) dx$  
> * If $f(x) \ge g(x)$ on $[a, b]$, then $\int_a^b f(x) dx \ge \int_a^b g(x) dx$.

> **4.5.8 THEOREM (Boundedness & Discontinuities)**  
> If $f$ is bounded on $[a, b]$ with finitely many discontinuities, then $f$ is integrable on $[a, b]$. If $f$ is unbounded on $[a, b]$, $f$ is not integrable.

---

### QUICK CHECK EXERCISES 4.5
*(See page 309 for answers.)*
1. Partition analysis on $[2, 7]$: $n = 4$, mesh $= 2$.  
2. Riemann sum for $2x - 8$: 3.  
3. Geometric evaluation: $\int_2^7 (2x - 8)dx = 5$.  
4. Integral properties: (a) $-10$ (b) 3 (c) 0 (d) $-12$.

---

## 4.6 THE FUNDAMENTAL THEOREM OF CALCULUS

### THE FUNDAMENTAL THEOREM OF CALCULUS (PARTS 1 & 2)

> **4.6.1 THEOREM (Fundamental Theorem of Calculus, Part 1)**  
> If $f$ is continuous on $[a, b]$ and $F$ is any antiderivative of $f$ on $[a, b]$, then
> $$\int_a^b f(x) dx = F(b) - F(a) = [F(x)]_a^b \tag{2}$$

> **4.6.2 THEOREM (Mean-Value Theorem for Integrals)**  
> If $f$ is continuous on $[a, b]$, then there exists at least one point $x^* \in [a, b]$ such that
> $$\int_a^b f(x) dx = f(x^*)(b - a) \tag{8}$$

> **4.6.3 THEOREM (Fundamental Theorem of Calculus, Part 2)**  
> If $f$ is continuous on an interval, then for any $a$ in the interval:
> $$\frac{d}{dx}\left[\int_a^x f(t) dt\right] = f(x) \tag{11}$$

### TOTAL AREA VS NET SIGNED AREA
$$\text{Total Area} = \int_a^b |f(x)| dx$$

### INTEGRATING A RATE OF CHANGE
$$\int_{t_1}^{t_2} F'(t) dt = F(t_2) - F(t_1)$$
* Displacement: $\int_{t_1}^{t_2} v(t) dt = s(t_2) - s(t_1)$
* Population growth: $\int_{t_1}^{t_2} P'(t) dt = P(t_2) - P(t_1)$

---

### QUICK CHECK EXERCISES 4.6
*(See page 322 for answers.)*
1. (a) $F(b) - F(a)$ (b) $F(b) - F(a)$ (c) $f(x)$.  
2. (a) $\int_0^2 (3x^2 - 2x)dx = [x^3 - x^2]_0^2 = 4$ (b) $\int_{-\pi}^\pi \cos x dx = 0$.  
3. 0.  
4. $\int_2^4 25t dt = [12.5t^2]_2^4 = 200 - 50 = 150\text{ ft}^2$.

---

## 4.7 RECTILINEAR MOTION REVISITED USING INTEGRATION

### DISPLACEMENT VS DISTANCE TRAVELED
* **Displacement:** $\int_{t_0}^{t_1} v(t) dt = s(t_1) - s(t_0)$ (Net signed area of $v(t)$).
* **Distance Traveled:** $\int_{t_0}^{t_1} |v(t)| dt$ (Total area under $|v(t)|$).

### CONSTANT ACCELERATION EQUATIONS
If $a(t) = a = \text{const}$:
$$v(t) = v_0 + at \tag{11}$$
$$s(t) = s_0 + v_0 t + \frac{1}{2}at^2 \tag{10}$$

### FREE-FALL MODEL
Taking upward as positive ($a = -g$, $g = 32\text{ ft/s}^2$ or $9.8\text{ m/s}^2$):
$$v(t) = v_0 - gt \tag{16}$$
$$s(t) = s_0 + v_0 t - \frac{1}{2}gt^2 \tag{15}$$

#### Examples:
* **Astrodome Throw:** $v_0 = 100\text{ ft/s}, s_0 = 7\text{ ft} \implies \text{max height} = 163.25\text{ ft}$ (does not hit 208 ft roof).
* **Penny from Empire State Building ($1250\text{ ft}$):** Hits ground at $t = 25/\sqrt{8} \approx 8.8\text{ s}$ with speed $200\sqrt{2}\text{ ft/s} \approx 192.8\text{ mi/h}$.

---

### QUICK CHECK EXERCISES 4.7
*(See page 331 for answers.)*
1. $s(t) = t^2 + t + 2$.  
2. $v(t) = 6 - 2t$.  
3. Displacement $= 3/2$; Distance $= 5/2$.  
4. $v^2 = 2gs \implies 48^2 = 2(32)h \implies h = 36\text{ ft}$.

---

## 4.8 AVERAGE VALUE OF A FUNCTION AND ITS APPLICATIONS

### DEFINITION OF AVERAGE VALUE

> **4.8.1 DEFINITION**  
> If $f$ is continuous on $[a, b]$, the **average value (mean value)** of $f$ on $[a, b]$ is
> $$f_{\text{ave}} = \frac{1}{b - a}\int_a^b f(x) dx \tag{3}$$

* Geometrically, $f_{\text{ave}}$ is the height of a rectangle over $[a, b]$ having the same area as the area under $y = f(x)$.
* Average velocity over $[t_0, t_1]$ equals the average value of the velocity function $v(t)$.

---

### QUICK CHECK EXERCISES 4.8
*(See page 336 for answers.)*
1. $\frac{1}{n}\sum_{k=1}^n a_k$.  
2. $\frac{1}{b - a}\int_a^b f(x)dx$.  
3. $f(x^*)$.  
4. $f_{\text{ave}} = \frac{1}{2}\int_1^3 4x^3 dx = \frac{1}{2}[x^4]_1^3 = \frac{80}{2} = 40$.

---

## 4.9 EVALUATING DEFINITE INTEGRALS BY SUBSTITUTION

### TWO METHODS FOR DEFINITE INTEGRALS BY SUBSTITUTION
* **Method 1 (Back-substitution):** Find indefinite antiderivative in terms of $x$, then evaluate between original limits $a$ and $b$.
* **Method 2 (Transform limits):**
  $$\int_a^b f(g(x))g'(x) dx = \int_{g(a)}^{g(b)} f(u) du \tag{Theorem 4.9.1}$$

### INTEGRALS OF SYMMETRIC FUNCTIONS OVER $[-a, a]$
* If $f$ is **odd** ($f(-x) = -f(x)$): $\int_{-a}^a f(x) dx = 0$.
* If $f$ is **even** ($f(-x) = f(x)$): $\int_{-a}^a f(x) dx = 2\int_0^a f(x) dx$.

---

### QUICK CHECK EXERCISES 4.9
*(See page 342 for answers.)*
1. $F(g(b)) - F(g(a))$.  
2. (a) $\int_1^9 u^3 du$ (b) $\int_1^5 \frac{1}{2\sqrt{u}} du$.  
3. (a) $2/3$ (b) $3/4$.

---

## CHAPTER 4 REVIEW EXERCISES
Exercises 1–78 reviewing antiderivatives, definite integrals, FTC Parts 1 & 2, area/total area calculations, $u$-substitution, rectilinear motion, average value, and differential equations.

---

## CHAPTER 4 MAKING CONNECTIONS
Riemann sum approximations with unequal subintervals, telescoping Riemann sums, and generalized substitution formulas.
