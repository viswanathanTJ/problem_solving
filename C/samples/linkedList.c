#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int val;
    struct Node *next;
} ll;

void add(ll **n, int val)
{
    ll *new = (ll *)malloc(sizeof(ll));
    new->val = val;
    new->next = NULL;
    if (*n == NULL)
        *n = new;
    else
    {
        ll *cur = *n;
        while (cur->next)
            cur = cur->next;
        cur->next = new;
    }
}

void rm(ll **n)
{
    ll *del = *n;
    *n = del->next;
    free(del);
}

void rm_by_index(ll *n, int index)
{
    ll *temp = n;
    if (index == 0)
    {
        n = n->next;
        temp->next = NULL;
        free(temp);
    }
    else
    {
        for (int i = 0; i < index - 1; i++)
            temp = temp->next;
        ll *del = temp->next;
        temp->next = temp->next->next;
        printf("\nElement deleted is : %d\n", del->val);
        free(del);
    }
    return;
}

void print(ll *n)
{
    ll *cur = n;
    while (cur)
    {
        printf("%d ", cur->val);
        cur = cur->next;
    }
}

int main()
{
    ll *l = NULL;
    add(&l, 5);
    add(&l, 4);
    add(&l, 3);
    add(&l, 2);
    add(&l, 1);
    print(l);
    rm(&l);
    printf("\n");
    print(l);
    rm_by_index(l,1);
    printf("\n");
    print(l);
}