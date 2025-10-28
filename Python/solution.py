from typing import List
import ast
from collections import defaultdict, Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=',')
            print()

        def is_valid_num(num, i, j):
            # check row
            for x in range(n):
                if x != j and board[i][x] == num:
                    return False

            # check col
            for x in range(n):
                if x != i and board[x][j] == num:
                    return False

            # check box
            row_start = (i // 3) * 3
            col_start = (j // 3) * 3
            for r in range(row_start, row_start + 3):
                for c in range(col_start, col_start + 3):
                    if (r, c) != (i, j) and num == board[r][c]:
                        return False

            return True 

        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num != '.':
                    is_valid = is_valid_num(num, i, j)
                    if not is_valid:
                        return False

        return True

inp = ast.literal_eval(input())
res = Solution().isValidSudoku(inp)
print(res)