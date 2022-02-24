#include <stdio.h>
#include <stdlib.h>

void sum(int a, int b) {
    printf("| %d |\n", a + b);
}

void sub(int a, int b) {
    printf("| %d |\n", a - b);
}

void fun(void(*p)(int, int)) {
    printf("------\n");
    int a = 2, b = 3;
    p(4, 10);
    printf("------\n");
}   

int main() {
    // fun(sum, 15, 20);
    fun(sum);
    fun(sub);
}