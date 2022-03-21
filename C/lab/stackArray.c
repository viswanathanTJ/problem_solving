#include<stdio.h>
#define MAX 20

int stack[MAX], top = -1;

void push(int n) {
    if(top==MAX-1)
        printf("Overflow\n");
    else {
        stack[++top] = n;
        printf("Inserted\n");
    }
}
void pop() {
    if(top==-1)
        printf("Underflow\n");
    else {
        printf("Popped element is %d\n", stack[top--]);
    }
}
void peek() {
    if(top==-1)
        printf("Stack is empty\n");
    else
        printf("%d\n", stack[top]);
}
void show() {
    if(top==-1)
        printf("Stack is empty\n");
    else {
        for (int i = top; i >= 0;i--)
            printf("%d ", stack[i]);
    }
}
int main() {
    push(5);
    push(10);
    push(15);
    push(20);
    push(25);
    peek();
    pop();
    show();
}