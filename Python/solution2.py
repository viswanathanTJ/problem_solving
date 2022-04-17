for _ in range(int(input())):
    n, l = int(input()), list(map(int, input().split()))

    d = {}
    max_pos = float('-inf')
    for e in l:
        d[e] = d.get(e, 0) + 1

    max_elem, k = float('-inf'), 0
    for x in set(l):
        if k < d[x]:
            max_elem = x
            k = d[x]
    start, res = 0, 0
    for x in l:
        if not k: break
        if x == max_elem: start = 1
        if start: 
            res += 1
            if x == max_elem:
                k -= 1
    print(res)

    #     max_pos = max(max_pos, d[e])
    # res = float('inf')
    # for i in range(n+1):
    #     for j in range(i+1, n+1):
    #         t = {}
    #         tmax = float('-inf')
    #         cl = len(l[i:j])
    #         if cl<res:
    #             for e in l[i:j]:
    #                 t[e] = t.get(e, 0) + 1
    #                 tmax = max(tmax, t[e])

    #             if tmax == max_pos:
    #                 res = min(res, cl)
    # print(res)
