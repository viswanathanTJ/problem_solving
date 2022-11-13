for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))
    res = 0
    m = 0
    if n == 2:
        print(l[0]+l[1]+1)
        continue
    s = sorted(l, reverse=True)
    for i in range(n):
        if l[i] > m:
            for j in range(i+1, n):
                ans = l[i] + l[j] + j - i
                res = max(ans, res)
            m = l[i]
    print(res)

    