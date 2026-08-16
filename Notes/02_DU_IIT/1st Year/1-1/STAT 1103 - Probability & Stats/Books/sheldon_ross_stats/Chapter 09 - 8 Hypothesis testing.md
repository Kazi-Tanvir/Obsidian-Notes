# Chapter 8: Hypothesis testing

## 8.1 Introduction

As in the previous chapter, let us suppose that a random sample from a population distribution, specified except for a vector of unknown parameters, is to be observed. However, rather than wishing to explicitly estimate the unknown parameters, let us now suppose that we are primarily concerned with using the resulting sample to test some particular hypothesis concerning them. As an illustration, suppose that a construction firm has just purchased a large supply of cables that have been guaranteed to have an average breaking strength of at least 7000 pounds per square inch (PSI). To verify this claim, the firm has decided to take a random sample of 10 of these cables to determine their breaking strengths. They will then use the result of this experiment to ascertain whether or not they accept the cable manufacturer’s hypothesis that the population mean is at least 7000 PSI.

A *statistical hypothesis* is usually a statement about a set of parameters of a population distribution. It is called a hypothesis because it is not known whether or not it is true. A primary problem is to develop a procedure for determining whether or not the values of a random sample from this population are consistent with the hypothesis. For instance, consider a particular normally distributed population having an unknown mean value $\theta$ and known variance 1. The statement “$\theta$ is less than 1” is a statistical hypothesis that we could try to test by observing a random sample from this population. If the random sample is deemed to be consistent with the hypothesis under consideration, we say that the hypothesis has been “accepted”; otherwise we say that it has been “rejected.”

Note that in accepting a given hypothesis we are not actually claiming that it is true but rather we are saying that the resulting data appear to be consistent with it.

## 8.2 Significance levels

Consider a population having distribution $F_\theta$, where $\theta$ is unknown, and suppose we want to test a specific hypothesis about $\theta$. We shall denote this hypothesis by $H_0$ and call it the *null hypothesis*. For example, if $F_\theta$ is a normal distribution function with mean $\theta$ and variance equal to 1, then two possible null hypotheses about $\theta$ are:
(a) $H_0 : \theta = 1$
(b) $H_0 : \theta \le 1$

A hypothesis that, when true, completely specifies the population distribution is called a *simple hypothesis*; one that does not is called a *composite hypothesis*.

A test for $H_0$ can be specified by defining a region $C$ in $n$-dimensional space (called the *critical region*) such that:
- accepts $H_0$ if $(X_1, \dots, X_n) \notin C$
- rejects $H_0$ if $(X_1, \dots, X_n) \in C$

### Errors in Hypothesis Testing
- **Type I error:** Incorrectly rejecting $H_0$ when it is true.
- **Type II error:** Incorrectly accepting $H_0$ when it is false.

The probability of a Type I error is bounded by $\alpha$, the *level of significance* of the test (commonly $\alpha = .1, .05, .005$).

## 8.3 Tests concerning the mean of a normal population

### 8.3.1 Case of known variance

Suppose that $X_1, \dots, X_n \sim N(\mu, \sigma^2)$ where $\sigma^2$ is known. To test:

$$H_0 : \mu = \mu_0 \quad \text{versus} \quad H_1 : \mu \neq \mu_0$$

Test statistic:

$$Z = \frac{\sqrt{n}(\bar{X} - \mu_0)}{\sigma} \sim N(0, 1) \quad \text{under } H_0$$

Decision rule at significance level $\alpha$:
- Reject $H_0$ if $\frac{\sqrt{n}}{\sigma} |\bar{X} - \mu_0| > z_{\alpha/2}$
- Accept $H_0$ if $\frac{\sqrt{n}}{\sigma} |\bar{X} - \mu_0| \le z_{\alpha/2} \tag{8.3.3}$

The $p$-value of the test is:

$$\text{$p$-value} = 2P\{Z \ge |t|\}$$

where $t = \frac{\sqrt{n}(\bar{x} - \mu_0)}{\sigma}$.

**Example 8.3.a.** Signal transmission: $n = 5, \sigma = 2, \mu_0 = 8, \bar{X} = 9.5$.

$$\text{TS} = \frac{\sqrt{5}}{2}(1.5) = 1.68 < z_{.025} = 1.96 \implies \text{Accept } H_0 \text{ at } \alpha = .05 \quad \blacksquare$$

**Example 8.3.b.** $p$-value for $\bar{X} = 8.5$: $\text{TS} = .559 \implies p\text{-value} = 2P\{Z > .559\} = .576$.
For $\bar{X} = 11.5$: $\text{TS} = 3.913 \implies p\text{-value} \approx .00005$ (reject $H_0$).

#### Operating Characteristic (OC) Curve and Power
The probability of accepting $H_0$ when the true mean is $\mu$:

$$\beta(\mu) = \Phi\left(\frac{\sqrt{n}(\mu_0 - \mu)}{\sigma} + z_{\alpha/2}\right) - \Phi\left(\frac{\sqrt{n}(\mu_0 - \mu)}{\sigma} - z_{\alpha/2}\right) \tag{8.3.4}$$

The *power* of the test is $1 - \beta(\mu)$.

**Sample Size Formula:** To ensure $\beta(\mu_1) \approx \beta$:

$$n \approx \frac{(z_{\alpha/2} + z_\beta)^2 \sigma^2}{(\mu_1 - \mu_0)^2} \tag{8.3.7}$$

**Example 8.3.c.** In Example 8.3.a with true mean $\mu = 10$: $\beta(10) = .392$.

**Example 8.3.d.** $n \approx \frac{(1.96 + .67)^2}{(1.2)^2} 4 \approx 19.21 \implies n = 20$.

#### 8.3.1.1 One-sided tests
1. To test $H_0 : \mu \le \mu_0$ vs $H_1 : \mu > \mu_0$:
   - Reject $H_0$ if $\frac{\sqrt{n}}{\sigma}(\bar{X} - \mu_0) > z_\alpha$.
   - $p\text{-value} = P\{Z \ge t\}$.

2. To test $H_0 : \mu \ge \mu_0$ vs $H_1 : \mu < \mu_0$:
   - Reject $H_0$ if $\frac{\sqrt{n}}{\sigma}(\bar{X} - \mu_0) < -z_\alpha$.
   - $p\text{-value} = P\{Z \le t\}$.

**Example 8.3.e.** $H_0 : \mu = 8$ vs $H_1 : \mu > 8 \implies \text{TS} = 1.68 \implies p\text{-value} = 1 - \Phi(1.68) = .0465$.

**Example 8.3.f.** Cigarette nicotine: $n = 20, \sigma = .8, \bar{X} = 1.54$. $H_0 : \mu \ge 1.6$ vs $H_1 : \mu < 1.6$. $\text{TS} = -.336 \implies p\text{-value} = .368$ (do not reject $H_0$).

**Table 8.1: $X_1, \dots, X_n \sim N(\mu, \sigma^2)$, $\sigma^2$ Known**

| $H_0$ | $H_1$ | Test Statistic TS | Significance Level $\alpha$ Test | $p$-Value if $\text{TS} = t$ |
| :--- | :--- | :--- | :--- | :--- |
| $\mu = \mu_0$ | $\mu \neq \mu_0$ | $\sqrt{n}(\bar{X} - \mu_0)/\sigma$ | Reject if $|\text{TS}| > z_{\alpha/2}$ | $2P\{Z \ge |t|\}$ |
| $\mu \le \mu_0$ | $\mu > \mu_0$ | $\sqrt{n}(\bar{X} - \mu_0)/\sigma$ | Reject if $\text{TS} > z_\alpha$ | $P\{Z \ge t\}$ |
| $\mu \ge \mu_0$ | $\mu < \mu_0$ | $\sqrt{n}(\bar{X} - \mu_0)/\sigma$ | Reject if $\text{TS} < -z_\alpha$ | $P\{Z \le t\}$ |

### 8.3.2 Case of unknown variance: the $t$-test

Test statistic:

$$T = \frac{\sqrt{n}(\bar{X} - \mu_0)}{S} \sim t_{n-1} \quad \text{under } H_0$$

For two-sided test $H_0 : \mu = \mu_0$ vs $H_1 : \mu \neq \mu_0$:
- Reject $H_0$ if $|T| > t_{\alpha/2, n-1} \tag{8.3.12}$
- $p\text{-value} = 2P\{T_{n-1} \ge |t|\}$

**Example 8.3.g.** Cholesterol study: $n = 50, \bar{X} = 14.8, S = 6.4 \implies T = \frac{\sqrt{50}(14.8)}{6.4} = 16.352$ (reject $H_0$).

**Example 8.3.h.** Water use: $n = 20, \mu_0 = 350, \bar{X} = 353.8, S = 21.8478 \implies T = .7778 \implies p\text{-value} = .4462$.

In R:

```r
> t.test(x, mu = 350)
```

**Example 8.3.i.** Tire mileage: $n = 12, \bar{X} = 37.2833, S = 2.7319$. $H_0 : \mu \ge 40$ vs $H_1 : \mu < 40$. $T = -3.4448 \implies p\text{-value} = .0027$.

**Example 8.3.j.** Service time: $n = 28, \mu_0 = 8 \implies T = 2.257 \implies p\text{-value} = .016$.

**Table 8.2: $X_1, \dots, X_n \sim N(\mu, \sigma^2)$, $\sigma^2$ Unknown**

