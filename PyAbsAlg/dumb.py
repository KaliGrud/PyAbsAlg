from abc import ABC,abstractmethod

class A(ABC):
    def f(self):
        raise NotImplementedError

class B(A):
    pass

class C(B):
    def f(self):
        print("Yo!")
try:
    b = B()
    b.f()
except NotImplementedError:
    print("that didn't work")
    c = C()
    c.f()

