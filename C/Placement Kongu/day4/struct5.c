#include <stdio.h>
#include <stdlib.h>

struct bank
{
    char name[50];
    int id, rs;
};

int main()
{
    int n, i;
    scanf("%d", &n);
    int more[n], mi = 0, ai;
    struct bank p[n];
    for (i = 0; i < n; i++)
    {
        scanf("%s %d %d", p[i].name, &p[i].id, &p[i].rs);
        if (p[i].rs < 500)
            printf("%s \n", p[i].name);
        if (p[i].id == 3)
            ai = i;
        if (p[i].rs > 1000)
            more[mi++] = i;
    }
    for (i = 0; i < mi; i++)
        printf("%s %d\n", p[more[i]].name, p[more[i]].rs + 200);
    printf("%s  ", p[ai].name);
}