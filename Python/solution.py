from typing import List

class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = (n * m) - 1
        while left <= right:
            mid = left + (right - left) // 2
            row_ind = mid // m
            col_ind = mid % m

            num = matrix[row_ind][col_ind]

            if num == target: return True

            if num > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return False


import ast
 
for _ in range(4):
    nums1 = ast.literal_eval(input())
    target = int(input())
    print(nums1, target)
    res = Solution().searchMatrix(nums1, target)
    print(res)