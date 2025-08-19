from typing import List
import ast

class Solution:
    # n / 3 times
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1, el2, cnt1, cnt2 = float('-inf'), float('-inf'), 0, 0

        for n in nums:
            if cnt1 == 0 and n != el2:
                cnt1 = 1
                el1 = n
            elif cnt2 == 0 and n != el1:
                cnt2 = 1
                el2 = n
            elif n == el1:
                cnt1 += 1
            elif n == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            
        cnt1, cnt2 = 0, 0
        for n in nums:
            if el1 == n:
                cnt1 += 1
            elif el2 == n:
                cnt2 += 1
            
        limit = len(nums) // 3
        res = []
        if cnt1 > limit: res.append(el1)
        if cnt2 > limit: res.append(el2)

        return sorted(res)

    def majorityElementBetter(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        limit = len(nums) // 3
        for n in nums:
            if n not in d:
                d[n] = 1
            elif d[n] != -1:
                print('inc', n)
                d[n] = d[n] + 1

            if d[n] > limit:
                res.append(n)
                d[n] = -1
        
        return res


res = Solution().majorityElement(ast.literal_eval(input()))
print(res)
