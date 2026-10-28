# CHAPTER 9: INFINITE SERIES

> Perspective creates the illusion that the sequence of railroad ties continues indefinitely but converges toward a single point infinitely far away.

In this chapter we will be concerned with infinite series, which are sums that involve infinitely many terms. Infinite series play a fundamental role in both mathematics and science—they are used, for example, to approximate trigonometric functions and logarithms, to solve differential equations, to evaluate difficult integrals, to create new functions, and to construct mathematical models of physical laws. Since it is impossible to add up infinitely many numbers directly, one goal will be to define exactly what we mean by the sum of an infinite series. However, unlike finite sums, it turns out that not all infinite series actually have a sum, so we will need to develop tools for determining which infinite series have sums and which do not. Once the basic ideas have been developed we will begin to apply our work; we will show how infinite series are used to evaluate such quantities as $\ln 2, e, \sin 3^\circ,$ and $\pi$, how they are used to create functions, and finally, how they are used to model physical laws.

---

## 9.1 SEQUENCES

In everyday language, the term "sequence" means a succession of things in a definite order—chronological order, size order, or logical order, for example. In mathematics, the term "sequence" is commonly used to denote a succession of numbers whose order is determined by a rule or a function. In this section, we will develop some of the basic ideas concerning sequences of numbers.

### DEFINITION OF A SEQUENCE

Stated informally, an **infinite sequence**, or more simply a **sequence**, is an unending succession of numbers, called **terms**. It is understood that the terms have a definite order; that is, there is a first term $a_1$, a second term $a_2$, a third term $a_3$, a fourth term $a_4$, and so forth. Such a sequence would typically be written as
$$a_1, a_2, a_3, a_4, \dots$$
where the dots are used to indicate that the sequence continues indefinitely. Some specific examples are
$$1, 2, 3, 4, \dots, \quad 1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \dots,$$
$$2, 4, 6, 8, \dots, \quad 1, -1, 1, -1, \dots$$
Each of these sequences has a definite pattern that makes it easy to generate additional terms if we assume that those terms follow the same pattern as the displayed terms. However, such patterns can be deceiving, so it is better to have a rule or formula for generating the terms. One way of doing this is to look for a function that relates each term in the sequence to its term number. For example, in the sequence
$$2, 4, 6, 8, \dots$$
each term is twice the term number; that is, the $n$th term in the sequence is given by the formula $2n$. We denote this by writing the sequence as
$$2, 4, 6, 8, \dots, 2n, \dots$$
We call the function $f(n) = 2n$ the **general term** of this sequence. Now, if we want to know a specific term in the sequence, we need only substitute its term number in the formula for the general term. For example, the 37th term in the sequence is $2 \cdot 37 = 74$.

#### Example 1
In each part, find the general term of the sequence.  
(a) $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, \dots$  
(b) $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{16}, \dots$  
(c) $\frac{1}{2}, -\frac{2}{3}, \frac{3}{4}, -\frac{4}{5}, \dots$  
(d) $1, 3, 5, 7, \dots$  

**Solution (a).** In Table 9.1.1, the four known terms have been placed below their term numbers, from which we see that the numerator is the same as the term number and the denominator is one greater than the term number. This suggests that the $n$th term has numerator $n$ and denominator $n + 1$, as indicated in the table. Thus, the sequence can be expressed as
$$\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, \dots, \frac{n}{n + 1}, \dots$$

##### Table 9.1.1
| Term Number | 1 | 2 | 3 | 4 | $\dots$ | $n$ | $\dots$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Term** | $\frac{1}{2}$ | $\frac{2}{3}$ | $\frac{3}{4}$ | $\frac{4}{5}$ | $\dots$ | $\frac{n}{n+1}$ | $\dots$ |

**Solution (b).** In Table 9.1.2, the denominators of the four known terms have been expressed as powers of 2 and the first four terms have been placed below their term numbers, from which we see that the exponent in the denominator is the same as the term number. This suggests that the denominator of the $n$th term is $2^n$, as indicated in the table. Thus, the sequence can be expressed as
$$\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{16}, \dots, \frac{1}{2^n}, \dots$$

##### Table 9.1.2
| Term Number | 1 | 2 | 3 | 4 | $\dots$ | $n$ | $\dots$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Term** | $\frac{1}{2}$ | $\frac{1}{2^2}$ | $\frac{1}{2^3}$ | $\frac{1}{2^4}$ | $\dots$ | $\frac{1}{2^n}$ | $\dots$ |

**Solution (c).** This sequence is identical to that in part (a), except for the alternating signs. Thus, the $n$th term in the sequence can be obtained by multiplying the $n$th term in part (a) by $(-1)^{n+1}$. This factor produces the correct alternating signs, since its successive values, starting with $n = 1$, are $1, -1, 1, -1, \dots$. Thus, the sequence can be written as
$$\frac{1}{2}, -\frac{2}{3}, \frac{3}{4}, -\frac{4}{5}, \dots, (-1)^{n+1}\frac{n}{n + 1}, \dots$$

**Solution (d).** In Table 9.1.3, the four known terms have been placed below their term numbers, from which we see that each term is one less than twice its term number. This suggests that the $n$th term in the sequence is $2n - 1$, as indicated in the table. Thus, the sequence can be expressed as
$$1, 3, 5, 7, \dots, 2n - 1, \dots$$

##### Table 9.1.3
| Term Number | 1 | 2 | 3 | 4 | $\dots$ | $n$ | $\dots$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Term** | 1 | 3 | 5 | 7 | $\dots$ | $2n - 1$ | $\dots$ |

When the general term of a sequence
$$a_1, a_2, a_3, \dots, a_n, \dots \tag{1}$$
is known, there is no need to write out the initial terms, and it is common to write only the general term enclosed in braces. Thus, (1) might be written as
$$\{a_n\}_{n=1}^{+\infty} \quad \text{or as} \quad \{a_n\}_{n=1}^{\infty}$$

For example, here are the four sequences in Example 1 expressed in brace notation:
* $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, \dots, \frac{n}{n+1}, \dots \implies \left\{\frac{n}{n+1}\right\}_{n=1}^{+\infty}$
* $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{16}, \dots, \frac{1}{2^n}, \dots \implies \left\{\frac{1}{2^n}\right\}_{n=1}^{+\infty}$
* $\frac{1}{2}, -\frac{2}{3}, \frac{3}{4}, -\frac{4}{5}, \dots, (-1)^{n+1}\frac{n}{n+1}, \dots \implies \left\{(-1)^{n+1}\frac{n}{n+1}\right\}_{n=1}^{+\infty}$
* $1, 3, 5, 7, \dots, 2n - 1, \dots \implies \{2n - 1\}_{n=1}^{+\infty}$

> *Note:* A sequence cannot be uniquely determined from a few initial terms. For example, the sequence whose general term is $f(n) = \frac{1}{3}(3 - 5n + 6n^2 - n^3)$ has 1, 3, and 5 as its first three terms, but its fourth term is also 5.

The letter $n$ in (1) is called the **index** for the sequence. It is not essential to use $n$ for the index; any letter not reserved for another purpose can be used. For example, we might view the general term of the sequence $a_1, a_2, a_3, \dots$ to be the $k$th term, in which case we would denote this sequence as $\{a_k\}_{k=1}^{+\infty}$. Moreover, it is not essential to start the index at 1; sometimes it is more convenient to start it at 0 (or some other integer). For example, consider the sequence
$$1, \frac{1}{2}, \frac{1}{2^2}, \frac{1}{2^3}, \dots$$
One way to write this sequence is
$$\left\{\frac{1}{2^{n-1}}\right\}_{n=1}^{+\infty}$$
However, the general term will be simpler if we think of the initial term in the sequence as the zeroth term, in which case we can write the sequence as
$$\left\{\frac{1}{2^n}\right\}_{n=0}^{+\infty}$$

We began this section by describing a sequence as an unending succession of numbers. Although this conveys the general idea, it is not a satisfactory mathematical definition because it relies on the term "succession," which is itself an undefined term. To motivate a precise definition, consider the sequence
$$2, 4, 6, 8, \dots, 2n, \dots$$
If we denote the general term by $f(n) = 2n$, then we can write this sequence as
$$f(1), f(2), f(3), \dots, f(n), \dots$$
which is a "list" of values of the function $f(n) = 2n, \; n = 1, 2, 3, \dots$ whose domain is the set of positive integers. This suggests the following definition.

> **9.1.1 DEFINITION**  
> A **sequence** is a function whose domain is a set of integers.

Typically, the domain of a sequence is the set of positive integers or the set of nonnegative integers. We will regard the expression $\{a_n\}_{n=1}^{+\infty}$ to be an alternative notation for the function $f(n) = a_n, \; n = 1, 2, 3, \dots$, and we will regard $\{a_n\}_{n=0}^{+\infty}$ to be an alternative notation for the function $f(n) = a_n, \; n = 0, 1, 2, 3, \dots$.

---

### GRAPHS OF SEQUENCES

Since sequences are functions, it makes sense to talk about the graph of a sequence. For example, the graph of the sequence $\{1/n\}_{n=1}^{+\infty}$ is the graph of the equation
$$y = \frac{1}{n}, \quad n = 1, 2, 3, \dots$$
Because the right side of this equation is defined only for positive integer values of $n$, the graph consists of a succession of isolated points (Figure 9.1.1a). This is different from the graph of $y = 1/x, \; x \ge 1$, which is a continuous curve (Figure 9.1.1b).

When the starting value for the index of a sequence is not relevant to the discussion, it is common to use a notation such as $\{a_n\}$ in which there is no reference to the starting value of $n$. We can distinguish between different sequences by using different letters for their general terms; thus, $\{a_n\}$, $\{b_n\}$, and $\{c_n\}$ denote three different sequences.

---

### LIMIT OF A SEQUENCE

Since sequences are functions, we can inquire about their limits. However, because a sequence $\{a_n\}$ is only defined for integer values of $n$, the only limit that makes sense is the limit of $a_n$ as $n \to +\infty$. In Figure 9.1.2 we have shown the graphs of four sequences, each of which behaves differently as $n \to +\infty$:
* The terms in the sequence $\{n + 1\}$ increase without bound.
* The terms in the sequence $\{(-1)^{n+1}\}$ oscillate between $-1$ and $1$.
* The terms in the sequence $\{n/(n + 1)\}$ increase toward a "limiting value" of 1.
* The terms in the sequence $\left\{1 + \left(-\frac{1}{2}\right)^n\right\}$ also tend toward a "limiting value" of 1, but do so in an oscillatory fashion.

Informally speaking, the limit of a sequence $\{a_n\}$ is intended to describe how $a_n$ behaves as $n \to +\infty$. To be more specific, we will say that a sequence $\{a_n\}$ approaches a limit $L$ if the terms in the sequence eventually become arbitrarily close to $L$. Geometrically, this means that for any positive number $\epsilon$ there is a point in the sequence after which all terms lie between the lines $y = L - \epsilon$ and $y = L + \epsilon$ (Figure 9.1.3). The following definition makes these ideas precise.

> **9.1.2 DEFINITION**  
> A sequence $\{a_n\}$ is said to **converge** to the limit $L$ if given any $\epsilon > 0$, there is a positive integer $N$ such that $|a_n - L| < \epsilon$ for $n \ge N$. In this case we write
> $$\lim_{n \to +\infty} a_n = L$$
> A sequence that does not converge to some finite limit is said to **diverge**.

#### Example 2
The first two sequences in Figure 9.1.2 diverge, and the second two converge to 1; that is,
$$\lim_{n \to +\infty} \frac{n}{n + 1} = 1 \quad \text{and} \quad \lim_{n \to +\infty} \left[1 + \left(-\frac{1}{2}\right)^n\right] = 1$$

The following theorem, which we state without proof, shows that the familiar properties of limits apply to sequences. This theorem ensures that the algebraic techniques used to find limits of the form $\lim_{x \to +\infty}$ can also be used for limits of the form $\lim_{n \to +\infty}$.

> **9.1.3 THEOREM**  
> Suppose that the sequences $\{a_n\}$ and $\{b_n\}$ converge to limits $L_1$ and $L_2$, respectively, and $c$ is a constant. Then:  
> (a) $\lim_{n \to +\infty} c = c$  
> (b) $\lim_{n \to +\infty} c a_n = c \lim_{n \to +\infty} a_n = c L_1$  
> (c) $\lim_{n \to +\infty} (a_n + b_n) = \lim_{n \to +\infty} a_n + \lim_{n \to +\infty} b_n = L_1 + L_2$  
> (d) $\lim_{n \to +\infty} (a_n - b_n) = \lim_{n \to +\infty} a_n - \lim_{n \to +\infty} b_n = L_1 - L_2$  
> (e) $\lim_{n \to +\infty} (a_n b_n) = \lim_{n \to +\infty} a_n \cdot \lim_{n \to +\infty} b_n = L_1 L_2$  
> (f) $\lim_{n \to +\infty} \left(\frac{a_n}{b_n}\right) = \frac{\lim_{n \to +\infty} a_n}{\lim_{n \to +\infty} b_n} = \frac{L_1}{L_2} \quad (\text{if } L_2 \neq 0)$

If the general term of a sequence is $f(n)$, where $f(x)$ is a function defined on the entire interval $[1, +\infty)$, then the values of $f(n)$ can be viewed as "sample values" of $f(x)$ taken at the positive integers. Thus,
$$\text{if } f(x) \to L \text{ as } x \to +\infty, \quad \text{then } f(n) \to L \text{ as } n \to +\infty$$
(Figure 9.1.4a). However, the converse is not true; that is, one cannot infer that $f(x) \to L$ as $x \to +\infty$ from the fact that $f(n) \to L$ as $n \to +\infty$ (Figure 9.1.4b).

#### Example 3
In each part, determine whether the sequence converges or diverges by examining the limit as $n \to +\infty$.
(a) $\left\{\frac{n}{2n + 1}\right\}_{n=1}^{+\infty}$
(b) $\left\{(-1)^{n+1}\frac{n}{2n + 1}\right\}_{n=1}^{+\infty}$
(c) $\left\{(-1)^{n+1}\frac{1}{n}\right\}_{n=1}^{+\infty}$
(d) $\{8 - 2n\}_{n=1}^{+\infty}$

**Solution (a).** Dividing numerator and denominator by $n$ and using Theorem 9.1.3 yields
$$\lim_{n \to +\infty} \frac{n}{2n + 1} = \lim_{n \to +\infty} \frac{1}{2 + 1/n} = \frac{\lim_{n \to +\infty} 1}{\lim_{n \to +\infty} (2 + 1/n)} = \frac{1}{2 + 0} = \frac{1}{2}$$
Thus, the sequence converges to $1/2$.

**Solution (b).** This sequence is the same as that in part (a), except for the factor of $(-1)^{n+1}$, which oscillates between $+1$ and $-1$. Thus, the terms in this sequence oscillate between positive and negative values, with the odd-numbered terms being identical to those in part (a) and the even-numbered terms being the negatives of those in part (a). Since the sequence in part (a) has a limit of $1/2$, it follows that the odd-numbered terms in this sequence approach $1/2$, and the even-numbered terms approach $-1/2$. Therefore, this sequence has no limit—it diverges.

**Solution (c).** Since $1/n \to 0$, the product $(-1)^{n+1}(1/n)$ oscillates between positive and negative values, with the odd-numbered terms approaching 0 through positive values and the even-numbered terms approaching 0 through negative values. Thus,
$$\lim_{n \to +\infty} (-1)^{n+1}\frac{1}{n} = 0$$
so the sequence converges to 0.

**Solution (d).** $\lim_{n \to +\infty} (8 - 2n) = -\infty$, so the sequence $\{8 - 2n\}_{n=1}^{+\infty}$ diverges.

#### Example 4
In each part, determine whether the sequence converges, and if so, find its limit.
(a) $1, \frac{1}{2}, \frac{1}{2^2}, \frac{1}{2^3}, \dots, \frac{1}{2^n}, \dots$
(b) $1, 2, 2^2, 2^3, \dots, 2^n, \dots$

**Solution.** Replacing $n$ by $x$ in the first sequence produces the power function $(1/2)^x$, and replacing $n$ by $x$ in the second sequence produces the power function $2^x$. Now recall that if $0 < b < 1$, then $b^x \to 0$ as $x \to +\infty$, and if $b > 1$, then $b^x \to +\infty$ as $x \to +\infty$ (Figure 6.1.1). Thus,
$$\lim_{n \to +\infty} \frac{1}{2^n} = 0 \quad \text{and} \quad \lim_{n \to +\infty} 2^n = +\infty$$
So, the sequence $\{1/2^n\}$ converges to 0, but the sequence $\{2^n\}$ diverges.

#### Example 5
Find the limit of the sequence $\left\{\frac{n}{e^n}\right\}_{n=1}^{+\infty}$.

**Solution.** The expression $\lim_{n \to +\infty} \frac{n}{e^n}$ is an indeterminate form of type $\infty/\infty$, so L'Hôpital's rule is indicated. However, we cannot apply this rule directly to $n/e^n$ because the functions $n$ and $e^n$ have been defined here only at the positive integers, and hence are not differentiable functions. To circumvent this problem we extend the domains of these functions to all real numbers, here implied by replacing $n$ by $x$, and apply L'Hôpital's rule to the limit of the quotient $x/e^x$. This yields
$$\lim_{x \to +\infty} \frac{x}{e^x} = \lim_{x \to +\infty} \frac{1}{e^x} = 0$$
from which we can conclude that $\lim_{n \to +\infty} \frac{n}{e^n} = 0$.

#### Example 6
Show that $\lim_{n \to +\infty} \sqrt[n]{n} = 1$.

**Solution.**
$$\lim_{n \to +\infty} \sqrt[n]{n} = \lim_{n \to +\infty} n^{1/n} = \lim_{n \to +\infty} e^{(1/n)\ln n} = e^0 = 1$$
(by L'Hôpital's rule applied to $(1/x)\ln x$).

Sometimes the even-numbered and odd-numbered terms of a sequence behave sufficiently differently that it is desirable to investigate their convergence separately. The following theorem, whose proof is omitted, is helpful for that purpose.

> **9.1.4 THEOREM**  
> A sequence converges to a limit $L$ if and only if the sequences of even-numbered terms and odd-numbered terms both converge to $L$.

#### Example 7
The sequence
$$\frac{1}{2}, \frac{1}{3}, \frac{1}{2^2}, \frac{1}{3^2}, \frac{1}{2^3}, \frac{1}{3^3}, \dots$$
converges to 0, since the even-numbered terms and the odd-numbered terms both converge to 0, and the sequence
$$1, \frac{1}{2}, 1, \frac{1}{3}, 1, \frac{1}{4}, \dots$$
diverges, since the odd-numbered terms converge to 1 and the even-numbered terms converge to 0.

---

### THE SQUEEZING THEOREM FOR SEQUENCES

> **9.1.5 THEOREM (The Squeezing Theorem for Sequences)**  
> Let $\{a_n\}$, $\{b_n\}$, and $\{c_n\}$ be sequences such that
> $$a_n \le b_n \le c_n \quad (\text{for all values of } n \text{ beyond some index } N)$$
> If the sequences $\{a_n\}$ and $\{c_n\}$ have a common limit $L$ as $n \to +\infty$, then $\{b_n\}$ also has the limit $L$ as $n \to +\infty$.

#### Example 8
Use numerical evidence to make a conjecture about the limit of the sequence $\left\{\frac{n!}{n^n}\right\}_{n=1}^{+\infty}$ and then confirm that your conjecture is correct.

