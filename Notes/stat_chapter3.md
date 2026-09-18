An exam-focused question bank and study system synthesized from the provided past examinations:

---

# STAT 1103: Probability and Statistics for Engineers I

## Comprehensive Exam Practice System & Question Bank

---

### How to Use This Booklet

1. **Hierarchy of Practice**: Prioritize **MUST-DO** questions first to ensure full syllabus coverage across high-frequency exam questions. Proceed to **HIGH-VALUE** problems for depth and **OPTIONAL** problems for edge cases.

2. **Label Conventions**:

* `[PYQ YYYY · Q#]`: Verified problem directly from official exam papers.

* `[GENERATED — based on <pattern>]`: Modeled strictly after recurring test designs to fill syllabus gaps.

* `Marks`: Actual historical mark allocations preserved from source papers.

3. **Pacing**: Target 1.8 minutes per mark for final exams (e.g., a 6-mark problem should take $\approx 10$ minutes).

---

### Syllabus & High-Yield Topic Map

| Module | Core Examinable Topics | Historical Frequency | Mark Share | Exam Traps & Recurring Formats |
| --- | --- | --- | --- | --- |
| **1. Descriptive Statistics** | Sample mean, variance, quartiles, boxplots, algebraic identity proofs | Very High (Midterm), Low-Med (Final) | 5–10% | Forgetting $n-1$ denominator in $s^2$; misapplying change of scale $z = (x-a)/b$ to variance. |
| **2. Probability Foundations** | Axioms, conditional probability, total probability, Bayes' Theorem, coin/dice combinations | 100% (Guaranteed Q1/Q2) | 20–25% | Coin run questions ("first 3 same OR last 3 same" overlapping inclusion-exclusion). |
| **3. Discrete Distributions** | PMF/CDF properties, Binomial, Poisson; MGF derivations, $E(X)$ & $\text{Var}(X)$<br> | 100% (Guaranteed Q3/Q4) | 15–20% | Expansion of binomial $(pe^t + 1-p)^n$; continuity correction when approximating via normal. |
| **4. Continuous Distributions** | PDF normalization constant $c$, CDF integration, Uniform, Exponential, Normal distribution | 100% (Guaranteed Q2/Q5) | 15–20% | Integrating over piece-wise limits; confusing median condition $F(m) = 0.5$ with mean. |
| **5. Joint Distributions** | Joint PMF/PDF, marginals, conditionals, $\text{Cov}(X,Y)$, conditional expectation $E(X\vert{}Y)$<br> | 100% (Guaranteed Mid & Final) | 15–20% | Finding marginals by summing/integrating wrong index; forgetting $\text{Cov}(X,Y) = E(XY) - E(X)E(Y)$. |
| **6. Sampling Distributions & Estimation** | CLT, sample mean distribution, $t$, $\chi^2$, Likelihood, MLE derivation, unbiasedness | 100% (Guaranteed Q6/Q7) | 20–25% | Boundary parameters where derivative is non-zero (shifted exponential $\hat{\theta} = X_{(1)}$). |
| **7. Confidence Intervals** | Single-mean $Z$ vs $t$, difference between means $(\mu_1 - \mu_2)$ with pooled variance | 100% (Guaranteed Q6/Q7) | 10–15% | Using $Z$ instead of $t$ when $\sigma$ is unknown and $n < 30$; calculating pooled standard error $s_p$. |

---

### MUST-DO Questions

**Q 1.1 — 6 marks**
MUST-DO · MEDIUM
[PYQ 2025 Final · Q1(c)] [Topic: Probability Foundations]

Five independent flips of a fair coin are made. Find the probability that:

1. The first three flips are the same;

2. Either the first three flips are the same, or the last three flips are the same;

3. There are at least two heads among the first three flips, and at least two tails among the last three flips.

