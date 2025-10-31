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
        for i in range(n):
            cur_left = max(height[i], cur_left)
            max_left[i] = cur_left
        
        print(max_left)

                    
        return res
            
            
            
            
            


        pass
         
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().trap(inp)
print(res)
