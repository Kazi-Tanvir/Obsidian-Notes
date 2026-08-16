# Chapter 16: Machine learning and big data

## 16.1 Introduction

The proliferation of data along with the ability to quickly compute has in recent years led to a variety of techniques for estimating probabilities that depend less on assuming a particular model for the data and more on utilizing large amounts of data. Such techniques are often referred to as being *machine learning*.

This chapter introduces techniques for estimating probabilities with large datasets:
- **Naive Bayes approach** (Sections 16.3 and 16.3.1)
- **Nearest neighbor rules** (Sections 16.4 and 16.6.1)
- **Model evaluation and loss functions** (Section 16.5)
- **Logistic regression for quantitative inputs** (Section 16.6.2)
- **Multi-armed bandit problems** (Section 16.7)

## 16.2 Late flight probabilities

Consider estimating the probability that a flight from California to NYC is late ($\ge 30$ min delay).
Each flight is characterized by a vector $(X_1, \dots, X_7)$:
- $X_1$: Airline (1 = American, 2 = Delta, 3 = United, 4 = Jet Blue)
- $X_2$: Origin (1 = LAX, 2 = SFO, 3 = SAN, 4 = OAK)
- $X_3$: Destination (1 = JFK, 2 = LGA, 3 = EWR)
- $X_4$: Day of week ($1 = \text{Mon}, \dots, 7 = \text{Sun}$)
- $X_5$: Departure time ($1 = \text{early morning}, \dots, 6 = \text{late evening}$)
- $X_6$: Plane size ($1 = \text{small}, 2 = \text{medium}, 3 = \text{large}$)
- $X_7$: Weather ($1 = \text{above average}, 2 = \text{average}, 3 = \text{stormy}$)

Total combinations: $4 \times 4 \times 3 \times 7 \times 6 \times 3 \times 3 = 18,144$.

## 16.3 The naive Bayes approach

Using Bayes' theorem:

$$P(L \mid X_1 = x_1, \dots, X_k = x_k) = \frac{P(L) P(X_1 = x_1, \dots, X_k = x_k \mid L)}{P(X_1 = x_1, \dots, X_k = x_k)}$$

Assuming independence of features given the outcome:

$$P(L \mid X_1 = x_1, \dots, X_k = x_k) \approx \frac{f(L) f_1(x_1 \mid L) \dots f_k(x_k \mid L)}{f_1(x_1) \dots f_k(x_k)}$$

**Table 16.1: Historical Flight Data ($N = 79$ flights, 25 late)**

| Flight vector | Number of such flights | Number late | Flight vector | Number of such flights | Number late |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (1,1,1,1) | 2 | 1 | (2,1,1,1) | 4 | 2 |
| (1,1,1,2) | 2 | 0 | (2,1,1,2) | 3 | 1 |
| (1,1,2,1) | 2 | 0 | (2,1,2,1) | 5 | 2 |
| (1,1,2,2) | 1 | 0 | (2,1,2,2) | 4 | 1 |
| (1,1,3,1) | 3 | 1 | (2,1,3,1) | 3 | 1 |
| (1,1,3,2) | 3 | 0 | (2,1,3,2) | 2 | 0 |
| (1,2,1,1) | 4 | 1 | (2,2,1,1) | 3 | 1 |
| (1,2,1,2) | 3 | 1 | (2,2,1,2) | 4 | 1 |
| (1,2,2,1) | 5 | 2 | (2,2,2,1) | 5 | 2 |
| (1,2,2,2) | 3 | 1 | (2,2,2,2) | 5 | 3 |
| (1,2,3,1) | 3 | 1 | (2,2,3,1) | 3 | 1 |
| (1,2,3,2) | 4 | 2 | (2,2,3,2) | 3 | 0 |

**Example 16.3.a.** Naive Bayes estimate for flight $(2, 1, 2, 2)$:

$$\hat{P}(L \mid 2, 1, 2, 2) = \frac{\frac{25}{79} \times \frac{15}{25} \times \frac{9}{25} \times \frac{12}{25} \times \frac{10}{25}}{\frac{44}{79} \times \frac{34}{79} \times \frac{30}{79} \times \frac{37}{79}} = \frac{25 \cdot 15 \cdot 9 \cdot 12 \cdot 10 \cdot 79^4}{79 \cdot 25^4 \cdot 44 \cdot 34 \cdot 30 \cdot 37} = .3078 \quad \blacksquare$$

### 16.3.1 A variation of naive Bayes approach (Conditional Independence)

Conditioning on disease status $D$ and $D^c$:

$$P(X_1 = x_1, \dots, X_n = x_n) = P(X_1 = x_1, \dots, X_n = x_n \mid D)P(D) + P(X_1 = x_1, \dots, X_n = x_n \mid D^c)P(D^c)$$

**Table 16.2: Historical Patient Test Data ($n = 68$)**

| Characterizing vector | Number of patients | Number with condition | Number without condition |
| :--- | :--- | :--- | :--- |
| (1,1,1) | 4 | 1 | 3 |
| (1,1,2) | 3 | 0 | 3 |
| (1,1,3) | 5 | 1 | 4 |
| (1,2,1) | 6 | 1 | 5 |
| (1,2,2) | 7 | 2 | 5 |
| (1,2,3) | 5 | 3 | 2 |
| (2,1,1) | 6 | 3 | 3 |
| (2,1,2) | 7 | 2 | 5 |
| (2,1,3) | 5 | 1 | 4 |
| (2,2,1) | 6 | 2 | 4 |
| (2,2,2) | 9 | 4 | 5 |
| (2,2,3) | 5 | 1 | 4 |

