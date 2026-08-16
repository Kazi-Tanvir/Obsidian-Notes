# APPENDICES

---

## APPENDIX A: GRAPHING FUNCTIONS USING CALCULATORS AND COMPUTER ALGEBRA SYSTEMS

### GRAPHING CALCULATORS AND COMPUTER ALGEBRA SYSTEMS
The development of new technology has significantly changed how and where mathematicians, engineers, and scientists perform their work, as well as their approach to problem solving. Among the most significant of these developments are programs called **Computer Algebra Systems (CAS)**, the most common being *Mathematica* and *Maple*.

Computer algebra systems not only have graphing capabilities, but also perform symbolic computations (e.g. factoring polynomials, exact arithmetic):
$$x^6 + 23x^5 + 147x^4 - 139x^3 - 3464x^2 - 2112x + 23040 = (x + 5)(x - 3)^2(x + 8)^3$$

---

### VIEWING WINDOWS & SETTINGS
* **Viewing Window (Viewing Rectangle):** Denoted $[a, b] \times [c, d]$, where $[a, b]$ is the $x$-interval and $[c, d]$ is the $y$-interval.
* **Scale Factors (Tick Marks):** `xScl` and `yScl` control tick spacing on the coordinate axes.
* **Common Pitfalls & Artifacts:**
  - **Compression:** Compressing axes may obscure vertical or horizontal detail.
  - **Sampling Error:** Discrete pixel evaluation may miss oscillations (e.g. $\cos(10\pi x)$ appearing constant).
  - **False Gaps:** Rapid changes in slope create vertical pixel jumps.
  - **False Line Segments:** Connectors drawn across vertical asymptotes/discontinuities (e.g. $y = 1/(x-1)$).
  - **Errors of Omission:** Fractional powers evaluated via real logarithms omitting negative branches (e.g. $x^{2/3}$).

---

### PARAMETRIC EQUATIONS, INVERSES, TRANSLATION, AND SCALING
* **Graphing $x = g(y)$ Parametrically:** $x = g(t), \; y = t$.
* **Graphing Inverse Functions $y = f^{-1}(x)$:** $x = f(t), \; y = t$.
* **Translation:** Circle $(x - x_0)^2 + (y - y_0)^2 = r^2 \implies x = x_0 + r\cos t, \; y = y_0 + r\sin t$ ($0 \le t \le 2\pi$).
* **Scaling:** Ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \implies x = a\cos t, \; y = b\sin t$ ($0 \le t \le 2\pi$).

---

## APPENDIX B: TRIGONOMETRY REVIEW

### ANGLES & RADIAN MEASURE
* **Degree–Radian Conversion:**
  $$1^\circ = \frac{\pi}{180}\text{ rad} \approx 0.01745\text{ rad}, \quad 1\text{ rad} = \left(\frac{180}{\pi}\right)^\circ \approx 57^\circ 17' 44.8'' \tag{1–2}$$
* **Arc Length and Sector Area (in Radians):**
  $$s = r\theta \tag{4}$$
  $$A = \frac{1}{2}r^2\theta \tag{5}$$

---

### TRIGONOMETRIC FUNCTIONS & UNIT CIRCLE

> **B.1 DEFINITION**
> For an angle $\theta$ in standard position intersecting a circle of radius $r = \sqrt{x^2 + y^2}$ at $P(x, y)$:
> $$\sin\theta = \frac{y}{r}, \quad \cos\theta = \frac{x}{r}, \quad \tan\theta = \frac{y}{x}$$
> $$\csc\theta = \frac{r}{y}, \quad \sec\theta = \frac{r}{x}, \quad \cot\theta = \frac{x}{y} \tag{6}$$

#### Values of Common Angles:

