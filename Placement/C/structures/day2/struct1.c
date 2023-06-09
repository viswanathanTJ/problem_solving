#include <stdio.h>
struct stu
{
    int rno, age, marks[5], tot, avg;
    char name[50];
};
int main()
{
    int n, i, j, c = 0;
    scanf("%d", &n);
    struct stu s[n];
    s[0].rno = 6;
    s[0].marks[0] = 4;
    for (i = 0; i < n; i++)
    {
        scanf("%d%s%d", &s[i].rno, s[i].name, &s[i].age);
        s[i].tot = 0;
        for (j = 0; j < 5; j++)
        {
            scanf("%d", &s[i].marks[j]);
            s[i].tot += s[i].marks[j];
        }
        s[i].avg = s[i].tot / 5;
    }
    for (i = 0; i < n; i++)
    {
        printf("%d %s %d ", s[i].rno, s[i].name, s[i].age);
        for (j = 0; j < 5; j++)
            printf("%d ", s[i].marks[j]);
        printf("%d %.d.00\n", s[i].tot, s[i].avg);
        if (s[i].tot >= 400 && s[i].tot <= 500)
            c++;
    }
    printf("Number of students with total marks between 400-500 is : %d\n", c);
    for (i = 0; i < n; i++)
        if (s[i].age > 18)
            printf("%s ", s[i].name);
}