#include<stdio.h>

int main() {
    int ar[] = {9, 3, 5, 6, 2, 1};
    int n = 6;
    int min_index;
    for (int i = 0; i < n;i++) {
        min_index = i;
        for (int j = i + 1; j < n;j++)
            if(ar[min_index] >= ar[j])
                min_index = j;
        int t = ar[i];
        ar[i] = ar[min_index];
        ar[min_index] = t;
    }
    for (int i = 0; i < n;i++)
        printf("%d ", ar[i]);
}