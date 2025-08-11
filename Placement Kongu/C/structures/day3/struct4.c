#include <stdio.h>

struct temp
{
    int a,b;
};

int main()
{
    struct temp s;
    scanf("%d %d", &s.a, &s.b);
    printf("%d and %d lies in quadrant ");
    if(s.a > 0 && s.b > 0)
        printf("1");
    else if(s.a > 0 && s.b < 0)
        printf("2");
    else if(s.a < 0 && s.b < 0)
        printf("3");
    else if(s.a > 0 && s.b > 0)
        printf("4");
}