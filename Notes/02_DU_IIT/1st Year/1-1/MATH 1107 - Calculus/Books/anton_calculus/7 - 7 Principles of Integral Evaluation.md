# CHAPTER 7: PRINCIPLES OF INTEGRAL EVALUATION

> The floating roof on the Stade de France sports complex is an ellipse. Finding the arc length of an ellipse involves numerical integration techniques introduced in this chapter.

In earlier chapters we obtained many basic integration formulas as an immediate consequence of the corresponding differentiation formulas. For example, knowing that the derivative of $\sin x$ is $\cos x$ enabled us to deduce that the integral of $\cos x$ is $\sin x$. Subsequently, we expanded our integration repertoire by introducing the method of $u$-substitution. That method enabled us to integrate many functions by transforming the integrand of an unfamiliar integral into a familiar form. However, $u$-substitution alone is not adequate to handle the wide variety of integrals that arise in applications, so additional integration techniques are still needed. In this chapter we will discuss some of those techniques, and we will provide a more systematic procedure for attacking unfamiliar integrals. We will talk more about numerical approximations of definite integrals, and we will explore the idea of integrating over infinite intervals.

---

## 7.1 AN OVERVIEW OF INTEGRATION METHODS

In this section we will give a brief overview of methods for evaluating integrals, and we will review the integration formulas that were discussed in earlier sections.

### METHODS FOR APPROACHING INTEGRATION PROBLEMS
There are three basic approaches for evaluating unfamiliar integrals:
* **Technology:** CAS programs such as *Mathematica*, *Maple*, and the open source program *Sage* are capable of evaluating extremely complicated integrals, and such programs are increasingly available for both computers and handheld calculators.
* **Tables:** Prior to the development of CAS programs, scientists relied heavily on tables to evaluate difficult integrals arising in applications. Such tables were compiled over many years, incorporating the skills and experience of many people. One such table appears in the endpapers of this text, but more comprehensive tables appear in various reference books such as the *CRC Standard Mathematical Tables and Formulae*, CRC Press, Inc., 2002.
* **Transformation Methods:** Transformation methods are methods for converting unfamiliar integrals into familiar integrals. These include $u$-substitution, algebraic manipulation of the integrand, and other methods that we will discuss in this chapter.

None of the three methods is perfect; for example, CAS programs often encounter integrals that they cannot evaluate and they sometimes produce answers that are unnecessarily complicated, tables are not exhaustive and may not include a particular integral of interest, and transformation methods rely on human ingenuity that may prove to be inadequate in difficult problems.

In this chapter we will focus on transformation methods and tables, so it will not be necessary to have a CAS. However, if you have a CAS, then you can use it to confirm the results in the examples, and there are exercises that are designed to be solved with a CAS.

---

### A REVIEW OF FAMILIAR INTEGRATION FORMULAS

The following is a list of basic integrals that we have encountered thus far:

#### CONSTANTS, POWERS, EXPONENTIALS
1. $\int du = u + C$
2. $\int a\,du = a\int du = au + C$
3. $\int u^r\,du = \frac{u^{r+1}}{r+1} + C, \quad r \neq -1$
4. $\int \frac{du}{u} = \ln |u| + C$
5. $\int e^u\,du = e^u + C$
6. $\int b^u\,du = \frac{b^u}{\ln b} + C, \quad b > 0, \; b \neq 1$

#### TRIGONOMETRIC FUNCTIONS
7. $\int \sin u\,du = -\cos u + C$
8. $\int \cos u\,du = \sin u + C$
9. $\int \sec^2 u\,du = \tan u + C$
10. $\int \csc^2 u\,du = -\cot u + C$
11. $\int \sec u \tan u\,du = \sec u + C$
12. $\int \csc u \cot u\,du = -\csc u + C$
13. $\int \tan u\,du = -\ln |\cos u| + C = \ln |\sec u| + C$
14. $\int \cot u\,du = \ln |\sin u| + C$

#### HYPERBOLIC FUNCTIONS
15. $\int \sinh u\,du = \cosh u + C$
16. $\int \cosh u\,du = \sinh u + C$
17. $\int \text{sech}^2 u\,du = \tanh u + C$
18. $\int \text{csch}^2 u\,du = -\coth u + C$
19. $\int \text{sech} u \tanh u\,du = -\text{sech} u + C$
20. $\int \text{csch} u \coth u\,du = -\text{csch} u + C$

