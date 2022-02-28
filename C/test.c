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

int height(node *root)
{
    if (root == NULL)
        return 0;
    int left = height(root->left);
    int right = height(root->right);
    return (left > right) ? left + 1 : right + 1;
}

int _print(node *root, int is_left, int offset, int depth, char s[20][255])
{
    char b[20];
    int width = 5;

    if (!root)
        return 0;

    sprintf(b, "(%03d)", root->val);

    int left = _print(root->left, 1, offset, depth + 1, s);
    int right = _print(root->right, 0, offset + left + width, depth + 1, s);

    for (int i = 0; i < width; i++)
        s[depth][offset + left + i] = b[i];

    if (depth && is_left)
    {
        for (int i = 0; i < width + right; i++)
            s[depth - 1][offset + left + width / 2 + i] = '-';

        s[depth - 1][offset + left + width / 2] = '.';
    }
    else if (depth && !is_left)
    {
        for (int i = 0; i < left + width; i++)
            s[depth - 1][offset - width / 2 + i] = '-';

        s[depth - 1][offset + left + width / 2] = '.';
    }

    return left + width + right;
}

void print(node *tree)
{
    char s[20][255];
    for (int i = 0; i < 20; i++)
        sprintf(s[i], "%80s", " ");

    _print(tree, 0, 0, 0, s);
    int h = height(tree);
    for (int i = 0; i < h; i++)
        printf("%s\n", s[i]);
}

int main() {
    node *root = NULL;
    add(&root, 80);
    add(&root, 70);
    add(&root, 90);
    add(&root, 100);
    // add(&root, 120);
    // add(&root, 85);
    // add(&root, 95);
    // add(&root, 60);
    // add(&root, 75);
    // add(&root, 50);
    // add(&root, 65);
    print(root);
}