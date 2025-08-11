#include <stdio.h>
#define max(a, b) a > b ? a : b

int main()
{
    int a[6];
    for (int i = 0; i < 6; i++)
        scanf("%d", &a[i]);
    int r = max(a[0] - a[3], a[1] - a[4]);
    printf("%d", max(r, a[2] - a[5]));
}