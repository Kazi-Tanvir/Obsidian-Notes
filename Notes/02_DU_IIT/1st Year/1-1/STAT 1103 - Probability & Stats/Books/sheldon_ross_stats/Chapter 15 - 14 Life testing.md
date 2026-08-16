# Chapter 14: Life testing *(Optional)*

## 14.1 Introduction

In this chapter, we consider a population of items having lifetimes that are assumed to be independent random variables with a common distribution that is specified up to an unknown parameter. The problem of interest will be to use whatever data are available to estimate this parameter.

## 14.2 Hazard rate functions

Consider a positive continuous random variable $X$ representing the lifetime of an item, with distribution function $F$ and density $f$. The *hazard rate* (or *failure rate*) function $\lambda(t)$ is defined by

$$\lambda(t) = \frac{f(t)}{1 - F(t)}$$

For small $dt$, $\lambda(t) dt \approx P\{X \in (t, t + dt) \mid X > t\}$.

When the lifetime is exponential, $\lambda(t) = \lambda$ (constant).

In general, the hazard rate uniquely determines the distribution:

$$1 - F(t) = \exp\left\{-\int_0^t \lambda(s) \, ds\right\} \tag{14.2.1}$$

For a linear hazard rate $\lambda(t) = a + bt$:

$$F(t) = 1 - e^{-at - bt^2/2}, \qquad f(t) = (a + bt)e^{-(at + bt^2/2)}, \quad t \ge 0$$

(When $a = 0$, this is the Rayleigh distribution).

**Example 14.2.a.** If smoker death rate is twice nonsmoker death rate ($\lambda_s(t) = 2\lambda_n(t)$), then the probability a smoker survives from age $A$ to age $B$ is the *square* (not half) of the probability for a nonsmoker.

## 14.3 The exponential distribution in life testing

### 14.3.1 Simultaneous testing — stopping at the $r$th failure

$n$ independent items simultaneously on test, stopped at $r$th failure ($r \le n$).
Observed data: failure times $x_1 \le x_2 \le \dots \le x_r$.

The maximum likelihood estimator of $\theta$ is:

$$\hat{\theta} = \frac{\sum_{i=1}^r X_{(i)} + (n - r)X_{(r)}}{r} = \frac{\tau}{r} \tag{14.3.3}$$

where $\tau = \sum_{i=1}^r X_{(i)} + (n - r)X_{(r)}$ is the *total-time-on-test* statistic.

Let $Y_1 = nX_{(1)}$ and $Y_j = (n - j + 1)(X_{(j)} - X_{(j-1)}), j = 2, \dots, r$.
The $Y_j$ are independent exponential random variables each with mean $\theta$, and $\tau = \sum_{j=1}^r Y_j \sim \text{Gamma}(r, 1/\theta)$, so:

$$\frac{2\tau}{\theta} \sim \chi_{2r}^2 \tag{14.3.5}$$

A $100(1 - \alpha)$ percent confidence interval for $\theta$:

$$\theta \in \left(\frac{2\tau}{\chi_{\alpha/2, 2r}^2}, \; \frac{2\tau}{\chi_{1-\alpha/2, 2r}^2}\right) \tag{14.3.6}$$

**Example 14.3.a.** $n = 50, r = 15, \tau = 525 \implies \text{df} = 30 \implies 95\% \text{ CI: } (22.35, 62.17)$.

**Example 14.3.b.** Battery claim $\theta \ge 150$: $n = 100, r = 20, \tau = 1800 \implies \text{TS} = 2(1800)/150 = 24 \implies p\text{-value} = P\{\chi_{40}^2 \le 24\} = .0213$ (reject $H_0$).

#### Expected Duration of the Test
$$E[X_{(r)}] = \theta \sum_{j=n-r+1}^n \frac{1}{j} \approx \theta \log\left(\frac{n}{n - r + 1}\right) \tag{14.3.7}$$
$$\text{Var}(X_{(r)}) = \theta^2 \sum_{j=n-r+1}^n \frac{1}{j^2} \approx \theta^2 \frac{r - 1}{n(n - r + 1)}$$

### 14.3.2 Sequential testing

