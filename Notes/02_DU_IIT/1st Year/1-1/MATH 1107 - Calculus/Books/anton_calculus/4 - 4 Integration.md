# CHAPTER 4: INTEGRATION

> If a dragster moves with varying velocity over a certain time interval, it is possible to find the distance it travels during that time interval using techniques of calculus.

In this chapter we will begin with an overview of the problem of finding areas—we will discuss what the term "area" means, and we will outline two approaches to defining and calculating areas. Following this overview, we will discuss the Fundamental Theorem of Calculus, which is the theorem that relates the problems of finding tangent lines and areas, and we will discuss techniques for calculating areas. We will then use the ideas in this chapter to define the average value of a function, to continue our study of rectilinear motion, and to examine some consequences of the chain rule in integral calculus.

---

## 4.1 AN OVERVIEW OF THE AREA PROBLEM

In this introductory section we will consider the problem of calculating areas of plane regions with curvilinear boundaries. All of the results in this section will be reexamined in more detail later in this chapter. Our purpose here is simply to introduce and motivate the fundamental concepts.

### THE AREA PROBLEM

Formulas for the areas of polygons, such as squares, rectangles, triangles, and trapezoids, were well known in many early civilizations. However, the problem of finding formulas for regions with curved boundaries (a circle being the simplest example) caused difficulties for early mathematicians.

The first real progress in dealing with the general area problem was made by the Greek mathematician **Archimedes**, who obtained areas of regions bounded by circular arcs, parabolas, spirals, and various other curves using an ingenious procedure that was later called the **method of exhaustion**. The method, when applied to a circle, consists of inscribing a succession of regular polygons in the circle and allowing the number of sides to increase indefinitely (Figure 4.1.1). As the number of sides increases, the polygons tend to "exhaust" the region inside the circle, and the areas of the polygons become better and better approximations of the exact area of the circle.

To see how this works numerically, let $A(n)$ denote the area of a regular $n$-sided polygon inscribed in a circle of radius 1. Table 4.1.1 shows the values of $A(n)$ for various choices of $n$. Note that for large values of $n$ the area $A(n)$ appears to be close to $\pi$ (square units), as one would expect. This suggests that for a circle of radius 1, the method of exhaustion is equivalent to an equation of the form
$$\lim_{n \to \infty} A(n) = \pi$$

#### Table 4.1.1: Values of $A(n)$
| $n$ | $A(n)$ |
| :---: | :---: |
| 100 | 3.13952597647 |
| 200 | 3.14107590781 |
| 300 | 3.14136298250 |
| 400 | 3.14146346236 |
| 500 | 3.14150997084 |
| 1000 | 3.14157198278 |
| 2000 | 3.14158748588 |
| 3000 | 3.14159035683 |
| 4000 | 3.14159136166 |
| 5000 | 3.14159182676 |
| 10,000 | 3.14159244688 |

> **Archimedes (287 B.C.–212 B.C.)**  
> Greek mathematician and scientist. Born in Syracuse, Sicily, Archimedes was the son of the astronomer Pheidias and possibly related to Hieron II, king of Syracuse. Most of the facts about his life come from the Roman biographer, Plutarch, who inserted a few tantalizing pages about him in the massive biography of the Roman soldier, Marcellus. In the words of one writer, "the account of Archimedes is slipped like a tissue-thin shaving of ham in a bull-choking sandwich."  
> Archimedes ranks with Newton and Gauss as one of the three greatest mathematicians who ever lived, and he is certainly the greatest mathematician of antiquity. His mathematical work is so modern in spirit and technique that it is barely distinguishable from that of a seventeenth-century mathematician, yet it was all done without benefit of algebra or a convenient number system. Among his mathematical achievements, Archimedes developed a general method (exhaustion) for finding areas and volumes, and he used the method to find areas bounded by parabolas and spirals and to find volumes of cylinders, paraboloids, and segments of spheres. He gave a procedure for approximating $\pi$ and bounded its value between $3\frac{10}{71}$ and $3\frac{1}{7}$. In spite of the limitations of the Greek numbering system, he devised methods for finding square roots and invented a method based on the Greek myriad (10,000) for representing numbers as large as 1 followed by 80 million billion zeros.  
> Of all his mathematical work, Archimedes was most proud of his discovery of a method for finding the volume of a sphere—he showed that the volume of a sphere is two-thirds the volume of the smallest cylinder that can contain it. At his request, the figure of a sphere and cylinder was engraved on his tombstone.  
> In addition to mathematics, Archimedes worked extensively in mechanics and hydrostatics. Nearly every schoolchild knows Archimedes as the absent-minded scientist who, on realizing that a floating object displaces its weight of liquid, leaped from his bath and ran naked through the streets of Syracuse shouting, "Eureka, Eureka!"—(meaning, "I have found it!"). Archimedes actually created the discipline of hydrostatics and used it to find equilibrium positions for various floating bodies. He laid down the fundamental postulates of mechanics, discovered the laws of levers, and calculated centers of gravity for various flat surfaces and solids. In the excitement of discovering the mathematical laws of the lever, he is said to have declared, "Give me a place to stand and I will move the earth."  
> Although Archimedes was apparently more interested in pure mathematics than its applications, he was an engineering genius. During the second Punic war, when Syracuse was attacked by the Roman fleet under the command of Marcellus, it was reported by Plutarch that Archimedes' military inventions held the fleet at bay for three years. He invented super catapults that showered the Romans with rocks weighing a quarter ton or more, and fearsome mechanical devices with iron "beaks and claws" that reached over the city walls, grasped the ships, and spun them against the rocks. After the first repulse, Marcellus called Archimedes a "geometrical Briareus (a hundred-armed mythological monster) who uses our ships like cups to ladle water from the sea."  
> Eventually the Roman army was victorious and contrary to Marcellus' specific orders the 75-year-old Archimedes was killed by a Roman soldier. According to one report of the incident, the soldier cast a shadow across the sand in which Archimedes was working on a mathematical problem. When the annoyed Archimedes yelled, "Don't disturb my circles," the soldier flew into a rage and cut the old man down.  
> Although there is no known likeness or statue of this great man, nine works of Archimedes have survived to the present day. Especially important is his treatise, *The Method of Mechanical Theorems*, which was part of a palimpsest found in Constantinople in 1906. In this treatise Archimedes explains how he made some of his discoveries, using reasoning that anticipated ideas of the integral calculus. Thought to be lost, the Archimedes palimpsest later resurfaced in 1998, when it was purchased by an anonymous private collector for two million dollars.

Since Greek mathematicians were suspicious of the concept of "infinity," they avoided its use in mathematical arguments. As a result, computation of area using the method of exhaustion was a very cumbersome procedure. It remained for Newton and Leibniz to obtain a general method for finding areas that explicitly used the notion of a limit. We will discuss their method in the context of the following problem.

> **4.1.1 THE AREA PROBLEM**  
> Given a function $f$ that is continuous and nonnegative on an interval $[a, b]$, find the area between the graph of $f$ and the interval $[a, b]$ on the $x$-axis (Figure 4.1.2).

---

### THE RECTANGLE METHOD FOR FINDING AREAS

One approach to the area problem is to use Archimedes' method of exhaustion in the following way:

* Divide the interval $[a, b]$ into $n$ equal subintervals, and over each subinterval construct a rectangle that extends from the $x$-axis to any point on the curve $y = f(x)$ that is above the subinterval; the particular point does not matter—it can be above the center, above an endpoint, or above any other point in the subinterval (Figure 4.1.3).
* For each $n$, the total area of the rectangles can be viewed as an approximation to the exact area under the curve over the interval $[a, b]$. Moreover, it is evident intuitively that as $n$ increases these approximations will get better and better and will approach the exact area as a limit (Figure 4.1.4). That is, if $A$ denotes the exact area under the curve and $A_n$ denotes the approximation to $A$ using $n$ rectangles, then
  $$A = \lim_{n \to +\infty} A_n$$
  We will call this the **rectangle method** for computing $A$.

To illustrate this idea, we will use the rectangle method to approximate the area under the curve $y = x^2$ over the interval $[0, 1]$ (Figure 4.1.5). We will begin by dividing the interval $[0, 1]$ into $n$ equal subintervals, from which it follows that each subinterval has length $1/n$; the endpoints of the subintervals occur at
$$0, \frac{1}{n}, \frac{2}{n}, \frac{3}{n}, \dots, \frac{n-1}{n}, 1$$
We want to construct a rectangle over each of these subintervals whose height is the value of the function $f(x) = x^2$ at some point in the subinterval. To be specific, let us use the right endpoints, in which case the heights of our rectangles will be
$$\left(\frac{1}{n}\right)^2, \left(\frac{2}{n}\right)^2, \left(\frac{3}{n}\right)^2, \dots, 1^2$$
and since each rectangle has a base of width $1/n$, the total area $A_n$ of the $n$ rectangles will be
$$A_n = \left[\left(\frac{1}{n}\right)^2 + \left(\frac{2}{n}\right)^2 + \left(\frac{3}{n}\right)^2 + \dots + 1^2\right]\left(\frac{1}{n}\right) \tag{1}$$

For example, if $n = 4$, then the total area of the four approximating rectangles would be
$$A_4 = \left[\left(\frac{1}{4}\right)^2 + \left(\frac{2}{4}\right)^2 + \left(\frac{3}{4}\right)^2 + 1^2\right]\left(\frac{1}{4}\right) = \frac{15}{32} = 0.46875$$

#### Table 4.1.2: Approximations $A_n$ for $y = x^2$ on $[0, 1]$
| $n$ | $A_n$ |
| :---: | :---: |
| 4 | 0.468750 |
| 10 | 0.385000 |
| 100 | 0.338350 |
| 1000 | 0.333834 |
| 10,000 | 0.333383 |
| 100,000 | 0.333338 |

These computations suggest that the exact area is close to $\frac{1}{3}$. Later in this chapter we will prove that this area is exactly $\frac{1}{3}$ by showing that $\lim_{n \to \infty} A_n = \frac{1}{3}$.

---

### THE ANTIDERIVATIVE METHOD FOR FINDING AREAS

Although the rectangle method is appealing intuitively, the limits that result can only be evaluated in certain cases. For this reason, progress on the area problem remained at a rudimentary level until the latter part of the seventeenth century when Isaac Newton and Gottfried Leibniz independently discovered a fundamental relationship between areas and derivatives. Briefly stated, they showed that if $f$ is a nonnegative continuous function on the interval $[a, b]$, and if $A(x)$ denotes the area under the graph of $f$ over the interval $[a, x]$, where $x$ is any point in the interval $[a, b]$ (Figure 4.1.7), then
$$A'(x) = f(x) \tag{2}$$

#### Example 1
For each of the functions $f$, find the area $A(x)$ between the graph of $f$ and the interval $[a, x] = [-1, x]$, and find the derivative $A'(x)$ of this area function.  
(a) $f(x) = 2$  
(b) $f(x) = x + 1$  
(c) $f(x) = 2x + 3$

**Solution (a).** $A(x) = 2(x - (-1)) = 2(x + 1) = 2x + 2$ is the area of a rectangle of height 2 and base $x + 1$. For this area function,
$$A'(x) = 2 = f(x)$$

**Solution (b).** $A(x) = \frac{1}{2}(x + 1)(x + 1) = \frac{x^2}{2} + x + \frac{1}{2}$ is the area of an isosceles right triangle with base and height equal to $x + 1$. For this area function,
$$A'(x) = x + 1 = f(x)$$

