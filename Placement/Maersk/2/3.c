#include<stdio.h>
int uni(int v){
    int r,s=1;
    while(v>0){
        r=v%10;
        s*=r;
        v=v/10;
    }
    return s;
}
int main(){
    int c[1000]={0};
    int n,i; scanf("%d",&n);
    int q=0;
    int a[n],b[n];
    for(i=0;i<n;i++)    scanf("%d",&a[i]);
    for(i=0;i<n;i++){
        b[i]=uni(a[i]);
        c[b[i]]++;
        if(c[b[i]]==1) { q++; c[b[i]]=3;
        }
    }
    printf("%d",q);
}