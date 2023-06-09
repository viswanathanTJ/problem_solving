#include <stdio.h>
#include <stdlib.h>

struct bank
{
    int id, rs;
    char name[50], city[50], dob[10];
};

int main()
{
    int n, i, index, action, amt;
    scanf("%d", &n);
    struct bank p[n];
    printf("Accounts created for the customers\n");
    for (i = 0; i < n; i++)
    {
        scanf("%d %s %s %[^ ]s", &p[i].id, p[i].name, p[i].city, p[i].dob);
        scanf("%d", &p[i].rs);
        printf("%d %s %s %s %d.00\n", p[i].id, p[i].name, p[i].city, p[i].dob, p[i].rs);
    }
    scanf("%d", &index);
    printf("\nCustomer details for the given account number\n");
    for (i = 0; i < n; i++)
        if (p[i].id == index)
            printf("%d %s %s %s %d.00\n", p[i].id, p[i].name, p[i].city, p[i].dob, p[i].rs);
    scanf("%d %d %d", &action, &index, &amt);
    for (i = 0; i < n; i++)
        if (p[i].id == index)
        {
            if (action == 1)
            {
                printf("\nAmount deposited\n");
                printf("%d %s %s %s %d.00", p[i].id, p[i].name, p[i].city, p[i].dob, p[i].rs + amt);
            }
            else
            {
                if (p[i].rs - amt >= 500)
                {
                    printf("\nAmount withdraw\n");
                    printf("%d %s %s %s %d.00", p[i].id, p[i].name, p[i].city, p[i].dob, p[i].rs - amt);
                }
                else
                    printf("\nYou have to maintain a minimum balance of Rs.500");
            }
        }
}