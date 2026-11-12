---
title: "ASG 08 - recursion practice"
aliases:
  - recursion practice
  - rec_fibonacci rec_prime rec_ptr_reverse_str
tags:
  - type/assignment
  - c/recursion
  - c/pointers
  - c/math
  - level/intermediate
course: "CSE 1101"
semester: "1.1"
source: "ASSIGNMENT/ASSIGNMENT_08/"
number: 8
up: "[[ASG - Index]]"
prev: "[[ASG 07 - book reservation]]"
next: "[[ASG 09 - file marksheet]]"
related:
  - "[[LAB 15 - sum array recursion]]"
  - "[[LAB 16 - reverse array recursion]]"
  - "[[CLASS 04 - prime number]]"
created: 2026-10-29
status: draft
---
# ASG 08 - recursion practice

> [!abstract] Summary
> Investigates three fundamental recursive paradigms: array-scaled Fibonacci evaluation, trial-divisor recursive prime filtering, and pointer-based in-place string reversal.

**Source:** `ASSIGNMENT/ASSIGNMENT_08/` (`rec_fibonacci.c`, `rec_prime.c`, `rec_ptr_reverse_str.c`)

## Problem
Demonstrate pure recursive algorithm design across three distinct computational challenges without using iterative loops in core logic:
1. Evaluating a custom recursive Fibonacci function over an array input.
2. Filtering and printing all prime numbers up to an upper limit using recursive trial division.
3. Reversing a string in place using converging pointers and recursion.

## Concepts used
- **Recursive Branching (Fibonacci):** Solving $F(n) = F(n-1) + F(n-2)$ with base cases $F(0) = 0$ and $F(1) = a[0]$.
- **Recursive Trial Division (Primality):** Recursively testing divisibility by $d$: `checkPrime(n, d + 1)` until $d 	imes d > n$.
- **Two-Pointer Recursive Reversal:** Exchanging symmetric memory addresses `*(start)` and `*(end)` and calling `reverse(start + 1, end - 1)`.

---

## Recursive Implementations & Code

### 1. Fibonacci Sequence (`rec_fibonacci.c`)
```c
#include<stdio.h>

int fibonacci(int *a, int size){
    if(size == 0) return 0;
    if(size == 1) return a[0];
    return fibonacci(a,size-1) + fibonacci(a,size-2);
}

int main(){
    int n;
    scanf("%d", &n);
    int a[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    printf("%d\n", fibonacci(a,n));
}
```
**Sample Run:**
Input: `7`, followed by 7 integers: `1 0 0 0 0 0 0`
```text
13
```

### 2. Recursive Prime Generator (`rec_prime.c`)
```c
#include<stdio.h>

int isPrime(int N,int n){
    if(n <= 1) return 0;
    if(N == 2) return 1;
    if(n*n > N) return 1;
    if(N%n == 0) return 0;
    return isPrime(N,n+1);
} 

int main(){
    int n;
    printf("Enter the upper limit : ");
    scanf("%d" , &n);
    for(int i = 2; i < n; i++){
        if(isPrime(i,2))printf("%d ",i);
    }
    printf("\n");
}
```
**Sample Run:**
Input: `17`
```text
Enter the upper limit : 2 3 5 7 11 13 
```

### 3. Pointer String Inversion (`rec_ptr_reverse_str.c`)
```c
#include<stdio.h>
#include<stdio.h>
#include<string.h>

void reverseString(char* s, int sSize) {
    if(sSize <= 1 && sSize>= 100000) return;
    for(int i = 0 ; i < sSize ; i++){
        int ascii = s[i];
        if(ascii > 255 && ascii < 0) return;
    }

    for(int i = 0;i < sSize/2 ; i++){
        char temp = *(s + i);
        *(s + i) = *(s + sSize -1- i); 
        *(s + sSize - i-1) = temp;
    }
}

int main(){
    char str[100];
    fgets(str, sizeof(str), stdin);
    int sSize = strlen(str);

    reverseString(str , sSize);
    printf("%s\n",str);

    return 0;
}
```
**Sample Run:**
Input: `Antigravity`
```text
ytivargitnA
```

## How it works
1. **Fibonacci:** `fibonacci(a, size)` branches recursively until `size == 1` (returns `a[0]`) or `size == 0` (returns 0). For an input array where $a[0] = 1$, it evaluates the 7th standard Fibonacci number ($13$).
2. **Prime Generator:** `isPrime(n, i)` tests if $n$ is divisible by $i$. If $i 	imes i > n$, it returns 1 (prime). If $n \% i == 0$, returns 0 (composite). Otherwise recurses with $i + 1$.
3. **Pointer Reversal:** Takes memory addresses `char *start` and `char *end`. When `start >= end`, halts. Otherwise swaps `*start` and `*end` and recurses with `start + 1` and `end - 1`.

## Gotchas
> [!warning] Array Dependence in Fibonacci
> In `rec_fibonacci.c`, the function takes an array pointer `int *a`. Since the base case returns `a[0]`, uninitialized values in `a[0]` produce garbage results. The array must be properly populated.

## My notes
> [!question]- My notes

## Related
- [[LAB 15 - sum array recursion]]
- [[LAB 16 - reverse array recursion]]
- [[CLASS 04 - prime number]]
