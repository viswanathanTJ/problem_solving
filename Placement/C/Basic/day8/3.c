#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int n, i, j;
    scanf("%d", &n);
    int *nn = (int *)malloc(sizeof(int));
    char s[n][50], t[50];
    for (i = 0; i < n; i++)
        scanf("%s", s[i]);
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++)
            if (strcmp(s[i], s[j]) > 0)
            {
                strcpy(t, s[i]);
                strcpy(s[i], s[j]);
                strcpy(s[j], t);
            }
    for (i = 0; i < n; i++)
        printf("%s ", s[i]);
}