# STAT 1103 — Statistics for Engineers I

> **Program:** BSSE 17, 16, 15, 14 | **Semester:** 1-1 | **Institute of Information Technology, University of Dhaka**
> **Complete Question Bank — Sorted by Exam**

---

## 📝 Mid Term Exam

### 17th Batch
**Total Marks: 20 | Time Allowed: 60 minutes**

*Instructions: Attempt all the questions.*

**1.**
- **(a)** Define complement of an event and mutually exclusive events with appropriate examples. Show that $P(A^c) = 1 - P(A)$. `(3 points)`
- **(b)** Define conditional probability and Bayes' rule with appropriate examples. `(3 points)`

**2.** An insurance company has three types of customers — high risk, medium risk, and low risk. Twenty percent of its customers are high risk, 35% are medium risk, and remaining are low risk. Also, the probability that a customer has at least one accident in the current year is 0.25 for high risk, 0.16 for medium risk, and 0.10 for low risk. `(6 points)`
- **(a)** Find the probability that a customer chosen at random will have at least one accident in the current year.
- **(b)** Find the probability that a customer is low risk, given that the person has had at least one accident during the current year.

**3.** A product is classified according to the number of defects it contains ($X_1 \in \{0, 1, 2, 3\}$) and the temperature set at the factory ($X_2 \in \{1 = \text{low}, 2 = \text{high}\}$). The joint probability mass function is given below: `(8 points)`

| $X_1$ \ $X_2$ | 1     | 2     |
|:--------------:|:-----:|:-----:|
| 0              | 1/8   | 1/16  |
| 1              | 1/16  | 1/16  |
| 2              | 3/16  | 1/8   |
| 3              | 1/8   | 1/4   |

- **(a)** Find the marginal distribution of $X_1$ and graphically present it.
- **(b)** Find the cumulative distribution of $X_1$ and graphically present it.
- **(c)** Find $\text{Cov}(X_1, X_2)$.
- **(d)** Find $E(X_1 \mid X_2 = 1)$.

### 16th Batch
**Marks: 20 | Duration: 60 minutes**

**1.** (3 points) Show the following:
   (a) $\sum(x_i-\bar{x})^2 = \sum x_i^2-(\sum x_j)^2/n$
   (b) $\sum(x_i-\bar{x})(y_i-\bar{y}) = \sum x_iy_i-(\sum x_i)(\sum y_i)/n$
   (c) $\sum(z_i-\bar{z})^2 = (1/b^2)\sum(x_i-\bar{x})^2$, where $z_i=(x_i-a)/b$

**2.** (7 points) From midterm exam scores $\{x_1,\dots,x_n\}$: [25 data points given]
   $\sum x^2=8596.99$, $\sum x=452.1$, $n=25$
   (a) Calculate sample mean and variance
   (b) Calculate sample mean and variance of $(x-\bar{x})/s_x$
   (c) Calculate three quartiles
   (d) Draw boxplot
   (e) Statement about distribution shape

**3.** 
   (a) (2 points) Define experiment, sample space, event with examples.
   (b) (2 points) What are the axioms of probability?

**4.** (6 points) Five independent coin flips, $P(H)=0.6$. Find probability that:
   (a) first three flips are the same
   (b) either first three or last three flips are the same
   (c) at least two heads in first three and at least two tails in last three

---

## 📝 Final Term Exam

### 17th Batch
**Marks: 60 | Duration: 3 hours**

*Instructions: Answer any 5 (five) of the following questions. When answering a question, please answer all the subsections of it at once.*

**1.**
- **(a)** A couple has two children. What is the probability that both are girls if the eldest is a girl? `[2]`
- **(b)** Two dice are thrown. Let $E$ be the event that the sum of the dice is odd, let $F$ be the event that the first die lands on 1, and let $G$ be the event that the sum is 5. Describe the events $EF$, $E \cup F$, $FG$, $EF^c$, $EFG$. `[4]`
- **(c)** Five independent flips of a fair coin are made. Find the probability that: `[6]`
  - (i) the first three flips are the same
  - (ii) either the first three flips are the same, or the last three flips are the same
  - (iii) there are at least two heads among the first three flips, and at least two tails among the last three flips

