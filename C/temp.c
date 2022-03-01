#include <stdio.h>
#include <stdlib.h>

void display(int arr[], int n);
void searching(int arr[], int n, int val);
void insert(int arr[], int n, int cap, int index, int val);
void sort(int arr[], int n);
void delete (int *arr, int n, int index);

struct arrays
{
    int n, *arr, cap;
};

int main()
{
    int i, index, val;
    struct arrays a;
    scanf("%d", &a.n);
    int del_arr[a.n], sort_arr[a.n];
    a.arr = (int*)malloc(a.n * sizeof(int));
    for (i = 0; i < a.n; i++)
    {
        scanf("%d", a.arr + i);
        del_arr[i] = *(a.arr + i);
        sort_arr[i] = *(a.arr + i);
    }
    
    scanf("%d", &a.cap);
    scanf("%d", &val);
    searching(a.arr, a.n, val);
    sort(sort_arr, a.n);

    scanf("%d %d", &index, &val);
    insert(a.arr, a.n, a.cap, index, val);
    scanf("%d", &index);
    delete(del_arr, a.n, index);
}

void searching(int arr[], int n, int val)
{
    int f = 1;
    for (int i = 0; i < n; i++)
        if (arr[i] == val)
        {
            printf("%d is found at index %d\n", val, i);
            f = 0;
        }
    if (f)
        printf("%d is not found in array\n", val);
}

void insert(int arr[], int n, int cap, int index, int val)
{
    if (n + 1 >= cap)
    {
        n++;
        arr = (int*)realloc(arr, n * sizeof(int));
        for (int i = n; i >= index; i--)
            arr[i] = arr[i - 1];
        arr[index - 1] = val;
        display(arr, n);
    }
    else
        printf("Cant insert element because capacity is full\n");
}

void display(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void sort(int arr[], int n)
{
    int t;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (arr[i] > arr[j])
            {
                t = arr[i];
                arr[i] = arr[j];
                arr[j] = t;
            }
    display(arr, n);
}

void delete (int arr[], int n, int index)
{
    for (int i = index-1; i < n; i++)
        arr[i] = arr[i+1];
    display(arr, n - 1);
}