from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic
import math

class Solution:

    def majorityElement(self, nums):
        d = defaultdict(int)

        for n in nums:
            d[n] = d[n] + 1

        sorted_d = sorted(d.items(), key = lambda x : x[1], reverse=True)
        
        return sorted_d.pop(0)[0]
        

        pass

    def majorityElementOptimal(self, nums):
        cnt = 0
        el = None

        for n in nums:
            if not el or not cnt:
                el = n
                cnt = 1
            elif el == n:
                cnt += 1
            else:
                cnt -= 1

        return el



        pass
         
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().majorityElement(inp)
# inp1 = int(input())
# res = Solution().majorityElement(inp, inp1)
print(res)
