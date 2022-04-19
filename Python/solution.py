class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right = None, None
    
def insert(root, val):
    if not root:
        return TreeNode(val)
    elif root.val > val:
        root.left = insert(root.left, val)
    elif root.val < val:
        root.right = insert(root.right, val)
    return root

# l = [6,5,7,8,9,3]
l = [3,1,2]
root = None
for x in l:
    root = insert(root, x)

def bfs(root):
    q = []
    q.append(root)
    while q:
        cur = q.pop(0)
        if cur:
            print(cur.val, end=' ')
            if not cur.left and not cur.right:
                continue
            if cur.left: q.append(cur.left)
            else: q.append(None)
            if cur.right: q.append(cur.right)
            else: q.append(None)
        else:
            print(None, end=' ')
                

bfs(root)

curleft = float('inf')
curright = float('-inf')

done = 1
def solution(node, less, great):
    global done
    if less and node.val < less.val:
        node.val, less.val = less.val, node.val
        done = 1
    if great and node.val > great.val:
        node.val, great.val = great.val, node.val
        done = 1
    if not done and node.left:
        solution(node.left, less, node)
    if not done and node.right: 
        solution(node.right, node, great)

while done:
    done = 0
    solution(root, None, None)
print()
bfs(root)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=' ')
        inorder(root.right)
# inorder(root)