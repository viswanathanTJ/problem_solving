#include <stdio.h>

int main(void)
{
    int m, t, a, b, c1, c2;
    scanf("%d", &t);
    while (t-- > 0)
    {
        scanf("%d %d %d", &m, &a, &b);
        c1 = a - m;
        if(c1 < 0) c1 = -c1;
        c2 = b - a;
        if(c2 < 0) c2 = -c2;
        c2 += 1;
        printf("%d\n", c1 < c2 ? c1 : c2);
    }
    return 0;
}
