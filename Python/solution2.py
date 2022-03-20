n, q = map(int, input().split())
a = list(map(int, input().split()))
while(not q-1):
    q -= 1
    l, r, x = map(int, input().split())
    for i in range(l-1, r):
        l[i] &= x
print(*l)