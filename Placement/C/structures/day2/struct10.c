#include <stdio.h>
#include <string.h>

struct stu
{
    char name[3], dept[5];
    int id;
};

int main()
{
    int n = 3, i;
    struct stu s[n];
    scanf("%s", s[i].name);
    printf("%s\n", s[i].name);
    for (i = 0; i < n; i++) {
        scanf("%d %s", &s[i].id, s[i].dept);
        printf("%d %s\n", s[i].id, s[i].dept);
    }
}