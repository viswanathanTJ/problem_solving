#MT 10 Q2
N = int(input())
x = list(map(int, input().split()))
sumx = sum(x)
Q = int(input())
mod = 1000000007
y = list(map(int, input().split()))
for i in range(Q):
    sumx += sumx
    print(sumx % mod)
