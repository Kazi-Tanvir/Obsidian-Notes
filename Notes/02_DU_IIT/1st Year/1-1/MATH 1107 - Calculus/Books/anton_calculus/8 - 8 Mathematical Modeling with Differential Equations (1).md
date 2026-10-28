# CHAPTER 8: MATHEMATICAL MODELING WITH DIFFERENTIAL EQUATIONS

> In the 1920s, excavation of an archeological site in Folsom, New Mexico, uncovered a collection of prehistoric stone spearheads now known as "Folsom points." In 1950, carbon dating of charred bison bones found nearby confirmed that human hunters lived in the area between 9000 B.C. and 8000 B.C. We will study carbon dating in this chapter.

Many fundamental laws of science and engineering can be expressed in terms of differential equations. We introduced the concept of a differential equation in Section 4.5, but in this chapter we will go into more detail. We will discuss some important mathematical models that involve differential equations, and we will discuss some methods for solving and approximating solutions of some of the basic types of differential equations. However, we will only be able to touch the surface of this topic, leaving many important topics in differential equations to courses that are devoted completely to the subject.

---

## 8.1 MODELING WITH DIFFERENTIAL EQUATIONS

In this section we will introduce some basic terminology and concepts concerning differential equations. We will also discuss the general idea of modeling with differential equations, and we will encounter important models that can be applied to demography, medicine, ecology, and physics. In later sections of this chapter we will investigate methods that may be used to solve these differential equations.

### TERMINOLOGY

Recall from Section 4.5 that a **differential equation** is an equation involving one or more derivatives of an unknown function. In this section we will denote the unknown function by $y = y(x)$ unless the differential equation arises from an applied problem involving time, in which case we will denote it by $y = y(t)$. The **order** of a differential equation is the order of the highest derivative that it contains. Some examples are given in Table 8.1.1. The last two equations in that table are expressed in "prime" notation, which does not specify the independent variable explicitly. However, you will usually be able to tell from the equation itself or from the context in which it arises whether to interpret $y'$ as $dy/dx$ or $dy/dt$.

#### Table 8.1.1
| DIFFERENTIAL EQUATION | ORDER |
| :--- | :---: |
| $\frac{dy}{dx} = 3y$ | 1 |
| $\frac{d^2y}{dx^2} - 6\frac{dy}{dx} + 8y = 0$ | 2 |
| $\frac{d^3y}{dt^3} - t\frac{dy}{dt} + (t^2 - 1)y = e^t$ | 3 |
| $y' - y = e^{2x}$ | 1 |
| $y'' + y' = \cos t$ | 2 |

### SOLUTIONS OF DIFFERENTIAL EQUATIONS

A function $y = y(x)$ is a **solution** of a differential equation on an open interval if the equation is satisfied identically on the interval when $y$ and its derivatives are substituted into the equation. For example, $y = e^{2x}$ is a solution of the differential equation
$$\frac{dy}{dx} - y = e^{2x} \tag{1}$$
on the interval $(-\infty, +\infty)$, since substituting $y$ and its derivative into the left side of this equation yields
$$\frac{dy}{dx} - y = \frac{d}{dx}[e^{2x}] - e^{2x} = 2e^{2x} - e^{2x} = e^{2x}$$
for all real values of $x$. However, this is not the only solution on $(-\infty, +\infty)$; for example, the function
$$y = e^{2x} + Ce^x \tag{2}$$
is also a solution for every real value of the constant $C$, since
$$\frac{dy}{dx} - y = \frac{d}{dx}[e^{2x} + Ce^x] - (e^{2x} + Ce^x) = (2e^{2x} + Ce^x) - (e^{2x} + Ce^x) = e^{2x}$$

After developing some techniques for solving equations such as (1), we will be able to show that *all* solutions of (1) on $(-\infty, +\infty)$ can be obtained by substituting values for the constant $C$ in (2). On a given interval, a solution of a differential equation from which all solutions on that interval can be derived by substituting values for arbitrary constants is called a **general solution** of the equation on the interval. Thus (2) is a general solution of (1) on the interval $(-\infty, +\infty)$.

> The first-order equation (1) has a single arbitrary constant in its general solution (2). Usually, the general solution of an $n\text{th}$-order differential equation will contain $n$ arbitrary constants. This is plausible, since $n$ integrations are needed to recover a function from its $n\text{th}$ derivative.

The graph of a solution of a differential equation is called an **integral curve** for the equation, so the general solution of a differential equation produces a family of integral curves corresponding to the different possible choices for the arbitrary constants. For example, Figure 8.1.1 shows some integral curves for (1), which were obtained by assigning values to the arbitrary constant in (2).

### INITIAL-VALUE PROBLEMS

When an applied problem leads to a differential equation, there are usually conditions in the problem that determine specific values for the arbitrary constants. As a rule of thumb, it requires $n$ conditions to determine values for all $n$ arbitrary constants in the general solution of an $n\text{th}$-order differential equation (one condition for each constant). For a first-order equation, the single arbitrary constant can be determined by specifying the value of the unknown function $y(x)$ at an arbitrary $x$-value $x_0$, say $y(x_0) = y_0$. This is called an **initial condition**, and the problem of solving a first-order equation subject to an initial condition is called a **first-order initial-value problem**. Geometrically, the initial condition $y(x_0) = y_0$ has the effect of isolating the integral curve that passes through the point $(x_0, y_0)$ from the complete family of integral curves.

#### Example 1
The solution of the initial-value problem
$$\frac{dy}{dx} - y = e^{2x}, \quad y(0) = 3$$
can be obtained by substituting the initial condition $x = 0, y = 3$ in the general solution (2) to find $C$. We obtain
$$3 = e^0 + Ce^0 = 1 + C$$
Thus, $C = 2$, and the solution of the initial-value problem, which is obtained by substituting this value of $C$ in (2), is
$$y = e^{2x} + 2e^x$$
Geometrically, this solution is realized as the integral curve in Figure 8.1.1 that passes through the point $(0, 3)$.

Since many important principles in the physical and social sciences involve rates of change, it should not be surprising that such principles can often be modeled by differential equations. Here are some examples of the modeling process.

### UNINHIBITED POPULATION GROWTH

One of the simplest models of population growth is based on the observation that when populations (people, plants, bacteria, and fruit flies, for example) are not constrained by environmental limitations, they tend to grow at a rate that is proportional to the size of the population—the larger the population, the more rapidly it grows.

To translate this principle into a mathematical model, suppose that $y = y(t)$ denotes the population at time $t$. At each point in time, the rate of increase of the population with respect to time is $dy/dt$, so the assumption that the rate of growth is proportional to the population is described by the differential equation
$$\frac{dy}{dt} = ky \tag{3}$$
where $k$ is a positive constant of proportionality that can usually be determined experimentally. Thus, if the population is known at some point in time, say $y = y_0$ at time $t = 0$, then a formula for the population $y(t)$ can be obtained by solving the initial-value problem
$$\frac{dy}{dt} = ky, \quad y(0) = y_0$$

### INHIBITED POPULATION GROWTH; LOGISTIC MODELS

The uninhibited population growth model was predicated on the assumption that the population $y = y(t)$ was not constrained by the environment. While this assumption is reasonable as long as the size of the population is relatively small, environmental effects become increasingly important as the population grows. In general, populations grow within ecological systems that can only support a certain number of individuals; the number $L$ of such individuals is called the **carrying capacity** of the system. When $y > L$, the population exceeds the capacity of the ecological system and tends to decrease toward $L$; when $y < L$, the population is below the capacity of the ecological system and tends to increase toward $L$; when $y = L$, the population is in balance with the capacity of the ecological system and tends to remain stable.

To translate this into a mathematical model, we must look for a differential equation in which $y > 0$, $L > 0$, and
$$\frac{dy}{dt} < 0 \text{ if } \frac{y}{L} > 1, \quad \frac{dy}{dt} > 0 \text{ if } \frac{y}{L} < 1, \quad \frac{dy}{dt} = 0 \text{ if } \frac{y}{L} = 1$$

Moreover, when the population is far below the carrying capacity (i.e., $y/L \approx 0$), then the environmental constraints should have little effect, and the growth rate should behave like the uninhibited population model. Thus, we want
$$\frac{dy}{dt} \approx ky \text{ if } \frac{y}{L} \approx 0$$
A simple differential equation that meets all of these requirements is
$$\frac{dy}{dt} = k\left(1 - \frac{y}{L}\right)y$$
where $k$ is a positive constant of proportionality. Thus if $k$ and $L$ can be determined experimentally, and if the population is known at some point, say $y(0) = y_0$, then a formula for the population $y(t)$ can be determined by solving the initial-value problem
$$\frac{dy}{dt} = k\left(1 - \frac{y}{L}\right)y, \quad y(0) = y_0 \tag{4}$$

This theory of population growth is due to the Belgian mathematician P. F. Verhulst (1804–1849), who introduced it in 1838 and described it as "logistic growth."* Thus, the differential equation in (4) is called the **logistic differential equation**, and the growth model described by (4) is called the **logistic model**.

> \* Verhulst's model fell into obscurity for nearly a hundred years because he did not have sufficient census data to test its validity. However, interest in the model was revived during the 1930s when biologists used it successfully to describe the growth of fruit fly and flour beetle populations. Verhulst himself used the model to predict that an upper limit of Belgium's population would be approximately 9,400,000. In 2006 the population was about 10,379,000.

### PHARMACOLOGY

When a drug (say, penicillin or aspirin) is administered to an individual, it enters the bloodstream and then is absorbed by the body over time. Medical research has shown that the amount of a drug that is present in the bloodstream tends to decrease at a rate that is proportional to the amount of the drug present—the more of the drug that is present in the bloodstream, the more rapidly it is absorbed by the body.

To translate this principle into a mathematical model, suppose that $y = y(t)$ is the amount of the drug present in the bloodstream at time $t$. At each point in time, the rate of change in $y$ with respect to $t$ is $dy/dt$, so the assumption that the rate of decrease is proportional to the amount $y$ in the bloodstream translates into the differential equation
$$\frac{dy}{dt} = -ky \tag{5}$$
where $k$ is a positive constant of proportionality that depends on the drug and can be determined experimentally. The negative sign is required because $y$ decreases with time. Thus, if the initial dosage of the drug is known, say $y = y_0$ at time $t = 0$, then a formula for $y(t)$ can be obtained by solving the initial-value problem
$$\frac{dy}{dt} = -ky, \quad y(0) = y_0$$

### SPREAD OF DISEASE

Suppose that a disease begins to spread in a population of $L$ individuals. Logic suggests that at each point in time the rate at which the disease spreads will depend on how many individuals are already affected and how many are not—as more individuals are affected, the opportunity to spread the disease tends to increase, but at the same time there are fewer individuals who are not affected, so the opportunity to spread the disease tends to decrease. Thus, there are two conflicting influences on the rate at which the disease spreads.

To translate this into a mathematical model, suppose that $y = y(t)$ is the number of individuals who have the disease at time $t$, so of necessity the number of individuals who do not have the disease at time $t$ is $L - y$. As the value of $y$ increases, the value of $L - y$ decreases, so the conflicting influences of the two factors on the rate of spread $dy/dt$ are taken into account by the differential equation
$$\frac{dy}{dt} = ky(L - y)$$
where $k$ is a positive constant of proportionality that depends on the nature of the disease and the behavior patterns of the individuals and can be determined experimentally. Thus, if the number of affected individuals is known at some point in time, say $y = y_0$ at time $t = 0$, then a formula for $y(t)$ can be obtained by solving the initial-value problem
$$\frac{dy}{dt} = ky(L - y), \quad y(0) = y_0 \tag{6}$$

> *Note:* Show that the model for the spread of disease can be viewed as a logistic model with constant of proportionality $kL$ by rewriting (6) appropriately.

### NEWTON'S LAW OF COOLING

If a hot object is placed into a cool environment, the object will cool at a rate proportional to the difference in temperature between the object and the environment. Similarly, if a cold object is placed into a warm environment, the object will warm at a rate that is again proportional to the difference in temperature between the object and the environment. Together, these observations comprise a result known as **Newton's Law of Cooling**. (Newton's Law of Cooling appeared previously in the exercises of Section 2.2 and was mentioned briefly in Section 4.8.) To translate this into a mathematical model, suppose that $T = T(t)$ is the temperature of the object at time $t$ and that $T_e$ is the temperature of the environment, which is assumed to be constant. Since the rate of change $dT/dt$ is proportional to $T - T_e$, we have
$$\frac{dT}{dt} = k(T - T_e)$$
where $k$ is a constant of proportionality. Moreover, since $dT/dt$ is positive when $T < T_e$, and is negative when $T > T_e$, the sign of $k$ must be negative. Thus if the temperature of the object is known at some time, say $T = T_0$ at time $t = 0$, then a formula for the temperature $T(t)$ can be obtained by solving the initial-value problem
$$\frac{dT}{dt} = k(T - T_e), \quad T(0) = T_0 \tag{7}$$

### VIBRATIONS OF SPRINGS

We conclude this section with an engineering model that leads to a second-order differential equation.

As shown in Figure 8.1.2, consider a block of mass $m$ attached to the end of a horizontal spring. Assume that the block is then set into vibratory motion by pulling the spring beyond its natural position and releasing it at time $t = 0$. We will be interested in finding a mathematical model that describes the vibratory motion of the block over time.

To translate this problem into mathematical form, we introduce a horizontal $x$-axis whose positive direction is to the right and whose origin is at the right end of the spring when the spring is in its natural position (Figure 8.1.3). Our goal is to find a model for the coordinate $x = x(t)$ of the point of attachment of the block to the spring as a function of time. In developing this model, we will assume that the only force on the mass $m$ is the restoring force of the spring, and we will ignore the influence of other forces such as friction, air resistance, and so forth. Recall from Hooke's Law (Section 5.6) that when the connection point has coordinate $x(t)$, the restoring force is $-kx(t)$, where $k$ is the spring constant. [The negative sign is due to the fact that the restoring force is to the left when $x(t)$ is positive, and the restoring force is to the right when $x(t)$ is negative.] It follows from Newton's Second Law of Motion [Equation (5) of Section 5.6] that this restoring force is equal to the product of the mass $m$ and the acceleration $d^2x/dt^2$ of the mass. In other words, we have
$$m\frac{d^2x}{dt^2} = -kx$$
which is a second-order differential equation for $x$. If at time $t = 0$ the mass is released from rest at position $x(0) = x_0$, then a formula for $x(t)$ can be found by solving the initial-value problem
$$m\frac{d^2x}{dt^2} = -kx, \quad x(0) = x_0, \quad x'(0) = 0 \tag{8}$$
[If at time $t = 0$ the mass is given an initial velocity $v_0 \neq 0$, then the condition $x'(0) = 0$ must be replaced by $x'(0) = v_0$.]

