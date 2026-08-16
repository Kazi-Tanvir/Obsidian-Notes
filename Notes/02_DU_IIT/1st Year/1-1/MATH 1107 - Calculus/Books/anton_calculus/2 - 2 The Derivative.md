# CHAPTER 2: THE DERIVATIVE

> One of the crowning achievements of calculus is its ability to capture continuous motion mathematically, allowing that motion to be analyzed instant by instant.

Many real-world phenomena involve changing quantities—the speed of a rocket, the inflation of currency, the number of bacteria in a culture, the shock intensity of an earthquake, the voltage of an electrical signal, and so forth. In this chapter we will develop the concept of a "derivative," which is the mathematical tool for studying the rate at which one quantity changes relative to another. The study of rates of change is closely related to the geometric concept of a tangent line to a curve, so we will also be discussing the general definition of a tangent line and methods for finding its slope and equation. Later in the chapter, we will consider some applications of the derivative. These will include ways in which different rates of change can be related as well as the use of linear functions to approximate nonlinear functions.

---

## 2.1 TANGENT LINES AND RATES OF CHANGE

In this section we will discuss three ideas: tangent lines to curves, the velocity of an object moving along a line, and the rate at which one variable changes relative to another. Our goal is to show how these seemingly unrelated ideas are, in actuality, closely linked.

### TANGENT LINES

In Example 1 of Section 1.1, we showed how the notion of a limit could be used to find an equation of a tangent line to a curve. At that stage in the text we did not have precise definitions of tangent lines and limits to work with, so the argument was intuitive and informal. However, now that limits have been defined precisely, we are in a position to give a mathematical definition of the tangent line to a curve $y = f(x)$ at a point $P(x_0, f(x_0))$ on the curve. As illustrated in Figure 2.1.1, consider a point $Q(x, f(x))$ on the curve that is distinct from $P$, and compute the slope $m_{PQ}$ of the secant line through $P$ and $Q$:
$$m_{PQ} = \frac{f(x) - f(x_0)}{x - x_0}$$
If we let $x$ approach $x_0$, then the point $Q$ will move along the curve and approach the point $P$. If the secant line through $P$ and $Q$ approaches a limiting position as $x \to x_0$, then we will regard that position to be the position of the tangent line at $P$. Stated another way, if the slope $m_{PQ}$ of the secant line through $P$ and $Q$ approaches a limit as $x \to x_0$, then we regard that limit to be the slope $m_{\tan}$ of the tangent line at $P$. Thus, we make the following definition.

> **2.1.1 DEFINITION**  
> Suppose that $x_0$ is in the domain of the function $f$. The **tangent line** to the curve $y = f(x)$ at the point $P(x_0, f(x_0))$ is the line with equation
> $$y - f(x_0) = m_{\tan}(x - x_0)$$
> where
> $$m_{\tan} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} \tag{1}$$
> provided the limit exists. For simplicity, we will also call this the tangent line to $y = f(x)$ at $x_0$.

#### Example 1
Use Definition 2.1.1 to find an equation for the tangent line to the parabola $y = x^2$ at the point $P(1, 1)$, and confirm the result agrees with that obtained in Example 1 of Section 1.1.

**Solution.** Applying Formula (1) with $f(x) = x^2$ and $x_0 = 1$, we have
$$m_{\tan} = \lim_{x \to 1} \frac{f(x) - f(1)}{x - 1} = \lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} \frac{(x - 1)(x + 1)}{x - 1} = \lim_{x \to 1} (x + 1) = 2$$
Thus, the tangent line to $y = x^2$ at $(1, 1)$ has equation
$$y - 1 = 2(x - 1) \quad \text{or equivalently} \quad y = 2x - 1$$

There is an alternative way of expressing Formula (1) that is commonly used. If we let $h$ denote the difference $h = x - x_0$, then $x \to x_0 \iff h \to 0$, so:
$$m_{\tan} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} \tag{2}$$

#### Example 2
Compute the slope in Example 1 using Formula (2).

