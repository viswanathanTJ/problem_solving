// Coding challenges are tests sent to potential employees by a company typically to serve as a zero or first round interview to get initial technical / coding signal on candidates.They are most often given to new graduates or interns, but anyone may be subject to a coding challengewelcome to C programming

#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *fp;
    char c;
    fp = fopen("input.txt", "w");
    fprintf(fp, "Coding challenges are tests sent to potential employees by a company typically to serve as a zero or first round interview to get initial technical/coding signal on candidates. They are most often given to new graduates or interns, but anyone may be subject to a coding challenge");
    fclose(fp);
    fp = fopen("input.txt", "a");
    char s[100];
    gets(s);
    fprintf(fp, "%[^\n]s", s);
    // fscanf(stdin, ())
    fputs(s, fp);
    fclose(fp);
}