#include <stdio.h>
#include <stdlib.h>
#define MAX 20

int q[MAX], adj[MAX][MAX], visited[MAX], f = 0, r = -1, n;

void bfs(int v)
{
    for (int i = 0; i < n; i++)
        if (adj[v][i] && !visited[i])
            q[++r] = i;
    if (f <= r)
    {
        visited[q[f]] = 1;
        printf("%d ", v);
        bfs(q[f++]);
    }
}

int main()
{
    int v, e;
    printf("Enter the number of vertices and edges(v,e): ");
    scanf("%d %d", &v, &e);
    n = v;
    for (int i = 0; i < e; i++)
    {
        int S, E;
        scanf("%d %d", &S, &E);
        adj[S][E] = 1;
    }
    printf("\nBFS\n");
    bfs(0);
    return 0;
}
/* inputs
5 6
0 1
0 2
1 3
1 4
2 4
0 4
*/