#### ALGEBRAIC FUNCTIONS ($a > 0$)
21. $\int \frac{du}{\sqrt{a^2 - u^2}} = \sin^{-1}\left(\frac{u}{a}\right) + C \quad (|u| < a)$
22. $\int \frac{du}{a^2 + u^2} = \frac{1}{a}\tan^{-1}\left(\frac{u}{a}\right) + C$
23. $\int \frac{du}{u\sqrt{u^2 - a^2}} = \frac{1}{a}\sec^{-1}\left(\frac{|u|}{a}\right) + C \quad (0 < a < |u|)$
24. $\int \frac{du}{\sqrt{a^2 + u^2}} = \ln\left(u + \sqrt{u^2 + a^2}\right) + C$
25. $\int \frac{du}{\sqrt{u^2 - a^2}} = \ln\left|u + \sqrt{u^2 - a^2}\right| + C \quad (0 < a < |u|)$
26. $\int \frac{du}{a^2 - u^2} = \frac{1}{2a}\ln\left|\frac{a + u}{a - u}\right| + C$
27. $\int \frac{du}{u\sqrt{a^2 - u^2}} = -\frac{1}{a}\ln\left|\frac{a + \sqrt{a^2 - u^2}}{u}\right| + C \quad (0 < |u| < a)$
28. $\int \frac{du}{u\sqrt{a^2 + u^2}} = -\frac{1}{a}\ln\left|\frac{a + \sqrt{a^2 + u^2}}{u}\right| + C$

> **REMARK:** Formula 25 is a generalization of a result in Theorem 6.8.6. Readers who did not cover Section 6.8 can ignore Formulas 24–28 for now, since we will develop other methods for obtaining them in this chapter.

---

### QUICK CHECK EXERCISES 7.1
*(See page 491 for answers.)*

1. Use algebraic manipulation and (if necessary) $u$-substitution to integrate the function.
   (a) $\int \frac{x+1}{x}\,dx =$
   (b) $\int \frac{x+2}{x+1}\,dx =$
   (c) $\int \frac{2x+1}{x^2+1}\,dx =$
   (d) $\int x e^{3\ln x}\,dx =$
2. Use trigonometric identities and (if necessary) $u$-substitution to integrate the function.
   (a) $\int \frac{1}{\csc x}\,dx =$
   (b) $\int \frac{1}{\cos^2 x}\,dx =$
   (c) $\int (\cot^2 x + 1)\,dx =$
   (d) $\int \frac{1}{\sec x + \tan x}\,dx =$
3. Integrate the function.
   (a) $\int \sqrt{x-1}\,dx =$
   (b) $\int e^{2x+1}\,dx =$
   (c) $\int (\sin^3 x \cos x + \sin x \cos^3 x)\,dx =$
   (d) $\int \frac{1}{(e^x + e^{-x})^2}\,dx =$

#### Quick Check Answers 7.1
1. (a) $x + \ln |x| + C$ (b) $x + \ln |x+1| + C$ (c) $\ln(x^2+1) + \tan^{-1} x + C$ (d) $\frac{x^5}{5} + C$
2. (a) $-\cos x + C$ (b) $\tan x + C$ (c) $-\cot x + C$ (d) $\ln(1+\sin x) + C$
3. (a) $\frac{2}{3}(x-1)^{3/2} + C$ (b) $\frac{1}{2}e^{2x+1} + C$ (c) $\frac{1}{2}\sin^2 x + C$ (d) $\frac{1}{4}\tanh x + C$

---

## 7.2 INTEGRATION BY PARTS

In this section we will discuss an integration technique that is essentially an antiderivative formulation of the formula for differentiating a product of two functions.

### THE PRODUCT RULE AND INTEGRATION BY PARTS
Our primary goal in this section is to develop a general method for attacking integrals of the form
$$\int f(x)g(x)\,dx$$
As a first step, let $G(x)$ be any antiderivative of $g(x)$. In this case $G'(x) = g(x)$, so the product rule for differentiating $f(x)G(x)$ can be expressed as
$$\frac{d}{dx}[f(x)G(x)] = f(x)G'(x) + f'(x)G(x) = f(x)g(x) + f'(x)G(x) \tag{1}$$
Integrating both sides:
$$\int f(x)g(x)\,dx = f(x)G(x) - \int f'(x)G(x)\,dx \tag{2}$$
In practice, we usually rewrite (2) by letting
$$u = f(x), \quad du = f'(x)\,dx$$
$$v = G(x), \quad dv = G'(x)\,dx = g(x)\,dx$$
This yields the standard **Integration by Parts formula**:
$$\int u\,dv = uv - \int v\,du \tag{3}$$

#### Example 1
Evaluate $\int x \cos x\,dx$.

**Solution.** Let $u = x$ and $dv = \cos x\,dx$. Then $du = dx$ and $v = \int \cos x\,dx = \sin x$.
Applying Formula (3):
$$\int x \cos x\,dx = x \sin x - \int \sin x\,dx = x \sin x - (-\cos x) + C = x \sin x + \cos x + C$$

---

### GUIDELINES FOR INTEGRATION BY PARTS & THE LIATE METHOD
A strategy that often works is to choose $u$ and $dv$ so that $u$ becomes "simpler" when differentiated, while leaving a $dv$ that can be readily integrated to obtain $v$.

