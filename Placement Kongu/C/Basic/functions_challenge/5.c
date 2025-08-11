#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *w = (int *)malloc(sizeof(int));
    int n, m, i, j;
    scanf("%d %d", &n, &m);
    int a[n][m], t;
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            scanf("%d", &a[i][j]);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            scanf("%d", &t);
            printf("%d ", t + a[i][j]);
        }
        printf("\n");
    }
}