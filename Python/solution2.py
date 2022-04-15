n = 7
mat = [[0]*n for _ in range(n)]
visited = [0] * n

while 1:
    s, e, w = map(int, input().split())
    if s == -1:
        break
    mat[s][e] = w
    mat[e][s] = w

keys = [float('inf')] * n
keys[0] = 0

def get_min():
    m, mi = float('inf'), 0
    for i in range(n):
        if not visited[i] and m > keys[i]:
            m = keys[i]
            mi = i
    visited[mi] = 1
    return mi

for _ in range(n):
    parent = get_min()
    for i in range(n):
        if not visited[i] and mat[parent][i] and \
                keys[i] > mat[parent][i] + keys[parent]:
            keys[i] = mat[parent][i] + keys[parent]
            
for i in range(n):
    print(0, 'to', i, 'is', keys[i])