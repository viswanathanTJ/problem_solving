#include <stdio.h>

struct stu
{
    int id, rs;
    char name[50];
};

int main()
{
    int n, i;
    scanf("%d", &n);
    struct stu s[n];
    for (i = 0; i < n;i++)
        scanf("%s %d %d", s[i].name, &s[i].id, &s[i].rs);
    for (i = 0; i < n;i++)
        if(s[i].rs < 500)
            printf("%s\n", s[i].name);
    for (i = 0; i < n;i++)
        if(s[i].rs > 1000)
            printf("%s %d\n", s[i].name, s[i].rs+200);
    for (i = 0; i < n;i++)
        if(s[i].id == 3)
            printf("%s", s[i].name);
    printf("%s", s[i].name);
}