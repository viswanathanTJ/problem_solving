from typing import List
import ast

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, profit = float('inf'), 0
        for p in prices:
            if p < low: 
                low = p
            else:
                profit = max(profit, p - low)
        return profit if profit > 0 else 0


res = Solution().maxProfit(ast.literal_eval(input()))
print(res)
