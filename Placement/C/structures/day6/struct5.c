#include <stdio.h>

struct stu
{
    int id, m[6], tot, avg;
    char name[50];
};

int main()
{
    int n, i, j, p;
    scanf("%d", &n);
    struct stu s[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d %s", &s[i].id, s[i].name);
        printf("%d %s ", s[i].id, s[i].name);
        p = 1;
        s[i].tot = s[i].avg = 0;
        for (j = 0; j < 6; j++)
        {
            scanf("%d", &s[i].m[j]);
            if (s[i].m[j] < 50)
                p = 0;
            printf("%d ", s[i].m[j]);
            s[i].tot += s[i].m[j];
        }
        s[i].avg = s[i].tot / 6;
        printf("%d %d.00\n", s[i].tot, s[i].avg);
        if (p)
        {
            printf("pass\n");
            if (s[i].avg >= 90 && s[i].avg <= 100)
                printf("Grade = S and Grade Point = 10\n");
            else if (s[i].avg >= 80 && s[i].avg < 90)
                printf("Grade = A and Grade Point = 9\n");
            else if (s[i].avg >= 70 && s[i].avg < 80)
                printf("Grade = B and Grade Point = 8\n");
            else if (s[i].avg >= 60 && s[i].avg < 69)
                printf("Grade = C and Grade Point = 7\n");
            else if (s[i].avg >= 50 && s[i].avg < 59)
                printf("Grade = D and Grade Point = 6\n");
        }
        else
            printf("fail\n");
    }
}