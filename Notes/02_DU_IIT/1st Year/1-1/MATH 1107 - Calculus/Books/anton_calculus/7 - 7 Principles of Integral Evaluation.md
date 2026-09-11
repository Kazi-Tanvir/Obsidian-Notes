# CHAPTER 7: PRINCIPLES OF INTEGRAL EVALUATION

> © AP/Wide World Photos  
> *The floating roof on the Stade de France sports complex is an ellipse. Finding the arc length of an ellipse involves numerical integration techniques introduced in this chapter.*

In earlier chapters we obtained many basic integration formulas as an immediate consequence of the corresponding differentiation formulas. For example, knowing that the derivative of $\sin x$ is $\cos x$ enabled us to deduce that the integral of $\cos x$ is $\sin x$. Subsequently, we expanded our integration repertoire by introducing the method of $u$-substitution. That method enabled us to integrate many functions by transforming the integrand of an unfamiliar integral into a familiar form. However, $u$-substitution alone is not adequate to handle the wide variety of integrals that arise in applications, so additional integration techniques are still needed. In this chapter we will discuss some of those techniques, and we will provide a more systematic procedure for attacking unfamiliar integrals. We will talk more about numerical approximations of definite integrals, and we will explore the idea of integrating over infinite intervals.

---

## 7.1 AN OVERVIEW OF INTEGRATION METHODS

In this section we will give a brief overview of methods for evaluating integrals, and we will review the integration formulas that were discussed in earlier sections.

### METHODS FOR APPROACHING INTEGRATION PROBLEMS

There are three basic approaches for evaluating unfamiliar integrals:

* **Technology**—CAS programs such as *Mathematica*, *Maple*, and the open source program *Sage* are capable of evaluating extremely complicated integrals, and such programs are increasingly available for both computers and handheld calculators.
* **Tables**—Prior to the development of CAS programs, scientists relied heavily on tables to evaluate difficult integrals arising in applications. Such tables were compiled over many years, incorporating the skills and experience of many people. One such table appears in the endpapers of this text, but more comprehensive tables appear in various reference books such as the *CRC Standard Mathematical Tables and Formulae*, CRC Press, Inc., 2002.
* **Transformation Methods**—Transformation methods are methods for converting unfamiliar integrals into familiar integrals. These include $u$-substitution, algebraic manipulation of the integrand, and other methods that we will discuss in this chapter.

None of the three methods is perfect; for example, CAS programs often encounter integrals that they cannot evaluate and they sometimes produce answers that are unnecessarily complicated, tables are not exhaustive and may not include a particular integral of interest, and transformation methods rely on human ingenuity that may prove to be inadequate in difficult problems.

In this chapter we will focus on transformation methods and tables, so it will not be necessary to have a CAS such as *Mathematica*, *Maple*, or *Sage*. However, if you have a CAS, then you can use it to confirm the results in the examples, and there are exercises that are designed to be solved with a CAS. If you have a CAS, keep in mind that many of the algorithms that it uses are based on the methods we will discuss here, so an understanding of these methods will help you to use your technology in a more informed way.

---

### A REVIEW OF FAMILIAR INTEGRATION FORMULAS

The following is a list of basic integrals that we have encountered thus far:

#### CONSTANTS, POWERS, EXPONENTIALS

1. $\int du = u + C$
2. $\int a \, du = a \int du = au + C$
3. $\int u^r \, du = \frac{u^{r+1}}{r + 1} + C, \quad r \neq -1$
4. $\int \frac{du}{u} = \ln |u| + C$
5. $\int e^u \, du = e^u + C$
6. $\int b^u \, du = \frac{b^u}{\ln b} + C, \quad b > 0, b \neq 1$

#### TRIGONOMETRIC FUNCTIONS

7. $\int \sin u \, du = -\cos u + C$
8. $\int \cos u \, du = \sin u + C$
9. $\int \sec^2 u \, du = \tan u + C$
10. $\int \csc^2 u \, du = -\cot u + C$
11. $\int \sec u \tan u \, du = \sec u + C$
12. $\int \csc u \cot u \, du = -\csc u + C$
13. $\int \tan u \, du = -\ln |\cos u| + C$
14. $\int \cot u \, du = \ln |\sin u| + C$

#### HYPERBOLIC FUNCTIONS

15. $\int \sinh u \, du = \cosh u + C$
16. $\int \cosh u \, du = \sinh u + C$
17. $\int \text{sech}^2 u \, du = \tanh u + C$
18. $\int \text{csch}^2 u \, du = -\coth u + C$
19. $\int \text{sech } u \tanh u \, du = -\text{sech } u + C$
20. $\int \text{csch } u \coth u \, du = -\text{csch } u + C$

#### ALGEBRAIC FUNCTIONS ($a > 0$)

21. $\int \frac{du}{\sqrt{a^2 - u^2}} = \sin^{-1}\left(\frac{u}{a}\right) + C \quad (|u| < a)$
22. $\int \frac{du}{a^2 + u^2} = \frac{1}{a}\tan^{-1}\left(\frac{u}{a}\right) + C$
23. $\int \frac{du}{u\sqrt{u^2 - a^2}} = \frac{1}{a}\sec^{-1}\left|\frac{u}{a}\right| + C \quad (0 < a < |u|)$
24. $\int \frac{du}{\sqrt{a^2 + u^2}} = \ln(u + \sqrt{u^2 + a^2}) + C$
25. $\int \frac{du}{\sqrt{u^2 - a^2}} = \ln|u + \sqrt{u^2 - a^2}| + C \quad (0 < a < |u|)$
26. $\int \frac{du}{a^2 - u^2} = \frac{1}{2a}\ln\left|\frac{a + u}{a - u}\right| + C$
27. $\int \frac{du}{u\sqrt{a^2 - u^2}} = -\frac{1}{a}\ln\left|\frac{a + \sqrt{a^2 - u^2}}{u}\right| + C \quad (0 < |u| < a)$
28. $\int \frac{du}{u\sqrt{a^2 + u^2}} = -\frac{1}{a}\ln\left|\frac{a + \sqrt{a^2 + u^2}}{u}\right| + C$

> **REMARK** Formula 25 is a generalization of a result in Theorem 6.8.6. Readers who did not cover Section 6.8 can ignore Formulas 24–28 for now, since we will develop other methods for obtaining them in this chapter.

---

### QUICK CHECK EXERCISES 7.1
*(See page 491 for answers.)*

1. Use algebraic manipulation and (if necessary) $u$-substitution to integrate the function.  
   (a) $\int \frac{x+1}{x} dx = \underline{\hspace{2cm}}$  
   (b) $\int \frac{x+2}{x+1} dx = \underline{\hspace{2cm}}$  
   (c) $\int \frac{2x+1}{x^2+1} dx = \underline{\hspace{2cm}}$  
   (d) $\int x e^{3\ln x} dx = \underline{\hspace{2cm}}$

2. Use trigonometric identities and (if necessary) $u$-substitution to integrate the function.  
   (a) $\int \frac{1}{\csc x} dx = \underline{\hspace{2cm}}$  
   (b) $\int \frac{1}{\cos^2 x} dx = \underline{\hspace{2cm}}$  
   (c) $\int (\cot^2 x + 1) dx = \underline{\hspace{2cm}}$  
   (d) $\int \frac{1}{\sec x + \tan x} dx = \underline{\hspace{2cm}}$

3. Integrate the function.  
   (a) $\int \sqrt{x-1} dx = \underline{\hspace{2cm}}$  
   (b) $\int e^{2x+1} dx = \underline{\hspace{2cm}}$  
   (c) $\int (\sin^3 x \cos x + \sin x \cos^3 x) dx = \underline{\hspace{2cm}}$  
   (d) $\int \frac{1}{(e^x + e^{-x})^2} dx = \underline{\hspace{2cm}}$

---

### EXERCISE SET 7.1

**1–30 Evaluate the integrals by making appropriate $u$-substitutions and applying the formulas reviewed in this section.**

