#include <stdio.h>
int main()
{
    int n, c = 0;
    scanf("%d", &n);
    while (n > 0)
    {
        c++;
        if (n == 0)
            break;
        n = n / 10;
    }
    printf("%d", c);
}