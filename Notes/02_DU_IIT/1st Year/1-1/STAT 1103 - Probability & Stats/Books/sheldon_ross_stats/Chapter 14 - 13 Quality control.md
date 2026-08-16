# Chapter 13: Quality control

## 13.1 Introduction

Almost every manufacturing process results in some random variation in the items it produces. That is, no matter how stringently the process is being controlled, there is always going to be some variation between the items produced. This variation is called *chance variation* and is considered to be inherent to the process. However, there is another type of variation that sometimes appears, due to some *assignable cause* (e.g., faulty machine setting, poor raw materials, human error). When the only variation present is due to chance, we say that the process is *in control*.

Control charts, determined by upper and lower control limits (UCL and LCL), help detect when a process goes out of control.

## 13.2 Control charts for average values: the $\bar{x}$ control chart

Suppose that when in control, the measurable characteristic of successive items are independent $N(\mu, \sigma^2)$ random variables. Data are partitioned into subgroups of size $n$ (typically $n = 4, 5,$ or $6$). Let $\bar{X}_i$ denote the average of the $i$th subgroup. When in control:

$$E[\bar{X}_i] = \mu, \qquad \text{Var}(\bar{X}_i) = \frac{\sigma^2}{n} \implies \frac{\bar{X}_i - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$

Since $P\{-3 < Z < 3\} = .9973$, the $3\sigma$ control limits are:

$$\text{UCL} = \mu + \frac{3\sigma}{\sqrt{n}}$$
$$\text{LCL} = \mu - \frac{3\sigma}{\sqrt{n}}$$

**Example 13.2.a.** Steel shafts diameter: $\mu = 3$ mm, $\sigma = .1$ mm, $n = 4$:
- $\text{LCL} = 3 - \frac{3(.1)}{\sqrt{4}} = 2.85$, $\text{UCL} = 3 + \frac{3(.1)}{\sqrt{4}} = 3.15$.
- Subgroup 10 has $\bar{X}_{10} = 3.20 > 3.15 \implies$ Out of control. $\blacksquare$

### Detection of Mean Shifts
If the mean shifts from $\mu$ to $\mu + a$ ($a > 0$), the probability that a subgroup average falls outside the control limits is approximately:

$$1 - \Phi\left(3 - \frac{a\sqrt{n}}{\sigma}\right)$$

The number of subgroups required to detect the shift has a geometric distribution with mean $\left[1 - \Phi\left(3 - \frac{a\sqrt{n}}{\sigma}\right)\right]^{-1}$.

### 13.2.1 Case of unknown $\mu$ and $\sigma$

When $\mu$ and $\sigma$ are unknown, we collect $k$ subgroups ($k \ge 20, nk \ge 100$).
- Estimate of $\mu$: $\bar{\bar{X}} = \frac{1}{k}\sum_{i=1}^k \bar{X}_i$.
- Subgroup sample standard deviations: $S_i = \sqrt{\frac{\sum_{j=1}^n (X_{(i-1)n+j} - \bar{X}_i)^2}{n - 1}}$.
- Average standard deviation: $\bar{S} = \frac{1}{k}\sum_{i=1}^k S_i$.

Since $\frac{(n-1)S_1^2}{\sigma^2} \sim \chi_{n-1}^2$:

$$E[S_1] = c(n)\sigma, \quad \text{where } c(n) = \frac{\sqrt{2}\Gamma(n/2)}{\sqrt{n-1}\Gamma((n-1)/2)}$$

**Table 13.1: Values of $c(n)$**

| $n$ | $c(n)$ |
| :--- | :--- |
| 2 | .7978849 |
| 3 | .8862266 |
| 4 | .9213181 |
| 5 | .9399851 |
| 6 | .9515332 |
| 7 | .9593684 |
| 8 | .9650309 |
| 9 | .9693103 |
| 10 | .9726596 |

Estimated control limits for $\bar{X}$:

$$\text{UCL} = \bar{\bar{X}} + \frac{3\bar{S}}{c(n)\sqrt{n}}, \qquad \text{LCL} = \bar{\bar{X}} - \frac{3\bar{S}}{c(n)\sqrt{n}} \tag{13.2.4}$$

**Example 13.2.b.** $n = 4, \bar{\bar{X}} = 3.067, \bar{S} = .122, c(4) = .9213$:
- $\text{LCL} = 2.868, \text{UCL} = 3.266$.
- Specification $3 \pm .1 \implies P\{2.9 \le X \le 3.1\} = .4948$.

## 13.3 $S$-control charts

To monitor the population variance:

$$E[S_i] = c(n)\sigma \tag{13.3.1}$$
$$\text{Var}(S_i) = \sigma^2[1 - c^2(n)] \tag{13.3.2}$$

Control limits when $\sigma$ is known:

$$\text{UCL} = \sigma[c(n) + 3\sqrt{1 - c^2(n)}] \tag{13.3.3}$$
$$\text{LCL} = \sigma[c(n) - 3\sqrt{1 - c^2(n)}]$$

Estimated control limits when $\sigma$ is unknown (using $\bar{S}/c(n)$):

$$\text{UCL} = \bar{S}\left[1 + 3\sqrt{\frac{1}{c^2(n)} - 1}\right] \tag{13.3.4}$$
$$\text{LCL} = \bar{S}\left[1 - 3\sqrt{\frac{1}{c^2(n)} - 1}\right]$$

**Example 13.3.a.** $k = 20$ subgroups of size $n = 5$: $\bar{\bar{X}} = 35.94, \bar{S} = 4.35, c(5) = .9400$.
- $\text{UCL}(\bar{X}) = 42.149, \text{LCL}(\bar{X}) = 29.731$.
- $\text{UCL}(S) = 9.087, \text{LCL}(S) = -.386$.
- Subgroups 10 and 15 fall outside $\bar{X}$ limits.

## 13.4 Control charts for the fraction defective ($p$-chart)

When items are classified as defective/acceptable, let $X \sim \text{Binomial}(n, p)$ and fraction defective $F = X/n$:

$$E[F] = p, \qquad \sqrt{\text{Var}(F)} = \sqrt{\frac{p(1 - p)}{n}}$$

Control limits:

$$\text{UCL} = p + 3\sqrt{\frac{p(1 - p)}{n}}, \qquad \text{LCL} = p - 3\sqrt{\frac{p(1 - p)}{n}}$$

Estimated from $k$ subgroups: $\bar{F} = \frac{\text{total defectives}}{\text{total items}}$:

$$\text{UCL} = \bar{F} + 3\sqrt{\frac{\bar{F}(1 - \bar{F})}{n}}, \qquad \text{LCL} = \bar{F} - 3\sqrt{\frac{\bar{F}(1 - \bar{F})}{n}}$$

**Example 13.4.a.** 20 samples of size 50 screws (34 total defectives $\implies \bar{F} = .034$):
- Initial limits: $\text{UCL} = .1109, \text{LCL} = -.0429$.
- Subgroup 1 ($F_1 = .12$) exceeds UCL. Eliminating subgroup 1: new $\bar{F} = 28/950 = .0295 \implies \text{UCL} = .1013, \text{LCL} = -.0423$.

## 13.5 Control charts for number of defects ($c$-chart)

When data represent number of defects per unit $X_i \sim \text{Poisson}(\lambda)$:

$$\text{UCL} = \lambda + 3\sqrt{\lambda}, \qquad \text{LCL} = \lambda - 3\sqrt{\lambda}$$

When $\lambda$ is estimated by $\bar{X}$:

$$\text{UCL} = \bar{X} + 3\sqrt{\bar{X}}, \qquad \text{LCL} = \bar{X} - 3\sqrt{\bar{X}}$$

**Table 13.2: Effect of Subgroup Size $n$ on Detecting a Poisson Mean Shift from 4 to 6**

| $n$ | Average Number of Items |
| :--- | :--- |
| 1 | 19.6 |
| 2 | 20.66 |
| 3 | 19.80 |
| 4 | 19.32 |
| 5 | 18.80 |
| 6 | 18.18 |
| 7 | 18.13 |
| 8 | 18.02 |
| 9 | 18.00 |
| 10 | 18.18 |
| 11 | 18.33 |
| 12 | 18.51 |

**Example 13.5.a.** Car defects across 20 units of 10 cars: $\bar{X} = 94.4 \implies \text{UCL} = 123.55, \text{LCL} = 65.25$. After eliminating outliers, in-control mean $= 82.56$.

## 13.6 Other control charts for detecting changes in the population mean

### 13.6.1 Moving-average control charts
Moving average of span $k$:

$$M_t = \frac{\bar{X}_t + \bar{X}_{t-1} + \dots + \bar{X}_{t-k+1}}{k} = M_{t-1} + \frac{\bar{X}_t - \bar{X}_{t-k}}{k}$$

For $t < k$, $M_t = \frac{1}{t}\sum_{i=1}^t \bar{X}_i$.

Control limits:

$$\text{UCL} = \begin{cases} \mu + \frac{3\sigma}{\sqrt{nt}} & \text{if } t < k \\ \mu + \frac{3\sigma}{\sqrt{nk}} & \text{if } t \ge k \end{cases}, \qquad \text{LCL} = \begin{cases} \mu - \frac{3\sigma}{\sqrt{nt}} & \text{if } t < k \\ \mu - \frac{3\sigma}{\sqrt{nk}} & \text{if } t \ge k \end{cases}$$

**Example 13.6.a.** Span $k = 8, n = 5, \mu = 10, \sigma = 2$. Out of control detected at $t = 11$.

### 13.6.2 Exponentially weighted moving-average (EWMA) control charts

$$W_t = \alpha \bar{X}_t + (1 - \alpha) W_{t-1}, \qquad W_0 = \mu$$

For large $t$:

$$E[W_t] = \mu, \qquad \text{Var}(W_t) \approx \frac{\sigma^2 \alpha}{n(2 - \alpha)}$$

Control limits:

$$\text{UCL} = \mu + 3\sigma \sqrt{\frac{\alpha}{n(2 - \alpha)}}, \qquad \text{LCL} = \mu - 3\sigma \sqrt{\frac{\alpha}{n(2 - \alpha)}}$$

Equivalence to moving average with span $k$: $k = \frac{2 - \alpha}{\alpha} \iff \alpha = \frac{2}{k + 1}$.

**Example 13.6.b.** Dispatch repair time: $\mu = 62, \sigma = 24, n = 4, \alpha = .25 \implies \text{LCL} = 48.39, \text{UCL} = 75.61$. Detected at $t = 14$.

**Example 13.6.c.** Data of 13.6.a with $\alpha = 2/9 \implies$ Detected as early as $t = 7$.

### 13.6.3 Cumulative sum (CUSUM) control charts

To detect an increase in mean:

$$Y_j = \bar{X}_j - \mu - \frac{d\sigma}{\sqrt{n}}$$
$$S_0 = 0, \qquad S_{j+1} = \max(S_j + Y_{j+1}, \; 0)$$

Signal out of control at first $j$ such that $S_j > B\frac{\sigma}{\sqrt{n}}$.

Two-sided CUSUM: Also plot $T_{j+1} = \max(T_j + W_{j+1}, \; 0)$ where $W_j = \mu - \bar{X}_j - \frac{d\sigma}{\sqrt{n}}$.
Standard parameter pairs: $(d = .25, B = 8.00)$, $(d = .50, B = 4.77)$, $(d = 1.00, B = 2.49)$.

**Example 13.6.d.** $\mu = 30, \sigma/\sqrt{n} = 8, d = .5, B = 5 \implies \text{Limit } = 40$. Out of control at $j = 8$ ($S_8 = 41$).

---

## Problems

1. $\bar{X}$ chart for $N(35, 3^2)$ with $n = 5$ on 20 subgroups. Test if in control.

2. Process in control with $\mu = 14, \sigma = 2, n = 5$. Shift of $2.2$ units in mean. Probability next subgroup falls outside limits, and average run length.

3. Proof that $E[\sqrt{Y}] = \sqrt{2} \frac{\Gamma(n/2)}{\Gamma((n-1)/2)}$ when $Y \sim \chi_{n-1}^2$.

4. 25 samples of size 5: $\sum \bar{X}_i = 357.2, \sum S_i = 4.88$.
   a. Control limits for $\bar{X}$ chart.
   b. Percentage conforming to $14.3 \pm .45$.

5. Revised limits for Example 13.3.a data.

6. Control limits for $S$-chart in Problem 4.

7. $\bar{X}$ and $S$ values for 20 subgroups of size 5: trial limits and revisions.

8. Spot welds shear strength ($n = 4, k = 30, \sum \bar{X}_i = 12660, \sum S_i = 500$). $\bar{X}$ and $S$ limits, percentage $< 400$ lbs.

9. Resistors in ohms ($n = 4, k = 20, \sum \bar{X}_i = 8620, \sum S_i = 450$). Limits and capability for $430 \pm 30$.

10. Ball bearing diameters ($n = 5, k = 15$ raw subgroups).

11. Quality characteristic ($n = 6, k = 50, \sum \bar{X}_i = 970, \sum S_i = 85$).

12. Bearing and seal assemblies ($n = 100, k = 20$ samples). $p$-chart control limits.

13. PC inspection for 12 days ($p$-chart with variable daily production).

14. Shift detection probability for $p$-chart ($p = .04 \to .08, n = 500$).

15. Defective chips on 15 days ($c$-chart).

16. Surface defects on 25 steel plates ($c$-chart).

17. Moving-average chart with span $k = 5$ on 25 subgroup averages ($N(30, 40), n = 4$).

18. Moving-average chart with span $k = 8$ on 20 subgroup averages ($N(50, 5)$).

19. EWMA chart with $\alpha = 1/3$ for Problem 17 data.

20. EWMA chart with $\alpha = 2/9$ for Problem 18 data.

21. Explain why moving-average control limits vary for $t < k$ while EWMA uses constant limits.

22. CUSUM chart for Problem 17 data ($d = .25, B = 8$ and $d = .5, B = 4.77$).

23. CUSUM chart for Problem 18 data ($d = 1, B = 2.49$).
