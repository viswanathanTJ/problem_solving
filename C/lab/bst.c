#include<stdio.h>
#include<stdlib.h>

typedef struct bst
{
    struct bst *left;
    struct bst *right;
    int val;
}node;

void add(node **root, int val) {
    node *new = (node *)malloc(sizeof(node));
    new->val = val;
    new->left = NULL;
    new->right = NULL;
    if(*root == NULL)
        *root = new;
    else {
        node *cur = *root;
        (cur->val < val) ? add(&cur->right, val) : add(&cur->left, val);
    }
}

int search(node *root, int n) {
    if(root == NULL)
        return 0;
    if(root->val == n)
        return 1;
    return (root->val < n) ? search(root->right, n) : search(root->left, n);
}

void preorder(node *root) {
    if(root == NULL)
        return;
    printf("%d ", root->val);
    preorder(root->left);
    preorder(root->right);
}
void postorder(node *root) {
    if(root == NULL)
        return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->val);
}
void inorder(node *root) {
    if(root == NULL)
        return;
    inorder(root->left);
    printf("%d ", root->val);
    inorder(root->right);
}

int main() {
    node *bst = NULL;
    add(&bst, 5);
    add(&bst, 10);
    add(&bst, 4);
    add(&bst, 15);
    add(&bst, 3);
    int n = 5;
    printf("%s\n", search(bst, n) ? "[+] Found" : "[-] Not found");
    preorder(bst);
    printf("\n");
    postorder(bst);
    printf("\n");
    inorder(bst);
}