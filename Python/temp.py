n = 7
a = 0

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print()

def fill_x(matrix, a):
    center = len(matrix) // 2
    print(center)
    for x in range(a+1):
        print('x', x)
        matrix[center-x][center] = 1 # top
        matrix[center+x][center] = 1 # bottom
        matrix[center][center-x] = 1 # left
        matrix[center][center+x] = 1 # right
        matrix[center-x][center-x] = 1 # top left
        matrix[center+x][center-x] = 1 # top right
        matrix[center-x][center+x] = 1 # bottom left
        matrix[center+x][center+x] = 1 # bottom right
        matrix[center][center] = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                # matrix down and right as 1
                if i < len(matrix)-1:
                    matrix[i+1][j] = 1
                if j < len(matrix[0])-1:
                    matrix[i][j+1] = 1
    return matrix

matrix = [[0 for x in range(n)] for y in range(n)]
nm = fill_x(matrix, 2)
print_matrix(nm)