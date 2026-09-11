# CHAPTER 6: EXPONENTIAL, LOGARITHMIC, AND INVERSE TRIGONOMETRIC FUNCTIONS

*The growth and decline of animal populations and natural resources can be modeled using basic functions studied in this chapter.*

We begin this chapter with a review of exponential and logarithmic functions. These functions have important applications, from modeling population growth and the spread of disease, to the measurement of the magnitude of an earthquake or the perceived loudness of a sound. Logarithmic and exponential functions are best understood within the context of inverse functions and we will derive an important relationship between the derivative of a function and the derivative of its inverse. This connection will allow us to compute derivative formulas for logarithmic and exponential functions, along with their associated integration formulas. Later in the chapter we will exploit this connection again, to find the derivatives of inverse trigonometric functions, together with some related integration formulas. Along the way, we will discuss L’Hôpital’s rule, a powerful tool for evaluating limits. We conclude the chapter with a study of some important combinations of exponential functions known as “hyperbolic functions.”

---

## 6.1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS

When logarithms were introduced in the seventeenth century as a computational tool, they provided scientists of that period computing power that was previously unimaginable. Although computers and calculators have replaced logarithm tables for numerical calculations, the logarithmic functions have wide-ranging applications in mathematics and science. In this section we will review some properties of exponents and logarithms and then develop results about exponential and logarithmic functions.

### IRRATIONAL EXPONENTS
Recall from algebra that if $b$ is a nonzero real number, then nonzero integer powers of $b$ are defined by
$$b^n = \underbrace{b \times b \times \dots \times b}_{n\text{ factors}} \quad\text{and}\quad b^{-n} = \frac{1}{b^n}$$
and if $n = 0$, then $b^0 = 1$. Also, if $p/q$ is a positive rational number expressed in lowest terms, then
$$b^{p/q} = \sqrt[q]{b^p} = (\sqrt[q]{b})^p \quad\text{and}\quad b^{-p/q} = \frac{1}{b^{p/q}}$$
If $b$ is negative, then some fractional powers of $b$ will have imaginary values—the quantity $(-2)^{1/2} = \sqrt{-2}$, for example. To avoid this complication, we will assume throughout this section that $b > 0$, even if it is not stated explicitly.

There are various methods for defining irrational powers such as
$$2^\pi, \quad 3^{\sqrt{2}}, \quad \pi^{-\sqrt{7}}$$
One approach is to define irrational powers of $b$ via successive approximations using rational powers of $b$. For example, to define $2^\pi$ consider the decimal representation of $\pi$: $3.1415926\dots$  
From this decimal we can form a sequence of rational numbers that gets closer and closer to $\pi$, namely,
$$3.1, \quad 3.14, \quad 3.141, \quad 3.1415, \quad 3.14159$$
and from these we can form a sequence of rational powers of 2:
$$2^{3.1}, \quad 2^{3.14}, \quad 2^{3.141}, \quad 2^{3.1415}, \quad 2^{3.14159}$$
Since the exponents of the terms in this sequence get successively closer to $\pi$, it seems plausible that the terms themselves will get successively closer to some number. It is that number that we define to be $2^\pi$. This is illustrated in Table 6.1.1, which suggests that to four decimal places the value of $2^\pi$ is
$$2^\pi \approx 8.8250 \tag{1}$$

#### Table 6.1.1
| $x$ | $2^x$ |
| :--- | :--- |
| 3 | 8.000000 |
| 3.1 | 8.574188 |
| 3.14 | 8.815241 |
| 3.141 | 8.821353 |
| 3.1415 | 8.824411 |
| 3.14159 | 8.824962 |
| 3.141592 | 8.824974 |
| 3.1415926 | 8.824977 |

With this notion for irrational powers, the following familiar laws of exponents hold for all real values of $p$ and $q$:
$$b^p b^q = b^{p+q}, \quad \frac{b^p}{b^q} = b^{p-q}, \quad (b^p)^q = b^{pq}$$

---

### THE FAMILY OF EXPONENTIAL FUNCTIONS
A function of the form $f(x) = b^x$, where $b > 0$, is called an **exponential function with base $b$**. Some examples are
$$f(x) = 2^x, \quad f(x) = \left(\frac{1}{2}\right)^x, \quad f(x) = \pi^x$$
Note that an exponential function has a constant base and variable exponent. Thus, functions such as $f(x) = x^2$ and $f(x) = x^\pi$ would not be classified as exponential functions, since they have a variable base and a constant exponent.

Figure 6.1.1 illustrates that the graph of $y = b^x$ has one of three general forms, depending on the value of $b$. The graph of $y = b^x$ has the following properties:
* The graph passes through $(0, 1)$ because $b^0 = 1$.
* If $b > 1$, the value of $b^x$ increases as $x$ increases. As you traverse the graph of $y = b^x$ from left to right, the values of $b^x$ increase indefinitely. If you traverse the graph from right to left, the values of $b^x$ decrease toward zero but never reach zero. Thus, the $x$-axis is a horizontal asymptote of the graph of $b^x$.
* If $0 < b < 1$, the value of $b^x$ decreases as $x$ increases. As you traverse the graph of $y = b^x$ from left to right, the values of $b^x$ decrease toward zero but never reach zero. Thus, the $x$-axis is a horizontal asymptote of the graph of $b^x$. If you traverse the graph from right to left, the values of $b^x$ increase indefinitely.
* If $b = 1$, then the value of $b^x$ is constant ($y = 1^x = 1$).

Some typical members of the family of exponential functions are graphed in Figure 6.1.2. The graph of $y = (1/b)^x$ is the reflection of the graph of $y = b^x$ about the $y$-axis because replacing $x$ by $-x$ in $y = b^x$ yields $y = b^{-x} = (1/b)^x$. For $b > 1$, the larger the base $b$, the more rapidly the function $f(x) = b^x$ increases for $x > 0$.

> **6.1.1 THEOREM**  
> If $b > 0$ and $b \neq 1$, then:  
> (a) The function $f(x) = b^x$ is defined for all real values of $x$, so its natural domain is $(-\infty, +\infty)$.  
> (b) The function $f(x) = b^x$ is continuous on the interval $(-\infty, +\infty)$, and its range is $(0, +\infty)$.

#### Example 1
Sketch the graph of the function $f(x) = 1 - 2^x$ and find its domain and range.

**Solution.** Start with a graph of $y = 2^x$. Reflect this graph across the $x$-axis to obtain the graph of $y = -2^x$, then translate that graph upward by 1 unit to obtain the graph of $y = 1 - 2^x$ (Figure 6.1.3). The dashed line $y = 1$ is a horizontal asymptote for the graph. The domain of $f$ is $(-\infty, +\infty)$ and the range is $(-\infty, 1)$.

---

### THE NATURAL EXPONENTIAL FUNCTION
Among all possible bases for exponential functions there is one particular base that plays a special role in calculus. That base, denoted by the letter $e$, is a certain irrational number whose value to six decimal places is
$$e \approx 2.718282 \tag{2}$$
This base is important in calculus because, as we will prove later, $b = e$ is the only base for which the slope of the tangent line to the curve $y = b^x$ at any point $P$ on the curve is equal to the $y$-coordinate at $P$. Thus, for example, the tangent line to $y = e^x$ at $(0, 1)$ has slope 1 (Figure 6.1.4).

*The use of the letter $e$ is in honor of the Swiss mathematician Leonhard Euler who is credited with recognizing the mathematical importance of this constant.*

The function $f(x) = e^x$ is called the **natural exponential function**. To simplify typography, the natural exponential function is sometimes written as $\exp(x)$, in which case the relationship $e^{x_1+x_2} = e^{x_1}e^{x_2}$ would be expressed as $\exp(x_1 + x_2) = \exp(x_1)\exp(x_2)$.

The constant $e$ also arises in the context of the graph of the equation
$$y = \left(1 + \frac{1}{x}\right)^x \tag{3}$$
As suggested by Figure 6.1.5 and Table 6.1.2, $y = e$ is a horizontal asymptote of this graph, and the limits
$$\lim_{x \to +\infty}\left(1 + \frac{1}{x}\right)^x = e \quad\text{and}\quad \lim_{x \to -\infty}\left(1 + \frac{1}{x}\right)^x = e \tag{4–5}$$
are satisfied. These limits can be derived from the limit
$$\lim_{x \to 0} (1 + x)^{1/x} = e \tag{6}$$
which is sometimes taken as the definition of $e$.

#### Table 6.1.2: The values of $(1 + 1/x)^x$ approach $e$ as $x \to +\infty$
| $x$ | $1 + 1/x$ | $(1 + 1/x)^x$ |
| :--- | :--- | :--- |
| 1 | 2 | 2.000000 |
| 10 | 1.1 | 2.593742 |
| 100 | 1.01 | 2.704814 |
| 1000 | 1.001 | 2.716924 |
| 10,000 | 1.0001 | 2.718146 |
| 100,000 | 1.00001 | 2.718268 |
| 1,000,000 | 1.000001 | 2.718280 |

---

### LOGARITHMIC FUNCTIONS
Recall from algebra that a logarithm is an exponent. More precisely, if $b > 0$ and $b \neq 1$, then for a positive value of $x$ the expression
$$\log_b x$$
(read “the logarithm to the base $b$ of $x$”) denotes that exponent to which $b$ must be raised to produce $x$. Thus, for example,
* $\log_{10} 100 = 2 \quad (\text{since } 10^2 = 100)$
* $\log_{10}(1/1000) = -3 \quad (\text{since } 10^{-3} = 1/1000)$
* $\log_2 16 = 4 \quad (\text{since } 2^4 = 16)$
* $\log_b 1 = 0 \quad (\text{since } b^0 = 1)$
* $\log_b b = 1 \quad (\text{since } b^1 = b)$

We call the function $f(x) = \log_b x$ the **logarithmic function with base $b$**. Logarithms with base 10 are called **common logarithms** and are often written simply as $\log x$.

Logarithmic functions can also be viewed as inverses of exponential functions. If $b > 0$ and $b \neq 1$, the graph of $f(x) = b^x$ passes the horizontal line test, so $b^x$ has an inverse. Solving $x = b^y$ for $y$ yields $y = \log_b x$.

> **6.1.2 THEOREM**  
> If $b > 0$ and $b \neq 1$, then $b^x$ and $\log_b x$ are inverse functions.

It follows from this theorem that the graphs of $y = b^x$ and $y = \log_b x$ are reflections of one another about the line $y = x$ (Figure 6.1.6). All graphs of $y = \log_b x$ pass through $(1, 0)$ (Figure 6.1.7).

The most important logarithm function in applications is the one with base $e$. This is called the **natural logarithm function** because $\log_e x$ is the inverse of the natural exponential function $e^x$. It is standard to denote the natural logarithm of $x$ by $\ln x$ (read “ell en of $x$”). For example,
$$\ln 1 = 0, \quad \ln e = 1, \quad \ln(1/e) = -1, \quad \ln(e^2) = 2$$
In general, $y = \ln x$ if and only if $x = e^y$.

#### Table 6.1.3: Correspondence Between Properties of $b^x$ and $\log_b x$
| PROPERTY OF $b^x$ | PROPERTY OF $\log_b x$ |
| :--- | :--- |
| $b^0 = 1$ | $\log_b 1 = 0$ |
| $b^1 = b$ | $\log_b b = 1$ |
| Range is $(0, +\infty)$ | Domain is $(0, +\infty)$ |
| Domain is $(-\infty, +\infty)$ | Range is $(-\infty, +\infty)$ |
| $x$-axis is a horizontal asymptote | $y$-axis is a vertical asymptote |

Cancellation properties:
$$\log_b(b^x) = x \quad\text{for all real } x, \quad b^{\log_b x} = x \quad\text{for } x > 0 \tag{7}$$
In the special case where $b = e$:
$$\ln(e^x) = x \quad\text{for all real } x, \quad e^{\ln x} = x \quad\text{for } x > 0 \tag{8}$$

---

### SOLVING EQUATIONS INVOLVING EXPONENTIALS AND LOGARITHMS

> **6.1.3 THEOREM (Algebraic Properties of Logarithms)**  
> If $b > 0, b \neq 1, a > 0, c > 0,$ and $r$ is any real number, then:  
> (a) $\log_b(ac) = \log_b a + \log_b c$ (Product property)  
> (b) $\log_b(a/c) = \log_b a - \log_b c$ (Quotient property)  
> (c) $\log_b(a^r) = r\log_b a$ (Power property)  
> (d) $\log_b(1/c) = -\log_b c$ (Reciprocal property)

*WARNING:* $\log_b(u + v) \neq \log_b u + \log_b v$ and $\log_b(u - v) \neq \log_b u - \log_b v$.

#### Example 2
Find $x$ such that: (a) $\log x = \sqrt{2}$ (b) $\ln(x + 1) = 5$ (c) $5^x = 7$

**Solution (a).** $x = 10^{\sqrt{2}} \approx 25.95$.  
**Solution (b).** $x + 1 = e^5 \implies x = e^5 - 1 \approx 147.41$.  
**Solution (c).** $x = \log_5 7 = \frac{\ln 7}{\ln 5} \approx 1.21$.

#### Example 3
A satellite that requires $7\text{ watts}$ of power to operate at full capacity is equipped with a radioisotope power supply whose power output $P$ in watts is given by $P = 75e^{-t/125}$, where $t$ is the time in days that the supply is used. How long can the satellite operate at full capacity?

**Solution.** Set $P = 7$:
$$7 = 75e^{-t/125} \implies \frac{7}{75} = e^{-t/125} \implies \ln(7/75) = -\frac{t}{125} \implies t = -125\ln(7/75) \approx 296.4\text{ days}$$

#### Example 4
Solve $\frac{e^x - e^{-x}}{2} = 1$ for $x$.

**Solution.** Multiplying both sides by 2: $e^x - e^{-x} = 2 \implies e^x - \frac{1}{e^x} = 2 \implies e^{2x} - 2e^x - 1 = 0$.  
Let $u = e^x$: $u^2 - 2u - 1 = 0 \implies u = \frac{2 \pm \sqrt{4 + 4}}{2} = 1 \pm \sqrt{2}$.  
Since $e^x > 0$, discard $1 - \sqrt{2}$. Thus $e^x = 1 + \sqrt{2} \implies x = \ln(1 + \sqrt{2}) \approx 0.881$.

---

### CHANGE OF BASE FORMULA FOR LOGARITHMS
$$\log_b x = \frac{\ln x}{\ln b} \tag{9}$$

#### Example 5
Use a calculating utility to evaluate $\log_2 5$ by expressing this logarithm in terms of natural logarithms.

**Solution.** $\log_2 5 = \frac{\ln 5}{\ln 2} \approx 2.321928$.

---

### LOGARITHMIC SCALES IN SCIENCE AND ENGINEERING
* **Sound Level:** $\beta = 10\log(I/I_0)$ decibels (dB), where $I_0 = 10^{-12}\text{ W/m}^2$.

#### Table 6.1.4: Sound Levels
| $\beta$ (dB) | $I/I_0$ |
| :--- | :--- |
| 0 | $10^0 = 1$ |
| 10 | $10^1 = 10$ |
| 20 | $10^2 = 100$ |
| 30 | $10^3 = 1000$ |
| 40 | $10^4 = 10,000$ |
| 50 | $10^5 = 100,000$ |
| $\vdots$ | $\vdots$ |
| 120 | $10^{12} = 1,000,000,000,000$ |

#### Example 6
A space shuttle taking off generates a sound level of $150\text{ dB}$ near the launchpad. By comparison, a car horn at one meter has a sound level of $110\text{ dB}$. What is the ratio of sound intensity of a space shuttle takeoff to that of a car horn?

**Solution.** $\beta_1 - \beta_2 = 10\log(I_1/I_0) - 10\log(I_2/I_0) = 10\log(I_1/I_2) \implies 150 - 110 = 40 = 10\log(I_1/I_2) \implies \log(I_1/I_2) = 4 \implies I_1/I_2 = 10^4 = 10,000$.

---

### EXPONENTIAL AND LOGARITHMIC GROWTH
Both $e^x$ and $\ln x$ increase as $x$ increases, but at drastically different rates (Table 6.1.5).
$$\lim_{x \to +\infty} e^x = +\infty, \quad \lim_{x \to +\infty} \ln x = +\infty \tag{10–11}$$
$$\lim_{x \to -\infty} e^x = 0, \quad \lim_{x \to 0^+} \ln x = -\infty \tag{12–13}$$
$$\lim_{x \to +\infty} e^{-x} = 0, \quad \lim_{x \to -\infty} e^{-x} = +\infty \tag{14–15}$$

---

### QUICK CHECK EXERCISES 6.1
*(See page 420 for answers.)*

1. The function $y = (1/2)^x$ has domain $\underline{\hspace{1.5cm}}$ and range $\underline{\hspace{1.5cm}}$.
2. The function $y = \ln(1 - x)$ has domain $\underline{\hspace{1.5cm}}$ and range $\underline{\hspace{1.5cm}}$.
3. Express as a power of 4: (a) 1 (b) 2 (c) $1/16$ (d) $\sqrt{8}$ (e) 5.
4. Solve each equation for $x$: (a) $e^x = 1/2$ (b) $10^{3x} = 1,000,000$ (c) $7e^{3x} = 56$.
5. Solve each equation for $x$: (a) $\ln x = 3$ (b) $\log(x - 1) = 2$ (c) $2\log x - \log(x + 1) = \log 4 - \log 3$.

#### QUICK CHECK ANSWERS 6.1
1. $(-\infty, +\infty); \; (0, +\infty)$  
2. $(-\infty, 1); \; (-\infty, +\infty)$  
3. (a) $4^0$ (b) $4^{1/2}$ (c) $4^{-2}$ (d) $4^{3/4}$ (e) $4^{\log_4 5}$  
4. (a) $\ln\frac{1}{2} = -\ln 2$ (b) $2$ (c) $\ln 2$  
5. (a) $e^3$ (b) $101$ (c) $2$

---

### EXERCISE SET 6.1

**1–2 Simplify the expression without using a calculating utility.**
1. (a) $-8^{2/3}$ (b) $(-8)^{2/3}$ (c) $8^{-2/3}$
2. (a) $2^{-4}$ (b) $4^{1.5}$ (c) $9^{-0.5}$

**3–4 Use a calculating utility to approximate the expression. Round your answer to four decimal places.**
3. (a) $2^{1.57}$ (b) $5^{-2.1}$
4. (a) $\sqrt[5]{24}$ (b) $\sqrt[8]{0.6}$

**5–6 Find the exact value of the expression without using a calculating utility.**
5. (a) $\log_2 16$ (b) $\log_2(1/32)$ (c) $\log_4 4$ (d) $\log_9 3$
6. (a) $\log_{10}(0.001)$ (b) $\log_{10}(10^4)$ (c) $\ln(e^3)$ (d) $\ln(\sqrt{e})$

**7–8 Use a calculating utility to approximate the expression. Round your answer to four decimal places.**
7. (a) $\log 23.2$ (b) $\ln 0.74$
8. (a) $\log 0.3$ (b) $\ln \pi$

**9–10 Use the logarithm properties in Theorem 6.1.3 to rewrite the expression in terms of $r, s,$ and $t$, where $r = \ln a, s = \ln b,$ and $t = \ln c$.**
9. (a) $\ln(a^2\sqrt{bc})$ (b) $\ln\frac{b}{a^3 c}$
10. (a) $\ln\frac{\sqrt[3]{c}}{ab}$ (b) $\ln\sqrt{\frac{ab^3}{c^2}}$

**11–12 Expand the logarithm in terms of sums, differences, and multiples of simpler logarithms.**
11. (a) $\log(10x\sqrt{x - 3})$ (b) $\ln\frac{x^2\sin^3 x}{\sqrt{x^2 + 1}}$
12. (a) $\log\frac{\sqrt[3]{x + 2}}{\cos 5x}$ (b) $\ln\sqrt{\frac{x^2 + 1}{x^3 + 5}}$

**13–15 Rewrite the expression as a single logarithm.**
13. $4\log 2 - \log 3 + \log 16$
14. $\frac{1}{2}\log x - 3\log(\sin 2x) + 2$
15. $2\ln(x + 1) + \frac{1}{3}\ln x - \ln(\cos x)$

**16–23 Solve for $x$ without using a calculating utility.**
16. $\log_{10}(1 + x) = 3$
17. $\log_{10}(\sqrt{x}) = -1$
18. $\ln(x^2) = 4$
19. $\ln(1/x) = -2$
20. $\log_3(3^x) = 7$
21. $\log_5(5^{2x}) = 8$
22. $\ln 4x - 3\ln(x^2) = \ln 2$
23. $\ln(1/x) + \ln(2x^3) = \ln 3$

**24–29 Solve for $x$ without using a calculating utility. Use the natural logarithm anywhere that logarithms are needed.**
24. $3^x = 2$
25. $5^{-2x} = 3$
26. $3e^{-2x} = 5$
27. $2e^{3x} = 7$
28. $e^x - 2xe^x = 0$
29. $xe^{-x} + 2e^{-x} = 0$
30. Solve $e^{-2x} - 3e^{-x} = -2$ for $x$ without using a calculating utility. [*Hint:* Rewrite the equation as a quadratic equation in $u = e^{-x}$.]

