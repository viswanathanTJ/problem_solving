from typing import List
import math
from icecream import ic
import sys
import os


class Solution:
    def two_sums(nums, target):
        value_ind = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in value_ind:
                return [i, value_ind[value]]
            value_ind[nums[i]] = i



## execution codes

solution = Solution()

with open('input.txt', 'r') as f:
    while True:
        l1 = f.readline().strip()
        if not l1: break
        l = list(map(int, l1.split(',')))
        t = int(f.readline().strip())
        res = Solution.two_sums(l, t)
        print(res)
