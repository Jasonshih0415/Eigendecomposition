# Eigendecomposition

The `matrix_compute` class is designed to compute eigenvalues and eigenvectors of a 2x2 matrix using a direct formula-based approach. This implementation is specifically tailored for 2x2 matrices and is both efficient and straightforward.

---

## Features
- **Eigenvalue Calculation:** Uses the coefficients of the quadratic equation derived from the matrix to compute eigenvalues.
- **Eigenvector Calculation:** Uses the first row of the matrix to compute the ratio of \(x_2\) to \(x_1\) and derive the eigenvectors.
- **Special Case Handling:** Provides predefined outputs for the zero matrix.

---
## calculation
- #### matrix A :
$$\begin{bmatrix} 
a & b \\ 
c & d 
\end{bmatrix}$$

- #### $ A-\lambda*I=0 $ :
$$\begin{bmatrix} 
a-\lambda & b \\ 
c & d-\lambda 
\end{bmatrix}$$

- #### Determinant:
$$\lambda^2 - (a+d)\lambda+(ad-bc) = 0$$

- #### eqution parameter
$$
A = 1\\ 
B = -(a + d)\\ 
C = (ad - bc)
$$

- #### Eigenvalues:
$$
\lambda_{1,2} = \frac{-B \pm \sqrt{B^2 - 4AC}}{2A}
$$

- #### Eigenvectors
$$
x_{i1} = 1 \\
Scaler = -(a-\lambda_{i})/b \\
x_{i2} = x_{i1}*Scaler \\
Eigenvalue_{i} = [x_{i1},x_{2}]
$$

## Installation

Clone the repository and ensure you have Python installed:
```bash
# Clone the repository
git clone https://github.com/username/matrix_compute.git

# Navigate to the project directory
cd matrix_compute
