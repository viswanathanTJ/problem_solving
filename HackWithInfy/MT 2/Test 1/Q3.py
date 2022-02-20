def LongestSubarray(a, n, k):
    pre = [0] * n
    for i in range(n):
        if (a[i] > k):
            pre[i] = 1
        else:
            pre[i] = -1
    for i in range(1, n):
        pre[i] = pre[i - 1] + pre[i]

    res, lo, hi = 0, 1, n
    while lo <= hi:
        mid = (lo + hi) // 2
        ok = False
        for i in range(mid - 1, n):
            x = pre[i]
            if (i - mid >= 0):
                x -= pre[i - mid]
            if (x > 0):
                ok = True
                break
        if (ok == True):
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res

n, k = map(int,input().split())
a = list(map(int,input().split()))
print(LongestSubarray(a, n, k))