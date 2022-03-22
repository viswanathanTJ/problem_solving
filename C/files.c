#include <stdio.h>
#include <string.h>
int main()
{
    char line[3];
    fgets(line, 3, stdin);
    printf("%d\n", line[2]);
    return 0;
}