---

### QUICK CHECK EXERCISES 8.1
*(See page 568 for answers.)*

1. Match each differential equation with its family of solutions.
   - (a) $x \frac{dy}{dx} = y$ — (i) $y = x^2 + C$
   - (b) $y'' = 4y$ — (ii) $y = C_1\sin 2x + C_2\cos 2x$
   - (c) $\frac{dy}{dx} = 2x$ — (iii) $y = C_1 e^{2x} + C_2 e^{-2x}$
   - (d) $\frac{d^2y}{dx^2} = -4y$ — (iv) $y = Cx$
2. If $y = C_1 e^{2x} + C_2 x e^{2x}$ is the general solution of a differential equation, then the order of the equation is \_\_\_\_, and a solution to the differential equation that satisfies the initial conditions $y(0) = 1, y'(0) = 4$ is given by $y =$ \_\_\_\_.
3. The graph of a differentiable function $y = y(x)$ passes through the point $(0, 1)$ and at every point $P(x, y)$ on the graph the tangent line is perpendicular to the line through $P$ and the origin. Find an initial-value problem whose solution is $y(x)$.
4. A glass of ice water with a temperature of $36^\circ\text{F}$ is placed in a room with a constant temperature of $68^\circ\text{F}$. Assuming that Newton's Law of Cooling applies, find an initial-value problem whose solution is the temperature of water $t$ minutes after it is placed in the room. [*Note:* The differential equation will involve a constant of proportionality.]

---

### EXERCISE SET 8.1

1. Confirm that $y = 3e^{x^3}$ is a solution of the initial-value problem $y' = 3x^2 y, \; y(0) = 3$.
2. Confirm that $y = \frac{1}{4}x^4 + 2\cos x + 1$ is a solution of the initial-value problem $y' = x^3 - 2\sin x, \; y(0) = 3$.

**3–4 State the order of the differential equation, and confirm that the functions in the given family are solutions.**
3. (a) $(1+x)\frac{dy}{dx} = y; \quad y = c(1+x)$  
   (b) $y'' + y = 0; \quad y = c_1\sin t + c_2\cos t$
4. (a) $2\frac{dy}{dx} + y = x - 1; \quad y = ce^{-x/2} + x - 3$  
   (b) $y'' - y = 0; \quad y = c_1 e^t + c_2 e^{-t}$

**5–8 True–False Determine whether the statement is true or false. Explain your answer.**
5. The equation
   $$\left(\frac{dy}{dx}\right)^2 = \frac{dy}{dx} + 2y$$
   is an example of a second-order differential equation.
6. The differential equation
   $$\frac{dy}{dx} = 2y + 1$$
   has a solution that is constant.
7. We expect the general solution of the differential equation
   $$\frac{d^3y}{dx^3} + 3\frac{d^2y}{dx^2} - \frac{dy}{dx} + 4y = 0$$
   to involve three arbitrary constants.
8. If every solution to a differential equation can be expressed in the form $y = Ae^{x+b}$ for some choice of constants $A$ and $b$, then the differential equation must be of second order.

**9–14 In each part, verify that the functions are solutions of the differential equation by substituting the functions into the equation.**
9. $y'' + y' - 2y = 0$  
   (a) $e^{-2x}$ and $e^x$  
   (b) $c_1 e^{-2x} + c_2 e^x$ ($c_1, c_2$ constants)
10. $y'' - y' - 6y = 0$  
    (a) $e^{-2x}$ and $e^{3x}$  
    (b) $c_1 e^{-2x} + c_2 e^{3x}$ ($c_1, c_2$ constants)
11. $y'' - 4y' + 4y = 0$  
    (a) $e^{2x}$ and $xe^{2x}$  
    (b) $c_1 e^{2x} + c_2 xe^{2x}$ ($c_1, c_2$ constants)
12. $y'' - 8y' + 16y = 0$  
    (a) $e^{4x}$ and $xe^{4x}$  
    (b) $c_1 e^{4x} + c_2 xe^{4x}$ ($c_1, c_2$ constants)
13. $y'' + 4y = 0$  
    (a) $\sin 2x$ and $\cos 2x$  
    (b) $c_1\sin 2x + c_2\cos 2x$ ($c_1, c_2$ constants)
14. $y'' + 4y' + 13y = 0$  
    (a) $e^{-2x}\sin 3x$ and $e^{-2x}\cos 3x$  
    (b) $e^{-2x}(c_1\sin 3x + c_2\cos 3x)$ ($c_1, c_2$ constants)

**15–20 Use the results of Exercises 9–14 to find a solution to the initial-value problem.**
15. $y'' + y' - 2y = 0, \quad y(0) = -1, \quad y'(0) = -4$
16. $y'' - y' - 6y = 0, \quad y(0) = 1, \quad y'(0) = 8$
17. $y'' - 4y' + 4y = 0, \quad y(0) = 2, \quad y'(0) = 2$
18. $y'' - 8y' + 16y = 0, \quad y(0) = 1, \quad y'(0) = 1$
19. $y'' + 4y = 0, \quad y(0) = 1, \quad y'(0) = 2$
20. $y'' + 4y' + 13y = 0, \quad y(0) = -1, \quad y'(0) = -1$

**21–26 Find a solution to the initial-value problem.**
21. $y' + 4x = 2, \quad y(0) = 3$
22. $y'' + 6x = 0, \quad y(0) = 1, \quad y'(0) = 2$
23. $y' - y^2 = 0, \quad y(1) = 2$ [*Hint:* Assume the solution has an inverse function $x = x(y)$. Find, and solve, a differential equation that involves $x'(y)$.]
24. $y' = 1 + y^2, \quad y(0) = 0$ (See Exercise 23.)
25. $x^2 y' + 2xy = 0, \quad y(1) = 2$ [*Hint:* Interpret the left-hand side of the equation as the derivative of a product of two functions.]
26. $xy' + y = e^x, \quad y(1) = 1 + e$ (See Exercise 25.)

#### FOCUS ON CONCEPTS
27. (a) Suppose that a quantity $y = y(t)$ increases at a rate that is proportional to the square of the amount present, and suppose that at time $t = 0$, the amount present is $y_0$. Find an initial-value problem whose solution is $y(t)$.  
    (b) Suppose that a quantity $y = y(t)$ decreases at a rate that is proportional to the square of the amount present, and suppose that at time $t = 0$, the amount present is $y_0$. Find an initial-value problem whose solution is $y(t)$.
28. (a) Suppose that a quantity $y = y(t)$ changes in such a way that $dy/dt = k\sqrt{y}$, where $k > 0$. Describe how $y$ changes in words.  
    (b) Suppose that a quantity $y = y(t)$ changes in such a way that $dy/dt = -ky^3$, where $k > 0$. Describe how $y$ changes in words.
29. (a) Suppose that a particle moves along an $s$-axis in such a way that its velocity $v(t)$ is always half of $s(t)$. Find a differential equation whose solution is $s(t)$.  
    (b) Suppose that an object moves along an $s$-axis in such a way that its acceleration $a(t)$ is always twice the velocity. Find a differential equation whose solution is $s(t)$.
30. Suppose that a body moves along an $s$-axis through a resistive medium in such a way that the velocity $v = v(t)$ decreases at a rate that is twice the square of the velocity.  
    (a) Find a differential equation whose solution is the velocity $v(t)$.  
    (b) Find a differential equation whose solution is the position $s(t)$.
31. Consider a solution $y = y(t)$ to the uninhibited population growth model.  
    (a) Use Equation (3) to explain why $y$ will be an increasing function of $t$.  
    (b) Use Equation (3) to explain why the graph $y = y(t)$ will be concave up.
32. Consider the logistic model for population growth.  
    (a) Explain why there are two constant solutions to this model.  
    (b) For what size of the population will the population be growing most rapidly?
33. Consider the model for the spread of disease.  
    (a) Explain why there are two constant solutions to this model.  
    (b) For what size of the infected population is the disease spreading most rapidly?
34. Explain why there is exactly one constant solution to the Newton's Law of Cooling model.
35. Show that if $c_1$ and $c_2$ are any constants, the function
    $$x = x(t) = c_1\cos\left(\sqrt{\frac{k}{m}}t\right) + c_2\sin\left(\sqrt{\frac{k}{m}}t\right)$$
    is a solution to the differential equation for the vibrating spring. (The corresponding motion of the spring is referred to as **simple harmonic motion**.)
36. (a) Use the result of Exercise 35 to solve the initial-value problem in (8).  
    (b) Find the amplitude, period, and frequency of your answer to part (a), and interpret each of these in terms of the motion of the spring.
37. **Writing.** Select one of the models in this section and write a paragraph that discusses conditions under which the model would not be appropriate. How might you modify the model to take those conditions into account?

---

### QUICK CHECK ANSWERS 8.1
1. (a) (iv) (b) (iii) (c) (i) (d) (ii)  
2. $2; \quad e^{2x} + 2xe^{2x}$  
3. $\frac{dy}{dx} = -\frac{x}{y}, \quad y(0) = 1$  
4. $\frac{dT}{dt} = k(T - 68), \quad T(0) = 36$

---

## 8.2 SEPARATION OF VARIABLES

In this section we will discuss a method, called "separation of variables," that can be used to solve a large class of first-order differential equations of a particular form. We will use this method to investigate mathematical models for exponential growth and decay, including population models and carbon dating.

### FIRST-ORDER SEPARABLE EQUATIONS

We will now consider a method of solution that can often be applied to first-order equations that are expressible in the form
$$h(y)\frac{dy}{dx} = g(x) \tag{1}$$
Such first-order equations are said to be **separable**. Some examples of separable equations are given in Table 8.2.1. The name "separable" arises from the fact that Equation (1) can be rewritten in the differential form
$$h(y)\,dy = g(x)\,dx \tag{2}$$
in which the expressions involving $x$ and $y$ appear on opposite sides. The process of rewriting (1) in form (2) is called **separating variables**.

> Some writers define a separable equation to be one that can be written in the form $dy/dx = G(x)H(y)$. Explain why this is equivalent to our definition.

#### Table 8.2.1
| EQUATION | FORM (1) | $h(y)$ | $g(x)$ |
| :--- | :--- | :---: | :---: |
| $\frac{dy}{dx} = \frac{x}{y}$ | $y\frac{dy}{dx} = x$ | $y$ | $x$ |
| $\frac{dy}{dx} = x^2 y^3$ | $\frac{1}{y^3}\frac{dy}{dx} = x^2$ | $\frac{1}{y^3}$ | $x^2$ |
| $\frac{dy}{dx} = y$ | $\frac{1}{y}\frac{dy}{dx} = 1$ | $\frac{1}{y}$ | $1$ |
| $\frac{dy}{dx} = y - \frac{y}{x}$ | $\frac{1}{y}\frac{dy}{dx} = 1 - \frac{1}{x}$ | $\frac{1}{y}$ | $1 - \frac{1}{x}$ |

To motivate a method for solving separable equations, assume that $h(y)$ and $g(x)$ are continuous functions of their respective variables, and let $H(y)$ and $G(x)$ denote antiderivatives of $h(y)$ and $g(x)$, respectively. Consider the equation that results if we integrate both sides of (2), the left side with respect to $y$ and the right side with respect to $x$. We then have
$$\int h(y)\,dy = \int g(x)\,dx \tag{3}$$
or, equivalently,
$$H(y) = G(x) + C \tag{4}$$
where $C$ denotes a constant. We claim that a differentiable function $y = y(x)$ is a solution to (1) if and only if $y$ satisfies Equation (4) for some choice of the constant $C$.

Suppose that $y = y(x)$ is a solution to (1). It then follows from the chain rule that
$$\frac{d}{dx}[H(y)] = \frac{dH}{dy}\frac{dy}{dx} = h(y)\frac{dy}{dx} = g(x) = \frac{dG}{dx} \tag{5}$$
Since the functions $H(y)$ and $G(x)$ have the same derivative with respect to $x$, they must differ by a constant (Theorem 3.8.3). It then follows that $y$ satisfies (4) for an appropriate choice of $C$. Conversely, if $y = y(x)$ is defined implicitly by Equation (4), then implicit differentiation shows that (5) is satisfied, and thus $y(x)$ is a solution to (1) (Exercise 67). Because of this, it is common practice to refer to Equation (4) as the "solution" to (1).

In summary, we have the following procedure for solving (1), called **separation of variables**:

> ### Separation of Variables
> **Step 1.** Separate the variables in (1) by rewriting the equation in the differential form
> $$h(y)\,dy = g(x)\,dx$$
> **Step 2.** Integrate both sides of the equation in Step 1 (the left side with respect to $y$ and the right side with respect to $x$):
> $$\int h(y)\,dy = \int g(x)\,dx$$
> **Step 3.** If $H(y)$ is any antiderivative of $h(y)$ and $G(x)$ is any antiderivative of $g(x)$, then the equation
> $$H(y) = G(x) + C$$
> will generally define a family of solutions implicitly. In some cases it may be possible to solve this equation explicitly for $y$.

#### Example 1
Solve the differential equation
$$\frac{dy}{dx} = -4xy^2$$
and then solve the initial-value problem
$$\frac{dy}{dx} = -4xy^2, \quad y(0) = 1$$

> *Note:* For an initial-value problem in which the differential equation is separable, you can either use the initial condition to solve for $C$, as in Example 1, or replace the indefinite integrals in Step 2 by definite integrals (Exercise 68).

*Solution.* For $y \neq 0$ we can write the differential equation in form (1) as
$$\frac{1}{y^2}\frac{dy}{dx} = -4x$$
Separating variables and integrating yields
$$\frac{1}{y^2}\,dy = -4x\,dx$$
$$\int \frac{1}{y^2}\,dy = \int -4x\,dx$$
or
$$-\frac{1}{y} = -2x^2 + C$$
Solving for $y$ as a function of $x$, we obtain
$$y = \frac{1}{2x^2 - C}$$
The initial condition $y(0) = 1$ requires that $y = 1$ when $x = 0$. Substituting these values into our solution yields $C = -1$ (verify). Thus, a solution to the initial-value problem is
$$y = \frac{1}{2x^2 + 1} \tag{6}$$
Some integral curves and our solution of the initial-value problem are graphed in Figure 8.2.1.

