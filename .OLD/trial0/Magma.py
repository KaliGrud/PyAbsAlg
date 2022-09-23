from abc import ABC,abstractmethod

class AbsMagma(ABC):
    @abstractmethod
    def op(self,a,b): return

    def is_idempotent(self,a):
        return a==self.op(a,a)

class AbsUnitalMagma(AbsMagma):
    @abstractmethod
    def get_identity(self): return

class AbsQuasigroup(AbsMagma):
    @abstractmethod
    def rdiv(self,a,b): return

    @abstractmethod
    def ldiv(self,a,b): return

class AbsLoop(AbsUnitalMagma,AbsQuasigroup):
    @abstractmethod
    def inv(self,a,b): return

class AbsSemigroup(AbsMagma):
    def is_associative(self): return True

class AbsMonoid(AbsUnitalMagma,AbsSemigroup): pass

