#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 256
int main()
{
    FILE *fptr1, *fptr2;
    fptr1 = fopen("input.txt", "w");
    fprintf(fptr1, "one\ntwo\nthree\nfour\nfive\nsix\nseven\neight\nnine\nten");
    fclose(fptr1);
    char newLine[100], str[100], c;
    fgets(newLine, 100, stdin);
    // printf("%s\n", newLine);
    int lno, temp = 0;
    // scanf("%d", &lno);
    // INPUT IS NOT PROVIDED ignore this one
    printf("%d\n", lno);
    fptr1 = fopen("input.txt", "r");
    fptr2 = fopen("replaced.txt", "w");
    while (!feof(fptr1))
    {
        fgets(str, 100, fptr1);
        temp++;
        if (temp != lno)
            fprintf(fptr2, "%s", str);
        else
            fprintf(fptr2, "%s", newLine);
    }
    fclose(fptr1);
    fclose(fptr2);
    remove("input.txt");
    rename("replaced.txt", "input.txt");
    fptr1 = fopen("input.txt", "r");
    while ((c = getc(fptr1)) != EOF)
    {
        printf("%c", c);
    }
    fclose(fptr1);
}