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

class AbsAlgebra(ABC):
    @abstractmethod
    def __addition__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __subtraction__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __multiplication__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __left_division__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __right_division__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __power__(self,a:Elem_t,n:int) -> Elem_t: ...

    def __symb_to_operator__(self,op:str="*") -> Oper_t:
        if op == "+":   return self.__addition__
        if op == "-":   return self.__subtraction__
        if op == "*":   return self.__multiplication__
        if op == "/":   return self.__left_division__
        if op == "//":  return self.__right_division__
        if op == "**":  return self.__power__

Alg_t   = TypeVar("Alg_t",bound=AbsAlgebra)

class AbsMagmaAlgebra(AbsAlgebra):
    @property
    @abstractmethod
    def __operator__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    def __addition__(self,*args) -> NoReturn:
        raise NotImplementedError
    def __subtraction__(self,*args) -> NoReturn:
        raise NotImplementedError
    def __multiplication__(self,a:Elem_t,b:Elem_t) -> Elem_t:
        return self.__operator__(a,b)
    def __power__(self,a:Elem_t,n:int):
        return reduce(self.__multiplication__,[a]*n)

class AbsUnitalMagmaAlgebra(AbsMagmaAlgebra):
    @property
    @abstractmethod
    def __identity__(self): ...

class AbsQuasigroupAlgebra(AbsMagmaAlgebra): ...
class AbsLoopAlgebra(AbsUnitalMagmaAlgebra,AbsQuasigroupAlgebra): ...
class AbsGroupAlgebra(AbsLoopAlgebra):
    """
    Abstract class which defines a group's algebra by its
    binary operator and related functions.
    """
    @abstractmethod
    def __operator__(self,a:Elem_t,b:Elem_t,**pars:Pars_t) -> Elem_t: ...

    def __generate_set_from_elements__(self,*elems:Elem_t,**pars:Pars_t) -> Tuple[Elem_t]:
        out: Tuple[Elem_t] = tuple()
        new: Tuple[Elem_t] = elems
        while len(new) > 0:
            out = (*out,*new) # union of <out> and <new>
            new = set(c for a,b in product(out,elems)\
                  if (c:=self.__operator__(a,b,**pars)) not in out) 
        return o
    def __call__(self,a,b,**pars:Pars_t) -> Elem_t:
        return self.__operator__(a,b,**pars)

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

class AbsGroupElement(ABC):
    @property
    @abstractmethod
    def __group__(self) -> Struc_t: ...

Elem_t  = TypeVar("Elem_t",bound=Union[AbsGroupElement,Any])
