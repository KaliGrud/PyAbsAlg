import numpy as np
from typing import  TypeVar,NewType,Union,Optional,Literal,\
                    Container,Hashable,Sized,Callable,\
                    Iterable,Iterator,Generator,Mapping,\
                    Sequence,Tuple,MutableSequence,List,\
                    NoReturn,Any
from abc    import  ABC,abstractmethod

############
# Abstract Algebra Class
############

Elem_t  = TypeVar("Elem_t")                 # Algebraic element
Pars_t  = TypeVar("Pars_t")                 # Function parameters
Set_t   = Iterable[Elem_t]                  # Algebraic set
Oper_t  = Callable[[Elem_t,Elem_t],Elem_t]  # Binary operator

Elem_opt  = Optional[Elem_t]  # Algebraic element as optional
Pars_opt  = Optional[Pars_t]  # Function parameters as optional
Set_opt   = Optional[Set_t]   # Algebraic set as optional 
Oper_opt  = Optional[Oper_t]  # Binary operator as optional

Elem_err  = Union[Elem_opt]  # Algebraic element as optional
Pars_err  = Union[Pars_opt]  # Function parameters as optional
Set_err   = Union[Set_opt]   # Algebraic set as optional 
Oper_err  = Union[Oper_opt]  # Binary operator as optional

class AbsAlgebra(ABC):
    @abstractmethod
    def __init__(self,*args,**kwargs) -> None:
        self._operators = { "+",self.__addition__,
                            "*",self.__multiplication__,
                            "@",self.__matrix_mul__,
                            "-",self.__substraction__,
                            "/",self.__right_divide__,
                            "//",self.__left_divide__,
                            "**",self.__power__, }
    def __addition__(self,a:Elem_t,b:Elem_t) -> Oper_t:
        raise NotImplementedError
    def __multiplication__(self,a:Elem_t,b:Elem_t) -> Oper_t:
        raise NotImplementedError
    def __matrix_mul__(self,a:Elem_t,b:Elem_t) -> Oper_t:
        raise NotImplementedError
    def __subtraction__(self,a:Elem_t,b:Elem_t) -> Oper_t:
        raise NotImplementedError
    def __left_division__(self,a:Elem_t,b:Elem_t) -> Oper_t:
        raise NotImplementedError
    def __right_division__(self,a:Elem_t,b:Elem_t) -> Oper_t:
        raise NotImplementedError
    def __power__(self,a:Elem_t,n:int) -> Oper_t:
        raise NotImplementedError
    def __getitem__(self,key:str) -> Oper_t:
        return self._operators[key]
    def __setitem__(self,key:str,value:Oper_t) -> Oper_t:
        self._operators[key] = value
        return value
    def get(self,key:str,default:Oper_opt=None) -> Oper_opt:
        return self._operators.get(key,default)

Alg_t = TypeVar("Alg_t",bound=AbsAlgebra)

############
# Abstract Algebra Structure
############


class AbsAlgStructure(ABC):
    @property
    @abstractmethod
    def __algebra__(self) -> Alg_t: ...
    @property
    @abstractmethod
    def __elements__(self) -> Set_t: ...

Struc_t = TypeVar("Struc_t",bound=AbsAlgStructure)

############
# Cardinality
############

class AlephNumber:
    """
    Class for Aleph Numbers, i.e. the cardinalties of some infinite sets
    e.g.
    >>> Aleph0 = Integers.cardinality
    >>> Aleph1 = Reals.cardinatity
    """
    def __init__(self,alpha:int) -> None:
        self.alpha = alpha
    def __len__(self) -> Literal[np.inf]:
        return np.inf
    def __eq__(self,othr) -> Optional[bool]:
        try:                                                          
            return self.alpha == othr.alpha
        except AttributeError:
            return None if othr == np.inf else False
    def __ne__(self,othr) -> Optional[bool]:
        try:
            return self.alpha != othr.alpha
        except AttributeError:
            return None if othr != np.inf else True
    def __lt__(self,othr) -> Optional[bool]:
        try:
            return self.alpha < othr.alpha
        except AttributeError:
            return None if othr < np.inf else False
    def __le__(self,othr) -> Optional[bool]:
        try:
            return self.alpha <= othr.alpha
        except AttributeError:
            return False if othr > np.inf else None
    def __gt__(self,othr) -> Optional[bool]:
        try:
            return self.alpha > othr.alpha
        except AttributeError:
            return True if othr <= np.inf else None
    def __ge__(self,othr) -> Optional[bool]:
        try:
            return self.alpha >= othr.alpha
        except AttributeError:
            return True if othr < np.inf else None 
    def __rpow__(self,othr):
        if othr != 2 or self.alpha != 0:
            raise ValueError
        else:
            return AlephNumber(1)

Card_t = Union[int,float,AlephNumber]

Aleph0 = AlephNumber(0)
Aleph1 = AlephNumber(1) 

############
# Abs Algebraic Sets
############

class AbsAlgSet(ABC):
    @property
    @abstractmethod
    def __cardinality__(self) -> Card_t: ...
    @abstractmethod
    def __contains__(self,obj) -> bool: ...
    @abstractmethod
    def __iter__(self) -> Iterable: ...
    @abstractmethod
    def __next__(self) -> Elem_t: ...

AlgSet_t = TypeVar("AlgSet_t",bound=AbsAlgSet)
Set_t  = Union[Set_t,AlgSet_t]

############
# Abstract Algebra Element
############

class AbsAlgElement(ABC):
    @property
    @abstractmethod
    def __structure__(self) -> Struc_t: ...
    @property
    def __algebra__(self) -> Alg_t:
        return self.__structure__.__algebra__
    def __add__(self,othr) -> Elem_t:
        return self.__algebra__["+"](self,othr)
    def __mul__(self,othr) -> Elem_t:
        return self.__algebra__["*"](self,othr)
    def __matmul__(self,othr) -> Elem_t:
        return self.__algebra__["@"](self,othr)
    def __sub__(self,othr) -> Elem_t:
        return self.__algebra__["-"](self,othr)
    def __truediv__(self,othr) -> Elem_t:
        return self.__algebra__["/"](self,othr)
    def __floordiv__(self,othr) -> Elem_t:
        return self.__algebra__["//"](self,othr)
    def __pow__(self,othr) -> Elem_t:
        return self.__algebra__["**"](self,othr)

Elem_t  = Union[Elem_t,AbsAlgElement]
