def dfsSoln(mat):
    r = len(mat)
    c = len(mat[0])
    visit = [[0]*c]*r
    cnt = 0
    for i in range(r):
        for j in range(c):
            if not visit[i][j] and mat[i][j] == 1:
                dfs(i, j, mat, visit)
                cnt += 1
    return cnt


def dfs(i, j, mat, visit):
    if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or visit[i][j] or mat[i][j] == 0:
        return
    visit[i][j] = True
    dfs(i + 1, j, mat, visit)
    dfs(i - 1, j, mat, visit)
    dfs(i, j + 1, mat, visit)
    dfs(i, j - 1, mat, visit)

    dfs(i + 1, j + 1, mat, visit)
    dfs(i - 1, j - 1, mat, visit)
    dfs(i + 1, j - 1, mat, visit)
    dfs(i - 1, j + 1, mat, visit)


r, c = int(input()), int(input())
mat = []
for _ in range(r):
    mat.append(list(map(int, input().split())))
print(dfsSoln(mat))
