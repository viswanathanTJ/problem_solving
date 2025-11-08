from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic
import math

class Solution:

    def pascalTriangleI(self, r, c):
        n = r
        r = c

        if r < n - r:
            r = n - r
            
        res = 1
        for i in range(r):
            res *= (n - i)
            ic(n - i)
            res //= (i + 1)
        
        return res



        pass
         
# for _ in range(3):
# inp = ast.literal_eval(input())
# res = Solution().rearrangeArray(inp)
inp1 = int(input())
inp2 = int(input())
res = Solution().pascalTriangleI(inp1, inp2)
print(res)