| $H_0$ | $H_1$ | Test Statistic TS | Significance Level $\alpha$ Test | $p$-Value if $\text{TS} = t$ |
| :--- | :--- | :--- | :--- | :--- |
| $\mu = \mu_0$ | $\mu \neq \mu_0$ | $\sqrt{n}(\bar{X} - \mu_0)/S$ | Reject if $|\text{TS}| > t_{\alpha/2, n-1}$ | $2P\{T_{n-1} \ge |t|\}$ |
| $\mu \le \mu_0$ | $\mu > \mu_0$ | $\sqrt{n}(\bar{X} - \mu_0)/S$ | Reject if $\text{TS} > t_{\alpha, n-1}$ | $P\{T_{n-1} \ge t\}$ |
| $\mu \ge \mu_0$ | $\mu < \mu_0$ | $\sqrt{n}(\bar{X} - \mu_0)/S$ | Reject if $\text{TS} < -t_{\alpha, n-1}$ | $P\{T_{n-1} \le t\}$ |

## 8.4 Testing the equality of means of two normal populations

### 8.4.1 Case of known variances
Test statistic:

$$Z = \frac{\bar{X} - \bar{Y}}{\sqrt{\sigma_x^2/n + \sigma_y^2/m}} \sim N(0, 1) \quad \text{under } H_0$$

**Example 8.4.a.** Tire lives: $\text{TS} = .066 \implies \text{Accept } H_0$.

### 8.4.2 Case of unknown variances with $\sigma_x^2 = \sigma_y^2 = \sigma^2$
Pooled variance:

$$S_p^2 = \frac{(n - 1)S_x^2 + (m - 1)S_y^2}{n + m - 2}$$

Test statistic:

$$T = \frac{\bar{X} - \bar{Y}}{S_p \sqrt{\frac{1}{n} + \frac{1}{m}}} \sim t_{n+m-2} \quad \text{under } H_0$$

In R:

```r
> t.test(x, y, var.equal = TRUE)
```

**Example 8.4.b.** Vitamin C vs placebo: $n = 10, m = 12$. $T = -1.8987, \text{df} = 20, p\text{-value} = 0.03606 \implies \text{Reject } H_0$.

### 8.4.3 Case of unknown and unequal variances
For large $n$ and $m$:

$$Z \approx \frac{\bar{X} - \bar{Y}}{\sqrt{S_x^2/n + S_y^2/m}} \sim N(0, 1)$$

*(Behrens-Fisher Problem)*

**Table 8.4: Two-Sample Tests for $H_0 : \mu_1 = \mu_2$ vs $H_1 : \mu_1 \neq \mu_2$**

| Assumption | Test Statistic TS | Significance Level $\alpha$ Test | $p$-Value if $\text{TS} = t$ |
| :--- | :--- | :--- | :--- |
| $\sigma_1, \sigma_2$ known | $\frac{\bar{X} - \bar{Y}}{\sqrt{\sigma_1^2/n + \sigma_2^2/m}}$ | Reject if $|\text{TS}| > z_{\alpha/2}$ | $2P\{Z \ge |t|\}$ |
| $\sigma_1 = \sigma_2$ | $\frac{\bar{X} - \bar{Y}}{\sqrt{\frac{(n-1)S_1^2 + (m-1)S_2^2}{n+m-2}}\sqrt{1/n + 1/m}}$ | Reject if $|\text{TS}| > t_{\alpha/2, n+m-2}$ | $2P\{T_{n+m-2} \ge |t|\}$ |
| $n, m$ large | $\frac{\bar{X} - \bar{Y}}{\sqrt{S_1^2/n + S_2^2/m}}$ | Reject if $|\text{TS}| > z_{\alpha/2}$ | $2P\{Z \ge |t|\}$ |

### 8.4.4 The paired $t$-test

When observations are paired $(X_i, Y_i)$, compute differences $W_i = X_i - Y_i$:

$$T = \frac{\sqrt{n}\bar{W}}{S_w} \sim t_{n-1}$$

**Example 8.4.c.** Industrial safety program (10 plants before and after):
$v = -2.2659, \text{df} = 9 \implies p\text{-value} = P(T_9 \le -2.266) = 0.0248 \implies \text{Reject } H_0$.

## 8.5 Hypothesis tests concerning the variance of a normal population

To test $H_0 : \sigma^2 = \sigma_0^2$ vs $H_1 : \sigma^2 \neq \sigma_0^2$:

$$\text{TS} = \frac{(n - 1)S^2}{\sigma_0^2} \sim \chi_{n-1}^2 \quad \text{under } H_0$$

$$p\text{-value} = 2\min\left(P\{\chi_{n-1}^2 < c\}, \; 1 - P\{\chi_{n-1}^2 < c\}\right)$$

**Example 8.5.a.** Tape ribbon thickness: $n = 20, S^2 = .025, \sigma_0^2 = .0225 \implies \text{TS} = 21.111 \implies p\text{-value} = P\{\chi_{19}^2 > 21.111\} = 0.3307$.

