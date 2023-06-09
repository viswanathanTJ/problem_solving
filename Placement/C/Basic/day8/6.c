#include <stdio.h>
int main()
{
    int a, d, h;
    scanf("%d %d %d", &a, &d, &h);
    for (int k = 0; k < h; k++)
    {
        if (k % 2 == 0)
            a *= 2;
        else
            d *= 2;
    }
    printf("%d", a + d);
}