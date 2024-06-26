from typing import List
import math
from icecream import ic
import sys
import os

class Solution:
    def group_anagrams(strs):
        from collections import defaultdict
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        mod = 10000000009
        m = defaultdict(list)
        key = 0
        for s in strs:
            key = 1
            for c in s:
                key *= primes[ord(c)-97] + mod
            m[key].append(s)
        return list(m.values())

    def matrix_solver(matrix):
        n = len(matrix)
        n1 = len(matrix[0])
        row = [0] * n
        col = [0] * n1
        for i in range(0, n):
            for j in range(0, n1):
                if not matrix[i][j]:
                    row[i] = 1
                    col[j] = 1

        for i in range(0, n):
            for j in range(0, n1):
                if row[i] or col[j]:
                    matrix[i][j] = 1
                
                
## execution codes

with open('input.txt', 'r') as f:
    while True:
        l1 = f.readline().strip()
        if not l1: break
        strs = eval(l1)
        res = Solution.matrix_solver(strs)
        print(res)