One aspect of our solution to Example 1 deserves special comment. Had the initial condition been $y(0) = 0$ instead of $y(0) = 1$, the method we used would have failed to yield a solution to the resulting initial-value problem (Exercise 25). This is due to the fact that we assumed $y \neq 0$ in order to rewrite the equation $dy/dx = -4xy^2$ in the form
$$\frac{1}{y^2}\frac{dy}{dx} = -4x$$
It is important to be aware of such assumptions when manipulating a differential equation algebraically.

#### Example 2
Solve the initial-value problem
$$(4y - \cos y)\frac{dy}{dx} - 3x^2 = 0, \quad y(0) = 0$$

> The solution of an initial-value problem in $x$ and $y$ can sometimes be expressed explicitly as a function of $x$ [as in Formula (6) of Example 1], or explicitly as a function of $y$ [as in Formula (8) of Example 2]. However, sometimes the solution cannot be expressed in either such form, so the only option is to express it implicitly as an equation in $x$ and $y$.

*Solution.* We can write the differential equation in form (1) as
$$(4y - \cos y)\frac{dy}{dx} = 3x^2$$
Separating variables and integrating yields
$$(4y - \cos y)\,dy = 3x^2\,dx$$
$$\int (4y - \cos y)\,dy = \int 3x^2\,dx$$
or
$$2y^2 - \sin y = x^3 + C \tag{7}$$
For the initial-value problem, the initial condition $y(0) = 0$ requires that $y = 0$ if $x = 0$. Substituting these values into (7) to determine the constant of integration yields $C = 0$ (verify). Thus, the solution of the initial-value problem is
$$2y^2 - \sin y = x^3$$
or
$$x = \sqrt[3]{2y^2 - \sin y} \tag{8}$$
Some integral curves and the solution of the initial-value problem in Example 2 are graphed in Figure 8.2.2.

Initial-value problems often result from geometrical questions, as in the following example.

#### Example 3
Find a curve in the $xy$-plane that passes through $(0, 3)$ and whose tangent line at a point $(x, y)$ has slope $2x/y^2$.

> **TECHNOLOGY MASTERY**  
> Some computer algebra systems can graph implicit equations. Figure 8.2.2 shows the graphs of (7) for $C = 0, \pm 1, \pm 2$, and $\pm 3$. If you have a CAS that can graph implicit equations, try to duplicate this figure.

*Solution.* Since the slope of the tangent line is $dy/dx$, we have
$$\frac{dy}{dx} = \frac{2x}{y^2} \tag{9}$$
and, since the curve passes through $(0, 3)$, we have the initial condition
$$y(0) = 3$$
Equation (9) is separable and can be written as
$$y^2\,dy = 2x\,dx$$
so
$$\int y^2\,dy = \int 2x\,dx \quad \text{or} \quad \frac{1}{3}y^3 = x^2 + C$$
It follows from the initial condition that $y = 3$ if $x = 0$. Substituting these values into the last equation yields $C = 9$ (verify), so the equation of the desired curve is
$$\frac{1}{3}y^3 = x^2 + 9 \quad \text{or} \quad y = (3x^2 + 27)^{1/3}$$

### EXPONENTIAL GROWTH AND DECAY MODELS

The population growth and pharmacology models developed in Section 8.1 are examples of a general class of models called **exponential models**. In general, exponential models arise in situations where a quantity increases or decreases at a rate that is proportional to the amount of the quantity present. More precisely, we make the following definition.

> **8.2.1 DEFINITION**  
> A quantity $y = y(t)$ is said to have an **exponential growth model** if it increases at a rate that is proportional to the amount of the quantity present, and it is said to have an **exponential decay model** if it decreases at a rate that is proportional to the amount of the quantity present. Thus, for an exponential growth model, the quantity $y(t)$ satisfies an equation of the form
> $$\frac{dy}{dt} = ky \quad (k > 0) \tag{10}$$
> and for an exponential decay model, the quantity $y(t)$ satisfies an equation of the form
> $$\frac{dy}{dt} = -ky \quad (k > 0) \tag{11}$$
> The constant $k$ is called the **growth constant** or the **decay constant**, as appropriate.

Equations (10) and (11) are separable since they have the form of (1), but with $t$ rather than $x$ as the independent variable. To illustrate how these equations can be solved, suppose that a positive quantity $y = y(t)$ has an exponential growth model and that we know the amount of the quantity at some point in time, say $y = y_0$ when $t = 0$. Thus, a formula for $y(t)$ can be obtained by solving the initial-value problem
$$\frac{dy}{dt} = ky, \quad y(0) = y_0$$
Separating variables and integrating yields
$$\int \frac{1}{y}\,dy = \int k\,dt$$
or (since $y > 0$)
$$\ln y = kt + C \tag{12}$$
The initial condition implies that $y = y_0$ when $t = 0$. Substituting these values in (12) yields $C = \ln y_0$ (verify). Thus,
$$\ln y = kt + \ln y_0$$
from which it follows that
$$y = e^{\ln y} = e^{kt + \ln y_0}$$
or, equivalently,
$$y = y_0 e^{kt} \tag{13}$$
We leave it for you to show that if $y = y(t)$ has an exponential decay model, and if $y(0) = y_0$, then
$$y = y_0 e^{-kt} \tag{14}$$

### INTERPRETING THE GROWTH AND DECAY CONSTANTS

The significance of the constant $k$ in Formulas (13) and (14) can be understood by reexamining the differential equations that gave rise to these formulas. For example, in the case of the exponential growth model, Equation (10) can be rewritten as
$$k = \frac{dy/dt}{y} \tag{15}$$
which states that the growth rate as a fraction of the entire population remains constant over time, and this constant is $k$. For this reason, $k$ is called the **relative growth rate** of the population. It is usual to express the relative growth rate as a percentage. Thus, a relative growth rate of 3% per unit of time in an exponential growth model means that $k = 0.03$. Similarly, the constant $k$ in an exponential decay model is called the **relative decay rate**.

> It is standard practice in applications to call (15) the *growth rate*, even though it is misleading (the growth rate is $dy/dt$). However, the practice is so common that we will follow it here.

#### Example 4
According to the U.S. Census Bureau, the world population in 2011 was 6.9 billion and growing at a rate of about 1.10% per year. Assuming an exponential growth model, estimate the world population at the beginning of the year 2030.

> In Example 4 the growth rate was given, so there was no need to calculate it. If the growth rate or decay rate is unknown, then it can be calculated using the initial condition and the value of $y$ at another point in time (Exercise 44).

*Solution.* We assume that the population at the beginning of 2011 was 6.9 billion and let
$$t = \text{time elapsed from the beginning of 2011 (in years)}$$
$$y = \text{world population (in billions)}$$
Since the beginning of 2011 corresponds to $t = 0$, it follows from the given data that
$$y_0 = y(0) = 6.9\text{ billion}$$
Since the growth rate is 1.10% ($k = 0.011$), it follows from (13) that the world population at time $t$ will be
$$y(t) = y_0 e^{kt} = 6.9e^{0.011t} \tag{16}$$
Since the beginning of the year 2030 corresponds to an elapsed time of $t = 19$ years ($2030 - 2011 = 19$), it follows from (16) that the world population by the year 2030 will be
$$y(19) = 6.9e^{0.011(19)} \approx 8.5$$
which is a population of approximately 8.5 billion.

### DOUBLING TIME AND HALF-LIFE

If a quantity $y$ has an exponential growth model, then the time required for the original size to double is called the **doubling time**, and if $y$ has an exponential decay model, then the time required for the original size to reduce by half is called the **half-life**. As it turns out, doubling time and half-life depend only on the growth or decay rate and not on the amount present initially. To see why this is so, suppose that $y = y(t)$ has an exponential growth model
$$y = y_0 e^{kt} \tag{17}$$
and let $T$ denote the amount of time required for $y$ to double in size. Thus, at time $t = T$ the value of $y$ will be $2y_0$, and hence from (17)
$$2y_0 = y_0 e^{kT} \quad \text{or} \quad e^{kT} = 2$$
Taking the natural logarithm of both sides yields $kT = \ln 2$, which implies that the doubling time is
$$T = \frac{1}{k}\ln 2 \tag{18}$$
We leave it as an exercise to show that Formula (18) also gives the half-life of an exponential decay model. Observe that this formula does not involve the initial amount $y_0$, so that in an exponential growth or decay model, the quantity $y$ doubles (or reduces by half) every $T$ units (Figure 8.2.3).

#### Example 5
It follows from (18) that with a continued growth rate of 1.10% per year, the doubling time for the world population will be
$$T = \frac{1}{0.011}\ln 2 \approx 63$$
or approximately 63 years. Thus, with a continued 1.10% annual growth rate the population of 6.9 billion in 2011 will double to 13.8 billion by the year 2074 and will double again to 27.6 billion by 2137.

### RADIOACTIVE DECAY

It is a fact of physics that radioactive elements disintegrate spontaneously in a process called **radioactive decay**. Experimentation has shown that the rate of disintegration is proportional to the amount of the element present, which implies that the amount $y = y(t)$ of a radioactive element present as a function of time has an exponential decay model.

Every radioactive element has a specific half-life; for example, the half-life of radioactive carbon-14 is about 5730 years. Thus, from (18), the decay constant for this element is
$$k = \frac{1}{T}\ln 2 = \frac{\ln 2}{5730} \approx 0.000121$$
and this implies that if there are $y_0$ units of carbon-14 present at time $t = 0$, then the number of units present after $t$ years will be approximately
$$y(t) = y_0 e^{-0.000121t} \tag{19}$$

#### Example 6
If 100 grams of radioactive carbon-14 are stored in a cave for 1000 years, how many grams will be left at that time?

*Solution.* From (19) with $y_0 = 100$ and $t = 1000$, we obtain
$$y(1000) = 100e^{-0.000121(1000)} = 100e^{-0.121} \approx 88.6$$
Thus, about 88.6 grams will be left.

### CARBON DATING

When the nitrogen in the Earth's upper atmosphere is bombarded by cosmic radiation, the radioactive element carbon-14 is produced. This carbon-14 combines with oxygen to form carbon dioxide, which is ingested by plants, which in turn are eaten by animals. In this way all living plants and animals absorb quantities of radioactive carbon-14. In 1947 the American nuclear scientist W. F. Libby* proposed the theory that the percentage of carbon-14 in the atmosphere and in living tissues of plants is the same. When a plant or animal dies, the carbon-14 in the tissue begins to decay. Thus, the age of an artifact that contains plant or animal material can be estimated by determining what percentage of its original carbon-14 content remains. Various procedures, called **carbon dating** or **carbon-14 dating**, have been developed for measuring this percentage.

> \* W. F. Libby, "Radiocarbon Dating," *American Scientist*, Vol. 44, 1956, pp. 98–112.

#### Example 7
In 1988 the Vatican authorized the British Museum to date a cloth relic known as the Shroud of Turin, possibly the burial shroud of Jesus of Nazareth. This cloth, which first surfaced in 1356, contains the negative image of a human body that was widely believed to be that of Jesus. The report of the British Museum showed that the fibers in the cloth contained between 92% and 93% of their original carbon-14. Use this information to estimate the age of the shroud.

*Solution.* From (19), the fraction of the original carbon-14 that remains after $t$ years is
$$\frac{y(t)}{y_0} = e^{-0.000121t}$$
Taking the natural logarithm of both sides and solving for $t$, we obtain
$$t = -\frac{1}{0.000121}\ln\left(\frac{y(t)}{y_0}\right)$$
Thus, taking $y(t)/y_0$ to be 0.93 and 0.92, we obtain
$$t = -\frac{1}{0.000121}\ln(0.93) \approx 600$$
$$t = -\frac{1}{0.000121}\ln(0.92) \approx 689$$
This means that when the test was done in 1988, the shroud was between 600 and 689 years old, thereby placing its origin between 1299 A.D. and 1388 A.D. Thus, if one accepts the validity of carbon-14 dating, the Shroud of Turin cannot be the burial shroud of Jesus of Nazareth.

---

### QUICK CHECK EXERCISES 8.2
*(See page 579 for answers.)*

1. Solve the first-order separable equation
   $$h(y)\frac{dy}{dx} = g(x)$$
   by completing the following steps:
   - **Step 1.** Separate the variables by writing the equation in the differential form \_\_\_\_.
   - **Step 2.** Integrate both sides of the equation in Step 1: \_\_\_\_.
   - **Step 3.** If $H(y)$ is any antiderivative of $h(y)$, $G(x)$ is any antiderivative of $g(x)$, and $C$ is an unspecified constant, then, as suggested by Step 2, the equation \_\_\_\_ will generally define a family of solutions to $h(y)\,dy/dx = g(x)$ implicitly.
2. Suppose that a quantity $y = y(t)$ has an exponential growth model with growth constant $k > 0$.
   - (a) $y(t)$ satisfies a first-order differential equation of the form $dy/dt =$ \_\_\_\_.
   - (b) In terms of $k$, the doubling time of the quantity is \_\_\_\_.
   - (c) If $y_0 = y(0)$ is the initial amount of the quantity, then an explicit formula for $y(t)$ is given by $y(t) =$ \_\_\_\_.
3. Suppose that a quantity $y = y(t)$ has an exponential decay model with decay constant $k > 0$.
   - (a) $y(t)$ satisfies a first-order differential equation of the form $dy/dt =$ \_\_\_\_.
   - (b) In terms of $k$, the half-life of the quantity is \_\_\_\_.
   - (c) If $y_0 = y(0)$ is the initial amount of the quantity, then an explicit formula for $y(t)$ is given by $y(t) =$ \_\_\_\_.
4. The initial-value problem
   $$\frac{dy}{dx} = -\frac{x}{y}, \quad y(0) = 1$$
   has solution $y(x) =$ \_\_\_\_.

---

### EXERCISE SET 8.2

**1–10 Solve the differential equation by separation of variables. Where reasonable, express the family of solutions as explicit functions of $x$.**
1. $\frac{dy}{dx} = \frac{y}{x}$
2. $\frac{dy}{dx} = 2(1 + y^2)x$
3. $\frac{\sqrt{1+x^2}}{1+y}\frac{dy}{dx} = -x$
4. $(1+x^4)\frac{dy}{dx} = \frac{x^3}{y}$
5. $(2+2y^2)y' = e^x y$
6. $y' = -xy$
7. $e^{-y}\sin x - y'\cos^2 x = 0$
8. $y' - (1+x)(1+y^2) = 0$
9. $\frac{dy}{dx} - \frac{y^2-y}{\sin x} = 0$
10. $y - \frac{dy}{dx}\sec x = 0$

