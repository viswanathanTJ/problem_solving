class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def enqueue(list, val):
    if list is None: return Node(val)
    t = list
    while t.next: t = t.next
    t.next = Node(val)
    return list

def deque(list):
    t = list
    list = list.next
    del t
    return list

def display(list):
    while list:
        print(list.val, end=' ')
        list = list.next
    print()

l = None
l = enqueue(l, 1)
l = enqueue(l, 2)
display(l)
l = deque(l)
display(l)