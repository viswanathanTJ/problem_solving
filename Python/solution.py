from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic
import math

class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ind = 0
        l, r = 0, n - 1
        while ind <= r:
            if nums[ind] == 2:
                nums[ind], nums[r] = nums[r], nums[ind]
                r -= 1
            elif nums[ind] == 0:
                nums[ind], nums[l] = nums[l], nums[ind]
                l += 1
                ind += 1
            else:
                ind += 1
        return nums
                
        
    
                
            
                

# for _ in range(3):
inp = ast.literal_eval(input())
# inp1 = int(input())
res = Solution().sortColors(inp)
# inp2 = int(input())
# res = Solution().pascalTriangleI(inp1, inp2)
print(res)
