from typing     import  TypeVar,NewType,Union,\
                        Container,Hashable,Sized,Callable,\
                        Iterable,Iterator,Generator,Mapping,\
                        Sequence,Tuple,MutableSequence,Any

Elem_t = TypeVar("Elem_t")
Alg_t  = TypeVar("Alg_t",bound=Sequence)

Oper_t = Callable[[Elem_t,Elem_t],Elem_t]

class AlephNumber:
    def __init__(self,N):
        self.N = N
    def __eq__(self,othr) -> bool:
        try:
            return self.N == othr.N 
        except AttributeError:
            return False 
    def __ne__(self,othr) -> bool:
        try:
            return self.N != othr.N
        except AttributeError:
            return True
    def __le__(self,othr) -> bool:
        try:
            return self.N <= othr.N
        except AttributeError:
            return False
    def __lt__(self,othr) -> bool:
        try:
            return self.N < othr.N
        except AttributeError:
            return False
    def __ge__(self,othr) -> bool:
        try:
            return self.N >= othr.N
        except AttributeError:
            return True
    def __gt__(self,othr) -> bool:
        try:
            return self.N > othr.N
        except AttributeError:
            return True
 
ALEPH0 = AlephNumber(0)
ALEPH1 = AlephNumber(1)