**Solution.**
$$m_{\tan} = \lim_{h \to 0} \frac{f(1 + h) - f(1)}{h} = \lim_{h \to 0} \frac{(1 + h)^2 - 1^2}{h} = \lim_{h \to 0} \frac{1 + 2h + h^2 - 1}{h} = \lim_{h \to 0} (2 + h) = 2$$

#### Example 3
Find an equation for the tangent line to the curve $y = 2/x$ at the point $(2, 1)$ on this curve.

**Solution.**
$$m_{\tan} = \lim_{h \to 0} \frac{f(2 + h) - f(2)}{h} = \lim_{h \to 0} \frac{\frac{2}{2 + h} - 1}{h} = \lim_{h \to 0} \frac{-h}{h(2 + h)} = -\lim_{h \to 0} \frac{1}{2 + h} = -\frac{1}{2}$$
Thus, an equation of the tangent line at $(2, 1)$ is
$$y - 1 = -\frac{1}{2}(x - 2) \quad \text{or equivalently} \quad y = -\frac{1}{2}x + 2$$

#### Example 4
Find the slopes of the tangent lines to the curve $y = \sqrt{x}$ at $x_0 = 1$, $x_0 = 4$, and $x_0 = 9$.

**Solution.** For a general value of $x_0$:
$$m_{\tan} = \lim_{h \to 0} \frac{\sqrt{x_0 + h} - \sqrt{x_0}}{h} = \lim_{h \to 0} \frac{(\sqrt{x_0 + h} - \sqrt{x_0})(\sqrt{x_0 + h} + \sqrt{x_0})}{h(\sqrt{x_0 + h} + \sqrt{x_0})} = \lim_{h \to 0} \frac{h}{h(\sqrt{x_0 + h} + \sqrt{x_0})} = \frac{1}{2\sqrt{x_0}}$$
* Slope at $x_0 = 1$: $\frac{1}{2\sqrt{1}} = \frac{1}{2}$
* Slope at $x_0 = 4$: $\frac{1}{2\sqrt{4}} = \frac{1}{4}$
* Slope at $x_0 = 9$: $\frac{1}{2\sqrt{9}} = \frac{1}{6}$

---

### VELOCITY (RECTILINEAR MOTION)

For motion along a straight line ($s$-axis) where position $s$ is a function of time $t$, $s = f(t)$:
* **Average Velocity** over $[t_0, t_0 + h]$:
  $$v_{\text{ave}} = \frac{\text{change in position}}{\text{time elapsed}} = \frac{f(t_0 + h) - f(t_0)}{h} \tag{4}$$
* **Instantaneous Velocity** at $t_0$:
  $$v_{\text{inst}} = \lim_{h \to 0} \frac{f(t_0 + h) - f(t_0)}{h} \tag{5}$$
Geometrically, $v_{\text{ave}}$ is the slope of the secant line, and $v_{\text{inst}}$ is the slope of the tangent line to the position versus time curve at $P(t_0, f(t_0))$.

#### Example 5 & 6
For position $s = f(t) = 1 + 5t - 2t^2$ (meters, seconds):
* Over $[0, 2]$: $v_{\text{ave}} = \frac{f(2) - f(0)}{2} = \frac{3 - 1}{2} = 1\text{ m/s}$.
* Over $[2, 3]$: $v_{\text{ave}} = \frac{f(3) - f(2)}{1} = \frac{-2 - 3}{1} = -5\text{ m/s}$.
* Instantaneous velocity at $t = 2$:
  $$v_{\text{inst}} = \lim_{h \to 0} \frac{[1 + 5(2 + h) - 2(2 + h)^2] - 3}{h} = \lim_{h \to 0} (-3 - 2h) = -3\text{ m/s}$$

---

### SLOPES AND RATES OF CHANGE

* **Average rate of change** of $y = f(x)$ over $[x_0, x_1]$:
  $$r_{\text{ave}} = \frac{f(x_1) - f(x_0)}{x_1 - x_0} = \frac{f(x_0 + h) - f(x_0)}{h}$$
* **Instantaneous rate of change** of $y$ with respect to $x$ at $x_0$:
  $$r_{\text{inst}} = \lim_{x_1 \to x_0} \frac{f(x_1) - f(x_0)}{x_1 - x_0} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$

