from abc import ABC,abstractmethod

class MagmaElement(object):
    def __init__(self,algebra,*pars):
        self.algebra = algebra
        self.pars = pars

    def __mul__(self,othr):
        return self.algebra._mul(self,othr)

class UnitalMagmaElement(MagmaElement):
    def is_identity(self):
        return self==self*self

class QuasigroupElement(MagmaElement):
    def __truediv__(self,othr):
        """
        Right Division: a = x*b <==> x = a/b
                   <==> x = cls.__truediv__(a,b) <==> x = a*cls.inv(b)
        """
        return self.algebra._rdiv(self,othr)

    def __floordiv__(self,othr):
        """
        Left Division: a = b*x <==> x = a//b
                  <==> x = cls.__floordiv__(a,b) <==> x = cls.inv(b)*a
        """
        return self.algebra._ldiv(self,othr)

class LoopElement(UnitalMagmaElement,QuasigroupElement):
    @property
    def inv(self):
        return self.algebra._inv(self)

class AbsMagma(ABC):
    """
    Abstract base class for a magma
        Defines:
            - binary operator ( _mul )
    """
    @classmethod
    @abstractmethod
    def _mul(cls,lhs: MagmaElement,rhs :MagmaElement) -> MagmaElement: return

    @classmethod
    def is_idempotent(cls,el):
        return el==cls._mul(el,el)

class AbsUnitalMagma(AbsMagma):
    """
    Abstract class for a unital magma
        Defines:
            - indentity element ( e ) 
    """
    @classmethod
    def is_identity(cls,el):
        return el==cls._mul(el,el)

    @classmethod
    @abstractmethod
    def _id(cls): return

class AbsQuasigroup(AbsMagma):
    @classmethod
    @abstractmethod
    def _ldiv(cls,lhs,rhs): return

    @classmethod
    @abstractmethod
    def _rdiv(cls,lhs,rhs): return

class AbsLoop(AbsQuasigroup,AbsUnitalMagma):
    @classmethod
    @abstractmethod
    def _inv(cls,el): return

