#include <stdio.h>

int main()
{
    int n, c = 0;
    scanf("%d", &n);
    unsigned long long int res = 1;
    while(n > 0) {
        res *= (n*n*n);
        n--;
    }
    while(res > 0) {
        c += (res % 10) == 0 ? 1 : 0;
        res /= 10;
    }
    printf("%d", c);
}