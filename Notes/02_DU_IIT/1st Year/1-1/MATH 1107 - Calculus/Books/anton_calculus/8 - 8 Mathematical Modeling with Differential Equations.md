# CHAPTER 8: MATHEMATICAL MODELING WITH DIFFERENTIAL EQUATIONS

> In the 1920s, excavation of an archeological site in Folsom, New Mexico, uncovered a collection of prehistoric stone spearheads now known as "Folsom points." In 1950, carbon dating of charred bison bones found nearby confirmed that human hunters lived in the area between 9000 B.C. and 8000 B.C.

Many fundamental laws of science and engineering can be expressed in terms of differential equations. In this chapter we will discuss important mathematical models involving differential equations, and methods for solving and approximating solutions of basic differential equations.

---

## 8.1 MODELING WITH DIFFERENTIAL EQUATIONS

### TERMINOLOGY
A **differential equation** is an equation involving one or more derivatives of an unknown function $y = y(x)$ or $y = y(t)$.
* The **order** of a differential equation is the order of the highest derivative that it contains.

| Differential Equation | Order |
| :--- | :---: |
| $\frac{dy}{dx} = 3y$ | 1 |
| $\frac{d^2y}{dx^2} - 6\frac{dy}{dx} + 8y = 0$ | 2 |
| $\frac{d^3y}{dt^3} - t\frac{dy}{dt} + (t^2 - 1)y = e^t$ | 3 |
| $y' - y = e^{2x}$ | 1 |
| $y'' + y' = \cos t$ | 2 |

### SOLUTIONS AND INITIAL-VALUE PROBLEMS
* A function $y = y(x)$ is a **solution** on an open interval if substitution into the equation satisfies it identically.
* A **general solution** contains arbitrary constants ($n$ arbitrary constants for an $n$th-order equation) representing a family of **integral curves**.
* An **initial condition** $y(x_0) = y_0$ isolates a single integral curve passing through $(x_0, y_0)$, forming an **initial-value problem (IVP)**.

#### Example 1
Solve the initial-value problem:
$$\frac{dy}{dx} - y = e^{2x}, \quad y(0) = 3$$
General solution is $y = e^{2x} + C e^x$. Setting $x = 0, y = 3 \implies 3 = 1 + C \implies C = 2$.
Thus, $y = e^{2x} + 2e^x$.

---

### CLASSICAL MODELS

1. **Uninhibited Population Growth:**
   $$\frac{dy}{dt} = ky, \quad y(0) = y_0 \quad (k > 0)$$
2. **Inhibited Population Growth (Logistic Model - P. F. Verhulst, 1838):**
   $$\frac{dy}{dt} = k\left(1 - \frac{y}{L}\right)y, \quad y(0) = y_0 \quad (L = \text{carrying capacity})$$
3. **Pharmacology (Drug Absorption in Bloodstream):**
   $$\frac{dy}{dt} = -ky, \quad y(0) = y_0 \quad (k > 0)$$
4. **Spread of Disease:**
   $$\frac{dy}{dt} = ky(L - y), \quad y(0) = y_0$$
5. **Newton's Law of Cooling:**
   $$\frac{dT}{dt} = k(T - T_e), \quad T(0) = T_0 \quad (k < 0, \; T_e = \text{ambient temperature})$$
6. **Vibrations of Springs (Hooke's Law & Newton's Second Law):**
   $$m\frac{d^2x}{dt^2} = -kx \implies m\frac{d^2x}{dt^2} + kx = 0, \quad x(0) = x_0, \; x'(0) = v_0$$

---

### QUICK CHECK EXERCISES 8.1
*(See page 568 for answers.)*
1. Matches: (a) $x\frac{dy}{dx} = y \implies y = Cx$; (b) $y'' = 4y \implies y = C_1 e^{2x} + C_2 e^{-2x}$; (c) $\frac{dy}{dx} = 2x \implies y = x^2 + C$; (d) $\frac{d^2y}{dx^2} = -4y \implies y = C_1\sin 2x + C_2\cos 2x$.
2. Order is 2; solution is $y = e^{2x} + 2xe^{2x}$.
3. $\frac{dy}{dx} = -\frac{x}{y}, \; y(0) = 1$.
4. $\frac{dT}{dt} = k(T - 68), \; T(0) = 36$.

---

## 8.2 SEPARATION OF VARIABLES

A first-order differential equation is **separable** if it can be written as:
$$h(y)\frac{dy}{dx} = g(x) \quad \iff \quad h(y)\,dy = g(x)\,dx \tag{1–2}$$