**11–14 Solve the initial-value problem by separation of variables.**
11. $y' = \frac{3x^2}{2y+\cos y}, \quad y(0) = \pi$
12. $y' - xe^y = 2e^y, \quad y(0) = 0$
13. $\frac{dy}{dt} = \frac{2t+1}{2y-2}, \quad y(0) = -1$
14. $y'\cosh^2 x - y\cosh 2x = 0, \quad y(0) = 3$

15. (a) Sketch some typical integral curves of the differential equation $y' = y/2x$.  
    (b) Find an equation for the integral curve that passes through the point $(2, 1)$.
16. (a) Sketch some typical integral curves of the differential equation $y' = -x/y$.  
    (b) Find an equation for the integral curve that passes through the point $(3, 4)$.

**17–18 Solve the differential equation and then use a graphing utility to generate five integral curves for the equation.**
17. $(x^2 + 4)\frac{dy}{dx} + xy = 0$
18. $(\cos y)y' = \cos x$

**19–20 [CAS] Solve the differential equation. If you have a CAS with implicit plotting capability, use the CAS to generate five integral curves for the equation.**
19. $y' = \frac{x^2}{1-y^2}$
20. $y' = \frac{y}{1+y^2}$

**21–24 True–False Determine whether the statement is true or false. Explain your answer.**
21. Every differential equation of the form $y' = f(y)$ is separable.
22. A differential equation of the form $h(x)\frac{dy}{dx} = g(y)$ is not separable.
23. If a radioactive element has a half-life of 1 minute, and if a container holds $32\text{ g}$ of the element at 1:00 p.m., then the amount remaining at 1:05 p.m. will be $1\text{ g}$.
24. If a population is growing exponentially, then the time it takes the population to quadruple is independent of the size of the population.

25. Suppose that the initial condition in Example 1 had been $y(0) = 0$. Show that none of the solutions generated in Example 1 satisfy this initial condition, and then solve the initial-value problem
    $$\frac{dy}{dx} = -4xy^2, \quad y(0) = 0$$
    Why does the method of Example 1 fail to produce this particular solution?
26. Find all ordered pairs $(x_0, y_0)$ such that if the initial condition in Example 1 is replaced by $y(x_0) = y_0$, the solution of the resulting initial-value problem is defined for all real numbers.
27. Find an equation of a curve with $x$-intercept 2 whose tangent line at any point $(x, y)$ has slope $xe^{-y}$.
28. Use a graphing utility to generate a curve that passes through the point $(1, 1)$ and whose tangent line at $(x, y)$ is perpendicular to the line through $(x, y)$ with slope $-2y/(3x^2)$.
29. Suppose that an initial population of 10,000 bacteria grows exponentially at a rate of 2% per hour and that $y = y(t)$ is the number of bacteria present $t$ hours later.  
    (a) Find an initial-value problem whose solution is $y(t)$.  
    (b) Find a formula for $y(t)$.  
    (c) How long does it take for the initial population of bacteria to double?  
    (d) How long does it take for the population of bacteria to reach 45,000?
30. A cell of the bacterium *E. coli* divides into two cells every 20 minutes when placed in a nutrient culture. Let $y = y(t)$ be the number of cells that are present $t$ minutes after a single cell is placed in the culture. Assume that the growth of the bacteria is approximated by an exponential growth model.  
    (a) Find an initial-value problem whose solution is $y(t)$.  
    (b) Find a formula for $y(t)$.  
    (c) How many cells are present after 2 hours?  
    (d) How long does it take for the number of cells to reach 1,000,000?
31. Radon-222 is a radioactive gas with a half-life of 3.83 days. This gas is a health hazard because it tends to get trapped in the basements of houses, and many health officials suggest that homeowners seal their basements to prevent entry of the gas. Assume that $5.0 \times 10^7$ radon atoms are trapped in a basement at the time it is sealed and that $y(t)$ is the number of atoms present $t$ days later.  
    (a) Find an initial-value problem whose solution is $y(t)$.  
    (b) Find a formula for $y(t)$.  
    (c) How many atoms will be present after 30 days?  
    (d) How long will it take for 90% of the original quantity of gas to decay?
32. Polonium-210 is a radioactive element with a half-life of 140 days. Assume that 10 milligrams of the element are placed in a lead container and that $y(t)$ is the number of milligrams present $t$ days later.  
    (a) Find an initial-value problem whose solution is $y(t)$.  
    (b) Find a formula for $y(t)$.  
    (c) How many milligrams will be present after 10 weeks?  
    (d) How long will it take for 70% of the original sample to decay?
33. Suppose that 100 fruit flies are placed in a breeding container that can support at most 10,000 flies. Assuming that the population grows exponentially at a rate of 2% per day, how long will it take for the container to reach capacity?
34. Suppose that the town of Grayrock had a population of 10,000 in 2006 and a population of 12,000 in 2011. Assuming an exponential growth model, in what year will the population reach 20,000?
35. A scientist wants to determine the half-life of a certain radioactive substance. She determines that in exactly 5 days a 10.0-milligram sample of the substance decays to 3.5 milligrams. Based on these data, what is the half-life?
36. Suppose that 30% of a certain radioactive substance decays in 5 years.  
    (a) What is the half-life of the substance in years?  
    (b) Suppose that a certain quantity of this substance is stored in a cave. What percentage of it will remain after $t$ years?

#### FOCUS ON CONCEPTS
37. (a) Make a conjecture about the effect on the graphs of $y = y_0 e^{kt}$ and $y = y_0 e^{-kt}$ of varying $k$ and keeping $y_0$ fixed. Confirm your conjecture with a graphing utility.  
    (b) Make a conjecture about the effect on the graphs of $y = y_0 e^{kt}$ and $y = y_0 e^{-kt}$ of varying $y_0$ and keeping $k$ fixed. Confirm your conjecture with a graphing utility.
38. (a) What effect does increasing $y_0$ and keeping $k$ fixed have on the doubling time or half-life of an exponential model? Justify your answer.  
    (b) What effect does increasing $k$ and keeping $y_0$ fixed have on the doubling time and half-life of an exponential model? Justify your answer.
39. (a) There is a trick, called the **Rule of 70**, that can be used to get a quick estimate of the doubling time or half-life of an exponential model. According to this rule, the doubling time or half-life is roughly 70 divided by the percentage growth or decay rate. For example, we showed in Example 5 that with a continued growth rate of 1.10% per year the world population would double every 63 years. This result agrees with the Rule of 70, since $70/1.10 \approx 63.6$. Explain why this rule works.  
    (b) Use the Rule of 70 to estimate the doubling time of a population that grows exponentially at a rate of 1% per year.  
    (c) Use the Rule of 70 to estimate the half-life of a population that decreases exponentially at a rate of 3.5% per hour.  
    (d) Use the Rule of 70 to estimate the growth rate that would be required for a population growing exponentially to double every 10 years.
40. Find a formula for the tripling time of an exponential growth model.
41. In 1950, a research team digging near Folsom, New Mexico, found charred bison bones along with some leaf-shaped projectile points (called the "Folsom points") that had been made by a Paleo-Indian hunting culture. It was clear from the evidence that the bison had been cooked and eaten by the makers of the points, so that carbon-14 dating of the bones made it possible for the researchers to determine when the hunters roamed North America. Tests showed that the bones contained between 27% and 30% of their original carbon-14. Use this information to show that the hunters lived roughly between 9000 B.C. and 8000 B.C.
42. (a) Use a graphing utility to make a graph of $p_{\text{rem}}$ versus $t$, where $p_{\text{rem}}$ is the percentage of carbon-14 that remains in an artifact after $t$ years.  
    (b) Use the graph to estimate the percentage of carbon-14 that would have to have been present in the 1988 test of the Shroud of Turin for it to have been the burial shroud of Jesus of Nazareth (see Example 7).
43. (a) It is currently accepted that the half-life of carbon-14 might vary $\pm 40$ years from its nominal value of 5730 years. Does this variation make it possible that the Shroud of Turin dates to the time of Jesus of Nazareth (see Example 7)?  
    (b) Review the subsection of Section 2.9 entitled Error Propagation, and then estimate the percentage error that results in the computed age of an artifact from an $r\%$ error in the half-life of carbon-14.
44. Suppose that a quantity $y$ has an exponential growth model $y = y_0 e^{kt}$ or an exponential decay model $y = y_0 e^{-kt}$, and it is known that $y = y_1$ if $t = t_1$. In each case find a formula for $k$ in terms of $y_0, y_1$, and $t_1$, assuming that $t_1 \neq 0$.
45. (a) Show that if a quantity $y = y(t)$ has an exponential model, and if $y(t_1) = y_1$ and $y(t_2) = y_2$, then the doubling time or the half-life $T$ is
    $$T = \left|\frac{(t_2 - t_1)\ln 2}{\ln(y_2/y_1)}\right|$$
    (b) In a certain 1-hour period the number of bacteria in a colony increases by 25%. Assuming an exponential growth model, what is the doubling time for the colony?
46. Suppose that $P$ dollars is invested at an annual interest rate of $r \times 100\%$. If the accumulated interest is credited to the account at the end of the year, then the interest is said to be compounded annually; if it is credited at the end of each 6-month period, then it is said to be compounded semiannually; and if it is credited at the end of each 3-month period, then it is said to be compounded quarterly. The more frequently the interest is compounded, the better it is for the investor since more of the interest is itself earning interest.  
    (a) Show that if interest is compounded $n$ times a year at equally spaced intervals, then the value $A$ of the investment after $t$ years is
    $$A = P\left(1 + \frac{r}{n}\right)^{nt}$$
    (b) One can imagine interest to be compounded each day, each hour, each minute, and so forth. Carried to the limit one can conceive of interest compounded at each instant of time; this is called **continuous compounding**. Thus, from part (a), the value $A$ of $P$ dollars after $t$ years when invested at an annual rate of $r \times 100\%$, compounded continuously, is
    $$A = \lim_{n \to +\infty} P\left(1 + \frac{r}{n}\right)^{nt}$$
    Use the fact that $\lim_{x \to 0}(1 + x)^{1/x} = e$ to prove that $A = Pe^{rt}$.  
    (c) Use the result in part (b) to show that money invested at continuous compound interest increases at a rate proportional to the amount present.
47. (a) If $\$1000$ is invested at 8% per year compounded continuously (Exercise 46), what will the investment be worth after 5 years?  
    (b) If it is desired that an investment at 8% per year compounded continuously should have a value of $\$10,000$ after 10 years, how much should be invested now?  
    (c) How long does it take for an investment at 8% per year compounded continuously to double in value?
48. What is the effective annual interest rate for an interest rate of $r\%$ per year compounded continuously?
49. Assume that $y = y(t)$ satisfies the logistic equation with $y_0 = y(0)$ the initial value of $y$.  
    (a) Use separation of variables to derive the solution
    $$y = \frac{y_0 L}{y_0 + (L - y_0)e^{-kt}}$$
    (b) Use part (a) to show that $\lim_{t \to +\infty} y(t) = L$.
50. Use your answer to Exercise 49 to derive a solution to the model for the spread of disease [Equation (6) of Section 8.1].
51. The graph of a solution to the logistic equation is known as a **logistic curve**, and if $y_0 > 0$, it has one of four general shapes, depending on the relationship between $y_0$ and $L$. In each part, assume that $k = 1$ and use a graphing utility to plot a logistic curve satisfying the given condition.  
    (a) $y_0 > L$  
    (b) $y_0 = L$  
    (c) $L/2 \le y_0 < L$  
    (d) $0 < y_0 < L/2$

**52–53 The graph of a logistic model**
$$y = \frac{y_0 L}{y_0 + (L - y_0)e^{-kt}}$$
**is shown. Estimate $y_0, L$, and $k$.**
52. (Graph shown in text: initial value around 200, carrying capacity 1000).
53. (Graph shown in text: initial value around 2, carrying capacity 8).

54. Plot a solution to the initial-value problem
    $$\frac{dy}{dt} = 0.98\left(1 - \frac{y}{5}\right)y, \quad y_0 = 1$$
55. Suppose that the growth of a population $y = y(t)$ is given by the logistic equation
    $$y = \frac{60}{5 + 7e^{-t}}$$
    (a) What is the population at time $t = 0$?  
    (b) What is the carrying capacity $L$?  
    (c) What is the constant $k$?  
    (d) When does the population reach half of the carrying capacity?  
    (e) Find an initial-value problem whose solution is $y(t)$.
56. Suppose that the growth of a population $y = y(t)$ is given by the logistic equation
    $$y = \frac{1000}{1 + 999e^{-0.9t}}$$
    (a) What is the population at time $t = 0$?  
    (b) What is the carrying capacity $L$?  
    (c) What is the constant $k$?  
    (d) When does the population reach 75% of the carrying capacity?  
    (e) Find an initial-value problem whose solution is $y(t)$.
57. Suppose that a university residence hall houses 1000 students. Following the semester break, 20 students in the hall return with the flu, and 5 days later 35 students have the flu.  
    (a) Use the result of Exercise 50 to find the number of students who will have the flu $t$ days after returning to school.  
    (b) Make a table that illustrates how the flu spreads day to day over a 2-week period.  
    (c) Use a graphing utility to generate a graph that illustrates how the flu spreads over a 2-week period.
58. Suppose that at time $t = 0$ an object with temperature $T_0$ is placed in a room with constant temperature $T_a$. If $T_0 < T_a$, then the temperature of the object will increase, and if $T_0 > T_a$, then the temperature will decrease. Assuming that Newton's Law of Cooling applies, show that in both cases the temperature $T(t)$ at time $t$ is given by
    $$T(t) = T_a + (T_0 - T_a)e^{-kt}$$
    where $k$ is a positive constant.
59. A cup of water with a temperature of $95^\circ\text{C}$ is placed in a room with a constant temperature of $21^\circ\text{C}$.  
    (a) Assuming that Newton's Law of Cooling applies, use the result of Exercise 58 to find the temperature of the water $t$ minutes after it is placed in the room. [*Note:* The solution will involve a constant of proportionality.]  
    (b) How many minutes will it take for the water to reach a temperature of $51^\circ\text{C}$ if it cools to $85^\circ\text{C}$ in 1 minute?
