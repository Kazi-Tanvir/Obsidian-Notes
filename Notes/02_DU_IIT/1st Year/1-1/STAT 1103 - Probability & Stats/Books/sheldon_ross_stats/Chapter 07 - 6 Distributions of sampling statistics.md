# Chapter 6: Distributions of sampling statistics

## 6.1 Introduction

The science of statistics deals with drawing conclusions from observed data. For instance, a typical situation in a technological study arises when one is confronted with a large collection, or population, of items that have measurable values associated with them. By suitably sampling from this collection, and then analyzing the sampled items, one hopes to be able to draw some conclusions about the collection as a whole.

To use sample data to make inferences about an entire population, it is necessary to make some assumptions about the relationship between the two. One such assumption, which is often quite reasonable, is that there is an underlying (population) probability distribution such that the measurable values of the items in the population can be thought of as being independent random variables having this distribution. If the sample data are then chosen in a random fashion, then it is reasonable to suppose that they too are independent values from the distribution.

**Definition.** If $X_1, \dots, X_n$ are independent random variables having a common distribution $F$, then we say that they constitute a *sample* (sometimes called a *random sample*) from the distribution $F$.

In most applications, the population distribution $F$ will not be completely specified and one will attempt to use the data to make inferences about $F$. Sometimes it will be supposed that $F$ is specified up to some unknown parameters (for instance, one might suppose that $F$ was a normal distribution function having an unknown mean and variance, or that it is a Poisson distribution function whose mean is not given), and at other times it might be assumed that almost nothing is known about $F$ (except maybe for assuming that it is a continuous, or a discrete, distribution). Problems in which the form of the underlying distribution is specified up to a set of unknown parameters are called *parametric inference problems*, whereas those in which nothing is assumed about the form of $F$ are called *nonparametric inference problems*.

**Example 6.1.a.** Suppose that a new process has just been installed to produce computer chips, and suppose that the successive chips produced by this new process will have useful lifetimes that are independent with a common unknown distribution $F$. Physical reasons sometimes suggest the parametric form of the distribution $F$; for instance, it may lead us to believe that $F$ is a normal distribution, or that $F$ is an exponential distribution. In such cases, we are confronted with a parametrical statistical problem in which we would want to use the observed data to estimate the parameters of $F$. For instance, if $F$ were assumed to be a normal distribution, then we would want to estimate its mean and variance; if $F$ were assumed to be exponential, we would want to estimate its mean. In other situations, there might not be any physical justification for supposing that $F$ has any particular form; in this case the problem of making inferences about $F$ would constitute a nonparametric inference problem. $\blacksquare$

In this chapter, we will be concerned with the probability distributions of certain *statistics* that arise from a sample, where a statistic is a random variable whose value is determined by the sample data. Two important statistics that we will discuss are the sample mean and the sample variance.

## 6.2 The sample mean

Consider a population of elements, each of which has a numerical value attached to it. We often suppose that the value associated with any member of the population can be regarded as being the value of a random variable having expectation $\mu$ and variance $\sigma^2$. The quantities $\mu$ and $\sigma^2$ are called the *population mean* and the *population variance*, respectively. Let $X_1, X_2, \dots, X_n$ be a sample of values from this population. The *sample mean* is defined by

$$\bar{X} = \frac{X_1 + \dots + X_n}{n}$$

Its expected value and variance are obtained as follows:

$$E[\bar{X}] = E\left[\frac{X_1 + \dots + X_n}{n}\right] = \frac{1}{n}(E[X_1] + \dots + E[X_n]) = \mu$$

and

$$\text{Var}(\bar{X}) = \text{Var}\left(\frac{X_1 + \dots + X_n}{n}\right) = \frac{1}{n^2}[\text{Var}(X_1) + \dots + \text{Var}(X_n)] = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}$$

Hence, the expected value of the sample mean is the population mean $\mu$ whereas its variance is $1/n$ times the population variance.

## 6.3 The central limit theorem

**Theorem 6.3.1 (The central limit theorem).** Let $X_1, X_2, \dots, X_n$ be a sequence of independent and identically distributed random variables each having mean $\mu$ and variance $\sigma^2$. Then for $n$ large, the distribution of

$$X_1 + \dots + X_n$$

is approximately normal with mean $n\mu$ and variance $n\sigma^2$.

It follows from the central limit theorem that

