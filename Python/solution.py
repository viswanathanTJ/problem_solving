from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic
import math

class Solution:

    def rearrangeArray(self, nums):
        # TC: O(n)
        # SC: O(n)
        pind, nind = 0, 1
        n = len(nums)
        res = [0] * n
        
        for i in range(n):
            if nums[i] < 0:
                if nind < n:
                    res[nind] = nums[i]
                    nind += 2
            else:
                if pind < n:
                    res[pind] = nums[i]
                    pind += 2
        
        return res
        
        
        pass
         
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().rearrangeArray(inp)
# inp1 = int(input())
# res = Solution().majorityElement(inp, inp1)
print(res)
