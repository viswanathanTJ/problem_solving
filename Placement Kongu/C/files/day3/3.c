#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    FILE *fp, *temp;
    fp = fopen("input.txt", "w");
    fprintf(fp, "Examly is here to help you\nFocus on your placement practice");
    fclose(fp);
    FILE *fptr = fopen("input.txt", "r");
    temp = fopen("input1.txt", "w");
    char c;
    while ((c = fgetc(fptr)) != EOF)
        if (c >= 'a' && c <= 'z')
            printf("%c", c - 32);
        else if (c >= 'A' && c <= 'Z')
            printf("%c", c + 32);
        else
            printf("%c", c);
    fclose(fptr);
}