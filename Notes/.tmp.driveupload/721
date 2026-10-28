# CHAPTER 2: THE DERIVATIVE

> One of the crowning achievements of calculus is its ability to capture continuous motion mathematically, allowing that motion to be analyzed instant by instant.

Many real-world phenomena involve changing quantities—the speed of a rocket, the inflation of currency, the number of bacteria in a culture, the shock intensity of an earthquake, the voltage of an electrical signal, and so forth. In this chapter we will develop the concept of a "derivative," which is the mathematical tool for studying the rate at which one quantity changes relative to another. The study of rates of change is closely related to the geometric concept of a tangent line to a curve, so we will also be discussing the general definition of a tangent line and methods for finding its slope and equation. Later in the chapter, we will consider some applications of the derivative. These will include ways in which different rates of change can be related as well as the use of linear functions to approximate nonlinear functions.

---

## 2.1 TANGENT LINES AND RATES OF CHANGE

In this section we will discuss three ideas: tangent lines to curves, the velocity of an object moving along a line, and the rate at which one variable changes relative to another. Our goal is to show how these seemingly unrelated ideas are, in actuality, closely linked.

### TANGENT LINES

In Example 1 of Section 1.1, we showed how the notion of a limit could be used to find an equation of a tangent line to a curve. At that stage in the text we did not have precise definitions of tangent lines and limits to work with, so the argument was intuitive and informal. However, now that limits have been defined precisely, we are in a position to give a mathematical definition of the tangent line to a curve $y = f(x)$ at a point $P(x_0, f(x_0))$ on the curve. As illustrated in Figure 2.1.1, consider a point $Q(x, f(x))$ on the curve that is distinct from $P$, and compute the slope $m_{PQ}$ of the secant line through $P$ and $Q$:
$$m_{PQ} = \frac{f(x) - f(x_0)}{x - x_0}$$

If we let $x$ approach $x_0$, then the point $Q$ will move along the curve and approach the point $P$. If the secant line through $P$ and $Q$ approaches a limiting position as $x \to x_0$, then we will regard that position to be the position of the tangent line at $P$. Stated another way, if the slope $m_{PQ}$ of the secant line through $P$ and $Q$ approaches a limit as $x \to x_0$, then we regard that limit to be the slope $m_{\text{tan}}$ of the tangent line at $P$. Thus, we make the following definition.

> **2.1.1 DEFINITION**  
> Suppose that $x_0$ is in the domain of the function $f$. The **tangent line** to the curve $y = f(x)$ at the point $P(x_0, f(x_0))$ is the line with equation
> $$y - f(x_0) = m_{\text{tan}}(x - x_0)$$
> where
> $$m_{\text{tan}} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} \tag{1}$$
> provided the limit exists. For simplicity, we will also call this the *tangent line to $y = f(x)$ at $x_0$*.

#### Example 1
Use Definition 2.1.1 to find an equation for the tangent line to the parabola $y = x^2$ at the point $P(1, 1)$, and confirm the result agrees with that obtained in Example 1 of Section 1.1.

**Solution.** Applying Formula (1) with $f(x) = x^2$ and $x_0 = 1$, we have
$$m_{\text{tan}} = \lim_{x \to 1} \frac{f(x) - f(1)}{x - 1} = \lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1} \frac{(x - 1)(x + 1)}{x - 1} = \lim_{x \to 1} (x + 1) = 2$$
Thus, the tangent line to $y = x^2$ at $(1, 1)$ has equation
$$y - 1 = 2(x - 1) \quad \text{or equivalently} \quad y = 2x - 1$$
which agrees with Example 1 of Section 1.1.

There is an alternative way of expressing Formula (1) that is commonly used. If we let $h$ denote the difference $h = x - x_0$, then the statement that $x \to x_0$ is equivalent to the statement $h \to 0$, so we can rewrite (1) in terms of $x_0$ and $h$ as
$$m_{\text{tan}} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} \tag{2}$$

#### Example 2
Compute the slope in Example 1 using Formula (2).

**Solution.** Applying Formula (2) with $f(x) = x^2$ and $x_0 = 1$, we obtain
$$m_{\text{tan}} = \lim_{h \to 0} \frac{f(1 + h) - f(1)}{h} = \lim_{h \to 0} \frac{(1 + h)^2 - 1^2}{h} = \lim_{h \to 0} \frac{1 + 2h + h^2 - 1}{h} = \lim_{h \to 0} (2 + h) = 2$$
which agrees with the slope found in Example 1.

#### Example 3
Find an equation for the tangent line to the curve $y = 2/x$ at the point $(2, 1)$ on this curve.

**Solution.** First, we will find the slope of the tangent line by applying Formula (2) with $f(x) = 2/x$ and $x_0 = 2$. This yields
$$m_{\text{tan}} = \lim_{h \to 0} \frac{f(2 + h) - f(2)}{h} = \lim_{h \to 0} \frac{\frac{2}{2 + h} - 1}{h} = \lim_{h \to 0} \frac{\frac{2 - (2 + h)}{2 + h}}{h} = \lim_{h \to 0} \frac{-h}{h(2 + h)} = -\lim_{h \to 0} \frac{1}{2 + h} = -\frac{1}{2}$$
Thus, an equation of the tangent line at $(2, 1)$ is
$$y - 1 = -\frac{1}{2}(x - 2) \quad \text{or equivalently} \quad y = -\frac{1}{2}x + 2$$

#### Example 4
Find the slopes of the tangent lines to the curve $y = \sqrt{x}$ at $x_0 = 1, x_0 = 4,$ and $x_0 = 9$.

**Solution.** We could compute each of these slopes separately, but it will be more efficient to find the slope for a general value of $x_0$ and then substitute the specific numerical values. Proceeding in this way we obtain
$$m_{\text{tan}} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} = \lim_{h \to 0} \frac{\sqrt{x_0 + h} - \sqrt{x_0}}{h}$$
$$= \lim_{h \to 0} \frac{\sqrt{x_0 + h} - \sqrt{x_0}}{h} \cdot \frac{\sqrt{x_0 + h} + \sqrt{x_0}}{\sqrt{x_0 + h} + \sqrt{x_0}} = \lim_{h \to 0} \frac{x_0 + h - x_0}{h(\sqrt{x_0 + h} + \sqrt{x_0})} = \lim_{h \to 0} \frac{1}{\sqrt{x_0 + h} + \sqrt{x_0}} = \frac{1}{2\sqrt{x_0}}$$
The slopes at $x_0 = 1, 4,$ and $9$ can now be obtained by substituting these values into our general formula for $m_{\text{tan}}$:
* slope at $x_0 = 1$: $\frac{1}{2\sqrt{1}} = \frac{1}{2}$
* slope at $x_0 = 4$: $\frac{1}{2\sqrt{4}} = \frac{1}{4}$
* slope at $x_0 = 9$: $\frac{1}{2\sqrt{9}} = \frac{1}{6}$

---

### VELOCITY

To describe the motion of an object completely, one must specify its speed (how fast it is going) and the direction in which it is moving. The speed and the direction of motion together comprise what is called the **velocity** of the object. For now we will only consider motion along a line; this is called **rectilinear motion**.

If a particle in rectilinear motion moves along an $s$-axis so that its position coordinate as a function of the elapsed time $t$ is
$$s = f(t) \tag{3}$$
then $f$ is called the **position function** of the particle; the graph of (3) is the **position versus time curve**. The **average velocity** of the particle over a time interval $[t_0, t_0 + h], h > 0$, is defined to be
$$v_{\text{ave}} = \frac{\text{change in position}}{\text{time elapsed}} = \frac{f(t_0 + h) - f(t_0)}{h} \tag{4}$$

#### Example 5
Suppose that $s = f(t) = 1 + 5t - 2t^2$ is the position function of a particle, where $s$ is in meters and $t$ is in seconds. Find the average velocities of the particle over the time intervals (a) $[0, 2]$ and (b) $[2, 3]$.

**Solution (a).** Applying (4) with $t_0 = 0$ and $h = 2$:
$$v_{\text{ave}} = \frac{f(2) - f(0)}{2} = \frac{3 - 1}{2} = 1\text{ m/s}$$

**Solution (b).** Applying (4) with $t_0 = 2$ and $h = 1$:
$$v_{\text{ave}} = \frac{f(3) - f(2)}{1} = \frac{-2 - 3}{1} = -5\text{ m/s}$$

We define the **instantaneous velocity** $v_{\text{inst}}$ of the particle at time $t_0$ to be the limit as $h \to 0$ of its average velocities $v_{\text{ave}}$ over time intervals between $t = t_0$ and $t = t_0 + h$:
$$v_{\text{inst}} = \lim_{h \to 0} \frac{f(t_0 + h) - f(t_0)}{h} \tag{5}$$

#### Example 6
Consider the particle in Example 5, whose position function is $s = f(t) = 1 + 5t - 2t^2$. Find the particle's instantaneous velocity at time $t = 2\text{ s}$.

**Solution.**
$$\text{instantaneous velocity} = \lim_{h \to 0} \frac{[1 + 5(2 + h) - 2(2 + h)^2] - 3}{h} = \lim_{h \to 0} \frac{-3h - 2h^2}{h} = \lim_{h \to 0} (-3 - 2h) = -3\text{ m/s}$$

Table 2.1.1 shows average velocities over smaller and smaller intervals approaching $-3\text{ m/s}$:

#### Table 2.1.1
| Time Interval | Average Velocity (m/s) |
| :--- | :---: |
| $2.0 \le t \le 3.0$ | $-5$ |
| $2.0 \le t \le 2.1$ | $-3.2$ |
| $2.0 \le t \le 2.01$ | $-3.02$ |
| $2.0 \le t \le 2.001$ | $-3.002$ |
| $2.0 \le t \le 2.0001$ | $-3.0002$ |

Geometrically, the instantaneous velocity $v_{\text{inst}}$ at time $t_0$ is the slope of the tangent line to the position versus time curve at the point $P(t_0, f(t_0))$.

---

### SLOPES AND RATES OF CHANGE

If $y = f(x)$, then we define the **average rate of change** of $y$ with respect to $x$ over the interval $[x_0, x_1]$ to be
$$r_{\text{ave}} = \frac{f(x_1) - f(x_0)}{x_1 - x_0} \tag{8}$$
and we define the **instantaneous rate of change** of $y$ with respect to $x$ at $x_0$ to be
$$r_{\text{inst}} = \lim_{x_1 \to x_0} \frac{f(x_1) - f(x_0)}{x_1 - x_0} \tag{9}$$

With $h = x_1 - x_0$:
$$r_{\text{ave}} = \frac{f(x_0 + h) - f(x_0)}{h} \tag{10}$$
$$r_{\text{inst}} = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} \tag{11}$$

#### Example 7
Find the rate of change of $y$ with respect to $x$ if (a) $y = 2x - 1$ (b) $y = -5x + 1$.

**Solution (a).** The slope is $m = 2$, so each 1-unit increase in $x$ produces a 2-unit increase in $y$.  
**Solution (b).** The slope is $m = -5$, so each 1-unit increase in $x$ produces a 5-unit decrease in $y$.

#### Example 8
A uniform rod of length $40\text{ cm} = 0.4\text{ m}$ is thermally insulated around its lateral surface with ends held at $25^\circ\text{C}$ and $5^\circ\text{C}$.  
If $x$ is in cm: $m = \frac{5 - 25}{40 - 0} = -0.5^\circ\text{C/cm}$.  
If $x$ is in m: $m = \frac{5 - 25}{0.4 - 0} = -50^\circ\text{C/m}$.

#### Example 9
Let $y = x^2 + 1$.  
(a) Find the average rate of change of $y$ with respect to $x$ over $[3, 5]$.  
(b) Find the instantaneous rate of change of $y$ with respect to $x$ when $x = -4$.

**Solution (a).** $r_{\text{ave}} = \frac{f(5) - f(3)}{5 - 3} = \frac{26 - 10}{2} = 8$.  
**Solution (b).** $r_{\text{inst}} = \lim_{x_1 \to -4} \frac{(x_1^2 + 1) - 17}{x_1 + 4} = \lim_{x_1 \to -4} (x_1 - 4) = -8$.

#### Example 10
Figure 2.1.12 shows a stress-test graph of cardiac output $V$ in liters (L) versus workload $W$ in $\text{kg}\cdot\text{m}$.  
(a) Using secant line through $(300, 13)$ and $(1200, 19)$: $r_{\text{ave}} \approx \frac{19 - 13}{1200 - 300} \approx 0.0067\text{ L}/(\text{kg}\cdot\text{m})$.  
(b) Using tangent line through $(0, 7)$ and $(900, 25)$ at $W = 300$: $r_{\text{inst}} \approx \frac{25 - 7}{900 - 0} = 0.02\text{ L}/(\text{kg}\cdot\text{m})$.

---

### QUICK CHECK EXERCISES 2.1
*(See page 122 for answers.)*

1. The slope $m_{\text{tan}}$ of the tangent line to the curve $y = f(x)$ at the point $P(x_0, f(x_0))$ is given by
   $$m_{\text{tan}} = \lim_{x \to x_0} \underline{\hspace{1.5cm}} = \lim_{h \to 0} \underline{\hspace{1.5cm}}$$
2. The tangent line to the curve $y = (x - 1)^2$ at the point $(-1, 4)$ has equation $4x + y = 0$. Thus, the value of the limit
   $$\lim_{x \to -1} \frac{x^2 - 2x - 3}{x + 1}$$
   is $\underline{\hspace{1cm}}$.
3. A particle is moving along an $s$-axis, where $s$ is in feet. During the first 5 seconds of motion, the position of the particle is given by
   $$s = 10 - (3 - t)^2, \quad 0 \le t \le 5$$
   Use this position function to complete each part:  
   (a) Initially, the particle moves a distance of $\underline{\hspace{1cm}}\text{ ft}$ in the (positive/negative) direction; then it reverses direction, traveling a distance of $\underline{\hspace{1cm}}\text{ ft}$ during the remainder of the 5-second period.  
   (b) The average velocity of the particle over the 5-second period is $\underline{\hspace{1cm}}$.
4. Let $s = f(t)$ be the equation of a position versus time curve for a particle in rectilinear motion, where $s$ is in meters and $t$ is in seconds. Assume that $s = -1$ when $t = 2$ and that the instantaneous velocity of the particle at this instant is $3\text{ m/s}$. The equation of the tangent line to the position versus time curve at time $t = 2$ is $\underline{\hspace{1cm}}$.
5. Suppose that $y = x^2 + x$.  
   (a) The average rate of change of $y$ with respect to $x$ over the interval $2 \le x \le 5$ is $\underline{\hspace{1cm}}$.  
   (b) The instantaneous rate of change of $y$ with respect to $x$ at $x = 2$, $r_{\text{inst}}$, is given by the limit $\underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 2.1
1. $\frac{f(x) - f(x_0)}{x - x_0}; \quad \frac{f(x_0 + h) - f(x_0)}{h}$  
2. $-4$  
3. (a) $9$; positive; $4$ (b) $1\text{ ft/s}$  
4. $s = 3t - 7$  
5. (a) $8$ (b) $\lim_{x \to 2} \frac{(x^2 + x) - 6}{x - 2}$ or $\lim_{h \to 0} \frac{[(2 + h)^2 + (2 + h)] - 6}{h}$

---

### EXERCISE SET 2.1

1. The accompanying figure shows the position versus time curve for an elevator that moves upward a distance of $60\text{ m}$ and then discharges its passengers.  
   (a) Estimate the instantaneous velocity of the elevator at $t = 10\text{ s}$.  
   (b) Sketch a velocity versus time curve for the motion of the elevator for $0 \le t \le 20$.
2. The accompanying figure shows the position versus time curve for an automobile over a period of time of $10\text{ s}$. Use the line segments shown in the figure to estimate the instantaneous velocity of the automobile at time $t = 4\text{ s}$ and again at time $t = 8\text{ s}$.
3. The accompanying figure shows the position versus time curve for a certain particle moving along a straight line. Estimate each of the following from the graph:  
   (a) the average velocity over the interval $0 \le t \le 3$  
   (b) the values of $t$ at which the instantaneous velocity is zero  
   (c) the values of $t$ at which the instantaneous velocity is either a maximum or a minimum  
   (d) the instantaneous velocity when $t = 3\text{ s}$.
4. The accompanying figure shows the position versus time curves of four different particles moving on a straight line. For each particle, determine whether its instantaneous velocity is increasing or decreasing with time.

**FOCUS ON CONCEPTS**

5. If a particle moves at constant velocity, what can you say about its position versus time curve?
6. An automobile, initially at rest, begins to move along a straight track. The velocity increases steadily until suddenly the driver sees a concrete barrier in the road and applies the brakes sharply at time $t_0$. The car decelerates rapidly, but it is too late—the car crashes into the barrier at time $t_1$ and instantaneously comes to rest. Sketch a position versus time curve that might represent the motion of the car. Indicate how characteristics of your curve correspond to the events of this scenario.

**7–10 For each exercise, sketch a curve and a line $L$ satisfying the stated conditions.**

7. $L$ is tangent to the curve and intersects the curve in at least two points.
8. $L$ intersects the curve in exactly one point, but $L$ is not tangent to the curve.
9. $L$ is tangent to the curve at two different points.
10. $L$ is tangent to the curve at two different points and intersects the curve at a third point.

