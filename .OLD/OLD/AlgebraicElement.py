from typing import  TypeVar,NewType,Union,\
                    Iterable,Iterator,Generator,Tuple,List,Dict,\
                    Callable,Any
from Base   import  Pars_t,Elem_t,Set_t,Alg_t,Magma_t,Group_t
from abc    import  ABC,abstractmethod

class AbsAlgebraicElement(ABC):
    @abstractmethod
    def __value__(self,*pars:Pars_t) -> Elem_t: ...

    @abstractmethod
    def __pars__(self) -> Tuple[Pars_t]: ...

class AbsMagmaElement(AbsAlgebraicElement):
    @abstractmethod
    def __magma_operator__(self,othr) -> Elem_t: ...

    def __add__(self,othr):
    if self.is_additive:
        return self.__magma_operator__(self,othr)
    return raise NotImplementedError

    def __mul__(self,othr) -> Elem_t:
    if self.is_multiplicative:
        return self.__magma_operator__(self,othr)
    return raise NotImplementedError

    @property
    @abstractmethod
    def is_additive_magma(self) -> bool: ...

    @is_additive_magma.setter
    @abstractmethod
    def is_additive_magma(self,tf) -> bool: ...

    @property
    @abstractmethod
    def is_multiplicative_magma(self) -> bool: ...

    @is_multiplicative_magma.setter
    @abstractmethod
    def is_multiplicative_magma(self,tf) -> bool: ...

class AbsGroupElement(AbsMagmaElement):

class AbsRingElement(AbsMagmaElement):
    @abstractmethod
    def __magma_operator__(self,othr) -> Elem_t: ...

    @abstractmethod
    def __ring_operator__(self,othr) -> Elem_t: ...

    def __mul__(self,othr) -> Elem_t:
        return self.__magma_operator__(self,othr)
 
    def __add__(self,othr) -> Elem_t:
        return self.__ring_operator__(self,othr)
