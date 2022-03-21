#include<stdio.h>

void swap(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int start, int end) {
    int pivot = arr[end];
    int pind = start;
    for (int i = start; i < end;i++) {
        if(arr[i] <= pivot)
            swap(&arr[i], &arr[pind++]);
    }
    swap(&arr[end], &arr[pind]);
    return pind;
}

void qsort(int arr[], int start, int end) {
    if(start < end) {
        int pind = partition(arr, start, end);
        qsort(arr, start, pind - 1);
        qsort(arr, pind + 1, end);
    }
}

int main() {
    int arr[] = {3, 4, 6, 2, 1, 7};
    int n = 7;
    qsort(arr, 0, 7);
    for (int i = 0; i < n;i++)
        printf("%d ", arr[i]);
}