### SOLUTION PROCEDURE
1. Separate variables: $h(y)\,dy = g(x)\,dx$
2. Integrate both sides: $\int h(y)\,dy = \int g(x)\,dx$
3. Solve $H(y) = G(x) + C$ explicitly for $y$ if possible.

#### Example 1
$$\frac{dy}{dx} = -4xy^2, \quad y(0) = 1 \implies \int \frac{dy}{y^2} = \int -4x\,dx \implies -\frac{1}{y} = -2x^2 + C \implies y = \frac{1}{2x^2 + 1}$$

#### Example 2
$$(4y - \cos y)\frac{dy}{dx} = 3x^2, \quad y(0) = 0 \implies 2y^2 - \sin y = x^3$$

---

### EXPONENTIAL GROWTH AND DECAY MODELS

> **8.2.1 DEFINITION**
> * **Growth Model:** $\frac{dy}{dt} = ky \implies y(t) = y_0 e^{kt} \quad (k > 0)$
> * **Decay Model:** $\frac{dy}{dt} = -ky \implies y(t) = y_0 e^{-kt} \quad (k > 0)$

* **Relative Growth/Decay Rate:** $k = \frac{dy/dt}{y}$
* **Doubling Time & Half-Life:**
  $$T = \frac{\ln 2}{k} \tag{18}$$
* **Rule of 70:** Doubling time / half-life $\approx \frac{70}{\text{percentage rate}}$.

---

### RADIOACTIVE DECAY & CARBON DATING
* **Carbon-14 Half-Life:** $T \approx 5730\text{ years} \implies k = \frac{\ln 2}{5730} \approx 0.000121\text{ yr}^{-1}$.
  $$y(t) = y_0 e^{-0.000121t}$$
* **Age from remaining fraction $y(t)/y_0$:**
  $$t = -\frac{1}{0.000121}\ln\left(\frac{y(t)}{y_0}\right)$$

#### Example 7 (The Shroud of Turin)
Fibers contained $92\%$ to $93\%$ of original C-14 in 1988:
$$t \approx -\frac{\ln(0.93)}{0.000121} \approx 600\text{ yr}, \quad t \approx -\frac{\ln(0.92)}{0.000121} \approx 689\text{ yr} \implies \text{Origin between 1299 A.D. and 1388 A.D.}$$

---

### LOGISTIC GROWTH SOLUTION
$$\frac{dy}{dt} = k\left(1 - \frac{y}{L}\right)y \implies y(t) = \frac{y_0 L}{y_0 + (L - y_0)e^{-kt}}$$
As $t \to +\infty$, $\lim_{t \to +\infty} y(t) = L$.

---

### QUICK CHECK EXERCISES 8.2
*(See page 579 for answers.)*
1. Step 1: $h(y)dy = g(x)dx$; Step 2: $\int h(y)dy = \int g(x)dx$; Step 3: $H(y) = G(x) + C$.
2. (a) $ky$ (b) $\frac{\ln 2}{k}$ (c) $y_0 e^{kt}$.
3. (a) $-ky$ (b) $\frac{\ln 2}{k}$ (c) $y_0 e^{-kt}$.
4. $y(x) = \sqrt{1 - x^2}$.

---

## 8.3 SLOPE FIELDS; EULER’S METHOD

### SLOPE FIELDS
For a first-order differential equation $y' = f(x, y)$, a **slope field** (or direction field) displays short tangent line segments of slope $f(x, y)$ at grid points in the $xy$-plane.

---

### EULER’S METHOD
Given $y' = f(x, y)$ and $y(x_0) = y_0$, with step size $\Delta x$:
$$x_{n+1} = x_n + \Delta x$$
$$y_{n+1} = y_n + f(x_n, y_n)\Delta x$$

#### Example 1
For $y' = y - x, \; y(0) = 2$ with $\Delta x = 0.1$:
* $y_1 = 2 + (2 - 0)(0.1) = 2.20000$
* $y_2 = 2.2 + (2.2 - 0.1)(0.1) = 2.41000$
* $y_3 = 2.41 + (2.41 - 0.2)(0.1) = 2.63100$
* Continuing to $x = 1.0$: $y_{10} \approx 4.59374$ (Exact: $y(1) = 1 + 1 + e^1 \approx 4.71828$, Error $\approx 0.12454$).

> **Error Property:** Absolute error in Euler's method is approximately proportional to step size $\Delta x$.

---

### QUICK CHECK EXERCISES 8.3
*(See page 586 for answers.)*
1. Matches: (a) IV (b) III (c) I (d) II
2. $y = 2x, \; x > 0$
3. $y_{n+1} = y_n + f(x_n, y_n)\Delta x$
4. For $y' = y, y(0) = 1$: (a) Two steps to $x=1$ ($\Delta x = 0.5$): $y_1 = 1 + 0.5(1) = 1.5$, $y_2 = 1.5 + 0.5(1.5) = 2.25$. (b) Exact: $y(1) = e \approx 2.71828$.

