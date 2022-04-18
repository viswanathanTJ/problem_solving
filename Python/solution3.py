def max_edge_remove(n, edges):
    def find(dsu, x):
        if dsu[x] == -1: return x
        dsu[x] = find(dsu, dsu[x])
        return dsu[x]

    def union(dsu,x,y):
        res1,res2 = find(dsu,x),find(dsu,y)
        if res1==res2: return False
        dsu[res1] = res2
        return True
    
    if n==1: return 0
    
    tot,rem1,rem2 = 0,n,n
    dsu1,dsu2 = {i:-1 for i in range(1,n+1)},{i:-1 for i in range(1,n+1)}
    print(dsu2)
    edges.sort(key=lambda x:x[2],reverse=True)

    for x,y,col in edges:
        if col==3: 
            res=union(dsu1,x,y); union(dsu2,x,y)
            if res: rem1-=1; rem2-=1; tot += 1
        elif col==1: 
            res=union(dsu1,x,y)
            if res: rem1-=1; tot += 1
        else: 
            res=union(dsu2,x,y)
            if res: rem2-=1; tot += 1
        if rem1==1 and rem2==1: return len(edges)-tot

    
    return -1

n, m = map(int, input().split())
l = []
for _ in range(m):
    l.append(list(map(int, input().split())))

print(max_edge_remove(n, l))