#### Example 9
Let $y = x^2 + 1$.
(a) Over $[3, 5]$: $r_{\text{ave}} = \frac{f(5) - f(3)}{5 - 3} = \frac{26 - 10}{2} = 8$.  
(b) At $x = -4$: $r_{\text{inst}} = \lim_{x_1 \to -4} \frac{(x_1^2 + 1) - 17}{x_1 + 4} = \lim_{x_1 \to -4} (x_1 - 4) = -8$.

---

### QUICK CHECK EXERCISES 2.1
*(See page 122 for answers.)*

1. $\lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$.  
2. Tangent line to $y = (x - 1)^2$ at $(-1, 4)$ is $4x + y = 0 \implies \lim_{x \to -1} \frac{x^2 - 2x - 3}{x + 1} = -4$.  
3. $s = 10 - (3 - t)^2, \; 0 \le t \le 5$: (a) Moves 9 ft in positive direction, reverses, travels 4 ft (b) $v_{\text{ave}} = 1\text{ ft/s}$.  
4. Tangent line at $t = 2$ with $s(2) = -1, v(2) = 3$ is $s - (-1) = 3(t - 2) \implies s = 3t - 7$.  
5. $y = x^2 + x$: (a) $r_{\text{ave}} = 8$ over $[2, 5]$ (b) $r_{\text{inst}} = \lim_{x \to 2} \frac{(x^2 + x) - 6}{x - 2}$.

#### QUICK CHECK ANSWERS 2.1
1. $\frac{f(x) - f(x_0)}{x - x_0}; \frac{f(x_0 + h) - f(x_0)}{h}$  
2. $-4$  
3. (a) 9; positive; 4 (b) $1\text{ ft/s}$  
4. $s = 3t - 7$  
5. (a) 8 (b) $\lim_{x \to 2} \frac{(x^2 + x) - 6}{x - 2}$ or $\lim_{h \to 0} \frac{[(2 + h)^2 + (2 + h)] - 6}{h}$  

---

## 2.2 THE DERIVATIVE FUNCTION

### DEFINITION OF THE DERIVATIVE FUNCTION

> **2.2.1 DEFINITION**  
> The function $f'$ defined by the formula
> $$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} \tag{2}$$
> is called the **derivative of $f$ with respect to $x$**. The domain of $f'$ consists of all $x$ in the domain of $f$ for which the limit exists.

The expression $\frac{f(x + h) - f(x)}{h}$ is called the **difference quotient**.

#### Finding an Equation for the Tangent Line to $y = f(x)$ at $x = x_0$:
* **Step 1.** Evaluate $f(x_0)$; the point of tangency is $(x_0, f(x_0))$.
* **Step 2.** Find $f'(x)$ and evaluate $f'(x_0)$, which is the slope $m$ of the line.
* **Step 3.** Substitute $m$ and $(x_0, f(x_0))$ into the point-slope form:
  $$y - f(x_0) = f'(x_0)(x - x_0) \tag{3}$$

#### Example 1 & 2
* For $f(x) = x^2$: $f'(x) = 2x$. At $x = 2$, slope is 4, tangent line is $y - 4 = 4(x - 2) \implies y = 4x - 4$.
* For $f(x) = x^3 - x$: $f'(x) = 3x^2 - 1$.
* For linear function $f(x) = mx + b$: $f'(x) = m$.
* For $f(x) = \sqrt{x}$: $f'(x) = \frac{1}{2\sqrt{x}}$.

#### Velocity Function:
$$v(t) = s'(t) = \lim_{h \to 0} \frac{s(t + h) - s(t)}{h}$$

---

### DIFFERENTIABILITY

> **2.2.2 DEFINITION**  
> A function $f$ is said to be **differentiable at $x_0$** if the limit
> $$f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$
> exists. If $f$ is differentiable at each point of the open interval $(a, b)$, then it is differentiable on $(a, b)$. If differentiable on $(-\infty, +\infty)$, $f$ is **differentiable everywhere**.

Common ways differentiability fails at a continuous point:
* **Corner points** (left and right limits of difference quotients are different finite values, e.g., $f(x) = |x|$ at $x = 0$).
* **Points of vertical tangency** (slopes of secant lines approach $+\infty$ or $-\infty$).

