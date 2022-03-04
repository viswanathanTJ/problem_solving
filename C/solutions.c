#include <stdio.h>
#include <stdlib.h>
int main()
{
    int *arr, *crr;
    arr = malloc(2 * sizeof(int));
    crr = calloc(2, sizeof(int));
    printf("arr[0]= %d\narr[1]=%d\n", *(arr), *(arr + 1));
    printf("arr[0]= %d\narr[1]=%d\n", *(crr), *(crr + 1));
    int a = 5;
    printf("arr[2]=%d\n", *(arr + 2));
    printf("crr[2]=%d\n", *(crr + 2));
    printf("After realloc\n");
    // arr = 

    return 0;
}