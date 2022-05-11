#include <stdio.h>
#include <string.h>
void decode(char seq[], int n)
{
    int stk[n + 1];
    int top = -1;
    for (int i = 0; i <= n; i++)
    {
        stk[++top] = (i + 1);
        if (i == n || seq[i] == 'I')
            while (top >= 0)
            {
                printf("%d", stk[top]);
                top--;
            }
    }
}

int main()
{
    char seq[8];
    scanf("%s", seq);
    decode(seq, strlen(seq));
    return 0;
}