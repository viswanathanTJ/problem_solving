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


print(solve("1.0.1", "1"))