When the integrand is a product of two functions from different categories, use the **LIATE** rule of priority for choosing $u$:
1. **L** - Logarithmic functions ($\ln x, \log_b x$)
2. **I** - Inverse trigonometric functions ($\sin^{-1} x, \tan^{-1} x$)
3. **A** - Algebraic functions ($x^n, \sqrt{x}$)
4. **T** - Trigonometric functions ($\sin x, \cos x, \tan x$)
5. **E** - Exponential functions ($e^x, 2^x$)

Take $u$ to be the function type that appears higher on this list, and let $dv$ be the rest of the integrand.

#### Example 2
Evaluate $\int x e^x\,dx$.

**Solution.** By LIATE, let $u = x$ (Algebraic) and $dv = e^x\,dx$ (Exponential).
Then $du = dx$ and $v = e^x$.
$$\int x e^x\,dx = x e^x - \int e^x\,dx = x e^x - e^x + C$$

#### Example 3
Evaluate $\int \ln x\,dx$.

**Solution.** Let $u = \ln x$ and $dv = dx$. Then $du = \frac{1}{x}\,dx$ and $v = x$.
$$\int \ln x\,dx = x\ln x - \int x\left(\frac{1}{x}\right)dx = x\ln x - \int dx = x\ln x - x + C$$

---

### REPEATED INTEGRATION BY PARTS

#### Example 4
Evaluate $\int x^2 e^{-x}\,dx$.

**Solution.** Let $u = x^2, dv = e^{-x}dx \implies du = 2x\,dx, v = -e^{-x}$.
$$\int x^2 e^{-x}\,dx = -x^2 e^{-x} + 2\int x e^{-x}\,dx$$
For the remaining integral, let $u = x, dv = e^{-x}dx \implies du = dx, v = -e^{-x}$:
$$\int x e^{-x}\,dx = -x e^{-x} - \int (-e^{-x})\,dx = -x e^{-x} - e^{-x}$$
Substituting back:
$$\int x^2 e^{-x}\,dx = -x^2 e^{-x} + 2(-x e^{-x} - e^{-x}) + C = -(x^2 + 2x + 2)e^{-x} + C$$

#### Example 5
Evaluate $\int e^x \cos x\,dx$.

**Solution.** Let $u = \cos x, dv = e^x dx \implies du = -\sin x\,dx, v = e^x$.
$$\int e^x \cos x\,dx = e^x \cos x + \int e^x \sin x\,dx \tag{5}$$
For $\int e^x \sin x\,dx$, let $u = \sin x, dv = e^x dx \implies du = \cos x\,dx, v = e^x$:
$$\int e^x \sin x\,dx = e^x \sin x - \int e^x \cos x\,dx$$
Substituting into (5):
$$\int e^x \cos x\,dx = e^x \cos x + e^x \sin x - \int e^x \cos x\,dx$$
$$2\int e^x \cos x\,dx = e^x \cos x + e^x \sin x \implies \int e^x \cos x\,dx = \frac{1}{2}e^x \cos x + \frac{1}{2}e^x \sin x + C$$

---

### TABULAR INTEGRATION BY PARTS
For integrals of the form $\int p(x)f(x)\,dx$ where $p(x)$ is a polynomial:
1. **Column 1 (Differentiation):** Differentiate $p(x)$ repeatedly until 0 is reached.
2. **Column 2 (Integration):** Integrate $f(x)$ repeatedly.
3. Draw diagonal arrows from row $i$ in Column 1 to row $i+1$ in Column 2.
4. Alternate signs $+ , -, +, -, \dots$ starting with $+$ on the first arrow.
5. Multiply connected pairs with their assigned signs and sum the terms.

| Repeated Differentiation $D$ | Repeated Integration $I$ | Sign |
| :---: | :---: | :---: |
| $x^2 - x$ | $\cos x$ | |
| $2x - 1$ | $\sin x$ | $(+)$ |
| $2$ | $-\cos x$ | $(-)$ |
| $0$ | $-\sin x$ | $(+)$ |

$$\int (x^2 - x)\cos x\,dx = (x^2 - x)\sin x + (2x - 1)\cos x - 2\sin x + C = (x^2 - x - 2)\sin x + (2x - 1)\cos x + C$$

#### Example 6
Evaluate $\int x^2\sqrt{x-1}\,dx$ using tabular integration by parts.

**Solution.**
* $D$-column: $x^2 \to 2x \to 2 \to 0$
* $I$-column: $(x-1)^{1/2} \to \frac{2}{3}(x-1)^{3/2} \to \frac{4}{15}(x-1)^{5/2} \to \frac{8}{105}(x-1)^{7/2}$
$$\int x^2\sqrt{x-1}\,dx = \frac{2}{3}x^2(x-1)^{3/2} - \frac{8}{15}x(x-1)^{5/2} + \frac{16}{105}(x-1)^{7/2} + C$$