### 8.5.1 Testing for the equality of variances of two normal populations
To test $H_0 : \sigma_x^2 = \sigma_y^2$ vs $H_1 : \sigma_x^2 \neq \sigma_y^2$:

$$\text{TS} = \frac{S_x^2}{S_y^2} \sim F_{n-1, m-1} \quad \text{under } H_0$$

$$p\text{-value} = 2\min\left(P\{F_{n-1, m-1} < v\}, \; 1 - P\{F_{n-1, m-1} < v\}\right)$$

**Example 8.5.b.** Chemical catalyst yields: $n = 10, m = 12, S_1^2 = .14, S_2^2 = .28 \implies F = .5 \implies p\text{-value} = .3075$.

## 8.6 Hypothesis tests in Bernoulli populations

To test $H_0 : p \le p_0$ vs $H_1 : p > p_0$:
- Exact $p$-value: $P\{\text{Bin}(n, p_0) \ge x\}$.

**Example 8.6.a.** Chip defectives: $n = 300, p_0 = .02, x = 10 \implies p\text{-value} = 1 - \text{pbinom}(9, 300, .02) = 0.0818$.

**Example 8.6.b.** Proofreader comparison: 18 out of 26 $\implies p\text{-value} = P\{\text{Bin}(26, .5) \ge 18\} = 0.0378$.

**Large Sample Test:**

$$\text{TS} = \frac{X - np_0}{\sqrt{np_0(1 - p_0)}} \approx Z \sim N(0, 1)$$

**Example 8.6.c.** $Z = 1.443 \implies p\text{-value} = .0745$.

**Two-sided Test $H_0 : p = p_0$ vs $H_1 : p \neq p_0$:**

$$p\text{-value} = 2\min(P\{\text{Bin}(n, p_0) \ge x\}, \; P\{\text{Bin}(n, p_0) \le x\})$$

**Example 8.6.d.** $n = 500, p_0 = .04, x = 16 \implies p\text{-value} = 2P\{X \le 16\} = 0.4316$.

### 8.6.1 Testing the equality of parameters in two Bernoulli populations
Fisher-Irwin Test: Given $X_1 + X_2 = k$, the conditional distribution of $X_1$ is hypergeometric:

$$P_{H_0}\{X_1 = i \mid X_1 + X_2 = k\} = \frac{\binom{n_1}{i}\binom{n_2}{k-i}}{\binom{n_1+n_2}{k}} \tag{8.6.1}$$

$$p\text{-value} = 2\min(P\{X \le x_1\}, \; P\{X \ge x_1\}) \tag{8.6.3}$$

**Example 8.6.e.** Transistor comparison: $n_1 = 100, x_1 = 20, n_2 = 100, x_2 = 12 \implies p\text{-value} = 0.1763$.

**Example 8.6.f.** DES observational study.

## 8.7 Tests concerning the mean of a Poisson distribution

To test $H_0 : \lambda = \lambda_0$ vs $H_1 : \lambda \neq \lambda_0$:

$$p\text{-value} = 2\min(P_{\lambda_0}\{X \ge x\}, \; P_{\lambda_0}\{X \le x\})$$

**Example 8.7.a.** Daily defective chips: $n = 5, \sum X_i = 154, H_0 : \lambda \le 25 \implies 5\lambda_0 = 125$.

$$p\text{-value} = 1 - \text{ppois}(153, 125) = 0.00666 \implies \text{Reject } H_0 \quad \blacksquare$$

### 8.7.1 Testing the relationship between two Poisson parameters
To test $H_0 : \lambda_2 = c\lambda_1$ vs $H_1 : \lambda_2 \neq c\lambda_1$:

**Proposition 8.7.1.**
$$P\{X_1 = k \mid X_1 + X_2 = n\} = \binom{n}{k} \left(\frac{\lambda_1}{\lambda_1 + \lambda_2}\right)^k \left(\frac{\lambda_2}{\lambda_1 + \lambda_2}\right)^{n-k}$$

Under $H_0$, $X_1 \mid X_1 + X_2 = n \sim \text{Binomial}\left(n, \frac{1}{1+c}\right)$.

**Example 8.7.b.** Accident rates: Plant 1 (8 weeks, 133 accidents), Plant 2 (6 weeks, 149 accidents). $H_0 : \lambda_2 = \frac{3}{4}\lambda_1 \implies p = \frac{4}{7}, n = 282, x_1 = 133 \implies p\text{-value} = 9.408 \times 10^{-4} \implies \text{Reject } H_0$.

---

## Problems

1. Consider a trial in which a jury must decide between the hypothesis that the defendant is guilty and the hypothesis that he or she is innocent.
   a. In the framework of hypothesis testing and the U.S. legal system, which of the hypotheses should be the null hypothesis?
   b. What do you think would be an appropriate significance level in this situation?