60. A glass of lemonade with a temperature of $40^\circ\text{F}$ is placed in a room with a constant temperature of $70^\circ\text{F}$, and 1 hour later its temperature is $52^\circ\text{F}$. Show that $t$ hours after the lemonade is placed in the room its temperature is approximated by $T = 70 - 30e^{-0.5t}$.
61. A rocket, fired upward from rest at time $t = 0$, has an initial mass of $m_0$ (including its fuel). Assuming that the fuel is consumed at a constant rate $k$, the mass $m$ of the rocket, while fuel is being burned, will be given by $m = m_0 - kt$. It can be shown that if air resistance is neglected and the fuel gases are expelled at a constant speed $c$ relative to the rocket, then the velocity $v$ of the rocket will satisfy the equation
    $$m\frac{dv}{dt} = ck - mg$$
    where $g$ is the acceleration due to gravity.  
    (a) Find $v(t)$ keeping in mind that the mass $m$ is a function of $t$.  
    (b) Suppose that the fuel accounts for 80% of the initial mass of the rocket and that all of the fuel is consumed in $100\text{ s}$. Find the velocity of the rocket in meters per second at the instant the fuel is exhausted. [*Note:* Take $g = 9.8\text{ m/s}^2$ and $c = 2500\text{ m/s}$.]
62. A bullet of mass $m$, fired straight up with an initial velocity of $v_0$, is slowed by the force of gravity and a drag force of air resistance $kv^2$, where $k$ is a positive constant. As the bullet moves upward, its velocity $v$ satisfies the equation
    $$m\frac{dv}{dt} = -(kv^2 + mg)$$
    where $g$ is the constant acceleration due to gravity.  
    (a) Show that if $x = x(t)$ is the height of the bullet above the barrel opening at time $t$, then
    $$mv\frac{dv}{dx} = -(kv^2 + mg)$$
    (b) Express $x$ in terms of $v$ given that $x = 0$ when $v = v_0$.  
    (c) Assuming that
    $$v_0 = 988\text{ m/s}, \quad g = 9.8\text{ m/s}^2$$
    $$m = 3.56 \times 10^{-3}\text{ kg}, \quad k = 7.3 \times 10^{-6}\text{ kg/m}$$
    use the result in part (b) to find out how high the bullet rises. [*Hint:* Find the velocity of the bullet at its highest point.]

**63–64 Suppose that a tank containing a liquid is vented to the air at the top and has an outlet at the bottom through which the liquid can drain. It follows from Torricelli's law in physics that if the outlet is opened at time $t = 0$, then at each instant the depth of the liquid $h(t)$ and the area $A(h)$ of the liquid's surface are related by**
$$A(h)\frac{dh}{dt} = -k\sqrt{h}$$
**where $k$ is a positive constant that depends on such factors as the viscosity of the liquid and the cross-sectional area of the outlet. Use this result in these exercises, assuming that $h$ is in feet, $A(h)$ is in square feet, and $t$ is in seconds.**
63. Suppose that the cylindrical tank in Figure Ex-63 (radius $1\text{ ft}$, height $4\text{ ft}$) is filled to a depth of 4 feet at time $t = 0$ and that the constant in Torricelli's law is $k = 0.025$.  
    (a) Find $h(t)$.  
    (b) How many minutes will it take for the tank to drain completely?
64. Follow the directions of Exercise 63 for the cylindrical tank in Figure Ex-64 (diameter $6\text{ ft}$, height $4\text{ ft}$ lying on its side), assuming that the tank is filled to a depth of 4 feet at time $t = 0$ and that the constant in Torricelli's law is $k = 0.025$.
65. Suppose that a particle moving along the $x$-axis encounters a resisting force that results in an acceleration of $a = dv/dt = -\frac{1}{32}v^2$. If $x = 0\text{ cm}$ and $v = 128\text{ cm/s}$ at time $t = 0$, find the velocity $v$ and position $x$ as a function of $t$ for $t \ge 0$.
66. Suppose that a particle moving along the $x$-axis encounters a resisting force that results in an acceleration of $a = dv/dt = -0.02\sqrt{v}$. Given that $x = 0\text{ cm}$ and $v = 9\text{ cm/s}$ at time $t = 0$, find the velocity $v$ and position $x$ as a function of $t$ for $t \ge 0$.

#### FOCUS ON CONCEPTS
67. Use implicit differentiation to prove that any differentiable function defined implicitly by Equation (4) will be a solution to (1).
68. Prove that a solution to the initial-value problem
    $$h(y)\frac{dy}{dx} = g(x), \quad y(x_0) = y_0$$
    is defined implicitly by the equation
    $$\int_{y_0}^y h(r)\,dr = \int_{x_0}^x g(s)\,ds$$
69. Let $L$ denote a tangent line at $(x, y)$ to a solution of Equation (1), and let $(x_1, y_1), (x_2, y_2)$ denote any two points on $L$. Prove that Equation (2) is satisfied by $dy = \Delta y = y_2 - y_1$ and $dx = \Delta x = x_2 - x_1$.
70. **Writing.** A student objects to the method of separation of variables because it often produces an equation in $x$ and $y$ instead of an explicit function $y = f(x)$. Discuss the pros and cons of this student's position.
71. **Writing.** A student objects to Step 2 in the method of separation of variables because one side of the equation is integrated with respect to $x$ while the other side is integrated with respect to $y$. Answer this student's objection. [*Hint:* Recall the method of integration by substitution.]

---

### QUICK CHECK ANSWERS 8.2
1. Step 1: $h(y)\,dy = g(x)\,dx$; Step 2: $\int h(y)\,dy = \int g(x)\,dx$; Step 3: $H(y) = G(x) + C$  
2. (a) $ky$  (b) $\frac{\ln 2}{k}$  (c) $y_0 e^{kt}$  
3. (a) $-ky$  (b) $\frac{\ln 2}{k}$  (c) $y_0 e^{-kt}$  
4. $y = \sqrt{1 - x^2}$

---

## 8.3 SLOPE FIELDS; EULER'S METHOD

In this section we will reexamine the concept of a slope field and we will discuss a method for approximating solutions of first-order equations numerically. Numerical approximations are important in cases where the differential equation cannot be solved exactly.

### FUNCTIONS OF TWO VARIABLES

We will be concerned here with first-order equations that are expressed with the derivative by itself on one side of the equation. For example,
$$y' = x^3 \quad \text{and} \quad y' = \sin(xy)$$
The first of these equations involves only $x$ on the right side, so it has the form $y' = f(x)$. However, the second equation involves both $x$ and $y$ on the right side, so it has the form $y' = f(x, y)$, where the symbol $f(x, y)$ stands for a function of the two variables $x$ and $y$. Later in the text we will study functions of two variables in more depth, but for now it will suffice to think of $f(x, y)$ as a formula that produces a unique output when values of $x$ and $y$ are given as inputs. For example, if
$$f(x, y) = x^2 + 3y$$
and if the inputs are $x = 2$ and $y = -4$, then the output is
$$f(2, -4) = 2^2 + 3(-4) = 4 - 12 = -8$$

> In applied problems involving time, it is usual to use $t$ as the independent variable, in which case one would be concerned with equations of the form $y' = f(t, y)$, where $y' = dy/dt$.

### SLOPE FIELDS

In Section 4.2 we introduced the concept of a slope field in the context of differential equations of the form $y' = f(x)$; the same principles apply to differential equations of the form
$$y' = f(x, y)$$
To see why this is so, let us review the basic idea. If we interpret $y'$ as the slope of a tangent line, then the differential equation states that at each point $(x, y)$ on an integral curve, the slope of the tangent line is equal to the value of $f$ at that point (Figure 8.3.1). For example, suppose that $f(x, y) = y - x$, in which case we have the differential equation
$$y' = y - x \tag{1}$$
A geometric description of the set of integral curves can be obtained by choosing a rectangular grid of points in the $xy$-plane, calculating the slopes of the tangent lines to the integral curves at the gridpoints, and drawing small segments of the tangent lines through those points. The resulting picture is called a **slope field** or a **direction field** for the differential equation because it shows the "slope" or "direction" of the integral curves at the gridpoints. The more gridpoints that are used, the better the description of the integral curves. For example, Figure 8.3.2 shows two slope fields for (1)—the first was obtained by hand calculation using the 49 gridpoints shown in the accompanying table, and the second, which gives a clearer picture of the integral curves, was obtained using 625 gridpoints and a CAS.

#### VALUES OF $f(x, y) = y - x$
| | $y = -3$ | $y = -2$ | $y = -1$ | $y = 0$ | $y = 1$ | $y = 2$ | $y = 3$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $x = -3$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| $x = -2$ | -1 | 0 | 1 | 2 | 3 | 4 | 5 |
| $x = -1$ | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
| $x = 0$ | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
| $x = 1$ | -4 | -3 | -2 | -1 | 0 | 1 | 2 |
| $x = 2$ | -5 | -4 | -3 | -2 | -1 | 0 | 1 |
| $x = 3$ | -6 | -5 | -4 | -3 | -2 | -1 | 0 |

It so happens that Equation (1) can be solved exactly using a method we will introduce in Section 8.4. We leave it for you to confirm that the general solution of this equation is
$$y = x + 1 + Ce^x \tag{2}$$
Figure 8.3.3 shows some of the integral curves superimposed on the slope field. Note that it was not necessary to have the general solution to construct the slope field. Indeed, slope fields are important precisely because they can be constructed in cases where the differential equation cannot be solved exactly.

### EULER'S METHOD

Consider an initial-value problem of the form
$$y' = f(x, y), \quad y(x_0) = y_0$$
The slope field for the differential equation $y' = f(x, y)$ gives us a way to visualize the solution of the initial-value problem, since the graph of the solution is the integral curve that passes through the point $(x_0, y_0)$. The slope field will also help us to develop a method for approximating the solution to the initial-value problem numerically.

We will not attempt to approximate $y(x)$ for all values of $x$; rather, we will choose some small increment $\Delta x$ and focus on approximating the values of $y(x)$ at a succession of $x$-values spaced $\Delta x$ units apart, starting from $x_0$. We will denote these $x$-values by
$$x_1 = x_0 + \Delta x, \quad x_2 = x_1 + \Delta x, \quad x_3 = x_2 + \Delta x, \quad x_4 = x_3 + \Delta x, \dots$$
and we will denote the approximations of $y(x)$ at these points by
$$y_1 \approx y(x_1), \quad y_2 \approx y(x_2), \quad y_3 \approx y(x_3), \quad y_4 \approx y(x_4), \dots$$

The technique that we will describe for obtaining these approximations is called **Euler's Method**. Although there are better approximation methods available, many of them use Euler's Method as a starting point, so the underlying concepts are important to understand.

The basic idea behind Euler's Method is to start at the known initial point $(x_0, y_0)$ and draw a line segment in the direction determined by the slope field until we reach the point $(x_1, y_1)$ with $x$-coordinate $x_1 = x_0 + \Delta x$ (Figure 8.3.4). If $\Delta x$ is small, then it is reasonable to expect that this line segment will not deviate much from the integral curve $y = y(x)$, and thus $y_1$ should closely approximate $y(x_1)$. To obtain the subsequent approximations, we repeat the process using the slope field as a guide at each step. Starting at the endpoint $(x_1, y_1)$, we draw a line segment determined by the slope field until we reach the point $(x_2, y_2)$ with $x$-coordinate $x_2 = x_1 + \Delta x$, and from that point we draw a line segment determined by the slope field to the point $(x_3, y_3)$ with $x$-coordinate $x_3 = x_2 + \Delta x$, and so forth. As indicated in Figure 8.3.4, this procedure produces a polygonal path that tends to follow the integral curve closely, so it is reasonable to expect that the $y$-values $y_2, y_3, y_4, \dots$ will closely approximate $y(x_2), y(x_3), y(x_4), \dots$.

To explain how the approximations $y_1, y_2, y_3, \dots$ can be computed, let us focus on a typical line segment. As indicated in Figure 8.3.5, assume that we have found the point $(x_n, y_n)$, and we are trying to determine the next point $(x_{n+1}, y_{n+1})$, where $x_{n+1} = x_n + \Delta x$. Since the slope of the line segment joining the points is determined by the slope field at the starting point, the slope is $f(x_n, y_n)$, and hence
$$\frac{y_{n+1} - y_n}{x_{n+1} - x_n} = \frac{y_{n+1} - y_n}{\Delta x} = f(x_n, y_n)$$
which we can rewrite as
$$y_{n+1} = y_n + f(x_n, y_n)\Delta x$$
This formula, which is the heart of Euler's Method, tells us how to use each approximation to compute the next approximation.

> ### Euler's Method
> To approximate the solution of the initial-value problem
> $$y' = f(x, y), \quad y(x_0) = y_0$$
> proceed as follows:  
> **Step 1.** Choose a nonzero number $\Delta x$ to serve as an *increment* or *step size* along the $x$-axis, and let
> $$x_1 = x_0 + \Delta x, \quad x_2 = x_1 + \Delta x, \quad x_3 = x_2 + \Delta x, \dots$$
> **Step 2.** Compute successively
> $$y_1 = y_0 + f(x_0, y_0)\Delta x$$
> $$y_2 = y_1 + f(x_1, y_1)\Delta x$$
> $$y_3 = y_2 + f(x_2, y_2)\Delta x$$
> $$\vdots$$
> $$y_{n+1} = y_n + f(x_n, y_n)\Delta x$$
> The numbers $y_1, y_2, y_3, \dots$ in these equations are the approximations of $y(x_1), y(x_2), y(x_3), \dots$.

#### Example 1
Use Euler's Method with a step size of 0.1 to make a table of approximate values of the solution of the initial-value problem
$$y' = y - x, \quad y(0) = 2 \tag{3}$$
over the interval $0 \le x \le 1$.

*Solution.* In this problem we have $f(x, y) = y - x$, $x_0 = 0$, and $y_0 = 2$. Moreover, since the step size is 0.1, the $x$-values at which the approximate values will be obtained are
$$x_1 = 0.1, \quad x_2 = 0.2, \quad x_3 = 0.3, \dots, \quad x_9 = 0.9, \quad x_{10} = 1$$
The first three approximations are
$$y_1 = y_0 + f(x_0, y_0)\Delta x = 2 + (2 - 0)(0.1) = 2.2$$
$$y_2 = y_1 + f(x_1, y_1)\Delta x = 2.2 + (2.2 - 0.1)(0.1) = 2.41$$
$$y_3 = y_2 + f(x_2, y_2)\Delta x = 2.41 + (2.41 - 0.2)(0.1) = 2.631$$

Here is a way of organizing all 10 approximations rounded to five decimal places:

