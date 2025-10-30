from typing import List
import ast
from collections import defaultdict, Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        print(len(s))
        res = 0
        for n in s:
            if n - 1 not in s:
                length = 1
                n += 1
                while n in s:
                    length += 1
                    n += 1
                res = max(res, length)
        
        return res
         
        
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().longestConsecutive(inp)
print(res)
