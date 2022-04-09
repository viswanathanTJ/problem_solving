ans = [0] * 1000000
dp = [-1]*1000000
def solve(num):
    if num<0: return 0
    if dp[num] != -1:
        return dp[num]
    else:
        ret = 0
        k = num
        while k != 0:
            v = k % 10
            if v != 0:
                ret += solve(num-v*v)
            k = k // 10
        if ret:
            dp[num] = 1
        else:
            dp[num] = 0
        return dp[num]


for i in range(10):
    n = 1
    for j in range(1, i+1):
        n*=i
    if n<=1000000:
        dp[n] = 1

for i in range(1000000):
    ty = solve(i)
    if ty >= 0:
        ans[i] = 1

for _ in range(int(input())):
    if dp[int(input())]:
        print('Yes')
    else:
        print('No')