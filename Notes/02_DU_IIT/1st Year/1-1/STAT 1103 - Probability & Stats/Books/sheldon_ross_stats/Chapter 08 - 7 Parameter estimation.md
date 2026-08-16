# Chapter 7: Parameter estimation

## 7.1 Introduction

Let $X_1, \dots, X_n$ be a random sample from a distribution $F_\theta$ that is specified up to a vector of unknown parameters $\theta$. For instance, the sample could be from a Poisson distribution whose mean value is unknown; or it could be from a normal distribution having an unknown mean and variance. Whereas in probability theory it is usual to suppose that all of the parameters of a distribution are known, the opposite is true in statistics, where a central problem is to use the observed data to make inferences about the unknown parameters.

In Section 7.2, we present the maximum likelihood method for determining estimators of unknown parameters. The estimates so obtained are called *point estimates*, because they specify a single quantity as an estimate of $\theta$. In Section 7.3, we consider the problem of obtaining *interval estimates*. In this case, rather than specifying a certain value as our estimate of $\theta$, we specify an interval in which we estimate that $\theta$ lies. Additionally, we consider the question of how much confidence we can attach to such an interval estimate. We illustrate by showing how to obtain an interval estimate of the unknown mean of a normal distribution whose variance is specified. We then consider a variety of interval estimation problems. In Section 7.3.1, we present an interval estimate of the mean of a normal distribution whose variance is unknown. In Section 7.3.2, we obtain an interval estimate of the variance of a normal distribution. In Section 7.4, we determine an interval estimate for the difference of two normal means, both when their variances are assumed to be known and when they are assumed to be unknown (although in the latter case we suppose that the unknown variances are equal). In Sections 7.5 and the optional Section 7.6, we present interval estimates of the mean of a Bernoulli random variable and the mean of an exponential random variable.

In the optional Section 7.7, we return to the general problem of obtaining point estimates of unknown parameters and show how to evaluate an estimator by considering its mean square error. The bias of an estimator is discussed, and its relationship to the mean square error is explored.

In the optional Section 7.8, we consider the problem of determining an estimate of an unknown parameter when there is some prior information available. This is the *Bayesian approach*, which supposes that prior to observing the data, information about $\theta$ is always available to the decision maker, and that this information can be expressed in terms of a probability distribution on $\theta$. In such a situation, we show how to compute the Bayes estimator, which is the estimator whose expected squared distance from $\theta$ is minimal.

## 7.2 Maximum likelihood estimators

Any statistic used to estimate the value of an unknown parameter $\theta$ is called an *estimator* of $\theta$. The observed value of the estimator is called the *estimate*. For instance, the usual estimator of the mean of a normal population, based on a sample $X_1, \dots, X_n$ from that population, is the sample mean $\bar{X} = \sum_i X_i / n$. If a sample of size 3 yields the data $X_1 = 2, X_2 = 3, X_3 = 4$, then the estimate of the population mean, resulting from the estimator $\bar{X}$, is the value 3.

Suppose that the random variables $X_1, \dots, X_n$, whose joint distribution is assumed given except for an unknown parameter $\theta$, are to be observed. The problem of interest is to use the observed values to estimate $\theta$.

A particular type of estimator, known as the *maximum likelihood estimator*, is widely used in statistics. Let $f(x_1, \dots, x_n \mid \theta)$ denote the joint probability mass function of the random variables $X_1, \dots, X_n$ when they are discrete, and let it be their joint probability density function when they are jointly continuous random variables. The function $f(x_1, \dots, x_n \mid \theta)$ is called the *likelihood function* of $\theta$. The maximum likelihood estimate $\hat{\theta}$ is defined to be that value of $\theta$ maximizing $f(x_1, \dots, x_n \mid \theta)$ where $x_1, \dots, x_n$ are the observed values.

In determining the maximizing value of $\theta$, it is often useful to maximize $\log[f(x_1, \dots, x_n \mid \theta)]$.

**Example 7.2.a (Maximum Likelihood Estimator of a Bernoulli Parameter).** Suppose that $n$ independent trials, each of which is a success with probability $p$, are performed. What is the maximum likelihood estimator of $p$?

**Solution.** The likelihood is

$$f(x_1, \dots, x_n \mid p) = p^{\sum_{i=1}^n x_i} (1 - p)^{n - \sum_{i=1}^n x_i}$$

Taking logarithms:

$$\log f(x_1, \dots, x_n \mid p) = \sum_{i=1}^n x_i \log p + \left(n - \sum_{i=1}^n x_i\right) \log(1 - p)$$

Differentiating with respect to $p$ and setting to zero yields:

$$\hat{p} = \frac{\sum_{i=1}^n x_i}{n} = \bar{X} \quad \blacksquare$$

**Example 7.2.b (Two Proofreaders / Capture-Recapture).** If proofreader 1 finds $n_1$ errors, proofreader 2 finds $n_2$ errors, and $n_{1, 2}$ errors are found by both, the estimate of $N$, the total number of errors, is

$$N \approx \frac{n_1 n_2}{n_{1, 2}}$$

For $m > 2$ proofreaders, let $n_f$ be the number of errors found by at least one proofreader:

$$\hat{N} = \frac{n_f}{1 - \prod_{i=1}^m (1 - \hat{p}_i)} \tag{7.2.1}$$
$$\hat{p}_i = \frac{n_i}{\hat{N}}, \quad i = 1, \dots, m \tag{7.2.2}$$

**Example 7.2.c (MLE of a Poisson Parameter).** If $X_1, \dots, X_n$ are independent Poisson random variables with mean $\lambda$,

$$\hat{\lambda} = \frac{\sum_{i=1}^n X_i}{n} = \bar{X} \quad \blacksquare$$

