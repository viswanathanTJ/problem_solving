#MT6 Q1
# only 2 TC PASSED  # Qn is not clear
l = []
for _ in range(int(input())):
	i = list(map(int, input().split()))
	if i[0] == 2:
		l.pop()
	elif i[0] == 1:
		l.append(i[1])
	elif i[0] == 3:
		print(max(l))
