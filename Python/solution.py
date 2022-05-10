from itertools import combinations, permutations
# for c in combinations([i for i in range(1, 10)], k):
#     print(c)
print(*permutations([1,2,3,4,5], 3))
# print(*combinations([1,2,3,4,5], 3))

def permute(arr, n, index):
    for i in range(index, n):
        arr[i], arr[index] = arr[index], arr[i]
        permute(arr, n, index + 1)
        arr[index], arr[i] = arr[i], arr[index]
    if index == n - 1:
        print(arr[:n], end=' ')

permute([1,2,3,4,5], 3, 0)