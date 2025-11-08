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
         
    def pascalTriangleII(self, r):
        res = [1]
        for i in range(1, r):
            res.append((res[-1]*(r - i)) // (i))
        return res

    def pascalTriangleIIBetter(self, r):
        n = r - 1
        def nCr(n, r):
            res = 1
            for i in range(r):
                res *= (n - i)
                res //= (i + 1)
            return res

        half = n // 2
        half += 1

        res = [nCr(n, i) for i in range(half)]
        res.extend(res[::-1] if n % 2 else res[:-1][::-1])
        
        return res
    
    def pascalTriangleIII(self, n):
        res = [[1]]
        for i in range(1, n + 1):
            row = [1]
            for j in range(1, i):
                row.append(res[-1][j] + res[-1][j-1])
            row.append(1)
            res.append(row)
        return res

# for _ in range(3):
# inp = ast.literal_eval(input())
# res = Solution().rearrangeArray(inp)
inp1 = int(input())
# inp2 = int(input())
# res = Solution().pascalTriangleI(inp1, inp2)
res = Solution().pascalTriangleIII(inp1)
print(res)
