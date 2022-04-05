#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i;
    scanf("%d", &n);
    int *a = (int *)malloc(sizeof(int));
    int arr[n], c;
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    printf("Memory successfully allocated using malloc.\n");
    int p = arr[0];
    arr[0] = arr[0] + arr[1];
    for (i = 1; i < n - 1; i++)
    {
        c = arr[i];
        arr[i] = p + arr[i + 1];
        p = c;
    }
    arr[n - 1] = p + arr[n - 1];
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
}