Write a function to calculate the multiplication of two matrices.

    Args:
        a: The first matrix.
        b: The second matrix.

    Returns:
        The multiplication of the two matrices.
    """
    return np.matmul(a, b)


def dot(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Write a function to calculate the dot product of two matrices.

    Args:
        a: The first matrix.
        b: The second matrix.

    Returns:
        The dot product of the two matrices.
    """
    return np.dot(a, b)