#### FOCUS ON CONCEPTS
**31–34 In each part, identify the domain and range of the function, and then sketch the graph of the function without using a graphing utility.**
31. (a) $f(x) = (1/2)^{x-1} - 1$ (b) $g(x) = \ln|x|$
32. (a) $f(x) = 1 + \ln(x - 2)$ (b) $g(x) = 3 + e^{x-2}$
33. (a) $f(x) = \ln(x^2)$ (b) $g(x) = e^{-x^2}$
34. (a) $f(x) = 1 - e^{-x+1}$ (b) $g(x) = 3\ln\sqrt[3]{x - 1}$

**35–38 True–False Determine whether the statement is true or false. Explain your answer.**
35. The function $y = x^3$ is an exponential function.
36. The graph of the exponential function with base $b$ passes through the point $(0, 1)$.
37. The natural logarithm function is the logarithmic function with base $e$.
38. The domain of a logarithmic function is the interval $x > 1$.

39. Use a calculating utility and the change of base formula (9) to find the values of $\log_2 7.35$ and $\log_5 0.6$, rounded to four decimal places.
40. [Graphing Utility] Graph $\ln x, e^x, \log x, 10^x$ on the same screen.
41. [Graphing Utility] Graph $\log_2 x, \ln x, \log_5 x, \log x$ on the same screen.
42. (a) Derive the general change of base formula $\log_b x = \frac{\log_a x}{\log_a b}$.  
    (b) Use the result in part (a) to find the exact value of $(\log_2 81)(\log_3 32)$ without using a calculating utility.
43. [Graphing Utility] Use a graphing utility to estimate the two points of intersection of the graphs of $y = 1.3^x$ and $y = \log_{1.3} x$.
44. [Graphing Utility] Use a graphing utility to estimate the two points of intersection of the graphs of $y = 0.6^{(x^2)}$ and $y = \log_{0.6}(x^2)$.

#### FOCUS ON CONCEPTS
45. (a) Is the curve in Figure Ex-45 the graph of an exponential function? Explain your reasoning.  
    (b) Find the equation of an exponential function that passes through the point $(4, 2)$.  
    (c) Find the equation of an exponential function that passes through the point $(2, 1/4)$.  
    (d) Use a graphing utility to generate the graph of an exponential function that passes through $(2, 5)$.
46. (a) Make a conjecture about the general shape of the graph of $y = \log(\log x)$, and sketch the graph of this equation and $y = \log x$ in the same coordinate system.  
    (b) Check your work in part (a) with a graphing utility.
47. Find the fallacy in the following “proof” that $1/8 > 1/4$: Multiply both sides of $3 > 2$ by $\log(1/2)$ to get $3\log(1/2) > 2\log(1/2) \implies \log(1/2)^3 > \log(1/2)^2 \implies \log(1/8) > \log(1/4) \implies 1/8 > 1/4$.
48. Prove the four algebraic properties of logarithms in Theorem 6.1.3.
49. If equipment in the satellite of Example 3 requires 15 watts to operate correctly, what is the operational lifetime of the power supply?
50. The equation $Q = 12e^{-0.055t}$ gives the mass $Q$ in grams of radioactive potassium-42 that will remain from some initial quantity after $t$ hours of radioactive decay.  
    (a) How many grams were there initially?  
    (b) How many grams remain after 4 hours?  
    (c) How long will it take to reduce the amount of radioactive potassium-42 to half of the initial amount?
51. The acidity of a substance is measured by its pH value, which is defined by $\text{pH} = -\log[H^+]$. Distilled water has $\text{pH} = 7$; acidic if $\text{pH} < 7$, basic if $\text{pH} > 7$. Find the pH of: (a) Arterial blood $[H^+] = 3.9 \times 10^{-8}\text{ mol/L}$ (b) Tomatoes $[H^+] = 6.3 \times 10^{-5}\text{ mol/L}$ (c) Milk $[H^+] = 4.0 \times 10^{-7}\text{ mol/L}$ (d) Coffee $[H^+] = 1.2 \times 10^{-6}\text{ mol/L}$.
52. Find $[H^+]$ in a solution having a pH equal to (a) 2.44 (b) 8.06.
53. The perceived loudness $\beta$ of a sound in decibels is $\beta = 10\log(I/I_0)$ where $I_0 = 10^{-12}\text{ W/m}^2$. Ear damage occurs at $90\text{ dB}$ or greater. Find the decibel level and state damage risk for: (a) Jet aircraft ($1.0 \times 10^2\text{ W/m}^2$) (b) Amplified rock music ($1.0\text{ W/m}^2$) (c) Garbage disposal ($1.0 \times 10^{-4}\text{ W/m}^2$) (d) TV ($3.2 \times 10^{-5}\text{ W/m}^2$).
54. If one sound is three times as intense as another, how much greater is its decibel level?
55. If moving automobile noise is $70\text{ dB}$ and blender is $93\text{ dB}$, find the ratio of blender noise intensity to automobile noise intensity.
56. If an echo intensity is $2/3$ of the original sound, how many echoes will be heard from a $120\text{ dB}$ sound given human hearing threshold is $10\text{ dB}$?
57. On the Richter scale, $\log E = 4.4 + 1.5M$.  
    (a) Find energy $E$ of 1906 San Francisco earthquake ($M = 8.2$).  
    (b) If energy is 10 times greater, how much greater is magnitude $M$?
58. If two earthquake magnitudes differ by 1 on the Richter scale, find the ratio of released energy of the larger to the smaller earthquake.

---

## 6.2 DERIVATIVES AND INTEGRALS INVOLVING LOGARITHMIC FUNCTIONS

In this section we will obtain derivative formulas for logarithmic functions, and we will explain why the natural logarithm function is preferred in calculus over logarithms with other bases. The derivative formulas that we derive will allow us to find and use corresponding integral formulas.

### DERIVATIVES OF LOGARITHMIC FUNCTIONS
We begin by establishing that $f(x) = \ln x$ is differentiable for $x > 0$ using the definition of derivative:
$$\frac{d}{dx}[\ln x] = \lim_{h \to 0} \frac{\ln(x + h) - \ln x}{h} = \lim_{h \to 0} \frac{1}{h}\ln\left(1 + \frac{h}{x}\right) = \frac{1}{x}\lim_{v \to 0} \ln(1 + v)^{1/v} = \frac{1}{x}\ln e = \frac{1}{x}$$
Thus,
$$\frac{d}{dx}[\ln x] = \frac{1}{x}, \quad x > 0 \tag{2}$$
For general base $b$:
$$\frac{d}{dx}[\log_b x] = \frac{1}{x \ln b}, \quad x > 0 \tag{3}$$

#### Example 1
(a) Slopes of tangent lines to $y = \ln x$ at $x = 1/2, 1, 3, 5$ are $1/x = 2, 1, 1/3, 1/5$.  
(b) $dy/dx = 1/x \neq 0$ for any $x$, so there are no horizontal tangent lines.

Chain rule extensions ($u > 0$):
$$\frac{d}{dx}[\ln u] = \frac{1}{u}\frac{du}{dx} \quad\text{and}\quad \frac{d}{dx}[\log_b u] = \frac{1}{u \ln b}\frac{du}{dx} \tag{4–5}$$

#### Example 2
$$\frac{d}{dx}[\ln(x^2 + 1)] = \frac{1}{x^2 + 1}(2x) = \frac{2x}{x^2 + 1}$$

#### Example 3
$$\frac{d}{dx}\left[\ln\left(\frac{x^2\sin x}{\sqrt{1 + x}}\right)\right] = \frac{d}{dx}\left[2\ln x + \ln(\sin x) - \frac{1}{2}\ln(1 + x)\right] = \frac{2}{x} + \cot x - \frac{1}{2 + 2x}$$

Derivative of $\ln|x|$:
$$\frac{d}{dx}[\ln|x|] = \frac{1}{x} \quad\text{if } x \neq 0 \tag{6}$$

#### Example 4
$$\frac{d}{dx}[\ln|\sin x|] = \frac{1}{\sin x}\cos x = \cot x$$

---

### LOGARITHMIC DIFFERENTIATION

#### Example 5
Find the derivative of $y = \frac{x^2\sqrt[3]{7x - 14}}{(1 + x^2)^4}$.  
Take natural log of both sides: $\ln y = 2\ln x + \frac{1}{3}\ln(7x - 14) - 4\ln(1 + x^2)$.  
Differentiating: $\frac{1}{y}\frac{dy}{dx} = \frac{2}{x} + \frac{7/3}{7x - 14} - \frac{8x}{1 + x^2}$.  
$$\frac{dy}{dx} = \frac{x^2\sqrt[3]{7x - 14}}{(1 + x^2)^4}\left[\frac{2}{x} + \frac{1}{3x - 6} - \frac{8x}{1 + x^2}\right]$$

---

### INTEGRALS INVOLVING $\ln x$
$$\int \frac{1}{u} du = \ln|u| + C \tag{8}$$

#### Examples 6–8
* $\int_1^e \frac{1}{x} dx = 1, \quad \int_{-e}^{-1}\frac{1}{x} dx = -1$.
* $\int \frac{3x^2}{x^3 + 5} dx = \ln|x^3 + 5| + C$.
* $\int \tan x dx = -\ln|\cos x| + C = \ln|\sec x| + C$.
* General principle: $\int \frac{g'(x)}{g(x)} dx = \ln|g(x)| + C$.

---

### DERIVATIVES OF REAL POWERS OF $x$
For any real number $r$:
$$\frac{d}{dx}[x^r] = rx^{r-1} \tag{9}$$

---

### QUICK CHECK EXERCISES 6.2
*(See page 427 for answers.)*

1. The equation of the tangent line to the graph of $y = \ln x$ at $x = e^2$ is $\underline{\hspace{1.5cm}}$.
2. Find $dy/dx$: (a) $y = \ln 3x$ (b) $y = \ln\sqrt{x}$ (c) $y = \log(1/|x|)$.
3. Use logarithmic differentiation to find the derivative of $f(x) = \frac{\sqrt{x + 1}}{\sqrt[3]{x - 1}}$.
4. $\lim_{h \to 0} \frac{\ln(1 + h)}{h} = \underline{\hspace{1.5cm}}$.
5. $\int_2^5 \frac{1}{t} dt = \underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 6.2
1. $y = \frac{x}{e^2} + 1$  
2. (a) $\frac{1}{x}$ (b) $\frac{1}{2x}$ (c) $-\frac{1}{x\ln 10}$  
3. $\frac{\sqrt{x + 1}}{\sqrt[3]{x - 1}}\left[\frac{1}{2(x + 1)} - \frac{1}{3(x - 1)}\right]$  
4. 1  
5. $\ln(5/2)$

---

### EXERCISE SET 6.2

**1–26 Find $dy/dx$.**
1. $y = \ln 5x$
2. $y = \ln(x/3)$
3. $y = \ln|1 + x|$
4. $y = \ln(2 + \sqrt{x})$
5. $y = \ln|x^2 - 1|$
6. $y = \ln|x^3 - 7x^2 - 3|$
7. $y = \ln\left(\frac{x}{1 + x^2}\right)$
8. $y = \ln\left|\frac{1 + x}{1 - x}\right|$
9. $y = \ln x^2$
10. $y = (\ln x)^3$
11. $y = \sqrt{\ln x}$
12. $y = \ln\sqrt{x}$
13. $y = x\ln x$
14. $y = x^3\ln x$
15. $y = x^2\log_2(3 - 2x)$
16. $y = x[\log_2(x^2 - 2x)]^3$
17. $y = \frac{x^2}{1 + \log x}$
18. $y = \frac{\log x}{1 + \log x}$
19. $y = \ln(\ln x)$
20. $y = \ln(\ln(\ln x))$
21. $y = \ln(\tan x)$
22. $y = \ln(\cos x)$
23. $y = \cos(\ln x)$
24. $y = \sin^2(\ln x)$
25. $y = \log(\sin^2 x)$
26. $y = \log(1 - \sin^2 x)$

**27–30 Use the method of Example 3 to help perform the indicated differentiation.**
27. $\frac{d}{dx}[\ln((x - 1)^3(x^2 + 1)^4)]$
28. $\frac{d}{dx}[\ln((\cos^2 x)\sqrt{1 + x^4})]$
29. $\frac{d}{dx}\left[\ln\frac{\cos x}{\sqrt{4 - 3x^2}}\right]$
30. $\frac{d}{dx}\left[\ln\sqrt{\frac{x - 1}{x + 1}}\right]$

**31–34 True–False Determine whether the statement is true or false. Explain your answer.**
31. The slope of the tangent line to the graph of $y = \ln x$ at $x = a$ approaches infinity as $a \to 0^+$.
32. If $\lim_{x \to +\infty} f'(x) = 0$, then the graph of $y = f(x)$ has a horizontal asymptote.
33. The derivative of $\ln|x|$ is an odd function.
34. We have $\frac{d}{dx}((\ln x)^2) = \frac{d}{dx}(2(\ln x)) = \frac{2}{x}$.

**35–38 Find $dy/dx$ using logarithmic differentiation.**
35. $y = x\sqrt[3]{1 + x^2}$
36. $y = \sqrt[5]{\frac{x - 1}{x + 1}}$
37. $y = \frac{(x^2 - 8)^{1/3}\sqrt{x^3 + 1}}{x^6 - 7x + 5}$
38. $y = \frac{\sin x \cos x \tan^3 x}{\sqrt{x}}$

**39–40 Find the derivatives:**
39. (a) $\frac{d}{dx}[\log_x e]$ (b) $\frac{d}{dx}[\log_x 2]$
40. (a) $\frac{d}{dx}[\log_{(1/x)} e]$ (b) $\frac{d}{dx}[\log_{(\ln x)} e]$

**41–44 Find the equation of the tangent line to the graph of $y = f(x)$ at $x = x_0$.**
41. $f(x) = \ln x; x_0 = e^{-1}$
42. $f(x) = \log x; x_0 = 10$
43. $f(x) = \ln(-x); x_0 = -e$
44. $f(x) = \ln|x|; x_0 = -2$

#### FOCUS ON CONCEPTS
45. (a) Find the equation of a line through the origin that is tangent to the graph of $y = \ln x$.  
    (b) Explain why the $y$-intercept of a tangent line to $y = \ln x$ must be 1 unit less than the $y$-coordinate of the point of tangency.
46. Use logarithmic differentiation to verify the product and quotient rules. Explain what properties of $\ln x$ are important for this verification.
47. Find a formula for the area $A(w)$ of the triangle bounded by the tangent line to $y = \ln x$ at $P(w, \ln w)$, the horizontal line through $P$, and the $y$-axis.
48. Find a formula for the area $A(w)$ of the triangle bounded by the tangent line to $y = \ln x^2$ at $P(w, \ln w^2)$, the horizontal line through $P$, and the $y$-axis.
49. Verify that $y = \ln(x + e)$ satisfies $dy/dx = e^{-y}$, with $y = 1$ when $x = 0$.
50. Verify that $y = -\ln(e^2 - x)$ satisfies $dy/dx = e^y$, with $y = -2$ when $x = 0$.
51. Find a function $f$ such that $y = f(x)$ satisfies $dy/dx = e^{-y}$, with $y = 0$ when $x = 0$.
52. Find a function $f$ such that $y = f(x)$ satisfies $dy/dx = e^y$, with $y = -\ln 2$ when $x = 0$.
53. Let $p$ denote paramecia population satisfying $0 = \ln p + 0.83 - \ln(2.3 - 0.0046p) - 2.3t$. Show $dp/dt = 0.0046p(500 - p)$.
54. Let $p$ denote US population satisfying $0 = \ln p + 45.817 - \ln(2225 - 4.2381p) - 0.02225t$. Show $dp/dt = 10^{-5}p(2225 - 4.2381p)$.
55–57. Limits by derivative definition:
55. (a) $\lim_{x \to 0}\frac{\ln(1 + 3x)}{x}$ (b) $\lim_{x \to 0}\frac{\ln(1 - 5x)}{x}$
56. (a) $\lim_{\Delta x \to 0}\frac{\ln(e^2 + \Delta x) - 2}{\Delta x}$ (b) $\lim_{w \to 1}\frac{\ln w}{w - 1}$
57. (a) $\lim_{x \to 0}\frac{\ln(\cos x)}{x}$ (b) $\lim_{h \to 0}\frac{(1 + h)^{\sqrt{2}} - 1}{h}$
58. Modify the derivation of Equation (2) to give another proof of Equation (3).

**59–72 Evaluate integrals:**
59. $\int \left(\frac{2}{x} + 3\sin x\right) dx$
60. $\int \left(\frac{1}{2t} + 2t\right) dt$
61. $\int \frac{dx}{x\ln x}; u = \ln x$
62. $\int \frac{\sin 3\theta}{1 + \cos 3\theta} d\theta; u = 1 + \cos 3\theta$
63. $\int \frac{x^4}{1 + x^5} dx$
64. $\int \frac{dx}{2x}$
65. $\int \frac{t + 1}{t} dt$
66. $\int \cot x dx$
67. $\int_0^2 \frac{3x}{1 + x^2} dx$
68. $\int_{1/2}^1 \frac{1}{2x} dx$
69. $\int_e^{e^2} \frac{\ln x}{x} dx; u = \ln x$
70. $\int_{e^{-3}}^{e^3} \frac{\sqrt{9 - (\ln x)^2}}{x} dx; u = \ln x$ (geometric evaluation)
71. $\int_0^e \frac{dx}{2x + e}$
72. $\int_0^{\pi/3} \frac{\sin x}{1 + \cos x} dx$
73. Solve IVP: $dy/dt = 1/t, y(-1) = 5$.
74. **Writing.** Review derivation of $\frac{d}{dx}[\ln x] = 1/x$.
75. **Writing.** Logarithmic differentiation simplification.

---

## 6.3 DERIVATIVES OF INVERSE FUNCTIONS; DERIVATIVES AND INTEGRALS INVOLVING EXPONENTIAL FUNCTIONS

### DIFFERENTIABILITY OF INVERSE FUNCTIONS
If $f$ is a differentiable and one-to-one function, then
$$(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))} \tag{2}$$
provided $f'(f^{-1}(x)) \neq 0$. In Leibniz notation:
$$\frac{dy}{dx} = \frac{1}{dx/dy} \tag{3}$$