2. A colony of laboratory mice consists of several thousand mice. The average weight of all the mice is 32 grams with a standard deviation of 4 grams. A laboratory assistant was asked by a scientist to select 25 mice for an experiment. However, before performing the experiment the scientist decided to weigh the mice as an indicator of whether the assistant’s selection constituted a random sample or whether it was made with some unconscious bias. If the sample mean of the 25 mice was 30.4, would this be significant evidence, at the 5 percent level of significance, against the hypothesis that the selection constituted a random sample?

3. A population distribution is known to have standard deviation 20. Determine the $p$-value of a test of the hypothesis that the population mean is equal to 50, if the average of a sample of 64 observations is (a) 52.5; (b) 55.0; (c) 57.5.

4. In a certain chemical process, it is very important that a particular solution that is to be used as a reactant have a pH of exactly 8.20. A method for determining pH that is available for solutions of this type is known to give measurements that are normally distributed with a mean equal to the actual pH and with a standard deviation of $.02$. Suppose 10 independent measurements yielded the following pH values:
   $$8.18, 8.17, 8.16, 8.15, 8.17, 8.21, 8.22, 8.16, 8.19, 8.18$$
   a. What conclusion can be drawn at the $\alpha = .10$ level of significance?
   b. What about at the $\alpha = .05$ level of significance?

5. The mean breaking strength of a certain type of fiber is required to be at least 200 psi. Past experience indicates that the standard deviation of breaking strength is 5 psi. If a sample of 8 pieces of fiber yielded breakage at the following pressures:
   $$210, 198, 195, 202, 197.4, 196, 199, 195.5$$
   would you conclude, at the 5 percent level of significance, that the fiber is unacceptable? What about at the 10 percent level of significance?

6. It is known that the average height of a man residing in the United States is 5 feet 10 inches and the standard deviation is 3 inches. To test the hypothesis that men in your city are “average,” a sample of 20 men have been chosen. The heights of the men in the sample follow:

| Man | Height in Inches | Man | Height in Inches |
| :--- | :--- | :--- | :--- |
| 1 | 72 | 11 | 70.4 |
| 2 | 68.1 | 12 | 76 |
| 3 | 69.2 | 13 | 72.5 |
| 4 | 72.8 | 14 | 74 |
| 5 | 71.2 | 15 | 71.8 |
| 6 | 72.2 | 16 | 69.6 |
| 7 | 70.8 | 17 | 75.6 |
| 8 | 74 | 18 | 70.6 |
| 9 | 66 | 19 | 76.2 |
| 10 | 70.3 | 20 | 77 |

   What do you conclude? Explain what assumptions you are making.

7. Suppose in Problem 4 that we wished to design a test so that if the pH were really equal to 8.20, then this conclusion will be reached with probability equal to $.95$. On the other hand, if the pH differs from 8.20 by $.03$ (in either direction), we want the probability of picking up such a difference to exceed $.95$.
   a. What test procedure should be used?
   b. What is the required sample size?
   c. If $\bar{x} = 8.31$, what is your conclusion?
   d. If the actual pH is 8.32, what is the probability of concluding that the pH is not 8.20, using the foregoing procedure?

8. Verify that the approximation in Equation (8.3.7) remains valid even when $\mu_1 < \mu_0$.

9. A British pharmaceutical company, Glaxo Holdings, has recently developed a new drug for migraine headaches. Among the claims Glaxo made for its drug, called somatriptan, was that the mean time it takes for it to enter the bloodstream is less than 10 minutes. To convince the Food and Drug Administration of the validity of this claim, Glaxo conducted an experiment on a randomly chosen set of migraine sufferers. To prove its claim, what should they have taken as the null and what as the alternative hypothesis?

10. The weights of salmon grown at a commercial hatchery are normally distributed with a standard deviation of 1.2 pounds. The hatchery claims that the mean weight of this year’s crop is at least 7.6 pounds. Suppose a random sample of 16 fish yielded an average weight of 7.2 pounds. Is this strong enough evidence to reject the hatchery’s claims at the (a) 5 percent level of significance; (b) 1 percent level of significance? (c) What is the $p$-value?

11. Consider a test of $H_0 : \mu \le 100$ versus $H_1 : \mu > 100$. Suppose that a sample of size 20 has a sample mean of $\bar{X} = 105$. Determine the $p$-value of this outcome if the population standard deviation is known to equal (a) 5; (b) 10; (c) 15.

12. An advertisement for a new toothpaste claims that it reduces cavities of children in their cavity-prone years. Cavities per year for this age group are normal with mean 3 and standard deviation 1. A study of 2500 children who used this toothpaste found an average of 2.95 cavities per child. Assume that the standard deviation of the number of cavities of a child using this new toothpaste remains equal to 1.
    a. Are these data strong enough, at the 5 percent level of significance, to establish the claim of the toothpaste advertisement?
    b. Do the data convince you to switch to this new toothpaste?

