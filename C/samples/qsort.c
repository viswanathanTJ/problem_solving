#include<stdio.h>

void swap(int *a, int*b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int ar[], int start, int end) {
    int pivot = ar[end];
    int pind = start;
    
    for (int i = start; i < end;i++)
        if(ar[i] <= pivot) 
            swap(&ar[i], &ar[pind++]);

    swap(&ar[end], &ar[pind]);
    return pind;
}

void qsort(int ar[], int start, int end) {
    if(start < end) {
        int pind = partition(ar, start, end);
        qsort(ar, start, pind - 1);
        qsort(ar, pind + 1, end);
    }
}

int main() {
    int arr[] = {3, 4, 2, 1, 5, 3, 7, 23};
    qsort(arr, 0, 8);
    for (int i = 0; i < 8;i++)
        printf("%d ", arr[i]);
}