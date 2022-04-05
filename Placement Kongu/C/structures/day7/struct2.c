#include <stdio.h>

struct stu
{
    char name[50];
    int age, w;
    float h;
};

int main()
{
    int n, i;
    scanf("%d", &n);
    struct stu s[n];
    for (i = 0; i < n; i++)
    {
        scanf("%s %d %d %f", s[i].name, &s[i].age, &s[i].w, &s[i].h);
        printf("Name: %s Age: %d Weight: %d Height: %.1f\n",
               s[i].name, s[i].age, s[i].w, s[i].h);
    }
}