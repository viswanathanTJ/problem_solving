class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def enque(self, val: int):
        if self.head is None:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)

    def deque(self):
        if self.head is None: return None
        cur = self.head
        self.head = self.head.next
        print('Dequed:', cur.val)
        del cur
    
    def show(self):
        if self.head is None: return
        cur = self.head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print()

queue = Queue()
print('Queue using Linked List')
print('-'*20)
while True:
    print('1.Enque\n2.Deque\n3.Show\n4.Exit')
    choice = input('Enter your choice:')
    match choice:
        case '1':
            val = input('Enter the value to enque: ')
            queue.enque(val)
        case '2':
            queue.deque()
        case '3':
            queue.show()
        case '4':
            break
        case _:
            print('Invalid choice')
    print()
    print('-'*20)
    print()