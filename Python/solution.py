s = []

for _ in range(int(input())):
    l = list(map(int, input().split()))
    q = l[0]
    if q == 1:
        s.append(l[1])
    elif q == 2:
        k, ind = l[1], l[2]
        t = []
        for x in s:
            t.append(x ^ k)
        print(sorted(t)[ind-1])
