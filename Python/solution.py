def gcd(x, y):
    while(y):
       x, y = y, x % y
    return x

n, l = int(input()), list(map(int, input().split()))
res = -1
for i in range(n-1):
    res = max(res, (l[i] * l[i+1]) // gcd(l[i], l[i+1]))
print(res)