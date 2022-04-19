#include<stdio.h>

int main() {
    char s[] = "aabbc";
    int a[26] = {0};
    for(int i=0;s[i]!='\0';i++) {
        if(a[s[i]-97] == 0)
            printf("%c", s[i]);
        a[s[i]-97]++;
    }
}