> **2.2.3 THEOREM (Differentiability Implies Continuity)**  
> If a function $f$ is differentiable at $x_0$, then $f$ is continuous at $x_0$.  
> *(Contrapositive: If $f$ is not continuous at $x_0$, then $f$ is not differentiable at $x_0$.)*

> **WARNING**  
> The converse of Theorem 2.2.3 is false: continuity does not imply differentiability (e.g., $f(x) = |x|$ at $x = 0$).

> **Bernhard Bolzano (1781–1848)**  
> Discovered continuous functions that are nowhere differentiable, initiating modern rigorous analysis.

---

### OTHER DERIVATIVE NOTATIONS

$$f'(x) = \frac{d}{dx}[f(x)] = D_x[f(x)] = y' = \frac{dy}{dx}$$
With increments $\Delta x = h$ and $\Delta y = f(x + \Delta x) - f(x)$:
$$\frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}$$
Alternative form:
$$f'(x) = \lim_{w \to x} \frac{f(w) - f(x)}{w - x}$$

---

### QUICK CHECK EXERCISES 2.2
*(See page 134 for answers.)*
1. Limit definition of $f'(x)$.  
2. (a) $(x^2)' = 2x$ (b) $(\sqrt{x})' = \frac{1}{2\sqrt{x}}$.  
3. Tangent line $2x + 3y = 5$ at $x = 1 \implies f(1) = 1, f'(1) = -2/3$.  
4. Theorem 2.2.3 (Differentiability implies continuity).

---

## 2.3 INTRODUCTION TO TECHNIQUES OF DIFFERENTIATION

### BASIC RULES

> **2.3.1 THEOREM (Constant Rule)**  
> $$\frac{d}{dx}[c] = 0 \tag{1}$$

> **2.3.2 & 2.3.3 THEOREMS (Power Rule & Extended Power Rule)**  
> For any real number $r$:
> $$\frac{d}{dx}[x^r] = rx^{r-1} \tag{7}$$

> **2.3.4 THEOREM (Constant Multiple Rule)**  
> $$\frac{d}{dx}[cf(x)] = c\frac{d}{dx}[f(x)] \tag{8}$$

> **2.3.5 THEOREM (Sum and Difference Rules)**  
> $$\frac{d}{dx}[f(x) \pm g(x)] = \frac{d}{dx}[f(x)] \pm \frac{d}{dx}[g(x)] \tag{9–10}$$

#### Higher Derivatives:
$$y'' = f''(x) = \frac{d^2y}{dx^2}, \quad y''' = f'''(x) = \frac{d^3y}{dx^3}, \quad y^{(n)} = f^{(n)}(x) = \frac{d^ny}{dx^n}$$

---

### QUICK CHECK EXERCISES 2.3
*(See page 142 for answers.)*
1. (a) $\frac{d}{dx}[\sqrt{6}] = 0$ (b) $\frac{d}{dx}[\sqrt{6}x] = \sqrt{6}$ (c) $\frac{d}{dx}[6\sqrt{x}] = \frac{3}{\sqrt{x}}$ (d) $\frac{d}{dx}[\sqrt{6x}] = \frac{\sqrt{6}}{2\sqrt{x}}$  
2. (a) $(x^3 + 5)' = 3x^2$ (b) $(x^5 + 5x^2)' = 5x^4 + 10x$ (c) $(\frac{x^3 + 5}{2})' = \frac{3}{2}x^2$ (d) $(x + 5x^{-2})' = 1 - 10x^{-3}$  
3. Slope of tangent line to $y = x^2 + 4x + 7$ at $x = 1$ is $2(1) + 4 = 6$.  
4. For $f(x) = 3x^3 - 3x^2 + x + 1 \implies f''(x) = 18x - 6$.

---

## 2.4 THE PRODUCT AND QUOTIENT RULES

### PRODUCT RULE

> **2.4.1 THEOREM (The Product Rule)**  
> If $f$ and $g$ are differentiable at $x$, then:
> $$\frac{d}{dx}[f(x)g(x)] = f(x)\frac{d}{dx}[g(x)] + g(x)\frac{d}{dx}[f(x)] \tag{1}$$
> In prime notation:
> $$(f \cdot g)' = f \cdot g' + g \cdot f'$$

