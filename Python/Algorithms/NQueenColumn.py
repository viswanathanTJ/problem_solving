n = 8
board = [['.']*n for _ in range(n)]


def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True


def solve(board, col, n):
    if col >= n:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'
            if solve(board, col+1, n):
                return True
            board[i][col] = '.'
    return False


solve(board, 0, n)
for i in board:
    print(*i)