Testing items one at a time, replacing each upon failure until a fixed time $T$, resulting in $r$ failures:

$$\hat{\theta} = \frac{T}{r}$$

A $100(1 - \alpha)$ percent confidence interval for $\theta$:

$$\theta \in \left(\frac{2T}{\chi_{\alpha/2, 2r}^2}, \; \frac{2T}{\chi_{1-\alpha/2, 2r}^2}\right)$$

**Example 14.3.c.** $T = 500, r = 10 \implies \hat{\theta} = 50 \implies 95\% \text{ CI: } (29.27, 103.52)$.

**Example 14.3.d.** $T = 600, r = 30, \theta_0 = 25 \implies p\text{-value} = P\{\chi_{60}^2 \le 48\} = .1321$.

### 14.3.3 Simultaneous testing — stopping by a fixed time

$n$ items tested simultaneously up to time $T$, where $R$ failures occur at $X_{(1)}, \dots, X_{(R)}$:

$$\tau = \sum_{i=1}^R X_{(i)} + (n - R)T \implies \hat{\theta} = \frac{\tau}{R}$$

### 14.3.4 The Bayesian approach

Working with the rate $\lambda = 1/\theta$. If prior on $\lambda$ is $\text{Gamma}(b, a)$:

$$g(\lambda) = \frac{a e^{-a\lambda}(a\lambda)^{b-1}}{\Gamma(b)}, \quad \lambda > 0$$

Then the posterior distribution of $\lambda$ given the data is $\text{Gamma}(b + R, a + \tau)$, and the Bayes estimator is:

$$E[\lambda \mid \text{data}] = \frac{b + R}{a + \tau}$$

**Example 14.3.e.** Prior $\text{Gamma}(2, 20)$, data $\tau = 116.1, R = 10 \implies E[\lambda \mid \text{data}] = \frac{2 + 10}{20 + 116.1} = \frac{12}{136.1} = .088$.

## 14.4 A two-sample problem

Let $X_1, \dots, X_n \sim \text{Exponential}(\theta_1)$ and $Y_1, \dots, Y_m \sim \text{Exponential}(\theta_2)$ be independent. To test $H_0 : \theta_1 = \theta_2$ vs $H_1 : \theta_1 \neq \theta_2$:

$$\frac{\bar{X}}{\bar{Y}} \sim F_{n, m} \quad \text{under } H_0$$

$$p\text{-value} = 2\min(P\{F_{n, m} \le v\}, \; 1 - P\{F_{n, m} \le v\})$$

**Example 14.4.a.** Plant 1 ($n = 10, \sum X_i = 420$), Plant 2 ($m = 15, \sum Y_i = 510$):
$\bar{X}/\bar{Y} = 42/34 = 1.2353 \implies p\text{-value} = 2(1 - .6553) = .6894 \implies$ Accept $H_0$.

## 14.5 The Weibull distribution in life testing

Hazard rate function:

$$\lambda(t) = \alpha \beta t^{\beta - 1}, \quad t > 0 \tag{14.5.1}$$

Distribution and density:

$$F(t) = 1 - \exp\{-\alpha t^\beta\}, \qquad f(t) = \alpha \beta t^{\beta-1}\exp\{-\alpha t^\beta\}, \quad t > 0 \tag{14.5.2}$$

Mean and variance:

$$E[X] = \alpha^{-1/\beta}\Gamma(1 + 1/\beta)$$
$$\text{Var}(X) = \alpha^{-2/\beta}\left[\Gamma(1 + 2/\beta) - \left(\Gamma(1 + 1/\beta)\right)^2\right]$$

### 14.5.1 Parameter estimation by least squares

$$\log\left(\log\left(\frac{1}{1 - F(x)}\right)\right) = \beta \log x + \log \alpha \tag{14.5.3}$$

Linear regression model: $y_i \approx \beta \log x_{(i)} + \log \alpha$.

**Method 1:**
$$y_i = \log\left\{-\log\left(1 - \frac{i}{n+1}\right)\right\}$$

**Method 2:**
$$y_i = \log\left\{\sum_{j=1}^i \frac{1}{n - j + 1}\right\}$$

