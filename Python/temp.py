n = 4
res = 999
l = [3, 2, 4, 1, 9]
fres = 0
for i in range(2, 9):
    # print(n&(n^i), end=' ')
    x = i
    for e in l:
        res = min(res, e&(e^i))
    nl = l[:]
    nl[0] = res
    t = nl[0]
    print(nl)
    for j in range(1, len(nl)):
        t = t ^ nl[j]
    fres = max(fres, t)
print(fres)
