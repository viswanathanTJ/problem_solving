#include <stdio.h>
#include <stdlib.h>

struct node
{
    struct node *left;
    struct node *right;
    int val;
};
// Insert Element
void add(struct node **root, int val)
{
    if (*root == NULL) {
        struct node *newnode = (struct node *)malloc(sizeof(struct node));
        newnode->val = val;
        newnode->left = newnode->right = NULL;
        *root = newnode;
    }
    else
    {
        struct node *cur = *root;
        (cur->val > val) ? add(&cur->left, val) : (cur->val < val) ? add(&cur->right, val) : printf("%d already present in tree\n", val);
    }
}

// Search element
int search(struct node *root, int val)
{
    if (root == NULL) return 0;
    if (root->val == val) return 1;
    return (val < root->val) ? search(root->left, val) : search(root->right, val);
}

// Print BST
int height(struct node* node)
{
    if (node == NULL)
        return 0;
    else {
        int left = height(node->left);
        int right = height(node->right);
        return (left > right) ? left+1 : right+1;
    }
} 
void printCurrentLevel(struct node* root, int level)
{
    if (root == NULL)
        return;
    if (level == 1)
        printf("%d", root->val);
    else if (level > 1) {
        printCurrentLevel(root->left, level - 1);
        printf("   ");
        printCurrentLevel(root->right, level - 1);
    }
}
void print(struct node* root)
{
    for (int i = 1; i <= height(root); i++) {
        printCurrentLevel(root, i);
        printf("\n");
    }
}
 

int main()
{
    struct node *root = NULL;
    int num, ch;
    while (1)
    {
        printf("\n1.Insert\n2.Search\n3.Print\n0.Exit\nEnter choice : ");
        scanf("%d", &ch);
        switch (ch)
        {
            case 1:
                printf("\nEnter element to insert: ");
                scanf("%d", &num);
                add(&root, num);
                break;
            case 2:
                printf("\nEnter element to search: ");
                scanf("%d", &num);
                printf("%s", search(root, num) ? "[*] Found\n" : "[-] Not found\n");
                break;
            case 3:
                print(root);
                break;
            case 0:
                return 0;
            default:
                printf("\nInvalid Input\n");
                break;
        }
    }
    return 0;
}