---

### INTEGRATION BY PARTS FOR DEFINITE INTEGRALS
$$\int_a^b u\,dv = \left[uv\right]_a^b - \int_a^b v\,du \tag{7}$$

#### Example 7
Evaluate $\int_0^1 \tan^{-1} x\,dx$.

**Solution.** Let $u = \tan^{-1} x, dv = dx \implies du = \frac{1}{1+x^2}dx, v = x$.
$$\int_0^1 \tan^{-1} x\,dx = [x\tan^{-1} x]_0^1 - \int_0^1 \frac{x}{1+x^2}\,dx = \left(1 \cdot \frac{\pi}{4} - 0\right) - \left[\frac{1}{2}\ln(1+x^2)\right]_0^1 = \frac{\pi}{4} - \frac{1}{2}\ln 2 = \frac{\pi}{4} - \ln\sqrt{2}$$

---

### REDUCTION FORMULAS
Integration by parts yields formulas that express an integral of a power in terms of a lower power:
$$\int \sin^n x\,dx = -\frac{1}{n}\sin^{n-1} x \cos x + \frac{n-1}{n}\int \sin^{n-2} x\,dx \tag{9}$$
$$\int \cos^n x\,dx = \frac{1}{n}\cos^{n-1} x \sin x + \frac{n-1}{n}\int \cos^{n-2} x\,dx \tag{10}$$
$$\int \sec^n x\,dx = \frac{\sec^{n-2} x \tan x}{n-1} + \frac{n-2}{n-1}\int \sec^{n-2} x\,dx \tag{20}$$
$$\int \tan^n x\,dx = \frac{\tan^{n-1} x}{n-1} - \int \tan^{n-2} x\,dx \tag{19}$$
$$\int x^n e^x\,dx = x^n e^x - n\int x^{n-1} e^x\,dx$$

#### Example 8
Evaluate $\int \cos^4 x\,dx$.

**Solution.** Applying (10) with $n=4$:
$$\int \cos^4 x\,dx = \frac{1}{4}\cos^3 x \sin x + \frac{3}{4}\int \cos^2 x\,dx = \frac{1}{4}\cos^3 x \sin x + \frac{3}{4}\left(\frac{1}{2}\cos x \sin x + \frac{1}{2}x\right) + C = \frac{1}{4}\cos^3 x \sin x + \frac{3}{8}\cos x \sin x + \frac{3}{8}x + C$$

---

### QUICK CHECK EXERCISES 7.2
*(See page 500 for answers.)*

1. (a) If $G'(x) = g(x)$, then $\int f(x)g(x)\,dx = f(x)G(x) - \int f'(x)G(x)\,dx$.
   (b) If $u = f(x)$ and $v = G(x)$, then $\int u\,dv = uv - \int v\,du$.
2. Choice of $u$ and $dv$:
   (a) $\int x\ln x\,dx \implies u = \ln x, dv = x\,dx$
   (b) $\int (x-2)\sin x\,dx \implies u = x-2, dv = \sin x\,dx$
   (c) $\int \sin^{-1} x\,dx \implies u = \sin^{-1} x, dv = dx$
   (d) $\int \frac{x}{\sqrt{x-1}}\,dx \implies u = x, dv = \frac{1}{\sqrt{x-1}}\,dx$
3. (a) $\int x e^{2x}\,dx = \left(\frac{x}{2} - \frac{1}{4}\right)e^{2x} + C$  
   (b) $\int \ln(x-1)\,dx = (x-1)\ln(x-1) - x + C$  
   (c) $\int_0^{\pi/6} x \sin 3x\,dx = \frac{1}{9}$
4. $\int \sin^3 x\,dx = -\frac{1}{3}\sin^2 x \cos x - \frac{2}{3}\cos x + C$

---

## 7.3 INTEGRATING TRIGONOMETRIC FUNCTIONS

### INTEGRATING POWERS OF SINE AND COSINE
* For $n = 2$:
  $$\int \sin^2 x\,dx = \frac{1}{2}x - \frac{1}{4}\sin 2x + C = \frac{1}{2}x - \frac{1}{2}\sin x \cos x + C$$
  $$\int \cos^2 x\,dx = \frac{1}{2}x + \frac{1}{4}\sin 2x + C = \frac{1}{2}x + \frac{1}{2}\sin x \cos x + C$$
* For $n = 3$:
  $$\int \sin^3 x\,dx = \frac{1}{3}\cos^3 x - \cos x + C$$
  $$\int \cos^3 x\,dx = \sin x - \frac{1}{3}\sin^3 x + C$$
