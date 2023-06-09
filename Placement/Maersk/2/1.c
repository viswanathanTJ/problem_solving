#include<stdio.h>

int main(){
    long long int b[100000]={0},f=0;
    long long int s,i,k=0,j; scanf("%lld",&s);
    long long int a[s],m[100];
    for(i=0;i<s;i++) scanf("%lld",&a[i]);
    for(i=0;i<s;i++) b[a[i]]++;
    for(i=0;i<s;i++)    
        if(b[a[i]]==1)
    m[k++]=a[i];
    for(i=0;i<k;i++){
        for(j=i+1;j<k;j++)
            if(m[i]>m[j]){
                int t=m[i];
                m[i]=m[j];
                m[j]=t;
            }
    }
    for(i=0;i<k;i++)
        printf("%lld ",m[i]);
}