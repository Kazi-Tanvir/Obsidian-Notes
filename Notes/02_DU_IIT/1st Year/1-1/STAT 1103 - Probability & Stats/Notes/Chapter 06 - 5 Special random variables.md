# Chapter 5: Special random variables

Certain types of random variables occur over and over again in applications. In this chapter, we will study a variety of them.

## 5.1 The Bernoulli and binomial random variables

Suppose that a trial, or an experiment, whose outcome can be classified as either a “success” or as a “failure” is performed. If we let $X = 1$ when the outcome is a success and $X = 0$ when it is a failure, then the probability mass function of $X$ is given by

$$\begin{aligned}
P\{X = 0\} &= 1 - p \tag{5.1.1} \\
P\{X = 1\} &= p
\end{aligned}$$

where $p, 0 \le p \le 1$, is the probability that the trial is a “success.”

A random variable $X$ is said to be a *Bernoulli random variable* (after the Swiss mathematician James Bernoulli) if its probability mass function is given by Equations (5.1.1) for some $p \in (0, 1)$. Its expected value is

$$E[X] = 1 \cdot P\{X = 1\} + 0 \cdot P\{X = 0\} = p$$

That is, the expectation of a Bernoulli random variable is the probability that the random variable equals 1.

Suppose now that $n$ independent trials, each of which results in a “success” with probability $p$ and in a “failure” with probability $1 - p$, are to be performed. If $X$ represents the number of successes that occur in the $n$ trials, then $X$ is said to be a *binomial random variable* with parameters $(n, p)$.

The probability mass function of a binomial random variable with parameters $n$ and $p$ is given by

$$P\{X = i\} = \binom{n}{i} p^i (1 - p)^{n-i}, \quad i = 0, 1, \dots, n \tag{5.1.2}$$

where $\binom{n}{i} = n!/[i!(n - i)!]$ is the number of different groups of $i$ objects that can be chosen from a set of $n$ objects. The validity of Equation (5.1.2) may be verified by first noting that the probability of any particular sequence of the $n$ outcomes containing $i$ successes and $n - i$ failures is, by the assumed independence of trials, $p^i(1 - p)^{n-i}$. Equation (5.1.2) then follows since there are $\binom{n}{i}$ different sequences of the $n$ outcomes leading to $i$ successes and $n - i$ failures — which can perhaps most easily be seen by noting that there are $\binom{n}{i}$ different selections of the $i$ trials that result in successes. For instance, if $n = 5, i = 2$, then there are $\binom{5}{2}$ choices of the two trials that are to result in successes — namely, any of the outcomes:

$$\begin{matrix}
(s, s, f, f, f) & (f, s, s, f, f) & (f, f, s, f, s) \\
(s, f, s, f, f) & (f, s, f, s, f) & (f, f, f, s, s) \\
(s, f, f, s, f) & (f, s, f, f, s) & (f, f, s, s, f) \\
(s, f, f, f, s) & &
\end{matrix}$$

where the outcome $(f, s, f, s, f)$ means, for instance, that the two successes appeared on trials 2 and 4. Since each of the $\binom{5}{2}$ outcomes has probability $p^2(1-p)^3$, we see that the probability of a total of 2 successes in 5 independent trials is $\binom{5}{2} p^2(1 - p)^3$. As a check, note that, by the binomial theorem, the probabilities sum to 1; that is,

$$\sum_{i=0}^n p(i) = \sum_{i=0}^n \binom{n}{i} p^i(1 - p)^{n-i} = [p + (1 - p)]^n = 1$$

The probability mass function of three binomial random variables with respective parameters $(10, .5)$, $(10, .3)$, and $(10, .6)$ are presented in Figure 5.1. The first of these is symmetric about the value $.5$, whereas the second is somewhat weighted, or skewed, to lower values and the third to higher values.

**Example 5.1.a.** It is known that disks produced by a certain company will be defective with probability $.01$ independently of each other. The company sells the disks in packages of 10 and offers a money-back guarantee that at most 1 of the 10 disks is defective. What proportion of packages is returned? If someone buys three packages, what is the probability that exactly one of them will be returned?

**Solution.** If $X$ is the number of defective disks in a package, then assuming that customers always take advantage of the guarantee, it follows that $X$ is a binomial random variable with parameters $(10, .01)$. Hence the probability that a package will have to be replaced is

$$\begin{aligned}
P\{X > 1\} &= 1 - P\{X = 0\} - P\{X = 1\} \\
&= 1 - \binom{10}{0}(.01)^0(.99)^{10} - \binom{10}{1}(.01)^1(.99)^9 \approx .005
\end{aligned}$$

Because each package will, independently, have to be replaced with probability $.005$, it follows from the law of large numbers that in the long run $.5$ percent of the packages will have to be replaced.

It follows from the foregoing that the number of packages that will be returned by a buyer of three packages is a binomial random variable with parameters $n = 3$ and $p = .005$. Therefore, the probability that exactly one of the three packages will be returned is $\binom{3}{1}(.005)(.995)^2 = .015$. $\blacksquare$

**Example 5.1.b.** The color of one’s eyes is determined by a single pair of genes, with the gene for brown eyes being dominant over the one for blue eyes. This means that an individual having two blue-eyed genes will have blue eyes, while one having either two brown-eyed genes or one brown-eyed and one blue-eyed gene will have brown eyes. When two people mate, the resulting offspring receives one randomly chosen gene from each of its parents’ gene pair. If the eldest child of a pair of brown-eyed parents has blue eyes, what is the probability that exactly two of the four other children (none of whom is a twin) of this couple also have blue eyes?

