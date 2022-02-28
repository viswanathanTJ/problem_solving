import math
import itertools
from functools import reduce
import operator

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def count(m, num):
    k = 0
    cnt = 0
    for i in range(1, len(l)+1):
        s = 0
        for j in range(k, len(m)):
            if len(m[j]) == i:
                s += math.floor(num/prod(m[j]))
            else:
                k = j
                break
        cnt += ((-1)**(i+1))*s
    return cnt


def findNumber(s, n, l):
    lo = l[0]
    hi = n*l[0]
    m = []
    perm = []
    for i in range(1, len(l)+1):
        perm.append(list(itertools.combinations(l, i)))
    for i in range(len(perm)):
        for element in perm[i]:
            m.append(element)
    while lo < hi:
        x = lo+(hi-lo)//2
        cnt = count(m, x)
        if cnt >= n:
           hi = x
        elif cnt < n:
           lo = x+1
    return lo


for i in range(int(input())):
    s = input()
    l = []
    for p in prime:
        if s[p-1] == '1':
            l.append(p)
    n = int(input())
    x = findNumber(s, n, l)
    print(x)
