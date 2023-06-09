#include <stdio.h>
#include <math.h>

struct com
{
    float r, i;
};

int main()
{
    struct com a, b, m, d;
    scanf("%f %f %f %f", &a.r, &a.i, &b.r, &b.i);
    m.r = a.r * b.r - a.i * b.i;
    m.i = a.r * b.i + b.r * a.i;
    d.r = (a.r * b.r + a.i * b.i) / (b.r * b.r + b.i * b.i);
    d.i = (a.i * b.r - a.r * b.i) / (b.r * b.r + b.i * b.i);
    printf("Sum = %.2f + %.2fi\n", a.r + b.r, a.i + b.i);
    printf("Difference = %.2f + %.2fi\n", a.r - b.r, a.i - b.i);
    printf("Product = %.2f + %.2fi\n", m.r, m.i);
    printf("Division = %.2f + %.2fi\n", d.r, d.i);
    printf("Modulus of first complex number = %.2f\n", sqrt((a.r*a.r)+(a.i*a.i)));
    printf("Modulus of first complex number = %.2f\n", sqrt((b.r*b.r)+(b.i*b.i)));
}