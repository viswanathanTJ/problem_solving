#include<stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int arr[20];
    int t = n, i=0;
    while(t!=0) {
        arr[i++] = t % 10;
        t /= 10;
    }
    for (int j = 0; j < i;j++)
        for (int k = j + 1; k < i;k++)
            if(arr[j] > arr[k]) {
                t = arr[j];
                arr[j] = arr[k];
                arr[k] = t;
            }
    int res = 0;
    for (int j = 0; j < i;j++)
        res = (res * 10) + arr[j];
    printf("%d", res);

    return 0;
}