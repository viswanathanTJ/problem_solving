# MT 10 Q3
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = (len(l)//2)-1
    c = l.count(1)
    if c >= m:
        print('YES')
    else:
        print('NO')
