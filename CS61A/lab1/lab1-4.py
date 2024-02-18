def falling(n, k):
    a = 1
    while k:
        a = a * n
        n = n - 1
        k = k - 1
    return a