13. There is some variability in the amount of phenobarbital in each capsule sold by a manufacturer. However, the manufacturer claims that the mean value is 20.0 mg. To test this, a sample of 25 pills yielded a sample mean of 19.7 with a sample standard deviation of 1.3. What inference would you draw from these data? In particular, are the data strong enough evidence to discredit the claim of the manufacturer? Use the 5 percent level of significance.

14. Twenty years ago, entering male high school students of Central High could do an average of 24 pushups in 60 seconds. To see whether this remains true today, a random sample of 36 freshmen was chosen. If their average was 22.5 with a sample standard deviation of 3.1, can we conclude that the mean is no longer equal to 24? Use the 5 percent level of significance.

15. The mean response time of a species of pigs to a stimulus is .8 second. Twenty-eight pigs were given 2 oz of alcohol and then tested. If their average response time was 1.0 second with a standard deviation of .3 second, can we conclude that alcohol affects the mean response time? Use the 5 percent level of significance.

16. Suppose that team A and team B are to play a National Football League game and that team A is favored by $f$ points. Let $S(A)$ and $S(B)$ denote the scores of teams A and B, and let $X = S(A) - S(B) - f$. That is, $X$ is the amount by which team A beats the point spread. It has been claimed that the distribution of $X$ is normal with mean 0 and standard deviation 14. Use data from randomly chosen football games to test this hypothesis.

17. A medical scientist believes that the average basal temperature of (outwardly) healthy individuals has increased over time and is now greater than 98.6 degrees Fahrenheit (37 degrees Celsius). To prove this, she has randomly selected 100 healthy individuals. If their mean temperature is 98.74 with a sample standard deviation of 1.1 degrees, does this prove her claim at the 5 percent level? What about at the 1 percent level?

18. Use the results of a Sunday’s worth of NFL professional football games to test the hypothesis that the average number of points scored by winning teams is less than or equal to 28. Use the 5 percent level of significance.

19. Use the results of a Sunday’s worth of major league baseball scores to test the hypothesis that the average number of runs scored by winning teams is at least 5.6. Use the 5 percent level of significance.

20. A car is advertised as having a gas mileage rating of at least 30 miles/gallon in highway driving. If the miles per gallon obtained in 10 independent experiments are 26, 24, 20, 25, 27, 25, 28, 30, 26, 33, should you believe the advertisement? What assumptions are you making?

21. A producer specifies that the mean lifetime of a certain type of battery is at least 240 hours. A sample of 18 such batteries yielded the following data:
    $$237, 242, 232, 242, 248, 230, 244, 243, 254, 262, 234, 220, 225, 236, 232, 218, 228, 240$$
    Assuming that the life of the batteries is approximately normally distributed, do the data indicate that the specifications are not being met?

22. Use the data of Example 2.3.i of Chapter 2 to test the null hypothesis that the average noise level directly outside of Grand Central Station is less than or equal to 80 decibels.

23. An oil company claims that the sulfur content of its diesel fuel is at most .15 percent. To check this claim, the sulfur contents of 40 randomly chosen samples were determined; the resulting sample mean and sample standard deviation were .162 and .040. Using the 5 percent level of significance, can we conclude that the company’s claims are invalid?

24. A company supplies plastic sheets for industrial use. A new type of plastic has been produced and the company would like to claim that the average stress resistance of this new product is at least 30.0, where stress resistance is measured in pounds per square inch (psi) necessary to crack the sheet. The following random sample was drawn off the production line:
    $$30.1, 32.7, 22.5, 27.5, 27.7, 29.8, 28.9, 31.4, 31.2, 24.3, 26.4, 22.8, 29.1, 33.4, 32.5, 21.7$$
    Assume normality and use the 5 percent level of significance.

25. It is claimed that a certain type of bipolar transistor has a mean value of current gain that is at least 210. A sample of these transistors is tested. If the sample mean value of current gain is 200 with a sample standard deviation of 35, would the claim be rejected at the 5 percent level of significance if
    a. the sample size is 25;
    b. the sample size is 64?

26. A manufacturer of capacitors claims that the breakdown voltage of these capacitors has a mean value of at least 100 V. A test of 12 of these capacitors yielded the following breakdown voltages:
    $$96, 98, 105, 92, 111, 114, 99, 103, 95, 101, 106, 97$$
    Do these results prove the manufacturer’s claim? Do they disprove them?