#### Euler's Method for $y' = y - x, \; y(0) = 2$ with $\Delta x = 0.1$
| $n$ | $x_n$ | $y_n$ | $f(x_n, y_n)\Delta x$ | $y_{n+1} = y_n + f(x_n, y_n)\Delta x$ |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 2.00000 | 0.20000 | 2.20000 |
| 1 | 0.1 | 2.20000 | 0.21000 | 2.41000 |
| 2 | 0.2 | 2.41000 | 0.22100 | 2.63100 |
| 3 | 0.3 | 2.63100 | 0.23310 | 2.86410 |
| 4 | 0.4 | 2.86410 | 0.24641 | 3.11051 |
| 5 | 0.5 | 3.11051 | 0.26105 | 3.37156 |
| 6 | 0.6 | 3.37156 | 0.27716 | 3.64872 |
| 7 | 0.7 | 3.64872 | 0.29487 | 3.94359 |
| 8 | 0.8 | 3.94359 | 0.31436 | 4.25795 |
| 9 | 0.9 | 4.25795 | 0.33579 | 4.59374 |
| 10 | 1.0 | 4.59374 | — | — |

Observe that each entry in the last column becomes the next entry in the third column. This is reminiscent of Newton's Method in which each successive approximation is used to find the next.

### ACCURACY OF EULER'S METHOD

It follows from (3) and the initial condition $y(0) = 2$ that the exact solution of the initial-value problem in Example 1 is
$$y = x + 1 + e^x$$
Thus, in this case we can compare the approximate values of $y(x)$ produced by Euler's Method with decimal approximations of the exact values (Table 8.3.1). In Table 8.3.1 the absolute error is calculated as
$$|\text{exact value} - \text{approximation}|$$
and the percentage error as
$$\frac{|\text{exact value} - \text{approximation}|}{|\text{exact value}|} \times 100\%$$

> As a rule of thumb, the absolute error in an approximation produced by Euler's Method is proportional to the step size. Thus, reducing the step size by half reduces the absolute and percentage errors by roughly half. However, reducing the step size increases the amount of computation, thereby increasing the potential for more roundoff error. Such matters are discussed in courses on differential equations or numerical analysis.

#### Table 8.3.1
| $x$ | EXACT SOLUTION | EULER APPROXIMATION | ABSOLUTE ERROR | PERCENTAGE ERROR |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 2.00000 | 2.00000 | 0.00000 | 0.00 |
| 0.1 | 2.20517 | 2.20000 | 0.00517 | 0.23 |
| 0.2 | 2.42140 | 2.41000 | 0.01140 | 0.47 |
| 0.3 | 2.64986 | 2.63100 | 0.01886 | 0.71 |
| 0.4 | 2.89182 | 2.86410 | 0.02772 | 0.96 |
| 0.5 | 3.14872 | 3.11051 | 0.03821 | 1.21 |
| 0.6 | 3.42212 | 3.37156 | 0.05056 | 1.48 |
| 0.7 | 3.71375 | 3.64872 | 0.06503 | 1.75 |
| 0.8 | 4.02554 | 3.94359 | 0.08195 | 2.04 |
| 0.9 | 4.35960 | 4.25795 | 0.10165 | 2.33 |
| 1.0 | 4.71828 | 4.59374 | 0.12454 | 2.64 |

> *Note:* Notice that the absolute error tends to increase as $x$ moves away from $x_0$.

---

### QUICK CHECK EXERCISES 8.3
*(See page 586 for answers.)*

1. Match each differential equation with its slope field (Figures I–IV).
   - (a) $y' = 2xy^2$
   - (b) $y' = e^{-y}$
   - (c) $y' = y$
   - (d) $y' = 2xy$
2. The slope field for $y' = y/x$ at the 16 gridpoints $(x, y)$, where $x = -2, -1, 1, 2$ and $y = -2, -1, 1, 2$ is shown in Figure Ex-2. Use this slope field and geometric reasoning to find the integral curve that passes through the point $(1, 2)$.
3. When using Euler's Method on the initial-value problem $y' = f(x, y), \; y(x_0) = y_0$, we obtain $y_{n+1}$ from $y_n, x_n$, and $\Delta x$ by means of the formula $y_{n+1} =$ \_\_\_\_.
4. Consider the initial-value problem $y' = y, \; y(0) = 1$.
   - (a) Use Euler's Method with two steps to approximate $y(1)$.
   - (b) What is the exact value of $y(1)$?

---

### EXERCISE SET 8.3

1. Sketch the slope field for $y' = xy/4$ at the 25 gridpoints $(x, y)$, where $x = -2, -1, \dots, 2$ and $y = -2, -1, \dots, 2$.
2. Sketch the slope field for $y' + y = 2$ at the 25 gridpoints $(x, y)$, where $x = 0, 1, \dots, 4$ and $y = 0, 1, \dots, 4$.
3. A slope field for the differential equation $y' = 1 - y$ is shown in Figure Ex-3. In each part, sketch the graph of the solution that satisfies the initial condition.  
   (a) $y(0) = -1$  
   (b) $y(0) = 1$  
   (c) $y(0) = 2$
4. Solve the initial-value problems in Exercise 3, and use a graphing utility to confirm that the integral curves for these solutions are consistent with the sketches you obtained from the slope field.

#### FOCUS ON CONCEPTS
5. Use the slope field in Exercise 3 to make a conjecture about the behavior of the solutions of $y' = 1 - y$ as $x \to +\infty$, and confirm your conjecture by examining the general solution of the equation.
6. In parts (a)–(f), match the differential equation with the slope field (Figure Ex-6, I–VI), and explain your reasoning.  
   (a) $y' = 1/x$  
   (b) $y' = 1/y$  
   (c) $y' = e^{-x^2}$  
   (d) $y' = y^2 - 1$  
   (e) $y' = \frac{x+y}{x-y}$  
   (f) $y' = (\sin x)(\sin y)$

**7–10 Use Euler's Method with the given step size $\Delta x$ or $\Delta t$ to approximate the solution of the initial-value problem over the stated interval. Present your answer as a table and as a graph.**
7. $dy/dx = \sqrt[3]{y}, \quad y(0) = 1, \quad 0 \le x \le 4, \quad \Delta x = 0.5$
8. $dy/dx = x - y^2, \quad y(0) = 1, \quad 0 \le x \le 2, \quad \Delta x = 0.25$
9. $dy/dt = \cos y, \quad y(0) = 1, \quad 0 \le t \le 2, \quad \Delta t = 0.5$
10. $dy/dt = e^{-y}, \quad y(0) = 0, \quad 0 \le t \le 1, \quad \Delta t = 0.1$

11. Consider the initial-value problem
    $$y' = \sin \pi t, \quad y(0) = 0$$
    Use Euler's Method with five steps to approximate $y(1)$.

**12–15 True–False Determine whether the statement is true or false. Explain your answer.**
12. If the graph of $y = f(x)$ is an integral curve for a slope field, then so is any vertical translation of this graph.
13. Every integral curve for the slope field $dy/dx = e^{xy}$ is the graph of an increasing function of $x$.
14. Every integral curve for the slope field $dy/dx = e^y$ is concave up.
15. If $p(y)$ is a cubic polynomial in $y$, then the slope field $dy/dx = p(y)$ has an integral curve that is a horizontal line.

#### FOCUS ON CONCEPTS
16. (a) Show that the solution of the initial-value problem $y' = e^{-x^2}, \; y(0) = 0$ is
    $$y(x) = \int_0^x e^{-t^2}\,dt$$
    (b) Use Euler's Method with $\Delta x = 0.05$ to approximate the value of
    $$y(1) = \int_0^1 e^{-t^2}\,dt$$
    and compare the answer to that produced by a calculating utility with a numerical integration capability.
17. The accompanying figure (Figure Ex-17) shows a slope field for the differential equation $y' = -x/y$.  
    (a) Use the slope field to estimate $y(1/2)$ for the solution that satisfies the given initial condition $y(0) = 1$.  
    (b) Compare your estimate to the exact value of $y(1/2)$.
18. Refer to slope field II in Quick Check Exercise 1.  
    (a) Does the slope field appear to have a horizontal line as an integral curve?  
    (b) Use the differential equation for the slope field to verify your answer to part (a).
19. Refer to the slope field in Exercise 3 and consider the integral curve through $(0, -1)$.  
    (a) Use the slope field to estimate where the integral curve intersects the $x$-axis.  
    (b) Compare your estimate in part (a) with the exact value of the $x$-intercept for the integral curve.
20. Consider the initial-value problem
    $$\frac{dy}{dx} = \frac{\sqrt{y}}{2}, \quad y(0) = 1$$
    (a) Use Euler's Method with step sizes of $\Delta x = 0.2, 0.1$, and $0.05$ to obtain three approximations of $y(1)$.  
    (b) Find $y(1)$ exactly.
21. A slope field of the form $y' = f(y)$ is said to be **autonomous**.  
    (a) Explain why the tangent segments along any horizontal line will be parallel for an autonomous slope field.  
    (b) The word *autonomous* means "independent." In what sense is an autonomous slope field independent?  
    (c) Suppose that $G(y)$ is an antiderivative of $1/[f(y)]$ and that $C$ is a constant. Explain why any differentiable function defined implicitly by $G(y) - x = C$ will be a solution to the equation $y' = f(y)$.
22. (a) Solve the equation $y' = \sqrt{y}$ and show that every nonconstant solution has a graph that is everywhere concave up.  
    (b) Explain how the conclusion in part (a) may be obtained directly from the equation $y' = \sqrt{y}$ without solving.
23. (a) Find a slope field whose integral curve through $(1, 1)$ satisfies $xy^3 - x^2 y = 0$ by differentiating this equation implicitly.  
    (b) Prove that if $y(x)$ is any integral curve of the slope field in part (a), then $x[y(x)]^3 - x^2 y(x)$ will be a constant function.  
    (c) Find an equation that implicitly defines the integral curve through $(-1, -1)$ of the slope field in part (a).
24. (a) Find a slope field whose integral curve through $(0, 0)$ satisfies $xe^y + ye^x = 0$ by differentiating this equation implicitly.  
    (b) Prove that if $y(x)$ is any integral curve of the slope field in part (a), then $xe^{y(x)} + y(x)e^x$ will be a constant function.  
    (c) Find an equation that implicitly defines the integral curve through $(1, 1)$ of the slope field in part (a).
25. Consider the initial-value problem $y' = y, \; y(0) = 1$, and let $y_n$ denote the approximation of $y(1)$ using Euler's Method with $n$ steps.  
    (a) What would you conjecture is the exact value of $\lim_{n \to +\infty} y_n$? Explain your reasoning.  
    (b) Find an explicit formula for $y_n$ and use it to verify your conjecture in part (a).
26. **Writing.** Explain the connection between Euler's Method and the local linear approximation discussed in Section 2.9.
27. **Writing.** Given a slope field, what features of an integral curve might be discussed from the slope field? Apply your ideas to the slope field in Exercise 3.

---

### QUICK CHECK ANSWERS 8.3
1. (a) IV (b) III (c) I (d) II  
2. $y = 2x, \; x > 0$  
3. $y_n + f(x_n, y_n)\Delta x$  
4. (a) $2.25$  (b) $e$

---

## 8.4 FIRST-ORDER DIFFERENTIAL EQUATIONS AND APPLICATIONS

In this section we will discuss a general method that can be used to solve a large class of first-order differential equations. We will use this method to solve differential equations related to the problems of mixing liquids and free fall retarded by air resistance.

### FIRST-ORDER LINEAR EQUATIONS

The simplest first-order equations are those that can be written in the form
$$\frac{dy}{dx} = q(x) \tag{1}$$
Such equations can often be solved by integration. For example, if
$$\frac{dy}{dx} = x^3 \tag{2}$$
then
$$y = \int x^3\,dx = \frac{x^4}{4} + C$$
is the general solution of (2) on the interval $(-\infty, +\infty)$. More generally, a first-order differential equation is called **linear** if it is expressible in the form
$$\frac{dy}{dx} + p(x)y = q(x) \tag{3}$$
Equation (1) is the special case of (3) that results when the function $p(x)$ is identically 0. Some other examples of first-order linear differential equations are
- $\frac{dy}{dx} + x^2 y = e^x$ with $p(x) = x^2, \; q(x) = e^x$
- $\frac{dy}{dx} + (\sin x)y + x^3 = 0$ with $p(x) = \sin x, \; q(x) = -x^3$
- $\frac{dy}{dx} + 5y = 2$ with $p(x) = 5, \; q(x) = 2$

We will assume that the functions $p(x)$ and $q(x)$ in (3) are continuous on a common interval, and we will look for a general solution that is valid on that interval. One method for doing this is based on the observation that if we define $\mu = \mu(x)$ by
$$\mu = e^{\int p(x)\,dx} \tag{4}$$
then
$$\frac{d\mu}{dx} = e^{\int p(x)\,dx} \cdot \frac{d}{dx}\left[\int p(x)\,dx\right] = \mu p(x)$$
Thus,
$$\frac{d}{dx}(\mu y) = \mu\frac{dy}{dx} + \frac{d\mu}{dx}y = \mu\frac{dy}{dx} + \mu p(x)y \tag{5}$$
If (3) is multiplied through by $\mu$, it becomes
$$\mu\frac{dy}{dx} + \mu p(x)y = \mu q(x)$$
Combining this with (5) we have
$$\frac{d}{dx}(\mu y) = \mu q(x) \tag{6}$$
This equation can be solved for $y$ by integrating both sides with respect to $x$ and then dividing through by $\mu$ to obtain
$$y = \frac{1}{\mu}\int \mu q(x)\,dx \tag{7}$$
which is a general solution of (3) on the interval. The function $\mu$ in (4) is called an **integrating factor** for (3), and this method for finding a general solution of (3) is called the **method of integrating factors**. Although one could simply memorize Formula (7), we recommend solving first-order linear equations by actually carrying out the steps used to derive this formula:

> ### The Method of Integrating Factors
> **Step 1.** Calculate the integrating factor
> $$\mu = e^{\int p(x)\,dx}$$
> Since any $\mu$ will suffice, we can take the constant of integration to be zero in this step.  
> **Step 2.** Multiply both sides of (3) by $\mu$ and express the result as
> $$\frac{d}{dx}(\mu y) = \mu q(x)$$
> **Step 3.** Integrate both sides of the equation obtained in Step 2 and then solve for $y$. Be sure to include a constant of integration in this step.

#### Example 1
Solve the differential equation
$$\frac{dy}{dx} - y = e^{2x}$$

