n, r = int(input()), 0

def splitter(n, s):
    global r
    while n >= s:
        x = n%(s*10)
        if x!=0 and x % 11 == 0:
            r += 1
        n = n//10

t = n
c = 0
while t > 0:
    if t!=0 and (t % 10) % 11 == 0:
        r += 1
    c += 1
    t = t//10
i = 10
for _ in range(1, c):
    splitter(n, i)
    i *= 10
print(r)