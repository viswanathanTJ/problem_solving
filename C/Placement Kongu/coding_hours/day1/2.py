n, l = int(input()), list(map(int, input().split()))
mods = list(map(int, input().split()))
r = 0
for i in l:
    f = 1
    for x in mods:
        if x % i:
            f = 0
    if f:
        r += 1
print(r)