#### Example 1
$f(2) = 1, f'(2) = 3/4 \implies (f^{-1})'(1) = \frac{1}{f'(2)} = \frac{4}{3}$.

> **6.3.1 THEOREM**  
> Suppose that the domain of a function $f$ is an open interval on which $f'(x) > 0$ or on which $f'(x) < 0$. Then $f$ is one-to-one, $f^{-1}(x)$ is differentiable at all values of $x$ in the range of $f$, and the derivative of $f^{-1}(x)$ is given by Formula (2).

#### Example 2
$f(x) = x^5 + x + 1$. Show $f$ has a differentiable inverse, and compute $(f^{-1})'(1)$.  
$f'(x) = 5x^4 + 1 > 0 \implies f$ is one-to-one. $f(0) = 1 \implies f^{-1}(1) = 0 \implies (f^{-1})'(1) = \frac{1}{f'(0)} = \frac{1}{1} = 1$.

---

### DERIVATIVES OF EXPONENTIAL FUNCTIONS
$$\frac{d}{dx}[b^x] = b^x \ln b \tag{5}$$
$$\frac{d}{dx}[e^x] = e^x \tag{6}$$
General chain rule forms:
$$\frac{d}{dx}[b^u] = b^u \ln b \frac{du}{dx} \quad\text{and}\quad \frac{d}{dx}[e^u] = e^u \frac{du}{dx} \tag{7–8}$$

#### Example 3
* $\frac{d}{dx}[2^x] = 2^x \ln 2$
* $\frac{d}{dx}[e^{-2x}] = -2e^{-2x}$
* $\frac{d}{dx}[e^{x^3}] = 3x^2 e^{x^3}$
* $\frac{d}{dx}[e^{\cos x}] = -(\sin x)e^{\cos x}$

#### Example 4
Differentiate $y = (x^2 + 1)^{\sin x}$:  
$\ln y = (\sin x)\ln(x^2 + 1) \implies \frac{1}{y}\frac{dy}{dx} = (\sin x)\frac{2x}{x^2 + 1} + (\cos x)\ln(x^2 + 1)$.  
$$\frac{dy}{dx} = (x^2 + 1)^{\sin x}\left[\frac{2x\sin x}{x^2 + 1} + (\cos x)\ln(x^2 + 1)\right]$$

---

### INTEGRALS INVOLVING EXPONENTIAL FUNCTIONS
$$\int b^u du = \frac{b^u}{\ln b} + C \quad\text{and}\quad \int e^u du = e^u + C \tag{9–10}$$

#### Examples 5–8
* $\int 2^x dx = \frac{2^x}{\ln 2} + C$.
* $\int e^{5x} dx = \frac{1}{5}e^{5x} + C$.
* $\int x^2 e^{x^3} dx = \frac{1}{3}e^{x^3} + C$.
* $\int_0^{\ln 3} e^x(1 + e^x)^{1/2} dx = \frac{16 - 4\sqrt{2}}{3}$.

---

### QUICK CHECK EXERCISES 6.3
*(See page 434 for answers.)*

1. Suppose that a one-to-one function $f$ has tangent line $y = 5x + 3$ at the point $(1, 8)$. Evaluate $(f^{-1})'(8)$.
2. In each case, from the given derivative, determine whether the function $f$ is invertible:  
   (a) $f'(x) = x^2 + 1$ (b) $f'(x) = x^2 - 1$ (c) $f'(x) = \sin x$ (d) $f'(x) = \frac{1}{2} - e^{x^2}$.
3. Evaluate the derivative: (a) $\frac{d}{dx}[e^x]$ (b) $\frac{d}{dx}[7^x]$ (c) $\frac{d}{dx}[\cos(e^x + 1)]$ (d) $\frac{d}{dx}[e^{3x-2}]$.
4. Let $f(x) = e^{x^3 + x}$. Use $f'(x)$ to verify that $f$ is one-to-one.
5. $\int_0^{\frac{1}{2}\ln 5} e^x dx = \underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 6.3
1. $1/5$  
2. (a) yes (b) no (c) no (d) yes  
3. (a) $e^x$ (b) $7^x\ln 7$ (c) $-e^x\sin(e^x + 1)$ (d) $3e^{3x-2}$  
4. $f'(x) = e^{x^3 + x}(3x^2 + 1) > 0$ for all $x$  
5. $\sqrt{5} - 1$

---

### EXERCISE SET 6.3

#### FOCUS ON CONCEPTS
1. Let $f(x) = x^5 + x^3 + x$.  
   (a) Show that $f$ is one-to-one and confirm that $f(1) = 3$.  
   (b) Find $(f^{-1})'(3)$.
2. Let $f(x) = x^3 + 2e^x$.  
   (a) Show that $f$ is one-to-one and confirm that $f(0) = 2$.  
   (b) Find $(f^{-1})'(2)$.

**3–4 Find $(f^{-1})'(x)$ using Formula (2), and check your answer by differentiating $f^{-1}$ directly.**
3. $f(x) = 2/(x + 3)$
4. $f(x) = \ln(2x + 1)$

**5–6 Determine whether the function $f$ is one-to-one by examining the sign of $f'(x)$.**
5. (a) $f(x) = x^2 + 8x + 1$  
   (b) $f(x) = 2x^5 + x^3 + 3x + 2$  
   (c) $f(x) = 2x + \sin x$  
   (d) $f(x) = \left(\frac{1}{2}\right)^x$
6. (a) $f(x) = x^3 + 3x^2 - 8$  
   (b) $f(x) = x^5 + 8x^3 + 2x - 1$  
   (c) $f(x) = \frac{x}{x + 1}$  
   (d) $f(x) = \log_b x, \; 0 < b < 1$

**7–10 Find the derivative of $f^{-1}$ by using Formula (3), and check your result by differentiating implicitly.**
7. $f(x) = 5x^3 + x - 7$
8. $f(x) = 1/x^2, \; x > 0$
9. $f(x) = 2x^5 + x^3 + 1$
10. $f(x) = 5x - \sin 2x, \; -\frac{\pi}{4} < x < \frac{\pi}{4}$

#### FOCUS ON CONCEPTS
11. Figure 0.4.8 is a “proof by picture” that the reflection of a point $P(a, b)$ about the line $y = x$ is the point $Q(b, a)$. Establish this result rigorously by completing each part.  
    (a) Prove that if $P$ is not on the line $y = x$, then $P$ and $Q$ are distinct, and the line $\overleftrightarrow{PQ}$ is perpendicular to the line $y = x$.  
    (b) Prove that if $P$ is not on the line $y = x$, the midpoint of segment $PQ$ is on the line $y = x$.  
    (c) Carefully explain what it means geometrically to reflect $P$ about the line $y = x$.  
    (d) Use the results of parts (a)–(c) to prove that $Q$ is the reflection of $P$ about the line $y = x$.
12. Prove that the reflection about the line $y = x$ of a line with slope $m, \; m \neq 0$, is a line with slope $1/m$. [*Hint:* Apply the result of the previous exercise to a pair of points on the line of slope $m$ and to a corresponding pair of points on the reflection of this line about the line $y = x$.]
13. Suppose that $f$ and $g$ are increasing functions. Determine which of the functions $f(x) + g(x)$, $f(x)g(x)$, and $f(g(x))$ must also be increasing.
14. Suppose that $f$ and $g$ are one-to-one functions. Determine which of the functions $f(x) + g(x)$, $f(x)g(x)$, and $f(g(x))$ must also be one-to-one.

**15–26 Find $dy/dx$.**
15. $y = e^{7x}$
16. $y = e^{-5x^2}$
17. $y = x^3 e^x$
18. $y = e^{1/x}$
19. $y = \frac{e^x - e^{-x}}{e^x + e^{-x}}$
20. $y = \sin(e^x)$
21. $y = e^x \tan x$
22. $y = \frac{e^x}{\ln x}$
23. $y = e^{(x - e^{3x})}$
24. $y = \exp(\sqrt{1 + 5x^3})$
25. $y = \ln(1 - xe^{-x})$
26. $y = \ln(\cos e^x)$

**27–30 Find $f'(x)$ by Formula (7) and then by logarithmic differentiation.**
27. $f(x) = 2^{x^2}$
28. $f(x) = 3^{-x}$
29. $f(x) = \pi^{\sin x}$
30. $f(x) = \pi^{x\tan x}$

**31–35 Find $dy/dx$ using the method of logarithmic differentiation.**
31. $y = (x^3 - 2x)^{\ln x}$
32. $y = x^{\sin x}$
33. $y = (\ln x)^{\tan x}$
34. $y = (x^2 + 3)^{\ln x}$
35. $y = (\ln x)^{\ln x}$

36. (a) Explain why Formula (5) cannot be used to find $(d/dx)[x^x]$.  
    (b) Find this derivative by logarithmic differentiation.

**37–42 Find $dy/dx$ using any method.**
37. $y = (x^3 - 2x^2 + 1)e^x$
38. $y = (2x^2 - 2x + 1)e^{2x}$
39. $y = (x^2 + \sqrt{x})3^x$
40. $y = (x^3 + \sqrt[3]{x})5^x$
41. $y = 4^{3\sin x - e^x}$
42. $y = 2^{\cos x + \ln x}$

**43–46 True–False Determine whether the statement is true or false. Explain your answer.**
43. If a function $y = f(x)$ satisfies $dy/dx = y$, then $y = e^x$.
44. If $y = f(x)$ is a function such that $dy/dx$ is a rational function, then $f(x)$ is also a rational function.
45. $\frac{d}{dx}(\log_b |x|) = \frac{1}{x\ln b}$
46. If the tangent line to the graph of $f(x) = b^x$ has slope 1 at the point $(0, 1)$, then $f$ is the natural exponential function.

47. (a) Show that $f(x) = x^3 - 3x^2 + 2x$ is not one-to-one on $(-\infty, +\infty)$.  
    (b) Find the largest value of $k$ such that $f$ is one-to-one on the interval $(-k, k)$.
48. (a) Show that the function $f(x) = x^4 - 2x^3$ is not one-to-one on $(-\infty, +\infty)$.  
    (b) Find the smallest value of $k$ such that $f$ is one-to-one on the interval $[k, +\infty)$.
49. Let $f(x) = x^4 + x^3 + 1, \; 0 \le x \le 2$.  
    (a) Show that $f$ is one-to-one.  
    (b) Let $g(x) = f^{-1}(x)$ and define $F(x) = f(2g(x))$. Find an equation for the tangent line to $y = F(x)$ at $x = 3$.
50. Let $f(x) = \frac{\exp(4 - x^2)}{x}, \; x > 0$.  
    (a) Show that $f$ is one-to-one.  
    (b) Let $g(x) = f^{-1}(x)$ and define $F(x) = f([g(x)]^2)$. Find $F'(1/2)$.
51. Show that for any constants $A$ and $k$, the function $y = Ae^{kt}$ satisfies the equation $dy/dt = ky$.
52. Show that for any constants $A$ and $B$, the function $y = Ae^{2x} + Be^{-4x}$ satisfies the equation $y'' + 2y' - 8y = 0$.
53. Show that  
    (a) $y = xe^{-x}$ satisfies the equation $xy' = (1 - x)y$  
    (b) $y = xe^{-x^2/2}$ satisfies the equation $xy' = (1 - x^2)y$.
54. Show that the rate of change of $y = 100e^{-0.2x}$ with respect to $x$ is proportional to $y$.
55. Suppose that the percentage of U.S. households with broadband Internet access is modeled by the equation
    $$P(t) = \frac{5300}{53 + 47e^{-0.182t}}$$
    where $P(t)$ is the percentage $t$ years after an initial survey result made in the year 2007.  
    (a) Use a graphing utility to graph the function $P(t)$.  
    (b) In words, explain what happens to the percentage over time. Check your conclusion by finding $\lim_{t \to +\infty} P(t)$.  
    (c) In words, what happens to the rate of population growth over time? Check your conclusion by graphing $P'(t)$.
56. Suppose that the population of oxygen-dependent bacteria in a pond is modeled by the equation
    $$P(t) = \frac{60}{5 + 7e^{-t}}$$
    where $P(t)$ is the population (in billions) $t$ days after an initial observation at time $t = 0$.  
    (a) Use a graphing utility to graph the function $P(t)$.  
    (b) In words, explain what happens to the population over time. Check your conclusion by finding $\lim_{t \to +\infty} P(t)$.  
    (c) In words, what happens to the rate of population growth over time? Check your conclusion by graphing $P'(t)$.

**57–59 Find the limit by interpreting the expression as an appropriate derivative.**
57. $\lim_{x \to 0}\frac{e^{3x} - 1}{x}$
58. $\lim_{x \to 0}\frac{\exp(x^2) - 1}{x}$
59. $\lim_{h \to 0}\frac{10^h - 1}{h}$

60. Suppose that a steel ball bearing is released within a vat of fluid and begins to sink. According to one model, the speed $v(t)$ (in m/s) of the ball bearing $t$ seconds after its release is given by the formula
    $$v(t) = \frac{9.8(1 - e^{-kt})}{k}$$
    where $k$ is a positive constant that corresponds to the resistance the fluid offers against the motion of the bearing. (The smaller the value of $k$, the weaker will be the resistance.) For $t$ fixed, determine the limiting value of the speed as $k \to 0^+$, and give a physical interpretation of the limit. [*Hint:* Interpret the limit as an appropriate derivative.]

**61–62 Evaluate the integral and check your answer by differentiating.**
61. $\int \left(\frac{2}{x} + 3e^x\right) dx$
62. $\int \left(\frac{1}{2t} - \sqrt{2}e^t\right) dt$

**63–64 Evaluate the integrals using the indicated substitutions.**
63. $\int e^{-5x} dx; \; u = -5x$
64. $\int \frac{e^x}{1 + e^x} dx; \; u = 1 + e^x$

**65–72 Evaluate the integrals using appropriate substitutions.**
65. $\int e^{2x} dx$
66. $\int e^{-x/2} dx$
67. $\int e^{\sin x}\cos x \, dx$
68. $\int x^3 e^{x^4} dx$
69. $\int x^2 e^{-2x^3} dx$
70. $\int \frac{e^x + e^{-x}}{e^x - e^{-x}} dx$
71. $\int \frac{dx}{e^x}$
72. $\int \sqrt{e^x} dx$

**73–74 Evaluate each integral by first modifying the form of the integrand.**
73. $\int [\ln(e^x) + \ln(e^{-x})] dx$
74. $\int e^{2\ln x} dx$

**75–76 Evaluate the integrals.**
75. $\int_{\ln 2}^3 5e^x dx$
76. $\int_0^1 (e^x - x) dx$

77. Evaluate the definite integral by making the indicated $u$-substitution: $\int_0^1 e^{2x-1} dx; \; u = 2x - 1$.

**78–80 Evaluate the integrals by any method.**
78. $\int_0^{\ln 5} e^x(3 - 4e^x) dx$
79. $\int_{-\ln 3}^{\ln 3}\frac{e^x}{e^x + 4} dx$
80. $\int_1^{\sqrt{2}} x e^{-x^2} dx$

**81–84 Medication can be administered to a patient in different ways. For a given method, let $c(t)$ denote the concentration of medication in the patient’s bloodstream (measured in mg/L) $t$ hours after the dose is given. Over the time interval $0 \le t \le b$, the area between the graph of $c = c(t)$ and the interval $[0, b]$ indicates the “availability” of the medication for the patient’s body over that time period. Determine which method provides the greater availability over the given interval.**
81. Method 1: $c(t) = 5(e^{-0.2t} - e^{-t})$,  
    Method 2: $c(t) = 4(e^{-0.2t} - e^{-3t})$; $[0, 4]$
82. Method 1: $c(t) = 5(e^{-0.2t} - e^{-t})$,  
    Method 2: $c(t) = 4(e^{-0.2t} - e^{-3t})$; $[0, 24]$
83. Method 1: $c(t) = 5.78(e^{-0.4t} - e^{-1.3t})$,  
    Method 2: $c(t) = 4.15(e^{-0.4t} - e^{-3t})$; $[0, 4]$
84. Method 1: $c(t) = 5.78(e^{-0.4t} - e^{-1.3t})$,  
    Method 2: $c(t) = 4.15(e^{-0.4t} - e^{-3t})$; $[0, 24]$

85. Suppose that at time $t = 0$ there are 750 bacteria in a growth medium and the bacteria population $y(t)$ grows at the rate $y'(t) = 802.137e^{1.528t}$ bacteria per hour. How many bacteria will there be in 12 hours?
86. Suppose that a particle moving along a coordinate line has velocity $v(t) = 25 + 10e^{-0.05t}\text{ ft/s}$.  
    (a) What is the distance traveled by the particle from time $t = 0$ to time $t = 10$?  
    (b) Does the term $10e^{-0.05t}$ have much effect on the distance traveled by the particle over that time interval? Explain your reasoning.
87. Find a positive value of $k$ such that the area under the graph of $y = e^{2x}$ over the interval $[0, k]$ is 3 square units.
88. Solve the initial-value problem: $\frac{dy}{dt} = -e^{2t}, \; y(0) = 6$.
89. Let $y(t)$ denote the number of *E. coli* cells in a container of nutrient solution $t$ minutes after the start of an experiment. Assume that $y(t)$ is modeled by the initial-value problem $\frac{dy}{dt} = (\ln 2)2^{t/20}, \; y(0) = 20$. Use this model to estimate the number of *E. coli* cells in the container 2 hours after the start of the experiment.
90. **Writing.** Let $G$ denote the graph of an invertible function $f$ and consider $G$ as a fixed set of points in the plane. Suppose we relabel the coordinate axes so that the $x$-axis becomes the $y$-axis and vice versa. Carefully explain why now the same set of points $G$ becomes the graph of $f^{-1}$ (with the coordinate axes in a nonstandard position). Use this result to explain Formula (2).
91. **Writing.** Suppose that $f$ has an inverse function. Carefully explain the connection between Formula (2) and implicit differentiation of the equation $x = f(y)$.

---

## 6.4 GRAPHS AND APPLICATIONS INVOLVING LOGARITHMIC AND EXPONENTIAL FUNCTIONS

### PROPERTIES OF $e^x$ AND $\ln x$
* $e^x > 0$ for all $x$; increasing on $(-\infty, +\infty)$; concave up everywhere.
* $\ln x$ defined for $x > 0$; increasing on $(0, +\infty)$; concave down everywhere.

#### Example 1
Sketch $y = e^{-x^2/2}$: Symmetric about $y$-axis, horizontal asymptote $y = 0$, relative max at $(0, 1)$, inflection points at $(\pm 1, e^{-1/2}) \approx (\pm 1, 0.61)$.

#### Example 2
Graph $f(x) = (\ln x)/x$: Defined on $(0, +\infty)$, $x$-intercept at $x = 1$, relative max at $(e, 1/e) \approx (2.7, 0.37)$, inflection point at $(e^{3/2}, \frac{3}{2}e^{-3/2}) \approx (4.5, 0.33)$, horizontal asymptote $y = 0$, vertical asymptote $x = 0$.

---

### LOGISTIC CURVES
$$y = \frac{L}{1 + Ae^{-kt}} \tag{1}$$
* Population approaches carrying capacity $L$ as $t \to +\infty$.
* Inflection point occurs at half the carrying capacity $y = L/2$ at time $t = \frac{\ln A}{k}$.
* Rate of growth: $\frac{dy}{dt} = \frac{k}{L}y(L - y)$.

---

### NEWTON’S LAW OF COOLING

#### Example 4
Lemonade warming from $40^\circ\text{F}$ in a $70^\circ\text{F}$ room: $T(t) = 70 - 30e^{-0.5t}$.  
Average temperature over first 5 hours:
$$T_{\text{ave}} = \frac{1}{5}\int_0^5 (70 - 30e^{-0.5t}) dt = 58 + 12e^{-2.5} \approx 59^\circ\text{F}$$

---

### QUICK CHECK EXERCISES 6.4
*(See page 441 for answers.)*

1. $f'(x) = (x - 4)^2 e^{-x/2}, f''(x) = -\frac{1}{2}(x - 4)(x - 8)e^{-x/2}$.  
   (a) Increasing on $(-\infty, +\infty)$ (b) Concave up on $(4, 8)$ (c) Concave down on $(-\infty, 4), (8, +\infty)$.
2. $f(x) = x^2(2\ln x - 3), f'(x) = 4x(\ln x - 1), f''(x) = 4\ln x$.  
   (a) Increasing on $(e, +\infty)$ (b) Concave down on $(0, 1)$.
3. $f(x) = (x - 2)^2 e^{x/2}, f'(x) = \frac{1}{2}(x^2 - 4)e^{x/2}, f''(x) = \frac{1}{4}(x^2 + 4x - 4)e^{x/2}$.  
   (a) Above $x$-axis on $(-\infty, 2), (2, +\infty)$ (b) Increasing on $(-\infty, -2], [2, +\infty)$ (c) Concave up on $(-\infty, -2 - 2\sqrt{2}), (-2 + 2\sqrt{2}, +\infty)$ (d) Rel min $(2, 0)$ (e) Rel max $(-2, 16e^{-1}) \approx (-2, 5.89)$ (f) Inflection points at $x = -2 \pm 2\sqrt{2}$.

#### QUICK CHECK ANSWERS 6.4
1. (a) $(-\infty, +\infty)$ (b) $(4, 8)$ (c) $(-\infty, 4), (8, +\infty)$  
2. (a) $(e, +\infty)$ (b) $(0, 1)$  
3. (a) $(-\infty, 2)$ and $(2, +\infty)$ (b) $(-\infty, -2]$ and $[2, +\infty)$ (c) $(-\infty, -2 - 2\sqrt{2})$ and $(-2 + 2\sqrt{2}, +\infty)$ (d) $(2, 0)$ (e) $(-2, 16e^{-1}) \approx (-2, 5.89)$ (f) $-2 \pm 2\sqrt{2}$

---

### EXERCISE SET 6.4

**1–4 Use the given derivative to find all critical points of $f$, and at each critical point determine whether a relative maximum, relative minimum, or neither occurs. Assume in each case that $f$ is continuous everywhere.**
1. $f'(x) = xe^{1-x^2}$
2. $f'(x) = x^4(e^x - 3)$
3. $f'(x) = \ln\left(\frac{2}{1 + x^2}\right)$
4. $f'(x) = e^{2x} - 5e^x + 6$

**5–8 Use a graphing utility to estimate the absolute maximum and minimum values of $f$, if any, on the stated interval, and then use calculus methods to find the exact values.**
5. $f(x) = x^3 e^{-2x}; \; [1, 4]$
6. $f(x) = \frac{\ln(2x)}{x}; \; [1, e]$
7. $f(x) = 5\ln(x^2 + 1) - 3x; \; [0, 4]$
8. $f(x) = (x^2 - 1)e^x; \; [-2, 2]$

**9–18 We will develop techniques in Section 6.5 to verify that**
$$\lim_{x \to +\infty}\frac{e^x}{x} = +\infty, \quad \lim_{x \to +\infty}\frac{x}{e^x} = 0, \quad \lim_{x \to -\infty} xe^x = 0$$
**In these exercises: (a) Use these results, as necessary, to find the limits of $f(x)$ as $x \to +\infty$ and as $x \to -\infty$. (b) Sketch a graph of $f(x)$ and identify all relative extrema, inflection points, and asymptotes (as appropriate). Check your work with a graphing utility.**
9. $f(x) = xe^x$
10. $f(x) = xe^{-x}$
11. $f(x) = x^2 e^{-2x}$
12. $f(x) = x^2 e^{2x}$
13. $f(x) = x^2 e^{-x^2}$
14. $f(x) = e^{-1/x^2}$
15. $f(x) = \frac{e^x}{1 - x}$
16. $f(x) = x^{2/3}e^x$
17. $f(x) = x^2 e^{1-x}$
18. $f(x) = x^3 e^{x-1}$

**19–24 We will develop techniques in Section 6.5 to verify that**
$$\lim_{x \to +\infty}\frac{\ln x}{x^r} = 0, \quad \lim_{x \to +\infty}\frac{x^r}{\ln x} = +\infty, \quad \lim_{x \to 0^+} x^r \ln x = 0$$
**for any positive real number $r$. In these exercises: (a) Use these results, as necessary, to find the limits of $f(x)$ as $x \to +\infty$ and as $x \to 0^+$. (b) Sketch a graph of $f(x)$ and identify all relative extrema, inflection points, and asymptotes (as appropriate). Check your work with a graphing utility.**
19. $f(x) = x\ln x$
20. $f(x) = x^2 \ln x$
21. $f(x) = x^2 \ln(2x)$
22. $f(x) = \ln(x^2 + 1)$
23. $f(x) = x^{2/3}\ln x$
24. $f(x) = x^{-1/3}\ln x$

#### FOCUS ON CONCEPTS
25. Consider the family of curves $y = xe^{-bx} \; (b > 0)$.  
    (a) Use a graphing utility to generate some members of this family.  
    (b) Discuss the effect of varying $b$ on the shape of the graph, and discuss the locations of the relative extrema and inflection points.
26. Consider the family of curves $y = e^{-bx^2} \; (b > 0)$.  
    (a) Use a graphing utility to generate some members of this family.  
    (b) Discuss the effect of varying $b$ on the shape of the graph, and discuss the locations of the relative extrema and inflection points.
27. (a) Determine whether the following limits exist, and if so, find them:
    $$\lim_{x \to +\infty} e^x \cos x, \quad \lim_{x \to -\infty} e^x \cos x$$
    (b) Sketch the graphs of the equations $y = e^x, \; y = -e^x,$ and $y = e^x \cos x$ in the same coordinate system, and label any points of intersection.  
    (c) Use a graphing utility to generate some members of the family $y = e^{ax}\cos bx \; (a > 0 \text{ and } b > 0)$, and discuss the effect of varying $a$ and $b$ on the shape of the curve.
28. Consider the family of curves $y = x^n e^{-x^2/n}$, where $n$ is a positive integer.  
    (a) Use a graphing utility to generate some members of this family.  
    (b) Discuss the effect of varying $n$ on the shape of the graph, and discuss the locations of the relative extrema and inflection points.

**29–32 True–False Determine whether the statement is true or false. Explain your answer.**
29. The graph of $y = e^x$ is the reflection of the graph of $y = \ln x$ across the $y$-axis.
30. If $f$ is a function with derivative $f'(x) = e^{(x-1)^2}$, then $f$ has a relative minimum at $x = 1$.
31. The average value of $f(x) = \ln x$ over the interval $[1, e^2]$ is greater than 1.
32. Assume that $A, k,$ and $L$ are positive constants. The graph of the logistic curve $y = L/(1 + Ae^{-kt}), \; t \ge 0$, is increasing with horizontal asymptote $y = L$.

33. Suppose that a population $y$ grows according to the logistic model given by Formula (1).  
    (a) At what rate is $y$ increasing at time $t = 0$?  
    (b) In words, describe how the rate of growth of $y$ varies with time.  
    (c) At what time is the population growing most rapidly?
34. Suppose that the number of individuals at time $t$ in a certain wildlife population is given by
    $$N(t) = \frac{340}{1 + 9(0.77)^t}, \quad t \ge 0$$
    where $t$ is in years. Use a graphing utility to estimate the time at which the size of the population is increasing most rapidly.
35. Suppose that the spread of a flu virus on a college campus is modeled by the function
    $$y(t) = \frac{1000}{1 + 999e^{-0.9t}}$$
    where $y(t)$ is the number of infected students at time $t$ (in days, starting with $t = 0$). Use a graphing utility to estimate the day on which the virus is spreading most rapidly.
36. The logistic growth model given in Formula (1) is equivalent to $ye^{kt} + Ay = Le^{kt}$ where $y$ is the population at time $t \; (t \ge 0)$ and $A, k,$ and $L$ are positive constants. Use implicit differentiation to verify that
    $$\frac{dy}{dt} = \frac{k}{L}y(L - y), \quad \frac{d^2 y}{dt^2} = \frac{k^2}{L^2}y(L - y)(L - 2y)$$
37. Assuming that $A, k,$ and $L$ are positive constants, verify that the graph of $y = L/(1 + Ae^{-kt})$ has an inflection point at $\left(\frac{1}{k}\ln A, \frac{1}{2}L\right)$.
38. Suppose that the number of bacteria in a culture at time $t$ is given by $N = 5000(25 + te^{-t/20})$.  
    (a) Find the largest and smallest number of bacteria in the culture during the time interval $0 \le t \le 100$.  
    (b) At what time during the time interval in part (a) is the number of bacteria decreasing most rapidly?
39. The concentration $C(t)$ of a drug in the bloodstream $t$ hours after it has been injected is commonly modeled by an equation of the form
    $$C(t) = \frac{K(e^{-bt} - e^{-at})}{a - b}$$
    where $K > 0$ and $a > b > 0$.  
    (a) At what time does the maximum concentration occur?  
    (b) Let $K = 1$ for simplicity, and use a graphing utility to check your result in part (a) by graphing $C(t)$ for various values of $a$ and $b$.
40. Let $s(t) = te^{-t}$ be the position function of a particle moving along a coordinate line, where $s$ is in meters and $t$ is in seconds. Use a graphing utility to generate the graphs of $s(t), v(t),$ and $a(t)$ for $t \ge 0$, and use those graphs where needed.  
    (a) Use the appropriate graph to make a rough estimate of the time at which the particle first reverses the direction of its motion; and then find the time exactly.  
    (b) Find the exact position of the particle when it first reverses the direction of its motion.  
    (c) Use the appropriate graphs to make a rough estimate of the time intervals on which the particle is speeding up and on which it is slowing down; and then find those time intervals exactly.

**41–42 Find the area under the curve $y = f(x)$ over the stated interval.**
41. $f(x) = e^{2x}; \; [0, \ln 2]$
42. $f(x) = 1/x; \; [1, 5]$

**43–44 Sketch the area enclosed by the curves and find its area.**
43. $y = e^x, \; y = e^{2x}, \; x = 0, \; x = \ln 2$
44. $x = 1/y, \; x = 0, \; y = 1, \; y = e$

**45–46 Sketch the curve and find the total area between the curve and the given interval on the $x$-axis.**
45. $y = e^x - 1; \; [-1, 1]$
46. $y = \frac{x - 2}{x}; \; [1, 3]$

**47–49 Find the average value of the function over the given interval.**
47. $f(x) = 1/x; \; [1, e]$
48. $f(x) = e^x; \; [-1, \ln 5]$
49. $f(x) = e^{-2x}; \; [0, 4]$

50. Suppose that the value of a yacht in dollars after $t$ years of use is $V(t) = 275,000e^{-0.17t}$. What is the average value of the yacht over its first 10 years of use?

**51–52 For the given velocity function $v(t)$: (a) Generate the velocity versus time curve, and use it to make a conjecture about the sign of the displacement over the given time interval. (b) Use a CAS to find the displacement.**
51. $v(t) = 0.5 - te^{-t}; \; 0 \le t \le 5$
52. $v(t) = t\ln(t + 0.1); \; 0 \le t \le 1$

**53–54 Use a graphing utility to determine the number of times the curves intersect and then apply Newton’s Method, where needed, to approximate the $x$-coordinates of all intersections.**
53. $y = 1$ and $y = e^x \sin x; \; 0 < x < \pi$
54. $y = e^{-x}$ and $y = \ln x$

55. For the function $f(x) = \frac{e^{-x}}{1 + x^2}$, use Newton’s Method to approximate the $x$-coordinates of the inflection points to two decimal places.
56. (a) Show that $e^x \ge 1 + x$ if $x \ge 0$.  
    (b) Show that $e^x \ge 1 + x + \frac{1}{2}x^2$ if $x \ge 0$.  
    (c) Confirm the inequalities in parts (a) and (b) with a graphing utility.

**57–58 Find the volume of the solid that results when the region enclosed by the given curves is revolved about the $x$-axis.**
57. $y = e^x, \; y = 0, \; x = 0, \; x = \ln 3$
58. $y = e^{-2x}, \; y = 0, \; x = 0, \; x = 1$

**59–60 Use cylindrical shells to find the volume of the solid generated when the region enclosed by the given curves is revolved about the $y$-axis.**
59. $y = \frac{1}{x^2 + 1}, \; x = 0, \; x = 1, \; y = 0$
60. $y = e^{x^2}, \; x = 1, \; x = \sqrt{3}, \; y = 0$

**61–62 Use the arc length formula from Exercise 24 of Section 5.4 to find the arc length of the curve.**
61. $x = e^t \cos t, \; y = e^t \sin t \; (0 \le t \le \pi/2)$
62. $x = e^t(\sin t + \cos t), \; y = e^t(\cos t - \sin t) \; (1 \le t \le 4)$

**63–64 Express the exact arc length of the curve over the given interval as an integral that has been simplified to eliminate the radical, and then evaluate the integral using a CAS.**
63. $y = \ln(\sec x)$ from $x = 0$ to $x = \pi/4$
64. $y = \ln(\sin x)$ from $x = \pi/4$ to $x = \pi/2$

**65–66 Use a CAS or a calculating utility with numerical integration capabilities to approximate the area of the surface generated by revolving the curve about the stated axis. Round your answer to two decimal places.**
65. $y = e^x, \; 0 \le x \le 1$; $x$-axis
66. $y = e^x, \; 1 \le y \le e$; $y$-axis

---

## 6.5 L’HÔPITAL’S RULE; INDETERMINATE FORMS

### INDETERMINATE FORMS OF TYPE 0/0

> **6.5.1 THEOREM (L’Hôpital’s Rule for Form 0/0)**  
> Suppose that $f$ and $g$ are differentiable functions on an open interval containing $x = a$, except possibly at $x = a$, and that
> $$\lim_{x \to a} f(x) = 0 \quad\text{and}\quad \lim_{x \to a} g(x) = 0$$
> If $\lim_{x \to a}[f'(x)/g'(x)]$ exists, or if this limit is $+\infty$ or $-\infty$, then
> $$\lim_{x \to a}\frac{f(x)}{g(x)} = \lim_{x \to a}\frac{f'(x)}{g'(x)}$$
> Moreover, this statement is also true in the case of a limit as $x \to a^-, x \to a^+, x \to -\infty,$ or as $x \to +\infty$.

#### Examples 1–2
* $\lim_{x \to 2}\frac{x^2 - 4}{x - 2} = \lim_{x \to 2}\frac{2x}{1} = 4$.
* $\lim_{x \to 0}\frac{\sin 2x}{x} = 2$.
* $\lim_{x \to \pi/2}\frac{1 - \sin x}{\cos x} = \lim_{x \to \pi/2}\frac{-\cos x}{-\sin x} = 0$.
* $\lim_{x \to 0}\frac{e^x - 1}{x^3} = +\infty$.
* $\lim_{x \to 0}\frac{1 - \cos x}{x^2} = \lim_{x \to 0}\frac{\sin x}{2x} = \frac{1}{2}$.
* $\lim_{x \to +\infty}\frac{x^{-4/3}}{\sin(1/x)} = 0$.

---

### INDETERMINATE FORMS OF TYPE $\infty/\infty$

> **6.5.2 THEOREM (L’Hôpital’s Rule for Form $\infty/\infty$)**  
> If $\lim_{x \to a} f(x) = \infty$ and $\lim_{x \to a} g(x) = \infty$, then
> $$\lim_{x \to a}\frac{f(x)}{g(x)} = \lim_{x \to a}\frac{f'(x)}{g'(x)}$$

#### Example 3
* $\lim_{x \to +\infty}\frac{x}{e^x} = \lim_{x \to +\infty}\frac{1}{e^x} = 0$.
* $\lim_{x \to 0^+}\frac{\ln x}{\csc x} = 0$.

Growth analysis: $e^x$ grows faster than any power $x^n$:
$$\lim_{x \to +\infty}\frac{x^n}{e^x} = 0 \quad\text{and}\quad \lim_{x \to +\infty}\frac{e^x}{x^n} = +\infty \tag{5–6}$$

---

### OTHER INDETERMINATE FORMS
* **Type $0 \cdot \infty$:** Rewrite as $\frac{f}{1/g}$ or $\frac{g}{1/f}$. (Example: $\lim_{x \to 0^+} x\ln x = 0$).
* **Type $\infty - \infty$:** Combine terms algebraically. (Example: $\lim_{x \to 0^+}\left(\frac{1}{x} - \frac{1}{\sin x}\right) = 0$).
* **Types $0^0, \infty^0, 1^\infty$:** Set $y = f(x)^{g(x)}$, evaluate $\lim \ln y = \lim g(x)\ln f(x)$, then $\lim y = e^{\lim \ln y}$.  
  (Example 6: $\lim_{x \to 0}(1 + \sin x)^{1/x} = e$).

---

### QUICK CHECK EXERCISES 6.5
*(See page 450 for answers.)*

1. Does L’Hôpital’s rule apply? (a) $\lim_{x \to 1}\frac{2x - 2}{x^3 + x - 2}$ (b) $\lim_{x \to 0}\frac{\cos x}{x}$ (c) $\lim_{x \to 0}\frac{e^{2x} - 1}{\tan x}$.
2. Evaluate each limit in Quick Check Exercise 1.
3. Using L’Hôpital’s rule, $\lim_{x \to +\infty}\frac{e^x}{500x^2} = \underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 6.5
1. (a) yes (b) no (c) yes  
2. (a) $1/2$ (b) does not exist (c) $2$  
3. $+\infty$

---

### EXERCISE SET 6.5

**1–2 Evaluate without and then with L’Hôpital’s rule:**
1. (a) $\lim_{x \to 2}\frac{x^2 - 4}{x^2 + 2x - 8}$ (b) $\lim_{x \to +\infty}\frac{2x - 5}{3x + 7}$
2. (a) $\lim_{x \to 0}\frac{\sin x}{\tan x}$ (b) $\lim_{x \to 1}\frac{x^2 - 1}{x^3 - 1}$

**3–6 True–False:**
3. L’Hôpital’s rule does not apply to $\lim_{x \to -\infty}\frac{\ln x}{x}$ (True, $\ln x$ not defined for $x \le 0$).
4. For polynomial $p(x)$, $\lim_{x \to +\infty}\frac{p(x)}{e^x} = 0$ (True).
5. If $n$ is sufficiently large, $\lim_{x \to +\infty}\frac{(\ln x)^n}{x} = +\infty$ (False, limit is 0).
6. $\lim_{x \to 0^+}(\sin x)^{1/x} = 0$ (True).

**7–44 Limits:**
7. $\lim_{x \to 0}\frac{e^x - 1}{\sin x}$
8. $\lim_{x \to 0}\frac{\sin 2x}{\sin 5x}$
9. $\lim_{\theta \to 0}\frac{\tan\theta}{\theta}$
10. $\lim_{t \to 0}\frac{te^t}{1 - e^t}$
11. $\lim_{x \to \pi^+}\frac{\sin x}{x - \pi}$
12. $\lim_{x \to 0^+}\frac{\sin x}{x^2}$
13. $\lim_{x \to +\infty}\frac{\ln x}{x}$
14. $\lim_{x \to +\infty}\frac{e^{3x}}{x^2}$
15. $\lim_{x \to 0^+}\frac{\cot x}{\ln x}$
16. $\lim_{x \to 0^+}\frac{1 - \ln x}{e^{1/x}}$
17. $\lim_{x \to +\infty}\frac{x^{100}}{e^x}$
18. $\lim_{x \to 0^+}\frac{\ln(\sin x)}{\ln(\tan x)}$
19. $\lim_{x \to +\infty} xe^{-x}$
20. $\lim_{x \to \pi^-}(x - \pi)\tan\frac{1}{2}x$
21. $\lim_{x \to +\infty} x\sin\frac{\pi}{x}$
22. $\lim_{x \to 0^+} \tan x\ln x$
23. $\lim_{x \to \pi/2^-}\sec 3x\cos 5x$
24. $\lim_{x \to \pi}(x - \pi)\cot x$
25. $\lim_{x \to +\infty}(1 - 3/x)^x$
26. $\lim_{x \to 0}(1 + 2x)^{-3/x}$
27. $\lim_{x \to 0}(e^x + x)^{1/x}$
28. $\lim_{x \to +\infty}(1 + a/x)^{bx}$
29. $\lim_{x \to 1}(2 - x)^{\tan[(\pi/2)x]}$
30. $\lim_{x \to +\infty}[\cos(2/x)]^{x^2}$
31. $\lim_{x \to 0}(\csc x - 1/x)$
32. $\lim_{x \to 0}\left(\frac{1}{x^2} - \frac{\cos 3x}{x^2}\right)$
33. $\lim_{x \to +\infty}(\sqrt{x^2 + x} - x)$
34. $\lim_{x \to 0}\left(\frac{1}{x} - \frac{1}{e^x - 1}\right)$
35. $\lim_{x \to +\infty}[x - \ln(x^2 + 1)]$
36. $\lim_{x \to +\infty}[\ln x - \ln(1 + x)]$
37. $\lim_{x \to 0^+} x^{\sin x}$
38. $\lim_{x \to 0^+}(e^{2x} - 1)^x$
39. $\lim_{x \to 0^+}\left(-\frac{1}{\ln x}\right)^x$
40. $\lim_{x \to +\infty} x^{1/x}$
41. $\lim_{x \to +\infty}(\ln x)^{1/x}$
42. $\lim_{x \to 0^+}(-\ln x)^x$
43. $\lim_{x \to \pi/2^-}(\tan x)^{(\pi/2) - x}$
44. Show that for any positive integer $n$  
    (a) $\lim_{x \to +\infty}\frac{\ln x}{x^n} = 0$  
    (b) $\lim_{x \to +\infty}\frac{x^n}{\ln x} = +\infty$.

#### FOCUS ON CONCEPTS
45. (a) Find the error in the following calculation:
    $$\lim_{x \to 1}\frac{x^3 - x^2 + x - 1}{x^3 - x^2} = \lim_{x \to 1}\frac{3x^2 - 2x + 1}{3x^2 - 2x} = \lim_{x \to 1}\frac{6x - 2}{6x - 2} = 1$$
    (b) Find the correct limit.
46. (a) Find the error in the following calculation:
    $$\lim_{x \to 2}\frac{e^{3x^2 - 12x + 12}}{x^4 - 16} = \lim_{x \to 2}\frac{(6x - 12)e^{3x^2 - 12x + 12}}{4x^3} = 0$$
    (b) Find the correct limit.

**47–50 Make a conjecture about the limit by graphing the function involved with a graphing utility; then check your conjecture using L’Hôpital’s rule.**
47. $\lim_{x \to +\infty}\frac{\ln(\ln x)}{\sqrt{x}}$
48. $\lim_{x \to 0^+} x^x$
49. $\lim_{x \to 0^+}(\sin x)^{3/\ln x}$
50. $\lim_{x \to (\pi/2)^-}\frac{4\tan x}{1 + \sec x}$

**51–54 Make a conjecture about the equations of horizontal asymptotes, if any, by graphing the equation with a graphing utility; then check your answer using L’Hôpital’s rule.**
51. $y = \ln x - e^x$
52. $y = x - \ln(1 + 2e^x)$
53. $y = (\ln x)^{1/x}$
54. $y = \left(\frac{x + 1}{x + 2}\right)^x$

55. Limits of the type
    $$0/\infty, \quad \infty/0, \quad 0^\infty, \quad \infty \cdot \infty, \quad +\infty + (+\infty), \quad +\infty - (-\infty), \quad -\infty + (-\infty), \quad -\infty - (+\infty)$$
    are not indeterminate forms. Find the following limits by inspection.  
    (a) $\lim_{x \to 0^+}\frac{x}{\ln x}$  
    (b) $\lim_{x \to +\infty}\frac{x^3}{e^{-x}}$  
    (c) $\lim_{x \to (\pi/2)^-}(\cos x)^{\tan x}$  
    (d) $\lim_{x \to 0^+}(\ln x)\cot x$  
    (e) $\lim_{x \to 0^+}\left(\frac{1}{x} - \ln x\right)$  
    (f) $\lim_{x \to -\infty}(x + x^3)$

56. There is a myth that circulates among beginning calculus students which states that all indeterminate forms of types $0^0, \infty^0,$ and $1^\infty$ have value 1 because “anything to the zero power is 1” and “1 to any power is 1.” The fallacy is that $0^0, \infty^0,$ and $1^\infty$ are not powers of numbers, but rather descriptions of limits. The following examples, which were suggested by Prof. Jack Staib of Drexel University, show that such indeterminate forms can have any positive real value:  
    (a) $\lim_{x \to 0^+}[x^{(\ln a)/(1 + \ln x)}] = a$ (form $0^0$)  
    (b) $\lim_{x \to +\infty}[x^{(\ln a)/(1 + \ln x)}] = a$ (form $\infty^0$)  
    (c) $\lim_{x \to 0}[(x + 1)^{(\ln a)/x}] = a$ (form $1^\infty$).  
    Verify these results.

**57–60 Verify that L’Hôpital’s rule is of no help in finding the limit; then find the limit, if it exists, by some other method.**
57. $\lim_{x \to +\infty}\frac{x + \sin 2x}{x}$
58. $\lim_{x \to +\infty}\frac{2x - \sin x}{3x + \sin x}$
59. $\lim_{x \to +\infty}\frac{x(2 + \sin 2x)}{x + 1}$
60. $\lim_{x \to +\infty}\frac{x(2 + \sin x)}{x^2 + 1}$

61. The accompanying schematic diagram represents an electrical circuit consisting of an electromotive force that produces a voltage $V$, a resistor with resistance $R$, and an inductor with inductance $L$. It is shown in electrical circuit theory that if the voltage is first applied at time $t = 0$, then the current $I$ flowing through the circuit at time $t$ is given by
    $$I = \frac{V}{R}(1 - e^{-Rt/L})$$
    What is the effect on the current at a fixed time $t$ if the resistance approaches 0 (i.e., $R \to 0^+$)?
62. (a) Show that $\lim_{x \to \pi/2}(\pi/2 - x)\tan x = 1$.  
    (b) Show that $\lim_{x \to \pi/2}\left(\frac{1}{\pi/2 - x} - \tan x\right) = 0$.  
    (c) It follows from part (b) that the approximation $\tan x \approx \frac{1}{\pi/2 - x}$ should be good for values of $x$ near $\pi/2$. Use a calculator to find $\tan x$ and $1/(\pi/2 - x)$ for $x = 1.57$; compare the results.
63. (a) Use a CAS to show that if $k$ is a positive constant, then $\lim_{x \to +\infty} x(k^{1/x} - 1) = \ln k$.  
    (b) Confirm this result using L’Hôpital’s rule. [*Hint:* Express the limit in terms of $t = 1/x$.]  
    (c) If $n$ is a positive integer, then it follows from part (a) with $x = n$ that the approximation $n(\sqrt[n]{k} - 1) \approx \ln k$ should be good when $n$ is large. Use this result and the square root key on a calculator to approximate the values of $\ln 0.3$ and $\ln 2$ with $n = 1024$, then compare the values obtained with values of the logarithms generated directly from the calculator. [*Hint:* The $n\text{th}$ roots for which $n$ is a power of 2 can be obtained as successive square roots.]
64. Find all values of $k$ and $l$ such that $\lim_{x \to 0}\frac{k + \cos lx}{x^2} = -4$.

#### FOCUS ON CONCEPTS
65. Let $f(x) = x^2 \sin(1/x)$.  
    (a) Are the limits $\lim_{x \to 0^+} f(x)$ and $\lim_{x \to 0^-} f(x)$ indeterminate forms?  
    (b) Use a graphing utility to generate the graph of $f$, and use the graph to make conjectures about the limits in part (a).  
    (c) Use the Squeezing Theorem (1.6.2) to confirm that your conjectures in part (b) are correct.
66. (a) Explain why L’Hôpital’s rule does not apply to the problem $\lim_{x \to 0}\frac{x^2 \sin(1/x)}{\sin x}$.  
    (b) Find the limit.
67. Find $\lim_{x \to 0^+}\frac{x\sin(1/x)}{\sin x}$ if it exists.
68. Suppose that functions $f$ and $g$ are differentiable at $x = a$ and that $f(a) = g(a) = 0$. If $g'(a) \neq 0$, show that $\lim_{x \to a}\frac{f(x)}{g(x)} = \frac{f'(a)}{g'(a)}$ without using L’Hôpital’s rule. [*Hint:* Divide the numerator and denominator of $f(x)/g(x)$ by $x - a$ and use the definitions for $f'(a)$ and $g'(a)$.]
69. **Writing.** Were we to use L’Hôpital’s rule to evaluate either $\lim_{x \to 0}\frac{\sin x}{x}$ or $\lim_{x \to +\infty}\left(1 + \frac{1}{x}\right)^x$, we could be accused of circular reasoning. Explain why.
70. **Writing.** Exercise 56 shows that the indeterminate forms $0^0$ and $\infty^0$ can assume any positive real value. However, it is often the case that these indeterminate forms have value 1. Read the article “Indeterminate Forms of Exponential Type” by John Baxley and Elmer Hayashi in the June–July 1978 issue of *The American Mathematical Monthly*, and write a short report on why this is the case.

---

## 6.6 LOGARITHMIC AND OTHER FUNCTIONS DEFINED BY INTEGRALS

### THE CONNECTION BETWEEN NATURAL LOGARITHMS AND INTEGRALS
The formal foundation defines the natural logarithm as an integral:

> **6.6.1 DEFINITION**  
> The **natural logarithm** of $x$ is denoted by $\ln x$ and is defined by the integral
> $$\ln x = \int_1^x \frac{1}{t} dt, \quad x > 0 \tag{1}$$

By Part 2 of the Fundamental Theorem of Calculus:
$$\frac{d}{dx}[\ln x] = \frac{d}{dx}\int_1^x \frac{1}{t} dt = \frac{1}{x} \quad (x > 0) \tag{2}$$

---

### ALGEBRAIC PROPERTIES DERIVED FROM INTEGRALS

> **6.6.2 THEOREM**  
> For any positive numbers $a$ and $c$ and any rational number $r$:  
> (a) $\ln ac = \ln a + \ln c$  
> (b) $\ln\frac{1}{c} = -\ln c$  
> (c) $\ln\frac{a}{c} = \ln a - \ln c$  
> (d) $\ln a^r = r\ln a$

---

### DEFINITIONS OF $e$ AND $e^x$ FROM INTEGRALS
* The constant $e$ is defined as the unique number such that $\ln e = \int_1^e \frac{1}{t} dt = 1$.
* The function $e^x$ is defined as the inverse of $\ln x$.
* For real exponents: $a^r = e^{r\ln a} \tag{7}$.

---

### INTEGRALS WITH FUNCTIONS AS LIMITS OF INTEGRATION
By the chain rule and Fundamental Theorem of Calculus:
$$\frac{d}{dx}\int_a^{g(x)} f(t) dt = f(g(x))g'(x) \tag{18}$$
$$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t) dt = f(g(x))g'(x) - f(h(x))h'(x)$$

#### Examples
* $\frac{d}{dx}\int_1^{\sin x} (1 - t^2) dt = (1 - \sin^2 x)\cos x = \cos^3 x$.
* Initial value problems: Solution to $\frac{dy}{dx} = f(x), y(x_0) = y_0$ is $y(x) = y_0 + \int_{x_0}^x f(t) dt$.
* Nonelementary special functions:
  * Error function: $\text{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2} dt$.
  * Fresnel sine and cosine: $S(x) = \int_0^x \sin(\frac{\pi t^2}{2}) dt, \quad C(x) = \int_0^x \cos(\frac{\pi t^2}{2}) dt$.

---

### QUICK CHECK EXERCISES 6.6
*(See page 462 for answers.)*

1. $\int_1^{1/e} \frac{1}{t} dt = \underline{\hspace{1.5cm}}$.
2. Estimate $\ln 2$ using Definition 6.6.1 and (a) a left endpoint approximation with $n = 2$ (b) a right endpoint approximation with $n = 2$.
3. $\pi^{1/(\ln \pi)} = \underline{\hspace{1.5cm}}$.
4. A solution to the initial-value problem $dy/dx = \cos x^3, y(0) = 2$ that is defined by an integral is $y = \underline{\hspace{1.5cm}}$.
5. $\frac{d}{dx}\left[\int_0^{e^{-x}}\frac{1}{1 + t^4} dt\right] = \underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 6.6
1. $-1$  
2. (a) $5/6$ (b) $7/12$  
3. $e$  
4. $y = 2 + \int_0^x \cos t^3 dt$  
5. $-\frac{e^{-x}}{1 + e^{-4x}}$

---

### EXERCISE SET 6.6

1. Sketch the curve $y = 1/t$, and shade a region under the curve whose area is  
   (a) $\ln 2$  
   (b) $-\ln 0.5$  
   (c) $2$.
2. Sketch the curve $y = 1/t$, and shade two different regions under the curve whose areas are $\ln 1.5$.
3. Given that $\ln a = 2$ and $\ln c = 5$, find  
   (a) $\int_1^{ac} \frac{1}{t} dt$  
   (b) $\int_1^{1/c} \frac{1}{t} dt$  
   (c) $\int_1^{a/c} \frac{1}{t} dt$  
   (d) $\int_1^{a^3} \frac{1}{t} dt$.
4. Given that $\ln a = 9$, find  
   (a) $\int_1^{\sqrt{a}} \frac{1}{t} dt$  
   (b) $\int_1^{2a} \frac{1}{t} dt$  
   (c) $\int_1^{2/a} \frac{1}{t} dt$  
   (d) $\int_2^a \frac{1}{t} dt$.
5. Approximate $\ln 5$ using the midpoint rule with $n = 10$, and estimate the magnitude of the error by comparing your answer to that produced directly by a calculating utility.
6. Approximate $\ln 3$ using the midpoint rule with $n = 20$, and estimate the magnitude of the error by comparing your answer to that produced directly by a calculating utility.
7. Simplify the expression and state the values of $x$ for which your simplification is valid.  
   (a) $e^{-\ln x}$  
   (b) $e^{\ln x^2}$  
   (c) $\ln(e^{-x^2})$  
   (d) $\ln(1/e^x)$  
   (e) $\exp(3\ln x)$  
   (f) $\ln(xe^x)$  
   (g) $\ln(e^{x - \sqrt[3]{x}})$  
   (h) $e^{x - \ln x}$
8. (a) Let $f(x) = e^{-2x}$. Find the simplest exact value of the function $f(\ln 3)$.  
   (b) Let $f(x) = e^x + 3e^{-x}$. Find the simplest exact value of the function $f(\ln 2)$.

**9–10 Express the given quantity as a power of $e$.**
9. (a) $3^\pi$ (b) $2^{\sqrt{2}}$
10. (a) $\pi^{-x}$ (b) $x^{2x}, \; x > 0$

**11–12 Find the limits by making appropriate substitutions in the limits given in Theorem 6.6.8.**
11. (a) $\lim_{x \to +\infty}\left(1 + \frac{1}{2x}\right)^x$ (b) $\lim_{x \to 0}(1 + 2x)^{1/x}$
12. (a) $\lim_{x \to +\infty}\left(1 + \frac{3}{x}\right)^x$ (b) $\lim_{x \to 0}(1 + x)^{1/(3x)}$

**13–14 Find $g'(x)$ using Formula (18) and check your answer by evaluating the integral and then differentiating.**
13. $g(x) = \int_1^{x^3} (t^2 - t) dt$
14. $g(x) = \int_\pi^{1/x} (1 - \cos t) dt$

**15–16 Find the derivative using Formula (18), and check your answer by evaluating the integral and then differentiating the result.**
15. (a) $\frac{d}{dx}\int_1^{x^3} \frac{1}{t} dt$ (b) $\frac{d}{dx}\int_1^{\ln x} e^t dt$
16. (a) $\frac{d}{dx}\int_{-1}^{x^2} \sqrt{t + 1} dt$ (b) $\frac{d}{dx}\int_\pi^{1/x} \sin t dt$

17. Let $F(x) = \int_0^x \frac{\sin t}{t^2 + 1} dt$. Find (a) $F(0)$ (b) $F'(0)$ (c) $F''(0)$.
18. Let $F(x) = \int_2^x \sqrt{3t^2 + 1} dt$. Find (a) $F(2)$ (b) $F'(2)$ (c) $F''(2)$.

**19–22 True–False Determine whether the equation is true or false. Explain your answer.**
19. $\int_1^{1/a} \frac{1}{t} dt = -\int_1^a \frac{1}{t} dt$, for $0 < a$
20. $\int_1^{\sqrt{a}} \frac{1}{t} dt = \frac{1}{2}\int_1^a \frac{1}{t} dt$, for $0 < a$
21. $\int_{-1}^e \frac{1}{t} dt = 1$
22. $\int \frac{2x}{1 + x^2} dx = \int_1^{1 + x^2} \frac{1}{t} dt + C$

23. (a) Use Formula (18) to find $\frac{d}{dx}\int_1^{x^2} t\sqrt{1 + t} dt$.  
    (b) Use a CAS to evaluate the integral and differentiate the resulting function.  
    (c) Use the simplification command of the CAS, if necessary, to confirm that the answers in parts (a) and (b) are the same.
24. Show that  
    (a) $\frac{d}{dx}\int_x^a f(t) dt = -f(x)$  
    (b) $\frac{d}{dx}\int_{g(x)}^a f(t) dt = -f(g(x))g'(x)$.

**25–26 Use the results in Exercise 24 to find the derivative.**
25. (a) $\frac{d}{dx}\int_x^\pi \cos(t^3) dt$ (b) $\frac{d}{dx}\int_{\tan x}^3 \frac{t^2}{1 + t^2} dt$
26. (a) $\frac{d}{dx}\int_x^0 \frac{1}{(t^2 + 1)^2} dt$ (b) $\frac{d}{dx}\int_{1/x}^\pi \cos^3 t dt$

27. Find $\frac{d}{dx}\left[\int_{3x}^{x^2}\frac{t - 1}{t^2 + 1} dt\right]$ by writing $\int_{3x}^{x^2}\frac{t - 1}{t^2 + 1} dt = \int_{3x}^0 \frac{t - 1}{t^2 + 1} dt + \int_0^{x^2}\frac{t - 1}{t^2 + 1} dt$.
28. Use Exercise 24(b) and the idea in Exercise 27 to show that
    $$\frac{d}{dx}\int_{h(x)}^{g(x)} f(t) dt = f(g(x))g'(x) - f(h(x))h'(x)$$
29. Use the result obtained in Exercise 28 to perform the following differentiations:  
    (a) $\frac{d}{dx}\int_{x^2}^{x^3}\sin^2 t dt$  
    (b) $\frac{d}{dx}\int_{-x}^x \frac{1}{1 + t} dt$.
30. Prove that the function $F(x) = \int_x^{5x}\frac{1}{t} dt$ is constant on the interval $(0, +\infty)$ by using Exercise 28 to find $F'(x)$. What is that constant?

#### FOCUS ON CONCEPTS
31. Let $F(x) = \int_0^x f(t) dt$, where $f$ is the function whose graph is shown in Figure Ex-31.  
    (a) Find $F(0), F(3), F(5), F(7),$ and $F(10)$.  
    (b) On what subintervals of the interval $[0, 10]$ is $F$ increasing? Decreasing?  
    (c) Where does $F$ have its maximum value? Its minimum value?  
    (d) Sketch the graph of $F$.
32. Determine the inflection point(s) for the graph of $F$ in Exercise 31.

**33–34 Express $F(x)$ in a piecewise form that does not involve an integral.**
33. $F(x) = \int_{-1}^x |t| dt$
34. $F(x) = \int_0^x f(t) dt$, where $f(x) = \begin{cases} x, & 0 \le x \le 2 \\ 2, & x > 2 \end{cases}$

**35–38 Use Formula (11) to solve the initial-value problem.**
35. $\frac{dy}{dx} = \frac{2x^2 + 1}{x}, \; y(1) = 2$
36. $\frac{dy}{dx} = \frac{x + 1}{\sqrt{x}}, \; y(1) = 0$
37. $\frac{dy}{dx} = \sec^2 x - \sin x, \; y(\pi/4) = 1$
38. $\frac{dy}{dx} = \frac{1}{x\ln x}, \; y(e) = 1$

39. Suppose that at time $t = 0$ there are $P_0$ individuals who have disease X, and suppose that a certain model for the spread of the disease predicts that the disease will spread at the rate of $r(t)$ individuals per day. Write a formula for the number of individuals who will have disease X after $x$ days.
40. Suppose that $v(t)$ is the velocity function of a particle moving along an $s$-axis. Write a formula for the coordinate of the particle at time $T$ if the particle is at $s_1$ at time $t = 1$.

#### FOCUS ON CONCEPTS
41. The accompanying figure shows the graphs of $y = f(x)$ and $y = \int_0^x f(t) dt$. Determine which graph is which, and explain your reasoning.
42. (a) Make a conjecture about the value of the limit $\lim_{k \to 0}\int_1^b t^{k-1} dt \; (b > 0)$.  
    (b) Check your conjecture by evaluating the integral and finding the limit. [*Hint:* Interpret the limit as the definition of the derivative of an exponential function.]
43. Let $F(x) = \int_0^x f(t) dt$, where $f$ is the function graphed in Figure Ex-43.  
    (a) Where do the relative minima of $F$ occur?  
    (b) Where do the relative maxima of $F$ occur?  
    (c) Where does the absolute maximum of $F$ on the interval $[0, 5]$ occur?  
    (d) Where does the absolute minimum of $F$ on the interval $[0, 5]$ occur?  
    (e) Where is $F$ concave up? Concave down?  
    (f) Sketch the graph of $F$.
44. CAS programs have commands for working with most of the important nonelementary functions. Check your CAS documentation for information about the error function $\text{erf}(x)$ [see Formula (12)], and then complete the following.  
    (a) Generate the graph of $\text{erf}(x)$.  
    (b) Use the graph to make a conjecture about the existence and location of any relative maxima and minima of $\text{erf}(x)$.  
    (c) Check your conjecture in part (b) using the derivative of $\text{erf}(x)$.  
    (d) Use the graph to make a conjecture about the existence and location of any inflection points of $\text{erf}(x)$.  
    (e) Check your conjecture in part (d) using the second derivative of $\text{erf}(x)$.  
    (f) Use the graph to make a conjecture about the existence of horizontal asymptotes of $\text{erf}(x)$.  
    (g) Check your conjecture in part (f) by using the CAS to find the limits of $\text{erf}(x)$ as $x \to \pm\infty$.
45. The Fresnel sine and cosine functions $S(x)$ and $C(x)$ were defined in Formulas (13) and (14) and graphed in Figure 6.6.4. Their derivatives were given in Formulas (15) and (16).  
    (a) At what points does $C(x)$ have relative minima? Relative maxima?  
    (b) Where do the inflection points of $C(x)$ occur?  
    (c) Confirm that your answers in parts (a) and (b) are consistent with the graph of $C(x)$.
46. Find the limit $\lim_{h \to 0}\frac{1}{h}\int_x^{x+h}\ln t \, dt$.
47. Find a function $f$ and a number $a$ such that $4 + \int_a^x f(t) dt = e^{2x}$.
48. (a) Give a geometric argument to show that $\frac{1}{x + 1} < \int_x^{x+1}\frac{1}{t} dt < \frac{1}{x}, \; x > 0$.  
    (b) Use the result in part (a) to prove that $\frac{1}{x + 1} < \ln\left(1 + \frac{1}{x}\right) < \frac{1}{x}, \; x > 0$.  
    (c) Use the result in part (b) to prove that $e^{x/(x+1)} < \left(1 + \frac{1}{x}\right)^x < e, \; x > 0$ and hence that $\lim_{x \to +\infty}\left(1 + \frac{1}{x}\right)^x = e$.  
    (d) Use the result in part (b) to prove that $\left(1 + \frac{1}{x}\right)^x < e < \left(1 + \frac{1}{x}\right)^{x+1}, \; x > 0$.
49. Use a graphing utility to generate the graph of $y = \left(1 + \frac{1}{x}\right)^{x+1} - \left(1 + \frac{1}{x}\right)^x$ in the window $[0, 100] \times [0, 0.2]$, and use that graph and part (d) of Exercise 48 to make a rough estimate of the error in the approximation $e \approx \left(1 + \frac{1}{50}\right)^{50}$.
50. (a) Divide the interval $[1, 2]$ into 5 subintervals of equal length, and use approximate Riemann sums to show that
    $$0.2\left[\frac{1}{1.2} + \frac{1}{1.4} + \frac{1}{1.6} + \frac{1}{1.8} + \frac{1}{2.0}\right] < \ln 2 < 0.2\left[\frac{1}{1.0} + \frac{1}{1.2} + \frac{1}{1.4} + \frac{1}{1.6} + \frac{1}{1.8}\right]$$
    (b) Show that if the interval $[1, 2]$ is divided into $n$ subintervals of equal length, then
    $$\sum_{k=1}^n \frac{1}{n + k} < \ln 2 < \sum_{k=0}^{n-1} \frac{1}{n + k}$$
    (c) Show that the difference between the two sums in part (b) is $1/(2n)$, and use this result to show that the sums in part (a) approximate $\ln 2$ with an error of at most 0.1.  
    (d) How large must $n$ be to ensure that the sums in part (b) approximate $\ln 2$ to three decimal places?
51. Prove: If $f$ is continuous on an open interval and $a$ is any point in that interval, then $F(x) = \int_a^x f(t) dt$ is continuous on the interval.
52. **Writing.** A student objects that it is circular reasoning to make the definition $\ln x = \int_1^x \frac{1}{t} dt$ since to evaluate the integral we need to know the value of $\ln x$. Write a short paragraph that answers this student’s objection.
53. **Writing.** Write a short paragraph that compares Definition 6.6.1 with the definition of the natural logarithm function given in Section 6.1. Be sure to discuss the issues surrounding continuity and differentiability.

---

## 6.7 DERIVATIVES AND INTEGRALS INVOLVING INVERSE TRIGONOMETRIC FUNCTIONS

### INVERSE TRIGONOMETRIC FUNCTIONS
To create invertible functions, the domains of trigonometric functions are restricted:
* $\sin^{-1} x$: Domain $[-1, 1]$, Range $[-\pi/2, \pi/2]$
* $\cos^{-1} x$: Domain $[-1, 1]$, Range $[0, \pi]$
* $\tan^{-1} x$: Domain $(-\infty, +\infty)$, Range $(-\pi/2, \pi/2)$
* $\sec^{-1} x$: Domain $(-\infty, -1] \cup [1, +\infty)$, Range $[0, \pi/2) \cup (\pi/2, \pi]$

#### Table 6.7.1: Properties of Inverse Trigonometric Functions
| FUNCTION | DOMAIN | RANGE | BASIC RELATIONSHIPS |
| :--- | :--- | :--- | :--- |
| $\sin^{-1}$ | $[-1, 1]$ | $[-\pi/2, \pi/2]$ | $\sin^{-1}(\sin x) = x \text{ for } -\pi/2 \le x \le \pi/2$; $\sin(\sin^{-1} x) = x \text{ for } -1 \le x \le 1$ |
| $\cos^{-1}$ | $[-1, 1]$ | $[0, \pi]$ | $\cos^{-1}(\cos x) = x \text{ for } 0 \le x \le \pi$; $\cos(\cos^{-1} x) = x \text{ for } -1 \le x \le 1$ |
| $\tan^{-1}$ | $(-\infty, +\infty)$ | $(-\pi/2, \pi/2)$ | $\tan^{-1}(\tan x) = x \text{ for } -\pi/2 < x < \pi/2$; $\tan(\tan^{-1} x) = x \text{ for } -\infty < x < +\infty$ |
| $\sec^{-1}$ | $(-\infty, -1] \cup [1, +\infty)$ | $[0, \pi/2) \cup (\pi/2, \pi]$ | $\sec^{-1}(\sec x) = x \text{ for } 0 \le x \le \pi, x \neq \pi/2$; $\sec(\sec^{-1} x) = x \text{ for } |x| \ge 1$ |

Useful identities:
$$\sin^{-1} x + \cos^{-1} x = \frac{\pi}{2}, \quad \cos(\sin^{-1} x) = \sqrt{1 - x^2}, \quad \sin(\cos^{-1} x) = \sqrt{1 - x^2}, \quad \tan(\sin^{-1} x) = \frac{x}{\sqrt{1 - x^2}}$$
$$\sec(\tan^{-1} x) = \sqrt{1 + x^2}, \quad \sin(\sec^{-1} x) = \frac{\sqrt{x^2 - 1}}{x} \ (x \ge 1)$$

---

### DERIVATIVE FORMULAS
$$\frac{d}{dx}[\sin^{-1} u] = \frac{1}{\sqrt{1 - u^2}}\frac{du}{dx}, \quad \frac{d}{dx}[\cos^{-1} u] = -\frac{1}{\sqrt{1 - u^2}}\frac{du}{dx} \tag{14–15}$$
$$\frac{d}{dx}[\tan^{-1} u] = \frac{1}{1 + u^2}\frac{du}{dx}, \quad \frac{d}{dx}[\cot^{-1} u] = -\frac{1}{1 + u^2}\frac{du}{dx} \tag{16–17}$$
$$\frac{d}{dx}[\sec^{-1} u] = \frac{1}{|u|\sqrt{u^2 - 1}}\frac{du}{dx}, \quad \frac{d}{dx}[\csc^{-1} u] = -\frac{1}{|u|\sqrt{u^2 - 1}}\frac{du}{dx} \tag{18–19}$$

---

### INTEGRATION FORMULAS
$$\int \frac{du}{\sqrt{a^2 - u^2}} = \sin^{-1}\frac{u}{a} + C \tag{24}$$
$$\int \frac{du}{a^2 + u^2} = \frac{1}{a}\tan^{-1}\frac{u}{a} + C \tag{23}$$
$$\int \frac{du}{u\sqrt{u^2 - a^2}} = \frac{1}{a}\sec^{-1}\frac{|u|}{a} + C \tag{25}$$

---

### QUICK CHECK EXERCISES 6.7
*(See page 472 for answers.)*

1. Exact values: (a) $\sin^{-1}(-1) = -\pi/2$ (b) $\tan^{-1}(1) = \pi/4$ (c) $\sin^{-1}(\frac{1}{2}\sqrt{3}) = \pi/3$ (d) $\cos^{-1}(1/2) = \pi/3$ (e) $\sec^{-1}(-2) = 2\pi/3$.
2. Exact values: (a) $\sin^{-1}(\sin \pi/7) = \pi/7$ (b) $\sin^{-1}(\sin 5\pi/7) = 2\pi/7$ (c) $\tan^{-1}(\tan 13\pi/6) = \pi/6$ (d) $\cos^{-1}(\cos 12\pi/7) = 2\pi/7$.
3. $\frac{d}{dx}[\sin^{-1}(2x)] = \frac{2}{\sqrt{1 - 4x^2}}$.
4. $\int_{-1/2}^{1/2} \frac{1}{\sqrt{1 - x^2}} dx = \pi/3$.

#### QUICK CHECK ANSWERS 6.7
1. (a) $-\pi/2$ (b) $\pi/4$ (c) $\pi/3$ (d) $\pi/3$ (e) $2\pi/3$  
2. (a) $\pi/7$ (b) $2\pi/7$ (c) $\pi/6$ (d) $2\pi/7$  
3. $\frac{2}{\sqrt{1 - 4x^2}}$  
4. $\pi/3$

---

### EXERCISE SET 6.7

1. Given that $\theta = \tan^{-1}\left(\frac{4}{3}\right)$, find the exact values of $\sin\theta, \cos\theta, \cot\theta, \sec\theta,$ and $\csc\theta$.
2. Given that $\theta = \sec^{-1} 2.6$, find the exact values of $\sin\theta, \cos\theta, \tan\theta, \cot\theta,$ and $\csc\theta$.
3. For which values of $x$ is it true that  
   (a) $\cos^{-1}(\cos x) = x$  
   (b) $\cos(\cos^{-1} x) = x$  
   (c) $\tan^{-1}(\tan x) = x$  
   (d) $\tan(\tan^{-1} x) = x$?

**4–5 Find the exact value of the given quantity.**
4. $\sec\left[\sin^{-1}\left(-\frac{3}{4}\right)\right]$
5. $\sin\left[2\cos^{-1}\left(\frac{3}{5}\right)\right]$

**6–7 Complete the identities using the triangle method (Figure 6.7.3).**
6. (a) $\sin(\cos^{-1} x) = {?}$ (b) $\tan(\cos^{-1} x) = {?}$  
   (c) $\csc(\tan^{-1} x) = {?}$ (d) $\sin(\tan^{-1} x) = {?}$
7. (a) $\cos(\tan^{-1} x) = {?}$ (b) $\tan(\cos^{-1} x) = {?}$  
   (c) $\sin(\sec^{-1} x) = {?}$ (d) $\cot(\sec^{-1} x) = {?}$

8. (a) Use a calculating utility set to radian measure to make tables of values of $y = \sin^{-1} x$ and $y = \cos^{-1} x$ for $x = -1, -0.8, -0.6, \dots, 0, 0.2, \dots, 1$. Round your answers to two decimal places.  
   (b) Plot the points obtained in part (a), and use the points to sketch the graphs of $y = \sin^{-1} x$ and $y = \cos^{-1} x$. Confirm that your sketches agree with those in Figure 6.7.1.  
   (c) Use your graphing utility to graph $y = \sin^{-1} x$ and $y = \cos^{-1} x$; confirm that the graphs agree with those in Figure 6.7.1.

9. In each part, sketch the graph and check your work with a graphing utility.  
   (a) $y = \sin^{-1} 2x$ (b) $y = \tan^{-1}\frac{1}{2}x$

10. The law of cosines states that $c^2 = a^2 + b^2 - 2ab\cos\theta$ where $a, b,$ and $c$ are the lengths of the sides of a triangle and $\theta$ is the angle formed by sides $a$ and $b$. Find $\theta$, to the nearest degree, for the triangle with $a = 2, b = 3,$ and $c = 4$.

**11–12 Use a calculating utility to approximate the solution of each equation. Where radians are used, express your answer to four decimal places, and where degrees are used, express it to the nearest tenth of a degree. [Note: In each part, the solution is not in the range of the relevant inverse trigonometric function.]**
11. (a) $\sin x = 0.37, \; \pi/2 < x < \pi$  
    (b) $\sin\theta = -0.61, \; 180^\circ < \theta < 270^\circ$
12. (a) $\cos x = -0.85, \; \pi < x < 3\pi/2$  
    (b) $\cos\theta = 0.23, \; -90^\circ < \theta < 0^\circ$

#### FOCUS ON CONCEPTS
13. (a) Use a calculating utility to evaluate the expressions $\sin^{-1}(\sin^{-1} 0.25)$ and $\sin^{-1}(\sin^{-1} 0.9)$, and explain what you think is happening in the second calculation.  
    (b) For what values of $x$ in the interval $-1 \le x \le 1$ will your calculating utility produce a real value for the function $\sin^{-1}(\sin^{-1} x)$?
14. A soccer player kicks a ball with an initial speed of $14\text{ m/s}$ at an angle $\theta$ with the horizontal (see Figure Ex-14). The ball lands $18\text{ m}$ down the field. If air resistance is neglected, then the ball will have a parabolic trajectory and the horizontal range $R$ will be given by
    $$R = \frac{v^2}{g}\sin 2\theta$$
    where $v$ is the initial speed of the ball and $g$ is the acceleration due to gravity. Using $g = 9.8\text{ m/s}^2$, approximate two values of $\theta$, to the nearest degree, at which the ball could have been kicked. Which angle results in the shorter time of flight? Why?

**15–26 Find $dy/dx$.**
15. $y = \sin^{-1}(3x)$
16. $y = \cos^{-1}\left(\frac{x + 1}{2}\right)$
17. $y = \sin^{-1}(1/x)$
18. $y = \cos^{-1}(\cos x)$
19. $y = \tan^{-1}(x^3)$
20. $y = \sec^{-1}(x^5)$
21. $y = (\tan x)^{-1}$
22. $y = \frac{1}{\tan^{-1} x}$
23. $y = e^x \sec^{-1} x$
24. $y = \ln(\cos^{-1} x)$
25. $y = \sin^{-1} x + \cos^{-1} x$
26. $y = x^2(\sin^{-1} x)^3$

**27–28 Find $dy/dx$ by implicit differentiation.**
27. $x^3 + x\tan^{-1} y = e^y$
28. $\sin^{-1}(xy) = \cos^{-1}(x - y)$

**29–30 Evaluate the integral and check your answer by differentiating.**
29. $\int \left[\frac{1}{2\sqrt{1 - x^2}} - \frac{3}{1 + x^2}\right] dx$
30. $\int \left[\frac{4}{x\sqrt{x^2 - 1}} + \frac{1 + x + x^3}{1 + x^2}\right] dx$

**31–48 Evaluate the integral.**
31. $\int \frac{dx}{\sqrt{1 - 4x^2}}$
32. $\int \frac{dx}{1 + 16x^2}$
33. $\int \frac{e^x}{1 + e^{2x}} dx$
34. $\int \frac{t}{t^4 + 1} dt$
35. $\int \frac{\sec^2 x \, dx}{\sqrt{1 - \tan^2 x}}$
36. $\int \frac{\sin\theta}{\cos^2\theta + 1} d\theta$
37. $\int_0^{1/\sqrt{2}}\frac{dx}{\sqrt{1 - x^2}}$
38. $\int_{-1}^1 \frac{dx}{1 + x^2}$
39. $\int_{\sqrt{2}}^2 \frac{dx}{x\sqrt{x^2 - 1}}$
40. $\int_{-\sqrt{2}}^{-2/\sqrt{3}}\frac{dx}{x\sqrt{x^2 - 1}}$
41. $\int_1^{\sqrt{3}}\frac{\sqrt{\tan^{-1} x}}{1 + x^2} dx$
42. $\int_1^{\sqrt{e}}\frac{dx}{x\sqrt{1 - (\ln x)^2}}$
43. $\int_1^3 \frac{dx}{\sqrt{x}(x + 1)}$
44. $\int_{\ln 2}^{\ln(2/\sqrt{3})}\frac{e^{-x} dx}{\sqrt{1 - e^{-2x}}}$
45. $\int_0^1 \frac{x}{\sqrt{4 - 3x^4}} dx$
46. $\int_1^2 \frac{1}{\sqrt{x}\sqrt{4 - x}} dx$
47. $\int_0^{1/\sqrt{3}}\frac{1}{1 + 9x^2} dx$
48. $\int_1^{\sqrt{2}}\frac{x}{3 + x^4} dx$

**49–50 Evaluate the integrals with the aid of Formulas (23), (24), and (25).**
49. (a) $\int \frac{dx}{\sqrt{9 - x^2}}$ (b) $\int \frac{dx}{5 + x^2}$ (c) $\int \frac{dx}{x\sqrt{x^2 - \pi}}$
50. (a) $\int \frac{e^x}{4 + e^{2x}} dx$ (b) $\int \frac{dx}{\sqrt{9 - 4x^2}}$ (c) $\int \frac{dy}{y\sqrt{5y^2 - 3}}$

**51–54 True–False Determine whether the statement is true or false. Explain your answer.**
51. By definition, $\sin^{-1}(\sin x) = x$ for all real numbers $x$.
52. The range of the inverse tangent function is the interval $-\frac{1}{2}\pi \le y \le \frac{1}{2}\pi$.
53. The graph of $y = \sec^{-1} x$ has a horizontal asymptote.
54. We can conclude from the derivatives of $\sin^{-1} x$ and $\cos^{-1} x$ that $\sin^{-1} x + \cos^{-1} x$ is constant.

#### FOCUS ON CONCEPTS
**55–56 The function $\cot^{-1} x$ is defined to be the inverse of the restricted cotangent function $\cot x, \; 0 < x < \pi$ and the function $\csc^{-1} x$ is defined to be the inverse of the restricted cosecant function $\csc x, \; -\pi/2 \le x \le \pi/2, \; x \neq 0$. Use these definitions in these and in all subsequent exercises that involve these functions.**
55. (a) Sketch the graphs of $\cot^{-1} x$ and $\csc^{-1} x$.  
    (b) Find the domain and range of $\cot^{-1} x$ and $\csc^{-1} x$.
56. Show that  
    (a) $\cot^{-1} x = \begin{cases} \tan^{-1}(1/x), & \text{if } x > 0 \\ \pi + \tan^{-1}(1/x), & \text{if } x < 0 \end{cases}$  
    (b) $\sec^{-1} x = \cos^{-1}(1/x)$, if $|x| \ge 1$  
    (c) $\csc^{-1} x = \sin^{-1}(1/x)$, if $|x| \ge 1$.
57. Most scientific calculators have keys for the values of only $\sin^{-1} x, \cos^{-1} x,$ and $\tan^{-1} x$. The formulas in Exercise 56 show how a calculator can be used to obtain values of $\cot^{-1} x, \sec^{-1} x,$ and $\csc^{-1} x$ for positive values of $x$. Use these formulas and a calculator to find numerical values for each of the following inverse trigonometric functions. Express your answers in degrees, rounded to the nearest tenth of a degree.  
    (a) $\cot^{-1} 0.7$ (b) $\sec^{-1} 1.2$ (c) $\csc^{-1} 2.3$
58. A camera is positioned $x$ feet from the base of a missile launching pad (see Figure Ex-58). If a missile of length $a$ feet is launched vertically, show that when the base of the missile is $b$ feet above the camera lens, the angle $\theta$ subtended at the lens by the missile is
    $$\theta = \cot^{-1}\left(\frac{x}{a + b}\right) - \cot^{-1}\left(\frac{x}{b}\right)$$
59. Use identity (5) and Formula (14) to obtain the derivative of $y = \cos^{-1} x$.
60. (a) Use Formula (2) in Section 6.3 to prove that $\left.\frac{d}{dx}[\cot^{-1} x]\right|_{x=0} = -1$.  
    (b) Use part (a) above, part (a) of Exercise 56 and the chain rule to show that $\frac{d}{dx}[\cot^{-1} x] = -\frac{1}{1 + x^2}$ for $-\infty < x < +\infty$.  
    (c) Conclude from part (b) that $\frac{d}{dx}[\cot^{-1} u] = -\frac{1}{1 + u^2}\frac{du}{dx}$ for $-\infty < u < +\infty$.
61. (a) Use part (c) of Exercise 56 and the chain rule to show that $\frac{d}{dx}[\csc^{-1} x] = -\frac{1}{|x|\sqrt{x^2 - 1}}$ for $1 < |x|$.  
    (b) Conclude from part (a) that $\frac{d}{dx}[\csc^{-1} u] = -\frac{1}{|u|\sqrt{u^2 - 1}}\frac{du}{dx}$ for $1 < |u|$.  
    (c) Use Equation (5) and parts (b) and (c) of Exercise 56 to show that if $|x| \ge 1$ then, $\sec^{-1} x + \csc^{-1} x = \pi/2$. Conclude from part (a) that $\frac{d}{dx}[\sec^{-1} x] = \frac{1}{|x|\sqrt{x^2 - 1}}$.  
    (d) Conclude from part (c) that $\frac{d}{dx}[\sec^{-1} u] = \frac{1}{|u|\sqrt{u^2 - 1}}\frac{du}{dx}$.
62. Use the derivative formula from part (d) of Exercise 61 to verify Formula (22).

**63–66 Find $dy/dx$.**
63. $y = \sec^{-1} x + \csc^{-1} x$
64. $y = \csc^{-1}(e^x)$
65. $y = \cot^{-1}(\sqrt{x})$
66. $y = \sqrt{\cot^{-1} x}$

67. The number of hours of daylight on a given day at a given point on the Earth’s surface depends on the latitude $\lambda$ of the point, the angle $\gamma$ through which the Earth has moved in its orbital plane during the time period from the vernal equinox (March 21), and the angle of inclination $\phi$ of the Earth’s axis of rotation measured from ecliptic north ($\phi \approx 23.45^\circ$). The number of hours of daylight $h$ can be approximated by the formula
    $$h = \begin{cases} 24, & D \ge 1 \\ 12 + \frac{2}{15}\sin^{-1} D, & |D| < 1 \\ 0, & D \le -1 \end{cases}$$
    where $D = \frac{\sin\phi \sin\gamma \tan\lambda}{\sqrt{1 - \sin^2\phi \sin^2\gamma}}$ and $\sin^{-1} D$ is in degree measure. Given that Fairbanks, Alaska, is located at a latitude of $\lambda = 65^\circ\text{ N}$ and also that $\gamma = 90^\circ$ on June 20 and $\gamma = 270^\circ$ on December 20, approximate:  
    (a) the maximum number of daylight hours at Fairbanks to one decimal place  
    (b) the minimum number of daylight hours at Fairbanks to one decimal place.
68. An Earth-observing satellite has horizon sensors that can measure the angle $\theta$ shown in Figure Ex-68. Let $R$ be the radius of the Earth (assumed spherical) and $h$ the distance between the satellite and the Earth’s surface.  
    (a) Show that $\sin\theta = \frac{R}{R + h}$.  
    (b) Find $\theta$, to the nearest degree, for a satellite that is $10,000\text{ km}$ from the Earth’s surface (use $R = 6378\text{ km}$).
69. An airplane is flying at a constant height of $3000\text{ ft}$ above water at a speed of $400\text{ ft/s}$. The pilot is to release a survival package so that it lands in the water at a sighted point $P$. If air resistance is neglected, then the package will follow a parabolic trajectory whose equation relative to the coordinate system in Figure Ex-69 is
    $$y = 3000 - \frac{g}{2v^2}x^2$$
    where $g$ is the acceleration due to gravity and $v$ is the speed of the airplane. Using $g = 32\text{ ft/s}^2$, find the “line of sight” angle $\theta$, to the nearest degree, that will result in the package hitting the target point.
70. Sketch the region enclosed by the curves $y = \frac{1}{\sqrt{1 - x^2}}$ and $y = 2$ and find the area of this region.
71. Estimate the value of $k \; (0 < k < 1)$ so that the region enclosed by $y = 1/\sqrt{1 - x^2}, \; y = x, \; x = 0,$ and $x = k$ has an area of 1 square unit.
72. Estimate the area of the region in the first quadrant enclosed by $y = \sin 2x$ and $y = \sin^{-1} x$.
73. Find the volume of the solid that results when the region enclosed by the curves $y = 1/\sqrt{4 + x^2}, \; x = -2, \; x = 2,$ and $y = 0$ is revolved about the $x$-axis.
74. Use a CAS to estimate the volume of the solid that results when the region enclosed by the curves $y = x\sqrt{\tan^{-1} x}$ and $y = x$ is revolved about the $x$-axis.
75. Consider the region enclosed by $y = \sin^{-1} x, \; y = 0,$ and $x = 1$. Find the volume of the solid generated by revolving the region about the $x$-axis using (a) disks (b) cylindrical shells.
76. (a) Find the volume $V$ of the solid generated when the region bounded by $y = 1/(1 + x^4), \; y = 0, \; x = 1,$ and $x = b \; (b > 1)$ is revolved about the $y$-axis.  
    (b) Find $\lim_{b \to +\infty} V$.

**77–79 Find the average value of the function over the given interval.**
77. $f(x) = \frac{1}{1 + x^2}; \; [1, \sqrt{3}]$
78. $f(x) = \frac{1}{\sqrt{1 - x^2}}; \; \left[-\frac{1}{2}, 0\right]$
79. $f(x) = \frac{e^{3x}}{1 + e^{6x}}; \; \left[-\frac{\ln 3}{6}, 0\right]$

80. Find a positive value of $k$ such that the average value of $f(x) = 1/(k^2 + x^2)$ over the interval $[-k, k]$ is $\pi$.

**81–83 Solve the initial-value problems.**
81. $\frac{dy}{dt} = \frac{3}{\sqrt{1 - t^2}}, \; y\left(\frac{\sqrt{3}}{2}\right) = 0$
82. $\frac{dy}{dx} = \frac{x^2 - 1}{x^2 + 1}, \; y(1) = \frac{\pi}{2}$
83. $\frac{dy}{dt} = \frac{1}{25 + 9t^2}, \; y\left(-\frac{5}{3}\right) = \frac{\pi}{30}$

84. Evaluate the limit by interpreting it as a Riemann sum in which the interval $[0, 1]$ is divided into $n$ subintervals of equal width:
    $$\lim_{n \to +\infty}\sum_{k=1}^n \frac{n}{n^2 + k^2}$$
85. Prove:  
    (a) $\sin^{-1}(-x) = -\sin^{-1} x$  
    (b) $\tan^{-1}(-x) = -\tan^{-1} x$.
86. Prove:  
    (a) $\cos^{-1}(-x) = \pi - \cos^{-1} x$  
    (b) $\sec^{-1}(-x) = \pi - \sec^{-1} x$.
87. Use the Mean-Value Theorem to prove that $\frac{x}{1 + x^2} < \tan^{-1} x < x \; (x > 0)$.
88. Prove:  
    (a) $\sin^{-1} x = \tan^{-1}\left(\frac{x}{\sqrt{1 - x^2}}\right) \quad (|x| < 1)$  
    (b) $\cos^{-1} x = \frac{\pi}{2} - \tan^{-1}\left(\frac{x}{\sqrt{1 - x^2}}\right) \quad (|x| < 1)$.
89. Prove: $\tan^{-1} x + \tan^{-1} y = \tan^{-1}\left(\frac{x + y}{1 - xy}\right)$ provided $-\pi/2 < \tan^{-1} x + \tan^{-1} y < \pi/2$. [*Hint:* Use an identity for $\tan(\alpha + \beta)$.]
90. Use the result in Exercise 89 to show that  
    (a) $\tan^{-1}\frac{1}{2} + \tan^{-1}\frac{1}{3} = \frac{\pi}{4}$  
    (b) $2\tan^{-1}\frac{1}{3} + \tan^{-1}\frac{1}{7} = \frac{\pi}{4}$.
91. Use identities (4) and (7) to obtain identity (11).
92. **Writing.** Suppose that $f$ is a nonconstant function that is twice-differentiable everywhere. Is it always possible to restrict the domain of $f$ to an open interval so that the restricted function has an inverse? Justify your answer by appealing to appropriate theorems.
93. **Writing.** Let $\theta = \tan^{-1}(-3/4)$ and explain why the triangle in Figure Ex-93 may be used to evaluate $\sin\theta$ and $\cos\theta$. More generally, suppose that $q$ denotes a rational number and that $\theta = \tan^{-1} q$ or that $\theta = \sin^{-1} q$. Find right triangles, with at least two sides labeled by integers, that may be used to evaluate $\sin\theta$ and $\cos\theta$.

---

## 6.8 HYPERBOLIC FUNCTIONS AND HANGING CABLES

### DEFINITIONS OF HYPERBOLIC FUNCTIONS

> **6.8.1 DEFINITION**  
> * Hyperbolic sine: $\sinh x = \frac{e^x - e^{-x}}{2}$  
> * Hyperbolic cosine: $\cosh x = \frac{e^x + e^{-x}}{2}$  
> * Hyperbolic tangent: $\tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$  
> * Hyperbolic cotangent: $\coth x = \frac{\cosh x}{\sinh x} = \frac{e^x + e^{-x}}{e^x - e^{-x}}$  
> * Hyperbolic secant: $\text{sech } x = \frac{1}{\cosh x} = \frac{2}{e^x + e^{-x}}$  
> * Hyperbolic cosecant: $\text{csch } x = \frac{1}{\sinh x} = \frac{2}{e^x - e^{-x}}$

---

### HYPERBOLIC IDENTITIES

> **6.8.2 THEOREM**  
> * $\cosh x + \sinh x = e^x, \quad \cosh x - \sinh x = e^{-x}$  
> * $\cosh^2 x - \sinh^2 x = 1$  
> * $1 - \tanh^2 x = \text{sech}^2 x, \quad \coth^2 x - 1 = \text{csch}^2 x$  
> * $\cosh(-x) = \cosh x, \quad \sinh(-x) = -\sinh x$  
> * $\sinh(x \pm y) = \sinh x\cosh y \pm \cosh x\sinh y$  
> * $\cosh(x \pm y) = \cosh x\cosh y \pm \sinh x\sinh y$  
> * $\sinh 2x = 2\sinh x\cosh x$  
> * $\cosh 2x = \cosh^2 x + \sinh^2 x = 2\sinh^2 x + 1 = 2\cosh^2 x - 1$

---

### DERIVATIVE AND INTEGRAL FORMULAS

> **6.8.3 THEOREM**  
> * $\frac{d}{dx}[\sinh u] = \cosh u \frac{du}{dx} \quad \Longleftrightarrow \quad \int \cosh u du = \sinh u + C$  
> * $\frac{d}{dx}[\cosh u] = \sinh u \frac{du}{dx} \quad \Longleftrightarrow \quad \int \sinh u du = \cosh u + C$  
> * $\frac{d}{dx}[\tanh u] = \text{sech}^2 u \frac{du}{dx} \quad \Longleftrightarrow \quad \int \text{sech}^2 u du = \tanh u + C$  
> * $\frac{d}{dx}[\coth u] = -\text{csch}^2 u \frac{du}{dx} \quad \Longleftrightarrow \quad \int \text{csch}^2 u du = -\coth u + C$  
> * $\frac{d}{dx}[\text{sech } u] = -\text{sech } u\tanh u \frac{du}{dx} \quad \Longleftrightarrow \quad \int \text{sech } u\tanh u du = -\text{sech } u + C$  
> * $\frac{d}{dx}[\text{csch } u] = -\text{csch } u\coth u \frac{du}{dx} \quad \Longleftrightarrow \quad \int \text{csch } u\coth u du = -\text{csch } u + C$

---

### INVERSE HYPERBOLIC FUNCTIONS AND LOGARITHMIC FORMS

> **6.8.4 THEOREM**  
> * $\sinh^{-1} x = \ln(x + \sqrt{x^2 + 1})$  
> * $\cosh^{-1} x = \ln(x + \sqrt{x^2 - 1}) \quad (x \ge 1)$  
> * $\tanh^{-1} x = \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right) \quad (|x| < 1)$  
> * $\coth^{-1} x = \frac{1}{2}\ln\left(\frac{x + 1}{x - 1}\right) \quad (|x| > 1)$  
> * $\text{sech}^{-1} x = \ln\left(\frac{1 + \sqrt{1 - x^2}}{x}\right) \quad (0 < x \le 1)$  
> * $\text{csch}^{-1} x = \ln\left(\frac{1}{x} + \frac{\sqrt{1 + x^2}}{|x|}\right) \quad (x \neq 0)$