27. A sample of 10 fish were caught at lake A and their PCB concentrations were measured using a certain technique. The resulting data in parts per million were:
    $$\text{Lake A: } 11.5, 10.8, 11.6, 9.4, 12.4, 11.4, 12.2, 11, 10.6, 10.8$$
    In addition, a sample of 8 fish were caught at lake B and their levels of PCB were measured by a different technique than that used at lake A:
    $$\text{Lake B: } 11.8, 12.6, 12.2, 12.5, 11.7, 12.1, 10.4, 12.6$$
    If it is known that the measuring technique used at lake A has a variance of .09 whereas the one used at lake B has a variance of .16, could you reject (at the 5 percent level of significance) a claim that the two lakes are equally contaminated?

28. A method for measuring the pH level of a solution yields a measurement value that is normally distributed with a mean equal to the actual pH of the solution and with a standard deviation equal to .05. An environmental pollution scientist claims that two different solutions come from the same source. If this were so, then the pH level of the solutions would be equal. To test the plausibility of this claim, 10 independent measurements were made of the pH level for both solutions:

| Measurements of Solution A | Measurements of Solution B |
| :--- | :--- |
| 6.24 | 6.27 |
| 6.31 | 6.25 |
| 6.28 | 6.33 |
| 6.30 | 6.27 |
| 6.25 | 6.24 |
| 6.26 | 6.31 |
| 6.24 | 6.28 |
| 6.29 | 6.29 |
| 6.22 | 6.34 |
| 6.28 | 6.27 |

    a. Do the data disprove the scientist’s claim? Use the 5 percent level of significance.
    b. What is the $p$-value?

29. The following are the values of independent samples from two different populations:
    $$\text{Sample 1: } 122, 114, 130, 165, 144, 133, 139, 142, 150$$
    $$\text{Sample 2: } 108, 125, 122, 140, 132, 120, 137, 128, 138$$
    Let $\mu_1$ and $\mu_2$ be the respective means of the two populations. Find the $p$-value of the test of the null hypothesis $H_0 : \mu_1 \le \mu_2$ versus the alternative $H_1 : \mu_1 > \mu_2$ when the population standard deviations are $\sigma_1 = 10$ and (a) $\sigma_2 = 5$; (b) $\sigma_2 = 10$; (c) $\sigma_2 = 20$.

30. The data below give the lifetimes in hundreds of hours of samples of two types of electronic tubes:
    $$\text{Type 1: } 32, 84, 37, 42, 78, 62, 59, 74$$
    $$\text{Type 2: } 39, 111, 55, 106, 90, 87, 85$$
    Assuming that variance of the logarithms is equal for the two populations, test, at the 5 percent level of significance, the hypothesis that the two population distributions are identical.

31. The viscosity of two different brands of car oil is measured and the following data resulted:
    $$\text{Brand 1: } 10.62, 10.58, 10.33, 10.72, 10.44, 10.74$$
    $$\text{Brand 2: } 10.50, 10.52, 10.58, 10.62, 10.55, 10.51, 10.53$$
    Test the hypothesis that the mean viscosity of the two brands is equal, assuming that the populations have normal distributions with equal variances.

32. It is argued that the resistance of wire A is greater than the resistance of wire B:

| Wire A | Wire B |
| :--- | :--- |
| .140 ohm | .135 ohm |
| .138 | .140 |
| .143 | .136 |
| .142 | .142 |
| .144 | .138 |
| .137 | .140 |

    What conclusion can you draw at the 10 percent significance level? Explain what assumptions you are making.

*(In Problems 33 through 40, assume that the population distributions are normal and have equal variances.)*

33. Twenty-five men between the ages of 25 and 30 (11 smokers and 14 nonsmokers) had systolic blood pressure:
    - Smokers: 124, 134, 136, 125, 133, 127, 135, 131, 133, 125, 118
    - Nonsmokers: 130, 122, 128, 129, 118, 122, 116, 127, 135, 120, 122, 120, 115, 123
    Test the hypothesis that the mean blood pressures of smokers and nonsmokers are the same.

34. Albino rats and carbon tetrachloride:
    - Dose .032 cc: 421, 462, 400, 378, 413
    - Dose .063 cc: 207, 17, 412, 74, 116
    Do the data prove that the larger dosage is more effective than the smaller?

35. Starting salaries: 16 industrial engineers ($\bar{X} = \$72,700, S = \$2400$) and 16 civil engineers ($\bar{Y} = \$71,400, S = \$2200$). Has the professor’s claim that IE > CE been verified? Find $p$-value.

36. Gasoline from crude oil:
    - Method A: 23.2, 26.6, 24.4, 23.5, 22.6, 25.7, 25.5
    - Method B: 25.7, 27.7, 26.2, 27.9, 25.0, 21.4, 26.1
    If 1% significance level is used, what is your recommendation?

37. Percentage of calories from fat:
    - July: 32.2, 27.4, 28.6, 32.4, 40.5, 26.2, 29.4, 25.8, 36.6, 30.3, 28.5, 32.0
    - January: 30.5, 28.4, 40.2, 37.6, 36.5, 38.8, 34.7, 29.5, 29.7, 37.2, 41.5, 37.0
    Test if mean fat percentage intake is the same for both months at (a) 5% and (b) 1% significance.

