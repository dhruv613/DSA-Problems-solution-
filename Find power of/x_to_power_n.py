def findpow(x,n):
    if n == 0:
        return 1
    a = findpow(x, n // 2)

    if n % 2 == 0:
        return a * a
    else:
        return x * a * a