**Solution (c).** Recall that the formula for the area of a trapezoid is $A = \frac{1}{2}(b + b')h$, where $b$ and $b'$ denote the lengths of the parallel sides of the trapezoid, and the altitude $h$ denotes the distance between the parallel sides. From Figure 4.1.8c:
$$A(x) = \frac{1}{2}((2x + 3) + 1)(x - (-1)) = x^2 + 3x + 2$$
is the area of a trapezoid with parallel sides of lengths 1 and $2x + 3$ and with altitude $x - (-1) = x + 1$. For this area function,
$$A'(x) = 2x + 3 = f(x)$$

Formula (2) is important because it relates the area function $A$ and the region-bounding function $f$. Although a formula for $A(x)$ may be difficult to obtain directly, its derivative, $f(x)$, is given. If a formula for $A(x)$ can be recovered from the given formula for $A'(x)$, then the area under the graph of $f$ over the interval $[a, b]$ can be obtained by computing $A(b)$.

The process of finding a function from its derivative is called **antidifferentiation**, and a procedure for finding areas via antidifferentiation is called the **antiderivative method**. To illustrate this method, let us revisit the problem of finding the area under $y = x^2$ over $[0, 1]$.

#### Example 2
Use the antiderivative method to find the area under the graph of $y = x^2$ over the interval $[0, 1]$.

**Solution.** Let $x$ be any point in the interval $[0, 1]$, and let $A(x)$ denote the area under the graph of $f(x) = x^2$ over the interval $[0, x]$. It follows from (2) that
$$A'(x) = x^2 \tag{3}$$
To find $A(x)$ we must look for a function whose derivative is $x^2$. By guessing, we see that one such function is $\frac{1}{3}x^3$, so by Theorem 3.8.3
$$A(x) = \frac{1}{3}x^3 + C \tag{4}$$
for some real constant $C$. We can determine the specific value for $C$ by considering the case where $x = 0$. In this case (4) implies that $A(0) = C$. But if $x = 0$, then the interval $[0, x]$ reduces to a single point. If we agree that the area above a single point should be taken as zero, then $A(0) = 0$ and this implies that $C = 0$. Thus, it follows from (4) that
$$A(x) = \frac{1}{3}x^3$$
is the area function we are seeking. This implies that the area under the graph of $y = x^2$ over the interval $[0, 1]$ is
$$A(1) = \frac{1}{3}(1^3) = \frac{1}{3}$$
This is consistent with the result that we previously obtained numerically.

---

### THE RECTANGLE METHOD AND THE ANTIDERIVATIVE METHOD COMPARED

The rectangle method and the antiderivative method provide two very different approaches to the area problem, each of which is important. The antiderivative method is usually the more efficient way to compute areas, but it is the rectangle method that is used to formally define the notion of area, thereby allowing us to prove mathematical results about areas. The underlying idea of the rectangle approach is also important because it can be adapted readily to such diverse problems as finding the volume of a solid, the length of a curve, the mass of an object, and the work done in pumping water out of a tank, to name a few.

---

### QUICK CHECK EXERCISES 4.1
*(See page 271 for answers.)*

1. Let $R$ denote the region below the graph of $f(x) = \sqrt{1 - x^2}$ and above the interval $[-1, 1]$.
   (a) Use a geometric argument to find the area of $R$.
   (b) What estimate results if the area of $R$ is approximated by the total area within the rectangles of the accompanying figure?
2. Suppose that when the area $A$ between the graph of a function $y = f(x)$ and an interval $[a, b]$ is approximated by the areas of $n$ rectangles, the total area of the rectangles is $A_n = 2 + (2/n)$, $n = 1, 2, \dots$. Then, $A = \underline{\hspace{1cm}}$.
3. The area under the graph of $y = x^2$ over the interval $[0, 3]$ is $\underline{\hspace{1cm}}$.
4. Find a formula for the area $A(x)$ between the graph of the function $f(x) = x$ and the interval $[0, x]$, and verify that $A'(x) = f(x)$.
5. The area under the graph of $y = f(x)$ over the interval $[0, x]$ is $A(x) = x + \sin x$. It follows that $f(x) = \underline{\hspace{1cm}}$.

#### QUICK CHECK ANSWERS 4.1
1. (a) $\frac{\pi}{2}$ (b) $1 + \frac{\sqrt{3}}{2}$  
2. $2$  
3. $9$  
4. $A(x) = \frac{x^2}{2}$; $A'(x) = \frac{2x}{2} = x = f(x)$  
5. $\cos x + 1$

---

### EXERCISE SET 4.1

**1–8 Estimate the area between the graph of the function $f$ and the interval $[a, b]$. Use an approximation scheme with $n$ rectangles similar to our treatment of $f(x) = x^2$ in this section. If your calculating utility will perform automatic summations, estimate the specified area using $n = 10, 50,$ and $100$ rectangles. Otherwise, estimate this area using $n = 2, 5,$ and $10$ rectangles.**
1. $f(x) = \sqrt{x}$; $[a, b] = [0, 1]$
2. $f(x) = \frac{1}{x + 1}$; $[a, b] = [0, 1]$
3. $f(x) = \sin x$; $[a, b] = [0, \pi]$
4. $f(x) = \cos x$; $[a, b] = [0, \pi/2]$
5. $f(x) = \frac{1}{x}$; $[a, b] = [1, 2]$
6. $f(x) = \cos x$; $[a, b] = [-\pi/2, \pi/2]$
7. $f(x) = \sqrt{1 - x^2}$; $[a, b] = [0, 1]$
8. $f(x) = \sqrt{1 - x^2}$; $[a, b] = [-1, 1]$

**9–14 Graph each function over the specified interval. Then use simple area formulas from geometry to find the area function $A(x)$ that gives the area between the graph of the specified function $f$ and the interval $[a, x]$. Confirm that $A'(x) = f(x)$ in every case.**
9. $f(x) = 3$; $[a, x] = [1, x]$
10. $f(x) = 5$; $[a, x] = [2, x]$
11. $f(x) = 2x + 2$; $[a, x] = [0, x]$
12. $f(x) = 3x - 3$; $[a, x] = [1, x]$
13. $f(x) = 2x + 2$; $[a, x] = [1, x]$
14. $f(x) = 3x - 3$; $[a, x] = [2, x]$

**15–18 True–False Determine whether the statement is true or false. Explain your answer.**
15. If $A(n)$ denotes the area of a regular $n$-sided polygon inscribed in a circle of radius 2, then $\lim_{n \to +\infty} A(n) = 2\pi$.
16. If the area under the curve $y = x^2$ over an interval is approximated by the total area of a collection of rectangles, the approximation will be too large.
17. If $A(x)$ is the area under the graph of a nonnegative continuous function $f$ over an interval $[a, x]$, then $A'(x) = f(x)$.
18. If $A(x)$ is the area under the graph of a nonnegative continuous function $f$ over an interval $[a, x]$, then $A(x)$ will be a continuous function.

**FOCUS ON CONCEPTS**
19. Explain how to use the formula for $A(x)$ found in the solution to Example 2 to determine the area between the graph of $y = x^2$ and the interval $[3, 6]$.
20. Repeat Exercise 19 for the interval $[-3, 9]$.
21. Let $A$ denote the area between the graph of $f(x) = \sqrt{x}$ and the interval $[0, 1]$, and let $B$ denote the area between the graph of $f(x) = x^2$ and the interval $[0, 1]$. Explain geometrically why $A + B = 1$.
22. Let $A$ denote the area between the graph of $f(x) = 1/x$ and the interval $[1, 2]$, and let $B$ denote the area between the graph of $f$ and the interval $[1/2, 1]$. Explain geometrically why $A = B$.
23. The area $A(x)$ under the graph of $f$ and over the interval $[a, x]$ is given: $A(x) = x^2 - 4$. Find the function $f$ and the value of $a$.
24. The area $A(x)$ under the graph of $f$ and over the interval $[a, x]$ is given: $A(x) = x^2 - x$. Find the function $f$ and the value of $a$.
25. **Writing.** Compare and contrast the rectangle method and the antiderivative method.
26. **Writing.** Suppose that $f$ is a nonnegative continuous function on an interval $[a, b]$ and that $g(x) = f(x) + C$, where $C$ is a positive constant. What will be the area of the region between the graphs of $f$ and $g$?

---

## 4.2 THE INDEFINITE INTEGRAL

In the last section we saw how antidifferentiation could be used to find exact areas. In this section we will develop some fundamental results about antidifferentiation.

### ANTIDERIVATIVES

> **4.2.1 DEFINITION**  
> A function $F$ is called an **antiderivative** of a function $f$ on a given open interval if $F'(x) = f(x)$ for all $x$ in the interval.

For example, the function $F(x) = \frac{1}{3}x^3$ is an antiderivative of $f(x) = x^2$ on the interval $(-\infty, +\infty)$ because for each $x$ in this interval
$$F'(x) = \frac{d}{dx}\left[\frac{1}{3}x^3\right] = x^2 = f(x)$$
However, $F(x) = \frac{1}{3}x^3$ is not the only antiderivative of $f$ on this interval. If we add any constant $C$ to $\frac{1}{3}x^3$, then the function $G(x) = \frac{1}{3}x^3 + C$ is also an antiderivative of $f$ on $(-\infty, +\infty)$, since
$$G'(x) = \frac{d}{dx}\left[\frac{1}{3}x^3 + C\right] = x^2 + 0 = f(x)$$
In general, once any single antiderivative is known, other antiderivatives can be obtained by adding constants to the known antiderivative. Thus,
$$\frac{1}{3}x^3, \quad \frac{1}{3}x^3 + 2, \quad \frac{1}{3}x^3 - 5, \quad \frac{1}{3}x^3 + \sqrt{2}$$
are all antiderivatives of $f(x) = x^2$.

> **4.2.2 THEOREM**  
> If $F(x)$ is any antiderivative of $f(x)$ on an open interval, then for any constant $C$ the function $F(x) + C$ is also an antiderivative on that interval. Moreover, each antiderivative of $f(x)$ on the interval can be expressed in the form $F(x) + C$ by choosing the constant $C$ appropriately.

### THE INDEFINITE INTEGRAL

The process of finding antiderivatives is called **antidifferentiation** or **integration**. Thus, if
$$\frac{d}{dx}[F(x)] = f(x) \tag{1}$$
then integrating (or antidifferentiating) the function $f(x)$ produces an antiderivative of the form $F(x) + C$. To emphasize this process, Equation (1) is recast using integral notation:
$$\int f(x) dx = F(x) + C \tag{2}$$
where $C$ is understood to represent an arbitrary constant. It is important to note that (1) and (2) are just different notations to express the same fact. For example,
$$\int x^2 dx = \frac{1}{3}x^3 + C \quad \text{is equivalent to} \quad \frac{d}{dx}\left[\frac{1}{3}x^3\right] = x^2$$
Note that if we differentiate an antiderivative of $f(x)$, we obtain $f(x)$ back again. Thus,
$$\frac{d}{dx}\left[\int f(x) dx\right] = f(x) \tag{3}$$

The expression $\int f(x) dx$ is called an **indefinite integral**. The adjective "indefinite" emphasizes that the result of antidifferentiation is a "generic" function, described only up to a constant term. The "elongated s" that appears on the left side of (2) is called an **integral sign**, the function $f(x)$ is called the **integrand**, and the constant $C$ is called the **constant of integration**. Equation (2) should be read as:
*The integral of $f(x)$ with respect to $x$ is equal to $F(x)$ plus a constant.*

The differential symbol, $dx$, in the differentiation and antidifferentiation operations $\frac{d}{dx}[\;]$ and $\int [\;] dx$ serves to identify the independent variable. If an independent variable other than $x$ is used, say $t$, then the notation must be adjusted appropriately: $\frac{d}{dt}[F(t)] = f(t)$ and $\int f(t) dt = F(t) + C$.

### INTEGRATION FORMULAS

#### Table 4.2.1: Integration Formulas
| | Differentiation Formula | Equivalent Integration Formula |
| :--- | :--- | :--- |
| 1. | $\frac{d}{dx}[x] = 1$ | $\int dx = x + C$ |
| 2. | $\frac{d}{dx}\left[\frac{x^{r+1}}{r+1}\right] = x^r \quad (r \neq -1)$ | $\int x^r dx = \frac{x^{r+1}}{r+1} + C \quad (r \neq -1)$ |
| 3. | $\frac{d}{dx}[\sin x] = \cos x$ | $\int \cos x dx = \sin x + C$ |
| 4. | $\frac{d}{dx}[-\cos x] = \sin x$ | $\int \sin x dx = -\cos x + C$ |
| 5. | $\frac{d}{dx}[\tan x] = \sec^2 x$ | $\int \sec^2 x dx = \tan x + C$ |
| 6. | $\frac{d}{dx}[-\cot x] = \csc^2 x$ | $\int \csc^2 x dx = -\cot x + C$ |
| 7. | $\frac{d}{dx}[\sec x] = \sec x \tan x$ | $\int \sec x \tan x dx = \sec x + C$ |
| 8. | $\frac{d}{dx}[-\csc x] = \csc x \cot x$ | $\int \csc x \cot x dx = -\csc x + C$ |

#### Example 1
* $\int x^2 dx = \frac{x^3}{3} + C$ ($r = 2$)
* $\int x^3 dx = \frac{x^4}{4} + C$ ($r = 3$)
* $\int \frac{1}{x^5} dx = \int x^{-5} dx = \frac{x^{-5+1}}{-5+1} + C = -\frac{1}{4x^4} + C$ ($r = -5$)
* $\int \sqrt{x} dx = \int x^{1/2} dx = \frac{x^{1/2+1}}{1/2+1} + C = \frac{2}{3}x^{3/2} + C = \frac{2}{3}(\sqrt{x})^3 + C$ ($r = 1/2$)

---

### PROPERTIES OF THE INDEFINITE INTEGRAL

> **4.2.3 THEOREM**  
> Suppose that $F(x)$ and $G(x)$ are antiderivatives of $f(x)$ and $g(x)$, respectively, and that $c$ is a constant. Then:  
> (a) A constant factor can be moved through an integral sign: $\int c f(x) dx = c F(x) + C$  
> (b) An antiderivative of a sum is the sum of the antiderivatives: $\int [f(x) + g(x)] dx = F(x) + G(x) + C$  
> (c) An antiderivative of a difference is the difference of the antiderivatives: $\int [f(x) - g(x)] dx = F(x) - G(x) + C$

#### Proof:
In general, to establish the validity of an equation of the form $\int h(x) dx = H(x) + C$, one must show that $\frac{d}{dx}[H(x)] = h(x)$. We are given that $F(x)$ and $G(x)$ are antiderivatives of $f(x)$ and $g(x)$, respectively, so $\frac{d}{dx}[F(x)] = f(x)$ and $\frac{d}{dx}[G(x)] = g(x)$.
Thus:
* $\frac{d}{dx}[c F(x)] = c \frac{d}{dx}[F(x)] = c f(x)$
* $\frac{d}{dx}[F(x) + G(x)] = \frac{d}{dx}[F(x)] + \frac{d}{dx}[G(x)] = f(x) + g(x)$
* $\frac{d}{dx}[F(x) - G(x)] = \frac{d}{dx}[F(x)] - \frac{d}{dx}[G(x)] = f(x) - g(x)$  
which proves the three statements of the theorem. $\blacksquare$

The statements in Theorem 4.2.3 can be summarized by:
$$\int c f(x) dx = c \int f(x) dx \tag{4}$$
$$\int [f(x) + g(x)] dx = \int f(x) dx + \int g(x) dx \tag{5}$$
$$\int [f(x) - g(x)] dx = \int f(x) dx - \int g(x) dx \tag{6}$$
More generally:
$$\int [c_1 f_1(x) + c_2 f_2(x) + \dots + c_n f_n(x)] dx = c_1 \int f_1(x) dx + c_2 \int f_2(x) dx + \dots + c_n \int f_n(x) dx \tag{7}$$

#### Example 2
Evaluate (a) $\int 4 \cos x dx = 4 \int \cos x dx = 4 \sin x + C$  
(b) $\int (x + x^2) dx = \int x dx + \int x^2 dx = \frac{x^2}{2} + \frac{x^3}{3} + C$

#### Example 3
$$\int (3x^6 - 2x^2 + 7x + 1) dx = 3\int x^6 dx - 2\int x^2 dx + 7\int x dx + \int 1 dx = \frac{3x^7}{7} - \frac{2x^3}{3} + \frac{7x^2}{2} + x + C$$

#### Example 4
(a) $\int \frac{\cos x}{\sin^2 x} dx = \int \frac{1}{\sin x}\frac{\cos x}{\sin x} dx = \int \csc x \cot x dx = -\csc x + C$  
(b) $\int \frac{t^2 - 2t^4}{t^4} dt = \int \left(\frac{1}{t^2} - 2\right) dt = \int (t^{-2} - 2) dt = \frac{t^{-1}}{-1} - 2t + C = -\frac{1}{t} - 2t + C$

---

### INTEGRAL CURVES & INITIAL-VALUE PROBLEMS

Graphs of antiderivatives of a function $f$ are called **integral curves** of $f$. We know from Theorem 4.2.2 that if $y = F(x)$ is any integral curve of $f(x)$, then all other integral curves are vertical translations of this curve: $y = F(x) + C$.

#### Example 5
Suppose that a curve $y = f(x)$ in the $xy$-plane has the property that at each point $(x, y)$ on the curve, the tangent line has slope $x^2$. Find an equation for the curve given that it passes through the point $(2, 1)$.  
**Solution.** Since the slope of the tangent line is $dy/dx$, we have $dy/dx = x^2$, and $y = \int x^2 dx = \frac{1}{3}x^3 + C$. Substituting $(2, 1)$ yields $1 = \frac{1}{3}(2^3) + C \implies C = -5/3$. Thus:
$$y = \frac{1}{3}x^3 - \frac{5}{3}$$

#### Example 6
Solve the initial-value problem:
$$\frac{dy}{dx} = \cos x, \quad y(0) = 1$$
**Solution.** $y = \int \cos x dx = \sin x + C$. Since $y(0) = 1$, we have $1 = \sin(0) + C \implies C = 1$. Thus, $y = \sin x + 1$.

### SLOPE FIELDS
A **slope field** (or direction field) for the differential equation $\frac{dy}{dx} = f(x)$ is obtained by choosing a grid of points in the $xy$-plane, calculating the slopes $f(x)$ at each grid point, and drawing short line segments through those points.

---

### QUICK CHECK EXERCISES 4.2
*(See page 281 for answers.)*

1. A function $F$ is an antiderivative of a function $f$ on an interval if $\underline{\hspace{1cm}}$ for all $x$ in the interval.
2. Write an equivalent integration formula for each given derivative formula:
   (a) $\frac{d}{dx}[\sqrt{x}] = \frac{1}{2\sqrt{x}}$  
   (b) $\frac{d}{dx}[\sin x] = \cos x$
3. Evaluate the integrals:
   (a) $\int [x^3 + x + 5] dx$  
   (b) $\int [\sec^2 x - \csc x \cot x] dx$
4. The graph of $y = x^2 + x$ is an integral curve for the function $f(x) = \underline{\hspace{1cm}}$. If $G$ is a function whose graph is also an integral curve for $f$, and if $G(1) = 5$, then $G(x) = \underline{\hspace{1cm}}$.
5. A slope field for the differential equation $\frac{dy}{dx} = \frac{2x}{x^2 - 4}$ has a line segment with slope $\underline{\hspace{1cm}}$ through the point $(0, 5)$ and has a line segment with slope $\underline{\hspace{1cm}}$ through the point $(-4, 1)$.

#### QUICK CHECK ANSWERS 4.2
1. $F'(x) = f(x)$  
2. (a) $\int \frac{1}{2\sqrt{x}} dx = \sqrt{x} + C$ (b) $\int \cos x dx = \sin x + C$  
3. (a) $\frac{1}{4}x^4 + \frac{1}{2}x^2 + 5x + C$ (b) $\tan x + \csc x + C$  
4. $2x + 1$; $x^2 + x + 3$  
5. $0$; $-2/3$

---

### EXERCISE SET 4.2

**1. In each part, confirm that the formula is correct, and state a corresponding integration formula.**
(a) $\frac{d}{dx}[\sqrt{1 + x^2}] = \frac{x}{\sqrt{1 + x^2}}$  
(b) $\frac{d}{dx}\left[\frac{1}{3}\sin(1 + x^3)\right] = x^2\cos(1 + x^3)$

**2. In each part, confirm that the stated formula is correct by differentiating.**
(a) $\int x\sin x dx = \sin x - x\cos x + C$  
(b) $\int \frac{dx}{(1 - x^2)^{3/2}} = \frac{x}{\sqrt{1 - x^2}} + C$

**FOCUS ON CONCEPTS**
3. What is a constant of integration? Why does an answer to an integration problem involve a constant of integration?
4. What is an integral curve of a function $f$? How are two integral curves of a function $f$ related?

**5–8 Find the derivative and state a corresponding integration formula.**
5. $\frac{d}{dx}[\sqrt{x^3 + 5}]$
6. $\frac{d}{dx}\left[\frac{x}{x^2 + 3}\right]$
7. $\frac{d}{dx}[\sin(2\sqrt{x})]$
8. $\frac{d}{dx}[\sin x - x\cos x]$

**9–10 Evaluate the integral by rewriting the integrand appropriately, if required, and applying the power rule (Formula 2 in Table 4.2.1).**
9. (a) $\int x^8 dx$  
   (b) $\int x^{5/7} dx$  
   (c) $\int x^3\sqrt{x} dx$
10. (a) $\int \sqrt[3]{x^2} dx$  
    (b) $\int \frac{1}{x^6} dx$  
    (c) $\int x^{-7/8} dx$

**11–14 Evaluate each integral by applying Theorem 4.2.3 and Formula 2 in Table 4.2.1 appropriately.**
11. $\int \left(5x + \frac{2}{3x^5}\right) dx$
12. $\int \left(x^{-1/2} - 3x^{7/5} + \frac{1}{9}\right) dx$
13. $\int [x^{-3} - 3x^{1/4} + 8x^2] dx$
14. $\int \left(\frac{10}{y^{3/4}} - \sqrt[3]{y} + \frac{4}{\sqrt{y}}\right) dy$

**15–30 Evaluate the integral and check your answer by differentiating.**
15. $\int x(1 + x^3) dx$
16. $\int (2 + y^2)^2 dy$
17. $\int x^{1/3}(2 - x)^2 dx$
18. $\int (1 + x^2)(2 - x) dx$
19. $\int \frac{x^5 + 2x^2 - 1}{x^4} dx$
20. $\int \frac{1 - 2t^3}{t^3} dt$
21. $\int [3\sin x - 2\sec^2 x] dx$
22. $\int [\csc^2 t - \sec t \tan t] dt$
23. $\int \sec x(\sec x + \tan x) dx$
24. $\int \csc x(\sin x + \cot x) dx$
25. $\int \frac{\sec\theta}{\cos\theta} d\theta$
26. $\int \frac{dy}{\csc y}$
27. $\int \frac{\sin x}{\cos^2 x} dx$
28. $\int \left(\phi + \frac{2}{\sin^2\phi}\right) d\phi$
29. $\int [1 + \sin^2\theta\csc\theta] d\theta$
30. $\int \frac{\sec x + \cos x}{2\cos x} dx$

**31. Evaluate the integral $\int \frac{1}{1 + \sin x} dx$ by multiplying the numerator and denominator by an appropriate expression.**

**32. Use the double-angle formula $\cos 2x = 2\cos^2 x - 1$ to evaluate the integral $\int \frac{1}{1 + \cos 2x} dx$.**

**33–36 True–False Determine whether the statement is true or false. Explain your answer.**
33. If $F(x)$ is an antiderivative of $f(x)$, then $\int f(x) dx = F(x) + C$.
34. If $C$ denotes a constant of integration, the two formulas $\int \cos x dx = \sin x + C$ and $\int \cos x dx = (\sin x + \pi) + C$ are both correct equations.
35. The function $f(x) = \sec x + 1$ is a solution to the initial-value problem $\frac{dy}{dx} = \sec x \tan x, \; y(0) = 1$.
36. Every integral curve of the slope field $\frac{dy}{dx} = \frac{1}{\sqrt{x^2 + 1}}$ is the graph of an increasing function of $x$.

**37. Use a graphing utility to generate some representative integral curves of the function $f(x) = 5x^4 - \sec^2 x$ over the interval $(-\pi/2, \pi/2)$.**

**38. Use a graphing utility to generate some representative integral curves of the function $f(x) = (x^2 - 1)/x^2$ over the interval $(0, 5)$.**

**39–40 Solve the initial-value problems.**
39. (a) $\frac{dy}{dx} = \sqrt[3]{x}, \; y(1) = 2$  
    (b) $\frac{dy}{dt} = \sin t + 1, \; y(\pi/3) = 1/2$  
    (c) $\frac{dy}{dx} = \frac{x + 1}{\sqrt{x}}, \; y(1) = 0$
40. (a) $\frac{dy}{dx} = \frac{1}{(2x)^3}, \; y(1) = 0$  
    (b) $\frac{dy}{dt} = \sec^2 t - \sin t, \; y(\pi/4) = 1$  
    (c) $\frac{dy}{dx} = x^2\sqrt{x^3}, \; y(0) = 0$

**41–44 A particle moves along an $s$-axis with position function $s = s(t)$ and velocity function $v(t) = s'(t)$. Use the given information to find $s(t)$.**
41. $v(t) = 32t; \; s(0) = 20$
42. $v(t) = \cos t; \; s(0) = 2$
43. $v(t) = 3\sqrt{t}; \; s(4) = 1$
44. $v(t) = \sin t; \; s(0) = 0$

**45. Find the general form of a function whose second derivative is $\sqrt{x}$. [Hint: Solve the equation $f''(x) = \sqrt{x}$ for $f(x)$ by integrating both sides twice.]**

**46. Find a function $f$ such that $f''(x) = x + \cos x$ and such that $f(0) = 1$ and $f'(0) = 2$. [Hint: Integrate both sides of the equation twice.]**

**47–51 Find an equation of the curve that satisfies the given conditions.**
47. At each point $(x, y)$ on the curve the slope is $2x + 1$; the curve passes through the point $(-3, 0)$.
48. At each point $(x, y)$ on the curve the slope is $(x + 1)^2$; the curve passes through the point $(-2, 8)$.
49. At each point $(x, y)$ on the curve the slope is $-\sin x$; the curve passes through the point $(0, 2)$.
50. At each point $(x, y)$ on the curve the slope equals the square of the distance between the point and the $y$-axis; the point $(-1, 2)$ is on the curve.
51. At each point $(x, y)$ on the curve, $y$ satisfies the condition $d^2y/dx^2 = 6x$; the line $y = 5 - 3x$ is tangent to the curve at the point where $x = 1$.

**52. [CAS] In each part, use a CAS to solve the initial-value problem.**
(a) $\frac{dy}{dx} = x^2 \cos 3x, \quad y(\pi/2) = -1$  
(b) $\frac{dy}{dx} = \frac{x^3}{(4 + x^2)^{3/2}}, \quad y(0) = -2$

**53. (a) Use a graphing utility to generate a slope field for the differential equation $dy/dx = x$ in the region $-5 \le x \le 5$ and $-5 \le y \le 5$.**  
(b) Graph some representative integral curves of the function $f(x) = x$.  
(c) Find an equation for the integral curve that passes through the point $(2, 1)$.

**54. (a) Use a graphing utility to generate a slope field for the differential equation $dy/dx = \sqrt{x}$ in the region $0 \le x \le 10$ and $-5 \le y \le 5$.**  
(b) Graph some representative integral curves of the function $f(x) = \sqrt{x}$ for $x > 0$.  
(c) Find an equation for the integral curve that passes through the point $(0, 1)$.

**55–58 The given slope field figure corresponds to one of the differential equations below. Identify the differential equation that matches the figure, and sketch solution curves through the highlighted points.**  
(a) $\frac{dy}{dx} = 2$  
(b) $\frac{dy}{dx} = -x$  
(c) $\frac{dy}{dx} = x^2 - 4$  
(d) $\frac{dy}{dx} = \sin x$  
55. Slope field showing constant slopes horizontally varying with $x^2 - 4$.  
56. Slope field showing slopes dependent only on $-x$.  
57. Slope field showing constant positive slope of 2 everywhere.  
58. Slope field showing periodic wave-like tangent directions for $\sin x$.

**FOCUS ON CONCEPTS**
59. Critique the following "proof" that an arbitrary constant must be zero:
$$C = \int 0 dx = \int 0 \cdot 0 dx = 0 \int 0 dx = 0$$
60. Critique the following "proof" that an arbitrary constant must be zero:
$$0 = \left(\int x dx\right) - \left(\int x dx\right) = \int (x - x) dx = \int 0 dx = C$$
61. Let $F$ and $G$ be the functions defined by $F(x) = \frac{x\sin x}{x}$ and $G(x) = \begin{cases} 2 + \sin x, & x > 0 \\ -1 + \sin x, & x < 0 \end{cases}$.  
(a) Show that $F$ and $G$ have the same derivative.  
(b) Show that $G(x) \neq F(x) + C$ for any constant $C$.  
(c) Do parts (a) and (b) contradict Theorem 4.2.2? Explain.
62. Follow the directions of Exercise 61 using $F(x) = \frac{x^2 + 3x}{x}$ and $G(x) = \begin{cases} x + 3, & x > 0 \\ x, & x < 0 \end{cases}$.

**63–64 Use a trigonometric identity to evaluate the integral.**
63. $\int \tan^2 x dx$
64. $\int \cot^2 x dx$

**65–66 Use the identities $\cos 2\theta = 1 - 2\sin^2\theta = 2\cos^2\theta - 1$ to help evaluate the integrals.**
65. $\int \sin^2(x/2) dx$
66. $\int \cos^2(x/2) dx$

**67. The speed of sound in air at $0^\circ\text{C}$ (or $273\text{ K}$ on the Kelvin scale) is $1087\text{ ft/s}$, but the speed $v$ increases as the temperature $T$ rises. Experimentation has shown that the rate of change of $v$ with respect to $T$ is**
$$\frac{dv}{dT} = \frac{1087}{2\sqrt{273}} T^{-1/2}$$
**where $v$ is in feet per second and $T$ is in kelvins (K). Find a formula that expresses $v$ as a function of $T$.**

**68. Suppose that a uniform metal rod $50\text{ cm}$ long is insulated laterally, and the temperatures at the exposed ends are maintained at $25^\circ\text{C}$ and $85^\circ\text{C}$, respectively. Assume that an $x$-axis is chosen as in Figure Ex-68 and that the temperature $T(x)$ satisfies the equation $\frac{d^2T}{dx^2} = 0$. Find $T(x)$ for $0 \le x \le 50$.**

**69. Writing.** What is an initial-value problem? Describe the sequence of steps for solving an initial-value problem.

**70. Writing.** What is a slope field? How are slope fields and integral curves related?

---

## 4.3 INTEGRATION BY SUBSTITUTION

In this section we will study a technique, called substitution, that can often be used to transform complicated integration problems into simpler ones.

### $u$-SUBSTITUTION

The method of substitution can be motivated by examining the chain rule from the viewpoint of antidifferentiation. For this purpose, suppose that $F$ is an antiderivative of $f$ and that $g$ is a differentiable function. The chain rule implies that the derivative of $F(g(x))$ can be expressed as
$$\frac{d}{dx}[F(g(x))] = F'(g(x))g'(x)$$
which we can write in integral form as
$$\int F'(g(x))g'(x) dx = F(g(x)) + C \tag{1}$$
or since $F$ is an antiderivative of $f$,
$$\int f(g(x))g'(x) dx = F(g(x)) + C \tag{2}$$
For our purposes it will be useful to let $u = g(x)$ and to write $du/dx = g'(x)$ in the differential form $du = g'(x)dx$. With this notation (2) can be expressed as
$$\int f(u) du = F(u) + C \tag{3}$$
The process of evaluating an integral of form (2) by converting it into form (3) with the substitution $u = g(x)$ and $du = g'(x)dx$ is called the **method of $u$-substitution**.

#### Example 1
Evaluate $\int (x^2 + 1)^{50} \cdot 2x dx$.  
**Solution.** If we let $u = x^2 + 1$, then $du/dx = 2x$, which implies that $du = 2x dx$. Thus:
$$\int (x^2 + 1)^{50} \cdot 2x dx = \int u^{50} du = \frac{u^{51}}{51} + C = \frac{(x^2 + 1)^{51}}{51} + C$$

#### Guidelines for $u$-Substitution
* **Step 1.** Look for some composition $f(g(x))$ within the integrand for which the substitution $u = g(x), \; du = g'(x)dx$ produces an integral that is expressed entirely in terms of $u$ and its differential $du$.
* **Step 2.** If you are successful in Step 1, then try to evaluate the resulting integral in terms of $u$.
* **Step 3.** If you are successful in Step 2, then replace $u$ by $g(x)$ to express your final answer in terms of $x$.

### EASY TO RECOGNIZE SUBSTITUTIONS

#### Example 2
* $\int \sin(x + 9) dx = \int \sin u du = -\cos u + C = -\cos(x + 9) + C \quad [u = x + 9, du = dx]$
* $\int (x - 8)^{23} dx = \int u^{23} du = \frac{u^{24}}{24} + C = \frac{(x - 8)^{24}}{24} + C \quad [u = x - 8, du = dx]$

#### Example 3
Evaluate $\int \cos 5x dx$.  
**Solution.** Let $u = 5x \implies du = 5 dx \implies dx = \frac{1}{5}du$:
$$\int \cos 5x dx = \int (\cos u) \cdot \frac{1}{5} du = \frac{1}{5}\int \cos u du = \frac{1}{5}\sin u + C = \frac{1}{5}\sin 5x + C$$

#### Example 4
$$\int \frac{dx}{(\frac{1}{3}x - 8)^5} = \int \frac{3 du}{u^5} = 3\int u^{-5} du = -\frac{3}{4}u^{-4} + C = -\frac{3}{4}\left(\frac{1}{3}x - 8\right)^{-4} + C \quad [u = \frac{1}{3}x - 8, du = \frac{1}{3}dx]$$

#### Example 5
$$\int \left(\frac{1}{x^2} + \sec^2 \pi x\right) dx = \int \frac{dx}{x^2} + \int \sec^2 \pi x dx = -\frac{1}{x} + \frac{1}{\pi}\tan \pi x + C$$

#### Example 6
Evaluate $\int \sin^2 x \cos x dx$.  
**Solution.** Let $u = \sin x \implies du = \cos x dx$:
$$\int \sin^2 x \cos x dx = \int u^2 du = \frac{u^3}{3} + C = \frac{\sin^3 x}{3} + C$$

#### Example 7
Evaluate $\int \frac{\cos\sqrt{x}}{\sqrt{x}} dx$.  
**Solution.** Let $u = \sqrt{x} \implies du = \frac{1}{2\sqrt{x}}dx \implies 2 du = \frac{1}{\sqrt{x}}dx$:
$$\int \frac{\cos\sqrt{x}}{\sqrt{x}} dx = \int 2\cos u du = 2\sin u + C = 2\sin\sqrt{x} + C$$

#### Example 8
$$\int t^4 \sqrt[3]{3 - 5t^5} dt = -\frac{1}{25}\int u^{1/3} du = -\frac{1}{25}\frac{u^{4/3}}{4/3} + C = -\frac{3}{100}(3 - 5t^5)^{4/3} + C \quad [u = 3 - 5t^5, du = -25t^4 dt]$$

### LESS APPARENT SUBSTITUTIONS

#### Example 9
Evaluate $\int x^2\sqrt{x - 1} dx$.  
**Solution.** Let $u = x - 1 \implies x = u + 1$ and $du = dx$. Then $x^2 = (u + 1)^2 = u^2 + 2u + 1$:
$$\int x^2\sqrt{x - 1} dx = \int (u^2 + 2u + 1)\sqrt{u} du = \int (u^{5/2} + 2u^{3/2} + u^{1/2}) du = \frac{2}{7}u^{7/2} + \frac{4}{5}u^{5/2} + \frac{2}{3}u^{3/2} + C$$
$$= \frac{2}{7}(x - 1)^{7/2} + \frac{4}{5}(x - 1)^{5/2} + \frac{2}{3}(x - 1)^{3/2} + C$$

#### Example 10
Evaluate $\int \cos^3 x dx$.  
**Solution.** Write $\int \cos^3 x dx = \int \cos^2 x \cos x dx = \int (1 - \sin^2 x)\cos x dx$. Let $u = \sin x, du = \cos x dx$:
$$\int (1 - u^2) du = u - \frac{u^3}{3} + C = \sin x - \frac{1}{3}\sin^3 x + C$$

---

### QUICK CHECK EXERCISES 4.3
*(See page 287 for answers.)*

1. Indicate the $u$-substitution:
   (a) $\int 3x^2(1 + x^3)^{25} dx = \int u^{25} du$ if $u = \underline{\hspace{1cm}}$ and $du = \underline{\hspace{1cm}}$.
   (b) $\int 2x\sin x^2 dx = \int \sin u du$ if $u = \underline{\hspace{1cm}}$ and $du = \underline{\hspace{1cm}}$.
   (c) $\int \frac{18x}{\sqrt{1 + 9x^2}} dx = \int \frac{1}{\sqrt{u}} du$ if $u = \underline{\hspace{1cm}}$ and $du = \underline{\hspace{1cm}}$.
2. Supply the missing integrand corresponding to the indicated $u$-substitution:
   (a) $\int 5(5x - 3)^{-1/3} dx = \int \underline{\hspace{1cm}} du; \; u = 5x - 3$
   (b) $\int (3 - \tan x)\sec^2 x dx = \int \underline{\hspace{1cm}} du; \; u = 3 - \tan x$
   (c) $\int \frac{\sqrt[3]{8 + \sqrt{x}}}{\sqrt{x}} dx = \int \underline{\hspace{1cm}} du; \; u = 8 + \sqrt{x}$

#### QUICK CHECK ANSWERS 4.3
1. (a) $1 + x^3; \; 3x^2 dx$ (b) $x^2; \; 2x dx$ (c) $1 + 9x^2; \; 18x dx$  
2. (a) $u^{-1/3}$ (b) $-u$ (c) $2\sqrt[3]{u}$

---

### EXERCISE SET 4.3

**1–8 Evaluate the integrals using the indicated substitutions.**
1. (a) $\int 2x(x^2 + 1)^{23} dx; \quad u = x^2 + 1$  
   (b) $\int \cos^3 x \sin x dx; \quad u = \cos x$
2. (a) $\int \frac{1}{\sqrt{x}}\sin\sqrt{x} dx; \quad u = \sqrt{x}$  
   (b) $\int \frac{3x}{\sqrt{4x^2 + 5}} dx; \quad u = 4x^2 + 5$
3. (a) $\int \sec^2(4x + 1) dx; \quad u = 4x + 1$  
   (b) $\int y\sqrt{1 + 2y^2} dy; \quad u = 1 + 2y^2$
4. (a) $\int \sqrt{\sin\pi\theta}\cos\pi\theta d\theta; \quad u = \sin\pi\theta$  
   (b) $\int (2x + 7)(x^2 + 7x + 3)^{4/5} dx; \quad u = x^2 + 7x + 3$
5. (a) $\int \cot x \csc^2 x dx; \quad u = \cot x$  
   (b) $\int (1 + \sin t)^9 \cos t dt; \quad u = 1 + \sin t$
6. (a) $\int \cos 2x dx; \quad u = 2x$  
   (b) $\int x\sec^2(x^2) dx; \quad u = x^2$
7. (a) $\int x^2\sqrt{1 + x} dx; \quad u = 1 + x$  
   (b) $\int [\csc(\sin x)]^2 \cos x dx; \quad u = \sin x$
8. (a) $\int \sin(x - \pi) dx; \quad u = x - \pi$  
   (b) $\int \frac{5x^4}{(x^5 + 1)^2} dx; \quad u = x^5 + 1$

**FOCUS ON CONCEPTS**
9. Explain the connection between the chain rule for differentiation and the method of $u$-substitution for integration.
10. Explain how the substitution $u = ax + b$ helps to perform an integration in which the integrand is $f(ax + b)$, where $f(x)$ is an easy to integrate function.

**11–36 Evaluate the integrals using appropriate substitutions.**
11. $\int (4x - 3)^9 dx$
12. $\int x^3\sqrt{5 + x^4} dx$
13. $\int \sin 7x dx$
14. $\int \cos(x/3) dx$
15. $\int \sec 4x \tan 4x dx$
16. $\int \sec^2 5x dx$
17. $\int t\sqrt{7t^2 + 12} dt$
18. $\int \frac{x}{\sqrt{4 - 5x^2}} dx$
19. $\int \frac{6}{(1 - 2x)^3} dx$
20. $\int \frac{x^2 + 1}{\sqrt{x^3 + 3x}} dx$
21. $\int \frac{x^3}{(5x^4 + 2)^3} dx$
22. $\int \frac{\sin(1/x)}{3x^2} dx$
23. $\int \frac{\sin(5/x)}{x^2} dx$
24. $\int \frac{\sec^2(\sqrt{x})}{\sqrt{x}} dx$
25. $\int \cos^4 3t \sin 3t dt$
26. $\int \cos 2t \sin^5 2t dt$
27. $\int x\sec^2(x^2) dx$
28. $\int \frac{\cos 4\theta}{(1 + 2\sin 4\theta)^4} d\theta$
29. $\int \cos 4\theta \sqrt{2 - \sin 4\theta} d\theta$
30. $\int \tan^3 5x \sec^2 5x dx$
31. $\int \sec^3 2x \tan 2x dx$
32. $\int [\sin(\sin\theta)]\cos\theta d\theta$
33. $\int \frac{y}{\sqrt{2y + 1}} dy$
34. $\int x\sqrt{4 - x} dx$
35. $\int \sin^3 2\theta d\theta$
36. $\int \sec^4 3\theta d\theta$ [Hint: Apply a trigonometric identity.]

**37–39 Evaluate the integrals assuming that $n$ is a positive integer and $b \neq 0$.**
37. $\int (a + bx)^n dx$
38. $\int \sqrt[n]{a + bx} dx$
39. $\int \sin^n(a + bx)\cos(a + bx) dx$

**40. [CAS] Use a CAS to check the answers you obtained in Exercises 37–39. If the answer produced by the CAS does not match yours, show that the two answers are equivalent.**

**FOCUS ON CONCEPTS**
41. (a) Evaluate the integral $\int \sin x \cos x dx$ by two methods: first by letting $u = \sin x$, and then by letting $u = \cos x$.  
    (b) Explain why the two apparently different answers obtained in part (a) are really equivalent.
42. (a) Evaluate the integral $\int (5x - 1)^2 dx$ by two methods: first square and integrate, then let $u = 5x - 1$.  
    (b) Explain why the two apparently different answers obtained in part (a) are really equivalent.

**43–44 Solve the initial-value problems.**
43. $\frac{dy}{dx} = \sqrt{5x + 1}, \quad y(3) = -2$
44. $\frac{dy}{dx} = 2 + \sin 3x, \quad y(\pi/3) = 0$

**45. (a) Evaluate $\int [x/\sqrt{x^2 + 1}] dx$.**  
(b) Use a graphing utility to generate some typical integral curves of $f(x) = x/\sqrt{x^2 + 1}$ over the interval $(-5, 5)$.

**46. (a) Evaluate $\int 2x\sin(25 - x^2) dx$.**  
(b) Use a graphing utility to generate some typical integral curves of $f(x) = 2x\sin(25 - x^2)$ over the interval $(-5, 5)$.

**47. Find a function $f$ such that the slope of the tangent line at a point $(x, y)$ on the curve $y = f(x)$ is $\sqrt{3x + 1}$ and the curve passes through the point $(0, 1)$.**

**48. A population of minnows in a lake is estimated to be 100,000 at the beginning of the year 2010. Suppose that $t$ years after the beginning of 2010 the rate of growth of the population $p(t)$ (in thousands) is given by $p'(t) = (3 + 0.12t)^{3/2}$. Estimate the projected population at the beginning of the year 2015.**

**49. Let $y(t)$ denote the number of *E. coli* cells in a container of nutrient solution $t$ minutes after the start of an experiment. Assume that $y(t)$ is modeled by the initial-value problem**
$$\frac{dy}{dt} = 0.95(0.79 + 0.024t)^{3/2}, \quad y(0) = 20$$
**Use this model to estimate the number of *E. coli* cells in the container 20 minutes after the start of the experiment.**

**50. Writing.** If you want to evaluate an integral by $u$-substitution, how do you decide what part of the integrand to choose for $u$?

**51. Writing.** The evaluation of an integral can sometimes result in apparently different answers (Exercises 41 and 42). Explain why this occurs and give an example. How might you show that two apparently different answers are actually equivalent?

---

## 4.4 THE DEFINITION OF AREA AS A LIMIT; SIGMA NOTATION

Our main goal in this section is to use the rectangle method to give a precise mathematical definition of the "area under a curve."

### SIGMA NOTATION

To simplify our computations, we will begin by discussing a useful notation for expressing lengthy sums in a compact form:
$$\sum_{k=m}^n f(k) \tag{1}$$
denotes the sum of the terms that result when we substitute successive integers for $k$, starting with $k = m$ and ending with $k = n$. The numbers $m$ and $n$ are called, respectively, the **lower** and **upper limits of summation**; and the letter $k$ is called the **index of summation**.

#### Example 1
* $\sum_{k=4}^8 k^3 = 4^3 + 5^3 + 6^3 + 7^3 + 8^3$
* $\sum_{k=1}^5 2k = 2\cdot 1 + 2\cdot 2 + 2\cdot 3 + 2\cdot 4 + 2\cdot 5 = 2 + 4 + 6 + 8 + 10$
* $\sum_{k=0}^5 (2k + 1) = 1 + 3 + 5 + 7 + 9 + 11$
* $\sum_{k=0}^5 (-1)^k(2k + 1) = 1 - 3 + 5 - 7 + 9 - 11$
* $\sum_{k=-3}^1 k^3 = (-3)^3 + (-2)^3 + (-1)^3 + 0^3 + 1^3 = -27 - 8 - 1 + 0 + 1$
* $\sum_{k=1}^3 k\sin\left(\frac{k\pi}{5}\right) = \sin\frac{\pi}{5} + 2\sin\frac{2\pi}{5} + 3\sin\frac{3\pi}{5}$

### PROPERTIES OF SUMS

> **4.4.1 THEOREM**  
> (a) $\sum_{k=1}^n c a_k = c \sum_{k=1}^n a_k$ (if $c$ does not depend on $k$)  
> (b) $\sum_{k=1}^n (a_k + b_k) = \sum_{k=1}^n a_k + \sum_{k=1}^n b_k$  
> (c) $\sum_{k=1}^n (a_k - b_k) = \sum_{k=1}^n a_k - \sum_{k=1}^n b_k$

#### Proof (a):
$\sum_{k=1}^n c a_k = c a_1 + c a_2 + \dots + c a_n = c(a_1 + a_2 + \dots + a_n) = c \sum_{k=1}^n a_k$. $\blacksquare$

#### Proof (b):
$\sum_{k=1}^n (a_k + b_k) = (a_1 + b_1) + (a_2 + b_2) + \dots + (a_n + b_n) = (a_1 + a_2 + \dots + a_n) + (b_1 + b_2 + \dots + b_n) = \sum_{k=1}^n a_k + \sum_{k=1}^n b_k$. $\blacksquare$

### SUMMATION FORMULAS

> **4.4.2 THEOREM**  
> (a) $\sum_{k=1}^n k = 1 + 2 + \dots + n = \frac{n(n+1)}{2}$  
> (b) $\sum_{k=1}^n k^2 = 1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}$  
> (c) $\sum_{k=1}^n k^3 = 1^3 + 2^3 + \dots + n^3 = \left[\frac{n(n+1)}{2}\right]^2$

