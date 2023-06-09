#include <stdio.h>
#include <string.h>

struct stu
{
    char name[20], dept[5];
    int id, sal;
};

int main()
{
    int n, i;
    scanf("%d", &n);
    int it[n], sal[n], si=0, ii=0;
    struct stu s[n];
    for (i = 0; i < n; i++)
    {
        scanf("%s %d %s %d", s[i].name, &s[i].id, s[i].dept, &s[i].sal);
        if(s[i].sal > 50000)
            sal[si++] = i;
        if(strcmp(s[i].dept, "IT") == 0)
            it[ii++] = i;
    }
    printf("IT department employees\n");
    for (i = 0; i < ii;i++)
        printf("Name : %s ID : %d Salary : %d\n", s[i].name, s[i].id, s[i].sal);
    printf("Employees with salary greater than 20000\n");
    for (i = 0; i < si;i++)
        printf("Name : %s ID : %d Dept : %s\n", s[i].name, s[i].id, s[i].dept);
}