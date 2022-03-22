n = int(input())
b = [0]*32
ans = [0]*32
i = 0
while n > 0:
    b[i] = n % 2
    i += 1
    n = n//2
    
ans[0] = b[0] ^ 1
for j in range(1, i):
    ans[j] = b[j] ^ b[j-1]
mul, out = 1, 0
for e in ans:
    out = out + e*mul
    mul *= 2
print(out)