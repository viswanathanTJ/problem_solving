from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k = k % len(nums)

        def reverse(arr, l, r): 
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k-1) 
        reverse(nums, k, len(nums) - 1) 

                

        return nums
            


        pass
         
# for _ in range(3):
inp = ast.literal_eval(input())
inp1 = int(input())
res = Solution().rotate(inp, inp1)
print(res)