**Example 7.2.d.** Traffic accidents in Berkeley: $\bar{X} = 2.7$. Estimated proportion of days with $\le 2$ accidents:

$$e^{-2.7}\left(1 + 2.7 + \frac{(2.7)^2}{2}\right) = .4936 \quad \blacksquare$$

**Example 7.2.e (MLE in a Normal Population).** If $X_1, \dots, X_n \sim N(\mu, \sigma^2)$,

$$\hat{\mu} = \bar{X} = \frac{\sum_{i=1}^n X_i}{n}$$
$$\hat{\sigma} = \sqrt{\frac{\sum_{i=1}^n (X_i - \bar{X})^2}{n}} \tag{7.2.3}$$

**Example 7.2.f (Lognormal Distribution and Kolmogorov's Law).** Sand grain sizes log-transformed: $\bar{x} = .7504, s = .4351$.

$$P\{2 < X < 3\} = P\left\{\frac{\log(2) - .7504}{.4351} < Z < \frac{\log(3) - .7504}{.4351}\right\} \approx 0.3406 \quad \blacksquare$$

**Example 7.2.g (Estimating the Parameter of a Uniform Distribution).** If $X_1, \dots, X_n \sim \text{Uniform}(0, \theta)$,

$$\hat{\theta} = \max(X_1, \dots, X_n)$$

### 7.2.1 Estimating life distributions *(Optional)*

Let $X$ denote the age at death. Hazard rate / failure rate $\lambda_i = P\{X = i \mid X > i - 1\}$, survival rate $s_i = 1 - \lambda_i$.

$$P\{X > i\} = s_1 s_2 \dots s_i$$
$$P\{X = n\} = s_1 \dots s_{n-1}(1 - s_n)$$

For censored data with survival times, $\hat{s}_i$ is estimated by the fraction of patients who started month $i$ and survived month $i$.

## 7.3 Interval estimates

### Known Variance $\sigma^2$
A $100(1 - \alpha)$ percent two-sided confidence interval for the mean $\mu$ of a normal population:

$$\bar{x} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

One-sided confidence intervals:
- Upper: $\left(\bar{x} - z_\alpha \frac{\sigma}{\sqrt{n}}, \; \infty\right)$
- Lower: $\left(-\infty, \; \bar{x} + z_\alpha \frac{\sigma}{\sqrt{n}}\right)$

**Example 7.3.a.** Signal transmission: $n = 9, \sigma = 2, \bar{x} = 9$.
95% CI: $9 \pm 1.96(2/3) = (7.69, 10.31)$.

**Example 7.3.b.** 95% one-sided intervals:
- Upper: $(7.903, \infty)$
- Lower: $(-\infty, 10.097)$

**Example 7.3.c.** 99% CI: $z_{.005} = 2.58 \implies 9 \pm 2.58(2/3) = 9 \pm 1.72 = (7.28, 10.72)$.

**Sample Size Determination:** To have interval length $b$, choose $n = \left(\frac{2 z_{\alpha/2} \sigma}{b}\right)^2$.

**Example 7.3.d.** Salmon hatchery: $\sigma = 0.3$, within $\pm 0.1 \implies n \ge \left(\frac{1.96 \times 0.3}{0.1}\right)^2 = 34.57 \implies n \ge 35$.

### 7.3.1 Confidence interval for a normal mean when the variance is unknown

Using the $t$-statistic with $n - 1$ degrees of freedom:

$$\mu \in \left(\bar{x} - t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}, \; \bar{x} + t_{\alpha/2, n-1} \frac{s}{\sqrt{n}}\right)$$

One-sided intervals:
- Upper: $\left(\bar{x} - t_{\alpha, n-1} \frac{s}{\sqrt{n}}, \; \infty\right)$
- Lower: $\left(-\infty, \; \bar{x} + t_{\alpha, n-1} \frac{s}{\sqrt{n}}\right)$

**Example 7.3.e.** Signal transmission with unknown variance: $\bar{x} = 9, s = 3.082, n = 9, t_{.025, 8} = 2.306 \implies (6.63, 11.37)$.

**Example 7.3.f.** Pulse rates: $n = 15$. In R:

```r
> d = c(54, 63, 58, 72, 49, 92, 70, 73, 69, 104, 48, 66, 80, 64, 77)
> l = mean(d) - qt(.975, 14) * sqrt(var(d)/15)
> u = mean(d) + qt(.975, 14) * sqrt(var(d)/15)
> c(l, u)
[1] 60.86694 77.66640
```

**Example 7.3.g (Monte Carlo Simulation).** Estimating integrals $\theta = \int_0^1 \sqrt{1 - y^2} \, dy = \pi/4$.

### 7.3.2 Prediction intervals

To predict $X_{n+1}$ from $X_1, \dots, X_n$:

$$X_{n+1} \in \left(\bar{X}_n - t_{\alpha/2, n-1} S_n \sqrt{1 + 1/n}, \; \bar{X}_n + t_{\alpha/2, n-1} S_n \sqrt{1 + 1/n}\right)$$

**Example 7.3.h.** Daily steps: $\bar{X}_7 = 6716.57, S_7 = 733.97, t_{.025, 6} = 2.447 \implies (4796.54, 8636.60)$.

### 7.3.3 Confidence intervals for the variance of a normal distribution

A $100(1 - \alpha)$ percent confidence interval for $\sigma^2$:

$$\sigma^2 \in \left(\frac{(n - 1)S^2}{\chi_{\alpha/2, n-1}^2}, \; \frac{(n - 1)S^2}{\chi_{1-\alpha/2, n-1}^2}\right)$$

**Example 7.3.i.** Washer thicknesses: $n = 10$, 90% CI for $\sigma$: $(.00269, .00608)$.

