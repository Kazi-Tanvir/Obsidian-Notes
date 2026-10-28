# Special Random Variables
**Mahbub Latif, PhD**  
July 2026

---

## 2. Plan
* **Discrete probability distributions**
  * The binomial distribution
  * The Poisson distribution
  * Hypergeometric distribution
* **Continuous probability distributions**
  * Normal distribution
  * Exponential distribution

---

## 3. The Binomial Random Variable

---

## 4. The Bernoulli Random Variable
* A trial that has only two outcomes (e.g., success or failure) is known as a **Bernoulli trial**
* Define a random variable $X$ as:
  $$X = \begin{cases} 1 & \text{if the outcome is a success} \\ 0 & \text{if the outcome is a failure.} \end{cases}$$
* $X$ follows a Bernoulli distribution with parameter $p$, where:
  $$p = \text{Pr}(\text{success}) = P(X = 1)$$

---

## 5. The Bernoulli Random Variable
* The random variable $X$ has the following probabilities corresponding to its values:
  $$P(X = 1) = p$$
  $$P(X = 0) = 1 - p$$
* The probability mass function of $X$:
  $$P(X = x) = p^x (1 - p)^{1-x}, \quad x = 0, 1; \quad 0 \le p \le 1$$
* $$E(X) = p \quad \text{and} \quad \mathrm{Var}(X) = p(1 - p)$$

---

## 6. The Binomial Random Variable
* Binomial random variable deals with the distribution of the number of successes in $n\ (\ge 1)$ independent Bernoulli trials
* The probability of success remains constant from trial to trial
* Let $X_1, \dots, X_n$ be independent and each follow a Bernoulli distribution with parameter $p$, and define:
  $$X = X_1 + \dots + X_n$$
* $X$ represents the number of successes in $n$ Bernoulli trials and follows a binomial distribution with parameters $n$ and $p$, i.e.:
  $$X \sim B(n, p)$$

---

## 7. The Binomial Random Variable
* The probability mass function of $X$:
  $$P(X = x) = \binom{n}{x} p^x (1 - p)^{n-x}, \quad x = 0, 1, \dots, n$$
* $\binom{n}{x} \to$ number of ways $x$ successes can be obtained in $n$ Bernoulli trials

---

## 8. Example 5.1a
* It is known that disks produced by a certain company will be defective with probability .01 independently of each other.
* The company sells the disks in packages of 10 and offers a money-back guarantee that at most 1 of the 10 disks is defective.
* What proportion of packages is returned?
* If someone buys three packages, what is the probability that exactly one of them will be returned?

---

## 9. Binomial Distribution Plots
*(Plots: Probability mass distributions for $B(10, 0.2)$, $B(10, 0.5)$, and $B(10, 0.8)$ across $k = 0, 1, \dots, 10$)*

---

## 10. Expectation of Binomial Distribution
$$E(X) = \sum_{x=0}^n x \binom{n}{x} p^x (1 - p)^{n-x}$$
$$= \sum_{x=1}^n x \frac{n!}{x!(n - x)!} p^x (1 - p)^{n-x}$$
$$= \sum_{x=1}^n \frac{n!}{(x - 1)!(n - x)!} p^x (1 - p)^{n-x}$$
$$= np \sum_{x=1}^n \frac{(n - 1)!}{(x - 1)!(n - x)!} p^{x-1} (1 - p)^{n-x}$$
$$= np$$

---

## 11. Variance of Binomial Distribution
$$E[X(X - 1)] = \sum_{x=0}^n x(x - 1)\binom{n}{x} p^x (1 - p)^{n-x}$$
$$= \sum_{x=2}^n x(x - 1)\binom{n}{x} p^x (1 - p)^{n-x}$$
$$= n(n - 1)p^2$$

$$\mathrm{Var}(X) = E(X^2) - [E(X)]^2$$
$$= E[X(X - 1)] + E(X) - [E(X)]^2$$
$$= n(n - 1)p^2 + np - n^2 p^2$$
$$= np(1 - p)$$

---