##### Table 9.1.4
| $n$ | $n! / n^n$ | $n$ | $n! / n^n$ |
| :---: | :---: | :---: | :---: |
| 1 | 1.0000000000 | 7 | 0.0061198990 |
| 2 | 0.5000000000 | 8 | 0.0024032593 |
| 3 | 0.2222222222 | 9 | 0.0009366567 |
| 4 | 0.0937500000 | 10 | 0.0003628800 |
| 5 | 0.0384000000 | 11 | 0.0001399059 |
| 6 | 0.0154320988 | 12 | 0.0000537232 |

**Solution.** Table 9.1.4, which was obtained with a calculating utility, suggests that the limit of the sequence may be 0. To confirm this we need to examine the limit of $a_n = \frac{n!}{n^n}$ as $n \to +\infty$. Although this is an indeterminate form of type $\infty/\infty$, L'Hôpital's rule is not helpful because we have no definition of $x!$ for values of $x$ that are not integers. However, let us write out some of the initial terms and the general term in the sequence:
$$a_1 = 1, \quad a_2 = \frac{1 \cdot 2}{2 \cdot 2} = \frac{1}{2}, \quad a_3 = \frac{1 \cdot 2 \cdot 3}{3 \cdot 3 \cdot 3} = \frac{2}{9} < \frac{1}{3}, \quad a_4 = \frac{1 \cdot 2 \cdot 3 \cdot 4}{4 \cdot 4 \cdot 4 \cdot 4} = \frac{3}{32} < \frac{1}{4}, \dots$$
If $n > 1$, the general term of the sequence can be rewritten as
$$a_n = \frac{1 \cdot 2 \cdot 3 \cdots n}{n \cdot n \cdot n \cdots n} = \frac{1}{n}\left(\frac{2 \cdot 3 \cdots n}{n \cdot n \cdots n}\right)$$
from which it follows that $a_n \le 1/n$. It is now evident that
$$0 \le a_n \le \frac{1}{n}$$
However, the two outside expressions have a limit of 0 as $n \to +\infty$; thus, the Squeezing Theorem for Sequences implies that $a_n \to 0$ as $n \to +\infty$, which confirms our conjecture.

> **9.1.6 THEOREM**  
> If $\lim_{n \to +\infty} |a_n| = 0$, then $\lim_{n \to +\infty} a_n = 0$.

**Proof.** Depending on the sign of $a_n$, either $a_n = |a_n|$ or $a_n = -|a_n|$. Thus, in all cases we have
$$-|a_n| \le a_n \le |a_n|$$
However, the limit of the two outside terms is 0, and hence the limit of $a_n$ is 0 by the Squeezing Theorem for Sequences. $\blacksquare$

#### Example 9
Consider the sequence
$$1, -\frac{1}{2}, \frac{1}{2^2}, -\frac{1}{2^3}, \dots, (-1)^n \frac{1}{2^n}, \dots$$
If we take the absolute value of each term, we obtain the sequence
$$1, \frac{1}{2}, \frac{1}{2^2}, \frac{1}{2^3}, \dots, \frac{1}{2^n}, \dots$$
which, as shown in Example 4, converges to 0. Thus, from Theorem 9.1.6 we have
$$\lim_{n \to +\infty} \left[(-1)^n \frac{1}{2^n}\right] = 0$$

---

### SEQUENCES DEFINED RECURSIVELY

Some sequences do not arise from a formula for the general term, but rather from a formula or set of formulas that specify how to generate each term in the sequence from terms that precede it; such sequences are said to be defined **recursively**, and the defining formulas are called **recursion formulas**. A good example is the mechanic's rule for approximating square roots:
$$x_1 = 1, \quad x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right) \tag{2}$$
describes the sequence produced by Newton's Method to approximate $\sqrt{a}$ as a zero of the function $f(x) = x^2 - a$. Table 9.1.5 shows the first five terms in an application of the mechanic's rule to approximate $\sqrt{2}$.

##### Table 9.1.5
| $n$ | $x_1 = 1, \; x_{n+1} = \frac{1}{2}(x_n + 2/x_n)$ | Decimal Approximation |
| :---: | :--- | :---: |
| | $x_1 = 1$ (Starting value) | 1.00000000000 |
| 1 | $x_2 = \frac{1}{2}[1 + \frac{2}{1}] = \frac{3}{2}$ | 1.50000000000 |
| 2 | $x_3 = \frac{1}{2}[\frac{3}{2} + \frac{2}{3/2}] = \frac{17}{12}$ | 1.41666666667 |
| 3 | $x_4 = \frac{1}{2}[\frac{17}{12} + \frac{2}{17/12}] = \frac{577}{408}$ | 1.41421568627 |
| 4 | $x_5 = \frac{1}{2}[\frac{577}{408} + \frac{2}{577/408}] = \frac{665,857}{470,832}$ | 1.41421356237 |
| 5 | $x_6 = \frac{1}{2}[\frac{665,857}{470,832} + \frac{2}{665,857/470,832}] = \frac{886,731,088,897}{627,013,566,048}$ | 1.41421356237 |

#### Example 10
Assuming that the sequence in Table 9.1.5 converges, show that the limit is $\sqrt{2}$.

**Solution.** Assume that $x_n \to L$, where $L$ is to be determined. Since $n + 1 \to +\infty$ as $n \to +\infty$, it is also true that $x_{n+1} \to L$ as $n \to +\infty$. Thus, if we take the limit of the expression
$$x_{n+1} = \frac{1}{2}\left(x_n + \frac{2}{x_n}\right)$$
as $n \to +\infty$, we obtain
$$L = \frac{1}{2}\left(L + \frac{2}{L}\right)$$
which can be rewritten as $L^2 = 2$. The negative solution of this equation is extraneous because $x_n > 0$ for all $n$, so $L = \sqrt{2}$.

---

### QUICK CHECK EXERCISES 9.1
*(See page 607 for answers.)*

1. Consider the sequence $4, 6, 8, 10, 12, \dots$.
   (a) If $\{a_n\}_{n=1}^{+\infty}$ denotes this sequence, then $a_1 = \underline{\quad}$, $a_4 = \underline{\quad}$, and $a_7 = \underline{\quad}$. The general term is $a_n = \underline{\quad}$.
   (b) If $\{b_n\}_{n=0}^{+\infty}$ denotes this sequence, then $b_0 = \underline{\quad}$, $b_4 = \underline{\quad}$, and $b_8 = \underline{\quad}$. The general term is $b_n = \underline{\quad}$.
2. What does it mean to say that a sequence $\{a_n\}$ converges?
3. Consider sequences $\{a_n\}$ and $\{b_n\}$, where $a_n \to 2$ as $n \to +\infty$ and $b_n = (-1)^n$. Determine which of the following sequences converge and which diverge. If a sequence converges, indicate its limit.
   (a) $\{b_n\}$
   (b) $\{3a_n - 1\}$
   (c) $\{b_n^2\}$
   (d) $\{a_n + b_n\}$
   (e) $\left\{\frac{1}{a_n^2 + 3}\right\}$
   (f) $\left\{\frac{b_n}{1000}\right\}$
4. Suppose that $\{a_n\}$, $\{b_n\}$, and $\{c_n\}$ are sequences such that $a_n \le b_n \le c_n$ for all $n \ge 10$, and that $\{a_n\}$ and $\{c_n\}$ both converge to 12. Then the $\underline{\quad}$ Theorem for Sequences implies that $\{b_n\}$ converges to $\underline{\quad}$.

---

### EXERCISE SET 9.1

**1–4** In each part, find a formula for the general term of the sequence, starting with $n = 1$.
1. (a) $1, \frac{1}{3}, \frac{1}{9}, \frac{1}{27}, \dots$
   (b) $1, -\frac{1}{3}, \frac{1}{9}, -\frac{1}{27}, \dots$
   (c) $\frac{1}{2}, \frac{3}{4}, \frac{5}{6}, \frac{7}{8}, \dots$
   (d) $\frac{1}{\sqrt{\pi}}, \frac{4}{\sqrt[3]{\pi}}, \frac{9}{\sqrt[4]{\pi}}, \frac{16}{\sqrt[5]{\pi}}, \dots$
2. In each part, find two formulas for the general term of the sequence, one starting with $n = 1$ and the other with $n = 0$.
   (a) $1, -r, r^2, -r^3, \dots$
   (b) $r, -r^2, r^3, -r^4, \dots$
3. (a) Write out the first four terms of the sequence $\{1 + (-1)^n\}$, starting with $n = 0$.
   (b) Write out the first four terms of the sequence $\{\cos n\pi\}$, starting with $n = 0$.
   (c) Use the results in parts (a) and (b) to express the general term of the sequence $4, 0, 4, 0, \dots$ in two different ways, starting with $n = 0$.
4. In each part, find a formula for the general term using factorials and starting with $n = 1$.
   (a) $1 \cdot 2, \; 1 \cdot 2 \cdot 3 \cdot 4, \; 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6, \; 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 \cdot 7 \cdot 8, \dots$
   (b) $1, \; 1 \cdot 2 \cdot 3, \; 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5, \; 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 \cdot 7, \dots$

**5–6** Let $f$ be the function $f(x) = \cos\left(\frac{\pi}{2}x\right)$ and define sequences $\{a_n\}$ and $\{b_n\}$ by $a_n = f(2n)$ and $b_n = f(2n + 1)$.
5. (a) Does $\lim_{x \to +\infty} f(x)$ exist? Explain.
   (b) Evaluate $a_1, a_2, a_3, a_4,$ and $a_5$.
   (c) Does $\{a_n\}$ converge? If so, find its limit.
6. (a) Evaluate $b_1, b_2, b_3, b_4,$ and $b_5$.
   (b) Does $\{b_n\}$ converge? If so, find its limit.
   (c) Does $\{f(n)\}$ converge? If so, find its limit.

**7–22** Write out the first five terms of the sequence, determine whether the sequence converges, and if so find its limit.
7. $\left\{\frac{n}{n + 2}\right\}_{n=1}^{+\infty}$
8. $\left\{\frac{n^2}{2n + 1}\right\}_{n=1}^{+\infty}$
9. $\{2\}_{n=1}^{+\infty}$
10. $\left\{\ln\left(\frac{1}{n}\right)\right\}_{n=1}^{+\infty}$
11. $\left\{\frac{\ln n}{n}\right\}_{n=1}^{+\infty}$
12. $\left\{n \sin\frac{\pi}{n}\right\}_{n=1}^{+\infty}$
13. $\{1 + (-1)^n\}_{n=1}^{+\infty}$
14. $\left\{\frac{(-1)^{n+1}}{n^2}\right\}_{n=1}^{+\infty}$
15. $\left\{(-1)^n \frac{2n^3}{n^3 + 1}\right\}_{n=1}^{+\infty}$
16. $\left\{\frac{n}{2^n}\right\}_{n=1}^{+\infty}$
17. $\left\{\frac{(n + 1)(n + 2)}{2n^2}\right\}_{n=1}^{+\infty}$
18. $\left\{\frac{\pi^n}{4^n}\right\}_{n=1}^{+\infty}$
19. $\{n^2 e^{-n}\}_{n=1}^{+\infty}$
20. $\{\sqrt{n^2 + 3n} - n\}_{n=1}^{+\infty}$
21. $\left\{\left(\frac{n + 3}{n + 1}\right)^n\right\}_{n=1}^{+\infty}$
22. $\left\{\left(1 - \frac{2}{n}\right)^n\right\}_{n=1}^{+\infty}$

**23–30** Find the general term of the sequence, starting with $n = 1$, determine whether the sequence converges, and if so find its limit.
23. $\frac{1}{2}, \frac{3}{4}, \frac{5}{6}, \frac{7}{8}, \dots$
24. $0, \frac{1}{2^2}, \frac{2}{3^2}, \frac{3}{4^2}, \dots$
25. $\frac{1}{3}, -\frac{1}{9}, \frac{1}{27}, -\frac{1}{81}, \dots$
26. $-1, 2, -3, 4, -5, \dots$
27. $\left(1 - \frac{1}{2}\right), \left(\frac{1}{3} - \frac{1}{2}\right), \left(\frac{1}{3} - \frac{1}{4}\right), \left(\frac{1}{5} - \frac{1}{4}\right), \dots$
28. $3, \frac{3}{2}, \frac{3}{2^2}, \frac{3}{2^3}, \dots$
29. $(\sqrt{2} - \sqrt{3}), (\sqrt{3} - \sqrt{4}), (\sqrt{4} - \sqrt{5}), \dots$
30. $\frac{1}{3^5}, -\frac{1}{3^6}, \frac{1}{3^7}, -\frac{1}{3^8}, \dots$

**31–34 True–False** Determine whether the statement is true or false. Explain your answer.
31. Sequences are functions.
32. If $\{a_n\}$ and $\{b_n\}$ are sequences such that $\{a_n + b_n\}$ converges, then $\{a_n\}$ and $\{b_n\}$ converge.
33. If $\{a_n\}$ diverges, then $a_n \to +\infty$ or $a_n \to -\infty$.
34. If the graph of $y = f(x)$ has a horizontal asymptote as $x \to +\infty$, then the sequence $\{f(n)\}$ converges.

**35–36** Use numerical evidence to make a conjecture about the limit of the sequence, and then use the Squeezing Theorem for Sequences (Theorem 9.1.5) to confirm that your conjecture is correct.
35. $\lim_{n \to +\infty} \frac{\sin^2 n}{n}$
36. $\lim_{n \to +\infty} \left(\frac{1 + n}{2n}\right)^n$

#### FOCUS ON CONCEPTS
37. Give two examples of sequences, all of whose terms are between $-10$ and 10, that do not converge. Use graphs of your sequences to explain their properties.
38. (a) Suppose that $f$ satisfies $\lim_{x \to 0^+} f(x) = +\infty$. Is it possible that the sequence $\{f(1/n)\}$ converges? Explain.
    (b) Find a function $f$ such that $\lim_{x \to 0^+} f(x)$ does not exist but the sequence $\{f(1/n)\}$ converges.
39. (a) Starting with $n = 1$, write out the first six terms of the sequence $\{a_n\}$, where
    $$a_n = \begin{cases} 1, & \text{if } n \text{ is odd} \\ n, & \text{if } n \text{ is even} \end{cases}$$
    (b) Starting with $n = 1$, and considering the even and odd terms separately, find a formula for the general term of the sequence
    $$1, \frac{1}{2^2}, 3, \frac{1}{2^4}, 5, \frac{1}{2^6}, \dots$$
    (c) Starting with $n = 1$, and considering the even and odd terms separately, find a formula for the general term of the sequence
    $$1, \frac{1}{3}, \frac{1}{3}, \frac{1}{5}, \frac{1}{5}, \frac{1}{7}, \frac{1}{7}, \frac{1}{9}, \frac{1}{9}, \dots$$
    (d) Determine whether the sequences in parts (a), (b), and (c) converge. For those that do, find the limit.
40. For what positive values of $b$ does the sequence $b, 0, b^2, 0, b^3, 0, b^4, \dots$ converge? Justify your answer.
41. Assuming that the sequence given in Formula (2) of this section converges, use the method of Example 10 to show that the limit of this sequence is $\sqrt{a}$.
42. Consider the sequence
    $$a_1 = \sqrt{6}, \quad a_2 = \sqrt{6 + \sqrt{6}}, \quad a_3 = \sqrt{6 + \sqrt{6 + \sqrt{6}}}, \quad a_4 = \sqrt{6 + \sqrt{6 + \sqrt{6 + \sqrt{6}}}}, \dots$$
    (a) Find a recursion formula for $a_{n+1}$.
    (b) Assuming that the sequence converges, use the method of Example 10 to find the limit.
43. (a) A bored student enters the number 0.5 in a calculator display and then repeatedly computes the square of the number in the display. Taking $a_0 = 0.5$, find a formula for the general term of the sequence $\{a_n\}$ of numbers that appear in the display.
    (b) Try this with a calculator and make a conjecture about the limit of $a_n$.
    (c) Confirm your conjecture by finding the limit of $a_n$.
    (d) For what values of $a_0$ will this procedure produce a convergent sequence?
44. Let
    $$f(x) = \begin{cases} 2x, & 0 \le x < 0.5 \\ 2x - 1, & 0.5 \le x < 1 \end{cases}$$
    Does the sequence $f(0.2), f(f(0.2)), f(f(f(0.2))), \dots$ converge? Justify your reasoning.
45. (a) Use a graphing utility to generate the graph of the equation $y = (2^x + 3^x)^{1/x}$, and then use the graph to make a conjecture about the limit of the sequence $\{(2^n + 3^n)^{1/n}\}_{n=1}^{+\infty}$.
    (b) Confirm your conjecture by calculating the limit.
46. Consider the sequence $\{a_n\}_{n=1}^{+\infty}$ whose $n$th term is
    $$a_n = \frac{1}{n}\sum_{k=1}^n \frac{1}{1 + (k/n)}$$
    Show that $\lim_{n \to +\infty} a_n = \ln 2$ by interpreting $a_n$ as the Riemann sum of a definite integral.
47. The sequence whose terms are $1, 1, 2, 3, 5, 8, 13, 21, \dots$ is called the **Fibonacci sequence** in honor of the Italian mathematician Leonardo ("Fibonacci") da Pisa (c. 1170–1250). This sequence has the property that after starting with two 1's, each term is the sum of the preceding two.
    (a) Denoting the sequence by $\{a_n\}$ and starting with $a_1 = 1$ and $a_2 = 1$, show that
    $$\frac{a_{n+2}}{a_{n+1}} = 1 + \frac{a_n}{a_{n+1}} \quad \text{if } n \ge 1$$
    (b) Give a reasonable informal argument to show that if the sequence $\{a_{n+1}/a_n\}$ converges to some limit $L$, then the sequence $\{a_{n+2}/a_{n+1}\}$ must also converge to $L$.
    (c) Assuming that the sequence $\{a_{n+1}/a_n\}$ converges, show that its limit is $(1 + \sqrt{5})/2$.
48. If we accept the fact that the sequence $\{1/n\}_{n=1}^{+\infty}$ converges to the limit $L = 0$, then according to Definition 9.1.2, for every $\epsilon > 0$ there exists a positive integer $N$ such that $|a_n - L| = |(1/n) - 0| < \epsilon$ when $n \ge N$. In each part, find the smallest possible value of $N$ for the given value of $\epsilon$.
    (a) $\epsilon = 0.5$  
    (b) $\epsilon = 0.1$  
    (c) $\epsilon = 0.001$
49. If we accept the fact that the sequence $\left\{\frac{n}{n + 1}\right\}_{n=1}^{+\infty}$ converges to the limit $L = 1$, then according to Definition 9.1.2, for every $\epsilon > 0$ there exists an integer $N$ such that $|a_n - L| = \left|\frac{n}{n + 1} - 1\right| < \epsilon$ when $n \ge N$. In each part, find the smallest value of $N$ for the given value of $\epsilon$.
    (a) $\epsilon = 0.25$  
    (b) $\epsilon = 0.1$  
    (c) $\epsilon = 0.001$
50. Use Definition 9.1.2 to prove that
    (a) the sequence $\{1/n\}_{n=1}^{+\infty}$ converges to 0
    (b) the sequence $\left\{\frac{n}{n + 1}\right\}_{n=1}^{+\infty}$ converges to 1.
51. **Writing.** Discuss, with examples, various ways that a sequence could diverge.
52. **Writing.** Discuss the convergence of the sequence $\{r^n\}$ considering the cases $|r| < 1, |r| > 1, r = 1,$ and $r = -1$ separately.

