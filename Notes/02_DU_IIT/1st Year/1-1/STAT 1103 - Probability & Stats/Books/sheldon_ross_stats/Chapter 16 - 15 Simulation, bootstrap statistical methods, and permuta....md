# Chapter 15: Simulation, bootstrap statistical methods, and permutation tests

## 15.1 Introduction

In this chapter we introduce two powerful modern statistical techniques: *bootstrap statistical methods* and *permutation tests*. Both are nonparametric procedures in the sense that they make no specific assumptions about the form of any underlying probability distributions. Bootstrap methods enable us to measure the efficacy of an estimator of a parameter, while permutation tests yield new ways to test certain statistical hypotheses. Both, however, require a large amount of computation in their implementation. The most efficient and effective way of doing the needed computation uses simulation.

## 15.2 Random numbers

The value of a uniform $(0, 1)$ random variable is called a *random number*. Today we commonly use pseudo-random number generators:

$$x_{n+1} = (a x_n + c) \pmod m, \quad n \ge 0$$

**Example 15.2.a.** If $a = 3, c = 7, m = 23, x_0 = 2$:
$$x_1 = 13, x_2 = 0, x_3 = 7, x_4 = 5, x_5 = 22, \dots$$
Pseudo-random numbers: $13/23, 0, 7/23, 5/23, 22/23, \dots$. $\blacksquare$

### Generating a Random Permutation (Fisher-Yates / Knuth Shuffle)
Given $r_1, \dots, r_n$:
For $k = n, n - 1, \dots, 2$:
1. Generate random number $U$ and let $I = \text{Int}(kU) + 1$.
2. Swap $r_I$ and $r_k$.

### 15.2.1 The Monte Carlo simulation approach
To estimate $E[h(X_1, \dots, X_n)]$, generate $r$ independent sets of $n$ random variables and compute:

$$\lim_{r \to \infty} \frac{Y_1 + \dots + Y_r}{r} = E[h(X_1, \dots, X_n)]$$

## 15.3 The bootstrap method

Let $X_1, \dots, X_n$ be a sample from $F$, and $d(X_1, \dots, X_n)$ an estimator of parameter $\theta$. The mean square error is:

$$\text{MSE}_F(d) = E_F[(d(X_1, \dots, X_n) - \theta)^2]$$

**Example 15.3.a.** For sample mean $\bar{X}_n$: $\text{MSE}_F(\bar{X}_n) = \sigma^2/n$, estimated by $S_n^2/n$.

The *empirical distribution function* $F_e$:

