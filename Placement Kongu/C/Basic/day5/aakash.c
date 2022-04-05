#include <stdio.h>

int main()
{
    int n, l, b;
    scanf("%d", &n);
    if (n < 10)
        printf("-1");
    else
        b = n % 10;
    l = n / 10;
    printf("%d", 2 * (l + b));
}