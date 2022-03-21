#include<stdio.h>
#include<stdlib.h>

struct Node {
    int val;
    struct Node *next;
} *top = NULL;

void append(int n) {
    struct Node *new = (struct Node *)malloc(sizeof(struct Node));
    new->val = n;
    if(top == NULL)
        new->next = NULL;
    else
        new->next = top;
    top = new;
    printf("Inserted\n");
}

void pop() {
    if(top == NULL)
        printf("Underflow\n");
    else {
        struct Node *temp = top;
        printf("Popped element is %d\n", temp->val);
        top = temp->next;
        free(temp);
    }
}

void display() {
    if(top != NULL) {
        struct Node *cur = top;
        while(cur) {
            printf("%d ", cur->val);
            cur = cur->next;
        }
    }
}

int main() {
    append(5);
    append(10);
    append(15);
    append(20);
    append(25);
    pop();
    display();
}