**Q 1.2 — 6 points**
MUST-DO · MEDIUM
[PYQ 2025 Midterm · Q2] [Topic: Bayes' Rule & Total Probability]

An insurance company has three types of customers: high risk, medium risk, and low risk. Twenty percent of its customers are high risk, 35% are medium risk, and the remaining are low risk. The probability that a customer has at least one accident in the current year is 0.25 for high risk, 0.16 for medium risk, and 0.10 for low risk.

1. Find the probability that a customer chosen at random will have at least one accident in the current year.

2. Find the probability that a customer is low risk, given that the person has had at least one accident during the current year.

**Q 1.3 — 7 marks**
MUST-DO · HARD
[PYQ 2025 Final · Q3(a, b)] [Topic: Moment Generating Functions & Discrete PMF]

1. Derive the moment generating function $M_X(t)$ of $X$, where the probability mass function of $X$ is given by:

$$P(X = x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x = 0, 1, \ldots, n$$

2. Using the moment generating function obtained, determine the expressions of the expected value and variance of $X$.

**Q 1.4 — 8 points**
MUST-DO · MEDIUM
[PYQ 2025 Midterm · Q3] [Topic: Bivariate Discrete Distributions]

A product is classified according to the number of defects it contains ($X_1 \in \{0, 1, 2, 3\}$) and the temperature set at the factory ($X_2 \in \{1 = \text{low}, 2 = \text{high}\}$). The joint PMF is given below:

|  | $X_2 = 1$ | $X_2 = 2$ |
| --- | --- | --- |
| **$X_1 = 0$** | 1/8 | 1/16 |
| **$X_1 = 1$** | 1/16 | 1/16 |
| **$X_1 = 2$** | 3/16 | 1/8 |
| **$X_1 = 3$** | 1/8 | 1/4 |

1. Find the marginal distribution of $X_1$ and graphically present it.

2. Find the cumulative distribution function of $X_1$ and graphically present it.

3. Find $\text{Cov}(X_1, X_2)$.

4. Find $E(X_1 \mid X_2 = 1)$.

**Q 1.5 — 8 marks**
MUST-DO · MEDIUM
[PYQ 2022 Final · Q5(a)] [Topic: Continuous Density Functions]

The probability density function of $X$ is given by:

$$f(x) = \begin{cases} c(1 - x^2) & -1 < x < 1 \\ 0 & \text{otherwise} \end{cases}$$

1. Find the value of $c$.

2. Find the cumulative distribution function $F(x)$, expected value $E(X)$, and variance $\text{Var}(X)$.

**Q 1.6 — 4 marks**
MUST-DO · HARD
[PYQ 2025 Final · Q7(b)] [Topic: Maximum Likelihood Estimation]

Let $X_1, \ldots, X_n$ be a random sample from a distribution whose probability density function is:

$$f(x) = \begin{cases} e^{-(x-\theta)} & x \ge \theta \\ 0 & \text{otherwise} \end{cases}$$

Obtain the maximum likelihood estimator of $\theta$.

**Q 1.7 — 6 marks**
MUST-DO · HARD
[PYQ 2025 Final · Q6(b)] [Topic: Two-Sample Confidence Intervals]

The burning times (in seconds) of floating smoke pots of two different types are recorded:

* **Type I**: 481, 506, 527, 661, 501, 572, 561, 501, 487, 524

* **Type II**: 526, 511, 556, 542, 491, 537, 582, 605, 558, 578

Assume burning times follow normal distributions with mean $\mu_1$ and $\mu_2$ respectively, and common variance $\sigma^2$. Find a 95% confidence interval for $(\mu_1 - \mu_2)$ and interpret it.

---

### Previous-Year Exam Vault

#### Descriptive Statistics & Basic Proofs

**Q 2.1 — 3 points**
HIGH-VALUE · EASY
[PYQ 2024 Midterm · Q1] [Topic: Summation Identities]

Show the following algebraic properties:

1. $\sum_{i=1}^{n}(x_i - \bar{x})^2 = \sum_{i=1}^{n} x_i^2 - \frac{1}{n}\left(\sum_{j=1}^{n} x_j\right)^2$

2. $\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y}) = \sum_{i=1}^{n} x_i y_i - \frac{1}{n}\left(\sum x_i\right)\left(\sum y_i\right)$

3. $\sum_{i=1}^{n}(z_i - \bar{z})^2 = \frac{1}{b^2}\sum_{i=1}^{n}(x_i - \bar{x})^2$, where $z_i = \frac{x_i - a}{b}$

**Q 2.2 — 7 points**
HIGH-VALUE · MEDIUM
[PYQ 2024 Midterm · Q2] [Topic: Exploratory Data Analysis & Quartiles]

From a sample of midterm exam scores $\{x_1, \ldots, x_{25}\}$:

Raw data: 11.5, 11.6, 12.4, 13.2, 13.3, 14.4, 14.9, 15.5, 15.7, 16.5, 17.8, 18.3, 18.8, 19.0, 19.1, 19.9, 19.9, 19.9, 20.5, 20.5, 20.9, 22.8, 23.0, 25.1, 27.6.

Summary: $\sum x^2 = 8596.99$, $\sum x = 452.1$, $n = 25$.

1. Calculate sample mean ($\bar{x}$) and sample variance ($s_x^2$).

