#include <stdio.h>
int a(int n)
{
    int m = n % 10;
    int v;
    while (n > 0)
    {
        v = n % 10;
        n = n / 10;
        if (n == 0)
            break;
    }
    return m + v;
}

int b(int n)
{
    int m = 0;
    int t = n;
    while (n > 0)
    {
        m = m * 10 + n % 10;
        n = n / 10;
    }
    if (t == m)
        return 1;
    else
        return 0;
}

int d(int n)
{
    int m = 0;
    while (n > 0)
    {
        m = m * 10 + n % 10;
        n = n / 10;
    }
    return m;
}
int c(int n)
{
    int co = 0;
    while (n > 0)
    {
        co++;
        n = n / 10;
    }
    return co;
}

int main()
{
    char v;
    int n, m, k;
    int t = 1000;
    char n1[10][100] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    scanf("%d %c", &n, &v);

    if (v == 'a' || v == 'A')
    {
        m = a(n);
        printf("Sum of first and last digit: %d", m);
    }
    else if (v == 'b' || v == 'B')
    {
        if (b(n))
            printf("Palindrome");
        else
            printf("Not palindrome");
    }
    else if (v == 'c' || v == 'C')
    {
        m = c(n);
        printf("Number of Digits: %d", m);
    }
    else if (v == 'd' || v == 'D')
    {
        m = d(n);
        while (m > 0)
        {
            k = m % 10;
            printf("%s ", n1[k]);
            m = m / 10;
        }
    }
    switch (0)
    {
    }
}