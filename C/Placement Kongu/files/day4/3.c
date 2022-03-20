#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *fs1, *fs2, *ft, *fout;
    fs1 = fopen("input1.txt", "w");
    fs2 = fopen("input2.txt", "w");
    fprintf(fs1, "It is a robust language with rich set of built-in functions and operators that can be used to write any complex program.");
    fprintf(fs2, "The C compiler combines the capabilities of an assembly language with features of a high-level language.");
    fclose(fs1);
    fclose(fs2);

    fout = fopen("output.txt", "w");
    fs1 = fopen("input1.txt", "r");
    fs2 = fopen("input2.txt", "r");
    char ch;
    while ((ch = fgetc(fs1)) != EOF)
        fputc(ch, fout);
    while ((ch = fgetc(fs2)) != EOF)
        fputc(ch, fout);
    fclose(fout);
    fclose(fs1);
    fclose(fs2);

    fout = fopen("output.txt", "r");
    while ((ch = getc(fout)) != EOF)
    {
        printf("%c", ch);
    }
    return 0;
}