#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

void getMissingNumber(int *arr, int len) {
    int i, j;

    for(i=0;i<len;i++) 
        for(j=i; j<len; j++)
            if(arr[i] > arr[j])
                arr[i] = arr[j] + arr[i] - (arr[j] = arr[i]);
                
    int diff = arr[0] - 0;
    for (i = 0; i < len; i++)
        if (arr[i] - i != diff)
            while (diff < arr[i] - i)
            {
                printf("%d ", i+diff);
                diff++;
            }
}

int main() {
    int *arr, result, len, i;
    scanf("%d", &len);
    arr = (int*)malloc(sizeof(int));
    for(i=0;i<len;i++)
        scanf("%d", &arr[i]);
    getMissingNumber(arr, len);
}