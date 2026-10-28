# CHAPTER 15: TOPICS IN VECTOR CALCULUS

> Results in this chapter provide tools for analyzing and understanding the behavior of hurricanes and other fluid flows.

The main theme of this chapter is the concept of a **"flow."** The body of mathematics that we will study here is concerned with analyzing flows of various types—the flow of a fluid or the flow of electricity, for example. Indeed, the early writings of Isaac Newton on calculus are replete with such nouns as "fluxion" and "fluent," which are rooted in the Latin *fluere* (to flow). We will begin this chapter by introducing the concept of a vector field, which is the mathematical description of a flow. In subsequent sections, we will introduce two new kinds of integrals that are used in a variety of applications to analyze properties of vector fields and flows. Finally, we conclude with three major theorems, **Green’s Theorem**, the **Divergence Theorem**, and **Stokes’ Theorem**. These theorems provide a deep insight into the nature of flows and are the basis for many of the most important principles in physics and engineering.

---

## 15.1 VECTOR FIELDS

In this section we will consider functions that associate vectors with points in 2-space or 3-space. We will see that such functions play an important role in the study of fluid flow, gravitational force fields, electromagnetic force fields, and a wide range of other applied problems.

### VECTOR FIELDS

To motivate the mathematical ideas in this section, consider a unit point-mass located at any point in the Universe. According to Newton’s Law of Universal Gravitation, the Earth exerts an attractive force on the mass that is directed toward the center of the Earth and has a magnitude that is inversely proportional to the square of the distance from the mass to the Earth’s center (Figure 15.1.1). This association of force vectors with points in space is called the **Earth’s gravitational field**. 

A similar idea arises in fluid flow. Imagine a stream in which the water flows horizontally at every level, and consider the layer of water at a specific depth. At each point of the layer, the water has a certain velocity, which we can represent by a vector at that point (Figure 15.1.2). This association of velocity vectors with points in the two-dimensional layer is called the **velocity field** at that layer. These ideas are captured in the following definition.

> **15.1.1 DEFINITION**  
> A **vector field in a plane** is a function that associates with each point $P$ in the plane a unique vector $\mathbf{F}(P)$ parallel to the plane. Similarly, a **vector field in 3-space** is a function that associates with each point $P$ in 3-space a unique vector $\mathbf{F}(P)$ in 3-space.

Observe that in this definition there is no reference to a coordinate system. However, for computational purposes it is usually desirable to introduce a coordinate system so that vectors can be assigned components. Specifically, if $\mathbf{F}(P)$ is a vector field in an $xy$-coordinate system, then the point $P$ will have some coordinates $(x, y)$ and the associated vector will have components that are functions of $x$ and $y$. Thus, the vector field $\mathbf{F}(P)$ can be expressed as
$$\mathbf{F}(x, y) = f(x, y)\mathbf{i} + g(x, y)\mathbf{j}$$
Similarly, in 3-space with an $xyz$-coordinate system, a vector field $\mathbf{F}(P)$ can be expressed as
$$\mathbf{F}(x, y, z) = f(x, y, z)\mathbf{i} + g(x, y, z)\mathbf{j} + h(x, y, z)\mathbf{k}$$

> *Note:* Notice that a vector field is really just a vector-valued function. The term "vector field" is commonly used in physics and engineering.

---

### GRAPHICAL REPRESENTATIONS OF VECTOR FIELDS

A vector field in 2-space can be pictured geometrically by drawing representative field vectors $\mathbf{F}(x, y)$ at some well-chosen points in the $xy$-plane. But, just as it is usually not possible to describe a plane curve completely by plotting finitely many points, so it is usually not possible to describe a vector field completely by drawing finitely many vectors. Nevertheless, such graphical representations can provide useful information about the general behavior of the field if the vectors are chosen appropriately. However, graphical representations of vector fields require a substantial amount of computation, so they are usually created using computers. Figure 15.1.3 shows four computer-generated vector fields:
* (a) $\mathbf{F}(x, y) = \frac{1}{5}\sqrt{y}\,\mathbf{i}$ might describe the velocity of the current in a stream at various depths. At the bottom of the stream the velocity is zero, but the speed of the current increases as the depth decreases. Points at the same depth have the same speed.
* (b) $\mathbf{F}(x, y) = -y\mathbf{i} + x\mathbf{j}$ might describe the velocity at points on a rotating wheel. At the center of the wheel the velocity is zero, but the speed increases with the distance from the center. Points at the same distance from the center have the same speed.
* (c) $\mathbf{F}(x, y) = \frac{x\mathbf{i} + y\mathbf{j}}{10(x^2 + y^2)^{3/2}}$ might describe the repulsive force of an electrical charge—the closer to the charge, the greater the force of repulsion.
* (d) $\mathbf{F}(x, y, z) = \frac{x\mathbf{i} + y\mathbf{j} + z\mathbf{k}}{(x^2 + y^2 + z^2)^{3/2}}$ shows a vector field in 3-space. Such pictures tend to be cluttered and hence are of lesser value than graphical representations of vector fields in 2-space. 

> *Note:* Vectors in parts (b) and (c) are not to scale—their lengths have been compressed for clarity. We will follow this procedure throughout this chapter.

---

### A COMPACT NOTATION FOR VECTOR FIELDS

Sometimes it is helpful to denote the vector fields $\mathbf{F}(x, y)$ and $\mathbf{F}(x, y, z)$ entirely in vector notation by identifying $(x, y)$ with the radius vector $\mathbf{r} = x\mathbf{i} + y\mathbf{j}$ and $(x, y, z)$ with the radius vector $\mathbf{r} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$. With this notation a vector field in either 2-space or 3-space can be written as $\mathbf{F}(\mathbf{r})$. When no confusion is likely to arise, we will sometimes omit the $\mathbf{r}$ altogether and denote the vector field as $\mathbf{F}$.

---

### INVERSE-SQUARE FIELDS

According to Newton’s Law of Universal Gravitation, particles with masses $m$ and $M$ attract each other with a force $\mathbf{F}$ of magnitude
$$\|\mathbf{F}\| = \frac{GmM}{r^2} \tag{1}$$
where $r$ is the distance between the particles and $G$ is a constant. If we assume that the particle of mass $M$ is located at the origin of an $xyz$-coordinate system and $\mathbf{r}$ is the radius vector to the particle of mass $m$, then $r = \|\mathbf{r}\|$, and the force $\mathbf{F}(\mathbf{r})$ exerted by the particle of mass $M$ on the particle of mass $m$ is in the direction of the unit vector $-\mathbf{r}/\|\mathbf{r}\|$. Thus, it follows from (1) that
$$\mathbf{F}(\mathbf{r}) = -\frac{GmM}{\|\mathbf{r}\|^2} \frac{\mathbf{r}}{\|\mathbf{r}\|} = -\frac{GmM}{\|\mathbf{r}\|^3}\mathbf{r} \tag{2}$$
If $m$ and $M$ are constant, and we let $c = -GmM$, then this formula can be expressed as
$$\mathbf{F}(\mathbf{r}) = \frac{c}{\|\mathbf{r}\|^3}\mathbf{r}$$
Vector fields of this form arise in electromagnetic as well as gravitational problems. Such fields are so important that they have their own terminology.

> **15.1.2 DEFINITION**  
> If $\mathbf{r}$ is a radius vector in 2-space or 3-space, and if $c$ is a constant, then a vector field of the form
> $$\mathbf{F}(\mathbf{r}) = \frac{c}{\|\mathbf{r}\|^3}\mathbf{r} \tag{3}$$
> is called an **inverse-square field**.

Observe that if $c > 0$ in (3), then $\mathbf{F}(\mathbf{r})$ has the same direction as $\mathbf{r}$, so each vector in the field is directed away from the origin; and if $c < 0$, then $\mathbf{F}(\mathbf{r})$ is oppositely directed to $\mathbf{r}$, so each vector in the field is directed toward the origin. In either case the magnitude of $\mathbf{F}(\mathbf{r})$ is inversely proportional to the square of the distance from the terminal point of $\mathbf{r}$ to the origin, since
$$\|\mathbf{F}(\mathbf{r})\| = \frac{|c|}{\|\mathbf{r}\|^3}\|\mathbf{r}\| = \frac{|c|}{\|\mathbf{r}\|^2}$$
In component form:
* In 2-space:
  $$\mathbf{F}(x, y) = \frac{c}{(x^2 + y^2)^{3/2}}(x\mathbf{i} + y\mathbf{j}) \tag{4}$$
* In 3-space:
  $$\mathbf{F}(x, y, z) = \frac{c}{(x^2 + y^2 + z^2)^{3/2}}(x\mathbf{i} + y\mathbf{j} + z\mathbf{k}) \tag{5}$$

#### Example 1
Coulomb’s law states that the electrostatic force exerted by one charged particle on another is directly proportional to the product of the charges and inversely proportional to the square of the distance between them. This has the same form as Newton’s Law of Universal Gravitation, so the electrostatic force field exerted by a charged particle is an inverse-square field. Specifically, if a particle of charge $Q$ is at the origin of a coordinate system, and if $\mathbf{r}$ is the radius vector to a particle of charge $q$, then the force $\mathbf{F}(\mathbf{r})$ that the particle of charge $Q$ exerts on the particle of charge $q$ is of the form
$$\mathbf{F}(\mathbf{r}) = \frac{qQ}{4\pi\epsilon_0\|\mathbf{r}\|^3}\mathbf{r}$$
where $\epsilon_0$ is a positive constant (called the *permittivity constant*). This formula is of form (3) with $c = qQ/(4\pi\epsilon_0)$.

---

### GRADIENT FIELDS

An important class of vector fields arises from the process of finding gradients. Recall that if $\phi$ is a function of three variables, then the gradient of $\phi$ is defined as
$$\nabla\phi = \frac{\partial\phi}{\partial x}\mathbf{i} + \frac{\partial\phi}{\partial y}\mathbf{j} + \frac{\partial\phi}{\partial z}\mathbf{k}$$
This formula defines a vector field in 3-space called the **gradient field** of $\phi$. Similarly, the gradient of a function of two variables defines a gradient field in 2-space. At each point in a gradient field where the gradient is nonzero, the vector points in the direction in which the rate of increase of $\phi$ is maximum.

#### Example 2
Sketch the gradient field of $\phi(x, y) = x + y$.

**Solution.**  
The gradient of $\phi$ is
$$\nabla\phi = \frac{\partial\phi}{\partial x}\mathbf{i} + \frac{\partial\phi}{\partial y}\mathbf{j} = \mathbf{i} + \mathbf{j}$$
which is constant [i.e., is the same vector at each point $(x, y)$]. A portion of the vector field is sketched in Figure 15.1.4 together with some level curves of $\phi$. Note that at each point, $\nabla\phi$ is normal to the level curve of $\phi$ through the point (Theorem 13.6.6).

---

### CONSERVATIVE FIELDS AND POTENTIAL FUNCTIONS

If $\mathbf{F}(\mathbf{r})$ is an arbitrary vector field in 2-space or 3-space, we can ask whether it is the gradient field of some function $\phi$, and if so, how we can find $\phi$. This is an important problem in various applications, and we will study it in more detail later. However, there is some terminology for such fields that we will introduce now.

> **15.1.3 DEFINITION**  
> A vector field $\mathbf{F}$ in 2-space or 3-space is said to be **conservative** in a region if it is the gradient field for some function $\phi$ in that region, that is, if
> $$\mathbf{F} = \nabla\phi$$
> The function $\phi$ is called a **potential function** for $\mathbf{F}$ in the region.

#### Example 3
Inverse-square fields are conservative in any region that does not contain the origin. For example, in the two-dimensional case the function
$$\phi(x, y) = -\frac{c}{(x^2 + y^2)^{1/2}} \tag{6}$$
is a potential function for (4) in any region not containing the origin, since
$$\nabla\phi(x, y) = \frac{\partial\phi}{\partial x}\mathbf{i} + \frac{\partial\phi}{\partial y}\mathbf{j} = \frac{cx}{(x^2 + y^2)^{3/2}}\mathbf{i} + \frac{cy}{(x^2 + y^2)^{3/2}}\mathbf{j} = \frac{c}{(x^2 + y^2)^{3/2}}(x\mathbf{i} + y\mathbf{j}) = \mathbf{F}(x, y)$$
In a later section we will discuss methods for finding potential functions for conservative vector fields.

---

### DIVERGENCE AND CURL

We will now define two important operations on vector fields in 3-space—the **divergence** and the **curl** of the field. These names originate in the study of fluid flow, in which case the divergence relates to the way in which fluid flows toward or away from a point and the curl relates to the rotational properties of the fluid at a point. We will investigate the physical interpretations of these operations in more detail later, but for now we will focus only on their computation.

> **15.1.4 DEFINITION**  
> If $\mathbf{F}(x, y, z) = f(x, y, z)\mathbf{i} + g(x, y, z)\mathbf{j} + h(x, y, z)\mathbf{k}$, then we define the **divergence of $\mathbf{F}$**, written $\text{div}\,\mathbf{F}$, to be the function given by
> $$\text{div}\,\mathbf{F} = \frac{\partial f}{\partial x} + \frac{\partial g}{\partial y} + \frac{\partial h}{\partial z} \tag{7}$$

> **15.1.5 DEFINITION**  
> If $\mathbf{F}(x, y, z) = f(x, y, z)\mathbf{i} + g(x, y, z)\mathbf{j} + h(x, y, z)\mathbf{k}$, then we define the **curl of $\mathbf{F}$**, written $\text{curl}\,\mathbf{F}$, to be the vector field given by
> $$\text{curl}\,\mathbf{F} = \left(\frac{\partial h}{\partial y} - \frac{\partial g}{\partial z}\right)\mathbf{i} + \left(\frac{\partial f}{\partial z} - \frac{\partial h}{\partial x}\right)\mathbf{j} + \left(\frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}\right)\mathbf{k} \tag{8}$$

> **REMARK**  
> Observe that $\text{div}\,\mathbf{F}$ and $\text{curl}\,\mathbf{F}$ depend on the point at which they are computed, and hence are more properly written as $\text{div}\,\mathbf{F}(x, y, z)$ and $\text{curl}\,\mathbf{F}(x, y, z)$. However, even though these functions are expressed in terms of $x, y,$ and $z$, it can be proved that their values at a fixed point depend only on the point and not on the coordinate system selected. This is important in applications, since it allows physicists and engineers to compute the curl and divergence in any convenient coordinate system.

Before proceeding to some examples, we note that $\text{div}\,\mathbf{F}$ has scalar values, whereas $\text{curl}\,\mathbf{F}$ has vector values (i.e., $\text{curl}\,\mathbf{F}$ is itself a vector field). Moreover, for computational purposes it is useful to note that the formula for the curl can be expressed in the determinant form
$$\text{curl}\,\mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ f & g & h \end{vmatrix} \tag{9}$$
You should verify that Formula (8) results if the determinant is computed by interpreting a "product" such as $(\partial/\partial x)(g)$ to mean $\partial g/\partial x$. Keep in mind, however, that (9) is just a mnemonic device and not a true determinant, since the entries in a determinant must be numbers, not vectors and partial derivative symbols.

#### Example 4
Find the divergence and the curl of the vector field
$$\mathbf{F}(x, y, z) = x^2 y\mathbf{i} + 2y^3 z\mathbf{j} + 3z\mathbf{k}$$

**Solution.**  
From (7)
$$\text{div}\,\mathbf{F} = \frac{\partial}{\partial x}(x^2 y) + \frac{\partial}{\partial y}(2y^3 z) + \frac{\partial}{\partial z}(3z) = 2xy + 6y^2 z + 3$$
and from (9)
$$\text{curl}\,\mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ x^2 y & 2y^3 z & 3z \end{vmatrix} = \left[\frac{\partial}{\partial y}(3z) - \frac{\partial}{\partial z}(2y^3 z)\right]\mathbf{i} + \left[\frac{\partial}{\partial z}(x^2 y) - \frac{\partial}{\partial x}(3z)\right]\mathbf{j} + \left[\frac{\partial}{\partial x}(2y^3 z) - \frac{\partial}{\partial y}(x^2 y)\right]\mathbf{k}$$
$$= -2y^3\mathbf{i} - x^2\mathbf{k}$$

#### Example 5
Show that the divergence of the inverse-square field
$$\mathbf{F}(x, y, z) = \frac{c}{(x^2 + y^2 + z^2)^{3/2}}(x\mathbf{i} + y\mathbf{j} + z\mathbf{k})$$
is zero.

**Solution.**  
The computations can be simplified by letting $r = (x^2 + y^2 + z^2)^{1/2}$, in which case $\mathbf{F}$ can be expressed as
$$\mathbf{F}(x, y, z) = \frac{cx\mathbf{i} + cy\mathbf{j} + cz\mathbf{k}}{r^3} = \frac{cx}{r^3}\mathbf{i} + \frac{cy}{r^3}\mathbf{j} + \frac{cz}{r^3}\mathbf{k}$$
We leave it for you to show that
$$\frac{\partial r}{\partial x} = \frac{x}{r}, \quad \frac{\partial r}{\partial y} = \frac{y}{r}, \quad \frac{\partial r}{\partial z} = \frac{z}{r}$$
Thus
$$\text{div}\,\mathbf{F} = c\left[\frac{\partial}{\partial x}\left(\frac{x}{r^3}\right) + \frac{\partial}{\partial y}\left(\frac{y}{r^3}\right) + \frac{\partial}{\partial z}\left(\frac{z}{r^3}\right)\right] \tag{10}$$
But
$$\frac{\partial}{\partial x}\left(\frac{x}{r^3}\right) = \frac{r^3 - x(3r^2)(x/r)}{(r^3)^2} = \frac{1}{r^3} - \frac{3x^2}{r^5}$$
$$\frac{\partial}{\partial y}\left(\frac{y}{r^3}\right) = \frac{1}{r^3} - \frac{3y^2}{r^5}$$
$$\frac{\partial}{\partial z}\left(\frac{z}{r^3}\right) = \frac{1}{r^3} - \frac{3z^2}{r^5}$$
Substituting these expressions in (10) yields
$$\text{div}\,\mathbf{F} = c\left[\frac{3}{r^3} - \frac{3x^2 + 3y^2 + 3z^2}{r^5}\right] = c\left[\frac{3}{r^3} - \frac{3r^2}{r^5}\right] = 0$$

