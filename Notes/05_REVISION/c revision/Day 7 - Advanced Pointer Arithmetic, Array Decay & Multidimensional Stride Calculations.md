---
tags:
- c
- pointers
- array-decay
- multidimensional-arrays
- pointer-arithmetic
- stride-calculation
date: 2026-08-29
day: 7
---

# Day 7: Advanced Pointer Arithmetic, Array Decay & Multidimensional Stride Calculations

---

## 1. Quick Reference & Cheat Sheet

### The Array Decay Rule (C17 §6.3.2.1)

An array expression of type `T[N]` implicitly converts ("decays") into a pointer of type `T*` pointing to its first element (`&arr[0]`), **EXCEPT** in exactly three circumstances:

1. **Operand of `sizeof`:** `sizeof(arr)` evaluates to the total memory footprint in bytes ($N \times \text{sizeof}(T)$), not the pointer size.

2. **Operand of Address-of (`&`):** `&arr` yields a pointer to the entire array of type `T (*)[N]`, not a pointer-to-pointer (`T**`).

3. **String Literal Initializer:** Used to initialize a character array (e.g. `char s[] = "abc";`).

### Array vs Pointer Comparison

| Characteristic | Array (`int arr[5];`) | Pointer (`int *ptr;`) |

| :--- | :--- | :--- |

| **Storage Allocation** | 20 contiguous bytes reserved in memory | 8 bytes of address storage reserved |

| **Lvalue / Mutability** | Non-modifiable lvalue (`arr = ...` is illegal) | Modifiable lvalue (`ptr = ...` is legal) |

| **`sizeof` Evaluation** | Returns total array byte size (20) | Returns pointer architecture size (8 on 64-bit) |

| **`&` (Address-of)** | `&arr` has type `int (*)[5]` (value is same address) | `&ptr` has type `int**` (address of the pointer variable) |

| **Target Address** | Fixed at allocation time | Can be redirected to arbitrary memory addresses |

### Multidimensional Indexing & Stride Formulations

For a 2D array `int matrix[R][C]`:

* **Row-Major Memory Layout:** Contiguous in RAM. Row $0$ is followed immediately by Row $1$.

* **Offset Formula:** Address of `matrix[r][c]` = $\text{Base} + (r \times C + c) \times \text{sizeof}(\text{int})$.

* **Pointer Arithmetic Equivalence:** `matrix[r][c] == *(*(matrix + r) + c) == *(matrix[r] + c)`.

* **Type of `matrix` when decayed:** `int (*)[C]` (Pointer to an array of $C$ integers).

---

## 2. In-Depth Theory & Low-Level Mechanics

### A. Pointer-to-Array (`T (*)[N]`) vs Array-of-Pointers (`T *[N]`)

Parentheses drastically alter compiler type parsing:

```c
// 1. Array of Pointers: 4 separate pointers in contiguous memory (32 bytes on 64-bit)
int *arr_of_ptrs[4];
// Each element can point to a separate, non-contiguous block in heap or stack.
// 2. Pointer to an Array: A single pointer variable (8 bytes on 64-bit)
int (*ptr_to_arr)[4];
// Points to a contiguous block of exactly 4 integers.
```

#### Pointer Arithmetic Scaling Differences:

```c
int grid[3][4] = {0};
int *p_elem = &grid[0][0]; // Type: int*
int (*p_row)[4] = grid; // Type: int (*)[4]
// Advancing by 1:
p_elem + 1; // Advances by 1 * sizeof(int) = 4 bytes (next column element)
p_row + 1; // Advances by 1 * sizeof(int[4]) = 16 bytes (next entire ROW!)
```

---

### B. Passing Multidimensional Arrays to Functions

When passing a 2D array to a function, the compiler **must know the column width** at compile-time (or runtime in C99 VLAs) to calculate row stride offsets:

```c
// ILLEGAL: Compiler cannot compute row strides!
// void process_grid(int matrix[][]); // ERROR: array has incomplete element type
// LEGAL: Compile-time fixed column size
void process_grid_fixed(int matrix[][4], size_t rows);
void process_grid_fixed_alt(int (*matrix)[4], size_t rows);
// LEGAL: C99 Variable Length Array (VLA) parameter notation (Cols MUST precede Matrix)
void process_grid_vla(size_t rows, size_t cols, int matrix[rows][cols]) {
for (size_t r = 0; r < rows; r++) {
for (size_t c = 0; c < cols; c++) {
matrix[r][c] += 1; // Compiler calculates stride using 'cols' parameter!
}
}
}
```

---

### C. Cache Locality & Row-Major Traversal Benchmarks

Because modern CPUs load contiguous memory into cache lines (typically 64 bytes per line), traversing a 2D matrix row-wise utilizes pre-fetched data, whereas column-wise traversal triggers constant cache misses.

