from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic

class Solution:

    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        
        l = 0
        r = n - 1
        
        max_left = -1
        max_right = -1

        while l <= r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                ic(max_left)
                res += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                res += max_right - height[r]
                r -= 1

        return res
            
            
            


        pass
         
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().trap(inp)
print(res)