38. Bat feeding flights: Female ($n = 12, \bar{X} = 180, S_x = 92$), Male ($m = 10, \bar{Y} = 136, S_y = 86$). Test equal means at 5% level.

39. Lead content of hair (micrograms):
    - 1880–1920: $n = 30, \bar{X} = 48.5, S = 14.5$
    - Today: $m = 100, \bar{Y} = 26.6, S = 12.3$
    (a) Test if lead content is less today at 1% level. (b) Find $p$-value.

40. Newborn weights in two counties: $n = 53, m = 44, \bar{X} = 6.8, \bar{Y} = 7.2, S_1^2 = 5.2, S_2^2 = 4.9$. Test equal means.

41. Blood lead levels in children: $\bar{x}_1 = .015, s_1 = .004, \bar{x}_2 = .006, s_2 = .006$ ($n = m = 33$). Find $p$-value.

42. Pitocin labor induction blood pressures before and after:

| Patient | Before | After | Patient | Before | After |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 134 | 140 | 6 | 140 | 138 |
| 2 | 122 | 130 | 7 | 118 | 124 |
| 3 | 132 | 135 | 8 | 127 | 126 |
| 4 | 130 | 126 | 9 | 125 | 132 |
| 5 | 128 | 134 | 10 | 142 | 144 |

    Do data indicate that injection changes blood pressure?

43. Jogging and pulse rate (8 subjects before and after):
    - Before: 74, 86, 98, 102, 78, 84, 79, 70
    - After: 70, 85, 90, 110, 71, 80, 69, 74

44. Devise a significance level $\alpha$ test of $H_0 : \sigma^2 \le \sigma_0^2$ versus $H_1 : \sigma^2 > \sigma_0^2$.

45. How is Problem 44 modified if $\mu$ is known?

46. Needleless vaccine injector: $n = 50, S = .08$. Test if $\sigma > .10$ at $\alpha = .10$.

47. Drug weight standard deviation: test if $\sigma < .4$ mg with data:
    $$5.728, 5.731, 5.722, 5.719, 5.727, 5.724, 5.718, 5.726, 5.723, 5.722$$

48. PCB monitoring methods: 8 measurements each:
    - Method 1: 6.2, 5.8, 5.7, 6.3, 5.9, 6.1, 6.2, 5.7
    - Method 2: 6.3, 5.7, 5.9, 6.4, 5.8, 6.2, 6.3, 5.5
    Test equal variance at $\alpha = .10$.

49. Test equal variance for Problem 31 data.

50. Develop a test of $H_0 : \sigma_x^2 < \sigma_y^2$ vs $H_1 : \sigma_x^2 > \sigma_y^2$ with sample stats given.

51. Waxed paper bags variance comparison ($n = 75$ each).

52. Aspirin vs placebo: 104 heart attacks in aspirin group (11,000 men) vs 189 in placebo group (11,000 men). Test equal probability.

53. Strokes in Aspirin study: 119 aspirin vs 98 placebo.

54. Infection cure rate: standard 72%, new drug 42/50. Find $p$-value.

55. Traffic initiative polls: (a) 56/100, (b) 68/120, (c) 62/110, (d) combined 186/330.

56. California African American twin birth rate (null 1.32%): (a) min twin births in 1000 to reject at 5%, (b) power if true rate is 1.80%.

57. Ambulance service: 70 of 200 life-threatening. Test $H_0 : p \ge .45$ at 5% and 1%.

58. Drug cure rate: standard 75%, new drug 42/50. Test equal effectiveness.

59. Repeat 58 with normal approximation.

60. Myeloma survival: Treatment 1 (39/72 survived), Treatment 2 (44/84 survived).

61. One-sided Fisher-Irwin test.

62. Recursive formula for hypergeometric distribution.

63. Large sample two-proportion z-test formula.

64. Apply Problem 63 test to Problem 60 data.

65. Framing effect on prostate cancer surgery decision (24/100 survival-framed vs 12/100 mortality-framed).

66. Larry Bird free throws (338 pairs: 251 made both, 34 made 1st only, 48 made 2nd only, 5 missed both).

67. VA Coronary bypass surgery (252/286) vs medical therapy (270/310).

68. Earthquakes in 8 years: 46, 62, 60, 58, 47, 50, 59, 49. Test $H_0 : \lambda = 52$ at 5%.

69. Top quark discovery: 27 events observed with baseline Poisson mean 6.7.

70. Poisson comparison: Sample 1 (24, 32, 29, 33, 40, 28, 34, 36), Sample 2 (42, 36, 41).

71. Confounding variable in observational study on smoking and heart disease.

72. Survivorship bias in stock analysis.
