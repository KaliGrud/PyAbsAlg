# import from within package
from . import AbsAlgebra,AbsAlgStructure,AbsAlgElement,AbsAlgSet,\
              Elem__t,Set__t,Oper__t,Alg__t,Struc__t,\
              Elem__o,Set__o,Oper__o,Alg__o,Struc__o,\
              Elem__e,Set__e,Oper__e,Alg__e,Struc__e,\
              Elem__f,Set__f,Oper__f,Alg__f,Struc__f,\
              Elem__u,Set__u,Oper__u,Alg__u,Struc__u\

# import from external packages
from typing     import  TypeVar,NewType,Union,\
                        Container,Hashable,Sized,Callable,\
                        Iterable,Iterator,Generator,Mapping,\
                        Sequence,Tuple,MutableSequence,List,\
                        NoReturn,Any
from abc        import  ABC,abstractmethod
from functools  import  reduce

############
# Abs Magma Algebras
############

class AbsMagmaAlgebra(AbsAlgebra):
    """
    Abstract class which defines a magma's algebra by its
    binary operator and related functions.
    """
    @abstractmethod
    def ___operator__(self,a:Elem__t,b:Elem__t,**pars) -> Elem__t: ...
    @abstractmethod
    def __identity__(self,**pars) -> Elem__e: ...
    @abstractmethod
    def __inverse__(self,a:Elem__t,**pars) -> Elem__e: ...
    def __power__(self,a:Elem__t,n:int,**pars) -> Elem__t:
        if n > 0:
            return reduce(self.___operator__,[a]*n)
        if n == 0:
            return self.__identity__(**pars)
        return self.__power__(self.__inverse__(a,**pars),abs(n))
    def __generate__(self,*elems:Elem__t,**pars) -> Set__t:
        out: Set__t = tuple()
        new: Set__t = elems
        while len(new) > 0:
            out = (*out,*new) # union of <out> and <new>
            new = set(c for a,b in product(out,elems)\
                  if (c:=self.___operator__(a,b,**pars)) not in out) 
        return out

class AbsUnitalMagmaAlgebra(AbsMagmaAlgebra):
    @property
    @abstractmethod
    def __identity__(self) -> Union[Elem__t,Callable[[Elem__t,...],Elem__t]]: ...

class AbsQuasigroupAlgebra(AbsMagmaAlgebra):
    @abstractmethod
    def __left_division__(self,a:Elem__t,b:Elem__t) -> Elem__t: ...
    @abstractmethod
    def __right_division__(self,a:Elem__t,b:Elem__t) -> Elem__t: ...

class AbsLoopAlgebra(AbsUnitalMagmaAlgebra,AbsQuasigroupAlgebra):
    @abstractmethod
    def __inverse__(self,a:Elem__t) -> Elem__t: ...

############
# Abs Magma Structures
############

class AbsMagma(AbsAlgStructure): ... 
class AbsUnitalMagma(AbsMagma): ...
class AbsQuasigroup(AbsMagma): ...
class AbsLoop(AbsUnitalMagma,AbsQuasigroup): ...

############
# Abs Magma Elements
############

class AbsMagmaElement(AbsAlgElement): ...
class AbsUnitalMagmaElement(AbsMagmaElement): ...
class AbsQuasigroupElement(AbsMagmaElement): ...
class AbsLoopElement(AbsUnitalMagmaElement,AbsQuasigroupElement): ...
