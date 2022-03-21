#include <stdio.h>
#include <stdlib.h>

#define MAX 100
int arr[MAX];
int top = -1;

void push(int n)
{
    if (top == MAX - 1)
        printf("\nStack is full");
    else
        arr[++top] = n;
}

void pop()
{
    if (top == -1)
        printf("\nArray is empty");
    else
        printf("\nPopped element %d", arr[top--]);
}

void peek()
{
    if (top == -1)
        printf("\nStack is empty");
    else
        printf("\nPeek element is %d", arr[top]);
}

void display()
{
    if (top == -1)
        printf("\nStack is empty");
    else
    {
        for (int i = top; i >= 0; i--)
            printf("%d ", arr[i]);
    }
}

int main()
{
    while (1)
    {
        printf("\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit\n");
        int ch, num;
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            printf("\nEnter element:");
            scanf("%d", &num);
            push(num);
            break;
        case 2:
            pop();
            break;
        case 3:
            peek();
            break;
        case 4:
            display();
            break;
        case 5:
            exit(0);
        }
    }
    return 0;
}