$$\frac{X_1 + \dots + X_n - n\mu}{\sigma\sqrt{n}}$$

is approximately a standard normal random variable; thus, for $n$ large,

$$P\left\{\frac{X_1 + \dots + X_n - n\mu}{\sigma\sqrt{n}} < x\right\} \approx P\{Z < x\}$$

where $Z$ is a standard normal random variable.

**Example 6.3.a.** An insurance company has 25,000 automobile policy holders. If the yearly claim of a policy holder is a random variable with mean 320 and standard deviation 540, approximate the probability that the total yearly claim exceeds 8.3 million.

**Solution.** Let $X = \sum_{i=1}^{25000} X_i$. By CLT, $X$ is approximately normal with mean $320 \times 25,000 = 8 \times 10^6$ and standard deviation $540\sqrt{25,000} = 8.5381 \times 10^4$.

$$P\{X > 8.3 \times 10^6\} = P\left\{\frac{X - 8 \times 10^6}{8.5381 \times 10^4} > \frac{.3 \times 10^6}{8.5381 \times 10^4}\right\} \approx P\{Z > 3.51\} \approx .00023 \quad \blacksquare$$

In R:

```r
> 1 - pnorm(8.3 * (10)^6, 320 * 25000, 540 * sqrt(25000))
[1] 0.0002210042
```

**Example 6.3.b.** Bridge capacity $W \sim N(400, 40^2)$ in thousands of pounds. Car weight mean 3, standard deviation $.3$. How many cars on bridge span for probability of structural damage to exceed $.1$?

**Solution.** $\sum_{i=1}^n X_i - W$ is approximately normal with mean $3n - 400$ and variance $.09n + 1600$.

$$P_n = P\left\{Z \ge \frac{400 - 3n}{\sqrt{.09n + 1600}}\right\}$$

Since $P\{Z \ge 1.28\} \approx .1$, setting $\frac{400 - 3n}{\sqrt{.09n + 1600}} \le 1.28 \implies n \ge 117$. $\blacksquare$

### Normal Approximation to the Binomial Distribution
For $X \sim \text{Binomial}(n, p)$ with large $n$:

$$\frac{X - np}{\sqrt{np(1 - p)}} \approx Z \sim N(0, 1)$$

**Example 6.3.c.** Freshmen admission: $n = 450, p = .3$. Probability that more than 150 attend:
Using continuity correction $P\{X > 150.5\}$:

$$P\{X > 150.5\} = P\left\{\frac{X - 135}{\sqrt{450(.3)(.7)}} \ge \frac{150.5 - 135}{\sqrt{94.5}}\right\} \approx P\{Z > 1.59\} = .06 \quad \blacksquare$$

### 6.3.1 Approximate distribution of the sample mean
$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \approx Z \sim N(0, 1)$$

**Example 6.3.d.** Worker weights $\mu = 167, \sigma = 27$.
(a) For $n = 36$: $P\{163 < \bar{X} < 170\} \approx P\{-0.8889 < Z < 0.8889\} = 0.6259$.
(b) For $n = 144$: $P\{163 < \bar{X} < 170\} \approx P\{-1.7778 < Z < 1.7778\} = 0.9246$. $\blacksquare$

**Example 6.3.e.** Star distance measurement $\sigma = 2$. For 95% certainty within $\pm .5$:

$$\frac{\sqrt{n}}{4} \ge 1.96 \implies n \ge 61.47 \implies n \ge 62 \quad \blacksquare$$

### 6.3.2 How large a sample is needed?
Rule of thumb: $n \ge 30$ ensures approximate normality for almost all population distributions. For symmetric distributions, even $n = 5$ or $n = 10$ suffices.

## 6.4 The sample variance

**Definition.** The statistic $S^2$, defined by

$$S^2 = \frac{\sum_{i=1}^n (X_i - \bar{X})^2}{n - 1}$$

is called the *sample variance*. $S = \sqrt{S^2}$ is called the *sample standard deviation*.

Using the identity $(n - 1)S^2 = \sum_{i=1}^n X_i^2 - n\bar{X}^2$, taking expectations yields:

$$(n - 1)E[S^2] = n(\sigma^2 + \mu^2) - n\left(\frac{\sigma^2}{n} + \mu^2\right) = (n - 1)\sigma^2 \implies E[S^2] = \sigma^2$$

## 6.5 Sampling distributions from a normal population

