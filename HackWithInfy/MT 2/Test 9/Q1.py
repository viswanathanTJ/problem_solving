# MT 9 Q1
n = int(input())
l2 = list(map(int, input().split()))
l1 = list(map(int, input().split()))

for i in range(n):
    l2[i] = l2[i]-l1[i]
l2.sort()
s, res = 0, 0
for i in range(n-1, -1, -1):
	s = s + l2[i]
	if s < 0:
		s = -s
		res = res + s
		s = 0

print(res)
