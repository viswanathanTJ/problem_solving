#include <stdio.h>

int bs(int a[], int low, int high, int x)
{
    int mid = (low + high) / 2;
    if (low > high)
        return -1;
    if (a[mid] == x)
        return mid;
    return (a[mid] < x) ? bs(a, mid + 1, high, x) : bs(a, low, mid, x);
}
int main()
{
    int n, i, x;
    printf("Enter array size:");
    scanf("%d", &n);
    printf("Enter array elemnts\n");
    int a[n];
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("\nEnter search element: ");
    scanf("%d", &x);
    int p = bs(a, 0, n - 1, x);
    if (p < 0)
        printf("\nNot found");
    else
        printf("\n%d found at index %d", x, p);

    return 0;
}
