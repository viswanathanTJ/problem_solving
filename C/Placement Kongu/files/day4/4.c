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
    // Type your code here
}

void average_temp(FILE *fp)
{
    // Type your code here
}
