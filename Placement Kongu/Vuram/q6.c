#include<stdio.h>

int dp[20] = {0};

int fib(int n) {
    if(n <= 1 ) return n;
    if(dp[n]) return dp[n];
    dp[n] = fib(n-1) + fib(n+2);
    return dp[n];
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", fib(n+1));
}