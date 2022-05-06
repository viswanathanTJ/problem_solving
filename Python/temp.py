def maxArea(H, n):
    ans, i, j = 0, 0, n-1
    s, e = 0, 0
    while i < j:
        if H[i] <= H[j]:
            res = H[i] * (j - i)
            i += 1
        else:
            res = H[j] * (j - i)
            j -= 1
        if res > ans:
            s, e = i, j
            k = min(H[i-1], H[j])
    ans = 0
    for x in range(s, e):
        ans += k - H[x]
    return ans

n, l = int(input()), list(map(int, input().split()))
print(maxArea(l, n))