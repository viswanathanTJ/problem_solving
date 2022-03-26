#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int m = 20, v = 40;
    for (int i = 0; i < n; i++, v += 4)
    {
        printf("%d ", m);
        m += v;
    }
}