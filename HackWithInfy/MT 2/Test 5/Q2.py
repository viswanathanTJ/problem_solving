# MT 5 Q2
n = int(input())
m, res = 0, 0
x = int(input())
l = list(map(int, input().split()))

for i in range(n):
    l[i] = (l[i]-1)//x

for i in range(n):
    if l[i] >= m:
        m = l[i]
        res = i

print(res+1)
