#include <stdio.h>

struct stu
{
    int id, gender, age;
};

int main()
{
    int n, i, m = 0, f = 0, a = 0;
    scanf("%d", &n);
    struct stu s[n];
    for (i = 0; i < n; i++) {
        scanf("%d %d %d", &s[i].id, &s[i].gender, &s[i].age);
        if(s[i].gender == 1)
            m++;
        if(s[i].gender == 2)
            f++;
        if(s[i].age > 40)
            a++;
    }
    printf("%d %d\n%d", m, f, a);
}