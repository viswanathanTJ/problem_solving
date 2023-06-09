#include <stdio.h>
#include <math.h>
int main()
{
    float p, r, c;
    int t, i;
    scanf("%f%f", &p, &r);
    scanf("%d", &t);
    for (i = 1; i <= t; i++)
    {
        c = (p * (pow((1 + r / 100), i)));
        printf("Year %d = %.2f\n", i, c);
    }
}