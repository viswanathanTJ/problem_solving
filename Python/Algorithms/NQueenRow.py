def printer(board):
    for row in board:
        print(*row)

def is_safe(row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    return True


def solve(row):
    if row >= n:
        return True
    for i in range(n):
        if is_safe(row, i):
            board[row][i] = 'Q'
            if solve(row+1):
                return True
            board[row][i] = '.'
    return False

n = 8
board = [['.']*n for _ in range(n)]
solve(0)
printer(board)