---

### QUICK CHECK EXERCISES 6.8
*(See page 483 for answers.)*

1. $\cosh x = \frac{e^x + e^{-x}}{2}, \sinh x = \frac{e^x - e^{-x}}{2}, \tanh x = \frac{e^x - e^{-x}}{e^x + e^{-x}}$.
2. Domains and ranges of hyperbolic functions.
3. Unit hyperbola $x^2 - y^2 = 1$.
4. Derivatives: $\sinh x, \cosh x, \text{sech}^2 x$.
5. Integrals: $\sinh x + C, \cosh x + C, \ln(\cosh x) + C$.
6. Inverse derivatives: $\frac{1}{\sqrt{x^2 - 1}}, \frac{1}{\sqrt{1 + x^2}}, \frac{1}{1 - x^2}$.

#### QUICK CHECK ANSWERS 6.8
1. $\frac{e^x + e^{-x}}{2}; \; \frac{e^x - e^{-x}}{2}; \; \frac{e^x - e^{-x}}{e^x + e^{-x}}$  
2. See Table 6.8.1 in text.  
3. unit hyperbola; $x^2 - y^2 = 1$  
4. $\sinh x; \; \cosh x; \; \text{sech}^2 x$  
5. $\sinh x + C; \; \cosh x + C; \; \ln(\cosh x) + C$  
6. $\frac{1}{\sqrt{x^2 - 1}}; \; \frac{1}{\sqrt{1 + x^2}}; \; \frac{1}{1 - x^2}$

