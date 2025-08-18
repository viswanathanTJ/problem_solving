#include <stdio.h>
int main()
{
    int n, k, sum = 0;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++)
    {
        int num;
        scanf("%d", &num);
        sum += (num / k);
    }
    printf("%d", sum);
    return 0;
}