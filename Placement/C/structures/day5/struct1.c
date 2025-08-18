#include <stdio.h>
#include <math.h>

struct axis
{
    int x1, x2, y1, y2;
};

int main()
{
    struct axis a;
    scanf("%d %d", &a.x1, &a.y1);
    scanf("%d %d", &a.x2, &a.y2);
    printf("Distance : %.2f\n", sqrt((a.x2 - a.x1) * (a.x2 - a.x1) + (a.y2 - a.y1) * (a.y2 - a.y1)));
    printf("Midpoint : %.2f %.2f\n", ((a.x1 + a.x2) / 2.0), ((a.y1 + a.y2) / 2.0));
}