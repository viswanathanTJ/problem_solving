from random import shuffle

class Node:
    def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
    
l = list(range(10, 15))
shuffle(l)
print(l)
tree = None
def insert(root, val):
    if root is None:
        return Node(val)
    elif root.val > val:
        root.left = insert(root.left, val)
    elif root.val < val:
        root.right = insert(root.right, val)
    return root

for x in l:
    tree = insert(tree, x)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

print('inorder')
inorder(tree)

def level_order(root):
    if root is None:
        return
    q = []
    q.append(root)
    while q:
        for _ in range(len(q)):
            cur = q.pop(0)
            print(cur.val, end=' ')
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        print()

print('\nlevel order')
level_order(tree)