**11–14 A function $y = f(x)$ and values of $x_0$ and $x_1$ are given.**  
**(a) Find the average rate of change of $y$ with respect to $x$ over the interval $[x_0, x_1]$.**  
**(b) Find the instantaneous rate of change of $y$ with respect to $x$ at the specified value of $x_0$.**  
**(c) Find the instantaneous rate of change of $y$ with respect to $x$ at an arbitrary value of $x_0$.**  
**(d) The average rate of change in part (a) is the slope of a certain secant line, and the instantaneous rate of change in part (b) is the slope of a certain tangent line. Sketch the graph of $y = f(x)$ together with those two lines.**

11. $y = 2x^2; \quad x_0 = 0, x_1 = 1$
12. $y = x^3; \quad x_0 = 1, x_1 = 2$
13. $y = 1/x; \quad x_0 = 2, x_1 = 3$
14. $y = 1/x^2; \quad x_0 = 1, x_1 = 2$

**15–18 A function $y = f(x)$ and an $x$-value $x_0$ are given.**  
**(a) Find a formula for the slope of the tangent line to the graph of $f$ at a general point $x = x_0$.**  
**(b) Use the formula obtained in part (a) to find the slope of the tangent line for the given value of $x_0$.**

15. $f(x) = x^2 - 1; \quad x_0 = -1$
16. $f(x) = x^2 + 3x + 2; \quad x_0 = 2$
17. $f(x) = x + \sqrt{x}; \quad x_0 = 1$
18. $f(x) = 1/\sqrt{x}; \quad x_0 = 4$

**19–22 True–False Determine whether the statement is true or false. Explain your answer.**

19. If $\lim_{x \to 1} \frac{f(x) - f(1)}{x - 1} = 3$, then $\lim_{h \to 0} \frac{f(1 + h) - f(1)}{h} = 3$.
20. A tangent line to a curve $y = f(x)$ is a particular kind of secant line to the curve.
21. The velocity of an object represents a change in the object's position.
22. A 50-foot horizontal metal beam is supported on either end by concrete pillars and a weight is placed on the middle of the beam. If $f(x)$ models how many inches the center of the beam sags when the weight measures $x$ tons, then the units of the rate of change of $y = f(x)$ with respect to $x$ are inches/ton.

23. Suppose that the outside temperature versus time curve over a 24-hour period is as shown in Figure Ex-23.  
    (a) Estimate the maximum temperature and the time at which it occurs.  
    (b) The temperature rise is fairly linear from 8 a.m. to 2 p.m. Estimate the rate at which the temperature is increasing during this time period.  
    (c) Estimate the time at which the temperature is decreasing most rapidly. Estimate the instantaneous rate of change of temperature with respect to time at this instant.
24. The accompanying figure shows the graph of the pressure $p$ in atmospheres (atm) versus the volume $V$ in liters (L) of 1 mole of an ideal gas at a constant temperature of 300 K (kelvins). Use the line segments shown in the figure to estimate the rate of change of pressure with respect to volume at the points where $V = 10\text{ L}$ and $V = 25\text{ L}$.
25. The accompanying figure shows the graph of the height $h$ in centimeters versus the age $t$ in years of an individual from birth to age 20.  
    (a) When is the growth rate greatest?  
    (b) Estimate the growth rate at age 5.  
    (c) At approximately what age between 10 and 20 is the growth rate greatest? Estimate the growth rate at this age.  
    (d) Draw a rough graph of the growth rate versus age.
26. An object is released from rest (its initial velocity is zero) from the Empire State Building at a height of $1250\text{ ft}$ above street level (Figure Ex-26). The height of the object can be modeled by the position function $s = f(t) = 1250 - 16t^2$.  
    (a) Verify that the object is still falling at $t = 5\text{ s}$.  
    (b) Find the average velocity of the object over the time interval from $t = 5$ to $t = 6\text{ s}$.  
    (c) Find the object's instantaneous velocity at time $t = 5\text{ s}$.
27. During the first $40\text{ s}$ of a rocket flight, the rocket is propelled straight up so that in $t$ seconds it reaches a height of $s = 0.3t^3\text{ ft}$.  
    (a) How high does the rocket travel in $40\text{ s}$?  
    (b) What is the average velocity of the rocket during the first $40\text{ s}$?  
    (c) What is the average velocity of the rocket during the first $1000\text{ ft}$ of its flight?  
    (d) What is the instantaneous velocity of the rocket at the end of $40\text{ s}$?
28. An automobile is driven down a straight highway such that after $0 \le t \le 12$ seconds it is $s = 4.5t^2$ feet from its initial position.  
    (a) Find the average velocity of the car over the interval $[0, 12]$.  
    (b) Find the instantaneous velocity of the car at $t = 6$.
29. A robot moves in the positive direction along a straight line so that after $t$ minutes its distance is $s = 6t^4$ feet from the origin.  
    (a) Find the average velocity of the robot over the interval $[2, 4]$.  
    (b) Find the instantaneous velocity at $t = 2$.
30. **Writing.** Discuss how the tangent line to the graph of a function $y = f(x)$ at a point $P(x_0, f(x_0))$ is defined in terms of secant lines to the graph through point $P$.
31. **Writing.** A particle is in rectilinear motion during the time interval $0 \le t \le 2$. Explain the connection between the instantaneous velocity of the particle at time $t = 1$ and the average velocities of the particle during portions of the interval $0 \le t \le 2$.

---

## 2.2 THE DERIVATIVE FUNCTION

In this section we will discuss the concept of a "derivative," which is the primary mathematical tool that is used to calculate and study rates of change.

### DEFINITION OF THE DERIVATIVE FUNCTION

> **2.2.1 DEFINITION**  
> The function $f'$ defined by the formula
> $$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} \tag{2}$$
> is called the **derivative of $f$ with respect to $x$**. The domain of $f'$ consists of all $x$ in the domain of $f$ for which the limit exists.

The expression $\frac{f(x + h) - f(x)}{h}$ that appears in (2) is commonly called the **difference quotient**.

#### Example 1
Find the derivative with respect to $x$ of $f(x) = x^2$, and use it to find the equation of the tangent line to $y = x^2$ at $x = 2$.

**Solution.**
$$f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} = \lim_{h \to 0} \frac{2xh + h^2}{h} = \lim_{h \to 0} (2x + h) = 2x$$
At $x = 2$, slope $m = f'(2) = 4$, point $(2, 4)$. Equation: $y - 4 = 4(x - 2) \implies y = 4x - 4$.

**Finding an Equation for the Tangent Line to $y = f(x)$ at $x = x_0$**
* **Step 1.** Evaluate $f(x_0)$; the point of tangency is $(x_0, f(x_0))$.
* **Step 2.** Find $f'(x)$ and evaluate $f'(x_0)$, which is the slope $m$ of the line.
* **Step 3.** Substitute the value of the slope $m$ and the point $(x_0, f(x_0))$ into the point-slope form:
  $$y - f(x_0) = f'(x_0)(x - x_0) \quad \text{or, equivalently,} \quad y = f(x_0) + f'(x_0)(x - x_0) \tag{3}$$

#### Example 2
(a) Find the derivative with respect to $x$ of $f(x) = x^3 - x$.  
(b) Graph $f$ and $f'$ together, and discuss the relationship between the two graphs.

**Solution (a).**
$$f'(x) = \lim_{h \to 0} \frac{[(x + h)^3 - (x + h)] - [x^3 - x]}{h} = \lim_{h \to 0} \frac{3x^2h + 3xh^2 + h^3 - h}{h} = 3x^2 - 1$$

#### Example 3
For a linear function $f(x) = mx + b$:
$$f'(x) = \lim_{h \to 0} \frac{[m(x + h) + b] - [mx + b]}{h} = \lim_{h \to 0} \frac{mh}{h} = m$$

#### Example 4
(a) For $f(x) = \sqrt{x}$, $f'(x) = \frac{1}{2\sqrt{x}}$.  
(b) At $x = 9$, slope $f'(9) = \frac{1}{2\sqrt{9}} = \frac{1}{6}$.  
(c) $\lim_{x \to 0^+} f'(x) = +\infty$ (tangent line becomes vertical) and $\lim_{x \to +\infty} f'(x) = 0$ (tangent line becomes horizontal).

---

### COMPUTING INSTANTANEOUS VELOCITY

If $f(t)$ is the position function of a particle in rectilinear motion, then the **velocity function** is
$$v(t) = f'(t) = \lim_{h \to 0} \frac{f(t + h) - f(t)}{h} \tag{4}$$

#### Example 5
For $s = f(t) = 1 + 5t - 2t^2$:
$$v(t) = \lim_{h \to 0} \frac{[1 + 5(t + h) - 2(t + h)^2] - [1 + 5t - 2t^2]}{h} = 5 - 4t\text{ m/s}$$

---

### DIFFERENTIABILITY

> **2.2.2 DEFINITION**  
> A function $f$ is said to be **differentiable at $x_0$** if the limit
> $$f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} \tag{5}$$
> exists. If $f$ is differentiable at each point of an open interval, we say $f$ is differentiable on that interval.

Two common geometric ways differentiability can fail:
1. **Corner points** (left and right limits of difference quotients are different finite numbers).
2. **Points of vertical tangency** (slopes tend toward $+\infty$ or $-\infty$).

#### Example 6
Let $f(x) = |x|$.
(a) At $x_0 = 0$:
$$\lim_{h \to 0^-} \frac{|h|}{h} = -1, \quad \lim_{h \to 0^+} \frac{|h|}{h} = 1$$
Since one-sided limits differ, $f'(0)$ does not exist.  
(b) For $x \neq 0$:
$$f'(x) = \begin{cases} 1, & x > 0 \\ -1, & x < 0 \end{cases}$$

---

### THE RELATIONSHIP BETWEEN DIFFERENTIABILITY AND CONTINUITY

> **2.2.3 THEOREM**  
> If a function $f$ is differentiable at $x_0$, then $f$ is continuous at $x_0$.

**Proof.** We must prove that $\lim_{h \to 0} [f(x_0 + h) - f(x_0)] = 0$:
$$\lim_{h \to 0} [f(x_0 + h) - f(x_0)] = \lim_{h \to 0} \left[\frac{f(x_0 + h) - f(x_0)}{h} \cdot h\right] = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} \cdot \lim_{h \to 0} h = f'(x_0) \cdot 0 = 0 \ \blacksquare$$

*Warning:* The converse is false. Continuous functions can fail to be differentiable (e.g., $f(x) = |x|$ at $x = 0$).

> **Bernhard Bolzano (1781–1848)**  
> Bohemian priest, philosopher, and mathematician who was among the first to emphasize rigorous proofs over geometric intuition and constructed continuous nowhere differentiable functions (1834).

---

### DERIVATIVES AT ENDPOINTS & OTHER NOTATIONS

* **One-sided derivatives:**
  $$f'_-(x) = \lim_{h \to 0^-} \frac{f(x + h) - f(x)}{h}, \quad f'_+(x) = \lim_{h \to 0^+} \frac{f(x + h) - f(x)}{h}$$
* Notations: $f'(x) = \frac{d}{dx}[f(x)] = D_x[f(x)] = y' = \frac{dy}{dx}$.
* Increment notation:
  $$\Delta x = x - x_0, \quad \Delta y = f(x + \Delta x) - f(x), \quad \frac{dy}{dx} = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} \tag{12}$$
* Alternative limit form:
  $$f'(x) = \lim_{w \to x} \frac{f(w) - f(x)}{w - x} \tag{13}$$

---

### QUICK CHECK EXERCISES 2.2
*(See page 134 for answers.)*

1. The function $f'(x)$ is defined by the formula $f'(x) = \lim_{h \to 0} \underline{\hspace{1.5cm}}$.
2. (a) The derivative of $f(x) = x^2$ is $f'(x) = \underline{\hspace{1cm}}$.  
   (b) The derivative of $f(x) = \sqrt{x}$ is $f'(x) = \underline{\hspace{1cm}}$.
3. Suppose that the line $2x + 3y = 5$ is tangent to the graph of $y = f(x)$ at $x = 1$. The value of $f(1)$ is $\underline{\hspace{1cm}}$ and the value of $f'(1)$ is $\underline{\hspace{1cm}}$.
4. Which theorem guarantees us that if $\lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$ exists, then $\lim_{x \to x_0} f(x) = f(x_0)$?

#### QUICK CHECK ANSWERS 2.2
1. $\frac{f(x + h) - f(x)}{h}$  
2. (a) $2x$ (b) $\frac{1}{2\sqrt{x}}$  
3. $1; \ -\frac{2}{3}$  
4. Theorem 2.2.3: If $f$ is differentiable at $x_0$, then $f$ is continuous at $x_0$.

---

### EXERCISE SET 2.2

1. Use the graph of $y = f(x)$ in Figure Ex-1 to estimate the value of $f'(1), f'(3), f'(5),$ and $f'(6)$.
2. For the function graphed in Figure Ex-2, arrange the numbers $0, f'(-3), f'(0), f'(2),$ and $f'(4)$ in increasing order.

**FOCUS ON CONCEPTS**

3. (a) If you are given an equation for the tangent line at the point $(a, f(a))$ on a curve $y = f(x)$, how would you go about finding $f'(a)$?  
   (b) Given that the tangent line to the graph of $y = f(x)$ at the point $(2, 5)$ has the equation $y = 3x - 1$, find $f'(2)$.  
   (c) For the function $y = f(x)$ in part (b), what is the instantaneous rate of change of $y$ with respect to $x$ at $x = 2$?
4. Given that the tangent line to $y = f(x)$ at the point $(1, 2)$ passes through the point $(-1, -1)$, find $f'(1)$.
5. Sketch the graph of a function $f$ for which $f(0) = -1, f'(0) = 0, f'(x) < 0 \text{ if } x < 0,$ and $f'(x) > 0 \text{ if } x > 0$.
6. Sketch the graph of a function $f$ for which $f(0) = 0, f'(0) = 0,$ and $f'(x) > 0 \text{ if } x < 0 \text{ or } x > 0$.
7. Given that $f(3) = -1$ and $f'(3) = 5$, find an equation for the tangent line to the graph of $y = f(x)$ at $x = 3$.
8. Given that $f(-2) = 3$ and $f'(-2) = -4$, find an equation for the tangent line to the graph of $y = f(x)$ at $x = -2$.

**9–14 Use Definition 2.2.1 to find $f'(x)$, and then find the tangent line to the graph of $y = f(x)$ at $x = a$.**

9. $f(x) = 2x^2; \quad a = 1$
10. $f(x) = 1/x^2; \quad a = -1$
11. $f(x) = x^3; \quad a = 0$
12. $f(x) = 2x^3 + 1; \quad a = -1$
13. $f(x) = \sqrt{x + 1}; \quad a = 8$
14. $f(x) = \sqrt{2x + 1}; \quad a = 4$

**15–20 Use Formula (12) to find $dy/dx$.**

15. $y = \frac{1}{x}$
16. $y = \frac{1}{x + 1}$
17. $y = x^2 - x$
18. $y = x^4$
19. $y = \frac{1}{\sqrt{x}}$
20. $y = \frac{1}{\sqrt{x - 1}}$

**21–22 Use Definition 2.2.1 (with appropriate change in notation) to obtain the derivative requested.**

21. Find $f'(t)$ if $f(t) = 4t^2 + t$.
22. Find $dV/dr$ if $V = \frac{4}{3}\pi r^3$.

**FOCUS ON CONCEPTS**

23. Match the graphs of the functions shown in (a)–(f) with the graphs of their derivatives in (A)–(F).
24. Let $f(x) = \sqrt{1 - x^2}$. Use a geometric argument to find $f'(\sqrt{2}/2)$.

**25–26 Sketch the graph of the derivative of the function whose graph is shown.**

25. Graphs (a), (b), (c) with linear/corner segments.
26. Graphs (a), (b), (c) with smooth peaks and cusps.

**27–30 True–False Determine whether the statement is true or false. Explain your answer.**

27. If a curve $y = f(x)$ has a horizontal tangent line at $x = a$, then $f'(a)$ is not defined.
28. If the tangent line to the graph of $y = f(x)$ at $x = -2$ has negative slope, then $f'(-2) < 0$.
29. If a function $f$ is continuous at $x = 0$, then $f$ is differentiable at $x = 0$.
30. If a function $f$ is differentiable at $x = 0$, then $f$ is continuous at $x = 0$.

**31–32 The given limit represents $f'(a)$ for some function $f$ and some number $a$. Find $f(x)$ and $a$ in each case.**

31. (a) $\lim_{\Delta x \to 0} \frac{\sqrt{1 + \Delta x} - 1}{\Delta x}$  
    (b) $\lim_{x_1 \to 3} \frac{x_1^2 - 9}{x_1 - 3}$
32. (a) $\lim_{h \to 0} \frac{\cos(\pi + h) + 1}{h}$  
    (b) $\lim_{x \to 1} \frac{x^7 - 1}{x - 1}$

