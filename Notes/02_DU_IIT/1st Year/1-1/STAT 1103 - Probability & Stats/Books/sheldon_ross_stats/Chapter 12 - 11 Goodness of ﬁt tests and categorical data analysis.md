# Chapter 11: Goodness of fit tests and categorical data analysis

## 11.1 Introduction

We are often interested in determining whether or not a particular probabilistic model is appropriate for a given random phenomenon. This determination often reduces to testing whether a given random sample comes from some specified, or partially specified, probability distribution. For example, we may a priori feel that the number of industrial accidents occurring daily at a particular plant should constitute a random sample from a Poisson distribution. Statistical tests that determine whether a given probabilistic mechanism is appropriate are called *goodness of fit tests*.

## 11.2 Goodness of fit tests when all parameters are specified

Suppose that $n$ independent random variables $Y_1, \dots, Y_n$, each taking on one of the values $1, 2, \dots, k$, are observed. We test:

$$H_0 : P\{Y = i\} = p_i, \quad i = 1, \dots, k$$
$$\text{versus} \quad H_1 : P\{Y = i\} \neq p_i \text{ for some } i = 1, \dots, k$$

Let $X_i$ denote the number of $Y_j$ that equal $i$. Under $H_0$, $E[X_i] = np_i$. The test statistic is:

$$T = \sum_{i=1}^k \frac{(X_i - np_i)^2}{np_i} \tag{11.2.1}$$

Computationally simpler formula:

$$T = \sum_{i=1}^k \frac{X_i^2}{np_i} - n \tag{11.2.2}$$

For large $n$, under $H_0$, $T$ has approximately a chi-square distribution with $k - 1$ degrees of freedom:

$$T \sim \chi_{k-1}^2$$

Reject $H_0$ at significance level $\alpha$ if $T \ge \chi_{\alpha, k-1}^2$, or if $p\text{-value} = P\{\chi_{k-1}^2 \ge t\} \le \alpha$.

Rule of thumb: $np_i \ge 1$ for all $i$ and at least $80\%$ of $np_i \ge 5$.

**Example 11.2.a (Birthdays and Death Days).** Sample of $n = 1251$ individuals across 12 months: $np_i = 104.25$.
- 12 categories: $T = 17.192, \text{df} = 11 \implies p\text{-value} = 0.1023$.
- 4 categories: $T = 14.775, \text{df} = 3 \implies p\text{-value} = 0.00202$ (reject $H_0$).

**Example 11.2.b.** Fluorescent bulb quality levels: $n = 30$, counts $c(3, 6, 9, 7, 5)$, probabilities $c(.15, .25, .35, .20, .05)$.
Using R:

```r
> x = c(3, 6, 9, 7, 5)
> chisq.test(x, p = c(.15, .25, .35, .20, .05))
# X-squared = 9.3476, df = 4, p-value = 0.05297
```

### 11.2.1 Determining the critical region by simulation *(Optional)*
Simulating $r$ independent sets of $n$ observations from $\{p_1, \dots, p_k\}$ to compute empirical $p$-value.

**Example 11.2.c.** Simulation critical value for Example 11.2.b is $9.52381 \approx \chi_{.05, 4}^2 = 9.488$.

## 11.3 Goodness of fit tests when some parameters are unspecified

If $m$ unknown parameters are estimated from the data by maximum likelihood, then for large $n$, under $H_0$:

$$T = \sum_{i=1}^k \frac{(X_i - n\hat{p}_i)^2}{n\hat{p}_i} \sim \chi_{k - 1 - m}^2$$

**Example 11.3.a.** Weekly accidents (30 weeks, total 95 accidents):
- $\hat{\lambda} = 95/30 = 3.16667$.
- Grouped into 5 regions: counts $X = c(6, 5, 8, 6, 5)$.
- $T = 21.99, \text{df} = 5 - 1 - 1 = 3 \implies p\text{-value} = 6.55 \times 10^{-5} \implies \text{Reject Poisson distribution}$.

## 11.4 Tests of independence in contingency tables

Consider a population classified by two characteristics ($X$ with $r$ categories, $Y$ with $s$ categories).

$$H_0 : P_{ij} = p_i q_j \quad \text{for all } i = 1, \dots, r, \; j = 1, \dots, s$$

Let $N_{ij}$ be the observed counts, $N_i = \sum_{j=1}^s N_{ij}, M_j = \sum_{i=1}^r N_{ij}$.
Estimators: $\hat{p}_i = N_i/n, \hat{q}_j = M_j/n \implies \hat{e}_{ij} = n\hat{p}_i\hat{q}_j = \frac{N_i M_j}{n}$.

Test statistic:

$$T = \sum_{j=1}^s \sum_{i=1}^r \frac{(N_{ij} - \hat{e}_{ij})^2}{\hat{e}_{ij}} = \sum_{j=1}^s \sum_{i=1}^r \frac{N_{ij}^2}{\hat{e}_{ij}} - n \sim \chi_{(r-1)(s-1)}^2$$

