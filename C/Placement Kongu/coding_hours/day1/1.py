s = input()
r = 0
for x in set(s):
    if s.count(x) == 1:
        r += 1
print(r)
