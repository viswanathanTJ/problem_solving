class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, val):
        if self.head is None: 
            self.head = Node(val)
            return
        new = Node(val)
        new.next = self.head
        self.head = new
    
    def pop(self):
        if self.head is None: return
        cur = self.head
        print('Popped:', cur.val)
        self.head = self.head.next
        del cur

    def show(self):
        if self.head is None: return
        cur = self.head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()

stack = Stack()
print('Stack using Linked List')
print('-'*20)
while True:
    print('1.Push\n2.Pop\n3.Show\n4.Exit')
    choice = input('Enter your choice:')
    match choice:
        case '1':
            val = input('Enter the value to push: ')
            stack.push(val)
        case '2':
            stack.pop()
        case '3':
            stack.show()
        case '4':
            break
        case _:
            print('Invalid choice')
    print()
    print('-'*20)
    print()