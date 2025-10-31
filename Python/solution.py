from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic

class Solution:

    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        
        max_left = [0] * n
        max_right = [0] * n
        
        cur_left = height[0]
        cur_right = height[-1]
        for i in range(n):
            cur_left = max(height[i], cur_left)
            cur_right = max(height[n - 1 - i], cur_right)
            max_left[i] = cur_left
            max_right[n - 1] = cur_right
        
        ic(max_left)
        ic(max_right)

        for i in range(n):
            res += min(max_right[i], max_left[i]) * height[i]
                    
        return res
            
            
            
            
            


        pass
         
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().trap(inp)
print(res)
