#include <stdio.h>
#include <string.h>
int main()
{
    int n;
    scanf("%d", &n);
    char str[n][20], s[20];
    for (int i = 0; i < n; i++)
    {
        scanf("%s", &str[i]);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (strcmp(str[i], str[j]) < 0)
            {
                strcpy(s, str[i]);
                strcpy(str[i], str[j]);
                strcpy(str[j], s);
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        printf("%d %s\n", i + 1, str[i]);
    }
    return 0;
}