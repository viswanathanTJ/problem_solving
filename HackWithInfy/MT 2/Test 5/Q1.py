# MT 5 Q1
n = input()
k = int(input())
n1 = len(n)
if len(n) <= k:
    print(0)
    quit()

a = ''
i = 0
while i < (n1-1) and k > 0:
    if int(n[i]) > int(n[i+1]):
        i += 1
        k -= 1
        continue

    else:
        a += n[i]
        i += 1

a += n[i]
i += 1
if k > 0:
    a = a[:-k]

if i <= (n1-1):
    while i < n1:
        a += n[i]
        i += 1

print(int(a) % ((10**9)+7))