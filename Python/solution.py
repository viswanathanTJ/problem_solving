from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic
import math

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            for j in range(i, len(nums) + 1):
                csum = 0
                for k in range(i, j):
                    csum += nums[k]
                    print(nums[k], end=',')
                res = max(csum, res)
                print(csum)
                
        return res

                
            
                

# for _ in range(3):
inp = ast.literal_eval(input())
# inp1 = int(input())
res = Solution().maxSubArray(inp)
# inp2 = int(input())
# res = Solution().pascalTriangleI(inp1, inp2)
print(res)
