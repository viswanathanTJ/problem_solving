class Solution:
    def get_path_count(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        # check if matrix obstacle at start
        if matrix[0][0]:
            return 0

        # create path count from that point
        matrix[0][0] = 1

        # check row path has no obstacle
        for i in range(1, row):
            if matrix[i][0] == 0:
                matrix[i][0] = matrix[i - 1][0]
            else:
                matrix[i][0] = 0

        # check col path has no obstacle
        for j in range(1, col):
            if matrix[0][j] == 0:
                matrix[0][j] = matrix[0][j - 1]
            else:
                matrix[0][j] = 0

        # add path count from that powint
        m = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][j] = matrix[i - 1][j] +\
                         matrix[i][j - 1]
                    if m<matrix[i][j]:
                        m = matrix[i][j]
                else:
                    matrix[i][j] = 0

        # return max(matrix[row - 1])
        return m


    def gen_grid(self, A, B):
        grid = [[0 for x in range(A)] for y in range(A)]

        midX = A//2
        midY = A//2

        B += 1
        if B == 1:
            grid[midX][midY] = 1
            for i in range(A):
                for j in range(A):
                    if i == midX and j == midY: 
                        grid[i][j] = 1
        else:
            for i in range(A):
                for j in range(A):
                    if i <= midX-B or i >= midX+B or j <=midY-B or j >= midY+B:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1

        return grid

    def solve(self, A, B):
        matrix = self.gen_grid(A, B)
        count = self.get_path_count(matrix)
        mod = int(1e9+7)
        # print(mod)
        if count > mod:
            return count%mod
        else:
            return count 

print(Solution().solve(3,0))
print(Solution().solve(25, 1))
print(Solution().solve(77, 26))
