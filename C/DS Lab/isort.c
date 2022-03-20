#include <stdio.h>

int main()
{
    int arr[] = {3, 4, 2, 1, 5, 3, 7, 23};
    int min_index;
    for (int i = 1; i < 8; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while(key < arr[j] && j >= 0) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j - 1] = key;
    }
    for (int i = 0; i < 8; i++)
        printf("%d ", arr[i]);
}