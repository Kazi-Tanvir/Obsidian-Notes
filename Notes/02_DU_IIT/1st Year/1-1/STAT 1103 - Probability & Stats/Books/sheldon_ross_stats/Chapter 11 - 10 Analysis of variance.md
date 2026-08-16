# Chapter 10: Analysis of variance

## 10.1 Introduction

A large company is considering purchasing, in quantity, one of four different computer packages designed to teach a new programming language. Some influential people within this company have claimed that these packages are basically interchangeable in that the one chosen will have little effect on the final competence of its user. To test this hypothesis the company has decided to choose 160 of its engineers, and divide them into 4 groups of size 40. Each member in group $i$ will then be given teaching package $i, i = 1, 2, 3, 4$, to learn the new language. When all the engineers complete their study, a comprehensive exam will be given. The company then wants to use the results of this examination to determine whether the computer teaching packages are really interchangeable or not. How can they do this?

Before answering this question, let us note that we clearly desire to be able to conclude that the teaching packages are indeed interchangeable when the average test scores in all the groups are similar and to conclude that the packages are essentially different when there is a large variation among these average test scores. However, to be able to reach such a conclusion, the method of division of the 160 engineers into 4 groups is of vital importance (random assignment).

If we let $X_{ij}, i = 1, \dots, 4, j = 1, \dots, 40$, denote the test score of the $j$th engineer in group $i$, a reasonable model might be to suppose that the $X_{ij}$ are independent random variables with $X_{ij} \sim N(\mu_i, \sigma^2)$. The hypothesis that the teaching packages are interchangeable is then equivalent to the hypothesis that $\mu_1 = \mu_2 = \mu_3 = \mu_4$.

## 10.2 An overview

In all of the models considered in this chapter, we assume that the data are normally distributed with the same (although unknown) variance $\sigma^2$. The analysis of variance approach for testing a null hypothesis $H_0$ concerning multiple parameters relating to the population means is based on deriving two estimators of the common variance $\sigma^2$. The first estimator is a valid estimator of $\sigma^2$ whether the null hypothesis is true or not, while the second one is a valid estimator only when $H_0$ is true. In addition, when $H_0$ is not true this latter estimator will tend to exceed $\sigma^2$. The test will be to compare the values of these two estimators, and to reject $H_0$ when the ratio of the second estimator to the first one is sufficiently large.

Suppose that $X_1, \dots, X_N$ are independent normal random variables having possibly different means but a common variance $\sigma^2$, and let $\mu_i = E[X_i], i = 1, \dots, N$. Then

$$\sum_{i=1}^N Z_i^2 = \sum_{i=1}^N (X_i - \mu_i)^2 / \sigma^2 \sim \chi_N^2 \tag{10.2.1}$$

If each $\mu_i$ can be expressed as a linear function of a fixed set of $k$ unknown parameters, and $\hat{\mu}_i$ is the resulting estimator of $\mu_i$, then

$$\sum_{i=1}^N (X_i - \hat{\mu}_i)^2 / \sigma^2 \sim \chi_{N-k}^2$$

## 10.3 One-way analysis of variance

Consider $m$ independent samples, each of size $n$, where $X_{ij} \sim N(\mu_i, \sigma^2), i = 1, \dots, m, j = 1, \dots, n$. We test:

$$H_0 : \mu_1 = \mu_2 = \dots = \mu_m \quad \text{versus} \quad H_1 : \text{not all the means are equal}$$

Let $X_{i.} = \sum_{j=1}^n X_{ij}/n$ and $X_{..} = \sum_{i=1}^m \sum_{j=1}^n X_{ij}/(nm) = \sum_{i=1}^m X_{i.}/m$.

### Within Samples Sum of Squares
$$SS_W = \sum_{i=1}^m \sum_{j=1}^n (X_{ij} - X_{i.})^2$$

$$\frac{SS_W}{\sigma^2} \sim \chi_{nm-m}^2 \implies E\left[\frac{SS_W}{nm - m}\right] = \sigma^2$$

### Between Samples Sum of Squares
$$SS_b = n \sum_{i=1}^m (X_{i.} - X_{..})^2$$

When $H_0$ is true:

$$\frac{SS_b}{\sigma^2} \sim \chi_{m-1}^2 \implies E\left[\frac{SS_b}{m - 1}\right] = \sigma^2 \tag{10.3.4}$$

