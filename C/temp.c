#include <stdio.h>

int main()
{
    int r, m1, m2, m3;
    scanf("%d %d %d %d", &r, &m1, &m2, &m3);
    int c1 = 0, c2 = 0, c3 = 0;
    int n1 = 0, n2 = 0, n3 = 0;
    int t1 = 25 - m1;
    int t2 = 120 - m2;
    int t3 = 12 - m3;
    while (r > 0)
    {
        c1++;
        if (n1 == 0 && c1 == t1)
        {
            r += 20;
            r--;
            n1 = t1 + 25;
        }
        else if (c1 == n1)
        {
            n1 += 25;
            r += 20;
            r--;
        }
        else
        {
            r--;
            if (r == 0)
                break;
        }
        c2++;
        if (n2 == 0 && c2 == t2)
        {
            r += 80;
            r--;
            n2 = t2 + 120;
        }
        else if (c2 == n2)
        {
            n2 += 120;
            r += 80;
            r--;
        }
        else
        {
            r--;
            if (r == 0)
                break;
        }
        c3++;
        if (c3 == t3 && n3 == 0)
        {
            r += 8;
            r--;
            n3 = t3 + 12;
        }
        else if (c3 == n3)
        {
            n3 += 12;
            r += 8;
            r--;
        }
        else
        {
            r--;
            if (r == 0)
                break;
        }
    }
    printf("Peter plays %d times before going broke", c1 + c2 + c3);

    return 0;
}