# CHAPTER 6: EXPONENTIAL, LOGARITHMIC, AND INVERSE TRIGONOMETRIC FUNCTIONS

> The growth and decline of animal populations and natural resources can be modeled using basic functions studied in this chapter.

We begin this chapter with a review of exponential and logarithmic functions. These functions have important applications, from modeling population growth and the spread of disease, to the measurement of the magnitude of an earthquake or the perceived loudness of a sound. Logarithmic and exponential functions are best understood within the context of inverse functions and we will derive an important relationship between the derivative of a function and the derivative of its inverse. This connection will allow us to compute derivative formulas for logarithmic and exponential functions, along with their associated integration formulas. Later in the chapter we will exploit this connection again, to find the derivatives of inverse trigonometric functions, together with some related integration formulas. Along the way, we will discuss L'Hôpital's rule, a powerful tool for evaluating limits. We conclude the chapter with a study of some important combinations of exponential functions known as "hyperbolic functions."

---

## 6.1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS

### IRRATIONAL EXPONENTS & LAWS OF EXPONENTS

Irrational powers such as $2^\pi$ are defined via sequences of rational approximations ($2^{3.1}, 2^{3.14}, 2^{3.141}, \dots \implies 2^\pi \approx 8.8250$).  
For all real exponents $p$ and $q$ ($b > 0$):
$$b^p b^q = b^{p+q}, \quad \frac{b^p}{b^q} = b^{p-q}, \quad (b^p)^q = b^{pq}$$

---

### EXPONENTIAL FUNCTIONS & NATURAL EXPONENTIAL FUNCTION

* **General Exponential:** $f(x) = b^x$ ($b > 0, b \neq 1$), domain $(-\infty, +\infty)$, range $(0, +\infty)$.
* **Base $e \approx 2.718282$:** The unique base such that the tangent line to $y = b^x$ at $(0, 1)$ has slope 1.
  $$\lim_{x \to 0} (1 + x)^{1/x} = e, \quad \lim_{x \to \pm\infty} \left(1 + \frac{1}{x}\right)^x = e$$

---

### LOGARITHMIC FUNCTIONS

* **Definition:** $y = \log_b x \iff x = b^y$ ($x > 0$).
* **Natural Logarithm:** $\ln x = \log_e x \iff x = e^y$.
* **Cancellation Equations:**
  $$\log_b(b^x) = x, \quad b^{\log_b x} = x \quad (x > 0)$$
  $$\ln(e^x) = x, \quad e^{\ln x} = x \quad (x > 0)$$

> **6.1.3 THEOREM (Algebraic Properties of Logarithms)**  
> (a) $\log_b(ac) = \log_b a + \log_b c$  
> (b) $\log_b(a/c) = \log_b a - \log_b c$  
> (c) $\log_b(a^r) = r\log_b a$  
> (d) $\log_b(1/c) = -\log_b c$

* **Change of Base Formula:**
  $$\log_b x = \frac{\ln x}{\ln b}$$

* **Logarithmic Scales:**
  * Sound Level: $\beta = 10\log(I/I_0)\text{ dB}$ (where $I_0 = 10^{-12}\text{ W/m}^2$).
  * Earthquake Magnitude (Richter Scale): $\log E = 4.4 + 1.5M$.
  * Acidity: $\text{pH} = -\log[H^+]$.

* **End Behavior & Growth Rates:**
  $$\lim_{x \to +\infty} e^x = +\infty, \quad \lim_{x \to -\infty} e^x = 0, \quad \lim_{x \to +\infty} \ln x = +\infty, \quad \lim_{x \to 0^+} \ln x = -\infty$$

---

### QUICK CHECK EXERCISES 6.1
*(See page 420 for answers.)*
1. Domain $(-\infty, +\infty)$; Range $(0, +\infty)$.  
2. Domain $(-\infty, 1)$; Range $(-\infty, +\infty)$.  
3. (a) $4^0$ (b) $4^{1/2}$ (c) $4^{-2}$ (d) $4^{3/4}$ (e) $4^{\log_4 5}$.  
4. (a) $x = \ln(1/2) = -\ln 2$ (b) $x = 2$ (c) $x = \ln 2$.  
5. (a) $x = e^3$ (b) $x = 101$ (c) $x = 2$.

---

## 6.2 DERIVATIVES AND INTEGRALS INVOLVING LOGARITHMIC FUNCTIONS

### DERIVATIVE FORMULAS

