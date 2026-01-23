def tribonaci(n):
    """Return the n-th Tribonacci number.

    The Tribonacci sequence is defined as follows:
    T(0) = 0, T(1) = 1, T(2) = 1
    T(n) = T(n-1) + T(n-2) + T(n-3) for n > 2

    Args:
        n (int): The index of the Tribonacci number to return.

    Returns:
        int: The n-th Tribonacci number.
    """
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c