#### QUICK CHECK ANSWERS 9.1
1. (a) $4; \; 10; \; 16; \; 2n + 2$ (b) $4; \; 12; \; 20; \; 2n + 4$
2. $\lim_{n \to +\infty} a_n$ exists
3. (a) diverges (b) converges to 5 (c) converges to 1 (d) diverges (e) converges to $1/7$ (f) diverges
4. Squeezing; 12

---

## 9.2 MONOTONE SEQUENCES

There are many situations in which it is important to know whether a sequence converges, but the value of the limit is not relevant to the problem at hand. In this section we will study several techniques that can be used to determine whether a sequence converges.

### TERMINOLOGY

> **9.2.1 DEFINITION**  
> A sequence $\{a_n\}_{n=1}^{+\infty}$ is called:  
> * **strictly increasing** if $a_1 < a_2 < a_3 < \cdots < a_n < \cdots$  
> * **increasing** if $a_1 \le a_2 \le a_3 \le \cdots \le a_n \le \cdots$  
> * **strictly decreasing** if $a_1 > a_2 > a_3 > \cdots > a_n > \cdots$  
> * **decreasing** if $a_1 \ge a_2 \ge a_3 \ge \cdots \ge a_n \ge \cdots$  
> A sequence that is either increasing or decreasing is said to be **monotone**, and a sequence that is either strictly increasing or strictly decreasing is said to be **strictly monotone**.

##### Table 9.2.1
| Sequence | Description |
| :--- | :--- |
| $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \dots, \frac{n}{n+1}, \dots$ | Strictly increasing |
| $1, \frac{1}{2}, \frac{1}{3}, \dots, \frac{1}{n}, \dots$ | Strictly decreasing |
| $1, 1, 2, 2, 3, 3, \dots$ | Increasing; not strictly increasing |
| $1, 1, \frac{1}{2}, \frac{1}{2}, \frac{1}{3}, \frac{1}{3}, \dots$ | Decreasing; not strictly decreasing |
| $1, -\frac{1}{2}, \frac{1}{3}, -\frac{1}{4}, \dots, (-1)^{n+1}\frac{1}{n}, \dots$ | Neither increasing nor decreasing |

### TESTING FOR MONOTONICITY

##### Table 9.2.2
| Difference Between Successive Terms | Ratio of Successive Terms | Conclusion |
| :---: | :---: | :---: |
| $a_{n+1} - a_n > 0$ | $a_{n+1}/a_n > 1$ | Strictly increasing |
| $a_{n+1} - a_n < 0$ | $a_{n+1}/a_n < 1$ | Strictly decreasing |
| $a_{n+1} - a_n \ge 0$ | $a_{n+1}/a_n \ge 1$ | Increasing |
| $a_{n+1} - a_n \le 0$ | $a_{n+1}/a_n \le 1$ | Decreasing |

#### Example 1
Use differences of successive terms to show that $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \dots, \frac{n}{n+1}, \dots$ is a strictly increasing sequence.

**Solution.** Let $a_n = \frac{n}{n+1}$. Then $a_{n+1} = \frac{n+1}{n+2}$. For $n \ge 1$:
$$a_{n+1} - a_n = \frac{n+1}{n+2} - \frac{n}{n+1} = \frac{n^2 + 2n + 1 - n^2 - 2n}{(n+1)(n+2)} = \frac{1}{(n+1)(n+2)} > 0$$
which proves that the sequence is strictly increasing.

#### Example 2
Use ratios of successive terms to show that the sequence in Example 1 is strictly increasing.

**Solution.**
$$\frac{a_{n+1}}{a_n} = \frac{(n+1)/(n+2)}{n/(n+1)} = \frac{n+1}{n+2} \cdot \frac{n+1}{n} = \frac{n^2 + 2n + 1}{n^2 + 2n} > 1$$
for $n \ge 1$. This proves that the sequence is strictly increasing.

#### Example 3
Let $f(x) = \frac{x}{x+1}$, so that $a_n = f(n)$. The function $f$ is increasing for $x \ge 1$ since
$$f'(x) = \frac{(x+1)(1) - x(1)}{(x+1)^2} = \frac{1}{(x+1)^2} > 0$$
Thus, $a_n = f(n) < f(n+1) = a_{n+1}$, which proves that the given sequence is strictly increasing.

##### Table 9.2.3
| Derivative of $f$ for $x \ge 1$ | Conclusion for $\{a_n = f(n)\}$ |
| :---: | :---: |
| $f'(x) > 0$ | Strictly increasing |
| $f'(x) < 0$ | Strictly decreasing |
| $f'(x) \ge 0$ | Increasing |
| $f'(x) \le 0$ | Decreasing |

### PROPERTIES THAT HOLD EVENTUALLY

> **9.2.2 DEFINITION**  
> If discarding finitely many terms from the beginning of a sequence produces a sequence with a certain property, then the original sequence is said to have that property **eventually**.

#### Example 4
Show that the sequence $\left\{\frac{10^n}{n!}\right\}_{n=1}^{+\infty}$ is eventually strictly decreasing.

**Solution.**
$$\frac{a_{n+1}}{a_n} = \frac{10^{n+1}/(n+1)!}{10^n/n!} = \frac{10^{n+1} n!}{10^n (n+1)!} = \frac{10}{n+1}$$
For $n \ge 10$, $\frac{a_{n+1}}{a_n} = \frac{10}{n+1} < 1$, so the sequence is eventually strictly decreasing.

---

### CONVERGENCE OF MONOTONE SEQUENCES

> **9.2.3 THEOREM**  
> If a sequence $\{a_n\}$ is eventually increasing, then there are two possibilities:  
> (a) There is a constant $M$, called an **upper bound** for the sequence, such that $a_n \le M$ for all $n$, in which case the sequence converges to a limit $L$ satisfying $L \le M$.  
> (b) No upper bound exists, in which case $\lim_{n \to +\infty} a_n = +\infty$.

> **9.2.4 THEOREM**  
> If a sequence $\{a_n\}$ is eventually decreasing, then there are two possibilities:  
> (a) There is a constant $M$, called a **lower bound** for the sequence, such that $a_n \ge M$ for all $n$, in which case the sequence converges to a limit $L$ satisfying $L \ge M$.  
> (b) No lower bound exists, in which case $\lim_{n \to +\infty} a_n = -\infty$.

#### Example 5
Show that the sequence $\left\{\frac{10^n}{n!}\right\}_{n=1}^{+\infty}$ converges and find its limit.

**Solution.** Since all terms are positive, it is bounded below by $M = 0$. Since it is eventually strictly decreasing, Theorem 9.2.4 guarantees that it converges to a nonnegative limit $L$. Successive terms satisfy $a_{n+1} = \frac{10}{n+1}a_n$. Taking limits:
$$L = \lim_{n \to +\infty} a_{n+1} = \lim_{n \to +\infty} \left(\frac{10}{n+1} a_n\right) = 0 \cdot L = 0$$
So $L = \lim_{n \to +\infty} \frac{10^n}{n!} = 0$. In general, for any real value of $x$,
$$\lim_{n \to +\infty} \frac{x^n}{n!} = 0 \tag{5}$$

### THE COMPLETENESS AXIOM

> **9.2.5 AXIOM (The Completeness Axiom)**  
> If a nonempty set $S$ of real numbers has an upper bound, then it has a smallest upper bound (called the **least upper bound**), and if a nonempty set $S$ of real numbers has a lower bound, then it has a largest lower bound (called the **greatest lower bound**).

#### Proof of Theorem 9.2.3
(a) Assume there exists $M$ such that $a_n \le M$ for $n = 1, 2, \dots$. By the Completeness Axiom there is a least upper bound $L$. Let $\epsilon > 0$. Since $L$ is the least upper bound, $L - \epsilon$ is not an upper bound, so there exists $a_N$ such that $a_N > L - \epsilon$. Since $\{a_n\}$ is increasing, for $n \ge N$:
$$L \ge a_n \ge a_N > L - \epsilon$$
Hence $|a_n - L| < \epsilon$ for all $n \ge N$, proving $\lim_{n \to +\infty} a_n = L \le M$.  
(b) If no upper bound exists, for any $M$ there is $a_N > M$, and for $n \ge N$, $a_n \ge a_N > M$. Thus $\lim_{n \to +\infty} a_n = +\infty$. $\blacksquare$

---

### QUICK CHECK EXERCISES 9.2
*(See page 614 for answers.)*

1. Classify each sequence as (I) increasing, (D) decreasing, or (N) neither increasing nor decreasing:
   $\{2^n\}$, $\{2^{-n}\}$, $\left\{\frac{5 - n}{n^2}\right\}$, $\left\{-\frac{1}{n^2}\right\}$, $\left\{\frac{(-1)^n}{n^2}\right\}$
2. Classify each sequence as (M) monotonic, (S) strictly monotonic, or (N) not monotonic:
   $\{n + (-1)^n\}$, $\{2n + (-1)^n\}$, $\{3n + (-1)^n\}$
3. Since $\frac{n/[2(n+1)]}{(n-1)/(2n)} = \frac{n^2}{n^2 - 1} > \underline{\quad}$, the sequence $\{(n-1)/(2n)\}$ is strictly $\underline{\quad}$.
4. Since $\frac{d}{dx}[(x - 8)^2] > 0$ for $x > \underline{\quad}$, the sequence $\{(n - 8)^2\}$ is strictly $\underline{\quad}$.

---

### EXERCISE SET 9.2

**1–6** Use the difference $a_{n+1} - a_n$ to show that the given sequence $\{a_n\}$ is strictly increasing or strictly decreasing.
1. $\left\{\frac{1}{n}\right\}_{n=1}^{+\infty}$
2. $\left\{1 - \frac{1}{n}\right\}_{n=1}^{+\infty}$
3. $\left\{\frac{n}{2n + 1}\right\}_{n=1}^{+\infty}$
4. $\left\{\frac{n}{4n - 1}\right\}_{n=1}^{+\infty}$
5. $\{n - 2^n\}_{n=1}^{+\infty}$
6. $\{n - n^2\}_{n=1}^{+\infty}$

**7–12** Use the ratio $a_{n+1}/a_n$ to show that the given sequence $\{a_n\}$ is strictly increasing or strictly decreasing.
7. $\left\{\frac{n}{2n + 1}\right\}_{n=1}^{+\infty}$
8. $\left\{\frac{2^n}{1 + 2^n}\right\}_{n=1}^{+\infty}$
9. $\{n e^{-n}\}_{n=1}^{+\infty}$
10. $\left\{\frac{10^n}{(2n)!}\right\}_{n=1}^{+\infty}$
11. $\left\{\frac{n^n}{n!}\right\}_{n=1}^{+\infty}$
12. $\left\{\frac{5^n}{2^{(n^2)}}\right\}_{n=1}^{+\infty}$

**13–16 True–False** Determine whether the statement is true or false. Explain your answer.
13. If $a_{n+1} - a_n > 0$ for all $n \ge 1$, then the sequence $\{a_n\}$ is strictly increasing.
14. A sequence $\{a_n\}$ is monotone if $a_{n+1} - a_n \neq 0$ for all $n \ge 1$.
15. Any bounded sequence converges.
16. If $\{a_n\}$ is eventually increasing, then $a_{100} < a_{200}$.

**17–20** Use differentiation to show that the given sequence is strictly increasing or strictly decreasing.
17. $\left\{\frac{n}{2n + 1}\right\}_{n=1}^{+\infty}$
18. $\left\{\frac{\ln(n + 2)}{n + 2}\right\}_{n=1}^{+\infty}$
19. $\{\tan^{-1} n\}_{n=1}^{+\infty}$
20. $\{n e^{-2n}\}_{n=1}^{+\infty}$

**21–24** Show that the given sequence is eventually strictly increasing or eventually strictly decreasing.
21. $\{2n^2 - 7n\}_{n=1}^{+\infty}$
22. $\left\{\frac{n}{n^2 + 10}\right\}_{n=1}^{+\infty}$
23. $\left\{\frac{n!}{3^n}\right\}_{n=1}^{+\infty}$
24. $\{n^5 e^{-n}\}_{n=1}^{+\infty}$

#### FOCUS ON CONCEPTS
25. Suppose that $\{a_n\}$ is a monotone sequence such that $1 \le a_n \le 2$ for all $n$. Must the sequence converge? If so, what can you say about the limit?
26. Suppose that $\{a_n\}$ is a monotone sequence such that $a_n \le 2$ for all $n$. Must the sequence converge? If so, what can you say about the limit?
27. Let $\{a_n\}$ be the sequence defined recursively by $a_1 = \sqrt{2}$ and $a_{n+1} = \sqrt{2 + a_n}$ for $n \ge 1$.
    (a) List the first three terms of the sequence.
    (b) Show that $a_n < 2$ for $n \ge 1$.
    (c) Show that $a_{n+1}^2 - a_n^2 = (2 - a_n)(1 + a_n)$ for $n \ge 1$.
    (d) Use the results in parts (b) and (c) to show that $\{a_n\}$ is a strictly increasing sequence. [Hint: If $x$ and $y$ are positive real numbers such that $x^2 - y^2 > 0$, then it follows by factoring that $x - y > 0$.]
    (e) Show that $\{a_n\}$ converges and find its limit $L$.
28. Let $\{a_n\}$ be the sequence defined recursively by $a_1 = 1$ and $a_{n+1} = \frac{1}{2}[a_n + (3/a_n)]$ for $n \ge 1$.
    (a) Show that $a_n \ge \sqrt{3}$ for $n \ge 2$. [Hint: What is the minimum value of $\frac{1}{2}[x + (3/x)]$ for $x > 0$?]
    (b) Show that $\{a_n\}$ is eventually decreasing. [Hint: Examine $a_{n+1} - a_n$ or $a_{n+1}/a_n$ and use the result in part (a).]
    (c) Show that $\{a_n\}$ converges and find its limit $L$.
29. The Beverton–Holt model is used to describe changes in a population from one generation to the next under certain assumptions. If the population in generation $n$ is given by $x_n$, the Beverton–Holt model predicts that the population in the next generation satisfies
    $$x_{n+1} = \frac{R K x_n}{K + (R - 1)x_n}$$
    for some positive constants $R$ and $K$ with $R > 1$. Let $\{x_n\}$ be the sequence of population values defined recursively by $x_1 = 60$, and for $n \ge 1, \; x_{n+1}$ is given by the Beverton–Holt model with $R = 10$ and $K = 300$.
    (a) List the first four terms of the sequence $\{x_n\}$.
    (b) If $0 < x_n < 300$, show that $0 < x_{n+1} < 300$. Conclude that $0 < x_n < 300$ for $n \ge 1$.
    (c) Show that $\{x_n\}$ is increasing.
    (d) Show that $\{x_n\}$ converges and find its limit $L$.
30. Let $\{x_n\}$ be a sequence of population values defined recursively by the Beverton–Holt model for which $x_1 > K$. Assume that the constants $R$ and $K$ satisfy $R > 1$ and $K > 0$.
    (a) If $x_n > K$, show that $x_{n+1} > K$. Conclude that $x_n > K$ for all $n \ge 1$.
    (b) Show that $\{x_n\}$ is decreasing.
    (c) Show that $\{x_n\}$ converges and find its limit $L$.
31. The goal of this exercise is to establish Formula (5), namely, $\lim_{n \to +\infty} \frac{x^n}{n!} = 0$. Let $a_n = |x|^n/n!$ and observe that the case where $x = 0$ is obvious, so we will focus on the case where $x \neq 0$.
    (a) Show that $a_{n+1} = \frac{|x|}{n + 1}a_n$.
    (b) Show that the sequence $\{a_n\}$ is eventually strictly decreasing.
    (c) Show that the sequence $\{a_n\}$ converges.
32. (a) Compare appropriate areas in the accompanying figure (Figure Ex-32) to deduce the following inequalities for $n \ge 2$:
    $$\int_1^n \ln x\,dx < \ln n! < \int_1^{n+1} \ln x\,dx$$
    (b) Use the result in part (a) to show that
    $$\frac{n^n}{e^{n-1}} < n! < \frac{(n + 1)^{n+1}}{e^n}, \quad n > 1$$
    (c) Use the Squeezing Theorem for Sequences (Theorem 9.1.5) and the result in part (b) to show that
    $$\lim_{n \to +\infty} \frac{\sqrt[n]{n!}}{n} = \frac{1}{e}$$
33. Use the left inequality in Exercise 32(b) to show that $\lim_{n \to +\infty} \sqrt[n]{n!} = +\infty$.
34. **Writing.** Give an example of an increasing sequence that is not eventually strictly increasing. What can you conclude about the terms of any such sequence? Explain.
35. **Writing.** Discuss the appropriate use of "eventually" for various properties of sequences. For example, which is a useful expression: "eventually bounded" or "eventually monotone"?

#### QUICK CHECK ANSWERS 9.2
1. I; D; N; I; N
2. N; M; S
3. 1; increasing
4. 8; eventually; increasing

---

## 9.3 INFINITE SERIES

### SUMS OF INFINITE SERIES

The purpose of this section is to discuss sums that contain infinitely many terms. The most familiar examples of such sums occur in the decimal representations of real numbers. For example, when we write $\frac{1}{3}$ in the decimal form $\frac{1}{3} = 0.3333\dots$, we mean
$$\frac{1}{3} = 0.3 + 0.03 + 0.003 + 0.0003 + \cdots$$
which suggests that the decimal representation of $\frac{1}{3}$ can be viewed as a sum of infinitely many real numbers.

> **9.3.1 DEFINITION**  
> An **infinite series** is an expression that can be written in the form
> $$\sum_{k=1}^\infty u_k = u_1 + u_2 + u_3 + \cdots + u_k + \cdots$$
> The numbers $u_1, u_2, u_3, \dots$ are called the **terms** of the series.

To obtain a precise definition of the sum, consider the sequence of (finite) sums:
$$s_1 = u_1, \quad s_2 = u_1 + u_2, \quad s_3 = u_1 + u_2 + u_3, \quad \dots, \quad s_n = \sum_{k=1}^n u_k$$
The number $s_n$ is called the **$n$th partial sum** of the series and the sequence $\{s_n\}_{n=1}^{+\infty}$ is called the **sequence of partial sums**.

> **9.3.2 DEFINITION**  
> Let $\{s_n\}$ be the sequence of partial sums of the series $u_1 + u_2 + u_3 + \cdots + u_k + \cdots$. If the sequence $\{s_n\}$ converges to a limit $S$, then the series is said to **converge** to $S$, and $S$ is called the **sum** of the series. We denote this by writing
> $$S = \sum_{k=1}^\infty u_k$$
> If the sequence of partial sums diverges, then the series is said to **diverge**. A divergent series has no sum.

#### Example 1
Determine whether the series $1 - 1 + 1 - 1 + 1 - 1 + \cdots$ converges or diverges. If it converges, find the sum.

**Solution.** The partial sums are $s_1 = 1, \; s_2 = 1 - 1 = 0, \; s_3 = 1 - 1 + 1 = 1, \; s_4 = 0$, and so forth. Thus, the sequence of partial sums is $1, 0, 1, 0, 1, 0, \dots$ (Figure 9.3.2). Since this is a divergent sequence, the given series diverges and consequently has no sum.

---

### GEOMETRIC SERIES

In many important series, each term is obtained by multiplying the preceding term by some fixed constant. Thus, if the initial term of the series is $a$ and each term is obtained by multiplying the preceding term by $r$, then the series has the form
$$\sum_{k=0}^\infty a r^k = a + ar + ar^2 + ar^3 + \cdots + ar^k + \cdots \quad (a \neq 0) \tag{5}$$
Such series are called **geometric series**, and the number $r$ is called the **ratio** for the series.

