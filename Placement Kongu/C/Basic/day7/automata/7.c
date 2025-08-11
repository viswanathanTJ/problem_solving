#include <stdio.h>
int main()
{
    char sing_ch;
    scanf("%c", &sing_ch);
    if ((sing_ch >= 'a' && sing_ch <= 'z') || (sing_ch >= 'A' && sing_ch <= 'Z'))
        printf("This is an alphabet.");
    else if (sing_ch >= '0' && sing_ch <= '9')
        printf("This is a digit.");
    else
        printf("This is a special character.");
}