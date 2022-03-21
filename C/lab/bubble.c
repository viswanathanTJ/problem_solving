#include <stdio.h>

int main()
{
    int arr[] = {3, 5, 6, 2, 1};
    int n = 5;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                int t = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = t;
            }
        }
    }
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
}