Let $X_1, \dots, X_n \sim N(\mu, \sigma^2)$ be independent.

### 6.5.1 Distribution of the sample mean
$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

### 6.5.2 Joint distribution of $\bar{X}$ and $S^2$

**Theorem 6.5.1.** If $X_1, \dots, X_n$ is a sample from a normal population with mean $\mu$ and variance $\sigma^2$, then $\bar{X}$ and $S^2$ are independent random variables, with:
- $\bar{X} \sim N(\mu, \sigma^2/n)$
- $\frac{(n - 1)S^2}{\sigma^2} \sim \chi_{n-1}^2$

**Example 6.5.a.** CPU time $n = 15, \mu = 20, \sigma^2 = 9$.

$$P\{S^2 > 12\} = P\left\{\frac{14S^2}{9} > \frac{14 \times 12}{9}\right\} = P\left\{\chi_{14}^2 > \frac{56}{3}\right\} \approx 0.1781 \quad \blacksquare$$

**Corollary 6.5.2.**
$$\frac{\sqrt{n}(\bar{X} - \mu)}{S} \sim t_{n-1}$$

## 6.6 Sampling from a finite population

For a population of size $N$ with proportion $p$ having a certain characteristic, a random sample of size $n$ has $X = \sum_{i=1}^n X_i$ members with the characteristic:

$$E[X] = np, \qquad \text{SD}(X) = \sqrt{np(1 - p)}$$
$$E[\bar{X}] = p, \qquad \text{Var}(\bar{X}) = \frac{p(1 - p)}{n}$$

When $N$ is large relative to $n$, the hypergeometric distribution of $X$ is well approximated by $\text{Binomial}(n, p)$.

**Example 6.6.a.** $p = .45, n = 200$:
(a) $E[X] = 90, \text{SD}(X) = \sqrt{200(.45)(.55)} = 7.0356$.
(b) $P(X \ge 101) = 1 - \text{pbinom}(100, 200, .45) \approx 0.0681$. $\blacksquare$

**Example 6.6.b.** Pork consumption in Denmark: $\mu = 147, \sigma = 62, n = 25 \implies \bar{X} \approx N(147, 12.4^2)$.

$$P\{\bar{X} > 150\} \approx P\left\{Z > \frac{3}{12.4}\right\} \approx 0.4044 \quad \blacksquare$$

---

## Problems

1. Suppose that $X_1, X_2, X_3$ are independent with the common probability mass function
   $$P\{X_i = 0\} = .2, \quad P\{X_i = 1\} = .3, \quad P\{X_i = 3\} = .5, \quad i = 1, 2, 3$$
   a. Plot the probability mass function of $\bar{X}_2 = \frac{X_1 + X_2}{2}$.
   b. Determine $E[\bar{X}_2]$ and $\text{Var}(\bar{X}_2)$.
   c. Plot the probability mass function of $\bar{X}_3 = \frac{X_1 + X_2 + X_3}{3}$.
   d. Determine $E[\bar{X}_3]$ and $\text{Var}(\bar{X}_3)$.

2. If 10 fair dice are rolled, approximate the probability that the sum of the values obtained (which ranges from 10 to 60) is between 30 and 40 inclusive.

3. Approximate the probability that the sum of 16 independent uniform $(0, 1)$ random variables exceeds 10.

4. A roulette wheel has 38 slots, numbered 0, 00, and 1 through 36. If you bet 1 on a specified number, you either win 35 if the roulette ball lands on that number or lose 1 if it does not. If you continually make such bets, approximate the probability that
   a. you are winning after 34 bets;
   b. you are winning after 1000 bets;
   c. you are winning after 100,000 bets.
   Assume that each roll of the roulette ball is equally likely to land on any of the 38 numbers.

5. A highway department has enough salt to handle a total of 80 inches of snowfall. Suppose the daily amount of snow has a mean of 1.5 inches and a standard deviation of .3 inch.
   a. Approximate the probability that the salt on hand will suffice for the next 50 days.
   b. What assumption did you make in solving part (a)?
   c. Do you think this assumption is justified? Explain briefly.

6. Fifty numbers are rounded off to the nearest integer and then summed. If the individual roundoff errors are uniformly distributed between $-.5$ and $.5$, what is the approximate probability that the resultant sum differs from the exact sum by more than 3?