---

### QUOTIENT RULE

> **2.4.2 THEOREM (The Quotient Rule)**  
> If $f$ and $g$ are differentiable at $x$ and $g(x) \neq 0$, then:
> $$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x)\frac{d}{dx}[f(x)] - f(x)\frac{d}{dx}[g(x)]}{[g(x)]^2} \tag{2}$$
> In prime notation:
> $$\left(\frac{f}{g}\right)' = \frac{g \cdot f' - f \cdot g'}{g^2}$$

#### Reciprocal Rule:
$$\left(\frac{1}{g}\right)' = -\frac{g'}{g^2}$$

---

### SUMMARY OF DIFFERENTIATION RULES (Table 2.4.1)

| Rule | Formula |
| :--- | :--- |
| **Constant** | $\frac{d}{dx}[c] = 0$ |
| **Power** | $\frac{d}{dx}[x^r] = rx^{r-1}$ |
| **Constant Multiple** | $(cf)' = cf'$ |
| **Sum / Difference** | $(f \pm g)' = f' \pm g'$ |
| **Product** | $(f \cdot g)' = f \cdot g' + g \cdot f'$ |
| **Quotient** | $(f/g)' = \frac{g \cdot f' - f \cdot g'}{g^2}$ |
| **Reciprocal** | $(1/g)' = -\frac{g'}{g^2}$ |

---

### QUICK CHECK EXERCISES 2.4
*(See page 148 for answers.)*
1. (a) $\frac{d}{dx}[x^2 f(x)] = x^2 f'(x) + 2x f(x)$  
   (b) $\frac{d}{dx}[\frac{f(x)}{x^2 + 1}] = \frac{(x^2 + 1)f'(x) - 2x f(x)}{(x^2 + 1)^2}$  
   (c) $\frac{d}{dx}[\frac{x^2 + 1}{f(x)}] = \frac{2x f(x) - (x^2 + 1)f'(x)}{[f(x)]^2}$  
2. Given $f(1) = -1, f'(1) = 2, g(1) = 3, g'(1) = -1$:  
   (a) $(2f - 3g)'(1) = 2(2) - 3(-1) = 7$  
   (b) $(f^2)'(1) = 2f(1)f'(1) = 2(-1)(2) = -4$  
   (c) $(fg)'(1) = f(1)g'(1) + g(1)f'(1) = (-1)(-1) + (3)(2) = 7$  
   (d) $(f/g)'(1) = \frac{g(1)f'(1) - f(1)g'(1)}{[g(1)]^2} = \frac{3(2) - (-1)(-1)}{9} = \frac{5}{9}$

---

## 2.5 DERIVATIVES OF TRIGONOMETRIC FUNCTIONS

### DERIVATIVE FORMULAS (RADIANS)

$$\begin{aligned}
\frac{d}{dx}[\sin x] &= \cos x & \frac{d}{dx}[\cos x] &= -\sin x \\
\frac{d}{dx}[\tan x] &= \sec^2 x & \frac{d}{dx}[\cot x] &= -\csc^2 x \\
\frac{d}{dx}[\sec x] &= \sec x \tan x & \frac{d}{dx}[\csc x] &= -\csc x \cot x
\end{aligned}$$

#### Key Limit Ingredients:
$$\lim_{h \to 0} \frac{\sin h}{h} = 1 \quad \text{and} \quad \lim_{h \to 0} \frac{1 - \cos h}{h} = 0$$

---

### QUICK CHECK EXERCISES 2.5
*(See page 153 for answers.)*
1. Derivatives of $\sin x, \cos x, \tan x, \sec x$.  
2. $f(x) = \sin x \cos x \implies f'(x) = \cos^2 x - \sin^2 x$, $f'(\pi/3) = (1/2)^2 - (\sqrt{3}/2)^2 = -1/2$.  
3. (a) $\frac{d}{dx}[\sin x]|_{x=\pi/2} = \cos(\pi/2) = 0$ (b) $\frac{d}{dx}[\csc x] = -\csc x \cot x$.

---

## 2.6 THE CHAIN RULE

### DERIVATIVES OF COMPOSITIONS

> **2.6.1 THEOREM (The Chain Rule)**  
> If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then $y = f(g(x))$ is differentiable at $x$, and
> $$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} \quad \text{where } u = g(x) \tag{1}$$
> In function notation:
> $$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x) \tag{2}$$

