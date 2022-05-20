def simple():
    print('Im simple')

def param(a):
    print('Parameter is', a)

def retme(a):
    return a

def retlist(l: list) -> list:
    return l

def rettuple(t: tuple) -> tuple:
    return t

def retdict(d: dict) -> dict:
    return d

def retfun(a):
    return retme(a)

def mulret(a, b):
    return a, b

simple()
param(1)
print(retme(12))
print(retlist([1,2,3]))
print(rettuple((1,2,3)))
print(retdict({'name': 'viswa', 'rno': '119'}))
print(retfun(1))
print(mulret(1, 2))