class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def insert_at_begin(list, val):
    if list is None: return Node(val)
    return Node(val, list)

def insert_at_end(list, val):
    if list is None: return Node(val)
    t = list
    while list.next:
        list = list.next
    list.next = Node(val)
    return t

def insert_at_mid(list, val):
    t = list
    slow = get_mid(list)
    nl = Node(val, slow.next)
    slow.next = nl
    return t

def delete_at_begin(list):
    t = list
    ret = list.next
    del t
    return ret

def delete_at_end(list):
    t = list
    while list.next and list.next.next: list = list.next
    del list.next
    list.next = None
    return t

def delete_at_mid(list):
    t = list    
    slow = get_mid(list)
    rm = slow.next
    slow.next = slow.next.next
    del rm
    return t

def get_mid(list):
    if list is not None:
        slow, fast = list, list
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

def print_list(list):
    while list:
        print(list.val, end=' ')
        list = list.next
    print()

list = None
list = insert_at_begin(list, 2)
list = insert_at_begin(list, 1)
print_list(list)
list = insert_at_mid(list, 0)
print_list(list)
list = delete_at_begin(list)
print_list(list)
list = delete_at_end(list)
print_list(list)
# list = insert_at_end(list, 3)
# list = insert_at_end(list, 5)
# print_list(list)
# list = insert_at_mid(list, 0)
# list = insert_at_end(list, 4)
# print_list(list)
# list = delete_at_mid(list)
# print_list(list)