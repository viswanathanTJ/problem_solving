#include <stdio.h>
#include <stdlib.h>
int main()
{
    int cprice, sprice, plamt;
    scanf("%d", &cprice);
    scanf("%d", &sprice);
    if (cprice < sprice)
    {
        plamt = abs(cprice - sprice);
        printf("profit amount: %d", plamt);
    }
    else if (sprice < cprice)
    {
        plamt = abs(sprice - cprice);
        printf("loss amount : %d", plamt);
    }
    else
    {
        printf("You are running in no profit no loss condition");
    }
}