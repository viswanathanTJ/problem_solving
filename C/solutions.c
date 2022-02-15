#include <stdio.h>
int recur(int num);
int main()
{
    int arr[] = {7, 2, 4, 1, 5, 3};
    for (int i = 1; i < 6; i++)
    {
        int hole = i;
        int value = arr[i];
        while (hole > 0 && arr[hole-1] > value)
        {
            arr[hole] = arr[hole-1];
            hole--;
        }
        arr[hole] = value;
    }
    for (int i = 0; i < 6; i++)
        printf("%d ", arr[i]);
    return 0;
}