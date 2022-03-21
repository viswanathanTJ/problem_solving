#include<stdio.h>
#define MAX 20

int q[MAX], f = -1, r = -1;

void enque(int n) {
    if(r == MAX-1)
        printf("Overflow\n");
    else {
        if(f==-1)
            f = 0;
        q[++r] = n;
        printf("Inserted\n");
    }
}
void deque() {
    if(f == -1)
        printf("Underflow\n");
    else
        printf("dequed %d\n", q[f++]);
}
void peek() {
    if(f==-1)
        printf("Queue empty\n");
    else
        printf("%d\n", q[f]);
}
void display() {
    if(f==-1)
        printf("Queue empty\n");
    else {
        for (int i = f; i <= r;i++)
            printf("%d ", q[i]);
    }
}

int main() {
    enque(5);
    enque(10);
    enque(15);
    enque(20);
    enque(25);
    deque();
    display();
}