> **9.3.3 THEOREM (Convergence of Geometric Series)**  
> A geometric series
> $$\sum_{k=0}^\infty a r^k = a + ar + ar^2 + \cdots + ar^k + \cdots \quad (a \neq 0)$$
> converges if $|r| < 1$ and diverges if $|r| \ge 1$. If the series converges, then the sum is
> $$\sum_{k=0}^\infty a r^k = \frac{a}{1 - r}$$

**Proof.** Let us treat the case $|r| = 1$ first. If $r = 1$, the series is $a + a + a + \cdots$, so $s_n = (n + 1)a$ and $\lim s_n = \pm\infty$. If $r = -1$, the series is $a - a + a - a + \cdots$, so $\{s_n\}$ is $a, 0, a, 0, \dots$, which diverges.  
Now consider $|r| \neq 1$. The $n$th partial sum is $s_n = a + ar + ar^2 + \cdots + ar^n$. Multiplying by $r$ yields $r s_n = ar + ar^2 + \cdots + ar^{n+1}$. Subtracting gives $(1 - r)s_n = a - ar^{n+1}$, so
$$s_n = \frac{a - ar^{n+1}}{1 - r} = \frac{a}{1 - r}(1 - r^{n+1}) \tag{9}$$
If $|r| < 1$, then $r^{n+1} \to 0$ as $n \to +\infty$, so $\{s_n\}$ converges and $\lim_{n \to +\infty} s_n = \frac{a}{1 - r}$. If $|r| > 1$, then $r^{n+1}$ diverges, so $\{s_n\}$ diverges. $\blacksquare$

#### Example 2
In each part, determine whether the series converges, and if so find its sum.  
(a) $\sum_{k=0}^\infty \frac{5}{4^k}$  
(b) $\sum_{k=1}^\infty \frac{3^{2k}}{5^{1-k}}$  

**Solution (a).** This is a geometric series with $a = 5$ and $r = 1/4$. Since $|r| = 1/4 < 1$, the series converges and the sum is
$$\frac{a}{1 - r} = \frac{5}{1 - 1/4} = \frac{20}{3}$$

**Solution (b).** This is a geometric series in concealed form, since we can rewrite it as
$$\sum_{k=1}^\infty \frac{3^{2k}}{5^{1-k}} = \sum_{k=1}^\infty \frac{9^k}{5^{1-k}} = \sum_{k=1}^\infty 9\left(\frac{9}{5}\right)^{k-1}$$
Since $r = 9/5 > 1$, the series diverges.

#### Example 3
Find the rational number represented by the repeating decimal $0.784784784\dots$.

**Solution.** We can write $0.784784784\dots = 0.784 + 0.000784 + 0.000000784 + \cdots$, so the given decimal is the sum of a geometric series with $a = 0.784$ and $r = 0.001$. Thus,
$$0.784784784\dots = \frac{a}{1 - r} = \frac{0.784}{1 - 0.001} = \frac{0.784}{0.999} = \frac{784}{999}$$

#### Example 4
In each part, find all values of $x$ for which the series converges, and find the sum of the series for those values of $x$.  
(a) $\sum_{k=0}^\infty x^k$  
(b) $3 - \frac{3x}{2} + \frac{3x^2}{4} - \frac{3x^3}{8} + \cdots + \frac{3(-1)^k}{2^k}x^k + \cdots$  

**Solution (a).** Geometric series with $a = 1, r = x$, so it converges if $|x| < 1$ with sum $\sum_{k=0}^\infty x^k = \frac{1}{1 - x}$.

**Solution (b).** Geometric series with $a = 3$ and $r = -x/2$. It converges if $|-x/2| < 1$, or $|x| < 2$. When it converges its sum is
$$\sum_{k=0}^\infty 3\left(-\frac{x}{2}\right)^k = \frac{3}{1 - (-x/2)} = \frac{6}{2 + x}$$

---

### TELESCOPING SUMS

#### Example 5
Determine whether the series $\sum_{k=1}^\infty \frac{1}{k(k+1)} = \frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \frac{1}{3 \cdot 4} + \cdots$ converges or diverges. If it converges, find the sum.

**Solution.** By partial fractions, $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$. The $n$th partial sum is
$$s_n = \sum_{k=1}^n \left(\frac{1}{k} - \frac{1}{k+1}\right) = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \cdots + \left(\frac{1}{n} - \frac{1}{n+1}\right) = 1 - \frac{1}{n+1}$$
Thus, $\sum_{k=1}^\infty \frac{1}{k(k+1)} = \lim_{n \to +\infty} s_n = \lim_{n \to +\infty} \left(1 - \frac{1}{n+1}\right) = 1$.

---

### HARMONIC SERIES

The **harmonic series** is $\sum_{k=1}^\infty \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \cdots$. Its partial sums satisfy $s_{2^n} > \frac{n+1}{2}$. As $n \to +\infty, \; \frac{n+1}{2} \to +\infty$, so no constant $M$ is greater than or equal to every partial sum. Thus, the harmonic series diverges. (Due to Nicole Oresme, 1323–1382).

---

### QUICK CHECK EXERCISES 9.3
*(See page 623 for answers.)*

1. In mathematics, the terms "sequence" and "series" have different meanings: a $\underline{\quad}$ is a succession, whereas a $\underline{\quad}$ is a sum.
2. Consider the series $\sum_{k=1}^\infty \frac{1}{2^k}$. If $\{s_n\}$ is the sequence of partial sums, then $s_1 = \underline{\quad}, \; s_2 = \underline{\quad}, \; s_3 = \underline{\quad}, \; s_4 = \underline{\quad},$ and $s_n = \underline{\quad}$.
3. What does it mean to say that a series $\sum u_k$ converges?
4. A geometric series is a series of the form $\sum_{k=0}^\infty \underline{\quad}$. This series converges to $\underline{\quad}$ if $\underline{\quad}$. This series diverges if $\underline{\quad}$.
5. The harmonic series has the form $\sum_{k=1}^\infty \underline{\quad}$. Does the harmonic series converge or diverge?

---

### EXERCISE SET 9.3

**1–2 In each part, find exact values for the first four partial sums, find a closed form for the $n$th partial sum, and determine whether the series converges by calculating the limit of the $n$th partial sum. If the series converges, then state its sum.**
1. (a) $2 + \frac{2}{5} + \frac{2}{5^2} + \dots + \frac{2}{5^{k-1}} + \dots$  
   (b) $\frac{1}{4} + \frac{2}{4} + \frac{2^2}{4} + \dots + \frac{2^{k-1}}{4} + \dots$  
   (c) $\frac{1}{2 \cdot 3} + \frac{1}{3 \cdot 4} + \frac{1}{4 \cdot 5} + \dots + \frac{1}{(k+1)(k+2)} + \dots$
2. (a) $\sum_{k=1}^\infty \left(\frac{1}{4}\right)^k$  
   (b) $\sum_{k=1}^\infty 4^{k-1}$  
   (c) $\sum_{k=1}^\infty \left(\frac{1}{k+3} - \frac{1}{k+4}\right)$

**3–14 Determine whether the series converges, and if so find its sum.**
3. $\sum_{k=1}^\infty \left(-\frac{3}{4}\right)^{k-1}$
4. $\sum_{k=1}^\infty \left(\frac{2}{3}\right)^{k+2}$
5. $\sum_{k=1}^\infty (-1)^{k-1}\frac{7}{6^{k-1}}$
6. $\sum_{k=1}^\infty \left(-\frac{3}{2}\right)^{k+1}$
7. $\sum_{k=1}^\infty \frac{1}{(k+2)(k+3)}$
8. $\sum_{k=1}^\infty \left(\frac{1}{2^k} - \frac{1}{2^{k+1}}\right)$
9. $\sum_{k=1}^\infty \frac{1}{9k^2 + 3k - 2}$
10. $\sum_{k=2}^\infty \frac{1}{k^2 - 1}$
11. $\sum_{k=3}^\infty \frac{1}{k - 2}$
12. $\sum_{k=5}^\infty \left(\frac{e}{\pi}\right)^{k-1}$
13. $\sum_{k=1}^\infty \frac{4^{k+2}}{7^{k-1}}$
14. $\sum_{k=1}^\infty 5^{3k} 7^{1-k}$

**15–16 Match each series with the graph of its sequence of partial sums.**
15. Match a series from one of Exercises 3, 5, 7, or 9 with the graph of its sequence of partial sums.
16. Match a series from one of Exercises 4, 6, 8, or 10 with the graph of its sequence of partial sums.

**17–20 True–False Determine whether the statement is true or false. Explain your answer.**
17. An infinite series converges if its sequence of terms converges.
18. The geometric series $a + ar + ar^2 + \dots + ar^n + \dots$ converges provided $|r| < 1$.
19. The harmonic series diverges.
20. An infinite series converges if its sequence of partial sums is bounded and monotone.

**21–24 Express the repeating decimal as a fraction.**
21. $0.9999\dots$
22. $0.4444\dots$
23. $5.373737\dots$
24. $0.451141414\dots$

**25.** Recall that a terminating decimal is a decimal whose digits are all 0 from some point on ($0.5 = 0.50000\dots$, for example). Show that a decimal of the form $0.a_1 a_2 \dots a_n 9999\dots$, where $a_n \neq 9$, can be expressed as a terminating decimal.

#### FOCUS ON CONCEPTS
26. The great Swiss mathematician Leonhard Euler sometimes reached incorrect conclusions in his pioneering work on infinite series. For example, Euler deduced that $\frac{1}{2} = 1 - 1 + 1 - 1 + \dots$ and $-1 = 1 + 2 + 4 + 8 + \dots$ by substituting $x = -1$ and $x = 2$ in the formula $\frac{1}{1-x} = 1 + x + x^2 + x^3 + \dots$. What was the problem with his reasoning?
27. A ball is dropped from a height of 10 m. Each time it strikes the ground it bounces vertically to a height that is $\frac{3}{4}$ of the preceding height. Find the total distance the ball will travel if it is assumed to bounce infinitely often.
28. The accompanying figure shows an "infinite staircase" constructed from cubes. Find the total volume of the staircase, given that the largest cube has a side of length 1 and each successive cube has a side whose length is half that of the preceding cube.
29. In each part, find a closed form for the $n$th partial sum of the series, and determine whether the series converges. If so, find its sum.  
    (a) $\ln\frac{1}{2} + \ln\frac{2}{3} + \ln\frac{3}{4} + \dots + \ln\frac{k}{k+1} + \dots$  
    (b) $\ln\left(1 - \frac{1}{4}\right) + \ln\left(1 - \frac{1}{9}\right) + \ln\left(1 - \frac{1}{16}\right) + \dots + \ln\left(1 - \frac{1}{(k+1)^2}\right) + \dots$
30. Use geometric series to show that:  
    (a) $\sum_{k=0}^\infty (-1)^k x^k = \frac{1}{1+x}$ if $-1 < x < 1$  
    (b) $\sum_{k=0}^\infty (x-3)^k = \frac{1}{4-x}$ if $2 < x < 4$  
    (c) $\sum_{k=0}^\infty (-1)^k x^{2k} = \frac{1}{1+x^2}$ if $-1 < x < 1$.
31. In each part, find all values of $x$ for which the series converges, and find the sum of the series for those values of $x$.  
    (a) $x - x^3 + x^5 - x^7 + x^9 - \dots$  
    (b) $\frac{1}{x^2} + \frac{2}{x^3} + \frac{4}{x^4} + \frac{8}{x^5} + \frac{16}{x^6} + \dots$  
    (c) $e^{-x} + e^{-2x} + e^{-3x} + e^{-4x} + e^{-5x} + \dots$
32. Show that for all real values of $x$: $\sin x - \frac{1}{2}\sin^2 x + \frac{1}{4}\sin^3 x - \frac{1}{8}\sin^4 x + \dots = \frac{2\sin x}{2 + \sin x}$.
33. Let $a_1$ be any real number, and let $\{a_n\}$ be defined recursively by $a_{n+1} = \frac{1}{2}(a_n + 1)$. Make a conjecture about the limit, and confirm by expressing $a_n$ in terms of $a_1$.
34. Show: $\sum_{k=1}^\infty \frac{\sqrt{k+1} - \sqrt{k}}{\sqrt{k^2+k}} = 1$.
35. Show: $\sum_{k=1}^\infty \left(\frac{1}{k} - \frac{1}{k+2}\right) = \frac{3}{2}$.
36. Show: $\frac{1}{1 \cdot 3} + \frac{1}{2 \cdot 4} + \frac{1}{3 \cdot 5} + \dots = \frac{3}{4}$.
37. Show: $\frac{1}{1 \cdot 3} + \frac{1}{3 \cdot 5} + \frac{1}{5 \cdot 7} + \dots = \frac{1}{2}$.
38. Nicole Oresme geometric method to find the sum of $\sum_{k=1}^\infty \frac{k}{2^k} = \frac{1}{2} + \frac{2}{4} + \frac{3}{8} + \frac{4}{16} + \dots = 2$.
39. Angle $\theta$ bisected in succession: show that the sequence of angles has limit $\theta/3$.
40. Use a CAS to find the sum of the series and confirm by hand:  
    (a) $\sum_{k=1}^\infty (-1)^{k+1}\frac{2^k}{3^{2-k}}$ (b) $\sum_{k=1}^\infty \frac{3^{3k}}{5^{k-1}}$ (c) $\sum_{k=1}^\infty \frac{1}{4k^2 - 1}$.
41. **Writing.** Discuss similarities and differences between what it means for a sequence to converge and what it means for a series to converge.
42. **Writing.** Zeno's dichotomy paradox and connection to geometric series.

#### QUICK CHECK ANSWERS 9.3
1. sequence; series  
2. $1/2; \; 3/4; \; 7/8; \; 15/16; \; 1 - 1/2^n$  
3. The sequence of partial sums converges.  
4. $a r^k \; (a \neq 0); \; \frac{a}{1-r}; \; |r| < 1; \; |r| \ge 1$  
5. $1/k;$ diverge

---

## 9.4 CONVERGENCE TESTS

### THE DIVERGENCE TEST

> **9.4.1 THEOREM (The Divergence Test)**  
> (a) If $\lim_{k \to +\infty} u_k \neq 0$, then the series $\sum u_k$ diverges.  
> (b) If $\lim_{k \to +\infty} u_k = 0$, then the series $\sum u_k$ may either converge or diverge.

**Proof (a).** If $\sum u_k$ converges to $S$, then $u_k = s_k - s_{k-1} \to S - S = 0$.  
**Proof (b).** Both the convergent geometric series $\sum (1/2)^k$ and divergent harmonic series $\sum (1/k)$ have $u_k \to 0$. $\blacksquare$

> **9.4.2 THEOREM**  
> If the series $\sum u_k$ converges, then $\lim_{k \to +\infty} u_k = 0$.

#### Example 1
The series $\sum_{k=1}^\infty \frac{k}{k+1} = \frac{1}{2} + \frac{2}{3} + \frac{3}{4} + \cdots$ diverges since $\lim_{k \to +\infty} \frac{k}{k+1} = 1 \neq 0$.

### ALGEBRAIC PROPERTIES OF INFINITE SERIES

> **9.4.3 THEOREM**  
> (a) If $\sum u_k$ and $\sum v_k$ converge, then $\sum (u_k \pm v_k) = \sum u_k \pm \sum v_k$.  
> (b) If $c \neq 0$, $\sum c u_k = c \sum u_k$.  
> (c) Convergence or divergence is unaffected by deleting a finite number of terms from a series.

#### Example 2
$\sum_{k=1}^\infty \left(\frac{3}{4^k} - \frac{2}{5^{k-1}}\right) = \sum_{k=1}^\infty \frac{3}{4^k} - \sum_{k=1}^\infty \frac{2}{5^{k-1}} = \frac{3/4}{1 - 1/4} - \frac{2}{1 - 1/5} = 1 - \frac{5}{2} = -\frac{3}{2}$.

#### Example 3
(a) $\sum_{k=1}^\infty \frac{5}{k} = 5\sum_{k=1}^\infty \frac{1}{k}$ diverges (constant times harmonic series).  
(b) $\sum_{k=10}^\infty \frac{1}{k}$ diverges (harmonic series with first 9 terms deleted).

---

### THE INTEGRAL TEST

> **9.4.4 THEOREM (The Integral Test)**  
> Let $\sum u_k$ be a series with positive terms. If $f$ is a function that is decreasing and continuous on an interval $[a, +\infty)$ and such that $u_k = f(k)$ for all $k \ge a$, then
> $$\sum_{k=1}^\infty u_k \quad \text{and} \quad \int_a^{+\infty} f(x)\,dx$$
> both converge or both diverge.

#### Example 4
(a) $\sum_{k=1}^\infty \frac{1}{k}$: $\int_1^{+\infty} \frac{1}{x}\,dx = \lim_{b \to +\infty} [\ln b - \ln 1] = +\infty \implies$ diverges.  
(b) $\sum_{k=1}^\infty \frac{1}{k^2}$: $\int_1^{+\infty} \frac{1}{x^2}\,dx = \lim_{b \to +\infty} \left[1 - \frac{1}{b}\right] = 1 \implies$ converges.

---

### $p$-SERIES