* For $n = 4$:
  $$\int \sin^4 x\,dx = \frac{3}{8}x - \frac{1}{4}\sin 2x + \frac{1}{32}\sin 4x + C$$
  $$\int \cos^4 x\,dx = \frac{3}{8}x + \frac{1}{4}\sin 2x + \frac{1}{32}\sin 4x + C$$

---

### PRODUCTS OF SINES AND COSINES: $\int \sin^m x \cos^n x\,dx$

| Condition | Procedure | Relevant Identity |
| :--- | :--- | :--- |
| **$n$ is odd** | Split off $\cos x$, express remaining cosine powers in terms of $\sin x$, substitute $u = \sin x$. | $\cos^2 x = 1 - \sin^2 x$ |
| **$m$ is odd** | Split off $\sin x$, express remaining sine powers in terms of $\cos x$, substitute $u = \cos x$. | $\sin^2 x = 1 - \cos^2 x$ |
| **$m$ and $n$ both even** | Use half-angle identities to reduce powers of $\sin x$ and $\cos x$. | $\sin^2 x = \frac{1}{2}(1 - \cos 2x)$, $\cos^2 x = \frac{1}{2}(1 + \cos 2x)$ |

#### Example 2
(a) $\int \sin^4 x \cos^5 x\,dx = \int \sin^4 x (1 - \sin^2 x)^2 \cos x\,dx = \int u^4(1 - 2u^2 + u^4)\,du = \frac{1}{5}\sin^5 x - \frac{2}{7}\sin^7 x + \frac{1}{9}\sin^9 x + C$  
(b) $\int \sin^4 x \cos^4 x\,dx = \int \left(\frac{1}{2}\sin 2x\right)^4 dx = \frac{1}{16}\int \sin^4 2x\,dx = \frac{3}{128}x - \frac{1}{128}\sin 4x + \frac{1}{1024}\sin 8x + C$

---

### PRODUCTS OF SINES AND COSINES WITH DIFFERENT FREQUENCIES
Use product-to-sum identities:
$$\sin \alpha \cos \beta = \frac{1}{2}[\sin(\alpha - \beta) + \sin(\alpha + \beta)] \tag{16}$$
$$\sin \alpha \sin \beta = \frac{1}{2}[\cos(\alpha - \beta) - \cos(\alpha + \beta)] \tag{17}$$
$$\cos \alpha \cos \beta = \frac{1}{2}[\cos(\alpha - \beta) + \cos(\alpha + \beta)] \tag{18}$$

#### Example 3
$$\int \sin 7x \cos 3x\,dx = \frac{1}{2}\int (\sin 4x + \sin 10x)\,dx = -\frac{1}{8}\cos 4x - \frac{1}{20}\cos 10x + C$$

---

### INTEGRATING PRODUCTS OF TANGENTS AND SECANTS: $\int \tan^m x \sec^n x\,dx$

| Condition | Procedure | Relevant Identity |
| :--- | :--- | :--- |
| **$n$ is even** | Split off $\sec^2 x$, express remaining secants in terms of $\tan x$, substitute $u = \tan x$. | $\sec^2 x = \tan^2 x + 1$ |
| **$m$ is odd** | Split off $\sec x \tan x$, express remaining tangents in terms of $\sec x$, substitute $u = \sec x$. | $\tan^2 x = \sec^2 x - 1$ |
| **$m$ even, $n$ odd** | Express powers of $\tan x$ in terms of $\sec x$, then use reduction formulas for powers of $\sec x$. | $\tan^2 x = \sec^2 x - 1$ |

Key basic results:
$$\int \tan x\,dx = \ln |\sec x| + C$$
$$\int \sec x\,dx = \ln |\sec x + \tan x| + C$$
$$\int \sec^3 x\,dx = \frac{1}{2}\sec x \tan x + \frac{1}{2}\ln |\sec x + \tan x| + C$$

---

### APPLICATION: MERCATOR'S MAP OF THE WORLD
On a Mercator projection where the equator has length $L$, the distance $D_\beta$ from the equator to latitude $\beta^\circ$ is
$$D_\beta = \frac{L}{2\pi}\int_0^{\beta\pi/180} \sec x\,dx$$
Between latitudes $\alpha^\circ$ and $\beta^\circ$ on the same side:
$$D = \frac{L}{2\pi}\ln\left|\frac{\sec \beta^\circ + \tan \beta^\circ}{\sec \alpha^\circ + \tan \alpha^\circ}\right|$$

---

### QUICK CHECK EXERCISES 7.3
*(See page 508 for answers.)*
1. (a) $\sin^2 x = \frac{1-\cos 2x}{2}$ (b) $\cos^2 x = \frac{1+\cos 2x}{2}$ (c) $\cos^2 x - \sin^2 x = \cos 2x$
2. (a) $\tan x + C$ (b) $\tan x - x + C$ (c) $\ln |\sec x + \tan x| + C$ (d) $\ln |\sec x| + C$
3. (a) $\int u^2 du$ (b) $\int (u^2 - 1)u^2 du$ (c) $\int u^3 du$ (d) $\int (u^2 - 1)du$

