# Remote Development Project Report

**Student Name**: Zixuan Gao  
**Student ID**: ZY2557203  

## System Configuration

The following table lists the configuration of the remote workstation used for this assignment. The development environment is based on WSL2 with Ubuntu 24.04.

| Item | Configuration |
| :--- | :--- |
| **CPU Model** | Intel Core Ultra 9 275 HX (24-core architecture, 18 threads allocated to WSL) |
| **Memory Size** | 15 GiB allocated to WSL |
| **Operating System Version** | Linux DESKTOP-L9OGAD6 5.15.167.4-microsoft-standard-WSL2 x86_64 (Ubuntu 24.04) |
| **Compiler Version** | gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 |
| **Python Version** | Python 3.12.9 |

These system details were checked using the following Unix/Linux commands:

~~~bash
lscpu
free -h
uname -a
gcc --version
python --version
~~~

## Implementation Details

In this assignment, I used a Unix/Linux command line environment under WSL2 to implement and test matrix multiplication in Python. The purpose of the project was not only to write a working program, but also to become familiar with command line operations and Markdown-based technical documentation.

The main task was to implement matrix multiplication manually without relying on external numerical libraries such as NumPy. This makes the algorithm easier to understand and verify. The implementation follows the standard definition of matrix multiplication:

- If matrix A has size m × n
- and matrix B has size n × p

then the result matrix C has size m × p, where each element is computed as:

C[i][j] = A[i][0] × B[0][j] + A[i][1] × B[1][j] + ... + A[i][n-1] × B[n-1][j]

The algorithm used in this assignment is the classical triple-loop method. It is simple, clear, and suitable for correctness verification.

## Python Language Implementation

- **Source Code**: Include the Python script with comments explaining key sections.
- **Execution Command**: Describe how to run the Python script.

### Source Code

~~~python
def matrix_multiply(A, B):
    """
    Multiply two matrices A and B using the standard triple-loop algorithm.
    A: list of lists, shape (m, n)
    B: list of lists, shape (n, p)
    Returns:
        Result matrix C with shape (m, p)
    """
    # Check if the matrices are empty
    if not A or not B:
        raise ValueError("Input matrices must not be empty.")

    # Check if dimensions are valid for multiplication
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions do not match for multiplication.")

    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Initialize result matrix with zeros
    C = [[0 for _ in range(p)] for _ in range(m)]

    # Triple-loop matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def print_matrix(M, name="Matrix"):
    print(f"{name}:")
    for row in M:
        print(row)
    print()


def main():
    # Example 1: square matrices
    A = [
        [1, 2],
        [3, 4]
    ]

    B = [
        [5, 6],
        [7, 8]
    ]

    C = matrix_multiply(A, B)

    print_matrix(A, "A")
    print_matrix(B, "B")
    print_matrix(C, "A x B")

    # Example 2: identity matrix test
    I = [
        [1, 0],
        [0, 1]
    ]

    D = matrix_multiply(A, I)
    print_matrix(D, "A x I")

    # Example 3: rectangular matrix multiplication
    E = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    F = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    G = matrix_multiply(E, F)
    print_matrix(E, "E")
    print_matrix(F, "F")
    print_matrix(G, "E x F")


if __name__ == "__main__":
    main()
~~~

### Execution Command

Save the file as `matrix_multiply.py`, then run it using:

~~~bash
python3 matrix_multiply.py
~~~

## Algorithm Verification

- **Correctness**: Explain the methodology used to verify the correctness of the matrix multiplication algorithm.

To verify the correctness of the implementation, I used the following methods.

### 1. Hand-Calculated Small Example

For the matrices:

A = [[1, 2],  
     [3, 4]]

B = [[5, 6],  
     [7, 8]]

the expected result is:

A × B = [[1×5 + 2×7, 1×6 + 2×8],  
         [3×5 + 4×7, 3×6 + 4×8]]

      = [[19, 22],  
         [43, 50]]

The program output matches this expected result, which confirms that the core multiplication logic is correct for a simple manually verifiable case.

### 2. Identity Matrix Test

A correct matrix multiplication implementation should satisfy:

A × I = A

where I is the identity matrix.

I tested the program using a 2×2 identity matrix, and the output remained unchanged. This confirms that the implementation satisfies a basic algebraic property of matrix multiplication.

### 3. Rectangular Matrix Test

I also tested the algorithm with non-square matrices:

- E: 2×3
- F: 3×2

This confirms that the implementation is not limited to square matrices and can handle valid rectangular matrix multiplication as long as the dimensions are compatible.

### 4. Dimension Checking

The program includes a dimension compatibility check. If the number of columns in the first matrix does not equal the number of rows in the second matrix, the program raises a `ValueError`.

This prevents invalid input from producing misleading results and improves the robustness of the implementation.

## C Language Implementation and Performance Analysis (bonus)

- **Source Code**: Include the C source code with comments explaining key sections.
- **Compilation Command**: Describe how to compile the program using GCC.
- **Execution Command**: Describe how to run the compiled program.
- **Execution Times**: Provide a table comparing the execution times of the C and Python implementations.
- **Analysis**: Discuss the performance differences observed and analyze the reasons behind them, considering factors like language execution models and memory management.
- **Important Note**: If you are aiming for the bonus, you must complete the work entirely on your own—specifically, AI can help you to learn and verify, but **NO AI DRAFTS**. Please note that the bonus rewards your **original thinking process** rather than just a "perfect" answer. If your submission appears suspiciously beyond a student's typical level, I may ask you to explain your logic face-to-face. You won't lose points for making honest mistakes, but if you cannot explain your work (indicating plagiarism or AI use), you will lose both the bonus and the points for the entire assignment. **Think carefully before you decide to go for it.**

This part was not included in my current submission.

I only completed the Python implementation and correctness verification in this assignment. Therefore, no C source code, performance comparison table, or detailed performance analysis is provided here.

## Conclusion

In this assignment, I practiced Unix/Linux command line operations, Markdown documentation, and Python-based remote development in a WSL2 environment.

The core programming task was to implement matrix multiplication using Python and verify its correctness through multiple test cases. During this process, I gained a clearer understanding of several important points:

- how to use Linux command line tools to inspect system information,
- how to organize a technical report using Markdown,
- how the standard matrix multiplication algorithm works,
- and how to verify program correctness using small examples and basic mathematical properties.

Although the algorithm itself is simple, this assignment showed that writing a complete technical report requires more than just code. Clear explanation, structured testing, and proper documentation are also important parts of software development.

## References

1. Python Software Foundation. *Python 3 Documentation*.
2. GNU Project. *GCC Documentation*.
3. Linux manual pages for `lscpu`, `free`, `uname`, and `gcc`.
4. Markdown Guide. *Basic Markdown Syntax*.

## Appendix

- **Additional Notes**:
  - The development environment used in this assignment is WSL2 rather than a native Linux installation, but the command line workflow is very similar to a standard Ubuntu environment.
  - The matrix multiplication algorithm used here is the classical triple-loop algorithm.
  - More advanced algorithms, such as block matrix multiplication and Strassen’s algorithm, exist, but they were not required for this assignment.
  - In this assignment, priority was given to correctness, clarity, and documentation instead of performance optimization.
