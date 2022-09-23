from typing import TypeVar,NewType,Tuple,Generator,Any,Union
from Base import AlephNumber,Aleph0,Aleph1
from abc import ABC,abstractmethod

el_t    = TypeVar('el_t') 
pars_t  = TypeVar('pars_t') 
card_t  = NewType('card_t',Union[int,AlephNumber])

class AbsMagmaAlgebra(ABC):
    @abstractmethod
    def __elements__(self,*args: pars_t) -> Generator[el_t,Any,Any]:
        """
        Returns generator which yield magma elements according to <args>
        """
        ...

    @abstractmethod
    def __operation__(self,a: el_t,b: el_t) -> el_t:
        """
        Returns the magma operation between two elements, i.e. a*b
        """
        ...

    @property
    @abstractmethod
    def __cardinality__(self) -> card_t:
        """
        Returns cardinality of the magma's set
        """
        ...

    def elements(self,*args: pars_t) -> Generator[el_t,Any,Any]:
        """
        Returns generator which yields magma elements accoding to <args>
        """
        return self.__elements__(*args)

    def get_elements(self,*args: pars_t) -> Tuple[el_t]:
        """
        Returns tuple of magma elements according to <args>
        """
        return tuple(self.__elements__(*args))

    def is_a_idempotent(self,a: el_t) -> bool:
        """
        Returns if an element is idempotent, i.e. a = a*a
        """
        return a==self(a,a)

    def is_ab_left_absorbing(self,a: el_t,b: el_t) -> bool:
        """
        Returns if a*b is left absorbing, i.e. a = a*b
        """
        return a==self(a,b)

    def is_ab_right_absorbing(self,a: el_t,b: el_t) -> bool:
        """
        Returns if a*b is right absorbing, i.e. b = a*b
        """
        return b==self(a,b)

    def is_ab_communative(self,a: el_t,b: el_t) -> bool:
        """
        Returns if a*b is communative, i.e. a*b = b*a
        """
        return self(a,b)==self(b,a)

    def is_abc_associative(self,a: el_t,b: el_t,c: el_t) -> bool:
        """
        Returns is a*b*c is associative, i.e. (a*b)*c = a*(b*c)
        """
        return self(self(a,b),c)==self(a,self(b,c))

    def __call__(self,a: el_t,b: el_t) -> el_t:
        """
        Returns binary magma operation between two inputs, i.e. a*b
        """
        return self.__operation__(a,b)
