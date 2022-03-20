#include <stdio.h>
#include <stdlib.h>
#define SIZE 10
int arr[SIZE];
int front = -1;
int rear = -1;
void enque();
void deque();
void show();

int main()
{
    int ch;
    while (1)
    {
        printf("\n1.Enque\n2.Deque\n3.Show\n4.Exit\n");
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
            show();
            break;
        case 4:
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
        rear += 1;
        arr[rear] = num;
    }
}

void deque()
{
    if (front == -1 || front > rear)
        printf("\nUnderflow\n");
    else
    {
        printf("\nDequed %d", arr[front]);
        front += 1;
    }
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