**Solution.** To begin, note that since the eldest child has blue eyes, it follows that both parents must have one blue-eyed and one brown-eyed gene. (For if either had two brown-eyed genes, then each child would receive at least one brown-eyed gene and would thus have brown eyes.) The probability that an offspring of this couple will have blue eyes is equal to the probability that it receives the blue-eyed gene from both parents, which is $\left(\frac{1}{2}\right)\left(\frac{1}{2}\right) = \frac{1}{4}$. Hence, because each of the other four children will have blue eyes with probability $\frac{1}{4}$, it follows that the probability that exactly two of them have this eye color is

$$\binom{4}{2}(1/4)^2(3/4)^2 = 27/128 \quad \blacksquare$$

**Example 5.1.c.** A communications system consists of $n$ components, each of which will, independently, function with probability $p$. The total system will be able to operate effectively if at least one-half of its components function.
(a) For what values of $p$ is a 5-component system more likely to operate effectively than a 3-component system?
(b) In general, when is a $2k + 1$ component system better than a $2k - 1$ component system?

**Solution.** (a) Because the number of functioning components is a binomial random variable with parameters $(n, p)$, it follows that the probability that a 5-component system will be effective is

$$\binom{5}{3}p^3(1 - p)^2 + \binom{5}{4}p^4(1 - p) + p^5$$

whereas the corresponding probability for a 3-component system is

$$\binom{3}{2}p^2(1 - p) + p^3$$

Hence, the 5-component system is better if

$$10p^3(1 - p)^2 + 5p^4(1 - p) + p^5 \ge 3p^2(1 - p) + p^3$$

which reduces to

$$3(p - 1)^2(2p - 1) \ge 0 \implies p \ge \frac{1}{2}$$

(b) In general, a system with $2k + 1$ components will be better than one with $2k - 1$ components if (and only if) $p \ge \frac{1}{2}$. To prove this, consider a system of $2k + 1$ components and let $X$ denote the number of the first $2k - 1$ that function. Then

$$P_{2k+1}(\text{effective}) = P\{X \ge k + 1\} + P\{X = k\}(1 - (1 - p)^2) + P\{X = k - 1\}p^2$$

which follows since the $2k+1$ component system will be effective if either
1. $X \ge k + 1$;
2. $X = k$ and at least one of the remaining 2 components function; or
3. $X = k - 1$ and both of the next 2 function.

Because $P_{2k-1}(\text{effective}) = P\{X \ge k\} = P\{X = k\} + P\{X \ge k + 1\}$, we obtain that

$$\begin{aligned}
P_{2k+1}(\text{effective}) - P_{2k-1}(\text{effective}) &= P\{X = k - 1\}p^2 - (1 - p)^2 P\{X = k\} \\
&= \binom{2k-1}{k-1}p^{k-1}(1 - p)^k p^2 - (1 - p)^2 \binom{2k-1}{k}p^k(1 - p)^{k-1} \\
&= \binom{2k-1}{k}p^k(1 - p)^k [p - (1 - p)] \quad \text{since } \binom{2k-1}{k-1} = \binom{2k-1}{k} \\
&\ge 0 \iff p \ge \frac{1}{2} \quad \blacksquare
\end{aligned}$$

**Example 5.1.d.** Suppose that 10 percent of the chips produced by a computer hardware manufacturer are defective. If we order 100 such chips, will $X$, the number of defective ones we receive, be a binomial random variable?

**Solution.** The random variable $X$ will be a binomial random variable with parameters $(100, .1)$ if each chip has probability $.9$ of being functional and if the functioning of successive chips is independent. Whether this is a reasonable assumption when we know that 10 percent of the chips produced are defective depends on additional factors. For instance, suppose that all the chips produced on a given day are always either functional or defective (with 90 percent of the days resulting in functional chips). In this case, if we know that all of our 100 chips were manufactured on the same day, then $X$ will not be a binomial random variable. This is so since the independence of successive chips is not valid. In fact, in this case, we would have

$$P\{X = 100\} = .1, \quad P\{X = 0\} = .9 \quad \blacksquare$$

Since a binomial random variable $X$, with parameters $n$ and $p$, represents the number of successes in $n$ independent trials, each having success probability $p$, we can represent $X$ as follows:

$$X = \sum_{i=1}^n X_i \tag{5.1.3}$$

where

$$X_i = \begin{cases} 1 & \text{if the } i\text{th trial is a success} \\ 0 & \text{otherwise} \end{cases}$$

Because the $X_i, i = 1, \dots, n$ are independent Bernoulli random variables, we have that

$$E[X_i] = P\{X_i = 1\} = p$$
$$\text{Var}(X_i) = E[X_i^2] - p^2 = p(1 - p)$$

Using the representation Equation (5.1.3), it is now an easy matter to compute the mean and variance of $X$:

$$E[X] = \sum_{i=1}^n E[X_i] = np$$
$$\text{Var}(X) = \sum_{i=1}^n \text{Var}(X_i) = np(1 - p)$$

If $X_1$ and $X_2$ are independent binomial random variables having respective parameters $(n_i, p), i = 1, 2$, then their sum is binomial with parameters $(n_1 + n_2, p)$.

### 5.1.1 Using R to calculate binomial probabilities

If $X$ is a binomial random variable with parameters $n$ and $p$, then:
- `dbinom(i, n, p)` returns $P(X = i)$
- `pbinom(i, n, p)` returns $P(X \le i)$

**Example 5.1.e.** If $X$ is a binomial random variable with parameters $n = 100, p = .75$, find $P(X = 70)$ and $P(X \ge 80)$.

**Solution.** Using R:

```r
> dbinom(70, 100, .75)
[1] 0.04575381
> 1 - pbinom(79, 100, .75)
[1] 0.1488311
```

To plot binomial probabilities in R:

```r
> i = seq(0, 10, 1)
> p = dbinom(i, 10, .4)
> plot(i, p)
```

## 5.2 The Poisson random variable