2. Calculate the sample mean and variance of the transformed variable $(x - \bar{x})/s_x$.

3. Calculate three quartiles ($Q_1, Q_2, Q_3$).

4. Draw a boxplot of the scores.

5. Make a statement about the shape of the distribution.

**Q 2.3 — 10 marks**
HIGH-VALUE · EASY
[PYQ 2022 Final · Q1] [Topic: Central Tendency & Outliers]

1. What is meant by the central tendency of a dataset? Which measure tends to be most influenced by outliers? **[2 marks]**

2. The sample mean of 12 numbers, which include 34, is 40. If 34 is removed from the set and 38 is added, what is the sample mean of the new set? **[2 marks]**

3. A software firm pays six junior software engineers $35,000 each, two staff engineers $100,000 each, and the owner $350,000:

* What is the mean salary? How many employees earn less than the mean? **[4 marks]**

* What is the median salary? How many earn less than the median? **[4 marks]**

---

#### Probability Foundations & Conditioning

**Q 2.4 — 6 marks**
HIGH-VALUE · EASY
[PYQ 2025 Final · Q1(a, b)] [Topic: Conditional Probability & Events]

1. A couple has two children. What is the probability that both are girls if the eldest is a girl? **[2 marks]**

2. Two dice are thrown. Let $E$ be the event that the sum of the dice is odd, let $F$ be the event that the first die lands on 1, and let $G$ be the event that the sum is 5. Explicitly describe the events $EF$, $E \cup F$, $FG$, $EF^c$, and $EFG$ **[4 marks]**.

**Q 2.5 — 6 points**
HIGH-VALUE · MEDIUM
[PYQ 2024 Midterm · Q4] [Topic: Biased Coin Flips]

Five independent flips of a coin are made with $P(H) = 0.6$. Find the probability that:

1. The first three flips are the same.

2. Either the first three flips are the same, or the last three flips are the same.

3. There are at least two heads among the first three flips and at least two tails among the last three flips.

**Q 2.6 — 5 marks**
HIGH-VALUE · MEDIUM
[PYQ 2022 Final · Q2(a)] [Topic: Medical Diagnostic Testing & Bayes]

Two percent of women aged 45 who participate in routine screening have breast cancer. Ninety percent of those with breast cancer have positive mammographies. Ten percent of the women who do not have breast cancer will also have positive mammographies. Given that a woman has a positive mammography, what is the probability she has breast cancer?

---

#### Random Variables, Expectation & Distributions

**Q 2.7 — 12 marks**
HIGH-VALUE · EASY
[PYQ 2025 Final · Q5] [Topic: Discrete Distributions]

A discrete random variable $X$ has the probability distribution:

| $x_i$ | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| $f(x_i)$ | 0.10 | 0.15 | 0.30 | 0.25 | 0.20 |

1. Verify whether this is a valid probability distribution **[3 marks]**.

2. Plot the probability distribution of $X$ **[2 marks]**.

3. Construct and plot the cumulative distribution function **[2 marks]**.

4. Calculate the variance and standard deviation of $X$ **[5 marks]**.

**Q 2.8 — 4 marks**
HIGH-VALUE · MEDIUM
[PYQ 2025 Final · Q2(c)] [Topic: Continuous Bivariate Density]

Suppose that Rockwell hardness $X$ and abrasion loss $Y$ of a specimen have a joint density:

$$f(x, y) = x + y, \quad 0 \le x \le 1, \; 0 \le y \le 1$$

Obtain the expression for the covariance of $X$ and $Y$.

**Q 2.9 — 8 marks**
HIGH-VALUE · MEDIUM
[PYQ 2022 Final · Q3(b, c)] [Topic: Theoretical Distributions]

1. Derive the expressions of the median for an exponential distribution with parameter $\lambda$, and a normal distribution with parameters $\mu$ and $\sigma^2$ **[3 marks]**.

2. Let $X \sim \text{Poisson}(\lambda)$. Obtain the algebraic expressions for $E(X)$ and $\text{Var}(X)$ **[5 marks]**.

**Q 2.10 — 6 marks**
HIGH-VALUE · MEDIUM
[PYQ 2022 Final · Q4(b, c)] [Topic: Binomial Applications]

1. Let $X$ be a binomial random variable with $E(X) = 7$ and $\text{Var}(X) = 2.1$. Find $P(X = 4)$ and $P(X > 2)$ **[4 marks]**.

2. If you buy a lottery ticket in 50 different lotteries, in each of which your chance of winning a prize is $1/100$, calculate the probability of winning a prize: (i) at least once, (ii) exactly once, (iii) at least twice **[6 marks]**.

