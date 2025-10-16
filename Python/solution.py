from typing import List
import ast

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_ind = len(nums) -1
        res = last_ind + 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i] = nums[last_ind]
                nums[last_ind] = -1
                last_ind -= 1
                res -= 1
        return res

        

inp = ast.literal_eval(input())
res = Solution().removeElement(inp, int(input()))
print(inp)
print(res)