---

### THE $\nabla$ OPERATOR

Thus far, the symbol $\nabla$ that appears in the gradient expression $\nabla\phi$ has not been given a meaning of its own. However, it is often convenient to view $\nabla$ as an operator
$$\nabla = \frac{\partial}{\partial x}\mathbf{i} + \frac{\partial}{\partial y}\mathbf{j} + \frac{\partial}{\partial z}\mathbf{k} \tag{11}$$
which when applied to $\phi(x, y, z)$ produces the gradient
$$\nabla\phi = \frac{\partial\phi}{\partial x}\mathbf{i} + \frac{\partial\phi}{\partial y}\mathbf{j} + \frac{\partial\phi}{\partial z}\mathbf{k}$$
We call (11) the **del operator**. This is analogous to the derivative operator $d/dx$, which when applied to $f(x)$ produces the derivative $f'(x)$.

The del operator allows us to express the divergence of a vector field
$$\mathbf{F} = f(x, y, z)\mathbf{i} + g(x, y, z)\mathbf{j} + h(x, y, z)\mathbf{k}$$
in dot product notation as
$$\text{div}\,\mathbf{F} = \nabla \cdot \mathbf{F} = \frac{\partial f}{\partial x} + \frac{\partial g}{\partial y} + \frac{\partial h}{\partial z} \tag{12}$$
and the curl of this field in cross-product notation as
$$\text{curl}\,\mathbf{F} = \nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ f & g & h \end{vmatrix} \tag{13}$$

---

### THE LAPLACIAN $\nabla^2$

The operator that results by taking the dot product of the del operator with itself is denoted by $\nabla^2$ and is called the **Laplacian operator**. This operator has the form
$$\nabla^2 = \nabla \cdot \nabla = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} \tag{14}$$
When applied to $\phi(x, y, z)$ the Laplacian operator produces the function
$$\nabla^2\phi = \frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2} + \frac{\partial^2\phi}{\partial z^2}$$
Note that $\nabla^2\phi$ can also be expressed as $\text{div}(\nabla\phi)$. The equation $\nabla^2\phi = 0$ or, equivalently,
$$\frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2} + \frac{\partial^2\phi}{\partial z^2} = 0$$
is known as **Laplace’s equation**. This partial differential equation plays an important role in a wide variety of applications, resulting from the fact that it is satisfied by the potential function for the inverse-square field.

---

> **Pierre-Simon de Laplace (1749–1827)**  
> French mathematician and physicist. Laplace is sometimes referred to as the French Isaac Newton because of his work in celestial mechanics. In a five-volume treatise entitled *Traité de Mécanique Céleste*, he solved extremely difficult problems involving gravitational interactions between the planets. In particular, he was able to show that our solar system is stable and not prone to catastrophic collapse as a result of these interactions. This was an issue of major concern at the time because Jupiter’s orbit appeared to be shrinking and Saturn’s expanding; Laplace showed that these were expected periodic anomalies. In addition to his work in celestial mechanics, he founded modern probability theory, showed with Lavoisier that respiration is a form of combustion, and developed methods that fostered many new branches of pure mathematics.  
> Laplace was born to moderately successful parents in Normandy, his father being a farmer and cider merchant. He matriculated in the theology program at the University of Caen at age 16 but left for Paris at age 18 with a letter of introduction to the influential mathematician d’Alembert, who eventually helped him undertake a career in mathematics. Laplace was a prolific writer, and after his election to the Academy of Sciences in 1773, the secretary wrote that the Academy had never received so many important research papers by so young a person in such a short time. Laplace had little interest in pure mathematics—he regarded mathematics merely as a tool for solving applied problems. In his impatience with mathematical detail, he frequently omitted complicated arguments with the statement, "It is easy to show that...." He admitted, however, that as time passed he often had trouble reconstructing the omitted details himself!  
> At the height of his fame, Laplace served on many government committees and held the posts of Minister of the Interior and Chancellor of the Senate. He barely escaped imprisonment and execution during the period of the Revolution, probably because he was able to convince each opposing party that he sided with them. Napoleon described him as a great mathematician but a poor administrator who "sought subtleties everywhere, had only doubtful ideas, and ... carried the spirit of the infinitely small into administration." In spite of his genius, Laplace was both egotistic and insecure, attempting to ensure his place in history by conveniently failing to credit mathematicians whose work he used—an unnecessary pettiness since his own work was so brilliant. However, on the positive side he was supportive of young mathematicians, often treating them as his own children. Laplace ranks as one of the most influential mathematicians in history.

---

### QUICK CHECK EXERCISES 15.1
*(See page 1093 for answers.)*

1. The function $\phi(x, y, z) = xy + yz + xz$ is a potential for the vector field $\mathbf{F} = \underline{\quad}$.
2. The vector field $\mathbf{F}(x, y, z) = \underline{\quad}$, defined for $(x, y, z) \neq (0, 0, 0)$, is always directed toward the origin and is of length equal to the distance from $(x, y, z)$ to the origin.
3. An inverse-square field is one that can be written in the form $\mathbf{F}(\mathbf{r}) = \underline{\quad}$.
4. The vector field $\mathbf{F}(x, y, z) = yz\mathbf{i} + xy^2\mathbf{j} + yz^2\mathbf{k}$ has divergence $\underline{\quad}$ and curl $\underline{\quad}$.

---

### EXERCISE SET 15.1

**Focus on Concepts**

**1–2.** Match the vector field $\mathbf{F}(x, y)$ with one of the plots (I, II, III, IV), and explain your reasoning.
1. (a) $\mathbf{F}(x, y) = x\mathbf{i}$  
   (b) $\mathbf{F}(x, y) = \sin x\,\mathbf{i} + \mathbf{j}$
2. (a) $\mathbf{F}(x, y) = \mathbf{i} + \mathbf{j}$  
   (b) $\mathbf{F}(x, y) = \frac{x}{\sqrt{x^2+y^2}}\mathbf{i} + \frac{y}{\sqrt{x^2+y^2}}\mathbf{j}$

**3–4.** Determine whether the statement about the vector field $\mathbf{F}(x, y)$ is true or false. If false, explain why.
3. $\mathbf{F}(x, y) = x^2\mathbf{i} - y\mathbf{j}$.
   (a) $\|\mathbf{F}(x, y)\| \to 0$ as $(x, y) \to (0, 0)$.
   (b) If $(x, y)$ is on the positive $y$-axis, then the vector points in the negative $y$-direction.
   (c) If $(x, y)$ is in the first quadrant, then the vector points down and to the right.
4. $\mathbf{F}(x, y) = \frac{x}{\sqrt{x^2+y^2}}\mathbf{i} - \frac{y}{\sqrt{x^2+y^2}}\mathbf{j}$.
   (a) As $(x, y)$ moves away from the origin, the lengths of the vectors decrease.
   (b) If $(x, y)$ is a point on the positive $x$-axis, then the vector points up.
   (c) If $(x, y)$ is a point on the positive $y$-axis, the vector points to the right.

**5–8.** Sketch the vector field by drawing some representative nonintersecting vectors. The vectors need not be drawn to scale, but they should be in reasonably correct proportion relative to each other.
5. $\mathbf{F}(x, y) = 2\mathbf{i} - \mathbf{j}$
6. $\mathbf{F}(x, y) = y\mathbf{j}, \quad y > 0$
7. $\mathbf{F}(x, y) = y\mathbf{i} - x\mathbf{j}$. [Note: Each vector in the field is perpendicular to the position vector $\mathbf{r} = x\mathbf{i} + y\mathbf{j}$.]
8. $\mathbf{F}(x, y) = \frac{x\mathbf{i} + y\mathbf{j}}{\sqrt{x^2+y^2}}$. [Note: Each vector in the field is a unit vector in the same direction as the position vector $\mathbf{r} = x\mathbf{i} + y\mathbf{j}$.]

**9–10.** Use a graphing utility to generate a plot of the vector field.
9. $\mathbf{F}(x, y) = \mathbf{i} + \cos y\,\mathbf{j}$
10. $\mathbf{F}(x, y) = y\mathbf{i} - x\mathbf{j}$

**11–14 True–False.** Determine whether the statement is true or false. Explain your answer.
11. The vector-valued function $\mathbf{F}(x, y) = y\mathbf{i} + x^2\mathbf{j} + xy\mathbf{k}$ is an example of a vector field in the $xy$-plane.
12. If $\mathbf{r}$ is a radius vector in 3-space, then a vector field of the form $\mathbf{F}(\mathbf{r}) = \frac{1}{\|\mathbf{r}\|^2}\mathbf{r}$ is an example of an inverse-square field.
13. If $\mathbf{F}$ is a vector field, then so is $\nabla \times \mathbf{F}$.
14. If $\mathbf{F}$ is a vector field and $\nabla \cdot \mathbf{F} = \phi$, then $\phi$ is a potential function for $\mathbf{F}$.

**15–16.** Confirm that $\phi$ is a potential function for $\mathbf{F}(\mathbf{r})$ on some region, and state the region.
15. (a) $\phi(x, y) = \tan^{-1}(xy); \quad \mathbf{F}(x, y) = \frac{y}{1+x^2 y^2}\mathbf{i} + \frac{x}{1+x^2 y^2}\mathbf{j}$  
    (b) $\phi(x, y, z) = x^2 - 3y^2 + 4z^2; \quad \mathbf{F}(x, y, z) = 2x\mathbf{i} - 6y\mathbf{j} + 8z\mathbf{k}$
16. (a) $\phi(x, y) = 2y^2 + 3x^2 y - xy^3; \quad \mathbf{F}(x, y) = (6xy - y^3)\mathbf{i} + (4y + 3x^2 - 3xy^2)\mathbf{j}$  
    (b) $\phi(x, y, z) = x\sin z + y\sin x + z\sin y; \quad \mathbf{F}(x, y, z) = (\sin z + y\cos x)\mathbf{i} + (\sin x + z\cos y)\mathbf{j} + (\sin y + x\cos z)\mathbf{k}$

**17–22.** Find $\text{div}\,\mathbf{F}$ and $\text{curl}\,\mathbf{F}$.
17. $\mathbf{F}(x, y, z) = x^2\mathbf{i} - 2\mathbf{j} + yz\mathbf{k}$
18. $\mathbf{F}(x, y, z) = xz^3\mathbf{i} + 2y^4 x^2\mathbf{j} + 5z^2 y\mathbf{k}$
19. $\mathbf{F}(x, y, z) = 7y^3 z^2\mathbf{i} - 8x^2 z^5\mathbf{j} - 3xy^4\mathbf{k}$
20. $\mathbf{F}(x, y, z) = e^{xy}\mathbf{i} - \cos y\,\mathbf{j} + \sin^2 z\,\mathbf{k}$
21. $\mathbf{F}(x, y, z) = \frac{1}{\sqrt{x^2+y^2+z^2}}(x\mathbf{i} + y\mathbf{j} + z\mathbf{k})$
22. $\mathbf{F}(x, y, z) = \ln x\,\mathbf{i} + e^{xyz}\mathbf{j} + \tan^{-1}(z/x)\mathbf{k}$

**23–24.** Find $\nabla \cdot (\mathbf{F} \times \mathbf{G})$.
23. $\mathbf{F}(x, y, z) = 2x\mathbf{i} + \mathbf{j} + 4y\mathbf{k}, \quad \mathbf{G}(x, y, z) = x\mathbf{i} + y\mathbf{j} - z\mathbf{k}$
24. $\mathbf{F}(x, y, z) = yz\mathbf{i} + xz\mathbf{j} + xy\mathbf{k}, \quad \mathbf{G}(x, y, z) = xy\mathbf{j} + xyz\mathbf{k}$

**25–26.** Find $\nabla \cdot (\nabla \times \mathbf{F})$.
25. $\mathbf{F}(x, y, z) = \sin x\,\mathbf{i} + \cos(x - y)\mathbf{j} + z\mathbf{k}$
26. $\mathbf{F}(x, y, z) = e^{xz}\mathbf{i} + 3xe^y\mathbf{j} - e^{yz}\mathbf{k}$

**27–28.** Find $\nabla \times (\nabla \times \mathbf{F})$.
27. $\mathbf{F}(x, y, z) = xy\mathbf{j} + xyz\mathbf{k}$
28. $\mathbf{F}(x, y, z) = y^2 x\mathbf{i} - 3yz\mathbf{j} + xy\mathbf{k}$

**29–30.** Use a CAS to check the calculations.
29. Exercises 23, 25, and 27.
30. Exercises 24, 26, and 28.

**31–38.** Let $k$ be a constant, $\mathbf{F} = \mathbf{F}(x, y, z)$, $\mathbf{G} = \mathbf{G}(x, y, z)$, and $\phi = \phi(x, y, z)$. Prove the following identities, assuming that all derivatives involved exist and are continuous.
31. $\text{div}(k\mathbf{F}) = k\,\text{div}\,\mathbf{F}$
32. $\text{curl}(k\mathbf{F}) = k\,\text{curl}\,\mathbf{F}$
33. $\text{div}(\mathbf{F} + \mathbf{G}) = \text{div}\,\mathbf{F} + \text{div}\,\mathbf{G}$
34. $\text{curl}(\mathbf{F} + \mathbf{G}) = \text{curl}\,\mathbf{F} + \text{curl}\,\mathbf{G}$
35. $\text{div}(\phi\mathbf{F}) = \phi\,\text{div}\,\mathbf{F} + \nabla\phi \cdot \mathbf{F}$
36. $\text{curl}(\phi\mathbf{F}) = \phi\,\text{curl}\,\mathbf{F} + \nabla\phi \times \mathbf{F}$
37. $\text{div}(\text{curl}\,\mathbf{F}) = 0$
38. $\text{curl}(\nabla\phi) = \mathbf{0}$
39. Rewrite the identities in Exercises 31, 33, 35, and 37 in an equivalent form using the notation $\nabla \cdot$ for divergence and $\nabla \times$ for curl.
40. Rewrite the identities in Exercises 32, 34, 36, and 38 in an equivalent form using the notation $\nabla \cdot$ for divergence and $\nabla \times$ for curl.

**41–42.** Verify that the radius vector $\mathbf{r} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$ has the stated property.
41. (a) $\text{curl}\,\mathbf{r} = \mathbf{0}$  
    (b) $\nabla\|\mathbf{r}\| = \frac{\mathbf{r}}{\|\mathbf{r}\|}$
42. (a) $\text{div}\,\mathbf{r} = 3$  
    (b) $\nabla\left(\frac{1}{\|\mathbf{r}\|}\right) = -\frac{\mathbf{r}}{\|\mathbf{r}\|^3}$

