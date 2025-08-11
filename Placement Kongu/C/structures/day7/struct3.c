#include <stdio.h>

struct axis
{
    int x, y;
};

int main()
{
    struct axis a;
    scanf("%d %d", &a.x, &a.y);
    if (a.x > 0 && a.y > 0)
        printf("%d and %d lies in quadrant 1", a.x, a.y);
    else if (a.x > 0 && a.y < 0)
        printf("%d and %d lies in quadrant 4", a.x, a.y);
    else if (a.x < 0 && a.y < 0)
        printf("%d and %d lies in quadrant 3", a.x, a.y);
    else if (a.x < 0 && a.y > 0)
        printf("%d and %d lies in quadrant 2", a.x, a.y);
}