// Write a program to find the total expenses including the discount.Given the ticket cost as 'X'.If the number of tickets purchased is less than 50, there is no discount.If the number of tickets purchased is between 50 and 100(both inclusive), then 10 % discount is offered.If the number of tickets purchased is between 101 and 200(both inclusive), 20 % discount is offered.If the number of tickets purchased is between 201 and 400(both inclusive), 30 % discount is offered.If the number of tickets purchased is between 401 and 500(both inclusive), 40 % discount is offered.If the number of tickets purchased is greater than 500, then 50 % discount is offered.

#include<stdio.h>

int main() {
    int cost, n;
    scanf("%d %d", &cost, &n);
    switch(n) {
        case 1 ... 49:
            break;
        case 50 ... 99:
            cost -= (cost*0.1);
            break;
        case 101 ... 200:
            cost -= (cost*0.2);
            break;
        case 201 ... 400:
            cost -= (cost*0.3);
            break;
        case 401 ... 500:
            cost -= (cost*0.4);
            break;
        default:
            cost -= (cost*0.5);
    }
    printf("%d.00", cost*n);
}