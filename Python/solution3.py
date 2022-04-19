from mimetypes import init

from idna import valid_contextj


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right = None, None
    
l = [3, 4,32,41,23,12]
def insert(root, val):
    if root is None:
        return TreeNode(val)
    elif root.val < val:
        root.right = insert(root.right, val)
    elif root.val > val:
        root.left = insert(root.left, val)
    return root
root = None
for i in l:
    root = insert(root, i)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)
inorder(root)