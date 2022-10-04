from sys        import  maxsize
from typing     import  TypeVar,NewType,Union,Optional,Literal,\
                        Container,Hashable,Sized,Callable,\
                        Iterable,Iterator,Generator,Mapping,\
                        Sequence,Tuple,MutableSequence,List,\
                        NoReturn,Any
from abc        import  ABC,abstractmethod
from functools  import  product

############
# Constants
############

MAX_INT = maxsize
MIN_INT = -maxsize-1

############
# Type Hinting Aliases
############

# Postfix key:
#     t : <type>
#     o : Optional[<type>] = Union[<type>,None]
#     n : Union[<type>,None,NoReturn]
#     f : Callable[[<type>,...],<type>]
#     u : Union[Callable[[<type>,...],<type>],<type>,None,NoReturn]

Pars__t  = TypeVar("Pars__t") # keyword parameter(s)
Pars__o  = Optional[Pars__t] 
Pars__e  = Union[Pars__o,NoReturn]
Pars__f  = Callable[[Pars__e,...],Pars__e]
Pars__u  = Union[Pars__f,Pars__e]

Elem__t  = TypeVar("Elem__t") # Algebraic element
Elem__o  = Optional[Elem__t] 
Elem__e  = Union[Elem__o,NoReturn]
Elem__f  = Callable[[Elem__e,...],Elem__e]
Elem__u  = Union[Elem__f,Elem__e]

Set__t   = Iterable[Elem__t] # Algebraic set
Set__o   = Optional[Set__t]
Set__e   = Union[Set__o,NoReturn]  
Set__f   = Callable[[Set__e,...],Set__e]  
Set__u   = Union[Set__f,Set__e]  

Oper__t  = Callable[[Elem__t,Elem__t],Elem__t] # Binary operator
Oper__o  = Optional[Oper__t]
Oper__e  = Union[Oper__t,NoReturn] 
Oper__f  = Callable[[Oper__e,...],Oper__e] 
Oper__u  = Union[Oper__f,Oper__e] 

############
# Abstract Algebra Class
############

class AbsAlgebra(ABC):
    def __init__(self,*args,**kwargs) -> None:
        self._operators = { "+",self.__addition__,
                            "*",self.__multiplication__,
                            "@",self.__matrix_mul__,
                            "-",self.__substraction__,
                            "/",self.__right_divide__,
                            "//",self.__left_divide__,
                            "**",self.__power__, }
    
    @abstractmethod
    def __addition__(self,a:Elem__u,b:Elem__u,**kw) -> Oper__u: ...
    
    @abstractmethod
    def __multiplication__(self,a:Elem__u,b:Elem__u,**kw) -> Oper__u: ...
    
    @abstractmethod
    def __matrix_mul__(self,a:Elem__u,b:Elem__u,**kw) -> Oper__u: ...
    
    @abstractmethod
    def __subtraction__(self,a:Elem__u,b:Elem__u,**kw) -> Oper__u: ...
    
    @abstractmethod
    def __left_division__(self,a:Elem__u,b:Elem__u,**kw) -> Oper__u: ...
    
    @abstractmethod 
    def __right_division__(self,a:Elem__u,b:Elem__u,**kw) -> Oper__u: ...
    
    def __power__(self,a:Elem__u,n:int) -> Elem__u:
        if n >= 0:
            return map(self.__multiplication__,[a]*n)
        return self.__power__(self.__right_division__(1,a),abs(n))
    
    def __getitem__(self,key:str) -> Oper__e:
        return self._operators[key]
    
    def __setitem__(self,key:str,value:Oper__e) -> Oper__e:
        self._operators[key] = value
        return value
    
    def get(self,key:str,default:Oper__o=None) -> Oper__o:
        return self._operators.get(key,default)


Alg__t = TypeVar("Alg__t",bound=AbsAlgebra)
Alg__o = Optional[Alg__t]
Alg__e = Union[Alg__o,NoReturn]
Alg__f = Callable[[Alg__e,...],Alg__e]
Alg__u = Union[Alg__f,Alg__e]

############
# Abstract Algebra Structure
############

class AbsAlgStructure(ABC):
    @property
    @abstractmethod
    def __algebra__(self) -> Alg__t: ...

    @property
    @abstractmethod
    def __elements__(self) -> Set__t: ...