---

#### Sampling, Estimation & Inference

**Q 2.11 — 6 marks**
HIGH-VALUE · HARD
[PYQ 2025 Final · Q4(c)] [Topic: Normal Approximation to Binomial]

Suppose 12 percent of the population is left-handed. Find the exact and approximate probability that there are between 11 and 14 left-handers (inclusive) in a random sample of 90 members of this population. Clearly state the associated distributions for calculating exact and approximate probabilities.

**Q 2.12 — 6 marks**
HIGH-VALUE · MEDIUM
[PYQ 2025 Final · Q6(a)] [Topic: Central Limit Theorem]

The lifetime of an electric bulb has $\mu = 500$ hours and $\sigma = 80$ hours. Approximate the probability that the sample mean lifetime $\bar{X}_n$ is greater than 525 hours when:

1. $n = 4$

2. $n = 16$

3. $n = 36$

What conclusion can you draw regarding the behavior of $\bar{X}$ as $n$ increases?

**Q 2.13 — 9 marks**
HIGH-VALUE · HARD
[PYQ 2022 Final · Q7] [Topic: Maximum Likelihood Properties]

1. Explain the concept of maximum likelihood estimation **[3 marks]**.

2. Let $X_1, \ldots, X_n$ be a random sample from $f(x; \theta) = \frac{1}{\theta} e^{-x/\theta}, \; x > 0$. Obtain the log-likelihood function and derive the MLE $\hat{\theta}$ **[6 marks]**.

3. Show that $\hat{\theta}$ is an unbiased estimator of $\theta$ and find $\text{Var}(\hat{\theta})$ **[3 marks]**.

**Q 2.14 — 9 marks**
HIGH-VALUE · MEDIUM
[PYQ 2022 Final · Q6(b)] [Topic: Confidence Intervals]

A sample of $n = 20$ cigarettes has an average nicotine content $\bar{x} = 1.2\text{ mg}$.

1. If known population standard deviation $\sigma = 2\text{ mg}$, compute a 95% confidence interval for the mean nicotine content. What is the probability that the mean nicotine content of a 20-cigarette sample exceeds $1.0\text{ mg}$? **[6 marks]**

2. If the population variance is unknown and sample variance is $s^2 = 0.04\text{ mg}^2$, compute the 95% confidence interval **[3 marks]**.

---

### Generated Practice Sets

**Q 3.1 — 6 marks**
HIGH-VALUE · HARD
[GENERATED — based on PYQ 2025 Q3(a) & 2022 Q3(c)] [Topic: Poisson MGF Derivation]

Let $X$ follow a Poisson distribution with parameter $\lambda$, where $P(X = x) = \frac{e^{-\lambda}\lambda^x}{x!}$ for $x = 0, 1, 2, \ldots$.

1. Derive the moment generating function $M_X(t)$ of $X$.

2. Using $M_X(t)$, determine $E(X)$ and $\text{Var}(X)$.

**Q 3.2 — 6 marks**
HIGH-VALUE · MEDIUM
[GENERATED — based on PYQ 2025 Q7(c) & 2022 Q6(b)] [Topic: One-Sample CI for Proportions]

In a random sample of 400 software deployment pipelines, 64 experienced deployment rollbacks.

1. Construct a 95% confidence interval for the true population proportion $p$ of pipelines experiencing rollbacks.

2. Determine how large a sample must be collected to ensure the margin of error does not exceed $0.02$ with 95% confidence.

**Q 3.3 — 4 marks**
OPTIONAL · MEDIUM
[GENERATED — based on PYQ 2022 Q5(b)] [Topic: Continuous Density Constants]

A continuous random variable $X$ has PDF:

$$f(x) = \begin{cases} kx(2 - x) & 0 \le x \le 2 \\ 0 & \text{otherwise} \end{cases}$$

1. Find the value of $k$.

2. Compute $P(0.5 < X < 1.5)$ and the cumulative distribution function $F(x)$.

---

### Common Traps & Exam Pitfalls

* **Continuity Correction Confusion**: When approximating a discrete binomial with a normal distribution (e.g., $P(11 \le X \le 14)$), forgetting to expand limits by $0.5$ (calculating $P(10.5 \le Y \le 14.5)$) results in inaccurate probability estimates.

* **Shifted Parameter MLE**: When solving for $\theta$ in $f(x) = e^{-(x-\theta)}$ for $x \ge \theta$, the likelihood $L(\theta) = e^{-\sum x_i + n\theta}$ increases monotonically with $\theta$. Setting the derivative $\frac{d\ln L}{d\theta} = n \ne 0$ yields no critical points. The maximum is strictly constrained by the boundary condition $\theta \le \min(X_i)$, making $\hat{\theta}_{\text{MLE}} = X_{(1)}$.

