#include <stdio.h>

char GetCoinState(char state, int n) {
    if(state == 'H' && n % 2)
        return 'T';
    else if(state == 'T' && n % 2)
        return 'H';
    else
        return state;
}

int main(void)
{
    int n;
    char state;
    state = getchar();
    scanf("%d", &n);
    char result = GetCoinState(state, n);
    printf("%c", result);
    return 0;
}
