#include <stdio.h>
#include <string.h>

struct stu
{
    char name[20], des[20],  dept[5];
    int bs;
};

int main()
{
    struct stu s;
    scanf("%s %s %s %d", s.name, s.des, s.dept, &s.bs);
    if(strcmp("Secretary", s.name) == 0 || strcmp("Addition_Secretary", s.name))
        printf("Air travel is allowd");
    else if ((strcmp("Joint Secretary", s.name) == 0 || strcmp("Deputy_Secretary", s.name) == 0)
                && s.bs > 20000)
        printf("Air travel is allowd");
    else if (strcmp("Under_Secretary", s.name) == 0 && strcmp("Marketing", s.dept) == 0)
        printf("Air travel is allowd");
    else
        printf("Air travel is not allowd");
}