## 12. Binomial Cumulative Distribution Function
* The cumulative distribution function of $X \sim B(n, p)$:
  $$P(X \le a) = \sum_{x=0}^a \binom{n}{x} p^x (1 - p)^{n-x}$$
* The following relationship is helpful to calculate cumulative distribution of binomial distribution:
  $$P(X = x + 1) = \frac{p}{1 - p} \frac{n - x}{x + 1} P(X = x)$$

---

## 13. Problems
1, 3, 5, 6, 7, 9

---

## 14. The Poisson Random Variable

---

## 15. The Poisson Random Variable
* A random variable $X$ is said to be a Poisson random variable with parameter $\lambda > 0$, if its probability mass function is given by:
  $$P(X = x) = \frac{e^{-\lambda}\lambda^x}{x!}, \quad x = 0, 1, 2, \dots$$
* Using the relationship $e^\lambda = \sum_{x=0}^\infty \frac{\lambda^x}{x!}$, it can be shown that $\sum_{x=0}^\infty P(X = x) = 1$ for a Poisson distribution
* For $X \sim \text{Po}(\lambda)$:
  $$E(X) = \mathrm{Var}(X) = \lambda$$

---

## 16. Poisson Distribution Plots
*(Plots: Probability mass distributions for $\text{Po}(10)$, $\text{Po}(2)$, and $\text{Po}(5)$ across $k$)*

---

## 17. Examples of Poisson Random Variables
* The number of misprints on a page of a book
* The number of people in a community living to 100 years of age
* The number of wrong telephone numbers that are dialed in a day
* The number of transistors that fail on their first day of use
* The number of customers entering a post office on a given day

---

## 18. Expectation and Variance of a Poisson Random Variable
$$E(X) = \sum_{x=0}^\infty x \frac{e^{-\lambda}\lambda^x}{x!} = \sum_{x=1}^\infty x \frac{e^{-\lambda}\lambda^x}{x!} = \sum_{x=1}^\infty \frac{e^{-\lambda}\lambda^x}{(x - 1)!} = \lambda$$

* Similarly:
  $$E[X(X - 1)] = \sum_{x=0}^\infty x(x - 1) \frac{e^{-\lambda}\lambda^x}{x!} = \lambda^2$$
  $$\mathrm{Var}(X) = E[X(X - 1)] + E(X) - [E(X)]^2 = \lambda$$

---

## 19. Poisson Approximation of Binomial Distribution
* Suppose $X \sim B(n, p)$, for a large $n$ and small $p$:
  $$P(X = x) = \binom{n}{x} p^x (1 - p)^{n-x} \simeq \frac{e^{-\lambda}\lambda^x}{x!}, \quad \text{where } \lambda = np$$
* **Examples:**
  * $X \sim B(70, .1)$
  * $$P(X = 5) = \begin{cases} 0.1284 & \text{for binomial} \\ 0.1277 & \text{for Poisson} \end{cases}$$

---

## 20. Examples: Poisson Distribution
* **Example 5.2a:**
  * Suppose that the average number of accidents occurring weekly on a particular stretch of a highway equals 3.
  * Calculate the probability that there is at least one accident this week.
* **Example 5.2b:**
  * Suppose the probability that an item produced by a certain machine will be defective is .1.
  * Find the probability that a sample of 10 items will contain at most one defective item.
  * Assume that the quality of successive items is independent.

---

## 21. Example 5.2d
* If the average number of claims handled daily by an insurance company is 5, what proportion of days have less than 3 claims?
* What is the probability that there will be 4 claims in exactly 3 of the next 5 days?
* Assume that the number of claims on different days is independent.

---

## 22. Distribution of Sum of Two Independent Poisson Random Variables
* If $X_1 \sim \text{Po}(\lambda_1)$ and $X_2 \sim \text{Po}(\lambda_2)$, then:
  $$Y = X_1 + X_2 \sim \text{Po}(\lambda_1 + \lambda_2)$$
