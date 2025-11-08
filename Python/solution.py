from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic
import math

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        print(nums)

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            h = len(nums) - 1
            while l < h:
                addition = nums[i] + nums[l] + nums[h]
                if addition > 0:
                    h -= 1
                elif addition < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[h]])
                    while l < h and nums[l] == nums[l + 1]:
                        l += 1
                    while l < h and nums[h] == nums[h - 1]:
                        h += 1
                    l += 1
                    h -= 1

        return res


# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().threeSum(inp)
# inp1 = int(input())
# inp2 = int(input())
# res = Solution().pascalTriangleI(inp1, inp2)
print(res)
