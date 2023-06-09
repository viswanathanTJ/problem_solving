class Parent:
    def m1(self, a):
        print('From parent m1()')
        print(a)

class Child:
    def m1(self, b):
        print('From child m1()')
        print(b)

a, b = map(int, input().split())
p = Parent()
c = Child()
p.m1(a)
c.m1(b)
