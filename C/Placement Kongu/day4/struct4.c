#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct supermarket
{
    int pno, cost, no;
    char exp[11];
};

int main()
{
    int n, i, index, cost, amt;
    char t[11];
    scanf("%d", &n);
    struct supermarket p[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d %d %d %[^\n]s", &p[i].pno, &p[i].cost, &p[i].no, p[i].exp);
        printf("%d %d.00 %d %s\n", p[i].pno, p[i].cost, p[i].no, p[i].exp);
    }
    scanf("%d", &index);
    printf("\nProduct details of the searched product number\n");
    for (i = 0; i < n; i++)
        if (p[i].pno == index)
            printf("%d %d.00 %d %s\n", p[i].pno, p[i].cost, p[i].no, p[i].exp);

    scanf("%d", &cost);
    printf("\nProduct details of the searched product cost\n");
    for (i = 0; i < n; i++)
        if (p[i].cost == cost)
            printf("%d %d.00 %d %s\n", p[i].pno, p[i].cost, p[i].no, p[i].exp);

    scanf("%s", t);
    printf("\nProduct with the searched expiry date\n");
    for (i = 0; i < n; i++)
        if (strcmp(t, p[i].exp) == 0)
            printf("%d %d.00 %d %s", p[i].pno, p[i].cost, p[i].no, p[i].exp);
}