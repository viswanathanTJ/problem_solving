from typing import List
import ast
from collections import defaultdict, Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            h = n - 1
            num = nums[i]
            while l < h:
                s = num + nums[l] + nums[h]
                if s == 0:
                    triplet = [num, nums[l], nums[h]]
                    res.append(triplet)
                    while l < h and nums[l] == nums[l+1]:
                        l += 1
                    while l < h and nums[h] == nums[h-1]:
                        h -= 1
                    l += 1
                    h -= 1
                elif s > 0:
                    h -= 1
                else:
                    l += 1
                
        return res




        pass
         
        
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().threeSum(inp)
print(res)
