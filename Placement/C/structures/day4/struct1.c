#include <stdio.h>
#include <stdlib.h>

struct arrays
{
    int n, *arr, cap;
};

int main()
{
    int i, t, val;
    struct arrays a, b, merge;
    scanf("%d", &a.n);
    a.arr = (int *)malloc(a.n * sizeof(int));
    for (i = 0; i < a.n; i++)
        scanf("%d", a.arr + i);
    scanf("%d", &a.cap);
    scanf("%d", &b.n);
    b.arr = (int *)malloc(b.n * sizeof(int));
    for (i = 0; i < b.n; i++)
        scanf("%d", (b.arr + i));
    merge.n = a.n + b.n;
    merge.arr = (int *)malloc(merge.n * sizeof(int));
    for (i = 0; i < a.n; i++)
        *(merge.arr + i) = *(a.arr + i);
    for (i = a.n, t = 0; t < b.n; i++, t++)
        *(merge.arr + i) = *(b.arr + t);
    for (i = 0; i < merge.n; i++)
        printf("%d ", *(merge.arr + i));
    scanf("%d %d", &t, &val);
    *(a.arr + t) = val;
    scanf("%d", &t);
    printf("\n%d \n", *(a.arr + (t)));
    for (i = 0; i < a.n; i++)
        printf("%d ", *(a.arr + i));
    printf("\n");
    for (i = a.n - 1; i >= 0; i--)
        printf("%d ", *(a.arr + i));
    printf(" ");
}