---

### EXERCISE SET 6.8

**1–2 Approximate the expression to four decimal places.**
1. (a) $\sinh 3$ (b) $\cosh(-2)$ (c) $\tanh(\ln 4)$  
   (d) $\sinh^{-1}(-2)$ (e) $\cosh^{-1} 3$ (f) $\tanh^{-1}\frac{3}{4}$
2. (a) $\text{csch}(-1)$ (b) $\text{sech}(\ln 2)$ (c) $\coth 1$  
   (d) $\text{sech}^{-1}\frac{1}{2}$ (e) $\coth^{-1} 3$ (f) $\text{csch}^{-1}(-\sqrt{3})$

**3. Find the exact numerical value of each expression.**  
(a) $\sinh(\ln 3)$ (b) $\cosh(-\ln 2)$  
(c) $\tanh(2\ln 5)$ (d) $\sinh(-3\ln 2)$

**4. In each part, rewrite the expression as a ratio of polynomials.**  
(a) $\cosh(\ln x)$ (b) $\sinh(\ln x)$  
(c) $\tanh(2\ln x)$ (d) $\cosh(-\ln x)$

**5. In each part, a value for one of the hyperbolic functions is given at an unspecified positive number $x_0$. Use appropriate identities to find the exact values of the remaining five hyperbolic functions at $x_0$.**  
(a) $\sinh x_0 = 2$ (b) $\cosh x_0 = 5/4$ (c) $\tanh x_0 = 4/5$

