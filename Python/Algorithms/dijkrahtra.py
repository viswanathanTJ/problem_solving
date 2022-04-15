n = 7
adj = [[0]*n for _ in range(n)]
while 1:
    s, e, w = map(int, input().split())
    if s == -1:
        break
    adj[s][e] = w
    adj[e][s] = w

key = [float('inf')]*n
visited = [0]*n
start = 5
key[start] = 0

def get_min():
    m, mi = float('inf'), 0
    for i in range(n):
        if not visited[i] and m > key[i]:
            m = key[i]
            mi = i
    visited[mi] = 1
    return mi

for _ in range(n):
    parent = get_min()
    for i in range(n):
        if adj[parent][i] and not visited[i] and \
                key[i] > adj[parent][i] + key[parent]:
            key[i] = adj[parent][i] + key[parent]

for i in range(n):
    print(start, 'to', i, 'is', key[i])


'''
inputs
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
5 to 0 is 12
5 to 1 is 8
5 to 2 is 9
5 to 3 is 8
5 to 4 is 7
5 to 5 is 0
5 to 6 is 1
'''