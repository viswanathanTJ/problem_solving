#include <stdio.h>

int dp[50], counts = 0;

int fib(int n)
{
    if (n <= 1)
        return n;
    if (dp[n] != 0)
        return dp[n];

    dp[n] = fib(n - 1) + fib(n - 2);
    return dp[n];
}

void checkValue(int n, int value)
{
    while (n > 0)
    {
        if (n % 10 == value)
            counts++;
        n /= 10;
    }
}

int main()
{
    // printf("%d ", fib(40));
    int value, start, end;
    printf("Enter value: ");
    scanf("%d", &value);
    printf("Enter start value: ");
    scanf("%d", &start);
    printf("Enter end value: ");
    scanf("%d", &end);
    // value = 8; start = 3000; end = 5000;
    int temp = 0, i = 0;
    while (temp <= end)
    {
        temp = fib(i++);
        if (temp >= start && temp <= end)
        {
            printf("%d ", temp);
            checkValue(temp, value);
        }
    }
    printf("\nCounts are: %d", counts);
    return 0;
}