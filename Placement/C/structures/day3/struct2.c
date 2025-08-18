#include<stdio.h>

struct temp {
    int h;
    float hh;
};

int main() {
    struct temp t, t1;
    scanf("%d %f", &t.h, &t.hh);
    scanf("%d %f", &t1.h, &t1.hh);
    printf("%d' - %f\"", t.h+t1.h, t.hh+t1.hh);
}