---

## 8.4 FIRST-ORDER LINEAR EQUATIONS AND APPLICATIONS

### FIRST-ORDER LINEAR DIFFERENTIAL EQUATIONS
A first-order equation is **linear** if it can be written as:
$$\frac{dy}{dx} + p(x)y = q(x) \tag{3}$$

### METHOD OF INTEGRATING FACTORS
1. **Calculate Integrating Factor:**
   $$\mu(x) = e^{\int p(x)\,dx} \tag{4}$$
2. **Multiply both sides by $\mu(x)$:**
   $$\frac{d}{dx}[\mu(x)y] = \mu(x)q(x)$$
3. **Integrate both sides and solve for $y$:**
   $$y(x) = \frac{1}{\mu(x)}\left[\int \mu(x)q(x)\,dx + C\right] \tag{7}$$

#### Example 1
Solve $\frac{dy}{dx} - y = e^{2x}$.
* $p(x) = -1 \implies \mu = e^{\int -1\,dx} = e^{-x}$.
* $\frac{d}{dx}[e^{-x}y] = e^{-x}e^{2x} = e^x$.
* $e^{-x}y = e^x + C \implies y = e^{2x} + Ce^x$.

#### Example 2
Solve $x\frac{dy}{dx} - y = x, \; y(1) = 2$.
* Standard form: $\frac{dy}{dx} - \frac{1}{x}y = 1 \implies \mu = e^{-\int \frac{1}{x}dx} = \frac{1}{x}$.
* $\frac{d}{dx}\left[\frac{y}{x}\right] = \frac{1}{x} \implies \frac{y}{x} = \ln x + C \implies y = x\ln x + Cx$.
* $y(1) = 2 \implies C = 2 \implies y = x\ln x + 2x$.

---

### APPLICATION 1: MIXING PROBLEMS
$$\frac{dy}{dt} = \text{rate in} - \text{rate out} \tag{10}$$

#### Example 3
A $100\text{ gal}$ tank contains $4\text{ lb}$ salt. Brine with $2\text{ lb/gal}$ enters at $5\text{ gal/min}$, and mixed solution drains at $5\text{ gal/min}$.
* $\text{rate in} = 2 \times 5 = 10\text{ lb/min}$.
* $\text{rate out} = \frac{y(t)}{100} \times 5 = \frac{y(t)}{20}\text{ lb/min}$.
* $\frac{dy}{dt} + \frac{1}{20}y = 10, \; y(0) = 4 \implies y(t) = 200 - 196e^{-t/20}$.
* At $t = 10\text{ min}$: $y(10) = 200 - 196e^{-0.5} \approx 81.1\text{ lb}$. Limiting amount as $t \to \infty$ is $200\text{ lb}$.

---

### APPLICATION 2: FREE FALL RETARDED BY AIR RESISTANCE
$$m\frac{dv}{dt} = -mg - cv \implies \frac{dv}{dt} + \frac{c}{m}v = -g, \quad v(0) = v_0 \tag{14}$$
Solution:
$$v(t) = e^{-ct/m}\left(v_0 + \frac{mg}{c}\right) - \frac{mg}{c} \tag{16}$$
* **Terminal Velocity:** $v_\tau = -\frac{mg}{c}$
* **Terminal Speed:** $|v_\tau| = \frac{mg}{c}$

---

### QUICK CHECK EXERCISES 8.4
*(See page 594 for answers.)*
1. Step 1: $\mu = e^{\int p(x)dx}$; Step 2: $\frac{d}{dx}[\mu y] = \mu q(x)$; Step 3: $y = \frac{1}{\mu}\int \mu q(x)dx$.
2. $\mu = x$.
3. $\frac{dy}{dt} + \frac{y}{20} = 15, \; y(0) = 30$.

---

## CHAPTER 8 MAKING CONNECTIONS

* **Homogeneous Differential Equations:** $\frac{dy}{dx} = f\left(\frac{y}{x}\right) \implies$ Substitution $u = \frac{y}{x} \implies y = ux, \; \frac{dy}{dx} = u + x\frac{du}{dx}$.
* **Bernoulli Equations:** $\frac{dy}{dx} + p(x)y = q(x)y^n \implies$ Substitution $u = y^{1-n} \implies \frac{du}{dx} + (1-n)p(x)u = (1-n)q(x)$ (Linear in $u$).
