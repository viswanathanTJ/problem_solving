#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *file, *fp;
    fp = fopen("input.txt", "w");
    fprintf(fp, "Examly is an AI Powered\nMobile First\nLearning and Assessment Tool for corporates and coaching centers of all sizes");
    fclose(fp);
    int lc = 1, wc = 0, cc = 0;
    fp = fopen("input.txt", "r");
    char c;
    while ((c = fgetc(fp)) != EOF)
    {
        if (c == ' ')
            wc++;
        else if (c == '\n')
            lc++;
        else
            cc++;
    }
    printf("Total words      = %d\n", wc + lc);
    printf("Total characters = %d\n", cc);
    printf("Total Space      = %d\n", wc);
    printf("Total lines      = %d ", lc);
    return 0;
}
