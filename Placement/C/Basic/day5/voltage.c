#include <stdio.h>

int cnt(int n)
{
    int count = 0;
    while (n)
    {
        if (!(n & 1))
            count++;
        n >>= 1;
    }
    return count;
}
int res(int N)
{
    int count = cnt(N);
    return (1 << count);
}
int main()
{
    int n;
    scanf("%d", &n);
    printf("%d", res(n));
}
