#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* get_sequence(char* str)
{
    int n = strlen(str);
    if(n > 9)
        return "String length exceed the given limit";
    else if(n==0) 
        return "String not found";
    int stk[n + 1], top = -1, ind = 0;
    char *ret = malloc(n);
    for (int i = 0; i <= n; i++)
    {
        stk[++top] = (i + 1);
        if (i == n || str[i] == 'I')
            while (top >= 0)
                ret[ind++] = stk[top--]+'0';
    }
    ret[ind] = '\0';
    return ret;
}

int main()
{
    char seq[8];
    scanf("%s", seq);
    printf("%s",get_sequence(seq));
    return 0;
}