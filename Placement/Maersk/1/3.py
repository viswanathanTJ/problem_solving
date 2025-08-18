def solve(l, m):
    n = len(l)
    s = 0
    j = n - 1
    for i in range(m, -1, -1):
        s += l[i]*j
        j -= 1
    j = 0
    for i in range(m+1, n):
        s += l[i] * j
        j += 1
    return s
    
    
n, l = int(input()), list(map(int, input().split()))
m = 0
for i in range(n):
    m = max(m, solve(l, i))
    
print(m)