---

## 7.4 TRIGONOMETRIC SUBSTITUTIONS

Trigonometric substitutions eliminate radicals in expressions of the forms $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, and $\sqrt{x^2 - a^2}$.

### SUMMARY OF TRIGONOMETRIC SUBSTITUTIONS (Table 7.4.1)

| Expression | Substitution | Restriction on $\theta$ | Simplification | Reference Triangle |
| :--- | :--- | :--- | :--- | :--- |
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$, $dx = a\cos\theta\,d\theta$ | $-\pi/2 \le \theta \le \pi/2$ | $a^2 - a^2\sin^2\theta = a^2\cos^2\theta \implies \sqrt{a^2-x^2} = a\cos\theta$ | Opp: $x$, Hyp: $a$, Adj: $\sqrt{a^2-x^2}$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$, $dx = a\sec^2\theta\,d\theta$ | $-\pi/2 < \theta < \pi/2$ | $a^2 + a^2\tan^2\theta = a^2\sec^2\theta \implies \sqrt{a^2+x^2} = a\sec\theta$ | Opp: $x$, Adj: $a$, Hyp: $\sqrt{a^2+x^2}$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$, $dx = a\sec\theta\tan\theta\,d\theta$ | $0 \le \theta < \pi/2$ ($x \ge a$), $\pi/2 < \theta \le \pi$ ($x \le -a$) | $a^2\sec^2\theta - a^2 = a^2\tan^2\theta \implies \sqrt{x^2-a^2} = a\tan\theta$ | Hyp: $x$, Adj: $a$, Opp: $\sqrt{x^2-a^2}$ |

#### Example 1
Evaluate $\int \frac{dx}{x^2\sqrt{4-x^2}}$.

**Solution.** Let $x = 2\sin\theta, dx = 2\cos\theta\,d\theta$.
$$\int \frac{2\cos\theta\,d\theta}{(4\sin^2\theta)(2\cos\theta)} = \frac{1}{4}\int \csc^2\theta\,d\theta = -\frac{1}{4}\cot\theta + C = -\frac{\sqrt{4-x^2}}{4x} + C$$

#### Example 3 (Area of an Ellipse)
For $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$:
$$A = 4\frac{b}{a}\int_0^a \sqrt{a^2 - x^2}\,dx = 4ab \int_0^{\pi/2} \cos^2\theta\,d\theta = 4ab\left(\frac{\pi}{4}\right) = \pi ab$$

---

### INTEGRALS INVOLVING $ax^2 + bx + c$
Complete the square: $ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right)$.

#### Example 6
Evaluate $\int \frac{x}{x^2 - 4x + 8}\,dx$.

**Solution.** $x^2 - 4x + 8 = (x-2)^2 + 4$. Let $u = x-2, du = dx, x = u+2$:
$$\int \frac{u+2}{u^2+4}\,du = \frac{1}{2}\int \frac{2u}{u^2+4}\,du + 2\int \frac{du}{u^2+4} = \frac{1}{2}\ln(u^2+4) + \tan^{-1}\left(\frac{u}{2}\right) + C = \frac{1}{2}\ln[(x-2)^2+4] + \tan^{-1}\left(\frac{x-2}{2}\right) + C$$

---

### QUICK CHECK EXERCISES 7.4
*(See page 514 for answers.)*
1. (a) $x = a\sin\theta$ (b) $x = a\tan\theta$ (c) $x = a\sec\theta$
2. If $x = 2\sec\theta$, (a) $\sin\theta = \frac{\sqrt{x^2-4}}{x}$ (b) $\cos\theta = \frac{2}{x}$ (c) $\tan\theta = \frac{\sqrt{x^2-4}}{2}$
3. (a) $x = 3\tan\theta$ (b) $x = 3\sin\theta$ (c) $x = \frac{1}{3}\sin\theta$ (d) $x = 3\sec\theta$ (e) $x = \sqrt{3}\tan\theta$ (f) $x = \frac{1}{9}\tan\theta$
4. (a) $u = x-1$ (b) $u = x-3$ (c) $u = x+2$

---

## 7.5 INTEGRATING RATIONAL FUNCTIONS BY PARTIAL FRACTIONS

Every proper rational function $P(x)/Q(x)$ ($\deg P < \deg Q$) can be decomposed into a sum of partial fractions based on the factorization of $Q(x)$ into linear and irreducible quadratic factors.

### RULES FOR PARTIAL FRACTION DECOMPOSITION

