import sys


def solve(n):
    col, pos_diag, neg_diag = set(), set(), set()
    board = [['.'] * n for _ in range(n)]
    res = []
    def backtrack(r):
        if r == n:
            copy = [''.join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                continue
            col.add(c)
            pos_diag.add(r+c)
            neg_diag.add(r-c)
            board[r][c] = 'Q'

            backtrack(r+1)

            col.remove(c)
            pos_diag.remove(r+c)
            neg_diag.remove(r-c)
            board[r][c] = '.'
    backtrack(0)
    for r in res:
        print_board(r)

def print_board(board):
    for y in board:
        for z in y:
            print(z, end=' ')
        print()
    print()

solve(5)