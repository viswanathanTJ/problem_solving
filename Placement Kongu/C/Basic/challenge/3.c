#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    if (!(n % 5))
        printf("You are a loser");
    else
        printf("%d", n % 5);
}