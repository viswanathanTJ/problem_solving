#include <stdio.h>
#include <string.h>

struct stu
{
    float cut;
    char name[100], dept[30], deg[15], roll[15], gender[10];
};

int main()
{
    int n, i;
    scanf("%d", &n);
    struct stu s[n];
    float hc = -999.0;
    int in = 0;
    for (i = 0; i < n; i++)
    {
        scanf("%s %s %s %s %s", s[i].name, s[i].roll, s[i].deg, s[i].dept, s[i].gender);
        scanf("%f", &s[i].cut);
        if (hc < s[i].cut)
        {
            hc = s[i].cut;
            in = i;
        }
    }
    printf("The student with the highest cutoff mark is :\n");
    printf(" Student name : %s\n", s[in].name);
    printf(" Student cutoff mark : %.2f\n", s[in].cut);
}