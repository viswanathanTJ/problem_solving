# MT 1 Q1
def maxdiff(l):
    i = 0
    j = len(l)-1
    l.sort()
    s = 0
    while i<j:
        s +=l[j]-l[i]
        i += 1
        j -= 1
    return s

l = []
for _ in range(int(input())):
    l.append(int(input()))
print(maxdiff(l))