#### Example 2
Evaluate $\sum_{k=1}^{30} k(k + 1)$.  
**Solution.** $\sum_{k=1}^{30} (k^2 + k) = \sum_{k=1}^{30} k^2 + \sum_{k=1}^{30} k = \frac{30(31)(61)}{6} + \frac{30(31)}{2} = 9920$.

#### Example 3
Express $\sum_{k=1}^n (3 + k)^2$ in closed form.  
**Solution.** $\sum_{k=1}^n (3 + k)^2 = 4^2 + 5^2 + \dots + (3+n)^2 = [1^2 + 2^2 + \dots + (3+n)^2] - [1^2 + 2^2 + 3^2] = \sum_{k=1}^{3+n} k^2 - 14 = \frac{(3+n)(4+n)(7+2n)}{6} - 14 = \frac{1}{6}(73n + 21n^2 + 2n^3)$.

---

### A DEFINITION OF AREA

> **4.4.3 DEFINITION (Area Under a Curve)**  
> If the function $f$ is continuous on $[a, b]$ and if $f(x) \ge 0$ for all $x$ in $[a, b]$, then the area $A$ under the curve $y = f(x)$ over the interval $[a, b]$ is defined by
> $$A = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*) \Delta x \tag{2}$$
> where $\Delta x = (b - a)/n$, and sample points $x_k^*$ are chosen as:
> * Left endpoint: $x_k^* = a + (k - 1)\Delta x$  
> * Right endpoint: $x_k^* = a + k\Delta x$  
> * Midpoint: $x_k^* = a + (k - \frac{1}{2})\Delta x$

> **4.4.4 THEOREM**  
> (a) $\lim_{n \to +\infty} \frac{1}{n} \sum_{k=1}^n 1 = 1$  
> (b) $\lim_{n \to +\infty} \frac{1}{n^2} \sum_{k=1}^n k = \frac{1}{2}$  
> (c) $\lim_{n \to +\infty} \frac{1}{n^3} \sum_{k=1}^n k^2 = \frac{1}{3}$  
> (d) $\lim_{n \to +\infty} \frac{1}{n^4} \sum_{k=1}^n k^3 = \frac{1}{4}$

#### Example 4
Find area under $f(x) = x^2$ on $[0, 1]$ via right endpoints.  
$\Delta x = 1/n, \; x_k^* = k/n$.
$$\sum_{k=1}^n \left(\frac{k}{n}\right)^2 \frac{1}{n} = \frac{1}{n^3}\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6n^3} \implies A = \lim_{n \to \infty} \frac{1}{6}\left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right) = \frac{1}{3}$$

#### Example 5
Find area under $y = 9 - x^2$ over $[0, 3]$ via midpoints: $A = 18$.

### NET SIGNED AREA

> **4.4.5 DEFINITION (Net Signed Area)**  
> If the function $f$ is continuous on $[a, b]$, then the net signed area $A$ between $y = f(x)$ and the interval $[a, b]$ is defined by
> $$A = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*) \Delta x \tag{9}$$

#### Example 7
Confirm that net signed area between $f(x) = x - 1$ and $[0, 2]$ is zero:
$\Delta x = 2/n, \; x_k^* = (k - 1)(2/n)$.
$$\sum_{k=1}^n \left[(k-1)\frac{2}{n} - 1\right]\frac{2}{n} = \sum_{k=1}^n \left[\frac{4}{n^2}k - \frac{4}{n^2} - \frac{2}{n}\right] \to 4\left(\frac{1}{2}\right) - 0 - 2 = 0$$

---

### QUICK CHECK EXERCISES 4.4
*(See page 299 for answers.)*

1. (a) Write the sum in two ways: $\frac{1}{2} + \frac{1}{4} + \frac{1}{6} + \frac{1}{8} = \sum_{k=1}^4 \underline{\hspace{1cm}} = \sum_{j=0}^3 \underline{\hspace{1cm}}$.  
   (b) Express the sum $10 + 10^2 + 10^3 + 10^4 + 10^5$ using sigma notation.
2. Express the sums in closed form: (a) $\sum_{k=1}^n k$ (b) $\sum_{k=1}^n (6k + 1)$ (c) $\sum_{k=1}^n k^2$.
3. Divide the interval $[1, 3]$ into $n = 4$ subintervals of equal length:  
   (a) Each subinterval has width $\underline{\hspace{1cm}}$.  
   (b) The left endpoints of the subintervals are $\underline{\hspace{1cm}}$.  
   (c) The midpoints of the subintervals are $\underline{\hspace{1cm}}$.  
   (d) The right endpoints of the subintervals are $\underline{\hspace{1cm}}$.
4. Find the left endpoint approximation for the area between the curve $y = x^2$ and the interval $[1, 3]$ using $n = 4$ equal subdivisions of the interval.
5. The right endpoint approximation for the net signed area between $y = f(x)$ and an interval $[a, b]$ is given by $\sum_{k=1}^n \frac{6k + 1}{n^2}$. Find the exact value of this net signed area.

#### QUICK CHECK ANSWERS 4.4
1. (a) $\frac{1}{2k}; \; \frac{1}{2(j+1)}$ (b) $\sum_{k=1}^5 10^k$  
2. (a) $\frac{n(n+1)}{2}$ (b) $3n(n+1) + n$ (c) $\frac{n(n+1)(2n+1)}{6}$  
3. (a) $0.5$ (b) $1, 1.5, 2, 2.5$ (c) $1.25, 1.75, 2.25, 2.75$ (d) $1.5, 2, 2.5, 3$  
4. $6.75$  
5. $\lim_{n \to +\infty} \frac{3n^2 + 4n}{n^2} = 3$

---

### EXERCISE SET 4.4

**1. Evaluate.**  
(a) $\sum_{k=1}^3 k^3$  
(b) $\sum_{j=2}^6 (3j - 1)$  
(c) $\sum_{i=-4}^1 (i^2 - i)$  
(d) $\sum_{n=0}^5 1$  
(e) $\sum_{k=0}^4 (-2)^k$  
(f) $\sum_{n=1}^6 \sin n\pi$

