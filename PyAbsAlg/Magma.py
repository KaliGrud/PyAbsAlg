# import from within package
from . import AbsAlgebra,AbsAlgStructure,AbsAlgElement,AbsAlgSet,\
              Elem_t,Set_t,Pars_t,Oper_t,Alg_t,Struc_t

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
    def __operator__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @property
    def __identity__(self) -> Elem_t:
        return NotImplementedError
    def __inverse__(self,a:Elem_t) -> Elem_t:
        return NotImplementedError
    def __power__(self,a:Elem_t,n:int) -> Elem_t:
        if n > 0:
            return reduce(self.__operator__,[a]*n)
        if n == 0:
            return self.__identity__
        return self.__power__(self.__inverse__(a),abs(n))
    def __generate__(self,*elems:Elem_t,**pars:Pars_t) -> Set_t:
        out: Set_t = tuple()
        new: Set_t = elems
        while len(new) > 0:
            out = (*out,*new) # union of <out> and <new>
            new = set(c for a,b in product(out,elems)\
                  if (c:=self.__call__(a,b,**pars)) not in out) 
        return out

class AbsUnitalMagmaAlgebra(AbsMagmaAlgebra):
    @property
    @abstractmethod
    def __identity__(self) -> Union[Elem_t,Callable[[Elem_t,...],Elem_t]]: ...

class AbsQuasigroupAlgebra(AbsMagmaAlgebra):
    @abstractmethod
    def __left_division__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __right_division__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...

class AbsLoopAlgebra(AbsUnitalMagmaAlgebra,AbsQuasigroupAlgebra):
    @abstractmethod
    def __inverse__(self,a:Elem_t) -> Elem_t: ...

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
