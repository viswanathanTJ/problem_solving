from typing import List
import ast

class Solution:
    # n / 2 times
    def majorityElement(self, nums: List[int]) -> List[int]:
        el, cnt = 0, 0

        for n in nums:
            if not cnt:
                el = n
                cnt = 1
            elif el == n:
                cnt += 1
            else:
                cnt -= 1
            
        return el

res = Solution().majorityElement(ast.literal_eval(input()))
print(res)
