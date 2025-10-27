from typing import List
import ast
from collections import defaultdict, Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = []
        suf = [0] * n

        for i in range(n):
            if not pre:
                pre.append(nums[i])
                suf[-1] = nums[n - 1 - i]
            else:
                pre.append(pre[-1] * nums[i])
                suf[n - 1 - i] = suf[n - i] * nums[n - 1 - i]
            
        out = [0] * n
        out[0] = suf[1]
        for i in range(1, n - 1):
            out[i] = pre[i - 1] * suf[i + 1]
        out[-1] = pre[n - 2]
        return out

inp = ast.literal_eval(input())
res = Solution().productExceptSelf(inp)
print(res)