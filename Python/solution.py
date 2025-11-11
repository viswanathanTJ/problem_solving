from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic
import math

class Solution:
    
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        
        for i in range(len(nums) - 3):
            if (i != 0 and nums[i] == nums[i-1]) or (nums[i]+nums[-1]+nums[-2]+nums[-3] < target):
                continue

            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target:
                break

            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                h = len(nums) - 1
                
                while k < h:
                    value = nums[i] + nums[j] + nums[k] + nums[h]
                    if value == target:
                        res.append([nums[i], nums[j], nums[k], nums[h]])
                        h -= 1
                        k += 1
                        while k < h and nums[k] == nums[k - 1]:
                            k += 1
                        while k < h and nums[h] == nums[h + 1]:
                            h -= 1
                    elif value > target:
                        h -= 1
                    else:
                        k += 1
                        
        return res
                
            
                

# for _ in range(3):
inp = ast.literal_eval(input())
inp1 = int(input())
res = Solution().fourSum(inp, inp1)
# inp2 = int(input())
# res = Solution().pascalTriangleI(inp1, inp2)
print(res)