**Table 7.1: $100(1 - \alpha)$ Percent Confidence Intervals ($X_1, \dots, X_n \sim N(\mu, \sigma^2)$)**

| Assumption | Parameter | Confidence Interval | Lower Interval | Upper Interval |
| :--- | :--- | :--- | :--- | :--- |
| $\sigma^2$ known | $\mu$ | $\bar{X} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$ | $\left(-\infty, \; \bar{X} + z_\alpha \frac{\sigma}{\sqrt{n}}\right)$ | $\left(\bar{X} - z_\alpha \frac{\sigma}{\sqrt{n}}, \; \infty\right)$ |
| $\sigma^2$ unknown | $\mu$ | $\bar{X} \pm t_{\alpha/2, n-1} \frac{S}{\sqrt{n}}$ | $\left(-\infty, \; \bar{X} + t_{\alpha, n-1} \frac{S}{\sqrt{n}}\right)$ | $\left(\bar{X} - t_{\alpha, n-1} \frac{S}{\sqrt{n}}, \; \infty\right)$ |
| $\mu$ unknown | $\sigma^2$ | $\left(\frac{(n-1)S^2}{\chi_{\alpha/2, n-1}^2}, \; \frac{(n-1)S^2}{\chi_{1-\alpha/2, n-1}^2}\right)$ | $\left(0, \; \frac{(n-1)S^2}{\chi_{1-\alpha, n-1}^2}\right)$ | $\left(\frac{(n-1)S^2}{\chi_{\alpha, n-1}^2}, \; \infty\right)$ |

## 7.4 Estimating the difference in means of two normal populations

Let $X_1, \dots, X_n \sim N(\mu_1, \sigma_1^2)$ and $Y_1, \dots, Y_m \sim N(\mu_2, \sigma_2^2)$ be independent.

### Known Variances
$$\mu_1 - \mu_2 \in \left(\bar{X} - \bar{Y} - z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}, \; \bar{X} - \bar{Y} + z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}\right)$$

**Example 7.4.a.** Cable insulation: $\sigma_A^2 = 40, \sigma_B^2 = 100 \implies \mu_B - \mu_A \in (6.49, 19.60)$.

### Unknown but Equal Variances $\sigma_1^2 = \sigma_2^2 = \sigma^2$
Pooled sample variance:

$$S_p^2 = \frac{(n - 1)S_1^2 + (m - 1)S_2^2}{n + m - 2}$$

Confidence interval:

$$\mu_1 - \mu_2 \in \left(\bar{X} - \bar{Y} \pm t_{\alpha/2, n+m-2} S_p \sqrt{\frac{1}{n} + \frac{1}{m}}\right) \tag{7.4.4}$$

**Example 7.4.b.** Equal variance case: 95% CI: $(5.83, 20.26)$.

**Table 7.2: $100(1 - \alpha)$ Percent Confidence Intervals for $\mu_1 - \mu_2$**

| Assumption | Confidence Interval | Lower Confidence Interval |
| :--- | :--- | :--- |
| $\sigma_1, \sigma_2$ known | $\bar{X} - \bar{Y} \pm z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}$ | $\left(-\infty, \; \bar{X} - \bar{Y} + z_\alpha\sqrt{\frac{\sigma_1^2}{n} + \frac{\sigma_2^2}{m}}\right)$ |
| $\sigma_1, \sigma_2$ unknown but equal | $\bar{X} - \bar{Y} \pm t_{\alpha/2, n+m-2} \sqrt{\left(\frac{1}{n} + \frac{1}{m}\right)\frac{(n-1)S_1^2 + (m-1)S_2^2}{n+m-2}}$ | $\left(-\infty, \; \bar{X} - \bar{Y} + t_{\alpha, n+m-2} \sqrt{\left(\frac{1}{n} + \frac{1}{m}\right)\frac{(n-1)S_1^2 + (m-1)S_2^2}{n+m-2}}\right)$ |

## 7.5 Approximate confidence interval for the mean of a Bernoulli random variable

For large $n$, with $\hat{p} = X/n$:

$$p \in \left(\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}\right)$$

**Example 7.5.a.** Transistors: $n = 100, X = 80 \implies \hat{p} = .8 \implies (.7216, .8784)$.

**Example 7.5.b.** Presidential poll: $\hat{p} = .52, \text{margin of error} = .04 \implies n \approx 599$.

**Sample Size:** To guarantee length $\le b$, $n \le (z_{\alpha/2})^2 / b^2$.

**Table 7.3: Approximate $100(1 - \alpha)$ Percent Confidence Intervals for $p$**

| Type of Interval | Confidence Interval |
| :--- | :--- |
| **Two-sided** | $\hat{p} \pm z_{\alpha/2}\sqrt{\hat{p}(1 - \hat{p})/n}$ |
| **One-sided lower** | $\left(-\infty, \; \hat{p} + z_\alpha\sqrt{\hat{p}(1 - \hat{p})/n}\right)$ |
| **One-sided upper** | $\left(\hat{p} - z_\alpha\sqrt{\hat{p}(1 - \hat{p})/n}, \; \infty\right)$ |

## 7.6 Confidence interval of the mean of the exponential distribution *(Optional)*

Since $\frac{2}{\theta} \sum_{i=1}^n X_i \sim \chi_{2n}^2$:

$$\theta \in \left(\frac{2\sum_{i=1}^n X_i}{\chi_{\alpha/2, 2n}^2}, \; \frac{2\sum_{i=1}^n X_i}{\chi_{1-\alpha/2, 2n}^2}\right)$$

**Example 7.6.a.** $n = 10, \sum X_i = 1740 \implies \theta \in (101.84, 362.85)$.

