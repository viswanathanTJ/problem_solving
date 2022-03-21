#include <stdio.h>

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int main()
{
    int arr[] = {3, 4, 2, 1, 5, 3, 7, 23};
    int min_index;
    for (int i = 0; i < 8;i++) {
        min_index = i;
        for (int j = i+1; j < 8;j++) {
            if(arr[min_index] >= arr[j])
                min_index = j;
        }
        swap(&arr[min_index], &arr[i]);
    }
    for (int i = 0; i < 8; i++)
        printf("%d ", arr[i]);
}