1. $\int (4 - 2x)^3 dx$
2. $\int \sqrt[3]{4 + 2x} dx$
3. $\int x \sec^2(x^2) dx$
4. $\int 4x \tan(x^2) dx$
5. $\int \frac{\sin 3x}{2 + \cos 3x} dx$
6. $\int \frac{1}{9 + 4x^2} dx$
7. $\int e^x \sinh(e^x) dx$
8. $\int \frac{\sec(\ln x)\tan(\ln x)}{x} dx$
9. $\int e^{\tan x} \sec^2 x dx$
10. $\int \frac{x}{\sqrt{1 - x^4}} dx$
11. $\int \cos^5 5x \sin 5x dx$
12. $\int \frac{\cos x}{\sin x \sqrt{\sin^2 x + 1}} dx$
13. $\int \frac{e^x}{\sqrt{4 + e^{2x}}} dx$
14. $\int \frac{e^{\tan^{-1} x}}{1 + x^2} dx$
15. $\int \frac{e^{\sqrt{x-1}}}{\sqrt{x-1}} dx$
16. $\int (x + 1) \cot(x^2 + 2x) dx$
17. $\int \frac{\cosh \sqrt{x}}{\sqrt{x}} dx$
18. $\int \frac{dx}{x(\ln x)^2}$
19. $\int \frac{dx}{\sqrt{x}\sqrt[3]{x}}$
20. $\int \sec(\sin\theta)\tan(\sin\theta)\cos\theta d\theta$
21. $\int \frac{\text{csch}^2(2/x)}{x^2} dx$
22. $\int \frac{dx}{\sqrt{x^2 - 4}}$
23. $\int \frac{e^{-x}}{4 - e^{-2x}} dx$
24. $\int \frac{\cos(\ln x)}{x} dx$
25. $\int \frac{e^x}{\sqrt{1 - e^{2x}}} dx$
26. $\int \frac{\sinh(x^{-1/2})}{x^{3/2}} dx$
27. $\int \frac{x}{\csc(x^2)} dx$
28. $\int \frac{e^x}{\sqrt{4 - e^{2x}}} dx$
29. $\int x 4^{-x^2} dx$
30. $\int 2^{\pi x} dx$

#### FOCUS ON CONCEPTS

31. (a) Evaluate the integral $\int \sin x \cos x dx$ using the substitution $u = \sin x$.  
    (b) Evaluate the integral $\int \sin x \cos x dx$ using the identity $\sin 2x = 2\sin x \cos x$.  
    (c) Explain why your answers to parts (a) and (b) are consistent.

32. (a) Derive the identity
    $$\frac{\text{sech}^2 x}{1 + \tanh^2 x} = \text{sech } 2x$$  
    (b) Use the result in part (a) to evaluate $\int \text{sech } x dx$.  
    (c) Derive the identity
    $$\text{sech } x = \frac{2e^x}{e^{2x} + 1}$$  
    (d) Use the result in part (c) to evaluate $\int \text{sech } x dx$.  
    (e) Explain why your answers to parts (b) and (d) are consistent.

33. (a) Derive the identity
    $$\frac{\sec^2 x}{\tan x} = \frac{1}{\sin x \cos x}$$  
    (b) Use the identity $\sin 2x = 2\sin x \cos x$ along with the result in part (a) to evaluate $\int \csc x dx$.  
    (c) Use the identity $\cos x = \sin[(\pi/2) - x]$ along with your answer to part (a) to evaluate $\int \sec x dx$.

---

### QUICK CHECK ANSWERS 7.1

1. (a) $x + \ln |x| + C$  
   (b) $x + \ln |x + 1| + C$  
   (c) $\ln(x^2 + 1) + \tan^{-1} x + C$  
   (d) $\frac{x^5}{5} + C$
2. (a) $-\cos x + C$  
   (b) $\tan x + C$  
   (c) $-\cot x + C$  
   (d) $\ln(1 + \sin x) + C$
3. (a) $\frac{2}{3}(x - 1)^{3/2} + C$  
   (b) $\frac{1}{2}e^{2x+1} + C$  
   (c) $\frac{1}{2}\sin^2 x + C$  
   (d) $\frac{1}{4}\tanh x + C$

---

## 7.2 INTEGRATION BY PARTS

In this section we will discuss an integration technique that is essentially an antiderivative formulation of the formula for differentiating a product of two functions.

### THE PRODUCT RULE AND INTEGRATION BY PARTS

Our primary goal in this section is to develop a general method for attacking integrals of the form
$$\int f(x)g(x) \, dx$$

As a first step, let $G(x)$ be any antiderivative of $g(x)$. In this case $G'(x) = g(x)$, so the product rule for differentiating $f(x)G(x)$ can be expressed as
$$\frac{d}{dx}[f(x)G(x)] = f(x)G'(x) + f'(x)G(x) = f(x)g(x) + f'(x)G(x) \tag{1}$$

