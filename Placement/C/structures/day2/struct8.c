#include <stdio.h>
#include <string.h>

struct stu
{
    char name[50];
    int id, yoe, salary;
};

int main()
{
    int n, i;
    scanf("%d", &n);
    struct stu s[n];
    for (i = 0; i < n; i++)
        scanf("%s %d %d %d", s[i].name, &s[i].id, &s[i].yoe, &s[i].salary);
    for (i = 0; i < n; i++) {
        printf("\n Employee Name :%s\n Employee Id: %d\n years of experience : %d\n", s[i].name, s[i].id, s[i].yoe);
        if(s[i].yoe >= 10)
            s[i].salary += (10 / 100) * s[i].salary;
        else if(s[i].yoe >= 5 && s[i].yoe < 10)
            s[i].salary += (5 / 100) * s[i].salary;
        else if(s[i].yoe >= 1 && s[i].yoe < 4)
            s[i].salary += (2 / 100) * s[i].salary;
        printf(" salary : %d ", s[i].salary);
        if(i!=n-1) printf("\n\n");
    }
}