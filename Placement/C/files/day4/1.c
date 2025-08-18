#include <stdio.h>

int main()
{
    int n, i, j;
    char c;
    scanf("%d", &n);
    FILE *fp = fopen("input.txt", "w+");
    for (j = 2, i = 0; i < n - 1; i++, j++)
    {
        fprintf(fp, "%d %d %d\n", j, j * j, j * j * j);
    }
    fclose(fp);

    fp = fopen("input.txt", "r");
    while ((c = getc(fp)) != EOF)
        printf("%c", c);
    fclose(fp);
    return 0;
}