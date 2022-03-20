#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    struct Node *left;
    struct Node *right;
    int val;
}node;

void add(node **root, int val)
{
    if (*root == NULL){
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
            (cur->val < val) ? add(&cur->right, val) : 
                printf("%d already present in tree\n", val);
    }
}

int search(node *root, int val)
{
    if (root == NULL)
        return 0;
    if (root->val == val)
        return 1;
    return (val < root->val) ? 
        search(root->left, val) : search(root->right, val);
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

// Print Level Order

int height(node *node)
{
    if (node == NULL)
        return 0;
    else
    {
        int left = height(node->left);
        int right = height(node->right);
        return (left > right) ? left + 1 : right + 1;
    }
}
void printCurrentLevel(node *root, int level, int h)
{
    if (root == NULL)
        return;
    if (level == 1)
        printf("%d ", root->val);
    else if (level > 1)
    {
        int mid = ((h&1) ? h+1 : h) / 2;
        printCurrentLevel(root->left, level - 1, h);
        int th = height(root);
        // 2nd level center space
        if (mid == level && h == th)
            printf("   ");
        for (int i = 0; i < h - level; i++)
            printf("   ");
        printCurrentLevel(root->right, level - 1, h);
    }
}

void print(node *root)
{
    int h = height(root);
    printf("Height is %d\n", h);
    int i, j;
    for (i = 1; i <= h; i++)
    {
        for (j = 0; j < h - i; j++)
            printf("   ");
        if(i==1)
            printf(" ");
        printCurrentLevel(root, i, h);
        printf("\n");
    }
}

int front = 0, rear = -1;
int queue[20];
void bfs_traverse(node *root)
{
    int val = root->val;
    if ((front <= rear) && (root->val == queue[front]))
    {
        // printf("f = %d rear = %d\n", front, rear);
        if (root->left != NULL) {

            queue[++rear] = root->left->val;
        }
        if (root->right != NULL) {
            queue[++rear] = root->right->val;
            // printf("%d \n", root->right->val);
        }
        front++;
    }
    if (root->left != NULL)
        bfs_traverse(root->left);
    if (root->right != NULL)
        bfs_traverse(root->right);
}

void printbfs(node *root) {
    queue[++rear] = root->val;
    bfs_traverse(root);
    for (int i = 0; i < rear;i++)
        printf("%d -> ", queue[i]);
    printf("%d\n", queue[rear]);
}

int main()
{
    node *root = NULL;
    add(&root, 100);
    add(&root, 500);
    add(&root, 200);
    // add(&root, 600);
    add(&root, 20);
    add(&root, 30);
    // add(&root, 25);
    add(&root, 10);
    // add(&root, 9);
    // add(&root, 11);
    // add(&root, 40);
    print(root);
    printf("\n");
    // queue[++rear] = root->val;
    printbfs(root);
    // bfs_traverse(root);
    // for (int i = 0; i <= rear; i++)
    //     printf("%d -> ", queue[i]);
    // bfs_traverse(root);
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
