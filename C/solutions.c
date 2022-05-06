#include <stdio.h>

int main()
{
    int n, i, add = 0, mul = 1, t, res = 0;
    scanf("%d", &n);
    int arr[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        t = arr[i];
        while (t > 0)
        {
            add += t % 10 != 0 ? t % 10 : 0;
            t /= 10;
        }
        if (arr[i] % add == 0)
        {
            res += 1;
            break;
        }
        add = 0;
        t = arr[i];
        while (t > 0)
        {
            mul *= t % 10 != 0 ? t % 10 : 1;
            t /= 10;
        }
        if (arr[i] % mul == 0)
            res += 1;
        mul = 1;
    }
    printf("%d", res);
}