A $p$-series is an infinite series of the form $\sum_{k=1}^\infty \frac{1}{k^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \cdots + \frac{1}{k^p} + \cdots$ where $p > 0$.

> **9.4.5 THEOREM (Convergence of $p$-Series)**  
> $$\sum_{k=1}^\infty \frac{1}{k^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \cdots + \frac{1}{k^p} + \cdots$$
> converges if $p > 1$ and diverges if $0 < p \le 1$.

#### Example 5
$1 + \frac{1}{\sqrt[3]{2}} + \frac{1}{\sqrt[3]{3}} + \dots + \frac{1}{\sqrt[3]{k}} + \dots$ diverges since it is a $p$-series with $p = 1/3 \le 1$.

### PROOF OF THE INTEGRAL TEST

> **9.4.6 THEOREM**  
> If $\sum u_k$ is a series with nonnegative terms, and if there is a constant $M$ such that $s_n = u_1 + u_2 + \cdots + u_n \le M$ for every $n$, then the series converges and the sum $S$ satisfies $S \le M$. If no such $M$ exists, then the series diverges.

**Proof of Theorem 9.4.4.** For $n > 1$, comparing rectangle areas under $y = f(x)$ yields (Figure 9.4.2):
$$\int_1^{n+1} f(x)\,dx < s_n < u_1 + \int_1^n f(x)\,dx \tag{2}$$
If $\int_1^{+\infty} f(x)\,dx = L < \infty$, then $s_n < u_1 + L$, so the series converges by Theorem 9.4.6. If the integral diverges, $s_n \to +\infty$ from the left inequality. $\blacksquare$

---

### QUICK CHECK EXERCISES 9.4
*(See page 631 for answers.)*

1. The divergence test says that if $\lim_{k \to +\infty} u_k \neq 0$, then the series $\sum u_k$ diverges.
2. Given that $a_1 = 3, \; \sum_{k=1}^\infty a_k = 1,$ and $\sum_{k=1}^\infty b_k = 5$, it follows that $\sum_{k=2}^\infty a_k = \underline{\quad}$ and $\sum_{k=1}^\infty (2a_k + b_k) = \underline{\quad}$.
3. Since $\int_1^{+\infty} (1/\sqrt{x})\,dx = +\infty$, the $\underline{\quad}$ test applied to the series $\sum_{k=1}^\infty \underline{\quad}$ shows that this series $\underline{\quad}$.
4. A $p$-series is a series of the form $\sum_{k=1}^\infty \underline{\quad}$. This series converges if $\underline{\quad}$. This series diverges if $\underline{\quad}$.

---

### EXERCISE SET 9.4

**1–2 Use Theorem 9.4.3 to find the sum of each series.**
1. (a) $\left(\frac{1}{2} + \frac{1}{4}\right) + \left(\frac{1}{2^2} + \frac{1}{4^2}\right) + \dots + \left(\frac{1}{2^k} + \frac{1}{4^k}\right) + \dots$  
   (b) $\sum_{k=1}^\infty \left(\frac{1}{5^k} - \frac{1}{k(k+1)}\right)$
2. (a) $\sum_{k=2}^\infty \left(\frac{1}{k^2 - 1} - \frac{7}{10^{k-1}}\right)$  
   (b) $\sum_{k=1}^\infty \left(7^{-k} 3^{k+1} - \frac{2^{k+1}}{5^k}\right)$

**3–4 For each given $p$-series, identify $p$ and determine whether the series converges.**
3. (a) $\sum_{k=1}^\infty \frac{1}{k^3}$ (b) $\sum_{k=1}^\infty \frac{1}{\sqrt{k}}$ (c) $\sum_{k=1}^\infty k^{-1}$ (d) $\sum_{k=1}^\infty k^{-2/3}$
4. (a) $\sum_{k=1}^\infty k^{-4/3}$ (b) $\sum_{k=1}^\infty \frac{1}{\sqrt[4]{k}}$ (c) $\sum_{k=1}^\infty \frac{1}{\sqrt[3]{k^5}}$ (d) $\sum_{k=1}^\infty \frac{1}{k^\pi}$

**5–6 Apply the divergence test and state what it tells you about the series.**
5. (a) $\sum_{k=1}^\infty \frac{k^2 + k + 3}{2k^2 + 1}$ (b) $\sum_{k=1}^\infty \left(1 + \frac{1}{k}\right)^k$ (c) $\sum_{k=1}^\infty \cos k\pi$ (d) $\sum_{k=1}^\infty \frac{1}{k!}$
6. (a) $\sum_{k=1}^\infty \frac{k}{e^k}$ (b) $\sum_{k=1}^\infty \ln k$ (c) $\sum_{k=1}^\infty \frac{1}{\sqrt{k}}$ (d) $\sum_{k=1}^\infty \frac{\sqrt{k}}{\sqrt{k}+3}$

**7–8 Confirm that the integral test is applicable and use it to determine whether the series converges.**
7. (a) $\sum_{k=1}^\infty \frac{1}{5k + 2}$ (b) $\sum_{k=1}^\infty \frac{1}{1 + 9k^2}$
8. (a) $\sum_{k=1}^\infty \frac{k}{1 + k^2}$ (b) $\sum_{k=1}^\infty \frac{1}{(4 + 2k)^{3/2}}$

**9–24 Determine whether the series converges.**
9. $\sum_{k=1}^\infty \frac{1}{k+6}$
10. $\sum_{k=1}^\infty \frac{3}{5^k}$
11. $\sum_{k=1}^\infty \frac{1}{\sqrt{k}+5}$
12. $\sum_{k=1}^\infty \frac{1}{\sqrt[k]{e}}$
13. $\sum_{k=1}^\infty \frac{1}{\sqrt[3]{2k-1}}$
14. $\sum_{k=3}^\infty \frac{\ln k}{k}$
15. $\sum_{k=1}^\infty \frac{k}{\ln(k+1)}$
16. $\sum_{k=1}^\infty k e^{-k^2}$
17. $\sum_{k=1}^\infty \left(1 + \frac{1}{k}\right)^{-k}$
18. $\sum_{k=1}^\infty \frac{k^2+1}{k^2+3}$
19. $\sum_{k=1}^\infty \frac{\tan^{-1} k}{1+k^2}$
20. $\sum_{k=1}^\infty \frac{1}{\sqrt{k^2+1}}$
21. $\sum_{k=1}^\infty k^2 \sin^2(1/k)$
22. $\sum_{k=1}^\infty k^2 e^{-k^3}$
23. $\sum_{k=5}^\infty 7k^{-1.01}$
24. $\sum_{k=1}^\infty \operatorname{sech}^2 k$

**25–26 Use the integral test to investigate the relationship between the value of $p$ and the convergence of the series.**
25. $\sum_{k=2}^\infty \frac{1}{k(\ln k)^p}$
26. $\sum_{k=3}^\infty \frac{1}{k(\ln k)[\ln(\ln k)]^p}$

#### FOCUS ON CONCEPTS
27. Suppose that $\sum u_k$ converges and $\sum v_k$ diverges. Show that $\sum (u_k + v_k)$ and $\sum (u_k - v_k)$ both diverge.
28. Find examples to show that if $\sum u_k$ and $\sum v_k$ both diverge, then $\sum (u_k + v_k)$ and $\sum (u_k - v_k)$ may either converge or diverge.
29–30 Determine whether each series converges or diverges:  
29. (a) $\sum_{k=1}^\infty \left[\left(\frac{2}{3}\right)^{k-1} + \frac{1}{k}\right]$ (b) $\sum_{k=1}^\infty \left[\frac{1}{3k+2} - \frac{1}{k^{3/2}}\right]$  
30. (a) $\sum_{k=2}^\infty \left[\frac{1}{k(\ln k)^2} - \frac{1}{k^2}\right]$ (b) $\sum_{k=2}^\infty \left[k e^{-k^2} + \frac{1}{k\ln k}\right]$
31–34 **True–False**  
31. If $\sum u_k$ converges to $L$, then $\sum (1/u_k)$ converges to $1/L$.  
32. If $\sum c u_k$ diverges for some constant $c$, then $\sum u_k$ must diverge.  
33. The integral test can be used to prove that a series diverges.  
34. The series $\sum_{k=1}^\infty \frac{1}{p^k}$ is a $p$-series.
35. Use a CAS to confirm $\sum_{k=1}^\infty \frac{1}{k^2} = \frac{\pi^2}{6}$ and $\sum_{k=1}^\infty \frac{1}{k^4} = \frac{\pi^4}{90}$, and find the sum of:  
    (a) $\sum_{k=1}^\infty \frac{3k^2 - 1}{k^4}$ (b) $\sum_{k=3}^\infty \frac{1}{k^2}$ (c) $\sum_{k=2}^\infty \frac{1}{(k-1)^4}$.
36. (a) Show $\int_{n+1}^{+\infty} f(x)\,dx < \sum_{k=n+1}^\infty u_k < \int_n^{+\infty} f(x)\,dx$.  
    (b) Show $s_n + \int_{n+1}^{+\infty} f(x)\,dx < S < s_n + \int_n^{+\infty} f(x)\,dx$.
37. (a) $s_n + \frac{1}{n+1} < \frac{\pi^2}{6} < s_n + \frac{1}{n}$. (b) Show $\frac{29}{18} < \frac{\pi^2}{6} < \frac{61}{36}$. (c) Check inequalities. (d) Upper and lower error bounds for $s_{10}$.
38. Error bounds on $s_{10}$ for: (a) $\sum_{k=1}^\infty \frac{1}{(2k+1)^2}$ (b) $\sum_{k=1}^\infty \frac{1}{k^2+1}$ (c) $\sum_{k=1}^\infty \frac{k}{e^k}$.
39. (a) $s_n + \frac{1}{3(n+1)^3} < \frac{\pi^4}{90} < s_n + \frac{1}{3n^3}$. (b) Find $n$ for length $\le 0.001$. (c) Approximate $\pi^4/90$ to 3 decimal places.
40. Harmonic series partial sums: (a) $\ln(n+1) < s_n < 1 + \ln n$. (b) Bounds on $s_{1,000,000}$. (c) Show $s_{10^9} < 22$. (d) Find $n$ for $s_n > 100$.
41. Integral test for $\sum_{k=1}^\infty k^2 e^{-k}$.
42. $\sum_{k=1}^\infty \frac{1}{k^3+1}$ integral test and CAS table.

#### QUICK CHECK ANSWERS 9.4
1. $\lim_{k \to +\infty} u_k \neq 0$  
2. $-2; \; 7$  
3. integral; $1/\sqrt{k}$; diverges  
4. $1/k^p; \; p > 1; \; 0 < p \le 1$

---

## 9.5 THE COMPARISON, RATIO, AND ROOT TESTS

### THE COMPARISON TEST

> **9.5.1 THEOREM (The Comparison Test)**  
> Let $\sum a_k$ and $\sum b_k$ be series with nonnegative terms and suppose that
> $$a_1 \le b_1, \; a_2 \le b_2, \; a_3 \le b_3, \dots, a_k \le b_k, \dots$$
> (a) If the "bigger series" $\sum b_k$ converges, then the "smaller series" $\sum a_k$ also converges.  
> (b) If the "smaller series" $\sum a_k$ diverges, then the "bigger series" $\sum b_k$ also diverges.

#### Informal Principles for Guessing:
* **9.5.2:** Constant terms in the denominator of $u_k$ can usually be deleted without affecting convergence/divergence.
* **9.5.3:** If a polynomial in $k$ appears as a factor in numerator or denominator of $u_k$, all but the leading term can usually be discarded.

#### Example 1
(a) $\sum_{k=1}^\infty \frac{1}{\sqrt{k} - 1/2}$ diverges by comparison with $\sum \frac{1}{\sqrt{k}}$ ($p = 1/2 \le 1$).  
(b) $\sum_{k=1}^\infty \frac{1}{2k^2 + k}$ converges by comparison with $\sum \frac{1}{2k^2}$ ($p = 2 > 1$).

---

### THE LIMIT COMPARISON TEST

> **9.5.4 THEOREM (The Limit Comparison Test)**  
> Let $\sum a_k$ and $\sum b_k$ be series with positive terms and suppose that
> $$\rho = \lim_{k \to +\infty} \frac{a_k}{b_k}$$
> If $\rho$ is finite and $\rho > 0$, then the series both converge or both diverge.

#### Example 2
(a) $\sum_{k=1}^\infty \frac{1}{\sqrt{k}+1}$: compare with $b_k = 1/\sqrt{k} \implies \rho = 1 \implies$ diverges.  
(b) $\sum_{k=1}^\infty \frac{1}{2k^2+k}$: compare with $b_k = 1/(2k^2) \implies \rho = 1 \implies$ converges.  
(c) $\sum_{k=1}^\infty \frac{3k^3 - 2k^2 + 4}{k^7 - k^3 + 2}$: compare with $b_k = 3/k^4 \implies \rho = 1 \implies$ converges.

---

### THE RATIO TEST

> **9.5.5 THEOREM (The Ratio Test)**  
> Let $\sum u_k$ be a series with positive terms and suppose that $\rho = \lim_{k \to +\infty} \frac{u_{k+1}}{u_k}$.  
> (a) If $\rho < 1$, the series converges.  
> (b) If $\rho > 1$ or $\rho = +\infty$, the series diverges.  
> (c) If $\rho = 1$, the series may converge or diverge (inconclusive).

#### Example 3
(a) $\sum \frac{1}{k!} \implies \rho = \lim \frac{1}{k+1} = 0 < 1 \implies$ converges.  
(b) $\sum \frac{k}{2^k} \implies \rho = \frac{1}{2} < 1 \implies$ converges.  
(c) $\sum \frac{k^k}{k!} \implies \rho = \lim (1 + 1/k)^k = e > 1 \implies$ diverges.  
(d) $\sum \frac{(2k)!}{4^k} \implies \rho = +\infty \implies$ diverges.  
(e) $\sum \frac{1}{2k-1} \implies \rho = 1$ (inconclusive; diverges by integral test).

---

### THE ROOT TEST

> **9.5.6 THEOREM (The Root Test)**  
> Let $\sum u_k$ be a series with positive terms and suppose that $\rho = \lim_{k \to +\infty} \sqrt[k]{u_k} = \lim_{k \to +\infty} (u_k)^{1/k}$.  
> (a) If $\rho < 1$, the series converges.  
> (b) If $\rho > 1$ or $\rho = +\infty$, the series diverges.  
> (c) If $\rho = 1$, the series may converge or diverge (inconclusive).

#### Example 4
(a) $\sum_{k=2}^\infty \left(\frac{4k-5}{2k+1}\right)^k \implies \rho = 2 > 1 \implies$ diverges.  
(b) $\sum_{k=1}^\infty \frac{1}{(\ln(k+1))^k} \implies \rho = \lim \frac{1}{\ln(k+1)} = 0 < 1 \implies$ converges.

---

### QUICK CHECK EXERCISES 9.5
*(See page 637 for answers.)*

1. The series $\sum_{k=1}^\infty \frac{2k^2+1}{2k^{8/3}-1}$ $\underline{\quad}$ by comparison with the $p$-series $\sum_{k=1}^\infty \underline{\quad}$.
2. Since $\lim_{k \to +\infty} \frac{(k+1)^3/3^{k+1}}{k^3/3^k} = \frac{1}{3}$, the series $\sum k^3/3^k$ $\underline{\quad}$ by the $\underline{\quad}$ test.
3. Since $\lim_{k \to +\infty} \frac{(k+1)!/3^{k+1}}{k!/3^k} = +\infty$, the series $\sum k!/3^k$ $\underline{\quad}$ by the $\underline{\quad}$ test.
4. Since $\lim_{k \to +\infty} (1/k^{k/2})^{1/k} = 0$, the series $\sum 1/k^{k/2}$ $\underline{\quad}$ by the $\underline{\quad}$ test.

---

### EXERCISE SET 9.5

**1–2 Make a guess about the convergence or divergence of the series, and confirm your guess using the comparison test.**
1. (a) $\sum_{k=1}^\infty \frac{1}{5k^2 - k}$ (b) $\sum_{k=1}^\infty \frac{3}{k - 1/4}$
2. (a) $\sum_{k=2}^\infty \frac{k+1}{k^2 - k}$ (b) $\sum_{k=1}^\infty \frac{2}{k^4 + k}$

**3. In each part, use the comparison test to show that the series converges.**
(a) $\sum_{k=1}^\infty \frac{1}{3^k + 5}$ (b) $\sum_{k=1}^\infty \frac{5\sin^2 k}{k!}$

**4. In each part, use the comparison test to show that the series diverges.**
(a) $\sum_{k=1}^\infty \frac{\ln k}{k}$ (b) $\sum_{k=1}^\infty \frac{k}{k^{3/2} - 1/2}$

**5–10 Use the limit comparison test to determine whether the series converges.**
5. $\sum_{k=1}^\infty \frac{4k^2 - 2k + 6}{8k^7 + k - 8}$
6. $\sum_{k=1}^\infty \frac{1}{9k + 6}$
7. $\sum_{k=1}^\infty \frac{5}{3^k + 1}$
8. $\sum_{k=1}^\infty \frac{k(k+3)}{(k+1)(k+2)(k+5)}$
9. $\sum_{k=1}^\infty \frac{1}{\sqrt[3]{8k^2 - 3k}}$
10. $\sum_{k=1}^\infty \frac{1}{(2k+3)^{17}}$

**11–16 Use the ratio test to determine whether the series converges. If the test is inconclusive, then say so.**
11. $\sum_{k=1}^\infty \frac{3^k}{k!}$
12. $\sum_{k=1}^\infty \frac{4^k}{k^2}$
13. $\sum_{k=1}^\infty \frac{1}{5k}$
14. $\sum_{k=1}^\infty k\left(\frac{1}{2}\right)^k$
15. $\sum_{k=1}^\infty \frac{k!}{k^3}$
16. $\sum_{k=1}^\infty \frac{k}{k^2+1}$

**17–20 Use the root test to determine whether the series converges. If the test is inconclusive, then say so.**
17. $\sum_{k=1}^\infty \left(\frac{3k+2}{2k-1}\right)^k$
18. $\sum_{k=1}^\infty \left(\frac{k}{100}\right)^k$
19. $\sum_{k=1}^\infty \frac{k}{5^k}$
20. $\sum_{k=1}^\infty (1 - e^{-k})^k$

**21–24 True–False Determine whether the statement is true or false. Explain your answer.**
21. The limit comparison test decides convergence based on a limit of the quotient of consecutive terms in a series.
22. If $\lim_{k \to +\infty} (u_{k+1}/u_k) = 5$, then $\sum u_k$ diverges.
23. If $\lim_{k \to +\infty} (k^2 u_k) = 5$, then $\sum u_k$ converges.
24. The root test decides convergence based on a limit of $k$th roots of terms in the sequence of partial sums for a series.

**25–49 Use any method to determine whether the series converges.**
25. $\sum_{k=0}^\infty \frac{7^k}{k!}$
26. $\sum_{k=1}^\infty \frac{1}{2k+1}$
27. $\sum_{k=1}^\infty \frac{k^2}{5^k}$
28. $\sum_{k=1}^\infty \frac{k! 10^k}{3^k}$
29. $\sum_{k=1}^\infty k^{50} e^{-k}$
30. $\sum_{k=1}^\infty \frac{k^2}{k^3+1}$
31. $\sum_{k=1}^\infty \frac{\sqrt{k}}{k^3+1}$
32. $\sum_{k=1}^\infty \frac{4}{2 + 3k^k}$
33. $\sum_{k=1}^\infty \frac{1}{\sqrt{k(k+1)}}$
34. $\sum_{k=1}^\infty \frac{2 + (-1)^k}{5^k}$
35. $\sum_{k=1}^\infty \frac{2 + \sqrt{k}}{(k+1)^3 - 1}$
36. $\sum_{k=1}^\infty \frac{4 + |\cos x|}{k^3}$
37. $\sum_{k=1}^\infty \frac{1}{1 + \sqrt{k}}$
38. $\sum_{k=1}^\infty \frac{k!}{k^k}$
39. $\sum_{k=1}^\infty \frac{\ln k}{e^k}$
40. $\sum_{k=1}^\infty \frac{k!}{e^{k^2}}$
41. $\sum_{k=0}^\infty \frac{(k+4)!}{4! k! 4^k}$
42. $\sum_{k=1}^\infty \left(\frac{k}{k+1}\right)^{k^2}$
43. $\sum_{k=1}^\infty \frac{1}{4 + 2^{-k}}$
44. $\sum_{k=1}^\infty \frac{\sqrt{k}\ln k}{k^3+1}$
45. $\sum_{k=1}^\infty \frac{\tan^{-1} k}{k^2}$
46. $\sum_{k=1}^\infty \frac{5^k + k}{k! + 3}$
47. $\sum_{k=0}^\infty \frac{(k!)^2}{(2k)!}$
48. $\sum_{k=1}^\infty \frac{[\pi(k+1)]^k}{k^{k+1}}$
49. $\sum_{k=1}^\infty \frac{\ln k}{3^k}$

**50.** For what positive values of $\alpha$ does the series $\sum_{k=1}^\infty (\alpha^k / k^\alpha)$ converge?

**51–52 Find the general term of the series and use the ratio test to show that the series converges.**
51. $1 + \frac{1 \cdot 2}{1 \cdot 3} + \frac{1 \cdot 2 \cdot 3}{1 \cdot 3 \cdot 5} + \frac{1 \cdot 2 \cdot 3 \cdot 4}{1 \cdot 3 \cdot 5 \cdot 7} + \dots$
52. $1 + \frac{1 \cdot 3}{3!} + \frac{1 \cdot 3 \cdot 5}{5!} + \frac{1 \cdot 3 \cdot 5 \cdot 7}{7!} + \dots$

**53.** Show that $\ln x < \sqrt{x}$ if $x > 0$, and use this result to investigate the convergence of:  
(a) $\sum_{k=1}^\infty \frac{\ln k}{k^2}$ (b) $\sum_{k=2}^\infty \frac{1}{(\ln k)^2}$.

#### FOCUS ON CONCEPTS
54. (a) Make a conjecture about the convergence of $\sum \sin(\pi/k)$ using local linear approximation of $\sin x$ at $x = 0$. (b) Confirm using limit comparison test.
55. (a) Use local quadratic approximation $1 - x^2/2$ for $\cos x$ at $x = 0$ to conjecture convergence of $\sum [1 - \cos(1/k)]$. (b) Confirm using limit comparison test.
56. Extended Limit Comparison Test:  
    (a) If $\lim (a_k/b_k) = 0$ and $\sum b_k$ converges, then $\sum a_k$ converges.  
    (b) If $\lim (a_k/b_k) = +\infty$ and $\sum b_k$ diverges, then $\sum a_k$ diverges.
57. Use Theorem 9.4.6 to prove the Comparison Test (Theorem 9.5.1).
58. **Writing.** What does the ratio test tell you about geometric series?
59. **Writing.** Strategy for deciding which convergence test to use.

#### QUICK CHECK ANSWERS 9.5
1. diverges; $1/k^{2/3}$  
2. converges; ratio  
3. diverges; ratio  
4. converges; root

---

## 9.6 ALTERNATING SERIES; ABSOLUTE AND CONDITIONAL CONVERGENCE

### ALTERNATING SERIES

An alternating series has terms that alternate in sign:
$$\sum_{k=1}^\infty (-1)^{k+1} a_k = a_1 - a_2 + a_3 - a_4 + \cdots \tag{1}$$
$$\sum_{k=1}^\infty (-1)^k a_k = -a_1 + a_2 - a_3 + a_4 - \cdots \tag{2}$$
where $a_k > 0$.

> **9.6.1 THEOREM (Alternating Series Test)**  
> An alternating series converges if:  
> (a) $a_1 \ge a_2 \ge a_3 \ge \cdots \ge a_k \ge \cdots$  
> (b) $\lim_{k \to +\infty} a_k = 0$

**Proof.** The even partial sums $s_{2n}$ form an increasing sequence bounded above by $a_1 \implies s_{2n} \to S_E$. The odd partial sums $s_{2n-1}$ form a decreasing sequence bounded below by $0 \implies s_{2n-1} \to S_O$. But $s_{2n-1} = s_{2n} + a_{2n}$, so $S_O = S_E + \lim a_{2n} = S_E + 0 = S_E = S$. $\blacksquare$

#### Example 1
(a) Alternating harmonic series $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots$ converges by AST.  
(b) $\sum_{k=1}^\infty (-1)^{k+1}\frac{k+3}{k(k+1)}$ converges by AST since $a_k > a_{k+1}$ and $a_k \to 0$.

---

### APPROXIMATING SUMS OF ALTERNATING SERIES

> **9.6.2 THEOREM (Alternating Series Error Bound)**  
> If an alternating series satisfies AST with sum $S$, then:  
> (a) $S$ lies between any two successive partial sums ($s_n \le S \le s_{n+1}$ or $s_{n+1} \le S \le s_n$).  
> (b) $|S - s_n| \le a_{n+1}$. The sign of $S - s_n$ is the same as the coefficient of $a_{n+1}$.

#### Example 2
Sum of alternating harmonic series is $\ln 2 = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots \approx 0.69315$.  
(a) For $n = 8$: $|\ln 2 - s_8| < a_9 = 1/9 < 0.12$. (Actual $|\ln 2 - 533/840| \approx 0.059$).  
(b) For 1-decimal place accuracy: $|S - s_n| \le 0.05 \implies a_{n+1} = \frac{1}{n+1} \le 0.05 \implies n \ge 19$. $s_{19} \approx 0.7$.

---

### ABSOLUTE & CONDITIONAL CONVERGENCE

> **9.6.3 DEFINITION**  
> A series $\sum u_k$ **converges absolutely** if $\sum |u_k|$ converges, and **diverges absolutely** if $\sum |u_k|$ diverges.

> **9.6.4 THEOREM**  
> If $\sum |u_k|$ converges, then $\sum u_k$ converges. (Absolute convergence implies convergence).

**Proof.** $0 \le u_k + |u_k| \le 2|u_k|$. Since $\sum 2|u_k|$ converges, $\sum (u_k + |u_k|)$ converges. Then $\sum u_k = \sum (u_k + |u_k|) - \sum |u_k|$ converges. $\blacksquare$

* A series that converges but diverges absolutely is **conditionally convergent** (e.g., $\sum \frac{(-1)^{k+1}}{k}$).

> **9.6.5 THEOREM (Ratio Test for Absolute Convergence)**  
> Let $\rho = \lim_{k \to +\infty} \frac{|u_{k+1}|}{|u_k|}$.  
> (a) If $\rho < 1$, the series converges absolutely (and therefore converges).  
> (b) If $\rho > 1$ or $\rho = +\infty$, the series diverges.  
> (c) If $\rho = 1$, the test is inconclusive.

#### Example 6
(a) $\sum_{k=1}^\infty \frac{(-1)^k 2^k}{k!} \implies \rho = \lim \frac{2}{k+1} = 0 < 1 \implies$ converges absolutely.  
(b) $\sum_{k=1}^\infty \frac{(-1)^k (2k-1)!}{3^k} \implies \rho = +\infty \implies$ diverges.

---

### QUICK CHECK EXERCISES 9.6
*(See page 648 for answers.)*

1. What characterizes an alternating series?
2. (a) $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k^2}$ converges by AST since $\underline{\quad}$ and $\underline{\quad}$. (b) If $S = \sum_{k=1}^\infty \frac{(-1)^{k+1}}{k^2}$ and $s_9 = \sum_{k=1}^9 \frac{(-1)^{k+1}}{k^2}$, then $|S - s_9| < \underline{\quad}$.
3. Classify as conditionally convergent, absolutely convergent, or divergent:  
   (a) $\sum \frac{(-1)^{k+1}}{k}$ (b) $\sum (-1)^k \frac{3k-1}{9k+15}$ (c) $\sum \frac{(-1)^k}{k(k+2)}$ (d) $\sum \frac{(-1)^{k+1}}{\sqrt[4]{k^3}}$
4. Given $\lim \frac{(k+1)^4/4^{k+1}}{k^4/4^k} = 1/4$, is $\sum (-1)^k k^4/4^k$ conditionally convergent, absolutely convergent, or divergent?

---

### EXERCISE SET 9.6

**1–2 Show that the series converges by confirming that it satisfies the hypotheses of the alternating series test (Theorem 9.6.1).**
1. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{2k+1}$
2. $\sum_{k=1}^\infty (-1)^{k+1}\frac{k}{3^k}$

**3–6 Determine whether the alternating series converges; justify your answer.**
3. $\sum_{k=1}^\infty (-1)^{k+1}\frac{k+1}{3k+1}$
4. $\sum_{k=1}^\infty (-1)^{k+1}\frac{k+1}{\sqrt{k}+1}$
5. $\sum_{k=1}^\infty (-1)^{k+1} e^{-k}$
6. $\sum_{k=3}^\infty (-1)^k \frac{\ln k}{k}$

**7–12 Use the ratio test for absolute convergence (Theorem 9.6.5) to determine whether the series converges or diverges. If the test is inconclusive, say so.**
7. $\sum_{k=1}^\infty \left(-\frac{3}{5}\right)^k$
8. $\sum_{k=1}^\infty (-1)^{k+1}\frac{2^k}{k!}$
9. $\sum_{k=1}^\infty (-1)^{k+1}\frac{3^k}{k^2}$
10. $\sum_{k=1}^\infty (-1)^k \frac{k}{5^k}$
11. $\sum_{k=1}^\infty (-1)^k \frac{k^3}{e^k}$
12. $\sum_{k=1}^\infty (-1)^{k+1}\frac{k^k}{k!}$

**13–28 Classify each series as absolutely convergent, conditionally convergent, or divergent.**
13. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{3k}$
14. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k^{4/3}}$
15. $\sum_{k=1}^\infty \frac{(-4)^k}{k^2}$
16. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k!}$
17. $\sum_{k=1}^\infty \frac{\cos k\pi}{k}$
18. $\sum_{k=3}^\infty (-1)^k \frac{\ln k}{k}$
19. $\sum_{k=1}^\infty (-1)^{k+1}\frac{k+2}{k(k+3)}$
20. $\sum_{k=1}^\infty \frac{(-1)^{k+1}k^2}{k^3+1}$
21. $\sum_{k=1}^\infty \sin\left(\frac{k\pi}{2}\right)$
22. $\sum_{k=1}^\infty \frac{\sin k}{k^3}$
23. $\sum_{k=2}^\infty \frac{(-1)^k}{k\ln k}$
24. $\sum_{k=1}^\infty \frac{(-1)^k}{\sqrt{k(k+1)}}$
25. $\sum_{k=2}^\infty \left(-\frac{1}{\ln k}\right)^k$
26. $\sum_{k=1}^\infty \frac{k\cos k\pi}{k^2+1}$
27. $\sum_{k=1}^\infty \frac{(-1)^{k+1}k!}{(2k-1)!}$
28. $\sum_{k=1}^\infty (-1)^{k+1}\frac{3^{2k-1}}{k^2+1}$