## 7.7 Evaluating a point estimator *(Optional)*

Mean square error:

$$r(d, \theta) = E[(d(X) - \theta)^2] = \text{Var}(d) + b_\theta^2(d)$$

where the bias is $b_\theta(d) = E[d(X)] - \theta$. For an unbiased estimator, $r(d, \theta) = \text{Var}(d)$.

**Example 7.7.a.** Sample mean is unbiased.

**Example 7.7.b (Optimal weights for independent unbiased estimators).**

$$\hat{\lambda} = \frac{1/\sigma_1^2}{1/\sigma_1^2 + 1/\sigma_2^2}, \qquad d = \frac{\sum_{i=1}^n d_i / \sigma_i^2}{\sum_{i=1}^n 1/\sigma_i^2}$$

**Example 7.7.c (Uniform $(0, \theta)$ estimators).**
- $d_1 = 2\bar{X} \implies r(d_1, \theta) = \frac{\theta^2}{3n}$
- $d_2 = \max X_i \implies r(d_2, \theta) = \frac{2\theta^2}{(n+1)(n+2)}$
- $d_{c^*} = \frac{n+2}{n+1} \max X_i \implies r(d_{c^*}, \theta) = \frac{\theta^2}{(n+1)^2}$ (minimal MSE among linear multiples)

## 7.8 The Bayes estimator *(Optional)*

Prior density $p(\theta)$, likelihood $f(x_1, \dots, x_n \mid \theta)$, posterior density:

$$f(\theta \mid x_1, \dots, x_n) = \frac{f(x_1, \dots, x_n \mid \theta)p(\theta)}{\int f(x_1, \dots, x_n \mid \theta)p(\theta) \, d\theta}$$

Bayes estimator minimizes expected squared error:

$$\hat{\theta}_{\text{Bayes}} = E[\theta \mid X_1, \dots, X_n]$$

**Example 7.8.a (Bernoulli with Uniform $(0, 1)$ Prior).** Posterior is Beta:

$$E[\theta \mid X_1, \dots, X_n] = \frac{\sum_{i=1}^n X_i + 1}{n + 2}$$

**Example 7.8.b (Normal Prior with Normal Likelihood).**
Prior $\theta \sim N(\mu, \sigma^2)$, data $X_i \sim N(\theta, \sigma_0^2)$:
Posterior is Normal with mean:

$$E[\theta \mid X_1, \dots, X_n] = \frac{\frac{n}{\sigma_0^2}}{\frac{n}{\sigma_0^2} + \frac{1}{\sigma^2}}\bar{X} + \frac{\frac{1}{\sigma^2}}{\frac{n}{\sigma_0^2} + \frac{1}{\sigma^2}}\mu \tag{7.8.3}$$
$$\text{Var}(\theta \mid X_1, \dots, X_n) = \frac{\sigma_0^2 \sigma^2}{n\sigma^2 + \sigma_0^2}$$

**Example 7.8.c.** Uniform prior mode equals MLE.

**Example 7.8.d.** Signal estimation with normal prior: $90\%$ credible interval is $(33.68, 53.82)$.

---

## Problems

1. Let $X_1, \dots, X_n$ be a sample from the distribution whose density function is
   $$f(x) = \begin{cases} e^{-(x-\theta)} & x \ge \theta \\ 0 & \text{otherwise} \end{cases}$$
   Determine the maximum likelihood estimator of $\theta$.

2. Determine the maximum likelihood estimator of $\theta$ when $X_1, \dots, X_n$ is a sample with density function
   $$f(x) = \frac{1}{2} e^{-|x-\theta|}, \quad -\infty < x < \infty$$

3. Let $X_1, \dots, X_n$ be a sample from a normal $\mu, \sigma^2$ population. Determine the maximum likelihood estimator of $\sigma^2$ when $\mu$ is known. What is the expected value of this estimator?

4. Determine the maximum likelihood estimates of $a$ and $\lambda$ when $X_1, \dots, X_n$ is a sample from the Pareto density function
   $$f(x) = \begin{cases} \lambda a^\lambda x^{-(\lambda+1)}, & \text{if } x \ge a \\ 0, & \text{if } x < a \end{cases}$$

5. Suppose that $X_1, \dots, X_n$ are normal with mean $\mu_1$; $Y_1, \dots, Y_n$ are normal with mean $\mu_2$; and $W_1, \dots, W_n$ are normal with mean $\mu_1 + \mu_2$. Assuming that all $3n$ random variables are independent with a common variance, find the maximum likelihood estimators of $\mu_1$ and $\mu_2$.

6. River floods are often measured by their discharges (in units of feet cubed per second). The value $v$ is said to be the value of a 100-year flood if $P\{D \ge v\} = .01$ where $D$ is the discharge of the largest flood in a randomly chosen year. The following table gives the flood discharges of the largest floods of the Blackstone River in Woonsocket, Rhode Island, in each of the years from 1929 to 1965. Assuming that these discharges follow a lognormal distribution, estimate the value of a 100-year flood.

**Table 7.4: Annual Floods of the Blackstone River (1929–1965).**

