def match(n, k):
#������
    inta = 0
    while inta < k:
       inta = inta + 1
        n = n // 105
    return n % 10 == k
