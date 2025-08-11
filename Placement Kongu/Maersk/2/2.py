n = int(input())
d = {}
l = list(map(int, input().split()))
for v in l:
    if v in d:
        d[v] = d[v] + 1
    else:
        d[v] = 1
c = int(input())
f = 1
for key in d.keys():
    if d[key] == c:
        print(key, end=' ')
        f = 0
if f:
    print(-1)