| Year | Flood Discharge ($\text{ft}^3/\text{s}$) | Year | Flood Discharge ($\text{ft}^3/\text{s}$) |
| :--- | :--- | :--- | :--- |
| 1929 | 4,570 | 1948 | 5,810 |
| 1930 | 1,970 | 1949 | 2,030 |
| 1931 | 8,220 | 1950 | 3,620 |
| 1932 | 4,530 | 1951 | 4,920 |
| 1933 | 5,780 | 1952 | 4,090 |
| 1934 | 6,560 | 1953 | 5,570 |
| 1935 | 7,500 | 1954 | 9,400 |
| 1936 | 15,000 | 1955 | 32,900 |
| 1937 | 6,340 | 1956 | 8,710 |
| 1938 | 15,100 | 1957 | 3,850 |
| 1939 | 3,840 | 1958 | 4,970 |
| 1940 | 5,860 | 1959 | 5,398 |
| 1941 | 4,480 | 1960 | 4,780 |
| 1942 | 5,330 | 1961 | 4,020 |
| 1943 | 5,310 | 1962 | 5,790 |
| 1944 | 3,830 | 1963 | 4,510 |
| 1945 | 3,410 | 1964 | 5,520 |
| 1946 | 3,830 | 1965 | 5,300 |
| 1947 | 3,150 | | |

7. Recall that $X$ is said to have a lognormal distribution with parameters $\mu$ and $\sigma^2$ if $\log(X)$ is normal with mean $\mu$ and variance $\sigma^2$. Suppose $X$ is such a lognormal random variable.
   a. Find $E[X]$.
   b. Find $\text{Var}(X)$. (*Hint: Make use of the formula for the moment generating function of a normal random variable.*)
   c. The following are, in minutes, travel times to work over a sequence of 10 days:
      $$42, 28, 53, 57, 67, 39, 35, 50, 44, 39$$
      Assuming an underlying lognormal distribution, use the data to estimate the mean travel time.

8. An electric scale gives a reading equal to the true weight plus a random error that is normally distributed with mean 0 and standard deviation $\sigma = .1$ mg. Suppose that the results of five successive weighings of the same object are as follows: $3.142, 3.163, 3.155, 3.150, 3.141$.
   a. Determine a 95 percent confidence interval estimate of the true weight.
   b. Determine a 99 percent confidence interval estimate of the true weight.

9. The PCB concentration of a fish caught in Lake Michigan was measured by a technique that is known to result in an error of measurement that is normally distributed with a standard deviation of $.08$ ppm (parts per million). Suppose the results of 10 independent measurements of this fish are:
   $$11.2, 12.4, 10.8, 11.6, 12.5, 10.1, 11.0, 12.2, 12.4, 10.6$$
   a. Give a 95 percent confidence interval for the PCB level of this fish.
   b. Give a 95 percent lower confidence interval.
   c. Give a 95 percent upper confidence interval.

10. The standard deviation of test scores on a certain achievement test is 11.3. If a random sample of 81 students had a sample mean score of 74.6, find a 90 percent confidence interval estimate for the average score of all students.

11. Let $X_1, \dots, X_n, X_{n+1}$ be a sample from a normal population having an unknown mean $\mu$ and variance 1. Let $\bar{X}_n = \sum_{i=1}^n X_i / n$ be the average of the first $n$ of them.
    a. What is the distribution of $X_{n+1} - \bar{X}_n$?
    b. If $\bar{X}_n = 4$, give an interval that, with 90 percent confidence, will contain the value of $X_{n+1}$.

12. If $X_1, \dots, X_n$ is a sample from a normal population whose mean $\mu$ is unknown but whose variance $\sigma^2$ is known, show that $(-\infty, \bar{X} + z_\alpha \sigma/\sqrt{n})$ is a $100(1 - \alpha)$ percent lower confidence interval for $\mu$.

13. A sample of 20 cigarettes is tested to determine nicotine content and the average value observed was 1.2 mg. Compute a 99 percent two-sided confidence interval for the mean nicotine content of a cigarette if it is known that the standard deviation of a cigarette’s nicotine content is $\sigma = .2$ mg.

14. In Problem 13, suppose that the population variance is not known in advance of the experiment. If the sample variance is $.04$, compute a 99 percent two-sided confidence interval for the mean nicotine content.

15. In Problem 14, compute a value $c$ for which we can assert “with 99 percent confidence” that $c$ is larger than the mean nicotine content of a cigarette.

16. Suppose that when sampling from a normal population having an unknown mean $\mu$ and unknown variance $\sigma^2$, we wish to determine a sample size $n$ so as to guarantee that the resulting $100(1 - \alpha)$ percent confidence interval for $\mu$ will be of size no greater than $A$, for given values $\alpha$ and $A$. Explain how we can approximately do this by a double sampling scheme that first takes a subsample of size 30 and then chooses the total sample size by using the results of the first subsample.

17. The following data resulted from 24 independent measurements of the melting point of lead:
    $$\begin{matrix}
    330^\circ\text{C} & 322^\circ\text{C} & 345^\circ\text{C} \\
    328.6^\circ\text{C} & 331^\circ\text{C} & 342^\circ\text{C} \\
    342.4^\circ\text{C} & 340.4^\circ\text{C} & 329.7^\circ\text{C} \\
    334^\circ\text{C} & 326.5^\circ\text{C} & 325.8^\circ\text{C} \\
    337.5^\circ\text{C} & 327.3^\circ\text{C} & 322.6^\circ\text{C} \\
    341^\circ\text{C} & 340^\circ\text{C} & 333^\circ\text{C} \\
    343.3^\circ\text{C} & 331^\circ\text{C} & 341^\circ\text{C} \\
    329.5^\circ\text{C} & 332.3^\circ\text{C} & 340^\circ\text{C}
    \end{matrix}$$
    Assuming that the measurements can be regarded as constituting a normal sample whose mean is the true melting point of lead, determine a 95 percent two-sided confidence interval for this value. Also determine a 99 percent two-sided confidence interval.

18. The following are scores on IQ tests of a random sample of 18 students at a large eastern university:
    $$130, 122, 119, 142, 136, 127, 120, 152, 141,$$
    $$132, 127, 118, 150, 141, 133, 137, 129, 142$$
    a. Construct a 95 percent confidence interval estimate of the average IQ score of all students at the university.
    b. Construct a 95 percent lower confidence interval estimate.
    c. Construct a 95 percent upper confidence interval estimate.

