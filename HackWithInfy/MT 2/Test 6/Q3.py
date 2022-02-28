#MT6 Q3
n = int(input())
l = []
for i in range(n):
 l.append(int(input()))

dp = [0]*201
dp[1] = 10
dp[2] = 55
a = [1]*10

i = 3
while i < 201:
 s = 0
 for x in range(10):
   s += a[x]
   a[x] = s
   dp[i] += (s*(10-x))
   dp[i] = dp[i] % ((10**9)+7)

 i += 1

s1 = 0
for i in l:
 s1 += dp[i]
 s1 = s1 % ((10**9)+7)

print(s1)
