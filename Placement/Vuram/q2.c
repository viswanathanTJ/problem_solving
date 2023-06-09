#include <stdio.h>

main()
{
    int n, s = 0, t, p;
    scanf("%d", &n);
    while (n)
    {
        t = n % 10;
        s += (9 - t);
        n /= 10;
    }
    printf("%d", s);
}