**43–44.** Let $\mathbf{r} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$, let $r = \|\mathbf{r}\|$, let $f$ be a differentiable function of one variable, and let $\mathbf{F}(\mathbf{r}) = f(r)\mathbf{r}$.
43. (a) Use the chain rule and Exercise 41(b) to show that $\nabla f(r) = \frac{f'(r)}{r}\mathbf{r}$.  
    (b) Use the result in part (a) and Exercises 35 and 42(a) to show that $\text{div}\,\mathbf{F} = 3f(r) + rf'(r)$.
44. (a) Use part (a) of Exercise 43, Exercise 36, and Exercise 41(a) to show that $\text{curl}\,\mathbf{F} = \mathbf{0}$.  
    (b) Use the result in part (a) of Exercise 43 and Exercises 35 and 42(a) to show that $\nabla^2 f(r) = \frac{2}{r}f'(r) + f''(r)$.
45. Use the result in Exercise 43(b) to show that the divergence of the inverse-square field $\mathbf{F} = \mathbf{r}/\|\mathbf{r}\|^3$ is zero.
46. Use the result of Exercise 43(b) to show that if $\mathbf{F}$ is a vector field of the form $\mathbf{F} = f(\|\mathbf{r}\|)\mathbf{r}$ and if $\text{div}\,\mathbf{F} = 0$, then $\mathbf{F}$ is an inverse-square field. [Suggestion: Let $r = \|\mathbf{r}\|$ and multiply $3f(r) + rf'(r) = 0$ through by $r^2$. Then write the result as a derivative of a product.]
47. A curve $C$ is called a *flow line* of a vector field $\mathbf{F}$ if $\mathbf{F}$ is a tangent vector to $C$ at each point along $C$ (see Figure Ex-47).  
    (a) Let $C$ be a flow line for $\mathbf{F}(x, y) = -y\mathbf{i} + x\mathbf{j}$, and let $(x, y)$ be a point on $C$ for which $y \neq 0$. Show that the flow lines satisfy the differential equation $\frac{dy}{dx} = -\frac{x}{y}$.  
    (b) Solve the differential equation in part (a) by separation of variables, and show that the flow lines are concentric circles centered at the origin.
48–50. Find a differential equation satisfied by the flow lines of $\mathbf{F}$ (see Exercise 47), and solve it to find equations for the flow lines of $\mathbf{F}$. Sketch some typical flow lines and tangent vectors.
48. $\mathbf{F}(x, y) = \mathbf{i} + x\mathbf{j}$
49. $\mathbf{F}(x, y) = x\mathbf{i} + \mathbf{j}, \quad x > 0$
50. $\mathbf{F}(x, y) = x\mathbf{i} - y\mathbf{j}, \quad x > 0 \text{ and } y > 0$
51. **Writing.** Discuss the similarities and differences between the concepts "vector field" and "slope field."
52. **Writing.** In physical applications it is often necessary to deal with vector quantities that depend not only on position in space but also on time. Give some examples and discuss how the concept of a vector field would need to be modified to apply to such situations.

#### QUICK CHECK ANSWERS 15.1
1. $(y + z)\mathbf{i} + (x + z)\mathbf{j} + (x + y)\mathbf{k}$  
2. $-\mathbf{r} = -x\mathbf{i} - y\mathbf{j} - z\mathbf{k}$  
3. $\frac{c}{\|\mathbf{r}\|^3}\mathbf{r}$  
4. $2xy + 2yz; \quad z^2\mathbf{i} + y\mathbf{j} + (y^2 - z)\mathbf{k}$

---

## 15.2 LINE INTEGRALS

In earlier chapters we considered three kinds of integrals in rectangular coordinates: single integrals over intervals, double integrals over two-dimensional regions, and triple integrals over three-dimensional regions. In this section we will discuss integrals along curves in two- or three-dimensional space.

### LINE INTEGRALS

The first goal of this section is to define what it means to integrate a function along a curve. To motivate the definition we will consider the problem of finding the mass of a very thin wire whose linear density function (mass per unit length) is known. We assume that we can model the wire by a smooth curve $C$ between two points $P$ and $Q$ in 3-space (Figure 15.2.1). Given any point $(x, y, z)$ on $C$, we let $f(x, y, z)$ denote the corresponding value of the density function. To compute the mass of the wire, we proceed as follows:
* Divide $C$ into $n$ very small sections using a succession of distinct partition points $P = P_0, P_1, P_2, \dots, P_{n-1}, P_n = Q$ as illustrated on the left side of Figure 15.2.2. Let $\Delta M_k$ be the mass of the $k$th section, and let $\Delta s_k$ be the length of the arc between $P_{k-1}$ and $P_k$.
* Choose an arbitrary sampling point $P_k^*(x_k^*, y_k^*, z_k^*)$ on the $k$th arc, as illustrated on the right side of Figure 15.2.2. If $\Delta s_k$ is very small, the value of $f$ will not vary much along the $k$th section and we can approximate $f$ along this section by the value $f(x_k^*, y_k^*, z_k^*)$. It follows that the mass of the $k$th section can be approximated by
  $$\Delta M_k \approx f(x_k^*, y_k^*, z_k^*)\,\Delta s_k$$
* The mass $M$ of the entire wire can then be approximated by
  $$M = \sum_{k=1}^n \Delta M_k \approx \sum_{k=1}^n f(x_k^*, y_k^*, z_k^*)\,\Delta s_k \tag{1}$$
* We will use the expression $\max \Delta s_k \to 0$ to indicate the process of increasing $n$ in such a way that the lengths of all the sections approach 0. It is plausible that the error in (1) will approach 0 as $\max \Delta s_k \to 0$ and the exact value of $M$ will be given by
  $$M = \lim_{\max \Delta s_k \to 0} \sum_{k=1}^n f(x_k^*, y_k^*, z_k^*)\,\Delta s_k \tag{2}$$

The limit in (2) is similar to the limit of Riemann sums used to define the definite integral of a function over an interval (Definition 4.5.1). With this similarity in mind, we make the following definition.

> *Note:* Although the term "curve integrals" is more descriptive, the integrals in Definition 15.2.1 are called "line integrals" for historical reasons.

> **15.2.1 DEFINITION**  
> If $C$ is a smooth curve in 2-space or 3-space, then the **line integral of $f$ with respect to $s$ along $C$** is
> $$\int_C f(x, y)\,ds = \lim_{\max \Delta s_k \to 0} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta s_k \quad \text{(2-space)} \tag{3}$$
> or
> $$\int_C f(x, y, z)\,ds = \lim_{\max \Delta s_k \to 0} \sum_{k=1}^n f(x_k^*, y_k^*, z_k^*)\,\Delta s_k \quad \text{(3-space)} \tag{4}$$
> provided this limit exists and does not depend on the choice of partition or on the choice of sample points.

It is usually impractical to evaluate line integrals directly from Definition 15.2.1. However, the definition is important in the application and interpretation of line integrals:
* If $C$ is a curve in 3-space that models a thin wire, and if $f(x, y, z)$ is the linear density function of the wire, then the mass $M$ of the wire is given by
  $$M = \int_C f(x, y, z)\,ds \tag{5}$$
* If $C$ is a smooth curve of arc length $L$, and $f$ is identically 1, then
  $$\int_C ds = \lim_{\max \Delta s_k \to 0} \sum_{k=1}^n \Delta s_k = \lim_{\max \Delta s_k \to 0} L = L \tag{6}$$
* If $C$ is a curve in the $xy$-plane and $f(x, y)$ is a nonnegative continuous function defined on $C$, then $\int_C f(x, y)\,ds$ can be interpreted as the area $A$ of the "sheet" that is swept out by a vertical line segment that extends upward from the point $(x, y)$ to a height of $f(x, y)$ and moves along $C$ from one endpoint to the other (Figures 15.2.3 and 15.2.4):
  $$A = \lim_{\max \Delta s_k \to 0} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta s_k = \int_C f(x, y)\,ds \tag{7}$$

Line integrals share linearity properties:
$$\int_C [f(x, y) + g(x, y)]\,ds = \int_C f(x, y)\,ds + \int_C g(x, y)\,ds$$

---

### EVALUATING LINE INTEGRALS

Suppose that $C$ is a curve in the $xy$-plane that is smoothly parametrized by
$$\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} \quad (a \le t \le b)$$
The arc length of $C$ between points $P_{k-1}$ and $P_k$ is given by
$$\Delta s_k = \int_{t_{k-1}}^{t_k} \|\mathbf{r}'(t)\|\,dt = \|\mathbf{r}'(t_k^*)\|\,\Delta t_k \tag{8}$$
Thus,
$$\int_C f(x, y)\,ds = \int_a^b f(x(t), y(t))\|\mathbf{r}'(t)\|\,dt \tag{9}$$
Similarly, for a smooth curve in 3-space parametrized by $\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k} \; (a \le t \le b)$:
$$\int_C f(x, y, z)\,ds = \int_a^b f(x(t), y(t), z(t))\|\mathbf{r}'(t)\|\,dt \tag{10}$$

In expanded coordinate form:
$$\int_C f(x, y)\,ds = \int_a^b f(x(t), y(t))\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt \tag{11}$$
$$\int_C f(x, y, z)\,ds = \int_a^b f(x(t), y(t), z(t))\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}\,dt \tag{12}$$

#### Example 1
Using the given parametrization, evaluate the line integral $\int_C (1 + xy^2)\,ds$.
(a) $C : \mathbf{r}(t) = t\mathbf{i} + 2t\mathbf{j} \quad (0 \le t \le 1)$  
(b) $C : \mathbf{r}(t) = (1 - t)\mathbf{i} + (2 - 2t)\mathbf{j} \quad (0 \le t \le 1)$

**Solution (a).**  
Since $\mathbf{r}'(t) = \mathbf{i} + 2\mathbf{j}$, we have $\|\mathbf{r}'(t)\| = \sqrt{5}$, and:
$$\int_C (1 + xy^2)\,ds = \int_0^1 [1 + t(2t)^2]\sqrt{5}\,dt = \int_0^1 (1 + 4t^3)\sqrt{5}\,dt = \sqrt{5}\left[t + t^4\right]_0^1 = 2\sqrt{5}$$

**Solution (b).**  
Since $\mathbf{r}'(t) = -\mathbf{i} - 2\mathbf{j}$, we have $\|\mathbf{r}'(t)\| = \sqrt{5}$, and:
$$\int_C (1 + xy^2)\,ds = \int_0^1 [1 + (1 - t)(2 - 2t)^2]\sqrt{5}\,dt = \int_0^1 [1 + 4(1 - t)^3]\sqrt{5}\,dt = \sqrt{5}\left[t - (1 - t)^4\right]_0^1 = 2\sqrt{5}$$

> *Note:* The integrals in parts (a) and (b) agree, showing that the value of a line integral with respect to arc length $s$ does not depend on the orientation of $C$.

#### Example 2
Evaluate the line integral $\int_C (xy + z^3)\,ds$ from $(1, 0, 0)$ to $(-1, 0, \pi)$ along the helix $C$ represented by $x = \cos t, y = \sin t, z = t \; (0 \le t \le \pi)$.

**Solution.**  
From (12):
$$\int_C (xy + z^3)\,ds = \int_0^\pi (\cos t\sin t + t^3)\sqrt{(-\sin t)^2 + (\cos t)^2 + 1^2}\,dt = \sqrt{2}\int_0^\pi (\cos t\sin t + t^3)\,dt = \sqrt{2}\left[\frac{\sin^2 t}{2} + \frac{t^4}{4}\right]_0^\pi = \frac{\sqrt{2}\pi^4}{4}$$

#### Example 3
Suppose that a semicircular wire has the equation $y = \sqrt{25 - x^2}$ and that its mass density is $\delta(x, y) = 15 - y$ (Figure 15.2.8). Find the mass of the wire.

**Solution.**  
Parametrizing $C$ as $x = 5\cos t, y = 5\sin t \; (0 \le t \le \pi)$:
$$M = \int_C (15 - y)\,ds = \int_0^\pi (15 - 5\sin t)\sqrt{(-5\sin t)^2 + (5\cos t)^2}\,dt = 5\int_0^\pi (15 - 5\sin t)\,dt = 5\left[15t + 5\cos t\right]_0^\pi = 75\pi - 50 \approx 185.6 \text{ units of mass}$$

In the special case where $t = s$ (arc length parameter):
$$\int_C f(x, y)\,ds = \int_a^b f(x(s), y(s))\,ds \tag{13}$$
$$\int_C f(x, y, z)\,ds = \int_a^b f(x(s), y(s), z(s))\,ds \tag{14}$$

#### Example 4
Find the area of the surface extending upward from the circle $x^2 + y^2 = 1$ in the $xy$-plane to the parabolic cylinder $z = 1 - x^2$ (Figure 15.2.9).

**Solution.**  
$$A = \int_C (1 - x^2)\,ds = \int_0^{2\pi} (1 - \cos^2 s)\,ds = \int_0^{2\pi} \sin^2 s\,ds = \frac{1}{2}\int_0^{2\pi}(1 - \cos 2s)\,ds = \pi$$

---

### LINE INTEGRALS WITH RESPECT TO $x, y,$ AND $z$

Letting $\Delta x_k = x_k - x_{k-1}$ and $\Delta y_k = y_k - y_{k-1}$:
$$\int_C f(x, y)\,dx = \lim_{\max \Delta s_k \to 0} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta x_k \tag{16}$$
$$\int_C f(x, y)\,dy = \lim_{\max \Delta s_k \to 0} \sum_{k=1}^n f(x_k^*, y_k^*)\,\Delta y_k \tag{17}$$

Evaluation formulas for $x = x(t), y = y(t), z = z(t) \; (a \le t \le b)$:
$$\int_C f(x, y, z)\,dz = \int_a^b f(x(t), y(t), z(t))z'(t)\,dt$$

#### Example 5
Evaluate $\int_C 3xy\,dy$, where $C$ is the line segment joining $(0, 0)$ and $(1, 2)$:
(a) Oriented from $(0, 0)$ to $(1, 2)$: $x = t, y = 2t \; (0 \le t \le 1) \implies \int_0^1 3(t)(2t)(2)\,dt = \int_0^1 12t^2\,dt = 4$.  
(b) Oriented from $(1, 2)$ to $(0, 0)$: $x = 1 - t, y = 2 - 2t \; (0 \le t \le 1) \implies \int_0^1 3(1 - t)(2 - 2t)(-2)\,dt = -4$.

Reversing the orientation of $C$ changes the sign of line integrals with respect to $x, y, z$:
$$\int_{-C} f(x, y)\,dx = -\int_C f(x, y)\,dx, \quad \int_{-C} g(x, y)\,dy = -\int_C g(x, y)\,dy \tag{18–19}$$
while
$$\int_{-C} f(x, y)\,ds = \int_C f(x, y)\,ds \tag{20}$$

Linear combination notation:
$$\int_C f(x, y)\,dx + g(x, y)\,dy = \int_a^b [f(x(t), y(t))x'(t) + g(x(t), y(t))y'(t)]\,dt \tag{21–23}$$

#### Example 6
Evaluate $\int_C 2xy\,dx + (x^2 + y^2)\,dy$ along circular arc $x = \cos t, y = \sin t \; (0 \le t \le \pi/2)$.

**Solution.**  
$$\int_C 2xy\,dx = \int_0^{\pi/2} 2\cos t\sin t(-\sin t)\,dt = -\frac{2}{3}$$
$$\int_C (x^2 + y^2)\,dy = \int_0^{\pi/2} (\cos^2 t + \sin^2 t)\cos t\,dt = 1$$
$$\int_C 2xy\,dx + (x^2 + y^2)\,dy = -\frac{2}{3} + 1 = \frac{1}{3}$$

#### Example 7
Evaluate $\int_C (3x^2 + y^2)\,dx + 2xy\,dy$ along circular arc $x = \cos t, y = \sin t \; (0 \le t \le \pi/2)$ using single-step formula (23).

**Solution.**  
$$\int_0^{\pi/2} [(3\cos^2 t + \sin^2 t)(-\sin t) + 2\cos t\sin t\cos t]\,dt = \int_0^{\pi/2} (-\cos^2 t - \sin^2 t)\sin t\,dt = \int_0^{\pi/2} -\sin t\,dt = [\cos t]_0^{\pi/2} = -1$$

---

### INTEGRATING A VECTOR FIELD ALONG A CURVE

With $d\mathbf{r} = dx\mathbf{i} + dy\mathbf{j} + dz\mathbf{k}$:
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C f(x, y, z)\,dx + g(x, y, z)\,dy + h(x, y, z)\,dz \tag{26–27}$$

> **15.2.2 DEFINITION**  
> If $\mathbf{F}$ is a continuous vector field and $C$ is a smooth oriented curve, then the **line integral of $\mathbf{F}$ along $C$** is
> $$\int_C \mathbf{F} \cdot d\mathbf{r} \tag{28}$$

Evaluation formula:
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t)\,dt \tag{29}$$

#### Example 8
Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$ where $\mathbf{F}(x, y) = \cos x\mathbf{i} + \sin x\mathbf{j}$:  
(a) $C : \mathbf{r}(t) = -\frac{\pi}{2}\mathbf{i} + t\mathbf{j} \quad (1 \le t \le 2) \implies \int_1^2 (-\mathbf{j}) \cdot \mathbf{j}\,dt = -1$.  
(b) $C : \mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j} \quad (-1 \le t \le 2) \implies \int_{-1}^2 (\cos t + 2t\sin t)\,dt = [-2t\cos t + 3\sin t]_{-1}^2 = -2\cos 1 - 4\cos 2 + 3(\sin 1 + \sin 2) \approx 5.83629$.

With unit tangent $\mathbf{T}$:
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C (\mathbf{F} \cdot \mathbf{T})\,ds \tag{30}$$
Reversing orientation: $\int_{-C} \mathbf{F} \cdot d\mathbf{r} = -\int_C \mathbf{F} \cdot d\mathbf{r} \tag{32}$.

#### Example 9
Use (30) to evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$ where $\mathbf{F}(x, y) = -y\mathbf{i} + x\mathbf{j}$:  
(a) $C : x^2 + y^2 = 3 \; (x, y \ge 0) \implies \mathbf{F} \parallel \mathbf{T} \implies \int_C \sqrt{3}\,ds = \sqrt{3}(\frac{\sqrt{3}\pi}{2}) = \frac{3\pi}{2}$.  
(b) $C : \mathbf{r}(t) = t\mathbf{i} + 2t\mathbf{j} \; (0 \le t \le 1) \implies \mathbf{F} \perp \mathbf{T} \implies \int_C 0\,ds = 0$.

---

### WORK AS A LINE INTEGRAL

> **15.2.3 DEFINITION**  
> Suppose that under the influence of a continuous force field $\mathbf{F}$ a particle moves along a smooth curve $C$ and that $C$ is oriented in the direction of motion of the particle. Then the **work performed by the force field** on the particle is
> $$W = \int_C \mathbf{F} \cdot d\mathbf{r} \tag{34}$$

---

### LINE INTEGRALS ALONG PIECEWISE SMOOTH CURVES

For $C = C_1 + C_2 + \dots + C_n$:
$$\int_C = \int_{C_1} + \int_{C_2} + \dots + \int_{C_n}$$

#### Example 10
Evaluate $\int_C x^2 y\,dx + x\,dy$ where $C$ is the triangular path from $(0, 0)$ to $(1, 0)$ to $(1, 2)$ to $(0, 0)$ (Figure 15.2.17).

**Solution.**  
* Along $C_1$: $x = t, y = 0 \; (0 \le t \le 1) \implies \int_0^1 0\,dt = 0$.  
* Along $C_2$: $x = 1, y = 2t \; (0 \le t \le 1) \implies \int_0^1 1(2)\,dt = 2$.  
* Along $C_3$: $x = 1 - t, y = 2 - 2t \; (0 \le t \le 1) \implies \int_0^1 [2(t-1)^3 + 2(t-1)]\,dt = -\frac{1}{2} - 1 = -\frac{3}{2}$.  
$$\int_C x^2 y\,dx + x\,dy = 0 + 2 + \left(-\frac{3}{2}\right) = \frac{1}{2}$$

---

