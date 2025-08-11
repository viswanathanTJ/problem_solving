n, l = int(input()), list(map(int, input().split()))

m = 1000
ind = 0
for i in range(n):
    if m > l[i]:
        m = l[i]
        ind = i
f = 1

for i in range(ind, n-1):
    if l[i] > l[i+1]:
        f = 0
        
for i in range(ind-1):
    if l[i] > l[i+1]:
        f = 0
        
if l[n-1] > l[0]:
    f = 0
    
if f:
    print('True')
    print(ind)
else:
    print('False')
    print(ind)