**2. Evaluate.**  
(a) $\sum_{k=1}^4 k\sin\frac{k\pi}{2}$  
(b) $\sum_{j=0}^5 (-1)^j$  
(c) $\sum_{i=7}^{20} \pi^2$  
(d) $\sum_{m=3}^5 2^{m+1}$  
(e) $\sum_{n=1}^6 \sqrt{n}$  
(f) $\sum_{k=0}^{10} \cos k\pi$

**3–8 Write each expression in sigma notation but do not evaluate.**
3. $1 + 2 + 3 + \dots + 10$
4. $3\cdot 1 + 3\cdot 2 + 3\cdot 3 + \dots + 3\cdot 20$
5. $2 + 4 + 6 + 8 + \dots + 20$
6. $1 + 3 + 5 + 7 + \dots + 15$
7. $1 - 3 + 5 - 7 + 9 - 11$
8. $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \frac{1}{5}$

**9. (a) Express the sum of the even integers from 2 to 100 in sigma notation.**  
(b) Express the sum of the odd integers from 1 to 99 in sigma notation.

**10. Express in sigma notation.**  
(a) $a_1 - a_2 + a_3 - a_4 + a_5$  
(b) $-b_0 + b_1 - b_2 + b_3 - b_4 + b_5$  
(c) $a_0 + a_1 x + a_2 x^2 + \dots + a_n x^n$  
(d) $a^5 + a^4 b + a^3 b^2 + a^2 b^3 + a b^4 + b^5$

**11–16 Use Theorem 4.4.2 to evaluate the sums. Check your answers using the summation feature of a calculating utility.**
11. $\sum_{k=1}^{100} k$
12. $\sum_{k=1}^{100} (7k + 1)$
13. $\sum_{k=1}^{20} k^2$
14. $\sum_{k=4}^{20} k^2$
15. $\sum_{k=1}^{30} k(k - 2)(k + 2)$
16. $\sum_{k=1}^6 (k - k^3)$

**17–20 Express the sums in closed form.**
17. $\sum_{k=1}^n \frac{3k}{n}$
18. $\sum_{k=1}^{n-1} \frac{k^2}{n}$
19. $\sum_{k=1}^{n-1} \frac{k^3}{n^2}$
20. $\sum_{k=1}^n \left(\frac{5}{n} - \frac{2k}{n}\right)$

**21–24 True–False Determine whether the statement is true or false. Explain your answer.**
21. For all positive integers $n$, $1^3 + 2^3 + \dots + n^3 = (1 + 2 + \dots + n)^2$.
22. The midpoint approximation is the average of the left endpoint approximation and the right endpoint approximation.
23. Every right endpoint approximation for the area under the graph of $y = x^2$ over an interval $[a, b]$ will be an overestimate.
24. For any continuous function $f$, the area between the graph of $f$ and an interval $[a, b]$ (on which $f$ is defined) is equal to the absolute value of the net signed area between the graph of $f$ and the interval $[a, b]$.

**FOCUS ON CONCEPTS**
25. (a) Write the first three and final two summands in the sum $\sum_{k=1}^n \left(2 + k\cdot\frac{3}{n}\right)^4 \frac{3}{n}$. Explain why this sum gives the right endpoint approximation for the area under the curve $y = x^4$ over the interval $[2, 5]$.  
    (b) Show that a change in the index range of the sum in part (a) can produce the left endpoint approximation for the area under the curve $y = x^4$ over the interval $[2, 5]$.
26. For a function $f$ that is continuous on $[a, b]$, Definition 4.4.5 says that the net signed area $A$ between $y = f(x)$ and the interval $[a, b]$ is $A = \lim_{n \to +\infty} \sum_{k=1}^n f(x_k^*) \Delta x$. Give geometric interpretations for the symbols $n, x_k^*,$ and $\Delta x$. Explain how to interpret the limit in this definition.

**27–30 Divide the specified interval into $n = 4$ subintervals of equal length and then compute $\sum_{k=1}^4 f(x_k^*) \Delta x$ with $x_k^*$ as (a) the left endpoint of each subinterval, (b) the midpoint of each subinterval, and (c) the right endpoint of each subinterval. Illustrate each part with a graph of $f$ that includes the rectangles whose areas are represented in the sum.**
27. $f(x) = 3x + 1; \quad [2, 6]$
28. $f(x) = 1/x; \quad [1, 9]$
29. $f(x) = \cos x; \quad [0, \pi]$
30. $f(x) = 2x - x^2; \quad [-1, 3]$

**31–34 [CAS] Use a calculating utility with summation capabilities or a CAS to obtain an approximate value for the area between the curve $y = f(x)$ and the specified interval with $n = 10, 20,$ and $50$ subintervals using the (a) left endpoint, (b) midpoint, and (c) right endpoint approximations.**
31. $f(x) = 1/x; \quad [1, 2]$
32. $f(x) = 1/x^2; \quad [1, 3]$
33. $f(x) = \sqrt{x}; \quad [0, 4]$
34. $f(x) = \sin x; \quad [0, \pi/2]$

**35–40 Use Definition 4.4.3 with $x_k^*$ as the right endpoint of each subinterval to find the area under the curve $y = f(x)$ over the specified interval.**
35. $f(x) = x/2; \quad [1, 4]$
36. $f(x) = 5 - x; \quad [0, 5]$
37. $f(x) = 9 - x^2; \quad [0, 3]$
38. $f(x) = 4 - \frac{1}{4}x^2; \quad [0, 3]$
39. $f(x) = x^3; \quad [2, 6]$
40. $f(x) = 1 - x^3; \quad [-3, -1]$

**41–44 Use Definition 4.4.3 with $x_k^*$ as the left endpoint of each subinterval to find the area under the curve $y = f(x)$ over the specified interval.**
41. $f(x) = x/2; \quad [1, 4]$
42. $f(x) = 5 - x; \quad [0, 5]$
43. $f(x) = 9 - x^2; \quad [0, 3]$
44. $f(x) = 4 - \frac{1}{4}x^2; \quad [0, 3]$

**45–48 Use Definition 4.4.3 with $x_k^*$ as the midpoint of each subinterval to find the area under the curve $y = f(x)$ over the specified interval.**
45. $f(x) = 2x; \quad [0, 4]$
46. $f(x) = 6 - x; \quad [1, 5]$
47. $f(x) = x^2; \quad [0, 1]$
48. $f(x) = x^2; \quad [-1, 1]$

**49–52 Use Definition 4.4.5 with $x_k^*$ as the right endpoint of each subinterval to find the net signed area between the curve $y = f(x)$ and the specified interval.**
49. $f(x) = x; \quad [-1, 1]$. Verify your answer with a simple geometric argument.
50. $f(x) = x; \quad [-1, 2]$. Verify your answer with a simple geometric argument.
51. $f(x) = x^2 - 1; \quad [0, 2]$
52. $f(x) = x^3; \quad [-1, 1]$

**53. (a) Show that the area under the graph of $y = x^3$ and over the interval $[0, b]$ is $b^4/4$.**  
(b) Find a formula for the area under $y = x^3$ over the interval $[a, b]$, where $a \ge 0$.

**54. Find the area between the graph of $y = \sqrt{x}$ and the interval $[0, 1]$. [Hint: Use the result of Exercise 21 of Section 4.1.]**

**55. An artist wants to create a rough triangular design using uniform square tiles glued edge to edge. She places $n$ tiles in a row to form the base of the triangle and then makes each successive row two tiles shorter than the preceding row. Find a formula for the number of tiles used in the design. [Hint: Your answer will depend on whether $n$ is even or odd.]**

**56. An artist wants to create a sculpture by gluing together uniform spheres. She creates a rough rectangular base that has 50 spheres along one edge and 30 spheres along the other. She then creates successive layers by gluing spheres in the grooves of the preceding layer. How many spheres will there be in the sculpture?**

**57–60 Consider the telescoping sum $\sum_{k=1}^4 [(k + 1)^3 - k^3] = 5^3 - 1^3 = 124$. Evaluate the telescoping sums in these exercises.**
57. $\sum_{k=5}^{17} (3^k - 3^{k-1})$
58. $\sum_{k=1}^{50} \left(\frac{1}{k} - \frac{1}{k+1}\right)$
59. $\sum_{k=2}^{20} \left(\frac{1}{k^2} - \frac{1}{(k-1)^2}\right)$
60. $\sum_{k=1}^{100} (2^{k+1} - 2^k)$

**61. (a) Show that $\frac{1}{1\cdot 3} + \frac{1}{3\cdot 5} + \dots + \frac{1}{(2n-1)(2n+1)} = \frac{n}{2n+1}$.**  
[Hint: $\frac{1}{(2n-1)(2n+1)} = \frac{1}{2}\left(\frac{1}{2n-1} - \frac{1}{2n+1}\right)$.]  
(b) Use the result in part (a) to find $\lim_{n \to +\infty} \sum_{k=1}^n \frac{1}{(2k-1)(2k+1)}$.

**62. (a) Show that $\frac{1}{1\cdot 2} + \frac{1}{2\cdot 3} + \frac{1}{3\cdot 4} + \dots + \frac{1}{n(n+1)} = \frac{n}{n+1}$.**  
[Hint: $\frac{1}{n(n+1)} = \frac{1}{n} - \frac{1}{n+1}$.]  
(b) Use the result in part (a) to find $\lim_{n \to +\infty} \sum_{k=1}^n \frac{1}{k(k+1)}$.

**63. Let $\bar{x}$ denote the arithmetic average of the $n$ numbers $x_1, x_2, \dots, x_n$. Use Theorem 4.4.1 to prove that $\sum_{i=1}^n (x_i - \bar{x}) = 0$.**

**64. Let $S = \sum_{k=0}^n a r^k$. Show that $S - rS = a - a r^{n+1}$ and hence that $\sum_{k=0}^n a r^k = \frac{a - a r^{n+1}}{1 - r} \quad (r \neq 1)$. (A sum of this form is called a geometric sum.)**

**65. By writing out the sums, determine whether the following are valid identities.**  
(a) $\int \left[\sum_{i=1}^n f_i(x)\right] dx = \sum_{i=1}^n \left[\int f_i(x) dx\right]$  
(b) $\frac{d}{dx}\left[\sum_{i=1}^n f_i(x)\right] = \sum_{i=1}^n \left[\frac{d}{dx}[f_i(x)]\right]$

**66. Which of the following are valid identities?**  
(a) $\sum_{i=1}^n a_i b_i = \left(\sum_{i=1}^n a_i\right)\left(\sum_{i=1}^n b_i\right)$  
(b) $\sum_{i=1}^n a_i^2 = \left(\sum_{i=1}^n a_i\right)^2$  
(c) $\sum_{i=1}^n \frac{a_i}{b_i} = \frac{\sum_{i=1}^n a_i}{\sum_{i=1}^n b_i}$  
(d) $\sum_{i=1}^n a_i = \sum_{j=0}^{n-1} a_{j+1}$

**67. Prove part (c) of Theorem 4.4.1.**

**68. Prove Theorem 4.4.4.**

**69. Writing.** What is net signed area? How does this concept expand our application of the rectangle method?

**70. Writing.** Based on Example 6, one might conjecture that the midpoint approximation always provides a better approximation than either endpoint approximation. Discuss the merits of this conjecture.

---

## 4.5 THE DEFINITE INTEGRAL

In this section we will introduce the concept of a "definite integral," which will link the concept of area to other important concepts such as length, volume, density, probability, and work.

### RIEMANN SUMS AND THE DEFINITE INTEGRAL

A **partition** of the interval $[a, b]$ is a collection of points
$$a = x_0 < x_1 < x_2 < \dots < x_{n-1} < x_n = b$$
that divides $[a, b]$ into $n$ subintervals of lengths $\Delta x_1 = x_1 - x_0, \; \Delta x_2 = x_2 - x_1, \dots, \; \Delta x_n = x_n - x_{n-1}$. The largest of these widths is called the **mesh size** of the partition, denoted $\max \Delta x_k$.

> **4.5.1 DEFINITION (The Definite Integral / Riemann Integral)**  
> A function $f$ is said to be **integrable** on a finite closed interval $[a, b]$ if the limit
> $$\lim_{\max \Delta x_k \to 0} \sum_{k=1}^n f(x_k^*) \Delta x_k$$
> exists and does not depend on the choice of partitions or on the choice of the points $x_k^*$ in the subintervals. When this is the case we denote the limit by the symbol
> $$\int_a^b f(x) dx = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n f(x_k^*) \Delta x_k$$
> which is called the **definite integral** of $f$ from $a$ to $b$. The sum $\sum_{k=1}^n f(x_k^*) \Delta x_k$ is called a **Riemann sum**.

> **Georg Friedrich Bernhard Riemann (1826–1866)**  
> German mathematician. Bernhard Riemann was the son of a Protestant minister. He studied physics under Weber and mathematics under Carl Friedrich Gauss at Göttingen University. In 1851 Riemann received his Ph.D. under Gauss, presenting his famous introductory lecture on the foundations of geometry, which delighted Gauss and laid the foundation for Einstein's general theory of relativity 50 years later. Riemann formulated the rigorous definition of the definite integral and made profound contributions to complex function theory and number theory before his early death at age 39.

> **4.5.2 THEOREM**  
> If a function $f$ is continuous on an interval $[a, b]$, then $f$ is integrable on $[a, b]$, and the net signed area $A$ between the graph of $f$ and the interval $[a, b]$ is
> $$A = \int_a^b f(x) dx \tag{1}$$

#### Example 1
Sketch the region and evaluate using geometry:  
(a) $\int_1^4 2 dx = 2(3) = 6$ (rectangle)  
(b) $\int_{-1}^2 (x + 2) dx = \frac{1}{2}(1 + 4)(3) = \frac{15}{2}$ (trapezoid)  
(c) $\int_0^1 \sqrt{1 - x^2} dx = \frac{1}{4}\pi(1^2) = \frac{\pi}{4}$ (quarter-circle)

#### Example 2
Evaluate (a) $\int_0^2 (x - 1) dx = 0$ (b) $\int_0^1 (x - 1) dx = -1/2$.

---

### PROPERTIES OF THE DEFINITE INTEGRAL

> **4.5.3 DEFINITION**  
> (a) If $a$ is in the domain of $f$, we define $\int_a^a f(x) dx = 0$.  
> (b) If $f$ is integrable on $[a, b]$, then we define $\int_b^a f(x) dx = -\int_a^b f(x) dx$.

#### Example 3
(a) $\int_1^1 x^2 dx = 0$  
(b) $\int_1^0 \sqrt{1 - x^2} dx = -\int_0^1 \sqrt{1 - x^2} dx = -\frac{\pi}{4}$

> **4.5.4 THEOREM**  
> If $f$ and $g$ are integrable on $[a, b]$ and $c$ is a constant, then $cf$, $f + g$, and $f - g$ are integrable on $[a, b]$ and:  
> (a) $\int_a^b c f(x) dx = c \int_a^b f(x) dx$  
> (b) $\int_a^b [f(x) + g(x)] dx = \int_a^b f(x) dx + \int_a^b g(x) dx$  
> (c) $\int_a^b [f(x) - g(x)] dx = \int_a^b f(x) dx - \int_a^b g(x) dx$

#### Example 4
$$\int_0^1 (5 - 3\sqrt{1 - x^2}) dx = \int_0^1 5 dx - 3\int_0^1 \sqrt{1 - x^2} dx = 5(1) - 3\left(\frac{\pi}{4}\right) = 5 - \frac{3\pi}{4}$$

> **4.5.5 THEOREM**  
> If $f$ is integrable on a closed interval containing the three points $a, b,$ and $c$, then
> $$\int_a^b f(x) dx = \int_a^c f(x) dx + \int_c^b f(x) dx$$
> no matter how the points are ordered.

> **4.5.6 THEOREM**  
> (a) If $f$ is integrable on $[a, b]$ and $f(x) \ge 0$ for all $x$ in $[a, b]$, then $\int_a^b f(x) dx \ge 0$.  
> (b) If $f$ and $g$ are integrable on $[a, b]$ and $f(x) \ge g(x)$ for all $x$ in $[a, b]$, then $\int_a^b f(x) dx \ge \int_a^b g(x) dx$.

### DISCONTINUITIES AND INTEGRABILITY

> **4.5.7 DEFINITION**  
> A function $f$ that is defined on an interval is said to be **bounded** on the interval if there is a positive number $M$ such that $-M \le f(x) \le M$ for all $x$ in the interval.

> **4.5.8 THEOREM**  
> Let $f$ be a function that is defined on the finite closed interval $[a, b]$.  
> (a) If $f$ has finitely many discontinuities in $[a, b]$ but is bounded on $[a, b]$, then $f$ is integrable on $[a, b]$.  
> (b) If $f$ is not bounded on $[a, b]$, then $f$ is not integrable on $[a, b]$.

---

### QUICK CHECK EXERCISES 4.5
*(See page 309 for answers.)*

1. In each part, use the partition of $[2, 7]$: points $2, 3, 4.5, 6.5, 7$.  
   (a) What is $n$, the number of subintervals?  
   (b) $x_0 = \underline{\hspace{0.5cm}}; x_1 = \underline{\hspace{0.5cm}}; x_2 = \underline{\hspace{0.5cm}}; x_3 = \underline{\hspace{0.5cm}}; x_4 = \underline{\hspace{0.5cm}}$.  
   (c) $\Delta x_1 = \underline{\hspace{0.5cm}}; \Delta x_2 = \underline{\hspace{0.5cm}}; \Delta x_3 = \underline{\hspace{0.5cm}}; \Delta x_4 = \underline{\hspace{0.5cm}}$.  
   (d) The mesh of this partition is $\underline{\hspace{0.5cm}}$.
2. Let $f(x) = 2x - 8$. Use the partition above and sample points $x_1^* = 2, x_2^* = 4, x_3^* = 5, x_4^* = 7$ to evaluate the Riemann sum $\sum_{k=1}^4 f(x_k^*) \Delta x_k$.
3. Evaluate $\int_2^7 (2x - 8) dx$ using geometry.
4. Suppose $\int_{-2}^1 g(x) dx = 5$ and $\int_1^2 g(x) dx = -2$. Evaluate:  
   (a) $\int_1^2 5g(x) dx$  
   (b) $\int_{-2}^2 g(x) dx$  
   (c) $\int_1^1 [g(x)]^2 dx$  
   (d) $\int_2^{-2} 4g(x) dx$

#### QUICK CHECK ANSWERS 4.5
1. (a) $n = 4$ (b) $2, 3, 4.5, 6.5, 7$ (c) $1, 1.5, 2, 0.5$ (d) $2$  
2. $3$  
3. $5$  
4. (a) $-10$ (b) $3$ (c) $0$ (d) $-12$

---

### EXERCISE SET 4.5

**1–4 Find the value of (a) $\sum_{k=1}^n f(x_k^*) \Delta x_k$ and (b) $\max \Delta x_k$.**
1. $f(x) = x + 1; \quad a = 0, b = 4; \quad n = 3; \quad \Delta x_1 = 1, \Delta x_2 = 1, \Delta x_3 = 2; \quad x_1^* = 1/3, x_2^* = 3/2, x_3^* = 3$
2. $f(x) = \cos x; \quad a = 0, b = 2\pi; \quad n = 4; \quad \Delta x_1 = \pi/2, \Delta x_2 = 3\pi/4, \Delta x_3 = \pi/2, \Delta x_4 = \pi/4; \quad x_1^* = \pi/4, x_2^* = \pi, x_3^* = 3\pi/2, x_4^* = 7\pi/4$
3. $f(x) = 4 - x^2; \quad a = -3, b = 4; \quad n = 4; \quad \Delta x_1 = 1, \Delta x_2 = 2, \Delta x_3 = 1, \Delta x_4 = 3; \quad x_1^* = -5/2, x_2^* = -1, x_3^* = 1/4, x_4^* = 3$
4. $f(x) = x^3; \quad a = -3, b = 3; \quad n = 4; \quad \Delta x_1 = 2, \Delta x_2 = 1, \Delta x_3 = 1, \Delta x_4 = 2; \quad x_1^* = -2, x_2^* = 0, x_3^* = 0, x_4^* = 2$

**5–8 Use the given values of $a$ and $b$ to express the following limits as integrals. (Do not evaluate the integrals.)**
5. $\lim_{\max \Delta x_k \to 0} \sum_{k=1}^n (x_k^*)^2 \Delta x_k; \quad a = -1, b = 2$
6. $\lim_{\max \Delta x_k \to 0} \sum_{k=1}^n (x_k^*)^3 \Delta x_k; \quad a = 1, b = 2$
7. $\lim_{\max \Delta x_k \to 0} \sum_{k=1}^n 4x_k^*(1 - 3x_k^*) \Delta x_k; \quad a = -3, b = 3$
8. $\lim_{\max \Delta x_k \to 0} \sum_{k=1}^n (\sin^2 x_k^*) \Delta x_k; \quad a = 0, b = \pi/2$

**9–10 Use Definition 4.5.1 to express the integrals as limits of Riemann sums. (Do not evaluate the integrals.)**
9. (a) $\int_1^2 2x dx$  
   (b) $\int_0^1 \frac{x}{x + 1} dx$
10. (a) $\int_1^2 \sqrt{x} dx$  
    (b) $\int_{-\pi/2}^{\pi/2} (1 + \cos x) dx$

**FOCUS ON CONCEPTS**
11. Explain informally why Theorem 4.5.4(a) follows from Definition 4.5.1.
12. Explain informally why Theorem 4.5.6(a) follows from Definition 4.5.1.

**13–16 Sketch the region whose signed area is represented by the definite integral, and evaluate the integral using an appropriate formula from geometry, where needed.**
13. (a) $\int_0^3 x dx$  
    (b) $\int_{-2}^{-1} x dx$  
    (c) $\int_{-1}^4 x dx$  
    (d) $\int_{-5}^5 x dx$
