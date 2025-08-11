#include <stdio.h>
int main()
{
    int a, b, c, sum = 0, i, n;
    scanf("%d", &n);
    a = 1;
    b = 2;
    c = 3;
    for (i = 0; i < n; i++)
    {
        sum += (a * b * c);
        a = b;
        b = c;
        c += 1;
    }
    printf("%d", sum);
}