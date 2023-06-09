// Q1
#include <stdio.h>
#define max(a, b) (a > b) ? a : b

main()
{
    int n, i;
    scanf("%d", &n);
    int arr[n];
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    int ms = arr[0];
    int cs = arr[0];
    for (i = 1; i < n; i++)
    {
        if (arr[i - 1] < arr[i])
        {
            cs = cs + arr[i];
            ms = max(ms, cs);
        }
        else
        {
            ms = max(ms, cs);
            cs = arr[i];
        }
    }
    printf("%d", max(ms, cs));
}
