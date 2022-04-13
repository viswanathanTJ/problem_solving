s = input()
while s:
    n, c = len(s), s[0]
    s = s.replace(c, '')
    if len(s) == n-1:
        print(c)
        break
else:
    print(0)
