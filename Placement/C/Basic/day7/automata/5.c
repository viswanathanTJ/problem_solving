// You are using GCC
#include <stdio.h>
int main()
{
    int chk_year;
    scanf("%d", &chk_year);
    if ((chk_year % 400) == 0)
        printf("%d is a leap year.", chk_year);
    else if ((chk_year % 100) == 0)
        printf("%d is a not leap year.", chk_year);
    else if ((chk_year % 4) == 0)
        printf("%d is a leap year.", chk_year);
    else
        printf("%d is not a leap year.", chk_year);
}