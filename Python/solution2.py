def func(n, k):
    res = (n * (n+1)) // 2
    kpow = k
    while kpow <= n:
        t = n // kpow
        res = res - (k - 1) * (t * (t + 1)) // 2
        kpow *= k
    return res


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(func(n, k))