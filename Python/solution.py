from itertools import combinations_with_replacement


def printCombination(arr, n, r):
    data = [0]*r
    combinationUtil(arr, data, 0, n - 1, 0, r)

def combinationUtil(arr, data, start, end, index, r):
    if (index == r):
        print(*data[:r])
        return
    i = start 
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1, end, index + 1, r)
        i += 1

arr = ['a','e','i','o','u']
r = 2
n = len(arr)
printCombination(arr, n, r)
# print(*combinations_with_replacement(arr, 2))