#### Generalized Derivative Formulas (Table 2.6.1):
$$\begin{aligned}
\frac{d}{dx}[u^r] &= ru^{r-1}\frac{du}{dx} & \frac{d}{dx}[\sin u] &= \cos u \frac{du}{dx} \\
\frac{d}{dx}[\cos u] &= -\sin u \frac{du}{dx} & \frac{d}{dx}[\tan u] &= \sec^2 u \frac{du}{dx} \\
\frac{d}{dx}[\cot u] &= -\csc^2 u \frac{du}{dx} & \frac{d}{dx}[\sec u] &= \sec u \tan u \frac{du}{dx} \\
\frac{d}{dx}[\csc u] &= -\csc u \cot u \frac{du}{dx}
\end{aligned}$$

---

### QUICK CHECK EXERCISES 2.6
*(See page 160 for answers.)*
1. outside; inside; inside  
2. $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$  
3. (a) $\frac{d}{dx}[(x^2 + 5)^{10}] = 20x(x^2 + 5)^9$ (b) $\frac{d}{dx}[\sqrt{1 + 6x}] = \frac{3}{\sqrt{1 + 6x}}$  
4. (a) $3\cos(3x + 2)$ (b) $4(x^2\tan x)^3(2x\tan x + x^2\sec^2 x)$  
5. (a) $g'(f(2))f'(2) = g'(3)(4) = -5(4) = -20$ (b) $f'(\frac{1}{3}g(3))\cdot \frac{1}{3}g'(3) = f'(2)\cdot \frac{1}{3}(-5) = -\frac{20}{3}$

---

## 2.7 IMPLICIT DIFFERENTIATION

### FUNCTIONS DEFINED IMPLICITLY

When an equation $F(x, y) = 0$ defines $y$ as a differentiable function of $x$ implicitly:
* Differentiate both sides with respect to $x$, applying the chain rule to terms involving $y$ (e.g., $\frac{d}{dx}[y^n] = ny^{n-1}\frac{dy}{dx}$, $\frac{d}{dx}[\sin y] = \cos y \frac{dy}{dx}$).
* Solve the resulting algebraic equation for $\frac{dy}{dx}$.

> **René Descartes (1596–1650)**  
> Founder of analytic geometry (*Folium of Descartes*: $x^3 + y^3 = 3xy$).

#### Example 2
$$5y^2 + \sin y = x^2 \implies 10y\frac{dy}{dx} + \cos y \frac{dy}{dx} = 2x \implies \frac{dy}{dx} = \frac{2x}{10y + \cos y}$$

#### Example 3 (Higher Derivatives)
$$4x^2 - 2y^2 = 9 \implies \frac{dy}{dx} = \frac{2x}{y} \implies \frac{d^2y}{dx^2} = \frac{2y - 2x(2x/y)}{y^2} = \frac{2y^2 - 4x^2}{y^3} = -\frac{9}{y^3}$$

---

### QUICK CHECK EXERCISES 2.7
*(See page 167 for answers.)*
1. $xy + 2y = 1 \implies y = \frac{1}{x + 2}$.  
2. $x^2 - y^3 = xy \implies \frac{dy}{dx} = \frac{2x - y}{x + 3y^2}$.  
3. $x + y + xy = 3$ at $(1, 1) \implies \text{slope} = -1$.  
4. $\sin y = x \implies \frac{d^2y}{dx^2} = \sec^2 y \tan y$.

---

## 2.8 RELATED RATES

In related rates problems, we relate unknown rates of change to known rates of change using the chain rule.

### 5-STEP STRATEGY FOR SOLVING RELATED RATES PROBLEMS
1. **Assign variables** to all quantities that vary with time.
2. **Identify known and unknown rates of change** as derivatives with respect to $t$.
3. **Write an equation** relating the variables (often using geometric formulas or Pythagorean theorem).
4. **Differentiate both sides** with respect to $t$ using the chain rule.
5. **Substitute known values** and solve for the required rate of change.

