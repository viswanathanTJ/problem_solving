n = 7
adj = [[0]*n for _ in range(n)]
while 1:
    s, e, w = map(int, input().split())
    if s == -1:
        break
    adj[s][e] = w


def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    for i in range(n):
        if adj[v][i] and not visited[i]:
            dfs(i)


def bfs(v):
    q = [v]
    while q:
        s = q.pop()
        for i in range(n):
            if adj[s][i] and not visited[i]:
                q.insert(0, i)
                visited[i] = 1
        print(s, end=' ')


print('DFS')
visited = [0]*n
dfs(0)
print('\nBFS')
visited = [0]*n
bfs(0)


'''
input
1 2 30
1 4 1
2 2 1
0 1 4
0 3 6
3 1 4
3 3 3
3 4 1
4 2 9
2 5 9
4 6 6
5 6 1
-1 -1 0
output
DFS
0 1 2 5 6 4 3 
BFS
0 1 3 2 4 5 6
'''
