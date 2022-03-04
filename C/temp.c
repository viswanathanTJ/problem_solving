#include <stdio.h>
#include <string.h>

struct stu
{
    char name[20], dept[30], deg[5], roll[10], gender[6];
    float cut;
};

int main()
{
    int n, i;
    scanf("%d", &n);
    struct stu s[n];
    float hc = 0;
    int in;
    for (i = 0; i < n; i++)
    {
        scanf("%s %s %s %s %s %f", s[i].name, s[i].roll, s[i].deg, s[i].dept, &s[i].cut);
        if (hc < s[i].cut)
            hc = s[i].cut;
    }
    printf("The student with the highest cutoff mark is :\n");
    printf(" Student name : %s\n", s[i].name);
    printf(" Student cutoff mark : %f\n", hc);
}