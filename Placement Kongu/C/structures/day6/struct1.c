#include <stdio.h>

struct stu
{
    int id, age, m[5], tot, avg;
    char name[50];
};

int main()
{
    int n, i, j, c = 0;
    scanf("%d", &n);
    struct stu s[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d %d %s", &s[i].id, &s[i].age, s[i].name);
        printf("%d %d %s ", s[i].id, s[i].age, s[i].name);
        s[i].tot = s[i].avg = 0;
        for (j = 0; j < 5; j++)
        {
            scanf("%d", &s[i].m[j]);
            printf("%d ", s[i].m[j]);
            s[i].tot += s[i].m[j];
        }
        if (s[i].tot >= 400 && s[i].tot <= 500)
            c++;
        s[i].avg = s[i].tot / 5;
        printf("%d %d.00\n", s[i].tot, s[i].avg);
    }
    printf("%d\n", c);
    for (i = 0; i < n; i++)
        if (s[i].age > 18)
            printf("%s ", s[i].name);
}