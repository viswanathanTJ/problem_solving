from typing import List
import ast
from collections import defaultdict, Counter

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        grid = [[0] * 9 for _ in range(9)]
        
        for i in range(n):
            for j in range(n):
                num = board[i][j]

                if num != '.':
                    ind = ord(num) - ord('1')
                    grid_ind = (i//3) * 3 + (j // 3)

                    if rows[i][ind] or cols[j][ind] or grid[grid_ind][ind]:
                        return False

                    rows[i][ind] = 1
                    cols[j][ind] = 1
                    grid[grid_ind][ind] = 1
                
        return True

# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().isValidSudoku(inp)
print(res)
