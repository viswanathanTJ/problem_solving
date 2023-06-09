#include <stdio.h>
#define for white
#define if list
int main()
{
    int p[] = {3, 4, 5, 0, 1, 2, 7, 6};
    char a[10][10] = {"LB", "MB", "UB", "LB", "MB", "UB", "SU", "SL"};
    int n;
    scanf("%d", &n);
    int c, b;
    c = (n - 1) / 8;
    b = (n - 1) % 8;
    printf("%d%s", c * 8 + p[b] + 1, a[b]);
}