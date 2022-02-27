#include <stdio.h>
#include <stdlib.h>
int main()
{
    int t, n=5;
    int oddc = 0, evenc = 0;
    // int *numbers = NULL;
    int *arr, *odd = NULL, *even = NULL;
    arr = malloc(n * sizeof(int));
    odd = malloc(n * sizeof(int));
    even = malloc(n * sizeof(int));
    for (int i = 1; i < n;i++) {
        // scanf("%d", &t);
        t = i + 13;
        if(t&1) {
            
            // oddc++;
            // odd = (int *)realloc(odd, oddc * sizeof(int));
            // odd[oddc - 1] = t;
        } else {
            evenc++;
            even = (int *)realloc(even, evenc * sizeof(int));
            even[evenc - 1] = t;
        }
    }
    for (int i = 0; i < oddc;i++)
        printf("%d ", *(odd + i));
    printf("\n");
    for (int i = 0; i < evenc;i++)
        printf("%d ", *(even + i));

    return 0;
}