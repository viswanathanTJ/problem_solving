def solve(s: str, n: int):
    c, v = s.count('c'), s.count('v')
    if c == 0 or v == 0:
        return 0
    i, j = 0, n
    while i < j:
        if c == v:
            return abs(i-j)
        elif c > v:
            if s[i] == 'c':
                i += 1
            else:
                j -= 1
            c -= 1
        else:
            if s[i] == 'v':
                i += 1
            else:
                j -= 1
            v -= 1

for _ in range(int(input())):
    n, s = int(input()), input()
    print(solve(s, n))