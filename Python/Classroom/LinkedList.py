from this import d


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_first(self, val):
        self.length += 1
        if self.head is None: self.head = Node(val); return
        new = Node(val)
        new.next = self.head
        self.head = new
        print('Inserted first node')

    def insert_at_index(self, val, index):
        if index == 0:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next and index > 1:
            cur = cur.next
            index -= 1
        new = Node(val)
        new.next = cur.next
        cur.next = new

    def insert_middle(self, val):
        if self.length == 1:
            self.insert_last(val)
            return
        self.insert_at_index(val, self.length//2)
        self.length += 1
        print('Inserted middle node')
    
    def insert_last(self, val):
        self.length += 1
        if self.head is None:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
    
    def delete_first(self):
        if self.head is None: return
        self.length -= 1
        print('Deleted first node:', self.head.val)
        del self.head
        self.head = self.head.next

    def delete_middle(self):
        if self.head is None: return
        mid = self.length//2
        cur = self.head
        while cur.next and mid > 1:
            cur = cur.next
            mid -= 1
        temp = cur.next
        print('Deleted middle node:', temp.val)
        cur.next = cur.next.next
        del temp

    def delete_last(self):
        if self.head is None: return
        self.length -= 1
        cur = self.head
        if cur.next is None:
            print('Deleted last node:', cur.val)
            del cur.next
            self.head = None
            return
        while cur.next and cur.next.next:
            cur = cur.next
        print('Deleted last node:', cur.next.val)
        temp = cur.next
        cur.next = None
        del temp
    
    def show(self):
        if self.head is None: return
        cur = self.head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print()
    
ll = LinkedList()
print('Linked List')
print('-'*20)
while True:
    print('1.Insert first\n2.Insert at position\n3.Insert middle\n4.Insert last\n5.Delete first\n6.Delete middle\n7.Delete last\n8.Show\n9.Exit')
    choice = input('Enter your choice:')
    match choice:
        case '1':
            val = input('Enter the value to insert: ')
            ll.insert_first(val)
        case '2':
            val = input('Enter the value to insert: ')
            index = int(input('Enter the index to insert: '))
            ll.insert_at_index(val, index)
        case '3':
            val = input('Enter the value to insert: ')
            ll.insert_middle(val)
        case '4':
            val = input('Enter the value to insert: ')
            ll.insert_last(val)
        case '5':
            ll.delete_first()
        case '6':
            ll.delete_middle()
        case '7':
            ll.delete_last()
        case '8':
            ll.show()
        case '9':
            break
        case _:
            print('Invalid choice')
    print()
    print('-'*20)
    print()