* Moment generating function of $X_1$:
  $$M_{X_1}(t) = E[e^{tX_1}] = \exp[\lambda_1(e^t - 1)]$$
* Moment generating function of $Y = X_1 + X_2$:
  $$M_Y(t) = M_{X_1}(t)M_{X_2}(t) = \exp[(\lambda_1 + \lambda_2)(e^t - 1)]$$

---

## 23. Example 5.2f & Problems
* **Example 5.2f:**
  * It has been established that the number of defective stereos produced daily at a certain plant is Poisson distributed with mean 4.
  * Over a 2-day span, what is the probability that the number of defective stereos does not exceed 3?
* **Problems:**
  * 13, 14, 18

---

## 24. Hypergeometric Distribution

---

## 25. Hypergeometric Distribution
* A bin contains $N + M$ batteries, of which $N$ are of acceptable quality and $M$ are defective
* A sample of size $n$ is randomly chosen (without replacement) and all possible sampled subsets are equally likely
* $X$ denotes the number of acceptable batteries in the sample of size $n$ and its probability mass function:
  $$P(X = x) = \frac{\binom{N}{x}\binom{M}{n - x}}{\binom{N + M}{n}}, \quad x = 0, 1, \dots, \min(n, N)$$
* $X$ follows a hypergeometric distribution with parameters $N$, $M$, and $n$

---

## 26. Example 5.3a
* The components of a 6-component system are to be randomly chosen from a bin of 20 used components.
* The resulting system will be functional if at least 4 of its 6 components are in working condition.
* If 15 of the 20 components in the bin are in working condition, what is the probability that the resulting system will be functional?
* $X$, the number of components with working condition out of six selected components, follows a hypergeometric distribution with parameters $N = 15, M = 5, n = 6$.

---

## 27. Hypergeometric Distribution: Mean and Variance
* The mean and variance of a hypergeometric distribution with parameters $N$, $M$, and $n$:
  $$E(X) = \frac{nN}{N + M} \quad \text{and} \quad \mathrm{Var}(X) = \frac{nNM}{(N + M)^2}\left[1 - \frac{n - 1}{N + M - 1}\right]$$

---

## 28. Hypergeometric Distribution (Derivation Part 1)
* Suppose $X = X_1 + \dots + X_n$, where $X_i = 1$ or $X_i = 0$ depending on whether the $i^{\text{th}}$ unit is selected or not
* $$E\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n E(X_i) = \frac{nN}{N + M}$$
* $$\mathrm{Var}(X) = \mathrm{Var}\left[\sum_i X_i\right] = \sum_i \mathrm{Var}(X_i) + \sum_{i \ne j} \mathrm{Cov}(X_i, X_j) = \frac{nN}{N + M} \times \frac{M}{N + M} + \sum_{i \ne j} \mathrm{Cov}(X_i, X_j)$$

---

## 29. Hypergeometric Distribution (Derivation Part 2)
$$\mathrm{Cov}(X_i, X_j) = E(X_i X_j) - E(X_i)E(X_j)$$
$$= P(X_i X_j = 1) - E(X_i)E(X_j)$$
$$= P(X_j = 1)P(X_i = 1 \mid X_j = 1) - P(X_i = 1)P(X_j = 1)$$
$$= \frac{N(N - 1)}{(N + M)(N + M - 1)} - \left[\frac{N}{N + M}\right]^2 = \frac{-NM}{(N + M)^2(N + M - 1)}$$

---

## 30. Hypergeometric Distribution (Derivation Part 3)
$$\mathrm{Var}(X) = \frac{nNM}{(N + M)^2} + \sum_{i \ne j} \mathrm{Cov}(X_i, X_j)$$
$$= \frac{nNM}{(N + M)^2} + \sum_{i \ne j} \left( \frac{-NM}{(N + M)^2(N + M - 1)} \right)$$
$$= \frac{nNM}{(N + M)^2} - \frac{n(n - 1)NM}{(N + M)^2(N + M - 1)}$$
$$= \frac{nNM}{(N + M)^2} \left[ 1 - \frac{n - 1}{N + M - 1} \right] = np(1 - p)\left[ 1 - \frac{n - 1}{N + M - 1} \right]$$