14. (a) $\int_0^2 (1 - \frac{1}{2}x) dx$  
    (b) $\int_{-1}^1 (1 - \frac{1}{2}x) dx$  
    (c) $\int_2^3 (1 - \frac{1}{2}x) dx$  
    (d) $\int_0^3 (1 - \frac{1}{2}x) dx$
15. (a) $\int_0^5 2 dx$  
    (b) $\int_0^\pi \cos x dx$  
    (c) $\int_{-1}^2 |2x - 3| dx$  
    (d) $\int_{-1}^1 \sqrt{1 - x^2} dx$
16. (a) $\int_{-10}^{-5} 6 dx$  
    (b) $\int_{-\pi/3}^{\pi/3} \sin x dx$  
    (c) $\int_0^3 |x - 2| dx$  
    (d) $\int_0^2 \sqrt{4 - x^2} dx$

**17. In each part, evaluate the integral, given that $f(x) = \begin{cases} |x - 2|, & x \ge 0 \\ x + 2, & x < 0 \end{cases}$.**  
(a) $\int_{-2}^0 f(x) dx$  
(b) $\int_{-2}^2 f(x) dx$  
(c) $\int_0^6 f(x) dx$  
(d) $\int_{-4}^6 f(x) dx$

**18. In each part, evaluate the integral, given that $f(x) = \begin{cases} 2x, & x \le 1 \\ 2, & x > 1 \end{cases}$.**  
(a) $\int_0^1 f(x) dx$  
(b) $\int_{-1}^1 f(x) dx$  
(c) $\int_1^{10} f(x) dx$  
(d) $\int_{1/2}^5 f(x) dx$

**FOCUS ON CONCEPTS**
**19–20 Use the areas shown in the figures to find (a) $\int_a^b f(x) dx$, (b) $\int_b^c f(x) dx$, (c) $\int_a^c f(x) dx$, (d) $\int_a^d f(x) dx$.**
19. Given areas between boundaries: over $[a, b]$ Area $= 0.8$; over $[b, c]$ Area $= 2.6$ (below axis); over $[c, d]$ Area $= 1.5$ (above axis).
20. Given areas between boundaries: over $[a, b]$ Area $= 10$; over $[b, c]$ Area $= 94$ (below axis); over $[c, d]$ Area $= 9$ (above axis).

**21. Find $\int_{-1}^2 [f(x) + 2g(x)] dx$ if $\int_{-1}^2 f(x) dx = 5$ and $\int_{-1}^2 g(x) dx = -3$.**

**22. Find $\int_1^4 [3f(x) - g(x)] dx$ if $\int_1^4 f(x) dx = 2$ and $\int_1^4 g(x) dx = 10$.**

**23. Find $\int_1^5 f(x) dx$ if $\int_0^1 f(x) dx = -2$ and $\int_0^5 f(x) dx = 1$.**

**24. Find $\int_3^{-2} f(x) dx$ if $\int_{-2}^1 f(x) dx = 2$ and $\int_1^3 f(x) dx = -6$.**

**25–28 Use Theorem 4.5.4 and appropriate formulas from geometry to evaluate the integrals.**
25. $\int_{-1}^3 (4 - 5x) dx$
26. $\int_{-2}^2 (1 - 3|x|) dx$
27. $\int_0^1 (x + 2\sqrt{1 - x^2}) dx$
28. $\int_{-3}^0 (2 + \sqrt{9 - x^2}) dx$

**29–32 True–False Determine whether the statement is true or false. Explain your answer.**
29. If $f(x)$ is integrable on $[a, b]$, then $f(x)$ is continuous on $[a, b]$.
30. It is the case that $0 < \int_{-1}^1 \frac{\cos x}{\sqrt{1 + x^2}} dx$.
31. If the integral of $f(x)$ over the interval $[a, b]$ is negative, then $f(x) \le 0$ for $a \le x \le b$.
32. The function $f(x) = \begin{cases} 0, & x \le 0 \\ x^2, & x > 0 \end{cases}$ is integrable over every closed interval $[a, b]$.

**33–34 Use Theorem 4.5.6 to determine whether the value of the integral is positive or negative.**
33. (a) $\int_2^3 \frac{\sqrt{x}}{1 - x} dx$  
    (b) $\int_0^4 \frac{x^2}{3 - \cos x} dx$
34. (a) $\int_{-3}^{-1} \frac{x^4}{\sqrt{3 - x}} dx$  
    (b) $\int_{-2}^2 \frac{x^3 - 9}{|x| + 1} dx$

**35. Prove that if $f$ is continuous and if $m \le f(x) \le M$ on $[a, b]$, then $m(b - a) \le \int_a^b f(x) dx \le M(b - a)$.**

**36. Find the maximum and minimum values of $\sqrt{x^3 + 2}$ for $0 \le x \le 3$. Use these values, and the inequalities in Exercise 35, to find bounds on the value of the integral $\int_0^3 \sqrt{x^3 + 2} dx$.**

**37–38 Evaluate the integrals by completing the square and applying appropriate formulas from geometry.**
37. $\int_0^{10} \sqrt{10x - x^2} dx$
38. $\int_0^3 \sqrt{6x - x^2} dx$

**39–40 Evaluate the limit by expressing it as a definite integral over the interval $[a, b]$ and applying appropriate formulas from geometry.**
39. $\lim_{\max \Delta x_k \to 0} \sum_{k=1}^n (3x_k^* + 1)\Delta x_k; \quad a = 0, b = 1$
40. $\lim_{\max \Delta x_k \to 0} \sum_{k=1}^n \sqrt{4 - (x_k^*)^2}\Delta x_k; \quad a = -2, b = 2$

**FOCUS ON CONCEPTS**
41. Let $f(x) = C$ be a constant function.  
(a) Use a formula from geometry to show that $\int_a^b f(x) dx = C(b - a)$.  
(b) Show that any Riemann sum for $f(x)$ over $[a, b]$ evaluates to $C(b - a)$. Use Definition 4.5.1 to show that $\int_a^b f(x) dx = C(b - a)$.
42. Define a function $f$ on $[0, 1]$ by $f(x) = \begin{cases} 1, & 0 < x \le 1 \\ 0, & x = 0 \end{cases}$. Use Definition 4.5.1 to show that $\int_0^1 f(x) dx = 1$.
43. It can be shown that every interval contains both rational and irrational numbers. Accepting this to be so, do you believe that the function $f(x) = \begin{cases} 1, & \text{if } x \text{ is rational} \\ 0, & \text{if } x \text{ is irrational} \end{cases}$ is integrable on a closed interval $[a, b]$? Explain your reasoning.
44. Define the function $f$ by $f(x) = \begin{cases} 1/x, & x \neq 0 \\ 0, & x = 0 \end{cases}$. Prove using Definition 4.5.1 that $f$ is not integrable on $[0, 1]$.
45. In each part, use Theorems 4.5.2 and 4.5.8 to determine whether the function $f$ is integrable on the interval $[-1, 1]$:  
(a) $f(x) = \cos x$  
(b) $f(x) = \begin{cases} x/|x|, & x \neq 0 \\ 0, & x = 0 \end{cases}$  
(c) $f(x) = \begin{cases} 1/x^2, & x \neq 0 \\ 0, & x = 0 \end{cases}$  
(d) $f(x) = \begin{cases} \sin(1/x), & x \neq 0 \\ 0, & x = 0 \end{cases}$
46. **Writing.** Write a short paragraph that discusses the similarities and differences between indefinite integrals and definite integrals.
47. **Writing.** Write a paragraph that explains informally what it means for a function to be "integrable."

---

## 4.6 THE FUNDAMENTAL THEOREM OF CALCULUS

In this section we will establish two basic relationships between definite and indefinite integrals that together constitute a result called the "Fundamental Theorem of Calculus."

### THE FUNDAMENTAL THEOREM OF CALCULUS (PART 1)

> **4.6.1 THEOREM (The Fundamental Theorem of Calculus, Part 1)**  
> If $f$ is continuous on $[a, b]$ and $F$ is any antiderivative of $f$ on $[a, b]$, then
> $$\int_a^b f(x) dx = F(b) - F(a) \tag{2}$$

#### Proof:
Let $x_1, x_2, \dots, x_{n-1}$ be any points in $[a, b]$ such that $a < x_1 < x_2 < \dots < x_{n-1} < b$. These values divide $[a, b]$ into $n$ subintervals $[a, x_1], [x_1, x_2], \dots, [x_{n-1}, b]$ whose lengths are $\Delta x_1, \Delta x_2, \dots, \Delta x_n$. By hypothesis, $F'(x) = f(x)$ for all $x$ in $[a, b]$, so $F$ satisfies the hypotheses of the Mean-Value Theorem (3.8.2) on each subinterval. Hence, there exist points $x_k^* \in [x_{k-1}, x_k]$ such that
$$F(x_1) - F(a) = F'(x_1^*)(x_1 - a) = f(x_1^*)\Delta x_1$$
$$F(x_2) - F(x_1) = F'(x_2^*)(x_2 - x_1) = f(x_2^*)\Delta x_2$$
$$\vdots$$
$$F(b) - F(x_{n-1}) = F'(x_n^*)(b - x_{n-1}) = f(x_n^*)\Delta x_n$$
Adding the preceding equations yields
$$F(b) - F(a) = \sum_{k=1}^n f(x_k^*)\Delta x_k \tag{4}$$
Let us now increase $n$ in such a way that $\max \Delta x_k \to 0$. Since $f$ is continuous, the right side of (4) approaches $\int_a^b f(x) dx$. However, the left side is independent of $n$. Thus:
$$F(b) - F(a) = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n f(x_k^*)\Delta x_k = \int_a^b f(x) dx \quad \blacksquare$$

It is standard to denote $F(b) - F(a)$ as $F(x)\Big|_a^b$ or $[F(x)]_a^b$.

#### Examples 1–5:
* $\int_1^2 x dx = \left[\frac{1}{2}x^2\right]_1^2 = \frac{1}{2}(4) - \frac{1}{2}(1) = \frac{3}{2}$
* $\int_0^3 (9 - x^2) dx = \left[9x - \frac{x^3}{3}\right]_0^3 = (27 - 9) - 0 = 18$
* $\int_0^{\pi/2} \cos x dx = [\sin x]_0^{\pi/2} = \sin(\pi/2) - \sin 0 = 1$
* $\int_1^9 \sqrt{x} dx = \left[\frac{2}{3}x^{3/2}\right]_1^9 = \frac{2}{3}(27 - 1) = \frac{52}{3}$
* $\int_4^9 x^2\sqrt{x} dx = \int_4^9 x^{5/2} dx = \left[\frac{2}{7}x^{7/2}\right]_4^9 = \frac{2}{7}(2187 - 128) = \frac{4118}{7} = 588\frac{2}{7}$
* $\int_0^{\pi/2} \frac{\sin x}{5} dx = \left[-\frac{1}{5}\cos x\right]_0^{\pi/2} = -\frac{1}{5}(0 - 1) = \frac{1}{5}$
* $\int_0^{\pi/3} \sec^2 x dx = [\tan x]_0^{\pi/3} = \sqrt{3} - 0 = \sqrt{3}$
* $\int_{-\pi/4}^{\pi/4} \sec x \tan x dx = [\sec x]_{-\pi/4}^{\pi/4} = \sqrt{2} - \sqrt{2} = 0$

#### Example 7 (Piecewise Functions)
Evaluate $\int_0^3 f(x) dx$ where $f(x) = \begin{cases} x^2, & x < 2 \\ 3x - 2, & x \ge 2 \end{cases}$:
$$\int_0^3 f(x) dx = \int_0^2 x^2 dx + \int_2^3 (3x - 2) dx = \left[\frac{x^3}{3}\right]_0^2 + \left[\frac{3x^2}{2} - 2x\right]_2^3 = \frac{8}{3} + \left(\frac{15}{2} - 2\right) = \frac{49}{6}$$

### TOTAL AREA
$$\text{Total Area} = \int_a^b |f(x)| dx \tag{7}$$

#### Example 8
Total area between $y = 1 - x^2$ and the $x$-axis over $[0, 2]$:
$$A = \int_0^1 (1 - x^2) dx + \int_1^2 -(1 - x^2) dx = \left[x - \frac{x^3}{3}\right]_0^1 - \left[x - \frac{x^3}{3}\right]_1^2 = \frac{2}{3} - \left(-\frac{4}{3}\right) = 2$$

---

### THE MEAN-VALUE THEOREM FOR INTEGRALS

> **4.6.2 THEOREM (The Mean-Value Theorem for Integrals)**  
> If $f$ is continuous on a closed interval $[a, b]$, then there is at least one point $x^*$ in $[a, b]$ such that
> $$\int_a^b f(x) dx = f(x^*)(b - a) \tag{8}$$

#### Example 9
For $f(x) = x^2$ on $[1, 4]$, $\int_1^4 x^2 dx = 21$. Setting $f(x^*)(4 - 1) = 3(x^*)^2 = 21 \implies (x^*)^2 = 7 \implies x^* = \sqrt{7} \approx 2.65 \in [1, 4]$.

---

### PART 2 OF THE FUNDAMENTAL THEOREM OF CALCULUS

> **4.6.3 THEOREM (The Fundamental Theorem of Calculus, Part 2)**  
> If $f$ is continuous on an interval, then $f$ has an antiderivative on that interval. In particular, if $a$ is any point in the interval, then the function $F$ defined by
> $$F(x) = \int_a^x f(t) dt$$
> is an antiderivative of $f$; that is, $F'(x) = f(x)$ for each $x$ in the interval, or in alternative notation:
> $$\frac{d}{dx}\left[\int_a^x f(t) dt\right] = f(x) \tag{11}$$

#### Examples 10–11:
* $\frac{d}{dx}\left[\int_1^x t^3 dt\right] = x^3$
* $\frac{d}{dx}\left[\int_1^x \frac{\sin t}{t} dt\right] = \frac{\sin x}{x}$ on $(0, +\infty)$

### INTEGRATING RATES OF CHANGE

> **4.6.4 PRINCIPLE**  
> Integrating the rate of change of $F(x)$ over an interval $[a, b]$ produces the change in the value of $F(x)$ that occurs as $x$ increases from $a$ to $b$:
> $$\int_a^b F'(x) dx = F(b) - F(a)$$

---

### QUICK CHECK EXERCISES 4.6
*(See page 322 for answers.)*

1. (a) If $F(x)$ is an antiderivative for $f(x)$, then $\int_a^b f(x) dx = \underline{\hspace{1cm}}$.  
   (b) $\int_a^b F'(x) dx = \underline{\hspace{1cm}}$.  
   (c) $\frac{d}{dx}\left[\int_a^x f(t) dt\right] = \underline{\hspace{1cm}}$.
2. (a) $\int_0^2 (3x^2 - 2x) dx = \underline{\hspace{1cm}}$  
   (b) $\int_{-\pi}^\pi \cos x dx = \underline{\hspace{1cm}}$
3. For the function $f(x) = 3x^2 - 2x$ and an interval $[a, b]$, the point $x^*$ guaranteed by the Mean-Value Theorem for Integrals is $x^* = 2/3$. It follows that $\int_a^b (3x^2 - 2x) dx = \underline{\hspace{1cm}}$.
4. The area of an oil spill is increasing at a rate of $25t \text{ ft}^2/\text{s}$ $t$ seconds after the spill. Between times $t = 2$ and $t = 4$ the area of the spill increases by $\underline{\hspace{1cm}}\text{ ft}^2$.

#### QUICK CHECK ANSWERS 4.6
1. (a) $F(b) - F(a)$ (b) $F(b) - F(a)$ (c) $f(x)$  
2. (a) $4$ (b) $0$  
3. $0$  
4. $150\text{ ft}^2$

---

### EXERCISE SET 4.6

**1. In each part, use a definite integral to find the area of the region, and check your answer using an appropriate formula from geometry.**  
(a) Region under $y = 2 - x$ over $[0, 2]$.  
(b) Region under $y = 2$ over $[-1, 1]$.  
(c) Region under $y = x + 1$ over $[0, 3]$.

**2. In each part, use a definite integral to find the area under the curve $y = f(x)$ over the stated interval, and check your answer using an appropriate formula from geometry.**  
(a) $f(x) = x; \quad [0, 5]$  
(b) $f(x) = 5; \quad [3, 9]$  
(c) $f(x) = x + 3; \quad [-1, 2]$

**3–4 Sketch the analogue of Figure 4.6.10 for the specified region/function, label $x^*$ and $f(x^*)$, and determine all values of $x^*$ that satisfy Equation (8).**  
3. (a) Region in 1(a). (b) Region in 1(b). (c) Region in 1(c).  
4. (a) Region in 2(a). (b) Region in 2(b). (c) Region in 2(c).

**5–8 Find the area under the curve $y = f(x)$ over the stated interval.**  
5. $f(x) = x^3; \quad [2, 3]$  
6. $f(x) = x^4; \quad [-1, 1]$  
7. $f(x) = 3\sqrt{x}; \quad [1, 4]$  
8. $f(x) = x^{-2/3}; \quad [1, 27]$

**9–10 Find all values of $x^*$ in the stated interval that satisfy Equation (8) in the Mean-Value Theorem for Integrals (4.6.2), and explain what these numbers represent.**  
9. (a) $f(x) = \sqrt{x}; \quad [0, 3]$  
   (b) $f(x) = x^2 + x; \quad [-12, 0]$  
10. (a) $f(x) = \sin x; \quad [-\pi, \pi]$  
    (b) $f(x) = 1/x^2; \quad [1, 3]$

**11–22 Evaluate the integrals using Part 1 of the Fundamental Theorem of Calculus.**  
11. $\int_{-2}^1 (x^2 - 6x + 12) dx$  
12. $\int_{-1}^2 4x(1 - x^2) dx$  
13. $\int_1^4 \frac{4}{x^2} dx$  
14. $\int_1^2 \frac{1}{x^6} dx$  
15. $\int_4^9 2x\sqrt{x} dx$  
16. $\int_1^4 \frac{1}{x\sqrt{x}} dx$  
17. $\int_{-\pi/2}^{\pi/2} \sin\theta d\theta$  
18. $\int_0^{\pi/4} \sec^2\theta d\theta$  
19. $\int_{-\pi/4}^{\pi/4} \cos x dx$  
20. $\int_0^{\pi/3} (2x - \sec x \tan x) dx$  
21. $\int_1^4 \left(\frac{1}{\sqrt{t}} - 3\sqrt{t}\right) dt$  
22. $\int_{\pi/6}^{\pi/2} \left(x + \frac{2}{\sin^2 x}\right) dx$

**23–24 Use Theorem 4.5.5 to evaluate the given integrals.**  
23. (a) $\int_{-1}^1 |2x - 1| dx$  
    (b) $\int_0^{3\pi/4} |\cos x| dx$  
24. (a) $\int_{-1}^2 \sqrt{2 + |x|} dx$  
    (b) $\int_0^{\pi/2} |\frac{1}{2} - \cos x| dx$

**25–26 A function $f(x)$ is defined piecewise on an interval. In these exercises: (a) Use Theorem 4.5.5 to find the integral of $f(x)$ over the interval. (b) Find an antiderivative of $f(x)$ on the interval. (c) Use parts (a) and (b) to verify Part 1 of the Fundamental Theorem of Calculus.**  
25. $f(x) = \begin{cases} x, & 0 \le x \le 1 \\ x^2, & 1 < x \le 2 \end{cases}$  
26. $f(x) = \begin{cases} \sqrt{x}, & 0 \le x < 1 \\ 1/x^2, & 1 \le x \le 4 \end{cases}$

**27–30 True–False Determine whether the statement is true or false. Explain your answer.**  
27. There does not exist a differentiable function $F(x)$ such that $F'(x) = |x|$.  
28. If $f(x)$ is continuous on the interval $[a, b]$, and if the definite integral of $f(x)$ over this interval has value 0, then the equation $f(x) = 0$ has at least one solution in the interval $[a, b]$.  
29. If $F(x)$ is an antiderivative of $f(x)$ and $G(x)$ is an antiderivative of $g(x)$, then $\int_a^b f(x) dx = \int_a^b g(x) dx$ if and only if $G(a) + F(b) = F(a) + G(b)$.  
30. If $f(x)$ is continuous everywhere and $F(x) = \int_0^x f(t) dt$, then the equation $F(x) = 0$ has at least one solution.

**31–34 Use a calculating utility to find the midpoint approximation of the integral using $n = 20$ subintervals, and then find the exact value of the integral using Part 1 of the Fundamental Theorem of Calculus.**  
31. $\int_1^3 \frac{1}{x^2} dx$  
32. $\int_0^{\pi/2} \sin x dx$  
33. $\int_{-1}^1 \sec^2 x dx$  
34. $\int_1^5 \frac{1}{x^3} dx$

**35–38 Sketch the region described and find its area.**  
35. The region under the curve $y = x^2 + 1$ and over the interval $[0, 3]$.  
36. The region below the curve $y = x - x^2$ and above the $x$-axis.  
37. The region under the curve $y = 3\sin x$ and over the interval $[0, 2\pi/3]$.  
38. The region below the interval $[-2, -1]$ and above the curve $y = x^3$.

**39–42 Sketch the curve and find the total area between the curve and the given interval on the $x$-axis.**  
39. $y = x^2 - x; \quad [0, 2]$  
40. $y = \sin x; \quad [0, 3\pi/2]$  
41. $y = 2\sqrt{x+1} - 3; \quad [0, 3]$  
42. $y = \frac{x^2 - 1}{x^2}; \quad [1/2, 2]$

**43. A student wants to find the area enclosed by the graphs of $y = \cos x, \; y = 0, \; x = 0,$ and $x = 0.8$.**  
(a) Show that the exact area is $\sin 0.8$.  
(b) The student uses a calculator to approximate the result in part (a) to three decimal places and obtains an incorrect answer of 0.014. What was the student's error? Find the correct approximation.

