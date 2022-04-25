import math

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

def fun(arr, n):
    count = 0
    for i in range(0, n):
        if (isFibonacci(arr[i]) == True):
            count = count + 1
    return count

n = int(input())
arr = []
for i in range(0, n):
    t = int(input())
    arr.append(t)
print(fun(arr, n))
