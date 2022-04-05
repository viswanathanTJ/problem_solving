#include <stdio.h>
int main()
{
    int n, i, m = 0;
    scanf("%d", &n);
    int a[n], b[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
        b[i] = 1;
    }
    for (i = 0; i < n - 1; i++)
    {
        if (a[i] > a[i + 1] && b[i] <= b[i + 1])
        {
            b[i] = b[i + 1] + 1;
            for (int j = i; j > 0; j--)
            {
                if (a[j - 1] > a[j] && b[j - 1] <= b[j])
                    b[j - 1] = b[j] + 1;
                else
                    break;
            }
        }
        else if (a[i] < a[i + 1] && b[i + 1] <= b[i])
            b[i + 1] = b[i] + 1;
    }
    for (i = 0; i < n; i++)
        m += b[i];
    printf("%d", m);
}