A random variable $X$, taking on one of the values $0, 1, 2, \dots$, is said to be a *Poisson random variable* with parameter $\lambda, \lambda > 0$, if its probability mass function is given by

$$P\{X = i\} = e^{-\lambda} \frac{\lambda^i}{i!}, \quad i = 0, 1, \dots \tag{5.2.1}$$

Equation (5.2.1) defines a probability mass function, since

$$\sum_{i=0}^\infty p(i) = e^{-\lambda} \sum_{i=0}^\infty \frac{\lambda^i}{i!} = e^{-\lambda} e^\lambda = 1$$

Its moment generating function is:

$$\phi(t) = E[e^{tX}] = \sum_{i=0}^\infty e^{ti} e^{-\lambda} \frac{\lambda^i}{i!} = e^{-\lambda} \sum_{i=0}^\infty \frac{(\lambda e^t)^i}{i!} = \exp\{\lambda(e^t - 1)\}$$

Differentiation yields:

$$\phi'(t) = \lambda e^t \exp\{\lambda(e^t - 1)\} \implies E[X] = \phi'(0) = \lambda$$
$$\phi''(t) = (\lambda e^t)^2 \exp\{\lambda(e^t - 1)\} + \lambda e^t \exp\{\lambda(e^t - 1)\} \implies \text{Var}(X) = \phi''(0) - (E[X])^2 = \lambda^2 + \lambda - \lambda^2 = \lambda$$

Thus both the mean and the variance of a Poisson random variable are equal to the parameter $\lambda$.

### Poisson Approximation to the Binomial Distribution
When $n$ is large and $p$ is small, a binomial random variable with parameters $(n, p)$ can be approximated by a Poisson random variable with mean $\lambda = np$:

$$P\{X = i\} \approx e^{-\lambda} \frac{\lambda^i}{i!}$$

**Example 5.2.a.** Suppose that the average number of accidents occurring weekly on a particular stretch of a highway equals 3. Calculate the probability that there is at least one accident this week.

**Solution.** Let $X$ denote the number of accidents during this week.

$$P\{X \ge 1\} = 1 - P\{X = 0\} = 1 - e^{-3} \frac{3^0}{0!} = 1 - e^{-3} \approx .9502 \quad \blacksquare$$

**Example 5.2.b.** Suppose the probability that an item produced by a certain machine will be defective is $.1$. Find the probability that a sample of 10 items will contain at most one defective item.

**Solution.** Exact binomial probability:

$$\binom{10}{0}(.1)^0(.9)^{10} + \binom{10}{1}(.1)^1(.9)^9 = .7361$$

Poisson approximation with $\lambda = 10(.1) = 1$:

$$e^{-1}\frac{1^0}{0!} + e^{-1}\frac{1^1}{1!} = 2e^{-1} \approx .7358 \quad \blacksquare$$

**Example 5.2.c.** Alpha-particle emissions: $\lambda = 3.2$.

$$P\{X \le 2\} = e^{-3.2} + 3.2 e^{-3.2} + \frac{(3.2)^2}{2} e^{-3.2} = .382 \quad \blacksquare$$

**Example 5.2.d.** Insurance claims with mean 5:

$$P\{X \le 2\} = e^{-5} + e^{-5}\frac{5^1}{1!} + e^{-5}\frac{5^2}{2!} = \frac{37}{2} e^{-5} \approx .1247$$

Probability of 4 claims in exactly 3 of the next 5 days:

$$P\{X = 4\} = e^{-5}\frac{5^4}{4!} \approx .1755 \implies \binom{5}{3}(.1755)^3(.8245)^2 \approx .0367 \quad \blacksquare$$

**Example 5.2.e (Matching Hats Problem).** If $n$ people randomly choose hats, the number $X$ of people selecting their own hat has approximately a Poisson distribution with mean 1, and $E[X] = 1$.

### Reproductive Property of the Poisson Distribution
If $X_1$ and $X_2$ are independent Poisson random variables with means $\lambda_1$ and $\lambda_2$, then $X_1 + X_2$ is a Poisson random variable with mean $\lambda_1 + \lambda_2$.

**Example 5.2.f.** Daily defective stereos $\lambda_1 = 4, \lambda_2 = 4 \implies X_1 + X_2 \sim \text{Poisson}(8)$:

$$P\{X_1 + X_2 \le 3\} = \sum_{i=0}^3 e^{-8}\frac{8^i}{i!} = .04238 \quad \blacksquare$$

### Splitting a Poisson Random Variable
If a Poisson number of events $N$ with mean $\lambda$ occurs, and each event is independently classified as type 1 with probability $p$ and type 2 with probability $1 - p$, then $N_1$ and $N_2$ are independent Poisson random variables with respective means $\lambda p$ and $\lambda(1 - p)$.

### 5.2.1 Using R to calculate Poisson probabilities

- `dpois(i, lambda)` returns $P(X = i)$
- `ppois(i, lambda)` returns $P(X \le i)$

## 5.3 The hypergeometric random variable *(Optional)*

A bin contains $N + M$ batteries, of which $N$ are acceptable and $M$ are defective. A sample of size $n$ is randomly chosen without replacement. If $X$ denotes the number of acceptable batteries:

$$P\{X = i\} = \frac{\binom{N}{i}\binom{M}{n-i}}{\binom{N+M}{n}}, \quad i = 0, 1, \dots, \min(N, n) \tag{5.3.1}$$

Mean and variance:

$$E[X] = np \quad \text{where } p = \frac{N}{N + M}$$
$$\text{Var}(X) = np(1 - p)\left[1 - \frac{n - 1}{N + M - 1}\right]$$

**Example 5.3.a.** System of 6 components chosen from 20 (15 working, 5 defective).