33. Find $dy/dx|_{x=1}$, given that $y = 1 - x^2$.
34. Find $dy/dx|_{x=-2}$, given that $y = (x + 2)/x$.
35. Find an equation for the line that is tangent to the curve $y = x^3 - 2x + 1$ at the point $(0, 1)$, and use a graphing utility to graph the curve and its tangent line on the same screen.
36. Use a graphing utility to graph the following on the same screen: the curve $y = x^2/4$, the tangent line to this curve at $x = 1$, and the secant line joining the points $(0, 0)$ and $(2, 1)$ on this curve.
37. Let $f(x) = 2^x$. Estimate $f'(1)$ by  
    (a) using a graphing utility to zoom in at an appropriate point until the graph looks like a straight line, and then estimating the slope  
    (b) using a calculating utility to estimate the limit in Formula (13) by making a table of values for a succession of values of $w$ approaching 1.
38. Let $f(x) = \sin x$. Estimate $f'(\pi/4)$ by  
    (a) using a graphing utility to zoom in at an appropriate point until the graph looks like a straight line, and then estimating the slope  
    (b) using a calculating utility to estimate the limit in Formula (13) by making a table of values for a succession of values of $w$ approaching $\pi/4$.

**39–40 The function $f$ whose graph is shown has values as given in the accompanying table:**  
$x: -1, 0, 1, 2, 3$; $f(x): 1.56, 0.58, 2.12, 2.34, 2.2$.

39. (a) Use data from the table to calculate the difference quotients
    $$\frac{f(3) - f(1)}{3 - 1}, \quad \frac{f(2) - f(1)}{2 - 1}, \quad \frac{f(2) - f(0)}{2 - 0}$$
    (b) Using the graph of $y = f(x)$, indicate which difference quotient in part (a) best approximates $f'(1)$ and which difference quotient gives the worst approximation to $f'(1)$.
40. Use data from the table to approximate the derivative values: (a) $f'(0.5)$ (b) $f'(2.5)$.

**FOCUS ON CONCEPTS**

41. Suppose that the cost of drilling $x$ feet for an oil well is $C = f(x)$ dollars.  
    (a) What are the units of $f'(x)$?  
    (b) In practical terms, what does $f'(x)$ mean in this case?  
    (c) What can you say about the sign of $f'(x)$?  
    (d) Estimate the cost of drilling an additional foot, starting at a depth of $300\text{ ft}$, given that $f'(300) = 1000$.
42. A paint manufacturing company estimates that it can sell $g = f(p)$ gallons of paint at a price of $p$ dollars per gallon.  
    (a) What are the units of $dg/dp$?  
    (b) In practical terms, what does $dg/dp$ mean in this case?  
    (c) What can you say about the sign of $dg/dp$?  
    (d) Given that $dg/dp|_{p=10} = -100$, what can you say about the effect of increasing the price from $\$10$ per gallon to $\$11$ per gallon?
43. It is a fact that when a flexible rope is wrapped around a rough cylinder, a small force of magnitude $F_0$ at one end can resist a large force of magnitude $F$ at the other end. The size of $F$ depends on the angle $\theta$ through which the rope is wrapped around the cylinder (Figure Ex-43).  
    (a) Estimate the values of $F$ and $dF/d\theta$ when the angle $\theta = 10\text{ radians}$.  
    (b) It can be shown that the force $F$ satisfies the equation $dF/d\theta = \mu F$, where the constant $\mu$ is called the coefficient of friction. Use the results in part (a) to estimate the value of $\mu$.
44. The accompanying figure shows the velocity versus time curve for a rocket in outer space where the only significant force on the rocket is from its engines. It can be shown that the mass $M(t)$ (in slugs) of the rocket at time $t$ seconds satisfies the equation $M(t) = \frac{T}{dv/dt}$ where $T$ is the thrust (in lb) of the rocket's engines and $v$ is the velocity (in ft/s) of the rocket. The thrust of the first stage of a Saturn V rocket is $T = 7,680,982\text{ lb}$. Use this value of $T$ and the line segment in the figure to estimate the mass of the rocket at time $t = 100$.
45. According to Newton's Law of Cooling, the rate of change of an object's temperature is proportional to the difference between the temperature of the object and that of the surrounding medium. The accompanying figure shows the graph of the temperature $T$ (in $^\circ\text{F}$) versus time $t$ (in minutes) for a cup of coffee, initially with a temperature of $200^\circ\text{F}$, cooling in a room at $75^\circ\text{F}$.  
    (a) Estimate $T$ and $dT/dt$ when $t = 10\text{ min}$.  
    (b) Newton's Law of Cooling can be expressed as $\frac{dT}{dt} = k(T - T_0)$ where $k$ is the constant of proportionality and $T_0$ is the ambient temperature. Use results in (a) to estimate $k$.
46. Show that $f(x)$ is continuous but not differentiable at the indicated point. Sketch the graph of $f$.  
    (a) $f(x) = \sqrt[3]{x}, \ x = 0$  
    (b) $f(x) = \sqrt[3]{(x - 2)^2}, \ x = 2$
47. Show that
    $$f(x) = \begin{cases} x^2 + 1, & x \le 1 \\ 2x, & x > 1 \end{cases}$$
    is continuous and differentiable at $x = 1$. Sketch the graph of $f$.
48. Show that
    $$f(x) = \begin{cases} x^2 + 2, & x \le 1 \\ x + 2, & x > 1 \end{cases}$$
    is continuous but not differentiable at $x = 1$. Sketch the graph of $f$.
49. Show that
    $$f(x) = \begin{cases} x\sin(1/x), & x \neq 0 \\ 0, & x = 0 \end{cases}$$
    is continuous but not differentiable at $x = 0$. Sketch the graph of $f$ near $x = 0$.
50. Show that
    $$f(x) = \begin{cases} x^2\sin(1/x), & x \neq 0 \\ 0, & x = 0 \end{cases}$$
    is continuous and differentiable at $x = 0$. Sketch the graph of $f$ near $x = 0$.

**FOCUS ON CONCEPTS**

51. Suppose that a function $f$ is differentiable at $x_0$ and that $f'(x_0) > 0$. Prove that there exists an open interval containing $x_0$ such that if $x_1$ and $x_2$ are any two points in this interval with $x_1 < x_0 < x_2$, then $f(x_1) < f(x_0) < f(x_2)$.
52. Suppose that a function $f$ is differentiable at $x_0$ and define $g(x) = f(mx + b)$, where $m$ and $b$ are constants. Prove that if $x_1$ is a point at which $mx_1 + b = x_0$, then $g(x)$ is differentiable at $x_1$ and $g'(x_1) = mf'(x_0)$.
53. Suppose that a function $f$ is differentiable at $x = 0$ with $f(0) = f'(0) = 0$, and let $y = mx, \ m \neq 0$, denote any line of nonzero slope through the origin.  
    (a) Prove that there exists an open interval containing 0 such that for all nonzero $x$ in this interval $|f(x)| < \frac{1}{2}|mx|$.  
    (b) Conclude from part (a) and the triangle inequality that there exists an open interval containing 0 such that $|f(x)| < |f(x) - mx|$ for all $x$ in this interval.  
    (c) Explain why the result obtained in part (b) may be interpreted to mean that the tangent line to the graph of $f$ at the origin is the best linear approximation to $f$ at that point.
54. Suppose that $f$ is differentiable at $x_0$. Modify the argument of Exercise 53 to prove that the tangent line to the graph of $f$ at the point $P(x_0, f(x_0))$ provides the best linear approximation to $f$ at $P$.
55. **Writing.** Write a paragraph that explains what it means for a function to be differentiable. Include examples of functions that are not differentiable as well as examples of functions that are differentiable.
56. **Writing.** Explain the relationship between continuity and differentiability.

---

## 2.3 INTRODUCTION TO TECHNIQUES OF DIFFERENTIATION

In this section we will develop some important theorems that will enable us to calculate derivatives more efficiently.

### DERIVATIVE OF A CONSTANT

> **2.3.1 THEOREM**  
> The derivative of a constant function is 0; that is, if $c$ is any real number, then
> $$\frac{d}{dx}[c] = 0 \tag{1}$$

#### Example 1
$$\frac{d}{dx}[1] = 0, \quad \frac{d}{dx}[-3] = 0, \quad \frac{d}{dx}[\pi] = 0, \quad \frac{d}{dx}[-\sqrt{2}] = 0$$

---

### DERIVATIVES OF POWER FUNCTIONS

> **2.3.2 THEOREM (The Power Rule)**  
> If $n$ is a positive integer, then
> $$\frac{d}{dx}[x^n] = nx^{n-1} \tag{5}$$

**Proof.** Let $f(x) = x^n$. Using the binomial formula for $(x + h)^n$:
$$f'(x) = \lim_{h \to 0} \frac{(x + h)^n - x^n}{h} = \lim_{h \to 0} \frac{nx^{n-1}h + \frac{n(n-1)}{2!}x^{n-2}h^2 + \dots + h^n}{h} = nx^{n-1} \ \blacksquare$$

> **2.3.3 THEOREM (Extended Power Rule)**  
> If $r$ is any real number, then
> $$\frac{d}{dx}[x^r] = rx^{r-1} \tag{7}$$

#### Example 2 & 3
* $\frac{d}{dx}[x^4] = 4x^3, \quad \frac{d}{dx}[x^5] = 5x^4, \quad \frac{d}{dt}[t^{12}] = 12t^{11}$
* $\frac{d}{dx}[x^\pi] = \pi x^{\pi - 1}$
* $\frac{d}{dx}\left[\frac{1}{x}\right] = \frac{d}{dx}[x^{-1}] = -x^{-2} = -\frac{1}{x^2}$
* $\frac{d}{dw}\left[\frac{1}{w^{100}}\right] = -100w^{-101} = -\frac{100}{w^{101}}$
* $\frac{d}{dx}[x^{4/5}] = \frac{4}{5}x^{-1/5}$
* $\frac{d}{dx}[\sqrt[3]{x}] = \frac{1}{3}x^{-2/3} = \frac{1}{3\sqrt[3]{x^2}}$

---

### CONSTANT MULTIPLE, SUM, AND DIFFERENCE RULES

> **2.3.4 THEOREM (Constant Multiple Rule)**  
> If $f$ is differentiable at $x$ and $c$ is any real number, then $cf$ is differentiable at $x$ and
> $$\frac{d}{dx}[cf(x)] = c\frac{d}{dx}[f(x)] \tag{8}$$

> **2.3.5 THEOREM (Sum and Difference Rules)**  
> If $f$ and $g$ are differentiable at $x$, then so are $f + g$ and $f - g$ and
> $$\frac{d}{dx}[f(x) + g(x)] = \frac{d}{dx}[f(x)] + \frac{d}{dx}[g(x)] \tag{9}$$
> $$\frac{d}{dx}[f(x) - g(x)] = \frac{d}{dx}[f(x)] - \frac{d}{dx}[g(x)] \tag{10}$$

#### Example 4, 5, 6
* $\frac{d}{dx}[4x^8] = 32x^7, \quad \frac{d}{dx}[-x^{12}] = -12x^{11}, \quad \frac{d}{dx}[\pi/x] = -\pi/x^2$
* $\frac{d}{dx}[2x^6 + x^{-9}] = 12x^5 - 9x^{-10}$
* $\frac{d}{dx}\left[\frac{\sqrt{x} - 2x}{\sqrt{x}}\right] = \frac{d}{dx}[1 - 2\sqrt{x}] = -\frac{1}{\sqrt{x}}$
* For $y = 3x^8 - 2x^5 + 6x + 1$: $\frac{dy}{dx} = 24x^7 - 10x^4 + 6$.

#### Example 7
At what points, if any, does the graph of $y = x^3 - 3x + 4$ have a horizontal tangent line?

**Solution.** $y'(x) = 3x^2 - 3 = 0 \implies x = \pm 1$. Points are $(-1, 6)$ and $(1, 2)$.

#### Example 8
Find the area of the triangle formed from the coordinate axes and the tangent line to the curve $y = 5x^{-1} - \frac{1}{5}x$ at the point $(5, 0)$.

**Solution.** $y'(x) = -5x^{-2} - 1/5 \implies y'(5) = -2/5$.  
Tangent line: $y - 0 = -\frac{2}{5}(x - 5) \implies y = -\frac{2}{5}x + 2$. Intercepts at $(5, 0)$ and $(0, 2)$. Area $= \frac{1}{2}(5)(2) = 5$.

---

### HIGHER DERIVATIVES

Successive derivatives: $f', f'' = (f')', f''' = (f'')', f^{(4)}, \dots, f^{(n)}$.
Notations: $\frac{dy}{dx}, \frac{d^2y}{dx^2}, \frac{d^3y}{dx^3}, \dots, \frac{d^ny}{dx^n} = f^{(n)}(x)$.

#### Example 9
For $f(x) = 3x^4 - 2x^3 + x^2 - 4x + 2$:
$$f'(x) = 12x^3 - 6x^2 + 2x - 4, \quad f''(x) = 36x^2 - 12x + 2, \quad f'''(x) = 72x - 12, \quad f^{(4)}(x) = 72, \quad f^{(n)}(x) = 0 \ (n \ge 5)$$

---

### QUICK CHECK EXERCISES 2.3
*(See page 142 for answers.)*

1. In each part, determine $f'(x)$: (a) $f(x) = \sqrt{6}$ (b) $f(x) = \sqrt{6}x$ (c) $f(x) = 6\sqrt{x}$ (d) $f(x) = \sqrt{6x}$.
2. In parts (a)–(d), determine $f'(x)$: (a) $f(x) = x^3 + 5$ (b) $f(x) = x^2(x^3 + 5)$ (c) $f(x) = \frac{x^3 + 5}{2}$ (d) $f(x) = \frac{x^3 + 5}{x^2}$.
3. The slope of the tangent line to the curve $y = x^2 + 4x + 7$ at $x = 1$ is $\underline{\hspace{1cm}}$.
4. If $f(x) = 3x^3 - 3x^2 + x + 1$, then $f''(x) = \underline{\hspace{1.5cm}}$.

#### QUICK CHECK ANSWERS 2.3
1. (a) $0$ (b) $\sqrt{6}$ (c) $3/\sqrt{x}$ (d) $\sqrt{6}/(2\sqrt{x})$  
2. (a) $3x^2$ (b) $5x^4 + 10x$ (c) $\frac{3}{2}x^2$ (d) $1 - 10x^{-3}$  
3. $6$  
4. $18x - 6$

---

### EXERCISE SET 2.3

**1–8 Find $dy/dx$.**

1. $y = 4x^7$
2. $y = -3x^{12}$
3. $y = 3x^8 + 2x + 1$
4. $y = \frac{1}{2}(x^4 + 7)$
5. $y = \pi^3$
6. $y = \sqrt{2}x + (1/\sqrt{2})$
7. $y = -\frac{1}{3}(x^7 + 2x - 9)$
8. $y = \frac{x^2 + 1}{5}$

**9–16 Find $f'(x)$.**

9. $f(x) = x^{-3} + \frac{1}{x^7}$
10. $f(x) = \sqrt{x} + \frac{1}{x}$
11. $f(x) = -3x^{-8} + 2\sqrt{x}$
12. $f(x) = 7x^{-6} - 5\sqrt{x}$
13. $f(x) = x^\pi + \frac{1}{x^{\sqrt{10}}}$
14. $f(x) = \sqrt[3]{\frac{8}{x}}$
15. $f(x) = (3x^2 + 1)^2$
16. $f(x) = ax^3 + bx^2 + cx + d \ (a, b, c, d \text{ constant})$

**17–18 Find $y'(1)$.**

17. $y = 5x^2 - 3x + 1$
18. $y = \frac{x^{3/2} + 2}{x}$

**19–20 Find $dx/dt$.**

19. $x = t^2 - t$
20. $x = \frac{t^2 + 1}{3t}$

**21–24 Find $dy/dx|_{x=1}$.**

21. $y = 1 + x + x^2 + x^3 + x^4 + x^5$
22. $y = \frac{1 + x + x^2 + x^3 + x^4 + x^5 + x^6}{x^3}$
23. $y = (1 - x)(1 + x)(1 + x^2)(1 + x^4)$
24. $y = x^{24} + 2x^{12} + 3x^8 + 4x^6$

**25–26 Approximate $f'(1)$ by considering the difference quotient $\frac{f(1 + h) - f(1)}{h}$ for values of $h$ near 0, and then find the exact value of $f'(1)$ by differentiating.**

25. $f(x) = x^3 - 3x + 1$
26. $f(x) = 1/x^2$

**27–28 Use a graphing utility to estimate the value of $f'(1)$ by zooming in on the graph of $f$, and then compare your estimate to the exact value obtained by differentiating.**

27. $f(x) = \frac{x^2 + 1}{x}$
28. $f(x) = \frac{x + 2x^{3/2}}{\sqrt{x}}$

**29–32 Find the indicated derivative.**

29. $\frac{d}{dt}[16t^2]$
30. $\frac{dC}{dr}$, where $C = 2\pi r$
31. $V'(r)$, where $V = \pi r^3$
32. $\frac{d}{d\alpha}[2\alpha^{-1} + \alpha]$

**33–36 True–False Determine whether the statement is true or false. Explain your answer.**

33. If $f$ and $g$ are differentiable at $x = 2$, then $\frac{d}{dx}[f(x) - 8g(x)]\Big|_{x=2} = f'(2) - 8g'(2)$.
34. If $f(x)$ is a cubic polynomial, then $f'(x)$ is a quadratic polynomial.
35. If $f'(2) = 5$, then $\frac{d}{dx}[4f(x) + x^3]\Big|_{x=2} = \frac{d}{dx}[4f(x) + 8]\Big|_{x=2} = 4f'(2) = 20$.
36. If $f(x) = x^2(x^4 - x)$, then $f''(x) = \frac{d}{dx}[x^2] \cdot \frac{d}{dx}[x^4 - x] = 2x(4x^3 - 1)$.

