#include <stdio.h>
#define x(a, b, c) a + b * 5 / 4 + c % 3 * 5
#define y(u, v) u > v ? u : v
#define z(i, j, k) ++i && ++j && ++k

int main()
{
    int a[8];
    for (int i = 0; i < 8; i++)
        scanf("%d", &a[i]);
    printf("x=%d\n", x(a[0], a[1], a[2]));
    printf("y=%d\n", y(a[3], a[4]));
    printf("z=%d", z(a[5], a[6], a[7]));
}