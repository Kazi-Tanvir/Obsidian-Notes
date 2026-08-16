# Chapter 9: Regression

## 9.1 Introduction

Many engineering and scientific problems are concerned with determining a relationship between a set of variables. For instance, in a chemical process, we might be interested in the relationship between the output of the process, the temperature at which it occurs, and the amount of catalyst employed. Knowledge of such a relationship would enable us to predict the output for various values of temperature and amount of catalyst.

In many situations, there is a single response variable $Y$, also called the *dependent variable*, which depends on the value of a set of input, also called *independent*, variables $x_1, \dots, x_r$. The simplest type of relationship between the dependent variable $Y$ and the input variables $x_1, \dots, x_r$ is a linear relationship. That is, for some constants $\beta_0, \beta_1, \dots, \beta_r$ the equation

$$Y = \beta_0 + \beta_1 x_1 + \dots + \beta_r x_r \tag{9.1.1}$$

would hold. In practice, such precision is almost never attainable, and the explicit relationship is

$$Y = \beta_0 + \beta_1 x_1 + \dots + \beta_r x_r + e \tag{9.1.2}$$

where $e$, representing the random error, is assumed to be a random variable having mean 0. That is,

$$E[Y \mid x] = \beta_0 + \beta_1 x_1 + \dots + \beta_r x_r$$

Equation (9.1.2) is called a *linear regression equation*. The quantities $\beta_0, \beta_1, \dots, \beta_r$ are called the *regression coefficients*. A simple linear regression model contains a single independent variable:

$$Y = \alpha + \beta x + e$$

**Example 9.1.a.** Experiment yield $y$ vs temperature $x$:

| $i$ | $x_i$ | $y_i$ | $i$ | $x_i$ | $y_i$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 100 | 45 | 6 | 150 | 68 |
| 2 | 110 | 52 | 7 | 160 | 75 |
| 3 | 120 | 54 | 8 | 170 | 76 |
| 4 | 130 | 63 | 9 | 180 | 92 |
| 5 | 140 | 62 | 10 | 190 | 88 |

A scatter diagram reflects a linear relationship subject to random error.

## 9.2 Least squares estimators of the regression parameters

For observations $(x_i, Y_i), i = 1, \dots, n$, the sum of squared differences is

$$SS = \sum_{i=1}^n (Y_i - A - B x_i)^2$$

Setting $\frac{\partial SS}{\partial A} = 0$ and $\frac{\partial SS}{\partial B} = 0$ gives the *normal equations*:

$$\sum_{i=1}^n Y_i = nA + B \sum_{i=1}^n x_i \tag{9.2.1}$$
$$\sum_{i=1}^n x_i Y_i = A \sum_{i=1}^n x_i + B \sum_{i=1}^n x_i^2$$

**Proposition 9.2.1.** The least squares estimators of $\beta$ and $\alpha$ are

$$B = \frac{\sum_{i=1}^n x_i Y_i - \bar{x}\sum_{i=1}^n Y_i}{\sum_{i=1}^n x_i^2 - n\bar{x}^2} = \frac{S_{xY}}{S_{xx}}$$
$$A = \bar{Y} - B\bar{x}$$

The straight line $A + Bx$ is called the *estimated regression line*.

In R:

```r
> fit = lm(y ~ x)
> plot(x, y)
> abline(fit)
```

**Example 9.2.a.** Relative humidity ($x$) vs moisture content ($y$):
Using R, the estimated regression line is $y = -2.5105 + 0.3232x$.

## 9.3 Distribution of the estimators

Assume $Y_i \sim N(\alpha + \beta x_i, \sigma^2)$ are independent.

**Notation:**
$$S_{xY} = \sum_{i=1}^n (x_i - \bar{x})(Y_i - \bar{Y}) = \sum_{i=1}^n x_i Y_i - n\bar{x}\bar{Y}$$
$$S_{xx} = \sum_{i=1}^n (x_i - \bar{x})^2 = \sum_{i=1}^n x_i^2 - n\bar{x}^2$$
$$S_{YY} = \sum_{i=1}^n (Y_i - \bar{Y})^2 = \sum_{i=1}^n Y_i^2 - n\bar{Y}^2$$

**Proposition 9.3.1.**
$$A \sim N\left(\alpha, \; \frac{\sigma^2 \sum x_i^2}{n S_{xx}}\right)$$
$$B \sim N\left(\beta, \; \frac{\sigma^2}{S_{xx}}\right)$$

The sum of squares of the residuals $SSR = \sum_{i=1}^n (Y_i - A - B x_i)^2$ satisfies:

$$\frac{SSR}{\sigma^2} \sim \chi_{n-2}^2$$

and $SSR$ is independent of $A$ and $B$. Computational identity:

$$SSR = \frac{S_{xx} S_{YY} - S_{xY}^2}{S_{xx}} \tag{9.3.4}$$

An unbiased estimator of $\sigma^2$ is $\frac{SSR}{n - 2}$.

**Example 9.3.a.** Moisture and density data: $SSR = 9.4698, y = 2.463 + 1.206x$.

## 9.4 Statistical inferences about the regression parameters

### 9.4.1 Inferences concerning $\beta$

$$\sqrt{\frac{(n - 2)S_{xx}}{SSR}}(B - \beta) \sim t_{n-2} \tag{9.4.2}$$

To test $H_0 : \beta = 0$ vs $H_1 : \beta \neq 0$:
- Reject $H_0$ if $\sqrt{\frac{(n - 2)S_{xx}}{SSR}}|B| > t_{\alpha/2, n-2}$.

A $100(1 - a)$ percent confidence interval for $\beta$:

$$B \pm \sqrt{\frac{SSR}{(n - 2)S_{xx}}} t_{a/2, n-2}$$

**Example 9.4.a.** Speed vs mpg: $t = -8.138, p\text{-value} = 0.000455 \implies \text{Reject } \beta = 0$.

**Example 9.4.b.** Using `confint(miles, level = 0.95)` in R.

#### 9.4.1.1 Regression to the mean
If $E[Y] = \alpha + \beta x$ and $0 < \beta < 1$, offspring of extreme parents tend to be closer to the average.

**Example 9.4.c.** Pearson's father and son heights data: $B = 0.46457, \text{TS} = -16.23 \implies p\text{-value} = 1.05 \times 10^{-7} \implies$ proves regression to the mean ($\beta < 1$).

**Example 9.4.d.** Motor vehicle deaths (regression fallacy).

### 9.4.2 Inferences concerning $\alpha$

A $100(1 - a)$ percent confidence interval for $\alpha$:

$$A \pm t_{a/2, n-2} \sqrt{\frac{SSR \sum x_i^2}{n(n - 2)S_{xx}}}$$

### 9.4.3 Inferences concerning the mean response $\alpha + \beta x_0$

$$A + B x_0 \sim N\left(\alpha + \beta x_0, \; \sigma^2\left[\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}\right]\right) \tag{9.4.4}$$

Confidence interval for $\alpha + \beta x_0$:

$$A + B x_0 \pm \sqrt{\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}} \sqrt{\frac{SSR}{n - 2}} t_{a/2, n-2}$$

**Example 9.4.e.** 95% CI for average height of sons of 68-inch fathers: $(67.24, 67.90)$.

### 9.4.4 Prediction interval of a future response

For a single future observation $Y(x_0)$ at input $x_0$:

$$Y(x_0) \in A + B x_0 \pm \sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}} \sqrt{\frac{SSR}{n - 2}} t_{a/2, n-2}$$

**Example 9.4.f.** Prediction interval for height of a specific son: $67.568 \pm 1.050 = (66.52, 68.62)$.

### 9.4.5 Summary of Distributional Results

| Inferences About | Distributional Result |
| :--- | :--- |
| $\beta$ | $\sqrt{\frac{(n-2)S_{xx}}{SSR}}(B - \beta) \sim t_{n-2}$ |
| $\alpha$ | $\sqrt{\frac{n(n-2)S_{xx}}{SSR \sum x_i^2}}(A - \alpha) \sim t_{n-2}$ |
| $\alpha + \beta x_0$ | $\frac{A + Bx_0 - (\alpha + \beta x_0)}{\sqrt{1/n + (x_0-\bar{x})^2/S_{xx}}\sqrt{SSR/(n-2)}} \sim t_{n-2}$ |
| $Y(x_0)$ | $\frac{Y(x_0) - A - Bx_0}{\sqrt{1 + 1/n + (x_0-\bar{x})^2/S_{xx}}\sqrt{SSR/(n-2)}} \sim t_{n-2}$ |

## 9.5 The coefficient of determination and the sample correlation coefficient

Total sum of squares: $S_{YY} = \sum_{i=1}^n (Y_i - \bar{Y})^2$.

The *coefficient of determination* $R^2$ is:

$$R^2 = \frac{S_{YY} - SSR}{S_{YY}} = 1 - \frac{SSR}{S_{YY}}$$

Furthermore, $|r| = \sqrt{R^2}$, where $r = \frac{S_{xY}}{\sqrt{S_{xx} S_{YY}}}$.

**Example 9.5.a.** Father-son height data: $R^2 = 0.9612$ (96% of variation in sons' heights is explained by fathers' heights).

## 9.6 Analysis of residuals: assessing the model

Standardized residuals:

$$\frac{Y_i - (A + B x_i)}{\sqrt{SSR/(n - 2)}}, \quad i = 1, \dots, n$$