---

## 31. Hypergeometric Distribution
$$np(1 - p)\left[1 - \frac{n - 1}{N + M - 1}\right] \to np(1 - p) \quad \text{when } (N + M) \to \infty$$

---

## 32. Hypergeometric Distribution
* Let $X \sim B(n, p)$ and $Y \sim B(m, p)$, then:
  $$P(X = i \mid X + Y = k) = \frac{\binom{n}{i}\binom{m}{k - i}}{\binom{n + m}{k}}$$

---

## 33. The Uniform Random Variable

---

## 34. The Uniform Random Variable
* A random variable $X$ is said to be uniformly distributed over the interval $[\alpha, \beta]$ if its pdf is given by:
  $$f(x) = \begin{cases} \frac{1}{\beta - \alpha} & \text{if } \alpha \le x \le \beta \\ 0 & \text{otherwise} \end{cases}$$
* Show that:
  $$E(X) = \frac{\alpha + \beta}{2} \quad \text{and} \quad \mathrm{Var}(X) = \frac{(\beta - \alpha)^2}{12}$$

---

## 35. The Normal Random Variable

---

## 36. The Normal Random Variable
* A random variable $X$ is said to be normally distributed random variable with parameters $\mu$ and $\sigma^2$, i.e. $X \sim N(\mu, \sigma^2)$, if its density is:
  $$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty$$
* The normal density function is bell-shaped and symmetric about its mean $\mu$
* The maximum value of the density function is $(\sigma\sqrt{2\pi})^{-1} \simeq 0.399/\sigma$, attained at $x = \mu$

---

## 37. Parameters of Normal Distribution and Its Density Function

---

## 38. Normal Distribution Parameter Plots
*(Plots: Comparison of locations $N(5, 4)$ vs. $N(10, 4)$ and scales $N(5, 4)$ vs. $N(5, 1.25)$)*

---

## 39. The Normal Random Variable: Mean and Variance
* **The expected value:**
  $$E(X - \mu) = \int_{-\infty}^\infty (x - \mu) \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}\,dx = 0 \implies E(X) = \mu$$
* **The variance:**
  $$\mathrm{Var}(X) = E(X - \mu)^2 = \int_{-\infty}^\infty (x - \mu)^2 \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}\,dx = \sigma^2$$

---

## 40. Distribution of a Linear Combination of a Normal Distribution
* If $X \sim N(\mu, \sigma^2)$, what is the distribution of $Y = a + bX$, where $a$ and $b$ are constants?
* If $M_X(t)$ is the moment generating function (mgf) of $X$, the mgf of $Y = a + bX$:
  $$M_Y(t) = \int e^{ty}f(x)\,dx = \int e^{t(a + bx)}f(x)\,dx = e^{ta}M_X(tb)$$

---

## 41. Distribution of a Linear Combination of a Normal Distribution (Continued)
* The mgf of $X \sim N(\mu, \sigma^2)$:
  $$M_X(t) = e^{t\mu + (t^2\sigma^2/2)}$$
* The mgf of $Y = a + bX$:
  $$M_Y(t) = e^{ta}M_X(tb) = e^{ta}e^{t\mu b + (t^2 b^2\sigma^2/2)} = e^{t(b\mu + a) + (t^2 b^2\sigma^2/2)}$$
* So,
  $$Y \sim N(a + b\mu, \sigma^2 b^2)$$

---

## 42. Standard Normal Distribution
* A normal distribution with mean 0 and variance 1 is known as the **standard normal distribution**, which is denoted by $Z \sim N(0, 1)$
* The mgf of standard normal distribution:
  $$M_Z(t) = e^{t^2/2}$$
* The probability density function of a standard normal distribution:
  $$\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}, \quad -\infty < x < \infty$$

---

## 43. Standard Normal Distribution
* If $X \sim N(\mu, \sigma^2)$ then:
  $$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$