$$P\{X \ge 4\} = \frac{\binom{15}{4}\binom{5}{2} + \binom{15}{5}\binom{5}{1} + \binom{15}{6}\binom{5}{0}}{\binom{20}{6}} \approx .8687 \quad \blacksquare$$

**Example 5.3.b (Capture-Recapture Method).** Estimating animal population $N$: $N \approx \frac{rn}{i}$.

**Example 5.3.c.** If $X \sim \text{Binomial}(n, p)$ and $Y \sim \text{Binomial}(m, p)$ are independent, the conditional distribution of $X$ given $X + Y = k$ is hypergeometric.

In R:
- `dhyper(i, N, M, n)`
- `phyper(i, N, M, n)`

## 5.4 The uniform random variable

A random variable $X$ is uniformly distributed over the interval $[\alpha, \beta]$ if:

$$f(x) = \begin{cases} \frac{1}{\beta - \alpha} & \text{if } \alpha \le x \le \beta \\ 0 & \text{otherwise} \end{cases}$$

For any subinterval $[a, b] \subseteq [\alpha, \beta]$:

$$P\{a < X < b\} = \frac{b - a}{\beta - \alpha}$$

Mean and variance:

$$E[X] = \frac{\alpha + \beta}{2}$$
$$\text{Var}(X) = \frac{(\beta - \alpha)^2}{12}$$

**Example 5.4.a.** Uniform over $[0, 10]$: (a) $P\{2 < X < 9\} = 7/10$, (b) $P\{1 < X < 4\} = 3/10$, (c) $P\{X < 5\} = 5/10$, (d) $P\{X > 6\} = 4/10$.

**Example 5.4.b.** Bus arrivals at 15-min intervals: Uniform on $(0, 30)$. (a) $1/3$, (b) $1/5$.

**Example 5.4.c.** Shockley equation $I = I_0(e^{aV} - 1)$ with $V \sim \text{Uniform}(1, 3)$: $E[I] \approx .3269$.

**Example 5.4.d (Choosing a Random Subset).** Generating random subset of size $k$ from $n$ elements using uniform random numbers.

**Example 5.4.e.** 2D uniform distribution over rectangular region $R = [0, a] \times [0, b]$ has joint density $f(x, y) = \frac{1}{ab}$, where $X$ and $Y$ are independent uniform random variables.

## 5.5 Normal random variables

A random variable is normally distributed with parameters $\mu$ and $\sigma^2$, denoted $X \sim N(\mu, \sigma^2)$, if its density is

$$f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-(x-\mu)^2/2\sigma^2}, \quad -\infty < x < \infty$$

Mean and variance:

$$E[X] = \mu, \qquad \text{Var}(X) = \sigma^2$$

### Properties:
1. If $X \sim N(\mu, \sigma^2)$, then $Y = a + bX \sim N(a + b\mu, \; b^2\sigma^2)$.
2. Standard normal: $Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$.
   $$\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-y^2/2} \, dy$$
   $$\Phi(-x) = 1 - \Phi(x)$$
3. $P\{a < X < b\} = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)$.
4. Moment generating function:
   $$\phi(t) = e^{\mu t + \sigma^2 t^2 / 2}$$
5. Sum of independent normal random variables: If $X_i \sim N(\mu_i, \sigma_i^2)$ are independent, then $\sum_{i=1}^n X_i \sim N\left(\sum_{i=1}^n \mu_i, \; \sum_{i=1}^n \sigma_i^2\right)$.

**Example 5.5.a.** $X \sim N(3, 16)$:
(a) $P\{X < 11\} = \Phi(2) = .9772$
(b) $P\{X > -1\} = \Phi(1) = .8413$
(c) $P\{2 < X < 7\} = \Phi(1) - \Phi(-0.25) = .4400$

**Example 5.5.b.** Binary signal transmission with normal channel noise:
- $P\{\text{error} \mid \text{message is } "1"\} = 1 - \Phi(1.5) = .0668$
- $P\{\text{error} \mid \text{message is } "0"\} = 1 - \Phi(2.5) = .0062$

**Example 5.5.c.** $W = 3V^2$ where $V \sim N(6, 1)$:
(a) $E[W] = 3(\text{Var}(V) + E^2[V]) = 3(1 + 36) = 111$.
(b) $P(W > 120) = P(V > \sqrt{40}) \approx 0.3728$.

**Example 5.5.d.** Annual LA rainfall $X_1, X_2 \sim N(12.08, 3.1^2)$ independent:
(a) $P(X_1 + X_2 > 25) \approx 0.4240$
(b) $P(X_1 - X_2 > 3) \approx 0.2469$

In R:
- `pnorm(x, mean, sd)` computes $P(X \le x)$
- `qnorm(1 - alpha, mean, sd)` computes percentiles $z_\alpha$
- `dnorm(x, mean, sd)` computes density

## 5.6 Exponential random variables

A continuous random variable has an exponential distribution with parameter $\lambda > 0$ if its density is

$$f(x) = \begin{cases} \lambda e^{-\lambda x} & x \ge 0 \\ 0 & x < 0 \end{cases}$$

Distribution function:

$$F(x) = 1 - e^{-\lambda x}, \quad x \ge 0$$

Mean and variance:

$$E[X] = \frac{1}{\lambda}, \qquad \text{Var}(X) = \frac{1}{\lambda^2}$$

Moment generating function:

$$\phi(t) = \frac{\lambda}{\lambda - t}, \quad t < \lambda$$

### Memoryless Property
$$P\{X > s + t \mid X > t\} = P\{X > s\}, \quad \text{for all } s, t \ge 0$$

**Proposition 5.6.1.** If $X_1, \dots, X_n$ are independent exponential random variables with parameters $\lambda_1, \dots, \lambda_n$, then $\min(X_1, \dots, X_n)$ is exponential with parameter $\sum_{i=1}^n \lambda_i$.

