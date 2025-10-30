from typing import List
import ast
from collections import defaultdict, Counter

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left + 1, right + 1]
            if res > target:
                right -= 1
            else:
                left += 1
                
        
# for _ in range(3):
inp = ast.literal_eval(input())
target = int(input())
res = Solution().twoSum(inp, target)
print(res)