### QUICK CHECK EXERCISES 15.2
*(See page 1111 for answers.)*

1. The area of the surface extending upward from the line segment $y = x \; (0 \le x \le 1)$ in the $xy$-plane to the plane $z = 2x + 1$ is $\underline{\quad}$.
2. Suppose that a wire has equation $y = 1 - x \; (0 \le x \le 1)$ and that its mass density is $\delta(x, y) = 2 - x$. The mass of the wire is $\underline{\quad}$.
3. If $C$ is the curve represented by the equations $x = \sin t, y = \cos t, z = t \; (0 \le t \le 2\pi)$, then $\int_C y\,dx - x\,dy + dz = \underline{\quad}$.
4. If $C$ is the unit circle $x^2 + y^2 = 1$ oriented counterclockwise and $\mathbf{F}(x, y) = x\mathbf{i} + y\mathbf{j}$, then $\int_C \mathbf{F} \cdot d\mathbf{r} = \underline{\quad}$.

---

### EXERCISE SET 15.2

**Focus on Concepts**

1. Let $C$ be the line segment from $(0, 0)$ to $(0, 1)$. In each part, evaluate the line integral along $C$ by inspection, and explain your reasoning.  
   (a) $\int_C ds$  
   (b) $\int_C \sin xy\,dy$
2. Let $C$ be the line segment from $(0, 2)$ to $(0, 4)$. In each part, evaluate the line integral along $C$ by inspection, and explain your reasoning.  
   (a) $\int_C ds$  
   (b) $\int_C e^{xy}\,dx$
3–4. Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$ by inspection for the force field $\mathbf{F}(x, y) = \mathbf{i} + \mathbf{j}$ and the curve $C$ shown in the figure. Explain your reasoning.
5. Use (30) to explain why the line integral in part (a) of Example 8 can be found by multiplying the length of the line segment $C$ by $-1$.
6. (a) Use (30) to explain why the line integral in part (b) of Example 8 should be close to, but somewhat less than, the length of the parabolic curve $C$.  
   (b) Verify the conclusion in part (a) of this exercise by computing the length of $C$ and comparing the length with the value of the line integral.

**7–10.** Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$ along the line segment $C$ from $P$ to $Q$.
7. $\mathbf{F}(x, y) = 8\mathbf{i} + 8\mathbf{j}; \quad P(-4, 4), Q(-4, 5)$
8. $\mathbf{F}(x, y) = 2\mathbf{i} + 5\mathbf{j}; \quad P(1, -3), Q(4, -3)$
9. $\mathbf{F}(x, y) = 2x\mathbf{j}; \quad P(-2, 4), Q(-2, 11)$
10. $\mathbf{F}(x, y) = -8x\mathbf{i} + 3y\mathbf{j}; \quad P(-1, 0), Q(6, 0)$

**11.** Let $C$ be the curve $x = 2t, y = t^2 \; (0 \le t \le 1)$. Evaluate:  
(a) $\int_C (x - \sqrt{y})\,ds$  
(b) $\int_C (x - \sqrt{y})\,dx$  
(c) $\int_C (x - \sqrt{y})\,dy$

**12.** Let $C$ be $x = t, y = 3t^2, z = 6t^3 \; (0 \le t \le 1)$. Evaluate:  
(a) $\int_C xyz^2\,ds$  
(b) $\int_C xyz^2\,dx$  
(c) $\int_C xyz^2\,dy$  
(d) $\int_C xyz^2\,dz$

**13.** Evaluate $\int_C (3x + 2y)\,dx + (2x - y)\,dy$ along:  
(a) Line segment from $(0, 0)$ to $(1, 1)$  
(b) Parabolic arc $y = x^2$ from $(0, 0)$ to $(1, 1)$  
(c) Curve $y = \sin(\pi x/2)$ from $(0, 0)$ to $(1, 1)$  
(d) Curve $x = y^3$ from $(0, 0)$ to $(1, 1)$

**14.** Evaluate $\int_C y\,dx + z\,dy - x\,dz$ along:  
(a) Line segment from $(0, 0, 0)$ to $(1, 1, 1)$  
(b) Twisted cubic $x = t, y = t^2, z = t^3$ from $(0, 0, 0)$ to $(1, 1, 1)$  
(c) Helix $x = \cos\pi t, y = \sin\pi t, z = t$ from $(1, 0, 0)$ to $(-1, 0, 1)$

**15–18 True–False.** Determine whether true or false. Explain.
15. If $C$ is a smooth oriented curve in the $xy$-plane and $f(x, y)$ is continuous on $C$, then $\int_C f(x, y)\,ds = -\int_{-C} f(x, y)\,ds$.
16. The line integral of a continuous vector field along a smooth curve $C$ is a vector.
17. If $\mathbf{F}(x, y) = f(x, y)\mathbf{i} + g(x, y)\mathbf{j}$ along a smooth oriented curve $C$ in the $xy$-plane, then $\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C f(x, y)\,dx + g(x, y)\,dy$.
18. If a smooth oriented curve $C$ in the $xy$-plane is a contour for a differentiable function $f(x, y)$, then $\int_C \nabla f \cdot d\mathbf{r} = 0$.

**19–22.** Evaluate line integral with respect to $s$:
19. $\int_C \frac{1}{1+x}\,ds; \quad C : \mathbf{r}(t) = t\mathbf{i} + \frac{2}{3}t^{3/2}\mathbf{j} \; (0 \le t \le 3)$
20. $\int_C \frac{x}{1+y^2}\,ds; \quad C : x = 1 + 2t, y = t \; (0 \le t \le 1)$
21. $\int_C 3x^2 yz\,ds; \quad C : x = t, y = t^2, z = \frac{2}{3}t^3 \; (0 \le t \le 1)$
22. $\int_C \frac{e^{-z}}{x^2+y^2}\,ds; \quad C : \mathbf{r}(t) = 2\cos t\mathbf{i} + 2\sin t\mathbf{j} + t\mathbf{k} \; (0 \le t \le 2\pi)$

**23–30.** Evaluate line integral along curve $C$:
23. $\int_C (x + 2y)\,dx + (x - y)\,dy; \quad C : x = 2\cos t, y = 4\sin t \; (0 \le t \le \pi/4)$
24. $\int_C (x^2 - y^2)\,dx + x\,dy; \quad C : x = t^{2/3}, y = t \; (-1 \le t \le 1)$
25. $\int_C -y\,dx + x\,dy; \quad C : y^2 = 3x \text{ from } (3, 3) \text{ to } (0, 0)$
26. $\int_C (y - x)\,dx + x^2 y\,dy; \quad C : y^2 = x^3 \text{ from } (1, -1) \text{ to } (1, 1)$
27. $\int_C (x^2 + y^2)\,dx - x\,dy; \quad C : x^2 + y^2 = 1 \text{ counterclockwise from } (1, 0) \text{ to } (0, 1)$
28. $\int_C (y - x)\,dx + xy\,dy; \quad C : \text{line segment from } (3, 4) \text{ to } (2, 1)$
29. $\int_C yz\,dx - xz\,dy + xy\,dz; \quad C : x = e^t, y = e^{3t}, z = e^{-t} \; (0 \le t \le 1)$
30. $\int_C x^2\,dx + xy\,dy + z^2\,dz; \quad C : x = \sin t, y = \cos t, z = t^2 \; (0 \le t \le \pi/2)$

**31–32.** Use a CAS to evaluate:
31. (a) $\int_C (x^3 + y^3)\,ds; \quad C : \mathbf{r}(t) = e^t\mathbf{i} + e^{-t}\mathbf{j} \; (0 \le t \le \ln 2)$  
    (b) $\int_C xe^z\,dx + (x - z)\,dy + (x^2 + y^2 + z^2)\,dz; \quad C : x = \sin t, y = \cos t, z = t \; (0 \le t \le \pi/2)$
32. (a) $\int_C x^7 y^3\,ds; \quad C : x = \cos^3 t, y = \sin^3 t \; (0 \le t \le \pi/2)$  
    (b) $\int_C x^5 z\,dx + 7y\,dy + y^2 z\,dz; \quad C : \mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j} + \ln t\,\mathbf{k} \; (1 \le t \le e)$

**33–34.** Evaluate $\int_C y\,dx - x\,dy$ along curves in figures.
**35–36.** Evaluate $\int_C x^2 z\,dx - yx^2\,dy + 3\,dz$ along curves in figures.

**37–40.** Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$:
37. $\mathbf{F}(x, y) = x^2\mathbf{i} + xy\mathbf{j}; \quad C : \mathbf{r}(t) = 2\cos t\mathbf{i} + 2\sin t\mathbf{j} \; (0 \le t \le \pi)$
38. $\mathbf{F}(x, y) = x^2 y\mathbf{i} + 4\mathbf{j}; \quad C : \mathbf{r}(t) = e^t\mathbf{i} + e^{-t}\mathbf{j} \; (0 \le t \le 1)$
39. $\mathbf{F}(x, y) = (x^2 + y^2)^{-3/2}(x\mathbf{i} + y\mathbf{j}); \quad C : \mathbf{r}(t) = e^t\sin t\mathbf{i} + e^t\cos t\mathbf{j} \; (0 \le t \le 1)$
40. $\mathbf{F}(x, y, z) = z\mathbf{i} + x\mathbf{j} + y\mathbf{k}; \quad C : \mathbf{r}(t) = \sin t\mathbf{i} + 3\sin t\mathbf{j} + \sin^2 t\mathbf{k} \; (0 \le t \le \pi/2)$

**41.** Mass of thin wire $y = \sqrt{9 - x^2} \; (0 \le x \le 3)$ with $\delta(x, y) = x\sqrt{y}$.
**42.** Mass of wire $x = e^t\cos t, y = e^t\sin t \; (0 \le t \le 1)$ if $\delta$ is proportional to distance from origin.
**43.** Mass of helix $x = 3\cos t, y = 3\sin t, z = 4t \; (0 \le t \le \pi/2)$ with $\delta = kx/(1 + y^2)$.
**44.** Mass of curve $x = 2t, y = \ln t, z = 4\sqrt{t} \; (1 \le t \le 4)$ if $\delta$ is proportional to distance above $xy$-plane.

**45–48.** Work done by force field $\mathbf{F}$:
45. $\mathbf{F}(x, y) = xy\mathbf{i} + x^2\mathbf{j}; \quad C : x = y^2 \text{ from } (0, 0) \text{ to } (1, 1)$
46. $\mathbf{F}(x, y) = (x^2 + xy)\mathbf{i} + (y - x^2 y)\mathbf{j}; \quad C : x = t, y = 1/t \; (1 \le t \le 3)$
47. $\mathbf{F}(x, y, z) = xy\mathbf{i} + yz\mathbf{j} + xz\mathbf{k}; \quad C : \mathbf{r}(t) = t\mathbf{i} + t^2\mathbf{j} + t^3\mathbf{k} \; (0 \le t \le 1)$
48. $\mathbf{F}(x, y, z) = (x + y)\mathbf{i} + xy\mathbf{j} - z^2\mathbf{k}; \quad C : \text{line segments } (0, 0, 0) \to (1, 3, 1) \to (2, -1, 4)$

**49–50.** Work done by $\mathbf{F}(x, y) = \frac{1}{x^2+y^2}\mathbf{i} + \frac{4}{x^2+y^2}\mathbf{j}$ along curves shown in figures.
**51.** Surface area extending from $y = x^2 \; (0 \le x \le 2)$ up to $z = 3x$.
**52.** Surface area extending from $y = \sqrt{4 - x^2}$ up to $z = x^2 y$.
**53.** Sinusoidal cut in top of cylindrical tin can $x = \cos t, y = \sin t, z = 2 + 0.5\sin 3t \; (0 \le t \le 2\pi)$.  
(a) Geometric lateral area  
(b) Line integral expression  
(c) Calculate surface area
**54.** Evaluate $\int_{-C} \frac{x\,dy - y\,dx}{x^2+y^2}$ where $C$ is $x^2 + y^2 = a^2$ counterclockwise.
**55.** Find $\lambda$ such that work done by $\mathbf{F}(x, y) = xy\mathbf{i} + (x - y)\mathbf{j}$ along $x = t, y = \lambda t(1 - t)$ from $(0, 0)$ to $(1, 0)$ is 1.
**56.** Farmer weighing 150 lb carrying 20 lb grain sack climbing helical staircase of radius 25 ft, height 60 ft, 4 revolutions, leaking 1 lb/10 ft.
**57.** Proof that $\max \Delta s_k \to 0 \iff \max \Delta t_k \to 0$.
**58–59 Writing.** Definite integrals vs line integrals; different types of line integrals.

#### QUICK CHECK ANSWERS 15.2
1. $2\sqrt{2}$  
2. $\frac{3\sqrt{2}}{2}$  
3. $4\pi$  
4. 0

---

## 15.3 INDEPENDENCE OF PATH; CONSERVATIVE VECTOR FIELDS

In this section we will show that for certain kinds of vector fields $\mathbf{F}$ the line integral of $\mathbf{F}$ along a curve depends only on the endpoints of the curve and not on the curve itself. Vector fields with this property, which include gravitational and electrostatic fields, are of special importance in physics and engineering.

### WORK INTEGRALS & INDEPENDENCE OF PATH

A work integral in scalar form is
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C f(x, y)\,dx + g(x, y)\,dy \quad \text{(2-space)} \tag{1}$$
$$\int_C \mathbf{F} \cdot d\mathbf{r} = \int_C f(x, y, z)\,dx + g(x, y, z)\,dy + h(x, y, z)\,dz \quad \text{(3-space)} \tag{2}$$

#### Example 1
The force field $\mathbf{F}(x, y) = y\mathbf{i} + x\mathbf{j}$ is conservative since $\mathbf{F} = \nabla(xy)$. Confirm that $\int_C \mathbf{F} \cdot d\mathbf{r} = 1$ along:
(a) Line segment $y = x$ from $(0, 0)$ to $(1, 1) \implies \int_0^1 2t\,dt = 1$.  
(b) Parabola $y = x^2$ from $(0, 0)$ to $(1, 1) \implies \int_0^1 3t^2\,dt = 1$.  
(c) Cubic $y = x^3$ from $(0, 0)$ to $(1, 1) \implies \int_0^1 4t^3\,dt = 1$.

---

### THE FUNDAMENTAL THEOREM OF LINE INTEGRALS

> **15.3.1 THEOREM (The Fundamental Theorem of Line Integrals)**  
> Suppose that $\mathbf{F}(x, y) = f(x, y)\mathbf{i} + g(x, y)\mathbf{j}$ is a conservative vector field in some open region $D$ containing $(x_0, y_0)$ and $(x_1, y_1)$ and that $f(x, y)$ and $g(x, y)$ are continuous in this region. If $\mathbf{F}(x, y) = \nabla\phi(x, y)$, and if $C$ is any piecewise smooth parametric curve starting at $(x_0, y_0)$, ending at $(x_1, y_1)$, and lying in $D$, then
> $$\int_C \mathbf{F}(x, y) \cdot d\mathbf{r} = \phi(x_1, y_1) - \phi(x_0, y_0) \tag{3}$$
> or, equivalently,
> $$\int_C \nabla\phi \cdot d\mathbf{r} = \phi(x_1, y_1) - \phi(x_0, y_0) \tag{4}$$

**Proof.**  
For a smooth curve $C$ given by $x = x(t), y = y(t) \; (a \le t \le b)$:
$$\int_C \mathbf{F}(x, y) \cdot d\mathbf{r} = \int_a^b \left[\frac{\partial\phi}{\partial x}\frac{dx}{dt} + \frac{\partial\phi}{\partial y}\frac{dy}{dt}\right] dt = \int_a^b \frac{d}{dt}[\phi(x(t), y(t))]\,dt = \phi(x(b), y(b)) - \phi(x(a), y(a)) = \phi(x_1, y_1) - \phi(x_0, y_0) \quad \blacksquare$$

Notation for path-independent line integrals:
$$\int_{(x_0, y_0)}^{(x_1, y_1)} \mathbf{F} \cdot d\mathbf{r} = \int_{(x_0, y_0)}^{(x_1, y_1)} \nabla\phi \cdot d\mathbf{r} = \phi(x_1, y_1) - \phi(x_0, y_0) \tag{5}$$

#### Example 2
Evaluate $\int_{(0, 0)}^{(1, 1)} (y\mathbf{i} + x\mathbf{j}) \cdot d\mathbf{r} = \phi(1, 1) - \phi(0, 0) = 1 - 0 = 1$.

---

### LINE INTEGRALS ALONG CLOSED PATHS

> **15.3.2 THEOREM**  
> If $f(x, y)$ and $g(x, y)$ are continuous on some open connected region $D$, then the following statements are equivalent:  
> (a) $\mathbf{F}(x, y) = f(x, y)\mathbf{i} + g(x, y)\mathbf{j}$ is a conservative vector field on $D$.  
> (b) $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$ for every piecewise smooth closed curve $C$ in $D$.  
> (c) $\int_C \mathbf{F} \cdot d\mathbf{r}$ is independent of the path from any point $P$ in $D$ to any point $Q$ in $D$ for every piecewise smooth curve $C$ in $D$.

---

### A TEST FOR CONSERVATIVE VECTOR FIELDS

> **15.3.3 THEOREM (Conservative Field Test)**  
> If $f(x, y)$ and $g(x, y)$ are continuous and have continuous first partial derivatives on some open region $D$, and if $\mathbf{F}(x, y) = f(x, y)\mathbf{i} + g(x, y)\mathbf{j}$ is conservative on $D$, then
> $$\frac{\partial f}{\partial y} = \frac{\partial g}{\partial x} \tag{9}$$
> at each point in $D$. Conversely, if $D$ is simply connected and (9) holds at each point in $D$, then $\mathbf{F}(x, y) = f(x, y)\mathbf{i} + g(x, y)\mathbf{j}$ is conservative.