19. Suppose that a random sample of nine recently sold houses in a certain city resulted in a sample mean price of $222,000, with a sample standard deviation of $22,000. Give a 95 percent upper confidence interval for the mean price of all recently sold houses in this city.

20. A company self-insures its large fleet of cars against collisions. To determine its mean repair cost per collision, it has randomly chosen a sample of 16 accidents. If the average repair cost in these accidents is $2200 with a sample standard deviation of $800, find a 90 percent confidence interval estimate of the mean cost per collision.

21. A standardized test is given annually to all sixth-grade students in the state of Washington. To determine the average score of students in her district, a school supervisor selects a random sample of 100 students. If the sample mean of these students’ scores is 320 and the sample standard deviation is 16, give a 95 percent confidence interval estimate of the average score of students in that supervisor’s district.

22. Each of 20 science students independently measured the melting point of lead. The sample mean and sample standard deviation of these measurements were (in degrees centigrade) 330.2 and 15.4, respectively. Construct (a) a 95 percent and (b) a 99 percent confidence interval estimate of the true melting point of lead.

23. A random sample of 300 CitiBank VISA cardholder accounts indicated a sample mean debt of $1220 with a sample standard deviation of $840. Construct a 95 percent confidence interval estimate of the average debt of all cardholders.

24. In Problem 23, find the smallest value $v$ that “with 90 percent confidence,” exceeds the average debt per cardholder.

25. Verify the formula given in Table 7.1 for the $100(1 - \alpha)$ percent lower confidence interval for $\mu$ when $\sigma$ is unknown.

26. The following are the daily number of steps taken by a certain individual in 20 weekdays:
    $$2,100 \quad 1,984 \quad 2,072 \quad 1,898$$
    $$1,950 \quad 1,992 \quad 2,096 \quad 2,103$$
    $$2,043 \quad 2,218 \quad 2,244 \quad 2,206$$
    $$2,210 \quad 2,152 \quad 1,962 \quad 2,007$$
    $$2,018 \quad 2,106 \quad 1,938 \quad 1,956$$
    Assuming that the daily number of steps is normally distributed, construct (a) a 95 percent and (b) a 99 percent two-sided confidence interval for the mean number of steps. (c) Determine the largest value $v$ that, “with 95 percent confidence,” will be less than the mean range.

27. Studies were conducted in Los Angeles to determine the carbon monoxide concentration near freeways. The measurements in ppm (parts per million) over a sampled period during the year were:
    $$102.2, 98.4, 104.1, 101, 102.2, 100.4, 98.6, 88.2, 78.8, 83,$$
    $$84.7, 94.8, 105.1, 106.2, 111.2, 108.3, 105.2, 103.2, 99, 98.8$$
    Compute a 95 percent two-sided confidence interval for the mean carbon monoxide concentration.

28. A set of 10 determinations, by a method devised by the chemist Karl Fischer, of the percentage of water in a methanol solution yielded the following data:
    $$.50, .55, .53, .56, .54, .57, .52, .60, .55, .58$$
    Assuming normality, use these data to give a 95 percent confidence interval for the actual percentage.

29. Suppose that $U_1, U_2, \dots$ is a sequence of independent uniform $(0, 1)$ random variables, and define $N$ by
    $$N = \min\{n : U_1 + \dots + U_n > 1\}$$
    That is, $N$ is the number of uniform $(0, 1)$ random variables that need to be summed to exceed 1. Use random numbers to determine the value of 36 random variables having the same distribution as $N$, and then use these data to obtain a 95 percent confidence interval estimate of $E[N]$. Based on this interval, guess the exact value of $E[N]$.

30. An important issue for a retailer is to decide when to reorder stock from a supplier. Suppose that the following data give the numbers of a certain type of item sold in each of 30 weeks:
    $$14, 8, 12, 9, 5, 22, 15, 12, 16, 7, 10, 9, 15, 15, 12,$$
    $$9, 11, 16, 8, 7, 15, 13, 9, 5, 18, 14, 10, 13, 7, 11$$
    Assuming that the numbers sold each week are independent random variables from a common distribution, use the data to obtain a 95 percent confidence interval for the mean number sold in a week.

31. A random sample of 16 professors at a large private university yielded a sample mean annual salary of $90,450 with a sample standard deviation of $9400. Determine a 95 percent confidence interval of the average salary of all professors at that university.

32. Let $X_1, \dots, X_{n+1}$ be a sample from a population with mean $\mu$ and variance $\sigma^2$. As noted in the text, the natural predictor of $X_{n+1}$ based on the data values $X_1, \dots, X_n$ is $\bar{X}_n = \sum_{i=1}^n X_i / n$. Determine the mean square error of this predictor. That is, find $E[(X_{n+1} - \bar{X}_n)^2]$.

33. National Safety Council data show that the number of accidental deaths due to drowning in the United States in the years from 1990 to 1993 were (in units of one thousand) 5.2, 4.6, 4.3, 4.8. Use these data to give an interval that will, with 95 percent confidence, contain the number of such deaths in 1994.

34. The daily dissolved oxygen concentration for a water stream has been recorded over 30 days. If the sample average of the 30 values is 2.5 mg/liter and the sample standard deviation is 2.12 mg/liter, determine a value which, with 90 percent confidence, exceeds the mean daily concentration.

35. Verify the formulas given in Table 7.1 for the $100(1 - \alpha)$ percent lower and upper confidence intervals for $\sigma^2$.