This implies that $f(x)G(x)$ is an antiderivative of the function on the right side of (1), so we can express (1) in integral form as
$$\int [f(x)g(x) + f'(x)G(x)] \, dx = f(x)G(x)$$
or, equivalently, as
$$\int f(x)g(x) \, dx = f(x)G(x) - \int f'(x)G(x) \, dx \tag{2}$$

This formula allows us to integrate $f(x)g(x)$ by integrating $f'(x)G(x)$ instead, and in many cases the net effect is to replace a difficult integration with an easier one. The application of this formula is called **integration by parts**.

In practice, we usually rewrite (2) by letting
$$u = f(x), \quad du = f'(x) \, dx$$
$$v = G(x), \quad dv = G'(x) \, dx = g(x) \, dx$$

This yields the following alternative form for (2):
$$\int u \, dv = uv - \int v \, du \tag{3}$$

#### Example 1
Use integration by parts to evaluate $\int x \cos x \, dx$.

> *Note that in Example 1 we omitted the constant of integration in calculating $v$ from $dv$. Had we included a constant of integration, it would have eventually dropped out. This is always the case in integration by parts [Exercise 68(b)], so it is common to omit the constant at this stage of the computation. However, there are certain cases in which making a clever choice of a constant of integration to include with $v$ can simplify the computation of $\int v \, du$ (Exercises 69–71).*

**Solution.** We will apply Formula (3). The first step is to make a choice for $u$ and $dv$ to put the given integral in the form $\int u \, dv$. We will let
$$u = x \quad\text{and}\quad dv = \cos x \, dx$$
(Other possibilities will be considered later.) The second step is to compute $du$ from $u$ and $v$ from $dv$. This yields
$$du = dx \quad\text{and}\quad v = \int dv = \int \cos x \, dx = \sin x$$
The third step is to apply Formula (3). This yields
$$\int \underbrace{x}_{u} \underbrace{\cos x \, dx}_{dv} = \underbrace{x}_{u} \underbrace{\sin x}_{v} - \int \underbrace{\sin x}_{v} \underbrace{dx}_{du} = x \sin x - (-\cos x) + C = x \sin x + \cos x + C$$

---

### GUIDELINES FOR INTEGRATION BY PARTS

The main goal in integration by parts is to choose $u$ and $dv$ to obtain a new integral that is easier to evaluate than the original. In general, there are no hard and fast rules for doing this; it is mainly a matter of experience that comes from lots of practice. A strategy that often works is to choose $u$ and $dv$ so that $u$ becomes “simpler” when differentiated, while leaving a $dv$ that can be readily integrated to obtain $v$. Thus, for the integral $\int x \cos x \, dx$ in Example 1, both goals were achieved by letting $u = x$ and $dv = \cos x \, dx$. In contrast, $u = \cos x$ would not have been a good first choice in that example, since $du/dx = -\sin x$ is no simpler than $u$. Indeed, had we chosen
$$u = \cos x, \quad dv = x \, dx$$
$$du = -\sin x \, dx, \quad v = \int x \, dx = \frac{x^2}{2}$$
then we would have obtained
$$\int x \cos x \, dx = \frac{x^2}{2}\cos x - \int \frac{x^2}{2}(-\sin x) \, dx = \frac{x^2}{2}\cos x + \frac{1}{2}\int x^2 \sin x \, dx$$
For this choice of $u$ and $dv$, the new integral is actually more complicated than the original.

There is another useful strategy for choosing $u$ and $dv$ that can be applied when the integrand is a product of two functions from different categories in the list:
$$\textbf{L}\text{ogarithmic}, \quad \textbf{I}\text{nverse trigonometric}, \quad \textbf{A}\text{lgebraic}, \quad \textbf{T}\text{rigonometric}, \quad \textbf{E}\text{xponential}$$

> *The LIATE method is discussed in the article “A Technique for Integration by Parts,” American Mathematical Monthly, Vol. 90, 1983, pp. 210–211, by Herbert Kasube.*

In this case you will often be successful if you take $u$ to be the function whose category occurs earlier in the list and take $dv$ to be the rest of the integrand. The acronym **LIATE** will help you to remember the order. The method does not work all the time, but it works often enough to be useful.

Note, for example, that the integrand in Example 1 consists of the product of the algebraic function $x$ and the trigonometric function $\cos x$. Thus, the LIATE method suggests that we should let $u = x$ and $dv = \cos x \, dx$, which proved to be a successful choice.

#### Example 2
Evaluate $\int x e^x \, dx$.

**Solution.** In this case the integrand is the product of the algebraic function $x$ with the exponential function $e^x$. According to LIATE we should let
$$u = x \quad\text{and}\quad dv = e^x \, dx$$
so that
$$du = dx \quad\text{and}\quad v = \int e^x \, dx = e^x$$
Thus, from (3)
$$\int x e^x \, dx = \int u \, dv = uv - \int v \, du = x e^x - \int e^x \, dx = x e^x - e^x + C$$

#### Example 3
Evaluate $\int \ln x \, dx$.

**Solution.** One choice is to let $u = 1$ and $dv = \ln x \, dx$. But with this choice finding $v$ is equivalent to evaluating $\int \ln x \, dx$ and we have gained nothing. Therefore, the only reasonable choice is to let
$$u = \ln x, \quad dv = dx$$
$$du = \frac{1}{x} \, dx, \quad v = \int dx = x$$
With this choice it follows from (3) that
$$\int \ln x \, dx = \int u \, dv = uv - \int v \, du = x \ln x - \int dx = x \ln x - x + C$$

---

### REPEATED INTEGRATION BY PARTS

It is sometimes necessary to use integration by parts more than once in the same problem.

#### Example 4
Evaluate $\int x^2 e^{-x} \, dx$.

**Solution.** Let
$$u = x^2, \quad dv = e^{-x} \, dx, \quad du = 2x \, dx, \quad v = \int e^{-x} \, dx = -e^{-x}$$
so that from (3)
$$\int x^2 e^{-x} \, dx = \int u \, dv = uv - \int v \, du = x^2(-e^{-x}) - \int -e^{-x}(2x) \, dx = -x^2 e^{-x} + 2\int x e^{-x} \, dx \tag{4}$$

The last integral is similar to the original except that we have replaced $x^2$ by $x$. Another integration by parts applied to $\int x e^{-x} \, dx$ will complete the problem. We let
$$u = x, \quad dv = e^{-x} \, dx, \quad du = dx, \quad v = \int e^{-x} \, dx = -e^{-x}$$
so that
$$\int x e^{-x} \, dx = x(-e^{-x}) - \int -e^{-x} \, dx = -x e^{-x} + \int e^{-x} \, dx = -x e^{-x} - e^{-x} + C$$
Finally, substituting this into the last line of (4) yields
$$\int x^2 e^{-x} \, dx = -x^2 e^{-x} + 2\int x e^{-x} \, dx = -x^2 e^{-x} + 2(-x e^{-x} - e^{-x}) + C = -(x^2 + 2x + 2)e^{-x} + C$$

The LIATE method suggests that integrals of the form
$$\int e^{ax}\sin bx \, dx \quad\text{and}\quad \int e^{ax}\cos bx \, dx$$
can be evaluated by letting $u = \sin bx$ or $u = \cos bx$ and $dv = e^{ax} \, dx$. However, this will require a technique that deserves special attention.

#### Example 5
Evaluate $\int e^x \cos x \, dx$.

**Solution.** Let
$$u = \cos x, \quad dv = e^x \, dx, \quad du = -\sin x \, dx, \quad v = \int e^x \, dx = e^x$$
Thus,
$$\int e^x \cos x \, dx = \int u \, dv = uv - \int v \, du = e^x \cos x + \int e^x \sin x \, dx \tag{5}$$
Since the integral $\int e^x \sin x \, dx$ is similar in form to the original integral $\int e^x \cos x \, dx$, it seems that nothing has been accomplished. However, let us integrate this new integral by parts. We let
$$u = \sin x, \quad dv = e^x \, dx, \quad du = \cos x \, dx, \quad v = \int e^x \, dx = e^x$$
Thus,
$$\int e^x \sin x \, dx = \int u \, dv = uv - \int v \, du = e^x \sin x - \int e^x \cos x \, dx$$
Together with Equation (5) this yields
$$\int e^x \cos x \, dx = e^x \cos x + e^x \sin x - \int e^x \cos x \, dx \tag{6}$$
which is an equation we can solve for the unknown integral. We obtain
$$2\int e^x \cos x \, dx = e^x \cos x + e^x \sin x$$
and hence
$$\int e^x \cos x \, dx = \frac{1}{2}e^x \cos x + \frac{1}{2}e^x \sin x + C$$

---

### A TABULAR METHOD FOR REPEATED INTEGRATION BY PARTS

Integrals of the form
$$\int p(x)f(x) \, dx$$
where $p(x)$ is a polynomial, can sometimes be evaluated using repeated integration by parts in which $u$ is taken to be $p(x)$ or one of its derivatives at each stage. Since $du$ is computed by differentiating $u$, the repeated differentiation of $p(x)$ will eventually produce 0, at which point you may be left with a simplified integration problem. A convenient method for organizing the computations into two columns is called **tabular integration by parts**.

> *More information on tabular integration by parts can be found in the articles “Tabular Integration by Parts,” College Mathematics Journal, Vol. 21, 1990, pp. 307–311, by David Horowitz and “More on Tabular Integration by Parts,” College Mathematics Journal, Vol. 22, 1991, pp. 407–410, by Leonard Gillman.*

> **Tabular Integration by Parts**  
> **Step 1.** Differentiate $p(x)$ repeatedly until you obtain 0, and list the results in the first column.  
> **Step 2.** Integrate $f(x)$ repeatedly and list the results in the second column.  
> **Step 3.** Draw an arrow from each entry in the first column to the entry that is one row down in the second column.  
> **Step 4.** Label the arrows with alternating $+$ and $-$ signs, starting with a $+$.  
> **Step 5.** For each arrow, form the product of the expressions at its tip and tail and then multiply that product by $+1$ or $-1$ in accordance with the sign on the arrow. Add the results to obtain the value of the integral.

This process is illustrated in Figure 7.2.1 for the integral $\int (x^2 - x)\cos x \, dx$:

| Repeated Differentiation | Sign | Repeated Integration |
| :---: | :---: | :---: |
| $x^2 - x$ | $+$ | $\cos x$ |
| $2x - 1$ | $-$ | $\sin x$ |
| $2$ | $+$ | $-\cos x$ |
| $0$ | | $-\sin x$ |

$$\int (x^2 - x)\cos x \, dx = (x^2 - x)\sin x + (2x - 1)\cos x - 2\sin x + C = (x^2 - x - 2)\sin x + (2x - 1)\cos x + C$$

#### Example 6
In Example 9 of Section 4.3 we evaluated $\int x^2 \sqrt{x - 1} \, dx$ using $u$-substitution. Evaluate this integral using tabular integration by parts.

**Solution.**

| Repeated Differentiation | Sign | Repeated Integration |
| :---: | :---: | :---: |
| $x^2$ | $+$ | $(x - 1)^{1/2}$ |
| $2x$ | $-$ | $\frac{2}{3}(x - 1)^{3/2}$ |
| $2$ | $+$ | $\frac{4}{15}(x - 1)^{5/2}$ |
| $0$ | | $\frac{8}{105}(x - 1)^{7/2}$ |

Thus, it follows that
$$\int x^2 \sqrt{x - 1} \, dx = \frac{2}{3}x^2(x - 1)^{3/2} - \frac{8}{15}x(x - 1)^{5/2} + \frac{16}{105}(x - 1)^{7/2} + C$$

> *The result obtained in Example 6 looks quite different from that obtained in Example 9 of Section 4.3. Show that the two answers are equivalent.*

---

### INTEGRATION BY PARTS FOR DEFINITE INTEGRALS

For definite integrals the formula corresponding to (3) is
$$\int_a^b u \, dv = \left[uv\right]_a^b - \int_a^b v \, du \tag{7}$$

> **REMARK** It is important to keep in mind that the variables $u$ and $v$ in this formula are functions of $x$ and that the limits of integration in (7) are limits on the variable $x$. Sometimes it is helpful to emphasize this by writing (7) as
> $$\int_{x=a}^b u \, dv = \left[uv\right]_{x=a}^b - \int_{x=a}^b v \, du \tag{8}$$

The next example illustrates how integration by parts can be used to integrate the inverse trigonometric functions.

#### Example 7
Evaluate $\int_0^1 \tan^{-1} x \, dx$.

**Solution.** Let
$$u = \tan^{-1} x, \quad dv = dx, \quad du = \frac{1}{1 + x^2} \, dx, \quad v = x$$
Thus,
$$\int_0^1 \tan^{-1} x \, dx = \int_0^1 u \, dv = \left[uv\right]_0^1 - \int_0^1 v \, du = \left[x \tan^{-1} x\right]_0^1 - \int_0^1 \frac{x}{1 + x^2} \, dx$$
*(The limits of integration refer to $x$; that is, $x = 0$ and $x = 1$.)*

But
$$\int_0^1 \frac{x}{1 + x^2} \, dx = \frac{1}{2}\int_0^1 \frac{2x}{1 + x^2} \, dx = \frac{1}{2}\left[\ln(1 + x^2)\right]_0^1 = \frac{1}{2}\ln 2$$
so
$$\int_0^1 \tan^{-1} x \, dx = \left[x \tan^{-1} x\right]_0^1 - \frac{1}{2}\ln 2 = \left(\frac{\pi}{4} - 0\right) - \frac{1}{2}\ln 2 = \frac{\pi}{4} - \ln\sqrt{2}$$

---

### REDUCTION FORMULAS

Integration by parts can be used to derive **reduction formulas** for integrals. These are formulas that express an integral involving a power of a function in terms of an integral that involves a lower power of that function. For example, if $n$ is a positive integer and $n \ge 2$, then integration by parts can be used to obtain the reduction formulas
$$\int \sin^n x \, dx = -\frac{1}{n}\sin^{n-1} x \cos x + \frac{n - 1}{n}\int \sin^{n-2} x \, dx \tag{9}$$
$$\int \cos^n x \, dx = \frac{1}{n}\cos^{n-1} x \sin x + \frac{n - 1}{n}\int \cos^{n-2} x \, dx \tag{10}$$

To illustrate how such formulas can be obtained, let us derive (10). We begin by writing $\cos^n x$ as $\cos^{n-1} x \cdot \cos x$ and letting
$$u = \cos^{n-1} x, \quad dv = \cos x \, dx$$
$$du = (n - 1)\cos^{n-2} x(-\sin x) \, dx = -(n - 1)\cos^{n-2} x \sin x \, dx, \quad v = \sin x$$
so that
$$\begin{aligned}
\int \cos^n x \, dx &= \int \cos^{n-1} x \cos x \, dx = \int u \, dv = uv - \int v \, du \\
&= \cos^{n-1} x \sin x + (n - 1)\int \sin^2 x \cos^{n-2} x \, dx \\
&= \cos^{n-1} x \sin x + (n - 1)\int (1 - \cos^2 x)\cos^{n-2} x \, dx \\
&= \cos^{n-1} x \sin x + (n - 1)\int \cos^{n-2} x \, dx - (n - 1)\int \cos^n x \, dx
\end{aligned}$$
Moving the last term on the right to the left side yields
$$n \int \cos^n x \, dx = \cos^{n-1} x \sin x + (n - 1)\int \cos^{n-2} x \, dx$$
from which (10) follows. The derivation of reduction formula (9) is similar (Exercise 63).

Reduction formulas (9) and (10) reduce the exponent of sine (or cosine) by 2. Thus, if the formulas are applied repeatedly, the exponent can eventually be reduced to 0 if $n$ is even or 1 if $n$ is odd, at which point the integration can be completed. We will discuss this method in more detail in the next section, but for now, here is an example that illustrates how reduction formulas work.

#### Example 8
Evaluate $\int \cos^4 x \, dx$.

**Solution.** From (10) with $n = 4$
$$\int \cos^4 x \, dx = \frac{1}{4}\cos^3 x \sin x + \frac{3}{4}\int \cos^2 x \, dx$$
Now apply (10) with $n = 2$:
$$= \frac{1}{4}\cos^3 x \sin x + \frac{3}{4}\left(\frac{1}{2}\cos x \sin x + \frac{1}{2}\int dx\right) = \frac{1}{4}\cos^3 x \sin x + \frac{3}{8}\cos x \sin x + \frac{3}{8}x + C$$

---

### QUICK CHECK EXERCISES 7.2
*(See page 500 for answers.)*

1. (a) If $G'(x) = g(x)$, then $\int f(x)g(x) \, dx = f(x)G(x) - \underline{\hspace{2cm}}$.  
   (b) If $u = f(x)$ and $v = G(x)$, then the formula in part (a) can be written in the form $\int u \, dv = \underline{\hspace{2cm}}$.
2. Find an appropriate choice of $u$ and $dv$ for integration by parts of each integral. Do not evaluate the integral.  
   (a) $\int x \ln x \, dx; \quad u = \underline{\hspace{1.5cm}}, \; dv = \underline{\hspace{1.5cm}}$  
   (b) $\int (x - 2)\sin x \, dx; \quad u = \underline{\hspace{1.5cm}}, \; dv = \underline{\hspace{1.5cm}}$  
   (c) $\int \sin^{-1} x \, dx; \quad u = \underline{\hspace{1.5cm}}, \; dv = \underline{\hspace{1.5cm}}$  
   (d) $\int \frac{x}{\sqrt{x - 1}} \, dx; \quad u = \underline{\hspace{1.5cm}}, \; dv = \underline{\hspace{1.5cm}}$
3. Use integration by parts to evaluate the integral.  
   (a) $\int x e^{2x} \, dx$  
   (b) $\int \ln(x - 1) \, dx$  
   (c) $\int_0^{\pi/6} x \sin 3x \, dx$
4. Use a reduction formula to evaluate $\int \sin^3 x \, dx$.

---

### EXERCISE SET 7.2

**1–38 Evaluate the integral.**

1. $\int x e^{-2x} \, dx$
2. $\int x e^{3x} \, dx$
3. $\int x^2 e^x \, dx$
4. $\int x^2 e^{-2x} \, dx$
5. $\int x \sin 3x \, dx$
6. $\int x \cos 2x \, dx$
7. $\int x^2 \cos x \, dx$
8. $\int x^2 \sin x \, dx$
9. $\int x \ln x \, dx$
10. $\int \sqrt{x}\ln x \, dx$
11. $\int (\ln x)^2 \, dx$
12. $\int \frac{\ln x}{\sqrt{x}} \, dx$
13. $\int \ln(3x - 2) \, dx$
14. $\int \ln(x^2 + 4) \, dx$
15. $\int \sin^{-1} x \, dx$
16. $\int \cos^{-1}(2x) \, dx$
17. $\int \tan^{-1}(3x) \, dx$
18. $\int x \tan^{-1} x \, dx$
19. $\int e^x \sin x \, dx$
20. $\int e^{3x}\cos 2x \, dx$
21. $\int \sin(\ln x) \, dx$
22. $\int \cos(\ln x) \, dx$
23. $\int x \sec^2 x \, dx$
24. $\int x \tan^2 x \, dx$
25. $\int x^3 e^{x^2} \, dx$
26. $\int \frac{x e^x}{(x + 1)^2} \, dx$
27. $\int_0^2 x e^{2x} \, dx$
28. $\int_0^1 x e^{-5x} \, dx$
29. $\int_1^e x^2 \ln x \, dx$
30. $\int_{\sqrt{e}}^e \frac{\ln x}{x^2} \, dx$
31. $\int_{-1}^1 \ln(x + 2) \, dx$
32. $\int_0^{\sqrt{3}/2} \sin^{-1} x \, dx$
33. $\int_2^4 \sec^{-1}\sqrt{\theta} \, d\theta$
34. $\int_1^2 x \sec^{-1} x \, dx$
35. $\int_0^\pi x \sin 2x \, dx$
36. $\int_0^\pi (x + x \cos x) \, dx$
37. $\int_1^3 \sqrt{x}\tan^{-1}\sqrt{x} \, dx$
38. $\int_0^2 \ln(x^2 + 1) \, dx$

**39–42 True–False Determine whether the statement is true or false. Explain your answer.**

39. The main goal in integration by parts is to choose $u$ and $dv$ to obtain a new integral that is easier to evaluate than the original.
40. Applying the LIATE strategy to evaluate $\int x^3 \ln x \, dx$, we should choose $u = x^3$ and $dv = \ln x \, dx$.
41. To evaluate $\int \ln e^x \, dx$ using integration by parts, choose $dv = e^x \, dx$.
42. Tabular integration by parts is useful for integrals of the form $\int p(x)f(x) \, dx$, where $p(x)$ is a polynomial and $f(x)$ can be repeatedly integrated.

**43–44 Evaluate the integral by making a $u$-substitution and then integrating by parts.**

43. $\int e^{\sqrt{x}} \, dx$
44. $\int \cos\sqrt{x} \, dx$

45. Prove that tabular integration by parts gives the correct answer for
    $$\int p(x)f(x) \, dx$$
    where $p(x)$ is any quadratic polynomial and $f(x)$ is any function that can be repeatedly integrated.
46. The computations of any integral evaluated by repeated integration by parts can be organized using tabular integration by parts. Use this organization to evaluate $\int e^x \cos x \, dx$ in two ways: first by repeated differentiation of $\cos x$ (compare Example 5), and then by repeated differentiation of $e^x$.

**47–52 Evaluate the integral using tabular integration by parts.**

47. $\int (3x^2 - x + 2)e^{-x} \, dx$
48. $\int (x^2 + x + 1)\sin x \, dx$
49. $\int 4x^4 \sin 2x \, dx$
50. $\int x^3 \sqrt{2x + 1} \, dx$
51. $\int e^{ax}\sin bx \, dx$
52. $\int e^{-3\theta}\sin 5\theta \, d\theta$

53. Consider the integral $\int \sin x \cos x \, dx$.  
    (a) Evaluate the integral two ways: first using integration by parts, and then using the substitution $u = \sin x$.  
    (b) Show that the results of part (a) are equivalent.  
    (c) Which of the two methods do you prefer? Discuss the reasons for your preference.

54. Evaluate the integral
    $$\int_0^1 \frac{x^3}{\sqrt{x^2 + 1}} \, dx$$
    using (a) integration by parts (b) the substitution $u = \sqrt{x^2 + 1}$.

55. (a) Find the area of the region enclosed by $y = \ln x$, the line $x = e$, and the $x$-axis.  
    (b) Find the volume of the solid generated when the region in part (a) is revolved about the $x$-axis.

56. Find the area of the region between $y = x \sin x$ and $y = x$ for $0 \le x \le \pi/2$.

57. Find the volume of the solid generated when the region between $y = \sin x$ and $y = 0$ for $0 \le x \le \pi$ is revolved about the $y$-axis.

58. Find the volume of the solid generated when the region enclosed between $y = \cos x$ and $y = 0$ for $0 \le x \le \pi/2$ is revolved about the $y$-axis.

59. A particle moving along the $x$-axis has velocity function $v(t) = t^3 \sin t$. How far does the particle travel from time $t = 0$ to $t = \pi$?

60. The study of sawtooth waves in electrical engineering leads to integrals of the form
    $$\int_{-\pi/\omega}^{\pi/\omega} t \sin(k\omega t) \, dt$$
    where $k$ is an integer and $\omega$ is a nonzero constant. Evaluate the integral.

61. Use reduction formula (9) to evaluate: (a) $\int \sin^4 x \, dx$ (b) $\int_0^{\pi/2}\sin^5 x \, dx$.

62. Use reduction formula (10) to evaluate: (a) $\int \cos^5 x \, dx$ (b) $\int_0^{\pi/2}\cos^6 x \, dx$.

63. Derive reduction formula (9).

64. In each part, use integration by parts or other methods to derive the reduction formula.  
    (a) $\int \sec^n x \, dx = \frac{\sec^{n-2} x \tan x}{n - 1} + \frac{n - 2}{n - 1}\int \sec^{n-2} x \, dx$  
    (b) $\int \tan^n x \, dx = \frac{\tan^{n-1} x}{n - 1} - \int \tan^{n-2} x \, dx$  
    (c) $\int x^n e^x \, dx = x^n e^x - n \int x^{n-1}e^x \, dx$

**65–66 Use the reduction formulas in Exercise 64 to evaluate the integrals.**

65. (a) $\int \tan^4 x \, dx$ (b) $\int \sec^4 x \, dx$ (c) $\int x^3 e^x \, dx$
66. (a) $\int x^2 e^{3x} \, dx$ (b) $\int_0^1 x e^{-\sqrt{x}} \, dx$ [*Hint:* First make a substitution.]

67. Let $f$ be a function whose second derivative is continuous on $[-1, 1]$. Show that
    $$\int_{-1}^1 x f''(x) \, dx = f'(1) + f'(-1) - f(1) + f(-1)$$

#### FOCUS ON CONCEPTS

68. (a) In the integral $\int x \cos x \, dx$, let $u = x, dv = \cos x \, dx, du = dx, v = \sin x + C_1$. Show that the constant $C_1$ cancels out, thus giving the same solution obtained by omitting $C_1$.  
    (b) Show that in general
    $$uv - \int v \, du = u(v + C_1) - \int (v + C_1) \, du$$
    thereby justifying the omission of the constant of integration when calculating $v$ in integration by parts.

69. Evaluate $\int \ln(x + 1) \, dx$ using integration by parts. Simplify the computation of $\int v \, du$ by introducing a constant of integration $C_1 = 1$ when going from $dv$ to $v$.

70. Evaluate $\int \ln(3x - 2) \, dx$ using integration by parts. Simplify the computation of $\int v \, du$ by introducing a constant of integration $C_1 = -2/3$ when going from $dv$ to $v$. Compare your solution with your answer to Exercise 13.

71. Evaluate $\int x \tan^{-1} x \, dx$ using integration by parts. Simplify the computation of $\int v \, du$ by introducing a constant of integration $C_1 = 1/2$ when going from $dv$ to $v$.

72. What equation results if integration by parts is applied to the integral
    $$\int \frac{1}{x \ln x} \, dx$$
    with the choices $u = \frac{1}{\ln x}$ and $dv = \frac{1}{x} \, dx$? In what sense is this equation true? In what sense is it false?

73. **Writing** Explain how the product rule for derivatives and the technique of integration by parts are related.

74. **Writing** For what sort of problems are the integration techniques of substitution and integration by parts “competing” techniques? Describe situations, with examples, where each of these techniques would be preferred over the other.

---

### QUICK CHECK ANSWERS 7.2

1. (a) $\int f'(x)G(x) \, dx$  
   (b) $uv - \int v \, du$
2. (a) $\ln x; \quad x \, dx$  
   (b) $x - 2; \quad \sin x \, dx$  
   (c) $\sin^{-1} x; \quad dx$  
   (d) $x; \quad \frac{1}{\sqrt{x - 1}} \, dx$
3. (a) $\left(\frac{x}{2} - \frac{1}{4}\right)e^{2x} + C$  
   (b) $(x - 1)\ln(x - 1) - x + C$  
   (c) $\frac{1}{9}$
---

## 7.3 INTEGRATING TRIGONOMETRIC FUNCTIONS

In the last section we derived reduction formulas for integrating positive integer powers of sine, cosine, tangent, and secant. In this section we will show how to work with those reduction formulas, and we will discuss methods for integrating other kinds of integrals that involve trigonometric functions.

### INTEGRATING POWERS OF SINE AND COSINE

We begin by recalling two reduction formulas from the preceding section.
$$\int \sin^n x \, dx = -\frac{1}{n}\sin^{n-1} x \cos x + \frac{n - 1}{n}\int \sin^{n-2} x \, dx \tag{1}$$
$$\int \cos^n x \, dx = \frac{1}{n}\cos^{n-1} x \sin x + \frac{n - 1}{n}\int \cos^{n-2} x \, dx \tag{2}$$

In the case where $n = 2$, these formulas yield
$$\int \sin^2 x \, dx = -\frac{1}{2}\sin x \cos x + \frac{1}{2}\int dx = \frac{1}{2}x - \frac{1}{2}\sin x \cos x + C \tag{3}$$
$$\int \cos^2 x \, dx = \frac{1}{2}\cos x \sin x + \frac{1}{2}\int dx = \frac{1}{2}x + \frac{1}{2}\sin x \cos x + C \tag{4}$$

Alternative forms of these integration formulas can be derived from the trigonometric identities
$$\sin^2 x = \frac{1}{2}(1 - \cos 2x) \quad\text{and}\quad \cos^2 x = \frac{1}{2}(1 + \cos 2x) \tag{5–6}$$
which follow from the double-angle formulas
$$\cos 2x = 1 - 2\sin^2 x \quad\text{and}\quad \cos 2x = 2\cos^2 x - 1$$
These identities yield
$$\int \sin^2 x \, dx = \frac{1}{2}\int (1 - \cos 2x) \, dx = \frac{1}{2}x - \frac{1}{4}\sin 2x + C \tag{7}$$
$$\int \cos^2 x \, dx = \frac{1}{2}\int (1 + \cos 2x) \, dx = \frac{1}{2}x + \frac{1}{4}\sin 2x + C \tag{8}$$

Observe that the antiderivatives in Formulas (3) and (4) involve both sines and cosines, whereas those in (7) and (8) involve sines alone. However, the apparent discrepancy is easy to resolve by using the identity
$$\sin 2x = 2\sin x \cos x$$
to rewrite (7) and (8) in forms (3) and (4), or conversely.

In the case where $n = 3$, the reduction formulas for integrating $\sin^3 x$ and $\cos^3 x$ yield
$$\int \sin^3 x \, dx = -\frac{1}{3}\sin^2 x \cos x + \frac{2}{3}\int \sin x \, dx = -\frac{1}{3}\sin^2 x \cos x - \frac{2}{3}\cos x + C \tag{9}$$
$$\int \cos^3 x \, dx = \frac{1}{3}\cos^2 x \sin x + \frac{2}{3}\int \cos x \, dx = \frac{1}{3}\cos^2 x \sin x + \frac{2}{3}\sin x + C \tag{10}$$

If desired, Formula (9) can be expressed in terms of cosines alone by using the identity $\sin^2 x = 1 - \cos^2 x$, and Formula (10) can be expressed in terms of sines alone by using the identity $\cos^2 x = 1 - \sin^2 x$. We leave it for you to do this and confirm that
$$\int \sin^3 x \, dx = \frac{1}{3}\cos^3 x - \cos x + C \tag{11}$$
$$\int \cos^3 x \, dx = \sin x - \frac{1}{3}\sin^3 x + C \tag{12}$$

> **TECHNOLOGY MASTERY**  
> The Maple CAS produces forms (11) and (12) when asked to integrate $\sin^3 x$ and $\cos^3 x$, but Mathematica produces
> $$\int \sin^3 x \, dx = -\frac{3}{4}\cos x + \frac{1}{12}\cos 3x + C$$
> $$\int \cos^3 x \, dx = \frac{3}{4}\sin x + \frac{1}{12}\sin 3x + C$$
> Use trigonometric identities to reconcile the results of the two programs.

We leave it as an exercise to obtain the following formulas by first applying the reduction formulas, and then using appropriate trigonometric identities.
$$\int \sin^4 x \, dx = \frac{3}{8}x - \frac{1}{4}\sin 2x + \frac{1}{32}\sin 4x + C \tag{13}$$
$$\int \cos^4 x \, dx = \frac{3}{8}x + \frac{1}{4}\sin 2x + \frac{1}{32}\sin 4x + C \tag{14}$$

#### Example 1
Find the volume $V$ of the solid that is obtained when the region under the curve $y = \sin^2 x$ over the interval $[0, \pi]$ is revolved about the $x$-axis (Figure 7.3.1).

**Solution.** Using the method of disks, Formula (5) of Section 5.2, and Formula (13) above yields
$$V = \int_0^\pi \pi \sin^4 x \, dx = \pi \left[\frac{3}{8}x - \frac{1}{4}\sin 2x + \frac{1}{32}\sin 4x\right]_0^\pi = \frac{3}{8}\pi^2$$

---

### INTEGRATING PRODUCTS OF SINES AND COSINES

If $m$ and $n$ are positive integers, then the integral
$$\int \sin^m x \cos^n x \, dx$$
can be evaluated by one of the three procedures stated in Table 7.3.1, depending on whether $m$ and $n$ are odd or even.

#### Table 7.3.1: Integrating Products of Sines and Cosines
| Case | Procedure | Relevant Identities |
| :--- | :--- | :--- |
| $n$ odd | • Split off a factor of $\cos x$.<br>• Apply the relevant identity.<br>• Make the substitution $u = \sin x$. | $\cos^2 x = 1 - \sin^2 x$ |
| $m$ odd | • Split off a factor of $\sin x$.<br>• Apply the relevant identity.<br>• Make the substitution $u = \cos x$. | $\sin^2 x = 1 - \cos^2 x$ |
| $m$ even<br>$n$ even | • Use the relevant identities to reduce the powers on $\sin x$ and $\cos x$. | $\sin^2 x = \frac{1}{2}(1 - \cos 2x)$<br>$\cos^2 x = \frac{1}{2}(1 + \cos 2x)$ |

#### Example 2
Evaluate: (a) $\int \sin^4 x \cos^5 x \, dx$ (b) $\int \sin^4 x \cos^4 x \, dx$

**Solution (a).** Since $n = 5$ is odd, we will follow the first procedure in Table 7.3.1:
$$\begin{aligned}
\int \sin^4 x \cos^5 x \, dx &= \int \sin^4 x \cos^4 x \cos x \, dx \\
&= \int \sin^4 x (1 - \sin^2 x)^2 \cos x \, dx \\
&= \int u^4(1 - u^2)^2 \, du \\
&= \int (u^4 - 2u^6 + u^8) \, du \\
&= \frac{1}{5}u^5 - \frac{2}{7}u^7 + \frac{1}{9}u^9 + C \\
&= \frac{1}{5}\sin^5 x - \frac{2}{7}\sin^7 x + \frac{1}{9}\sin^9 x + C
\end{aligned}$$

**Solution (b).** Since $m = n = 4$, both exponents are even, so we will follow the third procedure in Table 7.3.1:
$$\begin{aligned}
\int \sin^4 x \cos^4 x \, dx &= \int (\sin^2 x)^2 (\cos^2 x)^2 \, dx \\
&= \int \left(\frac{1}{2}[1 - \cos 2x]\right)^2 \left(\frac{1}{2}[1 + \cos 2x]\right)^2 \, dx \\
&= \frac{1}{16}\int (1 - \cos^2 2x)^2 \, dx \\
&= \frac{1}{16}\int \sin^4 2x \, dx
\end{aligned}$$

> *Note that this can be obtained more directly from the original integral using the identity $\sin x \cos x = \frac{1}{2}\sin 2x$.*

Letting $u = 2x, du = 2 \, dx$ or $dx = \frac{1}{2} \, du$:
$$= \frac{1}{32}\int \sin^4 u \, du = \frac{1}{32}\left[\frac{3}{8}u - \frac{1}{4}\sin 2u + \frac{1}{32}\sin 4u\right] + C \quad \text{Formula (13)}$$
$$= \frac{3}{128}x - \frac{1}{128}\sin 4x + \frac{1}{1024}\sin 8x + C$$

Integrals of the form
$$\int \sin mx \cos nx \, dx, \quad \int \sin mx \sin nx \, dx, \quad \int \cos mx \cos nx \, dx \tag{15}$$
can be found by using the trigonometric identities
$$\sin\alpha \cos\beta = \frac{1}{2}[\sin(\alpha - \beta) + \sin(\alpha + \beta)] \tag{16}$$
$$\sin\alpha \sin\beta = \frac{1}{2}[\cos(\alpha - \beta) - \cos(\alpha + \beta)] \tag{17}$$
$$\cos\alpha \cos\beta = \frac{1}{2}[\cos(\alpha - \beta) + \cos(\alpha + \beta)] \tag{18}$$
to express the integrand as a sum or difference of sines and cosines.

#### Example 3
Evaluate $\int \sin 7x \cos 3x \, dx$.

**Solution.** Using (16) yields
$$\int \sin 7x \cos 3x \, dx = \frac{1}{2}\int (\sin 4x + \sin 10x) \, dx = -\frac{1}{8}\cos 4x - \frac{1}{20}\cos 10x + C$$

---

### INTEGRATING POWERS OF TANGENT AND SECANT

The procedures for integrating powers of tangent and secant closely parallel those for sine and cosine. The idea is to use the following reduction formulas (which were derived in Exercise 64 of Section 7.2) to reduce the exponent in the integrand until the resulting integral can be evaluated:
$$\int \tan^n x \, dx = \frac{\tan^{n-1} x}{n - 1} - \int \tan^{n-2} x \, dx \tag{19}$$
$$\int \sec^n x \, dx = \frac{\sec^{n-2} x \tan x}{n - 1} + \frac{n - 2}{n - 1}\int \sec^{n-2} x \, dx \tag{20}$$

In the case where $n$ is odd, the exponent can be reduced to 1, leaving us with the problem of integrating $\tan x$ or $\sec x$. These integrals are given by
$$\int \tan x \, dx = \ln |\sec x| + C \tag{21}$$
$$\int \sec x \, dx = \ln |\sec x + \tan x| + C \tag{22}$$

Formula (21) can be obtained by writing
$$\int \tan x \, dx = \int \frac{\sin x}{\cos x} \, dx = -\ln |\cos x| + C \quad [u = \cos x, du = -\sin x \, dx] = \ln |\sec x| + C$$

To obtain Formula (22) we write
$$\begin{aligned}
\int \sec x \, dx &= \int \sec x \left(\frac{\sec x + \tan x}{\sec x + \tan x}\right) \, dx = \int \frac{\sec^2 x + \sec x \tan x}{\sec x + \tan x} \, dx \\
&= \ln |\sec x + \tan x| + C \quad [u = \sec x + \tan x, du = (\sec^2 x + \sec x \tan x) \, dx]
\end{aligned}$$

The following basic integrals occur frequently and are worth noting:
$$\int \tan^2 x \, dx = \tan x - x + C \tag{23}$$
$$\int \sec^2 x \, dx = \tan x + C \tag{24}$$

Formula (24) is already known to us, since the derivative of $\tan x$ is $\sec^2 x$. Formula (23) can be obtained by applying reduction formula (19) with $n = 2$ (verify) or, alternatively, by using the identity $1 + \tan^2 x = \sec^2 x$ to write
$$\int \tan^2 x \, dx = \int (\sec^2 x - 1) \, dx = \tan x - x + C$$

The formulas
$$\int \tan^3 x \, dx = \frac{1}{2}\tan^2 x - \ln |\sec x| + C \tag{25}$$
$$\int \sec^3 x \, dx = \frac{1}{2}\sec x \tan x + \frac{1}{2}\ln |\sec x + \tan x| + C \tag{26}$$
can be deduced from (21), (22), and reduction formulas (19) and (20) as follows:
$$\int \tan^3 x \, dx = \frac{1}{2}\tan^2 x - \int \tan x \, dx = \frac{1}{2}\tan^2 x - \ln |\sec x| + C$$
$$\int \sec^3 x \, dx = \frac{1}{2}\sec x \tan x + \frac{1}{2}\int \sec x \, dx = \frac{1}{2}\sec x \tan x + \frac{1}{2}\ln |\sec x + \tan x| + C$$

---

### INTEGRATING PRODUCTS OF TANGENTS AND SECANTS

If $m$ and $n$ are positive integers, then the integral
$$\int \tan^m x \sec^n x \, dx$$
can be evaluated by one of the three procedures stated in Table 7.3.2, depending on whether $m$ and $n$ are odd or even.

#### Table 7.3.2: Integrating Products of Tangents and Secants
| Case | Procedure | Relevant Identities |
| :--- | :--- | :--- |
| $n$ even | • Split off a factor of $\sec^2 x$.<br>• Apply the relevant identity.<br>• Make the substitution $u = \tan x$. | $\sec^2 x = \tan^2 x + 1$ |
| $m$ odd | • Split off a factor of $\sec x \tan x$.<br>• Apply the relevant identity.<br>• Make the substitution $u = \sec x$. | $\tan^2 x = \sec^2 x - 1$ |
| $m$ even<br>$n$ odd | • Use the relevant identities to reduce the integrand to powers of $\sec x$ alone.<br>• Then use the reduction formula for powers of $\sec x$. | $\tan^2 x = \sec^2 x - 1$ |

#### Example 4
Evaluate: (a) $\int \tan^2 x \sec^4 x \, dx$ (b) $\int \tan^3 x \sec^3 x \, dx$ (c) $\int \tan^2 x \sec x \, dx$

**Solution (a).** Since $n = 4$ is even, we will follow the first procedure in Table 7.3.2:
$$\begin{aligned}
\int \tan^2 x \sec^4 x \, dx &= \int \tan^2 x \sec^2 x \sec^2 x \, dx \\
&= \int \tan^2 x(\tan^2 x + 1)\sec^2 x \, dx \\
&= \int u^2(u^2 + 1) \, du = \frac{1}{5}u^5 + \frac{1}{3}u^3 + C = \frac{1}{5}\tan^5 x + \frac{1}{3}\tan^3 x + C
\end{aligned}$$

**Solution (b).** Since $m = 3$ is odd, we will follow the second procedure in Table 7.3.2:
$$\begin{aligned}
\int \tan^3 x \sec^3 x \, dx &= \int \tan^2 x \sec^2 x(\sec x \tan x) \, dx \\
&= \int (\sec^2 x - 1)\sec^2 x(\sec x \tan x) \, dx \\
&= \int (u^2 - 1)u^2 \, du = \frac{1}{5}u^5 - \frac{1}{3}u^3 + C = \frac{1}{5}\sec^5 x - \frac{1}{3}\sec^3 x + C
\end{aligned}$$

**Solution (c).** Since $m = 2$ is even and $n = 1$ is odd, we will follow the third procedure in Table 7.3.2:
$$\begin{aligned}
\int \tan^2 x \sec x \, dx &= \int (\sec^2 x - 1)\sec x \, dx \\
&= \int \sec^3 x \, dx - \int \sec x \, dx \quad \text{See (26) and (22)} \\
&= \frac{1}{2}\sec x \tan x + \frac{1}{2}\ln |\sec x + \tan x| - \ln |\sec x + \tan x| + C \\
&= \frac{1}{2}\sec x \tan x - \frac{1}{2}\ln |\sec x + \tan x| + C
\end{aligned}$$

---

### AN ALTERNATIVE METHOD FOR INTEGRATING POWERS OF SINE, COSINE, TANGENT, AND SECANT

The methods in Tables 7.3.1 and 7.3.2 can sometimes be applied if $m = 0$ or $n = 0$ to integrate positive integer powers of sine, cosine, tangent, and secant without reduction formulas. For example, instead of using the reduction formula to integrate $\sin^3 x$, we can apply the second procedure in Table 7.3.1:
$$\begin{aligned}
\int \sin^3 x \, dx &= \int (\sin^2 x)\sin x \, dx \\
&= \int (1 - \cos^2 x)\sin x \, dx \quad [u = \cos x, du = -\sin x \, dx] \\
&= -\int (1 - u^2) \, du = \frac{1}{3}u^3 - u + C = \frac{1}{3}\cos^3 x - \cos x + C
\end{aligned}$$
which agrees with (11).

> *With the aid of the identity $1 + \cot^2 x = \csc^2 x$, the techniques in Table 7.3.2 can be adapted to evaluate integrals of the form $\int \cot^m x \csc^n x \, dx$. It is also possible to derive reduction formulas for powers of cot and csc that are analogous to Formulas (19) and (20).*

---

### MERCATOR’S MAP OF THE WORLD

The integral of $\sec x$ plays an important role in the design of navigational maps for charting nautical and aeronautical courses. Sailors and pilots usually chart their courses along paths with constant compass headings; for example, the course might be $30^\circ$ northeast or $135^\circ$ southeast. Except for courses that are parallel to the equator or run due north or south, a course with constant compass heading spirals around the Earth toward one of the poles (as in the top part of Figure 7.3.2). In 1569 the Flemish mathematician and geographer Gerhard Kramer (1512–1594) (better known by the Latin name Mercator) devised a world map, called the **Mercator projection**, in which spirals of constant compass headings appear as straight lines. This was extremely important because it enabled sailors to determine compass headings between two points by connecting them with a straight line on a map (as in the bottom part of Figure 7.3.2).

If the Earth is assumed to be a sphere of radius $4000\text{ mi}$, then the lines of latitude at $1^\circ$ increments are equally spaced about $70\text{ mi}$ apart (why?). However, in the Mercator projection, the lines of latitude become wider apart toward the poles, so that two widely spaced latitude lines near the poles may be actually the same distance apart on the Earth as two closely spaced latitude lines near the equator. It can be proved that on a Mercator map in which the equatorial line has length $L$, the vertical distance $D_\beta$ on the map between the equator (latitude $0^\circ$) and the line of latitude $\beta^\circ$ is
$$D_\beta = \frac{L}{2\pi}\int_0^{\beta\pi/180} \sec x \, dx \tag{27}$$

---

### QUICK CHECK EXERCISES 7.3
*(See page 508 for answers.)*

1. Complete each trigonometric identity with an expression involving $\cos 2x$.  
   (a) $\sin^2 x = \underline{\hspace{2cm}}$  
   (b) $\cos^2 x = \underline{\hspace{2cm}}$  
   (c) $\cos^2 x - \sin^2 x = \underline{\hspace{2cm}}$

2. Evaluate the integral.  
   (a) $\int \sec^2 x \, dx = \underline{\hspace{2cm}}$  
   (b) $\int \tan^2 x \, dx = \underline{\hspace{2cm}}$  
   (c) $\int \sec x \, dx = \underline{\hspace{2cm}}$  
   (d) $\int \tan x \, dx = \underline{\hspace{2cm}}$

3. Use the indicated substitution to rewrite the integral in terms of $u$. Do not evaluate the integral.  
   (a) $\int \sin^2 x \cos x \, dx; \quad u = \sin x$  
   (b) $\int \sin^3 x \cos^2 x \, dx; \quad u = \cos x$  
   (c) $\int \tan^3 x \sec^2 x \, dx; \quad u = \tan x$  
   (d) $\int \tan^3 x \sec x \, dx; \quad u = \sec x$

---

### EXERCISE SET 7.3

**1–52 Evaluate the integral.**

1. $\int \cos^3 x \sin x \, dx$
2. $\int \sin^5 3x \cos 3x \, dx$
3. $\int \sin^2 5\theta \, d\theta$
4. $\int \cos^2 3x \, dx$
5. $\int \sin^3 a\theta \, d\theta$
6. $\int \cos^3 at \, dt$
7. $\int \sin ax \cos ax \, dx$
8. $\int \sin^3 x \cos^3 x \, dx$
9. $\int \sin^2 t \cos^3 t \, dt$
10. $\int \sin^3 x \cos^2 x \, dx$
11. $\int \sin^2 x \cos^2 x \, dx$
12. $\int \sin^2 x \cos^4 x \, dx$
13. $\int \sin 2x \cos 3x \, dx$
14. $\int \sin 3\theta \cos 2\theta \, d\theta$
15. $\int \sin x \cos(x/2) \, dx$
16. $\int \cos^{1/3} x \sin x \, dx$
17. $\int_0^{\pi/2} \cos^3 x \, dx$
18. $\int_0^{\pi/2} \sin^2\frac{x}{2}\cos^2\frac{x}{2} \, dx$
19. $\int_0^{\pi/3} \sin^4 3x \cos^3 3x \, dx$
20. $\int_{-\pi}^\pi \cos^2 5\theta \, d\theta$
21. $\int_0^{\pi/6} \sin 4x \cos 2x \, dx$
22. $\int_0^{2\pi} \sin^2 kx \, dx$
23. $\int \sec^2(2x - 1) \, dx$
24. $\int \tan 5x \, dx$
25. $\int e^{-x}\tan(e^{-x}) \, dx$
26. $\int \cot 3x \, dx$
27. $\int \sec 4x \, dx$
28. $\int \frac{\sec(\sqrt{x})}{\sqrt{x}} \, dx$
29. $\int \tan^2 x \sec^2 x \, dx$
30. $\int \tan^5 x \sec^4 x \, dx$
31. $\int \tan 4x \sec^4 4x \, dx$
32. $\int \tan^4 \theta \sec^4 \theta \, d\theta$
33. $\int \sec^5 x \tan^3 x \, dx$
34. $\int \tan^5 \theta \sec\theta \, d\theta$
35. $\int \tan^4 x \sec x \, dx$
36. $\int \tan^2 x \sec^3 x \, dx$
37. $\int \tan t \sec^3 t \, dt$
38. $\int \tan x \sec^5 x \, dx$
39. $\int \sec^4 x \, dx$
40. $\int \sec^5 x \, dx$
41. $\int \tan^3 4x \, dx$
42. $\int \tan^4 x \, dx$
43. $\int \sqrt{\tan x}\sec^4 x \, dx$
44. $\int \tan x \sec^{3/2} x \, dx$
45. $\int_0^{\pi/8} \tan^2 2x \, dx$
46. $\int_0^{\pi/6} \sec^3 2\theta \tan 2\theta \, d\theta$
47. $\int_0^{\pi/2} \tan^5\frac{x}{2} \, dx$
48. $\int_0^{1/4} \sec\pi x \tan\pi x \, dx$
49. $\int \cot^3 x \csc^3 x \, dx$
50. $\int \cot^2 3t \sec 3t \, dt$
51. $\int \cot^3 x \, dx$
52. $\int \csc^4 x \, dx$

**53–56 True–False Determine whether the statement is true or false. Explain your answer.**

53. To evaluate $\int \sin^5 x \cos^8 x \, dx$, use the trigonometric identity $\sin^2 x = 1 - \cos^2 x$ and the substitution $u = \cos x$.
54. To evaluate $\int \sin^8 x \cos^5 x \, dx$, use the trigonometric identity $\sin^2 x = 1 - \cos^2 x$ and the substitution $u = \cos x$.
55. The trigonometric identity $\sin\alpha \cos\beta = \frac{1}{2}[\sin(\alpha - \beta) + \sin(\alpha + \beta)]$ is often useful for evaluating integrals of the form $\int \sin^m x \cos^n x \, dx$.
56. The integral $\int \tan^4 x \sec^5 x \, dx$ is equivalent to one whose integrand is a polynomial in $\sec x$.

57. Let $m, n$ be distinct nonnegative integers. Use Formulas (16)–(18) to prove:  
    (a) $\int_0^{2\pi} \sin mx \cos nx \, dx = 0$  
    (b) $\int_0^{2\pi} \cos mx \cos nx \, dx = 0$  
    (c) $\int_0^{2\pi} \sin mx \sin nx \, dx = 0$.

58. Evaluate the integrals in Exercise 57 when $m$ and $n$ denote the same nonnegative integer.

59. Find the arc length of the curve $y = \ln(\cos x)$ over the interval $[0, \pi/4]$.

60. Find the volume of the solid generated when the region enclosed by $y = \tan x, y = 1,$ and $x = 0$ is revolved about the $x$-axis.

61. Find the volume of the solid that results when the region enclosed by $y = \cos x, y = \sin x, x = 0,$ and $x = \pi/4$ is revolved about the $x$-axis.

62. The region bounded below by the $x$-axis and above by the portion of $y = \sin x$ from $x = 0$ to $x = \pi$ is revolved about the $x$-axis. Find the volume of the resulting solid.

63. Use Formula (27) to show that if the length of the equatorial line on a Mercator projection is $L$, then the vertical distance $D$ between the latitude lines at $\alpha^\circ$ and $\beta^\circ$ on the same side of the equator (where $\alpha < \beta$) is
    $$D = \frac{L}{2\pi}\ln\left|\frac{\sec\beta^\circ + \tan\beta^\circ}{\sec\alpha^\circ + \tan\alpha^\circ}\right|$$

64. Suppose that the equator has a length of $100\text{ cm}$ on a Mercator projection. In each part, use the result in Exercise 63 to answer the question.  
    (a) What is the vertical distance on the map between the equator and the line at $25^\circ$ north latitude?  
    (b) What is the vertical distance on the map between New Orleans, Louisiana, at $30^\circ$ north latitude and Winnipeg, Canada, at $50^\circ$ north latitude?

#### FOCUS ON CONCEPTS

65. (a) Show that $\int \csc x \, dx = -\ln |\csc x + \cot x| + C$.  
    (b) Show that the result in part (a) can also be written as $\int \csc x \, dx = \ln |\csc x - \cot x| + C$ and $\int \csc x \, dx = \ln\left|\tan\frac{1}{2}x\right| + C$.

66. Rewrite $\sin x + \cos x$ in the form $A \sin(x + \phi)$ and use your result together with Exercise 65 to evaluate
    $$\int \frac{dx}{\sin x + \cos x}$$

67. Use the method of Exercise 66 to evaluate
    $$\int \frac{dx}{a\sin x + b\cos x} \quad (a, b \text{ not both zero})$$

68. (a) Use Formula (9) in Section 7.2 to show that
    $$\int_0^{\pi/2}\sin^n x \, dx = \frac{n - 1}{n}\int_0^{\pi/2}\sin^{n-2} x \, dx \quad (n \ge 2)$$  
    (b) Use this result to derive the Wallis sine formulas:
    $$\int_0^{\pi/2}\sin^n x \, dx = \frac{\pi}{2}\cdot \frac{1 \cdot 3 \cdot 5 \cdots (n - 1)}{2 \cdot 4 \cdot 6 \cdots n} \quad (n \text{ even and } \ge 2)$$
    $$\int_0^{\pi/2}\sin^n x \, dx = \frac{2 \cdot 4 \cdot 6 \cdots (n - 1)}{3 \cdot 5 \cdot 7 \cdots n} \quad (n \text{ odd and } \ge 3)$$

69. Use the Wallis formulas in Exercise 68 to evaluate: (a) $\int_0^{\pi/2}\sin^3 x \, dx$ (b) $\int_0^{\pi/2}\sin^4 x \, dx$ (c) $\int_0^{\pi/2}\sin^5 x \, dx$ (d) $\int_0^{\pi/2}\sin^6 x \, dx$.

70. Use Formula (10) in Section 7.2 and the method of Exercise 68 to derive the Wallis cosine formulas:
    $$\int_0^{\pi/2}\cos^n x \, dx = \frac{\pi}{2}\cdot \frac{1 \cdot 3 \cdot 5 \cdots (n - 1)}{2 \cdot 4 \cdot 6 \cdots n} \quad (n \text{ even and } \ge 2)$$
    $$\int_0^{\pi/2}\cos^n x \, dx = \frac{2 \cdot 4 \cdot 6 \cdots (n - 1)}{3 \cdot 5 \cdot 7 \cdots n} \quad (n \text{ odd and } \ge 3)$$

71. **Writing** Describe the various approaches for evaluating integrals of the form $\int \sin^m x \cos^n x \, dx$. Into what cases do these types of integrals fall? What procedures and identities are used in each case?

72. **Writing** Describe the various approaches for evaluating integrals of the form $\int \tan^m x \sec^n x \, dx$. Into what cases do these types of integrals fall? What procedures and identities are used in each case?

---

### QUICK CHECK ANSWERS 7.3

1. (a) $\frac{1 - \cos 2x}{2}$  
   (b) $\frac{1 + \cos 2x}{2}$  
   (c) $\cos 2x$
2. (a) $\tan x + C$  
   (b) $\tan x - x + C$  
   (c) $\ln |\sec x + \tan x| + C$  
   (d) $\ln |\sec x| + C$
3. (a) $\int u^2 \, du$  
   (b) $\int (u^2 - 1)u^2 \, du$  
   (c) $\int u^3 \, du$  
   (d) $\int (u^2 - 1) \, du$

---

