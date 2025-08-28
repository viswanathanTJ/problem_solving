from typing import List
import ast

class Solution:
    def rearrangeArray(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        pind, nind = 0, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                res[nind] = nums[i]
                nind += 2
            else:
                res[pind] = nums[i]
                pind += 2
        
        return res


res = Solution().rearrangeArray(ast.literal_eval(input()))
print(res)
