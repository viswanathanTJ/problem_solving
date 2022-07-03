#include <stdio.h>

int main()
{
    int arr[] = {3, 4, 2, 1, 5, 3, 7, 23};
    int n = 8;
    for(int i=0; i<n; i++) {
        int max = i;
        for(int j=i+1;j<n;j++)
            if(arr[i] < arr[j])
                max = j;
        if(max != i) {
            int temp = arr[i];
            arr[i] = arr[max];
            arr[max] = temp;
        }
    }
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    // int min_index;
    // for (int i = 0; i < 8; i++)
    // {
    //     int key = arr[i];
    //     int j = i;
    //     while(key < arr[j-1] && j > 0) {
    //         arr[j] = arr[j-1];
    //         j--;
    //     }
    //     arr[j] = key;
    // }
    // for (int i = 1; i < 8; i++)
    // {
    //     int key = arr[i];
    //     int j = i - 1;
    //     while(key < arr[j] && j >= 0)
    //         arr[j + 1] = arr[j--];
    //     arr[j + 1] = key;
    // }
    for (int i = 0; i < 8; i++)
        printf("%d ", arr[i]);
}