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

void pop(ll **n)
{
    ll *cur = *n;
    while (cur->next->next)
        cur = cur->next;
    cur->next = NULL;
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
    pop(&l);
    print(l);
}