6. Obtain the derivative formulas for $\text{csch } x, \text{sech } x,$ and $\coth x$ from the derivative formulas for $\sinh x, \cosh x,$ and $\tanh x$.
7. Find the derivatives of $\cosh^{-1} x$ and $\tanh^{-1} x$ by differentiating the formulas in Theorem 6.8.4.
8. Find the derivatives of $\sinh^{-1} x, \cosh^{-1} x,$ and $\tanh^{-1} x$ by differentiating the equations $x = \sinh y, x = \cosh y,$ and $x = \tanh y$ implicitly.

**9–28 Find $dy/dx$.**
9. $y = \sinh(4x - 8)$
10. $y = \cosh(x^4)$
11. $y = \coth(\ln x)$
12. $y = \ln(\tanh 2x)$
13. $y = \text{csch}(1/x)$
14. $y = \text{sech}(e^{2x})$
15. $y = \sqrt{4x + \cosh^2(5x)}$
16. $y = \sinh^3(2x)$
17. $y = x^3 \tanh^2(\sqrt{x})$
18. $y = \sinh(\cos 3x)$
19. $y = \sinh^{-1}\left(\frac{1}{3}x\right)$
20. $y = \sinh^{-1}(1/x)$
21. $y = \ln(\cosh^{-1} x)$
22. $y = \cosh^{-1}(\sinh^{-1} x)$
23. $y = \frac{1}{\tanh^{-1} x}$
24. $y = (\coth^{-1} x)^2$
25. $y = \cosh^{-1}(\cosh x)$
26. $y = \sinh^{-1}(\tanh x)$
27. $y = e^x \text{sech}^{-1}\sqrt{x}$
28. $y = (1 + x\text{csch}^{-1} x)^{10}$

