class NQueenRow:
    def __init__(self, n):
        self.board = [[0]*n]*n
        # self.solve(n, 0)

    def isSafe(self, n, r, c) -> bool:
        for i in range(r):
            if self.board[i][c] == 1:
                print('1for',i,c)
                return False

        for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
            if self.board[i][j] == 1:
                print('2for',i,j)
                return False
            
        for i, j in zip(range(r, -1, -1), range(c, n)):
            if self.board[i][j] == 1:
                print('3for',i,j)
                return False

        return True

    def solve(self, n, r) -> bool:
        if r >= n:
            return True
        for i in range(n):
            if self.isSafe(n, r, i) == True:
                self.board[r][i] = 1
                if self.solve(n, r+1) == False:
                    print('rn')
                    return True
                else:
                    self.board[r][i] = 0
        return False

    def __repr__(self):
        for l in self.board:
            for e in l:
                print(e, end=' ')
            print()
        return ''

n = int(input())
obj = NQueenRow(n)
print(obj)
obj.solve(n, 0)
print(obj)



