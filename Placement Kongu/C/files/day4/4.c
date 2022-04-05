#include <stdio.h>
#include <stdlib.h>
void count_temp(FILE *);
void average_temp(FILE *);
int main()
{
    FILE *fp;
    int temp;
    fp = fopen("input.txt", "w");
    fprintf(fp, "2 68 74 59 45 41 58 60 67 65 78 82 88 91 92 90 93 87 80 78 79 72 68 61 59");
    fclose(fp);
    fp = fopen("input.txt", "r");
    count_temp(fp);
    fseek(fp, 0, SEEK_SET);
    average_temp(fp);
    fclose(fp);
    return 0;
}
// You are using GCC
void count_temp(FILE *fp)
{
    int n, hd = 0, cd = 0, pd = 0;
    float tot = 0;
    fp = fopen("input.txt", "r");
    while ((fscanf(fp, "%d", &n)) == 1)
    {
        if (n > 84)
            hd++;
        else if (n > 59 && n < 85)
            pd++;
        else if (n < 60)
            cd++;
        tot += n;
    }
    printf("Hot Days : %d\n", hd);
    printf("Pleasant Days : %d\n", pd);
    printf("Cold Days : %d\n", cd);
    printf("Average Temperature : %.2f", tot / (hd + pd + cd));
    fclose(fp);
    // Type your code here
}

void average_temp(FILE *fp)
{
    // Type your code here
}