**2.**
- **(a)** Explain the concepts of probability mass and density functions with appropriate properties. `[4]`
- **(b)** What is a random variable? Compute $V(X)$, where $X$ represents an outcome when we roll a fair die. `[4]`
- **(c)** Suppose that the Rockwell hardness $X$ and abrasion loss $Y$ of a specimen have a joint density given by `[4]`
  $$f(x, y) = x + y, \quad 0 \leq x \leq 1; \quad 0 \leq y \leq 1.$$
  Obtain the expression of covariance of $X$ and $Y$.

**3.**
- **(a)** Derive the moment generating function of $X$, where the probability mass function of $X$ is given below: `[4]`
  $$P(X = x) = \binom{n}{x} p^x (1 - p)^{n - x}, \quad x = 0, 1, \dots, n$$
- **(b)** Using the moment generating function obtained in 3(a), determine the expressions of expected value and variance of the random variable $X$. `[3]`
- **(c)** Time required to repair a machine is an exponentially distributed random variable with parameter $\lambda = 1.5$. `[5]`
  - (i) What is the probability that the repair time exceeds 2 hours?
  - (ii) What is the median repair time?

**4.**
- **(a)** What is a sampling distribution? Describe the theorem associated with deriving the distribution of the sample mean. `[3]`
- **(b)** Describe $t$ and chi-square distribution with appropriate properties. `[3]`
- **(c)** Suppose 12 percent of the population is left-handers. Find the exact and approximate probability that there are between 11 and 14 left-handers in a random sample of 90 members of this population. You need to clearly mention the associated distributions for calculating exact and approximate probabilities. `[6]`

**5.** A discrete random variable $X$ has the following probability distribution:

| $x_i$    | 1    | 2    | 3    | 4    | 5    |
|:--------:|:----:|:----:|:----:|:----:|:----:|
| $f(x_i)$ | 0.10 | 0.15 | 0.30 | 0.25 | 0.20 |

- **(a)** Verify whether this is a valid probability distribution. `[3]`
- **(b)** Plot the probability distribution of $X$. `[2]`
- **(c)** Construct and plot the cumulative distribution function. `[2]`
- **(d)** Calculate the variance and standard deviation of $X$. `[5]`

**6.**
- **(a)** The lifetime (in hours) of a type of electric bulb has an expected value of 500 and a standard deviation of 80 hours. Approximate the probability that the sample mean of $n$ such bulbs is greater than 525 hours when: `[6]`
  - (i) $n = 4$
  - (ii) $n = 16$
  - (iii) $n = 36$
  
  What conclusion can you draw from it?

- **(b)** The following are burning times (in seconds) of floating smoke pots of two different types. `[6]`
  - Type I: 481, 506, 527, 661, 501, 572, 561, 501, 487, 524
  - Type II: 526, 511, 556, 542, 491, 537, 582, 605, 558, 578
  
  Assume burning time follows normal distributions with mean $\mu_1$ and $\mu_2$ for Type I and II pots, respectively, and $\sigma^2$ is the common variance. Find a 95% confidence interval for $(\mu_1 - \mu_2)$ and interpret it.

**7.**
- **(a)** What is a likelihood function? Define the maximum likelihood estimator and describe the procedure for obtaining the maximum likelihood estimator. `[4]`
- **(b)** Let $X_1, \dots, X_n$ be a random sample from a distribution whose probability density function is `[4]`
  $$f(x) = \begin{cases} e^{-(x - \theta)} & x \geq \theta \\ 0 & \text{otherwise} \end{cases}$$
  Obtain the maximum likelihood estimator of $\theta$.
- **(c)** A random sample of 300 CitiBank VISA cardholder accounts indicated a sample mean debt of USD 1220 with a sample standard deviation of USD 840. Construct a 90% confidence interval estimate of the average debt of all cardholders. Interpret the estimated confidence interval. `[4]`

### 16th Batch
**Marks: 60 | Duration: 3 hours**

**1.** 
- **(a)** Calculate sample mean and median of CGPA. Comment on distribution shape. `[4]`
- **(b)** Calculate variance and standard deviation of CGPA. `[5]`
- **(c)** Calculate coefficient of variation. Describe its use. `[3]`

**2.** 
- **(a)** What are axioms of probability? Show $P(A) = 1 - P(A^c)$. `[4]`
- **(b)** Study of children problem. `[2]`
- **(c)** Two factories producing radios problem. `[6]`