36. The capacities (in ampere-hours) of 10 batteries were recorded as follows:
    $$140, 136, 150, 144, 148, 152, 138, 141, 143, 151$$
    a. Estimate the population variance $\sigma^2$.
    b. Compute a 99 percent two-sided confidence interval for $\sigma^2$.
    c. Compute a value $v$ that enables us to state, with 90 percent confidence, that $\sigma^2$ is less than $v$.

37. Find a 95 percent two-sided confidence interval for the variance of the diameter of a rivet based on the data given here:
    $$\begin{matrix}
    6.68 & 6.66 & 6.62 & 6.72 \\
    6.76 & 6.67 & 6.70 & 6.72 \\
    6.78 & 6.66 & 6.76 & 6.72 \\
    6.76 & 6.70 & 6.76 & 6.76 \\
    6.74 & 6.74 & 6.81 & 6.66 \\
    6.64 & 6.79 & 6.72 & 6.82 \\
    6.81 & 6.77 & 6.60 & 6.72 \\
    6.74 & 6.70 & 6.64 & 6.78 \\
    6.70 & 6.70 & 6.75 & 6.79
    \end{matrix}$$
    Assume a normal population.

38. The following are independent samples from two normal populations, both of which have the same standard deviation $\sigma$:
    $$16, 17, 19, 20, 18 \quad \text{and} \quad 3, 4, 8$$
    Use them to estimate $\sigma$.

39. The amount of beryllium in a substance is often determined by the use of a photometric filtration method. If the weight of the beryllium is $\mu$, then the value given by the photometric filtration method is normally distributed with mean $\mu$ and standard deviation $\sigma$. A total of eight independent measurements of 3.180 mg of beryllium gave the following results:
    $$3.166, 3.192, 3.175, 3.180, 3.182, 3.171, 3.184, 3.177$$
    Use the preceding data to
    a. estimate $\sigma$;
    b. find a 90 percent confidence interval estimate of $\sigma$.

40. If $X_1, \dots, X_n$ is a sample from a normal population, explain how to obtain a $100(1 - \alpha)$ percent confidence interval for the population variance $\sigma^2$ when the population mean $\mu$ is known. Explain in what sense knowledge of $\mu$ improves the interval estimator compared with when it is unknown. Repeat Problem 38 if it is known that the mean burning time is 53.6 seconds.

41. A civil engineer wishes to measure the compressive strength of two different types of concrete. A random sample of 10 specimens of the first type yielded the following data (in psi):
    $$\text{Type 1: } 3250, 3268, 4302, 3184, 3266, 3297, 3332, 3502, 3064, 3116$$
    whereas a sample of 10 specimens of the second yielded the data:
    $$\text{Type 2: } 3094, 3106, 3004, 3066, 2984, 3124, 3316, 3212, 3380, 3018$$
    If we assume that the samples are normal with a common variance, determine
    a. a 95 percent two-sided confidence interval for $\mu_1 - \mu_2$, the difference in means;
    b. a 95 percent one-sided upper confidence interval for $\mu_1 - \mu_2$;
    c. a 95 percent one-sided lower confidence interval for $\mu_1 - \mu_2$.

42. Independent random samples are taken from the output of two machines on a production line. The weight of each item is of interest. From the first machine, a sample of size 36 is taken, with sample mean weight of 120 grams and a sample variance of 4. From the second machine, a sample of size 64 is taken, with a sample mean weight of 130 grams and a sample variance of 5. It is assumed that the weights of items from the first machine are normally distributed with mean $\mu_1$ and variance $\sigma^2$ and that the weights of items from the second machine are normally distributed with mean $\mu_2$ and variance $\sigma^2$ (that is, the variances are assumed to be equal). Find a 99 percent confidence interval for $\mu_1 - \mu_2$, the difference in population means.

43. Do Problem 42 when it is known in advance that the population variances are 4 and 5.

44. The following are the daily numbers of company website visits resulting from advertisements on two different types of media:

| Type I | Type II |
| :--- | :--- |
| 481 572 | 526 537 |
| 506 561 | 511 582 |
| 527 501 | 556 605 |
| 661 487 | 542 558 |
| 501 524 | 491 578 |

    Find a 99 percent confidence interval for the mean difference in daily visits assuming normality with unknown but equal variances.

45. If $X_1, \dots, X_n$ is a sample from a normal population having known mean $\mu_1$ and unknown variance $\sigma_1^2$, and $Y_1, \dots, Y_m$ is an independent sample from a normal population having known mean $\mu_2$ and unknown variance $\sigma_2^2$, determine a $100(1 - \alpha)$ percent confidence interval for $\sigma_1^2 / \sigma_2^2$.

46. Two analysts took repeated readings on the hardness of city water. Assuming that the readings of analyst $i$ constitute a sample from a normal population having variance $\sigma_i^2, i = 1, 2$, compute a 95 percent two-sided confidence interval for $\sigma_1^2 / \sigma_2^2$ when the data are as follows:

| Analyst 1 | Analyst 2 |
| :--- | :--- |
| .46 | .82 |
| .62 | .61 |
| .37 | .89 |
| .40 | .51 |
| .44 | .33 |
| .58 | .48 |
| .48 | .23 |
| .53 | .25 |
| | .67 |
| | .88 |

47. A problem of interest in baseball is whether a sacrifice bunt is a good strategy when there is a man on first base and no outs. The following data resulted from a study of randomly chosen Major League Baseball games played in 1959 and 1960:

| Base Occupied | Number of Outs | Number of Cases in Which 0 Runs Are Scored | Total Number of Cases |
| :--- | :--- | :--- | :--- |
| First | 0 | 1044 | 1728 |
| Second | 1 | 401 | 657 |

    a. Give a 95 percent confidence interval estimate for the probability of scoring at least one run when there is a man on first and no outs.
    b. Give a 95 percent confidence interval estimate for the probability of scoring at least one run when there is a man on second and one out.

