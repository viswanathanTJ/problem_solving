#include <stdio.h>

struct stu
{
    char name[50];
    int age, rs;
};

int main()
{
    int n, i;
    scanf("%d", &n);
    struct stu s[n];
    int arr[n], ii;
    for (i = 0; i < n; i++)
    {
        scanf("%s %d %d", s[i].name, &s[i].age, &s[i].rs);
        if (s[i].rs <= 200)
            printf("%s ", s[i].name);
        if (s[i].rs >= 1000)
            arr[ii++] = s[i].rs;
    }
    printf("\n");
    for (i = 0; i < ii; i++)
        printf("%d ", arr[i] + 100);
}