**29–32 True–False Determine whether the statement is true or false. Explain your answer.**
29. An alternating series is one whose terms alternate between even and odd.
30. If a series satisfies the hypothesis of the alternating series test, then the sequence of partial sums of the series oscillates between overestimates and underestimates for the sum of the series.
31. If a series converges, then either it converges absolutely or it converges conditionally.
32. If $\sum (u_k)^2$ converges, then $\sum u_k$ converges absolutely.

**33–36 For the stated value of $n$, find an upper bound on the absolute error that results if the sum is approximated by $s_n$.**
33. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k}; \; n = 7$
34. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k!}; \; n = 5$
35. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{\sqrt{k}}; \; n = 99$
36. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{(k+1)\ln(k+1)}; \; n = 3$

**37–40 Find a value of $n$ for which $s_n$ is ensured to approximate the sum to the stated accuracy.**
37. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k}; \; |\text{error}| < 0.0001$
38. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k!}; \; |\text{error}| < 0.00001$
39. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{\sqrt{k}};$ two decimal places
40. $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{(k+1)\ln(k+1)};$ one decimal place

**41–42 Error on $s_{10}$ for geometric series; compare with exact sum:**
41. $\frac{3}{4} - \frac{3}{8} + \frac{3}{16} - \frac{3}{32} + \dots$
42. $1 - \frac{2}{3} + \frac{4}{9} - \frac{8}{27} + \dots$

**43–46 Approximate the sum to two decimal places:**
43. $1 - \frac{1}{3!} + \frac{1}{5!} - \frac{1}{7!} + \dots$
44. $1 - \frac{1}{2!} + \frac{1}{4!} - \frac{1}{6!} + \dots$
45. $\frac{1}{1 \cdot 2} - \frac{1}{2 \cdot 2^2} + \frac{1}{3 \cdot 2^3} - \frac{1}{4 \cdot 2^4} + \dots$
46. $\frac{1}{1^5 + 4 \cdot 1} - \frac{1}{3^5 + 4 \cdot 3} + \frac{1}{5^5 + 4 \cdot 5} - \frac{1}{7^5 + 4 \cdot 7} + \dots$

#### FOCUS ON CONCEPTS
47. CAS error bound on $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots$.
48. Prove: If $\sum a_k$ converges absolutely, then $\sum a_k^2$ converges.
49. (a) Example where $\sum a_k$ converges but $\sum a_k^2$ diverges. (b) Example where $\sum a_k^2$ converges but $\sum a_k$ diverges.
50. Decomposing series into positive and negative parts $p_k, q_k$.
51. Rearrangement of conditionally convergent series: show that rearranging $\ln 2$ can yield $\frac{1}{2}\ln 2$.
52–54 Rearranging absolutely convergent series:  
52. Show $\frac{\pi^2}{8} = 1 + \frac{1}{3^2} + \frac{1}{5^2} + \frac{1}{7^2} + \dots$ from $\frac{\pi^2}{6} = \sum \frac{1}{k^2}$.  
53. Show $\frac{\pi^2}{12} = 1 - \frac{1}{2^2} + \frac{1}{3^2} - \frac{1}{4^2} + \dots$.  
54. Show $\frac{\pi^4}{96} = 1 + \frac{1}{3^4} + \frac{1}{5^4} + \frac{1}{7^4} + \dots$ from $\frac{\pi^4}{90} = \sum \frac{1}{k^4}$.
55. **Writing.** Discuss importance of hypotheses (a) and (b) of AST using $1 - \frac{1}{2} + \frac{2}{3} - \frac{1}{3} + \frac{2}{4} - \frac{1}{4} + \dots$.
56. **Writing.** Discuss how conditional convergence is "conditional".

#### QUICK CHECK ANSWERS 9.6
1. Terms alternate between positive and negative.  
2. (a) $1 \ge 1/4 \ge 1/9 \ge \cdots \ge 1/k^2 \ge 1/(k+1)^2 \ge \cdots; \; \lim_{k \to +\infty} 1/k^2 = 0$ (b) $1/100$  
3. (a) conditionally convergent (b) divergent (c) absolutely convergent (d) conditionally convergent  
4. absolutely convergent

---

## 9.7 MACLAURIN AND TAYLOR POLYNOMIALS

### LOCAL QUADRATIC APPROXIMATIONS

$$f(x) \approx f(x_0) + f'(x_0)(x - x_0) \tag{1}$$
$$f(x) \approx f(0) + f'(0)x + \frac{f''(0)}{2}x^2 \tag{4}$$

#### Example 1
For $e^x$ at $x = 0$: local linear is $1 + x$; local quadratic is $1 + x + \frac{x^2}{2}$.

### MACLAURIN POLYNOMIALS

