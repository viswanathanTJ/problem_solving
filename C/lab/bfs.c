#include <stdio.h>
#define MAX 20

int q[MAX], adj[MAX][MAX], visited[MAX], n, f = 0, r = -1;

void bfs(int v) {
    for (int i = 0; i < n;i++)
        if(adj[v][i] && !visited[i])
            q[++r] = i;
    if(f <= r) {
        visited[v] = 1;
        printf("%d ", v);
        bfs(q[f++]);
    }
}

int main() {
    int v, e;
    printf("Enter number of nodes and connections(v e): ");
    scanf("%d %d", &v, &e);
    n = v;
    for (int i = 0; i < e;i++) {
        int S, E;
        printf("\nEnter start end connections: ");
        scanf("%d %d", &S, &E);
        adj[S][E] = 1;
    }
    bfs(0);
}