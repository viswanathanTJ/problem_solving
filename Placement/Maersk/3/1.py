n = int(input())

i = 1
t = 1<<i

while t<n:
    t = 1<<i
    i += 1
    if t == n:
        print('Yes')
        print(sum(int(x) for x in str(n)))
        quit()
i-=1
print('No')
print(1<<i+i)