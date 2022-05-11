#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

char *getSequence(char *str)
{
    char *ret = malloc(100);
    int ind = 0;
    for (int i = 0; str[i]; i++)
    {
        int count = 1;
        if(str[i]-'0' > 0 && str[i]-'0' < 10) {
            while (str[i] == str[i + 1])
            {
                i++;
                count++;
            }
            ret[ind++] = str[i];
            ret[ind++] = count+'0';
        }
    }
    ret[ind] = '\0';
    return ind ? ret : "No string found";
}

int main()
{
    char word[100];
    scanf("%s", word);
    printf("%s", getSequence(word));
}