Residual plots check for linearity, homoscedasticity (constant variance), and normality.

## 9.7 Transforming to linearity

Exponential decay $W(t) \approx c e^{-dt} \implies \log W(t) \approx \log c - dt$.
Survival proportion $1 - P(x) \approx c(1 - d)^x \implies \log(1 - P(x)) \approx \log c + x \log(1 - d)$.

**Example 9.7.a.** Chemical percentage: $\hat{P} = 1 - .9847(.9901)^x$.

## 9.8 Weighted least squares

When $\text{Var}(Y_i) = \sigma^2 / w_i$, minimize $\sum_i w_i (Y_i - A - B x_i)^2$.

Normal equations:

$$\sum_i w_i Y_i = A \sum_i w_i + B \sum_i w_i x_i \tag{9.8.1}$$
$$\sum_i w_i x_i Y_i = A \sum_i w_i x_i + B \sum_i w_i x_i^2$$

**Example 9.8.a.** Grouped data estimation.
**Example 9.8.b.** Travel time proportional to distance ($w_i = 1/x_i$).
**Example 9.8.c / Variance Stabilization:** If $Y \sim \text{Poisson}(\lambda)$, $\text{Var}(\sqrt{Y}) \approx 0.25$, so fit $\sqrt{Y} = \alpha + \beta x + e$.

## 9.9 Polynomial regression

Model: $Y = \beta_0 + \beta_1 x + \dots + \beta_r x^r + e$.
Normal equations in matrix notation:

