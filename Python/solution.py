class Solution:
    def merge(self, intervals):
        n = len(intervals)
        res = []
        intervals.sort()
        
        for i in range(n):
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1] = [res[-1][0], max(intervals[i][1], res[-1][-1])]
        return res
            
        
    def merge1(self, intervals):
        res = []
        n = len(intervals)
        intervals.sort()

        for i in range(n):
            start, end = intervals[i]

            if res and res[-1][1] >= end:
                continue
            
            for j in range(i+1, n):
                if end >= intervals[j][0]:
                    end = max(end, intervals[j][1])
                else:
                    break
            
            res.append([start, end])
            
        return res

    

import ast
 
l = ast.literal_eval(input())
res = Solution().merge(l)
print(res)
l = ast.literal_eval(input())
res = Solution().merge(l)
print(res)
l = ast.literal_eval(input())
res = Solution().merge(l)
print(res)