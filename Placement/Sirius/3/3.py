class Parent:
    def add(a, b):
        return a+b
    pass
class Child1(Parent):
    def sub(a, b):
        return a-b
    pass
class Child2(Child1):
    def mul(a, b):
        return a*b
    pass
if __name__=='__main__':
    a, b = int(input()), int(input())
    c = Child2
    print(c.add(a, b))
    print(c.sub(a, b))
    print(c.mul(a, b))
