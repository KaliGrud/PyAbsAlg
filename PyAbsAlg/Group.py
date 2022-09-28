from typing     import  TypeVar,NewType,Union,\
                        Container,Hashable,Sized,Callable,\
                        Iterable,Iterator,Generator,Mapping,\
                        Sequence,Tuple,MutableSequence,List,\
                        NoReturn,Any
from abc        import  ABC,abstractmethod
from functools  import  reduce

Pars_t  = TypeVar("Pars_t")
Elem_t  = TypeVar("Elem_t")

Oper_t  = Callable[[Elem_t,Elem_t],Elem_t]

############
# Algebras as defined by their operators
############

class AbsAlgebra(ABC): ...
Alg_t = TypeVar("Alg_t",bound=AbsAlgebra)

class AbsMagmaAlgebra(AbsAlgebra):
    """
    Abstract class which defines a magma's algebra by its
    binary operator and related functions.
    """
    @abstractmethod
    def __operator__(self,a:Elem_t,b:Elem_t,**pars:Pars_t) -> Elem_t: ...

    def __power__(self,a:Elem_t,n:int):
        return reduce(self.__operator__,[a]*n)

    def __generate_set_from_elements__(self,*elems:Elem_t,**pars:Pars_t) -> Tuple[Elem_t]:
        out: Tuple[Elem_t] = tuple()
        new: Tuple[Elem_t] = elems
        while len(new) > 0:
            out = (*out,*new) # union of <out> and <new>
            new = set(c for a,b in product(out,elems)\
                  if (c:=self.__operator__(a,b,**pars)) not in out) 
        return out

    def __call__(self,a:Elem_t,b:Elem_t,**pars:Pars_t) -> Elem_t:
        return self.__operator__(a,b,**pars)

class AbsUnitalMagmaAlgebra(AbsMagmaAlgebra):
    @property
    @abstractmethod
    def __identity__(self): ...

class AbsQuasigroupAlgebra(AbsMagmaAlgebra):
    @abstractmethod
    def __left_divide__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __right_divide__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...

class AbsLoopAlgebra(AbsUnitalMagmaAlgebra,AbsQuasigroupAlgebra):
    @abstractmethod
    def __inverse__(self,a:Elem_t) -> Elem_t: ...

class AbsGroupAlgebra(AbsLoopAlgebra): ...

############
# Algebraic Structures
############

class AbsAlgebraicStructure(ABC):
    @property
    @abstractmethod
    def __algebra__(self) -> Alg_t: ...

    @property
    @abstractmethod
    def __elements__(self) -> Iterable: ...

    def __call__(self,a:Elem_t,b:Elem_t,op="*",**pars:Pars_t) -> Elem_t:
        binop = self.__algebra__.__symb_to_operator__(op)
        return binop(a,b,**pars)

Struc_t = TypeVar("Struc_t",bound=AbsAlgebraicStructure)

class AbsMagma(AbsAlgebraicStructure): ...
class AbsUnitalMagma(AbsMagma): ...
class AbsQuasigroup(AbsMagma): ...
class AbsLoop(AbsUnitalMagma,AbsQuasigroup): ...
class AbsGroup(AbsLoop): ...

############
# Algebraic Elements
############

class AbsMagmaElement(AbsAlgebraicElement): ...
class AbsUnitalMagmaElement(AbsMagmaElement): ...
class AbsQuasigroupElement(AbsMagmaElement): ...
class AbsLoopElement(AbsUnitalMagmaElement,AbsQuasigroupElement): ...

class AbsGroupElement(ABC):
    @property
    @abstractmethod
    def __group__(self) -> Struc_t: ...

Elem_t  = TypeVar("Elem_t",bound=Union[AbsGroupElement,Any])