### Test Statistic
$$TS = \frac{SS_b / (m - 1)}{SS_W / (nm - m)} \sim F_{m-1, nm-m} \quad \text{under } H_0$$

Reject $H_0$ at level $\alpha$ if $TS > F_{\alpha, m-1, nm-m}$.

### Sum of Squares Identity
$$\sum_{i=1}^m \sum_{j=1}^n X_{ij}^2 = nm X_{..}^2 + SS_b + SS_W$$

**Example 10.3.a.** Three brands of gasoline (5 motors each):
- $m = 3, n = 5 \implies X_{1.} = 20.6, X_{2.} = 15.6, X_{3.} = 33.6, X_{..} = 23.2667$.
- $SS_b = 863.3335, SS_W = 1991.5785$.
- $TS = \frac{863.3335/2}{1991.5785/12} = 2.60$.
- $p\text{-value} = 1 - \text{pf}(2.60, 2, 12) = 0.1153 > .05 \implies$ Do not reject $H_0$. $\blacksquare$

**Table 10.1: One-Way ANOVA Table**

| Source of Variation | Sum of Squares | Degrees of Freedom | Value of Test Statistic |
| :--- | :--- | :--- | :--- |
| **Between samples** | $SS_b = n \sum_{i=1}^m (X_{i.} - X_{..})^2$ | $m - 1$ | $TS = \frac{SS_b/(m-1)}{SS_W/(nm-m)}$ |
| **Within samples** | $SS_W = \sum_{i=1}^m \sum_{j=1}^n (X_{ij} - X_{i.})^2$ | $nm - m$ | |

### 10.3.1 Using R to do the computations

```r
> G = matrix(c(220, 244, 252, 251, 235, 272, 226, 232, 250, 246, 242, 238, 260, 225, 256), 3, 5)
> rm = rowMeans(G)
> mm = mean(G)
> d = rm - mm
> SSb = 5 * sum(d^2)
> SSw = sum(G^2) - 3 * 5 * mm^2 - SSb
> TS = (SSb/2)/(SSw/12)
> 1 - pf(TS, 2, 12)
[1] 0.1152489
```

### 10.3.2 Multiple comparisons of sample means (T-method / Tukey HSD)

With probability $1 - \alpha$, for every $i \neq j$:

$$X_{i.} - X_{j.} - W < \mu_i - \mu_j < X_{i.} - X_{j.} + W$$

where

$$W = \frac{1}{\sqrt{n}} C(m, nm - m, \alpha) \sqrt{\frac{SS_W}{nm - m}}$$

**Example 10.3.b.** High school GPAs ($m = 3, n = 4$):
- $SS_W/9 = .0431, p\text{-value} = .0046 \implies$ Reject equal means.
- $W = \frac{1}{\sqrt{4}}(3.95)\sqrt{.0431} = .410$.
- CIs: $\mu_1 - \mu_2 \in (-.410, .410)$, $\mu_1 - \mu_3 \in (.165, .985)$, $\mu_2 - \mu_3 \in (.165, .985)$.

### 10.3.3 One-way analysis of variance with unequal sample sizes

For sample sizes $n_1, \dots, n_m$:

$$SS_W = \sum_{i=1}^m \sum_{j=1}^{n_i} (X_{ij} - X_{i.})^2, \qquad \text{df} = \sum_{i=1}^m n_i - m$$
$$SS_b = \sum_{i=1}^m n_i (X_{i.} - X_{..})^2, \qquad \text{df} = m - 1$$

$$TS = \frac{SS_b / (m - 1)}{SS_W / (\sum_{i=1}^m n_i - m)} \sim F_{m-1, \; \sum n_i - m}$$

## 10.4 Two-factor analysis of variance: introduction and parameter estimation

Model: $X_{ij} \sim N(\mu + \alpha_i + \beta_j, \sigma^2), i = 1, \dots, m, j = 1, \dots, n$ with $\sum_{i=1}^m \alpha_i = \sum_{j=1}^n \beta_j = 0$.

Estimators:
- Grand mean: $\hat{\mu} = X_{..}$
- Row effect: $\hat{\alpha}_i = X_{i.} - X_{..}$
- Column effect: $\hat{\beta}_j = X_{.j} - X_{..}$

