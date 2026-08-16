# Chapter 12: Nonparametric hypothesis tests

## 12.1 Introduction

In this chapter, we shall develop some hypothesis tests in situations where the data come from a probability distribution whose underlying form is not specified. That is, it will not be assumed that the underlying distribution is normal, or exponential, or any other given type. Because no particular parametric form for the underlying distribution is assumed, such tests are called *nonparametric*.

The strength of a nonparametric test resides in the fact that it can be applied without any assumption on the form of the underlying distribution.

## 12.2 The sign test

Let $X_1, \dots, X_n$ denote a sample from a continuous distribution $F$ with median $m$ (where $F(m) = .5$). To test:

$$H_0 : m = m_0 \quad \text{versus} \quad H_1 : m \neq m_0$$

Let

$$I_i = \begin{cases} 1 & \text{if } X_i < m_0 \\ 0 & \text{if } X_i \ge m_0 \end{cases}$$

Then $I_1, \dots, I_n$ are independent Bernoulli random variables with parameter $p = F(m_0) = \frac{1}{2}$ under $H_0$. If $v = \sum_{i=1}^n I_i$ is the number of data values less than $m_0$:

$$p\text{-value} = 2\min\left(P\left\{\text{Bin}\left(n, \frac{1}{2}\right) \le v\right\}, \; P\left\{\text{Bin}\left(n, \frac{1}{2}\right) \le n - v\right\}\right) \tag{12.2.2}$$

**Example 12.2.a.** $n = 200$, 120 values $< m_0$ and 80 values $> m_0$:

$$p\text{-value} = 2P\left\{\text{Bin}\left(200, \frac{1}{2}\right) \le 80\right\} = 2 \times \text{pbinom}(80, 200, .5) = 0.00568 \implies \text{Reject } H_0 \quad \blacksquare$$

### One-Sided Sign Test
To test $H_0 : m \le m_0$ vs $H_1 : m > m_0$:

$$p\text{-value} = P\left\{\text{Bin}\left(n, \frac{1}{2}\right) \le v\right\}$$

**Example 12.2.b.** $H_0 : m \le 90$ vs $H_1 : m > 90$. In a sample of $n = 80$, 28 values $< 90$:

$$p\text{-value} = P\{\text{Bin}(80, .5) \le 28\} = 0.00484 \implies \text{Reject } H_0 \quad \blacksquare$$

## 12.3 The signed rank test

To test $H_0 : F \text{ is symmetric about } m_0$:
Let $Y_i = X_i - m_0, i = 1, \dots, n$. Rank the absolute values $|Y_1|, \dots, |Y_n|$.
Set $I_j = 1$ if the $j$th smallest absolute value comes from a negative $Y$, and $0$ otherwise.

Test statistic:

$$T = \sum_{j=1}^n j I_j$$

Under $H_0$:

$$E[T] = \frac{n(n + 1)}{4} \tag{12.3.1}$$
$$\text{Var}(T) = \frac{n(n + 1)(2n + 1)}{24} \tag{12.3.2}$$

$p$-value calculation:

$$p\text{-value} = 2P_{H_0}\{T \le t^*\}, \quad \text{where } t^* = \min\left(t, \; \frac{n(n + 1)}{2} - t\right)$$

Recursive calculation of $P_k(i) = P_{H_0}\{\sum_{j=1}^k j I_j \le i\}$:

$$P_k(i) = \frac{1}{2} P_{k-1}(i - k) + \frac{1}{2} P_{k-1}(i) \tag{12.3.6}$$

**Example 12.3.a / 12.3.b.** $n = 4, m_0 = 2, X = (4.2, 1.8, 5.3, 1.7) \implies T = 3, t^* = 3 \implies p\text{-value} = 2P_4(3) = 2\left(\frac{5}{16}\right) = 0.625$.

In R:

```r
> wilcox.test(x, mu = 2)
# V = 7, p-value = 0.625
```

## 12.4 The two-sample problem

Let $X_1, \dots, X_n \sim F$ and $Y_1, \dots, Y_m \sim G$ be independent samples from continuous distributions. We test:

$$H_0 : F = G$$

Rank all $N = n + m$ pooled observations. Let $R_i$ be the rank of $X_i$.
Test statistic (Wilcoxon Rank Sum / Mann-Whitney):

$$T = \sum_{i=1}^n R_i$$

**Example 12.4.a.** Wire corrosion: Treatment 1 ($n = 6$), Treatment 2 ($m = 5$). $T = 3 + 5 + 7 + 9 + 10 + 11 = 45$.

Recursive formula for $P(N, M, K) = P_{H_0}\{T \le K\}$:

$$P(N, M, K) = \frac{N}{N + M} P(N - 1, M, K - N - M) + \frac{M}{N + M} P(N, M - 1, K) \tag{12.4.3}$$

$$p\text{-value} = 2\min\{P(n, m, t), \; 1 - P(n, m, t - 1)\}$$

In R:

```r
> wilcox.test(x, y)
# W = 24, p-value = 0.1255
```

