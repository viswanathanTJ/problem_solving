#include <stdio.h>
int main()
{
    char id[100];
    int cat;
    float r1, r2, diff, amt, tamt;
    scanf("%s %d %f %f", id, &cat, &r1, &r2);
    printf("Consumer ID-%s\n", id);
    diff = r2 - r1;
    if (cat == 1)
        amt = diff * 8;
    else
        amt = diff * 12.50;
    if (diff <= 100)
        tamt = amt + (amt * 0.18);
    else
    {
        amt = amt + (amt * 0.3);
        tamt = amt + (amt * 0.18);
    }
    printf("Total Amount with GST-%.2f", tamt);
}