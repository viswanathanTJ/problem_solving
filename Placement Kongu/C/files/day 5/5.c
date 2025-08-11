#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
int main()
{
    FILE *fout;
    fout = fopen("input.txt", "w");
    fprintf(fout, "Features of C language\nIt is a robust language with rich set of built-in functions and operators");
    fclose(fout);
    fout = fopen("input.txt", "r");
    char c;
    while ((c = fgetc(fout)) != EOF)
    {
        if (c > 96 && c < 123)
            fputc(c - 32, stdout);
        else
            fputc(c, stdout);
    }
    fclose(fout);
}