#include <stdio.h>
int main()
{
    FILE *fp, *fileptr1, *fileptr2;
    char ch;
    fp = fopen("input.txt", "w");
    fprintf(fp, "One\nTwo\nThree\nFour\nFive\nSix\nSeven\nEight\nNine\nTen\nEleven\nTwelve");
    fclose(fp);

    char c;
    int n = 2, t = 1;
    scanf("%d", &n);
    // INPUT IS NOT
    fp = fopen("input.txt", "r");
    while ((c = fgetc(fp)) != EOF)
    {
        if (c == '\n')
            t++;
        if (n == t)
        {
            while ((c = fgetc(fp)) != '\n')
            {
            }
            printf("\n");
            t++;
        }
        else
            printf("%c", c);
    }
    fclose(fp);
}