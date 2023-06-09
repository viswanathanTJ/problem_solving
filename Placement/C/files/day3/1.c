#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char s[50], in[500], cmp[50];
    gets(in);
    scanf("%s", cmp);
    int c = 0, index = 1, len;
    for (len = 0; cmp[len] != '\0'; len++)
        ;
    char ch, pc = cmp[0];
    FILE *f = fopen("input.txt", "w+");
    fputs(in, f);
    fseek(f, 0, SEEK_SET);
    while ((ch = fgetc(f)) != EOF)
    {
        if (ch == cmp[index] && pc == cmp[index - 1])
        {
            index++;
            pc = ch;
            if (index == len)
                c++;
        }
        else
        {
            pc = cmp[0];
            index = 1;
        }
    }
    printf("%s - %d", cmp, c);
    fclose(f);
}