**FOCUS ON CONCEPTS**  
44. Explain why the Fundamental Theorem of Calculus may be applied without modification to definite integrals in which the lower limit of integration is greater than or equal to the upper limit of integration.  
45. (a) If $h'(t)$ is the rate of change of a child's height measured in inches per year, what does $\int_0^{10} h'(t) dt$ represent, and what are its units?  
    (b) If $r'(t)$ is the rate of change of the radius of a spherical balloon measured in centimeters per second, what does $\int_1^2 r'(t) dt$ represent, and what are its units?  
    (c) If $H'(t)$ is the rate of change of the speed of sound with respect to temperature measured in $\text{ft/s}$ per $^\circ\text{F}$, what does $\int_{32}^{100} H'(t) dt$ represent, and what are its units?  
    (d) If $v(t)$ is the velocity of a particle in rectilinear motion, measured in $\text{cm/h}$, what does $\int_{t_1}^{t_2} v(t) dt$ represent, and what are its units?  
46. (a) Use a graphing utility to generate the graph of $f(x) = \frac{1}{100}(x + 2)(x + 1)(x - 3)(x - 5)$ and make a conjecture about the sign of $\int_{-2}^5 f(x) dx$.  
    (b) Check your conjecture by evaluating the integral.

**47. Define $F(x)$ by $F(x) = \int_1^x (3t^2 - 3) dt$.**  
(a) Use Part 2 of the Fundamental Theorem of Calculus to find $F'(x)$.  
(b) Check the result in part (a) by first integrating and then differentiating.

**48. Define $F(x)$ by $F(x) = \int_{\pi/4}^x \cos 2t dt$.**  
(a) Use Part 2 of the Fundamental Theorem of Calculus to find $F'(x)$.  
(b) Check the result in part (a) by first integrating and then differentiating.

**49–52 Use Part 2 of the Fundamental Theorem of Calculus to find the derivatives.**  
49. (a) $\frac{d}{dx}\left[\int_1^x \sin(t^2) dt\right]$  
    (b) $\frac{d}{dx}\left[\int_1^x \sqrt{1 - \cos t} dt\right]$  
50. (a) $\frac{d}{dx}\left[\int_0^x \frac{dt}{1 + \sqrt{t}}\right]$  
    (b) $\frac{d}{dx}\left[\int_2^x \frac{dt}{t^2 + 3t - 4}\right]$  
51. $\frac{d}{dx}\left[\int_x^0 t\sec t dt\right]$ [Hint: Use Definition 4.5.3(b).]  
52. $\frac{d}{du}\left[\int_0^u |x| dx\right]$

**53. Let $F(x) = \int_4^x \sqrt{t^2 + 9} dt$. Find (a) $F(4)$ (b) $F'(4)$ (c) $F''(4)$.**

**54. Let $F(x) = \int_0^x \frac{\cos t}{t^2 + 3t + 5} dt$. Find (a) $F(0)$ (b) $F'(0)$ (c) $F''(0)$.**

**55. Let $F(x) = \int_0^x \frac{t - 3}{t^2 + 7} dt$ for $-\infty < x < +\infty$.**  
(a) Find the value of $x$ where $F$ attains its minimum value.  
(b) Find intervals over which $F$ is only increasing or only decreasing.  
(c) Find open intervals over which $F$ is only concave up or only concave down.

**56. [CAS] Use plotting and numerical integration commands of a CAS to generate the graph of the function $F$ in Exercise 55 over $[-20, 20]$, and confirm consistency.**

**57. (a) Over what open interval does the formula $F(x) = \int_1^x \frac{dt}{t}$ represent an antiderivative of $f(x) = 1/x$?**  
(b) Find a point where the graph of $F$ crosses the $x$-axis.

**58. (a) Over what open interval does the formula $F(x) = \int_1^x \frac{1}{t^2 - 9} dt$ represent an antiderivative of $f(x) = \frac{1}{x^2 - 9}$?**  
(b) Find a point where the graph of $F$ crosses the $x$-axis.

**59. Water Reservoir Problem**  
(a) Constant rate $r = 4\text{ gal/min}$ between 8:30 a.m. and 9:00 a.m. Total water supplied?  
(b) Water consumption increases linearly between 9:00 a.m. and 10:00 a.m. from $4\text{ gal/min}$ to $9\text{ gal/min}$. Total water supplied during that hour?  
(c) From 10:00 a.m. to 12 noon, rate $r(t) = 10 + \sqrt{t}\text{ gal/min}$ where $t$ is time in minutes since 10:00 a.m. Total water supplied during that 2-hour period?

**60. A traffic engineer monitors the rate at which cars enter the main highway during the afternoon rush hour: $R(t) = 100(1 - 0.0001t^2)\text{ cars/min}$ for $0 \le t \le 60$.**  
(a) When does the peak traffic flow into the highway occur?  
(b) Estimate the number of cars that enter the highway during the rush hour.

**61–62 Evaluate each limit by interpreting it as a Riemann sum in which the given interval is divided into $n$ subintervals of equal width.**  
61. $\lim_{n \to +\infty} \sum_{k=1}^n \frac{\pi}{4n}\sec^2\left(\frac{\pi k}{4n}\right); \quad [0, \pi/4]$  
62. $\lim_{n \to +\infty} \sum_{k=1}^n \frac{n}{(n + k)^2}; \quad [1, 2]$

**63. Prove the Mean-Value Theorem for Integrals (Theorem 4.6.2) by applying the Mean-Value Theorem (3.8.2) to an antiderivative $F$ for $f$.**

**64. Writing.** Write a short paragraph that describes the various ways in which integration and differentiation may be viewed as inverse processes. (Be sure to discuss both definite and indefinite integrals.)

**65. Writing.** Let $f$ denote a function that is continuous on an interval $[a, b]$, and let $x^*$ denote the point guaranteed by the Mean-Value Theorem for Integrals. Explain geometrically why $f(x^*)$ may be interpreted as a "mean" or average value of $f(x)$ over $[a, b]$.

---

## 4.7 RECTILINEAR MOTION REVISITED USING INTEGRATION

In Section 3.6 we used the derivative to define the notions of instantaneous velocity and acceleration for a particle in rectilinear motion. In this section we will resume the study of such motion using the tools of integration.

### FINDING POSITION AND VELOCITY BY INTEGRATION

Recall that $v(t) = s'(t)$ and $a(t) = v'(t)$. It follows that $s(t)$ is an antiderivative of $v(t)$ and $v(t)$ is an antiderivative of $a(t)$:
$$s(t) = \int v(t) dt \quad \text{and} \quad v(t) = \int a(t) dt \tag{1–2}$$

#### Example 1
Suppose that a particle moves with velocity $v(t) = \cos \pi t$ along a coordinate line. Assuming that the particle has coordinate $s = 4$ at time $t = 0$, find its position function.  
**Solution.** $s(t) = \int \cos \pi t dt = \frac{1}{\pi}\sin \pi t + C$. Since $s(0) = 4$, $4 = \frac{1}{\pi}\sin 0 + C \implies C = 4$. Thus:
$$s(t) = \frac{1}{\pi}\sin \pi t + 4$$

### COMPUTING DISPLACEMENT AND DISTANCE TRAVELED

* **Displacement:**
  $$\text{displacement over } [t_0, t_1] = \int_{t_0}^{t_1} v(t) dt = \int_{t_0}^{t_1} s'(t) dt = s(t_1) - s(t_0) \tag{3}$$
* **Distance Traveled:**
  $$\text{distance traveled during } [t_0, t_1] = \int_{t_0}^{t_1} |v(t)| dt \tag{4}$$

#### Example 2
Suppose $v(t) = t^2 - 2t\text{ m/s}$ ($0 \le t \le 3$).  
(a) Displacement: $\int_0^3 (t^2 - 2t) dt = \left[\frac{t^3}{3} - t^2\right]_0^3 = 9 - 9 = 0\text{ m}$.  
(b) Distance traveled: $v(t) \le 0$ on $[0, 2]$ and $v(t) \ge 0$ on $[2, 3]$:
$$\int_0^3 |v(t)| dt = \int_0^2 -(t^2 - 2t) dt + \int_2^3 (t^2 - 2t) dt = \frac{4}{3} + \frac{4}{3} = \frac{8}{3}\text{ m}$$

---

### ANALYZING THE VELOCITY VERSUS TIME CURVE

> **4.7.1 PRINCIPLE**  
> For a particle in rectilinear motion, the net signed area between the velocity versus time curve and the interval $[t_0, t_1]$ on the $t$-axis represents the displacement of the particle over that time interval, and the total area between the velocity versus time curve and the interval $[t_0, t_1]$ represents the distance traveled.

#### Example 3
Analyzing curves in Figure 4.7.5:
* (a) Net signed area $= 2$, total area $= 2 \implies$ displacement $= 2$, distance $= 2$.
* (b) Net signed area $= -2$, total area $= 2 \implies$ displacement $= -2$, distance $= 2$.
* (c) Net signed area $= 0$, total area $= 2 \implies$ displacement $= 0$, distance $= 2$.

---

### CONSTANT ACCELERATION

> **4.7.2 THEOREM (Constant Acceleration)**  
> If a particle moves with constant acceleration $a$ along an $s$-axis, and if the position and velocity at time $t = 0$ are $s_0$ and $v_0$, respectively, then:
> $$s(t) = s_0 + v_0 t + \frac{1}{2}at^2 \tag{10}$$
> $$v(t) = v_0 + at \tag{11}$$

#### Example 4 (Spacecraft)
Acceleration $a = 0.032\text{ m/s}^2$, $v_0 = 10,000\text{ m/s}$, $s_0 = 0$. After 1 hour ($t = 3600\text{ s}$):
$$s(3600) = 10,000(3600) + \frac{1}{2}(0.032)(3600)^2 \approx 36,200,000\text{ m}$$
$$v(3600) = 10,000 + (0.032)(3600) \approx 10,100\text{ m/s}$$

#### Example 5 (Woman Catching Bus)
Bus starts from rest with $a = 1\text{ m/s}^2$. Woman runs at $5\text{ m/s}$, starts $11\text{ m}$ behind door.
$s_w(t) = 5t, \; s_b(t) = \frac{1}{2}t^2$.
$5t = \frac{1}{2}t^2 + 11 \implies t^2 - 10t + 22 = 0 \implies t = 5 \pm \sqrt{3} \approx 3.3\text{ s}$ and $6.7\text{ s}$.

---

### FREE-FALL MODEL

With upward as positive direction ($a(t) = -g$, where $g \approx 9.8\text{ m/s}^2$ or $32\text{ ft/s}^2$):
$$s(t) = s_0 + v_0 t - \frac{1}{2}gt^2 \tag{15}$$
$$v(t) = v_0 - gt \tag{16}$$

#### Example 6 (Nolan Ryan in Astrodome)
Ceiling $208\text{ ft}$. $s_0 = 7\text{ ft}$, $v_0 = 100\text{ ft/s}$, $g = 32\text{ ft/s}^2$.
$v(t) = 100 - 32t = 0 \implies t = 25/8\text{ s}$.
$s(25/8) = 7 + 100(25/8) - 16(25/8)^2 = 163.25\text{ ft}$ (roughly $45\text{ ft}$ short of ceiling).

#### Example 7 (Empire State Building Penny Drop)
Height $s_0 = 1250\text{ ft}$, $v_0 = 0$.
$s(t) = 1250 - 16t^2 = 0 \implies t = \frac{25}{\sqrt{8}} \approx 8.8\text{ s}$.
Speed at impact: $|v| = 32\left(\frac{25}{\sqrt{8}}\right) = 200\sqrt{2} \approx 282.8\text{ ft/s}$ (more than $192\text{ mi/h}$).

---

### QUICK CHECK EXERCISES 4.7
*(See page 331 for answers.)*

1. Suppose that a particle is moving along an $s$-axis with velocity $v(t) = 2t + 1$. If at time $t = 0$ the particle is at position $s = 2$, the position function of the particle is $s(t) = \underline{\hspace{1cm}}$.
2. Let $v(t)$ denote the velocity function of a particle that is moving along an $s$-axis with constant acceleration $a = -2$. If $v(1) = 4$, then $v(t) = \underline{\hspace{1cm}}$.
3. Let $v(t)$ denote the velocity function of a particle in rectilinear motion. Suppose that $v(0) = -1, v(3) = 2$, and the velocity versus time curve is a straight line. The displacement of the particle between times $t = 0$ and $t = 3$ is $\underline{\hspace{1cm}}$, and the distance traveled by the particle over this period of time is $\underline{\hspace{1cm}}$.
4. Based on the free-fall model, from what height must a coin be dropped so that it strikes the ground with speed $48\text{ ft/s}$?

#### QUICK CHECK ANSWERS 4.7
1. $t^2 + t + 2$  
2. $6 - 2t$  
3. $\frac{3}{2}; \; \frac{5}{2}$  
4. $36\text{ ft}$

---

### EXERCISE SET 4.7

**FOCUS ON CONCEPTS**
**1. In each part, the velocity versus time curve is given for a particle moving along a line. Use the curve to find the displacement and the distance traveled by the particle over the time interval $0 \le t \le 3$.**  
(a) Constant velocity $v = 1$ from $t = 0$ to $t = 3$.  
(b) Linear velocity from $(0, 1)$ to $(3, -1)$.  
(c) Triangular pulse from $v = 0$ at $t = 0$ to $v = 1$ at $t = 1.5$ to $v = 0$ at $t = 3$.  
(d) Piecewise linear with positive and negative sections.

**2. Given a push, a ball rolls up an inclined plane and returns to its original position after 4 s. If the total distance traveled by the ball is 16 ft, sketch a velocity versus time curve for the ball.**

**3. The accompanying figure shows the acceleration versus time curve for a particle moving along a coordinate line. If the initial velocity of the particle is $20\text{ m/s}$, estimate (a) the velocity at time $t = 4\text{ s}$ (b) the velocity at time $t = 6\text{ s}$.**

**4. The accompanying figure shows the velocity versus time curve over the time interval $1 \le t \le 5$ for a particle moving along a horizontal coordinate line.**  
(a) What can you say about the sign of the acceleration over the time interval?  
(b) When is the particle speeding up? Slowing down?  
(c) What can you say about the location of the particle at time $t = 5$ relative to its location at time $t = 1$? Explain your reasoning.

**5–8 A particle moves along an $s$-axis. Use the given information to find the position function of the particle.**
5. (a) $v(t) = 3t^2 - 2t; \quad s(0) = 1$  
   (b) $a(t) = 3\sin 3t; \quad v(0) = 3; \quad s(0) = 3$
6. (a) $v(t) = 1 + \sin t; \quad s(0) = -3$  
   (b) $a(t) = t^2 - 3t + 1; \quad v(0) = 0; \quad s(0) = 0$
7. (a) $v(t) = 3t + 1; \quad s(2) = 4$  
   (b) $a(t) = 2t^{-3}; \quad v(1) = 0; \quad s(1) = 2$
8. (a) $v(t) = t^{2/3}; \quad s(8) = 0$  
   (b) $a(t) = \sqrt{t}; \quad v(4) = 1; \quad s(4) = -5$

**9–12 A particle moves with a velocity of $v(t)\text{ m/s}$ along an $s$-axis. Find the displacement and the distance traveled by the particle during the given time interval.**
9. (a) $v(t) = \sin t; \quad 0 \le t \le \pi/2$  
   (b) $v(t) = \cos t; \quad \pi/2 \le t \le 2\pi$
10. (a) $v(t) = 3t - 2; \quad 0 \le t \le 2$  
    (b) $v(t) = |1 - 2t|; \quad 0 \le t \le 2$
11. (a) $v(t) = t^3 - 3t^2 + 2t; \quad 0 \le t \le 3$  
    (b) $v(t) = \sqrt{t} - 2; \quad 0 \le t \le 3$
12. (a) $v(t) = t - \sqrt{t}; \quad 0 \le t \le 4$  
    (b) $v(t) = \frac{1}{\sqrt{t + 1}}; \quad 0 \le t \le 3$

**13–16 A particle moves with acceleration $a(t)\text{ m/s}^2$ along an $s$-axis and has velocity $v_0\text{ m/s}$ at time $t = 0$. Find the displacement and the distance traveled by the particle during the given time interval.**
13. $a(t) = 3; \quad v_0 = -1; \quad 0 \le t \le 2$
14. $a(t) = t - 2; \quad v_0 = 0; \quad 1 \le t \le 5$
15. $a(t) = 1/\sqrt{3t + 1}; \quad v_0 = 4/3; \quad 1 \le t \le 5$
16. $a(t) = \sin t; \quad v_0 = 1; \quad \pi/4 \le t \le \pi/2$

**17. In each part, use the given information to find the position, velocity, speed, and acceleration at time $t = 1$.**  
(a) $v = \sin(\frac{1}{2}\pi t); \quad s = 0 \text{ when } t = 0$  
(b) $a = -3t; \quad s = 1 \text{ and } v = 0 \text{ when } t = 0$

**18. In each part, use the given information to find the position, velocity, speed, and acceleration at time $t = 1$.**  
(a) $v = \cos(\frac{1}{3}\pi t); \quad s = 0 \text{ when } t = 3/2$  
(b) $a = 5t - t^3; \quad s = 1 \text{ and } v = -1/2 \text{ when } t = 0$

**19. The velocity of an ant running along the edge of a shelf is modeled by $v(t) = \begin{cases} 5t, & 0 \le t < 1 \\ \frac{6}{\sqrt{t}} - 1, & 1 \le t \le 2 \end{cases}$ where $t$ is in seconds and $v$ is in cm/s. Estimate the time at which the ant is $4\text{ cm}$ from its starting position.**

**20. The velocity of a mouse running alongside the baseboard of a room is modeled by $v(t) = 3\cos(\pi t/12) - 0.5t$ ($0 \le t \le 8$), where $t$ is in seconds and $v$ is in m/s. Estimate the time(s) at which the mouse is $2\text{ m}$ from its starting position.**

**21. Suppose that the velocity function of a particle moving along an $s$-axis is $v(t) = 20t^2 - 110t + 120\text{ ft/s}$ and that the particle is at the origin at time $t = 0$. Use a graphing utility to generate the graphs of $s(t), v(t),$ and $a(t)$ for the first 6 s of motion.**

**22. Suppose that the acceleration function of a particle moving along an $s$-axis is $a(t) = 4t - 30\text{ m/s}^2$ and that the position and velocity at time $t = 0$ are $s_0 = -5\text{ m}$ and $v_0 = 3\text{ m/s}$. Use a graphing utility to generate the graphs of $s(t), v(t),$ and $a(t)$ for the first 25 s of motion.**

**23–26 True–False Determine whether the statement is true or false. Explain your answer. Each question refers to a particle in rectilinear motion.**
23. If the particle has constant acceleration, the velocity versus time graph will be a straight line.
24. If the particle has constant nonzero acceleration, its position versus time curve will be a parabola.
25. If the total area between the velocity versus time curve and a time interval $[a, b]$ is positive, then the displacement of the particle over this time interval will be nonzero.
26. If $D(t)$ denotes the distance traveled by the particle over the time interval $[0, t]$, then $D(t)$ is an antiderivative for the speed of the particle.

**27–28 [CAS] For the given velocity function $v(t)$: (a) Generate the velocity versus time curve, and use it to make a conjecture about the sign of the displacement over the given time interval. (b) Use a CAS to find the displacement.**
27. $v(t) = 0.5 - t\sin t; \quad 0 \le t \le 5$
28. $v(t) = 0.5 - t\cos \pi t; \quad 0 \le t \le 1$

**29. Suppose that at time $t = 0$ a particle is at the origin of an $x$-axis and has a velocity of $v_0 = 25\text{ cm/s}$. For the first 4 s thereafter it has no acceleration, and then it is acted on by a retarding force that produces a constant negative acceleration of $a = -10\text{ cm/s}^2$.**  
(a) Sketch the acceleration versus time curve over the interval $0 \le t \le 12$.  
(b) Sketch the velocity versus time curve over the time interval $0 \le t \le 12$.  
(c) Find the $x$-coordinate of the particle at times $t = 8\text{ s}$ and $t = 12\text{ s}$.  
(d) What is the maximum $x$-coordinate of the particle over the time interval $0 \le t \le 12$?

**30–36 In these exercises assume that the object is moving with constant acceleration in the positive direction of a coordinate line, and apply Formulas (10) and (11) as appropriate. ($88\text{ ft/s} = 60\text{ mi/h}$.)**
30. A car traveling $60\text{ mi/h}$ along a straight road decelerates at a constant rate of $11\text{ ft/s}^2$.  
    (a) How long will it take until the speed is $45\text{ mi/h}$?  
    (b) How far will the car travel before coming to a stop?
31. Spotting a police car, you hit the brakes on your new Porsche to reduce your speed from $90\text{ mi/h}$ to $60\text{ mi/h}$ at a constant rate over a distance of $200\text{ ft}$.  
    (a) Find the acceleration in $\text{ft/s}^2$.  
    (b) How long does it take for you to reduce your speed to $55\text{ mi/h}$?  
    (c) At the acceleration obtained in part (a), how long would it take for you to bring your Porsche to a complete stop from $90\text{ mi/h}$?
32. A particle moving along a straight line is accelerating at a constant rate of $5\text{ m/s}^2$. Find the initial velocity if the particle moves $60\text{ m}$ in the first 4 s.
33. A motorcycle, starting from rest, speeds up with a constant acceleration of $2.6\text{ m/s}^2$. After it has traveled $120\text{ m}$, it slows down with a constant acceleration of $-1.5\text{ m/s}^2$ until it attains a speed of $12\text{ m/s}$. What is the distance traveled by the motorcycle at that point?
34. A sprinter in a $100\text{ m}$ race explodes out of the starting block with an acceleration of $4.0\text{ m/s}^2$, which she sustains for 2.0 s. Her acceleration then drops to zero for the rest of the race.  
    (a) What is her time for the race?  
    (b) Make a graph of her distance from the starting block versus time.
