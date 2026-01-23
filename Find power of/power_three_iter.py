def power_three_iter(n):
    """Return True if n is a power of three, else False using an iterative approach."""
    if n == 0:
        return False
    
    while n % 3 == 0:
        n = n // 3
    
    return n == 1