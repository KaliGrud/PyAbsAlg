from abc        import  ABC,abstractmethod
from typing     import  TypeVar,NewType,Union,\
                        Container,Hashable,Sized,Callable,\
                        Iterable,Iterator,Generator,Mapping,\
                        Sequence,Tuple,MutableSequence,Any
from itertools  import  product

class AbsAlgebra(ABC):
    @abstractmethod
    def __identity__(self) -> Elem_t: ...
    @abstractmethod
    def __inverse__(self,a:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __add_operator__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __sub_operator__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __mul_operator__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __right_div_operator__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    @abstractmethod
    def __left_div_operator__(self,a:Elem_t,b:Elem_t) -> Elem_t: ...
    def __getitem__(self,key) -> Oper_t:
        if   key == "+":  return self.__add_operator__
        elif key == "-":  return self.__sub_operator__
        elif key == "*":  return self.__mul_operator__
        elif key == "/":  return self.__right_div_operator__
        elif key == "//": return self.__left_div_operator__
        raise KeyError
    def __generate_from_element__(self,*elems:Elem_t,op:str="+") -> Tuple[Elem_t]:
        bin_op: Oper_t = self[op]
        out: Tuple[Elem_t] = tuple()
        while len(elems) > 0:
            out = (*out,*elems) # union of <out> and <elems>
            elems = set(c for a,b in product(out,elems)\
                    if (c:=bin_op(a,b)) not in out) # new unique algebraic elements 
        return out

class AbsAlgElement(ABC):
    @property
    @abstractmethod
    def __algebra__(self) -> Alg_t: ...
    def __add__(self,othr) -> Elem_t:
        return self.__algebra__["+"](self,othr)
    def __sub__(self,othr) -> Elem_t:
        return self.__algebra__["-"](self,othr)
    def __mul__(self,othr) -> Elem_t:
        return self.__algebra__["*"](self,othr)
    def __truediv__(self,othr) -> Elem_t:
        return self.__algebra__["/"](self,othr)
    def __floordiv__(self,othr) -> Elem_t:
        return self.__algebra__["//"](self,othr)

class AbsDiscreteAlgElement(AbsAlgElement):
    @abstractmethod
    def __getitem__(self,key) -> Elem_t: ...
    @abstractmethod
    def __len__(self): ...

class AbsParameterizedAlgElement(AbsAlgElement):
    @property
    @abstractmethod
    def __parameters__(self): ...

class AbsAlgContainer(ABC):
    @property
    @abstractmethod
    def __algebra__(self) -> Alg_t: ...
    @abstractmethod
    def __contains__(self,el:Elem_t) -> bool: ...

class AbsDiscreteAlgContainer(AbsAlgContainer):
    @abstractmethod
    def __getitem__(self,key) -> Elem_t: ...

class AbsIndexedAlgContainer(AbsDiscreteAlgContainer):
    @abstractmethod
    def __getitem__(self,idx:int) -> Elem_t: ...

class AbsCallableAlgContainer(AbsAlgContainer):
    @abstractmethod
    def __call__(self,*args,**kwargs) -> Elem_t: ...

class AbsContinuousAlgContainer(AbsCallableAlgContainer):
    @abstractmethod
    def __call__(self,*args,**kwargs) -> Elem_t: ...
    
class AbsAlgOrderedAlgContainer(AbsAlgContainer):
    @abstractmethod
    def __less_than__(self,a:Elem_t,b:Elem_t) -> bool: ...
    @abstractmethod
    def __less_than_or_equal__(self,a:Elem_t,b:Elem_t) -> bool: ...
    @abstractmethod
    def __greater_than__(self,a:Elem_t,b:Elem_t) -> bool: ...
    @abstractmethod
    def __greater_than_or_equal__(self,a:Elem_t,b:Elem_t) -> bool: ...
    @abstractmethod
    def __equal__(self,a:Elem_t,b:Elem_t) -> bool: ...
    @abstractmethod
    def __not_equal__(self,a:Elem_t,b:Elem_t) -> bool: ...
