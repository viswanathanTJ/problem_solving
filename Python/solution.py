s = input()
r = s[::-1]
res = 0
for i in range(len(s)):
    if s[i] == r[i]:
        res += 1
print(res)

# Number
s = input().split()
fi, se, th, fo = float('inf'), float('-inf'), float('inf'), float('-inf')
for i in s:
    fi = min(fi, int(i[0]))
    se = max(se, int(i[1]))
    th = min(th, int(i[2]))
    fo = max(fo, int(i[3]))
print(f'{fi}{se}{th}{fo}')