#include <stdio.h>
#include <string.h>

struct stu
{
    int id, age;
    char name[50];
};

int main()
{
    int n, i, ti;
    scanf("%d", &n);
    struct stu s[n];
    char t[50];
    for (i = 0; i < n; i++)
        scanf("%d %s %d", &s[i].id, s[i].name, &s[i].age);
    printf("Unsorted Student Records:\n");
    for (i = 0; i < n;i++)
        printf("Id = %d Name = %s Age = %d\n", s[i].id, s[i].name, s[i].age);
    printf("\n\n");
    printf("Student Records sorted by Name:\n");
    for (i = 0; i < n;i++)
        for (int j = i+1; j < n;j++) 
            if(strcmp(s[i].name, s[j].name) > 0) {
                ti = s[i].id;
                s[i].id = s[j].id;
                s[j].id = ti;
                ti = s[i].age;
                s[i].age = s[j].age;
                s[j].age = ti;
                strcpy(t, s[i].name);
                strcpy(s[i].name, s[j].name);
                strcpy(s[j].name, t);
            }
    for (i = 0; i < n;i++) {
        printf("Id = %d Name = %s Age = %d\n", s[i].id, s[i].name, s[i].age);
        if(i!=n-1)
            printf(" \n");
        else
            printf("\n");
    }
}