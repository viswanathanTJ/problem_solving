def solve(arr, n, k):
	x = n // k
	freq = {}
	for i in range(n):
		if arr[i] in freq:
			freq[arr[i]] += 1
		else:
			freq[arr[i]] = 1
	for i in freq:
		if (freq[i] > x):
			print(i)

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    solve(arr, n, k)
