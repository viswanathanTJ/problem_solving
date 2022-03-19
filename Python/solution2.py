def countsubarray(array, n, k):
    count = 0
    for i in range(0, n):
        if array[i] == k:
            print(array[i])

            count += 1
        mul = array[i]
        for j in range(i + 1, n):
            mul = mul * array[j]
            if mul == k:
                print(array[i], array[j])
                count += 1
            else:
                break
    return count

n, m = map(int, input().split())
k = n*m
l = list(map(int, input().split()))
size = len(l)
count = countsubarray(l, size, k)
print(count)