**Example 11.4.a.** Gender vs political affiliation ($2 \times 3$ table, $n = 300$):
- $TS = 6.433, \text{df} = (2-1)(3-1) = 2 \implies p\text{-value} = 0.0401 \implies$ Reject independence at $5\%$.

**Example 11.4.b.** Machine breakdowns vs shifts ($3 \times 4$ table, $n = 138$):
- $TS = 1.8148, \text{df} = 6 \implies p\text{-value} = 0.9359 \implies$ Accept independence.

## 11.5 Tests of independence in contingency tables having fixed marginal totals

The test statistic and its distribution $(\chi_{(r-1)(s-1)}^2)$ remain the same when row (or column) marginal totals are fixed in advance.

**Example 11.5.a.** Smoking and lung cancer (10,000 smokers, 20,000 nonsmokers):
- $TS = 79.83, \text{df} = 1 \implies p\text{-value} \approx 0 \implies$ Reject independence.

### Testing Equality of $m$ Discrete Populations
Testing $H_0 : p_{1, j} = \dots = p_{m, j}$ for all $j = 1, \dots, n$ is equivalent to testing for independence in an $m \times n$ contingency table.

**Example 11.5.b.** Female office worker abuse in 4 countries ($n = 500$ each):
- $TS = 19.51, \text{df} = 3 \implies p\text{-value} \approx .0002 \implies$ Reject equality of proportions.

## 11.6 The Kolmogorov–Smirnov goodness of fit test for continuous data *(Optional)*

For continuous distribution $F$, the empirical CDF is:

$$F_e(x) = \frac{\#\{i : Y_i \le x\}}{n}$$

Test statistic:

$$D = \max_x |F_e(x) - F(x)| = \max_{j=1, \dots, n} \left\{\frac{j}{n} - F(y_{(j)}), \; F(y_{(j)}) - \frac{j-1}{n}\right\} \tag{11.6.3}$$

**Proposition 11.6.1.** The distribution of $D$ under $H_0$ is distribution-free.

Modified test statistic:

$$D^* = \left(\sqrt{n} + 0.12 + \frac{0.11}{\sqrt{n}}\right) D$$

Critical values for $D^*$:
- $d_{.1}^* = 1.224$
- $d_{.05}^* = 1.358$
- $d_{.025}^* = 1.480$
- $d_{.01}^* = 1.626$

**Example 11.6.a.** Testing exponential distribution with mean 100 on $n = 10$ values:
- $D = .48315 \implies D^* = .48315(\sqrt{10} + 0.12 + 0.11/\sqrt{10}) = 1.603 > 1.480 \implies$ Reject at $\alpha = .025$.

---

## Problems

1. Mendelian genetics in garden peas: white (1/4), pink (1/2), red (1/4). Sample of 564: 141 white, 291 pink, 132 red. Test at 5% significance.

2. Die fairness: 1000 rolls:
   - Counts: 1: 158, 2: 172, 3: 164, 4: 181, 5: 160, 6: 165. Test fairness at 5%.

3. Birthday vs death month in 100 individuals (4-category test).

4. Daily power failures (mean 4.2 Poisson): 150 days observed counts.

5. Vacuum tube lifetimes: 41 (<30h), 31 (30–60h), 13 (60–90h), 15 (>90h). Test exponential with mean 50h.

6. Machine grade outputs: top (.40), high (.30), medium (.20), low (.10). Observed: 234, 117, 81, 68 out of 500.

7. Neutrino radiation across 24 sidereal hours (Table 11.3). Test uniform distribution.

8. Neutrino signal frequency per hour. Test Poisson(.3).

9. Engineer accident profile vs regional population (82%, 15%, 3%). Sample of 440: 366 (0), 68 (1), 6 (2+).

10. Earthquake occurrence by day of week (1100 earthquakes: Sun 156, Mon 144, Tue 170, Wed 158, Thu 172, Fri 148, Sat 152).

11. Coin tossing data fit check: 20,004 heads, 19,996 tails out of 40,000.

12. Simulation $p$-value for Problem 1 with $r = 1000, 5000, 10000$.

13. Test normality on sample of size 120 with $\bar{X} = 100, S = 15$.

14. Test Poisson distribution on Problem 4 data.

15. Migrant families income vs region ($4 \times 2$ table, $n = 500$).

16. Maternal age ($\le 20$ vs $> 20$) vs infant birthweight ($\le 2500$g vs $> 2500$g).

17. Repeat Problem 16 with doubled sample size.

18. Infant birthweight vs 1-year mortality (72,730 births).

19. Hypertension vs smoking (Nonsmoker, Moderate, Heavy).

20. Manufacturing quality before and after modification (Defective, Acceptable, Superior).

21. Cell phones in cars vs accidents (300 with phones, 400 without).

22. Fluoridated water vs cavities (200 teenagers from each town).

23. Malpractice lawsuits across 3 surgery types (Heart 16/400, Brain 19/300, Appendectomy 7/300).

24. Sunset colors vs next day rain (Table: Red, Mainly red, Yellow, Mainly yellow, Red and yellow, Gray).

25. Kolmogorov-Smirnov test for lognormal distribution ($\mu = 3, \sigma = 4$) on 12 mouse lifetimes.