35. A car that has stopped at a toll booth leaves the booth with a constant acceleration of $4\text{ ft/s}^2$. At the time the car leaves the booth it is $2500\text{ ft}$ behind a truck traveling with a constant velocity of $50\text{ ft/s}$. How long will it take for the car to catch the truck, and how far will the car be from the toll booth at that time?
36. In the final sprint of a rowing race the challenger is rowing at a constant speed of $12\text{ m/s}$. At the point where the leader is $100\text{ m}$ from the finish line and the challenger is $15\text{ m}$ behind, the leader is rowing at $8\text{ m/s}$ but starts accelerating at a constant $0.5\text{ m/s}^2$. Who wins?

**37–43 Assume that a free-fall model applies. Solve these exercises by applying Formulas (15) and (16). Take $g = 32\text{ ft/s}^2$ or $g = 9.8\text{ m/s}^2$.**
37. A projectile is launched vertically upward from ground level with an initial velocity of $112\text{ ft/s}$.  
    (a) Find the velocity at $t = 3\text{ s}$ and $t = 5\text{ s}$.  
    (b) How high will the projectile rise?  
    (c) Find the speed of the projectile when it hits the ground.
38. A rock tossed downward from a height of $112\text{ ft}$ reaches the ground in 2 s. What is its initial velocity?
39. A projectile is fired vertically upward from ground level with an initial velocity of $16\text{ ft/s}$.  
    (a) How long will it take for the projectile to hit the ground?  
    (b) How long will the projectile be moving upward?
40. In 1939, Joe Sprinz of the San Francisco Seals Baseball Club attempted to catch a ball dropped from a blimp at a height of $800\text{ ft}$.  
    (a) How long does it take for a ball to drop $800\text{ ft}$?  
    (b) What is the velocity of a ball in miles per hour after an $800\text{ ft}$ drop?
41. A model rocket is launched upward from ground level with an initial speed of $60\text{ m/s}$.  
    (a) How long does it take for the rocket to reach its highest point?  
    (b) How high does the rocket go?  
    (c) How long does it take for the rocket to drop back to the ground from its highest point?  
    (d) What is the speed of the rocket when it hits the ground?
42. (a) Use the results in Exercise 41 to make a conjecture about the relationship between the initial and final speeds of a projectile that is launched upward from ground level and returns to ground level.  
    (b) Prove your conjecture.
43. A model rocket is fired vertically upward with an initial velocity of $49\text{ m/s}$ from a tower $150\text{ m}$ high.  
    (a) How long will it take for the rocket to reach its maximum height?  
    (b) What is the maximum height?  
    (c) How long will it take for the rocket to pass its starting point on the way down?  
    (d) What is the velocity when it passes the starting point on the way down?  
    (e) How long will it take for the rocket to hit the ground?  
    (f) What will be its speed at impact?
44. **Writing.** Make a list of important features of a velocity versus time curve, and interpret each feature in terms of the motion.
45. **Writing.** Use Riemann sums to argue informally that integrating speed over a time interval produces the distance traveled.

---

## 4.8 AVERAGE VALUE OF A FUNCTION AND ITS APPLICATIONS

In this section we will define the notion of the "average value" of a function, and we will give various applications of this idea.

### AVERAGE VELOCITY REVISITED
$$v_{\text{ave}} = \frac{s(t_1) - s(t_0)}{t_1 - t_0} = \frac{1}{t_1 - t_0}\int_{t_0}^{t_1} v(t) dt \tag{1}$$

#### Example 1
$v(t) = 2 + \cos t$ on $[0, \pi]$:
$$v_{\text{ave}} = \frac{1}{\pi - 0}\int_0^\pi (2 + \cos t) dt = \frac{1}{\pi}[2t + \sin t]_0^\pi = \frac{1}{\pi}(2\pi) = 2$$

---

### AVERAGE VALUE OF A CONTINUOUS FUNCTION

> **4.8.1 DEFINITION (Average Value / Mean Value)**  
> If $f$ is continuous on $[a, b]$, then the **average value** (or **mean value**) of $f$ on $[a, b]$ is defined to be
> $$f_{\text{ave}} = \frac{1}{b - a}\int_a^b f(x) dx \tag{3}$$

#### Example 2
Find the average value of $f(x) = \sqrt{x}$ over $[1, 4]$, and find all points in the interval at which the value of $f$ is the same as the average.  
**Solution.**
$$f_{\text{ave}} = \frac{1}{4 - 1}\int_1^4 \sqrt{x} dx = \frac{1}{3}\left[\frac{2x^{3/2}}{3}\right]_1^4 = \frac{1}{3}\left(\frac{16}{3} - \frac{2}{3}\right) = \frac{14}{9} \approx 1.6$$
The $x$-values at which $f(x) = \sqrt{x}$ equals $14/9$ satisfy $\sqrt{x} = 14/9 \implies x = 196/81 \approx 2.4$.

#### Example 3
Show that if a body released from rest is in free fall, then its average velocity over $[0, T]$ is its velocity at time $t = T/2$.  
**Solution.** $v(t) = -gt$.
$$v_{\text{ave}} = \frac{1}{T}\int_0^T -gt dt = -\frac{g}{T}\left[\frac{1}{2}t^2\right]_0^T = -g\frac{T}{2} = v(T/2)$$

---

### QUICK CHECK EXERCISES 4.8
*(See page 336 for answers.)*

1. The arithmetic average of $n$ numbers, $a_1, a_2, \dots, a_n$ is $\underline{\hspace{1cm}}$.
2. If $f$ is continuous on $[a, b]$, then the average value of $f$ on $[a, b]$ is $\underline{\hspace{1cm}}$.
3. If $f$ is continuous on $[a, b]$, then the Mean-Value Theorem for Integrals guarantees that for at least one point $x^*$ in $[a, b]$, $\underline{\hspace{1cm}}$ equals the average value of $f$ on $[a, b]$.
4. The average value of $f(x) = 4x^3$ on $[1, 3]$ is $\underline{\hspace{1cm}}$.

#### QUICK CHECK ANSWERS 4.8
1. $\frac{1}{n}\sum_{k=1}^n a_k$  
2. $\frac{1}{b - a}\int_a^b f(x) dx$  
3. $f(x^*)$  
4. $40$

---

### EXERCISE SET 4.8

**1. (a) Find $f_{\text{ave}}$ of $f(x) = 2x$ over $[0, 4]$.**  
(b) Find a point $x^*$ in $[0, 4]$ such that $f(x^*) = f_{\text{ave}}$.  
(c) Sketch a graph of $f(x) = 2x$ over $[0, 4]$, and construct a rectangle over the interval whose area is the same as the area under the graph of $f$ over the interval.

**2. (a) Find $f_{\text{ave}}$ of $f(x) = x^2$ over $[0, 2]$.**  
(b) Find a point $x^*$ in $[0, 2]$ such that $f(x^*) = f_{\text{ave}}$.  
(c) Sketch a graph of $f(x) = x^2$ over $[0, 2]$, and construct a rectangle over the interval whose area is the same as the area under the graph of $f$ over the interval.

**3–8 Find the average value of the function over the given interval.**
3. $f(x) = 3x; \quad [1, 3]$
4. $f(x) = \sqrt[3]{x}; \quad [-1, 8]$
5. $f(x) = \sin x; \quad [0, \pi]$
6. $f(x) = \sec x \tan x; \quad [0, \pi/3]$
7. $f(x) = \frac{x}{(5x^2 + 1)^2}; \quad [0, 2]$
8. $f(x) = \sec^2 x; \quad [-\pi/4, \pi/4]$

**FOCUS ON CONCEPTS**
**9. Let $f(x) = 3x^2$.**  
(a) Find the arithmetic average of the values $f(0.4), f(0.8), f(1.2), f(1.6),$ and $f(2.0)$.  
(b) Find the arithmetic average of the values $f(0.1), f(0.2), f(0.3), \dots, f(2.0)$.  
(c) Find the average value of $f$ on $[0, 2]$.  
(d) Explain why the answer to part (c) is less than the answers to parts (a) and (b).

**10. In parts (a)–(d), let $f(x) = 1 + \frac{1}{x^2}$.**  
(a) Find the arithmetic average of the values $f(6/5), f(7/5), f(8/5), f(9/5),$ and $f(2)$.  
(b) Find the arithmetic average of the values $f(1.1), f(1.2), f(1.3), \dots, f(2)$.  
(c) Find the average value of $f$ on $[1, 2]$.  
(d) Explain why the answer to part (c) is greater than the answers to parts (a) and (b).

**11. In each part, the velocity versus time curve is given for a particle moving along a line. Use the curve to find the average velocity of the particle over the time interval $0 \le t \le 3$.**

**12. Suppose that a particle moving along a line starts from rest and has an average velocity of $2\text{ ft/s}$ over the time interval $0 \le t \le 5$. Sketch a velocity versus time curve for the particle assuming that the particle is also at rest at time $t = 5$. Explain how your curve satisfies the required properties.**

**13. Suppose that $f$ is a linear function. Using the graph of $f$, explain why the average value of $f$ on $[a, b]$ is $f\left(\frac{a + b}{2}\right)$.**

**14. Suppose that a particle moves along a coordinate line with constant acceleration. Show that the average velocity of the particle during a time interval $[a, b]$ matches the velocity of the particle at the midpoint of the interval.**

**15–18 True–False Determine whether the statement is true or false. Explain your answer.**
15. If $g_{\text{ave}} < f_{\text{ave}}$, then $g(x) \le f(x)$ on $[a, b]$.
16. The average value of a constant multiple of $f$ is the same multiple of $f_{\text{ave}}$; that is, $(c\cdot f)_{\text{ave}} = c\cdot f_{\text{ave}}$.
17. The average of the sum of two functions on an interval is the sum of the average values of the two functions on the interval; that is, $(f + g)_{\text{ave}} = f_{\text{ave}} + g_{\text{ave}}$.
18. The average of the product of two functions on an interval is the product of the average values of the two functions on the interval; that is, $(f\cdot g)_{\text{ave}} = f_{\text{ave}}\cdot g_{\text{ave}}$.

**19. (a) Suppose that the velocity function of a particle moving along a coordinate line is $v(t) = 3t^3 + 2$. Find the average velocity of the particle over the time interval $1 \le t \le 4$ by integrating.**  
(b) Suppose that the position function of a particle moving along a coordinate line is $s(t) = 6t^2 + t$. Find the average velocity of the particle over the time interval $1 \le t \le 4$ algebraically.

**20. (a) Suppose that the acceleration function of a particle moving along a coordinate line is $a(t) = t + 1$. Find the average acceleration of the particle over the time interval $0 \le t \le 5$ by integrating.**  
(b) Suppose that the velocity function of a particle moving along a coordinate line is $v(t) = \cos t$. Find the average acceleration of the particle over the time interval $0 \le t \le \pi/4$ algebraically.

**21. Water is run at a constant rate of $1\text{ ft}^3/\text{min}$ to fill a cylindrical tank of radius $3\text{ ft}$ and height $5\text{ ft}$. Assuming that the tank is initially empty, make a conjecture about the average weight of the water in the tank over the time period required to fill it, and then check your conjecture by integrating. [Take the weight density of water to be $62.4\text{ lb/ft}^3$.]**

**22. (a) The temperature of a $10\text{ m}$ long metal bar is $15^\circ\text{C}$ at one end and $30^\circ\text{C}$ at the other end. Assuming that the temperature increases linearly from the cooler end to the hotter end, what is the average temperature of the bar?**  
(b) Explain why there must be a point on the bar where the temperature is the same as the average, and find it.

**23. A traffic engineer monitors the rate at which cars enter the main highway during the afternoon rush hour: $R(t) = 100(1 - 0.0001t^2)\text{ cars/min}$ ($t$ in minutes since 4:30 p.m.). Find the average rate, in cars per minute, at which cars enter the highway during the first half hour of rush hour.**

**24. Suppose that the value of a yacht in dollars after $t$ years of use is $V(t) = 275,000\sqrt{\frac{20}{t+20}}$. What is the average value of the yacht over its first 10 years of use?**

**25. A large juice glass containing 60 ml of orange juice is replenished by a server. The accompanying figure shows the rate at which orange juice is poured into the glass in milliliters per second (ml/s). Show that the average rate of change of the volume of juice in the glass during these 5 s is equal to the average value of the rate of flow of juice into the glass.**

**26. [CAS] The function $J_0$ defined by $J_0(x) = \frac{1}{\pi}\int_0^\pi \cos(x\sin t) dt$ is called the Bessel function of order zero.**  
(a) Find a function $f$ and an interval $[a, b]$ for which $J_0(1)$ is the average value of $f$ over $[a, b]$.  
(b) Estimate $J_0(1)$.  
(c) Use a CAS to graph the equation $y = J_0(x)$ over the interval $0 \le x \le 8$.  
(d) Estimate the smallest positive zero of $J_0$.

**27. Find a positive value of $k$ such that the average value of $f(x) = \sqrt{3x}$ over the interval $[0, k]$ is 6.**

**28. Suppose that a tumor grows at the rate of $r(t) = kt\text{ grams per week}$ for some positive constant $k$, where $t$ is the number of weeks since the tumor appeared. When, during the second 26 weeks of growth, is the mass of the tumor the same as its average mass during that period?**

**29. Writing.** Consider the following statement: *The average value of the rate of change of a function over an interval is equal to the average rate of change of the function over that interval.* Write a short paragraph that explains why this statement may be interpreted as a rewording of Part 1 of the Fundamental Theorem of Calculus.

**30. Writing.** If an automobile gets an average of 25 miles per gallon of gasoline, then it is also the case that on average the automobile expends 1/25 gallon of gasoline per mile. Interpret this statement using the concept of the average value of a function over an interval.

---

## 4.9 EVALUATING DEFINITE INTEGRALS BY SUBSTITUTION

In this section we will discuss two methods for evaluating definite integrals in which a substitution is required.

### TWO METHODS FOR MAKING SUBSTITUTIONS IN DEFINITE INTEGRALS

* **Method 1:** First evaluate the indefinite integral $\int f(g(x))g'(x) dx$ by substitution, and then use the relationship $\int_a^b f(g(x))g'(x) dx = \left[\int f(g(x))g'(x) dx\right]_a^b$.
* **Method 2:** Make the substitution $u = g(x)$ directly in the definite integral, replacing $x$-limits $a$ and $b$ by $u$-limits $g(a)$ and $g(b)$:

> **4.9.1 THEOREM**  
> If $g'$ is continuous on $[a, b]$ and $f$ is continuous on an interval containing the values of $g(x)$ for $a \le x \le b$, then
> $$\int_a^b f(g(x))g'(x) dx = \int_{g(a)}^{g(b)} f(u) du$$

#### Proof:
Since $f$ is continuous, it has an antiderivative $F$. Let $u = g(x)$. The chain rule implies that $\frac{d}{dx}[F(g(x))] = f(g(x))g'(x)$. Thus $F(g(x))$ is an antiderivative of $f(g(x))g'(x)$ on $[a, b]$. Therefore, by Part 1 of the Fundamental Theorem of Calculus:
$$\int_a^b f(g(x))g'(x) dx = [F(g(x))]_a^b = F(g(b)) - F(g(a)) = \int_{g(a)}^{g(b)} f(u) du \quad \blacksquare$$

#### Example 1
Evaluate $\int_0^2 x(x^2 + 1)^3 dx$.  
* **Method 1:** $\int x(x^2 + 1)^3 dx = \frac{1}{2}\int u^3 du = \frac{(x^2 + 1)^4}{8} + C \implies \left[\frac{(x^2 + 1)^4}{8}\right]_0^2 = \frac{625}{8} - \frac{1}{8} = 78$.  
* **Method 2:** $u = x^2 + 1, du = 2x dx$. If $x = 0, u = 1$; if $x = 2, u = 5$.
  $$\int_0^2 x(x^2 + 1)^3 dx = \frac{1}{2}\int_1^5 u^3 du = \left[\frac{u^4}{8}\right]_1^5 = \frac{625}{8} - \frac{1}{8} = 78$$

#### Example 2
(a) $\int_0^{\pi/8} \sin^5 2x \cos 2x dx = \frac{1}{2}\int_0^{1/\sqrt{2}} u^5 du = \frac{1}{2}\left[\frac{u^6}{6}\right]_0^{1/\sqrt{2}} = \frac{1}{96}$  
(b) $\int_2^5 (2x - 5)(x - 3)^9 dx = \int_{-1}^2 (2u + 1)u^9 du = \left[\frac{2u^{11}}{11} + \frac{u^{10}}{10}\right]_{-1}^2 = \frac{52,233}{110} \approx 474.8$

#### Example 3
$$\int_1^3 \frac{\cos(\pi/x)}{x^2} dx = -\frac{1}{\pi}\int_\pi^{\pi/3} \cos u du = -\frac{1}{\pi}[\sin u]_\pi^{\pi/3} = -\frac{\sqrt{3}}{2\pi} \approx -0.2757$$

---

### QUICK CHECK EXERCISES 4.9
*(See page 342 for answers.)*

1. Assume that $g'$ is continuous on $[a, b]$ and that $f$ is continuous on an interval containing the values of $g(x)$ for $a \le x \le b$. If $F$ is an antiderivative for $f$, then $\int_a^b f(g(x))g'(x) dx = \underline{\hspace{1cm}}$.
2. In each part, use the substitution to replace the given integral with an integral involving the variable $u$:  
   (a) $\int_0^2 3x^2(1 + x^3)^3 dx; \quad u = 1 + x^3$  
   (b) $\int_0^2 \frac{x}{\sqrt{5 - x^2}} dx; \quad u = 5 - x^2$
3. Evaluate the integral by making an appropriate substitution:  
   (a) $\int_{-\pi}^0 \sin(3x - \pi) dx = \underline{\hspace{1cm}}$  
   (b) $\int_0^{\pi/2} \sqrt[3]{\sin x}\cos x dx = \underline{\hspace{1cm}}$

#### QUICK CHECK ANSWERS 4.9
1. $F(g(b)) - F(g(a))$  
2. (a) $\int_1^9 u^3 du$ (b) $\int_1^5 \frac{1}{2\sqrt{u}} du$  
3. (a) $\frac{2}{3}$ (b) $\frac{3}{4}$

---

### EXERCISE SET 4.9

**1–2 Express the integral in terms of the variable $u$, but do not evaluate it.**
1. (a) $\int_1^3 (2x - 1)^3 dx; \quad u = 2x - 1$  
   (b) $\int_0^4 3x\sqrt{25 - x^2} dx; \quad u = 25 - x^2$  
   (c) $\int_{-1/2}^{1/2} \cos(\pi\theta) d\theta; \quad u = \pi\theta$  
   (d) $\int_0^1 (x + 2)(x + 1)^5 dx; \quad u = x + 1$
2. (a) $\int_{-1}^4 (5 - 2x)^8 dx; \quad u = 5 - 2x$  
   (b) $\int_{-\pi/3}^{2\pi/3} \frac{\sin x}{\sqrt{2 + \cos x}} dx; \quad u = 2 + \cos x$  
   (c) $\int_0^{\pi/4} \tan^2 x \sec^2 x dx; \quad u = \tan x$  
   (d) $\int_0^1 x^3\sqrt{x^2 + 3} dx; \quad u = x^2 + 3$

**3–12 Evaluate the definite integral two ways: first by a $u$-substitution in the definite integral and then by a $u$-substitution in the corresponding indefinite integral.**
3. $\int_0^1 (2x + 1)^3 dx$
4. $\int_1^2 (4x - 2)^3 dx$
5. $\int_0^1 (2x - 1)^3 dx$
6. $\int_1^2 (4 - 3x)^8 dx$
7. $\int_0^8 x\sqrt{1 + x} dx$
8. $\int_{-3}^0 x\sqrt{1 - x} dx$
9. $\int_0^{\pi/2} 4\sin(x/2) dx$
10. $\int_0^{\pi/6} 2\cos 3x dx$
11. $\int_{-2}^{-1} \frac{x}{(x^2 + 2)^3} dx$
12. $\int_{1-\pi}^{1+\pi} \sec^2\left(\frac{1}{4}x - \frac{1}{4}\right) dx$

**13–16 Evaluate the definite integral by expressing it in terms of $u$ and evaluating the resulting integral using a formula from geometry.**
13. $\int_{-5/3}^{5/3} \sqrt{25 - 9x^2} dx; \quad u = 3x$
14. $\int_0^2 x\sqrt{16 - x^4} dx; \quad u = x^2$
15. $\int_{\pi/3}^{\pi/2} \sin\theta\sqrt{1 - 4\cos^2\theta} d\theta; \quad u = 2\cos\theta$
16. $\int_{-3}^1 \sqrt{3 - 2x - x^2} dx; \quad u = x + 1$

**17. A particle moves with a velocity of $v(t) = \sin \pi t\text{ m/s}$ along an $s$-axis. Find the distance traveled by the particle over the time interval $0 \le t \le 1$.**

**18. A particle moves with a velocity of $v(t) = 3\cos 2t\text{ m/s}$ along an $s$-axis. Find the distance traveled by the particle over the time interval $0 \le t \le \pi/8$.**

**19. Find the area under the curve $y = 9/(x + 2)^2$ over the interval $[-1, 1]$.**

**20. Find the area under the curve $y = 1/(3x + 1)^2$ over the interval $[0, 1]$.**

**21–34 Evaluate the integrals by any method.**
21. $\int_1^5 \frac{dx}{\sqrt{2x - 1}}$
22. $\int_1^2 \sqrt{5x - 1} dx$
23. $\int_{-1}^1 \frac{x^2 dx}{\sqrt{x^3 + 9}}$
24. $\int_{\pi/2}^\pi 6\sin x(\cos x + 1)^5 dx$
25. $\int_1^3 \frac{x + 2}{\sqrt{x^2 + 4x + 7}} dx$
26. $\int_1^2 \frac{dx}{x^2 - 6x + 9}$
27. $\int_0^{\pi/4} 4\sin x \cos x dx$
28. $\int_0^{\pi/4} \sqrt{\tan x}\sec^2 x dx$
29. $\int_0^{\sqrt{\pi}} 5x\cos(x^2) dx$
30. $\int_{\pi^2}^{4\pi^2} \frac{1}{\sqrt{x}}\sin\sqrt{x} dx$
31. $\int_{\pi/12}^{\pi/9} \sec^2 3\theta d\theta$
32. $\int_{\pi/6}^{\pi/3} \csc^2 2\theta d\theta$
33. $\int_0^1 \frac{y^2 dy}{\sqrt{4 - 3y}}$
34. $\int_{-1}^4 \frac{x dx}{\sqrt{5 + x}}$

**35. [CAS] (a) Use a CAS to find the exact value of the integral $\int_0^{\pi/6} \sin^4 x \cos^3 x dx$.**  
(b) Confirm the exact value by hand calculation. [Hint: $\cos^2 x = 1 - \sin^2 x$.]

**36. [CAS] (a) Use a CAS to find the exact value of the integral $\int_{-\pi/4}^{\pi/4} \tan^4 x dx$.**  
(b) Confirm the exact value by hand calculation. [Hint: $1 + \tan^2 x = \sec^2 x$.]

**37. (a) Find $\int_0^1 f(3x + 1) dx$ if $\int_1^4 f(x) dx = 5$.**  
(b) Find $\int_0^3 f(3x) dx$ if $\int_0^9 f(x) dx = 5$.  
(c) Find $\int_{-2}^0 x f(x^2) dx$ if $\int_0^4 f(x) dx = 1$.

**38. Given that $m$ and $n$ are positive integers, show that $\int_0^1 x^m(1 - x)^n dx = \int_0^1 x^n(1 - x)^m dx$ by making a substitution. Do not attempt to evaluate the integrals.**

**39. Given that $n$ is a positive integer, show that $\int_0^{\pi/2} \sin^n x dx = \int_0^{\pi/2} \cos^n x dx$ by using a trigonometric identity and making a substitution. Do not attempt to evaluate the integrals.**

**40. Given that $n$ is a positive integer, evaluate the integral $\int_0^1 x(1 - x)^n dx$.**

**41–44 Gravitation and Escape Velocity**  
Suppose an object is launched vertically upwards from Earth's surface with initial speed $3\text{ mi/s}$. Speed $v$ at distance $b$ miles above Earth's surface is $v \approx \left[9 - 191,000\int_0^b \frac{1}{(3963 + x)^2} dx\right]^{1/2}\text{ (mi/s)}$.  
41. Estimate speed at $200\text{ mi}$ above surface.  
42. Estimate speed at $400\text{ mi}$ above surface.  
43. Estimate distance from surface when speed is half initial speed.  
44. Estimate maximum distance from surface achieved by the object.

**45. Moon Illumination**  
(a) First week of 2005 data: Days 1–7 illumination fractions: $0.74, 0.65, 0.56, 0.45, 0.35, 0.25, 0.16$. Find the average fraction illuminated.  
(b) Model $f(x) = 0.5 + 0.5\sin(0.213x + 2.481)$. Find average value over $[0, 7]$.

**46. Root-Mean-Square (RMS) Voltage**  
Voltage $V = V_p \sin(2\pi f t)$. $V_{\text{rms}} = \sqrt{\text{average value of } V^2 \text{ over one period } [0, 1/f]}$.  
(a) Show that $V_{\text{rms}} = \frac{V_p}{\sqrt{2}}$.  
(b) If $V_{\text{rms}} = 120\text{ V}$ at $60\text{ Hz}$, what is peak voltage $V_p$?

**47. [CAS] (a) Find $\lim_{n \to +\infty} \sum_{k=1}^n \frac{\sin(k\pi/n)}{n}$ by evaluating an appropriate definite integral over $[0, 1]$.**  
(b) Check with a CAS.

**FOCUS ON CONCEPTS**  
48. Let $I = \int_{-1}^1 \frac{1}{1 + x^2} dx$.  
(a) Explain why $I > 0$.  
(b) Show that substitution $x = 1/u$ results in $I = -\int_{-1}^1 \frac{1}{1 + u^2} du = -I \implies 2I = 0 \implies I = 0$. What is the error?  
49. (a) Prove that if $f$ is an odd function, then $\int_{-a}^a f(x) dx = 0$ and give a geometric explanation.  
(b) Prove that if $f$ is an even function, then $\int_{-a}^a f(x) dx = 2\int_0^a f(x) dx$ and give a geometric explanation.  
50. Show that if $f$ and $g$ are continuous functions, then $\int_0^t f(t - x)g(x) dx = \int_0^t f(x)g(t - x) dx$.  
51. (a) Let $I = \int_0^a \frac{f(x)}{f(x) + f(a - x)} dx$. Show that $I = a/2$.  
(b) Use (a) to find $\int_0^3 \frac{\sqrt{x}}{\sqrt{x} + \sqrt{3 - x}} dx$.  
(c) Use (a) to find $\int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x} dx$.  
52. Evaluate:  
(a) $\int_{-1}^1 x\sqrt{\cos(x^2)} dx$  
(b) $\int_0^\pi \sin^8 x \cos^5 x dx$ [Hint: Let $u = x - \pi/2$.]  
53. **Writing.** Explain why the two substitution methods yield the same result.  
54. **Writing.** Discuss advantages of Method 2 over Method 1 in theoretical problems.