**Example 16.3.b.** Estimating $P(C \mid (2, 1, 2)) = .2963$.

## 16.4 Distance-based estimators. The $k$-nearest neighbors rule

Distance between qualitative vectors: $d(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^k I\{x_i \neq y_i\}$.

**Example 16.4.a.** For $(2, 1, 2, 2)$, taking all historical flights within distance $\le 1$: 7 late out of 20 $\implies \hat{p} = 7/20 = .35$.

### 16.4.1 A distance-weighted method
Weight for $j$th historical point: $w_j = \frac{1}{1 + d_j}$.
Estimate:

$$\hat{P}(L) = \frac{\sum_{j=1}^N I_j w_j}{\sum_{j=1}^N w_j} \tag{16.4.1}$$

**Example 16.4.b.** Distance-weighted estimate for $(2, 1, 2, 2) = .3117$.

### 16.4.2 Component-weighted distances
Let $a_i = |p_L(x_i) - p_L(\bar{x}_i)|$. Distance: $d(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^k a_i I\{x_i \neq y_i\}$.

## 16.5 Assessing the approaches

Test set evaluation using Brier score / quadratic loss:

$$L = \begin{cases} (1 - p_i)^2 & \text{if } l_i = 1 \\ p_i^2 & \text{if } l_i = 0 \end{cases}$$

Expected loss when true probability is $\alpha$: $E[L] = \alpha + (p - \alpha)^2 - \alpha^2$, minimized uniquely at $p = \alpha$.
Baseline predictor (unconditional mean $\beta$): average loss $= \beta(1 - \beta)$.

**Example 16.5.a.** If true probabilities are $\text{Uniform}(0, 1)$, baseline loss is $1/4 = .25$, optimal loss is $\int_0^1 (p - p^2) \, dp = 1/6 \approx .1667$.

## 16.6 When characterizing vectors are quantitative

### 16.6.1 Nearest neighbor rules
Standardize coordinates: $\tilde{x}_i = \frac{x_i - m_i}{s_i}$.
Distance: Euclidean distance $\sqrt{\sum_{i=1}^n (\tilde{x}_i - \tilde{y}_i)^2}$.
Weighted $k$-NN with geometric weights: $\frac{1 - \beta}{1 - \beta^N} \sum_{j=1}^N \beta^{j-1} I_j$.

### 16.6.2 Logistic regression
$$p(x_1, \dots, x_n) = \frac{e^{b_0 + \sum_{i=1}^n b_i x_i}}{1 + e^{b_0 + \sum_{i=1}^n b_i x_i}}$$

Fitted via R `glm(y ~ v1 + v2 + v3 + v4 + v5, family = binomial)`.

## 16.7 Choosing the best probability: a bandit problem

For two drugs with unknown success rates $p_1, p_2$:
- Use each drug once.
- After $n_i$ uses and $s_i$ successes ($i = 1, 2$):
  $$f_1 = \frac{s_1 + 1}{n_1 + 2}, \qquad f_2 = \frac{s_2 + 1}{n_2 + 2}$$
  $$r = \frac{f_1 - f_2}{\sqrt{\frac{f_1(1 - f_1)}{n_1} + \frac{f_2(1 - f_2)}{n_2}}}$$
  $$x = \Phi(r)$$
- Prescribe drug 1 with probability $x$, and drug 2 with probability $1 - x$.

In R:

```r
> f1 = (s1 + 1)/(n1 + 2)
> f2 = (s2 + 1)/(n2 + 2)
> r = (f1 - f2)/sqrt(f1 * (1 - f1)/n1 + f2 * (1 - f2)/n2)
> x = pnorm(r)
> runif(1) < x  # TRUE -> use drug 1, FALSE -> use drug 2
```

---

## Problems

1. Auto insurance policyholders characterized by $(x_1, x_2)$ (Sex: $1=\text{male}, 2=\text{female}$; Age: $1=<25, 2=25-40, 3=40-60, 4=60-70, 5=>70$).

**Table 16.4: Historical Data**

| Vector $(x_1, x_2)$ | Number with Vector | Number having an accident |
| :--- | :--- | :--- |
| (1,1) | 240 | 9 |
| (1,2) | 1050 | 18 |
| (1,3) | 1400 | 20 |
| (1,4) | 457 | 15 |
| (1,5) | 145 | 12 |
| (2,1) | 226 | 5 |
| (2,2) | 940 | 12 |
| (2,3) | 1420 | 14 |
| (2,4) | 420 | 11 |
| (2,5) | 142 | 13 |

   a. Naive Bayes estimate for 36-year-old woman $(2, 2)$.
   b. Modified naive Bayes estimate for 36-year-old woman.
   c. Naive Bayes estimate for 26-year-old man $(1, 2)$.
   d. Modified naive Bayes estimate for 24-year-old man $(1, 1)$.

2. Weighted distance approach on Problem 1 data for:
   a. 36-year-old woman;
   b. 26-year-old man.

3. Loss function assessment of naive Bayes vs weighted distance on Problem 1 cases.

4. Total loss comparison across all 6440 data points in Table 16.4.

5. Log loss function: Show that $E[-\log(p)]$ is minimized when $p = \alpha$.

6. Comparison study of logistic regression vs nearest neighbor.

7. Multi-armed bandit problem: Drug 1 ($n_1 = 55, s_1 = 36$), Drug 2 ($n_2 = 22, s_2 = 12$). Probability of choosing drug 1 next.
