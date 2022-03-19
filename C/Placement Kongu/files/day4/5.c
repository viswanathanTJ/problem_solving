#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *file, *fp;
    fp = fopen("input.txt", "w");
    fprintf(fp, "Examly is an AI Powered\nMobile First\nLearning and Assessment Tool for corporates and coaching centers of all sizes");
    fclose(fp);

    return 0;
}
