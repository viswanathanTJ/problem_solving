from typing import List
import ast
from collections import defaultdict, Counter
from icecream import ic
import math

class Solution:
    def printMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=" ")
            print()

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        self.printMatrix(matrix)
            
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

        self.printMatrix(matrix)

    def rotateBrute(self, matrix: List[List[int]]) -> None:
        self.printMatrix(matrix)
        mat = [[matrix[len(matrix) - 1 - j][i] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        matrix = mat
        self.printMatrix(matrix)
        return matrix


# for _ in range(3):
inp = ast.literal_eval(input())
res = Solution().rotate(inp)
# inp1 = int(input())
# inp2 = int(input())
# res = Solution().pascalTriangleI(inp1, inp2)
print(res)