* Prove this relationship!
* It can be shown that:
  $$E(Z) = E\left[\frac{X - \mu}{\sigma}\right] = 0 \quad \text{and} \quad \mathrm{Var}(Z) = \mathrm{Var}\left[\frac{X - \mu}{\sigma}\right] = 1$$

---

## 44. Cumulative Distribution of the Standard Normal Distribution
* The cdf of the standard normal distribution:
  $$\Phi(x) = P(Z < x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-y^2/2}\,dy$$
* This integration cannot be evaluated algebraically
* Most mathematical statistics books have tables providing $\Phi(x)$ values for different $x$ (see page 642 of the textbook for the table)
* An important relationship:
  $$\Phi(x) + \Phi(-x) = 1$$

---

## 45. Probability Calculation Related to $Z \sim N(0, 1)$
$$P(Z < 1.12) = \Phi(1.12) = 0.8686$$
$$P(Z > .73) = 1 - P(Z \le .73) = 1 - \Phi(.73) = 1 - 0.7673 = 0.2327$$

---

## 46. Standard Normal Probability Plots
*(Plots: Density curves showing shaded areas for $P(Z < 1.12)$ and $P(Z > 0.73)$)*

---

## 47. Probability Calculation Related to $Z \sim N(0, 1)$
$$P(Z < -1.22) = \Phi(-1.22) = 1 - \Phi(1.22) = 1 - 0.8686 = 0.1112$$
$$P(Z > -1.13) = 1 - P(Z \le -1.13) = 1 - \Phi(-1.13) = \Phi(1.13) = 0.8708$$

---

## 48. Standard Normal Probability Plots
*(Plots: Density curves showing shaded areas for $P(Z < -1.22)$ and $P(Z > -1.13)$)*

---

## 49. Probability Calculation Related to $Z \sim N(0, 1)$
$$P(1.1 < Z < 2.2) = \Phi(2.2) - \Phi(1.1) = 0.9861 - 0.8643 = 0.1218$$
$$P(-1.31 < Z < 1.92) = \Phi(1.92) - \Phi(-1.31) = \Phi(1.92) - 1 + \Phi(1.31) = 0.9726 - 1 + 0.9049 = 0.8775$$

---

## 50. Standard Normal Probability Plots
*(Plots: Density curves showing shaded areas for $P(1.1 < Z < 2.2)$ and $P(-1.31 < Z < 1.92)$)*

---

## 51. Probability Calculation Related to $X \sim N(\mu, \sigma^2)$
* For any $a < b$:
  $$P(a < X < b) = P\left(\frac{a - \mu}{\sigma} < \frac{X - \mu}{\sigma} < \frac{b - \mu}{\sigma}\right) = P\left(\frac{a - \mu}{\sigma} < Z < \frac{b - \mu}{\sigma}\right) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$$

---

## 52. Probability Calculation Related to $X \sim N(\mu, \sigma^2)$
* For $X \sim N(3, 16)$:
  $$P(X < 11) = \Phi\left(\frac{11 - 3}{4}\right) = \Phi(2) = 0.9772$$
* Calculate $P(X > -1)$ and $P(2 < X < 7)$

---

## 53. General Normal Probability Plots
*(Plots: Density curves showing shaded areas for $X < 11$ in $N(3, 16)$ and corresponding standard normal $Z < 2$)*

---

## 54. Sum of Several Independent Normal Variables
* Let $X_1, \dots, X_n$ be $n$ independent normal random variables, where $X_i \sim N(\mu_i, \sigma_i^2)$
* The distribution of $Y = \sum_{i=1}^n X_i$ follows a normal distribution with:
  $$\text{mean} = \sum_{i=1}^n \mu_i \quad \text{and} \quad \text{variance} = \sum_{i=1}^n \sigma_i^2$$

---

## 55. Example 5.5d
* Data from National Oceanic and Atmospheric Administration indicate that the yearly precipitation in Los Angeles is a normal random variable with a mean of 12.08 inches and standard deviation of 3.1 inches.
* Find the probability that total precipitation during the next two years will exceed 25 inches.

