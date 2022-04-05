#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);

    printf("the arithmetic operators result is %d %d %d %d\n", a + b, a - b, a * b, a / b);
    printf("the relational operators result is %d %d %d %d\n", a > b, a < b, a >= b, a <= b);
    printf("the logical operators result is %d %d %d %d\n", a && b, a || b, a != b, 43);
    printf("the increment operator result is %d %d %d %d\n", a++, ++a, b++, ++b);
    printf("the decrement operator result is %d %d %d %d\n", a--, --a, b--, --b);
    printf("the bitwise AND operator result is %d\n", a & b);
    printf("the bitwise OR operator result is %d\n", a | b);
    printf("the bitwise NOT operator result is %d ", a ^ b);
}