#### Example 3
For $\mathbf{F}(x, y) = (y + x)\mathbf{i} + (y - x)\mathbf{j}$:
$$\frac{\partial f}{\partial y} = 1, \quad \frac{\partial g}{\partial x} = -1 \implies \frac{\partial f}{\partial y} \neq \frac{\partial g}{\partial x}$$
Thus $\mathbf{F}$ is not conservative on any open set.

#### Example 4
Let $\mathbf{F}(x, y) = 2xy^3\mathbf{i} + (1 + 3x^2 y^2)\mathbf{j}$.  
(a) Show $\mathbf{F}$ is conservative: $\partial f/\partial y = 6xy^2 = \partial g/\partial x$.  
(b) Find $\phi$:
$$\phi = \int 2xy^3\,dx = x^2 y^3 + k(y)$$
$$\frac{\partial\phi}{\partial y} = 3x^2 y^2 + k'(y) = 1 + 3x^2 y^2 \implies k'(y) = 1 \implies k(y) = y + K$$
$$\phi(x, y) = x^2 y^3 + y + K$$

#### Example 5
Evaluate $\int_{(1, 4)}^{(3, 1)} 2xy^3\,dx + (1 + 3x^2 y^2)\,dy = \phi(3, 1) - \phi(1, 4) = (10 + K) - (68 + K) = -58$.

#### Example 6
For force field $\mathbf{F}(x, y) = e^y\mathbf{i} + xe^y\mathbf{j}$:
(a) $\partial f/\partial y = e^y = \partial g/\partial x \implies$ conservative.  
(b) Work along semicircle from $(1, 0)$ to $(-1, 0)$:
$$\phi(x, y) = xe^y + K \implies W = \phi(-1, 0) - \phi(1, 0) = -1 - 1 = -2$$

---

### CONSERVATIVE VECTOR FIELDS IN 3-SPACE & CONSERVATION OF ENERGY

In 3-space, $\mathbf{F} = f\mathbf{i} + g\mathbf{j} + h\mathbf{k}$ is conservative $\iff \text{curl}\,\mathbf{F} = \mathbf{0}$:
$$\frac{\partial f}{\partial y} = \frac{\partial g}{\partial x}, \quad \frac{\partial f}{\partial z} = \frac{\partial h}{\partial x}, \quad \frac{\partial g}{\partial z} = \frac{\partial h}{\partial y} \tag{19}$$
Potential energy $V(x, y, z) = -\phi(x, y, z)$:
$$W = \int_C \mathbf{F} \cdot d\mathbf{r} = -[V_f - V_i] = \frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2 \implies \frac{1}{2}mv_f^2 + V_f = \frac{1}{2}mv_i^2 + V_i$$

---

### QUICK CHECK EXERCISES 15.3
*(See page 1121 for answers.)*

1. If $C$ is a piecewise smooth curve from $(1, 2, 3)$ to $(4, 5, 6)$, then $\int_C dx + 2\,dy + 3\,dz = \underline{\quad}$.
2. If $C$ is the portion of the circle $x^2 + y^2 = 1$ where $0 \le x$, oriented counterclockwise, and $f(x, y) = ye^x$, then $\int_C \nabla f \cdot d\mathbf{r} = \underline{\quad}$.
3. A potential function for $\mathbf{F}(x, y, z) = yz\mathbf{i} + (xz + z)\mathbf{j} + (xy + y + 1)\mathbf{k}$ is $\phi(x, y, z) = \underline{\quad}$.
4. If $a, b, c$ are nonzero real numbers such that $x^5 y^a\mathbf{i} + x^b y^c\mathbf{j}$ is conservative, then $a = \underline{\quad}, b = \underline{\quad}, c = \underline{\quad}$.

---

### EXERCISE SET 15.3

**1–6.** Determine whether $\mathbf{F}$ is conservative. If so, find a potential function.
1. $\mathbf{F}(x, y) = x\mathbf{i} + y\mathbf{j}$
2. $\mathbf{F}(x, y) = 3y^2\mathbf{i} + 6xy\mathbf{j}$
3. $\mathbf{F}(x, y) = x^2 y\mathbf{i} + 5xy^2\mathbf{j}$
4. $\mathbf{F}(x, y) = e^x\cos y\mathbf{i} - e^x\sin y\mathbf{j}$
5. $\mathbf{F}(x, y) = (\cos y + y\cos x)\mathbf{i} + (\sin x - x\sin y)\mathbf{j}$
6. $\mathbf{F}(x, y) = x\ln y\mathbf{i} + y\ln x\mathbf{j}$

**7.** Evaluate $\int_C 2xy^3\,dx + (1 + 3x^2 y^2)\,dy$:  
(a) $C$ is line segment $(1, 4) \to (3, 1)$  
(b) $C$ is line segments $(1, 4) \to (1, 1) \to (3, 1)$

**8.** (a) Show $\int_C y\sin x\,dx - \cos x\,dy$ is path independent.  
(b) Evaluate along line segment $(0, 1) \to (\pi, -1)$.  
(c) Evaluate using Theorem 15.3.1.

**9–14.** Show integral is independent of path and find value:
9. $\int_{(1, 2)}^{(4, 0)} 3y\,dx + 3x\,dy$
10. $\int_{(0, 0)}^{(1, \pi/2)} e^x\sin y\,dx + e^x\cos y\,dy$
11. $\int_{(0, 0)}^{(3, 2)} 2xe^y\,dx + x^2 e^y\,dy$
12. $\int_{(-1, 2)}^{(0, 1)} (3x - y + 1)\,dx - (x + 4y + 2)\,dy$
13. $\int_{(2, -2)}^{(-1, 0)} 2xy^3\,dx + 3y^2 x^2\,dy$
14. $\int_{(1, 1)}^{(3, 3)} (e^x\ln y - \frac{e^y}{x})\,dx + (\frac{e^x}{y} - e^y\ln x)\,dy \quad (x, y > 0)$

**15–18.** Confirm $\mathbf{F}$ is conservative and find work from $P$ to $Q$:
15. $\mathbf{F}(x, y) = xy^2\mathbf{i} + x^2 y\mathbf{j}; \quad P(1, 1), Q(0, 0)$
16. $\mathbf{F}(x, y) = 2xy^3\mathbf{i} + 3x^2 y^2\mathbf{j}; \quad P(-3, 0), Q(4, 1)$
17. $\mathbf{F}(x, y) = ye^{xy}\mathbf{i} + xe^{xy}\mathbf{j}; \quad P(-1, 1), Q(2, 0)$
18. $\mathbf{F}(x, y) = e^{-y}\cos x\mathbf{i} - e^{-y}\sin x\mathbf{j}; \quad P(\pi/2, 1), Q(-\pi/2, 0)$

**19–22 True–False.**
19. If $\oint_C \mathbf{F} \cdot d\mathbf{r} = 0$ for some closed curve $C$, then $\mathbf{F}$ is conservative.
20. If $\mathbf{F}(x, y) = ay\mathbf{i} + bx\mathbf{j}$ is conservative, then $a = b$.
21. If $\phi(x, y)$ is a potential function for a constant vector field, then $z = \phi(x, y)$ is a plane.
22. If $f_y = g_x$ everywhere on the $xy$-plane, then there exists a potential $\phi$.

**23–24.** Find exact value of $\int_C \mathbf{F} \cdot d\mathbf{r}$:
23. $\mathbf{F}(x, y) = (e^y + ye^x)\mathbf{i} + (xe^y + e^x)\mathbf{j}; \quad C : \mathbf{r}(t) = \sin(\pi t/2)\mathbf{i} + \ln t\mathbf{j} \; (1 \le t \le 2)$
24. $\mathbf{F}(x, y) = 2xy\mathbf{i} + (x^2 + \cos y)\mathbf{j}; \quad C : \mathbf{r}(t) = t\mathbf{i} + t\cos(t/3)\mathbf{j} \; (0 \le t \le \pi)$
**25–26.** CAS numerical integration comparisons.

**Focus on Concepts**
**27–28.** Conservative field inspection from plots.
**29.** Normal vectors on circles in conservative fields.
**30.** Replacing circle by square.
**31.** Proof of 3D curl test for conservative fields.
**32.** Show $\int_C yz\,dx + xz\,dy + yx^2\,dz$ is not path independent.
**33.** Finding integrating factor $h(x)$ for conservative field.
**34.** Derivation of potential for 2D and 3D inverse-square fields.
**35.** Work done by 3D inverse-square field $\mathbf{F}(\mathbf{r}) = \frac{1}{\|\mathbf{r}\|^3}\mathbf{r}$.
**36.** Vortex field $\mathbf{F} = \frac{-y\mathbf{i} + x\mathbf{j}}{x^2+y^2}$ counterexample on non-simply connected domain.
**37–39.** Proofs of Theorems 15.3.1 and 15.3.2.
**40–41 Writing.** Methods for evaluating conservative line integrals; proving a field is not conservative.

#### QUICK CHECK ANSWERS 15.3
1. 18  
2. 2  
3. $xyz + yz + z$  
4. $a = 6, b = 6, c = 5$

---

## 15.4 GREEN’S THEOREM

In this section we will discuss a remarkable and beautiful theorem that expresses a double integral over a plane region in terms of a line integral around its boundary.

### GREEN’S THEOREM

> **15.4.1 THEOREM (Green's Theorem)**  
> Let $R$ be a simply connected plane region whose boundary is a simple, closed, piecewise smooth curve $C$ oriented counterclockwise. If $f(x, y)$ and $g(x, y)$ are continuous and have continuous first partial derivatives on some open set containing $R$, then
> $$\oint_C f(x, y)\,dx + g(x, y)\,dy = \iint_R \left(\frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}\right) dA \tag{1}$$

**Proof (for Type I / Type II regions).**  
We show $\oint_C f\,dx = -\iint_R \frac{\partial f}{\partial y}\,dA$ and $\oint_C g\,dy = \iint_R \frac{\partial g}{\partial x}\,dA$:
$$\oint_C f(x, y)\,dx = \int_{C_1} f(x, y)\,dx - \int_{-C_2} f(x, y)\,dx = \int_a^b [f(t, g_1(t)) - f(t, g_2(t))]\,dt$$
$$= -\int_a^b \int_{g_1(t)}^{g_2(t)} \frac{\partial f}{\partial y}\,dy\,dt = -\iint_R \frac{\partial f}{\partial y}\,dA \quad \blacksquare$$

#### Example 1
Evaluate $\oint_C x^2 y\,dx + x\,dy$ along the triangular path from $(0, 0)$ to $(1, 0)$ to $(1, 2)$ to $(0, 0)$ using Green’s Theorem.

**Solution.**  
$$\iint_R \left[\frac{\partial}{\partial x}(x) - \frac{\partial}{\partial y}(x^2 y)\right] dA = \int_0^1 \int_0^{2x} (1 - x^2)\,dy\,dx = \int_0^1 (2x - 2x^3)\,dx = \left[x^2 - \frac{x^4}{2}\right]_0^1 = \frac{1}{2}$$

---

> **George Green (1793–1841)**  
> English mathematician and physicist. Green left school at an early age to work in his father’s bakery and consequently had little early formal education. When his father opened a mill, the boy used the top room as a study in which he taught himself physics and mathematics from library books. In 1828 Green published his most important work, *An Essay on the Application of Mathematical Analysis to the Theories of Electricity and Magnetism*. Although Green’s Theorem appeared in that paper, the result went virtually unnoticed because of the small pressrun and local distribution. Following the death of his father in 1829, Green was urged by friends to seek a college education. In 1833, after four years of self-study to close the gaps in his elementary education, Green was admitted to Caius College, Cambridge. He graduated four years later, but with a disappointing performance on his final examinations—possibly because he was more interested in his own research. After a succession of works on light and sound, he was named to be Perse Fellow at Caius College. Two years later he died. In 1845, four years after his death, his paper of 1828 was published and the theories developed therein by this obscure, self-taught baker’s son helped pave the way to the modern theories of electricity and magnetism.

---

### FINDING WORK AND AREAS USING GREEN’S THEOREM

#### Example 2
Find work done by $\mathbf{F}(x, y) = (e^x - y^3)\mathbf{i} + (\cos y + x^3)\mathbf{j}$ counterclockwise around unit circle:
$$W = \iint_R (3x^2 + 3y^2)\,dA = 3\int_0^{2\pi}\int_0^1 r^3\,dr\,d\theta = \frac{3\pi}{2}$$

**Area formulas:**
$$A = \oint_C x\,dy = -\oint_C y\,dx = \frac{1}{2}\oint_C -y\,dx + x\,dy \tag{6}$$

#### Example 3
Area of ellipse $x = a\cos t, y = b\sin t \; (0 \le t \le 2\pi)$:
$$A = \frac{1}{2}\int_0^{2\pi} [(-b\sin t)(-a\sin t) + (a\cos t)(b\cos t)]\,dt = \frac{1}{2}ab\int_0^{2\pi} dt = \pi ab$$

---

### GREEN’S THEOREM FOR MULTIPLY CONNECTED REGIONS

$$\iint_R \left(\frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}\right) dA = \oint_{C_1} (f\,dx + g\,dy) + \oint_{C_2} (f\,dx + g\,dy) \tag{7}$$

#### Example 4
Evaluate $\oint_C \frac{-y\,dx + x\,dy}{x^2+y^2}$:  
(a) $C$ does not enclose origin: $\frac{\partial g}{\partial x} - \frac{\partial f}{\partial y} = 0 \implies 0$.  
(b) $C$ encloses origin: deform to small counterclockwise circle $C_a \implies \int_0^{2\pi} 1\,dt = 2\pi$.

---

### QUICK CHECK EXERCISES 15.4
*(See page 1129 for answers.)*

1. If $C$ is the square with vertices $(\pm 1, \pm 1)$ oriented counterclockwise, then $\oint_C -y\,dx + x\,dy = \underline{\quad}$.
2. If $C$ is the triangle with vertices $(0, 0), (1, 0), (1, 1)$ oriented counterclockwise, then $\oint_C 2xy\,dx + (x^2 + x)\,dy = \underline{\quad}$.
3. If $C$ is the unit circle centered at the origin and oriented counterclockwise, then $\oint_C (y^3 - y - x)\,dx + (x^3 + x + y)\,dy = \underline{\quad}$.
4. What region $R$ and choice of functions $f(x, y)$ and $g(x, y)$ allow us to claim $\int_0^1 \int_0^{\sqrt{1-x^2}} (2x + 2y)\,dy\,dx = \int_0^{\pi/2}(\sin^3 t + \cos^3 t)\,dt$?

---

### EXERCISE SET 15.4

**1–2.** Evaluate using Green’s Theorem and verify directly:
1. $\oint_C y^2\,dx + x^2\,dy$; square $(0, 0), (1, 0), (1, 1), (0, 1)$ counterclockwise.
2. $\oint_C y\,dx + x\,dy$; unit circle counterclockwise.

**3–14.** Use Green’s Theorem to evaluate $\oint_C f\,dx + g\,dy$:
3. $\oint_C 3xy\,dx + 2xy\,dy$; rectangle $-2 \le x \le 4, 1 \le y \le 2$.
4. $\oint_C (x^2 - y^2)\,dx + x\,dy$; circle $x^2 + y^2 = 9$.
5. $\oint_C x\cos y\,dx - y\sin x\,dy$; square $(0, 0), (\pi/2, 0), (\pi/2, \pi/2), (0, \pi/2)$.
6. $\oint_C y\tan^2 x\,dx + \tan x\,dy$; circle $x^2 + (y+1)^2 = 1$.
7. $\oint_C (x^2 - y)\,dx + x\,dy$; circle $x^2 + y^2 = 4$.
8. $\oint_C (e^x + y^2)\,dx + (e^y + x^2)\,dy$; region between $y = x^2$ and $y = x$.
9. $\oint_C \ln(1 + y)\,dx - \frac{xy}{1+y}\,dy$; triangle $(0, 0), (2, 0), (0, 4)$.
10. $\oint_C x^2 y\,dx - y^2 x\,dy$; first-quadrant boundary of $x^2 + y^2 = 16$.
11. $\oint_C \tan^{-1} y\,dx - \frac{y^2 x}{1+y^2}\,dy$; square $(0, 0), (1, 0), (1, 1), (0, 1)$.
12. $\oint_C \cos x\sin y\,dx + \sin x\cos y\,dy$; triangle $(0, 0), (3, 3), (0, 3)$.
13. $\oint_C x^2 y\,dx + (y + xy^2)\,dy$; region enclosed by $y = x^2$ and $x = y^2$.
14. Boundary between $y = x^2$ and $y = 2x$: (a) $\oint_C (6xy - y^2)\,dx$ (b) $\oint_C (6xy - y^2)\,dy$.

**15–18 True–False.**
19. CAS verification of Green's Theorem.
20. Area of ellipse via first and second formulas in (6).
21. Area of astroid $x = a\cos^3\phi, y = a\sin^3\phi \implies \frac{3}{8}\pi a^2$.
22. Area of triangle $(0, 0), (a, 0), (0, b) \implies \frac{1}{2}ab$.
23. Hyperbolic / elliptical sector area formulas.
24. Line integral area for hyperbola $x = a\cosh t, y = b\sinh t$.

