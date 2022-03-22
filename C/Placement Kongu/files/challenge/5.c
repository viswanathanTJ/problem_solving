#include <stdio.h>

typedef struct students
{
    int no, per;
    char name[50];
} stu;

int main()
{
    int n, i;
    scanf("%d", &n);
    stu s[n];
    for (i = 0; i < n; i++)
    {
        scanf("%d %s %d", &s[i].no, s[i].name, &s[i].per);
        printf("%d\n%s\n%d\n", s[i].no, s[i].name, s[i].per);
    }
}