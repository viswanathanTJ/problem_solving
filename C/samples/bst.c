#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    struct Node *left;
    struct Node *right;
    int val;
} node;

// node *create(int val)
// {
//     node *newnode = (node *)malloc(sizeof(node));
//     newnode->val = val;
//     newnode->left = NULL;
//     newnode->right = NULL;
//     return newnode;
// }
void add(node **root, int val)
{
    node *newnode = (node *)malloc(sizeof(node));
    newnode->val = val;
    newnode->left = NULL;
    newnode->right = NULL;
    if (*root == NULL)
        *root = newnode;
    else
    {
        node *cur = *root;
        if(cur->val > val)
            add(&cur->left, val);
        else if(cur->val < val)
            add(&cur->right, val);
        else
            printf("%d already present in tree\n", val);
    }
}

int search(node *root, int val)
{
    if (root == NULL)
        return 0;
    if (root->val == val)
        return 1;
    return (val < root->val) ? search(root->left, val) : search(root->right, val);
}

void preorder(node *root)
{
    if (root == NULL)
        return;
    printf("%d ", root->val);
    preorder(root->left);
    preorder(root->right);
}

void inorder(node *root)
{
    if (root == NULL)
        return;
    inorder(root->left);
    printf("%d ", root->val);
    inorder(root->right);
}

void postorder(node *root)
{
    if (root == NULL)
        return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->val);
}


int main()
{
    node *root = NULL;
    add(&root, 100);
    add(&root, 500);
    add(&root, 200);
    add(&root, 600);
    add(&root, 20);
    add(&root, 30);
    // add(&root, 25);
    add(&root, 10);
    preorder(root);
    printf("\n");
    postorder(root);
    printf("\n");
    inorder(root);
    printf("\n");
    printf("%s", search(root, 10) ? "[*] Found\n" : "[-] Not found\n");
    // print(root);
}

// int main()
// {
//     node *root = NULL;
//     int num;
//     int ch;
//     while (1)
//     {
//         printf("\n1.Insert\n2.Search\n3.Preorder\n4.Inorder\n5.Postorder\n0.Exit\nEnter choice : ");
//         scanf("%d", &ch);
//         switch (ch)
//         {
//             case 1:
//                 printf("\nEnter element: ");
//                 scanf("%d", &num);
//                 add(&root, num);
//                 printf("\n[+] Inserted\n");
//                 break;
//             case 2:
//                 printf("\nEnter element: ");
//                 scanf("%d", &num);
//                 printf("%s", search(root, num) ? "[*] Found\n" : "[-] Not found\n");
//                 break;
//             case 3:
//                 printf("\nPREORDER : ");
//                 preorder(root);
//                 break;
//             case 4:
//                 printf("\nINORDER : ");
//                 inorder(root);
//                 break;
//             case 5:
//                 printf("\nPOSTORDER : ");
//                 postorder(root);
//                 break;
//             case 0:
//                 exit(0);
//             default:
//                 printf("\nInvalid Input\n");
//                 break;
//         }
//     }
//     return 0;
// }

// int main()
// {
//     node *root = NULL;
//     add(&root, 100);
//     add(&root, 500);
//     add(&root, 200);
//     add(&root, 600);
//     add(&root, 20);
//     add(&root, 30);
//     // add(&root, 25);
//     add(&root, 10);
//     printLevelOrder(root);
// }

// int main()
// {
//     node *root = NULL;
//     int num;
//     int ch;
//     while (1)
//     {
//         printf("\n1.Insert\n2.Search\n3.Preorder\n4.Inorder\n5.Postorder\n0.Exit\nEnter choice : ");
//         scanf("%d", &ch);
//         switch (ch)
//         {
//             case 1:
//                 printf("\nEnter element: ");
//                 scanf("%d", &num);
//                 add(&root, num);
//                 printf("\n[+] Inserted\n");
//                 break;
//             case 2:
//                 printf("\nEnter element: ");
//                 scanf("%d", &num);
//                 printf("%s", search(root, num) ? "[*] Found\n" : "[-] Not found\n");
//                 break;
//             case 3:
//                 printf("\nPREORDER : ");
//                 preorder(root);
//                 break;
//             case 4:
//                 printf("\nINORDER : ");
//                 inorder(root);
//                 break;
//             case 5:
//                 printf("\nPOSTORDER : ");
//                 postorder(root);
//                 break;
//             case 0:
//                 exit(0);
//             default:
//                 printf("\nInvalid Input\n");
//                 break;
//         }
//     }
//     return 0;
// }