$$\mathbf{B} = (\mathbf{X}'\mathbf{X})^{-1} \mathbf{X}'\mathbf{Y}$$

**Example 9.9.a.** Quadratic fit $Y = 12.59 + 6.33x + 2.12x^2$.

## 9.10 Multiple linear regression *(Optional)*

Model: $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \mathbf{e}$ where $\mathbf{e} \sim N(\mathbf{0}, \sigma^2 \mathbf{I})$.
- Least squares estimator: $\mathbf{B} = (\mathbf{X}'\mathbf{X})^{-1} \mathbf{X}'\mathbf{Y}$
- $E[\mathbf{B}] = \boldsymbol{\beta}, \quad \text{Cov}(\mathbf{B}) = \sigma^2 (\mathbf{X}'\mathbf{X})^{-1}$
- Residual sum of squares: $SSR = \mathbf{Y}'\mathbf{Y} - \mathbf{B}'\mathbf{X}'\mathbf{Y}$, with $\frac{SSR}{\sigma^2} \sim \chi_{n-k-1}^2$

**Example 9.10.a.** Suicide rate vs population and divorce rate: $Y = 3.507 - 0.000248 x_1 + 0.2609 x_2$.
**Example 9.10.b.** Eucalyptus tree diameter vs age, elevation, rainfall, specific gravity.

### 9.10.1 Predicting future responses
- Confidence interval for mean response $\mathbf{x}'\boldsymbol{\beta}$: $\mathbf{x}'\mathbf{b} \pm t_{a/2, n-k-1}\sqrt{\frac{SSR}{n-k-1} \mathbf{x}'(\mathbf{X}'\mathbf{X})^{-1}\mathbf{x}}$
- Prediction interval for $Y(\mathbf{x})$: $\mathbf{x}'\mathbf{b} \pm t_{a/2, n-k-1}\sqrt{\frac{SSR}{n-k-1} [1 + \mathbf{x}'(\mathbf{X}'\mathbf{X})^{-1}\mathbf{x}]}$

**Example 9.10.c.** Steel hardness.

### 9.10.2 Dummy variables for categorical data

## 9.11 Logistic regression models for binary output data

Probability of success $p(x) = \frac{e^{a+bx}}{1 + e^{a+bx}}$.
Odds $o(x) = e^{a+bx}$, logit $\log o(x) = a + bx$.
Fitted using maximum likelihood in R via `glm(y ~ x, family = binomial)`.

**Example 9.11.a.** DDT liver cancer threshold model: $\hat{\alpha} = .005655$.

---

## Problems

1. The following data relate $x$, the moisture of a wet mix of a certain product, to $Y$, the density of the finished product:
   - $(5, 7.4), (6, 9.3), (7, 10.6), (10, 15.4), (12, 18.1), (15, 22.2), (18, 24.1), (20, 24.8)$
   a. Draw a scatter diagram.
   b. Fit a linear curve to the data.

2. Ordered units vs price at six locations:
   - Price: 50, 40, 35, 30, 20, 15
   - Number ordered: 88, 112, 123, 136, 158, 172
   How many units would be ordered if the price were 25?

3. Metal corrosion weight gain vs hours of exposure:
   - $(1.0, .02), (2.0, .03), (2.5, .035), (3.0, .042), (3.5, .05), (4.0, .054)$
   a. Plot a scatter diagram.
   b. Fit a linear relation.
   c. Predict percent weight gain when exposed for 3.2 hours.

4. Wood specific gravity ($x$) vs crushing strength ($y$ psi):
   $$(.41, 1850), (.46, 2620), (.44, 2340), (.47, 2690), (.42, 2160), (.39, 1760), (.41, 2500), (.44, 2750), (.43, 2730), (.44, 3120)$$
   a. Plot scatter diagram.
   b. Estimate regression coefficients.
   c. Predict crushing strength for specific gravity $.43$.

5. Speed-reading program weeks vs speed gain:
   $$(2, 21), (3, 42), (8, 102), (11, 130), (4, 52), (5, 57), (9, 105), (7, 85), (5, 62), (7, 90)$$

6. Infrared spectroscopy rubber readings vs percentage: $(0, .734), (20, .885), (40, 1.050), (60, 1.191), (80, 1.314), (100, 1.432)$. Estimate percentage for reading $1.15$.

7. 1996 SAT scores by state (Table 9.7: Alabama to Wyoming): predict math score from % graduates taking SAT.

8. Verify Equation (9.3.3) for $\text{Var}(A)$.

9. In Problem 4, (a) estimate error variance, (b) find 90% confidence interval for variance.

10. Verify identity $SSR = \frac{S_{xx}S_{YY} - S_{xY}^2}{S_{xx}}$.

11. Sunspots vs auto accident deaths (1970–1983). Test if auto deaths are affected by sunspots.

12. Law school classmates height vs salary ($n = 12$). Test if salary is related to height at $\alpha = .05$.

13. Regression to the mean algebraic properties when $0 < \beta < 1$.

14. Major league batting averages $Y = .159 + .4X + e$. Predict second year for $X = .200, .265, .310$.

15. Flight instructors' praise vs criticism and regression to the mean.

16. Verify distribution of $A$ (Equation 9.4.3).

17. Missing rivets ($x$) vs alignment errors ($y$) for 10 aircraft:
   $$(13, 7), (15, 7), (10, 5), (22, 12), (30, 15), (7, 2), (25, 13), (16, 9), (20, 11), (15, 8)$$
   a. Scatter diagram, b. Estimate coefficients, c. Test $H_0 : \alpha = 1$, d. Expected errors for 24 missing rivets, e. 90% CI.

18. SAT math scores by year (1994–2009).

19–23. Cigarette consumption vs cancer death rates (bladder, lung, kidney, leukemia).

24. Standardized residuals plot for Problem 1.

25. Light absorbed vs liver protein: $(.44, 2), (.82, 16), (1.20, 30), (1.61, 46), (1.83, 55)$.

26. Spot weld diameter vs shear strength ($n = 10$). Test slope $= 1$.

27. High school male age vs weight ($n = 10$). 95% CI for 17-year-olds.

28. Glass refractive index vs density ($n = 18$).

29. Regression through the origin $Y = \beta x + e$. Least squares estimator $B$, distribution, and prediction interval.

30. BMI vs systolic blood pressure ($n = 8$).

31. Weight vs systolic BP for 20 males.

32. Alloy stress vs cycles to failure $S = A/N^m$.

33. Task practice time model $T \approx t s^{-n}$.

34. Swimming pool chlorine residual decay $Y \approx a e^{-bx}$.

35. Heat dissipation $P = 1 - e^{-\alpha t}$.

36. Bacterial count after vaccination.

37. Hydrogen content vs distance from ingot base (quadratic fit).

38. Tumor weight reduction in mice vs drug dose (quadratic fit).

39. Boxcar impact speed vs damaged cans.

40. Weighted regression for reading speed.

41. Coal miners' pneumoconiosis vs years working.

42. Highway accidents vs daily traffic volume (weighted least squares and variance stabilization).

43. River peak discharge vs watershed area and slope.

44. Stream sediment load vs area and discharge.

45. Multiple linear regression fit for given dataset.

46. Stanford heart transplant survival time vs age and mismatch score.

47. Multiple linear regression test of coefficients.

48. Synthetic fiber tensile strength vs cotton percentage and drying time.

49. Machine component time to failure vs voltage, rpm, temperature.

50. Why prediction interval contains confidence interval for mean response.

51. Multiple regression with two independent variables.

52. Power cost per kWh vs load factor and coal cost.

53. Systolic BP vs age and weight.

54–55. Job satisfaction vs income and seniority.

56. Value $x$ where logistic function $p(x) = .5$.

57. Infant gestational age vs breastfeeding (logistic regression).

58. Anger score vs second heart attack (logistic regression).
