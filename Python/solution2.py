arr = [1, 2, 2, 1, 2]
# arr = [1,2,2,2,3,4,2,1]
s = set(arr)
n = len(arr) - 1
d = {}

print(s)
for i in s:
    d[i] = 0
    for j in range(n):
        if arr[j] != arr[j+1] and arr[j] == i:
            print(arr[j], j)
            d[i] += 1
if arr[n] != arr[n-1]:
    if arr[n] in d:
        d[arr[n]] = d[arr[n]] + 1
    else:
        d[arr[n]] = 1
if arr[n-1] != arr[n-2]:
    if arr[n-1] in d:
        d[arr[n-1]] = d[arr[n-1]] + 1
    else:
        d[arr[n-1]] = 1
print(d)
print(max(d.items(), key=lambda x: x[1])[0])
