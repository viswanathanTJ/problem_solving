#include <stdio.h>
#include <stdlib.h>

typedef struct BST
{
    int val;
    struct BST *left, *right;
} node;

void add(node **root, int val)
{
    if (*root == NULL)
    {
        node *newnode = (node *)malloc(sizeof(node));
        newnode->val = val;
        newnode->left = NULL;
        newnode->right = NULL;
        *root = newnode;
    }
    else
    {
        node *cur = *root;
        (cur->val > val) ? add(&cur->left, val) : 
            (cur->val < val) ? add(&cur->right, val)
                : printf("%d already present in tree\n", val);
    }
}

int search(node *root, int val) {
    if(root == NULL)
        return 0;
    if(root->val == val)
        return 1;
    return (val < root->val) ? search(root->left, val) :
        search(root->right, val);
}

void inorder(node *root) {
    if(root == NULL)
        return;
    inorder(root->left);
    printf("%d ", root->val);
    inorder(root->right);
}

void preorder(node *root) {
    if(root==NULL)
        return;
    printf("%d ", root->val);
    preorder(root->left);
    preorder(root->right);
}

void postorder(node *root) {
    if(root==NULL)
        return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->val);
}

int height(node *root) {
    if(root==NULL)
        return 0;
    int left = height(root->left);
    int right = height(root->right);
    return (left > right) ? left + 1 : right + 1;
}

void printCurrentLevel(node *root, int level) {
    if(root==NULL) {
        printf("   ");
        return;
    }
    if(level==1)
        printf("%d ", root->val);
    else if(level > 1) {
        printCurrentLevel(root->left, level - 1);
        int th = height(root);
        // printf("th=%d lev=%d\n", th, level);
        for (int i = 0; i < th-level;i++)
            printf(" ");
        printf("   ");
        printCurrentLevel(root->right, level - 1);
    }
}

void printBST(node *root) {
    int h = height(root);
    for (int i = 1; i <= h;i++) {
        for (int j = 0; j < h - i;j++)
            printf("   ");
        printCurrentLevel(root, i);
        printf("\n");
    }
}

int main() {
    node *root = NULL;
    add(&root, 80);
    add(&root, 70);
    add(&root, 90);
    add(&root, 60);
    add(&root, 75);
    add(&root, 50);
    add(&root, 65);
    printBST(root);
}