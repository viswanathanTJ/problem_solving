from typing import List
import ast
from collections import defaultdict, Counter

class Solution:

    def maxArea(self, height: List[int]) -> int:
        l, h = 0, len(height) - 1
        res = -1

        while l < h:
            low_height = min(height[h], height[l])
            length = low_height * abs(h - l)
            res = max(res, length)
            if height[h] >= height[l]:
                l += 1
            else:
                h -= 1

        return res

            
            
            
            
            
            


        pass
         
        
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().maxArea(inp)
print(res)
