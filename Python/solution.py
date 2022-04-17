s = "11111222223"
k = 3
s, k = '1', 2

def solve(d):
    if len(d) == k:
        # print(d)
        return d
    if len(d) < k:
        return d
    t = ''
    i = 0
    while i < len(d)-k:
        t += str(sum(map(int, d[i:k+i])))
        i += k
    t += str(sum(map(int, d[i:])))
    return solve(t)

res = solve(s)
print(res)