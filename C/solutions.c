#include<stdio.h>
#include<stdlib.h>
#define max(a,b) a > b ? a : b
#define p printf

struct mystruct {
    int a, b;
    char s[100];
    struct mystruct *next;
}s1, s2;

typedef struct mystruct s;

typedef struct newStruct {
    int a;
} ns;

int main() {
    int a = 5, b = 10;
    p("%d\n", max(a, b));
    s s3[10], *s4;
    ns nn, n1, n2;
    // nn.a = 5;
    p("%d\n", nn.a);
    s s5;
    s1.a = 5;
    s3[0].a = 10;
    s1.next = (s *)malloc(sizeof(s));
    s1.next = s4;
    p("%d", s1.a);
}