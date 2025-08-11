#include <stdio.h>

struct temp
{
    int r, i;
};

int main()
{
    struct temp t, t1;
    scanf("%d %d", &t.r, &t.i);
    scanf("%d %d", &t1.r, &t1.i);
    printf("%d.0 + %d.0i", t.r + t1.r, t.i + t1.i);
}