> **9.7.2 DEFINITION**  
> If $f$ can be differentiated $n$ times at 0:
> $$p_n(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots + \frac{f^{(n)}(0)}{n!}x^n = \sum_{k=0}^n \frac{f^{(k)}(0)}{k!}x^k \tag{7, 11}$$

> **Biographical Notes:**  
> * **Colin Maclaurin (1698–1746):** Scottish mathematician, author of *A Treatise of Fluxions* (1742).  
> * **Augustin Louis Cauchy (1789–1857):** French mathematician who brought rigor and modern analysis to calculus, publishing over 700 papers.

#### Example 2
Maclaurin polynomials for $e^x$: $p_n(x) = 1 + x + \frac{x^2}{2!} + \cdots + \frac{x^n}{n!}$.

#### Example 3
(a) For $\sin x$: $p_{2k+1}(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots + (-1)^k \frac{x^{2k+1}}{(2k+1)!}$.  
(b) For $\cos x$: $p_{2k}(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots + (-1)^k \frac{x^{2k}}{(2k)!}$.

### TAYLOR POLYNOMIALS

> **9.7.3 DEFINITION**  
> If $f$ can be differentiated $n$ times at $x_0$:
> $$p_n(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \cdots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k \tag{9, 10}$$

> **Brook Taylor (1685–1731):** English mathematician, studied perspective, string vibrations, and published the famous Taylor's theorem in 1715.

#### Example 4
Taylor polynomials for $\ln x$ about $x = 2$:
$$p_3(x) = \ln 2 + \frac{1}{2}(x - 2) - \frac{1}{8}(x - 2)^2 + \frac{1}{24}(x - 2)^3$$

#### Example 5
Maclaurin polynomial for $\frac{1}{1-x}$: $p_n(x) = \sum_{k=0}^n x^k = 1 + x + x^2 + \cdots + x^n$.

#### Example 6
Taylor polynomial for $1/x$ about $x = 1$: $p_n(x) = \sum_{k=0}^n (-1)^k (x - 1)^k$.

### THE $n$TH REMAINDER

$$f(x) = p_n(x) + R_n(x) \tag{13}$$

> **9.7.4 THEOREM (The Remainder Estimation Theorem / Lagrange Error Bound)**  
> If $|f^{(n+1)}(x)| \le M$ for all $x$ in an interval containing $x_0$, then
> $$|R_n(x)| \le \frac{M}{(n+1)!}|x - x_0|^{n+1} \tag{14}$$

#### Example 7
Approximate $e$ using $e^x$ at $x = 1$: for 5 decimal places, $\frac{3}{(n+1)!} \le 0.000005 \implies (n+1)! \ge 600,000 \implies n = 9$.
$$e \approx 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{9!} \approx 2.71828$$

#### Example 8
Approximate $\cos x \approx 1 - x^2/2!$ on $|x| \le 0.3309$ to ensure $|R_3(x)| \le 0.0005$.

---

### QUICK CHECK EXERCISES 9.7
*(See page 659 for answers.)*

1. $p_3(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3$
2. For $f(x) = e^{2x}$: $p_3(x) = 1 + 2x + 2x^2 + \frac{4}{3}x^3$
3. For $f(2) = 3, f'(2) = -4, f''(2) = 10$: $p_2(x) = 3 - 4(x - 2) + 5(x - 2)^2$
4. For $f(x) = x^5$ about $x = -1$: $p_3(x) = -1 + 5(x+1) - 10(x+1)^2 + 10(x+1)^3$
5. (a) $R_n(x) = f(x) - p_n(x)$ (b) $|R_4(x)| \le \frac{20}{5!}|x - 2|^5 = \frac{1}{6}|x - 2|^5$

---

### EXERCISE SET 9.7

**1–2 Find local quadratic and linear approximations at $x_0$:**
1. (a) $f(x) = e^{-x}; x_0 = 0$ (b) $f(x) = \cos x; x_0 = 0$
2. (a) $f(x) = \sin x; x_0 = \pi/2$ (b) $f(x) = \sqrt{x}; x_0 = 1$
3. (a) Quadratic approximation of $\sqrt{x}$ at $x_0 = 1$. (b) Approximate $\sqrt{1.1}$.
4. (a) Quadratic approximation of $\cos x$ at $x_0 = 0$. (b) Approximate $\cos 2^\circ$.
5. Approximate $\tan 61^\circ$.
6. Approximate $\sqrt{36.03}$.

**7–16 Find Maclaurin polynomials $n = 0, 1, 2, 3, 4$ and $n$th polynomial in sigma notation:**
7. $e^{-x}$ 8. $e^{ax}$ 9. $\cos\pi x$ 10. $\sin\pi x$ 11. $\ln(1+x)$ 12. $\frac{1}{1+x}$ 13. $\cosh x$ 14. $\sinh x$ 15. $x\sin x$ 16. $x e^x$

**17–24 Find Taylor polynomials $n = 0, 1, 2, 3, 4$ about $x_0$ and in sigma notation:**
17. $e^x; x_0 = 1$ 18. $e^{-x}; x_0 = \ln 2$ 19. $1/x; x_0 = -1$ 20. $\frac{1}{x+2}; x_0 = 3$
21. $\sin\pi x; x_0 = 1/2$ 22. $\cos x; x_0 = \pi/2$ 23. $\ln x; x_0 = 1$ 24. $\ln x; x_0 = e$

**25–26 Polynomials:**
25. (a) Third Maclaurin of $1 + 2x - x^2 + x^3$. (b) Third Taylor about $x = 1$.
26. (a) $n$th Maclaurin of $\sum c_k x^k$. (b) $n$th Taylor of $\sum c_k (x-1)^k$.

**27–30 First four distinct Taylor polynomials:**
27. $e^{-2x}; x_0 = 0$ 28. $\sin x; x_0 = \pi/2$ 29. $\cos x; x_0 = \pi$ 30. $\ln(x+1); x_0 = 0$

**31–34 True–False**
31. The tangent line is a first-degree Taylor polynomial.
32. Graph of $f$ and its Maclaurin polynomial have common $y$-intercept.
33. $p_6^{(4)}(x_0) = 4! f^{(4)}(x_0)$.
34. $|e^2 - p_4(2)| \le 9/5!$.

**35–36 Approximations:**
35. $\sqrt{e}$ to 4 decimal places.
36. $1/e$ to 3 decimal places.

#### FOCUS ON CONCEPTS
37. Matching $p(x) = 1 - x + 2x^2$ to graphs.
38. Given $f(1)=2, f'(1)=-3, f''(1)=0, f'''(1)=6$, construct Taylor polynomials.
39. Local linear and quadratic approximations for $e^{\sin x}$.
40. Sector of radius $r$, central angle $2\alpha \implies x \approx r\alpha^2/2$; Earth equator chord divergence.
41. Interval $[0, b]$ for $e^x \approx 1 + x + x^2/2$.
42. Taylor polynomial for $\sinh x$ about $x = \ln 4$.
43–46 Remainder estimation intervals for $\sin x, \cos x, \frac{1}{1+x^2}, \ln(1+x)$.

#### QUICK CHECK ANSWERS 9.7
1. $f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3$  
2. $1; 2; 2; 4/3$  
3. $3 - 4(x - 2) + 5(x - 2)^2$  
4. $-1; 5; -10; 10$  
5. (a) $f(x) - p_n(x)$ (b) $\frac{1}{6}|x - 2|^5$

---

## 9.8 MACLAURIN AND TAYLOR SERIES; POWER SERIES

### MACLAURIN AND TAYLOR SERIES

> **9.8.1 DEFINITION**  
> Taylor series for $f$ about $x = x_0$:
> $$\sum_{k=0}^\infty \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \cdots \tag{1}$$
> Maclaurin series ($x_0 = 0$):
> $$\sum_{k=0}^\infty \frac{f^{(k)}(0)}{k!}x^k = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots \tag{2}$$

#### Example 1
(a) $e^x = \sum_{k=0}^\infty \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$  
(b) $\sin x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$  
(c) $\cos x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$  
(d) $\frac{1}{1-x} = \sum_{k=0}^\infty x^k = 1 + x + x^2 + x^3 + \cdots$

#### Example 2
Taylor series for $1/x$ about $x = 1$: $\sum_{k=0}^\infty (-1)^k (x - 1)^k = 1 - (x - 1) + (x - 1)^2 - (x - 1)^3 + \cdots$.

---

### POWER SERIES IN $x$ AND $x - x_0$

$$\sum_{k=0}^\infty c_k x^k = c_0 + c_1 x + c_2 x^2 + \cdots \tag{3}$$
$$\sum_{k=0}^\infty c_k (x - x_0)^k = c_0 + c_1 (x - x_0) + c_2 (x - x_0)^2 + \cdots$$

> **9.8.2 & 9.8.3 THEOREMS (Radius and Interval of Convergence)**  
> For any power series $\sum c_k (x - x_0)^k$, exactly one of the following is true:  
> (a) Converges only for $x = x_0$ ($R = 0$).  
> (b) Converges absolutely for all $x$ ($R = +\infty$).  
> (c) Converges absolutely for $|x - x_0| < R$ and diverges for $|x - x_0| > R$. At endpoints $x = x_0 \pm R$, it may converge absolutely, conditionally, or diverge.

#### Example 3
(a) $\sum x^k \implies R = 1$, interval $(-1, 1)$.  
(b) $\sum \frac{x^k}{k!} \implies R = +\infty$, interval $(-\infty, +\infty)$.  
(c) $\sum k! x^k \implies R = 0$, interval $\{0\}$.  
(d) $\sum \frac{(-1)^k x^k}{3^k (k+1)} \implies R = 3$, interval $(-3, 3]$.

#### Example 4
$\sum_{k=1}^\infty \frac{(x-5)^k}{k^2} \implies R = 1$, interval $[4, 6]$.

---

### BESSEL FUNCTIONS
* $J_0(x) = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{2^{2k}(k!)^2} = 1 - \frac{x^2}{2^2(1!)^2} + \frac{x^4}{2^4(2!)^2} - \cdots \quad (R = +\infty)$
* $J_1(x) = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{2^{2k+1} k!(k+1)!} = \frac{x}{2} - \frac{x^3}{2^3(1!)(2!)} + \cdots \quad (R = +\infty)$

---

### QUICK CHECK EXERCISES 9.8
*(See page 668 for answers.)*

1. $\sum_{k=0}^\infty \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k$
2. $\lim |u_{k+1}/u_k| = 2|x| \implies R = 1/2$.
3. $\lim |u_{k+1}/u_k| = 0 \implies (-\infty, +\infty)$.
4. (a) 1 (b) converges (c) diverges (d) $[3, 5)$

---

### EXERCISE SET 9.8

**1–10 Maclaurin series in sigma notation:**
1. $e^{-x}$ 2. $e^{ax}$ 3. $\cos\pi x$ 4. $\sin\pi x$ 5. $\ln(1+x)$ 6. $\frac{1}{1+x}$ 7. $\cosh x$ 8. $\sinh x$ 9. $x\sin x$ 10. $x e^x$

**11–18 Taylor series in sigma notation:**
11. $e^x; x_0 = 1$ 12. $e^{-x}; x_0 = \ln 2$ 13. $1/x; x_0 = -1$ 14. $\frac{1}{x+2}; x_0 = 3$
15. $\sin\pi x; x_0 = 1/2$ 16. $\cos x; x_0 = \pi/2$ 17. $\ln x; x_0 = 1$ 18. $\ln x; x_0 = e$

**19–22 Interval of convergence and represented function:**
19. $1 - x + x^2 - x^3 + \dots = \frac{1}{1+x}, \; (-1, 1)$
20. $1 + x^2 + x^4 + \dots = \frac{1}{1-x^2}, \; (-1, 1)$
21. $1 + (x-2) + (x-2)^2 + \dots = \frac{1}{3-x}, \; (1, 3)$
22. $1 - (x+3) + (x+3)^2 - \dots = \frac{1}{x+4}, \; (-4, -2)$

**23–24 Domain and function values:**
23. $f(x) = \sum (-1)^k \frac{x^k}{2^k}$; (a) domain $(-2, 2)$, (b) $f(0)=1, f(1)=2/3$.
24. $f(x) = \sum (-1)^k \frac{(x-5)^k}{3^k}$; (a) domain $(2, 8)$, (b) $f(3)=3/5, f(6)=3/4$.

**25–28 True–False**
25. If converges conditionally at $x = 3$, converges for $|x| < 3$ and diverges for $|x| > 3$.
26. Ratio test is useful at endpoints.
27. Maclaurin series for polynomial has $R = +\infty$.
28. $\sum x^k/k!$ converges if $|x| < 1$.

**29–50 Radius and interval of convergence:**
29. $\sum \frac{x^k}{k+1}$ 30. $\sum 3^k x^k$ 31. $\sum \frac{(-1)^k x^k}{k!}$ 32. $\sum \frac{k!}{2^k} x^k$
33. $\sum \frac{5^k}{k^2}x^k$ 34. $\sum \frac{x^k}{\ln k}$ 35. $\sum \frac{x^k}{k(k+1)}$ 36. $\sum \frac{(-2)^k x^{k+1}}{k+1}$
37. $\sum \frac{(-1)^{k-1}x^k}{\sqrt{k}}$ 38. $\sum \frac{(-1)^k x^{2k}}{(2k)!}$ 39. $\sum \frac{3^k}{k!}x^k$ 40. $\sum \frac{(-1)^{k+1}x^k}{k(\ln k)^2}$
41. $\sum \frac{x^k}{1+k^2}$ 42. $\sum \frac{(-1)^k x^{2k+1}}{(2k+1)!}$ 43. $\sum \left(\frac{3}{4}\right)^k (x+5)^k$ 44. $\sum \frac{(x-3)^k}{2^k}$
45. $\sum \frac{(-1)^{k+1}(x+1)^k}{k}$ 46. $\sum \frac{(-1)^k (x-4)^k}{(k+1)^2}$ 47. $\sum \frac{(-1)^k (x+1)^{2k+1}}{k^2+4}$ 48. $\sum \frac{(2k+1)!}{k^3}(x-2)^k$
49. $\sum \frac{\pi^k(x-1)^{2k}}{(2k+1)!}$ 50. $\sum \frac{(2x-3)^k}{4^{2k}}$

**51–53 Special Functions & Proofs:**
51. Root test on $\sum \frac{x^k}{(\ln k)^k}$.
52. Domain of $f(x) = \sum \frac{1 \cdot 3 \cdot 5 \cdots (2k-1)}{(2k-2)!}x^k$.
53. Show $\sum (-1)^k \frac{x^k}{(2k)!}$ represents $\cos\sqrt{x}$ for $x \ge 0$ and $\cosh\sqrt{-x}$ for $x < 0$.

#### FOCUS ON CONCEPTS
54. Partial sum graphs approximating $1/(1-x)$.
55. (a) Even functions have zero odd coefficients. (b) Odd functions have zero even coefficients.
56–58 Radius of convergence operations on $\sum c_k (x-x_0)^k$ and $\sum d_k (x-x_0)^k$.
59. Radius of $\sum \frac{(pk)!}{(k!)^p}x^k$ is $1/p^p$.
60. Radius of $\sum \frac{(k+p)!}{k!(k+q)!}x^k$ is $+\infty$.
61. $J_1(x)$ converges for all $x$.
62. Approximate $J_0(1)$ and $J_1(1)$ to 4 decimal places.
63. Riemann zeta function $\zeta(x) = \sum_{k=1}^\infty \frac{1}{k^x}$.
64–66 Theorems on radius of convergence and conditional convergence at endpoints.
67. **Writing.** Sine from unit circle vs Maclaurin series.

#### QUICK CHECK ANSWERS 9.8
1. $\frac{f^{(k)}(x_0)}{k!}(x - x_0)^k$  
2. $1/2$  
3. $(-\infty, +\infty)$  
4. (a) 1 (b) converges (c) diverges (d) $[3, 5)$

---

## 9.9 CONVERGENCE OF TAYLOR SERIES

### THE CONVERGENCE PROBLEM

> **9.9.2 THEOREM**  
> $f(x) = \sum_{k=0}^\infty \frac{f^{(k)}(x_0)}{k!}(x - x_0)^k$ holds at $x$ if and only if $\lim_{n \to +\infty} R_n(x) = 0$.

#### Example 1
$\cos x = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!}$ converges to $\cos x$ for all $x$ since $|R_n(x)| \le \frac{|x|^{n+1}}{(n+1)!} \to 0$.

#### Example 2
Approximating $\sin 3^\circ = \sin(\pi/60)$: using 3rd degree polynomial gives $\sin 3^\circ \approx \frac{\pi}{60} - \frac{(\pi/60)^3}{3!} \approx 0.05234$.

#### Example 3
$e^x = \sum_{k=0}^\infty \frac{x^k}{k!}$ converges to $e^x$ for all $x$.

### APPROXIMATING LOGARITHMS & $\pi$
* $\ln\left(\frac{1+x}{1-x}\right) = 2\left(x + \frac{x^3}{3} + \frac{x^5}{5} + \frac{x^7}{7} + \cdots\right) \quad (-1 < x < 1)$ (James Gregory, 1668)
* $\tan^{-1} x = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots \quad (-1 \le x \le 1)$
* $\frac{\pi}{4} = 4\tan^{-1}(1/5) - \tan^{-1}(1/239)$ (Machin's formula)

### BINOMIAL SERIES

$$(1 + x)^m = 1 + \sum_{k=1}^\infty \frac{m(m-1)\cdots(m-k+1)}{k!}x^k \quad (|x| < 1) \tag{17–18}$$

#### Example 4
(a) $\frac{1}{(1+x)^2} = 1 - 2x + 3x^2 - 4x^3 + 5x^4 - \cdots = \sum_{k=0}^\infty (-1)^k(k+1)x^k$  
(b) $\frac{1}{\sqrt{1+x}} = 1 - \frac{1}{2}x + \frac{1 \cdot 3}{2^2 \cdot 2!}x^2 - \frac{1 \cdot 3 \cdot 5}{2^3 \cdot 3!}x^3 + \cdots = 1 + \sum_{k=1}^\infty (-1)^k \frac{1 \cdot 3 \cdot 5 \cdots (2k-1)}{2^k k!}x^k$

### TABLE 9.9.1: SOME IMPORTANT MACLAURIN SERIES
| Function | Maclaurin Series | Interval of Convergence |
| :--- | :--- | :--- |
| $\frac{1}{1-x}$ | $\sum_{k=0}^\infty x^k = 1 + x + x^2 + x^3 + \dots$ | $-1 < x < 1$ |
| $\frac{1}{1+x^2}$ | $\sum_{k=0}^\infty (-1)^k x^{2k} = 1 - x^2 + x^4 - x^6 + \dots$ | $-1 < x < 1$ |
| $e^x$ | $\sum_{k=0}^\infty \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$ | $-\infty < x < +\infty$ |
| $\sin x$ | $\sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$ | $-\infty < x < +\infty$ |
| $\cos x$ | $\sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$ | $-\infty < x < +\infty$ |
| $\ln(1+x)$ | $\sum_{k=1}^\infty \frac{(-1)^{k+1} x^k}{k} = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$ | $-1 < x \le 1$ |
| $\tan^{-1} x$ | $\sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{2k+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \dots$ | $-1 \le x \le 1$ |
| $\sinh x$ | $\sum_{k=0}^\infty \frac{x^{2k+1}}{(2k+1)!} = x + \frac{x^3}{3!} + \frac{x^5}{5!} + \dots$ | $-\infty < x < +\infty$ |
| $\cosh x$ | $\sum_{k=0}^\infty \frac{x^{2k}}{(2k)!} = 1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \dots$ | $-\infty < x < +\infty$ |
| $(1+x)^m$ | $1 + \sum_{k=1}^\infty \frac{m(m-1)\cdots(m-k+1)}{k!}x^k$ | $-1 < x < 1^*$ |

---

### QUICK CHECK EXERCISES 9.9
*(See page 677 for answers.)*

1. $\cos x = \sum_{k=0}^\infty (-1)^k \frac{x^{2k}}{(2k)!}$
2. $e^x = \sum_{k=0}^\infty \frac{x^k}{k!}$
3. $\ln(1+x) = \sum_{k=1}^\infty (-1)^{k+1}\frac{x^k}{k}$ for $x \in (-1, 1]$.
4. $(1+x)^m = 1 + \sum_{k=1}^\infty \frac{m(m-1)\cdots(m-k+1)}{k!}x^k$ if $|x| < 1$.

---

### EXERCISE SET 9.9

**1–2 Proofs:**
1. Prove Taylor series for $\sin x$ about $x = \pi/4$ converges for all $x$.
2. Prove Taylor series for $e^x$ about $x = 1$ converges for all $x$.

**3–10 Approximations:**
3. $\sin 4^\circ$ to 5 decimal places.
4. $\cos 3^\circ$ to 3 decimal places.
5. $\cos 0.1$ to 5 decimal places.
6. $\tan^{-1} 0.1$ to 3 decimal places.
7. $\sin 85^\circ$ to 4 decimal places.
8. $\cos(-175^\circ)$ to 4 decimal places.
9. $\sinh 0.5$ to 3 decimal places.
10. $\cosh 0.1$ to 3 decimal places.

**11–12 Logarithms:**
11. $\ln 1.25$ using first two terms of Gregory's series.
12. $\ln 3$ using first two terms of Gregory's series.

#### FOCUS ON CONCEPTS
13. Approximate $\pi$ using $\tan^{-1}(1/2)$ and $\tan^{-1}(1/3)$ with Machin-like identity.
14. Counterexample function $f(x) = e^{-1/x^2} \; (x \neq 0), f(0) = 0$, where all $f^{(n)}(0) = 0$.
15. Error bound on $\cos x \approx 1 - x^2/2 + x^4/24$ on $[-0.2, 0.2]$.
16. Error bound on $\ln(1+x) \approx x$ on $[-0.01, 0.01]$.
17. Binomial expansions of $\frac{1}{1+x}, \sqrt[3]{1+x}, \frac{1}{(1+x)^3}$.
18. Binomial coefficients $\binom{m}{k}$.
19. Error estimation for $\ln 2$: show $n = 13$ terms needed in Gregory's series for 5 decimal places.
20. Approximate $\ln(5/3)$ to 5 decimal places.
21. Prove Taylor series for $\cos x$ about any $x_0$ converges for all $x$.
22. Prove Taylor series for $\sin x$ about any $x_0$ converges for all $x$.
23. Normal distribution IQ integral estimation.
24. (a) Machin's formula $\frac{\pi}{4} = 4\tan^{-1}(1/5) - \tan^{-1}(1/239)$ to 25 decimal places. (b) Ramanujan's formula for $1/\pi$.

#### QUICK CHECK ANSWERS 9.9
1. $(-1)^k \frac{x^{2k}}{(2k)!}$  
2. $\frac{x^k}{k!}$  
3. $(-1)^{k+1}\frac{x^k}{k}; \; (-1, 1]$  
4. $\frac{m(m-1)\cdots(m-k+1)}{k!}x^k; \; 1$

---

## 9.10 DIFFERENTIATING AND INTEGRATING POWER SERIES; MODELING WITH TAYLOR SERIES

### DIFFERENTIATING & INTEGRATING POWER SERIES

> **9.10.2 THEOREM (Differentiation of Power Series)**  
> If $f(x) = \sum_{k=0}^\infty c_k(x - x_0)^k$ has radius of convergence $R > 0$, then $f$ is differentiable on $(x_0 - R, x_0 + R)$, and
> $$f'(x) = \sum_{k=0}^\infty \frac{d}{dx}[c_k(x - x_0)^k]$$
> with the same radius of convergence $R$.

> **9.10.3 THEOREM**  
> $f$ has derivatives of all orders on $(x_0 - R, x_0 + R)$.

> **9.10.4 THEOREM (Integration of Power Series)**  
> (a) $\int f(x)\,dx = \sum_{k=0}^\infty \left[\frac{c_k}{k+1}(x - x_0)^{k+1}\right] + C \quad (|x - x_0| < R)$  
> (b) $\int_\alpha^\beta f(x)\,dx = \sum_{k=0}^\infty \int_\alpha^\beta c_k(x - x_0)^k\,dx$.

> **9.10.6 THEOREM**  
> If $f(x) = \sum c_k (x - x_0)^k$ on an open interval, this power series is the Taylor series for $f$ about $x = x_0$.

#### Example 1
Differentiating $J_0(x) = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{2^{2k}(k!)^2} \implies J_0'(x) = \sum_{k=1}^\infty \frac{(-1)^k x^{2k-1}}{2^{2k-1} k!(k-1)!} = -J_1(x)$.

#### Example 2
(a) $e^{-x^2} = 1 - x^2 + \frac{x^4}{2!} - \frac{x^6}{3!} + \cdots$  
(b) $\ln x = (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \cdots \quad (0 < x \le 2)$  
(c) $\frac{1}{x} = 1 - (x-1) + (x-1)^2 - (x-1)^3 + \cdots \quad (0 < x < 2)$

#### Example 3
$\tan^{-1} x = \int \frac{1}{1+x^2}\,dx = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \cdots \quad (-1 \le x \le 1)$.

#### Example 4
$\int_0^1 e^{-x^2}\,dx = 1 - \frac{1}{3} + \frac{1}{5 \cdot 2!} - \frac{1}{7 \cdot 3!} + \frac{1}{9 \cdot 4!} - \frac{1}{11 \cdot 5!} \approx 0.747$.

#### Examples 5 & 6
Multiplication and division of series:
* $e^{-x^2}\tan^{-1} x = x - \frac{4}{3}x^3 + \frac{31}{30}x^5 - \cdots$
* $\tan x = \frac{\sin x}{\cos x} = x + \frac{x^3}{3} + \frac{2x^5}{15} + \cdots$

### MODELING PHYSICAL LAWS (PENDULUM PERIOD)

$$T = 4\sqrt{\frac{L}{g}}\int_0^{\pi/2} \frac{1}{\sqrt{1 - k^2\sin^2\phi}}\,d\phi = 2\pi\sqrt{\frac{L}{g}}\left(1 + \frac{k^2}{4} + \cdots\right)$$

---

### QUICK CHECK EXERCISES 9.10
*(See page 689 for answers.)*

1. $e^{-x^2} = \sum_{k=0}^\infty (-1)^k \frac{x^{2k}}{k!}$
2. $\frac{d}{dx}\sum_{k=1}^\infty (-1)^{k+1}\frac{x^k}{k} = 1 - x + x^2 - x^3 + \dots = \sum_{k=0}^\infty (-1)^k x^k$
3. $\left(\sum \frac{x^k}{k!}\right)\left(\sum \frac{x^k}{k+1}\right) = 1 + \frac{3}{2}x + \frac{4}{3}x^2 + \dots$
4. Given $f(1) = 4, f'(x) = \sum_{k=0}^\infty \frac{(-1)^k}{(k+1)!}(x-1)^k$: (a) $f'(1) = -1/2$ (b) $f(x) = 4 + (x-1) - \frac{1}{4}(x-1)^2 + \frac{1}{18}(x-1)^3 + \dots = 4 + \sum_{k=1}^\infty \frac{(-1)^{k+1}(x-1)^k}{k(k!)}$

---

### EXERCISE SET 9.10

**1–4 Substitutions:**
1. From $\frac{1}{1-x}$: (a) $\frac{1}{1+x}$ (b) $\frac{1}{1-x^2}$ (c) $\frac{1}{1-2x}$ (d) $\frac{1}{2-x}$
2. From $\ln(1+x)$: (a) $\ln(1-x)$ (b) $\ln(1+x^2)$ (c) $\ln(1+2x)$ (d) $\ln(2+x)$
3. Binomial substitutions: (a) $(2+x)^{-1/2}$ (b) $(1-x^2)^{-2}$
4. (a) $\frac{1}{a-x}$ (b) $\frac{1}{(a+x)^2}$

**5–8 First four terms and radius:**
5. (a) $\sin 2x$ (b) $e^{-2x}$ (c) $e^{x^2}$ (d) $x^2 \cos\pi x$
6. (a) $\cos 2x$ (b) $x^2 e^x$ (c) $x e^{-x}$ (d) $\sin(x^2)$
7. (a) $\frac{x^2}{1+3x}$ (b) $x\sinh 2x$ (c) $x(1-x^2)^{3/2}$
8. (a) $\frac{x}{x-1}$ (b) $3\cosh(x^2)$ (c) $\frac{x}{(1+2x)^3}$

**9–12 Trig/Log Identities & Taylor Expansions:**
9. (a) $\sin^2 x$ (b) $\ln[(1+x^3)^{12}]$
10. (a) $\cos^2 x$ (b) $\ln\left(\frac{1-x}{1+x}\right)$
11. Taylor of $1/x$ about $x = 1$.
12. Taylor of $1/x$ about $x = x_0$.

**13–16 Multiplication and Division of Series:**
13. (a) $e^x \sin x$ (b) $\sqrt{1+x}\ln(1+x)$
14. (a) $e^{-x^2}\cos x$ (b) $(1+x^2)^{4/3}(1+x)^{1/3}$
15. (a) $\sec x$ (b) $\frac{\sin x}{e^x}$
16. (a) $\frac{\tan^{-1} x}{1+x}$ (b) $\frac{\ln(1+x)}{1-x}$

**17–28 Differentiation, Integration, Limits:**
17. Derive $\sinh x, \cosh x$ series from $e^x, e^{-x}$.
18. First four terms of $\tanh x$.
19–20 Partial fractions Maclaurin series: 19. $\frac{4x-2}{x^2-1}$ 20. $\frac{x^3+x^2+2x-2}{x^2-1}$.
21–22 Confirm derivative formulas term by term: 21. (a) $\cos x$ (b) $\ln(1+x)$; 22. (a) $\sinh x$ (b) $\tan^{-1} x$.
23–24 Confirm integration formulas term by term: 23. (a) $e^x$ (b) $\sinh x$; 24. (a) $\sin x$ (b) $\frac{1}{1+x}$.
25–26 Intervals of convergence after differentiation/integration.
27. Maclaurin of $f(x) = \frac{x}{1-x^2}$; find $f^{(5)}(0), f^{(6)}(0)$.
28. For $f(x) = x^2 \cos 2x$, find $f^{(99)}(0)$.
29–30 Limits via series:  
29. (a) $\lim_{x \to 0} \frac{\sin x}{x} = 1$ (b) $\lim_{x \to 0} \frac{\tan^{-1} x - x}{x^3} = -\frac{1}{3}$.  
30. (a) $\lim_{x \to 0} \frac{1-\cos x}{\sin x} = 0$ (b) $\lim_{x \to 0} \frac{\ln\sqrt{1+x} - \sin 2x}{x} = -\frac{3}{2}$.

**31–34 Numerical Integrals to 3 decimal places:**
31. $\int_0^1 \sin(x^2)\,dx$ 32. $\int_0^{1/2} \tan^{-1}(2x^2)\,dx$ 33. $\int_0^{0.2} \sqrt[3]{1+x^4}\,dx$ 34. $\int_0^{1/2} \frac{dx}{\sqrt[4]{x^2+1}}$

#### FOCUS ON CONCEPTS
35. (a) $e^{x^4}$ series. (b) Series for $x^3 e^{x^4}$.
36. (a) $\sum_{k=1}^\infty k x^k = \frac{x}{(1-x)^2}$. (b) $\sum_{k=1}^\infty \frac{x^k}{k} = -\ln(1-x)$. (c) $\sum_{k=1}^\infty (-1)^{k+1}\frac{x^k}{k} = \ln(1+x)$.
37. Sums: (a) $\sum_{k=1}^\infty \frac{k}{3^k} = \frac{3}{4}$ (b) $\sum_{k=1}^\infty \frac{1}{k 4^k} = \ln(4/3)$.
38. Sums: (a) $\sum_{k=1}^\infty \frac{(-1)^{k+1}}{k} = \ln 2$ (b) $\sum_{k=1}^\infty \frac{(e-1)^k}{k e^k} = 1$.
39. Series for $\sinh^{-1} x = \int \frac{1}{\sqrt{1+x^2}}\,dx$.
40. Series for $\sin^{-1} x = \int \frac{1}{\sqrt{1-x^2}}\,dx$.
41. Carbon-14 radioactive decay series $y(t) = y_0 e^{-0.000121t}$.
42. Pendulum period models comparison.
43. Pendulum model using Wallis formula.
44. Earth gravitational force series $F = \frac{mg R^2}{(R+h)^2} \approx mg - \frac{2mgh}{R}$.
45. Bessel equations of order zero and one ($x y'' + y' + xy = 0$ and $x^2 y'' + xy' + (x^2 - 1)y = 0$).
46. Uniqueness of power series coefficients.
47. **Writing.** Qualitative limit analysis of $\lim_{x \to 0} \frac{x - \sin x}{x^3} = 1/6$.

#### QUICK CHECK ANSWERS 9.10
1. $(-1)^k \frac{x^{2k}}{k!}$  
2. $1; -1; 1; -1; (-1)^k x^k$  
3. $1; 3/2; 4/3$  
4. (a) $-1/2$ (b) $4; 1; -1/4; 1/18; 4; (-1)^{k+1}\frac{(x-1)^k}{k \cdot (k!)}$

---

## CHAPTER 9 REVIEW EXERCISES

1. What is the difference between an infinite sequence and an infinite series?
2. What is meant by the sum of an infinite series?
3. (a) What is a geometric series? Give some examples of convergent and divergent geometric series.  
   (b) What is a $p$-series? Give some examples of convergent and divergent $p$-series.
4. State conditions under which an alternating series is guaranteed to converge.
5. (a) What does it mean to say that an infinite series converges absolutely?  
   (b) What relationship exists between convergence and absolute convergence of an infinite series?
6. State the Remainder Estimation Theorem, and describe some of its uses.
7. If a power series in $x - x_0$ has radius of convergence $R$, what can you say about the set of $x$-values at which the series converges?
8. (a) Write down the formula for the Maclaurin series for $f$ in sigma notation.  
   (b) Write down the formula for the Taylor series for $f$ about $x = x_0$ in sigma notation.
9. Are the following statements true or false? If true, state a theorem to justify your conclusion; if false, then give a counterexample.  
   (a) If $\sum u_k$ converges, then $u_k \to 0$ as $k \to +\infty$.  
   (b) If $u_k \to 0$ as $k \to +\infty$, then $\sum u_k$ converges.  
   (c) If $f(n) = a_n$ for $n = 1, 2, 3, \dots$, and if $a_n \to L$ as $n \to +\infty$, then $f(x) \to L$ as $x \to +\infty$.  
   (d) If $f(n) = a_n$ for $n = 1, 2, 3, \dots$, and if $f(x) \to L$ as $x \to +\infty$, then $a_n \to L$ as $n \to +\infty$.  
   (e) If $0 < a_n < 1$, then $\{a_n\}$ converges.  
   (f) If $0 < u_k < 1$, then $\sum u_k$ converges.  
   (g) If $\sum u_k$ and $\sum v_k$ converge, then $\sum (u_k + v_k)$ diverges.  
   (h) If $\sum u_k$ and $\sum v_k$ diverge, then $\sum (u_k - v_k)$ converges.  
   (i) If $0 \le u_k \le v_k$ and $\sum v_k$ converges, then $\sum u_k$ converges.  
   (j) If $0 \le u_k \le v_k$ and $\sum u_k$ diverges, then $\sum v_k$ diverges.  
   (k) If an infinite series converges, then it converges absolutely.  
   (l) If an infinite series diverges absolutely, then it diverges.
10. State whether each of the following is true or false. Justify your answers.  
    (a) The function $f(x) = x^{1/3}$ has a Maclaurin series.  
    (b) $1 + \frac{1}{2} - \frac{1}{2} + \frac{1}{3} - \frac{1}{3} + \frac{1}{4} - \frac{1}{4} + \dots = 1$  
    (c) $1 + \frac{1}{2} - \frac{1}{2} + \frac{1}{2} - \frac{1}{2} + \frac{1}{2} - \frac{1}{2} + \dots = 1$
11. Find the general term of the sequence starting with $n = 1$, determine whether it converges, and find its limit:  
    (a) $\frac{3}{2^2 - 1^2}, \frac{4}{3^2 - 2^2}, \frac{5}{4^2 - 3^2}, \dots$ (b) $\frac{1}{3}, -\frac{2}{5}, \frac{3}{7}, -\frac{4}{9}, \dots$
12. Recursive sequence $a_0 = c, \; a_{k+1} = \sqrt{a_k}$; find limit for (a) $c = 1/2$ (b) $c = 3/2$.
13. Show eventually strictly monotone: (a) $\{(n-10)^4\}_{n=0}^{+\infty}$ (b) $\left\{\frac{100^n}{(2n)!(n!)}\right\}_{n=1}^{+\infty}$.
14. (a) Example of bounded sequence that diverges. (b) Example of monotonic sequence that diverges.
15–20 Determine whether the series converge:  
15. (a) $\sum \frac{1}{5k}$ (b) $\sum \frac{1}{5^k + 1}$  
16. (a) $\sum (-1)^k \frac{k+4}{k^2+k}$ (b) $\sum (-1)^{k+1}\left(\frac{k+2}{3k-1}\right)^k$  
17. (a) $\sum \frac{1}{k^3 + 2k + 1}$ (b) $\sum \frac{1}{(3+k)^{2/5}}$  
18. (a) $\sum \frac{\ln k}{k\sqrt{k}}$ (b) $\sum \frac{k^{4/3}}{8k^2 + 5k + 1}$  
19. (a) $\sum \frac{9}{\sqrt{k}+1}$ (b) $\sum \frac{\cos(1/k)}{k^2}$  
20. (a) $\sum \frac{k^{-1/2}}{2 + \sin^2 k}$ (b) $\sum \frac{(-1)^{k+1}}{k^2+1}$
21. Exact error when $\sum_{k=0}^\infty (1/5)^k$ is approximated by first 100 terms.
22. Given $\sum_{k=1}^n u_k = 2 - 1/n$: find (a) $u_{100}$ (b) $\lim u_k$ (c) $\sum_{k=1}^\infty u_k$.
23. Determine convergence and find sum:  
    (a) $\sum \left(\frac{3}{2^k} - \frac{2}{3^k}\right)$ (b) $\sum [\ln(k+1) - \ln k]$ (c) $\sum \frac{1}{k(k+2)}$ (d) $\sum [\tan^{-1}(k+1) - \tan^{-1} k]$.
24. Root test using $\lim \sqrt[n]{n!} = +\infty$ and $\lim \frac{\sqrt[n]{n!}}{n} = \frac{1}{e}$: (a) $\sum \frac{2^k}{k!}$ (b) $\sum \frac{k^k}{k!}$.
25. Values of $p$ for which $\sum \frac{1}{(a+bk)^p}$ converges ($p > 1$).
26. Interval of convergence of $\sum \frac{(x-x_0)^k}{b^k} \; (b > 0) \implies (x_0 - b, x_0 + b)$.
27. (a) $k^k \ge k!$. (b) Comparison test for $\sum k^{-k}$. (c) Root test for $\sum k^{-k}$.
28. Does $1 - \frac{2}{3} + \frac{3}{5} - \frac{4}{7} + \frac{5}{9} - \dots$ converge? (No, $n$th term $\to 1/2 \neq 0$).
29. (a) First five Maclaurin polynomials of $p(x) = 1 - 7x + 5x^2 + 4x^3$. (b) Maclaurin polynomials of degree $n$ polynomial.
30. Show $\sin x \approx x - \frac{x^3}{3!} + \frac{x^5}{5!}$ is accurate to 4 decimal places for $0 \le x \le \pi/4$.
31. Show $|\ln(1+x) - x| \le x^2/2$ for $0 < x < 1$.
32. Maclaurin series approximation of $\int_0^1 \frac{1-\cos x}{x}\,dx$ to 3 decimal places.
33. Sums by recognizing Maclaurin series:  
    (a) $2 + \frac{4}{2!} + \frac{8}{3!} + \frac{16}{4!} + \dots = e^2 - 1$  
    (b) $\pi - \frac{\pi^3}{3!} + \frac{\pi^5}{5!} - \frac{\pi^7}{7!} + \dots = \sin\pi = 0$  
    (c) $1 - \frac{e^2}{2!} + \frac{e^4}{4!} - \frac{e^6}{6!} + \dots = \cos e$  
    (d) $1 - \ln 3 + \frac{(\ln 3)^2}{2!} - \frac{(\ln 3)^3}{3!} + \dots = e^{-\ln 3} = 1/3$.
34. First four terms and radius of convergence:  
    (a) $\sum \frac{1 \cdot 2 \cdot 3 \cdots k}{1 \cdot 4 \cdot 7 \cdots (3k-2)}x^k$ ($R = 3$)  
    (b) $\sum (-1)^k \frac{1 \cdot 2 \cdot 3 \cdots k}{1 \cdot 3 \cdot 5 \cdots (2k-1)}x^{2k+1}$ ($R = \sqrt{2}$).
35. Taylor series for $\sqrt[3]{x}$ to approximate $\sqrt[3]{28}$ to 3 decimal places.
36. Differentiate Maclaurin series for $x e^x$ to show $\sum_{k=0}^\infty \frac{k+1}{k!} = 2e$.
37. Maclaurin series for: (a) $\sin x\cos x$ (b) $\frac{1}{2}\sin 2x$.

---

## CHAPTER 9 MAKING CONNECTIONS

1. As shown in Figure Ex-1, suppose lines $L_1$ and $L_2$ form an angle $\theta, \; 0 < \theta < \pi/2$ at $P$. $P_0$ is on $L_1$ at distance $a$ from $P$. A zig-zag path is constructed by dropping successive perpendiculars. Find:  
   (a) $P_0 P_1 + P_1 P_2 + P_2 P_3 + \dots = \frac{a\sin\theta}{1 - \cos\theta} = a\cot(\theta/2)$  
   (b) $P_0 P_1 + P_2 P_3 + P_4 P_5 + \dots = \frac{a\sin\theta}{1 - \cos^2\theta} = a\csc\theta$  
   (c) $P_1 P_2 + P_3 P_4 + P_5 P_6 + \dots = \frac{a\sin\theta\cos\theta}{1 - \cos^2\theta} = a\cot\theta$.
2. (a) Find $A$ and $B$ such that $\frac{6^k}{(3^{k+1} - 2^{k+1})(3^k - 2^k)} = \frac{2^k A}{3^k - 2^k} + \frac{2^k B}{3^{k+1} - 2^{k+1}}$ ($A = 1, B = -1$).  
   (b) Find closed form for $n$th partial sum and sum of series ($s_n = 1 - \frac{2^n}{3^{n+1}-2^{n+1}} \to 1$). *(Putnam Competition problem)*.
3. Show alternating $p$-series $1 - \frac{1}{2^p} + \frac{1}{3^p} - \frac{1}{4^p} + \dots$: converges absolutely if $p > 1$, conditionally if $0 < p \le 1$, diverges if $p \le 0$.
4. Bug on a 180 cm wire walks $180, -90, +60, -45, \dots$:  
   (a) Distance from $A$ when it stops after 1000 steps ($180\ln 2 \approx 124.77$ cm).  
   (b) Total distance traveled ($180\sum_{k=1}^{1000} \frac{1}{k} \approx 180(\ln 1001 + \gamma)$).
5. Relativistic kinetic energy $K = m_0 c^2\left[\frac{1}{\sqrt{1-(v/c)^2}} - 1\right]$. Binomial series shows $K \approx \frac{1}{2}m_0 v^2 + \frac{3}{8}m_0 \frac{v^4}{c^2} + \dots \approx \frac{1}{2}m_0 v^2$ when $v/c \approx 0$.
6. Air resistance velocity $v(t) = e^{-ct/m}(v_0 + mg/c) - mg/c$.  
   (a) Maclaurin series in $ct/m$: $v(t) \approx v_0 - \left(\frac{c v_0}{m} + g\right)t$.  
   (b) Second-order improvement: $+ \frac{1}{2}\left(\frac{c^2 v_0}{m^2} + \frac{cg}{m}\right)t^2$.

---

## EXPANDING THE CALCULUS HORIZON
*Iteration and Dynamical Systems* (available online at www.wiley.com/college/anton).
