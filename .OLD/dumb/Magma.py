import numpy as np

from abc import ABC,abstractmethod
from itertools import product
from typing import Any

class AbsMagmaElement(ABC):
    def __init__(self,*pars):
        self._pars = pars

    @property
    @abstractmethod
    def parameters(self):
        return self._pars

    def __eq__(self,othr):
        return all(s==o for s,o in zip(self._pars,othr._pars))

class AbsFlattenedMagmaElement(AbsMagmaElement):
    @property
    @abstractmethod
    def _flatten_par(self,n,par): return

    @property
    def flattened_parameters(self):
        return (self._flatten_par(i,par) for i,par in enumerate(self.parmeters))

    def __eq__(self,othr):
        return all(s==o for s,o in zip(self.flattened_parameters,othr.flattened_parameters))

class AbsMagmaAlgebra(ABC):
    @classmethod
    @abstractmethod
    def op(cls,a,b): return

    @classmethod
    @abstractmethod
    def _emtpy(cls,arg):
        return arg

    def _is_associative(cls,a,b,c):
        return cls.op(a,cls.op(b,c))==cls.op(cls(a,b),c)

    def _is_communative(cls,a,b):
        return cls.op(a,b)==cls,op(b,a)

    def _is_idempotent(cls,a):
        return a==cls.op(a,a)

    def _is_left_absorbative(cls,a,b):
        return a==cls.op(a,b)

    def _is_right_absorbative(cls,a,b):
        return b==cls.op(a,b)

class AbsQuasigroupAlgebra(AbsMagmaAlgebra):
    @classmethod
    @abstractmethod
    def ldiv(cls,a,b): return

    @classmethod
    @abstractmethod
    def rdiv(cls,a,b): return

class AbsUnitalMagmaAlgebra(AbsMagmaAlgebra):
    @property
    @abstractmethod
    def get_identity(self): return

class AbsLoopAlgebra(AbsUnitalMagmaAlgebra,AbsQuasigroupAlgebra):
    @classmethod
    def get_inverse(cls,a):
        return cls.ldiv(a,cls.get_identity())

class AbsMagmaSet(ABC):
    @property
    @abstractmethod
    def elements(self): return

    def __getitem__(self,key):
        return next(el for i,el in enumerate(self.elements) if i==key)

class AbsMappedMagmaSet(AbsMagmaSet):
    @abstractmethod
    def trans(self,*args): return

    def __call__(self,*args):
        return self.trans(*args)

    def __getitem__(self,key):
        return self.trans(super(AbsMappedMagmaSet,self).__getitem__(key))
