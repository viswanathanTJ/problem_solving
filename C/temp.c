#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

char *getSequence(char *str)
{
    int i, n = 0, a[10] = {0}, ind = 0;
    char *ret = malloc(100);
    for (i = 0; str[i]; i++)
        a[str[i] - '0']++;
    for (i = 1; i < 10; i++)
        if (a[i])
        {
            ret[ind++] = i+'0';
            ret[ind++] = a[i] + '0';
        }
    ret[ind] = '\0';
    return ret;
}

int main()
{
    char word[100];
    scanf("%s", word);
    printf("%s", getSequence(word));
}