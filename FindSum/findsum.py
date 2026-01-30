def findSum(n):
    if n == 0:
        return 0

    return n + findSum(n - 1)


print(findSum(4))