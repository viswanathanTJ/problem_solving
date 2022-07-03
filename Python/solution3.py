def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print()

def solve(A, B):
    grid = [[0 for x in range(A)] for y in range(A)]

    midX = A//2
    midY = A//2

    # creating matrix
    B += 1
    if B == 1:
        grid[midX][midY] = 1
        for i in range(A):
            for j in range(A):
                if i == midX and j == midY: grid[i][j] = 1
    else:
        for i in range(A):
            for j in range(A):
                if i <= midX-B or i >= midX+B or j <=midY-B or j >= midY+B:
                    grid[i][j] = 0
                else:
                    grid[i][j] = 1

    print_matrix(grid)

solve(5, 1)