**3.** 
- **(a)** Define moment generating function. `[3]`
- **(b)** If $E(X)=2, E(X^2)=8$, calculate $E[(2+4X)^2]$ and $E[X^2+(X+1)^2]$. `[3]`
- **(c)** Joint density function problem. `[6]`

**4.** 
- **(a)** At least half of airplane's engines must function problem. `[3]`
- **(b)** Derive MGF of $X_1$. `[5]`
- **(c)** Annual rainfall problem. `[4]`

**5.** 
- **(a)** Define sampling distribution. How does t differ from normal? `[3]`
- **(b)** Central limit theorem problem. `[5]`
- **(c)** Tobacco company claims problem. `[4]`

**6.** 
- **(a)** Difference between inferential and descriptive statistics. `[2]`
- **(b)** Estimation in statistical inference. `[5]`
- **(c)** Random sample from $N(80,\sigma^2)$ problem. `[5]`

**7.** 
- **(a)** Maximum likelihood estimation concept. `[3]`
- **(b)** Derive log-likelihood expressions. `[6]`
- **(c)** Show $\hat{\theta}$ is unbiased. `[3]`

### 15th Batch
**Marks: 60 | Duration: 3 hours**

*Answer Any FIVE.*

**1.** 
- **(a)** What are different approaches to summarizing data? Define frequency, relative frequency, cumulative relative frequency. `[3]`
- **(b)** When is median preferable over mean? Advantage of SD over variance? `[4]`
- **(c)** Calculate mean, median, Q1, Q3, mode of given transistor lifetime data. `[5]`

**2.** 
- **(a)** What is a random variable? Define discrete and continuous with examples. `[3]`
- **(b)** Define PMF and PDF. `[3]`
- **(c)** Joint density $f(x,y)=\frac{6}{7}(x^2+\frac{xy}{2})$, $0<x<1, 0<y<2$. Find marginals, independence, $E(X)$. `[6]`

**3.** 
- **(a)** Obtain $E(X)$ and CDF for exponential distribution with parameter $\lambda$. `[4]`
- **(b)** Explain memoryless property. `[3]`
- **(c)** Radio lifetime $\sim \text{Exp}(1/8)$. Probability of functioning after 10 years (new and used). `[5]`

**4.** 
- **(a)** What is sampling distribution? Differences between t and standard normal? `[4]`
- **(b)** Electrical part: mean 100hrs, SD 10hrs. For $n=16$, $P(\bar{X}<104)$ and $P(98<\bar{X}<104)$. `[4]`
- **(c)** Chip defective with probability 0.25. For 1000 chips, $P(\text{fewer than 200 defective})$. `[4]`

### 14th Batch
**Marks: 60 | Duration: 3 hours**

**1.** 
- **(a)** Define probability. Prove addition theorem for two events. `(5)`
- **(b)** Three hearts from 52 cards without replacement? `(4)`
- **(c)** $P(A)=0.4, P(B)=0.5, P(A \cap B)=0.2$. Find $P(A|B)$ and $P(B|A)$. `(3)`

**2.** 
- **(a)** State and prove Bayes' theorem. `(5)`
- **(b)** Factory machines A(25%), B(35%), C(40%). Defective rates 5%, 4%, 2%. $P(C|\text{defective})$? `(7)`

**3.** 
- **(a)** Define random variable. Discrete vs continuous. `(4)`
- **(b)** $P(X)$: 0.1, 0.2, 0.3, 0.25, 0.15. Find $E(X), E(X^2), \text{Var}(X)$. `(8)`

**4.** 
- **(a)** Define Binomial distribution. Derive mean and variance. `(6)`
- **(b)** $X \sim B(6,1/3)$, find $P(X \geq 2)$. `(6)`

**5.** 
- **(a)** Define normal distribution. Properties. `(4)`
- **(b)** Marks $\sim N(65,100)$. $P(55<X<75)$? `(4)`
- **(c)** Define standard normal. Relationship with normal. `(4)`

**6.** 
- **(a)** Define correlation. Positive vs negative. `(4)`
- **(b)** Calculate $r$ for $X=\{1,2,3,4,5\}$, $Y=\{2,4,5,4,5\}$. `(8)`