$$\frac{d}{dx}[\ln x] = \frac{1}{x} \quad (x > 0) \tag{2}$$
$$\frac{d}{dx}[\log_b x] = \frac{1}{x\ln b} \quad (x > 0) \tag{3}$$
$$\frac{d}{dx}[\ln |x|] = \frac{1}{x} \quad (x \neq 0) \tag{6}$$
Generalized: $\frac{d}{dx}[\ln u] = \frac{1}{u}\frac{du}{dx}$.

### LOGARITHMIC DIFFERENTIATION
To differentiate complicated products, quotients, and powers $y = f(x)$:
1. Take $\ln |y|$ of both sides.
2. Expand using logarithm laws.
3. Differentiate implicitly with respect to $x$: $\frac{1}{y}\frac{dy}{dx} = \dots$
4. Multiply by $y$ to obtain $\frac{dy}{dx}$.

### INTEGRALS INVOLVING $\ln x$
$$\int \frac{1}{u} du = \ln |u| + C \tag{8}$$
$$\int \frac{g'(x)}{g(x)} dx = \ln |g(x)| + C$$
$$\int \tan x dx = -\ln |\cos x| + C = \ln |\sec x| + C$$
$$\int \cot x dx = \ln |\sin x| + C$$

---

### QUICK CHECK EXERCISES 6.2
*(See page 427 for answers.)*
1. Tangent line at $x = e^2$: $y = \frac{x}{e^2} + 1$.  
2. (a) $\frac{1}{x}$ (b) $\frac{1}{2x}$ (c) $-\frac{1}{x\ln 10}$.  
3. $f'(x) = \frac{\sqrt{x+1}}{\sqrt[3]{x-1}}\left[\frac{1}{2(x+1)} - \frac{1}{3(x-1)}\right]$.  
4. $\lim_{h \to 0} \frac{\ln(1+h)}{h} = 1$.  
5. $\int_2^5 \frac{1}{t}dt = \ln(5/2)$.

---

## 6.3 DERIVATIVES OF INVERSE FUNCTIONS; EXPONENTIAL FUNCTIONS

### DERIVATIVE OF AN INVERSE FUNCTION

> **6.3.1 THEOREM**  
> If $f$ is differentiable and strictly monotone on an interval, then $f^{-1}$ is differentiable on the range of $f$, and
> $$(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))} \tag{2} \quad \text{or} \quad \frac{dy}{dx} = \frac{1}{dx/dy}$$

#### Derivatives of Exponentials:
$$\frac{d}{dx}[b^x] = b^x \ln b \tag{5}$$
$$\frac{d}{dx}[e^x] = e^x \tag{6}$$
$$\frac{d}{dx}[e^u] = e^u \frac{du}{dx}, \quad \frac{d}{dx}[b^u] = b^u \ln b \frac{du}{dx} \tag{7–8}$$

#### Integrals of Exponentials:
$$\int e^u du = e^u + C \tag{10}$$
$$\int b^u du = \frac{b^u}{\ln b} + C \tag{9}$$

---

### QUICK CHECK EXERCISES 6.3
*(See page 434 for answers.)*
1. $(f^{-1})'(8) = 1/5$.  
2. Invertibility: (a) yes (b) no (c) no (d) yes.  
3. (a) $e^x$ (b) $7^x \ln 7$ (c) $-e^x \sin(e^x + 1)$ (d) $3e^{3x-2}$.  
4. $f'(x) = e^{x^3+x}(3x^2+1) > 0 \implies$ one-to-one.  
5. $\int_0^{\frac{1}{2}\ln 5} e^x dx = \sqrt{5} - 1$.

---

## 6.4 GRAPHS AND APPLICATIONS INVOLVING LOGARITHMIC AND EXPONENTIAL FUNCTIONS

### LOGISTIC GROWTH MODEL
$$y = \frac{L}{1 + Ae^{-kt}} \tag{1}$$
* Population $y$ is strictly increasing for $t \ge 0$.
* Limiting carrying capacity: $\lim_{t \to +\infty} y = L$.
* Inflection point (maximum growth rate) occurs at $y = L/2$, where $t = \frac{\ln A}{k}$.
* Differential equations:
  $$\frac{dy}{dt} = \frac{k}{L}y(L - y), \quad \frac{d^2y}{dt^2} = \frac{k^2}{L^2}y(L - y)(L - 2y)$$

### NEWTON'S LAW OF COOLING
$$T(t) = T_0 + (T_{\text{init}} - T_0)e^{-kt}$$

---

