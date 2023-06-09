#include <stdio.h>

int main()
{
    int n, i;
    scanf("%d", &n);
    int a[n];
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    FILE *odd = fopen("odd.txt", "w+");
    FILE *even = fopen("even.txt", "w+");
    for (i = 0; i < n; i++)
        if (a[i] & 1)
            fprintf(odd, "%d ", a[i]);
        else
            fprintf(even, "%d ", a[i]);
    fseek(odd, 0, SEEK_SET);
    fseek(even, 0, SEEK_SET);
    while (fscanf(even, "%d", &n) == 1)
        printf("%d ", n);
    printf("\n");
    while (fscanf(odd, "%d", &n) == 1)
        printf("%d ", n);
    fclose(odd);
    fclose(even);
}