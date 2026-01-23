def power_three(n):
    # Base Case
    if n == 0:
        return False
    
    if n == 1:
        return True
    
    if n % 3 != 0:
        return False
    
    
    # Recursive case
    return power_three(n // 3)

print(power_three(9))