**Focus on Concepts**
25. 2D Green's Theorem as 3D curl flux: $\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_R (\text{curl}\,\mathbf{F} \cdot \mathbf{k})\,dA$.
26. Path independence via Green's Theorem.
27. Area between curves $f(x)$ and $g(x)$.
28. Geometric interpretation of $\int_C x\,dy$ and $\int_C y\,dx$.
29–30. Work done around closed paths using Green's Theorem.
31. Line integral around cardioid $r = a(1 + \cos\theta)$.
32–36. Centroid formulas using Green's Theorem: $\bar{x} = \frac{1}{2A}\oint_C x^2\,dy, \bar{y} = -\frac{1}{2A}\oint_C y^2\,dx$.
37. Curve maximizing $\oint_C \frac{1}{3}y^3\,dx + (x - \frac{1}{3}x^3)\,dy$ ($x^2 + y^2 = 1$).
38. Surveyor’s polygon area formula.
39–40. Green's Theorem on multiply connected regions.
41–42. **Writing.** Role of Fundamental Theorem of Calculus; planimeters.

#### QUICK CHECK ANSWERS 15.4
1. 8  
2. 1/2  
3. $2\pi$  
4. $R: x^2 + y^2 \le 1 \; (0 \le x, 0 \le y)$ and $f(x, y) = -y^2, g(x, y) = x^2$

---

## 15.5 SURFACE INTEGRALS

In this section we will discuss integrals over surfaces in three-dimensional space. Such integrals occur in problems involving fluid and heat flow, electricity, magnetism, mass, and center of gravity.

### DEFINITION OF A SURFACE INTEGRAL

> **15.5.1 DEFINITION**  
> If $\sigma$ is a smooth parametric surface, then the **surface integral of $f(x, y, z)$ over $\sigma$** is
> $$\iint_\sigma f(x, y, z)\,dS = \lim_{n \to \infty} \sum_{k=1}^n f(x_k^*, y_k^*, z_k^*)\,\Delta S_k \tag{3}$$
> * Mass of curved lamina: $M = \iint_\sigma f(x, y, z)\,dS \tag{4}$
> * Surface area: $S = \iint_\sigma dS \tag{5}$

---

### EVALUATING SURFACE INTEGRALS

> **15.5.2 THEOREM (Parametric Surfaces)**  
> Let $\sigma$ be a smooth parametric surface $\mathbf{r}(u, v) = x(u, v)\mathbf{i} + y(u, v)\mathbf{j} + z(u, v)\mathbf{k} \; ((u, v) \in R)$. Then
> $$\iint_\sigma f(x, y, z)\,dS = \iint_R f(x(u, v), y(u, v), z(u, v))\left\|\frac{\partial\mathbf{r}}{\partial u} \times \frac{\partial\mathbf{r}}{\partial v}\right\| dA \tag{6}$$

#### Example 1
Evaluate $\iint_\sigma x^2\,dS$ over sphere $x^2 + y^2 + z^2 = 1$.  
**Solution.**  
$$\mathbf{r}(\phi, \theta) = \sin\phi\cos\theta\mathbf{i} + \sin\phi\sin\theta\mathbf{j} + \cos\phi\mathbf{k} \implies \left\|\frac{\partial\mathbf{r}}{\partial\phi}\times\frac{\partial\mathbf{r}}{\partial\theta}\right\| = \sin\phi$$
$$\iint_\sigma x^2\,dS = \int_0^{2\pi}\int_0^\pi (\sin^2\phi\cos^2\theta)\sin\phi\,d\phi\,d\theta = \frac{4\pi}{3}$$

> **15.5.3 THEOREM (Nonparametric Surfaces)**  
> (a) Over $z = g(x, y)$:
> $$\iint_\sigma f(x, y, z)\,dS = \iint_R f(x, y, g(x, y))\sqrt{\left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2 + 1}\,dA \tag{8}$$
> (b) Over $y = g(x, z)$:
> $$\iint_\sigma f(x, y, z)\,dS = \iint_R f(x, g(x, z), z)\sqrt{\left(\frac{\partial y}{\partial x}\right)^2 + \left(\frac{\partial y}{\partial z}\right)^2 + 1}\,dA \tag{9}$$
> (c) Over $x = g(y, z)$:
> $$\iint_\sigma f(x, y, z)\,dS = \iint_R f(g(y, z), y, z)\sqrt{\left(\frac{\partial x}{\partial y}\right)^2 + \left(\frac{\partial x}{\partial z}\right)^2 + 1}\,dA \tag{10}$$

#### Example 2
Evaluate $\iint_\sigma xz\,dS$ where $\sigma$ is $x + y + z = 1$ in the first octant:
$$\iint_\sigma xz\,dS = \sqrt{3}\int_0^1 \int_0^{1-x} x(1 - x - y)\,dy\,dx = \frac{\sqrt{3}}{24}$$

#### Example 3
Evaluate $\iint_\sigma y^2 z^2\,dS$ over cone $z = \sqrt{x^2 + y^2}$ between $z = 1$ and $z = 2$:
$$\iint_\sigma y^2 z^2\,dS = \sqrt{2}\int_0^{2\pi}\int_1^2 (r\sin\theta)^2(r^2)r\,dr\,d\theta = \frac{21\pi}{\sqrt{2}}$$

#### Example 4
Mass of paraboloid lamina $z = x^2 + y^2 \le 1$ with constant density $\delta_0$:
$$M = \delta_0\int_0^{2\pi}\int_0^1 \sqrt{4r^2 + 1}\,r\,dr\,d\theta = \frac{\pi\delta_0}{6}(5\sqrt{5} - 1)$$

---

### QUICK CHECK EXERCISES 15.5
*(See page 1138 for answers.)*

1. Replacements for $dS$:  
   (a) $\|\mathbf{r}_u \times \mathbf{r}_v\|\,dA$  
   (b) $\sqrt{(\partial z/\partial x)^2 + (\partial z/\partial y)^2 + 1}\,dA$
2. Triangle $(1, 0, 0), (0, 1, 0), (0, 0, 1)$: $\iint_\sigma (x + y + z)\,dS = \underline{\quad}$.
3. Sphere of radius 2: $\iint_\sigma (x^2 + y^2 + z^2)\,dS = \underline{\quad}$.
4. Mass of curved lamina with density $f(x, y, z)$: $\underline{\quad}$.

---

### EXERCISE SET 15.5

**1–8.** Evaluate surface integral $\iint_\sigma f(x, y, z)\,dS$:
1. $f(x, y, z) = z^2; \quad \sigma : z = \sqrt{x^2+y^2}, 1 \le z \le 2$
2. $f(x, y, z) = xy; \quad \sigma : x + y + z = 1 \text{ in first octant}$
3. $f(x, y, z) = x^2 y; \quad \sigma : x^2 + z^2 = 1, 0 \le y \le 1, z \ge 0$
4. $f(x, y, z) = (x^2 + y^2)z; \quad \sigma : x^2 + y^2 + z^2 = 4, z \ge 1$
5. $f(x, y, z) = x - y - z; \quad \sigma : x + y = 1 \text{ in first octant}, 0 \le z \le 1$
6. $f(x, y, z) = x + y; \quad \sigma : z = 6 - 2x - 3y \text{ in first octant}$
7. $f(x, y, z) = x + y + z; \quad \sigma : \text{surface of unit cube } 0 \le x, y, z \le 1$
8. $f(x, y, z) = x^2 + y^2; \quad \sigma : \text{sphere } x^2 + y^2 + z^2 = a^2$

**9–12 True–False.**
**13–14.** Improper surface integrals over hemispheres and cones.
**15–18.** Symmetry considerations on unit sphere:
15. $\iint_\sigma x^n\,dS = 0$ for odd $n$.
16. $\iint_\sigma f(x)g(y, z)\,dS = 0$ for odd $f(x)$.
17. $\iint_\sigma x^2\,dS = \frac{1}{3}\iint_\sigma (x^2+y^2+z^2)\,dS = \frac{4\pi}{3}$.
18. $\iint_\sigma (x - y)^2\,dS = \frac{8\pi}{3}$.

**19–24.** Set up projections on $xy$-, $yz$-, and $xz$-planes.
**25–26.** CAS confirmations.
**27–30.** Mass of curved laminas.
**31–32.** Lamina properties and mass of spherical shell with density equal to distance to $xy$-plane ($M = 2\pi a^3$).
**33–34.** Centroid of paraboloid and spherical cap.
**35–38.** Parametric surface evaluations.
**39–40.** CAS mass and centroid of Möbius strip.
**41–42 Writing.** Surface integrals vs double integrals; evaluation strategy.

#### QUICK CHECK ANSWERS 15.5
1. (a) $\|\mathbf{r}_u \times \mathbf{r}_v\|\,dA$ (b) $\sqrt{(\partial z/\partial x)^2 + (\partial z/\partial y)^2 + 1}\,dA$  
2. $\frac{\sqrt{3}}{2}$  
3. $64\pi$  
4. $\iint_\sigma f(x, y, z)\,dS$

---

## 15.6 APPLICATIONS OF SURFACE INTEGRALS; FLUX

In this section we will discuss applications of surface integrals to vector fields associated with fluid flow and electrostatic forces. However, the ideas that we will develop will be general in nature and applicable to other kinds of vector fields as well.

### ORIENTED SURFACES & FLUX

For an orientable surface $\sigma$ with unit normal vector field $\mathbf{n}$:
> **15.6.1 PROBLEM & FLUX DEFINITION**  
> The **flux** of a vector field $\mathbf{F}$ across an oriented surface $\sigma$ is
> $$\Phi = \iint_\sigma \mathbf{F} \cdot \mathbf{n}\,dS \tag{4}$$

---

### EVALUATING FLUX INTEGRALS

> **15.6.2 THEOREM (Parametric Flux Formula)**  
> $$\Phi = \iint_\sigma \mathbf{F} \cdot \mathbf{n}\,dS = \iint_R \mathbf{F} \cdot \left(\frac{\partial\mathbf{r}}{\partial u} \times \frac{\partial\mathbf{r}}{\partial v}\right) dA \tag{5}$$

#### Example 1
Find flux of $\mathbf{F} = z\mathbf{k}$ across outward sphere $x^2 + y^2 + z^2 = a^2$:
$$\Phi = \int_0^{2\pi}\int_0^\pi a^3\sin\phi\cos^2\phi\,d\phi\,d\theta = \frac{4\pi a^3}{3}$$

---

### ORIENTATION OF NONPARAMETRIC SURFACES

> **15.6.3 THEOREM (Nonparametric Flux Formulas)**  
> * For $z = g(x, y)$ oriented upward:
>   $$\iint_\sigma \mathbf{F} \cdot \mathbf{n}\,dS = \iint_R \mathbf{F} \cdot \left(-\frac{\partial z}{\partial x}\mathbf{i} - \frac{\partial z}{\partial y}\mathbf{j} + \mathbf{k}\right) dA \tag{12}$$
> * For $z = g(x, y)$ oriented downward:
>   $$\iint_\sigma \mathbf{F} \cdot \mathbf{n}\,dS = \iint_R \mathbf{F} \cdot \left(\frac{\partial z}{\partial x}\mathbf{i} + \frac{\partial z}{\partial y}\mathbf{j} - \mathbf{k}\right) dA \tag{13}$$

#### Example 2
Find flux of $\mathbf{F} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$ upward across $z = 1 - x^2 - y^2 \ge 0$:
$$\Phi = \iint_R (x\mathbf{i} + y\mathbf{j} + z\mathbf{k}) \cdot (2x\mathbf{i} + 2y\mathbf{j} + \mathbf{k})\,dA = \iint_R (x^2 + y^2 + 1)\,dA = \int_0^{2\pi}\int_0^1 (r^2 + 1)r\,dr\,d\theta = \frac{3\pi}{2}$$

---

### QUICK CHECK EXERCISES 15.6
*(See page 1148 for answers.)*

1. (a) $\Phi = \underline{\quad}$  
   (b) Outward flux across unit sphere for $x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$: $\Phi = \underline{\quad}$.
2. (a) Parametric double integral for $\Phi$  
   (b) Flux for plane patch $\mathbf{r} = u\mathbf{i} + v\mathbf{j} + (u+v)\mathbf{k} \; (u^2+v^2 \le 1)$: $\Phi = \underline{\quad}$.
3. (a) Formula for $z = g(x, y)$ upward  
   (b) Flux across triangle $(1, 0, 0), (0, 1, 0), (0, 0, 1)$: $\Phi = \underline{\quad}$.
4. Physical interpretation of flux in incompressible fluid flow.

---

### EXERCISE SET 15.6

**1–7.** Flux across faces of cube, rectangle, and disks:
1. Qualitative flux signs through cube faces for $\mathbf{F} = z\mathbf{j}$.
2. Constant field $\mathbf{F} = 2\mathbf{i} - 2\mathbf{j} - 2\mathbf{k}$ across closed unit cube $\implies 0$.
3. $\mathbf{F} = x\mathbf{i}$ through square of side 4 in plane $x = -5 \implies -80$.
4. $\mathbf{F} = (y+1)\mathbf{j}$ through square of side 5 in $xz$-plane $\implies -25$.
5. $\mathbf{F} = x\mathbf{i} + y\mathbf{j} + (z^2+4)\mathbf{k}$ through $2 \times 3$ rectangle in $z = 1 \implies 30$.
6. $\mathbf{F} = 2\mathbf{i} + 3\mathbf{j}$ through disk of radius 5 in $y = 3 \implies 75\pi$.
7. $\mathbf{F} = 9\mathbf{j} + 8\mathbf{k}$ through disk of radius 5 in $z = 2 \implies 200\pi$.

**8.** Unit normal for cylinder $\mathbf{r}(u, v) = \cos v\mathbf{i} + \sin v\mathbf{j} + u\mathbf{k}$.
**9–16.** Flux across surfaces in 3-space:
9. $\mathbf{F} = x\mathbf{k}; \quad \sigma : 0 \le x, y \le 2 \text{ in } xy\text{-plane upward} \implies 0$.
10. $\mathbf{F} = 5z\mathbf{i} + y\mathbf{j} + 2x\mathbf{k}; \quad 0 \le x \le 2, 0 \le y \le 3 \text{ in } z = 2 \implies 12$.
11. $\mathbf{F} = x\mathbf{i} + y\mathbf{j} + 2z\mathbf{k}; \quad z = 1 - x^2 - y^2 \ge 0 \text{ upward} \implies 2\pi$.
12. $\mathbf{F} = x^2\mathbf{i} + (x + e^y)\mathbf{j} - \mathbf{k}; \quad 0 \le x \le 2, 0 \le z \le 4 \text{ in } y = -1 \implies -4(1 + e^{-1})$.
13. $\mathbf{F} = x\mathbf{i} + y\mathbf{j} + 2z\mathbf{k}; \quad z^2 = x^2 + y^2, 1 \le z \le 2 \text{ upward} \implies 0$.
14. $\mathbf{F} = y\mathbf{j} + \mathbf{k}; \quad z = x^2 + y^2 \le 4 \text{ downward} \implies 4\pi$.
15. $\mathbf{F} = x\mathbf{k}; \quad z = x^2 + y^2 \le y \text{ downward} \implies 0$.
16. $\mathbf{F} = x^2\mathbf{i} + yx\mathbf{j} + zx\mathbf{k}; \quad 6x + 3y + 2z = 6 \text{ first octant} \implies 3/4$.

**17–20.** Parametric surface flux:
17. $\mathbf{F} = x\mathbf{i} + y\mathbf{j} + \mathbf{k}; \quad \mathbf{r}(u, v) = u\cos v\mathbf{i} + u\sin v\mathbf{j} + (1 - u^2)\mathbf{k} \; (1 \le u \le 2) \implies -15\pi/2$.
18. $\mathbf{F} = e^{-y}\mathbf{i} - y\mathbf{j} + x\sin z\mathbf{k}; \quad \mathbf{r}(u, v) = 2\cos v\mathbf{i} + \sin v\mathbf{j} + u\mathbf{k} \; (0 \le u \le 5) \implies -10\pi$.
19. $\mathbf{F} = \sqrt{x^2+y^2}\mathbf{k}; \quad \mathbf{r}(u, v) = u\cos v\mathbf{i} + u\sin v\mathbf{j} + 2u\mathbf{k} \; (0 \le u \le \sin v, 0 \le v \le \pi) \implies 4/3$.
20. $\mathbf{F} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}; \quad \mathbf{r}(u, v) = 2\sin u\cos v\mathbf{i} + 2\sin u\sin v\mathbf{j} + 2\cos u\mathbf{k} \; (0 \le u \le \pi/3) \implies 8\pi$.

**21.** Flux across surface of cube $[-1, 1]^3$: (a) $\mathbf{F} = x\mathbf{i} \implies 8$ (b) $\mathbf{F} = x\mathbf{i}+y\mathbf{j}+z\mathbf{k} \implies 24$ (c) $\mathbf{F} = x^2\mathbf{i}+y^2\mathbf{j}+z^2\mathbf{k} \implies 0$.
**22.** Closed paraboloid cap $z = x^2 + y^2 \le 1$ with disk top $\implies 0$.
**23–26 True–False.**
**27–28.** Parametric flux evaluation.
**29–30.** Fluid flow and mass flow rates across planes and hemispheres.
**31–32.** Flux formulas for $x = g(y, z)$ and $y = g(z, x)$.
**33.** Central force field $\mathbf{F} = \|\mathbf{r}\|^k\mathbf{r} \implies \Phi = 4\pi a^{k+3}$; independent of radius when $k = -3$.
**34–35.** CAS parameter searches.
**36–37 Writing.** Flux vs line integrals; conceptual meaning.

#### QUICK CHECK ANSWERS 15.6
1. (a) $\iint_\sigma \mathbf{F} \cdot \mathbf{n}\,dS$ (b) $4\pi$  
2. (a) $\iint_R \mathbf{F} \cdot (\mathbf{r}_u \times \mathbf{r}_v)\,dA$ (b) 0  
3. (a) $\iint_R \mathbf{F} \cdot (-z_x\mathbf{i} - z_y\mathbf{j} + \mathbf{k})\,dA$ (b) 1/2  
4. The net volume of fluid crossing $\sigma$ in the positive direction per unit time.