### QUICK CHECK EXERCISES 6.4
*(See page 441 for answers.)*
Extrema, concavity, and inflection points for exponential/logarithmic combinations.

---

## 6.5 L'HÔPITAL'S RULE; INDETERMINATE FORMS

### L'HÔPITAL'S RULE FOR FORMS $0/0$ AND $\infty/\infty$

> **6.5.1 & 6.5.2 THEOREMS (L'Hôpital's Rule)**  
> If $\lim \frac{f(x)}{g(x)}$ produces indeterminate form $\frac{0}{0}$ or $\frac{\pm\infty}{\pm\infty}$, then:
> $$\lim \frac{f(x)}{g(x)} = \lim \frac{f'(x)}{g'(x)}$$
> provided the limit on the right exists or is $\pm\infty$.

> **Guillaume François Antoine de L'Hôpital (1661–1704)**  
> Published the first calculus textbook (*L'Analyse des Infiniment Petits*, 1696), presenting the rule taught to him by Johann Bernoulli.

### OTHER INDETERMINATE FORMS
* **Type $0 \cdot \infty$:** Rewrite $f(x)g(x) = \frac{f(x)}{1/g(x)}$ or $\frac{g(x)}{1/f(x)}$ to get $0/0$ or $\infty/\infty$.
* **Type $\infty - \infty$:** Combine algebraically (common denominator or rationalization).
* **Types $0^0, \infty^0, 1^\infty$:** Set $y = [f(x)]^{g(x)}$, evaluate $\lim \ln y = \lim g(x)\ln f(x) = L \implies \lim y = e^L$.

---

### QUICK CHECK EXERCISES 6.5
*(See page 450 for answers.)*
1. Applicability: (a) yes (b) no (c) yes.  
2. (a) $1/2$ (b) does not exist (c) 2.  
3. $\lim_{x \to +\infty} \frac{e^x}{500x^2} = +\infty$.

---

## 6.6 LOGARITHMIC AND OTHER FUNCTIONS DEFINED BY INTEGRALS

### THE FORMAL INTEGRAL DEFINITION OF $\ln x$

> **6.6.1 DEFINITION**  
> $$\ln x = \int_1^x \frac{1}{t} dt, \quad x > 0 \tag{1}$$

* $\frac{d}{dx}[\ln x] = \frac{1}{x}$.
* $e^x$ is formally defined as the inverse of $\ln x$.
* General real power: $a^r = e^{r\ln a}$.

### NONELEMENTARY FUNCTIONS DEFINED BY INTEGRALS
* **Error Function:** $\text{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2} dt \tag{12}$
* **Fresnel Integrals:** $S(x) = \int_0^x \sin\left(\frac{\pi t^2}{2}\right) dt, \quad C(x) = \int_0^x \cos\left(\frac{\pi t^2}{2}\right) dt \tag{13–14}$
* **Leibniz Rule:**
  $$\frac{d}{dx}\left[\int_a^{g(x)} f(t) dt\right] = f(g(x))g'(x) \tag{18}$$
  $$\frac{d}{dx}\left[\int_{h(x)}^{g(x)} f(t) dt\right] = f(g(x))g'(x) - f(h(x))h'(x)$$

---

### QUICK CHECK EXERCISES 6.6
*(See page 462 for answers.)*
1. $\int_1^{1/e} \frac{1}{t}dt = -1$.  
2. (a) $5/6$ (b) $7/12$.  
3. $e$.  
4. $y = 2 + \int_0^x \cos(t^3)dt$.  
5. $-\frac{e^{-x}}{1 + e^{-4x}}$.

---

## 6.7 DERIVATIVES AND INTEGRALS INVOLVING INVERSE TRIGONOMETRIC FUNCTIONS

### DEFINITIONS & RESTRICTED DOMAINS (Table 6.7.1)
* $\sin^{-1} x$: Domain $[-1, 1]$, Range $[-\pi/2, \pi/2]$
* $\cos^{-1} x$: Domain $[-1, 1]$, Range $[0, \pi]$
* $\tan^{-1} x$: Domain $(-\infty, +\infty)$, Range $(-\pi/2, \pi/2)$
* $\sec^{-1} x$: Domain $(-\infty, -1] \cup [1, +\infty)$, Range $[0, \pi/2) \cup (\pi/2, \pi]$

### DERIVATIVE FORMULAS
$$\begin{aligned}
\frac{d}{dx}[\sin^{-1} u] &= \frac{1}{\sqrt{1 - u^2}}\frac{du}{dx} & \frac{d}{dx}[\cos^{-1} u] &= -\frac{1}{\sqrt{1 - u^2}}\frac{du}{dx} \\
\frac{d}{dx}[\tan^{-1} u] &= \frac{1}{1 + u^2}\frac{du}{dx} & \frac{d}{dx}[\cot^{-1} u] &= -\frac{1}{1 + u^2}\frac{du}{dx} \\
\frac{d}{dx}[\sec^{-1} u] &= \frac{1}{|u|\sqrt{u^2 - 1}}\frac{du}{dx} & \frac{d}{dx}[\csc^{-1} u] &= -\frac{1}{|u|\sqrt{u^2 - 1}}\frac{du}{dx}
\end{aligned}$$

### INTEGRATION FORMULAS ($a > 0$)
$$\int \frac{du}{\sqrt{a^2 - u^2}} = \sin^{-1}\left(\frac{u}{a}\right) + C \tag{24}$$
$$\int \frac{du}{a^2 + u^2} = \frac{1}{a}\tan^{-1}\left(\frac{u}{a}\right) + C \tag{23}$$
$$\int \frac{du}{u\sqrt{u^2 - a^2}} = \frac{1}{a}\sec^{-1}\left|\frac{u}{a}\right| + C \tag{25}$$

---

### QUICK CHECK EXERCISES 6.7
*(See page 472 for answers.)*
1. Exact values: (a) $-\pi/2$ (b) $\pi/4$ (c) $\pi/3$ (d) $\pi/3$ (e) $2\pi/3$.  
2. (a) $\pi/7$ (b) $2\pi/7$ (c) $\pi/6$ (d) $2\pi/7$.  
3. $\frac{2}{\sqrt{1 - 4x^2}}$.  
4. $\int_{-1/2}^{1/2} \frac{1}{\sqrt{1 - x^2}}dx = \pi/3$.

---

## 6.8 HYPERBOLIC FUNCTIONS AND HANGING CABLES

### DEFINITIONS OF HYPERBOLIC FUNCTIONS

$$\begin{aligned}
\sinh x &= \frac{e^x - e^{-x}}{2} & \cosh x &= \frac{e^x + e^{-x}}{2} \\
\tanh x &= \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}} & \coth x &= \frac{\cosh x}{\sinh x} = \frac{e^x + e^{-x}}{e^x - e^{-x}} \\
\text{sech } x &= \frac{1}{\cosh x} = \frac{2}{e^x + e^{-x}} & \text{csch } x &= \frac{1}{\sinh x} = \frac{2}{e^x - e^{-x}}
\end{aligned}$$

