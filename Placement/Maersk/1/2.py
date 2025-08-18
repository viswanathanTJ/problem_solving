n = int(input())
n1, n2 = 0, 0
if not n&1:
    for i in range(n//2):
        n1 = (n1*10)+9
    print(2*n1)
else:
    for i in range(n//2):
        n2 = (n2*10)+9
    print(n2+(n2*10+9))