from typing import List
import ast
from collections import defaultdict, Counter

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_ind = {}
        for i in range(len(numbers)):
            num_ind[numbers[i]] = i + 1
        
        for i in range(len(numbers)):
            if target - numbers[i] in num_ind:
                return [i+1, num_ind[target - numbers[i]]]
            
        
# for _ in range(3):
inp = ast.literal_eval(input())
target = int(input())
res = Solution().twoSum(inp, target)
print(res)
