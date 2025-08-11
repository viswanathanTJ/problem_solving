class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def insert(list, val):
    if list is None: return Node(val)
    return Node(val, list)

def pop(list):
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
l = insert(l, 1)
l = insert(l, 2)
display(l)
l = pop(l)
display(l)  