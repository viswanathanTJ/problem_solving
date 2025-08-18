#include <stdio.h>
int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    int ar[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &ar[i]);
    int sum = ar[0];
    for (int i = 1; i < n; i++)
        ar[i] = (ar[i - 1] - k) + (ar[i] - k);
    printf("%d", ar[n - 1]);
    return 0;
}