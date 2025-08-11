#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

int main()
{
    int c, i, j, t, n, a[(int)10e9], b[(int)10e9];
    scanf("%d", &t);
    while(t-- > 0) {
        c = 0;
        scanf("%d", &n);
        for(i=0; i<n;i++)
            scanf("%d", &a[i]);
        for(i=0; i<n;i++)
            scanf("%d", &b[i]);
        for(i=0;i<n;i++)
            for(j=i+1;j<n;j++)
                if(a[i] == b[j])
                    c++;
                else if(a[j] == b[i])
                    c++;
        printf("%d\n", c);
    }
    
}