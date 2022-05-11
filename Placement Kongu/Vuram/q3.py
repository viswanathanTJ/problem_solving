input()
s = set()
for i in input().split():
    t = 1
    for x in i:
        t *= int(x)
    s.add(t)
print(len(s))