| $\theta$ (rad) | $\theta$ (deg) | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ | $\csc\theta$ | $\sec\theta$ | $\cot\theta$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $0^\circ$ | $0$ | $1$ | $0$ | — | $1$ | — |
| $\pi/6$ | $30^\circ$ | $1/2$ | $\sqrt{3}/2$ | $1/\sqrt{3}$ | $2$ | $2/\sqrt{3}$ | $\sqrt{3}$ |
| $\pi/4$ | $45^\circ$ | $1/\sqrt{2}$ | $1/\sqrt{2}$ | $1$ | $\sqrt{2}$ | $\sqrt{2}$ | $1$ |
| $\pi/3$ | $60^\circ$ | $\sqrt{3}/2$ | $1/2$ | $\sqrt{3}$ | $2/\sqrt{3}$ | $2$ | $1/\sqrt{3}$ |
| $\pi/2$ | $90^\circ$ | $1$ | $0$ | — | $1$ | — | $0$ |
| $2\pi/3$ | $120^\circ$ | $\sqrt{3}/2$ | $-1/2$ | $-\sqrt{3}$ | $2/\sqrt{3}$ | $-2$ | $-1/\sqrt{3}$ |
| $3\pi/4$ | $135^\circ$ | $1/\sqrt{2}$ | $-1/\sqrt{2}$ | $-1$ | $\sqrt{2}$ | $-\sqrt{2}$ | $-1$ |
| $5\pi/6$ | $150^\circ$ | $1/2$ | $-\sqrt{3}/2$ | $-1/\sqrt{3}$ | $2$ | $-2/\sqrt{3}$ | $-\sqrt{3}$ |
| $\pi$ | $180^\circ$ | $0$ | $-1$ | $0$ | — | $-1$ | — |
| $3\pi/2$ | $270^\circ$ | $-1$ | $0$ | — | $-1$ | — | $0$ |
| $2\pi$ | $360^\circ$ | $0$ | $1$ | $0$ | — | $1$ | — |

---

### KEY TRIGONOMETRIC IDENTITIES

* **Pythagorean Identities:**
  $$\sin^2\theta + \cos^2\theta = 1, \quad \tan^2\theta + 1 = \sec^2\theta, \quad 1 + \cot^2\theta = \csc^2\theta \tag{11–13}$$
* **Symmetry & Periodicity:**
  $$\sin(-\theta) = -\sin\theta, \quad \cos(-\theta) = \cos\theta, \quad \tan(-\theta) = -\tan\theta \tag{16, 19, 22}$$
  $$\sin(\theta \pm 2n\pi) = \sin\theta, \quad \cos(\theta \pm 2n\pi) = \cos\theta, \quad \tan(\theta \pm n\pi) = \tan\theta \tag{25–26, 29}$$
  $$\sin\left(\frac{\pi}{2} - \theta\right) = \cos\theta, \quad \cos\left(\frac{\pi}{2} - \theta\right) = \sin\theta, \quad \tan\left(\frac{\pi}{2} - \theta\right) = \cot\theta \tag{30–32}$$
* **Law of Cosines (Theorem B.2):**
  $$c^2 = a^2 + b^2 - 2ab\cos\theta$$
* **Addition & Subtraction Formulas:**
  $$\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta \tag{34, 36}$$
  $$\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta \tag{35, 37}$$
  $$\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta} \tag{38–39}$$
* **Double-Angle & Half-Angle Formulas:**
  $$\sin 2\alpha = 2\sin\alpha\cos\alpha \tag{40}$$
  $$\cos 2\alpha = \cos^2\alpha - \sin^2\alpha = 2\cos^2\alpha - 1 = 1 - 2\sin^2\alpha \tag{41, 43, 44}$$
  $$\cos^2\left(\frac{\alpha}{2}\right) = \frac{1 + \cos\alpha}{2}, \quad \sin^2\left(\frac{\alpha}{2}\right) = \frac{1 - \cos\alpha}{2} \tag{45–46}$$
* **Product-to-Sum Formulas:**
  $$\sin\alpha\cos\beta = \frac{1}{2}[\sin(\alpha - \beta) + \sin(\alpha + \beta)] \tag{47}$$
  $$\sin\alpha\sin\beta = \frac{1}{2}[\cos(\alpha - \beta) - \cos(\alpha + \beta)] \tag{48}$$
  $$\cos\alpha\cos\beta = \frac{1}{2}[\cos(\alpha - \beta) + \cos(\alpha + \beta)] \tag{49}$$
