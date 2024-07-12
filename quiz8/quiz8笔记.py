class A:
    def __init__(self, a):
        self.a = a
class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def modify(self):
        self.b += 10
I = A(10)
print(I.a)
J = B(I, 40)
print(J.a.a, J.b) #J.a -->I ,J.a.a --> I.a --> 10
J.modify()
print(J.b)

def f(a, b, c, *x, d=10, e=20, f=30, **y): # *x-->tuple **y-->dict
    print(a, b, c, x, d, e, f, y)
f(1, 2 ,3, 4, 5, 6, g=40, h=50)

class TwoElementSetError(Exception):
    pass

class TwoElementSet:
    def __init__(self, a, b):
        if a == b:
            raise TwoElementSetError('Set members should be distinct')
        self.a = a
        self.b = b
        

class CircularList:
    def  __init__ (self, values):
        self.values = values
    def __len__(self):
        return len(self.values)
    def __repr__(self):
        return f'CircularList({self.values})'
    def __str__(self):
        return '--'.join(str(e) for e in self.values)
cl = CircularList([1, 2, 3])
print(cl)