*Solution.* Comparing the given equation to (3), we see that we have a first-order linear equation with $p(x) = -1$ and $q(x) = e^{2x}$. These coefficients are continuous on the interval $(-\infty, +\infty)$, so the method of integrating factors will produce a general solution on this interval. The first step is to compute the integrating factor. This yields
$$\mu = e^{\int p(x)\,dx} = e^{\int (-1)\,dx} = e^{-x}$$
Next we multiply both sides of the given equation by $\mu$ to obtain
$$e^{-x}\frac{dy}{dx} - e^{-x}y = e^{-x}e^{2x}$$
which we can rewrite as
$$\frac{d}{dx}[e^{-x}y] = e^x$$
Integrating both sides of this equation with respect to $x$ we obtain
$$e^{-x}y = e^x + C$$
Finally, solving for $y$ yields the general solution
$$y = e^{2x} + Ce^x$$

> *Note:* Confirm that the solution obtained in Example 1 agrees with that obtained by substituting the integrating factor into Formula (7).

A differential equation of the form
$$P(x)\frac{dy}{dx} + Q(x)y = R(x)$$
can be solved by dividing through by $P(x)$ to put the equation in the form of (3) and then applying the method of integrating factors. However, the resulting solution will only be valid on intervals where $p(x) = Q(x)/P(x)$ and $q(x) = R(x)/P(x)$ are both continuous.

#### Example 2
Solve the initial-value problem
$$x\frac{dy}{dx} - y = x, \quad y(1) = 2$$

*Solution.* This differential equation can be written in the form of (3) by dividing through by $x$. This yields
$$\frac{dy}{dx} - \frac{1}{x}y = 1 \tag{8}$$
where $q(x) = 1$ is continuous on $(-\infty, +\infty)$ and $p(x) = -1/x$ is continuous on $(-\infty, 0)$ and $(0, +\infty)$. Since we need $p(x)$ and $q(x)$ to be continuous on a common interval, and since our initial condition requires a solution for $x = 1$, we will find a general solution of (8) on the interval $(0, +\infty)$. On this interval we have $|x| = x$, so that
$$\int p(x)\,dx = -\int \frac{1}{x}\,dx = -\ln|x| = -\ln x \quad \text{(taking the constant of integration to be 0)}$$
Thus, an integrating factor that will produce a general solution on the interval $(0, +\infty)$ is
$$\mu = e^{\int p(x)\,dx} = e^{-\ln x} = e^{\ln(1/x)} = \frac{1}{x}$$
Multiplying both sides of Equation (8) by this integrating factor yields
$$\frac{1}{x}\frac{dy}{dx} - \frac{1}{x^2}y = \frac{1}{x}$$
or
$$\frac{d}{dx}\left[\frac{1}{x}y\right] = \frac{1}{x}$$
Therefore, on the interval $(0, +\infty)$,
$$\frac{1}{x}y = \int \frac{1}{x}\,dx = \ln x + C$$
from which it follows that
$$y = x\ln x + Cx \tag{9}$$
The initial condition $y(1) = 2$ requires that $y = 2$ if $x = 1$. Substituting these values into (9) and solving for $C$ yields $C = 2$ (verify), so the solution of the initial-value problem is
$$y = x\ln x + 2x$$

> It is not accidental that the initial-value problem in Example 2 has a unique solution. If the coefficients of (3) are continuous on an open interval that contains the point $x_0$, then for any $y_0$ there will be a unique solution of (3) on that interval that satisfies the initial condition $y(x_0) = y_0$ [Exercise 29(b)].

We conclude this section with some applications of first-order differential equations.

### MIXING PROBLEMS

In a typical mixing problem, a tank is filled to a specified level with a solution that contains a known amount of some soluble substance (say salt). The thoroughly stirred solution is allowed to drain from the tank at a known rate, and at the same time a solution with a known concentration of the soluble substance is added to the tank at a known rate that may or may not differ from the draining rate. As time progresses, the amount of the soluble substance in the tank will generally change, and the usual mixing problem seeks to determine the amount of the substance in the tank at a specified time. This type of problem serves as a model for many kinds of problems: discharge and filtration of pollutants in a river, injection and absorption of medication in the bloodstream, and migrations of species into and out of an ecological system, for example.

#### Example 3
At time $t = 0$, a tank contains $4\text{ lb}$ of salt dissolved in $100\text{ gal}$ of water. Suppose that brine containing $2\text{ lb}$ of salt per gallon of brine is allowed to enter the tank at a rate of $5\text{ gal/min}$ and that the mixed solution is drained from the tank at the same rate (Figure 8.4.1). Find the amount of salt in the tank after 10 minutes.

*Solution.* Let $y(t)$ be the amount of salt (in pounds) after $t$ minutes. We are given that $y(0) = 4$, and we want to find $y(10)$. We will begin by finding a differential equation that is satisfied by $y(t)$. To do this, observe that $dy/dt$, which is the rate at which the amount of salt in the tank changes with time, can be expressed as
$$\frac{dy}{dt} = \text{rate in} - \text{rate out} \tag{10}$$
where *rate in* is the rate at which salt enters the tank and *rate out* is the rate at which salt leaves the tank. But the rate at which salt enters the tank is
$$\text{rate in} = (2\text{ lb/gal}) \cdot (5\text{ gal/min}) = 10\text{ lb/min}$$
Since brine enters and drains from the tank at the same rate, the volume of brine in the tank stays constant at $100\text{ gal}$. Thus, after $t$ minutes have elapsed, the tank contains $y(t)\text{ lb}$ of salt per $100\text{ gal}$ of brine, and hence the rate at which salt leaves the tank at that instant is
$$\text{rate out} = \left(\frac{y(t)}{100}\text{ lb/gal}\right) \cdot (5\text{ gal/min}) = \frac{y(t)}{20}\text{ lb/min}$$
Therefore, (10) can be written as
$$\frac{dy}{dt} = 10 - \frac{y}{20} \quad \text{or} \quad \frac{dy}{dt} + \frac{y}{20} = 10$$
which is a first-order linear differential equation satisfied by $y(t)$. Since we are given that $y(0) = 4$, the function $y(t)$ can be obtained by solving the initial-value problem
$$\frac{dy}{dt} + \frac{y}{20} = 10, \quad y(0) = 4$$
The integrating factor for the differential equation is
$$\mu = e^{\int (1/20)\,dt} = e^{t/20}$$
If we multiply the differential equation through by $\mu$, then we obtain
$$\frac{d}{dt}(e^{t/20}y) = 10e^{t/20}$$
$$e^{t/20}y = \int 10e^{t/20}\,dt = 200e^{t/20} + C$$
$$y(t) = 200 + Ce^{-t/20} \tag{11}$$
The initial condition states that $y = 4$ when $t = 0$. Substituting these values into (11) and solving for $C$ yields $C = -196$ (verify), so
$$y(t) = 200 - 196e^{-t/20} \tag{12}$$
The graph of (12) is shown in Figure 8.4.2. At time $t = 10$ the amount of salt in the tank is
$$y(10) = 200 - 196e^{-0.5} \approx 81.1\text{ lb}$$

Notice that it follows from (11) that
$$\lim_{t \to +\infty} y(t) = 200$$
for all values of $C$, so regardless of the amount of salt that is present in the tank initially, the amount of salt in the tank will eventually stabilize at $200\text{ lb}$. This can also be seen geometrically from the slope field for the differential equation shown in Figure 8.4.3. This slope field suggests the following: If the amount of salt present in the tank is greater than $200\text{ lb}$ initially, then the amount of salt will decrease steadily over time toward a limiting value of $200\text{ lb}$; and if the amount of salt is less than $200\text{ lb}$ initially, then it will increase steadily toward a limiting value of $200\text{ lb}$. The slope field also suggests that if the amount present initially is exactly $200\text{ lb}$, then the amount of salt in the tank will stay constant at $200\text{ lb}$. This can also be seen from (11), since $C = 0$ in this case (verify).

> *Note:* The graph shown in Figure 8.4.2 suggests that $y(t) \to 200$ as $t \to +\infty$. This means that over an extended period of time the amount of salt in the tank tends toward $200\text{ lb}$. Give an informal physical argument to explain why this result is to be expected.

### A MODEL OF FREE-FALL MOTION RETARDED BY AIR RESISTANCE

In Section 4.7 we considered the free-fall model of an object moving along a vertical axis near the surface of the Earth. It was assumed in that model that there is no air resistance and that the only force acting on the object is the Earth's gravity. Our goal here is to find a model that takes air resistance into account. For this purpose we make the following assumptions:
- The object moves along a vertical $s$-axis whose origin is at the surface of the Earth and whose positive direction is up (Figure 4.7.7).
- At time $t = 0$ the height of the object is $s_0$ and the velocity is $v_0$.
- The only forces on the object are the force $F_G = -mg$ of the Earth's gravity acting down and the force $F_R$ of air resistance acting opposite to the direction of motion. The force $F_R$ is called the **drag force**.

In the case of free-fall motion retarded by air resistance, the net force acting on the object is
$$F_G + F_R = -mg + F_R$$
and the acceleration is $d^2s/dt^2$, so Newton's Second Law of Motion [Equation (5) of Section 5.6] implies that
$$-mg + F_R = m\frac{d^2s}{dt^2} \tag{13}$$

Experimentation has shown that the force $F_R$ of air resistance depends on the shape of the object and its speed—the greater the speed, the greater the drag force. There are many possible models for air resistance, but one of the most basic assumes that the drag force $F_R$ is proportional to the velocity of the object, that is,
$$F_R = -cv$$
where $c$ is a positive constant that depends on the object's shape and properties of the air.* (The minus sign ensures that the drag force is opposite to the direction of motion.) Substituting this in (13) and writing $d^2s/dt^2$ as $dv/dt$, we obtain
$$-mg - cv = m\frac{dv}{dt}$$
Dividing by $m$ and rearranging we obtain
$$\frac{dv}{dt} + \frac{c}{m}v = -g$$
which is a first-order linear differential equation in the unknown function $v = v(t)$ with $p(t) = c/m$ and $q(t) = -g$ [see (3)]. For a specific object, the coefficient $c$ can be determined experimentally, so we will assume that $m, g$, and $c$ are known constants. Thus, the velocity function $v = v(t)$ can be obtained by solving the initial-value problem
$$\frac{dv}{dt} + \frac{c}{m}v = -g, \quad v(0) = v_0 \tag{14}$$

Once the velocity function is found, the position function $s = s(t)$ can be obtained by solving the initial-value problem
$$\frac{ds}{dt} = v(t), \quad s(0) = s_0 \tag{15}$$

In Exercise 25 we will ask you to solve (14) and show that
$$v(t) = e^{-ct/m}\left(v_0 + \frac{mg}{c}\right) - \frac{mg}{c} \tag{16}$$
Note that
$$\lim_{t \to +\infty} v(t) = -\frac{mg}{c} \tag{17}$$
(verify). Thus, the speed $|v(t)|$ does not increase indefinitely, as in free fall; rather, because of the air resistance, it approaches a finite limiting speed $v_\tau$ given by
$$v_\tau = \left|-\frac{mg}{c}\right| = \frac{mg}{c} \tag{18}$$
This is called the **terminal speed** of the object, and (17) is called its **terminal velocity**.

> **REMARK** Intuition suggests that near the limiting velocity, the velocity $v(t)$ changes very slowly; that is, $dv/dt \approx 0$. Thus, it should not be surprising that the limiting velocity can be obtained informally from (14) by setting $dv/dt = 0$ in the differential equation and solving for $v$. This yields
> $$v = -\frac{mg}{c}$$
> which agrees with (17).

> \* Other common models assume that $F_R = -cv^2$ or, more generally, $F_R = -cv^p$ for some value of $p$.

---

### QUICK CHECK EXERCISES 8.4
*(See page 594 for answers.)*

1. Solve the first-order linear differential equation
   $$\frac{dy}{dx} + p(x)y = q(x)$$
   by completing the following steps:
   - **Step 1.** Calculate the integrating factor $\mu =$ \_\_\_\_.
   - **Step 2.** Multiply both sides of the equation by the integrating factor and express the result as
     $$\frac{d}{dx}[\quad] = \quad$$
   - **Step 3.** Integrate both sides of the equation obtained in Step 2 and solve for $y =$ \_\_\_\_.
2. An integrating factor for
   $$\frac{dy}{dx} + \frac{y}{x} = q(x)$$
   is \_\_\_\_.
3. At time $t = 0$, a tank contains $30\text{ oz}$ of salt dissolved in $60\text{ gal}$ of water. Then brine containing $5\text{ oz}$ of salt per gallon of brine is allowed to enter the tank at a rate of $3\text{ gal/min}$ and the mixed solution is drained from the tank at the same rate. Give an initial-value problem satisfied by the amount of salt $y(t)$ in the tank at time $t$. Do not solve the problem.

---

### EXERCISE SET 8.4

**1–6 Solve the differential equation by the method of integrating factors.**
1. $\frac{dy}{dx} + 4y = e^{-3x}$
2. $\frac{dy}{dx} + 2xy = x$
3. $y' + y = \cos(e^x)$
4. $2\frac{dy}{dx} + 4y = 1$
5. $(x^2 + 1)\frac{dy}{dx} + xy = 0$
6. $\frac{dy}{dx} + y + \frac{1}{1 - e^x} = 0$

**7–10 Solve the initial-value problem.**
7. $x\frac{dy}{dx} + y = x, \quad y(1) = 2$
8. $x\frac{dy}{dx} - y = x^2, \quad y(1) = -1$
9. $\frac{dy}{dx} - 2xy = 2x, \quad y(0) = 3$
10. $\frac{dy}{dt} + y = 2, \quad y(0) = 1$

**11–14 True–False Determine whether the statement is true or false. Explain your answer.**
11. If $y_1$ and $y_2$ are two solutions to a first-order linear differential equation, then $y = y_1 + y_2$ is also a solution.
12. If the first-order linear differential equation
    $$\frac{dy}{dx} + p(x)y = q(x)$$
    has a solution that is a constant function, then $q(x)$ is a constant multiple of $p(x)$.
13. In a mixing problem, we expect the concentration of the dissolved substance within the tank to approach a finite limit over time.
14. In our model for free-fall motion retarded by air resistance, the terminal velocity is proportional to the weight of the falling object.

15. A slope field for the differential equation $y' = 2y - x$ is shown in Figure Ex-15. In each part, sketch the graph of the solution that satisfies the initial condition.  
    (a) $y(1) = 1$  
    (b) $y(0) = -1$  
    (c) $y(-1) = 0$
