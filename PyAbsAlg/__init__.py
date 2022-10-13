import sys,functools,itertools

from abc    import  ABC,abstractmethod
from typing import  TypeVar,NewType,Union,Optional,Literal,\
                    Container,Hashable,Sized,Callable,\
                    Iterable,Iterator,Generator,Mapping,\
                    Sequence,Tuple,MutableSequence,List,\
                    NoReturn,Any

####################################
#           TypeHinting            #
####################################

Pars__t = TypeVar("Pars__t")

Alg__x = TypeVar("Alg__x")
Alg__o = Optional[Alg__x]
Alg__f = Callable[[...],Alg__o]
Alg__t = Union[Alg__f,Alg__o]
Alg__e = Union[Alg__t,NoReturn]

Elem__x = TypeVar("Elem__x")
Elem__o = Optional[Elem__x]
Elem__f = Callable[[...],Elem__o]
Elem__t = Union[Elem__f,Elem__o]
Elem__e = Union[Elem__t,NoReturn]

Struc__x = TypeVar("Struc__x")
Struc__o = Optional[Struc__x]
Struc__f = Callable[[...],Struc__o]
Struc__t = Union[Struc__f,Struc__o]
Struc__e = Union[Struc__t,NoReturn]

Bin__x = Callable[[Elem__t,Elem__t],Elem__e]
Bin__o = Optional[Bin__x]
Bin__f = Callable[[...],Bin__o]
Bin__t = Union[Bin__f,Bin__o]
Bin__e = Union[Bin__t,NoReturn]


####################################
#        Abstract Algebra          #
####################################

class AbsAlgebra(ABC):
    """
    Abstract class for an algebra
    """
    def __init__(self,
            **pars:Pars__t
        ) -> None:
        self._pars = pars

    @abstractmethod
    def __getitem__(self,key): ...

class AbsMultiaryMagma(AbsAlgebra):
    """
    Abstract class for n multiary(n-ary)magma-like algebra,
    i.e. one closed operation with n operands
    """
    def __init__(self,
            nargs:int
            **pars:Pars__t
        ) -> None:
        super().__init__(**pars)
        self._nargs = nargs

    @abstractmethod
    def __operator__(self,
            *elems:Elem__t,
            **pars:Pars__t
        ) -> Elem__t: ...

    @property
    def nargs(self) -> int:
        return self._nargs

    def __call__(self,
            *elems:Elem__t,
            **pars:Pars__t
        ) -> Elem__t:
        _pars = dict(self._pars,**pars)
        return self.__operator__(*elems,**_pars)

    def generate_from_elements(self,
            *elems:Elem__t,
            **pars:Pars__t
        ) -> Tuple[Elem__t]:
        n = self.nargs
        out = tuple()
        new = (*elems,)
        while len(new) > 0:
            out = (*out,*new)
            combinations = itertools.combinations_with_replacement(out,n)
            permutations = map(itertools.permutations,combinations)
            unique_perms = map(list,map(set,permutations))
            perms = functools.reduce(lambda x,y: x+y,unique_perms)
            new = set(c for args in perms\
                    if (c:=self(*args,**pars)) not in out)
        return out


class AbsAlgebraicElement(ABC):
    @abstractmethod
    def __algebra__(self): ...


class AbsAlgebraicStructure(ABC): ...


####################################
#     Abstract Magma Algebra       #
####################################

class AbsMagmaAlgebra(AbsAlgebra):
    """
    Abstract class for a Magma Algebra
    """
    @abstractmethod
    def __operator__(self,
            a:Elem__t,
            b:Elem__t,
            **pars
        ) -> Elem__t: ...

    def __call__(self,
            a:Elem__t,
            b:Elem__t,
            **pars
        ) -> Elem__t:
        return self.__operator__(a,b,**pars)

    def __getitem__(self,
            key:dict
        ) -> Bin__t:
        return lambda a,b: self(a,b,**key)

    def is_a_idempotent(self,
            a:Elem__t,
            **pars
        ) -> bool:
        return a == self(a,a,**pars)

    def is_ab_communative(self,
            a:Elem__t,
            b:Elem__t,
            **pars
        ) -> bool:
        return self(a,b,**pars) == self(b,a,**pars)

    def is_ab_a(self,
            a:Elem__t,
            b:Elem__t,
            **pars
        ) -> bool:
        return a==self(a,b,**pars)

    def is_ab_b(self,
            a:Elem__t,
            b:Elem__t,
            **pars
        ) -> bool:
        return b==self(a,b,**pars)

    def is_abc_associative(self,
            a:Elem__t,
            b:Elem__t,
            c:Elem__t,
            **pars
        ) -> bool:
        ab = self(a,b,**pars)
        bc = self(b,c,**pars)
        return self(ab,c,**pars) == self(a,bc,**pars)

    def reduce(self,
            elems:Iterable[Elem__t],
            **pars
        ) -> Elem__t:
        return functools.reduce(self[pars],elems)

    def generate_from_elements(self,
            *elems:Elem__t,
            **pars
        ) -> Tuple[Elem__t]:
        n = self.nargs
        out = tuple()
        new = (*elems,)
        while len(new) > 0:
            prod = itertools.product(*out*n,*new*(n-1))
            func = lambda *args:itertools.permutations(*args,n)
            out = (*out,*new)
            new = {c for args in map(func,prod)\
                    if (c:=self(*args,**pars)) not in out}
        return out


class AbsUnitalMagmaAlgebra(AbsMagmaAlgebra):
    """
    Abstract Unital Magma Algebra Class
    """
    @abstractmethod
    def __identity__(self,**pars): ...

    def identity(self,**pars):
        return self.__identity__(**pars)


class AbsQuasigroupAlgebra(AbsMagmaAlgebra):
    @abstractmethod
    def __left_division__(self,
            a:Elem__t,
            b:Elem__t,
            **pars
        ) -> Elem__t: ...

    @abstractmethod
    def __right_division__(self,
            a:Elem__t,
            b:Elem__t,
            **pars
        ) -> Elem__t: ...


class AbsLoopAlgebra(AbsUnitalMagmaAlgebra,AbsQuasigroupAlgebra):
    @abstractmethod
    def __inverse__(self,
            a:Elem__t,
            **pars
        ) -> Elem__t: ...

    def inverse(self,
            a:Elem__t,
            **pars
        ) -> Elem__t:
        return self.__inverse__(a,**pars)


####################################
#     Abstract Magma Element       #
####################################

class AbsMagmaElement(AbsAlgebraicElement):
    """
    Abstract class for a Magma Element
    """
    @property
    @abstractmethod
    def __algebra__(self): ...

    @property
    def pars(self):
        return self.__algebra__._pars

    @property
    def __inverse__(self):
        return self.__algebra__.inverse(self,**self.pars)
    
    def __mul__(self,othr):
        return self.__algebra__(self,othr,**self.pars)

    def __truediv__(self,othr):
        return self.__algebra__.__right_division__(self,othr,**self.pars)

    def __floordiv__(self,othr):
        return self.__algebra__.__left_division__(self,othr,**self.pars)

    def __pow__(self,n:int):
        func = self.__algebra__.reduce
        if n < 0:
            return func([self.inverse]*abs(n),**self.pars)
        return func([self]*n,**self.pars)


####################################
#          Abstract Magma          #
####################################

class AbsMagma(AbsAlgebraicStructure):
    """
    Abstract class for a Magma
    """
    @property
    @abstractmethod
    def __algebra__(self): ...

    @property
    @abstractmethod
    def __elements__(self): ...
