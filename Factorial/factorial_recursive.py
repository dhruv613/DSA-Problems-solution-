def fac(n):
    """Compute the factorial of a non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.
    
    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * fac(n - 1)

    