#include <stdio.h>
#include <string.h>
int main()
{
    char a[100];
    int sum = 0;
    scanf("%[^\n]s", a);
    for (int i = 0; i < strlen(a); i++)
    {
        if (a[i] == 'Q' || a[i] == 'Z')
            sum += 10;
        else if (a[i] == 'J' || a[i] == 'X')
            sum += 8;
        else if (a[i] == 'K')
            sum += 5;
        else if (a[i] == 'F' || a[i] == 'H' || a[i] == 'V' || a[i] == 'W' || a[i] == 'Y')
            sum += 4;
        else if (a[i] == 'B' || a[i] == 'C' || a[i] == 'M' || a[i] == 'P')
            sum += 3;
        else if (a[i] == 'D' || a[i] == 'G')
            sum += 2;
        else if (a[i] == ' ')
            sum += 0;
        else
            sum += 1;
    }
    printf("%d", sum);
}