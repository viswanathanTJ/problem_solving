#include <stdio.h>
#include <limits.h>

int main()
{
    int i, j, n, t, a, r, c, max, min;
    scanf("%d", &t);
    while (t--)
    {
        int res = INT_MIN;
        scanf("%d %d", &r, &c);
        for (i = 0; i < r; i++)
        {
            max = INT_MIN;
            min = INT_MAX;
            for (j = 0; j < c; j++)
            {
                scanf("%d", &a);
                if (a > max)
                    max = a;
                if (a < min)
                    min = a;
            }
            if (max - min > res)
                res = max - min;
        }
        printf("%d\n", res);
    }
}