**Example 5.6.a.** Car battery lifetime.
**Example 5.6.b.** 3 interchangeable machines.
**Example 5.6.c.** Series system survival: $P\{\text{system life} > t\} = e^{-\sum \lambda_i t}$.

### 5.6.1 The Poisson Process *(Optional)*
Events occurring at rate $\lambda$ over time:
- The number of events $N(t)$ in $[0, t]$ is Poisson with mean $\lambda t$:
  $$P\{N(t) = k\} = e^{-\lambda t} \frac{(\lambda t)^k}{k!}$$
- Interarrival times $X_1, X_2, \dots$ are independent exponential random variables each with mean $1/\lambda$.

### 5.6.2 The Pareto Distribution *(Optional)*
If $X$ is exponential with rate $\lambda$, then $Y = \alpha e^X$ is a Pareto random variable with parameters $\alpha$ (minimum) and $\lambda$ (index):

$$F_Y(y) = 1 - \left(\frac{\alpha}{y}\right)^\lambda, \quad y \ge \alpha$$
$$f_Y(y) = \lambda \alpha^\lambda y^{-(\lambda + 1)}, \quad y \ge \alpha$$
$$E[Y] = \alpha \frac{\lambda}{\lambda - 1} \quad (\text{for } \lambda > 1)$$

80-20 rule connection when $\lambda = \log(5)/\log(4) \approx 1.161$.

## 5.7 The gamma distribution *(Optional)*

A random variable has a gamma distribution with parameters $(\alpha, \lambda), \lambda > 0, \alpha > 0$ if:

$$f(x) = \frac{\lambda e^{-\lambda x}(\lambda x)^{\alpha-1}}{\Gamma(\alpha)}, \quad x \ge 0$$

where the gamma function is defined by $\Gamma(\alpha) = \int_0^\infty e^{-y} y^{\alpha-1} \, dy$.

Properties:
- $\Gamma(\alpha) = (\alpha - 1)\Gamma(\alpha - 1)$
- For integer $n$: $\Gamma(n) = (n - 1)!$
- $\phi(t) = \left(\frac{\lambda}{\lambda - t}\right)^\alpha, \quad t < \lambda$
- $E[X] = \frac{\alpha}{\lambda}, \quad \text{Var}(X) = \frac{\alpha}{\lambda^2}$
- Sum of independent gamma random variables: $\sum_{i=1}^n X_i \sim \text{Gamma}\left(\sum \alpha_i, \lambda\right)$.
- Sum of $n$ independent exponentials with rate $\lambda$ is $\text{Gamma}(n, \lambda)$.

## 5.8 Distributions arising from the normal

### 5.8.1 The chi-square distribution
If $Z_1, \dots, Z_n$ are independent standard normal random variables, then

$$X = Z_1^2 + \dots + Z_n^2 \sim \chi_n^2$$

is a chi-square random variable with $n$ degrees of freedom.
- $\chi_n^2$ is identical to $\text{Gamma}(n/2, 1/2)$.
- $E[X] = n, \quad \text{Var}(X) = 2n$.
- Additive property: $\chi_{n_1}^2 + \chi_{n_2}^2 \sim \chi_{n_1+n_2}^2$.
- In R: `pchisq(x, n)`, `qchisq(1 - alpha, n)`.

### 5.8.2 The $t$-distribution
If $Z \sim N(0, 1)$ and $\chi_n^2$ are independent, then

$$T_n = \frac{Z}{\sqrt{\chi_n^2 / n}}$$

has a $t$-distribution with $n$ degrees of freedom.
- Symmetric about 0.
- $E[T_n] = 0 \ (n > 1)$, $\text{Var}(T_n) = \frac{n}{n - 2} \ (n > 2)$.
- In R: `pt(x, n)`, `qt(1 - alpha, n)`.

### 5.8.3 The $F$-distribution
If $\chi_n^2$ and $\chi_m^2$ are independent, then

$$F_{n, m} = \frac{\chi_n^2 / n}{\chi_m^2 / m}$$

has an $F$-distribution with $n$ numerator and $m$ denominator degrees of freedom.
- In R: `pf(x, n, m)`, `qf(1 - alpha, n, m)`.

## 5.9 The logistics distribution *(Optional)*

Distribution function:

$$F(x) = \frac{e^{(x-\mu)/v}}{1 + e^{(x-\mu)/v}}, \quad -\infty < x < \infty$$

Density function:

$$f(x) = \frac{e^{(x-\mu)/v}}{v(1 + e^{(x-\mu)/v})^2}$$

Mean: $E[X] = \mu$.

## 5.10 Distributions in R

**Table 5.2: Distribution Names in R.**

| Distribution | Name in R |
| :--- | :--- |
| binomial with parameters $n, p$ | `binom(n, p)` |
| Poisson with parameter $\lambda$ | `pois(lambda)` |
| hypergeometric with parameters $N, M, n$ | `hyper(N, M, n)` |
| standard normal | `norm` |
| normal with parameters $\mu, \sigma^2$ | `norm(mu, sigma)` |
| chi-square with $n$ degrees of freedom | `chisq(n)` |
| $T$-distribution with $n$ degrees of freedom | `t(n)` |
| $F$-distribution with degrees of freedom $n, m$ | `f(n, m)` |
| exponential with rate 1 | `exp` |
| exponential with rate $\lambda$ | `exp(lambda)` |
| gamma with parameters $\alpha, \lambda$ | `gamma(alpha, lambda)` |
| logistics with parameters $\mu, v$ | `logis(mu, v)` |
| uniform on $(0, 1)$ | `unif` |
| uniform on $(a, b)$ | `unif(a, b)` |

**Table 5.3: R commands.**