* **Angle of Inclination of a Line:**
  $$m = \tan\phi \quad (0^\circ \le \phi < 180^\circ \text{ or } 0 \le \phi < \pi) \tag{54}$$

---

## APPENDIX C: SOLVING POLYNOMIAL EQUATIONS

### POLYNOMIAL DEFINITIONS & PROPERTIES
A polynomial of degree $n$ has the form $p(x) = c_n x^n + c_{n-1}x^{n-1} + \dots + c_1 x + c_0$ ($c_n \neq 0$).

> **C.1 THEOREM (Fundamental Theorem of Algebra)**
> If complex roots are allowed, and if roots are counted according to their multiplicities, then a polynomial of degree $n$ has exactly $n$ roots:
> $$p(x) = a(x - r_1)^{m_1}(x - r_2)^{m_2}\cdots(x - r_k)^{m_k}, \quad \sum m_i = n \tag{3}$$

---

### DIVISION, REMAINDER, AND FACTOR THEOREMS

> **C.2 THEOREM (Division of Polynomials)**
> $p(x) = s(x)q(x) + r(x)$, where $\deg r(x) < \deg s(x)$ or $r(x) = 0$.

> **C.3 THEOREM (Remainder Theorem)**
> If a polynomial $p(x)$ is divided by $x - c$, then the remainder is $p(c)$.

> **C.4 THEOREM (Factor Theorem)**
> A polynomial $p(x)$ has a linear factor $x - c$ if and only if $p(c) = 0$.

---

### RATIONAL ZERO TEST

> **C.5 THEOREM (Rational Zero Theorem)**
> If $p(x) = c_n x^n + \dots + c_0$ has integer coefficients:
> * Any integer root $r$ must divide the constant term $c_0$.
> * Any rational root $r = a/b$ (in lowest terms) must have $a$ dividing $c_0$ and $b$ dividing the leading coefficient $c_n$.

---

## APPENDIX D: SELECTED PROOFS

### PROOFS OF BASIC LIMIT THEOREMS (D.1)
* **Limit of Constant:** $\lim_{x\to a} k = k$. Given $\epsilon > 0$, choosing any $\delta > 0$ yields $|k - k| = 0 < \epsilon$.
* **Limit of Sum:** $\lim_{x\to a} [f(x) + g(x)] = L_1 + L_2$. Uses triangle inequality $|(f(x) + g(x)) - (L_1 + L_2)| \le |f(x) - L_1| + |g(x) - L_2| < \epsilon/2 + \epsilon/2 = \epsilon$ with $\delta = \min(\delta_1, \delta_2)$.
* **Limit of Product:** $\lim_{x\to a} [f(x)g(x)] = L_1 L_2$. Decomposes $f(x)g(x) - L_1 L_2 = L_1(g(x) - L_2) + L_2(f(x) - L_1) + (f(x) - L_1)(g(x) - L_2)$.

---

### PROOF OF COMPOSITE CONTINUITY PROPERTY (D.2 / THEOREM 1.5.5)
If $\lim_{x\to c} g(x) = L$ and $f$ is continuous at $L$, then $\lim_{x\to c} f(g(x)) = f(L)$.
Given $\epsilon > 0$, continuity of $f$ provides $\delta_1 > 0$ such that $|f(u) - f(L)| < \epsilon$ whenever $|u - L| < \delta_1$. Then $\lim_{x\to c} g(x) = L$ provides $\delta > 0$ such that $|g(x) - L| < \delta_1$ whenever $0 < |x - c| < \delta$.

---

### PROOF OF THE CHAIN RULE (D.3 & D.4 / THEOREM 2.6.1)
Using $\Delta y = f'(u)\Delta u + \epsilon_2 \Delta u$ and $\Delta u = g'(x)\Delta x + \epsilon_1 \Delta x$:
$$\frac{\Delta y}{\Delta x} = [f'(u) + \epsilon_2][g'(x) + \epsilon_1] \xrightarrow{\Delta x \to 0} f'(u)g'(x) = \frac{dy}{du}\frac{du}{dx}$$