* **Fundamental Identity:** $\cosh^2 x - \sinh^2 x = 1$.
* **Catenary:** $y = a\cosh(x/a) + c$ models hanging cables.

### DERIVATIVES & INTEGRALS
$$\begin{aligned}
\frac{d}{dx}[\sinh u] &= \cosh u \frac{du}{dx} & \int \cosh u du &= \sinh u + C \\
\frac{d}{dx}[\cosh u] &= \sinh u \frac{du}{dx} & \int \sinh u du &= \cosh u + C \\
\frac{d}{dx}[\tanh u] &= \text{sech}^2 u \frac{du}{dx} & \int \text{sech}^2 u du &= \tanh u + C
\end{aligned}$$

### INVERSE HYPERBOLIC FUNCTIONS (Logarithmic Forms)
$$\begin{aligned}
\sinh^{-1} x &= \ln(x + \sqrt{x^2 + 1}) \\
cosh^{-1} x &= \ln(x + \sqrt{x^2 - 1}) \quad (x \ge 1) \\
\tanh^{-1} x &= \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right) \quad (|x| < 1)
\end{aligned}$$

---

### QUICK CHECK EXERCISES 6.8
*(See page 483 for answers.)*
Definitions, table of domain/ranges, unit hyperbola parametric equations, and derivatives/integrals.

---

## CHAPTER 6 REVIEW EXERCISES
Exercises 1–88 covering inverse functions, logarithmic and exponential derivatives/integrals, L'Hôpital's rule, integral-defined functions, inverse trigonometric functions, and hyperbolic functions.

---

## CHAPTER 6 MAKING CONNECTIONS
Radioactive decay continuous model derivation, geometric proof of $\lim_{h \to 0} \frac{e^h - 1}{h} = 1$, and geometric identity $\int_1^e \ln x dx + \int_0^1 e^x dx = e$.
