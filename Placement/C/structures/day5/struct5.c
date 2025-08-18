#include <stdio.h>
#include <string.h>

struct stu
{
    int id, m1, m2, m3;
    float avg;
    char name[20];
};

int main()
{
    int n, i;
    scanf("%d", &n);
    struct stu s[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d %s %d %d %d", &s[i].id, s[i].name, &s[i].m1, &s[i].m2, &s[i].m3);
        s[i].avg = (s[i].m1+s[i].m2+s[i].m3)/3;
    }
    for (i = 0; i < n; i++)
        printf("%.2f ", s[i].avg);
}