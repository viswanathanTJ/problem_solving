from typing import List
import ast

class Solution:
    def uniquePaths(self, m, n):
        res = 0
        paths = []

        def processIndex(i, j, is_row = False):
            # i = 6, j = 0
            # move to right
            s = 0
            if is_row:
                for col in range(i, n):
                    s += processIndex(col, 0)
            else:
                for row in range(j, m):
                    s += processIndex(row, 0, True)
            return s

        return processIndex(0, 0)


# res = Solution().uniquePaths(int(input()), int(input()))
# print(res)

def merge(arr, low, mid, high):
    left_ptr = low
    right_ptr = mid + 1
    res = [0] * (high - low + 1)
    ans = []
    k = 0
    while left_ptr <= mid and right_ptr <= high:
        if arr[left_ptr] >= arr[right_ptr]:
            res[k] = arr[right_ptr]
            ans.append(arr[right_ptr])
            k += 1
            right_ptr += 1
        else:
            res[k] = arr[left_ptr]
            ans.append(arr[left_ptr])
            k += 1
            left_ptr += 1

    while left_ptr <= mid:
        res[k] = arr[left_ptr]
        ans.append(arr[left_ptr])
        left_ptr += 1
        k += 1

    while right_ptr <= high:
        res[k] = arr[right_ptr]
        ans.append(arr[right_ptr])
        right_ptr += 1
        k += 1
    
    for i in range(low, high + 1):
        arr[i] = ans.pop(0)


def merge_sort(arr, low, high):
    # base case
    if low == high: return

    mid = (high + low) // 2

    # dividing
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)

    # solving
    merge(arr, low, mid, high)

'''
2 3 5 11 23 4 5 12

12
2
3
4
11
23 => 12 and 23 swapp
12
4 => 12 and 4 swap
5 => 12 and 5 swap
'''
def get_partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for k in range(low, high):
        if arr[k] < pivot:
            i += 1
            arr[k], arr[i] = arr[i], arr[k]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pIndex = get_partition(arr, low, high)
        quick_sort(arr, low, pIndex - 1)
        quick_sort(arr, pIndex + 1, high)


a = [3,4,2,1,9,5,6,22,20]
print(len(a))
quick_sort(a, 0, len(a) - 1)
print(a)