Struc__t = TypeVar("Struc__t",bound=AbsAlgStructure)
Struc__o = Optional[Struc__t]
Struc__e = Union[Struc__o,NoReturn]
Struc__f = Callable[[Struc__e,...],Struc__e]
Struc__u = Union[Struc__f,Struc__e]

############
# Cardinality
############

class AlephNumber:
    """
    Class for Aleph Numbers
    i.e. the cardinalties of some infinite sets
    """
    def __init__(self,alpha:int) -> None:
        self.alpha = alpha

    def __len__(self) -> Literal[MAX_INT]:
        return MAX_INT

    def __eq__(self,othr) -> Optional[bool]:
        try:                                                          
            return self.alpha == othr.alpha
        except AttributeError:
            return None if othr == MAX_INT else False

    def __ne__(self,othr) -> Optional[bool]:
        try:
            return self.alpha != othr.alpha
        except AttributeError:
            return None if othr == MAX_INT else True

    def __lt__(self,othr) -> Optional[bool]:
        try:
            return self.alpha < othr.alpha
        except AttributeError:
            return None if othr == MAX_INT else False

    def __le__(self,othr) -> Optional[bool]:
        try:
            return self.alpha <= othr.alpha
        except AttributeError:
            return None if othr == MAX_INT else False

    def __gt__(self,othr) -> Optional[bool]:
        try:
            return self.alpha > othr.alpha
        except AttributeError:
            return None if othr == MAX_INT else True

    def __ge__(self,othr) -> Optional[bool]:
        try:
            return self.alpha >= othr.alpha
        except AttributeError:
            return None if othr == MAX_INT else True


Card__t = Union[int,float,AlephNumber]
Card__o = Optional[Card__t]
Card__e = Union[Card__o,NoReturn]
Card__f = Callable[[Card__e,...],Card__e]
Card__u = Union[Card__f,Card__e]

Aleph0 = AlephNumber(0)
Aleph1 = AlephNumber(1) 

############
# Abs Algebraic Sets
############

class AbsAlgSet(ABC):
    @property
    def cardinality(self) -> Card__t:
        return self.__cardinality__()

    @abstractmethod
    def __cardinality__(self) -> Card__t: ...

    @abstractmethod
    def __contains__(self,elem:Elem__t,**kw) -> bool: ...

    @abstractmethod
    def __iter__(self): ...

    @abstractmethod
    def __next__(self) -> Elem__t: ...

    def __len__(self) -> Card__t:
        return self.__cardinality__


Set__t = Union[Set__t,TypeVar("Set__t",bound=AbsAlgSet)]
Set__o = Optional[Set__t]
Set__e = Union[Set__o,NoReturn]
Set__f = Callable[[Set__e,...],Set__e]
Set__u = Union[Set__f,Set__e]


class AbsDiscreteAlgSet(AbsAlgSet):
    @property
    @abstractmethod
    def __cardinality__(self) -> Card__u: ...

# Common algebraic sets

class NATURALS(AbsAlgSet):
    @property
    def __cardinality__(self) -> Literal[Aleph0]:
        return Aleph0

    def __contains__(self,elem:Elem__t) -> bool:
        return elem == int(elem) 

    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        self.n += 1
        if self.n < MAX_INT:
            return self.n
        else:
            raise StopIteration

############
# Abstract Algebra Element
############

class AbsAlgElement(ABC):
    @property
    @abstractmethod
    def __structure__(self) -> Struc__t: ...

    @property
    def __algebra__(self) -> Alg__t:
        return self.__structure__.__algebra__

    def __add__(self,othr) -> Elem__t:
        return self.__algebra__["+"](self,othr)

    def __mul__(self,othr) -> Elem__t:
        return self.__algebra__["*"](self,othr)

    def __matmul__(self,othr) -> Elem__t:
        return self.__algebra__["@"](self,othr)

    def __sub__(self,othr) -> Elem__t:
        return self.__algebra__["-"](self,othr)

    def __truediv__(self,othr) -> Elem__t:
        return self.__algebra__["/"](self,othr)

    def __floordiv__(self,othr) -> Elem__t:
        return self.__algebra__["//"](self,othr)

    def __pow__(self,othr) -> Elem__t:
        return self.__algebra__["**"](self,othr)

Elem__t = Union[Elem__t,TypeVar("Elem__t",bound=AbsAlgElement)]
