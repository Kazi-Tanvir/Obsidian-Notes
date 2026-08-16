# Chapter 4: Number Theory and Cryptography

The part of mathematics devoted to the study of the set of integers and their properties is known as **number theory**. In this chapter we will develop some of the important concepts of number theory including many of those used in computer science. As we develop number theory, we will use the proof methods developed in Chapter 1 to prove many theorems.

We will first introduce the notion of divisibility of integers, which we use to introduce modular, or clock, arithmetic. Modular arithmetic operates with the remainders of integers when they are divided by a fixed positive integer, called the modulus. We will prove many important results about modular arithmetic which we will use extensively in this chapter.

Integers can be represented with any positive integer $b$ greater than 1 as a base. In this chapter we discuss base $b$ representations of integers and give an algorithm for finding them. In particular, we will discuss binary, octal, and hexadecimal (base 2, 8, and 16) representations. We will describe algorithms for carrying out arithmetic using these representations and study their complexity. These algorithms were the first procedures called algorithms.

We will discuss prime numbers, the positive integers that have only 1 and themselves as positive divisors. We will prove that there are infinitely many primes; the proof we give is considered to be one of the most beautiful proofs in mathematics. We will discuss the distribution of primes and many famous open questions concerning primes. We will introduce the concept of greatest common divisors and study the Euclidean algorithm for computing them. This algorithm was first described thousands of years ago. We will introduce the fundamental theorem of arithmetic, a key result which tells us that every positive integer has a unique factorization into primes.

We will explain how to solve linear congruences, as well as systems of linear congruences, which we solve using the famous Chinese remainder theorem. We will introduce the notion of pseudoprimes, which are composite integers masquerading as primes, and show how this notion can help us rapidly generate prime numbers.

This chapter introduces several important applications of number theory. In particular, we will use number theory to generate pseudorandom numbers, to assign memory locations to computer files, and to find check digits used to detect errors in various kinds of identification numbers. We also introduce the subject of cryptography. Number theory plays an essential role both in classical cryptography, first used thousands of years ago, and modern cryptography, which plays an essential role in electronic communication. We will show how the ideas we develop can be used in cryptographical protocols, introducing protocols for sharing keys and for sending signed messages. Number theory, once considered the purest of subjects, has become an essential tool in providing computer and Internet security.

---

## 4.1 Divisibility and Modular Arithmetic

### 4.1.1 Division

> **Definition 1**  
> If $a$ and $b$ are integers with $a \neq 0$, we say that $a$ **divides** $b$ if there is an integer $c$ such that $b = ac$ (or equivalently, $b/a$ is an integer). We write $a \mid b$ when $a$ divides $b$, and $a \nmid b$ when $a$ does not divide $b$.

> **THEOREM 1**  
> Let $a, b, c$ be integers with $a \neq 0$:  
> (i) If $a \mid b$ and $a \mid c$, then $a \mid (b + c)$;  
> (ii) If $a \mid b$, then $a \mid bc$ for all integers $c$;  
> (iii) If $a \mid b$ and $b \mid c$, then $a \mid c$.

> **COROLLARY 1**  
> If $a \mid b$ and $a \mid c$, then $a \mid (mb + nc)$ for all integers $m, n$.

### 4.1.2 The Division Algorithm

> **THEOREM 2 (The Division Algorithm)**  
> Let $a$ be an integer and $d$ a positive integer. Then there are unique integers $q$ and $r$, with $0 \le r < d$, such that  
> $$a = dq + r$$  
> where $q = a \text{ div } d = \lfloor a/d \rfloor$ (quotient) and $r = a \bmod d = a - d\lfloor a/d \rfloor$ (remainder).

### 4.1.3 Modular Arithmetic

> **Definition 3**  
> If $a, b \in \mathbf{Z}$ and $m \in \mathbf{Z}^+$, $a$ is **congruent to** $b$ **modulo** $m$ ($a \equiv b \pmod m$) if $m \mid (a - b)$.

> **THEOREM 3 & 4**  
> - $a \equiv b \pmod m \iff a \bmod m = b \bmod m$.  
> - $a \equiv b \pmod m \iff a = b + km$ for some integer $k$.

> **THEOREM 5**  
> If $a \equiv b \pmod m$ and $c \equiv d \pmod m$, then:  
> $$a + c \equiv b + d \pmod m \quad \text{and} \quad ac \equiv bd \pmod m$$

> **COROLLARY 2**  
> - $(a + b) \bmod m = ((a \bmod m) + (b \bmod m)) \bmod m$  
> - $ab \bmod m = ((a \bmod m)(b \bmod m)) \bmod m$