**Example 10.4.a / 10.4.b.** Reading test scores: $\hat{\mu} = 74, \hat{\alpha} = (-1.2, 1, -0.8, 1), \hat{\beta} = (2.5, -4, -11.75, -1, 14.25)$.

## 10.5 Two-factor analysis of variance: testing hypotheses

- Error sum of squares: $SS_e = \sum_{i=1}^m \sum_{j=1}^n (X_{ij} - X_{i.} - X_{.j} + X_{..})^2, \text{df} = (n - 1)(m - 1)$
- Row sum of squares: $SS_r = n \sum_{i=1}^m (X_{i.} - X_{..})^2, \text{df} = m - 1$
- Column sum of squares: $SS_c = m \sum_{j=1}^n (X_{.j} - X_{..})^2, \text{df} = n - 1$

**Table 10.2: Two-Factor ANOVA ($N = (n - 1)(m - 1)$)**

| Sum of Squares | Degrees of Freedom | Null Hypothesis | Test Statistic | Significance Level $\alpha$ Test | $p$-Value if $\text{TS} = v$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Row** $SS_r$ | $m - 1$ | All $\alpha_i = 0$ | $\frac{SS_r/(m-1)}{SS_e/N}$ | Reject if $TS \ge F_{\alpha, m-1, N}$ | $P\{F_{m-1, N} \ge v\}$ |
| **Column** $SS_c$ | $n - 1$ | All $\beta_j = 0$ | $\frac{SS_c/(n-1)}{SS_e/N}$ | Reject if $TS \ge F_{\alpha, n-1, N}$ | $P\{F_{n-1, N} \ge v\}$ |
| **Error** $SS_e$ | $N = (n-1)(m-1)$ | | | | |

**Example 10.5.a.** Macroinvertebrates at 6 stations over 8 years:
- Year effect: $TS = 3.602, p\text{-value} = 0.005$ (reject $H_0$).
- Station effect: $TS = 22.67, p\text{-value} = 4.41 \times 10^{-10}$ (reject $H_0$).

## 10.6 Two-way analysis of variance with interaction

Model with $l$ replicates per cell:

$$X_{ijk} \sim N(\mu + \alpha_i + \beta_j + \gamma_{ij}, \sigma^2), \quad i = 1, \dots, m, \; j = 1, \dots, n, \; k = 1, \dots, l$$

where $\sum \alpha_i = \sum \beta_j = \sum_i \gamma_{ij} = \sum_j \gamma_{ij} = 0$.

Estimators:
- $\hat{\mu} = X_{...}$
- $\hat{\alpha}_i = X_{i..} - X_{...}$
- $\hat{\beta}_j = X_{.j.} - X_{...}$
- $\hat{\gamma}_{ij} = X_{ij.} - X_{i..} - X_{.j.} + X_{...}$

Sums of squares:
- $SS_e = \sum_{k=1}^l \sum_{j=1}^n \sum_{i=1}^m (X_{ijk} - X_{ij.})^2, \quad \text{df} = nm(l - 1)$
- $SS_r = nl \sum_{i=1}^m (X_{i..} - X_{...})^2, \quad \text{df} = m - 1$
- $SS_c = ml \sum_{j=1}^n (X_{.j.} - X_{...})^2, \quad \text{df} = n - 1$
- $SS_{int} = l \sum_{j=1}^n \sum_{i=1}^m (X_{ij.} - X_{i..} - X_{.j.} + X_{...})^2, \quad \text{df} = (n - 1)(m - 1)$

**Table 10.3: Two-way ANOVA with $l$ Observations per Cell ($N = nm(l - 1)$)**

| Source of Variation | Degrees of Freedom | Sum of Squares | $F$-Statistic | Level $\alpha$ Test | $p$-Value if $F = v$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Row** | $m - 1$ | $SS_r$ | $F_r = \frac{SS_r/(m-1)}{SS_e/N}$ | Reject $H_0^r$ if $F_r > F_{\alpha, m-1, N}$ | $P\{F_{m-1, N} > v\}$ |
| **Column** | $n - 1$ | $SS_c$ | $F_c = \frac{SS_c/(n-1)}{SS_e/N}$ | Reject $H_0^c$ if $F_c > F_{\alpha, n-1, N}$ | $P\{F_{n-1, N} > v\}$ |
| **Interaction** | $(n - 1)(m - 1)$ | $SS_{int}$ | $F_{int} = \frac{SS_{int}/((n-1)(m-1))}{SS_e/N}$ | Reject $H_0^{int}$ if $F_{int} > F_{\alpha, (n-1)(m-1), N}$ | $P\{F_{(n-1)(m-1), N} > v\}$ |
| **Error** | $N = nm(l - 1)$ | $SS_e$ | | | |

