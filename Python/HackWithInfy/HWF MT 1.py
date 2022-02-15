# 1
# Count number L, R
def memo(index, evenSum, oddSum, tight):
    if index == len(v):
        if evenSum > oddSum:
            return 1
        else:
            return 0

    if dp[index][evenSum][oddSum][tight] != -1:
        return dp[index][evenSum][oddSum][tight]
    limit = v[index] if tight else 9
    ans = 0
    for d in range(limit + 1):
        currTight = 0
        if d == v[index]:
            currTight = tight
        if d % 2 != 0:
            ans += memo(index + 1, evenSum,
                        oddSum + d, currTight)
        else:
            ans += memo(index + 1, evenSum + d,
                        oddSum, currTight)

    dp[index][evenSum][oddSum][tight] = ans
    return ans

def countNum(n):
	global dp, v
	v.clear()
	while n:
		v.append(n % 10)
		n //= 10
	v.reverse()
	dp = [[[[-1, -1] for i in range(180)] for j in range(180)]
            for k in range(18)]
	return memo(0, 0, 0, 1)

if __name__ == "__main__":
	dp, v = [], []
	L, R = int(input()), int(input())
	print(countNum(R) - countNum(L - 1))


# 2
# Charlie wants to divide
def solve(X, Y, m, n):
  r, h, v, i, j = 0, 1, 1, 0, 0
  while (i < m and j < n):
    if (X[i] > Y[j]):
      r += X[i] * v
      h += 1
      i += 1
    else:
      r += Y[j] * h
      v += 1
      j += 1

  t = 0
  while (i < m):
    t += X[i]
    i += 1
  r += t * v

  t = 0
  while (j < n):
    t += Y[j]
    j += 1
  r += t * h
  return r


m, n = map(int, input().split())
X = sorted(map(int, input().split()), reverse=True)
Y = sorted(map(int, input().split()), reverse=True)
print(solve(X, Y, m-1, n-1))
# 1 tc failed

# 3
for _ in range(int(input())):
    n = int(input())
    items = list(map(int, input().split()))
    i = 0
    m = 0
    iT = items[0]
    while i < n:
        c = 1
        j = i+1
        while j < n:
            if items[i] == items[j] and j != i+1:
                c += 1
                if j < n-1 and items[j] == items[j+1]:
                    j += 1
            j += 1
        if m < c:
            m = c
            iT = items[i]
        i += 1
    print(iT)