7. A six-sided die, in which each side is equally likely to appear, is repeatedly rolled until the total of all rolls exceeds 400. Approximate the probability that this will require more than 140 rolls.

8. The amount of time that a certain type of battery functions is a random variable with mean 5 weeks and standard deviation 1.5 weeks. Upon failure, it is immediately replaced by a new battery. Approximate the probability that 13 or more batteries will be needed in a year.

9. The lifetime of a certain electrical part is a random variable with mean 100 hours and standard deviation 20 hours. If 16 such parts are tested, find the probability that the sample mean is
   a. less than 104;
   b. between 98 and 104 hours.

10. A tobacco company claims that the amount of nicotine in its cigarettes is a random variable with mean 2.2 mg and standard deviation .3 mg. However, the sample mean nicotine content of 100 randomly chosen cigarettes was 3.1 mg. What is the approximate probability that the sample mean would have been as high or higher than 3.1 if the company’s claims were true?

11. The lifetime (in hours) of a type of electric bulb has expected value 500 and standard deviation 80. Approximate the probability that the sample mean of $n$ such bulbs is greater than 525 when
    a. $n = 4$;
    b. $n = 16$;
    c. $n = 36$;
    d. $n = 64$.

12. An instructor knows from past experience that student exam scores have mean 77 and standard deviation 15. At present the instructor is teaching two separate classes — one of size 25 and the other of size 64.
    a. Approximate the probability that the average test score in the class of size 25 lies between 72 and 82.
    b. Repeat part (a) for a class of size 64.
    c. What is the approximate probability that the average test score in the class of size 25 is higher than that of the class of size 64?
    d. Suppose the average scores in the two classes are 76 and 83. Which class, the one of size 25 or the one of size 64, do you think was more likely to have averaged 83?

13. If $X$ is binomial with parameters $n = 150, p = .6$, compute the exact value of $P\{X \le 80\}$ and compare with its normal approximation both (a) making use of and (b) not making use of the continuity correction.

14. Teams 1, 2, 3, 4 are all scheduled to play with each of the other teams 10 times. Whenever team $i$ plays team $j$, team $i$ is the winner with probability $P_{i, j}$, and team $j$ is the winner with probability $P_{j, i} = 1 - P_{i, j}$. If
    $$P_{1, 2} = .6, \quad P_{1, 3} = .7, \quad P_{1, 4} = .75,$$
    $$P_{2, 3} = .6, \quad P_{2, 4} = .70, \quad P_{3, 4} = .5,$$
    a. approximate the probability that team 1 wins at least 20 games.
    Suppose we want to approximate the probability that team 2 wins at least as many games as does team 1. To do so, let $X$ be the number of games that team 2 wins against team 1, let $Y$ be the total number of games that team 2 wins against teams 3 and 4, and let $Z$ be the total number of games that team 1 wins against teams 3 and 4.
    b. Are $X, Y, Z$ independent?
    c. Express the event that team 2 wins at least as many games as does team 1 in terms of the random variables $X, Y, Z$.
    d. Approximate the probability that team 2 wins at least as many games as team 1.

15. A club basketball team will play a 60-game season. Thirty-two of these games are against class A teams and 28 are against class B teams. The outcomes of all the games are independent. The team will win each game against a class A opponent with probability .5, and it will win each game against a class B opponent with probability .7. Let $X$ denote its total number of victories in the season.
    a. Is $X$ a binomial random variable?
    b. Let $X_A$ and $X_B$ denote, respectively, the number of victories against class A and class B teams. What are the distributions of $X_A$ and $X_B$?
    c. What is the relationship between $X_A, X_B,$ and $X$?
    d. Approximate the probability that the team wins 40 or more games.

16. Argue, based on the central limit theorem, that a Poisson random variable having mean $\lambda$ will approximately have a normal distribution with mean and variance both equal to $\lambda$ when $\lambda$ is large. If $X$ is Poisson with mean 100, compute the exact probability that $X$ is less than or equal to 116 and compare it with its normal approximation both when a continuity correction is utilized and when it is not.

17. Compute $P\{X \le 10\}$ when $X$ is a binomial random variable with parameters $n = 100, p = .1$. Now compare this with its (a) Poisson and (b) normal approximation. In using the normal approximation, write the desired probability as $P\{X < 10.5\}$ so as to utilize the continuity correction.

