l = list(map(int, input().split()))
n = len(l)
i = 0
while i < n-2:
    if l[i] + l[i+1] == l[i+2]:
        l[i+2] = l[i+2] * 2
        del l[i]
        del l[i]
        n -= 2
        i -= 1
    else:
        i += 1
print(*l)