| Command | Description |
| :--- | :--- |
| `dname(x)` | density or mass function |
| `pname(x)` | cumulative distribution function |
| `qname(beta)` | quantile function |
| `plot(x, y)` | plots $y$ as function of $x$ |

---

## Problems

1. A satellite system consists of 4 components and can function adequately if at least 2 of the 4 components are in working condition. If each component is, independently, in working condition with probability .6, what is the probability that the system functions adequately?

2. A communications channel transmits the digits 0 and 1. However, due to static, the digit transmitted is incorrectly received with probability .2. Suppose that we want to transmit an important message consisting of one binary digit. To reduce the chance of error, we transmit 00000 instead of 0 and 11111 instead of 1. If the receiver of the message uses “majority” decoding, what is the probability that the message will be incorrectly decoded? What independence assumptions are you making? (By majority decoding we mean that the message is decoded as “0” if there are at least three zeros in the message received and as “1” otherwise.)

3. If each voter is for Proposition A with probability .7, what is the probability that exactly 7 of 10 voters are for this proposition?

4. Suppose that a particular trait (such as eye color or left-handedness) of a person is classified on the basis of one pair of genes, and suppose that $d$ represents a dominant gene and $r$ a recessive gene. Thus, a person with $dd$ genes is pure dominance, one with $rr$ is pure recessive, and one with $rd$ is hybrid. The pure dominance and the hybrid are alike in appearance. Children receive 1 gene from each parent. If, with respect to a particular trait, 2 hybrid parents have a total of 4 children, what is the probability that 3 of the 4 children have the outward appearance of the dominant gene?

5. At least one-half of an airplane’s engines are required to function in order for it to operate. If each engine independently functions with probability $p$, for what values of $p$ is a 4-engine plane more likely to operate than a 2-engine plane?

6. Let $X$ be a binomial random variable with $E[X] = 7$ and $\text{Var}(X) = 2.1$. Find (a) $P\{X = 4\}$; (b) $P\{X > 12\}$.

7. If $X$ and $Y$ are binomial random variables with respective parameters $(n, p)$ and $(n, 1 - p)$, verify and explain the following identities:
   a. $P\{X \le i\} = P\{Y \ge n - i\}$;
   b. $P\{X = k\} = P\{Y = n - k\}$.

8. If $X$ is a binomial random variable with parameters $n$ and $p$, where $0 < p < 1$, show that
   a. $P\{X = k + 1\} = \frac{p}{1 - p} \frac{n - k}{k + 1} P\{X = k\}, \quad k = 0, 1, \dots, n - 1$.
   b. As $k$ goes from 0 to $n$, $P\{X = k\}$ first increases and then decreases, reaching its largest value when $k$ is the largest integer less than or equal to $(n + 1)p$.

9. An experiment has possible outcomes $1, 2, \dots, r$, with $i$ being the outcome with probability $p_i, \sum_{i=1}^r p_i = 1$. Suppose there are $n$ independent replications of this experiment, and let $N_i$ be the number of them that result in outcome $i, i = 1, \dots, r$.
   a. What is the distribution of $N_1$?
   b. Are $N_1$ and $N_2$ independent?
   c. What is the distribution of $N_1 + N_2$? (*Hint: Use the fact that $N_1 + N_2$ is the number of the $n$ experiments that result in either outcome 1 or outcome 2.*)
   d. For $k < r$, what is the distribution of $\sum_{i=1}^k N_i$?

10. Compare the Poisson approximation with the correct binomial probability for the following cases:
    a. $P\{X = 2\}$ when $n = 10, p = .1$;
    b. $P\{X = 0\}$ when $n = 10, p = .1$;
    c. $P\{X = 4\}$ when $n = 9, p = .2$.

11. If you buy a lottery ticket in 50 lotteries, in each of which your chance of winning a prize is $\frac{1}{100}$, what is the (approximate) probability that you will win a prize (a) at least once, (b) exactly once, and (c) at least twice?

12. The number of times that an individual contracts a cold in a given year is a Poisson random variable with parameter $\lambda = 3$. Suppose a new wonder drug (based on large quantities of vitamin C) has just been marketed that reduces the Poisson parameter to $\lambda = 2$ for 75 percent of the population. For the other 25 percent of the population, the drug has no appreciable effect on colds. If an individual tries the drug for a year and has 0 colds in that time, how likely is it that the drug is beneficial for him or her?

13. In the 1980s, an average of 121.95 workers died on the job each week. Give estimates of the following quantities:
    a. the proportion of weeks having 130 deaths or more;
    b. the proportion of weeks having 100 deaths or less.
    Explain your reasoning.

14. Approximately 80,000 marriages took place in the state of New York last year. Estimate the probability that for at least one of these couples
    a. both partners were born on April 30;
    b. both partners celebrated their birthday on the same day of the year.
    State your assumptions.

15. The game of frustration solitaire is played by turning the cards of a randomly shuffled deck of 52 playing cards over one at a time. Before you turn over the first card, say ace; before you turn over the second card, say two; before you turn over the third card, say three. Continue in this manner (saying ace again before turning over the fourteenth card, and so on). You lose if you ever turn over a card that matches what you have just said. Use the Poisson paradigm to approximate the probability of winning. (The actual probability is .01623.)

16. The probability of error in the transmission of a binary digit over a communication channel is $1/10^3$. Write an expression for the exact probability of more than 3 errors when transmitting a block of $10^3$ bits. What is its approximate value? Assume independence.

17. If $X$ is a Poisson random variable with mean $\lambda$, show that $P\{X = i\}$ first increases and then decreases as $i$ increases, reaching its maximum value when $i$ is the largest integer less than or equal to $\lambda$.

18. A contractor purchases a shipment of 100 transistors. It is his policy to test 10 of these transistors and to keep the shipment only if at least 9 of the 10 are in working condition. If the shipment contains 20 defective transistors, what is the probability it will be kept?

