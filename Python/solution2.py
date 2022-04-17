tasks = [2,2,3,3,2,4,4,4,4,4]
tasks = [2, 3, 3]
def minimum(tasks):
    d = {}
    for t in tasks:
        d[t] = d.get(t, 0)+1
    res = 0
    for k in d.keys():
        x = d.get(k)
        if x == 1: return -1
        if x == 2: res += 1
        if x == 3: res += 1
        if x >= 4:
            q = x // 3
            rem = x - 3 * q
            if not rem: res += q
            if rem == 1: res += (q-1+2)
            if rem == 2: res += (q+1)
    return res
print(minimum(tasks))