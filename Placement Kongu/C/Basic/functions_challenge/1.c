#include <stdio.h>

void common(int a[], int x, int b[], int y)
{
    for (int i = 0; i < x; i++)
        for (int j = 0; j < y; j++)
            if (a[i] == b[j])
            {
                printf("%d ", a[i]);
                break;
            }
}

int main()
{
    int n, m, i;
    scanf("%d %d", &n, &m);
    int a[n], b[m];
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    for (i = 0; i < m; i++)
        scanf("%d", &b[i]);
    common(a, n, b, m);
}