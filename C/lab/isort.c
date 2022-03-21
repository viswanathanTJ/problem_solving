#include<stdio.h>

int main() {
    int arr[] = {3, 5, 6, 2, 1};
    int n = 5;
    int key, j;
    for (int i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while(key <= arr[j] && j >= 0)
            arr[j + 1] = arr[j--];
        arr[j + 1] = key;
    }
    for (int i = 0; i < n;i++)
        printf("%d ", arr[i]);
}