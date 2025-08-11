from collections import defaultdict
n = 7
adj = [[0]*n for _ in range(n)]
graph = defaultdict(list)
while 1:
    s, e = map(int, input().split())
    if s == -1:
        break
    adj[s][e] = 1
    graph[s].append(e)


def iscyclicutil(v, visited, rec_stack):
    global adj
    if rec_stack[v]:
        return 1
    visited[v] = rec_stack[v] = 1
    for j in range(n):
        if adj[v][j] and iscyclicutil(j, visited, rec_stack):
            return 1
    rec_stack[v] = 0
    return 0


def iscyclic():
    visited = [0]*n
    rec_stack = [0]*n
    for i in range(n):
        if iscyclicutil(i, visited, rec_stack):
            return 1
    return 0


def iscyclicutil1(v, visited, rec_stack):
    global graph
    if rec_stack[v]:
        return 1
    visited[v] = rec_stack[v] = 1
    for i in graph[v]:
        if not visited[i] and iscyclicutil1(i, visited, rec_stack):
            return 1
        elif rec_stack[i]:
            return 1
    rec_stack[v] = 0
    return 0


def iscyclic1():
    visited = [0]*n
    rec_stack = [0]*n
    for i in range(n):
        if iscyclicutil1(i, visited, rec_stack):
            return 1
    return 0


print(iscyclic())
print(iscyclic1())