**Example 10.6.a.** Generator lifetime (3 materials, 2 temperatures, 4 replicates):
- Interaction: $F_{int} = 0.645, p\text{-value} = 0.536$ (no interaction).
- Material effect: $F_r = 2.480, p\text{-value} = 0.112$ (no material effect at 10%).
- Temperature effect: $F_c = 69.63, p\text{-value} = 1.34 \times 10^{-7}$ (significant temperature effect).

---

## Problems

1. Chemical purification with 3 resins (5 batches each):
   - Resin I: .046, .025, .014, .017, .043
   - Resin II: .038, .035, .031, .022, .012
   - Resin III: .031, .042, .020, .018, .039
   Test if there is no difference in efficiency.

2. Oscilloscope filters (20 readings each for Filter 1, Filter 2, Filter 3). Test at $\alpha = .05$.

3. Explain why we cannot efficiently test $H_0 : \mu_1 = \dots = \mu_m$ by running separate $t$-tests on all $\binom{m}{2}$ pairs.

4. 3 ovens heating temperatures (5 heats each):
   - Oven 1: 492.4, 493.6, 498.5, 488.6, 494
   - Oven 2: 488.5, 485.3, 482, 479.4, 478
   - Oven 3: 502.1, 492, 497.5, 495.3, 486.7
   Test if ovens operate at the same temperature.

5. Four chemical procedures for magnesium content (4 replicates each).

6. Weight loss on two diets ($n = 10$ each).

7. Polymer toxic waste removal at 3 temperatures (7 attempts each).

8. Show $SS_W = (n - 1)\sum_{i=1}^m S_i^2$.

9. Rat diet age at death (3 diets, $n = 10$ each):
   - Very Low Calorie: Mean 22.4, Var 24.0
   - Moderate Calorie: Mean 16.8, Var 23.2
   - High Calorie: Mean 13.7, Var 17.1

10. Plasma bradykininogen levels in Hodgkin's disease (Normal, Active, Inactive, $n = 13$ each).

11. Trunk flexor muscle strength of 75 girls (5 age groups of 15 each).

12. Inhaled steroids recovery times (3 steroids, $n = 12$ each). One-way ANOVA and Tukey CIs.

13. Meat brand fat content (3 brands, 5 servings each).

14. Bicyclist speeds with vitamin, fiber, and control groups ($n = 5$ each).

15. Test if 3 independent samples come from the same normal distribution (unequal sample sizes: $n_1 = 5, n_2 = 5, n_3 = 3$).

16. Show $\bar{x}_{..} = \sum \bar{x}_{i.}/m = \sum \bar{x}_{.j}/n$.

17. Summation properties for $x_{ij} = i + j^2$.

18. Summation properties for $x_{ij} = a_i + b_j$.

19. Pyrethrin content: 3 storage conditions $\times$ 4 extraction methods (Table 10.4).

20. Death rates per 10,000 adults in 4 seasons across 5 years (1982–1986).

21. Two-way ANOVA analysis for Problem 19.

22. 4 detergents tested in 3 washing machines.

23. 3 gasolines with 3 additives (Table 10.5).

24. Diet data stratified by gender (2 diets $\times$ 2 genders, 5 replicates per cell).

25. Laminated beam breaking strength: 3 glues $\times$ 3 wood types (5 replicates per cell).

26. Blood drug concentration: 4 age groups $\times$ 2 genders (5 replicates per cell).

27. Gasoline and additive with interaction (3 gasolines $\times$ 3 additives $\times$ 4 replicates).

28. Oxygen treatment and memory retention in elderly: 4 treatment lengths $\times$ 2 genders (5 replicates per cell).

29. Rat platelet production: Altitude vs Spleen removal (2 $\times$ 2 design, 8 replicates per cell).

30. Uniqueness of two-factor ANOVA parametrization $\sum \alpha_i = \sum \beta_j = 0$.
