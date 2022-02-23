#include <stdio.h>
#include <stdlib.h>

void sum(int a, int b) {
    printf("| %d |\n", a + b);
}

void fun(void(*p)(int, int), int a, int b) {
    printf("------\n");
    sum(a, b);
    printf("------\n");
}   

int main() {
    fun(sum, 15, 20);
}