**29–44 Evaluate the integrals.**
29. $\int \sinh^6 x \cosh x \, dx$
30. $\int \cosh(2x - 3) dx$
31. $\int \sqrt{\tanh x}\text{sech}^2 x \, dx$
32. $\int \text{csch}^2(3x) dx$
33. $\int \tanh 2x \, dx$
34. $\int \coth^2 x \text{csch}^2 x \, dx$
35. $\int_{\ln 2}^{\ln 3}\tanh x \text{sech}^3 x \, dx$
36. $\int_0^{\ln 3}\frac{e^x - e^{-x}}{e^x + e^{-x}} dx$
37. $\int \frac{dx}{\sqrt{1 + 9x^2}}$
38. $\int \frac{dx}{\sqrt{x^2 - 2}} \quad (x > \sqrt{2})$
39. $\int \frac{dx}{\sqrt{1 - e^{2x}}} \quad (x < 0)$
40. $\int \frac{\sin\theta \, d\theta}{\sqrt{1 + \cos^2\theta}}$
41. $\int \frac{dx}{x\sqrt{1 + 4x^2}}$
42. $\int \frac{dx}{\sqrt{9x^2 - 25}} \quad (x > 5/3)$
43. $\int_0^{1/2}\frac{dx}{1 - x^2}$
44. $\int_0^{\sqrt{3}}\frac{dt}{\sqrt{t^2 + 1}}$

**45–48 True–False Determine whether the statement is true or false. Explain your answer.**
45. The equation $\cosh x = \sinh x$ has no solutions.
46. Exactly two of the hyperbolic functions are bounded.
47. There is exactly one hyperbolic function $f(x)$ such that for all real numbers $a$, the equation $f(x) = a$ has a unique solution $x$.
48. The identities in Theorem 6.8.2 may be obtained from the corresponding trigonometric identities by replacing each trigonometric function with its hyperbolic analogue.

49. Find the area enclosed by $y = \sinh 2x, \; y = 0,$ and $x = \ln 3$.
50. Find the volume of the solid that is generated when the region enclosed by $y = \text{sech } x, \; y = 0, \; x = 0,$ and $x = \ln 2$ is revolved about the $x$-axis.
51. Find the volume of the solid that is generated when the region enclosed by $y = \cosh 2x, \; y = \sinh 2x, \; x = 0,$ and $x = 5$ is revolved about the $x$-axis.
52. Approximate the positive value of the constant $a$ such that the area enclosed by $y = \cosh ax, \; y = 0, \; x = 0,$ and $x = 1$ is 2 square units. Express your answer to at least five decimal places.
53. Find the arc length of the catenary $y = \cosh x$ between $x = 0$ and $x = \ln 2$.
54. Find the arc length of the catenary $y = a\cosh(x/a)$ between $x = 0$ and $x = x_1 \; (x_1 > 0)$.
55. In parts (a)–(f) find the limits, and confirm that they are consistent with the graphs in Figures 6.8.1 and 6.8.6.  
    (a) $\lim_{x \to +\infty}\sinh x$ (b) $\lim_{x \to -\infty}\sinh x$  
    (c) $\lim_{x \to +\infty}\tanh x$ (d) $\lim_{x \to -\infty}\tanh x$  
    (e) $\lim_{x \to +\infty}\sinh^{-1} x$ (f) $\lim_{x \to 1^-}\tanh^{-1} x$

#### FOCUS ON CONCEPTS
56. Explain how to obtain the asymptotes for $y = \tanh x$ from the curvilinear asymptotes for $y = \cosh x$ and $y = \sinh x$.
57. Prove that $\sinh x$ is an odd function of $x$ and that $\cosh x$ is an even function of $x$, and check that this is consistent with the graphs in Figure 6.8.1.

**58–59 Prove the identities.**
58. (a) $\cosh x + \sinh x = e^x$  
    (b) $\cosh x - \sinh x = e^{-x}$  
    (c) $\sinh(x + y) = \sinh x\cosh y + \cosh x\sinh y$  
    (d) $\sinh 2x = 2\sinh x\cosh x$  
    (e) $\cosh(x + y) = \cosh x\cosh y + \sinh x\sinh y$  
    (f) $\cosh 2x = \cosh^2 x + \sinh^2 x$  
    (g) $\cosh 2x = 2\sinh^2 x + 1$  
    (h) $\cosh 2x = 2\cosh^2 x - 1$
59. (a) $1 - \tanh^2 x = \text{sech}^2 x$  
    (b) $\tanh(x + y) = \frac{\tanh x + \tanh y}{1 + \tanh x\tanh y}$  
    (c) $\tanh 2x = \frac{2\tanh x}{1 + \tanh^2 x}$

60. Prove:  
    (a) $\cosh^{-1} x = \ln(x + \sqrt{x^2 - 1}), \; x \ge 1$  
    (b) $\tanh^{-1} x = \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right), \; -1 < x < 1$.
61. Use Exercise 60 to obtain the derivative formulas for $\cosh^{-1} x$ and $\tanh^{-1} x$.
62. Prove:  
    $\text{sech}^{-1} x = \cosh^{-1}(1/x), \; 0 < x \le 1$  
    $\coth^{-1} x = \tanh^{-1}(1/x), \; |x| > 1$  
    $\text{csch}^{-1} x = \sinh^{-1}(1/x), \; x \neq 0$
63. Use Exercise 62 to express the integral $\int \frac{du}{1 - u^2}$ entirely in terms of $\tanh^{-1}$.
64. Show that  
    (a) $\frac{d}{dx}[\text{sech}^{-1}|x|] = -\frac{1}{x\sqrt{1 - x^2}}$  
    (b) $\frac{d}{dx}[\text{csch}^{-1}|x|] = -\frac{1}{x\sqrt{1 + x^2}}$.
65. In each part, find the limit: (a) $\lim_{x \to +\infty}(\cosh^{-1} x - \ln x)$ (b) $\lim_{x \to +\infty}\frac{\cosh x}{e^x}$.
66. Use the first and second derivatives to show that the graph of $y = \tanh^{-1} x$ is always increasing and has an inflection point at the origin.
67. The integration formulas for $1/\sqrt{u^2 - a^2}$ in Theorem 6.8.6 are valid for $u > a$. Show that the following formula is valid for $u < -a$:
    $$\int \frac{du}{\sqrt{u^2 - a^2}} = -\cosh^{-1}\left(-\frac{u}{a}\right) + C \quad\text{or}\quad \ln|u + \sqrt{u^2 - a^2}| + C$$
68. Show that $(\sinh x + \cosh x)^n = \sinh nx + \cosh nx$.
69. Show that $\int_{-a}^a e^{tx} dx = \frac{2\sinh at}{t}$.
70. A cable is suspended between two poles as shown in Figure 6.8.2. Assume that the equation of the curve formed by the cable is $y = a\cosh(x/a)$, where $a$ is a positive constant. Suppose that the $x$-coordinates of the points of support are $x = -b$ and $x = b$, where $b > 0$.  
    (a) Show that the length $L$ of the cable is given by $L = 2a\sinh\frac{b}{a}$.  
    (b) Show that the sag $S$ (the vertical distance between the highest and lowest points on the cable) is given by $S = a\cosh\frac{b}{a} - a$.

**71–72 These exercises refer to the hanging cable described in Exercise 70.**
71. Assuming that the poles are $400\text{ ft}$ apart and the sag in the cable is $30\text{ ft}$, approximate the length of the cable by approximating $a$. Express your final answer to the nearest tenth of a foot. [*Hint:* First let $u = 200/a$.]
72. Assuming that the cable is $120\text{ ft}$ long and the poles are $100\text{ ft}$ apart, approximate the sag in the cable by approximating $a$. Express your final answer to the nearest tenth of a foot. [*Hint:* First let $u = 50/a$.]
73. The design of the Gateway Arch in St. Louis, Missouri, by architect Eero Saarinen was implemented using equations provided by Dr. Hannskarl Bandel. The equation used for the centerline of the arch was
    $$y = 693.8597 - 68.7672\cosh(0.0100333x)\text{ ft}$$
    for $x$ between $-299.2239$ and $299.2239$.  
    (a) Use a graphing utility to graph the centerline of the arch.  
    (b) Find the length of the centerline to four decimal places.  
    (c) For what values of $x$ is the height of the arch $100\text{ ft}$? Round your answers to four decimal places.  
    (d) Approximate, to the nearest degree, the acute angle that the tangent line to the centerline makes with the ground at the ends of the arch.
