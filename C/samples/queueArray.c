#include <stdio.h>
#include <stdlib.h>
#define SIZE 10
int arr[SIZE];
int front = -1, rear = -1;
void enque();
void deque();
void peek();
void show();

int main()
{
    int ch;
    while (1)
    {
        printf("\n1.Enque\n2.Deque\n3.Peek\n4.Show\n5.Exit\n");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            enque();
            break;
        case 2:
            deque();
            break;
        case 3:
            peek();
            break;
        case 4:
            show();
            break;
        case 5:
            exit(0);
        }
    }
    return 0;
}

void enque()
{
    if (rear == SIZE - 1)
        printf("\nOverflow\n");
    else
    {
        int num;
        if (front == -1)
            front = 0;
        printf("\nEnter number to push: ");
        scanf("%d", &num);
        arr[++rear] = num;
    }
}

void deque()
{
    if (front == -1 || front > rear)
        printf("\nUnderflow\n");
    else
        printf("\nDequed %d", arr[front++]);
}

void peek() {
    if(front == -1)
        printf("\nQueue is empty\n");
    else
        printf("Peek element is: %d\n", arr[front]);
}
void show()
{
    if (front == -1)
        printf("\nEmpty Queue\n");
    else
    {
        for (int i = front; i <= rear; i++)
            printf("%d ", arr[i]);
    }
}
