#include <stdio.h>
#include <string.h>

struct stu
{
    char name[50], des[50], dep[50];
    int id, bs, da, hra, pf, ts;
};

int main()
{
    int n = 10, i, c;
    struct stu s[n];
    for (i = 0; i < n; i++) {
        scanf("%s %d %s %s %d %d %d %d", s[i].name, &s[i].id, s[i].des, s[i].dep, &s[i].bs, &s[i].da, &s[i].hra, &s[i].pf);
        s[i].ts = s[i].bs + s[i].da + s[i].hra + s[i].pf;
    }
    scanf("%d", &c);
    for (i = 0; i < n; i++) 
        if(s[i].id == c) {
            printf("SALARY SLIP\n");
            printf("Employee Name : %s\nEmployee Total Salary : %d.00", s[i].name, s[i].ts);
            return 0;
        }
    printf("No Records Found for given Employee Number!");
}