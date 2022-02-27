# MT 5 Q3
s = input()
l = []
for i in s:
    if i.isalpha():
        l.append(i)
l = l[::-1]
r = []
for i in s:
    if i.isalpha():
        r.append(l.pop(0))
    else:
        r.append(i)
print(r)