---

## 15.7 THE DIVERGENCE THEOREM

In this section we will be concerned with flux across surfaces, such as spheres, that "enclose" a region of space. We will show that the flux across such surfaces can be expressed in terms of the divergence of the vector field, and we will use this result to give a physical interpretation of the concept of divergence.

### THE DIVERGENCE THEOREM

> **15.7.1 THEOREM (The Divergence Theorem / Gauss's Theorem)**  
> Let $G$ be a solid whose surface $\sigma$ is oriented outward. If $\mathbf{F}(x, y, z) = f(x, y, z)\mathbf{i} + g(x, y, z)\mathbf{j} + h(x, y, z)\mathbf{k}$ where $f, g,$ and $h$ have continuous first partial derivatives on some open set containing $G$, and if $\mathbf{n}$ is the outward unit normal on $\sigma$, then
> $$\iint_\sigma \mathbf{F} \cdot \mathbf{n}\,dS = \iiint_G \text{div}\,\mathbf{F}\,dV \tag{1}$$

**Proof (for simple $xy$-solid).**  
$$\iiint_G \frac{\partial h}{\partial z}\,dV = \iint_R [h(x, y, g_2(x, y)) - h(x, y, g_1(x, y))]\,dA = \iint_{\sigma_2} h\mathbf{k} \cdot \mathbf{n}\,dS + \iint_{\sigma_1} h\mathbf{k} \cdot \mathbf{n}\,dS = \iint_\sigma h\mathbf{k} \cdot \mathbf{n}\,dS$$
Summing the three components yields (1). $\blacksquare$

---

> **Carl Friedrich Gauss (1777–1855)**  
> German mathematician and scientist. Sometimes called the "prince of mathematicians," Gauss ranks with Newton and Archimedes as one of the three greatest mathematicians who ever lived. His father, a laborer, was an uncouth but honest man who would have liked Gauss to take up a trade such as gardening or bricklaying; but the boy’s genius for mathematics was not to be denied. In the entire history of mathematics there may never have been a child so precocious as Gauss—by his own account he worked out the rudiments of arithmetic before he could talk. One day, before he was even three years old, his genius became apparent to his parents in a very dramatic way. His father was preparing the weekly payroll for the laborers under his charge while the boy watched quietly from a corner. At the end of the long and tedious calculation, Gauss informed his father that there was an error in the result and stated the answer, which he had worked out in his head. To the astonishment of his parents, a check of the computations showed Gauss to be correct!  
> For his elementary education Gauss was enrolled in a squalid school run by a man named Büttner whose main teaching technique was thrashing. Büttner was in the habit of assigning long addition problems which, unknown to his students, were arithmetic progressions that he could sum up using formulas. On the first day that Gauss entered the arithmetic class, the students were asked to sum the numbers from 1 to 100. But no sooner had Büttner stated the problem than Gauss turned over his slate and exclaimed in his peasant dialect, "Ligget se’." (Here it lies.) For nearly an hour Büttner glared at Gauss, who sat with folded hands while his classmates toiled away. When Büttner examined the slates at the end of the period, Gauss’s slate contained a single number, 5050—the only correct solution in the class. To his credit, Büttner recognized the genius of Gauss and with the help of his assistant, John Bartels, had him brought to the attention of Karl Wilhelm Ferdinand, Duke of Brunswick. The shy and awkward boy, who was then fourteen, so captivated the Duke that he subsidized him through preparatory school, college, and the early part of his career.  
> From 1795 to 1798 Gauss studied mathematics at the University of Göttingen, receiving his degree in absentia from the University of Helmstadt. For his dissertation, he gave the first complete proof of the fundamental theorem of algebra, which states that every polynomial equation has as many solutions as its degree. At age 19 he solved a problem that baffled Euclid, inscribing a regular polygon of 17 sides in a circle using straightedge and compass; and in 1801, at age 24, he published his first masterpiece, *Disquisitiones Arithmeticae*, considered by many to be one of the most brilliant achievements in mathematics. In that book Gauss systematized the study of number theory (properties of the integers) and formulated the basic concepts that form the foundation of that subject.  
> In the same year that the *Disquisitiones* was published, Gauss again applied his phenomenal computational skills in a dramatic way. The astronomer Giuseppi Piazzi had observed the asteroid Ceres for 1/40 of its orbit, but lost it in the Sun. Using only three observations and the "method of least squares" that he had developed in 1795, Gauss computed the orbit with such accuracy that astronomers had no trouble relocating it the following year. This achievement brought him instant recognition as the premier mathematician in Europe, and in 1807 he was made Professor of Astronomy and head of the astronomical observatory at Göttingen.  
> In the years that followed, Gauss revolutionized mathematics by bringing to it standards of precision and rigor undreamed of by his predecessors. He had a passion for perfection that drove him to polish and rework his papers rather than publish less finished work in greater numbers—his favorite saying was *"Pauca, sed matura"* (Few, but ripe). As a result, many of his important discoveries were squirreled away in diaries that remained unpublished until years after his death.  
> Among his myriad achievements, Gauss discovered the Gaussian or "bell-shaped" error curve fundamental in probability, gave the first geometric interpretation of complex numbers and established their fundamental role in mathematics, developed methods of characterizing surfaces intrinsically by means of the curves that they contain, developed the theory of conformal (angle-preserving) maps, and discovered non-Euclidean geometry 30 years before the ideas were published by others. In physics he made major contributions to the theory of lenses and capillary action, and with Wilhelm Weber he did fundamental work in electromagnetism. Gauss invented the heliotrope, bifilar magnetometer, and an electrotelegraph.  
> Gauss was deeply religious and aristocratic in demeanor. He mastered foreign languages with ease, read extensively, and enjoyed mineralogy and botany as hobbies. He disliked teaching and was usually cool and discouraging to other mathematicians, possibly because he had already anticipated their work. It has been said that if Gauss had published all of his discoveries, the current state of mathematics would be advanced by 50 years. He was without a doubt the greatest mathematician of the modern era.

---

### EXAMPLES OF THE DIVERGENCE THEOREM

#### Example 1
Outward flux of $\mathbf{F} = z\mathbf{k}$ across sphere of radius $a$:
$$\Phi = \iiint_G 1\,dV = \text{volume}(G) = \frac{4\pi a^3}{3}$$

#### Example 2
Outward flux of $\mathbf{F} = 2x\mathbf{i} + 3y\mathbf{j} + z^2\mathbf{k}$ across unit cube:
$$\Phi = \int_0^1 \int_0^1 \int_0^1 (5 + 2z)\,dz\,dy\,dx = 6$$

#### Example 3
Outward flux of $\mathbf{F} = x^3\mathbf{i} + y^3\mathbf{j} + z^2\mathbf{k}$ across cylinder $x^2 + y^2 \le 9, 0 \le z \le 2$:
$$\Phi = \int_0^{2\pi}\int_0^3\int_0^2 (3r^2 + 2z)r\,dz\,dr\,d\theta = 279\pi$$

#### Example 4
Outward flux of $\mathbf{F} = x^3\mathbf{i} + y^3\mathbf{j} + z^3\mathbf{k}$ across hemisphere solid $z = \sqrt{a^2 - x^2 - y^2} \ge 0$:
$$\Phi = \int_0^{2\pi}\int_0^{\pi/2}\int_0^a (3\rho^2)\rho^2\sin\phi\,d\rho\,d\phi\,d\theta = \frac{6\pi a^5}{5}$$

---

### DIVERGENCE AS FLUX DENSITY & GAUSS’S LAW

* Divergence definition coordinate-free limit:
  $$\text{div}\,\mathbf{F}(P_0) = \lim_{\text{vol}(G) \to 0} \frac{1}{\text{vol}(G)}\iint_{\sigma(G)} \mathbf{F} \cdot \mathbf{n}\,dS \tag{9}$$
* Sources and Sinks: $\text{div}\,\mathbf{F} > 0$ (source), $\text{div}\,\mathbf{F} < 0$ (sink), $\text{div}\,\mathbf{F} = 0$ (incompressible / continuity equation).

> **15.7.2 THEOREM (Gauss's Law for Inverse-Square Fields)**  
> If $\mathbf{F}(\mathbf{r}) = \frac{c}{\|\mathbf{r}\|^3}\mathbf{r}$ is an inverse-square field in 3-space, and if $\sigma$ is a closed orientable surface surrounding the origin:
> $$\Phi = \iint_\sigma \mathbf{F} \cdot \mathbf{n}\,dS = 4\pi c \tag{11}$$
> In electrostatics ($c = \frac{Q}{4\pi\epsilon_0}$): $\Phi = \frac{Q}{\epsilon_0}$.

---

### QUICK CHECK EXERCISES 15.7
*(See page 1158 for answers.)*

1. The Divergence Theorem states that the surface integral $\underline{\quad}$ and the triple integral $\underline{\quad}$ have the same value.
2. The outward flux of $\mathbf{F}(x, y, z) = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$ across any unit cube is $\underline{\quad}$.
3. In steady-state incompressible fluid flow, $\text{div}\,\mathbf{F} > 0$ is called a $\underline{\quad}$, $\text{div}\,\mathbf{F} < 0$ is called a $\underline{\quad}$, and the continuity equation states that $\underline{\quad}$.
4. If $\mathbf{F}(\mathbf{r}) = \frac{c}{\|\mathbf{r}\|^3}\mathbf{r}$, outward flux across $\sigma$ surrounding origin is $\underline{\quad}$; if not surrounding origin, it is $\underline{\quad}$.

---

### EXERCISE SET 15.7

**1–4.** Verify the Divergence Theorem by evaluating both integrals:
1. $\mathbf{F}(x, y, z) = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$; unit cube $[0, 1]^3 \implies 3$.
2. $\mathbf{F}(x, y, z) = 5\mathbf{j} + 7\mathbf{k}$; sphere $x^2 + y^2 + z^2 = 1 \implies 0$.
3. $\mathbf{F}(x, y, z) = 2x\mathbf{i} - yz\mathbf{j} + z^2\mathbf{k}$; paraboloid $z = x^2 + y^2 \le 1$ capped by disk $\implies \pi$.
4. $\mathbf{F}(x, y, z) = xy\mathbf{i} + yz\mathbf{j} + xz\mathbf{k}$; cube $[0, 2]^3 \implies 24$.

**5–8 True–False.**
**9–19.** Calculate outward flux using Divergence Theorem:
9. $\mathbf{F} = (x^2 + y)\mathbf{i} + z^2\mathbf{j} + (e^y - z)\mathbf{k}$; box $0 \le x \le 3, 0 \le y \le 1, 0 \le z \le 2 \implies 12$.
10. $\mathbf{F} = z^3\mathbf{i} - x^3\mathbf{j} + y^3\mathbf{k}$; sphere $x^2 + y^2 + z^2 = a^2 \implies 0$.
11. $\mathbf{F} = (x - z)\mathbf{i} + (y - x)\mathbf{j} + (z - y)\mathbf{k}$; cylinder $x^2 + y^2 \le a^2, 0 \le z \le 1 \implies 3\pi a^2$.
12. $\mathbf{F} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}$; paraboloid solid $0 \le z \le 1 - x^2 - y^2 \implies 3\pi/2$.
13. $\mathbf{F} = x^3\mathbf{i} + y^3\mathbf{j} + z^3\mathbf{k}$; cylinder $x^2 + y^2 \le 4, 0 \le z \le 3 \implies 144\pi$.
14. $\mathbf{F} = (x^2 + y)\mathbf{i} + xy\mathbf{j} - (2xz + y)\mathbf{k}$; tetrahedron $x + y + z \le 1 \implies 0$.
15. $\mathbf{F} = (x^3 - e^y)\mathbf{i} + (y^3 + \sin z)\mathbf{j} + (z^3 - xy)\mathbf{k}$; upper hemisphere radius $2 \implies 96\pi/5$.
16. $\mathbf{F} = 2xz\mathbf{i} + yz\mathbf{j} + z^2\mathbf{k}$; upper hemisphere solid of radius $a \implies \pi a^4$.
17. $\mathbf{F} = x^2\mathbf{i} + y^2\mathbf{j} + z^2\mathbf{k}$; cone $\sqrt{x^2+y^2} \le z \le 1 \implies \pi/2$.
18. $\mathbf{F} = x^2 y\mathbf{i} - xy^2\mathbf{j} + (z + 2)\mathbf{k}$; between $z = x^2 + y^2$ and $z = 2x \implies \pi/2$.
19. $\mathbf{F} = x^3\mathbf{i} + x^2 y\mathbf{j} + xy\mathbf{k}$; solid bounded by $z = 4 - x^2, y + z = 5, z = 0, y = 0 \implies 8576/105$.

**20.** Volume formula $\text{vol}(G) = \frac{1}{3}\iint_\sigma \mathbf{r} \cdot \mathbf{n}\,dS$.
**21.** Flux across cylinder $(x+2)^2 + y^2 \le 9, -1 \le z \le 4 \implies 135\pi$.
**22–26 Focus on Concepts.** Constant field flux, positive/negative divergence fields, vector field plots, tangency on spheres/cubes.
**27–31.** Divergence theorem vector identities:
27. $\iint_\sigma \text{curl}\,\mathbf{F} \cdot \mathbf{n}\,dS = 0$
28. $\iint_\sigma \nabla f \cdot \mathbf{n}\,dS = \iiint_G \nabla^2 f\,dV$
29. $\iint_\sigma (f\nabla g) \cdot \mathbf{n}\,dS = \iiint_G (f\nabla^2 g + \nabla f \cdot \nabla g)\,dV$
30. $\iint_\sigma (f\nabla g - g\nabla f) \cdot \mathbf{n}\,dS = \iiint_G (f\nabla^2 g - g\nabla^2 f)\,dV$
31. $\iint_\sigma (f\mathbf{n}) \cdot \mathbf{v}\,dS = \iiint_G \nabla f \cdot \mathbf{v}\,dV$
**32.** Powers $k$ for $\text{div}(\mathbf{r}/\|\mathbf{r}\|^k) = 0 \implies k = 3$.
**33–36.** Source and sink identification.
**37.** CAS verification.
**38–39 Writing.** Coordinate independence and physical applications.

#### QUICK CHECK ANSWERS 15.7
1. $\iint_\sigma \mathbf{F} \cdot \mathbf{n}\,dS; \quad \iiint_G \text{div}\,\mathbf{F}\,dV$  
2. 3  
3. source; sink; $\text{div}\,\mathbf{F} = 0$  
4. $4\pi c; \quad 0$

---

## 15.8 STOKES’ THEOREM

In this section we will discuss a generalization of Green’s Theorem to three dimensions that has important applications in the study of vector fields, particularly in the analysis of rotational motion of fluids. This theorem will also provide us with a physical interpretation of the curl of a vector field.

### RELATIVE ORIENTATION OF CURVES AND SURFACES

If a person walks along boundary curve $C$ with head in direction of surface normal $\mathbf{n}$ and the surface is on the person's left, $C$ has positive orientation relative to $\sigma$ (right-hand rule).

---

### STOKES’ THEOREM

> **15.8.1 THEOREM (Stokes' Theorem)**  
> Let $\sigma$ be a piecewise smooth oriented surface bounded by a simple, closed, piecewise smooth curve $C$ with positive orientation. If the components of $\mathbf{F}(x, y, z) = f(x, y, z)\mathbf{i} + g(x, y, z)\mathbf{j} + h(x, y, z)\mathbf{k}$ have continuous first partial derivatives on some open set containing $\sigma$, and if $\mathbf{T}$ is the unit tangent vector to $C$, then
> $$\oint_C \mathbf{F} \cdot \mathbf{T}\,ds = \iint_\sigma (\text{curl}\,\mathbf{F}) \cdot \mathbf{n}\,dS \tag{2}$$
> or in work integral notation:
> $$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_\sigma (\text{curl}\,\mathbf{F}) \cdot \mathbf{n}\,dS \tag{3}$$

---

> **Sir George Gabriel Stokes (1819–1903)**  
> Irish mathematician and physicist. Born in Skreen, Ireland, Stokes came from a family deeply rooted in the Church of Ireland. His father was a rector, his mother the daughter of a rector, and three of his brothers took holy orders. He received his early education from his father and a local parish clerk. In 1837, he entered Pembroke College and after graduating with top honors accepted a fellowship at the college. In 1847 he was appointed Lucasian professor of mathematics at Cambridge, a position once held by Isaac Newton (and now held by the British physicist, Stephen Hawking), but one that had lost its esteem through the years. By virtue of his accomplishments, Stokes ultimately restored the position to the eminence it once held. Unfortunately, the position paid very little and Stokes was forced to teach at the Government School of Mines during the 1850s to supplement his income.  
> Stokes was one of several outstanding nineteenth century scientists who helped turn the physical sciences in a more empirical direction. He systematically studied hydrodynamics, elasticity of solids, behavior of waves in elastic solids, and diffraction of light. For Stokes, mathematics was a tool for his physical studies. He wrote classic papers on the motion of viscous fluids that laid the foundation for modern hydrodynamics; he elaborated on the wave theory of light; and he wrote papers on gravitational variation that established him as a founder of the modern science of geodesy.  
> Stokes was honored in his later years with degrees, medals, and memberships in foreign societies. He was knighted in 1889. Throughout his life, Stokes gave generously of his time to learned societies and readily assisted those who sought his help in solving problems. He was deeply religious and vitally concerned with the relationship between science and religion.

---

### USING STOKES’ THEOREM

#### Example 1
Find work done by $\mathbf{F} = x^2\mathbf{i} + 4xy^3\mathbf{j} + y^2 x\mathbf{k}$ around rectangle $0 \le x \le 1, 0 \le y \le 3$ in plane $z = y$:
$$\text{curl}\,\mathbf{F} = 2xy\mathbf{i} - y^2\mathbf{j} + 4y^3\mathbf{k}$$
$$W = \iint_R (2xy\mathbf{i} - y^2\mathbf{j} + 4y^3\mathbf{k}) \cdot (0\mathbf{i} + \mathbf{j} - \mathbf{k})\,dA = \int_0^1 \int_0^3 (-y^2 - 4y^3)\,dy\,dx = -90$$

#### Example 2
Verify Stokes’ Theorem for $\mathbf{F} = 2z\mathbf{i} + 3x\mathbf{j} + 5y\mathbf{k}$ on $z = 4 - x^2 - y^2 \ge 0$:  
* Line integral: $C : x = 2\cos t, y = 2\sin t, z = 0 \implies \int_0^{2\pi} 12\cos^2 t\,dt = 12\pi$.  
* Surface integral: $\text{curl}\,\mathbf{F} = 5\mathbf{i} + 2\mathbf{j} + 3\mathbf{k} \implies \iint_R (10x + 4y + 3)\,dA = 3(\text{Area}) = 12\pi$.

> **REMARK (Surface Independence)**  
> If $\sigma_1$ and $\sigma_2$ are different oriented surfaces sharing the same boundary $C$:
> $$\iint_{\sigma_1}(\text{curl}\,\mathbf{F}) \cdot \mathbf{n}\,dS = \iint_{\sigma_2}(\text{curl}\,\mathbf{F}) \cdot \mathbf{n}\,dS$$

---

### CURL VIEWED AS CIRCULATION

* Circulation of $\mathbf{F}$ around $C_a$: $\oint_{C_a} \mathbf{F} \cdot \mathbf{T}\,ds$.
* Circulation density limit:
  $$\text{curl}\,\mathbf{F}(P_0) \cdot \mathbf{n} = \lim_{a \to 0} \frac{1}{\pi a^2}\oint_{C_a} \mathbf{F} \cdot \mathbf{T}\,ds \tag{9}$$
* Irrotational vector field: $\text{curl}\,\mathbf{F} = \mathbf{0}$.

---

### QUICK CHECK EXERCISES 15.8
*(See page 1166 for answers.)*

1. Line integral $\oint_C \mathbf{F} \cdot \mathbf{T}\,ds$ and surface integral $\iint_\sigma (\text{curl}\,\mathbf{F}) \cdot \mathbf{n}\,dS$ are equal.
2. If $\text{curl}\,\mathbf{F} = 5\mathbf{i} + 2\mathbf{j} + 3\mathbf{k}$, $\oint_C \mathbf{F} \cdot \mathbf{T}\,ds$ for circle of radius $a$ in $xy$-plane is $\underline{\quad}$.
3. (a) Equality of surface integrals over $\sigma_1$ and $\sigma_2$ with same boundary $C$.  
   (b) Value for paraboloid cap of radius $a$: $\underline{\quad}$.
4. Maximum circulation density occurs in the direction of the $\underline{\quad}$ of the velocity vector field.

---

### EXERCISE SET 15.8

**1–4.** Verify Stokes’ Theorem:
1. $\mathbf{F} = (x - y)\mathbf{i} + (y - z)\mathbf{j} + (z - x)\mathbf{k}; \quad \sigma : x + y + z = 1 \text{ in first octant} \implies -1/2$.
2. $\mathbf{F} = x^2\mathbf{i} + y^2\mathbf{j} + z^2\mathbf{k}; \quad \sigma : z = \sqrt{x^2+y^2} \le 1 \implies 0$.
3. $\mathbf{F} = x\mathbf{i} + y\mathbf{j} + z\mathbf{k}; \quad \sigma : z = \sqrt{a^2 - x^2 - y^2} \implies 0$.
4. $\mathbf{F} = (z - y)\mathbf{i} + (z + x)\mathbf{j} - (x + y)\mathbf{k}; \quad \sigma : z = 9 - x^2 - y^2 \ge 0 \implies 18\pi$.

**5–12.** Use Stokes’ Theorem to evaluate $\oint_C \mathbf{F} \cdot d\mathbf{r}$:
5. $\mathbf{F} = z^2\mathbf{i} + 2x\mathbf{j} - y^3\mathbf{k}; \quad C : x^2 + y^2 = 1 \text{ in } xy\text{-plane} \implies 2\pi$.
6. $\mathbf{F} = xz\mathbf{i} + 3x^2 y^2\mathbf{j} + yx\mathbf{k}; \quad C : \text{rectangle in } z = y \implies 0$.
7. $\mathbf{F} = 3z\mathbf{i} + 4x\mathbf{j} + 2y\mathbf{k}; \quad C : \text{boundary of paraboloid cap } z = 4 - x^2 - y^2 \implies 16\pi$.
8. $\mathbf{F} = -3y^2\mathbf{i} + 4z\mathbf{j} + 6x\mathbf{k}; \quad C : \text{triangle } (2, 0, 0), (0, 2, 1), (0, 0, 0) \text{ in } z = \frac{1}{2}y \implies 14$.
9. $\mathbf{F} = xy\mathbf{i} + x^2\mathbf{j} + z^2\mathbf{k}; \quad C : \text{intersection of } z = x^2 + y^2 \text{ and } z = y \implies \pi/8$.
10. $\mathbf{F} = xy\mathbf{i} + yz\mathbf{j} + zx\mathbf{k}; \quad C : \text{triangle } (1, 0, 0), (0, 1, 0), (0, 0, 1) \implies -1/2$.
11. $\mathbf{F} = (x - y)\mathbf{i} + (y - z)\mathbf{j} + (z - x)\mathbf{k}; \quad C : x^2 + y^2 = a^2 \text{ in } xy\text{-plane} \implies \pi a^2$.
12. $\mathbf{F} = (z + \sin x)\mathbf{i} + (x + y^2)\mathbf{j} + (y + e^z)\mathbf{k}; \quad C : x^2 + y^2 + z^2 = 1 \cap z = \sqrt{x^2+y^2} \implies \pi/2$.

**13–16 True–False.**
**17.** Triangle circulation and maximum circulation density direction for $\mathbf{F} = (x - z)\mathbf{i} + (y - x)\mathbf{j} + (z - xy)\mathbf{k}$.
**18.** Proof that flux of curl field across closed surface is zero.
**19–20.** Flow plots and curl determination at origin.
**21.** Proof that conservative field has $\text{curl}\,\mathbf{F} = \mathbf{0}$.
**22.** Faraday’s Law of Induction $\oint_C \mathbf{E} \cdot d\mathbf{r} = -\iint_\sigma \frac{\partial\mathbf{B}}{\partial t}\cdot\mathbf{n}\,dS \implies \text{curl}\,\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}$.
**23.** CAS verification.
**24–25 Writing.** Coordinate independence of curl; comparison of fundamental theorems.

#### QUICK CHECK ANSWERS 15.8
1. $\oint_C \mathbf{F} \cdot \mathbf{T}\,ds; \quad \iint_\sigma (\text{curl}\,\mathbf{F}) \cdot \mathbf{n}\,dS$  
2. $3\pi a^2$  
3. (a) $\iint_{\sigma_1}(\text{curl}\,\mathbf{F}) \cdot \mathbf{n}\,dS = \iint_{\sigma_2}(\text{curl}\,\mathbf{F}) \cdot \mathbf{n}\,dS$ (b) $3\pi a^2$  
4. curl

---

## CHAPTER 15 REVIEW EXERCISES

1. In words, what is a vector field? Give some physical examples of vector fields.
2. (a) Give a physical example of an inverse-square field $\mathbf{F}(\mathbf{r})$ in 3-space.  
   (b) Write a formula for a general inverse-square field $\mathbf{F}(\mathbf{r})$ in terms of the radius vector $\mathbf{r}$.  
   (c) Write a formula for a general inverse-square field $\mathbf{F}(x, y, z)$ in 3-space using rectangular coordinates.
3. Find an explicit coordinate expression for the vector field $\mathbf{F}(x, y)$ that at every point $(x, y) \neq (1, 2)$ is the unit vector directed from $(x, y)$ to $(1, 2)$.
4. Find $\nabla\left(\frac{x + y}{x - y}\right)$.
5. Find $\text{curl}(z\mathbf{i} + x\mathbf{j} + y\mathbf{k})$.
6. Let $\mathbf{F}(x, y, z) = \frac{x}{x^2+y^2}\mathbf{i} + \frac{y}{x^2+y^2}\mathbf{j} + \frac{z}{x^2+y^2}\mathbf{k}$. Sketch the level surface $\text{div}\,\mathbf{F} = 1$.
7. Assume that $C$ is the parametric curve $x = x(t), y = y(t) \; (a \le t \le b)$. In each part, express the line integral as a definite integral with variable of integration $t$:  
   (a) $\int_C f(x, y)\,dx + g(x, y)\,dy$  
   (b) $\int_C f(x, y)\,ds$
8. (a) Express the mass $M$ of a thin wire in 3-space as a line integral.  
   (b) Express the length of a curve as a line integral.
9. Give a physical interpretation of $\int_C \mathbf{F} \cdot \mathbf{T}\,ds$.
10. State some alternative notations for $\int_C \mathbf{F} \cdot \mathbf{T}\,ds$.
11. Evaluate $\int_C (x - y)\,ds; \quad C : x^2 + y^2 = 1$.
12. Evaluate $\int_C x\,dx + z\,dy - 2y^2\,dz; \quad C : x = \cos t, y = \sin t, z = t \; (0 \le t \le 2\pi)$.
13. Evaluate $\int_C \mathbf{F} \cdot d\mathbf{r}$ where $\mathbf{F}(x, y) = (x/y)\mathbf{i} - (y/x)\mathbf{j}; \quad \mathbf{r}(t) = t\mathbf{i} + 2t\mathbf{j} \; (1 \le t \le 2)$.
14. Find the work done by the force field $\mathbf{F}(x, y) = y^2\mathbf{i} + xy\mathbf{j}$ moving a particle from $(0, 0)$ to $(1, 1)$ along $y = x^2$.
15. State the Fundamental Theorem of Line Integrals, including all required hypotheses.
16. Evaluate $\int_C \nabla f \cdot d\mathbf{r}$ where $f(x, y, z) = xy^2 z^3$ and $\mathbf{r}(t) = t\mathbf{i} + (t^2 + t)\mathbf{j} + \sin(3\pi t/2)\mathbf{k} \; (0 \le t \le 1)$.
17. Let $\mathbf{F}(x, y) = y\mathbf{i} - 2x\mathbf{j}$.  
    (a) Find a nonzero function $h(x)$ such that $h(x)\mathbf{F}(x, y)$ is a conservative vector field.  
    (b) Find a nonzero function $g(y)$ such that $g(y)\mathbf{F}(x, y)$ is a conservative vector field.
18. Let $\mathbf{F}(x, y) = (ye^{xy} - 1)\mathbf{i} + xe^{xy}\mathbf{j}$.  
    (a) Show that $\mathbf{F}$ is a conservative vector field.  
    (b) Find a potential function for $\mathbf{F}$.  
    (c) Find the work performed by the force field on a particle moving along the sawtooth curve $x = t + \sin^{-1}(\sin t), y = (2/\pi)\sin^{-1}(\sin t) \; (0 \le t \le 8\pi)$.
19. State Green’s Theorem, including all of the required hypotheses.
20. Express the area of a plane region as a line integral.
21. Polar area formula via Green's Theorem: $A = \frac{1}{2}\int_\alpha^\beta [f(\theta)]^2\,d\theta$.
22. (a) Use Green’s Theorem to prove that $\oint_C f(x)\,dx + g(y)\,dy = 0$ for simple closed curve $C$.  
    (b) What does this tell you about $\mathbf{F}(x, y) = f(x)\mathbf{i} + g(y)\mathbf{j}$?
23. Express surface integral $\iint_\sigma f(x, y, z)\,dS$ over parametric surface $\mathbf{r}(u, v)$ as double integral.
24. Evaluate $\iint_\sigma z\,dS; \quad \sigma : x^2 + y^2 = 1 \; (0 \le z \le 1)$.
25. Orientability analysis of self-intersecting / Möbius type surface.
26. Physical interpretation of $\iint_\sigma \mathbf{F} \cdot \mathbf{n}\,dS$.
27. Find flux of $\mathbf{F}(x, y, z) = x\mathbf{i} + y\mathbf{j} + 2z\mathbf{k}$ through $z = 1 - x^2 - y^2 \ge 0$ upward.
28. Find flux of $\mathbf{F}(x, y, z) = x\mathbf{i} + 2y\mathbf{j} + 3z\mathbf{k}$ through unit sphere outward.
29. State the Divergence Theorem and Stokes’ Theorem, including all required hypotheses.
30. Prove $\iint_\sigma D_{\mathbf{n}}\phi\,dS = \iiint_G \left(\frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2} + \frac{\partial^2\phi}{\partial z^2}\right) dV$.
31. Evaluate $\iint_\sigma D_{\mathbf{n}} f\,dS$ for $f(x, y, z) = x^2 + y^2 + z^2$ over unit sphere with inward normal.
32. Use Stokes’ Theorem to evaluate $\iint_\sigma \text{curl}\,\mathbf{F} \cdot \mathbf{n}\,dS$ where $\mathbf{F} = (z - y)\mathbf{i} + (x + z)\mathbf{j} - (x + y)\mathbf{k}$ on $z = 2 - x^2 - y^2 \ge 1$.
33. Show that if $\mathbf{F}$ is conservative in an open spherical region, then $\text{curl}\,\mathbf{F} = \mathbf{0}$.
34–35. Test if $\mathbf{F}$ is conservative:
34. (a) $\mathbf{F} = z^2\mathbf{i} + e^{-y}\mathbf{j} + 2xz\mathbf{k}$ (b) $\mathbf{F} = xy\mathbf{i} + x^2\mathbf{j} + \sin z\mathbf{k}$
35. (a) $\mathbf{F} = \sin x\mathbf{i} + z\mathbf{j} + y\mathbf{k}$ (b) $\mathbf{F} = z\mathbf{i} + 2yz\mathbf{j} + y^2\mathbf{k}$
36. Coulomb electric force field $\mathbf{F}(\mathbf{r}) = \frac{qQ}{4\pi\epsilon_0\|\mathbf{r}\|^3}\mathbf{r}$:  
    (a) Express in coordinate form.  
    (b) Work moving $q$ along straight line from $(3, 0, 0)$ to $(3, 1, 5)$.