> **KARL FRIEDRICH GAUSS (1777–1855)**  
> “Prince of Mathematics.” Laid the foundations of modern number theory with his 1801 treatise *Disquisitiones Arithmeticae*, introducing congruence notation and modular arithmetic.

---

## 4.2 Integer Representations and Algorithms

### 4.2.1 Base $b$ Expansions

> **THEOREM 1**  
> Let $b > 1$ be an integer. Every positive integer $n$ can be expressed uniquely as:  
> $$n = a_k b^k + a_{k-1} b^{k-1} + \dots + a_1 b + a_0$$  
> where $0 \le a_i < b$ and $a_k \neq 0$. Notated as $(a_k a_{k-1} \dots a_1 a_0)_b$.

- **Binary (base 2):** Digits 0, 1.
- **Octal (base 8):** Digits 0–7 (each octal digit = 3 binary digits).
- **Hexadecimal (base 16):** Digits 0–9, A–F (each hex digit = 4 binary digits).

```pascal
ALGORITHM 1 Constructing Base b Expansions.
procedure base b expansion(n, b: positive integers with b > 1)
  q := n
  k := 0
  while q != 0
    ak := q mod b
    q := q div b
    k := k + 1
  return (ak-1, ..., a1, a0)
```

### 4.2.2 Fast Modular Exponentiation

```pascal
ALGORITHM 5 Fast Modular Exponentiation.
procedure modular exponentiation(b: integer, n = (ak-1...a1a0)2, m: positive integers)
  x := 1
  power := b mod m
  for i := 0 to k - 1
    if ai = 1 then x := (x * power) mod m
    power := (power * power) mod m
  return x {x = b^n mod m}
```
*Complexity:* $O((\log m)^2 \log n)$ bit operations.

---

## 4.3 Primes and Greatest Common Divisors

### 4.3.1 Primes & Fundamental Theorem of Arithmetic

> **Definition 1**  
> An integer $p > 1$ is **prime** if its only positive factors are 1 and $p$. Otherwise, it is **composite**.

> **THEOREM 1 (Fundamental Theorem of Arithmetic)**  
> Every integer $n > 1$ can be written uniquely as a prime or as the product of two or more primes in nondecreasing order: $n = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$.

> **THEOREM 2**  
> If $n$ is composite, then $n$ has a prime divisor $\le \sqrt{n}$.

> **THEOREM 3 (Euclid)**  
> There are infinitely many primes.

> **THEOREM 4 (Prime Number Theorem)**  
> $\lim_{x \to \infty} \frac{\pi(x)}{x / \ln x} = 1$, where $\pi(x)$ is the prime counting function.

> **MARIN MERSENNE (1588–1648)**  
> French Minim monk who studied primes of the form $M_p = 2^p - 1$ (*Mersenne primes*).

> **TERENCE TAO (BORN 1975) & YITANG ZHANG (BORN 1955)**  
> Fields Medalist Tao (co-prover of Green-Tao theorem on prime arithmetic progressions) and Zhang (proved bounded prime gaps $< 70\text{ million}$ in 2013).

### 4.3.2 Greatest Common Divisor and GCD Algorithms

> **Definition 2 & 3**  
> - $\gcd(a, b)$ is the largest integer dividing both $a$ and $b$.  
> - $a$ and $b$ are **relatively prime** if $\gcd(a, b) = 1$.  
> - $a_1, \dots, a_n$ are **pairwise relatively prime** if $\gcd(a_i, a_j) = 1$ for all $i \neq j$.

> **THEOREM 5**  
> $ab = \gcd(a, b) \cdot \operatorname{lcm}(a, b)$.

```pascal
ALGORITHM 1 The Euclidean Algorithm.
procedure gcd(a, b: positive integers)
  x := a
  y := b
  while y != 0
    r := x mod y
    x := y
    y := r
  return x {gcd(a, b) is x}
```

> **THEOREM 6 (Bézout’s Theorem)**  
> If $a, b \in \mathbf{Z}^+$, there exist integers $s, t$ such that $\gcd(a, b) = sa + tb$. ($s, t$ are **Bézout coefficients**).

> **ÉTIENNE BÉZOUT (1730–1783)**  
> French mathematician, author of influential textbooks and creator of Bézout's identity and algebraic elimination theory.

---

## 4.4 Solving Congruences

### 4.4.1 Linear Congruences & Inverses

> **THEOREM 1**  
> If $\gcd(a, m) = 1$ and $m > 1$, then the inverse $\bar{a}$ of $a$ modulo $m$ (satisfying $a\bar{a} \equiv 1 \pmod m$) exists and is unique modulo $m$.

### 4.4.2 Chinese Remainder Theorem

