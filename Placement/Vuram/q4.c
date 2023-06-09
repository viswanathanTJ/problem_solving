#include <stdio.h>
#define max(a, b) a > b ? a : b
#define min(a, b) a < b ? a : b

int main()
{
    int i, x, y, p, max = -1, min = 9999;
    scanf("%d %d %d", &x, &y, &p);
    for (i = 1; i <= p; i++)
        if (i & 1)
            x *= 2;
        else
            y *= 2;
    x = max(x, y);
    y = min(x, y);
    printf("%d", x / y);
}