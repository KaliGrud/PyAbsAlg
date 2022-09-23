from Base   import  *
from abc    import  ABC,abstractmethod
from typing import  TypeVar,NewType,Union,\
                    Iterable,Iterator,Generator,Tuple,List,Dict,\
                    Callable,Any

class AbsAlgebraicSet(ABC):
    @abstractmethod(ABC):
    def __elements__(self,*pars:Pars_t) -> Iterator: ...

class AbsFiniteAlgebraic 