---

## CHAPTER 4 REVIEW EXERCISES

**1–4 Evaluate the integrals.**
1. $\int \left(\frac{1}{2x^3} + 4\sqrt{x}\right) dx$
2. $\int [u^3 - 2u + 7] du$
3. $\int [4\sin x + 2\cos x] dx$
4. $\int \sec x(\tan x + \cos x) dx$

**5. Solve the initial-value problems.**  
(a) $\frac{dy}{dx} = \frac{1 - x}{\sqrt{x}}, \quad y(1) = 0$  
(b) $\frac{dy}{dx} = \cos x - 5x, \quad y(0) = 1$  
(c) $\frac{dy}{dx} = \sqrt[3]{x}, \quad y(1) = 2$

**6. The accompanying figure shows the slope field for a differential equation $dy/dx = f(x)$. Which of the following functions is most likely to be $f(x)$?**  
$$\sqrt{x}, \quad \sin x, \quad x^4, \quad x$$
**Explain your reasoning.**

**7. (a) Show that the substitutions $u = \sec x$ and $u = \tan x$ produce different values for the integral $\int \sec^2 x \tan x dx$.**  
(b) Explain why both are correct.

**8. Use the two substitutions in Exercise 7 to evaluate the definite integral $\int_0^{\pi/4} \sec^2 x \tan x dx$ and confirm that they produce the same result.**

**9. Evaluate the integral $\int \frac{x^7}{\sqrt{x^4 + 2}} dx$ by making the substitution $u = x^4 + 2$.**

**10. Evaluate the integral $\int \sqrt{1 + x^{-2/3}} dx$ by making the substitution $u = 1 + x^{2/3}$.**

**11–14 Evaluate the integrals by hand, and check your answers with a CAS if you have one.**
11. $\int \frac{\cos 3x}{\sqrt{5 + 2\sin 3x}} dx$
12. $\int \frac{\sqrt{3 + \sqrt{x}}}{\sqrt{x}} dx$
13. $\int \frac{x^2}{(ax^3 + b)^2} dx$
14. $\int x\sec^2(ax^2) dx$

**15. Express $\sum_{k=4}^{18} k(k - 3)$ in sigma notation with:**  
(a) $k = 0$ as the lower limit of summation  
(b) $k = 5$ as the lower limit of summation.

**16. (a) Fill in the blank: $1 + 3 + 5 + \dots + (2n - 1) = \sum_{k=1}^n \underline{\hspace{1cm}}$.**  
(b) Use part (a) to prove that the sum of the first $n$ consecutive odd integers is a perfect square.

**17. Find the area under the graph of $f(x) = 4x - x^2$ over the interval $[0, 4]$ using Definition 4.4.3 with $x_k^*$ as the right endpoint of each subinterval.**

**18. Find the area under the graph of $f(x) = 5x - x^2$ over the interval $[0, 5]$ using Definition 4.4.3 with $x_k^*$ as the left endpoint of each subinterval.**

**19–20 Use a calculating utility to find the left endpoint, right endpoint, and midpoint approximations to the area under the curve $y = f(x)$ over the stated interval using $n = 10$ subintervals.**
19. $y = 1/x; \quad [1, 2]$
20. $y = \tan x; \quad [0, 1]$

**21. The definite integral of $f$ over the interval $[a, b]$ is defined as the limit $\int_a^b f(x) dx = \lim_{\max \Delta x_k \to 0} \sum_{k=1}^n f(x_k^*) \Delta x_k$. Explain what the various symbols on the right side of this equation mean.**

**22. Use a geometric argument to evaluate $\int_0^1 |2x - 1| dx$.**

**23. Suppose that $\int_0^1 f(x) dx = 1/2, \; \int_1^2 f(x) dx = 1/4, \; \int_0^3 f(x) dx = -1, \; \int_0^1 g(x) dx = 2$. In each part, evaluate if possible; if not enough information, say so.**  
(a) $\int_0^2 f(x) dx$  
(b) $\int_1^3 f(x) dx$  
(c) $\int_2^3 5f(x) dx$  
(d) $\int_1^0 g(x) dx$  
(e) $\int_0^1 g(2x) dx$  
(f) $\int_0^1 [g(x)]^2 dx$

**24. In parts (a)–(d), use the information in Exercise 23 to evaluate the given integral. If there is not enough information, say so.**  
(a) $\int_0^1 [f(x) + g(x)] dx$  
(b) $\int_0^1 f(x)g(x) dx$  
(c) $\int_0^1 \frac{f(x)}{g(x)} dx$  
(d) $\int_0^1 [4g(x) - 3f(x)] dx$

**25. In each part, evaluate the integral. Where appropriate, you may use a geometric formula.**  
(a) $\int_{-1}^1 (1 + \sqrt{1 - x^2}) dx$  
(b) $\int_0^3 (x\sqrt{x^2 + 1} - \sqrt{9 - x^2}) dx$  
(c) $\int_0^1 x\sqrt{1 - x^4} dx$

**26. In each part, find the limit by interpreting it as a limit of Riemann sums in which the interval $[0, 1]$ is divided into $n$ subintervals of equal length.**  
(a) $\lim_{n \to +\infty} \frac{\sqrt{1} + \sqrt{2} + \sqrt{3} + \dots + \sqrt{n}}{n^{3/2}}$  
(b) $\lim_{n \to +\infty} \frac{1^4 + 2^4 + 3^4 + \dots + n^4}{n^5}$

**27–34 Evaluate the integrals using the Fundamental Theorem of Calculus and (if necessary) properties of the definite integral.**
27. $\int_{-3}^0 (x^2 - 4x + 7) dx$
28. $\int_{-1}^2 x(1 + x^3) dx$
29. $\int_1^3 \frac{1}{x^2} dx$
30. $\int_1^8 (5x^{2/3} - 4x^{-2}) dx$
31. $\int_0^1 (x - \sec x \tan x) dx$
32. $\int_1^4 \left(\frac{3}{\sqrt{t}} - 5\sqrt{t} - t^{-3/2}\right) dt$
33. $\int_0^2 |2x - 3| dx$
34. $\int_0^{\pi/2} |\frac{1}{2} - \sin x| dx$

**35–36 Find the area under the curve $y = f(x)$ over the stated interval.**
35. $f(x) = \sqrt{x}; \quad [1, 9]$
36. $f(x) = x^{-3/5}; \quad [1, 4]$

**37. Find the area that is above the $x$-axis but below the curve $y = (1 - x)(x - 2)$. Make a sketch of the region.**

**38. [CAS] Use a CAS to find the area of the region in the first quadrant that lies below the curve $y = x + x^2 - x^3$ and above the $x$-axis.**

**39–40 Sketch the curve and find the total area between the curve and the given interval on the $x$-axis.**
39. $y = x^2 - 1; \quad [0, 3]$
40. $y = \sqrt{x + 1} - 1; \quad [-1, 1]$

**41. Define $F(x)$ by $F(x) = \int_1^x (t^3 + 1) dt$.**  
(a) Use Part 2 of the Fundamental Theorem of Calculus to find $F'(x)$.  
(b) Check the result in part (a) by first integrating and then differentiating.

**42. Define $F(x)$ by $F(x) = \int_4^x \frac{1}{\sqrt{t}} dt$.**  
(a) Use Part 2 of the Fundamental Theorem of Calculus to find $F'(x)$.  
(b) Check the result in part (a) by first integrating and then differentiating.

**43–46 Use Part 2 of the Fundamental Theorem of Calculus to find the derivatives.**
43. $\frac{d}{dx}\left[\int_0^x \frac{1}{t^4 + 5} dt\right]$
44. $\frac{d}{dx}\left[\int_0^x \frac{t}{\cos t^2} dt\right]$
45. $\frac{d}{dx}\left[\int_0^x |t - 1| dt\right]$
46. $\frac{d}{dx}\left[\int_\pi^x \cos\sqrt{t} dt\right]$

**47. State the two parts of the Fundamental Theorem of Calculus, and explain what is meant by the statement "Differentiation and integration are inverse processes."**

**48. [CAS] Let $F(x) = \int_0^x \frac{t^2 - 3}{t^4 + 7} dt$.**  
(a) Find the intervals on which $F$ is increasing and those on which $F$ is decreasing.  
(b) Find the open intervals on which $F$ is concave up and those on which $F$ is concave down.  
(c) Find the $x$-values, if any, at which the function $F$ has absolute extrema.  
(d) Use a CAS to graph $F$, and confirm that the results in parts (a), (b), and (c) are consistent with the graph.

**49. Use differentiation to prove that the function $F(x) = \int_0^x \frac{1}{1 + t^2} dt + \int_0^{1/x} \frac{1}{1 + t^2} dt$ is constant on the interval $(0, +\infty)$.**

**50. What is the natural domain of the function $F(x) = \int_1^x \frac{1}{t^2 - 9} dt$? Explain your reasoning.**

**51. In each part, determine the values of $x$ for which $F(x)$ is positive, negative, or zero without performing the integration; explain your reasoning.**  
(a) $F(x) = \int_1^x \frac{t^4}{t^2 + 3} dt$  
(b) $F(x) = \int_{-1}^x \sqrt{4 - t^2} dt$

**52. [CAS] Use a CAS to approximate the largest and smallest values of the integral $\int_{-1}^x \frac{t}{\sqrt{2 + t^3}} dt$ for $1 \le x \le 3$.**

**53. Find all values of $x^*$ in the stated interval that are guaranteed to exist by the Mean-Value Theorem for Integrals, and explain what these numbers represent.**  
(a) $f(x) = \sqrt{x}; \quad [0, 3]$  
(b) $f(x) = 2x - x^2; \quad [0, 2]$

**54. A 10-gram tumor is discovered in a laboratory rat on March 1. The tumor is growing at a rate of $r(t) = t/7\text{ grams per week}$, where $t$ denotes the number of weeks since March 1. What will be the mass of the tumor on June 7?**

**55. Use the graph of $f$ shown in Figure Ex-55 to find the average value of $f$ on the interval $[0, 10]$.**

**56. Find the average value of $f(x) = x^2 + \frac{1}{x^2}$ over the interval $[1/2, 2]$.**

**57. Derive the formulas for the position and velocity functions of a particle that moves with constant acceleration along a coordinate line.**

**58. Velocity Data Points Analysis ($0 \le t \le 40\text{ s}$)**  
(a) Does the particle have constant acceleration? Explain your reasoning.  
(b) Is there any 15 s time interval during which the acceleration is constant? Explain your reasoning.  
(c) Estimate the distance traveled by the particle from time $t = 0$ to time $t = 40$.  
(d) Estimate the average velocity of the particle over the 40 s time period.  
(e) Is the particle ever slowing down during the 40 s time period? Explain your reasoning.  
(f) Is there sufficient information for you to determine the $s$-coordinate of the particle at time $t = 10$? If so, find it. If not, explain what additional information you need.

**59–62 A particle moves along an $s$-axis. Use the given information to find the position function of the particle.**
59. $v(t) = t^3 - 2t^2 + 1; \quad s(0) = 1$
60. $a(t) = 4\cos 2t; \quad v(0) = -1, \quad s(0) = -3$
61. $v(t) = 2t - 3; \quad s(1) = 5$
62. $a(t) = \cos t - 2t; \quad v(0) = 0, \quad s(0) = 0$

**63–66 A particle moves with a velocity of $v(t)\text{ m/s}$ along an $s$-axis. Find the displacement and the distance traveled by the particle during the given time interval.**
63. $v(t) = 2t - 4; \quad 0 \le t \le 6$
64. $v(t) = |t - 3|; \quad 0 \le t \le 5$
65. $v(t) = \frac{1}{2} - \frac{1}{t^2}; \quad 1 \le t \le 3$
66. $v(t) = \frac{3}{\sqrt{t}}; \quad 4 \le t \le 9$

**67–68 A particle moves with acceleration $a(t)\text{ m/s}^2$ along an $s$-axis and has velocity $v_0\text{ m/s}$ at time $t = 0$. Find the displacement and the distance traveled by the particle during the given time interval.**
67. $a(t) = -2; \quad v_0 = 3; \quad 1 \le t \le 4$
68. $a(t) = \frac{1}{\sqrt{5t + 1}}; \quad v_0 = 2; \quad 0 \le t \le 3$

**69. A car traveling $60\text{ mi/h}$ ($= 88\text{ ft/s}$) along a straight road decelerates at a constant rate of $10\text{ ft/s}^2$.**  
(a) How long will it take until the speed is $45\text{ mi/h}$?  
(b) How far will the car travel before coming to a stop?

**70. Suppose that the velocity function of a particle moving along an $s$-axis is $v(t) = 20t^2 - 100t + 50\text{ ft/s}$ and that the particle is at the origin at time $t = 0$. Use a graphing utility to generate the graphs of $s(t), v(t),$ and $a(t)$ for the first 6 s of motion.**

**71. A ball is thrown vertically upward from a height of $s_0\text{ ft}$ with an initial velocity of $v_0\text{ ft/s}$. If the ball is caught at height $s_0$, determine its average speed through the air using the free-fall model.**

**72. A rock, dropped from an unknown height, strikes the ground with a speed of $24\text{ m/s}$. Find the height from which the rock was dropped.**

**73–77 Evaluate the integrals by making an appropriate substitution.**
73. $\int_0^1 (2x + 1)^4 dx$
74. $\int_{-5}^0 x\sqrt{4 - x} dx$
75. $\int_0^1 \frac{dx}{\sqrt{3x + 1}}$
76. $\int_0^{\sqrt{\pi}} x\sin x^2 dx$
77. $\int_0^1 \sin^2(\pi x)\cos(\pi x) dx$

**78. Find a function $f$ and a number $a$ such that $2 + \int_a^x f(t) dt = \frac{8}{x + 3}$.**

---

## CHAPTER 4 MAKING CONNECTIONS

**1. Consider a Riemann sum $\sum_{k=1}^n 2x_k^* \Delta x_k$ for the integral of $f(x) = 2x$ over an interval $[a, b]$.**  
(a) Show that if $x_k^*$ is the midpoint of the $k$th subinterval, the Riemann sum is a telescoping sum. (See Exercises 57–60 of Section 4.4 for other examples of telescoping sums.)  
(b) Use part (a), Definition 4.5.1, and Theorem 4.5.2 to evaluate the definite integral of $f(x) = 2x$ over $[a, b]$.

**2. The function $f(x) = \sqrt{x}$ is continuous on $[0, 4]$ and therefore integrable on this interval. Evaluate $\int_0^4 \sqrt{x} dx$ by using Definition 4.5.1. Use subintervals of unequal length given by the partition**
$$0 < 4(1)^2/n^2 < 4(2)^2/n^2 < \dots < 4(n - 1)^2/n^2 < 4$$
**and let $x_k^*$ be the right endpoint of the $k$th subinterval.**

**3. Make appropriate modifications and repeat Exercise 2 for $\int_0^8 \sqrt[3]{x} dx$.**

**4. Given a continuous function $f$ and a positive real number $m$, let $g$ denote the function defined by the composition $g(x) = f(mx)$.**  
(a) Suppose that $\sum_{k=1}^n g(x_k^*) \Delta x_k$ is any Riemann sum for the integral of $g$ over $[0, 1]$. Use the correspondence $u_k = m x_k, \; u_k^* = m x_k^*$ to create a Riemann sum for the integral of $f$ over $[0, m]$. How are the values of the two Riemann sums related?  
(b) Use part (a), Definition 4.5.1, and Theorem 4.5.2 to find an equation that relates the integral of $g$ over $[0, 1]$ with the integral of $f$ over $[0, m]$.  
(c) How is your answer to part (b) related to Theorem 4.9.1?

**5. Given a continuous function $f$, let $g$ denote the function defined by $g(x) = 2x f(x^2)$.**  
(a) Suppose that $\sum_{k=1}^n g(x_k^*) \Delta x_k$ is any Riemann sum for the integral of $g$ over $[2, 3]$, with $x_k^* = (x_k + x_{k-1})/2$ the midpoint of the $k$th subinterval. Use the correspondence $u_k = x_k^2, \; u_k^* = (x_k^*)^2$ to create a Riemann sum for the integral of $f$ over $[4, 9]$. How are the values of the two Riemann sums related?  
(b) Use part (a), Definition 4.5.1, and Theorem 4.5.2 to find an equation that relates the integral of $g$ over $[2, 3]$ with the integral of $f$ over $[4, 9]$.  
(c) How is your answer to part (b) related to Theorem 4.9.1?
