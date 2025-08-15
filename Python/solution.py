from typing import List

class Solution:
    def sortArrays(self, nums1, m, nums2, n):
        p1, p2, ins = m-1, n-1, m + n - 1
        while p1 > -1 and p2 > -1:
            if nums1[p1] > nums2[p2]:
                nums1[ins] = nums1[p1]
                p1 -= 1
            else:
                nums1[ins] = nums2[p2]
                p2 -= 1
            ins -= 1
        
        while p2 > -1:
            nums1[ins] = nums2[p2]
            p2 -= 1
            ins -= 1
        
                
        
    def sortArraysNoSpace(self, nums1, m, nums2, n):
        # no extra space
        left, right = m - 1, 0
        while left > -1 and right < n:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left -= 1
                right += 1
            else:
                break

        for i in range(m):
            for j in range(m):
                if nums1[i] < nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]

        nums2.sort()
        ind = 0
        for i in range(m, m+n):
            nums1[i] = nums2[ind]
            ind += 1
        
        
    def sortArraysNaive(self, nums1, m, nums2, n):
        res = [0] * (m+n)
        i, i1, i2 = 0, 0, 0
        while i1 < m and i2 < n:
            if nums1[i1] <= nums2[i2]:
                res[i] = nums1[i1]
                i1 += 1
            else:
                res[i] = nums2[i2]
                i2 += 1
            i += 1
        
        while i1 < m:
            res[i] = nums1[i1]
            i1 += 1
            i += 1
        while i2 < n:
            res[i] = nums2[i2]
            i2 += 1
            i += 1
        
        for i in range(m+n):
            nums1[i] = res[i]
            

import ast
 
nums1 = ast.literal_eval(input())
res = Solution().sortArrays(nums1, int(input()), ast.literal_eval(input()), int(input()))
print(nums1)