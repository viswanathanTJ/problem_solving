from typing import List
import ast
from collections import defaultdict, Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        triplets = set()
        
        num_ind = {}

        for i in range(n):
            num_ind[nums[i]] = i

        for i in range(n):
            for j in range(i, n):
                num = nums[i]
                third_num = nums[j] + nums[i]
                third_num *= -1
                if third_num in num_ind:
                    k = num_ind[third_num]
                    if (i != j and i != k and j != k):
                        triplet = tuple(sorted([num, third_num, nums[j]]))
                        if triplet not in triplets:
                            triplets.add(triplet)
        
        return [list(x) for x in triplets] 





        pass
         
        
# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().threeSum(inp)
print(res)
