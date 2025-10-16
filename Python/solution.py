from typing import List
import ast
from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return [x[0] for x in sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True)[:k]]
        return [x[0] for x in Counter(nums).most_common(k)]

inp = ast.literal_eval(input())
res = Solution().topKFrequent(inp, int(input()))
print(res)