class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert(head, val):
    new = Node(val)
    if not head: return new
    else:
        cur = head
        while cur.next:
            cur = cur.next
        cur.next = new
    return head

def pprint(k, head, n):
    cur, temp = head, head
    for i in range(k-1):
        cur = cur.next
    while cur:
        print(cur.val, end=' ')
        cur = cur.next
    for i in range(k-1):
        print(temp.val, end=' ')
        temp = temp.next

head = None
n, l, k = int(input()), list(map(int, input().split())), int(input())

for i in l:
    head = insert(head, i)

pprint(k, head, n)