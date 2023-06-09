#include<stdio.h>

int main() {
    int n,i,j,t,of=1,ef=1,oc=1,ec=1;
    scanf("%d", &n);
    // n = 4;
    int a[n];
    // int a[] = {2,5,4,6};
    for(i=0;i<n;i++) scanf("%d", &a[i]);

    for(i=0;i<n;i++)
        for(j=i+1;j<n;j++)
            if(a[i] > a[j]) {
                t = a[i];
                a[i] = a[j];
                a[j] = t;
            }

    for(i=n-1;i>-1;i--) {
        if(a[i]%2 == 0) 
            if(ef) ef = 0;
            else {
                ec--;
                printf("Second largest even number %d ", a[i]);
                break;
            }
    }
    for(i=0;i<n;i++) {
        if(a[i]&1) 
            if(of) of = 0;
            else {
                oc--;
                printf("\nSecond smallest odd number %d ", a[i]);
                break;
            }
    }
    if(oc) printf("\nNo second smallest odd number available.");
    if(ec) printf("\nNo second largest even number available.");
}