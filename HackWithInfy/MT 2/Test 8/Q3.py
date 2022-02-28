# MT 8 Q3   
n = int(input())
coins = list(map(int, input().split()))
amount = int(input())
dp = [amount + 1] * (amount + 1)
dp[0] = 0
for i in range(1, amount + 1):
	for coin in coins:
		if i >= coin:
			dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[amount] if dp[amount] != amount + 1 else -1)