```text
Memory Buffer: [ (0,0) (0,1) (0,2) (0,3) ] [ (1,0) (1,1) (1,2) (1,3) ]
Row-Wise (Fast): ───► ───► ───► ───► (Stride: 1 element, sequential access)
Col-Wise (Slow): ───► ───► (Stride: C elements, cache misses!)
```

---

## 3. Thoughtful Mini-Project (~1 Hour Scope)

### Project Title: Contiguous 2D Tensor / Matrix Engine with Strided Slice Views (`tensor2d`)

#### Objective

Build a cache-friendly, flat-buffer 2D Matrix engine in C that supports dynamic creation, zero-copy submatrix slicing (views), and cache-optimized matrix multiplication using pointer stride arithmetic.

#### Functional Requirements

1. **Core Data Structure:**

```c
typedef struct {
size_t rows;
size_t cols;
size_t stride_row; // Elements to advance per row step (crucial for zero-copy slicing!)
size_t stride_col; // Elements to advance per col step
double *data; // Contiguous memory buffer
bool is_view; // True if viewing a parent matrix (prevents double-free)
} Tensor2D;
```

2. **Operations:**

* `tensor_create(rows, cols)`: Single contiguous `malloc(rows * cols * sizeof(double))`.

* `tensor_free(tensor)`: Frees memory if not a slice view.

* `tensor_set(t, r, c, val)` and `tensor_get(t, r, c)`: Calculated via `data[r * stride_row + c * stride_col]`.

* `tensor_slice(src, r_start, r_len, c_start, c_len)`: Creates a zero-copy sub-view sharing the parent's memory buffer.

* `tensor_matmul(A, B, out)`: Cache-aware multiplication (`i-k-j` loop ordering).

