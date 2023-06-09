#include <stdio.h>
#include <string.h>

struct studs
{
    char name[50];
    int m1, m2, m3;
    float avg;
};

int main()
{
    int n, i;
    float a;
    char t[50];
    scanf("%d", &n);
    struct studs s[n];
    for (i = 0; i < n;i++) {
        scanf("%s %d %d %d", s[i].name, &s[i].m1, &s[i].m2, &s[i].m3);
        s[i].avg = (s[i].m1+s[i].m2+s[i].m3)/3;
    }
    for (i = 0; i < n;i++)
        for (int j = i + 1; j < n;j++)
            if(s[i].avg < s[j].avg) {
                strcpy(t, s[i].name);
                strcpy(s[i].name, s[j].name);
                strcpy(s[j].name, t);
                a = s[i].avg;
                s[i].avg = s[j].avg;
                s[j].avg = a;
            }

    for (i = 0; i < n;i++)
        printf("%s %.2f\n", s[i].name, s[i].avg);
}