> **THEOREM 2 (Chinese Remainder Theorem)**  
> Let $m_1, m_2, \dots, m_n$ be pairwise relatively prime positive integers $> 1$. The system:
> $$\begin{aligned}
> x &\equiv a_1 \pmod{m_1} \\
> x &\equiv a_2 \pmod{m_2} \\
> &\;\;\vdots \\
> x &\equiv a_n \pmod{m_n}
> \end{aligned}$$
> has a unique solution modulo $m = m_1 m_2 \dots m_n$ given by:
> $$x \equiv \sum_{k=1}^n a_k M_k y_k \pmod m$$
> where $M_k = m / m_k$ and $M_k y_k \equiv 1 \pmod{m_k}$.

### 4.4.3 Fermat’s Little Theorem & Pseudoprimes

> **THEOREM 3 (Fermat’s Little Theorem)**  
> If $p$ is prime and $p \nmid a$, then $a^{p-1} \equiv 1 \pmod p$. (For all $a$, $a^p \equiv a \pmod p$).

- **Pseudoprime to base $b$:** Composite $n$ where $b^{n-1} \equiv 1 \pmod n$.
- **Carmichael Number:** Composite $n$ where $b^{n-1} \equiv 1 \pmod n$ for all $\gcd(b, n) = 1$ (e.g., $561 = 3 \cdot 11 \cdot 17$).
- **Primitive Root:** $r \in \mathbf{Z}_p$ whose powers generate all nonzero elements of $\mathbf{Z}_p$.
- **Discrete Logarithm:** $e = \log_r a$ where $r^e \equiv a \pmod p$.

---

## 4.5 Applications of Congruences

1. **Hashing Functions:** $h(k) = k \bmod m$. Linear probing $h(k, i) = (h(k) + i) \bmod m$ resolves collisions.
2. **Pseudorandom Number Generators:** Linear congruential generator $x_{n+1} = (ax_n + c) \bmod m$.
3. **Check Digits:**
   - **Parity bit:** $x_{n+1} = \sum_{i=1}^n x_i \bmod 2$.
   - **UPC (12-digit):** $3x_1 + x_2 + 3x_3 + \dots + 3x_{11} + x_{12} \equiv 0 \pmod{10}$.
   - **ISBN-10:** $\sum_{i=1}^{10} i x_i \equiv 0 \pmod{11}$. Detects all single and transposition errors.
   - **USPS Money Orders:** $x_{11} = \sum_{i=1}^{10} x_i \bmod 9$.
   - **Airline Tickets:** $a_{15} = a_1 a_2 \dots a_{14} \bmod 7$.

---

## 4.6 Cryptography

### 4.6.1 Classical Ciphers
- **Caesar / Shift Cipher:** $f(p) = (p + k) \bmod 26$, $f^{-1}(c) = (c - k) \bmod 26$.
- **Affine Cipher:** $f(p) = (ap + b) \bmod 26$ with $\gcd(a, 26) = 1$; decryption $p = \bar{a}(c - b) \bmod 26$.
- **Block Transposition Cipher:** Permutes blocks of $m$ characters by permutation $\sigma$.

### 4.6.2 The RSA Cryptosystem
1. Choose large primes $p, q$. Compute $n = pq$ and $\phi(n) = (p-1)(q-1)$.
2. Choose $e$ such that $\gcd(e, \phi(n)) = 1$. Public Key: $(n, e)$.
3. Compute private key $d$ such that $de \equiv 1 \pmod{(p-1)(q-1)}$.
4. **Encryption:** $c = m^e \bmod n$.
5. **Decryption:** $m = c^d \bmod n$.

> **CLIFFORD COCKS (BORN 1950)**  
> British mathematician at GCHQ who originally discovered public-key cryptography and RSA in 1973.

> **RIVEST, SHAMIR, & ADLEMAN (RSA)**  
> Ronald Rivest, Adi Shamir, and Leonard Adleman introduced public-key RSA cryptography at MIT in 1976.

### 4.6.3 Protocols & Homomorphic Encryption
- **Diffie-Hellman Key Exchange:** Alice and Bob compute shared key $(a^{k_2})^{k_1} \equiv (a^{k_1})^{k_2} \equiv a^{k_1 k_2} \pmod p$ without sharing secret exponents.
- **Digital Signatures:** Encrypt with sender's private key $D_{(n,e)}(m)$, verified by sender's public key $E_{(n,e)}$.
- **Homomorphic Encryption:** RSA is multiplicatively homomorphic ($E(m_1)E(m_2) \equiv E(m_1 m_2) \pmod n$). Craig Gentry constructed the first fully homomorphic encryption scheme in 2009.