* **Linear Factor Rule:** For each factor $(ax + b)^m$, include:
  $$\frac{A_1}{ax+b} + \frac{A_2}{(ax+b)^2} + \dots + \frac{A_m}{(ax+b)^m}$$
* **Quadratic Factor Rule:** For each irreducible factor $(ax^2 + bx + c)^m$, include:
  $$\frac{A_1 x + B_1}{ax^2+bx+c} + \frac{A_2 x + B_2}{(ax^2+bx+c)^2} + \dots + \frac{A_m x + B_m}{(ax^2+bx+c)^m}$$

#### Example 1 (Distinct Linear Factors)
$$\int \frac{dx}{(x-1)(x+2)} = \int \left(\frac{1/3}{x-1} - \frac{1/3}{x+2}\right)dx = \frac{1}{3}\ln|x-1| - \frac{1}{3}\ln|x+2| + C = \frac{1}{3}\ln\left|\frac{x-1}{x+2}\right| + C$$

#### Example 2 (Repeated Linear Factors)
$$\frac{2x+4}{x^2(x-2)} = \frac{-2}{x} + \frac{-2}{x^2} + \frac{2}{x-2} \implies \int \frac{2x+4}{x^2(x-2)}\,dx = -2\ln|x| + \frac{2}{x} + 2\ln|x-2| + C = 2\ln\left|\frac{x-2}{x}\right| + \frac{2}{x} + C$$

#### Improper Rational Functions
If $\deg P \ge \deg Q$, perform polynomial long division first:
$$\frac{P(x)}{Q(x)} = \text{Quotient}(x) + \frac{\text{Remainder}(x)}{Q(x)}$$

---

### QUICK CHECK EXERCISES 7.5
*(See page 523 for answers.)*
1. Forms: $\frac{A}{(ax+b)^k}$ or $\frac{Ax+B}{(ax^2+bx+c)^k}$.
2. (a) Degree of numerator < degree of denominator. (b) $\deg P < \deg Q$. (c) Perform polynomial long division.
4. (a) $A = 1$ (b) $B = 2$.
5. (a) $\ln\left|\frac{x+1}{1-2x}\right| + C$ (b) $\frac{2}{3}\ln|3x+2| - \tan^{-1} x + C$.

---

## 7.6 USING COMPUTER ALGEBRA SYSTEMS AND TABLES OF INTEGRALS

### MATCHES & SUBSTITUTIONS
* **Fractional powers of $x$:** Substitute $u = x^{1/n}$ where $n = \text{lcm}$ of denominators.
  * Example: $\int \frac{\sqrt{x}}{1+\sqrt[3]{x}}\,dx$ with $u = x^{1/6} \implies x = u^6, dx = 6u^5 du$.
* **Weierstrass Substitution:** For rational functions of $\sin x$ and $\cos x$, set $u = \tan(x/2)$:
  $$\sin x = \frac{2u}{1+u^2}, \quad \cos x = \frac{1-u^2}{1+u^2}, \quad dx = \frac{2}{1+u^2}\,du \tag{5}$$

---

### QUICK CHECK EXERCISES 7.6
*(See page 533 for answers.)*
3. (a) $\frac{1}{4}\ln\left|\frac{x+2}{x-2}\right| + C$
   (b) $\frac{1}{6}\sin 3x + \frac{1}{2}\sin x + C$
   (c) $-\frac{e^x}{2}\sqrt{1-e^{2x}} + \frac{1}{2}\sin^{-1}(e^x) + C$
   (d) $\frac{1}{2}\ln(x^2 - 4x + 8) + \tan^{-1}\left(\frac{x-2}{2}\right) + C$

---

## 7.7 NUMERICAL INTEGRATION; SIMPSON’S RULE

### RIEMANN SUM & APPROXIMATION FORMULAS
Let $\Delta x = \frac{b-a}{n}$, $y_k = f(x_k)$, $y_{m_k} = f(m_k)$.

* **Left Endpoint:** $L_n = \frac{b-a}{n}[y_0 + y_1 + \dots + y_{n-1}]$
* **Right Endpoint:** $R_n = \frac{b-a}{n}[y_1 + y_2 + \dots + y_n]$
* **Midpoint Approximation:** $M_n = \frac{b-a}{n}[y_{m_1} + y_{m_2} + \dots + y_{m_n}]$
* **Trapezoidal Rule:**
  $$T_n = \frac{1}{2}(L_n + R_n) = \frac{b-a}{2n}[y_0 + 2y_1 + 2y_2 + \dots + 2y_{n-1} + y_n] \tag{2}$$
* **Simpson’s Rule ($n$ even):**
  $$S_n = \frac{1}{3}(2M_{n/2} + T_{n/2}) = \frac{b-a}{3n}[y_0 + 4y_1 + 2y_2 + 4y_3 + 2y_4 + \dots + 2y_{n-2} + 4y_{n-1} + y_n] \tag{8}$$

