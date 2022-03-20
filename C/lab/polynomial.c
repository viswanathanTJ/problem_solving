#include<stdio.h>
#include<stdlib.h>

typedef struct node {
    int coeff, pow;
    struct node *next;
} poly;

void create(int coeff, int pow, poly **p) {
    poly *new = (poly *)malloc(sizeof(poly));
    new->coeff = coeff;
    new->pow = pow;
    new->next = NULL;
    if(*p == NULL)
        *p = new;
    else {
        poly *cur = *p;
        while(cur->next) 
            cur = cur->next;
        cur->next = (poly *)malloc(sizeof(poly));
        cur->next = new;
    }
}

poly* add(poly *p1, poly *p2) {
    poly *res = NULL;
    while(p1 && p2) {
        if(p1->pow > p2->pow) {
            create(p1->coeff, p1->pow, &res);
            p1 = p1->next;
        } else if (p2->pow > p1->pow) {
            create(p2->coeff, p2->pow, &res);
            p2 = p2->next;
        } else {
            create(p1->coeff + p2->coeff, p1->pow, &res);
            p1 = p1->next;
            p2 = p2->next;
        }
    }
    while(p1||p2) {
        if(p1) {
            create(p1->coeff, p1->pow, &res);
            p1 = p1->next;
        }
        if(p2) {
            create(p2->coeff, p2->pow, &res);
            p2 = p2->next;
        }
    }
    return res;
}

void display(poly* p) {
    poly *cur = p;
    while(cur->next) {
        printf("%d(x^%d) + ", cur->coeff, cur->pow);
        cur = cur->next;
    }
    printf("%d(x^%d)\n", cur->coeff, cur->pow);
}

int main() {
    poly *p1 = NULL, *p2 = NULL;
    create(2, 1, &p1);
    create(3, 2, &p1);
    create(4, 3, &p1);
    create(5, 3, &p1);
    create(10, 4, &p1);
    create(11, 5, &p1);
    create(5, 1, &p2);
    create(6, 2, &p2);
    create(7, 3, &p2);
    display(p1);
    display(p2);
    poly *res = add(p1, p2);
    display(res);
}

/*
int main()
{
    struct node* p1 = NULL, *p2 = NULL, *res = NULL;
    int cn,pn,n=1,poly,dp, choice;
    while(1)
    {
      printf("\n1.Add an Expression\n2.Add\n3.Display\n0.Exit\nEnter your choice: ");
      scanf("%d",&choice);
      switch(choice)
      {
        case 1:
            printf("\nEnter an Choice Polynomial 1 or 2:");
            scanf("%d",&poly);
            printf("\nEnter Cofficient: ");
            scanf("%d",&cn);
            printf("\nEnter Power: ");
            scanf("%d",&pn);
            if(poly==1)
                create(cn,pn,&p1);
            else if(poly==2)
                create(cn,pn,&p2);
            break;
        case 2:
            if(p1||p2) {
                res = add(p1, p2);
                display(res);
            } else
                printf("Polynomials are empty\n");
            break;
        case 3:
            printf("\n1.Display(p1)\n2.Display(p2)\n3.Diplay(res)\nEnter choice: ");
            scanf("%d",&dp);
            if(dp==1) {
                if(p1 != NULL)
                    display(p1);
                else
                    printf("Polynomial 1 is empty\n");
            }
            else if(dp==2)
                if(p2 != NULL)
                    display(p2);
                else
                    printf("Polynomial 2 is empty\n");
            else
                if(res != NULL)
                    display(res);
                else
                    printf("Addition is required\n");
            break;
        case 0:
            return 0;
        default:
            printf("\nInvalid Input\n");
      }
    }
    return 0;
}
*/