* **Inclusion-Exclusion Overcounting in Coin Runs**: In problems finding $P(A \cup B)$ where $A = \{\text{first 3 flips same}\}$ and $B = \{\text{last 3 flips same}\}$, subtracting the intersection $P(A \cap B)$ requires accounting for overlapping cases: all 5 Heads ($HHHHH$), all 5 Tails ($TTTTT$), as well as alternating runs like $HHHTTT$ if lengths permit. For 5 flips: $A \cap B = \{HHHHH, TTTTT\}$.

* **Degrees of Freedom in Pooled Two-Sample $t$**: When calculating confidence intervals for $\mu_1 - \mu_2$ with $n_1 = 10$ and $n_2 = 10$, the degrees of freedom are $n_1 + n_2 - 2 = 18$. Do not use $n-1 = 9$ or critical values from $Z$.

---

### 7-Day Exam Preparation Plan

```

Day 1: Descriptive Statistics & Proofs

├── Practice: Summation proofs (Q2.1), grouped mean/variance transformations[cite: 1]

├── Core Focus: Calculate Quartiles, IQR, and Outlier fences manually[cite: 1]

└── Target Set: Q2.1, Q2.2, Q2.3[cite: 1]

Day 2: Probability Foundations & Conditioning

├── Practice: Set operations on multi-dice spaces, Independence theorems[cite: 1]

├── Core Focus: Bayes' Theorem multi-partition tables & Coin run sequences[cite: 1]

└── Target Set: Q1.1, Q1.2, Q2.4, Q2.5, Q2.6[cite: 1]

Day 3: Univariate Discrete & Continuous Distributions

├── Practice: Integration of density functions, Normalizing constant $c$[cite: 1]

├── Core Focus: Derivation of Median ($F(m)=0.5$) for Exponential and Normal[cite: 1]

└── Target Set: Q1.5, Q2.7, Q2.9, Q2.10, Q3.3[cite: 1]

Day 4: Moment Generating Functions & Bivariate Distributions

├── Practice: Maclaurin series expansion, $M_X'(0)$ and $M_X''(0)$ derivations[cite: 1]

├── Core Focus: Joint marginal tables, Covariance formulas, Conditional expectation[cite: 1]

└── Target Set: Q1.3, Q1.4, Q2.8, Q3.1[cite: 1]

Day 5: Sampling Distributions & CLT

├── Practice: Sample mean standard error $\sigma/\sqrt{n}$ scaling[cite: 1]

├── Core Focus: Binomial to Normal approximation with $\pm 0.5$ continuity corrections[cite: 1]

└── Target Set: Q2.11, Q2.12[cite: 1]

Day 6: Estimation & Confidence Intervals

├── Practice: Log-likelihood maximization and boundary value analysis[cite: 1]

├── Core Focus: Single $t$ vs $Z$, Pooled two-sample $t$ with equal variance[cite: 1]

└── Target Set: Q1.6, Q1.7, Q2.13, Q2.14, Q3.2[cite: 1]

Day 7: Full Timed Simulation

├── 09:00 - 12:00: Solve 2025 Final Examination (5 chosen questions under timed conditions)[cite: 1]

└── 14:00 - 16:30: Cross-check against Solutions Key, correct weak spots, review distribution properties[cite: 1]

```

---

# SOLUTIONS & STEP-BY-STEP ANSWER KEY

### For MUST-DO Questions

---

#### Solution to Q 1.1 [PYQ 2025 Final · Q1(c)]

Five fair coin tosses: Sample space size $N = 2^5 = 32$.

1. **First three flips are the same**:

* Sequences start with $HHH$ or $TTT$.

* Valid forms: $HHH \_ \; \_$ ($2^2 = 4$ ways) and $TTT \_ \; \_$ ($2^2 = 4$ ways).

* Total favorable outcomes = $4 + 4 = 8$.

* $P(\text{First 3 same}) = \frac{8}{32} = \frac{1}{4} = 0.25$.

2. **Either first three flips are same ($A$) OR last three flips are same ($B$)**:

* By symmetry: $\vert{}A\vert{} = 8$, $\vert{}B\vert{} = 8$.

* Intersection $A \cap B$: First 3 are same AND last 3 are same.

* If first 3 are $H$, flip 3 is $H$. For last 3 to be same, flips 4 and 5 must also be $H \implies (H,H,H,H,H)$.