74. Suppose that a hollow tube rotates with a constant angular velocity of $\omega\text{ rad/s}$ about a horizontal axis at one end of the tube (see Figure Ex-74). Assume that an object is free to slide without friction in the tube while the tube is rotating. Let $r$ be the distance from the object to the pivot point at time $t \ge 0$, and assume that the object is at rest and $r = 0$ when $t = 0$. It can be shown that if the tube is horizontal at time $t = 0$ and rotating as shown in the figure, then
    $$r = \frac{g}{2\omega^2}[\sinh(\omega t) - \sin(\omega t)]$$
    during the period that the object is in the tube. Assume that $t$ is in seconds and $r$ is in meters, and use $g = 9.8\text{ m/s}^2$ and $\omega = 2\text{ rad/s}$.  
    (a) Graph $r$ versus $t$ for $0 \le t \le 1$.  
    (b) Assuming that the tube has a length of $1\text{ m}$, approximately how long does it take for the object to reach the end of the tube?  
    (c) Use the result of part (b) to approximate $dr/dt$ at the instant that the object reaches the end of the tube.
75. The accompanying figure shows a person pulling a boat by holding a rope of length $a$ attached to the bow and walking along the edge of a dock. If we assume that the rope is always tangent to the curve traced by the bow of the boat, then this curve, which is called a *tractrix*, has the property that the segment of the tangent line between the curve and the $y$-axis has a constant length $a$. It can be proved that the equation of this tractrix is
    $$y = a\text{sech}^{-1}\frac{x}{a} - \sqrt{a^2 - x^2}$$
    (a) Show that to move the bow of the boat to a point $(x, y)$, the person must walk a distance $D = a\text{sech}^{-1}\frac{x}{a}$ from the origin.  
    (b) If the rope has a length of $15\text{ m}$, how far must the person walk from the origin to bring the boat $10\text{ m}$ from the dock? Round your answer to two decimal places.  
    (c) Find the distance traveled by the bow along the tractrix as it moves from its initial position to the point where it is $5\text{ m}$ from the dock.
76. **Writing.** Suppose that, by analogy with the trigonometric functions, we define $\cosh t$ and $\sinh t$ geometrically using Figure 6.8.3b:  
    “For any real number $t$, define $x = \cosh t$ and $y = \sinh t$ to be the unique values of $x$ and $y$ such that  
    (i) $P(x, y)$ is on the right branch of the unit hyperbola $x^2 - y^2 = 1$;  
    (ii) $t$ and $y$ have the same sign (or are both 0);  
    (iii) the area of the region bounded by the $x$-axis, the right branch of the unit hyperbola, and the segment from the origin to $P$ is $|t|/2$.”  
    Discuss what properties would first need to be verified in order for this to be a legitimate definition.
77. **Writing.** Investigate what properties of $\cosh t$ and $\sinh t$ can be proved directly from the geometric definition in Exercise 76. Write a short description of the results of your investigation.

---

## CHAPTER 6 REVIEW EXERCISES

1. In each part, find $f^{-1}(x)$ if the inverse exists.  
   (a) $f(x) = (e^x)^2 + 1$  
   (b) $f(x) = \sin\left(\frac{1 - 2x}{x}\right), \; \frac{2}{4 + \pi} \le x \le \frac{2}{4 - \pi}$  
   (c) $f(x) = \frac{1}{1 + 3\tan^{-1} x}$

2. (a) State the restrictions on the domains of $\sin x, \cos x, \tan x,$ and $\sec x$ that are imposed to make those functions one-to-one in the definitions of $\sin^{-1} x, \cos^{-1} x, \tan^{-1} x,$ and $\sec^{-1} x$.  
   (b) Sketch the graphs of the restricted trigonometric functions in part (a) and their inverses.

3. In each part, find the exact numerical value of the given expression.  
   (a) $\cos[\cos^{-1}(4/5) + \sin^{-1}(5/13)]$  
   (b) $\sin[\sin^{-1}(4/5) + \cos^{-1}(5/13)]$

4. In each part, sketch the graph, and check your work with a graphing utility.  
   (a) $f(x) = 3\sin^{-1}(x/2)$  
   (b) $f(x) = \cos^{-1} x - \pi/2$  
   (c) $f(x) = 2\tan^{-1}(-3x)$  
   (d) $f(x) = \cos^{-1} x + \sin^{-1} x$

5. Suppose that the graph of $y = \log x$ is drawn with equal scales of 1 inch per unit in both the $x$- and $y$-directions. If a bug wants to walk along the graph until it reaches a height of $5\text{ ft}$ above the $x$-axis, how many miles to the right of the origin will it have to travel?

6. Find the largest value of $a$ such that the function $f(x) = xe^{-x}$ has an inverse on the interval $(-\infty, a]$.

7. Express the following function as a rational function of $x$:
   $$3\ln\sqrt{e^{2x}(e^x)^3} + 2\exp(\ln 1)$$

8. Suppose that $y = Ce^{kt}$, where $C$ and $k$ are constants, and let $Y = \ln y$. Show that the graph of $Y$ versus $t$ is a line, and state its slope and $Y$-intercept.

9. (a) Sketch the curves $y = \pm e^{-x/2}$ and $y = e^{-x/2}\sin 2x$ for $-\pi/2 \le x \le 3\pi/2$ in the same coordinate system, and check your work using a graphing utility.  
   (b) Find all $x$-intercepts of the curve $y = e^{-x/2}\sin 2x$ in the stated interval, and find the $x$-coordinates of all points where this curve intersects the curves $y = \pm e^{-x/2}$.

10. Suppose that a package of medical supplies is dropped from a helicopter straight down by parachute into a remote area. The velocity $v$ (in feet per second) of the package $t$ seconds after it is released is given by $v = 24.61(1 - e^{-1.3t})$.  
    (a) Graph $v$ versus $t$.  
    (b) Show that the graph has a horizontal asymptote $v = c$.  
    (c) The constant $c$ is called the *terminal velocity*. Explain what the terminal velocity means in practical terms.  
    (d) Can the package actually reach its terminal velocity? Explain.  
    (e) How long does it take for the package to reach 98% of its terminal velocity?

11. A breeding group of 20 bighorn sheep is released in a protected area in Colorado. It is expected that with careful management the number of sheep, $N$, after $t$ years will be given by the formula
    $$N = \frac{220}{1 + 10(0.83^t)}$$
    and that the sheep population will be able to maintain itself without further supervision once the population reaches a size of 80.  
    (a) Graph $N$ versus $t$.  
    (b) How many years must the state of Colorado maintain a program to care for the sheep?  
    (c) How many bighorn sheep can the environment in the protected area support? [*Hint:* Examine the graph of $N$ versus $t$ for large values of $t$.]

12. An oven is preheated and then remains at a constant temperature. A potato is placed in the oven to bake. Suppose that the temperature $T$ (in $^\circ\text{F}$) of the potato $t$ minutes later is given by $T = 400 - 325(0.97^t)$. The potato will be considered done when its temperature is anywhere between $260^\circ\text{F}$ and $280^\circ\text{F}$.  
    (a) During what interval of time would the potato be considered done?  
    (b) How long does it take for the difference between the potato and oven temperatures to be cut in half?

13. (a) Show that the graphs of $y = \ln x$ and $y = x^{0.2}$ intersect.  
    (b) Approximate the solution(s) of the equation $\ln x = x^{0.2}$ to three decimal places.

14. (a) Show that for $x > 0$ and $k \neq 0$ the equations $x^k = e^x$ and $\frac{\ln x}{x} = \frac{1}{k}$ have the same solutions.  
    (b) Use the graph of $y = (\ln x)/x$ to determine the values of $k$ for which the equation $x^k = e^x$ has two distinct positive solutions.  
    (c) Estimate the positive solution(s) of $x^8 = e^x$.

**15–18 Find the limits.**
15. $\lim_{t \to \pi/2^+} e^{\tan t}$
16. $\lim_{\theta \to 0^+} [\ln(\sin 2\theta) - \ln(\tan\theta)]$
17. $\lim_{x \to +\infty}\left(1 + \frac{3}{x}\right)^{-x}$
18. $\lim_{x \to +\infty}\left(1 + \frac{a}{x}\right)^{bx}, \; a, b > 0$

**19–20 Find $dy/dx$ by first using algebraic properties of the natural logarithm function.**
19. $y = \ln\left[\frac{(x + 1)(x + 2)^2}{(x + 3)^3 (x + 4)^4}\right]$
20. $y = \ln\left[\frac{\sqrt{x}\sqrt[3]{x + 1}}{\sin x \sec x}\right]$

**21–38 Find $dy/dx$.**
21. $y = \ln 2x$
22. $y = (\ln x)^2$
23. $y = \sqrt[3]{\ln x + 1}$
24. $y = \ln(\sqrt[3]{x} + 1)$
25. $y = \log(\ln x)$
26. $y = \frac{1 + \log x}{1 - \log x}$
27. $y = \ln(x^{3/2}\sqrt{1 + x^4})$
28. $y = \ln\left(\frac{\sqrt{x}\cos x}{1 + x^2}\right)$
29. $y = e^{\ln(x^2 + 1)}$
30. $y = \ln\left(\frac{1 + e^x + e^{2x}}{1 - e^{3x}}\right)$
31. $y = 2x e^{\sqrt{x}}$
32. $y = \frac{a}{1 + b e^{-x}}$
33. $y = \frac{1}{\pi}\tan^{-1} 2x$
34. $y = 2^{\sin^{-1} x}$
35. $y = x^{(e^x)}$
36. $y = (1 + x)^{1/x}$
37. $y = \sec^{-1}(2x + 1)$
38. $y = \sqrt{\cos^{-1} x^2}$

**39–40 Find $dy/dx$ using logarithmic differentiation.**
39. $y = \frac{x^3}{\sqrt{x^2 + 1}}$
40. $y = \sqrt[3]{\frac{x^2 - 1}{x^2 + 1}}$

41. (a) Make a conjecture about the shape of the graph of $y = \frac{1}{2}x - \ln x$, and draw a rough sketch.  
    (b) Check your conjecture by graphing the equation over the interval $0 < x < 5$ with a graphing utility.  
    (c) Show that the slopes of the tangent lines to the curve at $x = 1$ and $x = e$ have opposite signs.  
    (d) What does part (c) imply about the existence of a horizontal tangent line to the curve? Explain.  
    (e) Find the exact $x$-coordinates of all horizontal tangent lines to the curve.

42. Recall from Section 6.1 that the loudness $\beta$ of a sound in decibels (dB) is given by $\beta = 10\log(I/I_0)$, where $I$ is the intensity of the sound in watts per square meter ($\text{W/m}^2$) and $I_0$ is a constant that is approximately the intensity of a sound at the threshold of human hearing. Find the rate of change of $\beta$ with respect to $I$ at the point where  
    (a) $I/I_0 = 10$ (b) $I/I_0 = 100$ (c) $I/I_0 = 1000$.

43. A particle is moving along the curve $y = x\ln x$. Find all values of $x$ at which the rate of change of $y$ with respect to time is three times that of $x$. [Assume that $dx/dt$ is never zero.]

44. Find the equation of the tangent line to the graph of $y = \ln(5 - x^2)$ at $x = 2$.

45. Find the value of $b$ so that the line $y = x$ is tangent to the graph of $y = \log_b x$. Confirm your result by graphing both $y = x$ and $y = \log_b x$ in the same coordinate system.

46. In each part, find the value of $k$ for which the graphs of $y = f(x)$ and $y = \ln x$ share a common tangent line at their point of intersection. Confirm your result by graphing $y = f(x)$ and $y = \ln x$ in the same coordinate system.  
    (a) $f(x) = \sqrt{x} + k$ (b) $f(x) = k\sqrt{x}$

47. If $f$ and $g$ are inverse functions and $f$ is differentiable on its domain, must $g$ be differentiable on its domain? Give a reasonable informal argument to support your answer.

48. In each part, find $(f^{-1})'(x)$ using Formula (2) of Section 6.3, and check your answer by differentiating $f^{-1}$ directly.  
    (a) $f(x) = 3/(x + 1)$ (b) $f(x) = \sqrt{e^x}$

49. Find a point on the graph of $y = e^{3x}$ at which the tangent line passes through the origin.

50. Show that the rate of change of $y = 5000e^{1.07x}$ is proportional to $y$.

51. Show that the function $y = e^{ax}\sin bx$ satisfies $y'' - 2ay' + (a^2 + b^2)y = 0$ for any real constants $a$ and $b$.

52. Show that the function $y = \tan^{-1} x$ satisfies $y'' = -2\sin y\cos^3 y$.

53. Suppose that the population of deer on an island is modeled by the equation
    $$P(t) = \frac{95}{5 - 4e^{-t/4}}$$
    where $P(t)$ is the number of deer $t$ weeks after an initial observation at time $t = 0$.  
    (a) Use a graphing utility to graph the function $P(t)$.  
    (b) In words, explain what happens to the population over time. Check your conclusion by finding $\lim_{t \to +\infty} P(t)$.  
    (c) In words, what happens to the rate of population growth over time? Check your conclusion by graphing $P'(t)$.

54. The equilibrium constant $k$ of a balanced chemical reaction changes with the absolute temperature $T$ according to the law
    $$k = k_0 \exp\left(-\frac{q(T - T_0)}{2T_0 T}\right)$$
    where $k_0, q,$ and $T_0$ are constants. Find the rate of change of $k$ with respect to $T$.

**55–56 Find the limit by interpreting the expression as an appropriate derivative.**
55. $\lim_{h \to 0}\frac{(1 + h)^\pi - 1}{h}$
56. $\lim_{x \to e}\frac{1 - \ln x}{(x - e)\ln x}$

57. Suppose that $\lim f(x) = \pm\infty$ and $\lim g(x) = \pm\infty$. In each of the four possible cases, state whether $\lim[f(x) - g(x)]$ is an indeterminate form, and give a reasonable informal argument to support your answer.

58. (a) Under what conditions will a limit of the form $\lim_{x \to a}[f(x)/g(x)]$ be an indeterminate form?  
    (b) If $\lim_{x \to a} g(x) = 0$, must $\lim_{x \to a}[f(x)/g(x)]$ be an indeterminate form? Give some examples to support your answer.

**59–62 Evaluate the given limit.**
59. $\lim_{x \to +\infty}(e^x - x^2)$
60. $\lim_{x \to 1}\frac{\ln x}{x^4 - 1}$
61. $\lim_{x \to 0}\frac{x^2 e^x}{\sin^2 3x}$
62. $\lim_{x \to 0}\frac{a^x - 1}{x}, \; a > 0$

**63–64 Find: (a) the intervals on which $f$ is increasing, (b) the intervals on which $f$ is decreasing, (c) the open intervals on which $f$ is concave up, (d) the open intervals on which $f$ is concave down, and (e) the $x$-coordinates of all inflection points.**
63. $f(x) = 1/e^{x^2}$
64. $f(x) = \tan^{-1} x^2$

**65–66 Use any method to find the relative extrema of the function $f$.**
65. $f(x) = \ln(1 + x^2)$
66. $f(x) = x^2 e^x$

**67–68 In each part, find the absolute minimum $m$ and the absolute maximum $M$ of $f$ on the given interval (if they exist), and state where the absolute extrema occur.**
67. $f(x) = e^x/x^2; \; (0, +\infty)$
68. $f(x) = x^x; \; (0, +\infty)$

69. Use a graphing utility to estimate the absolute maximum and minimum values of $f(x) = x/2 + \ln(x^2 + 1)$, if any, on the interval $[-4, 0]$, and then use calculus methods to find the exact values.
70. Prove that $x \le \sin^{-1} x$ for all $x$ in $[0, 1]$.

**71–74 Evaluate the integrals.**
71. $\int [x^{-2/3} - 5e^x] dx$
72. $\int \left[\frac{3}{4x} - \sec^2 x\right] dx$
73. $\int \left[\frac{1}{1 + x^2} + \frac{2}{\sqrt{1 - x^2}}\right] dx$
74. $\int \left[\frac{12}{x\sqrt{x^2 - 1}} + \frac{1 - x^4}{1 + x^2}\right] dx$

**75–76 Use a calculating utility to find the left endpoint, right endpoint, and midpoint approximations to the area under the curve $y = f(x)$ over the stated interval using $n = 10$ subintervals.**
75. $y = \ln x; \; [1, 2]$
76. $y = e^x; \; [0, 1]$

77. Interpret the expression as a definite integral over $[0, 1]$, and then evaluate the limit by evaluating the integral:
    $$\lim_{\max \Delta x_k \to 0}\sum_{k=1}^n e^{x_k^*} \Delta x_k$$

78. Find the limit $\lim_{n \to +\infty}\frac{e^{1/n} + e^{2/n} + e^{3/n} + \dots + e^{n/n}}{n}$ by interpreting it as a limit of Riemann sums in which the interval $[0, 1]$ is divided into $n$ subintervals of equal length.

**79–80 Find the area under the curve $y = f(x)$ over the stated interval.**
79. $f(x) = e^x; \; [1, 3]$
80. $f(x) = \frac{1}{x}; \; [1, e^3]$

**81. Solve the initial-value problems.**  
(a) $\frac{dy}{dx} = \cos x - 5e^x, \; y(0) = 0$  
(b) $\frac{dy}{dx} = xe^{x^2}, \; y(0) = 0$

**82–84 Evaluate the integrals by making an appropriate substitution.**
82. $\int_e^{e^2}\frac{dx}{x\ln x}$
83. $\int_0^1 \frac{dx}{\sqrt{e^x}}$
84. $\int_0^{2/\sqrt{3}}\frac{1}{4 + 9x^2} dx$

85. Find the volume of the solid whose base is the region bounded between the curves $y = \sqrt{x}$ and $y = 1/\sqrt{x}$ for $1 \le x \le 4$ and whose cross sections taken perpendicular to the $x$-axis are squares.

86. Find the average value of $f(x) = e^x + e^{-x}$ over the interval $[\ln\frac{1}{2}, \ln 2]$.

**87. In each part, prove the identity.**  
(a) $\cosh 3x = 4\cosh^3 x - 3\cosh x$  
(b) $\cosh\frac{1}{2}x = \sqrt{\frac{1}{2}(\cosh x + 1)}$  
(c) $\sinh\frac{1}{2}x = \pm\sqrt{\frac{1}{2}(\cosh x - 1)}$

88. Show that for any constant $a$, the function $y = \sinh(ax)$ satisfies the equation $y'' = a^2 y$.

---

## CHAPTER 6 MAKING CONNECTIONS

1. Consider a simple model of radioactive decay. We assume that given any quantity of a radioactive element, the fraction of the quantity that decays over a period of time will be a constant that depends on only the particular element and the length of the time period. We choose a time parameter $-\infty < t < +\infty$ and let $A = A(t)$ denote the amount of the element remaining at time $t$. We also choose units of measure such that the initial amount of the element is $A(0) = 1$, and we let $b = A(1)$ denote the amount at time $t = 1$. Prove that the function $A(t)$ has the following properties:  
   (a) $A(-t) = \frac{1}{A(t)}$ [*Hint:* For $t > 0$, you can interpret $A(t)$ as the fraction of any given amount that remains after a time period of length $t$.]  
   (b) $A(s + t) = A(s) \cdot A(t)$ [*Hint:* First consider positive $s$ and $t$. For the other cases use the property in part (a).]  
   (c) If $n$ is any nonzero integer, then $A(1/n) = (A(1))^{1/n} = b^{1/n}$.  
   (d) If $m$ and $n$ are integers with $n \neq 0$, then $A(m/n) = (A(1))^{m/n} = b^{m/n}$.  
   (e) Assuming that $A(t)$ is a continuous function of $t$, then $A(t) = b^t$. [*Hint:* Prove that if two continuous functions agree on the set of rational numbers, then they are equal.]  
   (f) If we replace the assumption that $A(0) = 1$ by the condition $A(0) = A_0$, prove that $A = A_0 b^t$.

2. Refer to Figure 6.1.5.  
   (a) Make the substitution $h = 1/x$ and conclude that
   $$(1 + h)^{1/h} < e < (1 - h)^{-1/h} \quad\text{for } h > 0$$
   and
   $$(1 - h)^{-1/h} < e < (1 + h)^{1/h} \quad\text{for } h < 0$$
   (b) Use the inequalities in part (a) and the Squeezing Theorem to prove that
   $$\lim_{h \to 0}\frac{e^h - 1}{h} = 1$$
   (c) Explain why the limit in part (b) confirms Figure 6.1.4.  
   (d) Use the limit in part (b) to prove that $\frac{d}{dx}(e^x) = e^x$.

3. Give a convincing geometric argument to show that
   $$\int_1^e \ln x \, dx + \int_0^1 e^x dx = e$$
