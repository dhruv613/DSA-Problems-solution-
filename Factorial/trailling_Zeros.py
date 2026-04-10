def trailingZeroes(n):
    count = 0

    while n > 5:
        n = n // 5
        count += n
    return count


n = 10
print(trailingZeroes(n))