19. Let $X$ denote a hypergeometric random variable with parameters $n, m,$ and $k$. That is,
    $$P\{X = i\} = \frac{\binom{n}{i}\binom{m}{k-i}}{\binom{n+m}{k}}, \quad i = 0, 1, \dots, \min(k, n)$$
    a. Derive a formula for $P\{X = i\}$ in terms of $P\{X = i - 1\}$.
    b. Use part (a) to compute $P\{X = i\}$ for $i = 0, 1, 2, 3, 4, 5$ when $n = m = 10, k = 5$, by starting with $P\{X = 0\}$.
    c. Based on the recursion in part (a), write a program to compute the hypergeometric distribution function.
    d. Use your program from part (c) to compute $P\{X \le 10\}$ when $n = m = 30, k = 15$.

20. Independent trials, each of which is a success with probability $p$, are successively performed. Let $X$ denote the first trial resulting in a success. That is, $X$ will equal $k$ if the first $k-1$ trials are all failures and the $k$th a success. $X$ is called a *geometric random variable*. Compute
    a. $P\{X = k\}, k = 1, 2, \dots$;
    b. $E[X]$.
    Let $Y$ denote the number of trials needed to obtain $r$ successes. $Y$ is called a *negative binomial random variable*. Compute
    c. $P\{Y = k\}, k = r, r + 1, \dots$ (*Hint: In order for $Y$ to equal $k$, how many successes must result in the first $k - 1$ trials and what must be the outcome of trial $k$?*)
    d. Show that $E[Y] = r/p$ (*Hint: Write $Y = Y_1 + \dots + Y_r$ where $Y_i$ is the number of trials needed to go from a total of $i - 1$ to a total of $i$ successes.*)

21. If $U$ is uniformly distributed on $(0, 1)$, show that $a + (b - a)U$ is uniform on $(a, b)$.

22. You arrive at a bus stop at 10 o’clock, knowing that the bus will arrive at some time uniformly distributed between 10 and 10:30. What is the probability that you will have to wait longer than 10 minutes? If at 10:15 the bus has not yet arrived, what is the probability that you will have to wait at least an additional 10 minutes?

23. Let $X_1$ and $X_2$ be independent normal random variables, each having mean 10 and variance $\sigma^2$. Which probability is larger:
    a. $P(X_1 > 15)$ or $P(X_1 + X_2 > 25)$;
    b. $P(X_1 > 15)$ or $P(X_1 + X_2 > 30)$?
    c. Find $x$ such that $P(X_1 + X_2 > x) = P(X_1 > 15)$.

24. The Scholastic Aptitude Test mathematics test scores across the population of high school seniors follow a normal distribution with mean 500 and standard deviation 100. If five seniors are randomly chosen, find the probability that (a) all scored below 600 and (b) exactly three of them scored above 640.

25. The annual rainfall (in inches) in a certain region is normally distributed with $\mu = 40, \sigma = 4$. What is the probability that in 2 of the next 4 years the rainfall will exceed 50 inches? Assume that the rainfalls in different years are independent.

26. The weekly demand for a product approximately has a normal distribution with mean 1000 and standard deviation 200. The current on hand inventory is 2200 and no deliveries will be occurring in the next two weeks. Assuming that the demands in different weeks are independent,
    a. what is the probability that the demand in each of the next 2 weeks is less than 1100?
    b. what is the probability that the total of the demands in the next 2 weeks exceeds 2200?

27. Let $X$ be normal with mean $\mu$ and variance $\sigma^2$. For fixed $\mu$, show that $P(X > 10)$ is an increasing function of $\sigma$ when $\mu < 10$, and a decreasing function of $\sigma$ when $\mu > 10$. Give an intuitive reason why the preceding is true.

28. A manufacturer produces bolts that are specified to be between 1.19 and 1.21 inches in diameter. If its production process results in a bolt’s diameter being normally distributed with mean 1.20 inches and standard deviation .005, what percentage of bolts will not meet specifications?

29. Let $I = \int_{-\infty}^\infty e^{-x^2/2} \, dx$.
    a. Show that for any $\mu$ and $\sigma$, $\frac{1}{\sqrt{2\pi}\sigma} \int_{-\infty}^\infty e^{-(x-\mu)^2/2\sigma^2} \, dx = 1$ is equivalent to $I = \sqrt{2\pi}$.
    b. Show that $I = \sqrt{2\pi}$ by writing $I^2 = \int_{-\infty}^\infty e^{-x^2/2} \, dx \int_{-\infty}^\infty e^{-y^2/2} \, dy = \int_{-\infty}^\infty \int_{-\infty}^\infty e^{-(x^2+y^2)/2} \, dx \, dy$ and then evaluating the double integral by means of a change of variables to polar coordinates.

30. A random variable $X$ is said to have a lognormal distribution if $\log X$ is normally distributed. If $X$ is lognormal with $E[\log X] = \mu$ and $\text{Var}(\log X) = \sigma^2$, determine the distribution function of $X$. That is, what is $P\{X \le x\}$?

31. The salaries of pediatric physicians are approximately normally distributed. If 25 percent of these physicians earn below 180,000 and 25 percent earn above 320,000, what fraction earn
    a. below 250,000;
    b. between 260,000 and 300,000?

32. The sample mean and sample standard deviation on your economics examination were 60 and 20, respectively; the sample mean and sample standard deviation on your statistics examination were 55 and 10, respectively. You scored 70 on the economics exam and 62 on the statistics exam. Assuming that the two histograms of test scores are approximately normal histograms,
    a. on which exam was your percentile score highest?
    b. approximate the percentage of the scores on the economics exam that were below your score.
    c. approximate the percentage of the scores on the statistics exam that were below your score.

