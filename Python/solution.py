from typing import List
import ast

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, s = float('-inf'), 0
        for n in nums:
            s += n
            res = max(s, res)
            if s < 0: s = 0
        return res

res = Solution().maxSubArray(ast.literal_eval(input()))
print(res)
