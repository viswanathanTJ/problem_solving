def solve(version1, version2):
    a = list(map(int, version1.split('.')))
    b = list(map(int, version2.split('.')))
    while len(a) > len(b):
        b.append(0)
    while len(b) > len(a):
        a.append(0)
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1
    return 0


def soln(version1, version2):
    v1, v2 = version1.split('.'), version2.split('.')
    m, n = len(v1), len(v2)
    i = j = 0
    while i < m or j < n:
        r1 = int(v1[i]) if i < m else 0
        r2 = int(v2[i]) if j < n else 0
        if r1 < r2: return -1
        elif (r1 > r2): return 1
        i += 1
        j += 1
    return 0

print(soln("1.0.1", "1"))
