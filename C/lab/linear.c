#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < n; i++)
        if (t == arr[i])
        {

            printf("%d found at index %d", t, i);
            return 0;
        }
    printf("%d is not found");
}