16. Solve the initial-value problems in Exercise 15, and use a graphing utility to confirm that the integral curves for these solutions are consistent with the sketches you obtained from the slope field.

#### FOCUS ON CONCEPTS
17. Use the slope field in Exercise 15 to make a conjecture about the effect of $y_0$ on the behavior of the solution of the initial-value problem $y' = 2y - x, \; y(0) = y_0$ as $x \to +\infty$, and check your conjecture by examining the solution of the initial-value problem.
18. Consider the slope field in Exercise 15.  
    (a) Use Euler's Method with $\Delta x = 0.1$ to estimate $y(1/2)$ for the solution that satisfies the initial condition $y(0) = 1$.  
    (b) Would you conjecture your answer in part (a) to be greater than or less than the actual value of $y(1/2)$? Explain.  
    (c) Check your conjecture in part (b) by finding the exact value of $y(1/2)$.
19. (a) Use Euler's Method with a step size of $\Delta x = 0.2$ to approximate the solution of the initial-value problem
    $$y' = x + y, \quad y(0) = 1$$
    over the interval $0 \le x \le 1$.  
    (b) Solve the initial-value problem exactly, and calculate the error and the percentage error in each of the approximations in part (a).  
    (c) Sketch the exact solution and the approximate solution together.
20. It was stated at the end of Section 8.3 that reducing the step size in Euler's Method by half reduces the error in each approximation by about half. Confirm that the error in $y(1)$ is reduced by about half if a step size of $\Delta x = 0.1$ is used in Exercise 19.
21. At time $t = 0$, a tank contains $25\text{ oz}$ of salt dissolved in $50\text{ gal}$ of water. Then brine containing $4\text{ oz}$ of salt per gallon of brine is allowed to enter the tank at a rate of $2\text{ gal/min}$ and the mixed solution is drained from the tank at the same rate.  
    (a) How much salt is in the tank at an arbitrary time $t$?  
    (b) How much salt is in the tank after $25\text{ min}$?
22. A tank initially contains $200\text{ gal}$ of pure water. Then at time $t = 0$ brine containing $5\text{ lb}$ of salt per gallon of brine is allowed to enter the tank at a rate of $20\text{ gal/min}$ and the mixed solution is drained from the tank at the same rate.  
    (a) How much salt is in the tank at an arbitrary time $t$?  
    (b) How much salt is in the tank after $30\text{ min}$?
23. A tank with a $1000\text{ gal}$ capacity initially contains $500\text{ gal}$ of water that is polluted with $50\text{ lb}$ of particulate matter. At time $t = 0$, pure water is added at a rate of $20\text{ gal/min}$ and the mixed solution is drained off at a rate of $10\text{ gal/min}$. How much particulate matter is in the tank when it reaches the point of overflowing?
24. The water in a polluted lake initially contains $1\text{ lb}$ of mercury salts per $100,000\text{ gal}$ of water. The lake is circular with diameter $30\text{ m}$ and uniform depth $3\text{ m}$. Polluted water is pumped from the lake at a rate of $1000\text{ gal/h}$ and is replaced with fresh water at the same rate. Construct a table that shows the amount of mercury in the lake (in lb) at the end of each hour over a 12-hour period. Discuss any assumptions you made. [*Note:* Use $1\text{ m}^3 = 264\text{ gal}$.]
25. (a) Use the method of integrating factors to derive solution (16) to the initial-value problem (14). [*Note:* Keep in mind that $c, m$, and $g$ are constants.]  
    (b) Show that (16) can be expressed in terms of the terminal speed (18) as
    $$v(t) = e^{-gt/v_\tau}(v_0 + v_\tau) - v_\tau$$
    (c) Show that if $s(0) = s_0$, then the position function of the object can be expressed as
    $$s(t) = s_0 - v_\tau t + \frac{v_\tau}{g}(v_0 + v_\tau)(1 - e^{-gt/v_\tau})$$
26. Suppose a fully equipped skydiver weighing $240\text{ lb}$ has a terminal speed of $120\text{ ft/s}$ with a closed parachute and $24\text{ ft/s}$ with an open parachute. Suppose further that this skydiver is dropped from an airplane at an altitude of $10,000\text{ ft}$, falls for $25\text{ s}$ with a closed parachute, and then falls the rest of the way with an open parachute.  
    (a) Assuming that the skydiver's initial vertical velocity is zero, use Exercise 25 to find the skydiver's vertical velocity and height at the time the parachute opens. [*Note:* Take $g = 32\text{ ft/s}^2$.]  
    (b) Use a calculating utility to find a numerical solution for the total time that the skydiver is in the air.
27. The accompanying figure (Figure Ex-27) is a schematic diagram of a basic $RL$ series electrical circuit that contains a power source with a time-dependent voltage of $V(t)$ volts (V), a resistor with a constant resistance of $R$ ohms ($\Omega$), and an inductor with a constant inductance of $L$ henrys (H). If you don't know anything about electrical circuits, don't worry; all you need to know is that electrical theory states that a current of $I(t)$ amperes (A) flows through the circuit where $I(t)$ satisfies the differential equation
    $$L\frac{dI}{dt} + RI = V(t)$$
    (a) Find $I(t)$ if $R = 10\,\Omega, \; L = 5\text{ H}, \; V$ is a constant $20\text{ V}$, and $I(0) = 0\text{ A}$.  
    (b) What happens to the current over a long period of time?
28. Find $I(t)$ for the electrical circuit in Exercise 27 if $R = 6\,\Omega, \; L = 3\text{ H}, \; V(t) = 3\sin t\text{ V}$, and $I(0) = 15\text{ A}$.

#### FOCUS ON CONCEPTS
29. (a) Prove that any function $y = y(x)$ defined by Equation (7) will be a solution to (3).  
    (b) Consider the initial-value problem
    $$\frac{dy}{dx} + p(x)y = q(x), \quad y(x_0) = y_0$$
    where the functions $p(x)$ and $q(x)$ are both continuous on some open interval. Using the general solution for a first-order linear equation, prove that this initial-value problem has a unique solution on the interval.
30. (a) Prove that solutions need not be unique for nonlinear initial-value problems by finding two solutions to
    $$y\frac{dy}{dx} = x, \quad y(0) = 0$$
    (b) Prove that solutions need not exist for nonlinear initial-value problems by showing that there is no solution for
    $$y\frac{dy}{dx} = -x, \quad y(0) = 0$$
31. **Writing.** Explain why the quantity $\mu$ in the Method of Integrating Factors is called an "integrating factor" and explain its role in this method.
32. **Writing.** Suppose that a given first-order differential equation can be solved both by the method of integrating factors and by separation of variables. Discuss the advantages and disadvantages of each method.

---

### QUICK CHECK ANSWERS 8.4
1. Step 1: $e^{\int p(x)\,dx}$; Step 2: $\mu y, \; \mu q(x)$; Step 3: $\frac{1}{\mu}\int \mu q(x)\,dx$  
2. $x$  
3. $\frac{dy}{dt} + \frac{y}{20} = 15, \quad y(0) = 30$

---

## CHAPTER 8 REVIEW EXERCISES

1. Classify the following first-order differential equations as separable, linear, both, or neither.  
   (a) $\frac{dy}{dx} - 3y = \sin x$  
   (b) $\frac{dy}{dx} + xy = x$  
   (c) $y\frac{dy}{dx} - x = 1$  
   (d) $\frac{dy}{dx} + xy^2 = \sin(xy)$
2. Which of the given differential equations are separable?  
   (a) $\frac{dy}{dx} = f(x)g(y)$  
   (b) $\frac{dy}{dx} = \frac{f(x)}{g(y)}$  
   (c) $\frac{dy}{dx} = f(x) + g(y)$  
   (d) $\frac{dy}{dx} = \sqrt{f(x)g(y)}$

**3–5 Solve the differential equation by the method of separation of variables.**
3. $\frac{dy}{dx} = (1+y^2)x^2$
4. $3\tan y - \frac{dy}{dx}\sec x = 0$
5. $(1+y^2)y' = e^x y$

**6–8 Solve the initial-value problem by the method of separation of variables.**
6. $y' = 1+y^2, \quad y(0) = 1$
7. $y' = \frac{y^5}{x(1+y^4)}, \quad y(1) = 1$
8. $y' = 4y^2\sec^2 2x, \quad y(\pi/8) = 1$

9. Sketch the integral curve of $y' = -2xy^2$ that passes through the point $(0, 1)$.
10. Sketch the integral curve of $2yy' = 1$ that passes through the point $(0, 1)$ and the integral curve that passes through the point $(0, -1)$.
11. Sketch the slope field for $y' = xy/8$ at the 25 gridpoints $(x, y)$, where $x = 0, 1, \dots, 4$ and $y = 0, 1, \dots, 4$.
12. Solve the differential equation $y' = xy/8$, and find a family of integral curves for the slope field in Exercise 11.

**13–14 Use Euler's Method with the given step size $\Delta x$ to approximate the solution of the initial-value problem over the stated interval. Present your answer as a table and as a graph.**
13. $dy/dx = \sqrt{y}, \quad y(0) = 1, \quad 0 \le x \le 4, \quad \Delta x = 0.5$
14. $dy/dx = \sin y, \quad y(0) = 1, \quad 0 \le x \le 2, \quad \Delta x = 0.5$

15. Consider the initial-value problem
    $$y' = \cos 2\pi t, \quad y(0) = 1$$
    Use Euler's Method with five steps to approximate $y(1)$.
16. Cloth found in an Egyptian pyramid contains 78.5% of its original carbon-14. Estimate the age of the cloth.
17. In each part, find an exponential growth model $y = y_0 e^{kt}$ that satisfies the stated conditions.  
    (a) $y_0 = 2$; doubling time $T = 5$  
    (b) $y(0) = 5$; growth rate 1.5%  
    (c) $y(1) = 1; \quad y(10) = 100$  
    (d) $y(1) = 1$; doubling time $T = 5$
18. Suppose that an initial population of 5000 bacteria grows exponentially at a rate of 1% per hour and that $y = y(t)$ is the number of bacteria present after $t$ hours.  
    (a) Find an initial-value problem whose solution is $y(t)$.  
    (b) Find a formula for $y(t)$.  
    (c) What is the doubling time for the population?  
    (d) How long does it take for the population of bacteria to reach 30,000?

**19–20 Solve the differential equation by the method of integrating factors.**
19. $\frac{dy}{dx} + 3y = e^{-2x}$
20. $\frac{dy}{dx} + y - \frac{1}{1+e^x} = 0$

**21–23 Solve the initial-value problem by the method of integrating factors.**
21. $y' - xy = x, \quad y(0) = 3$
22. $xy' + 2y = 4x^2, \quad y(1) = 2$
23. $y'\cosh x + y\sinh x = \cosh^2 x, \quad y(0) = 2$

24. [CAS] (a) Solve the initial-value problem
    $$y' - y = x\sin 3x, \quad y(0) = 1$$
    by the method of integrating factors, using a CAS to perform any difficult integrations.  
    (b) Use the CAS to solve the initial-value problem directly, and confirm that the answer is consistent with that obtained in part (a).  
    (c) Graph the solution.
25. A tank contains $1000\text{ gal}$ of fresh water. At time $t = 0\text{ min}$, brine containing $5\text{ oz}$ of salt per gallon of brine is poured into the tank at a rate of $10\text{ gal/min}$, and the mixed solution is drained from the tank at the same rate. After $15\text{ min}$ that process is stopped and fresh water is poured into the tank at the rate of $5\text{ gal/min}$, and the mixed solution is drained from the tank at the same rate. Find the amount of salt in the tank at time $t = 30\text{ min}$.
26. Suppose that a room containing $1200\text{ ft}^3$ of air is free of carbon monoxide. At time $t = 0$ cigarette smoke containing 4% carbon monoxide is introduced at the rate of $0.1\text{ ft}^3/\text{min}$, and the well-circulated mixture is vented from the room at the same rate.  
    (a) Find a formula for the percentage of carbon monoxide in the room at time $t$.  
    (b) Extended exposure to air containing 0.012% carbon monoxide is considered dangerous. How long will it take to reach this level?  
    *Source:* This is based on a problem from William E. Boyce and Richard C. DiPrima, *Elementary Differential Equations*, 7th ed., John Wiley & Sons, New York, 2001.

---

## CHAPTER 8 MAKING CONNECTIONS

1. Consider the first-order differential equation
   $$\frac{dy}{dx} + py = q$$
   where $p$ and $q$ are constants. If $y = y(x)$ is a solution to this equation, define $u = u(x) = q - py(x)$.  
   (a) Without solving the differential equation, show that $u$ grows exponentially as a function of $x$ if $p < 0$, and decays exponentially as a function of $x$ if $0 < p$.  
   (b) Use the result of part (a) and Equations (13–14) of Section 8.2 to solve the initial-value problem
   $$\frac{dy}{dx} + 2y = 4, \quad y(0) = -1$$

2. Consider a differential equation of the form
   $$\frac{dy}{dx} = f(ax + by + c)$$
   where $f$ is a function of a single variable. If $y = y(x)$ is a solution to this equation, define $u = u(x) = ax + by(x) + c$.  
   (a) Find a separable differential equation that is satisfied by the function $u$.  
   (b) Use your answer to part (a) to solve
   $$\frac{dy}{dx} = \frac{1}{x+y}$$

3. A first-order differential equation is **homogeneous** if it can be written in the form
   $$\frac{dy}{dx} = f\left(\frac{y}{x}\right) \quad \text{for } x \neq 0$$
   where $f$ is a function of a single variable. If $y = y(x)$ is a solution to a first-order homogeneous differential equation, define $u = u(x) = y(x)/x$.  
   (a) Find a separable differential equation that is satisfied by the function $u$.  
   (b) Use your answer to part (a) to solve
   $$\frac{dy}{dx} = \frac{x - y}{x + y}$$

4. A first-order differential equation is called a **Bernoulli equation** if it can be written in the form
   $$\frac{dy}{dx} + p(x)y = q(x)y^n \quad \text{for } n \neq 0, 1$$
   If $y = y(x)$ is a solution to a Bernoulli equation, define $u = u(x) = [y(x)]^{1-n}$.  
   (a) Find a first-order linear differential equation that is satisfied by $u$.  
   (b) Use your answer to part (a) to solve the initial-value problem
   $$x\frac{dy}{dx} - y = -2xy^2, \quad y(1) = \frac{1}{2}$$