33. Value at risk (VAR) has become a key concept in financial calculations. The VAR of an investment is defined as that value $v$ such that there is only a 1 percent chance that the loss from the investment will exceed $v$.
    a. If the gain from an investment is a normal random variable with mean 10 and variance 49, determine the value at risk. (If $X$ is the gain, then $-X$ is the loss.)
    b. Among a set of investments whose gains are all normally distributed show that the one having the smallest VAR is the one having the largest value of $\mu - 2.33\sigma$, where $\mu$ and $\sigma^2$ are the mean and variance of the gain from the investment.

34. The annual rainfall in Cincinnati is normally distributed with mean 40.14 inches and standard deviation 8.7 inches.
    a. What is the probability this year’s rainfall will exceed 42 inches?
    b. What is the probability that the sum of the next 2 years’ rainfall will exceed 84 inches?
    c. What is the probability that the sum of the next 3 years’ rainfall will exceed 126 inches?
    d. For parts (b) and (c), what independence assumptions are you making?

35. The height of adult women in the United States is normally distributed with mean 64.5 inches and standard deviation 2.4 inches. Find the probability that a randomly chosen woman is
    a. less than 63 inches tall;
    b. less than 70 inches tall;
    c. between 63 and 70 inches tall.
    d. Alice is 72 inches tall. What percentage of women is shorter than Alice?
    e. Find the probability that the average of the heights of two randomly chosen women exceeds 66 inches.
    f. Repeat part (e) for four randomly chosen women.

36. An IQ test produces scores that are normally distributed with mean value 100 and standard deviation 14.2. The top 1 percent of all scores are in what range?

37. The time (in hours) required to repair a machine is an exponentially distributed random variable with parameter $\lambda = 1$.
    a. What is the probability that a repair time exceeds 2 hours?
    b. What is the conditional probability that a repair takes at least 3 hours, given that its duration exceeds 2 hours?

38. The number of years a radio functions is exponentially distributed with parameter $\lambda = \frac{1}{8}$. If Jones buys a used radio, what is the probability that it will be working after an additional 10 years?

39. Jones figures that the total number of thousands of miles that a used auto can be driven before it would need to be junked is an exponential random variable with parameter $\frac{1}{20}$. Smith has a used car that he claims has been driven only 10,000 miles. If Jones purchases the car, what is the probability that she would get at least 20,000 additional miles out of it? Repeat under the assumption that the lifetime mileage of the car is not exponentially distributed but rather is (in thousands of miles) uniformly distributed over $(0, 40)$.

40. *(From optional sections)* Let $X_1, X_2, \dots, X_n$ denote the first $n$ interarrival times of a Poisson process and set $S_n = \sum_{i=1}^n X_i$.
    a. What is the interpretation of $S_n$?
    b. Argue that the two events $\{S_n \le t\}$ and $\{N(t) \ge n\}$ are identical.
    c. Use part (b) to show that
       $$P\{S_n \le t\} = 1 - \sum_{j=0}^{n-1} e^{-\lambda t}\frac{(\lambda t)^j}{j!}$$
    d. By differentiating the distribution function of $S_n$ given in part (c), conclude that $S_n$ is a gamma random variable with parameters $n$ and $\lambda$. (This result also follows from Corollary 5.7.2.)

41. *(From optional sections)* Earthquakes occur in a given region in accordance with a Poisson process with rate 5 per year.
    a. What is the probability there will be at least two earthquakes in the first half of 2015?
    b. Assuming that the event in part (a) occurs, what is the probability that there will be no earthquakes during the first 9 months of 2016?
    c. Assuming that the event in part (a) occurs, what is the probability that there will be at least four earthquakes over the first 9 months of the year 2015?

42. *(From optional sections)* When shooting at a target in a two-dimensional plane, suppose that the horizontal miss distance is normally distributed with mean 0 and variance 4 and is independent of the vertical miss distance, which is also normally distributed with mean 0 and variance 4. Let $D$ denote the distance between the point at which the shot lands and the target. Find $E[D]$.

43. If $X$ is a chi-square random variable with 6 degrees of freedom, find
    a. $P\{X \le 6\}$;
    b. $P\{3 \le X \le 9\}$.

44. If $X$ and $Y$ are independent chi-square random variables with 3 and 6 degrees of freedom, respectively, determine the probability that $X + Y$ will exceed 10.

45. Show that $\Gamma(1/2) = \sqrt{\pi}$ (*Hint: Evaluate $\int_0^\infty e^{-x} x^{-1/2} \, dx$ by letting $x = y^2/2, dx = y \, dy$.*)

46. If $T$ has a $t$-distribution with 8 degrees of freedom, find (a) $P\{T \ge 1\}$, (b) $P\{T \le 2\}$, and (c) $P\{-1 < T < 1\}$.

47. If $T_n$ has a $t$-distribution with $n$ degrees of freedom, show that $T_n^2$ has an $F$-distribution with 1 and $n$ degrees of freedom.

48. Let $\Phi$ be the standard normal distribution function. If, for constants $a$ and $b > 0$,
    $$P\{X \le x\} = \Phi\left(\frac{x - a}{b}\right)$$
    characterize the distribution of $X$.

49. *(From optional sections)* Suppose that $Y$ has a Pareto distribution with minimal parameter $\alpha$ and index parameter $\lambda$.
    a. Find $E[Y]$ when $\lambda > 1$, and show that $E[Y] = \infty$ when $\lambda \le 1$.
    b. Find $\text{Var}(Y)$ when $\lambda > 2$.

50. *(From optional sections)* Suppose that $Y = \alpha e^X$, where $X$ is exponential with rate $\lambda$. Use the lack of memory property of the exponential to argue that the conditional distribution of $Y$ given that $Y > y_0 > \alpha$ is Pareto with parameters $y_0$ and $\lambda$.
