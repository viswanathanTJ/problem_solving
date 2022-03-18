#include <stdio.h>
#define p(n) printf("Num is %d", n);
#define s scanf
struct rec
{
    int x, y, z;
};
int main()
{
    // p(6);
    int a;
    s("%d", &a);
    p(a)
    return 0;
}