from collections import defaultdict


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

for k in graph.keys():
    print(k, graph.get(k))

visited = [0] * (n+1)
l = []

def dfs(v):
    visited[v] = 1
    l.append(v)
    for i in range(n+1):
        if not visited[i] and (i in [x[0] for x in graph[v]]):
            dfs(i)

dfs(1)
print(l)

destroy = 0
for key in graph.keys():
    for e, w in graph.get(key):
        if w == 3:
            print('1 enough')
