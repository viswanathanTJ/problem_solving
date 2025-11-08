from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic
import math

class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pind, nind = 0, 1

        for i in range(len(nums)):
            if nums[i] < 0: # neg
                if i != nind:
                    nums[i], nums[nind] = nums[nind], nums[i]
                nind += 2
            else: # pos
                if i != pind:
                    nums[i], nums[pind] = nums[pind], nums[i]
                pind += 2

        return nums



        pass

    def rearrangeArrayBetter(self, nums: List[int]) -> List[int]:
        # O(n)
        res = []

        pos = []
        neg = []

        for n in nums:
            if n > -1:
                pos.append(n)
            else:
                neg.append(n)
        
        for p, n in zip(pos, neg):
            res.append(p)
            res.append(n)

        return res




        pass
         
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().rearrangeArray(inp)
# inp1 = int(input())
# res = Solution().majorityElement(inp, inp1)
print(res)