---

## Problems

1. Compute failure rate function for Weibull distribution $F(t) = 1 - e^{-\alpha t^\beta}$.

2. Show that for independent $X$ and $Y$, $\lambda_{\min(X, Y)}(t) = \lambda_X(t) + \lambda_Y(t)$.

3. Lung cancer rate $\lambda(t) = .027 + .025((t - 40)/10)^4, t \ge 40$. Probability of surviving to (a) age 50, (b) age 60 without lung cancer.

4. Hazard rate $\lambda(t) = t^3, t > 0$. Find (a) $P\{X > 2\}$, (b) $P\{.4 < X < 1.4\}$, (c) $E[X]$, (d) $P\{X > 2 \mid X > 1\}$.

5. Increasing Failure Rate (IFR) distributions: Show $\text{Gamma}(2, \lambda)$ is IFR, and $\text{Gamma}(\alpha, \lambda)$ is IFR for $\alpha \ge 1$.

6. Show that uniform distribution on $(a, b)$ is IFR.

7. Geometric interpretation of total time on test $\tau = \sum_{j=1}^r Y_j$.

8. 30 transistors tested until 10th failure: failure times $4.1, 7.3, 13.2, 18.8, 24.5, 30.8, 38.1, 45.5, 53, 62.2$.
   a. MLE of $\theta$.
   b. 95% two-sided CI for $\theta$.
   c. 95% lower bound for $\theta$.
   d. Test $H_0 : \theta = 7.5$ at $\alpha = .10$.

9. $p$-value formula for testing $H_0 : \theta = \theta_0$ in simultaneous failure-censored testing.

10. 30 items tested until 8th failure: test $H_0 : \theta = 10$ at $5\%$.

11. 20 items tested until 10th failure ($\theta = 10$). Mean and variance of test duration.

12. Sample size $n$ needed for mean test duration $\le 3$ hours with $r = 10, \theta = 20$.

13. Sequential life test: $T = 300$ hours, 16 failures: (a) MLE of $\theta$, (b) Test $H_0 : \theta = 20$, (c) 95% CI.

14. Relation between Poisson process and chi-square distribution $P\{X \ge n\} = F_{\chi_{2n}^2}(x)$ where $X \sim \text{Poisson}(x/2)$.

15. Sequential testing stopping at $\min(r\text{th failure}, T)$: Likelihood and MLE.

16. Verification of general MLE formula $\hat{\theta} = \tau/r$.

17. 10 components on test (5 active, 5 replacement): 9 failures occurred before 200 hours. MLE of mean life.

18. Leukemia patient remission times with right-censoring ($n = 20$). MLE of mean remission time.

19. Bayes estimate of $\lambda$ with prior $\text{Gamma}(1, 100)$ for Problem 17 data.

20. Bayes estimate of $\lambda$ with prior $\text{Exponential}(30)$ for Problem 18 data.

21. Two-sample exponential test: Electrical insulation failure times (Type I vs Type II).

22. Two-sample exponential test with failure censoring ($n_1 = 20, r_1 = 10$ and $n_2 = 10, r_2 = 7$).

23. Proof that $E[X] = \alpha^{-1/\beta}\Gamma(1 + 1/\beta)$ for Weibull distribution.

24. Variance of Weibull distribution.

25. Least squares parameter estimation for Weibull data: $15.4, 16.8, 6.2, 10.6, 21.4, 18.2, 1.6, 12.5, 19.4, 17$.

26. Show $\alpha X^\beta \sim \text{Exponential}(1)$ when $X \sim \text{Weibull}(\alpha, \beta)$.

27. Generating Weibull random variables from uniform $U$: $[-(1/\alpha)\log U]^{1/\beta}$.

28. Probability Integral Transform: $F(X) \sim \text{Uniform}(0, 1)$.

29. Distribution of uniform order statistics $U_{(i)}$ and proof that $E[F(X_{(i)})] = \frac{i}{n+1}$.

30. Proof that $-\log U \sim \text{Exponential}(1)$ and derivation of $E[-\log(1 - F(X_{(i)}))] = \sum_{j=1}^i \frac{1}{n-j+1}$.