#### Examples:
* **Spreading Oil Spill:** $A = \pi r^2 \implies \frac{dA}{dt} = 2\pi r \frac{dr}{dt}$.
* **Baseball Runner:** $x^2 + 90^2 = y^2 \implies 2x\frac{dx}{dt} = 2y\frac{dy}{dt} \implies \frac{dy}{dt} = \frac{x}{y}\frac{dx}{dt}$.
* **Rocket Tracking Camera:** $\tan \phi = \frac{h}{3000} \implies \sec^2\phi \frac{d\phi}{dt} = \frac{1}{3000}\frac{dh}{dt}$.
* **Conical Filter:** $V = \frac{1}{3}\pi r^2 y$, with $r = \frac{1}{4}y \implies V = \frac{\pi}{48}y^3 \implies \frac{dV}{dt} = \frac{\pi}{16}y^2 \frac{dy}{dt}$.

---

### QUICK CHECK EXERCISES 2.8
*(See page 175 for answers.)*
1. $A = x^2, \frac{dx}{dt} = 3 \implies \frac{dA}{dt}\big|_{x=10} = 2(10)(3) = 60$.  
2. $A = x^2, \frac{dA}{dt} = 3 \implies \frac{dx}{dt}\big|_{x=10} = \frac{3}{20}$.  
3. Ladder $x^2 + y^2 = 100 \implies x\frac{dx}{dt} + y\frac{dy}{dt} = 0$.  
4. Cylinder $V = \pi r^2 h \implies \frac{dV}{dt} = 2\pi rh \frac{dr}{dt} + \pi r^2 \frac{dh}{dt}$.

---

## 2.9 LOCAL LINEAR APPROXIMATION; DIFFERENTIALS

### LOCAL LINEAR APPROXIMATION

For $x$ near $x_0$:
$$f(x) \approx f(x_0) + f'(x_0)(x - x_0) \tag{1}$$
$$f(x_0 + \Delta x) \approx f(x_0) + f'(x_0)\Delta x \tag{2}$$

#### Examples:
* $\sqrt{x} \approx 1 + \frac{1}{2}(x - 1)$ near $x_0 = 1 \implies \sqrt{1.1} \approx 1 + 0.05 = 1.05$.
* $\sin x \approx x$ near $x_0 = 0 \implies \sin 2^\circ \approx 0.0349066$.
* $(1 + x)^k \approx 1 + kx$ near $x_0 = 0$.

---

### DIFFERENTIALS

Let $dx = \Delta x$ be an independent variable. Then the **differential** $dy$ is defined by:
$$dy = f'(x) dx \tag{5}$$
* $\Delta y = f(x + \Delta x) - f(x)$ represents the actual change along the curve.
* $dy$ represents the change along the tangent line.
* $\Delta y \approx dy = f'(x) dx$.

### ERROR PROPAGATION
* **Measurement error:** $dx = \Delta x = x - x_0$
* **Propagated error:** $\Delta y \approx dy = f'(x) dx$
* **Relative error:** $\frac{dq}{q}$
* **Percentage error:** $\frac{dq}{q} \times 100\%$

---

### QUICK CHECK EXERCISES 2.9
*(See page 183 for answers.)*
1. tangent; $f(x)$; $x_0$  
2. $y = 5 - x^2$ at $x_0 = 2 \implies y = 1 - 4(x - 2) = -4x + 9$.  
3. $y = 5 - x^2$: $dy = -0.4, \Delta y = -0.41$.  
4. Percentage error in intensity: within $\pm 1\%$.

---

## CHAPTER 2 REVIEW EXERCISES
Exercises 1–64 reviewing all differentiation rules, tangent lines, rectilinear motion, implicit differentiation, related rates, and differentials.

---

## CHAPTER 2 MAKING CONNECTIONS
Explores functions satisfying $f(x + y) = f(x)f(y)$, derivatives of products of $n$ functions by induction, multiple forms of quotient rule derivation, and robotics applications.