37. A spherical balloon is being inflated.  
    (a) Find a general formula for the instantaneous rate of change of the volume $V$ with respect to the radius $r$, given that $V = \frac{4}{3}\pi r^3$.  
    (b) Find the rate of change of $V$ with respect to $r$ at the instant when the radius is $r = 5$.
38. Find $\frac{d}{d\lambda}\left[\frac{\lambda\lambda_0 + \lambda^6}{2 - \lambda_0}\right]$ ($\lambda_0$ is constant).
39. Find an equation of the tangent line to the graph of $y = f(x)$ at $x = -3$ if $f(-3) = 2$ and $f'(-3) = 5$.
40. Find an equation of the tangent line to the graph of $y = f(x)$ at $x = 2$ if $f(2) = -2$ and $f'(2) = -1$.

**41–42 Find $d^2y/dx^2$.**

41. (a) $y = 7x^3 - 5x^2 + x$  
    (b) $y = 12x^2 - 2x + 3$  
    (c) $y = \frac{x + 1}{x}$  
    (d) $y = (5x^2 - 3)(7x^3 + x)$
42. (a) $y = 4x^7 - 5x^3 + 2x$  
    (b) $y = 3x + 2$  
    (c) $y = \frac{3x - 2}{5x}$  
    (d) $y = (x^3 - 5)(2x + 3)$

**43–44 Find $y'''$.**

43. (a) $y = x^{-5} + x^5$  
    (b) $y = 1/x$  
    (c) $y = ax^3 + bx + c$
44. (a) $y = 5x^2 - 4x + 7$  
    (b) $y = 3x^{-2} + 4x^{-1} + x$  
    (c) $y = ax^4 + bx^2 + c$

45. Find  
    (a) $f'''(2)$, where $f(x) = 3x^2 - 2$  
    (b) $\frac{d^2y}{dx^2}\Big|_{x=1}$, where $y = 6x^5 - 4x^2$  
    (c) $\frac{d^4}{dx^4}[x^{-3}]\Big|_{x=1}$.
46. Find  
    (a) $y'''(0)$, where $y = 4x^4 + 2x^3 + 3$  
    (b) $\frac{d^4y}{dx^4}\Big|_{x=1}$, where $y = 6/x^4$.
47. Show that $y = x^3 + 3x + 1$ satisfies $y''' + xy'' - 2y' = 0$.
48. Show that if $x \neq 0$, then $y = 1/x$ satisfies the equation $x^3y''' + x^2y'' - xy' = 0$.

**49–50 Use a graphing utility to make rough estimates of the locations of all horizontal tangent lines, and then find their exact locations by differentiating.**

49. $y = \frac{1}{3}x^3 - \frac{3}{2}x^2 + 2x$
50. $y = \frac{x^2 + 9}{x}$

**FOCUS ON CONCEPTS**

51. Find a function $y = ax^2 + bx + c$ whose graph has an $x$-intercept of 1, a $y$-intercept of $-2$, and a tangent line with a slope of $-1$ at the $y$-intercept.
52. Find $k$ if the curve $y = x^2 + k$ is tangent to the line $y = 2x$.
53. Find the $x$-coordinate of the point on the graph of $y = x^2$ where the tangent line is parallel to the secant line that cuts the curve at $x = -1$ and $x = 2$.
54. Find the $x$-coordinate of the point on the graph of $y = \sqrt{x}$ where the tangent line is parallel to the secant line that cuts the curve at $x = 1$ and $x = 4$.
55. Find the coordinates of all points on the graph of $y = 1 - x^2$ at which the tangent line passes through the point $(2, 0)$.
56. Show that any two tangent lines to the parabola $y = ax^2, \ a \neq 0$, intersect at a point that is on the vertical line halfway between the points of tangency.
57. Suppose that $L$ is the tangent line at $x = x_0$ to the graph of the cubic equation $y = ax^3 + bx$. Find the $x$-coordinate of the point where $L$ intersects the graph a second time.
58. Show that the segment of the tangent line to the graph of $y = 1/x$ that is cut off by the coordinate axes is bisected by the point of tangency.
59. Show that the triangle that is formed by any tangent line to the graph of $y = 1/x, \ x > 0$, and the coordinate axes has an area of 2 square units.
60. Find conditions on $a, b, c,$ and $d$ so that the graph of the polynomial $f(x) = ax^3 + bx^2 + cx + d$ has  
    (a) exactly two horizontal tangents  
    (b) exactly one horizontal tangent  
    (c) no horizontal tangents.
61. Newton's Law of Universal Gravitation states that the magnitude $F$ of the force exerted by a point with mass $M$ on a point with mass $m$ is $F = \frac{GmM}{r^2}$ where $G$ is a constant and $r$ is the distance between the bodies. Assuming that the points are moving, find a formula for the instantaneous rate of change of $F$ with respect to $r$.
62. In the temperature range between $0^\circ\text{C}$ and $700^\circ\text{C}$ the resistance $R$ (in ohms) of a certain platinum resistance thermometer is given by $R = 10 + 0.04124T - 1.779 \times 10^{-5}T^2$ where $T$ is temperature in $^\circ\text{C}$. Where in $[0^\circ\text{C}, 700^\circ\text{C}]$ is the resistance most sensitive and least sensitive to temperature changes?

**63–64 Use a graphing utility to make rough estimates of the intervals on which $f'(x) > 0$, and then find those intervals exactly by differentiating.**

63. $f(x) = x - \frac{1}{x}$
64. $f(x) = x^3 - 3x$

**65–68 Determine whether a piecewise-defined function $f$ is differentiable at $x = x_0$. (Theorem: Let $f$ be continuous at $x_0$ and suppose that $\lim_{x \to x_0} f'(x)$ exists. Then $f$ is differentiable at $x_0$, and $f'(x_0) = \lim_{x \to x_0} f'(x)$.)**

65. Show that $f(x) = \begin{cases} x^2 + x + 1, & x \le 1 \\ 3x, & x > 1 \end{cases}$ is continuous at $x = 1$. Determine whether $f$ is differentiable at $x = 1$. If so, find the value of the derivative there. Sketch the graph of $f$.
66. Let $f(x) = \begin{cases} x^2 - 16x, & x < 9 \\ \sqrt{x}, & x \ge 9 \end{cases}$. Is $f$ continuous at $x = 9$? Determine whether $f$ is differentiable at $x = 9$. If so, find the derivative.
67. Let $f(x) = \begin{cases} x^2, & x \le 1 \\ \sqrt{x}, & x > 1 \end{cases}$. Determine whether $f$ is differentiable at $x = 1$. If so, find the derivative.
68. Let $f(x) = \begin{cases} x^3 + \frac{1}{16}, & x < 1/2 \\ \frac{3}{4}x^2, & x \ge 1/2 \end{cases}$. Determine whether $f$ is differentiable at $x = 1/2$. If so, find the derivative.

69. Find all points where $f$ fails to be differentiable. Justify your answer.  
    (a) $f(x) = |3x - 2|$  
    (b) $f(x) = |x^2 - 4|$
70. In each part, compute $f', f'', f'''$, and then state the formula for $f^{(n)}$.  
    (a) $f(x) = 1/x$  
    (b) $f(x) = 1/x^2$
71. (a) Prove: $\frac{d^2}{dx^2}[cf(x)] = c\frac{d^2}{dx^2}[f(x)]$ and $\frac{d^2}{dx^2}[f(x) + g(x)] = \frac{d^2}{dx^2}[f(x)] + \frac{d^2}{dx^2}[g(x)]$.  
    (b) Do the results in part (a) generalize to $n$th derivatives? Justify your answer.
72. Let $f(x) = x^8 - 2x + 3$; find $\lim_{w \to 2} \frac{f'(w) - f'(2)}{w - 2}$.
73. (a) Find $f^{(n)}(x)$ if $f(x) = x^n, \ n = 1, 2, 3, \dots$.  
    (b) Find $f^{(n)}(x)$ if $f(x) = x^k$ and $n > k$.  
    (c) Find $f^{(n)}(x)$ if $f(x) = a_0 + a_1x + a_2x^2 + \dots + a_nx^n$.
74. (a) Prove: If $f''(x)$ exists for each $x$ in $(a, b)$, then both $f$ and $f'$ are continuous on $(a, b)$.  
    (b) What can be said about the continuity of $f$ and its derivatives if $f^{(n)}(x)$ exists for each $x$ in $(a, b)$?
75. Let $f(x) = (mx + b)^n$, where $m$ and $b$ are constants and $n$ is an integer. Prove that $f'(x) = nm(mx + b)^{n-1}$.

**76–77 Verify the result of Exercise 75 for $f(x)$.**

76. $f(x) = (2x + 3)^2$
77. $f(x) = (3x - 1)^3$

**78–81 Use the result of Exercise 75 to compute the derivative of the given function $f(x)$.**

78. $f(x) = \frac{1}{x - 1}$
79. $f(x) = \frac{3}{(2x + 1)^2}$
80. $f(x) = \frac{x}{x + 1}$
81. $f(x) = \frac{2x^2 + 4x + 3}{x^2 + 2x + 1}$

82. Extending the Power Rule to negative integers: Let $f(x) = x^n$ with $n < 0$, $m = -n > 0$.  
    (a) Show that the Power Rule holds for $n = 0$.  
    (b) Use $\frac{d}{dx}[1/x^m] = -mx^{m-1}\frac{1}{x^{2m}}$ to conclude $f'(x) = nx^{n-1}$.

---

## 2.4 THE PRODUCT AND QUOTIENT RULES

In this section we will develop techniques for differentiating products and quotients of functions whose derivatives are known.

### THE PRODUCT RULE

> **2.4.1 THEOREM (The Product Rule)**  
> If $f$ and $g$ are differentiable at $x$, then so is the product $f \cdot g$, and
> $$\frac{d}{dx}[f(x)g(x)] = f(x)\frac{d}{dx}[g(x)] + g(x)\frac{d}{dx}[f(x)] \tag{1}$$
> or $(f \cdot g)' = f \cdot g' + g \cdot f'$.

**Proof.**
$$\frac{d}{dx}[f(x)g(x)] = \lim_{h \to 0} \frac{f(x + h)g(x + h) - f(x)g(x)}{h}$$
$$= \lim_{h \to 0} \frac{f(x + h)g(x + h) - f(x + h)g(x) + f(x + h)g(x) - f(x)g(x)}{h}$$
$$= \lim_{h \to 0} f(x + h) \lim_{h \to 0} \frac{g(x + h) - g(x)}{h} + \lim_{h \to 0} g(x) \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$
$$= f(x)g'(x) + g(x)f'(x) \ \blacksquare$$

#### Example 1
Find $dy/dx$ if $y = (4x^2 - 1)(7x^3 + x)$.

**Solution (Product Rule).**
$$\frac{dy}{dx} = (4x^2 - 1)\frac{d}{dx}[7x^3 + x] + (7x^3 + x)\frac{d}{dx}[4x^2 - 1] = (4x^2 - 1)(21x^2 + 1) + (7x^3 + x)(8x) = 140x^4 - 9x^2 - 1$$

#### Example 2
Find $ds/dt$ if $s = (1 + t)\sqrt{t}$.

**Solution.**
$$\frac{ds}{dt} = (1 + t)\frac{d}{dt}[\sqrt{t}] + \sqrt{t}\frac{d}{dt}[1 + t] = \frac{1 + t}{2\sqrt{t}} + \sqrt{t} = \frac{1 + 3t}{2\sqrt{t}}$$

---

### THE QUOTIENT RULE

> **2.4.2 THEOREM (The Quotient Rule)**  
> If $f$ and $g$ are both differentiable at $x$ and if $g(x) \neq 0$, then $f/g$ is differentiable at $x$ and
> $$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x)\frac{d}{dx}[f(x)] - f(x)\frac{d}{dx}[g(x)]}{[g(x)]^2} \tag{2}$$
> or $\left(\frac{f}{g}\right)' = \frac{g \cdot f' - f \cdot g'}{g^2}$.

**Proof.**
$$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \lim_{h \to 0} \frac{\frac{f(x + h)}{g(x + h)} - \frac{f(x)}{g(x)}}{h} = \lim_{h \to 0} \frac{f(x + h)g(x) - f(x)g(x + h)}{h \cdot g(x)g(x + h)}$$
Adding and subtracting $f(x)g(x)$ in the numerator:
$$= \lim_{h \to 0} \frac{g(x)\frac{f(x + h) - f(x)}{h} - f(x)\frac{g(x + h) - g(x)}{h}}{g(x)g(x + h)} = \frac{g(x)f'(x) - f(x)g'(x)}{[g(x)]^2} \ \blacksquare$$

#### Example 3
Find $y'(x)$ for $y = \frac{x^3 + 2x^2 - 1}{x + 5}$.

**Solution.**
$$\frac{dy}{dx} = \frac{(x + 5)(3x^2 + 4x) - (x^3 + 2x^2 - 1)(1)}{(x + 5)^2} = \frac{2x^3 + 17x^2 + 20x + 1}{(x + 5)^2}$$

#### Example 4
Let $f(x) = \frac{x^2 - 1}{x^4 + 1}$. Find the exact locations of horizontal tangent lines.

**Solution.**
$$\frac{dy}{dx} = \frac{(x^4 + 1)(2x) - (x^2 - 1)(4x^3)}{(x^4 + 1)^2} = \frac{-2x(x^4 - 2x^2 - 1)}{(x^4 + 1)^2} = 0$$
$x = 0$ or $x^2 = 1 + \sqrt{2} \implies x = \pm\sqrt{1 + \sqrt{2}} \approx \pm 1.55$.

---

### SUMMARY OF DIFFERENTIATION RULES

#### Table 2.4.1: Rules for Differentiation
| Rule | Derivative Formula |
| :--- | :--- |
| Constant Rule | $\frac{d}{dx}[c] = 0$ |
| Power Rule | $\frac{d}{dx}[x^r] = rx^{r-1}$ |
| Constant Multiple Rule | $(cf)' = cf'$ |
| Sum Rule | $(f + g)' = f' + g'$ |
| Difference Rule | $(f - g)' = f' - g'$ |
| Product Rule | $(f \cdot g)' = f \cdot g' + g \cdot f'$ |
| Quotient Rule | $\left(\frac{f}{g}\right)' = \frac{g \cdot f' - f \cdot g'}{g^2}$ |
| Reciprocal Rule | $\left(\frac{1}{g}\right)' = -\frac{g'}{g^2}$ |

---

### QUICK CHECK EXERCISES 2.4
*(See page 148 for answers.)*

1. (a) $\frac{d}{dx}[x^2 f(x)] = \underline{\hspace{1.5cm}}$  
   (b) $\frac{d}{dx}\left[\frac{f(x)}{x^2 + 1}\right] = \underline{\hspace{1.5cm}}$  
   (c) $\frac{d}{dx}\left[\frac{x^2 + 1}{f(x)}\right] = \underline{\hspace{1.5cm}}$
2. Find $F'(1)$ given that $f(1) = -1, f'(1) = 2, g(1) = 3,$ and $g'(1) = -1$:  
   (a) $F(x) = 2f(x) - 3g(x)$  
   (b) $F(x) = [f(x)]^2$  
   (c) $F(x) = f(x)g(x)$  
   (d) $F(x) = f(x)/g(x)$

