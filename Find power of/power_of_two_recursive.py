def power_two(n):
    # Base Case
    if n == 0:
        return False
    
    if n % 2 != 0:
        return False
    
    if n == 1:
        return True
    
    # Recursive case
    return power_two(n // 2)

(power_two(5))