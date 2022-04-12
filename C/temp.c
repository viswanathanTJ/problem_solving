#include <stdio.h>
int n, c = 1, a[100][100];

void rec(int start)
{
    int i, j;
    for (i = start - 1; i < n; i++)
    {
        for (j = start; j < n - 1; j++)
        {
            if (i + 1 == j)
            {
                // if (c == 15)
                // {
                //     printf("c is 15 %d %d\n", i, j);
                // }
                a[i][j] = c++;
                // printf("%d %d = %d\n", i, j, a[i][j]);
                break;
            }
        }
    }
    // bottom right to top
    i = start + 1;
    for (j = i - start; j > 0; j--)
        a[j][i] = c++;
}

int main()
{
    int i, j;
    n = 6;
    // assigning zeros to the array
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            a[i][j] = 0;
    // center value added
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            if (i == j)
                a[i][j] = c++;
    // bottom right to top
    i = n - 1;
    for (j = n - 2; j >= 0; j--)
        a[j][i] = c++;

    // top right to top left
    i = 0;
    for (j = n - 2; j > 0; j--)
        a[i][j] = c++;

    // filling recursively
    for (i = 2; i < n - 1; i += 2)
    {
        // printf("rec %d\n", i);
        rec(i);
        c--;
    }

    // print array
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
            printf("%d ", a[i][j]);
        printf("\n");
    }
    return 0;
}