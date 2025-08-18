from functools import reduce
from operator import mul


n, l = int(input()), list(map(int, input().split()))
r = 0
for i in range(n + 1): 
    for j in range(i + 1, n + 1): 
        sub = l[i:j]
        r = max(reduce(mul, sub, 1), r)

print(r)