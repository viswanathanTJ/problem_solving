#include<stdio.h>
#include<stdlib.h>
#define MAX 20

int visited[MAX], adj[MAX][MAX], n;

void dfs(int s) {
    printf("%d ", s);
    visited[s] = 1;
    for (int i = 0; i < n;i++)
        if(adj[s][i] && !visited[i])
            dfs(i);
}

int main(){
    int v, e;
    printf("Enter the number of vertices and edges(v,e): ");
    scanf("%d %d", &v, &e);
    n = v;
    for(int i=0; i<e; i++){
        int S, E;
        scanf("%d %d", &S, &E);
        adj[S][E] = 1;
    }
    printf("\nDFS\n");
    dfs(0);
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