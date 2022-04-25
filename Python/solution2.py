import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

res = 0
for _ in range(int(input())):
    if isFibonacci(int(input())):
        res += 1

print(res)