#MT 6 Q2
n = int(input())-1
m = int(input())-1
x = int(input())-1
y = int(input())-1


def fact(x):
	if x <= 1:
		return 1
	return x * fact(x-1)


res = fact(n+m)
res = res//(fact(n))
res = res//(fact(m))

r1 = fact(x+y)
r1 = r1//(fact(x))
r1 = r1//(fact(y))

x1 = n-x
y1 = m-y

r2 = fact(x1+y1)
r2 = r2//(fact(x1))
r2 = r2//(fact(y1))
print(res-(r1*r2))