$$F_e(x) = \frac{\#\{i \le n : x_i \le x\}}{n}$$

Bootstrap estimate of MSE:

$$\text{MSE}_{F_e}(d) = E_{F_e}[(d(X_1, \dots, X_n) - \theta_e)^2]$$

**Example 15.3.b.** For $\bar{X}_n$: $\text{MSE}_{F_e}(\bar{X}_n) = \frac{1}{n^2}\sum_{i=1}^n (x_i - \bar{x}_n)^2$.

**Example 15.3.c (Bootstrap for Sample Variance).** $n = 8$, data $5, 9, 12, 8, 7, 15, 3, 6 \implies \bar{x}_8 = 8.125, \theta_e = \text{Var}_{F_e}(X) \approx 13.11$. Bootstrap simulation algorithm estimates $\text{MSE}_{F_e}(S_n^2)$.

### Estimating Error Probabilities
To estimate $p_h = P_F(|d(X_1, \dots, X_n) - \theta| \le h) \approx P_{F_e}(|d(X_1, \dots, X_n) - \theta_e| \le h)$:

**Example 15.3.d.** PSAT scores ($n = 16$, $\bar{x} = 524.7$):
- $P_{F_e}(|\bar{X}_{16} - 524.7| \le 5) \approx .1801$.
- $P_{F_e}(|\bar{X}_{16} - 524.7| \le 10) \approx .3542$.
- For standard deviation $\sigma_e = 86.27$: $P_{F_e}(|S_{16} - 86.27| \le 10) \approx .5424$.

## 15.4 Permutation tests

To test $H_0 : X_1, \dots, X_N$ are i.i.d. vs $H_1 : X_j$ increases with $j$:
Test statistic $T = \sum_{j=1}^N j X_j$.
Conditional on the observed set $S = \{x_1, \dots, x_N\}$, all $N!$ permutations are equally likely under $H_0$:

$$p\text{-value} = P\left\{\sum_{j=1}^N I_j x_j \ge t\right\} = \frac{\#\{\text{permutations with } T \ge t\}}{N!}$$

**Example 15.4.a.** DVD player weekly sales over 12 weeks: $t = 1178 \implies p\text{-value} \approx .00039$ (reject $H_0$).

### 15.4.1 Normal approximations in permutation tests
Under $H_0$:

$$E[T] = \frac{N(N + 1)}{2}\bar{x}$$
$$\text{Var}(T) = (v - c)\frac{N(N + 1)(2N + 1)}{6} + \frac{c N^2(N + 1)^2}{4}$$

where $v = \frac{1}{N}\sum_{i=1}^N x_i^2 - \bar{x}^2$ and $c = \frac{1}{N - 1}\left(\bar{x}^2 - \frac{1}{N}\sum_{k=1}^N x_k^2\right) = -\frac{v}{N - 1}$.

**Example 15.4.b.** For Example 15.4.a: $E[T] = 1300, \text{Var}(T) = 1958.81 \implies Z = \frac{1178 - 1300}{\sqrt{1958.81}} = -2.757 \implies p\text{-value} = .0029$.

**Example 15.4.c.** $N = 4$, data $13, 7, 5, 3$: $E[T] = 70, \text{Var}(T) = 93.33 \implies p\text{-value} \approx .049$ (exact $= 1/24 \approx .042$).

### 15.4.2 Two-sample permutation tests
To test $H_0 : F = G$ vs $H_1 : G \text{ larger than } F$ for samples $X_1, \dots, X_n$ and $X_{n+1}, \dots, X_{n+m}$:
Test statistic $T = \sum_{i \in R} x_i$ where $R$ is a randomly chosen subset of size $n$ from $\{1, \dots, n + m\}$.

Under $H_0$:

$$E_{H_0}\left[\sum_{i \in R} x_i\right] = n\bar{x}$$
$$\text{Var}_{H_0}\left(\sum_{i \in R} x_i\right) = \frac{nm}{n + m - 1}\left(\frac{\sum_{i=1}^{n+m} x_i^2}{n + m} - \bar{x}^2\right)$$

## 15.5 Generating discrete random variables

Discrete inverse transform method: generate uniform $(0, 1)$ random number $U$, find $i$ such that $\sum_{j=1}^{i-1} p_j < U \le \sum_{j=1}^i p_j$.

**Example 15.5.a.** Bernoulli random variable.
**Example 15.5.b.** Binomial random variable using recursive probability ratios:

$$p_{i+1} = \frac{n - i}{i + 1} \frac{p}{1 - p} p_i$$

Average iterations required: $np + 1$.

## 15.6 Generating continuous random variables

**Proposition 15.6.1 (Inverse Transformation Method).** If $U \sim \text{Uniform}(0, 1)$ and $F$ is a continuous distribution function, then

$$X = F^{-1}(U) \sim F$$

**Example 15.6.a (Exponential Generation).**
$$X = -\frac{1}{\lambda}\log(1 - U) \stackrel{d}{=} -\frac{1}{\lambda}\log U$$

### 15.6.1 Generating a normal random variable (Box-Muller Method)
If $U_1, U_2$ are independent $\text{Uniform}(0, 1)$:

$$X = \sqrt{-2\log U_1}\cos(2\pi U_2)$$
$$Y = \sqrt{-2\log U_1}\sin(2\pi U_2)$$

are independent standard normal random variables $N(0, 1)$.

## 15.7 Determining the number of simulation runs in a Monte Carlo study

Two-stage simulation:
1. Generate initial $k$ runs to estimate sample variance $S_k^2$.
2. Choose total runs $r$ such that $z_{\alpha/2} \frac{S_k}{\sqrt{r}} \le \text{desired margin of error}$.

---

## Problems

1. Linear congruential generator: $x_0 = 5, x_n = 3x_{n-1} \pmod 5$. Find $x_1, \dots, x_{10}$.

2. Successive generation algorithm for random permutations.

3. Estimating ratio $\theta = E[X_1]/E[Y_1]$ and bootstrap MSE.

4. Bootstrap estimate of $\text{Var}(S^2)$: (a) $n = 2, X = (1, 3)$; (b) $n = 15$ dataset.

5. Estimating $p = P\{\sum_{i=1}^8 X_i / 8 < \mu\}$ using bootstrap on data $5, 2, 8, 6, 24, 6, 9, 4$.

6. Student exam scores trend: $68, 64, 72, 80, 72, 84, 76, 86, 94, 92$.

7. Baseball player hitting trend: $8, 3, 7, 12, 4, 7, 13, 6, 0, 9, 12, 4, 4, 6, 10$.

8. Two-sample permutation test for radiation-exposed mice lifetimes ($n_1 = 8, n_2 = 8$).

9. Permutation test on Chapter 12 Problem 13 data.

10. Permutation test on Chapter 12 Problem 16 data.

11. Discrete inverse transform algorithm for Poisson random variable with mean $\lambda$.

12. Geometric random variable generation: $X = \text{Int}\left(\frac{\log(1 - U)}{\log(1 - p)}\right) + 1$.

13. Inverse transform generation for $f(x) = \frac{e^x}{e - 1}, 0 < x < 1$.

14. Inverse transform generation for $F(x) = x^n, 0 < x < 1$.

15. Inverse transform generation for $F(x) = \frac{1}{2}(x + x^2), 0 < x < 1$.

16. Two-stage simulation sample size determination for 20 generated values.
