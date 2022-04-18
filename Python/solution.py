T = int(input())
for _ in range(T):
    n, ar = int(input()), list(map(int, input().split(' ')))
    d = {}
    for x in ar:
        if x not in d:
            d[x] = 0
        d[x] += 1
    maxElem, k = -99999, 0
    for x in set(ar):
        if k < d[x]:
            maxElem = x
            k = d[x]
    # temp = []
    print(maxElem, k)
    start = 0
    res = 0
    # count = 0
    for x in ar:
        if k == 0:
            break
        if x == maxElem:
            start = 1
        if start:
            res += 1
            if x == maxElem:
                k -= 1
    print(res)