---

### PROOF OF CRITICAL POINT THEOREM (D.5 / THEOREM 4.2.2)
If $f$ has a local maximum at $x_0$ and is differentiable, then:
* For $h > 0$: $\frac{f(x_0+h)-f(x_0)}{h} \le 0 \implies f'(x_0) \le 0$.
* For $h < 0$: $\frac{f(x_0+h)-f(x_0)}{h} \ge 0 \implies f'(x_0) \ge 0$.
* Therefore, $f'(x_0) = 0$.

---

### PROOFS OF SUMMATION FORMULAS (D.6 / THEOREM 5.4.2)
* **Sum of First $n$ Integers:** Adding in forward and reverse orders yields $2\sum_{k=1}^n k = n(n+1) \implies \sum_{k=1}^n k = \frac{n(n+1)}{2}$.
* **Sum of Squares:** Using telescoping sum $\sum_{k=1}^n [(k+1)^3 - k^3] = (n+1)^3 - 1 = 3\sum k^2 + 3\sum k + n$, solving for $\sum k^2$ yields $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$.

---

### PROOF OF THE LIMIT COMPARISON TEST (D.7 / THEOREM 9.5.4)
For $\rho = \lim \frac{a_k}{b_k} > 0$, setting $\epsilon = \rho/2$ yields $\frac{1}{2}\rho b_k < a_k < \frac{3}{2}\rho b_k$ for $k \ge K$. By direct comparison with multiples of $\sum b_k$, both series share the same convergence behavior.

---

### PROOF OF THE RATIO TEST (D.8 / THEOREM 9.5.5)
If $\lim \frac{u_{k+1}}{u_k} = \rho < 1$, choose $r$ with $\rho < r < 1$. For $k \ge K$, $u_{k+1} < r u_k$, bounding $\sum u_k$ by a convergent geometric series $\sum r^k u_K$. If $\rho > 1$, terms do not approach 0 ($u_k \not\to 0$), so the series diverges.

---

### PROOF OF THE REMAINDER ESTIMATION THEOREM (D.9 / THEOREM 9.7.4)
Since $|R_n^{(n+1)}(t)| \le M$ and $R_n^{(k)}(x_0) = 0$ for $k = 0, 1, \dots, n$, integrating $n+1$ successive times from $x_0$ to $x$ gives:
$$|R_n(x)| \le \frac{M}{(n+1)!}|x - x_0|^{n+1}$$

---

### PROOF OF EQUALITY OF MIXED PARTIALS (D.10 / THEOREM 13.3.2)
Using the difference function $w(\Delta x, \Delta y) = f(x+\Delta x, y+\Delta y) - f(x+\Delta x, y) - f(x, y+\Delta y) + f(x, y)$, applying the single-variable Mean-Value Theorem twice (first in $x$, then in $y$) gives $w(\Delta x, \Delta y) = f_{xy}(c, d)\Delta x \Delta y$. Taking the limit as $(\Delta x, \Delta y) \to (0, 0)$ and using continuity proves $f_{xy}(x, y) = f_{yx}(x, y)$.

---

### PROOF OF TWO-VARIABLE CHAIN RULE (D.11 / THEOREM 13.5.1)
Using differentiability $\Delta z = \frac{\partial z}{\partial x}\Delta x + \frac{\partial z}{\partial y}\Delta y + \epsilon \sqrt{(\Delta x)^2 + (\Delta y)^2}$:
$$\frac{\Delta z}{\Delta t} = \frac{\partial z}{\partial x}\frac{\Delta x}{\Delta t} + \frac{\partial z}{\partial y}\frac{\Delta y}{\Delta t} + \epsilon \frac{\sqrt{(\Delta x)^2 + (\Delta y)^2}}{\Delta t} \xrightarrow{\Delta t \to 0} \frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}$$