48. A random sample of 1200 engineers included 48 Hispanic Americans, 80 African Americans, and 204 females. Determine 90 percent confidence intervals for the proportion of all engineers who are
    a. female;
    b. Hispanic Americans or African Americans.

49. To estimate $p$, the proportion of all newborn babies that are male, the gender of 10,000 newborn babies was noted. If 5106 of them were male, determine (a) a 90 percent and (b) a 99 percent confidence interval estimate of $p$.

50. An airline is interested in determining the proportion of its customers who are flying for reasons of business. If they want to be 90 percent certain that their estimate will be correct to within 2 percent, how large a random sample should they select?

51. A recent newspaper poll indicated that Candidate A is favored over Candidate B by a 53 to 47 percentage, with a margin of error of $\pm 4$ percent. The newspaper then stated that since the 6-point gap is larger than the margin of error, its readers can be certain that Candidate A is the current choice. Is this reasoning correct?

52. A market research firm is interested in determining the proportion of households that are watching a particular sporting event. To accomplish this task, they plan on using a telephone poll of randomly chosen households. How large a sample is needed if they want to be 90 percent certain that their estimate is correct to within $\pm .02$?

53. In a recent study, 79 of 140 meteorites were observed to enter the atmosphere with a velocity of less than 25 miles per second. If we take $\hat{p} = 79/140$ as an estimate of the probability that an arbitrary meteorite that enters the atmosphere will have a speed less than 25 miles per second, what can we say, with 99 percent confidence, about the maximum error of our estimate?

54. A random sample of 100 items from a production line revealed 17 of them to be defective. Compute a 95 percent two-sided confidence interval for the probability that an item produced is defective. Determine also a 99 percent upper confidence interval for this value. What assumptions are you making?

55. Of 100 randomly detected cases of individuals having lung cancer, 67 died within 5 years of detection.
    a. Estimate the probability that a person contracting lung cancer will die within 5 years.
    b. How large an additional sample would be required to be 95 percent confident that the error in estimating the probability in part (a) is less than $.02$?

56. Derive $100(1 - \alpha)$ percent lower and upper confidence intervals for $p$, when the data consist of the values of $n$ independent Bernoulli random variables with parameter $p$.

57. Suppose the lifetimes of batteries are exponentially distributed with mean $\theta$. If the average of a sample of 10 batteries is 36 hours, determine a 95 percent two-sided confidence interval for $\theta$.

58. Determine $100(1 - \alpha)$ percent one-sided upper and lower confidence intervals for $\theta$ in Problem 57.

59. Let $X_1, \dots, X_n$ denote a sample from a population whose mean value $\theta$ is unknown. Use the results of Example 7.7.b to argue that among all unbiased estimators of $\theta$ of the form $\sum_{i=1}^n \lambda_i X_i, \sum_{i=1}^n \lambda_i = 1$, the one with minimal mean square error has $\lambda_i \equiv 1/n, i = 1, \dots, n$.

60. Consider two independent samples from normal populations having the same variance $\sigma^2$, of respective sizes $n$ and $m$. That is, $X_1, \dots, X_n$ and $Y_1, \dots, Y_m$ are independent samples from normal populations each having variance $\sigma^2$. Let $S_x^2$ and $S_y^2$ denote the respective sample variances. Thus both $S_x^2$ and $S_y^2$ are unbiased estimators of $\sigma^2$. Show by using the results of Example 7.7.b along with the fact that $\text{Var}(\chi_k^2) = 2k$ that the minimum mean square estimator of $\sigma^2$ of the form $\lambda S_x^2 + (1 - \lambda)S_y^2$ is
    $$S_p^2 = \frac{(n - 1)S_x^2 + (m - 1)S_y^2}{n + m - 2}$$

61. Consider two estimators $d_1$ and $d_2$ of a parameter $\theta$. If $E[d_1] = \theta, \text{Var}(d_1) = 6$ and $E[d_2] = \theta + 2, \text{Var}(d_2) = 2$, which estimator should be preferred?

62. Suppose that the number of accidents occurring daily in a certain plant has a Poisson distribution with an unknown mean $\lambda$. Based on previous experience in similar industrial plants, suppose that a statistician’s initial feelings about the possible value of $\lambda$ can be expressed by an exponential distribution with parameter 1. That is, the prior density is $p(\lambda) = e^{-\lambda}, 0 < \lambda < \infty$. Determine the Bayes estimate of $\lambda$ if there are a total of 83 accidents over the next 10 days. What is the maximum likelihood estimate?

63. The functional lifetimes in hours of computer chips produced by a certain semiconductor firm are exponentially distributed with mean $1/\lambda$. Suppose that the prior distribution on $\lambda$ is the gamma distribution with density function
    $$g(x) = \frac{e^{-x}x^2}{2}, \quad 0 < x < \infty$$
    If the average life of the first 20 chips tested is 4.6 hours, compute the Bayes estimate of $\lambda$.

64. Each item produced will, independently, be defective with probability $p$. If the prior distribution on $p$ is uniform on $(0, 1)$, compute the posterior probability that $p$ is less than $.2$ given
    a. a total of 2 defectives out of a sample of size 10;
    b. a total of 1 defective out of a sample of size 10;
    c. a total of 10 defectives out of a sample of size 10.

65. The breaking strength of a certain type of cloth is to be measured for 10 specimens. The underlying distribution is normal with unknown mean $\theta$ but with a standard deviation equal to 3 psi. Suppose also that based on previous experience we feel that the unknown mean has a prior distribution that is normally distributed with mean 200 and standard deviation 2. If the average breaking strength of a sample of 20 specimens is 182 psi, determine a region that contains $\theta$ with probability $.95$.
