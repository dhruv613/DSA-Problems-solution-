def Sum_of_digits(n):
    """
    This function takes an integer n and returns the sum of its digits.
    """
    return sum(int(digit) for digit in str(abs(n)))


def Sum_of_digits_iter(n):
    """
    This function takes an integer n and returns the sum of its digits using iteration.
    """
    if n == 0:
        return 0

    for i in range(len(str(n))):
        return n % 10 + Sum_of_digits_iter(n // 10)

print(Sum_of_digits(1234))
print(Sum_of_digits_iter(1234))


def Sum_of_digits_recursive_2(n):
    """
    The function takes an integer n and returns the sum of its digits using recursion.
    """
    if n == 0:
        return 0
    return n % 10 + Sum_of_digits_recursive_2(n // 10)
    

def Sum_of_digits_whileloop(n):
    """
    The function takes an integer n and returns the sum of its digits using a while loop.
    """
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total