* If first 3 are $T$, flip 3 is $T$. Similarly, all 5 must be $T \implies (T,T,T,T,T)$.

* Thus, $A \cap B = \{HHHHH, TTTTT\} \implies \vert{}A \cap B\vert{} = 2$.

* Using Inclusion-Exclusion:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{8}{32} + \frac{8}{32} - \frac{2}{32} = \frac{14}{32} = \frac{7}{16} = 0.4375$$

3. **At least two heads in first 3 flips ($C$) AND at least two tails in last 3 flips ($D$)**:

* Break down by flip 3 ($F_3$):

* **Case 1: $F_3 = H$**

* For $C$: Among $(F_1, F_2)$, at least one $H$ is needed $\implies \{HH, HT, TH\}$ (3 outcomes).

* For $D$: Since $F_3 = H$, the last two flips $(F_4, F_5)$ must both be $T \implies \{TT\}$ (1 outcome).

* Total favorable = $3 \times 1 = 3$.

* **Case 2: $F_3 = T$**

* For $C$: Since $F_3 = T$, the first two flips $(F_1, F_2)$ must both be $H \implies \{HH\}$ (1 outcome).

* For $D$: Among $(F_4, F_5)$, at least one $T$ is needed $\implies \{TT, TH, HT\}$ (3 outcomes).

* Total favorable = $1 \times 3 = 3$.

* Total favorable outcomes = $3 + 3 = 6$.

* $P(C \cap D) = \frac{6}{32} = \frac{3}{16} = 0.1875$.

---

#### Solution to Q 1.2 [PYQ 2025 Midterm · Q2]

Let $H, M, L$ denote the events of selecting High, Medium, and Low risk customers:

$$P(H) = 0.20, \quad P(M) = 0.35, \quad P(L) = 1 - (0.20 + 0.35) = 0.45$$

Let $A$ denote the event of having at least one accident:

$$P(A \mid H) = 0.25, \quad P(A \mid M) = 0.16, \quad P(A \mid L) = 0.10$$

1. **Total Probability $P(A)$**:

$$\begin{aligned}    P(A) &= P(H)P(A \mid H) + P(M)P(A \mid M) + P(L)P(A \mid L) \\    &= (0.20)(0.25) + (0.35)(0.16) + (0.45)(0.10) \\    &= 0.050 + 0.056 + 0.045 = 0.151    \end{aligned}$$

2. **Bayes' Rule for $P(L \mid A)$**:

$$P(L \mid A) = \frac{P(L)P(A \mid L)}{P(A)} = \frac{0.045}{0.151} = \frac{45}{151} \approx 0.2980$$

---

#### Solution to Q 1.3 [PYQ 2025 Final · Q3(a, b)]

1. **Derivation of MGF $M_X(t)$**:

$$\begin{aligned}    M_X(t) = E\left[e^{tX}\right] &= \sum_{x=0}^{n} e^{tx} \binom{n}{x} p^x (1-p)^{n-x} \\    &= \sum_{x=0}^{n} \binom{n}{x} (p e^t)^x (1-p)^{n-x}    \end{aligned}$$

By the Binomial Theorem $(a + b)^n = \sum_{x=0}^n \binom{n}{x} a^x b^{n-x}$ where $a = pe^t$ and $b = 1-p$:

$$M_X(t) = (p e^t + 1 - p)^n$$

2. **Expectation and Variance**:

* First derivative:

$$M_X'(t) = n(pe^t + 1 - p)^{n-1}(pe^t)$$

$$E[X] = M_X'(0) = n(p + 1 - p)^{n-1}(p) = n(1)p = np$$

* Second derivative:

$$M_X''(t) = n(n-1)(pe^t + 1 - p)^{n-2}(pe^t)^2 + n(pe^t + 1 - p)^{n-1}(pe^t)$$

$$E[X^2] = M_X''(0) = n(n-1)(1)p^2 + n(1)p = n^2 p^2 - n p^2 + np$$

* Variance:

$$\text{Var}(X) = E[X^2] - (E[X])^2 = (n^2 p^2 - np^2 + np) - (np)^2 = np(1-p)$$

---

#### Solution to Q 1.4 [PYQ 2025 Midterm · Q3]

Given joint PMF $p(x_1, x_2)$:

1. **Marginal Distribution of $X_1$**:

Sum across columns ($X_2 = 1, 2$):

* $P(X_1 = 0) = \frac{1}{8} + \frac{1}{16} = \frac{3}{16} = 0.1875$

