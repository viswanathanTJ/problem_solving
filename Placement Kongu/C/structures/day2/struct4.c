#include <stdio.h>

typedef struct stu
{
    char name[50], st[50], loc[50], city[50];
    int id, salary, dno, pin, d, m, y;
}ss;

int main()
{
    int n, i;
    scanf("%d", &n);
    ss s[n];
    for (i = 0; i < n;i++) {
        scanf("%s %d %d %d %s %s %s %d %d %d %d",
              s[i].name, &s[i].id, &s[i].salary, &s[i].dno,
              &s[i].st, &s[i].loc, &s[i].city, &s[i].pin,
              &s[i].d, &s[i].m, &s[i].y);
        printf("%s %d %d %d %s %s %s %d %d %d %d",
              s[i].name, s[i].id, s[i].salary, s[i].dno,
              s[i].st, s[i].loc, s[i].city, s[i].pin,
              s[i].d, s[i].m, s[i].y);
        printf("\n");
    }
}