#### Complete Starter Code Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <string.h>
typedef struct {
size_t rows;
size_t cols;
size_t stride_row;
size_t stride_col;
double *data;
bool is_view;
} Tensor2D;
Tensor2D *tensor_create(size_t rows, size_t cols) {
if (rows == 0 || cols == 0) return NULL;
Tensor2D *t = (Tensor2D *)malloc(sizeof(Tensor2D));
if (!t) return NULL;
t->data = (double *)malloc(rows * cols * sizeof(double));
if (!t->data) {
free(t);
return NULL;
}
t->rows = rows;
t->cols = cols;
t->stride_row = cols; // Standard row-major stride
t->stride_col = 1;
t->is_view = false;
memset(t->data, 0, rows * cols * sizeof(double));
return t;
}
void tensor_free(Tensor2D *t) {
if (!t) return;
if (!t->is_view && t->data) {
free(t->data);
}
free(t);
}
static inline void tensor_set(Tensor2D *t, size_t r, size_t c, double val) {
assert(r < t->rows && c < t->cols);
t->data[r * t->stride_row + c * t->stride_col] = val;
}
static inline double tensor_get(const Tensor2D *t, size_t r, size_t c) {
assert(r < t->rows && c < t->cols);
return t->data[r * t->stride_row + c * t->stride_col];
}
// Zero-copy submatrix view
Tensor2D *tensor_slice(const Tensor2D *src, size_t r_start, size_t r_len, size_t c_start, size_t c_len) {
assert(src != NULL);
assert(r_start + r_len <= src->rows);
assert(c_start + c_len <= src->cols);
Tensor2D *view = (Tensor2D *)malloc(sizeof(Tensor2D));
if (!view) return NULL;
view->rows = r_len;
view->cols = c_len;
view->stride_row = src->stride_row; // Inherits parent's row stride!
view->stride_col = src->stride_col;
view->data = src->data + (r_start * src->stride_row + c_start * src->stride_col);
view->is_view = true;
return view;
}
// Cache-friendly Matrix Multiplication (i-k-j loop order)
bool tensor_matmul(const Tensor2D *A, const Tensor2D *B, Tensor2D *out) {
if (!A || !B || !out || A->cols != B->rows || out->rows != A->rows || out->cols != B->cols) {
return false;
}
for (size_t i = 0; i < out->rows; i++) {
for (size_t j = 0; j < out->cols; j++) {
tensor_set(out, i, j, 0.0);
}
}
// i-k-j loop ordering maximizes cache line re-use for B
for (size_t i = 0; i < A->rows; i++) {
for (size_t k = 0; k < A->cols; k++) {
double a_ik = tensor_get(A, i, k);
for (size_t j = 0; j < B->cols; j++) {
double current = tensor_get(out, i, j);
tensor_set(out, i, j, current + a_ik * tensor_get(B, k, j));
}
}
}
return true;
}
void tensor_print(const Tensor2D *t, const char *label) {
printf("=== Tensor: %s (%zux%zu, Stride: %zu, %s) ===\n",
label, t->rows, t->cols, t->stride_row, t->is_view ? "VIEW" : "OWNER");
for (size_t r = 0; r < t->rows; r++) {
printf(" [ ");
for (size_t c = 0; c < t->cols; c++) {
printf("%6.2f ", tensor_get(t, r, c));
}
printf("]\n");
}
printf("\n");
}
int main(void) {
// 1. Create 4x4 parent matrix
Tensor2D *mat = tensor_create(4, 4);
double counter = 1.0;
for (size_t r = 0; r < 4; r++) {
for (size_t c = 0; c < 4; c++) {
tensor_set(mat, r, c, counter++);
}
}
tensor_print(mat, "Original 4x4 Matrix");
// 2. Extract zero-copy 2x2 submatrix view (rows 1-2, cols 1-2)
Tensor2D *sub_view = tensor_slice(mat, 1, 2, 1, 2);
tensor_print(sub_view, "Zero-Copy 2x2 Center Sub-view");
// Mutate view and verify mutation reflects in parent
tensor_set(sub_view, 0, 0, 99.0);
printf("Mutated sub_view[0,0] to 99.0:\n");
tensor_print(mat, "Parent Matrix After View Mutation");
// 3. Test Matrix Multiplication
Tensor2D *A = tensor_create(2, 3);
Tensor2D *B = tensor_create(3, 2);
Tensor2D *C = tensor_create(2, 2);
tensor_set(A, 0, 0, 1); tensor_set(A, 0, 1, 2); tensor_set(A, 0, 2, 3);
tensor_set(A, 1, 0, 4); tensor_set(A, 1, 1, 5); tensor_set(A, 1, 2, 6);
tensor_set(B, 0, 0, 7); tensor_set(B, 0, 1, 8);
tensor_set(B, 1, 0, 9); tensor_set(B, 1, 1, 1);
tensor_set(B, 2, 0, 2); tensor_set(B, 2, 1, 3);
tensor_matmul(A, B, C);
tensor_print(C, "Matrix Multiplication Result (A x B)");
tensor_free(sub_view);
tensor_free(mat);
tensor_free(A);
tensor_free(B);
tensor_free(C);
return 0;
}
```

---

## 4. Error Handling & Defensive Programming Challenge

### Scenario: The Double-Pointer Matrix Casting & Jagged Memory Deallocation Bug

Examine the following buggy 2D matrix allocation and processing code:

```c
#include <stdio.h>
#include <stdlib.h>
// BUGGY IMPLEMENTATION
void process_square_matrix(int **matrix, size_t n) {
// Problem: If caller passes 'int grid[4][4]', passing it as 'int**' causes CRASH!
// Reason: 'grid' decays to 'int (*)[4]', which is NOT compatible with 'int**'.
for (size_t i = 0; i < n; i++) {
for (size_t j = 0; j < n; j++) {
printf("%d ", matrix[i][j]);
}
printf("\n");
}
}
// BUGGY JAGGED ALLOCATOR
int **create_jagged_matrix(size_t rows, size_t cols) {
int **m = (int **)malloc(rows * sizeof(int *));
for (size_t i = 0; i < rows; i++) {
// Leak Bug: If malloc fails on i = 5, previous 0..4 chunks are leaked!
m[i] = (int *)malloc(cols * sizeof(int));
}
return m;
}
```

### Analysis of Vulnerabilities:

1. **Type Incompatibility (`T**` vs `T[R][C]`):** A 2D array `int grid[4][4]` is a contiguous 64-byte block of memory. When cast to `int**`, the expression `matrix[i]` dereferences the first 4 bytes of integer data as if they were a 64-bit pointer address, causing an immediate segmentation fault (`SIGSEGV`).

2. **Partial Allocation Memory Leak:** In loop-based jagged allocations, if allocation fails mid-way, returning `NULL` without unwinding and freeing previously allocated rows causes permanent memory leaks.

### Defensive Fix (Contiguous Allocation with Atomic Rollback):

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
// Fix 1: True flat contiguous allocation with pointer array wrapper
int **create_matrix_safe(size_t rows, size_t cols) {
if (rows == 0 || cols == 0) return NULL;
// Allocate row pointers
int **row_ptrs = (int **)malloc(rows * sizeof(int *));
if (!row_ptrs) return NULL;
// Allocate contiguous payload in ONE single allocation block
int *payload = (int *)malloc(rows * cols * sizeof(int));
if (!payload) {
free(row_ptrs);
return NULL;
}
// Set up row pointers to slice the contiguous payload
for (size_t i = 0; i < rows; i++) {
row_ptrs[i] = payload + (i * cols);
}
return row_ptrs;
}
// Fix 2: Clean atomic deallocation
void free_matrix_safe(int **matrix) {
if (!matrix) return;
if (matrix[0]) {
free(matrix[0]); // Free single contiguous payload
}
free(matrix); // Free pointer table
}
```