* $P(X_1 = 1) = \frac{1}{16} + \frac{1}{16} = \frac{2}{16} = 0.1250$

* $P(X_1 = 2) = \frac{3}{16} + \frac{1}{8} = \frac{5}{16} = 0.3125$

* $P(X_1 = 3) = \frac{1}{8} + \frac{1}{4} = \frac{6}{16} = 0.3750$

*(Check sum: $\frac{3+2+5+6}{16} = 1.0$)*. Plot as a vertical spike graph at $x_1 \in \{0, 1, 2, 3\}$.

2. **Cumulative Distribution $F_{X_1}(x)$**:

$$F_{X_1}(x) = \begin{cases}    0 & x < 0 \\    3/16 = 0.1875 & 0 \le x < 1 \\    5/16 = 0.3125 & 1 \le x < 2 \\    10/16 = 0.6250 & 2 \le x < 3 \\    1.0 & x \ge 3    \end{cases}$$

Plot as a right-continuous step function with closed circles at step jumps.

3. **$\text{Cov}(X_1, X_2)$**:

* Marginal of $X_2$:

* $P(X_2 = 1) = \frac{1}{8} + \frac{1}{16} + \frac{3}{16} + \frac{1}{8} = \frac{8}{16} = 0.5$

* $P(X_2 = 2) = \frac{1}{16} + \frac{1}{16} + \frac{1}{8} + \frac{1}{4} = \frac{8}{16} = 0.5$

* $E[X_2] = 1(0.5) + 2(0.5) = 1.5$

* $E[X_1] = 0\left(\frac{3}{16}\right) + 1\left(\frac{2}{16}\right) + 2\left(\frac{5}{16}\right) + 3\left(\frac{6}{16}\right) = \frac{2 + 10 + 18}{16} = \frac{30}{16} = 1.875$

* $E[X_1 X_2] = \sum x_1 x_2 p(x_1, x_2)$:

$$\begin{aligned}      E[X_1 X_2] &= (1)(1)\left(\frac{1}{16}\right) + (1)(2)\left(\frac{1}{16}\right) + (2)(1)\left(\frac{3}{16}\right) + (2)(2)\left(\frac{1}{8}\right) \\      &\quad + (3)(1)\left(\frac{1}{8}\right) + (3)(2)\left(\frac{1}{4}\right) \\      &= \frac{1}{16} + \frac{2}{16} + \frac{6}{16} + \frac{8}{16} + \frac{6}{16} + \frac{24}{16} = \frac{47}{16} = 2.9375      \end{aligned}$$

* $\text{Cov}(X_1, X_2) = E[X_1 X_2] - E[X_1]E[X_2] = 2.9375 - (1.875)(1.5) = 2.9375 - 2.8125 = 0.125$

4. **Conditional Expectation $E[X_1 \mid X_2 = 1]$**:

$P(X_1 = x_1 \mid X_2 = 1) = \frac{p(x_1, 1)}{P(X_2 = 1)} = \frac{p(x_1, 1)}{0.5} = 2 p(x_1, 1)$:

* $P(0 \mid 1) = 2(1/8) = 1/4$

* $P(1 \mid 1) = 2(1/16) = 1/8$

* $P(2 \mid 1) = 2(3/16) = 3/8$

* $P(3 \mid 1) = 2(1/8) = 1/4$

$$E[X_1 \mid X_2 = 1] = 0\left(\frac{1}{4}\right) + 1\left(\frac{1}{8}\right) + 2\left(\frac{3}{8}\right) + 3\left(\frac{1}{4}\right) = \frac{1 + 6 + 6}{8} = \frac{13}{8} = 1.625$$

---

#### Solution to Q 1.5 [PYQ 2022 Final · Q5(a)]

1. **Value of $c$**:

$$\int_{-1}^{1} c(1 - x^2)\, dx = 1 \implies 2c \int_{0}^{1} (1 - x^2)\, dx = 1$$

$$2c \left[ x - \frac{x^3}{3} \right]_0^1 = 2c \left(\frac{2}{3}\right) = \frac{4c}{3} = 1 \implies c = \frac{3}{4}$$

2. **$F(x)$, $E(X)$, and $\text{Var}(X)$**:

* For $-1 \le x \le 1$:

$$F(x) = \int_{-1}^{x} \frac{3}{4}(1 - t^2)\, dt = \frac{3}{4} \left[ t - \frac{t^3}{3} \right]_{-1}^x = \frac{3}{4} \left( x - \frac{x^3}{3} - \left(-1 + \frac{1}{3}\right) \right) = \frac{3}{4}x - \frac{x^3}{4} + \frac{1}{2}$$