18. The temperature at which a thermostat goes off is normally distributed with variance $\sigma^2$. If the thermostat is to be tested five times, find
    a. $P\{S^2/\sigma^2 \le 1.8\}$
    b. $P\{.85 \le S^2/\sigma^2 \le 1.15\}$
    where $S^2$ is the sample variance of the five data values.

19. In Problem 18, how large a sample would be necessary to ensure that the probability in part (a) is at least .95?

20. Consider two independent samples — the first of size 10 from a normal population having variance 4 and the second of size 5 from a normal population having variance 2. Compute the probability that the sample variance from the second sample exceeds the one from the first. (*Hint: Relate it to the $F$-distribution.*)

21. Twelve percent of the population is left-handed. Find the probability that there are between 10 and 14 left-handers in a random sample of 100 members of this population. That is, find $P\{10 \le X \le 14\}$, where $X$ is the number of left-handers in the sample.

22. Fifty-two percent of the residents of a certain city are in favor of teaching evolution in high school. Find or approximate the probability that at least 50 percent of a random sample of size $n$ is in favor of teaching evolution, when
    a. $n = 10$;
    b. $n = 100$;
    c. $n = 1000$;
    d. $n = 10,000$.

23. The following table gives the percentages of individuals of a given city, categorized by gender, that follow certain negative health practices. Suppose a random sample of 300 men is chosen. Approximate the probability that
    a. at least 150 of them rarely eat breakfast;
    b. fewer than 100 of them smoke.

| | Sleeps 6 Hours or Less per Night | Smoker | Rarely Eats Breakfast | Is 20 Percent or More Overweight |
| :--- | :--- | :--- | :--- | :--- |
| **Men** | 22.7 | 28.4 | 45.4 | 29.6 |
| **Women** | 21.4 | 22.8 | 42.0 | 25.6 |

*Source: U.S. National Center for Health Statistics, Health Promotion and Disease Prevention.*

24. (Use the table from Problem 23.) Suppose a random sample of 300 women is chosen. Approximate the probability that
    a. at least 60 of them are overweight by 20 percent or more;
    b. fewer than 50 of them sleep 6 hours or less nightly.

25. (Use the table from Problem 23.) Suppose random samples of 300 women and of 300 men are chosen. Approximate the probability that more women than men rarely eat breakfast.

26. The following table uses data concerning the percentages of teenage male and female full-time workers whose annual salaries fall in different salary groupings. Suppose random samples of 1000 men and 1000 women were chosen. Use the table to approximate the probability that
    a. at least half of the women earned less than $20,000;
    b. more than half of the men earned $20,000 or more;
    c. more than half of the women and more than half of the men earned $20,000 or more;
    d. 250 or fewer of the women earned at least $25,000;
    e. at least 200 of the men earned $50,000 or more;
    f. more women than men earned between $20,000 and $24,999.

| Earnings Range | Percentage of Women | Percentage of Men |
| :--- | :--- | :--- |
| $4999 or less | 2.8 | 1.8 |
| $5000 to $9999 | 10.4 | 4.7 |
| $10,000 to $19,999 | 41.0 | 23.1 |
| $20,000 to $24,999 | 16.5 | 13.4 |
| $25,000 to $49,999 | 26.3 | 42.1 |
| $50,000 and over | 3.0 | 14.9 |

*Source: U.S. Department of Commerce, Bureau of the Census.*

27. Today, roughly 10.5 percent of the labor force belong to a union. If five workers are randomly chosen, what is the probability that none of them belong to a union? Compare your answer to what it would have been in 1983 when 20.1 percent of the workforce belonged to a union.

28. The sample mean and sample standard deviation of all San Francisco student scores on the most recent Scholastic Aptitude Test examination in mathematics were 517 and 120. Approximate the probability that a random sample of 144 students would have an average score exceeding
    a. 507;
    b. 517;
    c. 537;
    d. 550.

29. The average salary of newly graduated students with bachelor’s degrees in chemical engineering is $53,600, with a standard deviation of $3200. Approximate the probability that the average salary of a sample of 12 recently graduated chemical engineers exceeds $55,000.

30. A certain component is critical to the operation of an electrical system and must be replaced immediately upon failure. If the mean lifetime of this type of component is 100 hours and its standard deviation is 30 hours, how many of the components must be in stock so that the probability that the system is in continual operation for the next 2000 hours is at least .95?
