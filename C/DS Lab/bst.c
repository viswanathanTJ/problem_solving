#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    struct Node *left;
    struct Node *right;
    int val;
} node;

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
}