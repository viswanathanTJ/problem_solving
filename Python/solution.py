from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_pointer = nums[0]
        fast_pointer = nums[0]
        
        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]
            if fast_pointer == slow_pointer:
                break

        fast_pointer = nums[0]
        
        while fast_pointer != slow_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]

        return fast_pointer
        
    def findDuplicateNoob(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)
        return -1
    

import ast
 
l = ast.literal_eval(input())
res = Solution().findDuplicate(l)
print(res)
l = ast.literal_eval(input())
res = Solution().findDuplicate(l)
print(res)
l = ast.literal_eval(input())
res = Solution().findDuplicate(l)
print(res)