---

## CHAPTER 15 MAKING CONNECTIONS

Assume that the motion of a particle of mass $m$ is described by a smooth vector-valued function
$$\mathbf{r}(t) = x(t)\mathbf{i} + y(t)\mathbf{j} + z(t)\mathbf{k} \quad (a \le t \le b)$$
where $t$ denotes time. Let $C$ denote the graph of the vector-valued function and let $v(t)$ and $\mathbf{a}(t)$ denote the respective speed and acceleration of the particle at time $t$.

1. **Free Motion & Work-Kinetic Energy Theorem:**  
   When the particle is moving "freely" under the influence of force field $\mathbf{F}$, Newton's Second Law becomes $\mathbf{F}(\mathbf{r}(t)) = m\mathbf{a}(t)$. By Theorem 12.6.2 ($\mathbf{a} = \frac{dv}{dt}\mathbf{T} + \kappa v^2\mathbf{N}$):
   $$\int_C \mathbf{F} \cdot \mathbf{T}\,ds = \int_C m\left(\frac{dv}{dt}\right)ds = m\int_a^b v(t)\frac{dv}{dt}\,dt = m\int_a^b \frac{d}{dt}\left[\frac{1}{2}v(t)^2\right] dt = \frac{1}{2}m[v(b)]^2 - \frac{1}{2}m[v(a)]^2$$
   This proves that the work performed by $\mathbf{F}$ on the particle is equal to the change in kinetic energy of the particle.

2. **Constrained Motion:**  
   Suppose that the particle moves along a prescribed curve $C$ with support force $\mathbf{S}$. The resultant force is $\mathbf{F} + \mathbf{S}$. Since $\mathbf{S}$ is normal to the curve ($\mathbf{S} \cdot \mathbf{T} = 0$), the work performed by the resultant force equals the work performed by $\mathbf{F}$, which equals the change in kinetic energy:
   $$\int_C (\mathbf{F} + \mathbf{S}) \cdot \mathbf{T}\,ds = \int_C \mathbf{F} \cdot \mathbf{T}\,ds = \frac{1}{2}m[v(b)]^2 - \frac{1}{2}m[v(a)]^2$$

3. **Conservation of Energy:**  
   If $\mathbf{F}$ is conservative with potential $\phi$ and potential energy $V = -\phi$, then $\int_C \mathbf{F} \cdot \mathbf{T}\,ds = -(V_f - V_i)$. Equating this to $\frac{1}{2}mv_f^2 - \frac{1}{2}mv_i^2$ yields the total mechanical energy conservation law:
   $$\frac{1}{2}mv_i^2 + V_i = \frac{1}{2}mv_f^2 + V_f$$

4. **Playground Slide Speed:**  
   A girl with mass $m$ slides down a frictionless playground slide of length $l$ inclined at angle $\theta$ with the horizontal, starting from rest. By conservation of energy, change in kinetic energy equals loss of gravitational potential energy:
   $$\frac{1}{2}mv^2 - 0 = mgh = mgl\sin\theta \implies v = \sqrt{2gl\sin\theta}$$

---

## EXPANDING THE CALCULUS HORIZON

To learn how the topics in this chapter can be used to model hurricane behavior, see the module entitled **Hurricane Modeling** at: `www.wiley.com/college/anton`