---

## 56. Quantiles/Percentiles of Standard Normal Distribution
* $z_\alpha \to 100(1 - \alpha)^{\text{th}}$ percentile of standard normal distribution:
  $$P(Z < z_\alpha) = 1 - \alpha$$
* From the table, we can find:
  * $z_{.05} = 1.645$
  * $z_{.025} = 1.96$
  * $z_{.01} = 2.33$

---

## 57. Quantiles Visualization
*(Plot: Standard normal curve showing area $1 - \alpha$ to the left of $z_\alpha$ and upper tail area $\alpha$)*

---

## 58. Quantiles/Percentiles of a General Normal Distribution
* The $p^{\text{th}}$ quantile of $X \sim N(\mu, \sigma^2)$:
  $$P(X \le x_p) = p \implies \Phi\left(\frac{x_p - \mu}{\sigma}\right) = p \implies x_p = \mu + \sigma\Phi^{-1}(p)$$
* It can be shown that for $p \ge 0.50$:
  $$\Phi^{-1}(p) = z_{1-p}$$

---

## 59. Quantiles/Percentiles of a General Normal Distribution
* The quartiles of $X \sim N(\mu, \sigma^2)$:
  $$Q_1 = \mu + \sigma\Phi^{-1}(.25)$$
  $$Q_2 = \mu + \sigma\Phi^{-1}(.50)$$
  $$Q_3 = \mu + \sigma\Phi^{-1}(.75)$$
* The inter-quartile range (IQR) is a measure of spread:
  $$\text{IQR} = Q_3 - Q_1$$

---

## 60. Exponential Random Variables

---

## 61. Exponential Random Variables
* An exponential random variable with parameter $\lambda > 0$ has the following probability density function:
  $$f(x) = \lambda e^{-\lambda x}, \quad x \ge 0$$
* The moment generating function of an exponential random variable:
  $$M_X(t) = \frac{\lambda}{\lambda - t}$$
* Show that:
  $$E(X) = \frac{1}{\lambda} \quad \text{and} \quad \mathrm{Var}(X) = \frac{1}{\lambda^2}$$

---

## 62. Exponential Distribution Properties & Plots
*(Plots: Exponential density curves for rates $\lambda = 1, 2, 3$)*

* **The cumulative distribution function:**
  $$F(x) = \int_0^x \lambda e^{-\lambda y}\,dy = 1 - e^{-\lambda x}$$
  $$P(a < X < b) = F(b) - F(a) = e^{-\lambda a} - e^{-\lambda b}$$
* **Memoryless property of exponential random variable:**
  * If $X$ follows an exponential distribution with parameter $\lambda$:
    $$P(X > s + t \mid X > t) = P(X > s)$$

---

## 63. Distribution Arising from the Normal: The Chi-Square Distribution
* Let $Z_1, \dots, Z_n$ be independent and identically distributed as $N(0, 1)$, then $\sum_{i=1}^n Z_i^2$ follows a chi-square distribution with $n$ degrees of freedom, i.e.:
  $$\sum_{i=1}^n Z_i^2 \sim \chi^2_n$$

---

## 64. Distribution Arising from the Normal: The t-Distribution
* Let $Z \sim N(0, 1)$ and $X \sim \chi^2_n$ be independent, then $\frac{Z}{\sqrt{X/n}}$ follows a $t$-distribution with $n$ degrees of freedom, i.e.:
  $$\frac{Z}{\sqrt{X/n}} \sim t_n$$

---

## 65. Distribution Arising from the Normal: The F-Distribution
* Let $X \sim \chi^2_n$ and $Y \sim \chi^2_m$ be independent, then $\frac{X/n}{Y/m}$ follows an $F$-distribution with $n$ and $m$ degrees of freedom, i.e.:
  $$\frac{X/n}{Y/m} \sim F_{n, m}$$

---

## 66. Problems
1, 3, 5, 6, 7, 8, 10, 11, 13, 14, 23, 24, 25, 26, 33, 34, 35, 36, 37, 38

---