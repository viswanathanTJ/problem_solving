#include <stdio.h>

int main()
{
    int a,b,n;
    scanf("%d %d %d", &a, &b, &n);
    for(int i=0;i<n;i++)
        if(i%2)
            b *= 2;
        else
            a *= 2;
    printf("%d", a+b);
}