Complete specification:

$$F(x) = \begin{cases} 0 & x < -1 \\ \frac{1}{2} + \frac{3x - x^3}{4} & -1 \le x \le 1 \\ 1 & x > 1 \end{cases}$$

* $E[X] = \int_{-1}^{1} x \cdot \frac{3}{4}(1 - x^2)\, dx = 0$ (integrand is an odd function over symmetric limits).

* Variance:

$$\begin{aligned}      \text{Var}(X) = E[X^2] &= \int_{-1}^{1} x^2 \cdot \frac{3}{4}(1 - x^2)\, dx = 2 \cdot \frac{3}{4} \int_{0}^{1} (x^2 - x^4)\, dx \\      &= \frac{3}{2} \left[ \frac{x^3}{3} - \frac{x^5}{5} \right]_0^1 = \frac{3}{2} \left(\frac{2}{15}\right) = \frac{1}{5} = 0.2      \end{aligned}$$

---

#### Solution to Q 1.6 [PYQ 2025 Final · Q7(b)]

Given $f(x) = e^{-(x-\theta)} \mathbf{1}_{\{x \ge \theta\}}$.

For a random sample $X_1, \ldots, X_n$:

$$L(\theta) = \prod_{i=1}^n e^{-(X_i - \theta)} \mathbf{1}_{\{X_i \ge \theta\}} = e^{-\sum_{i=1}^n X_i + n\theta} \prod_{i=1}^n \mathbf{1}_{\{X_i \ge \theta\}}$$

Note that $\prod_{i=1}^n \mathbf{1}_{\{X_i \ge \theta\}} = 1$ if and only if $\min(X_1, \ldots, X_n) \ge \theta$, denoted as $X_{(1)} \ge \theta$.

To maximize $L(\theta)$:

* The function $e^{n\theta}$ is strictly increasing with respect to $\theta$.

* However, $\theta$ is bounded from above by the condition $\theta \le X_{(1)}$.

* Since $L(\theta) = 0$ for $\theta > X_{(1)}$ and strictly increases for $\theta \le X_{(1)}$, the likelihood reaches its absolute maximum at the upper boundary:

$$\hat{\theta}_{\text{MLE}} = X_{(1)} = \min(X_1, X_2, \ldots, X_n)$$

---

#### Solution to Q 1.7 [PYQ 2025 Final · Q6(b)]

Data calculations:

* **Type I ($n_1 = 10$)**: Values: $481, 506, 527, 661, 501, 572, 561, 501, 487, 524$

$$\sum x_1 = 5321 \implies \bar{x}_1 = 532.1$$

$$\sum x_1^2 = 2857443 \implies s_1^2 = \frac{2857443 - \frac{5321^2}{10}}{9} = \frac{26002.9}{9} \approx 2889.21$$

* **Type II ($n_2 = 10$)**: Values: $526, 511, 556, 542, 491, 537, 582, 605, 558, 578$

$$\sum x_2 = 5486 \implies \bar{x}_2 = 548.6$$

$$\sum x_2^2 = 3019808 \implies s_2^2 = \frac{3019808 - \frac{5486^2}{10}}{9} = \frac{10088.4}{9} \approx 1120.93$$

1. **Pooled Variance ($s_p^2$)**:

$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2} = \frac{26002.9 + 10088.4}{18} = \frac{36091.3}{18} \approx 2005.07$$

$$s_p = \sqrt{2005.07} \approx 44.778$$

2. **Standard Error**:

$$SE = s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}} = 44.778 \sqrt{\frac{1}{10} + \frac{1}{10}} = 44.778 \sqrt{0.2} \approx 20.025$$

3. **Critical Value**:

Degrees of freedom $\nu = 10 + 10 - 2 = 18$. For a 95% confidence interval ($\alpha = 0.05 \implies \alpha/2 = 0.025$), from Table A3:

$$t_{0.025, 18} = 2.101$$

4. **Confidence Interval**:

$$(\bar{x}_1 - \bar{x}_2) \pm t_{0.025, 18} \cdot SE$$

$$(532.1 - 548.6) \pm 2.101(20.025) \implies -16.5 \pm 42.073 \implies [-58.57\text{ s}, \; 25.57\text{ s}]$$

5. **Interpretation**:

We are 95% confident that the true difference between the mean burning times of Type I and Type II smoke pots lies within $-58.57$ and $+25.57$ seconds. Because the interval contains $0$, there is no statistically significant evidence at the 5% significance level to conclude that the mean burning times of the two types differ.
