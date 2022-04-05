#include <stdio.h>
int s(int n)
{
    int v = n, c = 0;
    while (v != 0)
    {
        if (!(n % v))
            c++;
        v--;
    }
    return c;
}
int main()
{
    int n, m, c = 0, v;
    scanf("%d %d", &n, &m);
    for (int i = n; i <= m; i++)
    {
        v = s(i);
        if (v == 4)
            c++;
    }
    printf("%d", c);
}