### 12.4.1 Testing the equality of multiple probability distributions (Kruskal-Wallis Test)

To test $H_0 : F_1 = F_2 = \dots = F_k$ for $k$ populations with sample sizes $n_1, \dots, n_k$ and total size $N = \sum n_i$:
Rank all $N$ observations and let $R_i$ be the sum of ranks for sample $i$.

Test statistic:

$$TS = \sum_{i=1}^k \frac{R_i^2}{n_i}$$

Under $H_0$, when all $n_i \ge 5$:

$$\frac{12}{N(N + 1)} TS - 3(N + 1) \sim \chi_{k-1}^2$$

**Example 12.4.c.** Library visitors ($k = 3, n_1 = n_2 = n_3 = 10, N = 30$):
- $R_1 = 176, R_2 = 175, R_3 = 114$.
- $\frac{12}{30 \times 31}\left(\frac{176^2 + 175^2 + 114^2}{10}\right) - 93 = 3.254$.
- $p\text{-value} = P\{\chi_2^2 \ge 3.254\} = 0.1965 \implies$ Accept $H_0$. $\blacksquare$

## 12.5 The runs test for randomness

Let a sequence contain $n$ 1's and $m$ 0's ($N = n + m$), with $R$ being the total number of runs.

Under $H_0$ (randomness):

$$P_{H_0}\{R = 2k\} = 2 \frac{\binom{m-1}{k-1}\binom{n-1}{k-1}}{\binom{m+n}{n}} \tag{12.5.1}$$
$$P_{H_0}\{R = 2k + 1\} = \frac{\binom{m-1}{k-1}\binom{n-1}{k} + \binom{m-1}{k}\binom{n-1}{k-1}}{\binom{m+n}{n}}$$

$$p\text{-value} = 2\min(P_{H_0}\{R \ge r\}, \; P_{H_0}\{R \le r\})$$

**Example 12.5.a.** Team win-loss sequence (20 W, 10 L, 20 runs): $p\text{-value} = 0.01845 \implies$ Reject randomness.

**Example 12.5.b.** Battery lifetimes: 19 values categorized around median 169 (10 ones, 9 zeros, 8 runs): $p\text{-value} = .357 \implies$ Accept randomness.

### Large-Sample Normal Approximation
For large $n$ and $m$:

$$\mu = \frac{2nm}{n + m} + 1, \qquad \sigma = \sqrt{\frac{2nm(2nm - n - m)}{(n + m)^2(n + m - 1)}} \tag{12.5.2}$$

$$p\text{-value} \approx 2\min\left(\Phi\left(\frac{r - \mu}{\sigma}\right), \; 1 - \Phi\left(\frac{r - \mu}{\sigma}\right)\right)$$

**Example 12.5.c.** $n = 60, m = 60, r = 75 \implies \mu = 61, \sigma = 5.454 \implies p\text{-value} \approx .0102$.

---

## Problems

1. Hypertension medicine on 18 patients: Diastolic BP changes:
   $$-5, -1, +2, +8, -25, +1, +5, -12, -16, -9, -8, -18, -5, -22, +4, -21, -15, -11$$
   Use sign test to determine if medicine has an effect. What is the $p$-value?

2. Computer system problem-solving times (8 design problems on Computer A vs Computer B):
   - A: 15, 32, 17, 26, 42, 29, 12, 38
   - B: 22, 29, 1, 23, 46, 25, 19, 47
   Determine sign test $p$-value.

3. Median systolic BP (null = 128) in sample of 100 men:
   a. 60 men above 128;
   b. 70 men above 128;
   c. 80 men above 128.

4. 16-year-old female weights: $n = 200$, test $H_0 : m \ge 110$ if 120 weigh $< 110$.

5. Financial accountant salaries: 2004 median $\$124,400$; 2007 sample of 14 incomes.

6. Gasoline additive mileage on 8 cars: sign test vs signed rank test.

7. Signed rank test for Problems 1 and 2.

8. Albumin content in blood for 12 patients before and after treatment.

9. Aircraft cruising speed before and after painting ($n = 10$).

10. Spectrochemical determinations for nickel with two instruments ($n = 10$).

11. One-sided analog of the signed rank test for $H_0 : m = m_0$ vs $H_1 : m > m_0$.

12. Bilingual coding scores in French vs English ($n = 6$ each).

13. Traffic accidents in 8 treatment vs 7 control cities.

14. Normal approximation and simulation $p$-value for Problem 13.

15. Republican vs Democrat adult male weights ($n = 8$ each).

16. Rat worm treatment (dose .032 vs .063, $n = 5$ each).

17. Beaver dispersal distances (9 females vs 23 males).

18. Health clinic visits after football win, loss, or no game (10 weeks each).

19. Production run of 50 items with 11 defectives: items 8, 12, 13, 14, 31, 32, 37, 38, 40, 41, 42. Test randomness using runs test.

20. Quality levels of 25 articles tested for randomness.

21. Runs test around a predetermined value vs sample median.

22. Major El Niño events (1800–1987) magnitudes (Table 12.1): test randomness of occurrences.
