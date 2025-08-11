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
    int arr[] = {69,14,59,18,25,81,35,12};
    qsort(arr, 0, 7);
    for (int i = 0; i < 8;i++)
        printf("%d ", arr[i]);
}