---

### ERROR BOUNDS THEOREMS
* **Theorem 7.7.1 (Concavity Relationships):**
  * If $f$ is concave down on $(a, b)$: $T_n < \int_a^b f(x)\,dx < M_n$ and $|E_M| < |E_T|$.
  * If $f$ is concave up on $(a, b)$: $M_n < \int_a^b f(x)\,dx < T_n$ and $|E_M| < |E_T|$.
* **Theorem 7.7.2 (Midpoint and Trapezoidal Bounds):**
  $$|E_M| \le \frac{(b-a)^3 K_2}{24n^2}, \quad |E_T| \le \frac{(b-a)^3 K_2}{12n^2} \quad \text{where } |f''(x)| \le K_2$$
* **Theorem 7.7.3 (Simpson's Error Bound):**
  $$|E_S| \le \frac{(b-a)^5 K_4}{180n^4} \quad \text{where } |f^{(4)}(x)| \le K_4$$

> Simpson's Rule is exact ($|E_S| = 0$) for any polynomial of degree 3 or less!

---

### QUICK CHECK EXERCISES 7.7
*(See page 547 for answers.)*
1. (a) $T_n = \frac{1}{2}(L_n + R_n)$ (b) $T_n = \frac{b-a}{2n}[y_0 + 2y_1 + \dots + 2y_{n-1} + y_n]$
2. Concave up: $M_n < I < T_n$.
3. (a) $S_6 = \frac{2}{3}M_3 + \frac{1}{3}T_3$ (b) $S_6 = \frac{b-a}{18}(y_0 + 4y_1 + 2y_2 + 4y_3 + 2y_4 + 4y_5 + y_6)$.
4. (a) $\frac{1}{2400}$ (b) $\frac{1}{1200}$ (c) $\frac{1}{1,800,000}$.
5. For $\int_1^3 \frac{1}{x^2}\,dx$: (a) $M_1 = 1/2$ (b) $T_1 = 10/9$ (c) $S_2 = 19/27$.

---

## 7.8 IMPROPER INTEGRALS

### TYPE 1: INFINITE INTERVALS
* **Definition 7.8.1:** $\int_a^{+\infty} f(x)\,dx = \lim_{b \to +\infty} \int_a^b f(x)\,dx$
* **Definition 7.8.3:** $\int_{-\infty}^b f(x)\,dx = \lim_{a \to -\infty} \int_a^b f(x)\,dx$
* $\int_{-\infty}^{+\infty} f(x)\,dx = \int_{-\infty}^c f(x)\,dx + \int_c^{+\infty} f(x)\,dx$ (converges if and only if both parts converge).

> **7.8.2 THEOREM ($p$-Integrals over $[1, +\infty)$)**
> $$\int_1^{+\infty} \frac{dx}{x^p} = \begin{cases} \frac{1}{p-1} & \text{if } p > 1 \\ \text{diverges} & \text{if } p \le 1 \end{cases}$$

---

### TYPE 2: INFINITE DISCONTINUITIES
* **Discontinuity at $b$ (Definition 7.8.4):** $\int_a^b f(x)\,dx = \lim_{k \to b^-} \int_a^k f(x)\,dx$
* **Discontinuity at $a$ (Definition 7.8.5):** $\int_a^b f(x)\,dx = \lim_{k \to a^+} \int_k^b f(x)\,dx$
* **Discontinuity at interior point $c \in (a, b)$:** $\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$

> **$p$-Integrals over $(0, 1]$:**
> $$\int_0^1 \frac{dx}{x^p} \text{ converges for } p < 1, \text{ diverges for } p \ge 1$$

---

### QUICK CHECK EXERCISES 7.8
*(See page 557 for answers.)*
1. (a) Proper (b) Improper ($x = \pi$) (c) Improper (infinite interval) (d) Improper (infinite interval & asymptote at $x=1$).
3. $\int_1^{+\infty} x^{-p}dx$ converges to $\frac{1}{p-1}$ provided $p > 1$.
4. (a) $1$ (b) Diverges (c) Diverges (d) $3$.

---

## CHAPTER 7 MAKING CONNECTIONS: THE GAMMA FUNCTION

> **The Gamma Function $\Gamma(x)$:**
> $$\Gamma(x) = \int_0^{+\infty} t^{x-1}e^{-t}\,dt \quad (x > 0)$$
> * $\Gamma(1) = 1$
> * $\Gamma(x+1) = x\Gamma(x) \implies \Gamma(n) = (n-1)!$ for positive integers $n$.
> * $\Gamma(1/2) = \sqrt{\pi}$
> * $\Gamma(3/2) = \frac{1}{2}\sqrt{\pi}, \quad \Gamma(5/2) = \frac{3}{4}\sqrt{\pi}$
