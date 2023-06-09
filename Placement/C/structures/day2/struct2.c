#include<stdio.h>

int main() {
    printf("Plain Egg-1.45\n");
    printf("Bacon and Egg-2.45\n");
    printf("Muffin-0.45\n");
    printf("French Toast-1.99\n");
    printf("Fruit Basket-2.49\n");
    printf("Cereal-0.69\n");
    printf("Coffee-0.50\n");
    printf("Tea-0.75\n");
    int n, q;
    float menu[] = {0, 1.45, 2.45, 0.45, 1.99, 2.49, 0.69, 0.50, 0.75};
    scanf("%d%d", &n, &q);
    float r = menu[n] * q;
    printf("%.2f", r + ((5 / 100.0) * r));
}