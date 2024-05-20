# Import necessary modules
from mojo import tensor

# Define a function to perform matrix multiplication using def
def matrix_multiply(A: tensor[float], B: tensor[float]) -> tensor[float]:
    # Get the dimensions of the matrices
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to the number of rows in B.")

    # Initialize the result matrix with zeros
    C = tensor[float](shape=(rows_A, cols_B), fill=0.0)

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i, j] += A[i, k] * B[k, j]
    
    return C

# Example usage
def main():
    # Define two matrices A and B
    A = tensor[float]([[1.0, 2.0], [3.0, 4.0]])
    B = tensor[float]([[5.0, 6.0], [7.0, 8.0]])

    # Perform matrix multiplication
    C = matrix_multiply(A, B)

    # Print the result
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Matrix C (A * B):")
    print(C)

# Call the main function
main()