#### QUICK CHECK ANSWERS 2.4
1. (a) $x^2 f'(x) + 2xf(x)$ (b) $\frac{(x^2 + 1)f'(x) - 2xf(x)}{(x^2 + 1)^2}$ (c) $\frac{2xf(x) - (x^2 + 1)f'(x)}{[f(x)]^2}$  
2. (a) $7$ (b) $-4$ (c) $7$ (d) $\frac{5}{9}$

---

### EXERCISE SET 2.4

**1–4 Compute the derivative of the given function $f(x)$ by (a) multiplying and then differentiating and (b) using the product rule. Verify that (a) and (b) yield the same result.**

1. $f(x) = (x + 1)(2x - 1)$
2. $f(x) = (3x^2 - 1)(x^2 + 2)$
3. $f(x) = (x^2 + 1)(x^2 - 1)$
4. $f(x) = (x + 1)(x^2 - x + 1)$

**5–20 Find $f'(x)$.**

5. $f(x) = (3x^2 + 6)(2x - 1/4)$
6. $f(x) = (2 - x - 3x^3)(7 + x^5)$
7. $f(x) = (x^3 + 7x^2 - 8)(2x^{-3} + x^{-4})$
8. $f(x) = (x^{-1} + x^{-2})(3x^3 + 27)$
9. $f(x) = (x - 2)(x^2 + 2x + 4)$
10. $f(x) = (x^2 + x)(x^2 - x)$
11. $f(x) = \frac{3x + 4}{x^2 + 1}$
12. $f(x) = \frac{x - 2}{x^4 + x + 1}$
13. $f(x) = \frac{x^2}{3x - 4}$
14. $f(x) = \frac{2x^2 + 5}{3x - 4}$
15. $f(x) = \frac{(2\sqrt{x} + 1)(x - 1)}{x + 3}$
16. $f(x) = (2\sqrt{x} + 1)\left(\frac{2 - x}{x^2 + 3x}\right)$
17. $f(x) = (2x + 1)(1 + 1/x)(x^{-3} + 7)$
18. $f(x) = x^{-5}(x^2 + 2x)(4 - 3x)(2x^9 + 1)$
19. $f(x) = (x^7 + 2x - 3)^3$
20. $f(x) = (x^2 + 1)^4$

**21–24 Find $dy/dx|_{x=1}$.**

21. $y = \frac{2x - 1}{x + 3}$
22. $y = \frac{4x + 1}{x^2 - 5}$
23. $y = \left(\frac{3x + 2}{x}\right)(x^{-5} + 1)$
24. $y = (2x^7 - x^2)\left(\frac{x - 1}{x + 1}\right)$

**25–26 Use a graphing utility to estimate the value of $f'(1)$ by zooming in on the graph of $f$, and then compare your estimate to the exact value obtained by differentiating.**

25. $f(x) = \frac{x}{x^2 + 1}$
26. $f(x) = \frac{x^2 - 1}{x^2 + 1}$

27. Find $g'(4)$ given that $f(4) = 3$ and $f'(4) = -5$:  
    (a) $g(x) = \sqrt{x}f(x)$  
    (b) $g(x) = f(x)/x$
28. Find $g'(3)$ given that $f(3) = -2$ and $f'(3) = 4$:  
    (a) $g(x) = 3x^2 - 5f(x)$  
    (b) $g(x) = \frac{2x + 1}{f(x)}$
29. In parts (a)–(d), $F(x)$ is expressed in terms of $f(x)$ and $g(x)$. Find $F'(2)$ given that $f(2) = -1, f'(2) = 4, g(2) = 1,$ and $g'(2) = -5$:  
    (a) $F(x) = 5f(x) + 2g(x)$  
    (b) $F(x) = f(x) - 3g(x)$  
    (c) $F(x) = f(x)g(x)$  
    (d) $F(x) = f(x)/g(x)$
30. Find $F'(\pi)$ given that $f(\pi) = 10, f'(\pi) = -1, g(\pi) = -3,$ and $g'(\pi) = 2$:  
    (a) $F(x) = 6f(x) - 5g(x)$  
    (b) $F(x) = x(f(x) + g(x))$  
    (c) $F(x) = 2f(x)g(x)$  
    (d) $F(x) = \frac{f(x)}{4 + g(x)}$

**31–36 Find all values of $x$ at which the tangent line to the given curve satisfies the stated property.**

31. $y = \frac{x^2 - 1}{x + 2}$; horizontal
32. $y = \frac{x^2 + 1}{x - 1}$; horizontal
33. $y = \frac{x^2 + 1}{x + 1}$; parallel to the line $y = x$
34. $y = \frac{x + 3}{x + 2}$; perpendicular to the line $y = x$
35. $y = \frac{1}{x + 4}$; passes through the origin
36. $y = \frac{2x + 5}{x + 2}$; $y$-intercept 2

**FOCUS ON CONCEPTS**

37. (a) What should it mean to say that two curves intersect at right angles?  
    (b) Show that the curves $y = 1/x$ and $y = 1/(2 - x)$ intersect at right angles.
38. Find all values of $a$ such that the curves $y = a/(x - 1)$ and $y = x^2 - 2x + 1$ intersect at right angles.
39. Find a general formula for $F''(x)$ if $F(x) = xf(x)$ and $f$ and $f'$ are differentiable at $x$.
40. Suppose that the function $f$ is differentiable everywhere and $F(x) = xf(x)$.  
    (a) Express $F'''(x)$ in terms of $x$ and derivatives of $f$.  
    (b) For $n \ge 2$, conjecture a formula for $F^{(n)}(x)$.
41. A manufacturer of athletic footwear finds that the sales of their ZipStride brand running shoes is a function $f(p)$ of selling price $p$. Suppose that $f(120) = 9000\text{ pairs}$ and $f'(120) = -60\text{ pairs/dollar}$. Revenue $R(p) = p \cdot f(p)$. Find $R'(120)$. What impact would a small increase in price have on revenue?
42. Solve the problem in Exercise 41 under the assumption that $f(120) = 9000$ and $f'(120) = -80$.
43. Use the quotient rule (Theorem 2.4.2) to derive the formula for the derivative of $f(x) = x^{-n}$, where $n$ is a positive integer.

---

## 2.5 DERIVATIVES OF TRIGONOMETRIC FUNCTIONS

The main objective of this section is to obtain formulas for the derivatives of the six basic trigonometric functions (with $x$ in radians).

### DERIVATIVE OF $\sin x$ AND $\cos x$

Using $\lim_{h \to 0} \frac{\sin h}{h} = 1$ and $\lim_{h \to 0} \frac{1 - \cos h}{h} = 0$:
$$\frac{d}{dx}[\sin x] = \lim_{h \to 0} \frac{\sin(x + h) - \sin x}{h} = \lim_{h \to 0} \frac{\sin x\cos h + \cos x\sin h - \sin x}{h} = \cos x \tag{3}$$
$$\frac{d}{dx}[\cos x] = -\sin x \tag{4}$$

### DERIVATIVES OF OTHER TRIGONOMETRIC FUNCTIONS

$$\frac{d}{dx}[\tan x] = \sec^2 x \tag{5}$$
$$\frac{d}{dx}[\sec x] = \sec x \tan x \tag{6}$$
$$\frac{d}{dx}[\cot x] = -\csc^2 x \tag{7}$$
$$\frac{d}{dx}[\csc x] = -\csc x \cot x \tag{8}$$

#### Example 1
$\frac{d}{dx}[x\sin x] = x\cos x + \sin x$.

#### Example 2
$\frac{d}{dx}\left[\frac{\sin x}{1 + \cos x}\right] = \frac{(1 + \cos x)(\cos x) - (\sin x)(-\sin x)}{(1 + \cos x)^2} = \frac{1}{1 + \cos x}$.

#### Example 3
For $f(x) = \sec x$: $f'(x) = \sec x\tan x, \ f''(x) = \sec^3 x + \sec x\tan^2 x$.  
$f''(\pi/4) = (\sqrt{2})^3 + (\sqrt{2})(1)^2 = 3\sqrt{2}$.

#### Example 4 (Flagpole Shadow)
Shadow length $s = 50\cot\theta$. $\frac{ds}{d\theta} = -50\csc^2\theta$.  
At $\theta = 45^\circ$ ($\pi/4$ rad): $\frac{ds}{d\theta} = -100\text{ ft/rad} = -\frac{5\pi}{9}\text{ ft/deg} \approx -1.75\text{ ft/deg}$.

#### Example 5 (Simple Harmonic Motion)
Position $s = -3\cos t\text{ cm}$. Velocity $v = 3\sin t\text{ cm/s}$. The mass oscillates periodically between $-3\text{ cm}$ and $3\text{ cm}$ with period $2\pi\text{ s}$.

---

### QUICK CHECK EXERCISES 2.5
*(See page 153 for answers.)*

1. Find $dy/dx$: (a) $y = \sin x$ (b) $y = \cos x$ (c) $y = \tan x$ (d) $y = \sec x$.
2. Find $f'(x)$ and $f'(\pi/3)$ if $f(x) = \sin x\cos x$.
3. Use a derivative to evaluate each limit:  
   (a) $\lim_{h \to 0} \frac{\sin(\pi/2 + h) - 1}{h}$  
   (b) $\lim_{h \to 0} \frac{\csc(x + h) - \csc x}{h}$

#### QUICK CHECK ANSWERS 2.5
1. (a) $\cos x$ (b) $-\sin x$ (c) $\sec^2 x$ (d) $\sec x\tan x$  
2. $f'(x) = \cos^2 x - \sin^2 x, \ f'(\pi/3) = -\frac{1}{2}$  
3. (a) $\frac{d}{dx}[\sin x]\Big|_{x=\pi/2} = 0$ (b) $\frac{d}{dx}[\csc x] = -\csc x\cot x$

---

### EXERCISE SET 2.5

**1–18 Find $f'(x)$.**

1. $f(x) = 4\cos x + 2\sin x$
2. $f(x) = \frac{5}{x^2} + \sin x$
3. $f(x) = -4x^2\cos x$
4. $f(x) = 2\sin^2 x$
5. $f(x) = \frac{5 - \cos x}{5 + \sin x}$
6. $f(x) = \frac{\sin x}{x^2 + \sin x}$
7. $f(x) = \sec x - \sqrt{2}\tan x$
8. $f(x) = (x^2 + 1)\sec x$
9. $f(x) = 4\csc x - \cot x$
10. $f(x) = \cos x - x\csc x$
11. $f(x) = \sec x\tan x$
12. $f(x) = \csc x\cot x$
13. $f(x) = \frac{\cot x}{1 + \csc x}$
14. $f(x) = \frac{\sec x}{1 + \tan x}$
15. $f(x) = \sin^2 x + \cos^2 x$
16. $f(x) = \sec^2 x - \tan^2 x$
17. $f(x) = \frac{\sin x\sec x}{1 + x\tan x}$
18. $f(x) = \frac{(x^2 + 1)\cot x}{3 - \cos x\csc x}$

**19–24 Find $d^2y/dx^2$.**

19. $y = x\cos x$
20. $y = \csc x$
21. $y = x\sin x - 3\cos x$
22. $y = x^2\cos x + 4\sin x$
23. $y = \sin x\cos x$
24. $y = \tan x$

25. Find the equation of the line tangent to the graph of $\tan x$ at (a) $x = 0$ (b) $x = \pi/4$ (c) $x = -\pi/4$.
26. Find the equation of the line tangent to the graph of $\sin x$ at (a) $x = 0$ (b) $x = \pi$ (c) $x = \pi/4$.
27. (a) Show that $y = x\sin x$ is a solution to $y'' + y = 2\cos x$.  
    (b) Show that $y = x\sin x$ is a solution of $y^{(4)} + y'' = -2\cos x$.
28. (a) Show that $y = \cos x$ and $y = \sin x$ are solutions of $y'' + y = 0$.  
    (b) Show that $y = A\sin x + B\cos x$ is a solution of $y'' + y = 0$ for all constants $A$ and $B$.
29. Find all values in $[-2\pi, 2\pi]$ at which the graph of $f$ has a horizontal tangent line:  
    (a) $f(x) = \sin x$  
    (b) $f(x) = x + \cos x$  
    (c) $f(x) = \tan x$  
    (d) $f(x) = \sec x$
30. (a) Use a graphing utility to make rough estimates of the values in $[0, 2\pi]$ at which the graph of $y = \sin x\cos x$ has a horizontal tangent line.  
    (b) Find the exact locations of the points where the graph has a horizontal tangent line.
31. A 10 ft ladder leans against a wall at an angle $\theta$ with the horizontal (Figure Ex-31). The top is $x$ feet above ground. If pushed toward the wall, find the rate at which $x$ changes with respect to $\theta$ when $\theta = 60^\circ$ (in ft/deg).
32. An airplane is flying horizontally at $3800\text{ ft}$ (Figure Ex-32). At what rate is distance $s$ to fixed point $P$ changing with respect to $\theta$ when $\theta = 30^\circ$ (in ft/deg)?
33. A searchlight is $50\text{ m}$ from a tall building (Figure Ex-33). Find the rate at which illuminated spot height $D$ changes with respect to $\theta$ when $\theta = 45^\circ$ (in m/deg).
34. Satellite horizon sensor with Earth radius $r = 6378\text{ km}$:  
    (a) Show $h = r(\csc\theta - 1)$.  
    (b) Find $dh/d\theta$ at $\theta = 30^\circ$ (in km/deg).

**35–38 True–False Determine whether the statement is true or false. Explain your answer.**

35. If $g(x) = f(x)\sin x$, then $g'(x) = f'(x)\cos x$.
36. If $g(x) = f(x)\sin x$, then $g'(0) = f(0)$.
37. If $f(x)\cos x = \sin x$, then $f'(x) = \sec^2 x$.
38. Suppose that $g(x) = f(x)\sec x$, where $f(0) = 8$ and $f'(0) = -2$. Then $g'(0) = 8\sec 0\tan 0 = 0$.

**39–40 Calculate the first few derivatives and observe the pattern.**

39. $\frac{d^{87}}{dx^{87}}[\sin x]$
40. $\frac{d^{100}}{dx^{100}}[\cos x]$

41. Let $f(x) = \cos x$. Find all positive integers $n$ for which $f^{(n)}(x) = \sin x$.
42. Let $f(x) = \sin x$. Find all positive integers $n$ for which $f^{(n)}(x) = \sin x$.

**FOCUS ON CONCEPTS**

43. In each part, determine where $f$ is differentiable:  
    (a) $\sin x$ (b) $\cos x$ (c) $\tan x$ (d) $\cot x$ (e) $\sec x$ (f) $\csc x$ (g) $\frac{1}{1 + \cos x}$ (h) $\frac{1}{\sin x\cos x}$ (i) $\frac{\cos x}{2 - \sin x}$
44. (a) Derive $\frac{d}{dx}[\cos x] = -\sin x$ using derivative definition.  
    (b) Use $\sin x, \cos x$ derivatives to obtain $\cot x$ derivative.  
    (c) Obtain $\sec x$ derivative.  
    (d) Obtain $\csc x$ derivative.
45. Derive $\frac{d}{dx}[\sin x] = \cos x$ using the difference identity $\sin\alpha - \sin\beta = 2\sin\left(\frac{\alpha - \beta}{2}\right)\cos\left(\frac{\alpha + \beta}{2}\right)$.
46. Derive $\frac{d}{dx}[\cos x] = -\sin x$ using the difference identity $\cos\alpha - \cos\beta = -2\sin\left(\frac{\alpha - \beta}{2}\right)\sin\left(\frac{\alpha + \beta}{2}\right)$.
47. (a) Show $\lim_{h \to 0} \frac{\tan h}{h} = 1$.  
    (b) Derive the derivative of $\tan x$ directly from definition.
48. Without using trigonometric identities, find $\lim_{x \to 0} \frac{\tan(x + y) - \tan y}{x}$.
49. If $x$ is measured in degrees, prove:  
    (a) $\frac{d}{dx}[\sin x] = \frac{\pi}{180}\cos x$  
    (b) $\frac{d}{dx}[\cos x] = -\frac{\pi}{180}\sin x$.
50. **Writing.** Relationship between periodicity of $f$ and $f'$.

---

## 2.6 THE CHAIN RULE

In this section we will derive a formula that expresses the derivative of a composition $f \circ g$ in terms of the derivatives of $f$ and $g$.

### THE CHAIN RULE

> **2.6.1 THEOREM (The Chain Rule)**  
> If $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then the composition $f \circ g$ is differentiable at $x$. Moreover, if $y = f(g(x))$ and $u = g(x)$, then $y = f(u)$ and
> $$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} \tag{1}$$

*Alternative form:*
$$\frac{d}{dx}[f(g(x))] = f'(g(x))g'(x) \tag{2}$$

#### Example 1
Find $dy/dx$ if $y = \cos(x^3)$.

**Solution.** Let $u = x^3, y = \cos u$. $\frac{dy}{dx} = (-\sin u)(3x^2) = -3x^2\sin(x^3)$.

#### Example 2
Find $dw/dt$ if $w = \tan x$ and $x = 4t^3 + t$.

**Solution.** $\frac{dw}{dt} = \frac{dw}{dx}\frac{dx}{dt} = (\sec^2 x)(12t^2 + 1) = (12t^2 + 1)\sec^2(4t^3 + t)$.

#### Example 3 & 4
* $\frac{d}{dx}[\tan^2 x] = 2\tan x\sec^2 x$
* $\frac{d}{dx}[\sqrt{x^2 + 1}] = \frac{x}{\sqrt{x^2 + 1}}$

---

### GENERALIZED DERIVATIVE FORMULAS

$$\frac{d}{dx}[f(u)] = f'(u)\frac{du}{dx} \tag{3}$$

#### Table 2.6.1: Generalized Derivative Formulas
| Function | Generalized Derivative |
| :--- | :--- |
| $u^r$ | $\frac{d}{dx}[u^r] = ru^{r-1}\frac{du}{dx}$ |
| $\sin u$ | $\frac{d}{dx}[\sin u] = \cos u\frac{du}{dx}$ |
| $\cos u$ | $\frac{d}{dx}[\cos u] = -\sin u\frac{du}{dx}$ |
| $\tan u$ | $\frac{d}{dx}[\tan u] = \sec^2 u\frac{du}{dx}$ |
| $\cot u$ | $\frac{d}{dx}[\cot u] = -\csc^2 u\frac{du}{dx}$ |
| $\sec u$ | $\frac{d}{dx}[\sec u] = \sec u\tan u\frac{du}{dx}$ |
| $\csc u$ | $\frac{d}{dx}[\csc u] = -\csc u\cot u\frac{du}{dx}$ |

#### Example 5 & 6
* $\frac{d}{dx}[\sin(2x)] = 2\cos(2x)$
* $\frac{d}{dx}[\tan(x^2 + 1)] = 2x\sec^2(x^2 + 1)$
* $\frac{d}{dx}[\sqrt{x^3 + \csc x}] = \frac{3x^2 - \csc x\cot x}{2\sqrt{x^3 + \csc x}}$
* $\frac{d}{dx}[(x^2 - x + 2)^{3/4}] = \frac{3}{4}(x^2 - x + 2)^{-1/4}(2x - 1)$
* $\frac{d}{dx}[(1 + x^5\cot x)^{-8}] = (8x^5\csc^2 x - 40x^4\cot x)(1 + x^5\cot x)^{-9}$
* $\frac{d}{dx}[\sin(\sqrt{1 + \cos x})] = -\frac{\sin x\cos(\sqrt{1 + \cos x})}{2\sqrt{1 + \cos x}}$
* $\frac{d\mu}{dt} = \sec\sqrt{\omega t}\tan\sqrt{\omega t}\frac{\omega}{2\sqrt{\omega t}}$ where $\mu = \sec\sqrt{\omega t}$.

---

### QUICK CHECK EXERCISES 2.6
*(See page 160 for answers.)*

1. The chain rule states that the derivative of the composition of two functions is the derivative of the $\underline{\hspace{1cm}}$ function evaluated at the $\underline{\hspace{1cm}}$ function times the derivative of the $\underline{\hspace{1cm}}$ function.
2. If $y$ is a differentiable function of $u$, and $u$ is a differentiable function of $x$, then $\frac{dy}{dx} = \underline{\hspace{1cm}} \cdot \underline{\hspace{1cm}}$.
3. Find $dy/dx$: (a) $y = (x^2 + 5)^{10}$ (b) $y = \sqrt{1 + 6x}$.
4. Find $dy/dx$: (a) $y = \sin(3x + 2)$ (b) $y = (x^2\tan x)^4$.
5. Suppose that $f(2) = 3, f'(2) = 4, g(3) = 6,$ and $g'(3) = -5$. Evaluate:  
   (a) $h'(2)$, where $h(x) = g(f(x))$  
   (b) $k'(3)$, where $k(x) = f\left(\frac{1}{3}g(x)\right)$.

#### QUICK CHECK ANSWERS 2.6
1. outside; inside; inside  
2. $\frac{dy}{du} \cdot \frac{du}{dx}$  
3. (a) $20x(x^2 + 5)^9$ (b) $\frac{3}{\sqrt{1 + 6x}}$  
4. (a) $3\cos(3x + 2)$ (b) $4(x^2\tan x)^3(2x\tan x + x^2\sec^2 x)$  
5. (a) $g'(f(2))f'(2) = -20$ (b) $f'\left(\frac{1}{3}g(3)\right)\cdot \frac{1}{3}g'(3) = -\frac{20}{3}$

---

### EXERCISE SET 2.6

1. Given that $f'(0) = 2, g(0) = 0,$ and $g'(0) = 3$, find $(f \circ g)'(0)$.
2. Given that $f'(9) = 5, g(2) = 9,$ and $g'(2) = -3$, find $(f \circ g)'(2)$.
3. Let $f(x) = x^5$ and $g(x) = 2x - 3$: (a) Find $(f \circ g)(x)$ and $(f \circ g)'(x)$. (b) Find $(g \circ f)(x)$ and $(g \circ f)'(x)$.
4. Let $f(x) = 5\sqrt{x}$ and $g(x) = 4 + \cos x$: (a) Find $(f \circ g)(x)$ and $(f \circ g)'(x)$. (b) Find $(g \circ f)(x)$ and $(g \circ f)'(x)$.

**FOCUS ON CONCEPTS**

5. Given table: $x=3: f=5, f'=-2, g=5, g'=7$; $x=5: f=3, f'=-1, g=12, g'=4$.  
   (a) $F'(3)$ where $F(x) = f(g(x))$ (b) $G'(3)$ where $G(x) = g(f(x))$.
6. Given table: $x=-1: f=2, f'=3, g=2, g'=-3$; $x=2: f=0, f'=4, g=1, g'=-5$.  
   (a) $F'(-1)$ where $F(x) = f(g(x))$ (b) $G'(-1)$ where $G(x) = g(f(x))$.

**7–26 Find $f'(x)$.**

7. $f(x) = (x^3 + 2x)^{37}$
8. $f(x) = (3x^2 + 2x - 1)^6$
9. $f(x) = \left(\frac{x^3 - 7}{x}\right)^{-2}$
10. $f(x) = \frac{1}{(x^5 - x + 1)^9}$
11. $f(x) = \frac{4}{(3x^2 - 2x + 1)^3}$
12. $f(x) = \sqrt{x^3 - 2x + 5}$
13. $f(x) = \sqrt{4 + \sqrt{3x}}$
14. $f(x) = \sqrt[3]{12 + \sqrt{x}}$
15. $f(x) = \sin(1/x^2)$
16. $f(x) = \tan\sqrt{x}$
17. $f(x) = 4\cos^5 x$
18. $f(x) = 4x + 5\sin^4 x$
19. $f(x) = \cos^2(3\sqrt{x})$
20. $f(x) = \tan^4(x^3)$
21. $f(x) = 2\sec^2(x^7)$
22. $f(x) = \cos^3\left(\frac{x}{x + 1}\right)$
23. $f(x) = \sqrt{\cos(5x)}$
24. $f(x) = \sqrt{3x - \sin^2(4x)}$
25. $f(x) = [x + \csc(x^3 + 3)]^{-3}$
26. $f(x) = [x^4 - \sec(4x^2 - 2)]^{-4}$

**27–40 Find $dy/dx$.**

27. $y = x^3\sin^2(5x)$
28. $y = \sqrt{x}\tan^3(\sqrt{x})$
29. $y = x^5\sec(1/x)$
30. $y = \frac{\sin x}{\sec(3x + 1)}$
31. $y = \cos(\cos x)$
32. $y = \sin(\tan 3x)$
33. $y = \cos^3(\sin 2x)$
34. $y = \frac{1 + \csc(x^2)}{1 - \cot(x^2)}$
35. $y = (5x + 8)^7(1 - \sqrt{x})^6$
36. $y = (x^2 + x)^5\sin^8 x$
37. $y = \left(\frac{x - 5}{2x + 1}\right)^3$
38. $y = \left(\frac{1 + x^2}{1 - x^2}\right)^{17}$
39. $y = \frac{(2x + 3)^3}{(4x^2 - 1)^8}$
40. $y = [1 + \sin^3(x^5)]^{12}$

**41–42 [CAS] Use a CAS to find $dy/dx$.**

41. $y = [x\sin 2x + \tan^4(x^7)]^5$
42. $y = \tan^4\left(\frac{2 + (7 - x)\sqrt{3x^2 + 5}}{x^3 + \sin x}\right)$

**43–50 Find an equation for the tangent line to the graph at the specified value of $x$.**

43. $y = x\cos 3x, \quad x = \pi$
44. $y = \sin(1 + x^3), \quad x = -3$
45. $y = \sec^3(\pi/2 - x), \quad x = -\pi/2$
46. $y = (x - 1/x)^3, \quad x = 2$
47. $y = \tan(4x^2), \quad x = \sqrt{\pi}$
48. $y = 3\cot^4 x, \quad x = \pi/4$
49. $y = x^2\sqrt{5 - x^2}, \quad x = 1$
50. $y = \frac{x}{\sqrt{1 - x^2}}, \quad x = 0$

**51–54 Find $d^2y/dx^2$.**

51. $y = x\cos(5x) - \sin^2 x$
52. $y = \sin(3x^2)$
53. $y = \frac{1 + x}{1 - x}$
54. $y = x\tan(1/x)$

**55–58 Find the indicated derivative.**

55. $y = \cot^3(\pi - \theta)$; find $dy/d\theta$.
56. $\lambda = \left(\frac{au + b}{cu + d}\right)^6$; find $d\lambda/du$.
57. $\frac{d}{d\omega}[a\cos^2\pi\omega + b\sin^2\pi\omega]$.
58. $x = \csc^2(\pi/3 - y)$; find $dx/dy$.

59–60. Graphing utility investigations of $f(x) = x\sqrt{4 - x^2}$ and $f(x) = \sin x^2\cos x$.

**61–64 True–False Determine whether the statement is true or false. Explain your answer.**

61. If $y = f(x)$, then $\frac{d}{dx}[\sqrt{y}] = \sqrt{f'(x)}$.
62. If $y = f(u)$ and $u = g(x)$, then $dy/dx = f'(x) \cdot g'(x)$.
63. If $y = \cos[g(x)]$, then $dy/dx = -\sin[g'(x)]$.
64. If $y = \sin^3(3x^3)$, then $dy/dx = 27x^2\sin^2(3x^3)\cos(3x^3)$.

65. Simple harmonic motion: $y = A\cos\omega t$.  
    (a) Show $\frac{d^2y}{dt^2} = -\omega^2 y$.  
    (b) Show period $T = 2\pi/\omega$.  
    (c) Frequency $f = 1/T$.  
    (d) Amplitude, period, frequency for $y = 0.6\cos 15t$.
66. Find $A$ so that $y = A\sin 3t$ satisfies $\frac{d^2y}{dt^2} + 2y = 4\sin 3t$.

**FOCUS ON CONCEPTS**

67. From Figure Ex-67, evaluate $\frac{d}{dx}[\sqrt{x + f(x)}]\Big|_{x=-1}$.
68. Evaluate $\frac{d}{dx}[f(2\sin x)]\Big|_{x=\pi/6}$.
69. Atmospheric pressure $p$ vs altitude $h$: estimate $p, dp/dh$ at $h = 2\text{ mi}$, and time rate of change.
70. Crate drag force $F = \frac{\mu W}{\cos\theta + \mu\sin\theta}$ with $W = 150\text{ lb}, \mu = 0.3$.
71. Find $\frac{d}{dx}[|\sin x|]$ on $(-\pi, \pi)$ for $x \neq 0$.
72. Derive $\frac{d}{dx}[\cos x]$ using $\cos x = \sin(\pi/2 - x)$.
73. Continuity and non-differentiability of $f(x) = \begin{cases} x\sin(1/x), & x \neq 0 \\ 0, & x = 0 \end{cases}$.
74. Continuity and differentiability of $f(x) = \begin{cases} x^2\sin(1/x), & x \neq 0 \\ 0, & x = 0 \end{cases}$.
75. Table derivatives for $g(x) = [f(x)]^3$ and $h(x) = f(x^3)$.
76. $f'(x) = \sqrt{3x + 4}, g(x) = x^2 - 1 \implies$ find $F'(x) = (f \circ g)'(x)$.
77. $f'(x) = \frac{x}{x^2 + 1}, g(x) = \sqrt{3x - 1} \implies$ find $F'(x)$.
78. Find $f'(x^2)$ if $\frac{d}{dx}[f(x^2)] = x^2$.
79. Find $\frac{d}{dx}[f(x)]$ if $\frac{d}{dx}[f(3x)] = 6x$.
80. Prove: $f'$ is odd if $f$ is even; $f'$ is even if $f$ is odd.
81. Geometric illustrations of parity derivative rules.
82. Four-link chain rule: $y = f_1(u), u = f_2(v), v = f_3(w), w = f_4(x)$.
83. Formula for $\frac{d}{dx}[f(g(h(x)))]$.
84. **Writing.** Cofunction derivative relations.

---

## 2.7 IMPLICIT DIFFERENTIATION

### FUNCTIONS DEFINED EXPLICITLY AND IMPLICITLY

> **2.7.1 DEFINITION**  
> We will say that a given equation in $x$ and $y$ defines the function $f$ **implicitly** if the graph of $y = f(x)$ coincides with a portion of the graph of the equation.

#### Example 1
$x = y^2$ implicitly defines $f_1(x) = \sqrt{x}$ and $f_2(x) = -\sqrt{x}$.

> **René Descartes (1596–1650)**  
> French philosopher and mathematician. Graduated with a law degree, served as military engineer, invented analytic geometry (*Discourse on the Method*, 1637), and co-founded modern physiology.

---

### IMPLICIT DIFFERENTIATION METHOD

#### Example 2
Find $dy/dx$ if $5y^2 + \sin y = x^2$.

**Solution.**
$$\frac{d}{dx}[5y^2 + \sin y] = \frac{d}{dx}[x^2] \implies 10y\frac{dy}{dx} + \cos y\frac{dy}{dx} = 2x \implies \frac{dy}{dx} = \frac{2x}{10y + \cos y}$$

#### Example 3
Find $d^2y/dx^2$ if $4x^2 - 2y^2 = 9$.

**Solution.**
$$8x - 4y\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = \frac{2x}{y}$$
$$\frac{d^2y}{dx^2} = \frac{y(2) - 2x(dy/dx)}{y^2} = \frac{2y - 2x(2x/y)}{y^2} = \frac{2y^2 - 4x^2}{y^3} = -\frac{9}{y^3}$$

#### Example 4
Slopes of tangent lines to $y^2 - x + 1 = 0$ at $(2, -1)$ and $(2, 1)$:
$$2y\frac{dy}{dx} - 1 = 0 \implies \frac{dy}{dx} = \frac{1}{2y}$$
At $(2, -1)$, slope is $-1/2$; at $(2, 1)$, slope is $1/2$.

#### Example 5 (Folium of Descartes)
$x^3 + y^3 = 3xy$.  
(a) $3x^2 + 3y^2\frac{dy}{dx} = 3x\frac{dy}{dx} + 3y \implies \frac{dy}{dx} = \frac{y - x^2}{y^2 - x}$.  
(b) Tangent line at $(3/2, 3/2)$: slope $m = -1 \implies y - 3/2 = -(x - 3/2) \implies x + y = 3$.  
(c) Horizontal tangent: $y = x^2 \implies x^3 + x^6 = 3x^3 \implies x^3(x^3 - 2) = 0 \implies x = 2^{1/3}$, point $(2^{1/3}, 2^{2/3}) \approx (1.26, 1.59)$.

---

### QUICK CHECK EXERCISES 2.7
*(See page 167 for answers.)*

1. The equation $xy + 2y = 1$ defines implicitly the function $y = \underline{\hspace{1cm}}$.
2. Use implicit differentiation to find $dy/dx$ for $x^2 - y^3 = xy$.
3. The slope of the tangent line to the graph of $x + y + xy = 3$ at $(1, 1)$ is $\underline{\hspace{1cm}}$.
4. Use implicit differentiation to find $d^2y/dx^2$ for $\sin y = x$.

#### QUICK CHECK ANSWERS 2.7
1. $\frac{1}{x + 2}$  
2. $\frac{dy}{dx} = \frac{2x - y}{x + 3y^2}$  
3. $-1$  
4. $\frac{d^2y}{dx^2} = \sec^2 y\tan y$

---

### EXERCISE SET 2.7

**1–2 (a) Find $dy/dx$ by differentiating implicitly. (b) Solve for $y$ in terms of $x$ and differentiate. (c) Confirm consistency.**

1. $x + xy - 2x^3 = 2$
2. $\sqrt{y} - \sin x = 2$

**3–12 Find $dy/dx$ by implicit differentiation.**

3. $x^2 + y^2 = 100$
4. $x^3 + y^3 = 3xy^2$
5. $x^2y + 3xy^3 - x = 3$
6. $x^3y^2 - 5x^2y + x = 1$
7. $\frac{1}{\sqrt{x}} + \frac{1}{\sqrt{y}} = 1$
8. $x^2 = \frac{x + y}{x - y}$
9. $\sin(x^2y^2) = x$
10. $\cos(xy^2) = y$
11. $\tan^3(xy^2 + y) = x$
12. $\frac{xy^3}{1 + \sec y} = 1 + y^4$

**13–18 Find $d^2y/dx^2$ by implicit differentiation.**

13. $2x^2 - 3y^2 = 4$
14. $x^3 + y^3 = 1$
15. $x^3y^3 - 4 = 0$
16. $xy + y^2 = 2$
17. $y + \sin y = x$
18. $x\cos y = y$

**19–20 Find slopes in two ways: by solving for $y$ and by implicit differentiation.**

19. $x^2 + y^2 = 1; \quad (1/2, \sqrt{3}/2), (1/2, -\sqrt{3}/2)$
20. $y^2 - x + 1 = 0; \quad (10, 3), (10, -3)$

**21–24 True–False Determine whether the statement is true or false. Explain your answer.**

21. If an equation in $x$ and $y$ defines a function $y = f(x)$ implicitly, then the graph of the equation and the graph of $f$ are identical.
22. $f(x) = \begin{cases} \sqrt{1 - x^2}, & 0 < x \le 1 \\ -\sqrt{1 - x^2}, & -1 \le x \le 0 \end{cases}$ is defined implicitly by $x^2 + y^2 = 1$.
23. The function $|x|$ is not defined implicitly by $(x + y)(x - y) = 0$.
24. If $y$ is defined implicitly as a function of $x$ by $x^2 + y^2 = 1$, then $dy/dx = -x/y$.

25. Proof of Power Rule for negative integer exponents via implicit differentiation of $y = x^m = 1/x^{-m}$.
26. Proof of Power Rule for rational exponents $r = m/n$ via implicit differentiation of $y^n = x^m$.

**27–30 Find tangent line slopes at specified points:**

27. $x^4 + y^4 = 16; \quad (1, \sqrt[4]{15})$ [Lamé's special quartic]
28. $y^3 + yx^2 + x^2 - 3y^2 = 0; \quad (0, 3)$ [trisectrix]
29. $2(x^2 + y^2)^2 = 25(x^2 - y^2); \quad (3, 1)$ [lemniscate]
30. $x^{2/3} + y^{2/3} = 4; \quad (-1, 3\sqrt{3})$ [four-cusped hypocycloid]

**31–34 Find the specified derivative:**

31. $a^4 - t^4 = 6a^2t; \quad da/dt$
32. $\sqrt{u} + \sqrt{v} = 5; \quad du/dv$
33. $a^2\omega^2 + b^2\lambda^2 = 1; \quad d\omega/d\lambda$
34. $y = \sin x; \quad dx/dy$

**FOCUS ON CONCEPTS**

35. Horizontal tangents of ellipse $x^2 + xy + y^2 = 3$ along $y = -2x$.
36. Horizontal tangents of rotated ellipse $x^2 - xy + y^2 = 1$.
37. CAS analysis of $y^4 + y^2 = x(x - 1)$.
38. Vertical tangents of $y^4 + y^2 = x(x - 1)$.
39. Parameters $a, b$ for $x^2y + ay^2 = b$ with tangent $4x + 3y = 7$ at $(1, 1)$.
40. Points where tangent to $y^3 = 2x^2$ is perpendicular to $x + 2y - 2 = 0$.
41–42. Tangents to rotated ellipse $x^2 - xy + y^2 = 4$.
43–44. Orthogonal trajectories for circles $x^2 + (y - c)^2 = c^2$ & $(x - k)^2 + y^2 = k^2$, and hyperbolas $xy = c$ & $x^2 - y^2 = k$.
45–46. CAS analysis of $x^3 - 2xy + y^3 = 0$.
47. $dy/dx$ given $2y^3t + t^3y = 1$ and $dt/dx = 1/\cos t$.
48. Tangent lines from origin to ellipse $2x^2 - 4x + y^2 + 1 = 0$.
49. **Writing.** Explicit vs implicit function definitions.
50. **Writing.** Meaning of undefined implicit derivative expressions.

---

## 2.8 RELATED RATES

In this section we will study related rates problems, where one tries to find the rate at which some quantity is changing by relating it to other quantities whose rates of change are known.

### STRATEGY FOR SOLVING RELATED RATES PROBLEMS

* **Step 1.** Assign letters to all quantities that vary with time. Give a definition for each letter.
* **Step 2.** Identify the rates of change that are known and the rate of change that is to be found. Interpret each rate as a derivative.
* **Step 3.** Find an equation that relates the variables. Draw an appropriately labeled figure.
* **Step 4.** Differentiate both sides of the equation with respect to time $t$.
* **Step 5.** Substitute all known values for the variables and rates of change, then solve for the unknown rate of change.

#### Example 1
$y = x^3$. Find $dy/dt$ at $t = 1$ if $x = 2$ and $dx/dt = 4$.  
$$\frac{dy}{dt} = 3x^2\frac{dx}{dt} = 3(2^2)(4) = 48$$

#### Example 2 (Oil Spill)
Circular spill $A = \pi r^2$. If $dr/dt = 2\text{ ft/s}$, find $dA/dt$ when $r = 60\text{ ft}$.  
$$\frac{dA}{dt} = 2\pi r\frac{dr}{dt} = 2\pi(60)(2) = 240\pi\text{ ft}^2\text{/s} \approx 754\text{ ft}^2\text{/s}$$

#### Example 3 (Baseball Diamond)
Diamond $90\text{ ft}$ square. Player runs 2nd to 3rd at $30\text{ ft/s}$. When $x = 20\text{ ft}$ from 3rd, distance to home is $y = \sqrt{20^2 + 90^2} = 10\sqrt{85}\text{ ft}$.
$$x^2 + 90^2 = y^2 \implies 2x\frac{dx}{dt} = 2y\frac{dy}{dt} \implies \frac{dy}{dt} = \frac{20}{10\sqrt{85}}(-30) = -\frac{60}{\sqrt{85}} \approx -6.51\text{ ft/s}$$

#### Example 4 (Rocket Tracking Camera)
Camera $3000\text{ ft}$ from pad. Rocket rising at $880\text{ ft/s}$ at height $h = 4000\text{ ft}$.
$$\tan\phi = \frac{h}{3000} \implies \sec^2\phi\frac{d\phi}{dt} = \frac{1}{3000}\frac{dh}{dt}$$
When $h = 4000$, $\sec\phi = 5000/3000 = 5/3$.
$$\left(\frac{5}{3}\right)^2\frac{d\phi}{dt} = \frac{880}{3000} \implies \frac{d\phi}{dt} = \frac{66}{625} \approx 0.11\text{ rad/s} \approx 6.05^\circ\text{/s}$$

#### Example 5 (Conical Filter Draining)
Cone height $16\text{ cm}$, radius $4\text{ cm}$. Drainage rate $dV/dt = -2\text{ cm}^3\text{/min}$.  
$r/y = 4/16 \implies r = y/4$. Volume $V = \frac{1}{3}\pi (y/4)^2 y = \frac{\pi}{48}y^3$.
$$\frac{dV}{dt} = \frac{\pi}{16}y^2\frac{dy}{dt} \implies \frac{dy}{dt} = \frac{16}{\pi y^2}(-2) = -\frac{32}{\pi y^2}$$
When $y = 8\text{ cm}$: $\frac{dy}{dt} = -\frac{32}{\pi(64)} = -\frac{1}{2\pi} \approx -0.16\text{ cm/min}$.

---

### QUICK CHECK EXERCISES 2.8
*(See page 175 for answers.)*

1. If $A = x^2$ and $\frac{dx}{dt} = 3$, find $\frac{dA}{dt}\Big|_{x=10}$.
2. If $A = x^2$ and $\frac{dA}{dt} = 3$, find $\frac{dx}{dt}\Big|_{x=10}$.
3. A 10-foot ladder stands on a horizontal floor and leans against a vertical wall. Use $x$ for the floor distance and $y$ for wall height. Find an equation relating the rates of change of $x$ and $y$.
4. Suppose that a block of cylindrical ice melts retaining its shape. Find an equation relating rates of change of $V, h,$ and $r$.

#### QUICK CHECK ANSWERS 2.8
1. $60$  
2. $\frac{3}{20}$  
3. $x\frac{dx}{dt} + y\frac{dy}{dt} = 0$  
4. $\frac{dV}{dt} = 2\pi rh\frac{dr}{dt} + \pi r^2\frac{dh}{dt}$

---

### EXERCISE SET 2.8

**1–4 Both $x$ and $y$ denote functions of $t$ that are related by the given equation. Find the specified derivative.**

1. $y = 3x + 5$: (a) $dx/dt = 2$, find $dy/dt$ at $x = 1$. (b) $dy/dt = -1$, find $dx/dt$ at $x = 0$.
2. $x + 4y = 3$: (a) $dx/dt = 1$, find $dy/dt$ at $x = 2$. (b) $dy/dt = 4$, find $dx/dt$ at $x = 3$.
3. $4x^2 + 9y^2 = 1$: (a) $dx/dt = 3$, find $dy/dt$ at $(1/(2\sqrt{2}), 1/(3\sqrt{2}))$. (b) $dy/dt = 8$, find $dx/dt$ at $(1/3, -\sqrt{5}/9)$.
4. $x^2 + y^2 = 2x + 4y$: (a) $dx/dt = -5$, find $dy/dt$ at $(3, 1)$. (b) $dy/dt = 6$, find $dx/dt$ at $(1 + \sqrt{2}, 2 + \sqrt{3})$.

**FOCUS ON CONCEPTS**

5. Square of side $x$: (a) figure (b) $A = x^2$ (c) $dA/dt = 2x(dx/dt)$ (d) rate when $x = 3\text{ ft}, dx/dt = 2\text{ ft/min}$.
6. Circle of radius $r$: rate when $r = 5\text{ cm}, dr/dt = 2\text{ cm/s}$.
7. Cylinder volume: $h = 6\text{ in}, dh/dt = 1\text{ in/s}, r = 10\text{ in}, dr/dt = -1\text{ in/s}$.
8. Rectangle diagonal: $x = 3\text{ ft}, y = 4\text{ ft}, dx/dt = 1/2\text{ ft/s}, dy/dt = -1/4\text{ ft/s}$.
9. Right triangle angle $\theta$: $x = 2, y = 2, dx/dt = 1, dy/dt = -1/4$.
10. $z = x^3y^2$ with $x = 1, y = 2, dx/dt = -2, dy/dt = 3$.
11. Clock minute hand ($4\text{ in}$): rate of area swept out.
12. Pond circular ripple: $dr/dt = 3\text{ ft/s}$ after $10\text{ s}$.
13. Oil spill: $dA/dt = 6\text{ mi}^2\text{/h}$, find $dr/dt$ when area is $9\text{ mi}^2$.
14. Spherical balloon inflation: $dV/dt = 3\text{ ft}^3\text{/min}$, diameter rate when $r = 1\text{ ft}$.
15. Spherical balloon deflation: $dr/dt = -15\text{ cm/min}$, air removal rate when $r = 9\text{ cm}$.
16. $17\text{ ft}$ ladder pulled at $5\text{ ft/s}$: top descent rate when $8\text{ ft}$ high.
17. $13\text{ ft}$ ladder slipping at $2\text{ ft/s}$: foot speed when top is $5\text{ ft}$ high.
18. $10\text{ ft}$ plank pushed toward wall at $6\text{ in/s}$: rate of change of ground angle when $2\text{ ft}$ away.
19. Softball diamond ($60\text{ ft}$ square): runner 1st to 2nd at $25\text{ ft/s}$, rate of distance from home when $10\text{ ft}$ from 2nd.
20. Rocket rising tracked by radar $5\text{ mi}$ away: rocket speed when $4\text{ mi}$ high and distance increasing at $2000\text{ mi/h}$.
21. Rocket tracking camera: distance rate when rocket is $4000\text{ ft}$ up rising at $880\text{ ft/s}$.
22. Rocket tracking camera: rocket speed when $\theta = \pi/4$ and $d\theta/dt = 0.2\text{ rad/s}$.
23. Satellite elliptical orbit $r = \frac{4995}{1 + 0.12\cos\theta}$: (a) perigee and apogee altitudes (b) altitude rate when $\theta = 120^\circ, d\theta/dt = 2.7^\circ\text{/min}$.
24. Aircraft flying at $4000\text{ ft}$ altitude at $300\text{ mi/h}$: (a) $d\theta/dt$ when $\theta = 30^\circ$ (b) distance rate of change.
25. Conical water tank ($r = 10\text{ ft}, h = 24\text{ ft}$): depth rate when $16\text{ ft}$ deep and inflow is $20\text{ ft}^3\text{/min}$.
26. Conical grain pile ($h = 2r$): height rate when $h = 6\text{ ft}$ and flow is $8\text{ ft}^3\text{/min}$.
27. Conical sand pile ($h = 2r$): volume flow rate when $h = 10\text{ ft}$ and $dh/dt = 5\text{ ft/min}$.
28. Conical wheat pile ($r = h/2$): circumference rate when $h = 8\text{ ft}$ and flow is $10\text{ ft}^3\text{/min}$.
29. Aircraft climbing at $30^\circ$ at $500\text{ mi/h}$: altitude gain rate.
30. Boat pulled to dock by rope over pulley $10\text{ ft}$ high: speed when $125\text{ ft}$ rope is out and pulled at $20\text{ ft/min}$.
31. Rope pull rate to achieve boat speed of $12\text{ ft/min}$ at $125\text{ ft}$ rope length.
32. Man $6\text{ ft}$ walking at $3\text{ ft/s}$ toward $18\text{ ft}$ light: (a) shadow length rate (b) shadow tip speed.
33. Rotating beacon $4\text{ km}$ offshore (1 rev / 10 s): beam speed along straight shore at $45^\circ$.
34. Missile intercepting aircraft at right angles ($600\text{ mi/h}$ and $1200\text{ mi/h}$): distance rate when $2\text{ mi}$ and $4\text{ mi}$ from impact point.
35. Missile interception with flight path angle $120^\circ$.
36. Police helicopter at altitude $1/2\text{ mi}$ flying north at $100\text{ mi/h}$, car driving west at $75\text{ mi/h}$.
37. Particle on $\frac{xy^3}{1 + y^2} = \frac{8}{5}$ with $dx/dt = 6$ at $(1, 2)$: (a) $dy/dt$ (b) rising or falling.
38. Particle on $y = \sqrt{x^3 + 17}$ at $(2, 5)$ with $dy/dt = 2$: find $dx/dt$.
39. Particle on $y = 2x$ at $(3, 6)$ with $dx/dt = -2$: rate of distance from $(3, 0)$.
40. Particle on $y = \sqrt{x}$ at $x = 3$ with $dx/dt = 4$: (a) distance rate to $(2, 0)$ (b) angle of inclination rate.
41. Particle on $y = x/(x^2 + 1)$: points where $dx/dt = 3dy/dt$.
42. Particle on $16x^2 + 9y^2 = 144$: points where $dx/dt = dy/dt$.
43. Thin lens equation $1/s + 1/S = 1/f$ ($f = 6\text{ cm}$): image distance rate when $s = 10\text{ cm}, ds/dt = -2\text{ cm/s}$.
44. Water evaporating from conical reservoir proportional to surface area: show depth decreases at constant rate.
45. Spherical meteor burning proportional to surface area: show radius decreases at constant rate.
46. Clock hands ($4\text{ in}$ and $3\text{ in}$): rate of distance between tips at 9 o'clock.
47. Coffee pouring into truncated cone cup at $20\text{ cm}^3\text{/s}$: level rise rate halfway up.

---

## 2.9 LOCAL LINEAR APPROXIMATION; DIFFERENTIALS

### LOCAL LINEAR APPROXIMATION

> **Local Linear Approximation of $f$ at $x_0$**  
> $$f(x) \approx f(x_0) + f'(x_0)(x - x_0) \tag{1}$$
> or in increment form with $\Delta x = x - x_0$:
> $$f(x_0 + \Delta x) \approx f(x_0) + f'(x_0)\Delta x \tag{2}$$

#### Example 1
(a) Local linear approximation of $f(x) = \sqrt{x}$ at $x_0 = 1$:
$$\sqrt{x} \approx 1 + \frac{1}{2}(x - 1)$$
(b) Approximate $\sqrt{1.1} \approx 1 + \frac{1}{2}(0.1) = 1.05$ (calculator value: $1.04881$).

#### Example 2
(a) Local linear approximation of $\sin x$ at $x_0 = 0$: $\sin x \approx x$.  
(b) Approximate $\sin 2^\circ = \sin(\pi/90) \approx 0.0349066$ (calculator value: $0.0348995$).

---

### DIFFERENTIALS

Define $dx$ to be an independent variable, and define $dy$ by:
$$dy = f'(x)dx \tag{5}$$
If $dx \neq 0$, then $\frac{dy}{dx} = f'(x)$.
* $\Delta x = dx$
* $\Delta y = f(x + \Delta x) - f(x)$
* $\Delta y \approx dy = f'(x)dx \tag{7}$

#### Example 3 & 4
* For $y = x^2$: $dy = 2x\,dx$. At $x = 1$, $dy = 2\,dx$.
* For $y = \sqrt{x}$: $\Delta y = \sqrt{x + \Delta x} - \sqrt{x}$ and $dy = \frac{1}{2\sqrt{x}}dx$.  
  At $x = 4$ with $dx = \Delta x = 3$: $\Delta y = \sqrt{7} - 2 \approx 0.65$, $dy = \frac{1}{4}(3) = 0.75$.

---

### ERROR PROPAGATION

* Exact value: $x_0, y_0 = f(x_0)$
* Measured value: $x$
* Measurement error: $dx = \Delta x = x - x_0$
* Propagated error: $\Delta y = f(x) - f(x_0) \approx dy = f'(x)dx$
* Relative error: $\frac{\Delta q}{q} \approx \frac{dq}{q}$
* Percentage error: $\frac{\Delta q}{q} \times 100\%$

#### Example 5
Square side measured as $10\text{ in}$ with error at most $\pm 1/32\text{ in}$. Area $y = x^2$.  
$dy = 2x\,dx = 20\,dx$. Since $|dx| \le 1/32$, $|dy| \le 20(1/32) = 5/8\text{ in}^2$.

#### Example 6
Sphere diameter measured with percentage error $\pm 0.4\%$. Volume $V = \frac{1}{6}\pi x^3$.  
$$\frac{dV}{V} = \frac{\frac{1}{2}\pi x^2 dx}{\frac{1}{6}\pi x^3} = 3\frac{dx}{x}$$
Since $|dx/x| \le 0.004$, $|dV/V| \le 3(0.004) = 0.012 = 1.2\%$.

---

### DIFFERENTIAL FORMULAS

* $d[c] = 0$
* $d[cf] = c\,df$
* $d[f + g] = df + dg$
* $d[fg] = f\,dg + g\,df$
* $d\left[\frac{f}{g}\right] = \frac{g\,df - f\,dg}{g^2}$

---

### QUICK CHECK EXERCISES 2.9
*(See page 183 for answers.)*

1. The local linear approximation of $f$ at $x_0$ uses the $\underline{\hspace{1cm}}$ line to the graph of $y = f(x)$ at $x = x_0$ to approximate values of $\underline{\hspace{1cm}}$ for values of $x$ near $\underline{\hspace{1cm}}$.
2. Find an equation for the local linear approximation to $y = 5 - x^2$ at $x_0 = 2$.
3. Let $y = 5 - x^2$. Find $dy$ and $\Delta y$ at $x = 2$ with $dx = \Delta x = 0.1$.
4. Light intensity $I = f(x)$. If $x = 10\text{ m}, f(10) = 0.2\text{ W/m}^2, f'(10) = -0.04\text{ W/m}^3$, with measurement error $\pm 0.05\text{ m}$, estimate the percentage error in intensity.

#### QUICK CHECK ANSWERS 2.9
1. tangent; $f(x)$; $x_0$  
2. $y = 1 + (-4)(x - 2)$ or $y = -4x + 9$  
3. $dy = -0.4, \ \Delta y = -0.41$  
4. within $\pm 1\%$

---

### EXERCISE SET 2.9

1. (a) Linear approx of $x^3$ at $x_0 = 1$. (b) In terms of $\Delta x$. (c) Approximate $(1.02)^3$.
2. (a) Linear approx of $1/x$ at $x_0 = 2$. (b) In terms of $\Delta x$. (c) Approximate $1/2.05$.

**FOCUS ON CONCEPTS**

3. (a) Linear approx of $\sqrt{1 + x}$ at $x_0 = 0$; approximate $\sqrt{0.9}$ and $\sqrt{1.1}$. (b) Graphical illustration.
4. Why local linear approximations of square roots are always overestimates.

**5–10 Confirm the local linear approximation at $x_0 = 0$:**

5. $(1 + x)^{15} \approx 1 + 15x$
6. $\frac{1}{\sqrt{1 - x}} \approx 1 + \frac{1}{2}x$
7. $\tan x \approx x$
8. $\frac{1}{1 + x} \approx 1 - x$

**9–12 Confirm local linear approximation of $f$ at $x_0 = 1$ ($\Delta x = x - 1$):**

9. $f(x) = x^4; \ (1 + \Delta x)^4 \approx 1 + 4\Delta x$
10. $f(x) = \sqrt{x}; \ \sqrt{1 + \Delta x} \approx 1 + \frac{1}{2}\Delta x$
11. $f(x) = \frac{1}{2 + x}; \ \frac{1}{3 + \Delta x} \approx \frac{1}{3} - \frac{1}{9}\Delta x$
12. $f(x) = (4 + x)^3; \ (5 + \Delta x)^3 \approx 125 + 75\Delta x$

**13–16 Confirm local linear approximation at $x_0 = 0$ and estimate interval where error $\le \pm 0.1$:**

13. $\sqrt{x + 3} \approx \sqrt{3} + \frac{1}{2\sqrt{3}}x$
14. $\frac{1}{\sqrt{9 - x}} \approx \frac{1}{3} + \frac{1}{54}x$
15. $\tan 2x \approx 2x$
16. $\frac{1}{(1 + 2x)^5} \approx 1 - 10x$

17. (a) Approximate $\sin 1^\circ$ via $\sin x \approx x$. (b) Choice of $x_0$ for $\sin 44^\circ$. (c) Approximate $\sin 44^\circ$.
18. (a) Approximate $\tan 2^\circ$ via $\tan x \approx x$. (b) Choice of $x_0$ for $\tan 61^\circ$. (c) Approximate $\tan 61^\circ$.

**19–27 Use appropriate local linear approximation to estimate:**

19. $(3.02)^4$
20. $(1.97)^3$
21. $\sqrt{65}$
22. $\sqrt{24}$
23. $\sqrt{80.9}$
24. $\sqrt{36.03}$
25. $\sin 0.1$
26. $\tan 0.2$
27. $\cos 31^\circ$

**FOCUS ON CONCEPTS**

28. Binomial approximation $(1 + x)^k \approx 1 + kx$: (a) derive and estimate $(1.001)^{37}$ (b) compare (c) binomial theorem connection.
29. Use $(1 + x)^k \approx 1 + kx$ to show $\sqrt[3]{8.24} \approx 2.02$ and $(4.08)^{3/2} \approx 8.24$.
30. Building height $h = 500\tan 6^\circ \approx 52\text{ ft}$.
31. $y = 1/x$: find $dy, \Delta y$ at $x = 1$ with $dx = -0.5$.
32. $y = \sqrt{x}$: find $dy, \Delta y$ at $x = 9$ with $dx = -1$.

**33–36 Find formulas for $dy$ and $\Delta y$:**

33. $y = x^3$
34. $y = 8x - 4$
35. $y = x^2 - 2x + 1$
36. $y = \sin x$

**37–40 Find differential $dy$:**

37. (a) $y = 4x^3 - 7x^2$ (b) $y = x\cos x$
38. (a) $y = 1/x$ (b) $y = 5\tan x$
39. (a) $y = x\sqrt{1 - x}$ (b) $y = (1 + x)^{-17}$
40. (a) $y = \frac{1}{x^3 - 1}$ (b) $y = \frac{1 - x^3}{2 - x}$

**41–44 True–False Determine whether the statement is true or false. Explain your answer.**

41. A differential $dy$ is defined to be a very small change in $y$.
42. The error in approximation (2) is the same as the error in approximation (7).
43. A local linear approximation to a function can never be identically equal to the function.
44. A local linear approximation to a nonconstant function can never be constant.

**45–48 Use $dy$ to approximate $\Delta y$:**

45. $y = \sqrt{3x - 2}$; from $x = 2$ to $x = 2.03$
46. $y = \sqrt{x^2 + 8}$; from $x = 1$ to $x = 0.97$
47. $y = \frac{x}{x^2 + 1}$; from $x = 2$ to $x = 1.96$
48. $y = x\sqrt{8x + 1}$; from $x = 3$ to $x = 3.05$

49. Square side $10\text{ ft} \pm 0.1\text{ ft}$: (a) area error (b) percentage errors.
50. Cube side $25\text{ cm} \pm 1\text{ cm}$: (a) volume error (b) percentage errors.
51. Right triangle hypotenuse $10\text{ in}$, angle $30^\circ \pm 1^\circ$: errors in opposite and adjacent sides.
52. Right triangle side $25\text{ cm}$, angle $60^\circ \pm 0.5^\circ$: errors in adjacent side and hypotenuse.
53. Resistance $R = k/r^2$ with $r$ error $\pm 5\%$: percentage error in $R$.
54. $12\text{ ft}$ ladder: height change when $\theta$ changes from $60^\circ$ to $59^\circ$.
55. Triangle area $A = \frac{1}{4}H^2\sin 2\theta$ with $H = 4\text{ cm}, \theta = 30^\circ \pm 15'$.
56. Square side error $\pm 1\% \implies$ area percentage error $\pm 2\%$.
57. Cube side error $\pm 2\% \implies$ volume percentage error $\pm 6\%$.
58. Sphere radius error to ensure volume error within $\pm 3\%$.
59. Circle diameter error to ensure area error within $\pm 1\%$.
60. Steel cube ($1\text{ in}$) coated with $0.01\text{ in}$ copper: estimate volume of coating.
61. Metal rod ($L = 15\text{ cm}, d = 5\text{ cm}$) coated with $0.1\text{ cm}$ insulation: estimate volume.
62. Pendulum period $P = 2\pi\sqrt{L/g}$: show percentage error in $P$ is half percentage error in $L$.
63. Linear thermal expansion $\Delta L = \alpha L\Delta T$: (a) find $\alpha$ for rod from $20^\circ\text{C}$ to $30^\circ\text{C}$ (b) aluminum pole at $40^\circ\text{C}$.
64. Volume expansion $\Delta V = \beta V\Delta T$: ethyl alcohol tank truck delivery volume.
65. **Writing.** Local linear approximation equivalence to differentials.
66. **Writing.** Small angle approximation $\sin x \approx x$ applications.

---

## CHAPTER 2 REVIEW EXERCISES

1. Explain the difference between average and instantaneous rates of change, and discuss how they are calculated.
2. In parts (a)–(d), use the function $y = \frac{1}{2}x^2$:  
   (a) Find the average rate of change of $y$ with respect to $x$ over $[3, 4]$.  
   (b) Find the instantaneous rate of change at $x = 3$.  
   (c) Find the instantaneous rate of change at a general $x$-value.  
   (d) Sketch the graph of $y = \frac{1}{2}x^2$ together with secant and tangent lines.
3. Complete each part for $f(x) = x^2 + 1$:  
   (a) Slope of tangent line at general $x$.  
   (b) Slope of tangent line at $x = 2$.
4. A car travels a straight road $120\text{ mi}$ long. For first $100\text{ mi}$, average velocity is $50\text{ mi/h}$. Show that no matter how fast it travels the final $20\text{ mi}$, it cannot average $60\text{ mi/h}$ for the trip.
5. Average passing velocity $v_{\text{ave}} = \frac{3(h + 1)^{2.5} + 580h - 3}{10h}$. Estimate instantaneous velocity at $t = 1$.
6. Skydiver distance $s(t) = 976((0.835)^t - 1) + 176t$. Estimate instantaneous velocity at $t = 15$.
7. Particle motion $s = 3t^2 + t$: (a) average velocity over $[1, 3]$ (b) instantaneous velocity at $t = 1$.
8. State the definition of a derivative, and give two interpretations of it.
9. Use the definition of derivative to find $dy/dx$: (a) $y = \sqrt{9 - 4x}$ (b) $y = \frac{x}{x + 1}$.
10. For $f(x) = \begin{cases} x^2 - 1, & x \le 1 \\ k(x - 1), & x > 1 \end{cases}$, find $k$ for: (a) continuous (b) differentiable.
11. From graph of $y = f'(x)$ in Figure Ex-11: (a) horizontal tangents of $f$ (b) positive slope intervals (c) negative slope intervals (d) $g''(0)$ for $g(x) = f(x)\sin x$.
12. Sketch graph of $f$ with $f(0) = 1, f'(0) = 0, f'(x) > 0 \ (x < 0), f'(x) < 0 \ (x > 0)$.
13. World population $N(t)$: (a) estimate $dN/dt$ at $t = 2000$ (b) instantaneous growth rate $\frac{dN/dt}{N}$.
14. Graph $f(x) = |x^4 - x - 1| - x$ and estimate where derivative does not exist.

**15–18 [CAS] (a) Use CAS to find $f'(x)$ via Definition 2.2.1; (b) check by hand; (c) find $f''(x)$.**

15. $f(x) = x^2\sin x$
16. $f(x) = \sqrt{x} + \cos^2 x$
17. $f(x) = \frac{2x^2 - x + 5}{3x + 2}$
18. $f(x) = \frac{\tan x}{1 + x^2}$

19. Draining tank $W = 100(t - 15)^2\text{ gal}$: (a) drainage rate at $t = 5\text{ min}$ (b) average rate during first $5\text{ min}$.
20. Cube volume $V = l^3$: (a) average rate as $l$ increases from 2 to 4 (b) instantaneous rate at $l = 5$.
21–22. Zooming in on graph of $f$ at $x_0$ to estimate slope and check with exact derivative.
23. Differentiable $f$ at $x = 1$ with $\lim_{h \to 0} \frac{f(1 + h)}{h} = 5$: find $f(1)$ and $f'(1)$.
24. Differentiable $f$ at $x = 2$ with $\lim_{x \to 2} \frac{x^3f(x) - 24}{x - 2} = 28$: find $f(2)$ and $f'(2)$.
25. Find equations of all lines through the origin tangent to $y = x^3 - 9x^2 - 16x$.
26. Values of $x$ where tangent to $y = 2x^3 - x^2$ is perpendicular to $x + 4y = 10$.
27. For $f(x) = x^2$, show that tangent slope at $x = \frac{1}{2}(a + b)$ equals secant slope through $(a, a^2)$ and $(b, b^2)$.
28. Given $f(1) = 1, g(1) = -2, f'(1) = 3, g'(1) = -1$, evaluate derivatives of $f(x)g(x), f(x)/g(x), \sqrt{f(x)}, f(1)g'(1)$.

**29–32 Find $f'(x)$.**

29. (a) $f(x) = x^8 - 3\sqrt{x} + 5x^{-3}$ (b) $f(x) = (2x + 1)^{101}(5x^2 - 7)$
30. (a) $f(x) = \sin x + 2\cos^3 x$ (b) $f(x) = (1 + \sec x)(x^2 - \tan x)$
31. (a) $f(x) = \sqrt{3x + 1}(x - 1)^2$ (b) $f(x) = \left(\frac{3x + 1}{x^2}\right)^3$
32. (a) $f(x) = \cot\left(\frac{\csc 2x}{x^3 + 5}\right)$ (b) $f(x) = \frac{1}{2x + \sin^3 x}$

**33–34 Find values of $x$ with horizontal tangent lines:**

33. $f(x) = (2x + 7)^6(x - 2)^5$
34. $f(x) = \frac{(x - 3)^4}{x^2 + 2x}$

35. Common tangent lines to $y = x^2 + 1$ and $y = -x^2 - 1$.
36. Generalization of Exercise 35 to $y = x^n + n - 1$ and $y = -x^n - n + 1$ for even/odd $n$.
37. Points where tangent to $y = 3x - \tan x$ is parallel to $y - x = 2$.
38. Approximate $x$ where tangent to $y = x^3 - \sin x$ is horizontal.
39. Tangent line to $y = M\sin x + N\cos x$ at $x = 3\pi/4$.
40. Tangent line to $y = M\tan x + N\sec x$ at $x = 0$.
41. Given $f'(x) = 2xf(x)$ and $f(2) = 5$: (a) $g'(\pi/3)$ for $g(x) = f(\sec x)$ (b) $h'(2)$ for $h(x) = [f(x)/(x - 1)]^4$.

**42–44 Find $dy/dx$.**

42. $y = \sqrt[4]{6x - 5}$
43. $y = \sqrt[3]{x^2 + x}$
44. $y = \frac{(3 - 2x)^{4/3}}{x^2}$

**45–46 Differentiate implicitly and explicitly and compare.**

45. $x^3 + xy - 2x = 1$
46. $xy = x - y$

**47–50 Implicit differentiation for $dy/dx$.**

47. $\frac{1}{y} + \frac{1}{x} = 1$
48. $x^3 - y^3 = 6xy$
49. $\sec(xy) = y$
50. $x^2 = \frac{\cot y}{1 + \csc y}$

**51–52 Implicit differentiation for $d^2y/dx^2$.**

51. $3x^2 - 4y^2 = 7$
52. $2xy - y^2 = 3$

53. Slope of quadratrix of Hippias $y = x\tan(\pi y/2)$ at $(1/2, 1/2)$.
54. Points on $y^2 = 2x^3$ perpendicular to $4x - 3y + 1 = 0$.
55. Collinear points on rotated ellipse $x^2 + xy + y^2 = 4$ have parallel tangents.
56–57. Horizontal and vertical tangent points on $x^3 - xy + y^3 = 0$.
58. Tangent line equation to parabola $y^2 = kx$ at $(x_0, y_0)$ is $y_0y = \frac{1}{2}k(x + x_0)$.
59. Circular oil boom pulled at $5\text{ m/min}$: area shrinking rate when diameter is $100\text{ m}$.
60. Right triangle with growing hypotenuse ($a\text{ cm/s}$) and shrinking leg ($b\text{ cm/s}$): acute angle rate of change.
61. Find $\Delta x, \Delta y, dy$ for given changes.
62. Local linear approximation for $\cot 46^\circ$.
63. Great Pyramid of Giza ($230\text{ m}$ square base, angle $\phi = 51^\circ \pm 0.5^\circ$): height and allowable error.

---

## CHAPTER 2 MAKING CONNECTIONS

1. Suppose that $f$ is a function with properties: (i) $f$ is differentiable everywhere, (ii) $f(x + y) = f(x)f(y)$, (iii) $f(0) \neq 0$, and (iv) $f'(0) = 1$.  
   (a) Show that $f(0) = 1$. [Hint: Consider $f(0 + 0)$.]  
   (b) Show that $f(x) > 0$ for all $x$. [Hint: First show $f(x) \neq 0$ for any $x$ by considering $f(x - x)$.]  
   (c) Use the definition of derivative to show that $f'(x) = f(x)$ for all $x$.
2. Suppose that $f$ and $g$ have properties (i)–(iv) in Exercise 1:  
   (a) Show $y = f(2x)$ satisfies $y' = 2y$ in two ways: using property (ii), and via chain rule.  
   (b) Show $y = f(kx)$ satisfies $y' = ky$.  
   (c) Find $k$ such that $y = f(x)g(x)$ satisfies $y' = ky$.  
   (d) If $h = f/g$, find $h'(x)$ and conjecture relationship between $f$ and $g$.
3. (a) Apply the product rule twice to show $(f \cdot g \cdot h)' = f'gh + fg'h + fgh'$.  
   (b) Derive formula for $(f \cdot g \cdot h \cdot k)'$.  
   (c) Conjecture formula for product of $n$ functions and prove by mathematical induction.
4. (a) Apply the quotient rule twice to show $[(f/g)/h]' = \frac{f'gh - fg'h - fgh'}{g^2h^2}$.  
   (b) Derive by first simplifying $(f/g)/h$.  
   (c) Apply quotient rule twice to derive $[f/(g/h)]'$.  
   (d) Derive by first simplifying $f/(g/h)$.
5. Derive the quotient rule for $h(x) = f(x)/g(x)$ in two ways:  
   (a) Write $h(x) = f(x)[g(x)]^{-1}$ and use product and chain rules.  
   (b) Write $f(x) = h(x)g(x)$ and use product rule to solve for $h'(x)$.
